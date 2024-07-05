# PromotionsService

A list of all methods in the `PromotionsService` service. Click on the method name to view detailed information about that method.

| Methods                                                                                                     | Description                                                                                            |
| :---------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------- |
| [multichannel_promotions_get_by_id](#multichannel_promotions_get_by_id)                                     | Gets the multichannel promotion with the identifier which is set by Voyado                             |
| [multichannel_promotions_update](#multichannel_promotions_update)                                           | Updates an existing multichannel promotion.                                                            |
| Only multichannel promotion in status 'Draft' can be updated.                                               |
| [multichannel_promotions_delete_by_id](#multichannel_promotions_delete_by_id)                               | Only unassigned multichannel promotions can be deleted                                                 |
| [multichannel_promotions_get_validity_by_id](#multichannel_promotions_get_validity_by_id)                   | Gets the multichannel promotion with the identifier which is an internal reference for Voyado          |
| [multichannel_promotions_update_validity](#multichannel_promotions_update_validity)                         | Updates duration of an existing multichannel promotion.                                                |
| Only multichannel promotion in status 'Draft' can be updated.                                               |
| [multichannel_promotions_get_by_external_id](#multichannel_promotions_get_by_external_id)                   | Gets the multichannel promotion with the identifier which is an external reference for Voyado          |
| [multichannel_promotions_create](#multichannel_promotions_create)                                           | Only creates multichannel promotion in status 'Draft'.                                                 |
| [multichannel_promotions_delete_by_external_id](#multichannel_promotions_delete_by_external_id)             | Only unassigned multichannel promotions can be deleted                                                 |
| [multichannel_promotions_get_by_validity_external_id](#multichannel_promotions_get_by_validity_external_id) | Gets the multichannel promotion validity with the identifier which is an external reference for Voyado |
| [offer_promotions_redeem_by_promotion_id](#offer_promotions_redeem_by_promotion_id)                         | Redeem a promotion (multichannel offer or mobile swipe) for a Contact using the internal promotion Id  |

Redemption channel can be POS, ECOM or OTHER. |
|[offer_promotions_reactivate_promotion_code](#offer_promotions_reactivate_promotion_code)| Reactivate a redeemed reward voucher |

## multichannel_promotions_get_by_id

Gets the multichannel promotion with the identifier which is set by Voyado

- HTTP Method: `GET`
- Endpoint: `/api/v2/promotions/multichannels/{id}`

**Parameters**

| Name | Type | Required | Description                      |
| :--- | :--- | :------- | :------------------------------- |
| id\_ | str  | ✅       | Promotion identifier from Voyado |

**Return Type**

`MultichannelPromotionModel`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.promotions.multichannel_promotions_get_by_id(id_="id")

print(result)
```

## multichannel_promotions_update

Updates an existing multichannel promotion.
Only multichannel promotion in status 'Draft' can be updated.

- HTTP Method: `PUT`
- Endpoint: `/api/v2/promotions/multichannels/{id}`

**Parameters**

| Name         | Type                                                                  | Required | Description                              |
| :----------- | :-------------------------------------------------------------------- | :------- | :--------------------------------------- |
| request_body | [MultichannelPromotionModel](../models/MultichannelPromotionModel.md) | ✅       | The request body.                        |
| id\_         | str                                                                   | ✅       | Voyado multichannel promotion identifier |

**Return Type**

`MultichannelPromotionModel`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment
from voyado_engage.models import MultichannelPromotionModel

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = MultichannelPromotionModel(
    id_="00000000-0000-0000-0000-000000000000",
    status="Ended",
    external_id="externalId",
    name="name",
    validity={
        "start_date": "startDate",
        "end_date": "endDate",
        "assigned_validity": {
            "unit": "Months",
            "amount": 2103185352
        }
    },
    presentation={
        "heading": "heading",
        "description": "description",
        "link": "link"
    },
    redemption_channels=[
        {
            "type_": "POS",
            "value_type": "PERCENT",
            "value": "value",
            "local_values": [
                {}
            ],
            "instruction": "instruction"
        }
    ]
)

result = sdk.promotions.multichannel_promotions_update(
    request_body=request_body,
    id_="id"
)

print(result)
```

## multichannel_promotions_delete_by_id

Only unassigned multichannel promotions can be deleted

- HTTP Method: `DELETE`
- Endpoint: `/api/v2/promotions/multichannels/{id}`

**Parameters**

| Name | Type | Required | Description                                   |
| :--- | :--- | :------- | :-------------------------------------------- |
| id\_ | str  | ✅       | Voyado identifier to a multichannel promotion |

**Return Type**

`StatusCodeResult`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.promotions.multichannel_promotions_delete_by_id(id_="id")

print(result)
```

## multichannel_promotions_get_validity_by_id

Gets the multichannel promotion with the identifier which is an internal reference for Voyado

- HTTP Method: `GET`
- Endpoint: `/api/v2/promotions/multichannels/{id}/validity`

**Parameters**

| Name | Type | Required | Description                 |
| :--- | :--- | :------- | :-------------------------- |
| id\_ | str  | ✅       | Identifier inside of Voyado |

**Return Type**

`PromotionValidityModel`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.promotions.multichannel_promotions_get_validity_by_id(id_="id")

print(result)
```

## multichannel_promotions_update_validity

Updates duration of an existing multichannel promotion.
Only multichannel promotion in status 'Draft' can be updated.

- HTTP Method: `PUT`
- Endpoint: `/api/v2/promotions/multichannels/{id}/validity`

**Parameters**

| Name         | Type                                                          | Required | Description                              |
| :----------- | :------------------------------------------------------------ | :------- | :--------------------------------------- |
| request_body | [PromotionValidityModel](../models/PromotionValidityModel.md) | ✅       | The request body.                        |
| id\_         | str                                                           | ✅       | Voyado multichannel promotion identifier |

**Return Type**

`MultichannelPromotionModel`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment
from voyado_engage.models import PromotionValidityModel

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = PromotionValidityModel(
    start_date="startDate",
    end_date="endDate",
    assigned_validity={
        "unit": "Months",
        "amount": 2103185352
    }
)

result = sdk.promotions.multichannel_promotions_update_validity(
    request_body=request_body,
    id_="id"
)

print(result)
```

## multichannel_promotions_get_by_external_id

Gets the multichannel promotion with the identifier which is an external reference for Voyado

- HTTP Method: `GET`
- Endpoint: `/api/v2/promotions/multichannels`

**Parameters**

| Name        | Type | Required | Description                           |
| :---------- | :--- | :------- | :------------------------------------ |
| external_id | str  | ✅       | External identifier outside of Voyado |

**Return Type**

`MultichannelPromotionModel`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.promotions.multichannel_promotions_get_by_external_id(external_id="externalId")

print(result)
```

## multichannel_promotions_create

Only creates multichannel promotion in status 'Draft'.

- HTTP Method: `POST`
- Endpoint: `/api/v2/promotions/multichannels`

**Parameters**

| Name         | Type                                                                          | Required | Description       |
| :----------- | :---------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [MultichannelBasePromotionModel](../models/MultichannelBasePromotionModel.md) | ✅       | The request body. |

**Return Type**

`MultichannelPromotionModel`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment
from voyado_engage.models import MultichannelBasePromotionModel

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = MultichannelBasePromotionModel(
    external_id="externalId",
    name="name",
    validity={
        "start_date": "startDate",
        "end_date": "endDate",
        "assigned_validity": {
            "unit": "Months",
            "amount": 2103185352
        }
    },
    presentation={
        "heading": "heading",
        "description": "description",
        "link": "link"
    },
    redemption_channels=[
        {
            "type_": "POS",
            "value_type": "PERCENT",
            "value": "value",
            "local_values": [
                {}
            ],
            "instruction": "instruction"
        }
    ]
)

result = sdk.promotions.multichannel_promotions_create(request_body=request_body)

print(result)
```

## multichannel_promotions_delete_by_external_id

Only unassigned multichannel promotions can be deleted

- HTTP Method: `DELETE`
- Endpoint: `/api/v2/promotions/multichannels`

**Parameters**

| Name        | Type | Required | Description                                     |
| :---------- | :--- | :------- | :---------------------------------------------- |
| external_id | str  | ✅       | External identifier to a multichannel promotion |

**Return Type**

`StatusCodeResult`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.promotions.multichannel_promotions_delete_by_external_id(external_id="externalId")

print(result)
```

## multichannel_promotions_get_by_validity_external_id

Gets the multichannel promotion validity with the identifier which is an external reference for Voyado

- HTTP Method: `GET`
- Endpoint: `/api/v2/promotions/multichannels/validity`

**Parameters**

| Name        | Type | Required | Description                           |
| :---------- | :--- | :------- | :------------------------------------ |
| external_id | str  | ✅       | External identifier outside of Voyado |

**Return Type**

`PromotionValidityModel`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.promotions.multichannel_promotions_get_by_validity_external_id(external_id="externalId")

print(result)
```

## offer_promotions_redeem_by_promotion_id

Redeem a promotion (multichannel offer or mobile swipe) for a Contact using the internal promotion Id

Redemption channel can be POS, ECOM or OTHER.

- HTTP Method: `POST`
- Endpoint: `/api/v2/promotions/codes/{promotionId}/redeem`

**Parameters**

| Name         | Type                                            | Required | Description             |
| :----------- | :---------------------------------------------- | :------- | :---------------------- |
| request_body | [RedeemBodyModel](../models/RedeemBodyModel.md) | ✅       | The request body.       |
| promotion_id | str                                             | ✅       | The id of the promotion |

**Return Type**

`dict`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment
from voyado_engage.models import RedeemBodyModel

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = RedeemBodyModel(
    redemption_channel="redemptionChannel"
)

result = sdk.promotions.offer_promotions_redeem_by_promotion_id(
    request_body=request_body,
    promotion_id="promotionId"
)

print(result)
```

## offer_promotions_reactivate_promotion_code

Reactivate a redeemed reward voucher

- HTTP Method: `POST`
- Endpoint: `/api/v2/promotions/reward-vouchers/{id}/reactivate`

**Parameters**

| Name | Type | Required | Description                  |
| :--- | :--- | :------- | :--------------------------- |
| id\_ | str  | ✅       | The id of the reward voucher |

**Return Type**

`str`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.promotions.offer_promotions_reactivate_promotion_code(id_="id")

with open("output-file.ext", "w") as f:
    f.write(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
