# ChallengesService

A list of all methods in the `ChallengesService` service. Click on the method name to view detailed information about that method.

| Methods                                                                               | Description                                                                                |
| :------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------------- |
| [challenge_get_challenge_by_id](#challenge_get_challenge_by_id)                       | Get an challenge assignment by id.                                                         |
| [challenge_get_challenge_definition_by_id](#challenge_get_challenge_definition_by_id) | Get a challenge definition by id.                                                          |
| [challenge_get_challenge_definitions](#challenge_get_challenge_definitions)           | Get a list of all the challenge definitions.                                               |
| [challenge_get_challenges](#challenge_get_challenges)                                 | Search for challenges for a contact.                                                       |
| [challenge_add_challenge_check_points](#challenge_add_challenge_check_points)         | Send in a list of checkpoints to be assigned to a some challenge for a number of contacts, |

the endpoint will able to take max 1000 checkpoint rows.

### The following fields should be provided:

- definitionId: Must be a Guid
- contactId: Must be a Guid
- checkPointAmount: Number of checkpoints to assign to the challenge

### Important info:

If some rows are not correct it will still result in an accepted response code and be skipped. Please
check the response for NotAccepted items |
|[challenge_consent](#challenge_consent)| Will assign the challenge for the contact and return true. If the contact already
has been assigned for the challenge it will also return true. |

## challenge_get_challenge_by_id

Get an challenge assignment by id.

- HTTP Method: `GET`
- Endpoint: `/api/v2/challenges/{id}`

**Parameters**

| Name | Type | Required | Description   |
| :--- | :--- | :------- | :------------ |
| id\_ | str  | ✅       | Assignment id |

**Return Type**

`ChallengeAssignmentModel`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.challenges.challenge_get_challenge_by_id(id_="id")

print(result)
```

## challenge_get_challenge_definition_by_id

Get a challenge definition by id.

- HTTP Method: `GET`
- Endpoint: `/api/v2/challenges/definitions/{id}`

**Parameters**

| Name | Type | Required | Description   |
| :--- | :--- | :------- | :------------ |
| id\_ | str  | ✅       | Definition id |

**Return Type**

`ChallengeDefinitionModel`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.challenges.challenge_get_challenge_definition_by_id(id_="id")

print(result)
```

## challenge_get_challenge_definitions

Get a list of all the challenge definitions.

- HTTP Method: `GET`
- Endpoint: `/api/v2/challenges/definitions`

**Parameters**

| Name   | Type                                                                                          | Required | Description                                                          |
| :----- | :-------------------------------------------------------------------------------------------- | :------- | :------------------------------------------------------------------- |
| offset | int                                                                                           | ❌       | Defaults to 0                                                        |
| count  | int                                                                                           | ❌       | Defaults to 100                                                      |
| status | [ChallengeGetChallengeDefinitionsStatus](../models/ChallengeGetChallengeDefinitionsStatus.md) | ❌       | All, Active, Draft or Ended. If not specified it will default to All |

**Return Type**

`ChallengeDefinitionModelsResult`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment
from voyado_engage.models import ChallengeGetChallengeDefinitionsStatus

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.challenges.challenge_get_challenge_definitions(
    offset=2,
    count=1,
    status="All"
)

print(result)
```

## challenge_get_challenges

Search for challenges for a contact.

- HTTP Method: `GET`
- Endpoint: `/api/v2/challenges`

**Parameters**

| Name          | Type                                                                      | Required | Description                                                                     |
| :------------ | :------------------------------------------------------------------------ | :------- | :------------------------------------------------------------------------------ |
| contact_id    | str                                                                       | ✅       | Contact id                                                                      |
| definition_id | str                                                                       | ❌       | Definition id - Optional to limit to a certain challenge definition             |
| offset        | int                                                                       | ❌       | Defaults to 0                                                                   |
| count         | int                                                                       | ❌       | Defaults to 100                                                                 |
| filter        | [ChallengeGetChallengesFilter](../models/ChallengeGetChallengesFilter.md) | ❌       | All, Active, Completed or NotCompleted. If not specified it will default to All |

**Return Type**

`ChallengeAssignmentModelsResult`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment
from voyado_engage.models import ChallengeGetChallengesFilter

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.challenges.challenge_get_challenges(
    contact_id="contactId",
    definition_id="definitionId",
    offset=3,
    count=1,
    filter="All"
)

print(result)
```

## challenge_add_challenge_check_points

Send in a list of checkpoints to be assigned to a some challenge for a number of contacts,
the endpoint will able to take max 1000 checkpoint rows.

### The following fields should be provided:

- definitionId: Must be a Guid
- contactId: Must be a Guid
- checkPointAmount: Number of checkpoints to assign to the challenge

### Important info:

If some rows are not correct it will still result in an accepted response code and be skipped. Please
check the response for NotAccepted items

- HTTP Method: `POST`
- Endpoint: `/api/v2/challenges/checkpoints`

**Parameters**

| Name         | Type                                                                | Required | Description       |
| :----------- | :------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [List[ChallengeCheckPointDto]](../models/ChallengeCheckPointDto.md) | ✅       | The request body. |

**Return Type**

`AddCheckpointToChallengeAssignmentResult`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = [
    {
        "definition_id": "00000000-0000-0000-0000-000000000000",
        "contact_id": "00000000-0000-0000-0000-000000000000",
        "checkpoint_amount": 2
    }
]

result = sdk.challenges.challenge_add_challenge_check_points(request_body=request_body)

print(result)
```

## challenge_consent

Will assign the challenge for the contact and return true. If the contact already
has been assigned for the challenge it will also return true.

- HTTP Method: `POST`
- Endpoint: `/api/v2/challenges/definitions/{id}/assign`

**Parameters**

| Name       | Type | Required | Description   |
| :--------- | :--- | :------- | :------------ |
| id\_       | str  | ✅       | Definition id |
| contact_id | str  | ✅       | Contact id    |

**Return Type**

`bool`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

result = sdk.challenges.challenge_consent(
    id_="id",
    contact_id="contactId"
)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
