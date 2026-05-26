# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ..._models import BaseModel

__all__ = ["DirectoryListResponse"]


class DirectoryListResponse(BaseModel):
    commit_hash: Optional[str] = None

    commit_id: Optional[str] = None

    files: Optional[Dict[str, object]] = None
