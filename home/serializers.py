from rest_framework import serializers

from . import models


class memberSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Member
        fields = [
            "last_updated",
            "created",
            "user",
            "nama",
            "email"
        ]

class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserItfess
        fields = [
            "nama",
            "wa_number",
            "last_updated",
            "created",
            "email",
            "utusan",
        ]