# ListInboxItemsTransaction

Matched transaction for this inbox item, if any


## Fields

| Field                                | Type                                 | Required                             | Description                          | Example                              |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `id`                                 | *str*                                | :heavy_check_mark:                   | Transaction ID (UUID)                | a1b2c3d4-5678-4e7a-9c1a-2b7c1e24c2a4 |
| `amount`                             | *float*                              | :heavy_check_mark:                   | Transaction amount                   | 123.45                               |
| `currency`                           | *str*                                | :heavy_check_mark:                   | Transaction currency (ISO 4217)      | USD                                  |
| `name`                               | *str*                                | :heavy_check_mark:                   | Transaction name or payee            | Acme Corp                            |
| `date_`                              | *str*                                | :heavy_check_mark:                   | Transaction date (ISO 8601)          | 2024-05-01                           |