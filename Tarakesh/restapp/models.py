from django.db import models
from django.contrib import admin
# Create your models here.
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    remark = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
class ContactAdmin(admin.ModelAdmin):
    list_display=["name","email","phone","remark","submitted_at"]
    