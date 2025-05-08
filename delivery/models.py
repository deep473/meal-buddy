from django.db import models

# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    email = models.CharField(max_length = 20)
    mobile = models.CharField(max_length = 10)
    address = models.CharField(max_length = 50)

class Restaurant(models.Model):
    name = models.CharField(max_length = 20)
    picture = models.URLField(max_length = 200, default='https://designshack.net/wp-content/uploads/Free-Simple-Restaurant-Logo-Template.jpg')
    cuisine = models.CharField(max_length = 200)
    rating = models.FloatField()
    
class Item(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete = models.CASCADE, related_name = "items")
    name = models.CharField(max_length = 20)
    description = models.CharField(max_length = 200)
    price = models.FloatField()
    vegeterian = models.BooleanField(default=False)
    picture = models.URLField(max_length = 400, default='https://www.indiafilings.com/learn/wp-content/uploads/2024/08/How-to-Start-Food-Business.jpg')

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE, related_name = "cart")
    items = models.ManyToManyField("Item", related_name = "carts")

    def total_price(self):
        return sum(item.price for item in self.items.all())
    