# Invoices
(*invoices*)

## Overview

### Available Operations

* [list](#list) - List all invoices
* [get_invoices_payment_status](#get_invoices_payment_status) - Payment status
* [summary](#summary) - Invoice summary
* [get](#get) - Retrieve a invoice
* [delete](#delete) - Delete a invoice

## list

Retrieve a list of invoices for the authenticated team.

### Example Usage

```python
from midday import Midday


with Midday(
    token="MIDDAY_API_KEY",
) as m_client:

    res = m_client.invoices.list(cursor="25", sort=[
        "createdAt",
        "desc",
    ], page_size=25, q="Acme", start="2024-01-01", end="2024-01-31", statuses=[
        "paid",
        "unpaid",
    ], customers=[
        "customer-uuid-1",
        "customer-uuid-2",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `cursor`                                                            | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 | 25                                                                  |
| `sort`                                                              | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 | [<br/>"createdAt",<br/>"desc"<br/>]                                 |
| `page_size`                                                         | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 | 25                                                                  |
| `q`                                                                 | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 | Acme                                                                |
| `start`                                                             | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 | 2024-01-01                                                          |
| `end`                                                               | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 | 2024-01-31                                                          |
| `statuses`                                                          | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 | [<br/>"paid",<br/>"unpaid"<br/>]                                    |
| `customers`                                                         | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 | [<br/>"customer-uuid-1",<br/>"customer-uuid-2"<br/>]                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ListInvoicesResponse](../../models/listinvoicesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get_invoices_payment_status

Get payment status for the authenticated team.

### Example Usage

```python
from midday import Midday


with Midday(
    token="MIDDAY_API_KEY",
) as m_client:

    res = m_client.invoices.get_invoices_payment_status()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetInvoicesPaymentStatusResponse](../../models/getinvoicespaymentstatusresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## summary

Get summary of invoices for the authenticated team.

### Example Usage

```python
from midday import Midday, models


with Midday(
    token="MIDDAY_API_KEY",
) as m_client:

    res = m_client.invoices.summary(status=models.GetInvoiceSummaryStatus.PAID)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         | Example                                                                             |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `status`                                                                            | [Optional[models.GetInvoiceSummaryStatus]](../../models/getinvoicesummarystatus.md) | :heavy_minus_sign:                                                                  | Filter summary by invoice status                                                    | paid                                                                                |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |                                                                                     |

### Response

**[List[models.GetInvoiceSummaryResponse]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get

Retrieve a invoice by its unique identifier for the authenticated team.

### Example Usage

```python
from midday import Midday


with Midday(
    token="MIDDAY_API_KEY",
) as m_client:

    res = m_client.invoices.get(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetInvoiceByIDResponse](../../models/getinvoicebyidresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## delete

Delete an invoice by its unique identifier for the authenticated team. Only invoices with status 'draft' or 'canceled' can be deleted directly. If the invoice is not in one of these statuses, update its status to 'canceled' before attempting deletion.

### Example Usage

```python
from midday import Midday


with Midday(
    token="MIDDAY_API_KEY",
) as m_client:

    res = m_client.invoices.delete(id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteInvoiceResponse](../../models/deleteinvoiceresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |