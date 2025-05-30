# Customers
(*customers*)

## Overview

### Available Operations

* [list](#list) - List all customers
* [create](#create) - Create customer
* [get](#get) - Retrieve a customer
* [delete](#delete) - Delete a customer
* [update](#update) - Update a customer

## list

Retrieve a list of customers for the authenticated team.

### Example Usage

```python
from midday import Midday


with Midday(
    token="MIDDAY_API_KEY",
) as m_client:

    res = m_client.customers.list(q="acme", sort=[
        "name",
        "asc",
    ], cursor="eyJpZCI6IjEyMyJ9", page_size=20)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `q`                                                                 | *OptionalNullable[str]*                                             | :heavy_minus_sign:                                                  | N/A                                                                 | acme                                                                |
| `sort`                                                              | List[*str*]                                                         | :heavy_minus_sign:                                                  | N/A                                                                 | [<br/>"name",<br/>"asc"<br/>]                                       |
| `cursor`                                                            | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | N/A                                                                 | eyJpZCI6IjEyMyJ9                                                    |
| `page_size`                                                         | *Optional[float]*                                                   | :heavy_minus_sign:                                                  | N/A                                                                 | 20                                                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.ListCustomersResponse](../../models/listcustomersresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## create

Create a new customer for the authenticated team.

### Example Usage

```python
from midday import Midday


with Midday(
    token="MIDDAY_API_KEY",
) as m_client:

    res = m_client.customers.create(request={
        "id": "b3b7c1e2-4c2a-4e7a-9c1a-2b7c1e24c2a4",
        "name": "Acme Corporation",
        "email": "contact@acme.com",
        "country": "United States",
        "address_line1": "123 Main Street",
        "address_line2": "Suite 400",
        "city": "San Francisco",
        "state": "California",
        "zip": "94105",
        "phone": "+1-555-123-4567",
        "website": "https://acme.com",
        "note": "Preferred contact method is email. Large enterprise client.",
        "vat_number": "US123456789",
        "country_code": "US",
        "contact": "John Smith",
        "tags": [
            {
                "id": "e7a9c1a2-4c2a-4e7a-9c1a-2b7c1e24c2a4",
                "name": "VIP",
            },
            {
                "id": "f1b2c3d4-5678-4e7a-9c1a-2b7c1e24c2a4",
                "name": "Enterprise",
            },
        ],
    })

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                             | Type                                                                  | Required                                                              | Description                                                           |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `request`                                                             | [models.CreateCustomerRequest](../../models/createcustomerrequest.md) | :heavy_check_mark:                                                    | The request object to use for the request.                            |
| `retries`                                                             | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)      | :heavy_minus_sign:                                                    | Configuration to override the default retry behavior of the client.   |

### Response

**[models.CreateCustomerResponse](../../models/createcustomerresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## get

Retrieve a customer by ID for the authenticated team.

### Example Usage

```python
from midday import Midday


with Midday(
    token="MIDDAY_API_KEY",
) as m_client:

    res = m_client.customers.get(id="b3b7c1e2-4c2a-4e7a-9c1a-2b7c1e24c2a4")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | b3b7c1e2-4c2a-4e7a-9c1a-2b7c1e24c2a4                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.GetCustomerByIDResponse](../../models/getcustomerbyidresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## delete

Delete a customer by ID for the authenticated team.

### Example Usage

```python
from midday import Midday


with Midday(
    token="MIDDAY_API_KEY",
) as m_client:

    res = m_client.customers.delete(id="b3b7c1e2-4c2a-4e7a-9c1a-2b7c1e24c2a4")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | N/A                                                                 | b3b7c1e2-4c2a-4e7a-9c1a-2b7c1e24c2a4                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |                                                                     |

### Response

**[models.DeleteCustomerResponse](../../models/deletecustomerresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |

## update

Update a customer by ID for the authenticated team.

### Example Usage

```python
from midday import Midday


with Midday(
    token="MIDDAY_API_KEY",
) as m_client:

    res = m_client.customers.update(id_param="b3b7c1e2-4c2a-4e7a-9c1a-2b7c1e24c2a4", name="Acme Corporation", email="contact@acme.com", id="b3b7c1e2-4c2a-4e7a-9c1a-2b7c1e24c2a4", country="United States", address_line1="123 Main Street", address_line2="Suite 400", city="San Francisco", state="California", zip="94105", phone="+1-555-123-4567", website="https://acme.com", note="Preferred contact method is email. Large enterprise client.", vat_number="US123456789", country_code="US", contact="John Smith", tags=[
        {
            "id": "e7a9c1a2-4c2a-4e7a-9c1a-2b7c1e24c2a4",
            "name": "VIP",
        },
        {
            "id": "f1b2c3d4-5678-4e7a-9c1a-2b7c1e24c2a4",
            "name": "Enterprise",
        },
    ])

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                   | Type                                                                                                                                        | Required                                                                                                                                    | Description                                                                                                                                 | Example                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| `id_param`                                                                                                                                  | *str*                                                                                                                                       | :heavy_check_mark:                                                                                                                          | N/A                                                                                                                                         | b3b7c1e2-4c2a-4e7a-9c1a-2b7c1e24c2a4                                                                                                        |
| `name`                                                                                                                                      | *str*                                                                                                                                       | :heavy_check_mark:                                                                                                                          | Name of the customer or organization                                                                                                        | Acme Corporation                                                                                                                            |
| `email`                                                                                                                                     | *str*                                                                                                                                       | :heavy_check_mark:                                                                                                                          | Primary email address of the customer                                                                                                       | contact@acme.com                                                                                                                            |
| `id`                                                                                                                                        | *Optional[str]*                                                                                                                             | :heavy_minus_sign:                                                                                                                          | Unique identifier of the customer. Required for updates, omit for new customers                                                             | b3b7c1e2-4c2a-4e7a-9c1a-2b7c1e24c2a4                                                                                                        |
| `country`                                                                                                                                   | *OptionalNullable[str]*                                                                                                                     | :heavy_minus_sign:                                                                                                                          | Country name where the customer is located                                                                                                  | United States                                                                                                                               |
| `address_line1`                                                                                                                             | *OptionalNullable[str]*                                                                                                                     | :heavy_minus_sign:                                                                                                                          | First line of the customer's address                                                                                                        | 123 Main Street                                                                                                                             |
| `address_line2`                                                                                                                             | *OptionalNullable[str]*                                                                                                                     | :heavy_minus_sign:                                                                                                                          | Second line of the customer's address (suite, apartment, etc.)                                                                              | Suite 400                                                                                                                                   |
| `city`                                                                                                                                      | *OptionalNullable[str]*                                                                                                                     | :heavy_minus_sign:                                                                                                                          | City where the customer is located                                                                                                          | San Francisco                                                                                                                               |
| `state`                                                                                                                                     | *OptionalNullable[str]*                                                                                                                     | :heavy_minus_sign:                                                                                                                          | State or province where the customer is located                                                                                             | California                                                                                                                                  |
| `zip`                                                                                                                                       | *OptionalNullable[str]*                                                                                                                     | :heavy_minus_sign:                                                                                                                          | ZIP or postal code of the customer's address                                                                                                | 94105                                                                                                                                       |
| `phone`                                                                                                                                     | *OptionalNullable[str]*                                                                                                                     | :heavy_minus_sign:                                                                                                                          | Primary phone number of the customer                                                                                                        | +1-555-123-4567                                                                                                                             |
| `website`                                                                                                                                   | *OptionalNullable[str]*                                                                                                                     | :heavy_minus_sign:                                                                                                                          | Website URL of the customer                                                                                                                 | https://acme.com                                                                                                                            |
| `note`                                                                                                                                      | *OptionalNullable[str]*                                                                                                                     | :heavy_minus_sign:                                                                                                                          | Internal notes about the customer for team reference                                                                                        | Preferred contact method is email. Large enterprise client.                                                                                 |
| `vat_number`                                                                                                                                | *OptionalNullable[str]*                                                                                                                     | :heavy_minus_sign:                                                                                                                          | VAT (Value Added Tax) number of the customer                                                                                                | US123456789                                                                                                                                 |
| `country_code`                                                                                                                              | *OptionalNullable[str]*                                                                                                                     | :heavy_minus_sign:                                                                                                                          | Country code in ISO 3166-1 alpha-2 format                                                                                                   | US                                                                                                                                          |
| `contact`                                                                                                                                   | *OptionalNullable[str]*                                                                                                                     | :heavy_minus_sign:                                                                                                                          | Primary contact person's name at the customer organization                                                                                  | John Smith                                                                                                                                  |
| `tags`                                                                                                                                      | List[[models.UpdateCustomerTagRequest](../../models/updatecustomertagrequest.md)]                                                           | :heavy_minus_sign:                                                                                                                          | Array of tags to associate with the customer for categorization                                                                             | [<br/>{<br/>"id": "e7a9c1a2-4c2a-4e7a-9c1a-2b7c1e24c2a4",<br/>"name": "VIP"<br/>},<br/>{<br/>"id": "f1b2c3d4-5678-4e7a-9c1a-2b7c1e24c2a4",<br/>"name": "Enterprise"<br/>}<br/>] |
| `retries`                                                                                                                                   | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                            | :heavy_minus_sign:                                                                                                                          | Configuration to override the default retry behavior of the client.                                                                         |                                                                                                                                             |

### Response

**[models.UpdateCustomerResponse](../../models/updatecustomerresponse.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| errors.APIError | 4XX, 5XX        | \*/\*           |