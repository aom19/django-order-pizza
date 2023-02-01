from django.urls import path

from .views import HelloAuthView

urlpatterns = [
    path('', HelloAuthView.as_view(), name='hello-auth'),
]