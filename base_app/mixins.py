from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect

from auth_app.models import UserPermissions, UsersData


class RoleRequiredMixin(UserPassesTestMixin):
    required_roles = []

    def test_func(self):
        access_status = True
        permissions_list = []
        for permission in UserPermissions.objects.filter(user_data=UsersData.objects.get(id=self.request.user.id)):
            permissions_list.append(permission.permission_name)

        for permission in self.required_roles:
            if permission not in permissions_list:
                access_status = False
                break

        if not self.request.user.admin_permission:
            access_status = False

        return access_status

    def handle_no_permission(self):
        return redirect('AdminLoginPageClass')
