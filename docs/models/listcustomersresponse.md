# ListCustomersResponse

Retrieve a list of customers for the authenticated team.


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `meta`                                                           | [models.ListCustomersMeta](../models/listcustomersmeta.md)       | :heavy_check_mark:                                               | Pagination metadata for the customers response                   |
| `data`                                                           | List[[models.ListCustomersData](../models/listcustomersdata.md)] | :heavy_check_mark:                                               | Array of customers matching the query criteria                   |