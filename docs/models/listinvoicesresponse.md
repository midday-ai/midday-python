# ListInvoicesResponse

Response containing a list of invoices and pagination metadata


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `meta`                                                         | [models.ListInvoicesMeta](../models/listinvoicesmeta.md)       | :heavy_check_mark:                                             | Pagination metadata                                            |
| `data`                                                         | List[[models.ListInvoicesData](../models/listinvoicesdata.md)] | :heavy_check_mark:                                             | Array of invoice objects                                       |