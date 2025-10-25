from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('invoices/', views.get_invoices, name='get_invoices'),
    path('invoices/<str:invoice_id>/', views.get_single_invoice, name='get_single_invoice'),
    path('invoices/create/', views.create_invoice, name='create_invoice'),
    path('invoices/<str:invoice_id>/pay/', views.pay_invoice, name='pay_invoice'),
]
