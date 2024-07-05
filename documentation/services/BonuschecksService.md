# BonuschecksService

A list of all methods in the `BonuschecksService` service. Click on the method name to view detailed information about that method.

| Methods                                                                                 | Description                                                          |
| :-------------------------------------------------------------------------------------- | :------------------------------------------------------------------- |
| [bonus_checks_get_bonus_checks_for_contact](#bonus_checks_get_bonus_checks_for_contact) | Get all bonus checks for a contact. Expired, redeemed and available. |

The result can be paginated, using the offset and
count query parameters. |
|[bonus_checks_get_redeemed_bonus_checks_for_contact](#bonus_checks_get_redeemed_bonus_checks_for_contact)| Get redeemed bonus checks for a contact.
The result can be paginated, using the offset and
count query parameters. |
|[bonus_checks_get_available_bonus_checks](#bonus_checks_get_available_bonus_checks)| Get available bonus checks for a contact.

Expired and redeemed bonus checks are excluded

The result can be paginated, using the _offset_
and _count_ query parameters. |
|[bonus_checks_redeem_bonus_check](#bonus_checks_redeem_bonus_check)| Redeem a bonus check for a certain contact. |

## bonus_checks_get_bonus_checks_for_contact

Get all bonus checks for a contact. Expired, redeemed and available.
The result can be paginated, using the offset and
count query parameters.

- HTTP Method: `GET`
- Endpoint: `/api/v2/contacts/{contactId}/bonuschecks`

**Parameters**

| Name       | Type | Required | Description                                              |
| :--------- | :--- | :------- | :------------------------------------------------------- |
| contact_id | str  | ✅       | Contact identifier (GUID).                               |
| offset     | int  | ❌       | The first item to retrieve. (Default value 0)            |
| count      | int  | ❌       | The max number of items to retrieve. (Default value 100) |

**Return Type**

`PagedResultOfAllBonusCheckModel`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.bonuschecks.bonus_checks_get_bonus_checks_for_contact(
    contact_id="contactId",
    offset=3,
    count=6
)

print(result)
```

## bonus_checks_get_redeemed_bonus_checks_for_contact

Get redeemed bonus checks for a contact.
The result can be paginated, using the offset and
count query parameters.

- HTTP Method: `GET`
- Endpoint: `/api/v2/contacts/{contactId}/bonuschecks/redeemed`

**Parameters**

| Name       | Type | Required | Description                                              |
| :--------- | :--- | :------- | :------------------------------------------------------- |
| contact_id | str  | ✅       | Contact identifier (GUID).                               |
| offset     | int  | ❌       | The first item to retrieve. (Default value 0)            |
| count      | int  | ❌       | The max number of items to retrieve. (Default value 100) |

**Return Type**

`PagedResultOfRedeemedBonusCheckModel`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.bonuschecks.bonus_checks_get_redeemed_bonus_checks_for_contact(
    contact_id="contactId",
    offset=3,
    count=8
)

print(result)
```

## bonus_checks_get_available_bonus_checks

Get available bonus checks for a contact.

Expired and redeemed bonus checks are excluded

The result can be paginated, using the _offset_
and _count_ query parameters.

- HTTP Method: `GET`
- Endpoint: `/api/v2/contacts/{contactId}/bonuschecks/available`

**Parameters**

| Name       | Type | Required | Description                                      |
| :--------- | :--- | :------- | :----------------------------------------------- |
| contact_id | str  | ✅       | Contact identifier (GUID).                       |
| offset     | int  | ❌       | Number of items to skip. (Default value 0)       |
| count      | int  | ❌       | Max number of items to take. (Default value 100) |

**Return Type**

`PagedResultOfAvailableBonusCheckModel`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.bonuschecks.bonus_checks_get_available_bonus_checks(
    contact_id="contactId",
    offset=5,
    count=9
)

print(result)
```

## bonus_checks_redeem_bonus_check

Redeem a bonus check for a certain contact.

- HTTP Method: `POST`
- Endpoint: `/api/v2/contacts/{contactId}/bonuschecks/{bonusCheckId}/redeem`

**Parameters**

| Name           | Type | Required | Description                |
| :------------- | :--- | :------- | :------------------------- |
| contact_id     | str  | ✅       | Contact identifier (GUID). |
| bonus_check_id | str  | ✅       | Bonus check identifier.    |

**Return Type**

`RedeemedBonusCheckModel`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.bonuschecks.bonus_checks_redeem_bonus_check(
    contact_id="contactId",
    bonus_check_id="bonusCheckId"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
