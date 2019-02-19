from django.contrib.auth.models import User, Group
from django.views.generic import ListView
from rest_framework import serializers
from .models import Contact


class ListContactView(ListView):
    class Meta:
        model = Contact


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')