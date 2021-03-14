from django.db import models


class Shopping(models.Model):
    id = models.IntegerField(blank=False, auto_created=True, primary_key=True)
    article_name = models.CharField(max_length=100, blank=False, default='')
    article_price_original = models.DecimalField(max_digits=10, decimal_places=2, blank=False, default=0.00)
    currency_original = models.CharField(max_length=5, blank=False, default='')
    supermarket = models.CharField(max_length=70, blank=False, default='')
    article_price_calculated = models.DecimalField(max_digits=10, decimal_places=2, blank=False, default=0.00)
    currency_calculated = models.CharField(max_length=5, blank=False, default='')
    bio = models.BooleanField(default=False)
    category = models.CharField(max_length=200, blank=False, default='')
