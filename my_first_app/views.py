from django.shortcuts import render
from django.core.mail import EmailMessage
from django.conf import settings
from .models import UsersMail
from datetime import datetime
# Create your views here.

def SentMail(request):
    users = ['abc@gmail.com', 'xyz@gmail.com', 'pqr@gmail.com']
    # users = ['neeraj246850@gmail.com']
    count = 0
    for user_email in users:
        email = EmailMessage(
            'Test'
            'Hi, This is the sample email',
            settings.EMAIL_HOST_USER, 
            [user_email],
        )

        now = datetime.now()

        # current_time = now.strftime("%H:%M:%S")

        email.fail_silently = False
        email.send()

        status = 'Not Sent'
        if email.fail_silently:
            status = 'Sent'
        else:
            count += 1

        q = UsersMail(email_id=user_email, email_sent_time=now, email_status=status)
        q.save()  

    context = {'count':count}       
    return render(request, 'index.html', context)    


