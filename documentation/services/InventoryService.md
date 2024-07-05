# InventoryService

A list of all methods in the `InventoryService` service. Click on the method name to view detailed information about that method.

| Methods                                                       | Description                            |
| :------------------------------------------------------------ | :------------------------------------- |
| [inventory_update_stock_level](#inventory_update_stock_level) | Update stock level for a specific SKU. |

Request model:

- Sku\*: Unique SKU of the product. E.g: "123XYZ"
- Quantity\*: The latest stock quantity of the product. E.g: 10
- Locale: Culture code. A corresponding product feed should be configured. E.g: "sv-se"
- ExternalId: External identifier. E.g: "SE-123XYZ"

\* required |
|[inventory_update_stock_levels](#inventory_update_stock_levels)| Batch update of stock levels for multiple SKU's.

Request model:

- Sku\*: Unique SKU of the product. E.g: "123XYZ"
- Quantity\*: The latest stock quantity of the product. E.g: 10
- Locale: Culture code. A corresponding product feed should be configured. E.g: "sv-se"
- ExternalId: External identifier. E.g: "SE-123XYZ"

\* required |
|[back_in_stock_subscription_subscribe](#back_in_stock_subscription_subscribe)| Create a back in stock subscription for a specific SKU.

Request model:

- ContactId\*: Contact id of the subscriber. E.g: "FF9FD9AF-6778-4714-B0FE-F6E6612840C8"
- Sku\*: Unique SKU of the product. E.g: "123XYZ"
- Locale\*: Culture code. A corresponding product feed should be configured. E.g: "sv-se"
- ExternalId: External identifier. E.g: "SE-123XYZ"

\* required |
|[back_in_stock_subscription_unsubscribe](#back_in_stock_subscription_unsubscribe)| Delete a specific back in stock subscription. |

## inventory_update_stock_level

Update stock level for a specific SKU.

Request model:

- Sku\*: Unique SKU of the product. E.g: "123XYZ"
- Quantity\*: The latest stock quantity of the product. E.g: 10
- Locale: Culture code. A corresponding product feed should be configured. E.g: "sv-se"
- ExternalId: External identifier. E.g: "SE-123XYZ"

\* required

- HTTP Method: `PUT`
- Endpoint: `/api/v2/inventory/stock-levels`

**Parameters**

| Name         | Type                                                | Required | Description       |
| :----------- | :-------------------------------------------------- | :------- | :---------------- |
| request_body | [StockLevelRequest](../models/StockLevelRequest.md) | ✅       | The request body. |

**Return Type**

`dict`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment
from voyado_engage.models import StockLevelRequest

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = StockLevelRequest(
    sku="sku",
    locale="locale",
    quantity=6,
    external_id="externalId"
)

result = sdk.inventory.inventory_update_stock_level(request_body=request_body)

print(result)
```

## inventory_update_stock_levels

Batch update of stock levels for multiple SKU's.

Request model:

- Sku\*: Unique SKU of the product. E.g: "123XYZ"
- Quantity\*: The latest stock quantity of the product. E.g: 10
- Locale: Culture code. A corresponding product feed should be configured. E.g: "sv-se"
- ExternalId: External identifier. E.g: "SE-123XYZ"

\* required

- HTTP Method: `PUT`
- Endpoint: `/api/v2/inventory/stock-levels/batch`

**Parameters**

| Name         | Type                                                      | Required | Description       |
| :----------- | :-------------------------------------------------------- | :------- | :---------------- |
| request_body | [List[StockLevelRequest]](../models/StockLevelRequest.md) | ✅       | The request body. |

**Return Type**

`dict`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = [
    {
        "sku": "sku",
        "locale": "locale",
        "quantity": 6,
        "external_id": "externalId"
    }
]

result = sdk.inventory.inventory_update_stock_levels(request_body=request_body)

print(result)
```

## back_in_stock_subscription_subscribe

Create a back in stock subscription for a specific SKU.

Request model:

- ContactId\*: Contact id of the subscriber. E.g: "FF9FD9AF-6778-4714-B0FE-F6E6612840C8"
- Sku\*: Unique SKU of the product. E.g: "123XYZ"
- Locale\*: Culture code. A corresponding product feed should be configured. E.g: "sv-se"
- ExternalId: External identifier. E.g: "SE-123XYZ"

\* required

- HTTP Method: `POST`
- Endpoint: `/api/v2/inventory/backinstock/subscriptions`

**Parameters**

| Name         | Type                                                    | Required | Description       |
| :----------- | :------------------------------------------------------ | :------- | :---------------- |
| request_body | [SubscriptionRequest](../models/SubscriptionRequest.md) | ✅       | The request body. |

**Return Type**

`dict`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment
from voyado_engage.models import SubscriptionRequest

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = SubscriptionRequest(
    contact_id="00000000-0000-0000-0000-000000000000",
    sku="sku",
    locale="locale",
    external_id="externalId"
)

result = sdk.inventory.back_in_stock_subscription_subscribe(request_body=request_body)

print(result)
```

## back_in_stock_subscription_unsubscribe

Delete a specific back in stock subscription.

- HTTP Method: `DELETE`
- Endpoint: `/api/v2/inventory/backinstock/subscriptions/{subscriptionId}`

**Parameters**

| Name            | Type | Required | Description |
| :-------------- | :--- | :------- | :---------- |
| subscription_id | str  | ✅       |             |

**Return Type**

`dict`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.inventory.back_in_stock_subscription_unsubscribe(subscription_id="subscriptionId")

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
