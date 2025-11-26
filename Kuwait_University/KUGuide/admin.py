from django.contrib import admin
from .admin_dashboard import KUGuideAdminSite
from .models import (
    Profile,
    FAQCategory,
    FAQ,
    Major,
    Certification,
    ChatbotQuery,
    ContactMessage,
)

# Use the custom admin site everywhere
admin_site = KUGuideAdminSite(name="KUGuideAdmin")


# ==============================
#  Profile Admin
# ==============================
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "university_id", "major", "user_last_login")
    search_fields = ("user__username", "university_id", "major")
    list_filter = ("major",)
    ordering = ("user__username",)

    def user_last_login(self, obj):
        return obj.user.last_login

    user_last_login.short_description = "Last login"
    user_last_login.admin_order_field = "user__last_login"


# ==============================
#  FAQ Admin
# ==============================
class FAQInline(admin.TabularInline):
    model = FAQ
    extra = 1


class FAQCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    inlines = [FAQInline]
    search_fields = ("name",)
    ordering = ("name",)


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


class MajorAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)
    inlines = [CertificationInline]
    ordering = ("name",)


class CertificationAdmin(admin.ModelAdmin):
    list_display = ("name", "major", "provider")
    list_filter = ("major", "provider")
    search_fields = ("name", "major__name", "provider")
    ordering = ("major__name", "name")


# ==============================
#  Chatbot Query Admin
# ==============================
class ChatbotQueryAdmin(admin.ModelAdmin):
    list_display = ("user", "question", "timestamp")
    search_fields = ("user__username", "question", "response")
    date_hierarchy = "timestamp"
    ordering = ("-timestamp",)


# ==============================
#  Contact Message Admin
# ==============================
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    search_fields = ("name", "email", "message")
    date_hierarchy = "created_at"
    ordering = ("-created_at",)


# ===== Register everything with the custom admin site (exactly once) =====
admin_site.register(Profile, ProfileAdmin)
admin_site.register(FAQCategory, FAQCategoryAdmin)
admin_site.register(FAQ, FAQAdmin)
admin_site.register(Major, MajorAdmin)
admin_site.register(Certification, CertificationAdmin)
admin_site.register(ChatbotQuery, ChatbotQueryAdmin)
admin_site.register(ContactMessage, ContactMessageAdmin)
