from django import forms
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class College(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=10)

    def __str__(self):
        return self.location


class Role(models.Model):
    role_name = models.CharField(max_length=15)

    def __str__(self):
        return self.role_name


class Member(models.Model):
    f_name = models.CharField(max_length=10)
    m_name = models.CharField(max_length=10)
    l_name= models.CharField(max_length=10)
    phone = PhoneNumberField(null=False, blank=False, unique=True)
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    def __str__(self):
        return self.f_name + " " + self.m_name + " " + self.l_name


class LeaderPosition(models.Model):
    position_name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.position_name


class Leader(models.Model):
    name = models.ForeignKey(Member, on_delete=models.CASCADE)
    position = models.ForeignKey(LeaderPosition, on_delete=models.CASCADE)
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.ForeignKey(Member, on_delete=models.CASCADE)
    username = models.CharField(max_length=15)
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return self.username


class PostCategory(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Post(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(PostCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=10)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

