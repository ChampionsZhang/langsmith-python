# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from ..._types import SequenceNotStr

__all__ = [
    "BoxCreateParams",
    "ProxyConfig",
    "ProxyConfigAccessControl",
    "ProxyConfigCallback",
    "ProxyConfigCallbackRequestHeader",
    "ProxyConfigRule",
    "ProxyConfigRuleHeader",
]


class BoxCreateParams(TypedDict, total=False):
    delete_after_stop_seconds: int

    fs_capacity_bytes: int

    idle_ttl_seconds: int

    mem_bytes: int

    name: str

    proxy_config: ProxyConfig

    restore_memory: bool
    """
    RestoreMemory, when non-nil, overrides the server default for whether to resume
    the sandbox from its captured memory snapshot.

    true → resume from the memory snapshot if it exists; cold-boot the sandbox
    otherwise. false → always cold-boot, even if a memory snapshot exists. nil → use
    the server default.

    Applies to this request only; a later stop+start of the same sandbox reverts to
    the server default.
    """

    snapshot_id: str

    snapshot_name: str

    tag_value_ids: SequenceNotStr[str]

    vcpus: int


class ProxyConfigAccessControl(TypedDict, total=False):
    allow_list: SequenceNotStr[str]

    deny_list: SequenceNotStr[str]


class ProxyConfigCallbackRequestHeader(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["plaintext", "opaque", "workspace_secret"]]

    is_set: bool

    value: str


class ProxyConfigCallback(TypedDict, total=False):
    match_hosts: Required[SequenceNotStr[str]]

    ttl_seconds: Required[int]

    url: Required[str]

    full_request: bool

    request_headers: Iterable[ProxyConfigCallbackRequestHeader]


class ProxyConfigRuleHeader(TypedDict, total=False):
    name: Required[str]

    type: Required[Literal["plaintext", "opaque", "workspace_secret"]]

    is_set: bool

    value: str


class ProxyConfigRule(TypedDict, total=False):
    match_hosts: Required[SequenceNotStr[str]]

    name: Required[str]

    enabled: bool

    headers: Iterable[ProxyConfigRuleHeader]

    match_paths: SequenceNotStr[str]


class ProxyConfig(TypedDict, total=False):
    access_control: ProxyConfigAccessControl

    callbacks: Iterable[ProxyConfigCallback]

    no_proxy: SequenceNotStr[str]

    rules: Iterable[ProxyConfigRule]
