from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .forms import ContactForm
from django.conf import settings

# Create your views here.
def home_view(request):
    return render(request, "home.html", {})


def about_me_view(request):
    return render(request, "about_me.html", {})

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data [name]
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Create HTML message
            html_message = render_to_string(
                'emails/contact.html',
                {'name': name, 'email': email, 'message': message}

            )
            

            # Send email
            send_mail(
                subject="New Contact Form Submission",
                message=message, #Plain text version
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['your_email@example.com'],
                                fail_silently=False,
                html_message=html_message
                                
           ) 


            return render (request, 'contact_success.html', {'name': name})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})            
                