from django.urls import path

from . import views

urlpatterns = [
    path('', views.allocate_view, name='allocate'),
    path('hall/<int:hall_id>/', views.hall_view, name='hall_detail'),
]
