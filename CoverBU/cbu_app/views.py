from django.shortcuts import render
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

from cbu_app.models import CBU
from cbu_app.serializers import CBUSerializer


class CreateCBU(generics.CreateAPIView):

    serializer_class = CBUSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.validated_data['owner'] = self.request.user
        serializer.save()


class UserOwnerCBUList(generics.ListAPIView):

    serializer_class = CBUSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return CBU.objects.filter(owner=user)