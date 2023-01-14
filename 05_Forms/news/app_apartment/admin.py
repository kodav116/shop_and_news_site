from django.contrib import admin
from app_apartment.models import Apartment, RoomType, ApartmentNews, RoomCount


class ApartmentAdmin(admin.ModelAdmin):
    list_display = ['address', 'name']


class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ['address', 'room_type', 'room_count']


class ApartmentNewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'short_description', 'text']


class RoomCountAdmin(admin.ModelAdmin):
    list_display = ['count']


admin.site.register(Apartment, ApartmentAdmin)
admin.site.register(RoomType, RoomTypeAdmin)
admin.site.register(ApartmentNews, ApartmentNewsAdmin)
admin.site.register(RoomCount, RoomCountAdmin)
