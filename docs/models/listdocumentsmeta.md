# ListDocumentsMeta

Pagination metadata for the documents list.


## Fields

| Field                             | Type                              | Required                          | Description                       | Example                           |
| --------------------------------- | --------------------------------- | --------------------------------- | --------------------------------- | --------------------------------- |
| `cursor`                          | *OptionalNullable[str]*           | :heavy_minus_sign:                | Cursor for pagination.            | 20                                |
| `has_previous_page`               | *bool*                            | :heavy_check_mark:                | Whether there is a previous page. | false                             |
| `has_next_page`                   | *bool*                            | :heavy_check_mark:                | Whether there is a next page.     | true                              |