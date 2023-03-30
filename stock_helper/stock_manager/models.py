import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Investor(AbstractUser):
    favorite_stock = models.ManyToManyField(
        "Stock", related_name="interested_investors"
    )

    def favorites(self):
        return [s.name for s in self.favorite_stock.all()]


# TODO need to implement
class DailyProfit(models.Model):
    date = models.DateField(default=datetime.date.today)
    investor = models.ForeignKey("Investor", on_delete=models.CASCADE)
    profit = models.IntegerField(default=0)
    relative_profit = models.IntegerField(default=0)


class TradeRecord(models.Model):
    stock = models.ForeignKey("Stock", on_delete=models.PROTECT)
    owner = models.ForeignKey("Investor", on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    price = models.IntegerField(default=0)


class Stock(models.Model):
    code = models.CharField(max_length=30, primary_key=True, unique=True, blank=False)
    name = models.CharField(max_length=30, blank=False)
    daily_save = models.BooleanField(default=False)
