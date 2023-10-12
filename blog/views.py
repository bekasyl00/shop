from django.shortcuts import render,redirect
from .models import order
from .serializers import Itemser,Orderser
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Item
from cloudipsp import Api, Checkout
import time

class ITEMSpage(ModelViewSet):
    queryset=Item.objects.all ()
    serializer_class=Itemser
    
def hom(request):
    return render(request,'blog/home.html')
        
class orderAdd(APIView):
    def post(self,req):
        Order=Orderser(data=req.data)
        print(req.data)
        if Order.is_valid():
            Order.save()
            
            api = Api(merchant_id=1396424,
               secret_key='test')
            checkout = Checkout(api=api)
            data = {
                "currency": "USD",
                "amount": int(req.data['sum'])*100,
                "order_desc":"оплата товаров",
                "order_id":str(time.time())
                }
            url = checkout.url(data).get('checkout_url')
            return Response({'result':'sdfsdb...','url':url})
        return Response({'result':'info'})
        



def user_info(request):
    users = order.objects.all()
    return render(request, 'blog/home.html', {'users': users})

def delete_user(request, user_id):
    user = order.objects.get(pk=user_id)
    if request.method == 'POST':
        user.delete()
    return redirect('user_info')

