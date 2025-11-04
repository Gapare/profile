from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from .models import ContactSubmission
from django.contrib import messages

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save to database
            submission = ContactSubmission(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            submission.save()
            
            # Send email
            send_mail(
                f"New contact from {form.cleaned_data['name']}",
                form.cleaned_data['message'],
                form.cleaned_data['email'],
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )
            
            messages.success(request, "Your message has been sent!")
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'contact/contact.html', {'form': form})