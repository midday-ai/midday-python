"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .revenuecurrent import RevenueCurrent, RevenueCurrentTypedDict
from .revenuepercentage import RevenuePercentage, RevenuePercentageTypedDict
from .revenueprevious import RevenuePrevious, RevenuePreviousTypedDict
from midday.types import BaseModel
import pydantic
from typing_extensions import Annotated, TypedDict


class RevenueResultItemTypedDict(TypedDict):
    date_: str
    r"""Date for the metric (ISO 8601)"""
    precentage: RevenuePercentageTypedDict
    current: RevenueCurrentTypedDict
    previous: RevenuePreviousTypedDict


class RevenueResultItem(BaseModel):
    date_: Annotated[str, pydantic.Field(alias="date")]
    r"""Date for the metric (ISO 8601)"""

    precentage: RevenuePercentage

    current: RevenueCurrent

    previous: RevenuePrevious
