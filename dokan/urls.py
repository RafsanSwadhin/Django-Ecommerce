from django.contrib import admin
from django.urls import path
from .views import home  # fix the import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home')  # fix the view call
]
