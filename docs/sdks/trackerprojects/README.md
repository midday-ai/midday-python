# TrackerProjects
(*tracker_projects*)

## Overview

### Available Operations

* [list](#list) - List all tracker projects
* [create](#create) - Create a tracker project
* [get](#get) - Retrieve a tracker project
* [delete](#delete) - Delete a tracker project
* [update](#update) - Update a tracker project

## list

List all tracker projects for the authenticated team.

### Example Usage

```python
from midday import Midday, models


with Midday(
    token="MIDDAY_API_KEY",
) as m_client:

    res = m_client.tracker_projects.list(cursor="eyJpZCI6IjEyMyJ9", page_size=20, q="website", start="2024-04-01", end="2024-04-30", status=models.ListTrackerProjectsStatus.IN_PROGRESS, customers=[
        "customer-1",
        "customer-2",
    ], tags=[
        "tag-1",
        "tag-2",
    ], sort=[
        "-createdAt",
        "name",
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                       | Type                                                                                            | Required                                                                                        | Description                                                                                     | Example                                                                                         |
| ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `cursor`                                                                                        | *OptionalNullable[str]*                                                                         | :heavy_minus_sign:                                                                              | N/A                                                                                             | eyJpZCI6IjEyMyJ9                                                                                |
| `page_size`                                                                                     | *Optional[float]*                                                                               | :heavy_minus_sign:                                                                              | N/A                                                                                             | 20                                                                                              |
| `q`                                                                                             | *OptionalNullable[str]*                                                                         | :heavy_minus_sign:                                                                              | N/A                                                                                             | website                                                                                         |
| `start`                                                                                         | *OptionalNullable[str]*                                                                         | :heavy_minus_sign:                                                                              | N/A                                                                                             | 2024-04-01                                                                                      |
| `end`                                                                                           | *OptionalNullable[str]*                                                                         | :heavy_minus_sign:                                                                              | N/A                                                                                             | 2024-04-30                                                                                      |
| `status`                                                                                        | [OptionalNullable[models.ListTrackerProjectsStatus]](../../models/listtrackerprojectsstatus.md) | :heavy_minus_sign:                                                                              | Filter projects by status                                                                       | in_progress                                                                                     |
| `customers`                                                                                     | List[*str*]                                                                                     | :heavy_minus_sign:                                                                              | N/A                                                                                             | [<br/>"customer-1",<br/>"customer-2"<br/>]                                                      |
| `tags`                                                                                          | List[*str*]                                                                                     | :heavy_minus_sign:                                                                              | N/A                                                                                             | [<br/>"tag-1",<br/>"tag-2"<br/>]                                                                |
| `sort`                                                                                          | List[*str*]                                                                                     | :heavy_minus_sign:                                                                              | N/A                                                                                             | [<br/>"-createdAt",<br/>"name"<br/>]                                                            |
| `retries`                                                                                       | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                | :heavy_minus_sign:                                                                              | Configuration to override the default retry behavior of the client.                             |                                                                                                 |

### Response

**[models.TrackerProjectsResponse](../../models/trackerprojectsresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create

Create a tracker project for the authenticated team.

### Example Usage

```python
from midday import Midday


with Midday(
    token="MIDDAY_API_KEY",
) as m_client:

    res = m_client.tracker_projects.create(request={
        "name": "New Project",
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                         | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `request`                                                                         | [models.CreateTrackerProjectRequest](../../models/createtrackerprojectrequest.md) | :heavy_check_mark:                                                                | The request object to use for the request.                                        |
| `retries`                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                  | :heavy_minus_sign:                                                                | Configuration to override the default retry behavior of the client.               |

### Response

**[models.TrackerProjectResponse](../../models/trackerprojectresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get

Retrieve a tracker project for the authenticated team.

### Example Usage

```python
from midday import Midday


with Midday(
    token="MIDDAY_API_KEY",
) as m_client:

    res = m_client.tracker_projects.get(id="b7e6c8e2-1f2a-4c3b-9e2d-1a2b3c4d5e6f")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | b7e6c8e2-1f2a-4c3b-9e2d-1a2b3c4d5e6f                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.TrackerProjectResponse](../../models/trackerprojectresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## delete

Delete a tracker project for the authenticated team.

### Example Usage

```python
from midday import Midday


with Midday(
    token="MIDDAY_API_KEY",
) as m_client:

    res = m_client.tracker_projects.delete(id="b7e6c8e2-1f2a-4c3b-9e2d-1a2b3c4d5e6f")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | b7e6c8e2-1f2a-4c3b-9e2d-1a2b3c4d5e6f                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DeleteTrackerProjectResponse](../../models/deletetrackerprojectresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update

Update a tracker project for the authenticated team.

### Example Usage

```python
from midday import Midday, models


with Midday(
    token="MIDDAY_API_KEY",
) as m_client:

    res = m_client.tracker_projects.update(id="b7e6c8e2-1f2a-4c3b-9e2d-1a2b3c4d5e6f", name="Website Redesign", description="Complete redesign of the company website with modern UI/UX and improved performance", estimate=120, rate=75, currency="USD", status=models.UpdateTrackerProjectStatus.IN_PROGRESS, customer_id="a1b2c3d4-e5f6-7890-abcd-1234567890ef", tags=[
        {
            "id": "f1e2d3c4-b5a6-7890-1234-567890abcdef",
            "value": "Design",
        },
        {
            "id": "e2d3c4b5-a6f1-7890-1234-567890abcdef",
            "value": "Frontend",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                      | Type                                                                                                                                           | Required                                                                                                                                       | Description                                                                                                                                    | Example                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                                                                                                                                           | *str*                                                                                                                                          | :heavy_check_mark:                                                                                                                             | N/A                                                                                                                                            | b7e6c8e2-1f2a-4c3b-9e2d-1a2b3c4d5e6f                                                                                                           |
| `name`                                                                                                                                         | *str*                                                                                                                                          | :heavy_check_mark:                                                                                                                             | Name of the project                                                                                                                            | Website Redesign                                                                                                                               |
| `description`                                                                                                                                  | *OptionalNullable[str]*                                                                                                                        | :heavy_minus_sign:                                                                                                                             | Detailed description of the project                                                                                                            | Complete redesign of the company website with modern UI/UX and improved performance                                                            |
| `estimate`                                                                                                                                     | *OptionalNullable[float]*                                                                                                                      | :heavy_minus_sign:                                                                                                                             | Estimated total hours required to complete the project                                                                                         | 120                                                                                                                                            |
| `billable`                                                                                                                                     | *OptionalNullable[bool]*                                                                                                                       | :heavy_minus_sign:                                                                                                                             | Whether the project is billable to the customer                                                                                                | true                                                                                                                                           |
| `rate`                                                                                                                                         | *OptionalNullable[float]*                                                                                                                      | :heavy_minus_sign:                                                                                                                             | Hourly rate for the project in the specified currency                                                                                          | 75                                                                                                                                             |
| `currency`                                                                                                                                     | *OptionalNullable[str]*                                                                                                                        | :heavy_minus_sign:                                                                                                                             | Currency code for the project rate in ISO 4217 format                                                                                          | USD                                                                                                                                            |
| `status`                                                                                                                                       | [Optional[models.UpdateTrackerProjectStatus]](../../models/updatetrackerprojectstatus.md)                                                      | :heavy_minus_sign:                                                                                                                             | Current status of the project                                                                                                                  | in_progress                                                                                                                                    |
| `customer_id`                                                                                                                                  | *OptionalNullable[str]*                                                                                                                        | :heavy_minus_sign:                                                                                                                             | Unique identifier of the customer associated with this project                                                                                 | a1b2c3d4-e5f6-7890-abcd-1234567890ef                                                                                                           |
| `tags`                                                                                                                                         | List[[models.UpdateTrackerProjectTag](../../models/updatetrackerprojecttag.md)]                                                                | :heavy_minus_sign:                                                                                                                             | Array of tags to associate with the project                                                                                                    | [<br/>{<br/>"id": "f1e2d3c4-b5a6-7890-1234-567890abcdef",<br/>"value": "Design"<br/>},<br/>{<br/>"id": "e2d3c4b5-a6f1-7890-1234-567890abcdef",<br/>"value": "Frontend"<br/>}<br/>] |
| `retries`                                                                                                                                      | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                               | :heavy_minus_sign:                                                                                                                             | Configuration to override the default retry behavior of the client.                                                                            |                                                                                                                                                |

### Response

**[models.TrackerProjectResponse](../../models/trackerprojectresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |