from rest_framework import serializers
from .models import CarBrand, CarModel, UserCar


class CarBrandSerializer(serializers.HyperlinkedModelSerializer):
    models = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = CarBrand
        fields = ['id', 'url', 'name', 'created_at', 'models']


class CarModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CarModel
        fields = ['id', 'url', 'name', 'created_at', 'updated_at', 'car_brand']


class UserCarSerializer(serializers.HyperlinkedModelSerializer):

    """
it gives the option to create new UserCar with all brands and all models.
Does not check if model is of the selected brand.
"""

    class Meta:
        model = UserCar
        fields = '__all__'
