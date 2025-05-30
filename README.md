# midday

Developer-friendly & type-safe Python SDK specifically catered to leverage *midday* API.

<div align="left">
    <a href="https://www.speakeasy.com/?utm_source=midday&utm_campaign=python"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>


Midday API: Midday is a platform for Invoicing, Time tracking, File reconciliation, Storage, Financial Overview & your own Assistant.
<!-- End Summary [summary] -->

<!-- Start Table of Contents [toc] -->
## Table of Contents
<!-- $toc-max-depth=2 -->
* [midday](#midday)
  * [SDK Installation](#sdk-installation)
  * [IDE Support](#ide-support)
  * [SDK Example Usage](#sdk-example-usage)
  * [Authentication](#authentication)
  * [Available Resources and Operations](#available-resources-and-operations)
  * [Retries](#retries)
  * [Error Handling](#error-handling)
  * [Server Selection](#server-selection)
  * [Custom HTTP Client](#custom-http-client)
  * [Resource Management](#resource-management)
  * [Debugging](#debugging)
* [Development](#development)
  * [Maturity](#maturity)
  * [Contributions](#contributions)

<!-- End Table of Contents [toc] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

> [!TIP]
> To finish publishing your SDK to PyPI you must [run your first generation action](https://www.speakeasy.com/docs/github-setup#step-by-step-guide).


> [!NOTE]
> **Python version upgrade policy**
>
> Once a Python version reaches its [official end of life date](https://devguide.python.org/versions/), a 3-month grace period is provided for users to upgrade. Following this grace period, the minimum python version supported in the SDK will be updated.

The SDK can be installed with either *pip* or *poetry* package managers.

### PIP

*PIP* is the default package installer for Python, enabling easy installation and management of packages from PyPI via the command line.

```bash
pip install git+<UNSET>.git
```

### Poetry

*Poetry* is a modern tool that simplifies dependency management and package publishing by using a single `pyproject.toml` file to handle project metadata and dependencies.

```bash
poetry add git+<UNSET>.git
```

### Shell and script usage with `uv`

You can use this SDK in a Python shell with [uv](https://docs.astral.sh/uv/) and the `uvx` command that comes with it like so:

```shell
uvx --from midday python
```

It's also possible to write a standalone Python script without needing to set up a whole project like so:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "midday",
# ]
# ///

from midday import Midday

sdk = Midday(
  # SDK arguments
)

# Rest of script here...
```

Once that is saved to a file, you can run it with `uv run script.py` where
`script.py` can be replaced with the actual file name.
<!-- End SDK Installation [installation] -->

<!-- Start IDE Support [idesupport] -->
## IDE Support

### PyCharm

Generally, the SDK will work well with most IDEs out of the box. However, when using PyCharm, you can enjoy much better integration with Pydantic by installing an additional plugin.

- [PyCharm Pydantic Plugin](https://docs.pydantic.dev/latest/integrations/pycharm/)
<!-- End IDE Support [idesupport] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
# Synchronous Example
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

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from midday import Midday, models

async def main():

    async with Midday(
        token="MIDDAY_API_KEY",
    ) as m_client:

        res = await m_client.transactions.list_async(cursor="eyJpZCI6IjEyMyJ9", sort=[
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

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name    | Type | Scheme      | Environment Variable |
| ------- | ---- | ----------- | -------------------- |
| `token` | http | HTTP Bearer | `MIDDAY_TOKEN`       |

To authenticate with the API the `token` parameter must be set when initializing the SDK client instance. For example:
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
<!-- End Authentication [security] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

<details open>
<summary>Available methods</summary>

### [bank_accounts](docs/sdks/bankaccounts/README.md)

* [list](docs/sdks/bankaccounts/README.md#list) - List all bank accounts
* [create](docs/sdks/bankaccounts/README.md#create) - Create a bank account
* [get](docs/sdks/bankaccounts/README.md#get) - Retrieve a bank account
* [delete](docs/sdks/bankaccounts/README.md#delete) - Delete a bank account
* [update](docs/sdks/bankaccounts/README.md#update) - Update a bank account

### [customers](docs/sdks/customers/README.md)

* [list](docs/sdks/customers/README.md#list) - List all customers
* [create](docs/sdks/customers/README.md#create) - Create customer
* [get](docs/sdks/customers/README.md#get) - Retrieve a customer
* [delete](docs/sdks/customers/README.md#delete) - Delete a customer
* [update](docs/sdks/customers/README.md#update) - Update a customer

### [documents](docs/sdks/documents/README.md)

* [list](docs/sdks/documents/README.md#list) - List all documents
* [get](docs/sdks/documents/README.md#get) - Retrieve a document
* [delete](docs/sdks/documents/README.md#delete) - Delete a document

### [inbox](docs/sdks/inbox/README.md)

* [list](docs/sdks/inbox/README.md#list) - List all inbox items
* [get](docs/sdks/inbox/README.md#get) - Retrieve a inbox item
* [delete](docs/sdks/inbox/README.md#delete) - Delete a inbox item
* [update](docs/sdks/inbox/README.md#update) - Update a inbox item

### [invoices](docs/sdks/invoices/README.md)

* [list](docs/sdks/invoices/README.md#list) - List all invoices
* [get_invoices_payment_status](docs/sdks/invoices/README.md#get_invoices_payment_status) - Payment status
* [summary](docs/sdks/invoices/README.md#summary) - Invoice summary
* [get](docs/sdks/invoices/README.md#get) - Retrieve a invoice
* [delete](docs/sdks/invoices/README.md#delete) - Delete a invoice

### [metrics](docs/sdks/metrics/README.md)

* [revenue](docs/sdks/metrics/README.md#revenue) - Revenue metrics
* [profit](docs/sdks/metrics/README.md#profit) - Profit metrics
* [burn_rate](docs/sdks/metrics/README.md#burn_rate) - Burn rate metrics
* [runway](docs/sdks/metrics/README.md#runway) - Runway metrics
* [expenses](docs/sdks/metrics/README.md#expenses) - Expense metrics
* [spending](docs/sdks/metrics/README.md#spending) - Spending metrics


### [search](docs/sdks/search/README.md)

* [search](docs/sdks/search/README.md#search) - Search

### [tags](docs/sdks/tags/README.md)

* [list](docs/sdks/tags/README.md#list) - List all tags
* [create](docs/sdks/tags/README.md#create) - Create a new tag
* [get](docs/sdks/tags/README.md#get) - Retrieve a tag
* [delete](docs/sdks/tags/README.md#delete) - Delete a tag
* [update](docs/sdks/tags/README.md#update) - Update a tag

### [teams](docs/sdks/teams/README.md)

* [list](docs/sdks/teams/README.md#list) - List all teams
* [get](docs/sdks/teams/README.md#get) - Retrieve a team
* [update](docs/sdks/teams/README.md#update) - Update a team
* [members](docs/sdks/teams/README.md#members) - List all team members

### [tracker](docs/sdks/tracker/README.md)

* [delete](docs/sdks/tracker/README.md#delete) - Delete a tracker entry

### [tracker_entries](docs/sdks/trackerentries/README.md)

* [list](docs/sdks/trackerentries/README.md#list) - List all tracker entries

### [tracker_projects](docs/sdks/trackerprojects/README.md)

* [list](docs/sdks/trackerprojects/README.md#list) - List all tracker projects
* [create](docs/sdks/trackerprojects/README.md#create) - Create a tracker project
* [get](docs/sdks/trackerprojects/README.md#get) - Retrieve a tracker project
* [delete](docs/sdks/trackerprojects/README.md#delete) - Delete a tracker project
* [update](docs/sdks/trackerprojects/README.md#update) - Update a tracker project

### [transactions](docs/sdks/transactions/README.md)

* [list](docs/sdks/transactions/README.md#list) - List all transactions
* [create](docs/sdks/transactions/README.md#create) - Create a transaction
* [get](docs/sdks/transactions/README.md#get) - Retrieve a transaction
* [delete](docs/sdks/transactions/README.md#delete) - Delete a transaction
* [update](docs/sdks/transactions/README.md#update) - Update a transaction
* [create_many](docs/sdks/transactions/README.md#create_many) - Bulk create transactions
* [delete_many](docs/sdks/transactions/README.md#delete_many) - Bulk delete transactions
* [update_many](docs/sdks/transactions/README.md#update_many) - Bulk update transactions

### [users](docs/sdks/users/README.md)

* [get](docs/sdks/users/README.md#get) - Retrieve the current user
* [update](docs/sdks/users/README.md#update) - Update the current user

</details>
<!-- End Available Resources and Operations [operations] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries. If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API. However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a `RetryConfig` object to the call:
```python
from midday import Midday, models
from midday.utils import BackoffStrategy, RetryConfig


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
    ], type_=models.ListTransactionsType.EXPENSE,
        RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False))

    # Handle response
    print(res)

```

If you'd like to override the default retry strategy for all operations that support retries, you can use the `retry_config` optional parameter when initializing the SDK:
```python
from midday import Midday, models
from midday.utils import BackoffStrategy, RetryConfig


with Midday(
    retry_config=RetryConfig("backoff", BackoffStrategy(1, 50, 1.1, 100), False),
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
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations. All operations return a response object or raise an exception.

By default, an API error will raise a errors.APIError exception, which has the following properties:

| Property        | Type             | Description           |
|-----------------|------------------|-----------------------|
| `.status_code`  | *int*            | The HTTP status code  |
| `.message`      | *str*            | The error message     |
| `.raw_response` | *httpx.Response* | The raw HTTP response |
| `.body`         | *str*            | The response content  |

When custom error responses are specified for an operation, the SDK may also raise their associated exceptions. You can refer to respective *Errors* tables in SDK docs for more details on possible exception types for each operation. For example, the `list_async` method may raise the following exceptions:

| Error Type      | Status Code | Content Type |
| --------------- | ----------- | ------------ |
| errors.APIError | 4XX, 5XX    | \*/\*        |

### Example

```python
from midday import Midday, errors, models


with Midday(
    token="MIDDAY_API_KEY",
) as m_client:
    res = None
    try:

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

    except errors.APIError as e:
        # handle exception
        raise(e)
```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Override Server URL Per-Client

The default server can be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
from midday import Midday, models


with Midday(
    server_url="https://api.midday.ai",
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
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [httpx](https://www.python-httpx.org/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with your own HTTP client instance.
Depending on whether you are using the sync or async version of the SDK, you can pass an instance of `HttpClient` or `AsyncHttpClient` respectively, which are Protocol's ensuring that the client has the necessary methods to make API calls.
This allows you to wrap the client with your own custom logic, such as adding custom headers, logging, or error handling, or you can just pass an instance of `httpx.Client` or `httpx.AsyncClient` directly.

For example, you could specify a header for every request that this sdk makes as follows:
```python
from midday import Midday
import httpx

http_client = httpx.Client(headers={"x-custom-header": "someValue"})
s = Midday(client=http_client)
```

or you could wrap the client with your own custom logic:
```python
from midday import Midday
from midday.httpclient import AsyncHttpClient
import httpx

class CustomClient(AsyncHttpClient):
    client: AsyncHttpClient

    def __init__(self, client: AsyncHttpClient):
        self.client = client

    async def send(
        self,
        request: httpx.Request,
        *,
        stream: bool = False,
        auth: Union[
            httpx._types.AuthTypes, httpx._client.UseClientDefault, None
        ] = httpx.USE_CLIENT_DEFAULT,
        follow_redirects: Union[
            bool, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
    ) -> httpx.Response:
        request.headers["Client-Level-Header"] = "added by client"

        return await self.client.send(
            request, stream=stream, auth=auth, follow_redirects=follow_redirects
        )

    def build_request(
        self,
        method: str,
        url: httpx._types.URLTypes,
        *,
        content: Optional[httpx._types.RequestContent] = None,
        data: Optional[httpx._types.RequestData] = None,
        files: Optional[httpx._types.RequestFiles] = None,
        json: Optional[Any] = None,
        params: Optional[httpx._types.QueryParamTypes] = None,
        headers: Optional[httpx._types.HeaderTypes] = None,
        cookies: Optional[httpx._types.CookieTypes] = None,
        timeout: Union[
            httpx._types.TimeoutTypes, httpx._client.UseClientDefault
        ] = httpx.USE_CLIENT_DEFAULT,
        extensions: Optional[httpx._types.RequestExtensions] = None,
    ) -> httpx.Request:
        return self.client.build_request(
            method,
            url,
            content=content,
            data=data,
            files=files,
            json=json,
            params=params,
            headers=headers,
            cookies=cookies,
            timeout=timeout,
            extensions=extensions,
        )

s = Midday(async_client=CustomClient(httpx.AsyncClient()))
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Resource Management [resource-management] -->
## Resource Management

The `Midday` class implements the context manager protocol and registers a finalizer function to close the underlying sync and async HTTPX clients it uses under the hood. This will close HTTP connections, release memory and free up other resources held by the SDK. In short-lived Python programs and notebooks that make a few SDK method calls, resource management may not be a concern. However, in longer-lived programs, it is beneficial to create a single SDK instance via a [context manager][context-manager] and reuse it across the application.

[context-manager]: https://docs.python.org/3/reference/datamodel.html#context-managers

```python
from midday import Midday
def main():

    with Midday(
        token="MIDDAY_API_KEY",
    ) as m_client:
        # Rest of application here...


# Or when using async:
async def amain():

    async with Midday(
        token="MIDDAY_API_KEY",
    ) as m_client:
        # Rest of application here...
```
<!-- End Resource Management [resource-management] -->

<!-- Start Debugging [debug] -->
## Debugging

You can setup your SDK to emit debug logs for SDK requests and responses.

You can pass your own logger class directly into your SDK.
```python
from midday import Midday
import logging

logging.basicConfig(level=logging.DEBUG)
s = Midday(debug_logger=logging.getLogger("midday"))
```

You can also enable a default debug logger by setting an environment variable `MIDDAY_DEBUG` to true.
<!-- End Debugging [debug] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically. Any manual changes added to internal files will be overwritten on the next generation. 
We look forward to hearing your feedback. Feel free to open a PR or an issue with a proof of concept and we'll do our best to include it in a future release. 

### SDK Created by [Speakeasy](https://www.speakeasy.com/?utm_source=midday&utm_campaign=python)
