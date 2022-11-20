from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('create_qr/', views.create_qr_page, name='create_qr_page'),
    path('create_qr/<str:mode>', views.create_qr, name='create_qr'),
    path('qr/log_in', views.log_in, name='logged_in'),
    path('qr/log_out', views.log_out, name='logged_out'),
    path('qr/rest', views.rest, name='rest'),
    
]
