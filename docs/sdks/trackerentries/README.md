# TrackerEntries
(*tracker_entries*)

## Overview

### Available Operations

* [list](#list) - List all tracker entries

## list

List all tracker entries for the authenticated team.

### Example Usage

```python
from midday import Midday


with Midday(
    token="MIDDAY_API_KEY",
) as m_client:

    res = m_client.tracker_entries.list(from_="2024-04-01", to="2024-04-30", project_id="b3b6e2c2-1f2a-4e3b-9c1d-2a4b6e2c21f2")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `from_`                                                             | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 2024-04-01                                                          |
| `to`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | 2024-04-30                                                          |
| `project_id`                                                        | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 | b3b6e2c2-1f2a-4e3b-9c1d-2a4b6e2c21f2                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ListTrackerEntriesResponse](../../models/listtrackerentriesresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |