from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_record, name='create_record'),
    path('view/<int:id>/', views.view_record, name='view_record'),
    path('update/<int:id>/', views.update_record, name='update_record'),
    path('delete/<int:id>/', views.delete_record, name='delete_record'),
]
