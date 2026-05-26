# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from langsmith_api import Langsmith, AsyncLangsmith
from langsmith_api.types.datasets import GroupRunsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGroup:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_runs(self, client: Langsmith) -> None:
        group = client.datasets.group.runs(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            group_by="run_metadata",
            metadata_key="metadata_key",
            session_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(GroupRunsResponse, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_runs_with_all_params(self, client: Langsmith) -> None:
        group = client.datasets.group.runs(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            group_by="run_metadata",
            metadata_key="metadata_key",
            session_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            filters={"foo": ["string"]},
            limit=1,
            offset=0,
            per_group_limit=1,
            preview=True,
        )
        assert_matches_type(GroupRunsResponse, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_runs(self, client: Langsmith) -> None:
        response = client.datasets.group.with_raw_response.runs(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            group_by="run_metadata",
            metadata_key="metadata_key",
            session_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = response.parse()
        assert_matches_type(GroupRunsResponse, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_runs(self, client: Langsmith) -> None:
        with client.datasets.group.with_streaming_response.runs(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            group_by="run_metadata",
            metadata_key="metadata_key",
            session_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = response.parse()
            assert_matches_type(GroupRunsResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_runs(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.datasets.group.with_raw_response.runs(
                dataset_id="",
                group_by="run_metadata",
                metadata_key="metadata_key",
                session_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            )


class TestAsyncGroup:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_runs(self, async_client: AsyncLangsmith) -> None:
        group = await async_client.datasets.group.runs(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            group_by="run_metadata",
            metadata_key="metadata_key",
            session_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(GroupRunsResponse, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_runs_with_all_params(self, async_client: AsyncLangsmith) -> None:
        group = await async_client.datasets.group.runs(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            group_by="run_metadata",
            metadata_key="metadata_key",
            session_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            filters={"foo": ["string"]},
            limit=1,
            offset=0,
            per_group_limit=1,
            preview=True,
        )
        assert_matches_type(GroupRunsResponse, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_runs(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.datasets.group.with_raw_response.runs(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            group_by="run_metadata",
            metadata_key="metadata_key",
            session_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        group = await response.parse()
        assert_matches_type(GroupRunsResponse, group, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_runs(self, async_client: AsyncLangsmith) -> None:
        async with async_client.datasets.group.with_streaming_response.runs(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            group_by="run_metadata",
            metadata_key="metadata_key",
            session_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            group = await response.parse()
            assert_matches_type(GroupRunsResponse, group, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_runs(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.datasets.group.with_raw_response.runs(
                dataset_id="",
                group_by="run_metadata",
                metadata_key="metadata_key",
                session_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            )
