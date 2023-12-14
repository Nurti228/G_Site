from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.site_view, name='book')
]
