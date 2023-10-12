from django.db import models
from django.utils import timezone
import pytz
astana_timezone = pytz.timezone('Asia/Almaty')  # Это часовой пояс Астаны
current_time_in_astana = timezone.now().astimezone(astana_timezone)
context = {
    'current_time_in_astana': current_time_in_astana,
}

class Item(models.Model):
    slug=models.SlugField('Уникальная названия')
    title=models.CharField("Нозвания товара", max_length=200)
    image=models.CharField('Фото товара',max_length=200)
    desc=models.TextField('Описания товара')
    price=models.DecimalField('Цена', max_digits=5, decimal_places=2)
    korz=models.CharField(default='10354898_cart_trolley_ui_web_icon.svg',max_length=200)
    ptich=models.CharField(default='326572_check_icon.svg',max_length=200)
    def __str__(self):
        return self.title
    
    
class order(models.Model):
 
    name=models.CharField("Имя пользователя", max_length=200)
    surname=models.CharField("Фамилия", max_length=200)
    email=models.CharField("Email", max_length=200)
    phone=models.CharField("Телефон номер", max_length=200)
    basket=models.TextField("Код товара")
    timer = models.DateTimeField('Дата', default=timezone.now)







    
    def __str__(self):
        return self.name +''+self.surname+' ('+self.phone +')'



    