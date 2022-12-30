from django.contrib import admin

from .models import Menu, MenuItem


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')
    list_filter = ('menu',)
    search_fields = ('name', 'menu')
