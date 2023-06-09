from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.hashers import make_password
# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email not found!")
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.password = make_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique= True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    profile_image = models.ImageField(blank=True, upload_to='profiles', default='/profiles/default_profile.jpeg')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_full_name(self):
        return self.first_name + " "+ self.last_name
    
    def get_short_name(self):
        return self.first_name
    
    def __str__(self):
        return self.email
    
class Store(models.Model):  
    barcode_id = models.TextField(primary_key=True)
    item_name = models.CharField(max_length=255)
    price = models.IntegerField(max_length=255)
    categories = models.TextField(max_length=255)
    item_image = models.ImageField(blank=True, upload_to='items', default='/items/default_item.jpeg')

    def __str__(self):
        return self.item_name

class Cart_User(models.Model):
    cart_id=models.BigIntegerField();
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.cart_id)+"--"+str(self.user_id.id)

    class Meta:
        unique_together = ("cart_id", "user_id")


class Cart(models.Model):
    item = models.ForeignKey(Store, on_delete=models.CASCADE)
    cart_id=models.IntegerField(default=1)
    def __str__(self):
        return f"{self.item.item_name} : {self.cart_id}"

    class Meta:
        ordering = ['item__item_name']