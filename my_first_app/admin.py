from django.contrib import admin
from .models import UsersMail
# Register your models here.
@admin.register(UsersMail)
class UsersMailModelAdmin(admin.ModelAdmin):
    list_display = ['email_id', 'email_sent_time', 'email_status']