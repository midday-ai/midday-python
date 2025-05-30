# ListDocumentsResponse

Response containing a list of documents and pagination metadata.


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `meta`                                                           | [models.ListDocumentsMeta](../models/listdocumentsmeta.md)       | :heavy_check_mark:                                               | Pagination metadata for the documents list.                      |
| `data`                                                           | List[[models.ListDocumentsData](../models/listdocumentsdata.md)] | :heavy_check_mark:                                               | Array of document objects.                                       |