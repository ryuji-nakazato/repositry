from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.MyLoginView.as_view(), name="login"),
    path('logout/', views.MyLogoutView.as_view(), name="logout"),
    path('index/', views.IndexView.as_view(), name="index"),
    path('password_change/', views.PasswordChange.as_view(), name="password_change"),
    path('password_change/done/', views.PasswordChangeDone.as_view(), name="password_change_done"),
]