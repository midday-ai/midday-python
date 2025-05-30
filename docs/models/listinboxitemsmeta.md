# ListInboxItemsMeta

Pagination metadata for the inbox list response.


## Fields

| Field                                                                       | Type                                                                        | Required                                                                    | Description                                                                 | Example                                                                     |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| `cursor`                                                                    | *OptionalNullable[str]*                                                     | :heavy_minus_sign:                                                          | A cursor for pagination, representing the last item from the previous page. | b3b7c1e2-4c2a-4e7a-9c1a-2b7c1e24c2a4                                        |
| `has_previous_page`                                                         | *bool*                                                                      | :heavy_check_mark:                                                          | Whether there is a previous page of results.                                | false                                                                       |
| `has_next_page`                                                             | *bool*                                                                      | :heavy_check_mark:                                                          | Whether there is a next page of results.                                    | true                                                                        |