#
from django.urls import path

from . import views

app_name = "users_app"

urlpatterns = [
    path(
        'register/', 
        views.UserRegisterView.as_view(),
        name='user-register',
    ),
    path(
        '', 
        views.LoginUser.as_view(),
        name='user-login',
    ),
    # path(
    #     'cliente', 
    #     views.LoginClienteUser.as_view(),
    #     name='user-cliente-login',
    # ),
    
    path(
        'logout/', 
        views.LogoutView.as_view(),
        name='user-logout',
    ),
    path(
        'update/', 
        views.PasswordResetByUser.as_view(),
        name='user-update',
    ),
    path(
        'user-verification/<pk>/', 
        views.CodeVerificationView.as_view(),
        name='user-verification',
    ),

    path(
        'user-verification/', 
        views.CargoListview.as_view(),
        name='user-verification',
    ),
    
    
]