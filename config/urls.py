from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('linebot_maria.urls')),
    path('admin/', admin.site.urls),
]
