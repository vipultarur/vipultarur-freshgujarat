from django.urls import reverse
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission 
from django.contrib.auth import get_user_model

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    cource =  models.CharField(max_length=30)
    img=models.ImageField(upload_to='user/profile',default="")
    Enrollment = models.CharField(max_length=30, unique=True)
    number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)

    # Add unique related_name for groups and user_permissions
    groups = models.ManyToManyField(Group, related_name='customuser_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_permissions')

    def __str__(self):
        return self.username
    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()
        profile = Profile(user=user, bio=self.cleaned_data['bio'])
        profile.save()
        return user
    

    
class Banner(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50,unique=True)
    status=models.BooleanField(default=False)
    img=models.ImageField(upload_to='Banner/',default="")
    datetime=models.DateTimeField

    def __str__(self):
        return self.name

class Events(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50,unique=True)
    des= models.CharField(max_length=100,unique=True)
    status=models.BooleanField(default=False)
    img=models.ImageField(upload_to='events/',default="")
    datetime=models.DateTimeField

    def __str__(self):
        return self.name

class Services(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50,unique=True)
    des= models.CharField(max_length=100,unique=True)
    status=models.BooleanField(default=False)
    img=models.ImageField(upload_to='Services/',default="")
    datetime=models.DateTimeField
    
    def __str__(self):
        return self.name
class About(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50,unique=True)
    des= models.CharField(max_length=100,unique=True)
    email= models.CharField(max_length=100,unique=True)
    location= models.CharField(max_length=100)
    status=models.BooleanField(default=False)
    img=models.ImageField(upload_to='about/',default="")
    number = models.CharField(max_length=10, blank=True, null=True)
    starttime=models.DateTimeField
    endtime=models.DateTimeField
    
    
    def __str__(self):
        return self.name

class Classcis(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50,unique=True)
    slug=models.SlugField(max_length=100,unique=True)
    price=models.IntegerField(default="")
    dec=models.CharField(max_length=300)
    status=models.BooleanField(default=False)
    img=models.ImageField(upload_to='Classcis/',default="")
    datetime=models.DateTimeField
    
    def get_url(self):
        return reverse('classcis_detail',args=[self.Category.slug,self.slug])

    def __str__(self):
        return self.name

class Masessage(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50,unique=True)
    des= models.CharField(max_length=100,unique=True)
    status=models.BooleanField(default=False)
    img=models.ImageField(upload_to='message/',default="")
    datetime=models.DateTimeField

    def __str__(self):
        return self.name
    

class Gallary(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50,unique=True)
    status=models.BooleanField(default=False)
    img=models.ImageField(upload_to='Gallary/',default="")
    datetime=models.DateTimeField

    def __str__(self):
        return self.name

class links(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50,unique=True)
    url = models.CharField(max_length=50,unique=True)
    status=models.BooleanField(default=False)
    img=models.ImageField(upload_to='links/',default="")
    datetime=models.DateTimeField

    def __str__(self):
        return self.name
    
class Title(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50,unique=True)
    url = models.CharField(max_length=50,unique=True)
    status=models.BooleanField(default=False)
    img=models.ImageField(upload_to='title/',default="")
    datetime=models.DateTimeField

    def __str__(self):
        return self.name