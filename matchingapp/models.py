from django.db import models
from django.contrib.auth.models import User


# 需要テーブル
class Demand(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             null=True,
                             blank=False)
    item = models.CharField(max_length=10)
    quantity = models.IntegerField()
    postalcode = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    deadline = models.DateField()
    completed = models.BooleanField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} {self.item} {str(self.quantity)}"

    class Meta:
        ordering = ['deadline']


# 供給テーブル
class Supply(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             null=True,
                             blank=False)
    item = models.CharField(max_length=10)
    quantity = models.IntegerField()
    postalcode = models.CharField(max_length=10)
    address = models.CharField(max_length=50)
    shipmentdate = models.DateField()
    completed = models.BooleanField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} {self.item} {str(self.quantity)}"

    class Meta:
        ordering = ['shipmentdate']
