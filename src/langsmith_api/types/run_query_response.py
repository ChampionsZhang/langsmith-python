# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel
from .run_schema import RunSchema

__all__ = ["RunQueryResponse"]


class RunQueryResponse(BaseModel):
    cursors: Dict[str, Optional[str]]

    runs: List[RunSchema]

    parsed_query: Optional[str] = None

    search_cursors: Optional[Dict[str, Optional[object]]] = None
