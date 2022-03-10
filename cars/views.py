from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly
from .models import CarBrand, CarModel, UserCar
from .serializers import CarBrandSerializer, CarModelSerializer, UserCarSerializer


class CarBrandView(viewsets.ModelViewSet):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly]


class CarModelView(viewsets.ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly]


class UserCarView(viewsets.ModelViewSet):
    queryset = UserCar.objects.all()
    serializer_class = UserCarSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly]
