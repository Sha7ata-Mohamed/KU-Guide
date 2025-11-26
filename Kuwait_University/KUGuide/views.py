# KUGuide/views.py
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .models import Profile, ContactMessage  # only models you actually use here
from .forms import ProfileForm, SignInForm  # <-- import forms from .forms


def _infer_university_id(user):
    """Try to determine a stable identifier for a user."""

    if user.username:
        return user.username

    email_local_part = (user.email or "").split("@")[0]
    if email_local_part:
        return email_local_part

    return f"user-{user.pk or 'unknown'}"


def _get_or_create_profile(user):
    """Return a profile for ``user`` ensuring ``university_id`` is present."""

    profile, _ = Profile.objects.get_or_create(
        user=user,
        defaults={
            "university_id": _infer_university_id(user),
            "major": "",
            "bio": "",
        },
    )

    if not profile.university_id:
        profile.university_id = _infer_university_id(user)
        profile.save(update_fields=["university_id"])

    return profile


def index_view(request):
    return render(request, "index.html")


def faq_view(request):
    return render(request, "faq.html")


def career_view(request):
    return render(request, "career.html")


def profile_view(request):
    profile = None
    stats = {
        "questions": 0,
        "groups": 0,
        "courses": 0,
        "materials": 0,
    }
    if request.user.is_authenticated:
        profile = _get_or_create_profile(request.user)
    return render(request, "profile.html", {"profile": profile, "stats": stats})


@login_required
def profile_edit_view(request):
    profile = _get_or_create_profile(request.user)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated.")
            return redirect("profile")  # or "KUGuide:profile" if namespaced
    else:
        form = ProfileForm(instance=profile)
    return render(request, "profile_edit.html", {"form": form})


def profile_settings_view(request):
    return render(request, "profile_settings.html")


def my_groups_view(request):
    return render(request, "groups.html")


def my_courses_view(request):
    return render(request, "courses.html")


def activity_view(request):
    return render(request, "activity.html")


def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        message = request.POST.get("message", "").strip()

        if name and email and message:
            try:
                ContactMessage.objects.create(
                    user=request.user if request.user.is_authenticated else None,
                    name=name,
                    email=email,
                    message=message,
                )
                messages.success(request, "Thanks! Your message has been sent.")
                return redirect("contact")
            except Exception:
                messages.error(
                    request, "Could not save your message. Please try again later."
                )
        else:
            messages.error(request, "Please fill out all fields.")

    return render(request, "contact.html")


def signin_view(request):
    """
    Sign-in using KU email (validated in form) + password.
    We map email -> username then authenticate.
    """
    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"].lower()
            password = form.cleaned_data["password"]

            try:
                # Find user by email
                user = User.objects.filter(email__iexact=email).first()
                if not user:
                    messages.error(request, "No account found with this email address.")
                    return render(request, "signin.html", {"form": form})

                # Authenticate user
                auth_user = authenticate(
                    request, username=user.username, password=password
                )
                if auth_user:
                    if form.cleaned_data.get("remember_me"):
                        request.session.set_expiry(1209600)  # 2 weeks
                    else:
                        request.session.set_expiry(0)  # Until browser closes
                    login(request, auth_user)
                    messages.success(request, "Welcome back!")
                    next_url = request.GET.get("next", "index")
                    return redirect(next_url)
                else:
                    messages.error(request, "Invalid password.")
            except Exception:
                messages.error(
                    request, "An error occurred during sign in. Please try again."
                )
    else:
        form = SignInForm()

    return render(request, "signin.html", {"form": form})
