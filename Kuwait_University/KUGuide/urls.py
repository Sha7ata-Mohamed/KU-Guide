# KUGuide/urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("", views.index_view, name="index"),
    path("faq/", views.faq_view, name="faq"),
    path("career/", views.career_view, name="career"),

    path("profile/", views.profile_view, name="profile"),
    path("profile/edit/", views.profile_edit_view, name="profile_edit"),
    path("profile/settings/", views.profile_settings_view, name="profile_settings"),
    path("groups/", views.my_groups_view, name="my_groups"),
    path("courses/", views.my_courses_view, name="my_courses"),
    path("activity/", views.activity_view, name="activity"),

    path("contact/", views.contact_view, name="contact"),
    path("signin/", views.signin_view, name="signin"),
    
    # Password Reset URLs
    path("password_reset/", auth_views.PasswordResetView.as_view(
        template_name="registration/password_reset_form.html",
        email_template_name="registration/password_reset_email.html",
        success_url="/password_reset/done/",
    ), name="password_reset"),
    
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(
        template_name="registration/password_reset_done.html"
    ), name="password_reset_done"),
    
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
        template_name="registration/password_reset_confirm.html",
        success_url="/reset/done/"
    ), name="password_reset_confirm"),
    
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(
        template_name="registration/password_reset_complete.html"
    ), name="password_reset_complete"),
]
