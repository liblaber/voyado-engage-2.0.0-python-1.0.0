# StoresService

A list of all methods in the `StoresService` service. Click on the method name to view detailed information about that method.

| Methods                                         | Description                                          |
| :---------------------------------------------- | :--------------------------------------------------- |
| [stores_v_get_stores](#stores_v_get_stores)     |                                                      |
| [stores_v_create_store](#stores_v_create_store) |                                                      |
| [stores_v_get_store](#stores_v_get_store)       |                                                      |
| [stores_v_update_store](#stores_v_update_store) | Updates a store. externalId is the store identifier. |

## stores_v_get_stores

- HTTP Method: `GET`
- Endpoint: `/api/v2/stores`

**Parameters**

| Name             | Type | Required | Description                                                                                |
| :--------------- | :--- | :------- | :----------------------------------------------------------------------------------------- |
| include_inactive | bool | ❌       | Value indicating if the inactive stores should be included or not. (Default value = false) |

**Return Type**

`List[ApiStore]`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.stores.stores_v_get_stores(include_inactive=False)

print(result)
```

## stores_v_create_store

- HTTP Method: `POST`
- Endpoint: `/api/v2/stores`

**Parameters**

| Name         | Type                              | Required | Description       |
| :----------- | :-------------------------------- | :------- | :---------------- |
| request_body | [ApiStore](../models/ApiStore.md) | ✅       | The request body. |

**Return Type**

`ApiStore`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment
from voyado_engage.models import ApiStore

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = ApiStore(
    name="name",
    city="city",
    country_code="countryCode",
    county="county",
    email="email",
    adjacent_zip_codes="adjacentZipCodes",
    email_unsubscribe_text="emailUnsubscribeText",
    email_view_online_text="emailViewOnlineText",
    external_id="externalId",
    footer_html="footerHtml",
    header_html="headerHtml",
    homepage="homepage",
    phone_number="phoneNumber",
    region="region",
    sender_address="senderAddress",
    sender_name="senderName",
    street="street",
    type_="type",
    zip_code="zipCode",
    active=False,
    time_zone="timeZone"
)

result = sdk.stores.stores_v_create_store(request_body=request_body)

print(result)
```

## stores_v_get_store

- HTTP Method: `GET`
- Endpoint: `/api/v2/stores/{externalId}`

**Parameters**

| Name             | Type | Required | Description                                                                   |
| :--------------- | :--- | :------- | :---------------------------------------------------------------------------- |
| external_id      | str  | ✅       | The external id of the store to get.                                          |
| include_inactive | bool | ❌       | Value indicating if the store can be inactive or not. (Default value = false) |

**Return Type**

`ApiStore`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.stores.stores_v_get_store(
    external_id="externalId",
    include_inactive=True
)

print(result)
```

## stores_v_update_store

Updates a store. externalId is the store identifier.

- HTTP Method: `POST`
- Endpoint: `/api/v2/stores/{externalId}`

**Parameters**

| Name         | Type                              | Required | Description                             |
| :----------- | :-------------------------------- | :------- | :-------------------------------------- |
| request_body | [ApiStore](../models/ApiStore.md) | ✅       | The request body.                       |
| external_id  | str                               | ✅       | The external id of the store to update. |

**Return Type**

`ApiStore`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment
from voyado_engage.models import ApiStore

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = ApiStore(
    name="name",
    city="city",
    country_code="countryCode",
    county="county",
    email="email",
    adjacent_zip_codes="adjacentZipCodes",
    email_unsubscribe_text="emailUnsubscribeText",
    email_view_online_text="emailViewOnlineText",
    external_id="externalId",
    footer_html="footerHtml",
    header_html="headerHtml",
    homepage="homepage",
    phone_number="phoneNumber",
    region="region",
    sender_address="senderAddress",
    sender_name="senderName",
    street="street",
    type_="type",
    zip_code="zipCode",
    active=False,
    time_zone="timeZone"
)

result = sdk.stores.stores_v_update_store(
    request_body=request_body,
    external_id="externalId"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
