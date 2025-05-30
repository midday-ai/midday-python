# Search
(*search*)

## Overview

### Available Operations

* [search](#search) - Search

## search

Search across all data, invoices, documents, customers, transactions, and more.

### Example Usage

```python
from midday import Midday


with Midday(
    token="MIDDAY_API_KEY",
) as m_client:

    res = m_client.search.search(search_term="Acme", language="en")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `search_term`                                                       | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 | Acme                                                                |
| `language`                                                          | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 | en                                                                  |
| `limit`                                                             | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 | 30                                                                  |
| `items_per_table_limit`                                             | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 | 5                                                                   |
| `relevance_threshold`                                               | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 | 0.01                                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[List[models.SearchResponse]](../../models/.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |