from django.contrib.auth import login
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Car
from .serializers import CarListSerializer, CarCreateSerializer, CarDetailSerializer, CarUpdateSerializer, \
    UserRegisterSerializer, UserLoginSerializer


@api_view(['GET'])
def car_list_view(request):
    cars = Car.objects.all()
    serializer = CarListSerializer(cars, many=True)
    return Response(serializer.data)


@api_view(['GET', 'DELETE'])
def car_detail_view(request, car_id):
    car = Car.objects.get(id=car_id)
    if request.method == 'GET':
        serializer = CarDetailSerializer(car)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
def create_car_view(request):
    if request.method == 'POST':
        serializer = CarCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['PUT'])
def update_car_view(request, car_id):
    car = Car.objects.get(id=car_id)
    serializer = CarUpdateSerializer(car, data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def user_register_view(request):
    serializer = UserRegisterSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def user_login_view(request):
    serializer = UserLoginSerializer(data=request.data, context={'request': request})
    if serializer.is_valid(raise_exception=True):
        user = serializer.validated_data['user']
        login(request, user)
        return Response(serializer.data, status.HTTP_200_OK)
    return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def user_logout_view(request):
    request.session.flush()
    return Response(status.HTTP_204_NO_CONTENT)
