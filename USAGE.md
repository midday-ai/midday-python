<!-- Start SDK Example Usage [usage] -->
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