# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["WorkspaceCreateParams"]


class WorkspaceCreateParams(TypedDict, total=False):
    display_name: Required[str]

    id: str

    tenant_handle: Optional[str]
