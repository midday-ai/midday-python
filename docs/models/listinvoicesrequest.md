# ListInvoicesRequest


## Fields

| Field                                    | Type                                     | Required                                 | Description                              | Example                                  |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| `cursor`                                 | *OptionalNullable[str]*                  | :heavy_minus_sign:                       | N/A                                      | 25                                       |
| `sort`                                   | List[*str*]                              | :heavy_minus_sign:                       | N/A                                      | [<br/>"createdAt",<br/>"desc"<br/>]      |
| `page_size`                              | *Optional[float]*                        | :heavy_minus_sign:                       | N/A                                      | 25                                       |
| `q`                                      | *OptionalNullable[str]*                  | :heavy_minus_sign:                       | N/A                                      | Acme                                     |
| `start`                                  | *OptionalNullable[str]*                  | :heavy_minus_sign:                       | N/A                                      | 2024-01-01                               |
| `end`                                    | *OptionalNullable[str]*                  | :heavy_minus_sign:                       | N/A                                      | 2024-01-31                               |
| `statuses`                               | List[*str*]                              | :heavy_minus_sign:                       | N/A                                      | [<br/>"paid",<br/>"unpaid"<br/>]         |
| `customers`                              | List[*str*]                              | :heavy_minus_sign:                       | N/A                                      | [<br/>"customer-uuid-1",<br/>"customer-uuid-2"<br/>] |