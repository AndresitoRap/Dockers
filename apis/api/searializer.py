from rest_framework import serializers
from .models import Category, Product, Customer, Operator, Order, OrderItem, Bill


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class OperatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operator
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):
    # Agrega un campo personalizado 'total' que se calcula utilizando el método 'get_total'
    total = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = "__all__"

    # Método para obtener el total del objeto 'OrderItem'
    def get_total(self, obj):
        return obj.total()


class BillSerializer(serializers.ModelSerializer):
    # Agrega un campo 'order_items' que se obtiene utilizando el serializador de 'OrderItem'
    order_items = OrderItemSerializer(
        source="order.orderitem_set", many=True, read_only=True
    )

    class Meta:
        model = Bill
        fields = "__all__"
