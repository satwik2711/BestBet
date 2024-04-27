from django.urls import path
from .views import bestbet

urlpatterns = [
    path('bestbet/', bestbet, name='bestbet'),
]
