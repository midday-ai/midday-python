# ListInvoicesMeta

Pagination metadata


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          | Example                                              |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `cursor`                                             | *Nullable[str]*                                      | :heavy_check_mark:                                   | Cursor for pagination; null if there is no next page | 25                                                   |
| `has_previous_page`                                  | *bool*                                               | :heavy_check_mark:                                   | Indicates if there is a previous page of results     | false                                                |
| `has_next_page`                                      | *bool*                                               | :heavy_check_mark:                                   | Indicates if there is a next page of results         | true                                                 |