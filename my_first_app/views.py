from django.shortcuts import render
from django.core.mail import EmailMessage
from django.conf import settings
from .models import UsersMail
from datetime import datetime
# Create your views here.
from .form import WriteEmail

def SentMail(request):
    if request.method == 'GET':
        form = WriteEmail()
    if request.method == 'POST':
        users = ['abc@gmail.com', 'xyz@gmail.com', 'pqr@gmail.com']
        # users = ['neeraj246850@gmail.com']
        form = WriteEmail(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            for user_email in users:
                email = EmailMessage(
                subject,
                message,
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

                q = UsersMail(email_id=user_email, email_sent_time=now, email_status=status, email_message=message)
                q.save()  

    context = {'form':form}       
    return render(request, 'index.html', context)    


