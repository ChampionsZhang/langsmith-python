# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["DirectoryCommitParams"]


class DirectoryCommitParams(TypedDict, total=False):
    owner: Required[str]

    files: Dict[str, object]
    """
    Files maps path to an Entry (object = create/update/link, null = delete/unlink).
    """

    parent_commit: str
