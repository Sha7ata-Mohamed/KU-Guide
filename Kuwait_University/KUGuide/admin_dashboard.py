# KUGuide/admin_dashboard.py
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile, FAQ, FAQCategory, Major, Certification, ChatbotQuery, ContactMessage


class KUGuideAdminSite(admin.AdminSite):
    site_header = "Kuwait University Guide Admin"
    site_title = "KUGuide Admin Portal"
    index_title = "Welcome to KUGuide Dashboard"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path("dashboard/", self.admin_view(self.dashboard_view), name="dashboard"),
        ]
        return custom_urls + urls

    def dashboard_view(self, request):
        stats = {
            "total_users": User.objects.count(),
            "total_profiles": Profile.objects.count(),
            "total_faqs": FAQ.objects.count(),
            "faq_categories": FAQCategory.objects.count(),
            "majors": Major.objects.count(),
            "certifications": Certification.objects.count(),
            "chatbot_queries": ChatbotQuery.objects.count(),
            "contact_messages": ContactMessage.objects.count(),
        }
        return render(request, "admin/dashboard.html", {"stats": stats})
