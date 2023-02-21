from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    order = models.ForeignKey("Order", on_delete=models.SET_NULL , blank = True, null = True)
    counter = models.IntegerField(default=0)


class Order(models.Model):
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    name = models.CharField(max_length=20, default="Complex Order")
    description = models.TextField(default="заказик")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=100500)

    def fdescription(self):
        total = ''
        for orderitem in Item.objects.filter(order=self):
            total += orderitem.name + " (" + str(orderitem.counter) + "); "
        return total

    def fprice(self):
        total = 0
        for orderitem in Item.objects.filter(order=self):
            total += orderitem.price * orderitem.counter
        return total