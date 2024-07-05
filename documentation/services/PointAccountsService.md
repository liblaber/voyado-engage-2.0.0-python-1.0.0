# PointAccountsService

A list of all methods in the `PointAccountsService` service. Click on the method name to view detailed information about that method.

| Methods                                                             | Description                                                |
| :------------------------------------------------------------------ | :--------------------------------------------------------- |
| [point_account_point_account_get](#point_account_point_account_get) | Get the point account by point account id                  |
| [point_account_point_definition](#point_account_point_definition)   | ## Gets a point account matched with the pointDefinitionId |

Gets the name, id and description for each pointDefinition |
|[point_account_point_transactions](#point_account_point_transactions)| |
|[point_account_point_definitions](#point_account_point_definitions)| ## Gets point definitions |
|[point_account_point_account_get2](#point_account_point_account_get2)| Gets a list of accounts by contact id |
|[point_account_point_transactions2](#point_account_point_transactions2)| There are two ways to fetch the list of transactions:

- Using just the accountId returns the transactions for that particular points account. If this is used, the parameters contactId and definitionId are not required. If they are given, they will just be ignored.
- The other way is to specify both contactId and definitionId. Both must be given.

The optional parameters offset and count can be used in both cases to paginate the results.
The optional parameter filter can also be used to fetch active points, pending points or both.
All parameters are added to the query string. |
|[point_account_add_point_transactions](#point_account_add_point_transactions)| ## Point transactions being sent to a contacts specified point account, the endpoint will able to take max 1000 transaction rows.

### The following fields should be provided and have certain rules:

- contactId: Must be a Guid
- amount: The amount of points, negative amounts are accepted.
- definitionId: specifies to which point account each transaction should be sent to
- timeStamp: If not provided then the default value is taken from the requestors system timezone.
- source: Must be provided or else that specified transaction will not be accepted.
- description: Must be provided or else that transaction will not be accepted.
- validFrom: If not provided then the default value is taken from the requestors system timezone.
- validTo: Specifies how long the points are valid

### Important info:

If some rows are not correct it will still result in an accepted response code and be skipped. Please
check the response for NotAccepted items

### Idempotency-Key:

The idempotency key is a unique identifier included in the header of an HTTP request to ensure the idempotence of certain operations. An idempotent operation is one that produces the same result regardless of how many times it is executed with the same input.

#### Purpose

The primary purpose of the idempotency key is to enable safe retries of requests. In situations where a client needs to resend a request due to network issues or other transient failures, the idempotency key helps prevent unintended side effects by ensuring that repeated requests with the same key result in the same outcome. |

## point_account_point_account_get

Get the point account by point account id

- HTTP Method: `GET`
- Endpoint: `/api/v2/point-accounts/{id}`

**Parameters**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| id\_ | int  | ✅       | Account id  |

**Return Type**

`PointAccountModel`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.point_accounts.point_account_point_account_get(id_=5)

print(result)
```

## point_account_point_definition

## Gets a point account matched with the pointDefinitionId

Gets the name, id and description for each pointDefinition

- HTTP Method: `GET`
- Endpoint: `/api/v2/point-accounts/definitions/{id}`

**Parameters**

| Name | Type | Required | Description   |
| :--- | :--- | :------- | :------------ |
| id\_ | int  | ✅       | Definition Id |

**Return Type**

`PointDefinitionModel`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.point_accounts.point_account_point_definition(id_=5)

print(result)
```

## point_account_point_transactions

- HTTP Method: `GET`
- Endpoint: `/api/v2/point-accounts/transactions/{id}`

**Parameters**

| Name | Type | Required | Description    |
| :--- | :--- | :------- | :------------- |
| id\_ | int  | ✅       | Transaction id |

**Return Type**

`PointTransactionModel`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.point_accounts.point_account_point_transactions(id_=7)

print(result)
```

## point_account_point_definitions

## Gets point definitions

- HTTP Method: `GET`
- Endpoint: `/api/v2/point-accounts/definitions`

**Parameters**

| Name   | Type | Required | Description     |
| :----- | :--- | :------- | :-------------- |
| offset | int  | ❌       | Defaults to 0   |
| count  | int  | ❌       | Defaults to 100 |

**Return Type**

`List[PointDefinitionModel]`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.point_accounts.point_account_point_definitions(
    offset=8,
    count=3
)

print(result)
```

## point_account_point_account_get2

Gets a list of accounts by contact id

- HTTP Method: `GET`
- Endpoint: `/api/v2/point-accounts`

**Parameters**

| Name       | Type | Required | Description     |
| :--------- | :--- | :------- | :-------------- |
| contact_id | str  | ✅       | Contact id      |
| offset     | int  | ❌       | Defaults to 0   |
| count      | int  | ❌       | Defaults to 100 |

**Return Type**

`PointAccountModelsResult`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.point_accounts.point_account_point_account_get2(
    contact_id="contactId",
    offset=9,
    count=10
)

print(result)
```

## point_account_point_transactions2

There are two ways to fetch the list of transactions:

- Using just the accountId returns the transactions for that particular points account. If this is used, the parameters contactId and definitionId are not required. If they are given, they will just be ignored.
- The other way is to specify both contactId and definitionId. Both must be given.

The optional parameters offset and count can be used in both cases to paginate the results.
The optional parameter filter can also be used to fetch active points, pending points or both.
All parameters are added to the query string.

- HTTP Method: `GET`
- Endpoint: `/api/v2/point-accounts/transactions`

**Parameters**

| Name          | Type                                                                                      | Required | Description                                                              |
| :------------ | :---------------------------------------------------------------------------------------- | :------- | :----------------------------------------------------------------------- |
| contact_id    | str                                                                                       | ❌       | Contact id - Required together with definitionId if not using account id |
| definition_id | int                                                                                       | ❌       | Definition id - Required together with contactId if not using account id |
| account_id    | int                                                                                       | ❌       | Account id - Required if contactId and definitionId is not provided      |
| offset        | int                                                                                       | ❌       | Defaults to 0                                                            |
| count         | int                                                                                       | ❌       | Defaults to 100                                                          |
| filter        | [PointAccountPointTransactions2Filter](../models/PointAccountPointTransactions2Filter.md) | ❌       | All, Active or Pending. If not specified it will default to All.         |

**Return Type**

`PointTransactionModelsResult`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment
from voyado_engage.models import PointAccountPointTransactions2Filter

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.point_accounts.point_account_point_transactions2(
    contact_id="contactId",
    definition_id=5,
    account_id=5,
    offset=8,
    count=8,
    filter="All"
)

print(result)
```

## point_account_add_point_transactions

## Point transactions being sent to a contacts specified point account, the endpoint will able to take max 1000 transaction rows.

### The following fields should be provided and have certain rules:

- contactId: Must be a Guid
- amount: The amount of points, negative amounts are accepted.
- definitionId: specifies to which point account each transaction should be sent to
- timeStamp: If not provided then the default value is taken from the requestors system timezone.
- source: Must be provided or else that specified transaction will not be accepted.
- description: Must be provided or else that transaction will not be accepted.
- validFrom: If not provided then the default value is taken from the requestors system timezone.
- validTo: Specifies how long the points are valid

### Important info:

If some rows are not correct it will still result in an accepted response code and be skipped. Please
check the response for NotAccepted items

### Idempotency-Key:

The idempotency key is a unique identifier included in the header of an HTTP request to ensure the idempotence of certain operations. An idempotent operation is one that produces the same result regardless of how many times it is executed with the same input.

#### Purpose

The primary purpose of the idempotency key is to enable safe retries of requests. In situations where a client needs to resend a request due to network issues or other transient failures, the idempotency key helps prevent unintended side effects by ensuring that repeated requests with the same key result in the same outcome.

- HTTP Method: `POST`
- Endpoint: `/api/v2/point-accounts/transactions`

**Parameters**

| Name            | Type                                                                      | Required | Description                  |
| :-------------- | :------------------------------------------------------------------------ | :------- | :--------------------------- |
| request_body    | [List[PointTransactionToAccount]](../models/PointTransactionToAccount.md) | ✅       | The request body.            |
| idempotency_key | str                                                                       | ❌       | Optional, lasts for 24 hours |

**Return Type**

`PointTransactionToAccountResultModel`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = [
    {
        "contact_id": "00000000-0000-0000-0000-000000000000",
        "amount": 4.07,
        "definition_id": 3,
        "time_stamp": "timeStamp",
        "source": "source",
        "description": "description",
        "valid_from": "validFrom",
        "valid_to": "validTo"
    }
]

result = sdk.point_accounts.point_account_add_point_transactions(
    request_body=request_body,
    idempotency_key="Idempotency-Key"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
