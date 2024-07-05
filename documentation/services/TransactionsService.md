# TransactionsService

A list of all methods in the `TransactionsService` service. Click on the method name to view detailed information about that method.

| Methods                                                                     | Description                                                                            |
| :-------------------------------------------------------------------------- | :------------------------------------------------------------------------------------- |
| [import_transactions_import_receipts](#import_transactions_import_receipts) | The /receipts endpoint is used to store each customers purchase and returns in Engage. |

All fields in the data model can be used for segmentation and analysis in Engage.
If you want to send out transactional emails, use the /orders endpoint instead.

### Identification

To be able to store a receipt in Voyado, you need to connect it to a specific
contact.

In the example payload below the contact type is “Member” and the key type is “email”
The key has to be a unique data field for the specific contact type,
normally one of these fields:

- contactId
- email
- mobilePhone
- memberNumber
- externalId
- socialSecurityNumber (personal identity number - only Swedish or Finnish) |
  |[import_transactions_import](#import_transactions_import)| Required on **receipt**:
  externalId (Unique receipt id), invoiceNumber, customerKey,
  customerKeyType, invoiceCreatedDate, InvoiceModifiedDate, StoreName, StoreNumber

Required on **transaction**:
externalId (Unique transaction id), articleNr, quantity, price and type (RETURN/DISCOUNT/PURCHASE)
Note! It's recommended to include Sku, as it's a required
attribute when enriching purchase data from article data. |

## import_transactions_import_receipts

The /receipts endpoint is used to store each customers purchase and returns in Engage.
All fields in the data model can be used for segmentation and analysis in Engage.
If you want to send out transactional emails, use the /orders endpoint instead.

### Identification

To be able to store a receipt in Voyado, you need to connect it to a specific
contact.

In the example payload below the contact type is “Member” and the key type is “email”
The key has to be a unique data field for the specific contact type,
normally one of these fields:

- contactId
- email
- mobilePhone
- memberNumber
- externalId
- socialSecurityNumber (personal identity number - only Swedish or Finnish)

- HTTP Method: `POST`
- Endpoint: `/api/v2/receipts`

**Parameters**

| Name         | Type                            | Required | Description       |
| :----------- | :------------------------------ | :------- | :---------------- |
| request_body | [Receipt](../models/Receipt.md) | ✅       | The request body. |

**Return Type**

`dict`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment
from voyado_engage.models import Receipt

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = Receipt(
    contact={
        "match_key": "matchKey",
        "match_key_type": "Email",
        "contact_type": "contactType"
    },
    unique_receipt_id="uniqueReceiptId",
    receipt_number="receiptNumber",
    created_date="createdDate",
    store_external_id="storeExternalId",
    currency="currency",
    exchange_rate_to_group_currency=8.94,
    total_gross_price=7.19,
    tax_details=[
        {
            "description": "description",
            "value": 1.89,
            "percent": 9.91,
            "total_including_tax": 9.84,
            "total_excluding_tax": 8.88
        }
    ],
    payment_methods=[
        {
            "type_": "type",
            "description": "description",
            "value": 5.08,
            "extra_data": [
                {
                    "name": "name",
                    "value": "value"
                }
            ]
        }
    ],
    items=[
        {
            "type_": "PURCHASE",
            "sku": "sku",
            "quantity": 1,
            "pack_quantity": 8.92,
            "gross_paid_price": 1.17,
            "tax_amount": 4.39,
            "tax_percent": 1.12,
            "extra_data": [
                {
                    "name": "name",
                    "value": "value"
                }
            ],
            "article_number": "articleNumber",
            "article_name": "articleName",
            "article_group": "articleGroup",
            "margin_percent": 6.91,
            "awards_bonus": False,
            "discounts": [
                {
                    "value": 9.91,
                    "type_": "type",
                    "description": "description"
                }
            ]
        }
    ],
    used_bonus_checks=[
        {
            "check_number": "checkNumber"
        }
    ],
    used_promotions=[
        {
            "promotion_id": "promotionId",
            "coupon_id": "couponId"
        }
    ],
    extra_data=[
        {
            "name": "name",
            "value": "value"
        }
    ]
)

result = sdk.transactions.import_transactions_import_receipts(request_body=request_body)

print(result)
```

## import_transactions_import

Required on **receipt**:
externalId (Unique receipt id), invoiceNumber, customerKey,
customerKeyType, invoiceCreatedDate, InvoiceModifiedDate, StoreName, StoreNumber

Required on **transaction**:
externalId (Unique transaction id), articleNr, quantity, price and type (RETURN/DISCOUNT/PURCHASE)
Note! It's recommended to include Sku, as it's a required
attribute when enriching purchase data from article data.

- HTTP Method: `POST`
- Endpoint: `/api/v2/transactions`

**Parameters**

| Name         | Type                                                              | Required | Description       |
| :----------- | :---------------------------------------------------------------- | :------- | :---------------- |
| request_body | [ImportTransactionsObject](../models/ImportTransactionsObject.md) | ✅       | The request body. |

**Return Type**

`dict`

**Example Usage Code Snippet**

```python
from voyado_engage import VoyadoEngage, Environment
from voyado_engage.models import ImportTransactionsObject

sdk = VoyadoEngage(
    access_token="YOUR_ACCESS_TOKEN",
    base_url=Environment.DEFAULT.value
)

request_body = ImportTransactionsObject(
    receipts={}
)

result = sdk.transactions.import_transactions_import(request_body=request_body)

print(result)
```

<!-- This file was generated by liblab | https://liblab.com/ -->
