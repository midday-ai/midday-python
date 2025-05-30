# UpdateTransactionsResponse

Transactions updated


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `meta`                                                               | [models.UpdateTransactionsMeta](../models/updatetransactionsmeta.md) | :heavy_check_mark:                                                   | Pagination metadata for the transactions response                    |
| `data`                                                               | List[[models.TransactionResponse](../models/transactionresponse.md)] | :heavy_check_mark:                                                   | Array of transactions matching the query criteria                    |