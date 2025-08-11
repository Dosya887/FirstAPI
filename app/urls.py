from django.urls import path
from . import views

urlpatterns = [
    path('cars/', views.car_list_view),
    path('car/<int:car_id>/', views.car_detail_view),
    path('car_create/', views.create_car_view),
    path('car_update/<int:car_id>/', views.update_car_view),
]