from django.contrib import admin
from .models import User, UserProfile
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'fullname', 'username',
                    'is_admin', 'role', 'is_active')
    ordering = ('is_admin', 'created_date')
    list_filter = ()

    fieldsets = (

    )

    search_fields = ()
    ordering = ()

    filter_horizontal = ()


admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile)
