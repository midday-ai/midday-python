# GetBankAccountByIDResponse

A single bank account object response.


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          | Example                                              |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `id`                                                 | *str*                                                | :heavy_check_mark:                                   | Unique identifier for the bank account.              | b7e6c2a0-1f2d-4c3b-9a8e-123456789abc                 |
| `name`                                               | *Nullable[str]*                                      | :heavy_check_mark:                                   | Name of the bank account.                            | Checking Account                                     |
| `currency`                                           | *Nullable[str]*                                      | :heavy_check_mark:                                   | Currency code of the bank account (e.g., USD, EUR).  | USD                                                  |
| `type`                                               | *Nullable[str]*                                      | :heavy_check_mark:                                   | Type of the bank account (e.g., depository, credit). | depository                                           |
| `enabled`                                            | *bool*                                               | :heavy_check_mark:                                   | Whether the bank account is enabled.                 | true                                                 |
| `balance`                                            | *Nullable[float]*                                    | :heavy_check_mark:                                   | Current balance of the bank account.                 | 1500.75                                              |
| `manual`                                             | *Nullable[bool]*                                     | :heavy_check_mark:                                   | Whether the bank account is a manual account.        | false                                                |