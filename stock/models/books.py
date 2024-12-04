from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django_resized import ResizedImageField

from stock.models import Category





class Book(models.Model):
    title = models.CharField(max_length=225)
    author = models.CharField(max_length=225)
    cover = ResizedImageField(size=[600, 840], crop=['middle', 'center'], upload_to='books/')
    categories = models.ManyToManyField(Category, 'books', null=True)
    price = models.IntegerField()
    short_description = models.CharField(max_length=512, null=True, blank=True)
    long_description = models.TextField(null=True, blank=True)
    quantity = models.IntegerField(default=0)
    isbn = models.CharField(max_length=225)
    sku = models.CharField(max_length=225)

    @property
    def rating(self):
        return self.sku


class AdditionalInfo(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    desc = models.CharField(max_length=225)


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)])
    text = models.CharField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)
