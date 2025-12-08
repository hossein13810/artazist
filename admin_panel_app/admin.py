from django.contrib import admin

from admin_panel_app.models import SourcesData, WithdrawalsData, OperationMessagesData

admin.site.register(SourcesData)
admin.site.register(WithdrawalsData)
admin.site.register(OperationMessagesData)
