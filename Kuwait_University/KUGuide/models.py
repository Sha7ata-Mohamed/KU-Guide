# KUGuide/models.py
from django.db import models
from django.contrib.auth.models import User

def profile_upload_to(instance, filename):
    return f"profile_pics/user_{instance.user_id}/{filename}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    university_id = models.CharField(max_length=15, unique=True)
    major = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to=profile_upload_to, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)  # clearer than "last_login"

    def __str__(self):
        return f"{self.user.username} ({self.major or '—'})"


class FAQCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "FAQ Categories"

    def __str__(self):
        return self.name


class FAQ(models.Model):
    category = models.ForeignKey(FAQCategory, on_delete=models.CASCADE, related_name="faqs")
    question = models.TextField()
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question[:70]


class Major(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Certification(models.Model):
    major = models.ForeignKey(Major, on_delete=models.CASCADE, related_name="certifications")
    name = models.CharField(max_length=150)
    provider = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    link = models.URLField()

    def __str__(self):
        return f"{self.name} - {self.major.name}"


class ChatbotQuery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chatbot_queries")
    question = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Query by {self.user.username} on {self.timestamp.strftime('%Y-%m-%d %H:%M')}"


class ContactMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="contact_messages")
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"
