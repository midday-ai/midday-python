"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from midday.types import BaseModel, Nullable, UNSET_SENTINEL
import pydantic
from pydantic import model_serializer
from typing import Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class DateFormatRequest(str, Enum):
    r"""User's preferred date format. Available options: 'dd/MM/yyyy', 'MM/dd/yyyy', 'yyyy-MM-dd', 'dd.MM.yyyy'"""

    DD_SLASH_MM_SLASHYYYY = "dd/MM/yyyy"
    MM_SLASHDD_SLASHYYYY = "MM/dd/yyyy"
    YYYY_DASH_MM_DASHDD = "yyyy-MM-dd"
    DD_DOT_MM_DOTYYYY = "dd.MM.yyyy"


class UpdateCurrentUserRequestTypedDict(TypedDict):
    full_name: NotRequired[str]
    r"""Full name of the user. Must be between 2 and 32 characters"""
    team_id: NotRequired[str]
    r"""Unique identifier of the team the user belongs to"""
    email: NotRequired[str]
    r"""Email address of the user"""
    avatar_url: NotRequired[str]
    r"""URL to the user's avatar image. Must be hosted on midday.ai domain"""
    locale: NotRequired[str]
    r"""User's preferred locale for internationalization (language and region)"""
    week_starts_on_monday: NotRequired[bool]
    r"""Whether the user's calendar week starts on Monday (true) or Sunday (false)"""
    timezone: NotRequired[str]
    r"""User's timezone identifier in IANA Time Zone Database format"""
    time_format: NotRequired[float]
    r"""User's preferred time format: 12 for 12-hour format, 24 for 24-hour format"""
    date_format: NotRequired[DateFormatRequest]
    r"""User's preferred date format. Available options: 'dd/MM/yyyy', 'MM/dd/yyyy', 'yyyy-MM-dd', 'dd.MM.yyyy'"""


class UpdateCurrentUserRequest(BaseModel):
    full_name: Annotated[Optional[str], pydantic.Field(alias="fullName")] = None
    r"""Full name of the user. Must be between 2 and 32 characters"""

    team_id: Annotated[Optional[str], pydantic.Field(alias="teamId")] = None
    r"""Unique identifier of the team the user belongs to"""

    email: Optional[str] = None
    r"""Email address of the user"""

    avatar_url: Annotated[Optional[str], pydantic.Field(alias="avatarUrl")] = None
    r"""URL to the user's avatar image. Must be hosted on midday.ai domain"""

    locale: Optional[str] = None
    r"""User's preferred locale for internationalization (language and region)"""

    week_starts_on_monday: Annotated[
        Optional[bool], pydantic.Field(alias="weekStartsOnMonday")
    ] = None
    r"""Whether the user's calendar week starts on Monday (true) or Sunday (false)"""

    timezone: Optional[str] = None
    r"""User's timezone identifier in IANA Time Zone Database format"""

    time_format: Annotated[Optional[float], pydantic.Field(alias="timeFormat")] = None
    r"""User's preferred time format: 12 for 12-hour format, 24 for 24-hour format"""

    date_format: Annotated[
        Optional[DateFormatRequest], pydantic.Field(alias="dateFormat")
    ] = None
    r"""User's preferred date format. Available options: 'dd/MM/yyyy', 'MM/dd/yyyy', 'yyyy-MM-dd', 'dd.MM.yyyy'"""


class UpdateCurrentUserDateFormatResponse(str, Enum):
    r"""User's preferred date format. Available options: 'dd/MM/yyyy', 'MM/dd/yyyy', 'yyyy-MM-dd', 'dd.MM.yyyy'"""

    DD_SLASH_MM_SLASHYYYY = "dd/MM/yyyy"
    MM_SLASHDD_SLASHYYYY = "MM/dd/yyyy"
    YYYY_DASH_MM_DASHDD = "yyyy-MM-dd"
    DD_DOT_MM_DOTYYYY = "dd.MM.yyyy"


class UpdateCurrentUserTeamTypedDict(TypedDict):
    r"""Team information that the user belongs to"""

    id: str
    r"""Unique identifier of the team"""
    name: str
    r"""Name of the team or organization"""
    logo_url: str
    r"""URL to the team's logo image"""
    plan: str
    r"""Current subscription plan of the team"""


class UpdateCurrentUserTeam(BaseModel):
    r"""Team information that the user belongs to"""

    id: str
    r"""Unique identifier of the team"""

    name: str
    r"""Name of the team or organization"""

    logo_url: Annotated[str, pydantic.Field(alias="logoUrl")]
    r"""URL to the team's logo image"""

    plan: str
    r"""Current subscription plan of the team"""


class UpdateCurrentUserResponseTypedDict(TypedDict):
    r"""The updated user"""

    id: str
    r"""Unique identifier of the user"""
    full_name: str
    r"""Full name of the user"""
    email: str
    r"""Email address of the user"""
    avatar_url: Nullable[str]
    r"""URL to the user's avatar image"""
    locale: Nullable[str]
    r"""User's preferred locale for internationalization (language and region)"""
    week_starts_on_monday: Nullable[bool]
    r"""Whether the user's calendar week starts on Monday (true) or Sunday (false)"""
    timezone: Nullable[str]
    r"""User's timezone identifier in IANA Time Zone Database format"""
    time_format: Nullable[float]
    r"""User's preferred time format: 12 for 12-hour format, 24 for 24-hour format"""
    date_format: Nullable[UpdateCurrentUserDateFormatResponse]
    r"""User's preferred date format. Available options: 'dd/MM/yyyy', 'MM/dd/yyyy', 'yyyy-MM-dd', 'dd.MM.yyyy'"""
    team: Nullable[UpdateCurrentUserTeamTypedDict]
    r"""Team information that the user belongs to"""


class UpdateCurrentUserResponse(BaseModel):
    r"""The updated user"""

    id: str
    r"""Unique identifier of the user"""

    full_name: Annotated[str, pydantic.Field(alias="fullName")]
    r"""Full name of the user"""

    email: str
    r"""Email address of the user"""

    avatar_url: Annotated[Nullable[str], pydantic.Field(alias="avatarUrl")]
    r"""URL to the user's avatar image"""

    locale: Nullable[str]
    r"""User's preferred locale for internationalization (language and region)"""

    week_starts_on_monday: Annotated[
        Nullable[bool], pydantic.Field(alias="weekStartsOnMonday")
    ]
    r"""Whether the user's calendar week starts on Monday (true) or Sunday (false)"""

    timezone: Nullable[str]
    r"""User's timezone identifier in IANA Time Zone Database format"""

    time_format: Annotated[Nullable[float], pydantic.Field(alias="timeFormat")]
    r"""User's preferred time format: 12 for 12-hour format, 24 for 24-hour format"""

    date_format: Annotated[
        Nullable[UpdateCurrentUserDateFormatResponse],
        pydantic.Field(alias="dateFormat"),
    ]
    r"""User's preferred date format. Available options: 'dd/MM/yyyy', 'MM/dd/yyyy', 'yyyy-MM-dd', 'dd.MM.yyyy'"""

    team: Nullable[UpdateCurrentUserTeam]
    r"""Team information that the user belongs to"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = [
            "avatarUrl",
            "locale",
            "weekStartsOnMonday",
            "timezone",
            "timeFormat",
            "dateFormat",
            "team",
        ]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in type(self).model_fields.items():
            k = f.alias or n
            val = serialized.get(k)
            serialized.pop(k, None)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (
                self.__pydantic_fields_set__.intersection({n})
                or k in null_default_fields
            )  # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
