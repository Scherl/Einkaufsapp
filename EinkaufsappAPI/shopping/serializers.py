from rest_framework import serializers
from .models import Shopping


class ShoppingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shopping
        fields = ('id',
                  'article_name',
                  'article_price_original',
                  'currency_original',
                  'supermarket',
                  'article_price_calculated',
                  'currency_calculated',
                  'bio')

