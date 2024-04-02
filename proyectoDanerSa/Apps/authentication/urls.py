from django.urls import path
from django.contrib.auth import views as auth_views
from .views import login_view, forgot_password

app_name = "Apps.authentication"
urlpatterns = [
    path('accounts/login/', login_view, name="login"),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name="logout"),


]