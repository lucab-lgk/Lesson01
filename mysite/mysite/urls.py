from django.contrib import admin
from django.urls import path, include  # Importer `include` pour inclure les URL des apps

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('your_app.urls')),  # Inclut les URLs de ton application
]