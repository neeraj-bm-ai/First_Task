from django.db import models
import datetime
# Create your models here.
class UsersMail(models.Model):
    email_id = models.EmailField(max_length=50, primary_key=True)
    email_sent_time = models.DateTimeField(auto_now_add=True, blank=True)
    email_status = models.CharField(max_length=10)

    # def __str__(self):
    #     return str(self.id)