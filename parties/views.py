from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import PartiesForm



def parties(request):
    """
    A view to return contact page and render the form, allowing a user
    to contact the website owner/manager by submitting the form.
    """
    if request.method == 'POST':
        parties_form = PartiesForm(request.POST)
        if parties_form.is_valid():
            full_name = parties_form.cleaned_data['full_name']
            user_email = parties_form.cleaned_data['email']
            message = parties_form.cleaned_data['message']
            try:
                send_mail(
                    # to capture the user email it's displayd in subject field and can be responded to
                    f"Message from {full_name}, <{user_email}>", 
                    message,
                    user_email,
                    [settings.DEFAULT_FROM_EMAIL],
                    fail_silently=False
                )
                return redirect('thankyou_parties')
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
    else:
        # Attempt to prefill full_name and email fields for logged in user, if they have
        # this information saved in the profile
        if request.user.is_authenticated:
            profile = Profile.objects.get(user=request.user)
            user_email = profile.user.email
            parties_form = PartiesForm(initial={
                'full_name': profile.profile_full_name,
                'email': user_email,
                })
        else:
            parties_form = PartiesForm()

    context = {
        'parties_form': parties_form,
        
    }

    return render(request, 'parties/parties.html', context)


def parties_thankyou(request):
    """
    A view to return contact_thankyou page in order \
        to inform user that the message was succseddfully sent
    """
    return render(request, 'parties/thankyou_parties.html')
    