from rest_framework.routers import SimpleRouter
from .views import ITEMSpage,orderAdd
from django.urls import path
from .views import user_info,delete_user
router =SimpleRouter()
router.register('api/items',ITEMSpage)



urlpatterns = [
    path('',user_info,name='user_info'),
    path('api/order-add/', orderAdd.as_view()),
    path('delete_user/<int:user_id>/', delete_user, name='delete_user'),
    
]
urlpatterns+=router.urls
