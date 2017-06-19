from django.db import models
from book_author.models import BookAuthor
import datetime
from dateutil.relativedelta import relativedelta
from user.models import RentUser
# Create your models here.

class Book(models.Model):
    author = models.ManyToManyField(BookAuthor)
    can_be_rented = models.BooleanField(default=True)
    book_name = models.CharField(max_length=256)
    rent_cost = models.FloatField()
    count_month_rented = models.IntegerField(default=0)
    rent_estimate_time = models.DateTimeField(default=datetime.datetime.now())
    owner = models.ForeignKey(RentUser, null=True)

    def save(self, *args, **kwargs):
        if self.count_month_rented != 0:
            self.rent_estimate_time = datetime.datetime.today() + relativedelta(months=self.count_month_rented)
        super().save(*args, **kwargs)