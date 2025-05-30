# CreateBankAccountRequest

Schema for creating a new bank account.


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        | Example                                            |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `name`                                             | *str*                                              | :heavy_check_mark:                                 | The name of the bank account.                      | Checking Account                                   |
| `currency`                                         | *Optional[str]*                                    | :heavy_minus_sign:                                 | The currency code for the bank account (ISO 4217). | USD                                                |
| `manual`                                           | *Optional[bool]*                                   | :heavy_minus_sign:                                 | Whether the bank account is a manual account.      | false                                              |