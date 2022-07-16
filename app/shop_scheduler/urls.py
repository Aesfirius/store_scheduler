from django.urls import path
from . import views


urlpatterns = [
    path("login/", views.LoginView.as_view(), name='login'),
    path("logout/", views.user_logout, name='logout'),

    path("", views.HomeView.as_view(), name='home'),

    path("store_locations/", views.HomeView.as_view(), name='store_locations'),
    path("store_location/<str:sl_id>/", views.HomeView.as_view(), name='store_location'),
    path("store_location/add", views.HomeView.as_view(), name='store_location'),
    path("store_location/upd", views.HomeView.as_view(), name='store_location'),
    path("store_location/del", views.HomeView.as_view(), name='store_location'),

    path("products/", views.HomeView.as_view(), name='products'),
    path("product/<str:p_id>/", views.HomeView.as_view(), name='product'),
    path("product/add/", views.HomeView.as_view(), name='product'),
    path("product/upd/", views.HomeView.as_view(), name='product'),
    path("product/del/", views.HomeView.as_view(), name='product'),

    path("settings/", views.SettingsView.as_view(), name='settings'),
    path("settings/share/", views.ShareView.as_view(), name='share'),
    path("settings/share/add/", views.ShareView.as_view(), name='share'),
    path("settings/share/del/", views.ShareView.as_view(), name='share'),
]
