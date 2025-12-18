from django.urls import path
from optimizer.views import index, optimize

urlpatterns = [
    path('', index),
    path('optimize/', optimize),
]
