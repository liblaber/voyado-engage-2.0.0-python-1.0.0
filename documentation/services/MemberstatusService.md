# MemberstatusService

A list of all methods in the `MemberstatusService` service. Click on the method name to view detailed information about that method.

| Methods                                     | Description                                         |
| :------------------------------------------ | :-------------------------------------------------- |
| [member_status_v_get](#member_status_v_get) | Gets the first found member that matches the query. |

Operation to get member overview. Is usually called from
POS after a member gives some identification information
this method returns the status together with contactId (GUID)
and memberNumber (if available). The contactId may be used
to get detailed contact information.

Common identification fields that may be used in the query:
socialSecurityNumber, email, mobilePhone, memberNumber and externalId

The language of the returned answer is controlled by the language setting of the user connected to the API-key. |

## member_status_v_get

Gets the first found member that matches the query.

Operation to get member overview. Is usually called from
POS after a member gives some identification information
this method returns the status together with contactId (GUID)
and memberNumber (if available). The contactId may be used
to get detailed contact information.

Common identification fields that may be used in the query:
socialSecurityNumber, email, mobilePhone, memberNumber and externalId

The language of the returned answer is controlled by the language setting of the user connected to the API-key.

- HTTP Method: `GET`
- Endpoint: `/api/v2/memberstatus`

**Parameters**

| Name  | Type | Required | Description                                 |
| :---- | :--- | :------- | :------------------------------------------ |
| query | str  | ✅       | ```{fieldId}:{value}```, e.g. email:test@test.com |

**Return Type**

`MemberStatusModel`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.memberstatus.member_status_v_get(query="query")

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
