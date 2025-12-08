from django.contrib import admin
from django.contrib.auth.models import Group

from auth_app.models import UsersData, CreateNewUserData, UserPermissions


class UserDataShowMode(admin.ModelAdmin):
    fieldsets = ((None, {"fields": ('user_firstname', 'user_lastname', 'phone_number', 'national_code', 'home_address', 'user_last_login', 'admin_permission', 'device_token', 'master_of_admins', 'birth_day', 'gender', 'set_identification_code', 'my_identification_code', 'password')}),)


admin.site.register(UsersData, UserDataShowMode)
admin.site.register(CreateNewUserData)
admin.site.register(UserPermissions)
admin.site.unregister(Group)
