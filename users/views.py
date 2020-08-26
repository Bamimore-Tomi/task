from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import send_mail
from .forms import EmailForm 
from .forms import UserRegisterForm
# Create your views here.

def register(request):
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created, you can now login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
@login_required
@user_passes_test(lambda person: person.is_superuser)
def mail_users(request):
    if request.method=="POST":
        mail_form = EmailForm(request.POST)
        if mail_form.is_valid():
            subject = mail_form.cleaned_data['subject']
            message = mail_form.cleaned_data['message']
            sender = mail_form.cleaned_data['sender']
            recipients = list(User.objects.filter(is_active=True).values_list("email", flat=True))
            cc = mail_form.cleaned_data['cc']
            if cc:
                recipients.append(sender)
            send_mail(subject, message , sender , recipients)
            messages.success(request, f'Mail Has Been Sent to All Users')
    else:
        mail_form = EmailForm()
    return render(request, 'users/mail.html', { 'form':  mail_form })
@login_required
def profile(request):
    return render(request, 'users/profile.html')