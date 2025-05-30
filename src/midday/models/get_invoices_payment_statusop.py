"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from midday.types import BaseModel
import pydantic
from typing_extensions import Annotated, TypedDict


class GetInvoicesPaymentStatusResponseTypedDict(TypedDict):
    r"""Payment status for the authenticated team."""

    score: float
    r"""Score associated with the invoice payment status"""
    payment_status: str
    r"""The payment status of the invoice"""


class GetInvoicesPaymentStatusResponse(BaseModel):
    r"""Payment status for the authenticated team."""

    score: float
    r"""Score associated with the invoice payment status"""

    payment_status: Annotated[str, pydantic.Field(alias="paymentStatus")]
    r"""The payment status of the invoice"""
