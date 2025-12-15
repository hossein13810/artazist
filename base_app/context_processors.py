import datetime

import jdatetime

from auth_app.models import UsersData, UserPermissions
from wallet_app.models import WalletsData


def user_info(request):
    if request.user.is_authenticated and not request.user.is_staff:
        if not request.user.admin_permission:
            user_inventory = WalletsData.objects.get(user_data=UsersData.objects.get(id=request.user.id)).inventory
        else:
            user_inventory = ''
            
        return {
            'user_phone_number': str(request.user.phone_number),
            'user_inventory': user_inventory,
            'user_admin_permissions': list(UserPermissions.objects.filter(user_data_id=request.user.id).values_list('permission_name', flat=True))
        }
    return {}
