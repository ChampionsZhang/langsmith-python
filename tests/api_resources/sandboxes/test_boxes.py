# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from langsmith_api import Langsmith, AsyncLangsmith
from langsmith_api.types.sandboxes import (
    BoxListResponse,
    BoxStartResponse,
    BoxCreateResponse,
    BoxUpdateResponse,
    BoxRetrieveResponse,
    BoxGetStatusResponse,
    BoxCreateSnapshotResponse,
    BoxGenerateServiceURLResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBoxes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Langsmith) -> None:
        box = client.sandboxes.boxes.create()
        assert_matches_type(BoxCreateResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Langsmith) -> None:
        box = client.sandboxes.boxes.create(
            delete_after_stop_seconds=0,
            fs_capacity_bytes=0,
            idle_ttl_seconds=0,
            mem_bytes=0,
            name="name",
            proxy_config={
                "access_control": {
                    "allow_list": ["string"],
                    "deny_list": ["string"],
                },
                "callbacks": [
                    {
                        "match_hosts": ["string"],
                        "ttl_seconds": 60,
                        "url": "url",
                        "full_request": True,
                        "request_headers": [
                            {
                                "name": "name",
                                "type": "plaintext",
                                "is_set": True,
                                "value": "value",
                            }
                        ],
                    }
                ],
                "no_proxy": ["string"],
                "rules": [
                    {
                        "match_hosts": ["string"],
                        "name": "name",
                        "enabled": True,
                        "headers": [
                            {
                                "name": "name",
                                "type": "plaintext",
                                "is_set": True,
                                "value": "value",
                            }
                        ],
                        "match_paths": ["string"],
                    }
                ],
            },
            restore_memory=True,
            snapshot_id="snapshot_id",
            snapshot_name="snapshot_name",
            tag_value_ids=["string"],
            vcpus=0,
        )
        assert_matches_type(BoxCreateResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Langsmith) -> None:
        response = client.sandboxes.boxes.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = response.parse()
        assert_matches_type(BoxCreateResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Langsmith) -> None:
        with client.sandboxes.boxes.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = response.parse()
            assert_matches_type(BoxCreateResponse, box, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Langsmith) -> None:
        box = client.sandboxes.boxes.retrieve(
            "name",
        )
        assert_matches_type(BoxRetrieveResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Langsmith) -> None:
        response = client.sandboxes.boxes.with_raw_response.retrieve(
            "name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = response.parse()
        assert_matches_type(BoxRetrieveResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Langsmith) -> None:
        with client.sandboxes.boxes.with_streaming_response.retrieve(
            "name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = response.parse()
            assert_matches_type(BoxRetrieveResponse, box, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.sandboxes.boxes.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Langsmith) -> None:
        box = client.sandboxes.boxes.update(
            path_name="name",
        )
        assert_matches_type(BoxUpdateResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Langsmith) -> None:
        box = client.sandboxes.boxes.update(
            path_name="name",
            delete_after_stop_seconds=0,
            fs_capacity_bytes=0,
            idle_ttl_seconds=0,
            mem_bytes=0,
            body_name="name",
            proxy_config={
                "access_control": {
                    "allow_list": ["string"],
                    "deny_list": ["string"],
                },
                "callbacks": [
                    {
                        "match_hosts": ["string"],
                        "ttl_seconds": 60,
                        "url": "url",
                        "full_request": True,
                        "request_headers": [
                            {
                                "name": "name",
                                "type": "plaintext",
                                "is_set": True,
                                "value": "value",
                            }
                        ],
                    }
                ],
                "no_proxy": ["string"],
                "rules": [
                    {
                        "match_hosts": ["string"],
                        "name": "name",
                        "enabled": True,
                        "headers": [
                            {
                                "name": "name",
                                "type": "plaintext",
                                "is_set": True,
                                "value": "value",
                            }
                        ],
                        "match_paths": ["string"],
                    }
                ],
            },
            tag_value_ids=["string"],
            vcpus=0,
        )
        assert_matches_type(BoxUpdateResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Langsmith) -> None:
        response = client.sandboxes.boxes.with_raw_response.update(
            path_name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = response.parse()
        assert_matches_type(BoxUpdateResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Langsmith) -> None:
        with client.sandboxes.boxes.with_streaming_response.update(
            path_name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = response.parse()
            assert_matches_type(BoxUpdateResponse, box, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_name` but received ''"):
            client.sandboxes.boxes.with_raw_response.update(
                path_name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Langsmith) -> None:
        box = client.sandboxes.boxes.list()
        assert_matches_type(BoxListResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Langsmith) -> None:
        box = client.sandboxes.boxes.list(
            limit=0,
            name_contains="name_contains",
            offset=0,
            sort_by="sort_by",
            sort_direction="sort_direction",
            status="status",
        )
        assert_matches_type(BoxListResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Langsmith) -> None:
        response = client.sandboxes.boxes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = response.parse()
        assert_matches_type(BoxListResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Langsmith) -> None:
        with client.sandboxes.boxes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = response.parse()
            assert_matches_type(BoxListResponse, box, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Langsmith) -> None:
        box = client.sandboxes.boxes.delete(
            "name",
        )
        assert box is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Langsmith) -> None:
        response = client.sandboxes.boxes.with_raw_response.delete(
            "name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = response.parse()
        assert box is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Langsmith) -> None:
        with client.sandboxes.boxes.with_streaming_response.delete(
            "name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = response.parse()
            assert box is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.sandboxes.boxes.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_snapshot(self, client: Langsmith) -> None:
        box = client.sandboxes.boxes.create_snapshot(
            path_name="name",
            body_name="name",
        )
        assert_matches_type(BoxCreateSnapshotResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_snapshot_with_all_params(self, client: Langsmith) -> None:
        box = client.sandboxes.boxes.create_snapshot(
            path_name="name",
            body_name="name",
            checkpoint="checkpoint",
            include_memory=True,
        )
        assert_matches_type(BoxCreateSnapshotResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create_snapshot(self, client: Langsmith) -> None:
        response = client.sandboxes.boxes.with_raw_response.create_snapshot(
            path_name="name",
            body_name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = response.parse()
        assert_matches_type(BoxCreateSnapshotResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create_snapshot(self, client: Langsmith) -> None:
        with client.sandboxes.boxes.with_streaming_response.create_snapshot(
            path_name="name",
            body_name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = response.parse()
            assert_matches_type(BoxCreateSnapshotResponse, box, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create_snapshot(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_name` but received ''"):
            client.sandboxes.boxes.with_raw_response.create_snapshot(
                path_name="",
                body_name="name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_generate_service_url(self, client: Langsmith) -> None:
        box = client.sandboxes.boxes.generate_service_url(
            name="name",
        )
        assert_matches_type(BoxGenerateServiceURLResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_generate_service_url_with_all_params(self, client: Langsmith) -> None:
        box = client.sandboxes.boxes.generate_service_url(
            name="name",
            expires_in_seconds=0,
            port=0,
        )
        assert_matches_type(BoxGenerateServiceURLResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_generate_service_url(self, client: Langsmith) -> None:
        response = client.sandboxes.boxes.with_raw_response.generate_service_url(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = response.parse()
        assert_matches_type(BoxGenerateServiceURLResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_generate_service_url(self, client: Langsmith) -> None:
        with client.sandboxes.boxes.with_streaming_response.generate_service_url(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = response.parse()
            assert_matches_type(BoxGenerateServiceURLResponse, box, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_generate_service_url(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.sandboxes.boxes.with_raw_response.generate_service_url(
                name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_status(self, client: Langsmith) -> None:
        box = client.sandboxes.boxes.get_status(
            "name",
        )
        assert_matches_type(BoxGetStatusResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_status(self, client: Langsmith) -> None:
        response = client.sandboxes.boxes.with_raw_response.get_status(
            "name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = response.parse()
        assert_matches_type(BoxGetStatusResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_status(self, client: Langsmith) -> None:
        with client.sandboxes.boxes.with_streaming_response.get_status(
            "name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = response.parse()
            assert_matches_type(BoxGetStatusResponse, box, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_status(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.sandboxes.boxes.with_raw_response.get_status(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_start(self, client: Langsmith) -> None:
        box = client.sandboxes.boxes.start(
            "name",
        )
        assert_matches_type(BoxStartResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_start(self, client: Langsmith) -> None:
        response = client.sandboxes.boxes.with_raw_response.start(
            "name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = response.parse()
        assert_matches_type(BoxStartResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_start(self, client: Langsmith) -> None:
        with client.sandboxes.boxes.with_streaming_response.start(
            "name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = response.parse()
            assert_matches_type(BoxStartResponse, box, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_start(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.sandboxes.boxes.with_raw_response.start(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stop(self, client: Langsmith) -> None:
        box = client.sandboxes.boxes.stop(
            "name",
        )
        assert box is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_stop(self, client: Langsmith) -> None:
        response = client.sandboxes.boxes.with_raw_response.stop(
            "name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = response.parse()
        assert box is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_stop(self, client: Langsmith) -> None:
        with client.sandboxes.boxes.with_streaming_response.stop(
            "name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = response.parse()
            assert box is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_stop(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            client.sandboxes.boxes.with_raw_response.stop(
                "",
            )


class TestAsyncBoxes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLangsmith) -> None:
        box = await async_client.sandboxes.boxes.create()
        assert_matches_type(BoxCreateResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLangsmith) -> None:
        box = await async_client.sandboxes.boxes.create(
            delete_after_stop_seconds=0,
            fs_capacity_bytes=0,
            idle_ttl_seconds=0,
            mem_bytes=0,
            name="name",
            proxy_config={
                "access_control": {
                    "allow_list": ["string"],
                    "deny_list": ["string"],
                },
                "callbacks": [
                    {
                        "match_hosts": ["string"],
                        "ttl_seconds": 60,
                        "url": "url",
                        "full_request": True,
                        "request_headers": [
                            {
                                "name": "name",
                                "type": "plaintext",
                                "is_set": True,
                                "value": "value",
                            }
                        ],
                    }
                ],
                "no_proxy": ["string"],
                "rules": [
                    {
                        "match_hosts": ["string"],
                        "name": "name",
                        "enabled": True,
                        "headers": [
                            {
                                "name": "name",
                                "type": "plaintext",
                                "is_set": True,
                                "value": "value",
                            }
                        ],
                        "match_paths": ["string"],
                    }
                ],
            },
            restore_memory=True,
            snapshot_id="snapshot_id",
            snapshot_name="snapshot_name",
            tag_value_ids=["string"],
            vcpus=0,
        )
        assert_matches_type(BoxCreateResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.sandboxes.boxes.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = await response.parse()
        assert_matches_type(BoxCreateResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLangsmith) -> None:
        async with async_client.sandboxes.boxes.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = await response.parse()
            assert_matches_type(BoxCreateResponse, box, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLangsmith) -> None:
        box = await async_client.sandboxes.boxes.retrieve(
            "name",
        )
        assert_matches_type(BoxRetrieveResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.sandboxes.boxes.with_raw_response.retrieve(
            "name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = await response.parse()
        assert_matches_type(BoxRetrieveResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLangsmith) -> None:
        async with async_client.sandboxes.boxes.with_streaming_response.retrieve(
            "name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = await response.parse()
            assert_matches_type(BoxRetrieveResponse, box, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.sandboxes.boxes.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncLangsmith) -> None:
        box = await async_client.sandboxes.boxes.update(
            path_name="name",
        )
        assert_matches_type(BoxUpdateResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLangsmith) -> None:
        box = await async_client.sandboxes.boxes.update(
            path_name="name",
            delete_after_stop_seconds=0,
            fs_capacity_bytes=0,
            idle_ttl_seconds=0,
            mem_bytes=0,
            body_name="name",
            proxy_config={
                "access_control": {
                    "allow_list": ["string"],
                    "deny_list": ["string"],
                },
                "callbacks": [
                    {
                        "match_hosts": ["string"],
                        "ttl_seconds": 60,
                        "url": "url",
                        "full_request": True,
                        "request_headers": [
                            {
                                "name": "name",
                                "type": "plaintext",
                                "is_set": True,
                                "value": "value",
                            }
                        ],
                    }
                ],
                "no_proxy": ["string"],
                "rules": [
                    {
                        "match_hosts": ["string"],
                        "name": "name",
                        "enabled": True,
                        "headers": [
                            {
                                "name": "name",
                                "type": "plaintext",
                                "is_set": True,
                                "value": "value",
                            }
                        ],
                        "match_paths": ["string"],
                    }
                ],
            },
            tag_value_ids=["string"],
            vcpus=0,
        )
        assert_matches_type(BoxUpdateResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.sandboxes.boxes.with_raw_response.update(
            path_name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = await response.parse()
        assert_matches_type(BoxUpdateResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLangsmith) -> None:
        async with async_client.sandboxes.boxes.with_streaming_response.update(
            path_name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = await response.parse()
            assert_matches_type(BoxUpdateResponse, box, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_name` but received ''"):
            await async_client.sandboxes.boxes.with_raw_response.update(
                path_name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLangsmith) -> None:
        box = await async_client.sandboxes.boxes.list()
        assert_matches_type(BoxListResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLangsmith) -> None:
        box = await async_client.sandboxes.boxes.list(
            limit=0,
            name_contains="name_contains",
            offset=0,
            sort_by="sort_by",
            sort_direction="sort_direction",
            status="status",
        )
        assert_matches_type(BoxListResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.sandboxes.boxes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = await response.parse()
        assert_matches_type(BoxListResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLangsmith) -> None:
        async with async_client.sandboxes.boxes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = await response.parse()
            assert_matches_type(BoxListResponse, box, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLangsmith) -> None:
        box = await async_client.sandboxes.boxes.delete(
            "name",
        )
        assert box is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.sandboxes.boxes.with_raw_response.delete(
            "name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = await response.parse()
        assert box is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLangsmith) -> None:
        async with async_client.sandboxes.boxes.with_streaming_response.delete(
            "name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = await response.parse()
            assert box is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.sandboxes.boxes.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_snapshot(self, async_client: AsyncLangsmith) -> None:
        box = await async_client.sandboxes.boxes.create_snapshot(
            path_name="name",
            body_name="name",
        )
        assert_matches_type(BoxCreateSnapshotResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_snapshot_with_all_params(self, async_client: AsyncLangsmith) -> None:
        box = await async_client.sandboxes.boxes.create_snapshot(
            path_name="name",
            body_name="name",
            checkpoint="checkpoint",
            include_memory=True,
        )
        assert_matches_type(BoxCreateSnapshotResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create_snapshot(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.sandboxes.boxes.with_raw_response.create_snapshot(
            path_name="name",
            body_name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = await response.parse()
        assert_matches_type(BoxCreateSnapshotResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create_snapshot(self, async_client: AsyncLangsmith) -> None:
        async with async_client.sandboxes.boxes.with_streaming_response.create_snapshot(
            path_name="name",
            body_name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = await response.parse()
            assert_matches_type(BoxCreateSnapshotResponse, box, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create_snapshot(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `path_name` but received ''"):
            await async_client.sandboxes.boxes.with_raw_response.create_snapshot(
                path_name="",
                body_name="name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_generate_service_url(self, async_client: AsyncLangsmith) -> None:
        box = await async_client.sandboxes.boxes.generate_service_url(
            name="name",
        )
        assert_matches_type(BoxGenerateServiceURLResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_generate_service_url_with_all_params(self, async_client: AsyncLangsmith) -> None:
        box = await async_client.sandboxes.boxes.generate_service_url(
            name="name",
            expires_in_seconds=0,
            port=0,
        )
        assert_matches_type(BoxGenerateServiceURLResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_generate_service_url(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.sandboxes.boxes.with_raw_response.generate_service_url(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = await response.parse()
        assert_matches_type(BoxGenerateServiceURLResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_generate_service_url(self, async_client: AsyncLangsmith) -> None:
        async with async_client.sandboxes.boxes.with_streaming_response.generate_service_url(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = await response.parse()
            assert_matches_type(BoxGenerateServiceURLResponse, box, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_generate_service_url(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.sandboxes.boxes.with_raw_response.generate_service_url(
                name="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_status(self, async_client: AsyncLangsmith) -> None:
        box = await async_client.sandboxes.boxes.get_status(
            "name",
        )
        assert_matches_type(BoxGetStatusResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_status(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.sandboxes.boxes.with_raw_response.get_status(
            "name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = await response.parse()
        assert_matches_type(BoxGetStatusResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_status(self, async_client: AsyncLangsmith) -> None:
        async with async_client.sandboxes.boxes.with_streaming_response.get_status(
            "name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = await response.parse()
            assert_matches_type(BoxGetStatusResponse, box, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_status(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.sandboxes.boxes.with_raw_response.get_status(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_start(self, async_client: AsyncLangsmith) -> None:
        box = await async_client.sandboxes.boxes.start(
            "name",
        )
        assert_matches_type(BoxStartResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_start(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.sandboxes.boxes.with_raw_response.start(
            "name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = await response.parse()
        assert_matches_type(BoxStartResponse, box, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_start(self, async_client: AsyncLangsmith) -> None:
        async with async_client.sandboxes.boxes.with_streaming_response.start(
            "name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = await response.parse()
            assert_matches_type(BoxStartResponse, box, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_start(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.sandboxes.boxes.with_raw_response.start(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stop(self, async_client: AsyncLangsmith) -> None:
        box = await async_client.sandboxes.boxes.stop(
            "name",
        )
        assert box is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_stop(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.sandboxes.boxes.with_raw_response.stop(
            "name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        box = await response.parse()
        assert box is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_stop(self, async_client: AsyncLangsmith) -> None:
        async with async_client.sandboxes.boxes.with_streaming_response.stop(
            "name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            box = await response.parse()
            assert box is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_stop(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `name` but received ''"):
            await async_client.sandboxes.boxes.with_raw_response.stop(
                "",
            )
