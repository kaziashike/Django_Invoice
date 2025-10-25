from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('all_invoices/', views.get_invoices),
    path('create_invoice/', views.create_invoice),
    path('pay_invoice/<int:invoice_id>/', views.pay_invoice),
    path('single_invoice/<int:invoice_id>/', views.get_single_invoice),
]
