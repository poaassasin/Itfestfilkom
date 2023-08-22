from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class UserItfess(AbstractUser):

    # Fields
    username = models.CharField(max_length=254, unique=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    nama = models.TextField(max_length=100)
    utusan = models.TextField(max_length=100)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    email = models.EmailField(unique=True)
    wa_number = models.TextField(max_length=20, verbose_name="Nomor WA")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','nama','utusan','wa_number']

    class Meta:
        pass

    def __str__(self):
        return str(self.nama)

    def get_absolute_url(self):
        return reverse("Users_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("Users_update", args=(self.pk,))

class Member(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    nama = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    user = models.ForeignKey(UserItfess, on_delete=models.CASCADE)
    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("member_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("member_update", args=(self.pk,))
