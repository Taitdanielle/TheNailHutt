from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from profiles.models import UserProfile


def contact(request):
    """
    A view to return contact page and render the form, allowing a user
    to contact the website owner/manager by submitting the form.
    """
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            full_name = contact_form.cleaned_data['full_name']
            user_email = contact_form.cleaned_data['email']
            message = contact_form.cleaned_data['message']
            try:
                send_mail(
                    # to capture the user email it's displayd in subject field and can be responded to
                    f"Message from {full_name}, <{user_email}>", 
                    message,
                    user_email,
                    [settings.DEFAULT_FROM_EMAIL],
                    fail_silently=False
                )
                return redirect('contact_thankyou')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
    else:
            contact_form = ContactForm()

    context = {
        'contact_form': contact_form,
        
   }

    return render(request, 'contact/contact.html', context)


def contact_thankyou(request):
    """
    A view to return contact_thankyou page in order \
        to inform user that the message was succseddfully sent
    """
    return render(request, 'contact/thankyou_contact.html')