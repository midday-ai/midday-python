# ListCustomersMeta

Pagination metadata for the customers response


## Fields

| Field                                                           | Type                                                            | Required                                                        | Description                                                     | Example                                                         |
| --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- | --------------------------------------------------------------- |
| `cursor`                                                        | *Nullable[str]*                                                 | :heavy_check_mark:                                              | Cursor for the next page of results, null if no more pages      | eyJpZCI6IjQ1NiJ9                                                |
| `has_previous_page`                                             | *bool*                                                          | :heavy_check_mark:                                              | Whether there are more customers available on the previous page | false                                                           |
| `has_next_page`                                                 | *bool*                                                          | :heavy_check_mark:                                              | Whether there are more customers available on the next page     | true                                                            |