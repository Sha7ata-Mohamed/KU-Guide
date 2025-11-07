from django.contrib import admin
from .admin_dashboard import KUGuideAdminSite
from .models import (
    Profile,
    FAQCategory,
    FAQ,
    Major,
    Certification,
    ChatbotQuery,
    ContactMessage
)

admin_site = KUGuideAdminSite(name="KUGuideAdmin")

# Register models with the custom admin site
admin_site.register(Profile)
admin_site.register(FAQCategory)
admin_site.register(FAQ)
admin_site.register(Major)
admin_site.register(Certification)
admin_site.register(ChatbotQuery)
admin_site.register(ContactMessage)

# ==============================
#  Profile Admin
# ==============================
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "university_id", "major", "last_login")
    search_fields = ("user__username", "university_id", "major")
    list_filter = ("major",)
    ordering = ("user__username",)


# ==============================
#  FAQ Admin
# ==============================
class FAQInline(admin.TabularInline):
    model = FAQ
    extra = 1


@admin.register(FAQCategory)
class FAQCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    inlines = [FAQInline]
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question", "category", "created_at")
    list_filter = ("category",)
    search_fields = ("question", "answer", "category__name")
    date_hierarchy = "created_at"


# ==============================
#  Major & Certification Admin
# ==============================
class CertificationInline(admin.TabularInline):
    model = Certification
    extra = 1


@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)
    inlines = [CertificationInline]
    ordering = ("name",)


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ("name", "major", "provider")
    list_filter = ("major", "provider")
    search_fields = ("name", "major__name", "provider")
    ordering = ("major__name", "name")


# ==============================
#  Chatbot Query Admin
# ==============================
@admin.register(ChatbotQuery)
class ChatbotQueryAdmin(admin.ModelAdmin):
    list_display = ("user", "question", "timestamp")
    search_fields = ("user__username", "question", "response")
    date_hierarchy = "timestamp"
    ordering = ("-timestamp",)


# ==============================
#  Contact Message Admin
# ==============================
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    search_fields = ("name", "email", "message")
    date_hierarchy = "created_at"
    ordering = ("-created_at",)


