# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["WorkspaceUpdateResponse"]


class WorkspaceUpdateResponse(BaseModel):
    """Tenant schema."""

    id: str

    created_at: datetime

    display_name: str

    is_deleted: bool

    is_personal: bool

    data_plane_url: Optional[str] = None

    organization_id: Optional[str] = None

    tenant_handle: Optional[str] = None
