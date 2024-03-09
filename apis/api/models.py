from django.db import models


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.PositiveBigIntegerField(default=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    identification = models.PositiveBigIntegerField(default=True)
    addres = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    phone = models.PositiveBigIntegerField()

    def __str__(self):
        return self.name


class Operator(models.Model):
    operator_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE)
    operator_name = models.ForeignKey(Operator, on_delete=models.CASCADE)
    created_order = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.order_id}: {self.customer_name.name} ({self.customer_name.identification})"


class OrderItem(models.Model):
    order_item_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField()
    discount = models.PositiveBigIntegerField(default=0)

    # Método que calcula el subtotal del ítem
    def subtotal(self):
        return self.quantity * self.product.price

    # Método que calcula el total del ítem considerando el descuento
    def total(self):
        return max(self.quantity * self.product.price - self.discount, 0)


class Bill(models.Model):
    bill_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    total = models.PositiveBigIntegerField(editable=False)

    # Método que calcula el total de la factura sumando los totales de los ítems del pedido
    def calculate_total(self):
        total = sum(item.total() for item in self.order.orderitem_set.all())
        return max(total, 0)

    # Método que se ejecuta al guardar la factura y actualiza el total utilizando el método anterior
    def save(self, *args, **kwargs):
        self.total = self.calculate_total()
        super().save(*args, **kwargs)
