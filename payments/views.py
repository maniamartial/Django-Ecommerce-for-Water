import math
from datetime import datetime
from products.models import Order
from payments.form import PhoneNumber
from django.http import HttpResponse
from django.shortcuts import redirect, render
import requests
from requests.auth import HTTPBasicAuth
import datetime
import json
from . mpesa_credentials import MpesaAccessToken, LipanaMpesaPpassword


def getAccessToken(request):
    consumer_key = 'XjWEg9z1ihL9zoXO1JRaCOhfIJAgB8cu'
    consumer_secret = 'y48BAeDDA0AgXqI2'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']
    return HttpResponse(validated_mpesa_access_token)


def showform(request):

    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartitems = order.get_cart_items
        total = math.trunc(order.get_cart_totals)

        print(cartitems)

    form = PhoneNumber()
    if request.method == 'POST':
        form = PhoneNumber(request.POST)
        if form.is_valid():

            form.save()
            number = '254' + str(form.cleaned_data.get('phone'))
            print(number)

            print(total)
            access_token = MpesaAccessToken.validated_mpesa_access_token
            api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
            headers = {"Authorization": "Bearer %s" % access_token}
            request = {
                "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
                "Password": LipanaMpesaPpassword.decode_password,
                "Timestamp": LipanaMpesaPpassword.lipa_time,
                "TransactionType": "CustomerPayBillOnline",
                "Amount": total,
                "PartyA":  number,  # replace with your phone number to get stk push -600989
                "PartyB": LipanaMpesaPpassword.Business_short_code,
                "PhoneNumber": number,  # replace with your phone number to get stk push
                "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
                "AccountReference": "Mania",
                "TransactionDesc": "Fear not for I am with you"
            }

            response = requests.post(api_url, json=request, headers=headers)
            print(response)
            # return HttpResponse('success')
            return redirect('paymentcomplete')

    context = {'form': form}
    return render(request, 'payments/payments.html', context)


# The last page
def thankspayment(request):

    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartitems = order.get_cart_items
        total = order.get_cart_totals

        print(cartitems)
        print(total)
    t_time = datetime.datetime.now()
    hours = 0.5
    added_time = datetime.timedelta(hours=hours)
    time = t_time + added_time
    print(time)

    context = {'time': time}
    return render(request, 'payments/thanks.html', context)
