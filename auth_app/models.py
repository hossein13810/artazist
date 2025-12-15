from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.db import models


class UsersDataManager(BaseUserManager):
    def create_user(self, user_firstname, user_lastname, phone_number, national_code, home_address, user_last_login, password=None):
        if not phone_number:
            raise ValueError('Enter Phone Number: ')
        else:
            user = self.model(user_firstname=user_firstname, user_lastname=user_lastname, phone_number=phone_number, national_code=national_code, home_address=home_address, user_last_login=user_last_login)
            user.set_password(password)
            user.save()
            return user

    def create_superuser(self, phone_number, password):
        user = self.create_user(user_firstname='admin', user_lastname='admin', phone_number=phone_number, national_code='', home_address='', user_last_login=None, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user


class UsersData(AbstractBaseUser):
    user_firstname = models.CharField(max_length=200, blank=True, null=True)
    user_lastname = models.CharField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(max_length=200, blank=True, null=True, unique=True)
    national_code = models.CharField(max_length=200, blank=True, null=True)
    home_address = models.TextField(blank=True, null=True)
    birth_day = models.CharField(max_length=200, blank=True, null=True)
    gender = models.CharField(max_length=200, blank=True, null=True)
    user_last_login = models.DateTimeField(blank=True, null=True)
    admin_permission = models.BooleanField(default=False, blank=True, null=True)
    master_of_admins = models.BooleanField(default=False, blank=True, null=True)
    device_token = models.CharField(max_length=500, blank=True, null=True)
    set_identification_code = models.CharField(max_length=500, blank=True, null=True)
    my_identification_code = models.CharField(max_length=500, blank=True, null=True)
    is_staff = models.BooleanField(default=False, blank=True, null=True)

    objects = UsersDataManager()

    USERNAME_FIELD = 'phone_number'

    def __str__(self):
        return self.phone_number if self.phone_number else self.national_code

    @staticmethod
    def has_perm(perm, obj=None):
        return True

    @staticmethod
    def has_module_perms(app_label):
        return True


class CreateNewUserData(models.Model):
    user_phone_number = models.CharField(max_length=200, blank=True, null=True)
    user_random_code = models.CharField(max_length=200, blank=True, null=True)
    send_time = models.DateTimeField(blank=True, null=True)
    try_count = models.IntegerField(blank=True, null=True)


class UserPermissions(models.Model):
    user_data = models.ForeignKey(UsersData, blank=True, null=True, on_delete=models.CASCADE)
    permission_name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.user_data.phone_number)
