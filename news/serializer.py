# coding: utf-8

from rest_framework import serializers

from .models import Pick


class PickSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pick
        fields = ('user_id', 'pick_id')
