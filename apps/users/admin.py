from django.contrib import admin

# Register your models here.

from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):

    pass

# admin useradmin关联注册


admin.site.register(UserProfile,UserProfileAdmin)


