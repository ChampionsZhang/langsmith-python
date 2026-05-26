# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from langsmith_api import Langsmith, AsyncLangsmith
from langsmith_api.types import FeedbackSchema
from langsmith_api.pagination import SyncOffsetPaginationTopLevelArray, AsyncOffsetPaginationTopLevelArray

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPublic:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_feedbacks(self, client: Langsmith) -> None:
        public = client.public.retrieve_feedbacks(
            share_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncOffsetPaginationTopLevelArray[FeedbackSchema], public, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_feedbacks_with_all_params(self, client: Langsmith) -> None:
        public = client.public.retrieve_feedbacks(
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
        assert_matches_type(SyncOffsetPaginationTopLevelArray[FeedbackSchema], public, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_feedbacks(self, client: Langsmith) -> None:
        response = client.public.with_raw_response.retrieve_feedbacks(
            share_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        public = response.parse()
        assert_matches_type(SyncOffsetPaginationTopLevelArray[FeedbackSchema], public, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_feedbacks(self, client: Langsmith) -> None:
        with client.public.with_streaming_response.retrieve_feedbacks(
            share_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            public = response.parse()
            assert_matches_type(SyncOffsetPaginationTopLevelArray[FeedbackSchema], public, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_feedbacks(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `share_token` but received ''"):
            client.public.with_raw_response.retrieve_feedbacks(
                share_token="",
            )


class TestAsyncPublic:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_feedbacks(self, async_client: AsyncLangsmith) -> None:
        public = await async_client.public.retrieve_feedbacks(
            share_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncOffsetPaginationTopLevelArray[FeedbackSchema], public, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_feedbacks_with_all_params(self, async_client: AsyncLangsmith) -> None:
        public = await async_client.public.retrieve_feedbacks(
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
        assert_matches_type(AsyncOffsetPaginationTopLevelArray[FeedbackSchema], public, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_feedbacks(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.public.with_raw_response.retrieve_feedbacks(
            share_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        public = await response.parse()
        assert_matches_type(AsyncOffsetPaginationTopLevelArray[FeedbackSchema], public, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_feedbacks(self, async_client: AsyncLangsmith) -> None:
        async with async_client.public.with_streaming_response.retrieve_feedbacks(
            share_token="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            public = await response.parse()
            assert_matches_type(AsyncOffsetPaginationTopLevelArray[FeedbackSchema], public, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_feedbacks(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `share_token` but received ''"):
            await async_client.public.with_raw_response.retrieve_feedbacks(
                share_token="",
            )
