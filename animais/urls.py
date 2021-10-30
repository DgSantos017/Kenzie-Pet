from django.urls import path
from .views import AnimalView

urlpatterns = [
    path('animais/', AnimalView.as_view())
]
