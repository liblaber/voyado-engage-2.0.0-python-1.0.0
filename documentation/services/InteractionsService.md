# InteractionsService

A list of all methods in the `InteractionsService` service. Click on the method name to view detailed information about that method.

| Methods                                                                                                                                                | Description                                                                                                                     |
| :----------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------ |
| [interaction_get_interaction](#interaction_get_interaction)                                                                                            | Retrieve a specific Interaction by providing the interactionId.                                                                 |
| [interaction_delete_interaction](#interaction_delete_interaction)                                                                                      | Delete a specific Interaction by providing the interactionId.                                                                   |
| [interaction_get_interactions](#interaction_get_interactions)                                                                                          | Retrieve multiple Interactions of a specified type connected to a specific contactId. Both schemaId and contactId are required. |
| The continuation parameter can be used to access the next page when there are more than 50 records available. This token can be found in the response. |
| [interaction_create_interaction](#interaction_create_interaction)                                                                                      | Create a new Interaction connected to a specific contactId.                                                                     |

## interaction_get_interaction

Retrieve a specific Interaction by providing the interactionId.

- HTTP Method: `GET`
- Endpoint: `/api/v2/interactions/{interactionId}`

**Parameters**

| Name           | Type | Required | Description |
| :------------- | :--- | :------- | :---------- |
| interaction_id | str  | ✅       |             |

**Return Type**

`InteractionModel`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.interactions.interaction_get_interaction(interaction_id="interactionId")

print(result)
```

## interaction_delete_interaction

Delete a specific Interaction by providing the interactionId.

- HTTP Method: `DELETE`
- Endpoint: `/api/v2/interactions/{interactionId}`

**Parameters**

| Name           | Type | Required | Description |
| :------------- | :--- | :------- | :---------- |
| interaction_id | str  | ✅       |             |

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.interactions.interaction_delete_interaction(interaction_id="interactionId")

print(result)
```

## interaction_get_interactions

Retrieve multiple Interactions of a specified type connected to a specific contactId. Both schemaId and contactId are required.
The continuation parameter can be used to access the next page when there are more than 50 records available. This token can be found in the response.

- HTTP Method: `GET`
- Endpoint: `/api/v2/interactions`

**Parameters**

| Name         | Type | Required | Description |
| :----------- | :--- | :------- | :---------- |
| contact_id   | str  | ✅       |             |
| schema_id    | str  | ✅       |             |
| continuation | str  | ❌       |             |

**Return Type**

`InteractionPage`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.interactions.interaction_get_interactions(
    contact_id="contactId",
    schema_id="schemaId",
    continuation="continuation"
)

print(result)
```

## interaction_create_interaction

Create a new Interaction connected to a specific contactId.

- HTTP Method: `POST`
- Endpoint: `/api/v2/interactions`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | any  | ✅       | The request body. |

**Return Type**

`InteractionCreateResponse`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment
from voyado_engage.models import any

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = ""

result = sdk.interactions.interaction_create_interaction(request_body=request_body)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
