# ContactsService

A list of all methods in the `ContactsService` service. Click on the method name to view detailed information about that method.

| Methods                               | Description                      |
| :------------------------------------ | :------------------------------- |
| [contacts_v_count](#contacts_v_count) | Get number of approved contacts. |

This is a cached value that will be updated with a
set frequency (normally once every 20 min). |
|[contacts_v_get_contact_by_id](#contacts_v_get_contact_by_id)| Get a single contact, using the unique identifier.

The dynamic fields of the response object depend on
the current instance configuration. |
|[contacts_v_update_contact_post](#contacts_v_update_contact_post)| Update one or several fields of a single contact.
Dont send an empty value unless you want it to be empty. |
|[contacts_v_delete_with_header_param](#contacts_v_delete_with_header_param)| |
|[contacts_v_count_by_contact_type](#contacts_v_count_by_contact_type)| Get number of approved contacts of given type.

This is a cached value that will be updated with a
set frequency (normally once every 20 min). |
|[contact_bulk_get_bulk_status](#contact_bulk_get_bulk_status)| |
|[contacts_v_get_contact_by_type_and_key_value_in_url_async](#contacts_v_get_contact_by_type_and_key_value_in_url_async)| ! Please be aware that this endpoint is currently usable with either the key value being provided through !
! the path or a query param. Hence there being two of the same endpoints. !
! We recommend that you use the query param version (the first) as it is the more versatile one of the two !

Get a single contact of a certain type, using a key
value that corresponds to the current instance configuration. This can
only be used for contact types with exactly ONE key.

The dynamic fields of the response object depend on
the current configuration. |
|[product_recommendation_get_product_recommendations](#product_recommendation_get_product_recommendations)| |
|[contact_retail_kpi_get_purchase_history](#contact_retail_kpi_get_purchase_history)| Following summary shows the purchase history for a single contact, over all time, 12 months and 24 months. |
|[back_in_stock_subscription_get_by_contact_id](#back_in_stock_subscription_get_by_contact_id)| Get back in stock subscriptions for a contact |
|[contacts_v_get_contact_by_external_id_async](#contacts_v_get_contact_by_external_id_async)| Get a single contact of a certain type, using the
contact's external id.

The dynamic fields of the response object depend on
the current configuration. |
|[contacts_v_get_contact_by_type_and_key_value_async](#contacts_v_get_contact_by_type_and_key_value_async)| Get a single contact of a certain type, using a key
value that corresponds to the current instance configuration. This can
only be used for contact types with exactly ONE key.

The dynamic fields of the response object depend on
the current configuration. |
|[contact_message_get_latest_messages_by_contact_id](#contact_message_get_latest_messages_by_contact_id)| Get the latest messages (max 500) a contact has received |
|[transactions_get_transactions_by_contact_id](#transactions_get_transactions_by_contact_id)| Get all purchase transactions for a single contact with
optional offset and number of transactions in response. |
|[bonus_point_transactions_get_bonus_point_transactions_for_contact](#bonus_point_transactions_get_bonus_point_transactions_for_contact)| |
|[contacts_v_get_changed_contact_ids](#contacts_v_get_changed_contact_ids)| |
|[offer_promotions_get_promotions_for_contact](#offer_promotions_get_promotions_for_contact)| Get available promotions for a contact. To filter on redemptionChannelType add it as a query string
?redemptionChannelType=POS
It can be POS, ECOM or OTHER |
|[contact_overview_get_contact_id_async](#contact_overview_get_contact_id_async)| Get the contactId for one (or several) contacts using either:

- email
- socialSecurityNumber
- mobilePhone
- customKey (the customKey must be configured by your supplier)
- any - the any field can contain email, socialSecurityNumber, mobilePhone or the custom key (and are checked in that order) |
  |[contacts_v_create_contact_header_param](#contacts_v_create_contact_header_param)| Create a new, approved contact.

If the contacts key identifier (example: Email) already exists : returns the GUID of the first entry found. |
|[contacts_v_promote_to_member](#contacts_v_promote_to_member)| Promote a contact to a member with one or several required fields. |
|[contact_bulk_create_contacts_in_bulk](#contact_bulk_create_contacts_in_bulk)| |
|[contact_bulk_update_contacts_in_bulk](#contact_bulk_update_contacts_in_bulk)| |
|[contact_preferences_accepts_sms](#contact_preferences_accepts_sms)| Update the preference that indicates whether or not
a contact accepts to be contacted via sms. This will also approve an unapproved contact.
The primary way of updating a contact preference is through the update contacts endpoint. |
|[bonus_point_transactions_adjust_reward_points](#bonus_point_transactions_adjust_reward_points)| Adds reward points to a contact. |
|[contact_preferences_accepts_email](#contact_preferences_accepts_email)| Update the preference that indicates whether or not
a contact accepts to be contacted via email. This will also approve an unapproved contact.
The primary way of updating a contact preference is through the update contacts endpoint. |
|[contact_preferences_accepts_postal](#contact_preferences_accepts_postal)| Update the preference that indicates whether or not
a contact accepts to be contacted via regular mail. This will also approve an unapproved contact.
The primary way of updating a contact preference is through the update contacts endpoint. |
|[assign_promotion_assign](#assign_promotion_assign)| Assign a promotion (multichannel offer only) to a Contact using the internal Contact Id
and the id of the promotion |
|[offer_promotions_redeem](#offer_promotions_redeem)| Redeem a promotion (multichannel offer or mobile swipe) for a Contact using the internal Contact Id

Redemption channel can be POS, ECOM or OTHER. |
|[contact_message_sms_unsubscribe_contact](#contact_message_sms_unsubscribe_contact)| Optional messageId input if user wants to unsubscribe on specific message instead of last sent Sms |
|[contact_message_email_unsubscribe_contact](#contact_message_email_unsubscribe_contact)| Optional messageId input if user wants to unsubscribe on specific message instead of last sent email |
|[contacts_v_update_contact_type](#contacts_v_update_contact_type)| Updates the contactType for a contact if all expected contact data is available |

## contacts_v_count

Get number of approved contacts.

This is a cached value that will be updated with a
set frequency (normally once every 20 min).

- HTTP Method: `GET`
- Endpoint: `/api/v2/contacts/count`

**Return Type**

`int`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.contacts.contacts_v_count()

print(result)
```

## contacts_v_get_contact_by_id

Get a single contact, using the unique identifier.

The dynamic fields of the response object depend on
the current instance configuration.

- HTTP Method: `GET`
- Endpoint: `/api/v2/contacts/{contactId}`

**Parameters**

| Name       | Type | Required | Description                |
| :--------- | :--- | :------- | :------------------------- |
| contact_id | str  | ✅       | Contact identifier (GUID). |

**Return Type**

`IApiContact`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.contacts.contacts_v_get_contact_by_id(contact_id="contactId")

print(result)
```

## contacts_v_update_contact_post

Update one or several fields of a single contact.
Dont send an empty value unless you want it to be empty.

- HTTP Method: `POST`
- Endpoint: `/api/v2/contacts/{contactId}`

**Parameters**

| Name         | Type | Required | Description                |
| :----------- | :--- | :------- | :------------------------- |
| request_body | any  | ✅       | The request body.          |
| contact_id   | str  | ✅       | Contact identifier (GUID). |

**Return Type**

`IApiContact`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment
from voyado_engage.models import any

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = ""

result = sdk.contacts.contacts_v_update_contact_post(
    request_body=request_body,
    contact_id="contactId"
)

print(result)
```

## contacts_v_delete_with_header_param

- HTTP Method: `DELETE`
- Endpoint: `/api/v2/contacts/{contactId}`

**Parameters**

| Name       | Type | Required | Description                                       |
| :--------- | :--- | :------- | :------------------------------------------------ |
| contact_id | str  | ✅       | Contact identifier (GUID).                        |
| source     | str  | ❌       | Source system identifier (instance configuration) |

**Return Type**

`dict`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.contacts.contacts_v_delete_with_header_param(
    contact_id="contactId",
    source="source"
)

print(result)
```

## contacts_v_count_by_contact_type

Get number of approved contacts of given type.

This is a cached value that will be updated with a
set frequency (normally once every 20 min).

- HTTP Method: `GET`
- Endpoint: `/api/v2/contacts/{contactType}/count`

**Parameters**

| Name         | Type | Required | Description                                     |
| :----------- | :--- | :------- | :---------------------------------------------- |
| contact_type | str  | ✅       | Id for contact type, e.g. "member" or "contact" |

**Return Type**

`int`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.contacts.contacts_v_count_by_contact_type(contact_type="contactType")

print(result)
```

## contact_bulk_get_bulk_status

- HTTP Method: `GET`
- Endpoint: `/api/v2/contacts/bulk/status`

**Parameters**

| Name     | Type | Required | Description                 |
| :------- | :--- | :------- | :-------------------------- |
| batch_id | str  | ✅       | Id from bulk contact import |

**Return Type**

`dict`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.contacts.contact_bulk_get_bulk_status(batch_id="batchId")

print(result)
```

## contacts_v_get_contact_by_type_and_key_value_in_url_async

! Please be aware that this endpoint is currently usable with either the key value being provided through !
! the path or a query param. Hence there being two of the same endpoints. !
! We recommend that you use the query param version (the first) as it is the more versatile one of the two !

Get a single contact of a certain type, using a key
value that corresponds to the current instance configuration. This can
only be used for contact types with exactly ONE key.

The dynamic fields of the response object depend on
the current configuration.

- HTTP Method: `GET`
- Endpoint: `/api/v2/contacts/{contactType}/bykey/{keyValue}`

**Parameters**

| Name         | Type | Required | Description                            |
| :----------- | :--- | :------- | :------------------------------------- |
| contact_type | str  | ✅       | Contact type, e.g. "member".           |
| key_value    | str  | ✅       | Key value, e.g. ssn, phone number etc. |

**Return Type**

`IApiContact`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.contacts.contacts_v_get_contact_by_type_and_key_value_in_url_async(
    contact_type="contactType",
    key_value="keyValue"
)

print(result)
```

## product_recommendation_get_product_recommendations

- HTTP Method: `GET`
- Endpoint: `/api/v2/contacts/{contactId}/productrecommendations`

**Parameters**

| Name       | Type | Required | Description                |
| :--------- | :--- | :------- | :------------------------- |
| contact_id | str  | ✅       | Contact identifier (GUID). |

**Return Type**

`ProductRecommendationsModel`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.contacts.product_recommendation_get_product_recommendations(contact_id="contactId")

print(result)
```

## contact_retail_kpi_get_purchase_history

Following summary shows the purchase history for a single contact, over all time, 12 months and 24 months.

- HTTP Method: `GET`
- Endpoint: `/api/v2/contacts/{contactId}/purchasehistorysummary`

**Parameters**

| Name       | Type | Required | Description               |
| :--------- | :--- | :------- | :------------------------ |
| contact_id | str  | ✅       | Contact identifier (GUID) |

**Return Type**

`PurchaseHistorySummary`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.contacts.contact_retail_kpi_get_purchase_history(contact_id="contactId")

print(result)
```

## back_in_stock_subscription_get_by_contact_id

Get back in stock subscriptions for a contact

- HTTP Method: `GET`
- Endpoint: `/api/v2/contacts/{contactId}/backinstock/subscriptions`

**Parameters**

| Name       | Type | Required | Description |
| :--------- | :--- | :------- | :---------- |
| contact_id | str  | ✅       |             |

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.contacts.back_in_stock_subscription_get_by_contact_id(contact_id="contactId")

print(result)
```

## contacts_v_get_contact_by_external_id_async

Get a single contact of a certain type, using the
contact's external id.

The dynamic fields of the response object depend on
the current configuration.

- HTTP Method: `GET`
- Endpoint: `/api/v2/contacts/{contactType}/byexternalid/{externalId}`

**Parameters**

| Name         | Type | Required | Description                           |
| :----------- | :--- | :------- | :------------------------------------ |
| contact_type | str  | ✅       | Contact type, e.g. Member or Contact. |
| external_id  | str  | ✅       | External contact id.                  |

**Return Type**

`IApiContact`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.contacts.contacts_v_get_contact_by_external_id_async(
    contact_type="contactType",
    external_id="externalId"
)

print(result)
```

## contacts_v_get_contact_by_type_and_key_value_async

Get a single contact of a certain type, using a key
value that corresponds to the current instance configuration. This can
only be used for contact types with exactly ONE key.

The dynamic fields of the response object depend on
the current configuration.

- HTTP Method: `GET`
- Endpoint: `/api/v2/contacts/{contactType}/bykey`

**Parameters**

| Name         | Type | Required | Description                            |
| :----------- | :--- | :------- | :------------------------------------- |
| contact_type | str  | ✅       | Contact type, e.g. "member".           |
| key_value    | str  | ✅       | Key value, e.g. ssn, phone number etc. |

**Return Type**

`IApiContact`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.contacts.contacts_v_get_contact_by_type_and_key_value_async(
    contact_type="contactType",
    key_value="keyValue"
)

print(result)
```

## contact_message_get_latest_messages_by_contact_id

Get the latest messages (max 500) a contact has received

- HTTP Method: `GET`
- Endpoint: `/api/v2/contacts/{contactId}/messages/latest`

**Parameters**

| Name       | Type | Required | Description                                                     |
| :--------- | :--- | :------- | :-------------------------------------------------------------- |
| contact_id | str  | ✅       | Contact identifier (GUID).                                      |
| count      | int  | ❌       | Max number of items to take. (Default value 100, Max value 500) |

**Return Type**

`ListResultOfApiMessage`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.contacts.contact_message_get_latest_messages_by_contact_id(
    contact_id="contactId",
    count=6
)

print(result)
```

## transactions_get_transactions_by_contact_id

Get all purchase transactions for a single contact with
optional offset and number of transactions in response.

- HTTP Method: `GET`
- Endpoint: `/api/v2/contacts/{contactId}/transactions`

**Parameters**

| Name       | Type | Required | Description                                      |
| :--------- | :--- | :------- | :----------------------------------------------- |
| contact_id | str  | ✅       | Contact identifier (GUID)                        |
| offset     | int  | ❌       | Number of items to skip. (Default value 0)       |
| count      | int  | ❌       | Max number of items to take. (Default value 100) |

**Return Type**

`PagedResultOfTransactionItem`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.contacts.transactions_get_transactions_by_contact_id(
    contact_id="contactId",
    offset=1,
    count=4
)

print(result)
```

## bonus_point_transactions_get_bonus_point_transactions_for_contact

- HTTP Method: `GET`
- Endpoint: `/api/v2/contacts/{contactId}/bonuspointtransactions`

**Parameters**

| Name       | Type | Required | Description                                              |
| :--------- | :--- | :------- | :------------------------------------------------------- |
| contact_id | str  | ✅       | The contact identifier (GUID).                           |
| offset     | int  | ❌       | The first item to retrieve. (Default value 0)            |
| count      | int  | ❌       | The max number of items to retrieve. (Default value 100) |

**Return Type**

`PagedResultOfBonusPointTransactionModel`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.contacts.bonus_point_transactions_get_bonus_point_transactions_for_contact(
    contact_id="contactId",
    offset=3,
    count=3
)

print(result)
```

## contacts_v_get_changed_contact_ids

- HTTP Method: `GET`
- Endpoint: `/api/v2/contacts/changes`

**Parameters**

| Name        | Type                                  | Required | Description                                         |
| :---------- | :------------------------------------ | :------- | :-------------------------------------------------- |
| change_type | [ChangeType](../models/ChangeType.md) | ✅       | Created, Updated or Deleted                         |
| from_date   | str                                   | ✅       | Start of timespan (ex 2023-05-04 11:20:00.000)      |
| to_date     | str                                   | ❌       | End of timespan (Default the current time and date) |

**Return Type**

`dict`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment
from voyado_engage.models import ChangeType

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.contacts.contacts_v_get_changed_contact_ids(
    change_type="Created",
    from_date="fromDate",
    to_date="toDate"
)

print(result)
```

## offer_promotions_get_promotions_for_contact

Get available promotions for a contact. To filter on redemptionChannelType add it as a query string
?redemptionChannelType=POS
It can be POS, ECOM or OTHER

- HTTP Method: `GET`
- Endpoint: `/api/v2/contacts/{contactId}/promotions`

**Parameters**

| Name                    | Type | Required | Description                                                  |
| :---------------------- | :--- | :------- | :----------------------------------------------------------- |
| contact_id              | str  | ✅       | Contact identifier                                           |
| redemption_channel_type | str  | ❌       | Filter on redemptionChannelType it can be POS, ECOM or OTHER |

**Return Type**

`List[ApiPromotionModel]`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.contacts.offer_promotions_get_promotions_for_contact(
    contact_id="contactId",
    redemption_channel_type="redemptionChannelType"
)

print(result)
```

## contact_overview_get_contact_id_async

Get the contactId for one (or several) contacts using either:

- email
- socialSecurityNumber
- mobilePhone
- customKey (the customKey must be configured by your supplier)
- any - the any field can contain email, socialSecurityNumber, mobilePhone or the custom key (and are checked in that order)

- HTTP Method: `GET`
- Endpoint: `/api/v2/contacts/id`

**Parameters**

| Name                   | Type | Required | Description |
| :--------------------- | :--- | :------- | :---------- |
| contact_type           | str  | ❌       |             |
| email                  | str  | ❌       |             |
| social_security_number | str  | ❌       |             |
| mobile_phone           | str  | ❌       |             |
| custom_key             | str  | ❌       |             |
| any                    | str  | ❌       |             |

**Return Type**

`str`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.contacts.contact_overview_get_contact_id_async(
    contact_type="contactType",
    email="email",
    social_security_number="socialSecurityNumber",
    mobile_phone="mobilePhone",
    custom_key="customKey",
    any="any"
)

with open("output-file.ext", "w") as f:
    f.write(result)
```

## contacts_v_create_contact_header_param

Create a new, approved contact.

If the contacts key identifier (example: Email) already exists : returns the GUID of the first entry found.

- HTTP Method: `POST`
- Endpoint: `/api/v2/contacts`

**Parameters**

| Name                 | Type | Required | Description                                                                                                                  |
| :------------------- | :--- | :------- | :--------------------------------------------------------------------------------------------------------------------------- |
| request_body         | any  | ✅       | The request body.                                                                                                            |
| source               | str  | ❌       | Source system identifier (instance configuration)                                                                            |
| store_external_id    | str  | ❌       | The unique id code of the current store (and therefore also the recruited-by store). Not mandatory but strongly recommended. |
| create_as_unapproved | str  | ❌       | Contact is not approved on creation. (Default value false)                                                                   |

**Return Type**

`IApiContact`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment
from voyado_engage.models import any

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = ""

result = sdk.contacts.contacts_v_create_contact_header_param(
    request_body=request_body,
    source="source",
    store_external_id="storeExternalId",
    create_as_unapproved="createAsUnapproved"
)

print(result)
```

## contacts_v_promote_to_member

Promote a contact to a member with one or several required fields.

- HTTP Method: `POST`
- Endpoint: `/api/v2/contacts/{contactId}/promoteToMember`

**Parameters**

| Name         | Type | Required | Description                                       |
| :----------- | :--- | :------- | :------------------------------------------------ |
| request_body | any  | ✅       | The request body.                                 |
| contact_id   | str  | ✅       | Contact identifier (GUID).                        |
| source       | str  | ❌       | Source system identifier (instance configuration) |

**Return Type**

`IApiContact`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment
from voyado_engage.models import any

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = ""

result = sdk.contacts.contacts_v_promote_to_member(
    request_body=request_body,
    contact_id="contactId",
    source="source"
)

print(result)
```

## contact_bulk_create_contacts_in_bulk

- HTTP Method: `POST`
- Endpoint: `/api/v2/contacts/bulk`

**Parameters**

| Name         | Type | Required | Description                                               |
| :----------- | :--- | :------- | :-------------------------------------------------------- |
| request_body | any  | ✅       | The request body.                                         |
| contact_type | str  | ❌       | Optional, if not set the default ContactType will be used |

**Return Type**

`str`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment
from voyado_engage.models import any

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = ""

result = sdk.contacts.contact_bulk_create_contacts_in_bulk(
    request_body=request_body,
    contact_type="contactType"
)

with open("output-file.ext", "w") as f:
    f.write(result)
```

## contact_bulk_update_contacts_in_bulk

- HTTP Method: `PATCH`
- Endpoint: `/api/v2/contacts/bulk`

**Parameters**

| Name                    | Type | Required | Description                                               |
| :---------------------- | :--- | :------- | :-------------------------------------------------------- |
| request_body            | any  | ✅       | The request body.                                         |
| contact_type            | str  | ❌       | Optional, if not set the default ContactType will be used |
| avoid_triggering_export | bool | ❌       | Optional, default value is false                          |

**Return Type**

`str`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment
from voyado_engage.models import any

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = ""

result = sdk.contacts.contact_bulk_update_contacts_in_bulk(
    request_body=request_body,
    contact_type="contactType",
    avoid_triggering_export=False
)

with open("output-file.ext", "w") as f:
    f.write(result)
```

## contact_preferences_accepts_sms

Update the preference that indicates whether or not
a contact accepts to be contacted via sms. This will also approve an unapproved contact.
The primary way of updating a contact preference is through the update contacts endpoint.

- HTTP Method: `POST`
- Endpoint: `/api/v2/contacts/{contactId}/preferences/acceptsSms`

**Parameters**

| Name         | Type                                    | Required | Description                |
| :----------- | :-------------------------------------- | :------- | :------------------------- |
| request_body | [BoolRequest](../models/BoolRequest.md) | ✅       | The request body.          |
| contact_id   | str                                     | ✅       | Contact identifier (GUID). |

**Return Type**

`IApiContact`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment
from voyado_engage.models import BoolRequest

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = BoolRequest(
    value=True
)

result = sdk.contacts.contact_preferences_accepts_sms(
    request_body=request_body,
    contact_id="contactId"
)

print(result)
```

## bonus_point_transactions_adjust_reward_points

Adds reward points to a contact.

- HTTP Method: `POST`
- Endpoint: `/api/v2/contacts/{contactId}/rewardpointtransaction`

**Parameters**

| Name         | Type                                                        | Required | Description                |
| :----------- | :---------------------------------------------------------- | :------- | :------------------------- |
| request_body | [ApiAdjustRewardPoints](../models/ApiAdjustRewardPoints.md) | ✅       | The request body.          |
| contact_id   | str                                                         | ✅       | Contact identifier (GUID). |

**Return Type**

`ApiAdjustRewardPointsResponse`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment
from voyado_engage.models import ApiAdjustRewardPoints

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = ApiAdjustRewardPoints(
    points=1.86,
    description="description",
    type_="type"
)

result = sdk.contacts.bonus_point_transactions_adjust_reward_points(
    request_body=request_body,
    contact_id="contactId"
)

print(result)
```

## contact_preferences_accepts_email

Update the preference that indicates whether or not
a contact accepts to be contacted via email. This will also approve an unapproved contact.
The primary way of updating a contact preference is through the update contacts endpoint.

- HTTP Method: `POST`
- Endpoint: `/api/v2/contacts/{contactId}/preferences/acceptsEmail`

**Parameters**

| Name         | Type                                    | Required | Description                |
| :----------- | :-------------------------------------- | :------- | :------------------------- |
| request_body | [BoolRequest](../models/BoolRequest.md) | ✅       | The request body.          |
| contact_id   | str                                     | ✅       | Contact identifier (GUID). |

**Return Type**

`IApiContact`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment
from voyado_engage.models import BoolRequest

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = BoolRequest(
    value=True
)

result = sdk.contacts.contact_preferences_accepts_email(
    request_body=request_body,
    contact_id="contactId"
)

print(result)
```

## contact_preferences_accepts_postal

Update the preference that indicates whether or not
a contact accepts to be contacted via regular mail. This will also approve an unapproved contact.
The primary way of updating a contact preference is through the update contacts endpoint.

- HTTP Method: `POST`
- Endpoint: `/api/v2/contacts/{contactId}/preferences/acceptsPostal`

**Parameters**

| Name         | Type                                    | Required | Description                |
| :----------- | :-------------------------------------- | :------- | :------------------------- |
| request_body | [BoolRequest](../models/BoolRequest.md) | ✅       | The request body.          |
| contact_id   | str                                     | ✅       | Contact identifier (GUID). |

**Return Type**

`IApiContact`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment
from voyado_engage.models import BoolRequest

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = BoolRequest(
    value=True
)

result = sdk.contacts.contact_preferences_accepts_postal(
    request_body=request_body,
    contact_id="contactId"
)

print(result)
```

## assign_promotion_assign

Assign a promotion (multichannel offer only) to a Contact using the internal Contact Id
and the id of the promotion

- HTTP Method: `POST`
- Endpoint: `/api/v2/contacts/{contactId}/promotions/{promotionId}/assign`

**Parameters**

| Name         | Type | Required | Description             |
| :----------- | :--- | :------- | :---------------------- |
| contact_id   | str  | ✅       | Contact identifier      |
| promotion_id | str  | ✅       | The id of the promotion |

**Return Type**

`dict`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.contacts.assign_promotion_assign(
    contact_id="contactId",
    promotion_id="promotionId"
)

print(result)
```

## offer_promotions_redeem

Redeem a promotion (multichannel offer or mobile swipe) for a Contact using the internal Contact Id

Redemption channel can be POS, ECOM or OTHER.

- HTTP Method: `POST`
- Endpoint: `/api/v2/contacts/{contactId}/promotions/{promotionId}/redeem`

**Parameters**

| Name         | Type                                            | Required | Description             |
| :----------- | :---------------------------------------------- | :------- | :---------------------- |
| request_body | [RedeemBodyModel](../models/RedeemBodyModel.md) | ✅       | The request body.       |
| contact_id   | str                                             | ✅       | Contact identifier      |
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

result = sdk.contacts.offer_promotions_redeem(
    request_body=request_body,
    contact_id="contactId",
    promotion_id="promotionId"
)

print(result)
```

## contact_message_sms_unsubscribe_contact

Optional messageId input if user wants to unsubscribe on specific message instead of last sent Sms

- HTTP Method: `POST`
- Endpoint: `/api/v2/contacts/{contactId}/unsubscribeSms`

**Parameters**

| Name       | Type | Required | Description                |
| :--------- | :--- | :------- | :------------------------- |
| contact_id | str  | ✅       | Contact identifier (GUID). |
| message_id | str  | ❌       | Message Id (string).       |

**Return Type**

`dict`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.contacts.contact_message_sms_unsubscribe_contact(
    contact_id="contactId",
    message_id="messageId"
)

print(result)
```

## contact_message_email_unsubscribe_contact

Optional messageId input if user wants to unsubscribe on specific message instead of last sent email

- HTTP Method: `POST`
- Endpoint: `/api/v2/contacts/{contactId}/unsubscribeEmail`

**Parameters**

| Name       | Type | Required | Description                |
| :--------- | :--- | :------- | :------------------------- |
| contact_id | str  | ✅       | Contact identifier (GUID). |
| message_id | str  | ❌       | Message Id (string).       |

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.contacts.contact_message_email_unsubscribe_contact(
    contact_id="contactId",
    message_id="messageId"
)

print(result)
```

## contacts_v_update_contact_type

Updates the contactType for a contact if all expected contact data is available

- HTTP Method: `POST`
- Endpoint: `/api/v2/contacts/{contactId}/updateContactType`

**Parameters**

| Name            | Type | Required | Description                  |
| :-------------- | :--- | :------- | :--------------------------- |
| contact_id      | str  | ✅       | Contact identifier (GUID).   |
| contact_type_id | str  | ✅       | The ContactType id (string). |

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.contacts.contacts_v_update_contact_type(
    contact_id="contactId",
    contact_type_id="contactTypeId"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
