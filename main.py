from uuid import uuid4
import mercadopago
from decouple import config

back_urls = {
    "success": "http://127.0.0.1:5000/compra-certa",
    "failure": "http://127.0.0.1:5000/compra-errada",
    "pending": "http://127.0.0.1:5000/compra-pendente",
}


def generate_link_payment(items):
    ACCESS_TOKEN = config('ACCESS_TOKEN')
    sdk = mercadopago.SDK(ACCESS_TOKEN)

    request = {
        "items": items,
        "back_urls": {
            "success": "http://127.0.0.1:5000/compra-certa",
            "failure": "http://127.0.0.1:5000/compra-errada",
            "pending": "http://127.0.0.1:5000/compra-pendente",
        },
        "auto_return": "all",
        "notification_url": "http://localhost:5000/notifications",
    }

    preference_response = sdk.preference().create(request)
    preference = preference_response["response"]
    # print(preference)
    # print(preference["init_point"])
    return preference["init_point"]


items = [
    # {
    #     "id": "1",
    #     "title": "Coca-Cola",
    #     "description": "Refrigerante Coca-Cola",
    #     "quantity": 3,
    #     "currency_id": "BRL",
    #     "unit_price": 8,
    # }
    {
        "id": "2",
        "title": "Misto quente",
        "description": "Lanche com pão, presunto e queijo",
        "quantity": 1,
        "currency_id": "BRL",
        "unit_price": 15.0,
    }
]

response = generate_link_payment(items)
print(response)


# curl -X POST \
#     'https://api.mercadopago.com/instore/orders/qr/seller/collectors/446566691/pos/SUC001POS001/qrs'\
#     -H 'Content-Type: application/json' \
#        -H 'Authorization: Bearer TEST-7434*********159-03141*********cee51edf8*********f94f589-1*********' \
#     -d '{
#   "external_reference": "reference_12345",
#   "title": "Product order",
#   "description": "Purchase description.",
#   "notification_url": "https://www.yourserver.com/notifications",
#   "total_amount": 100,
#   "items": [
#     {
#       "sku_number": "A123K9191938",
#       "category": "marketplace",
#       "title": "Point Mini",
#       "description": "This is the Point Mini",
#       "unit_price": 100,
#       "quantity": 1,
#       "unit_measure": "unit",
#       "total_amount": 100
#     }
#   ],
#   "sponsor": {
#     "id": 662208785
#   },
#   "cash_out": {
#     "amount": 0
#   }
# }'