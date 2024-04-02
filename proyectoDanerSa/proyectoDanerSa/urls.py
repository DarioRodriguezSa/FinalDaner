from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.urls import include, path
from django.contrib.auth import views as auth_views
from Apps.pos.views import ListaVentasgraph  # Importa la vista desde el espacio de nombres "Apps.pos"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Apps.pos.urls')),
    path('', include('Apps.authentication.urls')),
    path('inventario/', include('Apps.inventario.urls')),
    path('clientes/', include('Apps.clientes.urls')),
    path('ventas/', include('Apps.ventas.urls')),
    path('compras/', include('Apps.compras.urls')),
    path('rutas/', include('Apps.rutas.urls')),
    path('reporte_generales/', include('Apps.reportes_generales.urls')),
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('accounts/password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
