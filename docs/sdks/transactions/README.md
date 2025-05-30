# Transactions
(*transactions*)

## Overview

### Available Operations

* [list](#list) - List all transactions
* [create](#create) - Create a transaction
* [get](#get) - Retrieve a transaction
* [delete](#delete) - Delete a transaction
* [update](#update) - Update a transaction
* [create_many](#create_many) - Bulk create transactions
* [delete_many](#delete_many) - Bulk delete transactions
* [update_many](#update_many) - Bulk update transactions

## list

Retrieve a list of transactions for the authenticated team.

### Example Usage

```python
from midday import Midday, models


with Midday(
    token="MIDDAY_API_KEY",
) as m_client:

    res = m_client.transactions.list(cursor="eyJpZCI6IjEyMyJ9", sort=[
        "date",
        "desc",
    ], page_size=50, q="office supplies", categories=[
        "office-supplies",
        "travel",
    ], tags=[
        "tag-1",
        "tag-2",
    ], start="2024-04-01T00:00:00.000Z", end="2024-04-30T23:59:59.999Z", accounts=[
        "account-1",
        "account-2",
    ], assignees=[
        "user-1",
        "user-2",
    ], statuses=[
        "pending",
        "completed",
    ], recurring=[
        "monthly",
        "annually",
    ], attachments=models.Attachments.INCLUDE, amount_range=[
        100,
        1000,
    ], amount=[
        "150.75",
        "299.99",
    ], type_=models.ListTransactionsType.EXPENSE)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                       | Type                                                                                                                                                            | Required                                                                                                                                                        | Description                                                                                                                                                     | Example                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `cursor`                                                                                                                                                        | *OptionalNullable[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                              | N/A                                                                                                                                                             | eyJpZCI6IjEyMyJ9                                                                                                                                                |
| `sort`                                                                                                                                                          | List[*str*]                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                              | N/A                                                                                                                                                             | [<br/>"date",<br/>"desc"<br/>]                                                                                                                                  |
| `page_size`                                                                                                                                                     | *Optional[float]*                                                                                                                                               | :heavy_minus_sign:                                                                                                                                              | N/A                                                                                                                                                             | 50                                                                                                                                                              |
| `q`                                                                                                                                                             | *OptionalNullable[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                              | N/A                                                                                                                                                             | office supplies                                                                                                                                                 |
| `categories`                                                                                                                                                    | List[*str*]                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                              | N/A                                                                                                                                                             | [<br/>"office-supplies",<br/>"travel"<br/>]                                                                                                                     |
| `tags`                                                                                                                                                          | List[*str*]                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                              | N/A                                                                                                                                                             | [<br/>"tag-1",<br/>"tag-2"<br/>]                                                                                                                                |
| `start`                                                                                                                                                         | *OptionalNullable[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                              | N/A                                                                                                                                                             | 2024-04-01T00:00:00.000Z                                                                                                                                        |
| `end`                                                                                                                                                           | *OptionalNullable[str]*                                                                                                                                         | :heavy_minus_sign:                                                                                                                                              | N/A                                                                                                                                                             | 2024-04-30T23:59:59.999Z                                                                                                                                        |
| `accounts`                                                                                                                                                      | List[*str*]                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                              | N/A                                                                                                                                                             | [<br/>"account-1",<br/>"account-2"<br/>]                                                                                                                        |
| `assignees`                                                                                                                                                     | List[*str*]                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                              | N/A                                                                                                                                                             | [<br/>"user-1",<br/>"user-2"<br/>]                                                                                                                              |
| `statuses`                                                                                                                                                      | List[*str*]                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                              | N/A                                                                                                                                                             | [<br/>"pending",<br/>"completed"<br/>]                                                                                                                          |
| `recurring`                                                                                                                                                     | List[*str*]                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                              | N/A                                                                                                                                                             | [<br/>"monthly",<br/>"annually"<br/>]                                                                                                                           |
| `attachments`                                                                                                                                                   | [OptionalNullable[models.Attachments]](../../models/attachments.md)                                                                                             | :heavy_minus_sign:                                                                                                                                              | Filter transactions based on attachment presence. 'include' returns only transactions with attachments, 'exclude' returns only transactions without attachments | include                                                                                                                                                         |
| `amount_range`                                                                                                                                                  | List[*Nullable[float]*]                                                                                                                                         | :heavy_minus_sign:                                                                                                                                              | N/A                                                                                                                                                             | [<br/>100,<br/>1000<br/>]                                                                                                                                       |
| `amount`                                                                                                                                                        | List[*str*]                                                                                                                                                     | :heavy_minus_sign:                                                                                                                                              | N/A                                                                                                                                                             | [<br/>"150.75",<br/>"299.99"<br/>]                                                                                                                              |
| `type`                                                                                                                                                          | [OptionalNullable[models.ListTransactionsType]](../../models/listtransactionstype.md)                                                                           | :heavy_minus_sign:                                                                                                                                              | Transaction type to filter by. 'income' for money received, 'expense' for money spent                                                                           | expense                                                                                                                                                         |
| `retries`                                                                                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                | :heavy_minus_sign:                                                                                                                                              | Configuration to override the default retry behavior of the client.                                                                                             |                                                                                                                                                                 |

### Response

**[models.ListTransactionsResponse](../../models/listtransactionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create

Create a transaction

### Example Usage

```python
from midday import Midday


with Midday(
    token="MIDDAY_API_KEY",
) as m_client:

    res = m_client.transactions.create()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `request`                                                                   | [models.CreateTransactionRequest](../../models/createtransactionrequest.md) | :heavy_check_mark:                                                          | The request object to use for the request.                                  |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.TransactionResponse](../../models/transactionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get

Retrieve a transaction by its ID for the authenticated team.

### Example Usage

```python
from midday import Midday


with Midday(
    token="MIDDAY_API_KEY",
) as m_client:

    res = m_client.transactions.get(id="391723c9-de99-4039-b8e2-4fa5bbdf9480")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.TransactionResponse](../../models/transactionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## delete

Delete a transaction for the authenticated team. Only manually created transactions can be deleted via this endpoint or the form. Transactions inserted by bank connections cannot be deleted, but can be excluded by updating the status.

### Example Usage

```python
from midday import Midday


with Midday(
    token="MIDDAY_API_KEY",
) as m_client:

    res = m_client.transactions.delete(id="92766ee2-a2bc-44aa-97af-6891695fc321")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteTransactionResponse](../../models/deletetransactionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update

Update a transaction for the authenticated team. If there's no change, returns it as it is.

### Example Usage

```python
from midday import Midday


with Midday(
    token="MIDDAY_API_KEY",
) as m_client:

    res = m_client.transactions.update(id="f0c1d0ef-5679-4c1b-9698-2c64e97e8c1d")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                         | Type                                                                                              | Required                                                                                          | Description                                                                                       |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `id`                                                                                              | *str*                                                                                             | :heavy_check_mark:                                                                                | N/A                                                                                               |
| `category_slug`                                                                                   | *OptionalNullable[str]*                                                                           | :heavy_minus_sign:                                                                                | Category slug for the transaction.                                                                |
| `status`                                                                                          | [OptionalNullable[models.UpdateTransactionStatus]](../../models/updatetransactionstatus.md)       | :heavy_minus_sign:                                                                                | Status of the transaction.                                                                        |
| `internal`                                                                                        | *Optional[bool]*                                                                                  | :heavy_minus_sign:                                                                                | Whether the transaction is internal.                                                              |
| `recurring`                                                                                       | *Optional[bool]*                                                                                  | :heavy_minus_sign:                                                                                | Whether the transaction is recurring.                                                             |
| `frequency`                                                                                       | [OptionalNullable[models.UpdateTransactionFrequency]](../../models/updatetransactionfrequency.md) | :heavy_minus_sign:                                                                                | Recurring frequency of the transaction.                                                           |
| `note`                                                                                            | *OptionalNullable[str]*                                                                           | :heavy_minus_sign:                                                                                | Note for the transaction.                                                                         |
| `assigned_id`                                                                                     | *OptionalNullable[str]*                                                                           | :heavy_minus_sign:                                                                                | Assigned user ID for the transaction.                                                             |
| `retries`                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                  | :heavy_minus_sign:                                                                                | Configuration to override the default retry behavior of the client.                               |

### Response

**[models.TransactionResponse](../../models/transactionresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create_many

Bulk create transactions for the authenticated team.

### Example Usage

```python
from midday import Midday


with Midday(
    token="MIDDAY_API_KEY",
) as m_client:

    res = m_client.transactions.create_many()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [List[models.RequestBody]](../../models/.md)                        | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.TransactionResponse]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## delete_many

Bulk delete transactions for the authenticated team. Only manually created transactions can be deleted via this endpoint or the form. Transactions inserted by bank connections cannot be deleted, but can be excluded by updating the status.

### Example Usage

```python
from midday import Midday


with Midday(
    token="MIDDAY_API_KEY",
) as m_client:

    res = m_client.transactions.delete_many()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `request`                                                           | [List[str]](../../models/.md)                                       | :heavy_check_mark:                                                  | The request object to use for the request.                          |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[List[models.DeleteTransactionsResponse]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update_many

Bulk update transactions for the authenticated team. If there's no change, returns it as it is.

### Example Usage

```python
from midday import Midday


with Midday(
    token="MIDDAY_API_KEY",
) as m_client:

    res = m_client.transactions.update_many()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                     | Type                                                                          | Required                                                                      | Description                                                                   |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| `request`                                                                     | [models.UpdateTransactionsRequest](../../models/updatetransactionsrequest.md) | :heavy_check_mark:                                                            | The request object to use for the request.                                    |
| `retries`                                                                     | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)              | :heavy_minus_sign:                                                            | Configuration to override the default retry behavior of the client.           |

### Response

**[models.UpdateTransactionsResponse](../../models/updatetransactionsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |