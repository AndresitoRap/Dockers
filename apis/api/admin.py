from django.contrib import admin
from .models import Category, Product, Customer, Operator, Order, OrderItem, Bill

# Registra los modelos en el panel de administración de Django
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Operator)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Bill)
