from django.urls import path
from . import views

urlpatterns = [
    path('cars/', views.car_list_view),
    path('car/<int:car_id>/', views.car_detail_view),
    path('car_create/', views.create_car_view),
    path('car_update/<int:car_id>/', views.update_car_view),

    path('user/register/', views.user_register_view),
    path('user/login/', views.user_login_view),
    path("user/logout/", views.user_logout_view),
]