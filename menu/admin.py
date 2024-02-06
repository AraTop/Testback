from django.contrib import admin
from menu.models import Menu


@admin.register(Menu)
class UserAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'menu_name')
