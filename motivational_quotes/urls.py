from django.contrib import admin
from django.urls import path
from quotes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('get-quote/', views.get_quote, name='get_quote'),  # Add this line for AJAX quote fetching
]
