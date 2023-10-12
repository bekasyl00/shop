from rest_framework.serializers import ModelSerializer
from .models import Item,order



class Itemser(ModelSerializer):
    class  Meta:
        model=Item
        fields='__all__'
        
        
class Orderser(ModelSerializer):
    class  Meta:
        model=order
        fields='__all__'
        
        