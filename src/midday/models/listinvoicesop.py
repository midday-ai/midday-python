"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from midday.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from midday.utils import FieldMetadata, QueryParamMetadata
import pydantic
from pydantic import model_serializer
from typing import List, Optional
from typing_extensions import Annotated, NotRequired, TypedDict


class ListInvoicesRequestTypedDict(TypedDict):
    cursor: NotRequired[Nullable[str]]
    sort: NotRequired[Nullable[List[str]]]
    page_size: NotRequired[float]
    q: NotRequired[Nullable[str]]
    start: NotRequired[Nullable[str]]
    end: NotRequired[Nullable[str]]
    statuses: NotRequired[Nullable[List[str]]]
    customers: NotRequired[Nullable[List[str]]]


class ListInvoicesRequest(BaseModel):
    cursor: Annotated[
        OptionalNullable[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET

    sort: Annotated[
        OptionalNullable[List[str]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET

    page_size: Annotated[
        Optional[float],
        pydantic.Field(alias="pageSize"),
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = None

    q: Annotated[
        OptionalNullable[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET

    start: Annotated[
        OptionalNullable[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET

    end: Annotated[
        OptionalNullable[str],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET

    statuses: Annotated[
        OptionalNullable[List[str]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET

    customers: Annotated[
        OptionalNullable[List[str]],
        FieldMetadata(query=QueryParamMetadata(style="form", explode=True)),
    ] = UNSET

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = [
            "cursor",
            "sort",
            "pageSize",
            "q",
            "start",
            "end",
            "statuses",
            "customers",
        ]
        nullable_fields = [
            "cursor",
            "sort",
            "q",
            "start",
            "end",
            "statuses",
            "customers",
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


class ListInvoicesMetaTypedDict(TypedDict):
    r"""Pagination metadata"""

    cursor: Nullable[str]
    r"""Cursor for pagination; null if there is no next page"""
    has_previous_page: bool
    r"""Indicates if there is a previous page of results"""
    has_next_page: bool
    r"""Indicates if there is a next page of results"""


class ListInvoicesMeta(BaseModel):
    r"""Pagination metadata"""

    cursor: Nullable[str]
    r"""Cursor for pagination; null if there is no next page"""

    has_previous_page: Annotated[bool, pydantic.Field(alias="hasPreviousPage")]
    r"""Indicates if there is a previous page of results"""

    has_next_page: Annotated[bool, pydantic.Field(alias="hasNextPage")]
    r"""Indicates if there is a next page of results"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["cursor"]
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


class ListInvoicesStatus(str, Enum):
    r"""Current status of the invoice"""

    DRAFT = "draft"
    OVERDUE = "overdue"
    PAID = "paid"
    UNPAID = "unpaid"
    CANCELED = "canceled"


class ListInvoicesCustomerTypedDict(TypedDict):
    r"""Customer details"""

    id: str
    r"""Unique identifier for the customer"""
    name: str
    r"""Name of the customer"""
    website: Nullable[str]
    r"""Website URL of the customer"""
    email: Nullable[str]
    r"""Email address of the customer"""


class ListInvoicesCustomer(BaseModel):
    r"""Customer details"""

    id: str
    r"""Unique identifier for the customer"""

    name: str
    r"""Name of the customer"""

    website: Nullable[str]
    r"""Website URL of the customer"""

    email: Nullable[str]
    r"""Email address of the customer"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = ["website", "email"]
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


class ListInvoicesDataTypedDict(TypedDict):
    r"""Invoice object"""

    id: str
    r"""Unique identifier for the invoice"""
    status: ListInvoicesStatus
    r"""Current status of the invoice"""
    due_date: str
    r"""Due date of the invoice in ISO 8601 format"""
    issue_date: str
    r"""Issue date of the invoice in ISO 8601 format"""
    invoice_number: str
    r"""Invoice number as shown to the customer"""
    amount: float
    r"""Total amount of the invoice"""
    currency: str
    r"""Currency code (ISO 4217) for the invoice amount"""
    customer: ListInvoicesCustomerTypedDict
    r"""Customer details"""
    paid_at: Nullable[str]
    r"""Timestamp when the invoice was paid (ISO 8601), or null if unpaid"""
    reminder_sent_at: Nullable[str]
    r"""Timestamp when a payment reminder was sent (ISO 8601), or null if never sent"""
    note: Nullable[str]
    r"""Optional note attached to the invoice"""
    vat: Nullable[float]
    r"""Value-added tax amount, or null if not applicable"""
    tax: Nullable[float]
    r"""Tax amount, or null if not applicable"""
    discount: Nullable[float]
    r"""Discount amount applied to the invoice, or null if none"""
    subtotal: Nullable[float]
    r"""Subtotal before taxes and discounts, or null if not calculated"""
    viewed_at: Nullable[str]
    r"""Timestamp when the invoice was viewed by the customer (ISO 8601), or null if never viewed"""
    customer_name: Nullable[str]
    r"""Name of the customer as shown on the invoice, or null if not set"""
    sent_to: Nullable[str]
    r"""Email address to which the invoice was sent, or null if not sent"""
    sent_at: Nullable[str]
    r"""Timestamp when the invoice was sent (ISO 8601), or null if not sent"""
    created_at: str
    r"""Timestamp when the invoice was created (ISO 8601)"""
    updated_at: str
    r"""Timestamp when the invoice was last updated (ISO 8601)"""


class ListInvoicesData(BaseModel):
    r"""Invoice object"""

    id: str
    r"""Unique identifier for the invoice"""

    status: ListInvoicesStatus
    r"""Current status of the invoice"""

    due_date: Annotated[str, pydantic.Field(alias="dueDate")]
    r"""Due date of the invoice in ISO 8601 format"""

    issue_date: Annotated[str, pydantic.Field(alias="issueDate")]
    r"""Issue date of the invoice in ISO 8601 format"""

    invoice_number: Annotated[str, pydantic.Field(alias="invoiceNumber")]
    r"""Invoice number as shown to the customer"""

    amount: float
    r"""Total amount of the invoice"""

    currency: str
    r"""Currency code (ISO 4217) for the invoice amount"""

    customer: ListInvoicesCustomer
    r"""Customer details"""

    paid_at: Annotated[Nullable[str], pydantic.Field(alias="paidAt")]
    r"""Timestamp when the invoice was paid (ISO 8601), or null if unpaid"""

    reminder_sent_at: Annotated[Nullable[str], pydantic.Field(alias="reminderSentAt")]
    r"""Timestamp when a payment reminder was sent (ISO 8601), or null if never sent"""

    note: Nullable[str]
    r"""Optional note attached to the invoice"""

    vat: Nullable[float]
    r"""Value-added tax amount, or null if not applicable"""

    tax: Nullable[float]
    r"""Tax amount, or null if not applicable"""

    discount: Nullable[float]
    r"""Discount amount applied to the invoice, or null if none"""

    subtotal: Nullable[float]
    r"""Subtotal before taxes and discounts, or null if not calculated"""

    viewed_at: Annotated[Nullable[str], pydantic.Field(alias="viewedAt")]
    r"""Timestamp when the invoice was viewed by the customer (ISO 8601), or null if never viewed"""

    customer_name: Annotated[Nullable[str], pydantic.Field(alias="customerName")]
    r"""Name of the customer as shown on the invoice, or null if not set"""

    sent_to: Annotated[Nullable[str], pydantic.Field(alias="sentTo")]
    r"""Email address to which the invoice was sent, or null if not sent"""

    sent_at: Annotated[Nullable[str], pydantic.Field(alias="sentAt")]
    r"""Timestamp when the invoice was sent (ISO 8601), or null if not sent"""

    created_at: Annotated[str, pydantic.Field(alias="createdAt")]
    r"""Timestamp when the invoice was created (ISO 8601)"""

    updated_at: Annotated[str, pydantic.Field(alias="updatedAt")]
    r"""Timestamp when the invoice was last updated (ISO 8601)"""

    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = []
        nullable_fields = [
            "paidAt",
            "reminderSentAt",
            "note",
            "vat",
            "tax",
            "discount",
            "subtotal",
            "viewedAt",
            "customerName",
            "sentTo",
            "sentAt",
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


class ListInvoicesResponseTypedDict(TypedDict):
    r"""Response containing a list of invoices and pagination metadata"""

    meta: ListInvoicesMetaTypedDict
    r"""Pagination metadata"""
    data: List[ListInvoicesDataTypedDict]
    r"""Array of invoice objects"""


class ListInvoicesResponse(BaseModel):
    r"""Response containing a list of invoices and pagination metadata"""

    meta: ListInvoicesMeta
    r"""Pagination metadata"""

    data: List[ListInvoicesData]
    r"""Array of invoice objects"""
