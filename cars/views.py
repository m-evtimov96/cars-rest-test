from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly
from .models import CarBrand, CarModel, UserCar
from .serializers import CarBrandSerializer, CarModelSerializer, UserCarSerializer


class CarBrandView(viewsets.ModelViewSet):
    """
    Multichoice filter by id can be used on get: localhost:8000/car-brand/?id__in=1,3,5
    """
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly]
    filter_fields = {
        'id': ["in", "exact"]
    }

class CarModelView(viewsets.ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly]
    filter_fields = {
        'id': ["in", "exact"]
    }


class UserCarView(viewsets.ModelViewSet):
    queryset = UserCar.objects.all()
    serializer_class = UserCarSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly]
    filter_fields = {
        'id': ["in", "exact"]
    }