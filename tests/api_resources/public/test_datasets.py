# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from langsmith_api import Langsmith, AsyncLangsmith
from langsmith_api.types import (
    TracerSession,
    FeedbackSchema,
)
from langsmith_api.pagination import SyncOffsetPaginationTopLevelArray, AsyncOffsetPaginationTopLevelArray
from langsmith_api.types.public import (
    DatasetListResponse,
    DatasetListComparativeResponse,
    DatasetRetrieveSessionsBulkResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDatasets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Langsmith) -> None:
        dataset = client.public.datasets.list(
            share_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DatasetListResponse, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Langsmith) -> None:
        dataset = client.public.datasets.list(
            share_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
            offset=0,
            sort_by="name",
            sort_by_desc=True,
        )
        assert_matches_type(DatasetListResponse, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Langsmith) -> None:
        response = client.public.datasets.with_raw_response.list(
            share_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(DatasetListResponse, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Langsmith) -> None:
        with client.public.datasets.with_streaming_response.list(
            share_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(DatasetListResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `share_token` but received ''"):
            client.public.datasets.with_raw_response.list(
                share_token="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_comparative(self, client: Langsmith) -> None:
        dataset = client.public.datasets.list_comparative(
            share_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(
            SyncOffsetPaginationTopLevelArray[DatasetListComparativeResponse], dataset, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_comparative_with_all_params(self, client: Langsmith) -> None:
        dataset = client.public.datasets.list_comparative(
            share_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
            name="name",
            name_contains="name_contains",
            offset=0,
            sort_by="name",
            sort_by_desc=True,
        )
        assert_matches_type(
            SyncOffsetPaginationTopLevelArray[DatasetListComparativeResponse], dataset, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_comparative(self, client: Langsmith) -> None:
        response = client.public.datasets.with_raw_response.list_comparative(
            share_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(
            SyncOffsetPaginationTopLevelArray[DatasetListComparativeResponse], dataset, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_comparative(self, client: Langsmith) -> None:
        with client.public.datasets.with_streaming_response.list_comparative(
            share_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(
                SyncOffsetPaginationTopLevelArray[DatasetListComparativeResponse], dataset, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_comparative(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `share_token` but received ''"):
            client.public.datasets.with_raw_response.list_comparative(
                share_token="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_feedback(self, client: Langsmith) -> None:
        dataset = client.public.datasets.list_feedback(
            share_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncOffsetPaginationTopLevelArray[FeedbackSchema], dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_feedback_with_all_params(self, client: Langsmith) -> None:
        dataset = client.public.datasets.list_feedback(
            share_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            has_comment=True,
            has_score=True,
            key=["string"],
            level="run",
            limit=1,
            offset=0,
            run=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            session=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            source=["api"],
            user=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(SyncOffsetPaginationTopLevelArray[FeedbackSchema], dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_feedback(self, client: Langsmith) -> None:
        response = client.public.datasets.with_raw_response.list_feedback(
            share_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(SyncOffsetPaginationTopLevelArray[FeedbackSchema], dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_feedback(self, client: Langsmith) -> None:
        with client.public.datasets.with_streaming_response.list_feedback(
            share_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(SyncOffsetPaginationTopLevelArray[FeedbackSchema], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_feedback(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `share_token` but received ''"):
            client.public.datasets.with_raw_response.list_feedback(
                share_token="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_sessions(self, client: Langsmith) -> None:
        dataset = client.public.datasets.list_sessions(
            share_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncOffsetPaginationTopLevelArray[TracerSession], dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_sessions_with_all_params(self, client: Langsmith) -> None:
        dataset = client.public.datasets.list_sessions(
            share_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            dataset_version="dataset_version",
            facets=True,
            limit=1,
            name="name",
            name_contains="name_contains",
            offset=0,
            sort_by="name",
            sort_by_desc=True,
            sort_by_feedback_key="sort_by_feedback_key",
            accept="accept",
        )
        assert_matches_type(SyncOffsetPaginationTopLevelArray[TracerSession], dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_sessions(self, client: Langsmith) -> None:
        response = client.public.datasets.with_raw_response.list_sessions(
            share_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(SyncOffsetPaginationTopLevelArray[TracerSession], dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_sessions(self, client: Langsmith) -> None:
        with client.public.datasets.with_streaming_response.list_sessions(
            share_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(SyncOffsetPaginationTopLevelArray[TracerSession], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_sessions(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `share_token` but received ''"):
            client.public.datasets.with_raw_response.list_sessions(
                share_token="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_sessions_bulk(self, client: Langsmith) -> None:
        dataset = client.public.datasets.retrieve_sessions_bulk(
            share_tokens=["string"],
        )
        assert_matches_type(DatasetRetrieveSessionsBulkResponse, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_sessions_bulk(self, client: Langsmith) -> None:
        response = client.public.datasets.with_raw_response.retrieve_sessions_bulk(
            share_tokens=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(DatasetRetrieveSessionsBulkResponse, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_sessions_bulk(self, client: Langsmith) -> None:
        with client.public.datasets.with_streaming_response.retrieve_sessions_bulk(
            share_tokens=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(DatasetRetrieveSessionsBulkResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDatasets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLangsmith) -> None:
        dataset = await async_client.public.datasets.list(
            share_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DatasetListResponse, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLangsmith) -> None:
        dataset = await async_client.public.datasets.list(
            share_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
            offset=0,
            sort_by="name",
            sort_by_desc=True,
        )
        assert_matches_type(DatasetListResponse, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.public.datasets.with_raw_response.list(
            share_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(DatasetListResponse, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLangsmith) -> None:
        async with async_client.public.datasets.with_streaming_response.list(
            share_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(DatasetListResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `share_token` but received ''"):
            await async_client.public.datasets.with_raw_response.list(
                share_token="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_comparative(self, async_client: AsyncLangsmith) -> None:
        dataset = await async_client.public.datasets.list_comparative(
            share_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(
            AsyncOffsetPaginationTopLevelArray[DatasetListComparativeResponse], dataset, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_comparative_with_all_params(self, async_client: AsyncLangsmith) -> None:
        dataset = await async_client.public.datasets.list_comparative(
            share_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
            name="name",
            name_contains="name_contains",
            offset=0,
            sort_by="name",
            sort_by_desc=True,
        )
        assert_matches_type(
            AsyncOffsetPaginationTopLevelArray[DatasetListComparativeResponse], dataset, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_comparative(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.public.datasets.with_raw_response.list_comparative(
            share_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(
            AsyncOffsetPaginationTopLevelArray[DatasetListComparativeResponse], dataset, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_comparative(self, async_client: AsyncLangsmith) -> None:
        async with async_client.public.datasets.with_streaming_response.list_comparative(
            share_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(
                AsyncOffsetPaginationTopLevelArray[DatasetListComparativeResponse], dataset, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_comparative(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `share_token` but received ''"):
            await async_client.public.datasets.with_raw_response.list_comparative(
                share_token="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_feedback(self, async_client: AsyncLangsmith) -> None:
        dataset = await async_client.public.datasets.list_feedback(
            share_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncOffsetPaginationTopLevelArray[FeedbackSchema], dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_feedback_with_all_params(self, async_client: AsyncLangsmith) -> None:
        dataset = await async_client.public.datasets.list_feedback(
            share_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            has_comment=True,
            has_score=True,
            key=["string"],
            level="run",
            limit=1,
            offset=0,
            run=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            session=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            source=["api"],
            user=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(AsyncOffsetPaginationTopLevelArray[FeedbackSchema], dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_feedback(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.public.datasets.with_raw_response.list_feedback(
            share_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(AsyncOffsetPaginationTopLevelArray[FeedbackSchema], dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_feedback(self, async_client: AsyncLangsmith) -> None:
        async with async_client.public.datasets.with_streaming_response.list_feedback(
            share_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(AsyncOffsetPaginationTopLevelArray[FeedbackSchema], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_feedback(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `share_token` but received ''"):
            await async_client.public.datasets.with_raw_response.list_feedback(
                share_token="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_sessions(self, async_client: AsyncLangsmith) -> None:
        dataset = await async_client.public.datasets.list_sessions(
            share_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncOffsetPaginationTopLevelArray[TracerSession], dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_sessions_with_all_params(self, async_client: AsyncLangsmith) -> None:
        dataset = await async_client.public.datasets.list_sessions(
            share_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            dataset_version="dataset_version",
            facets=True,
            limit=1,
            name="name",
            name_contains="name_contains",
            offset=0,
            sort_by="name",
            sort_by_desc=True,
            sort_by_feedback_key="sort_by_feedback_key",
            accept="accept",
        )
        assert_matches_type(AsyncOffsetPaginationTopLevelArray[TracerSession], dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_sessions(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.public.datasets.with_raw_response.list_sessions(
            share_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(AsyncOffsetPaginationTopLevelArray[TracerSession], dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_sessions(self, async_client: AsyncLangsmith) -> None:
        async with async_client.public.datasets.with_streaming_response.list_sessions(
            share_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(AsyncOffsetPaginationTopLevelArray[TracerSession], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_sessions(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `share_token` but received ''"):
            await async_client.public.datasets.with_raw_response.list_sessions(
                share_token="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_sessions_bulk(self, async_client: AsyncLangsmith) -> None:
        dataset = await async_client.public.datasets.retrieve_sessions_bulk(
            share_tokens=["string"],
        )
        assert_matches_type(DatasetRetrieveSessionsBulkResponse, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_sessions_bulk(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.public.datasets.with_raw_response.retrieve_sessions_bulk(
            share_tokens=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(DatasetRetrieveSessionsBulkResponse, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_sessions_bulk(self, async_client: AsyncLangsmith) -> None:
        async with async_client.public.datasets.with_streaming_response.retrieve_sessions_bulk(
            share_tokens=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(DatasetRetrieveSessionsBulkResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True
