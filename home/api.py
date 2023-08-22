from rest_framework import viewsets, permissions

from . import serializers
from . import models


class memberViewSet(viewsets.ModelViewSet):
    """ViewSet for the member class"""

    queryset = models.Member.objects.all()
    serializer_class = serializers.memberSerializer
    permission_classes = [permissions.IsAuthenticated]


class UsersViewSet(viewsets.ModelViewSet):
    """ViewSet for the Users class"""

    queryset = models.UserItfess.objects.all()
    serializer_class = serializers.UsersSerializer
    permission_classes = [permissions.IsAuthenticated]