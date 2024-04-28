from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/', Dashboard, name="dashboard"),
    path('login/', Login, name="login"),
    path('register/', Register, name="register"),
    path('update/', UpdateProfile, name="update_profile"),
    path('password/change/', ChangePassword, name="change_password"),
    path('logout/', logout_view, name='logout'),
]