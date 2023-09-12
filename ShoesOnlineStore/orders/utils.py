import json
from django.contrib.sessions.backends.db import SessionStore
from rest_framework.response import Response
from rest_framework import status
from decimal import Decimal
from orders.models import OrderItem
from shoes.models import Product
from shoes.serializer import ProductSimpleSerializer
session = SessionStore()
session_key = "products"


def remove_product_from_session(id):
    global session
    id = str(id)

    if session_key not in session:
        return Response({"message": "Empty cart"})

    if id not in session[session_key]:
        return Response({"message": "Item does not exist"})
    del session[session_key][id]
    session.save()

    return Response({"message": "Deleted"})


def add_product_to_session(id, price, quantity, total_price):
    global session
    if session_key not in session:
        session = SessionStore(session_key=session_key)

    if session_key not in session:
        session[session_key] = {}

    product = {
        id: {
            'price': str(price),
            'quantity': quantity,
            'total_price': str(total_price)}
    }

    session[session_key].update(product)
    session.save()
    return session[session_key]


class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        return super(DecimalEncoder, self).default(obj)


def session_cart() -> dict:

    global session
    global session_key
    # session.get(session_key, {})
    if session_key in session:
        # if session[session_key]:  # != {}:
        cart_item = {}
        main_total = Decimal(0)
        for k, v in session[session_key].items():
            product = Product.objects.get(id=int(k))
            serilized_product = ProductSimpleSerializer(product).data
            price = Decimal(v['price'])
            sub_total = Decimal(v['total_price'])

            serilized_product.update(
                {'price': price, 'sub_total': sub_total, 'size': serilized_product['size'][0], 'quantity': v['quantity']})

            main_total += sub_total
            cart_item[serilized_product['id']] = serilized_product

        data = {'cart_items': cart_item, 'grand_total': main_total}
        return data  # json.dumps(data, cls=DecimalEncoder)
    else:
        # clear_session()
        return {"message": "Empty cart"}


def print_session_items():
    global session
    for item in session[session_key]:
        print("**********" + item+"************")


def clear_session():
    global session
    if session_key in session:
        del session[session_key]
        session.save()


def create_orderItems_from_session(order):

    global product

    product = None
    # Parse the JSON string
    # data = json.loads(session_cart())
    data = session_cart()
    if "cart_items" in data:
        # Access the cart_items and grand_total properties
        cart_items = data["cart_items"]
        grand_total = data["grand_total"]

        # Iterate through the cart items
        for item in cart_items.values():

            product = Product.objects.filter(id=item.get(
                'id'), available_quantity__gte=item["quantity"]).first()
            if product:
                orderItem = OrderItem.objects.create(
                    order=order, product=product, quantity=item["quantity"])
        # product.update(
        #     available_quantity=product.available_quantity-item_quantity)
            else:
                return Response({'message': "Error:Unavailable product or Invalid product"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'message': "Error:Unavailable product or Invalid product"})
