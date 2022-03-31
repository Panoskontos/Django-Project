from django.urls import path
from .views import home, watch

urlpatterns = [
    path('home/', home),
    path('watch/', watch),
]
