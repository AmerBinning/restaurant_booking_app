from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

# New url pattern below
urlpatterns = [
    path('', views.home, name='homepage'),
    path('auth/signup/', views.signup, name='signup'),
    path('auth/login/', auth_views.LoginView.as_view(template_name='registration/login.html', redirect_authenticated_user=True), name='login'),
    path('auth/logout/', auth_views.LogoutView.as_view(template_name='registration/signup.html'), name='logout'),
    path('restaurants/', views.restaurants, name='restaurants'),
<<<<<<< HEAD
    path('profile/', views.dashboard, name='user_dashboard'),
    path('restaurants/<int:restaurant_id>/', views.restaurant_detail, name='detail'),
    path('restaurants/new-restaurant/', views.RestaurantCreate.as_view(), name='rnew'),
    path('restaurants/<int:pk>/restaurant_confirm_delete/', views.RestaurantDelete.as_view(), name='restaurants_delete'),
    path('restaurants/<int:pk>/update/', views.RestaurantUpdate.as_view(), name='restaurants_update'),
=======
    path('dashboard/', views.dashboard, name='user_dashboard'),
    path('profile/', views.update_user_info, name='update_user_info'),
    path('restaurants/<int:restaurant_id>/', views.restaurant_detail, name='rdetail'),
    path('restaurants/new-restaurant/', views.RestaurantCreate.as_view(), name='rnew'),
    path('restaurants/<int:restaurant_id>/reservations/create', views.create_reservation, name='newReservation'),
    path('restaurants/<int:restaurant_id>/add-menu/', views.add_menu, name='add_menu'),
>>>>>>> master
]



