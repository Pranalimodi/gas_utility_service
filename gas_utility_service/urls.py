# gas_utility_service/urls.py

from django.contrib import admin
from django.urls import path, include
from customer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer/', include('customer.urls')),
    path('', views.home, name='home'),  # Serve home view at the root URL
]
