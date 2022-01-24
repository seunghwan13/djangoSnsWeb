from django.urls import path
from . import views

urlpatterns = [
    path('sign-up/', views.sign_up_view, name='signup'),
    path('sign-in/', views.sign_in_view, name='signin'),
    path('logout/', views.logout, name='logout'),
    path('user/', views.user_view, name='user-list'),
    path('user/follow/<int:id>', views.user_follow, name='user-follow'),
]