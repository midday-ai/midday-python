# ListTransactionsResponse

Retrieve a list of transactions for the authenticated team.


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `meta`                                                               | [models.ListTransactionsMeta](../models/listtransactionsmeta.md)     | :heavy_check_mark:                                                   | Pagination metadata for the transactions response                    |
| `data`                                                               | List[[models.TransactionResponse](../models/transactionresponse.md)] | :heavy_check_mark:                                                   | Array of transactions matching the query criteria                    |