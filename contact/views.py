from django.shortcuts import render, redirect
from django.views import View
from contact.forms import ContactForm


class ContactView(View):
    def get(self, request, *args, **kwargs):
        initial_data = {}

        if request.user.is_authenticated:
            initial_data['username']= getattr(request.user, 'username', '')

        form = ContactForm(initial=initial_data)

        context = {'form': form}

        return render(request, 'contact/contact.html', context)


    def post(self,  request, *args, **kwargs):
        form = ContactForm(request.POST)

        if form.is_valid():
            contact_instance = form.save(commit=False)

            if request.user.is_authenticated:
                contact_instance.user = request.user

            contact_instance.save()

            return redirect('shopping_store:index')

        context = {'form': form}

        return render(request, 'contact/contact.html', context)