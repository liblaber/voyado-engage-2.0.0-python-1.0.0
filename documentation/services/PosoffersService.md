# PosoffersService

A list of all methods in the `PosoffersService` service. Click on the method name to view detailed information about that method.

| Methods                                                                     | Description                                                        |
| :-------------------------------------------------------------------------- | :----------------------------------------------------------------- |
| [pos_offer_get_all_pos_offers_by_key](#pos_offer_get_all_pos_offers_by_key) | Get all POS offers for a contact. Expired, redeemed and available. |

Finds the contact by using a key value other than Contact Id. This can
only be used for contact types with exactly ONE key.
The contact key attribute is configured for each Voyado instance. |
|[pos_offer_get_available_pos_offers_by_key](#pos_offer_get_available_pos_offers_by_key)| Get all available POS offers for a contact.
Expired and redeemed offers are excluded.

Finds the contact by using a key value other than Contact Id. This can
only be used for contact types with exactly ONE key.
The contact key attribute is configured for each Voyado instance. |
|[pos_offer_get_all_pos_offers_by_contact_type_and_key](#pos_offer_get_all_pos_offers_by_contact_type_and_key)| Get all POS offers for a contact. Expired, redeemed and available.

Finds the contact by using a key value other than Contact Id. This can
only be used for contact types with exactly ONE key.
The contact key attribute is configured for each Voyado instance. |
|[pos_offer_get_available_pos_offers_by_contact_type_and_key](#pos_offer_get_available_pos_offers_by_contact_type_and_key)| Get all available POS offers for a contact.
Expired and redeemed offers are excluded.

Finds the contact by using a key value other than Contact Id. This can
only be used for contact types with exactly ONE key.
The contact key attribute is configured for each Voyado instance. |
|[pos_offer_get_all_pos_offers_for_contact](#pos_offer_get_all_pos_offers_for_contact)| Get all POS offers for a contact. Expired, redeemed and available.
The result can be paginated, using the offset and
count query parameters.
Note: _expiresOn_ is obsolete and is always **null** |
|[pos_offer_get_available_pos_offers_for_contact](#pos_offer_get_available_pos_offers_for_contact)| Get all available POS offers for a contact.
Expired and redeemed offers are excluded.

The result can be paginated, using the offset and
count query parameters. |
|[pos_offer_redeem](#pos_offer_redeem)| Redeems a POS offer for a Contact using the internal Contact Id |
|[pos_offer_redeem_by_key](#pos_offer_redeem_by_key)| Redeems a POS offer for a Contact using the key for the contact type

Finds the contact by using a key value other than Contact Id. This can
only be used for contact types with exactly ONE key.
The contact key attribute is configured for each Voyado instance. |
|[pos_offer_redeem_by_contact_type_and_key](#pos_offer_redeem_by_contact_type_and_key)| Redeems a POS offer for a Contact using the key for the contact type

Finds the contact by using a key value other than Contact Id. This can
only be used for contact types with exactly ONE key.
The contact key attribute is configured for each Voyado instance. |

## pos_offer_get_all_pos_offers_by_key

Get all POS offers for a contact. Expired, redeemed and available.

Finds the contact by using a key value other than Contact Id. This can
only be used for contact types with exactly ONE key.
The contact key attribute is configured for each Voyado instance.

- HTTP Method: `GET`
- Endpoint: `/api/v2/contacts/bykey/{keyValue}/posoffers/all`

**Parameters**

| Name      | Type | Required | Description                                                      |
| :-------- | :--- | :------- | :--------------------------------------------------------------- |
| key_value | str  | ✅       | Key value, e.g. ssn, externalId, memberNumber, phone number etc. |

**Return Type**

`PagedResultOfAllLoyaltyBarClaimModel`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.posoffers.pos_offer_get_all_pos_offers_by_key(key_value="keyValue")

print(result)
```

## pos_offer_get_available_pos_offers_by_key

Get all available POS offers for a contact.
Expired and redeemed offers are excluded.

Finds the contact by using a key value other than Contact Id. This can
only be used for contact types with exactly ONE key.
The contact key attribute is configured for each Voyado instance.

- HTTP Method: `GET`
- Endpoint: `/api/v2/contacts/bykey/{keyValue}/posoffers/available`

**Parameters**

| Name      | Type | Required | Description                                                      |
| :-------- | :--- | :------- | :--------------------------------------------------------------- |
| key_value | str  | ✅       | Key value, e.g. ssn, externalId, memberNumber, phone number etc. |

**Return Type**

`PagedResultOfAvailableLoyaltyBarClaimModel`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.posoffers.pos_offer_get_available_pos_offers_by_key(key_value="keyValue")

print(result)
```

## pos_offer_get_all_pos_offers_by_contact_type_and_key

Get all POS offers for a contact. Expired, redeemed and available.

Finds the contact by using a key value other than Contact Id. This can
only be used for contact types with exactly ONE key.
The contact key attribute is configured for each Voyado instance.

- HTTP Method: `GET`
- Endpoint: `/api/v2/contacts/{contactType}/bykey/{keyValue}/posoffers/all`

**Parameters**

| Name         | Type | Required | Description                                                      |
| :----------- | :--- | :------- | :--------------------------------------------------------------- |
| key_value    | str  | ✅       | Key value, e.g. ssn, externalId, memberNumber, phone number etc. |
| contact_type | str  | ✅       | Contact type, e.g. "member".                                     |

**Return Type**

`PagedResultOfAllLoyaltyBarClaimModel`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.posoffers.pos_offer_get_all_pos_offers_by_contact_type_and_key(
    key_value="keyValue",
    contact_type="contactType"
)

print(result)
```

## pos_offer_get_available_pos_offers_by_contact_type_and_key

Get all available POS offers for a contact.
Expired and redeemed offers are excluded.

Finds the contact by using a key value other than Contact Id. This can
only be used for contact types with exactly ONE key.
The contact key attribute is configured for each Voyado instance.

- HTTP Method: `GET`
- Endpoint: `/api/v2/contacts/{contactType}/bykey/{keyValue}/posoffers/available`

**Parameters**

| Name         | Type | Required | Description                                                      |
| :----------- | :--- | :------- | :--------------------------------------------------------------- |
| key_value    | str  | ✅       | Key value, e.g. ssn, externalId, memberNumber, phone number etc. |
| contact_type | str  | ✅       | Contact type, e.g. "member".                                     |

**Return Type**

`PagedResultOfAvailableLoyaltyBarClaimModel`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.posoffers.pos_offer_get_available_pos_offers_by_contact_type_and_key(
    key_value="keyValue",
    contact_type="contactType"
)

print(result)
```

## pos_offer_get_all_pos_offers_for_contact

Get all POS offers for a contact. Expired, redeemed and available.
The result can be paginated, using the offset and
count query parameters.
Note: _expiresOn_ is obsolete and is always **null**

- HTTP Method: `GET`
- Endpoint: `/api/v2/contacts/{contactId}/posoffers/all`

**Parameters**

| Name       | Type | Required | Description                                              |
| :--------- | :--- | :------- | :------------------------------------------------------- |
| contact_id | str  | ✅       | Contact identifier (GUID).                               |
| offset     | int  | ❌       | The first item to retrieve. (Default value 0)            |
| count      | int  | ❌       | The max number of items to retrieve. (Default value 100) |

**Return Type**

`PagedResultOfAllLoyaltyBarClaimModel`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.posoffers.pos_offer_get_all_pos_offers_for_contact(
    contact_id="contactId",
    offset=2,
    count=7
)

print(result)
```

## pos_offer_get_available_pos_offers_for_contact

Get all available POS offers for a contact.
Expired and redeemed offers are excluded.

The result can be paginated, using the offset and
count query parameters.

- HTTP Method: `GET`
- Endpoint: `/api/v2/contacts/{contactId}/posoffers/available`

**Parameters**

| Name       | Type | Required | Description                                              |
| :--------- | :--- | :------- | :------------------------------------------------------- |
| contact_id | str  | ✅       | Contact identifier (GUID).                               |
| offset     | int  | ❌       | The first item to retrieve. (Default value 0)            |
| count      | int  | ❌       | The max number of items to retrieve. (Default value 100) |

**Return Type**

`PagedResultOfAvailableLoyaltyBarClaimModel`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.posoffers.pos_offer_get_available_pos_offers_for_contact(
    contact_id="contactId",
    offset=3,
    count=0
)

print(result)
```

## pos_offer_redeem

Redeems a POS offer for a Contact using the internal Contact Id

- HTTP Method: `POST`
- Endpoint: `/api/v2/contacts/{contactId}/posoffers/{id}/redeem`

**Parameters**

| Name       | Type | Required | Description                                   |
| :--------- | :--- | :------- | :-------------------------------------------- |
| id\_       | str  | ✅       | The id returned from the get operation (GUID) |
| contact_id | str  | ✅       | Contact identifier (GUID).                    |

**Return Type**

`RedeemedLoyaltyBarClaimModel`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.posoffers.pos_offer_redeem(
    id_="id",
    contact_id="contactId"
)

print(result)
```

## pos_offer_redeem_by_key

Redeems a POS offer for a Contact using the key for the contact type

Finds the contact by using a key value other than Contact Id. This can
only be used for contact types with exactly ONE key.
The contact key attribute is configured for each Voyado instance.

- HTTP Method: `POST`
- Endpoint: `/api/v2/contacts/bykey/{keyValue}/posoffers/{id}/redeem`

**Parameters**

| Name      | Type | Required | Description                                                      |
| :-------- | :--- | :------- | :--------------------------------------------------------------- |
| id\_      | str  | ✅       | The id returned from the get operation (GUID)                    |
| key_value | str  | ✅       | Key value, e.g. ssn, externalId, memberNumber, phone number etc. |

**Return Type**

`RedeemedLoyaltyBarClaimModel`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.posoffers.pos_offer_redeem_by_key(
    id_="id",
    key_value="keyValue"
)

print(result)
```

## pos_offer_redeem_by_contact_type_and_key

Redeems a POS offer for a Contact using the key for the contact type

Finds the contact by using a key value other than Contact Id. This can
only be used for contact types with exactly ONE key.
The contact key attribute is configured for each Voyado instance.

- HTTP Method: `POST`
- Endpoint: `/api/v2/contacts/{contactType}/bykey/{keyValue}/posoffers/{id}/redeem`

**Parameters**

| Name         | Type | Required | Description                                                      |
| :----------- | :--- | :------- | :--------------------------------------------------------------- |
| id\_         | str  | ✅       | The id returned from the get operation (GUID)                    |
| key_value    | str  | ✅       | Key value, e.g. ssn, externalId, memberNumber, phone number etc. |
| contact_type | str  | ✅       | Contact type, e.g. "member" or "contact".                        |

**Return Type**

`RedeemedLoyaltyBarClaimModel`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.posoffers.pos_offer_redeem_by_contact_type_and_key(
    id_="id",
    key_value="keyValue",
    contact_type="contactType"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
