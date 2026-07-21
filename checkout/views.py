from django.shortcuts import render, redirect
from django.views import View
from checkout.forms import AddressForm
from checkout.models import Address


class CheckoutView(View):
    def get(self, request, *args, **kwargs):

        form = AddressForm()

        if request.user.is_authenticated:

            initial_data = {
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                'email': request.user.email,
                'phone_number': getattr(request.user, 'phone_number', ''),
            }

            try:
                last_address = Address.objects.filter(user=request.user).latest('created_at')
                form = AddressForm(instance=last_address)
            except:
                form = AddressForm(initial=initial_data)

        context = {'form': form}
        return render(request, 'checkout/checkout.html', context)

    def post(self, request, *args, **kwargs):

        existing_address = Address.objects.filter(user=request.user, is_billing=True).first()

        form = AddressForm(request.POST, instance=existing_address)

        if form.is_valid():
            address_instance = form.save(commit=False)

            address_instance.user = request.user

            address_instance.is_billing = True
            address_instance.save()

            return redirect('shopping_store:index')

        context = {'form': form}
        return render(request, 'checkout/checkout.html', context)
