# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = [
    "BoxListResponse",
    "Sandbox",
    "SandboxProxyConfig",
    "SandboxProxyConfigAccessControl",
    "SandboxProxyConfigCallback",
    "SandboxProxyConfigCallbackRequestHeader",
    "SandboxProxyConfigRule",
    "SandboxProxyConfigRuleHeader",
]


class SandboxProxyConfigAccessControl(BaseModel):
    allow_list: Optional[List[str]] = None

    deny_list: Optional[List[str]] = None


class SandboxProxyConfigCallbackRequestHeader(BaseModel):
    name: str

    type: Literal["plaintext", "opaque", "workspace_secret"]

    is_set: Optional[bool] = None

    value: Optional[str] = None


class SandboxProxyConfigCallback(BaseModel):
    match_hosts: List[str]

    ttl_seconds: int

    url: str

    full_request: Optional[bool] = None

    request_headers: Optional[List[SandboxProxyConfigCallbackRequestHeader]] = None


class SandboxProxyConfigRuleHeader(BaseModel):
    name: str

    type: Literal["plaintext", "opaque", "workspace_secret"]

    is_set: Optional[bool] = None

    value: Optional[str] = None


class SandboxProxyConfigRule(BaseModel):
    match_hosts: List[str]

    name: str

    enabled: Optional[bool] = None

    headers: Optional[List[SandboxProxyConfigRuleHeader]] = None

    match_paths: Optional[List[str]] = None


class SandboxProxyConfig(BaseModel):
    access_control: Optional[SandboxProxyConfigAccessControl] = None

    callbacks: Optional[List[SandboxProxyConfigCallback]] = None

    no_proxy: Optional[List[str]] = None

    rules: Optional[List[SandboxProxyConfigRule]] = None


class Sandbox(BaseModel):
    id: Optional[str] = None

    created_at: Optional[str] = None

    created_by: Optional[str] = None

    dataplane_url: Optional[str] = None

    delete_after_stop_seconds: Optional[int] = None

    fs_capacity_bytes: Optional[int] = None

    idle_ttl_seconds: Optional[int] = None

    mem_bytes: Optional[int] = None

    name: Optional[str] = None

    proxy_config: Optional[SandboxProxyConfig] = None

    size_class: Optional[str] = None

    snapshot_id: Optional[str] = None

    status: Optional[str] = None

    status_message: Optional[str] = None

    stopped_at: Optional[str] = None

    updated_at: Optional[str] = None

    updated_by: Optional[str] = None

    vcpus: Optional[int] = None


class BoxListResponse(BaseModel):
    offset: Optional[int] = None

    sandboxes: Optional[List[Sandbox]] = None
