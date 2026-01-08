import graphene
from graphene_django import DjangoObjectType
from .models import Customer, Product, Order
import re
from django.db import transaction

class CustomerType(DjangoObjectType):
    class Meta:
        model = Customer
        fields = ("id", "name", "email", "phone", "created_at")

class ProductType(DjangoObjectType):
    class Meta:
        model = Product
        fields = ("id", "name", "price", "stock")

class OrderType(DjangoObjectType):
    class Meta:
        model = Order
        fields = ("id", "customer", "order_date", "total_amount", "products")

from graphene_django.filter import DjangoFilterConnectionField
from .filters import CustomerFilter, ProductFilter, OrderFilter

class Query(graphene.ObjectType):
    all_customers = DjangoFilterConnectionField(CustomerType, filterset_class=CustomerFilter)
    all_products = DjangoFilterConnectionField(ProductType, filterset_class=ProductFilter)
    all_orders = DjangoFilterConnectionField(OrderType, filterset_class=OrderFilter)

class CustomerInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    email = graphene.String(required=True)
    phone = graphene.String()

class CreateCustomer(graphene.Mutation):
    class Arguments:
        input = CustomerInput(required=True)

    customer = graphene.Field(CustomerType)
    message = graphene.String()

    @staticmethod
    def mutate(root, info, input):
        if Customer.objects.filter(email=input.email).exists():
            raise Exception("Email already exists.")

        phone_pattern = re.compile(r"^\+?[1-9]\d{1,14}$")
        if input.phone and not phone_pattern.match(input.phone):
            raise Exception("Invalid phone number format.")

        customer = Customer(name=input.name, email=input.email, phone=input.phone)
        customer.save()
        return CreateCustomer(customer=customer, message="Customer created successfully.")

class BulkCreateCustomers(graphene.Mutation):
    class Arguments:
        input = graphene.List(graphene.NonNull(CustomerInput), required=True)
    
    customers = graphene.List(CustomerType)
    errors = graphene.List(graphene.String)

    @staticmethod
    def mutate(root, info, input):
        successful_customers = []
        error_messages = []

        with transaction.atomic():
            for i, customer_data in enumerate(input):
                try:
                    if Customer.objects.filter(email=customer_data.email).exists():
                        raise Exception(f"Customer {i}: Email already exists.")

                    phone_pattern = re.compile(r"^\+?[1-9]\d{1,14}$")
                    if customer_data.phone and not phone_pattern.match(customer_data.phone):
                        raise Exception(f"Customer {i}: Invalid phone number format.")

                    customer = Customer(name=customer_data.name, email=customer_data.email, phone=customer_data.phone)
                    customer.save()
                    successful_customers.append(customer)
                except Exception as e:
                    error_messages.append(str(e))
        
        return BulkCreateCustomers(customers=successful_customers, errors=error_messages)

class ProductInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    price = graphene.Decimal(required=True)
    stock = graphene.Int()

class CreateProduct(graphene.Mutation):
    class Arguments:
        input = ProductInput(required=True)

    product = graphene.Field(ProductType)

    @staticmethod
    def mutate(root, info, input):
        if input.price < 0:
            raise Exception("Price cannot be negative.")
        if input.stock and input.stock < 0:
            raise Exception("Stock cannot be negative.")

        product = Product(name=input.name, price=input.price, stock=input.stock or 0)
        product.save()
        return CreateProduct(product=product)

class OrderInput(graphene.InputObjectType):
    customer_id = graphene.ID(required=True)
    product_ids = graphene.List(graphene.NonNull(graphene.ID), required=True)
    order_date = graphene.DateTime()

class CreateOrder(graphene.Mutation):
    class Arguments:
        input = OrderInput(required=True)

    order = graphene.Field(OrderType)

    @staticmethod
    def mutate(root, info, input):
        customer = Customer.objects.get(pk=input.customer_id)
        if not customer:
            raise Exception("Invalid customer ID.")

        if not input.product_ids:
            raise Exception("At least one product must be selected.")

        products = []
        for product_id in input.product_ids:
            product = Product.objects.get(pk=product_id)
            if not product:
                raise Exception(f"Invalid product ID: {product_id}")
            products.append(product)

        order = Order(customer=customer, order_date=input.order_date)
        order.save()
        order.products.set(products)
        order.calculate_total_amount()
        
        return CreateOrder(order=order)


class Mutation(graphene.ObjectType):
    create_customer = CreateCustomer.Field()
    bulk_create_customers = BulkCreateCustomers.Field()
    create_product = CreateProduct.Field()
    create_order = CreateOrder.Field()
    update_low_stock_products = UpdateLowStockProducts.Field()
class UpdateLowStockProducts(graphene.Mutation):
    updated_products = graphene.List(ProductType)
    success = graphene.Boolean()
    message = graphene.String()

    @staticmethod
    def mutate(root, info):
        low_stock_products = Product.objects.filter(stock__lt=10)
        updated_list = []
        for product in low_stock_products:
            product.stock += 10
            product.save()
            updated_list.append(product)
        
        return UpdateLowStockProducts(
            updated_products=updated_list,
            success=True,
            message=f"Successfully updated {len(updated_list)} products."
        )
