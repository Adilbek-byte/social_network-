from django.urls import path
from django.contrib.auth.views import (LoginView, LogoutView, 
PasswordResetView, PasswordChangeView, 
PasswordChangeDoneView, PasswordResetDoneView,
PasswordResetConfirmView, PasswordResetCompleteView,
)

from . import views

app_name ='tweets'

urlpatterns = [
path('', views.dashboard, name='dashboard'),
path('register/', views.register, name='register'),											
path('login/', views.user_login, name='login'),
path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
path('edit/', views.edit, name='edit'),
path('users/', views.user_list, name='user_list'),

path('users/<username>/', views.user_detail, name='user_detail'),

path('users/follow/', views.user_follow, name='user_follow'), 







path('password_change/', PasswordChangeView.as_view(template_name='registration/password_change.html'), name='password_change'),
path('password_change/done/', PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), name='password_change_done'),

path('password_reset/', PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset'),
path('password_reset/done/', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
path('reset/done/', PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
]  