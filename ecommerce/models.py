from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    published = models.DateField()
    image = models.ImageField(upload_to='ecommerce/images', default='')
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items = models.CharField(max_length=5000)
    name = models.CharField(max_length=100)
    mobile_no = models.IntegerField()
    address = models.CharField(max_length=700)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)
    mobile_no = models.IntegerField(default=0)

    def __str__(self):
        return self.desc[0:10] + "..."