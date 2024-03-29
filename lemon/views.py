from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from django.http import Http404
from lemon.forms import ContactForm
from django.core.mail import EmailMessage
from django.template.loader import get_template
#from dal import autocomplete
from departments.models import *
from django.contrib import messages
# Create your views here.

def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the
            # contact information
            template = get_template('contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            }
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Lemonotes" +'',
                ['volkanaktas98@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            messages.success(request,"Your message has been sent. Thank You for your interest..")
            return redirect('contact')

    return render(request, 'contact.html', {
        'form': form_class,
    })


# class CategoryAutocomplete(autocomplete.Select2QuerySetView):
#     def get_queryset(self):
#         # Don't forget to filter out results depending on the visitor !
#         if not self.request.user.is_authenticated():
#             return Category.objects.none()

#         qs = Category.objects.all()

#         if self.q:
#             qs = qs.filter(name__istartswith=self.q)

#         return qs
