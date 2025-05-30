# BankAccounts
(*bank_accounts*)

## Overview

### Available Operations

* [list](#list) - List all bank accounts
* [create](#create) - Create a bank account
* [get](#get) - Retrieve a bank account
* [delete](#delete) - Delete a bank account
* [update](#update) - Update a bank account

## list

Retrieve a list of bank accounts for the authenticated team.

### Example Usage

```python
from midday import Midday


with Midday(
    token="MIDDAY_API_KEY",
) as m_client:

    res = m_client.bank_accounts.list()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `enabled`                                                           | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `manual`                                                            | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.ListBankAccountsResponse](../../models/listbankaccountsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create

Create a new bank account for the authenticated team.

### Example Usage

```python
from midday import Midday


with Midday(
    token="MIDDAY_API_KEY",
) as m_client:

    res = m_client.bank_accounts.create(request={
        "name": "Checking Account",
        "currency": "USD",
        "manual": False,
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                   | Type                                                                        | Required                                                                    | Description                                                                 |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `request`                                                                   | [models.CreateBankAccountRequest](../../models/createbankaccountrequest.md) | :heavy_check_mark:                                                          | The request object to use for the request.                                  |
| `retries`                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)            | :heavy_minus_sign:                                                          | Configuration to override the default retry behavior of the client.         |

### Response

**[models.CreateBankAccountResponse](../../models/createbankaccountresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get

Retrieve a bank account by ID for the authenticated team.

### Example Usage

```python
from midday import Midday


with Midday(
    token="MIDDAY_API_KEY",
) as m_client:

    res = m_client.bank_accounts.get(id="b7e6c2a0-1f2d-4c3b-9a8e-123456789abc")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | b7e6c2a0-1f2d-4c3b-9a8e-123456789abc                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetBankAccountByIDResponse](../../models/getbankaccountbyidresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## delete

Delete a bank account by ID for the authenticated team.

### Example Usage

```python
from midday import Midday


with Midday(
    token="MIDDAY_API_KEY",
) as m_client:

    res = m_client.bank_accounts.delete(id="b7e6c2a0-1f2d-4c3b-9a8e-123456789abc")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | b7e6c2a0-1f2d-4c3b-9a8e-123456789abc                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DeleteBankAccountResponse](../../models/deletebankaccountresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update

Update a bank account by ID for the authenticated team.

### Example Usage

```python
from midday import Midday, models


with Midday(
    token="MIDDAY_API_KEY",
) as m_client:

    res = m_client.bank_accounts.update(id_param="b7e6c2a0-1f2d-4c3b-9a8e-123456789abc", id="b7e6c2a0-1f2d-4c3b-9a8e-123456789abc", name="Checking Account", enabled=True, balance=1500.75, currency="USD", type_=models.UpdateBankAccountType.DEPOSITORY)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                       | Type                                                                            | Required                                                                        | Description                                                                     | Example                                                                         |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `id_param`                                                                      | *str*                                                                           | :heavy_check_mark:                                                              | N/A                                                                             | b7e6c2a0-1f2d-4c3b-9a8e-123456789abc                                            |
| `id`                                                                            | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | The unique identifier of the bank account.                                      | b7e6c2a0-1f2d-4c3b-9a8e-123456789abc                                            |
| `name`                                                                          | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | The name of the bank account.                                                   | Checking Account                                                                |
| `enabled`                                                                       | *Optional[bool]*                                                                | :heavy_minus_sign:                                                              | Whether the bank account is enabled.                                            | true                                                                            |
| `balance`                                                                       | *Optional[float]*                                                               | :heavy_minus_sign:                                                              | Current balance of the bank account.                                            | 1500.75                                                                         |
| `currency`                                                                      | *Optional[str]*                                                                 | :heavy_minus_sign:                                                              | The currency code for the bank account (ISO 4217).                              | USD                                                                             |
| `type`                                                                          | [Optional[models.UpdateBankAccountType]](../../models/updatebankaccounttype.md) | :heavy_minus_sign:                                                              | Type of the bank account.                                                       | depository                                                                      |
| `retries`                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                | :heavy_minus_sign:                                                              | Configuration to override the default retry behavior of the client.             |                                                                                 |

### Response

**[models.UpdateBankAccountResponse](../../models/updatebankaccountresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |