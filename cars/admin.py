from django.contrib import admin
from .models import CarBrand, CarModel, UserCar


@admin.register(CarBrand)
class CarBrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')


@admin.register(UserCar)
class UserCarAdmin(admin.ModelAdmin):
    list_display = ('user', 'car_brand', 'car_model')
