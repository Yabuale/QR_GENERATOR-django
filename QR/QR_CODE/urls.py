from django.urls import path
from .views import generate_qr_code

app_name = 'qr_code_app'

urlpatterns = [
    path('', generate_qr_code, name='generate_qr_code'),
]
