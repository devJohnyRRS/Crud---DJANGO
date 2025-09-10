from django.urls import path
from . import views

urlpatterns = [
    path('create_contact/', views.create_contact, name='create_contact'),
    path('update_contact/<int:id>/', views.update_contact, name='update_contact'),
    path('delete_contact/<int:id>/', views.delete_contact, name='delete_contact'),
]