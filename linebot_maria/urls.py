from django.urls import path
from .views import IndexView

urlpatterns = [
    path('callback/', IndexView.as_view(), name='callback'),
]
