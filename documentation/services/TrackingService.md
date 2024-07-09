# TrackingService

A list of all methods in the `TrackingService` service. Click on the method name to view detailed information about that method.

| Methods                                   | Description                                                                                         |
| :---------------------------------------- | :-------------------------------------------------------------------------------------------------- |
| [cart_register_cart](#cart_register_cart) | Register an update to a specific cart for a given contact. Should be the latest update of the cart. |

Request model:

- CartReference: Unique identifier of the cart. Links the update to a specific cart. Ex: "006788ba-9f65-49c6-b3a0-2315d1854728"
- Time: Time of the cart update. ISO8601 with Time Zone Designators. Ex: "2021-09-22T11:00:00+02:00"
- ContactId: Contact id of the cart owner. GUID or short GUID. Ex: "ae16a9b4-f581-4568-8948-a96100b2afd4"
- Language: Culture code of the cart. A corresponding product feed should be configured. Ex: "sv-SE"
- Url: Url to the cart. Ex: "https://www.store.se/cart?id=006788ba-9f65-49c6-b3a0-2315d1854728"
- Items: Collection of cart items. Ex: ```[{"Sku":"90183744","Quantity":1},{"Sku":"90156607","Quantity":1}]``` |
  |[cart_register_carts](#cart_register_carts)| Register a batch of cart updates. Cart updates are processed according to update time. If multiple cart updates are registered with the same identifier only the latest update (according to update time) is considered.  


Request model:

- CartReference: Unique identifier of the cart. Links the update to a specific cart. Ex: "006788ba-9f65-49c6-b3a0-2315d1854728"
- Time: Time of the cart update. ISO8601 with Time Zone Designators. Ex: "2021-09-22T11:00:00+02:00"
- ContactId: Contact id of the cart owner. GUID or short GUID. Ex: "ae16a9b4-f581-4568-8948-a96100b2afd4"
- Language: Culture code of the cart. A corresponding product feed should be configured. Ex: "sv-SE"
- Url: Url to the cart. Ex: "https://www.store.se/cart?id=006788ba-9f65-49c6-b3a0-2315d1854728"
- Items: Collection of cart items. Ex: "[{"Sku":"90183744","Quantity":1},{"Sku":"90156607","Quantity":1}]" |
  |[product_view_v_register_product_view](#product_view_v_register_product_view)| Register a view of a specific product for a given contact.

Request model:

- ItemId: Unique SKU/Article Id/Item Id of the viewed product. Will be matched against SKU on the imported articles in Voyado. Ex: "123XYZ"
- Category: Category of the product on the website. Will be used for filtering. Ex: "novels &gt; cormac mccarthy &gt; the road"
- Time: Time of the product view. ISO8601 with Time Zone Designators. Ex: "2021-09-22T11:00:00+02:00".
- ContactId: Contact id of the viewer. GUID or short GUID. Ex: "FF9FD9AF-6778-4714-B0FE-F6E6612840C8"
- SessionId: Unique identifier of the session. Ex: "3b7e493b-5dfe-4b98-b6cf-049f2ea4309d"
- NewSession: Boolean value that indicates that new session.
- Language: Culture code of the cart. A corresponding product feed should be configured. Ex: "sv-SE"
- Url: Url of the productview. Ex: "https://www.voyado.com?sku=eu901-011-v10"
- ExternalReferrer: The external site that the user came from (clicked a link) Ex: "https://www.google.com" |
  |[product_view_v_register_product_views](#product_view_v_register_product_views)| Register a collection of views to specific products for given contacts.

Request model:

- ItemId: Unique SKU/Article Id/Item Id of the viewed product. Will be matched against SKU on the imported articles in Voyado. Ex: "123XYZ"
- Category: Category of the product on the website. Will be used for filtering. Ex: "novels &gt; cormac mccarthy &gt; the road"
- Time: Time of the product view. ISO8601 with Time Zone Designators. Ex: "2021-09-22T11:00:00+02:00"
- ContactId: Contact id of the viewer. GUID or short GUID. Ex: "FF9FD9AF-6778-4714-B0FE-F6E6612840C8"
- SessionId: Unique identifier of the session. Ex: "3b7e493b-5dfe-4b98-b6cf-049f2ea4309d"
- NewSession: Boolean value that indicates that new session.
- Language: Culture code of the cart. A corresponding product feed should be configured. Ex: "sv-SE"
- Url: Url of the productview. Ex: "https://www.voyado.com?sku=eu901-011-v10"
- ExternalReferrer: The external site that the user came from (clicked a link) Ex: "https://www.google.com" |

## cart_register_cart

Register an update to a specific cart for a given contact. Should be the latest update of the cart.

Request model:

- CartReference: Unique identifier of the cart. Links the update to a specific cart. Ex: "006788ba-9f65-49c6-b3a0-2315d1854728"
- Time: Time of the cart update. ISO8601 with Time Zone Designators. Ex: "2021-09-22T11:00:00+02:00"
- ContactId: Contact id of the cart owner. GUID or short GUID. Ex: "ae16a9b4-f581-4568-8948-a96100b2afd4"
- Language: Culture code of the cart. A corresponding product feed should be configured. Ex: "sv-SE"
- Url: Url to the cart. Ex: "https://www.store.se/cart?id=006788ba-9f65-49c6-b3a0-2315d1854728"
- Items: Collection of cart items. Ex: "[{"Sku":"90183744","Quantity":1},{"Sku":"90156607","Quantity":1}]"

- HTTP Method: `POST`
- Endpoint: `/api/v2/tracking/carts`

**Parameters**

| Name         | Type                                      | Required | Description       |
| :----------- | :---------------------------------------- | :------- | :---------------- |
| request_body | [CartApiModel](../models/CartApiModel.md) | ✅       | The request body. |

**Return Type**

`OkResult`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment
from voyado_engage.models import CartApiModel

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = CartApiModel(
    cart_reference="cartReference",
    time="time",
    contact_id="contactId",
    language="language",
    url="url",
    items=[
        {
            "sku": "sku",
            "quantity": 10
        }
    ]
)

result = sdk.tracking.cart_register_cart(request_body=request_body)

print(result)
```

## cart_register_carts

Register a batch of cart updates. Cart updates are processed according to update time. If multiple cart updates are registered with the same identifier only the latest update (according to update time) is considered.

Request model:

- CartReference: Unique identifier of the cart. Links the update to a specific cart. Ex: "006788ba-9f65-49c6-b3a0-2315d1854728"
- Time: Time of the cart update. ISO8601 with Time Zone Designators. Ex: "2021-09-22T11:00:00+02:00"
- ContactId: Contact id of the cart owner. GUID or short GUID. Ex: "ae16a9b4-f581-4568-8948-a96100b2afd4"
- Language: Culture code of the cart. A corresponding product feed should be configured. Ex: "sv-SE"
- Url: Url to the cart. Ex: "https://www.store.se/cart?id=006788ba-9f65-49c6-b3a0-2315d1854728"
- Items: Collection of cart items. Ex: "[{"Sku":"90183744","Quantity":1},{"Sku":"90156607","Quantity":1}]"

- HTTP Method: `POST`
- Endpoint: `/api/v2/tracking/carts/batch`

**Parameters**

| Name         | Type                                            | Required | Description       |
| :----------- | :---------------------------------------------- | :------- | :---------------- |
| request_body | [List[CartApiModel]](../models/CartApiModel.md) | ✅       | The request body. |

**Return Type**

`OkResult`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = [
    {
        "cart_reference": "cartReference",
        "time": "time",
        "contact_id": "contactId",
        "language": "language",
        "url": "url",
        "items": [
            {
                "sku": "sku",
                "quantity": 10
            }
        ]
    }
]

result = sdk.tracking.cart_register_carts(request_body=request_body)

print(result)
```

## product_view_v_register_product_view

Register a view of a specific product for a given contact.

Request model:

- ItemId: Unique SKU/Article Id/Item Id of the viewed product. Will be matched against SKU on the imported articles in Voyado. Ex: "123XYZ"
- Category: Category of the product on the website. Will be used for filtering. Ex: "novels &gt; cormac mccarthy &gt; the road"
- Time: Time of the product view. ISO8601 with Time Zone Designators. Ex: "2021-09-22T11:00:00+02:00".
- ContactId: Contact id of the viewer. GUID or short GUID. Ex: "FF9FD9AF-6778-4714-B0FE-F6E6612840C8"
- SessionId: Unique identifier of the session. Ex: "3b7e493b-5dfe-4b98-b6cf-049f2ea4309d"
- NewSession: Boolean value that indicates that new session.
- Language: Culture code of the cart. A corresponding product feed should be configured. Ex: "sv-SE"
- Url: Url of the productview. Ex: "https://www.voyado.com?sku=eu901-011-v10"
- ExternalReferrer: The external site that the user came from (clicked a link) Ex: "https://www.google.com"

- HTTP Method: `POST`
- Endpoint: `/api/v2/tracking/productview`

**Parameters**

| Name         | Type                                                    | Required | Description       |
| :----------- | :------------------------------------------------------ | :------- | :---------------- |
| request_body | [ProductViewApiModel](../models/ProductViewApiModel.md) | ✅       | The request body. |

**Return Type**

`dict`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment
from voyado_engage.models import ProductViewApiModel

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = ProductViewApiModel(
    item_id="itemId",
    category="category",
    time="time",
    contact_id="contactId",
    session_id="sessionId",
    new_session=True,
    language="language",
    url="url",
    external_referrer="externalReferrer",
    utm=[
        {
            "key": "key",
            "value": "value"
        }
    ]
)

result = sdk.tracking.product_view_v_register_product_view(request_body=request_body)

print(result)
```

## product_view_v_register_product_views

Register a collection of views to specific products for given contacts.

Request model:

- ItemId: Unique SKU/Article Id/Item Id of the viewed product. Will be matched against SKU on the imported articles in Voyado. Ex: "123XYZ"
- Category: Category of the product on the website. Will be used for filtering. Ex: "novels &gt; cormac mccarthy &gt; the road"
- Time: Time of the product view. ISO8601 with Time Zone Designators. Ex: "2021-09-22T11:00:00+02:00"
- ContactId: Contact id of the viewer. GUID or short GUID. Ex: "FF9FD9AF-6778-4714-B0FE-F6E6612840C8"
- SessionId: Unique identifier of the session. Ex: "3b7e493b-5dfe-4b98-b6cf-049f2ea4309d"
- NewSession: Boolean value that indicates that new session.
- Language: Culture code of the cart. A corresponding product feed should be configured. Ex: "sv-SE"
- Url: Url of the productview. Ex: "https://www.voyado.com?sku=eu901-011-v10"
- ExternalReferrer: The external site that the user came from (clicked a link) Ex: "https://www.google.com"

- HTTP Method: `POST`
- Endpoint: `/api/v2/tracking/productviews`

**Parameters**

| Name         | Type                                                          | Required | Description       |
| :----------- | :------------------------------------------------------------ | :------- | :---------------- |
| request_body | [List[ProductViewApiModel]](../models/ProductViewApiModel.md) | ✅       | The request body. |

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
        "item_id": "itemId",
        "category": "category",
        "time": "time",
        "contact_id": "contactId",
        "session_id": "sessionId",
        "new_session": True,
        "language": "language",
        "url": "url",
        "external_referrer": "externalReferrer",
        "utm": [
            {
                "key": "key",
                "value": "value"
            }
        ]
    }
]

result = sdk.tracking.product_view_v_register_product_views(request_body=request_body)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
