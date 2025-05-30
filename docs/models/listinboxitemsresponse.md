# ListInboxItemsResponse

Retrieve a list of inbox items for the authenticated team.


## Fields

| Field                                                              | Type                                                               | Required                                                           | Description                                                        |
| ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ |
| `meta`                                                             | [models.ListInboxItemsMeta](../models/listinboxitemsmeta.md)       | :heavy_check_mark:                                                 | Pagination metadata for the inbox list response.                   |
| `data`                                                             | List[[models.ListInboxItemsData](../models/listinboxitemsdata.md)] | :heavy_check_mark:                                                 | List of inbox items                                                |