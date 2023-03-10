from django.urls import path

from .views import HelloAuthView, UserCreationView

urlpatterns = [
    path('', HelloAuthView.as_view(), name='hello-auth'),
    path('signup/', UserCreationView.as_view(), name='sign_up'),
]