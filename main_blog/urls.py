from django.urls import path
from .views import index, categoria

urlpatterns = [
    path('', index, name='index'),
    path('categoria/<str:nombre>', categoria, name='categoria')
]