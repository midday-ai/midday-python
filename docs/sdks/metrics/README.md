# Metrics
(*metrics*)

## Overview

### Available Operations

* [revenue](#revenue) - Revenue metrics
* [profit](#profit) - Profit metrics
* [burn_rate](#burn_rate) - Burn rate metrics
* [runway](#runway) - Runway metrics
* [expenses](#expenses) - Expense metrics
* [spending](#spending) - Spending metrics

## revenue

Revenue metrics for the authenticated team.

### Example Usage

```python
from midday import Midday


with Midday(
    token="MIDDAY_API_KEY",
) as m_client:

    res = m_client.metrics.revenue(from_="2023-01-01", to="2023-12-31", currency="USD")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `from_`                                                             | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 2023-01-01                                                          |
| `to`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 2023-12-31                                                          |
| `currency`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 | USD                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetRevenueResponseSchema](../../models/getrevenueresponseschema.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## profit

Profit metrics for the authenticated team.

### Example Usage

```python
from midday import Midday


with Midday(
    token="MIDDAY_API_KEY",
) as m_client:

    res = m_client.metrics.profit(from_="2023-01-01", to="2023-12-31", currency="USD")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `from_`                                                             | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 2023-01-01                                                          |
| `to`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 2023-12-31                                                          |
| `currency`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 | USD                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetProfitResponseSchema](../../models/getprofitresponseschema.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## burn_rate

Burn rate metrics for the authenticated team.

### Example Usage

```python
from midday import Midday


with Midday(
    token="MIDDAY_API_KEY",
) as m_client:

    res = m_client.metrics.burn_rate(from_="2023-01-01", to="2023-12-31", currency="USD")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `from_`                                                             | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 2023-01-01                                                          |
| `to`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 2023-12-31                                                          |
| `currency`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 | USD                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[List[models.GetBurnRateResponseSchema]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## runway

Runway metrics for the authenticated team.

### Example Usage

```python
from midday import Midday


with Midday(
    token="MIDDAY_API_KEY",
) as m_client:

    res = m_client.metrics.runway(from_="2023-01-01", to="2023-12-31", currency="USD")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `from_`                                                             | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 2023-01-01                                                          |
| `to`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 2023-12-31                                                          |
| `currency`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 | USD                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[float](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## expenses

Expense metrics for the authenticated team.

### Example Usage

```python
from midday import Midday


with Midday(
    token="MIDDAY_API_KEY",
) as m_client:

    res = m_client.metrics.expenses(from_="2023-01-01", to="2023-12-31", currency="USD")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `from_`                                                             | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 2023-01-01                                                          |
| `to`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 2023-12-31                                                          |
| `currency`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 | USD                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetExpensesResponseSchema](../../models/getexpensesresponseschema.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## spending

Spending metrics for the authenticated team.

### Example Usage

```python
from midday import Midday


with Midday(
    token="MIDDAY_API_KEY",
) as m_client:

    res = m_client.metrics.spending(from_="2023-01-01", to="2023-12-31", currency="USD")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `from_`                                                             | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 2023-01-01                                                          |
| `to`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 2023-12-31                                                          |
| `currency`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 | USD                                                                 |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[List[models.SpendingResultArray]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |