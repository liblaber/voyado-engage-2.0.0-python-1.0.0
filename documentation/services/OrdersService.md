# OrdersService

A list of all methods in the `OrdersService` service. Click on the method name to view detailed information about that method.

| Methods                                         | Description                                                                                                                        |
| :---------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------- |
| [orders_register_order](#orders_register_order) | The /orders endpoint is used to trigger automation flows in Engage and send out information about the order to your end customers. |

It could be used, for example, for an order confirmation, delivery confirmation or a return confirmation from an e-commerce
system or store. The endpoint is called every time a change happens that you want to act on in Engage. All the data needed must
be sent with every call, since this endpoint saves no data concerning orders. If you need to save data, use the /receipts endpoint instead.

Note that there is no check against previous requests of the same order,
thus two identical requests to this endpoint will trigger any matching automation twice.

To accept an order:

- The different orderStatus and paymentStatus values must be configured in Voyado.
- totalGrossPrice, totalTax, item quantities etc. must be correct and add up.

If the order is not accepted, a response with HTTP Status Code 400 or 422 and an error code will be returned. |

## orders_register_order

The /orders endpoint is used to trigger automation flows in Engage and send out information about the order to your end customers.
It could be used, for example, for an order confirmation, delivery confirmation or a return confirmation from an e-commerce
system or store. The endpoint is called every time a change happens that you want to act on in Engage. All the data needed must
be sent with every call, since this endpoint saves no data concerning orders. If you need to save data, use the /receipts endpoint instead.

Note that there is no check against previous requests of the same order,
thus two identical requests to this endpoint will trigger any matching automation twice.

To accept an order:

- The different orderStatus and paymentStatus values must be configured in Voyado.
- totalGrossPrice, totalTax, item quantities etc. must be correct and add up.

If the order is not accepted, a response with HTTP Status Code 400 or 422 and an error code will be returned.

- HTTP Method: `POST`
- Endpoint: `/api/v2/orders`

**Parameters**

| Name         | Type                        | Required | Description       |
| :----------- | :-------------------------- | :------- | :---------------- |
| request_body | [Order](../models/Order.md) | ✅       | The request body. |

**Return Type**

`StatusCodeResult`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment
from voyado_engage.models import Order

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = Order(
    contact={
        "match_key": "matchKey",
        "match_key_type": "Email"
    },
    order_number="orderNumber",
    order_status="orderStatus",
    payment_status="paymentStatus",
    language="language",
    created_date="createdDate",
    shipping_date="shippingDate",
    status_changed_date="statusChangedDate",
    store_id="storeId",
    currency="currency",
    exchange_rate_to_group_currency=9.6,
    extra_data={},
    total_gross_price=9.8,
    total_tax=7.73,
    tax_details=[
        {
            "description": "description",
            "value": 5.55,
            "percent": 1.96,
            "total_including_tax": 9.77,
            "total_excluding_tax": 8.29
        }
    ],
    payment_methods=[
        {
            "type_": "type",
            "description": "description",
            "value": 7.44,
            "extra_data": {}
        }
    ],
    items=[
        {
            "type_": "PURCHASE",
            "sku": "sku",
            "quantity": 0.1,
            "gross_paid_price": 3.23,
            "gross_paid_price_per_unit": 2.41,
            "tax_amount": 4.68,
            "tax_percent": 2.6,
            "description": "description",
            "image_url": "imageUrl",
            "target_url": "targetUrl",
            "extra_data": {},
            "total_discount": 2.06,
            "original_price": 5.07,
            "original_price_per_unit": 5.96,
            "discounts": [
                {
                    "value": -273220990.98,
                    "type_": "type",
                    "description": "description",
                    "extra_data": {}
                }
            ],
            "discounted": True
        }
    ],
    freight_fee={
        "value": 9.6,
        "tax": 0.26,
        "tax_percent": 9.9
    },
    handling_fee={
        "value": 9.6,
        "tax": 0.26,
        "tax_percent": 9.9
    },
    total_round_off={
        "value": 9.6,
        "tax": 0.26,
        "tax_percent": 9.9
    },
    total_discounts=1.47,
    total_original_price=7.35,
    total_items_price=2.46,
    total_net_price=1.99,
    any_return_items=True
)

result = sdk.orders.orders_register_order(request_body=request_body)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
