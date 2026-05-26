# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from langsmith_api import Langsmith, AsyncLangsmith
from langsmith_api._utils import parse_datetime
from langsmith_api.types.datasets import (
    SplitCreateResponse,
    SplitRetrieveResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSplits:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Langsmith) -> None:
        split = client.datasets.splits.create(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            examples=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            split_name="split_name",
        )
        assert_matches_type(SplitCreateResponse, split, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Langsmith) -> None:
        split = client.datasets.splits.create(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            examples=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            split_name="split_name",
            remove=True,
        )
        assert_matches_type(SplitCreateResponse, split, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Langsmith) -> None:
        response = client.datasets.splits.with_raw_response.create(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            examples=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            split_name="split_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        split = response.parse()
        assert_matches_type(SplitCreateResponse, split, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Langsmith) -> None:
        with client.datasets.splits.with_streaming_response.create(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            examples=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            split_name="split_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            split = response.parse()
            assert_matches_type(SplitCreateResponse, split, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.datasets.splits.with_raw_response.create(
                dataset_id="",
                examples=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                split_name="split_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Langsmith) -> None:
        split = client.datasets.splits.retrieve(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SplitRetrieveResponse, split, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Langsmith) -> None:
        split = client.datasets.splits.retrieve(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            as_of=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SplitRetrieveResponse, split, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Langsmith) -> None:
        response = client.datasets.splits.with_raw_response.retrieve(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        split = response.parse()
        assert_matches_type(SplitRetrieveResponse, split, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Langsmith) -> None:
        with client.datasets.splits.with_streaming_response.retrieve(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            split = response.parse()
            assert_matches_type(SplitRetrieveResponse, split, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.datasets.splits.with_raw_response.retrieve(
                dataset_id="",
            )


class TestAsyncSplits:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLangsmith) -> None:
        split = await async_client.datasets.splits.create(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            examples=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            split_name="split_name",
        )
        assert_matches_type(SplitCreateResponse, split, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLangsmith) -> None:
        split = await async_client.datasets.splits.create(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            examples=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            split_name="split_name",
            remove=True,
        )
        assert_matches_type(SplitCreateResponse, split, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.datasets.splits.with_raw_response.create(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            examples=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            split_name="split_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        split = await response.parse()
        assert_matches_type(SplitCreateResponse, split, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLangsmith) -> None:
        async with async_client.datasets.splits.with_streaming_response.create(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            examples=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            split_name="split_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            split = await response.parse()
            assert_matches_type(SplitCreateResponse, split, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.datasets.splits.with_raw_response.create(
                dataset_id="",
                examples=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                split_name="split_name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLangsmith) -> None:
        split = await async_client.datasets.splits.retrieve(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SplitRetrieveResponse, split, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncLangsmith) -> None:
        split = await async_client.datasets.splits.retrieve(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            as_of=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SplitRetrieveResponse, split, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.datasets.splits.with_raw_response.retrieve(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        split = await response.parse()
        assert_matches_type(SplitRetrieveResponse, split, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLangsmith) -> None:
        async with async_client.datasets.splits.with_streaming_response.retrieve(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            split = await response.parse()
            assert_matches_type(SplitRetrieveResponse, split, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.datasets.splits.with_raw_response.retrieve(
                dataset_id="",
            )
