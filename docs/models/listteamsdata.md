# ListTeamsData


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        | Example                                            |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `id`                                               | *str*                                              | :heavy_check_mark:                                 | Unique identifier of the team                      | 123e4567-e89b-12d3-a456-426614174000               |
| `name`                                             | *str*                                              | :heavy_check_mark:                                 | Name of the team or organization                   | Acme Corporation                                   |
| `logo_url`                                         | *Nullable[str]*                                    | :heavy_check_mark:                                 | URL to the team's logo image                       | https://cdn.midday.ai/logos/acme-corp.png          |
| `plan`                                             | [models.ListTeamsPlan](../models/listteamsplan.md) | :heavy_check_mark:                                 | Current subscription plan of the team              | pro                                                |