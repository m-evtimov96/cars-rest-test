from django.db import models
from safedelete.models import SafeDeleteModel, SOFT_DELETE_CASCADE
from cars_auth.models import User


class CarBrand(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE

    name = models.CharField(max_length=35)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class CarModel(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE

    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    car_brand = models.ForeignKey(CarBrand, related_name='models', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class UserCar(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE

    first_reg = models.DateTimeField()
    odometer = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car_brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.car_brand.name} {self.car_model.name} with owner {self.user.username}'
