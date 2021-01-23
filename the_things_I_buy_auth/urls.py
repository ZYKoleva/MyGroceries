from django.urls import path

from the_things_I_buy_auth.views import login_user, logout_user, register_user, reset_password

urlpatterns = [
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', register_user, name='register'),
    path('reset_psw/', reset_password, name = 'reset password')
]