from django.contrib import admin
from .models import Account
# Register your models here.


class AccountAdmin(admin.ModelAdmin):
    model = Account
    list_display = ('username', 'email', 'mobile','is_staff','is_verified','is_active','last_login','joined_date') 
    
    readonly_fields = ('last_login','joined_date','password')
    ordering = ('joined_date', )
    filter_horizontal =()
    list_filter = ()
    fieldsets =()



admin.site.register(Account,AccountAdmin)