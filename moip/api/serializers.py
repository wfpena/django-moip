# -*- coding: utf-8 -*-
from rest_framework import serializers

from moip.models import Subscriptions


class SubscriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriptions
        fields = '__all__'
