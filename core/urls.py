from django.urls  import path
from .views import index, contact, login_view, logout_view, register_qr


urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register_qr/', register_qr, name='register_qr'),
]
