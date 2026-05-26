# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["WorkspaceListResponse", "WorkspaceListResponseItem"]


class WorkspaceListResponseItem(BaseModel):
    id: str

    created_at: datetime

    display_name: str

    is_deleted: bool

    is_personal: bool

    data_plane_url: Optional[str] = None

    organization_id: Optional[str] = None

    permissions: Optional[List[str]] = None

    read_only: Optional[bool] = None

    role_id: Optional[str] = None

    role_name: Optional[str] = None

    tenant_handle: Optional[str] = None


WorkspaceListResponse: TypeAlias = List[WorkspaceListResponseItem]
