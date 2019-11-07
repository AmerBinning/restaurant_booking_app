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
    path('profile/', views.dashboard, name='user_dashboard'),
    path('restaurants/<int:restaurant_id>/', views.restaurant_detail, name='detail'),
    path('restaurants/new-restaurant/', views.RestaurantCreate.as_view(), name='rnew'),
    path('restaurants/<int:pk>/restaurant_confirm_delete/', views.RestaurantDelete.as_view(), name='restaurants_delete'),
    path('restaurants/<int:pk>/update/', views.RestaurantUpdate.as_view(), name='restaurants_update'),
]



