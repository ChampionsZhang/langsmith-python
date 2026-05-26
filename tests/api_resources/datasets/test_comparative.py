# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from langsmith_api import Langsmith, AsyncLangsmith
from langsmith_api._utils import parse_datetime
from langsmith_api.types.datasets import ComparativeCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestComparative:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Langsmith) -> None:
        comparative = client.datasets.comparative.create(
            experiment_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(ComparativeCreateResponse, comparative, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Langsmith) -> None:
        comparative = client.datasets.comparative.create(
            experiment_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            description="description",
            extra={"foo": "bar"},
            modified_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            reference_dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ComparativeCreateResponse, comparative, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Langsmith) -> None:
        response = client.datasets.comparative.with_raw_response.create(
            experiment_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comparative = response.parse()
        assert_matches_type(ComparativeCreateResponse, comparative, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Langsmith) -> None:
        with client.datasets.comparative.with_streaming_response.create(
            experiment_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comparative = response.parse()
            assert_matches_type(ComparativeCreateResponse, comparative, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Langsmith) -> None:
        comparative = client.datasets.comparative.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, comparative, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Langsmith) -> None:
        response = client.datasets.comparative.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comparative = response.parse()
        assert_matches_type(object, comparative, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Langsmith) -> None:
        with client.datasets.comparative.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comparative = response.parse()
            assert_matches_type(object, comparative, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Langsmith) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `comparative_experiment_id` but received ''"
        ):
            client.datasets.comparative.with_raw_response.delete(
                "",
            )


class TestAsyncComparative:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLangsmith) -> None:
        comparative = await async_client.datasets.comparative.create(
            experiment_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(ComparativeCreateResponse, comparative, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLangsmith) -> None:
        comparative = await async_client.datasets.comparative.create(
            experiment_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            description="description",
            extra={"foo": "bar"},
            modified_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            name="name",
            reference_dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(ComparativeCreateResponse, comparative, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.datasets.comparative.with_raw_response.create(
            experiment_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comparative = await response.parse()
        assert_matches_type(ComparativeCreateResponse, comparative, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLangsmith) -> None:
        async with async_client.datasets.comparative.with_streaming_response.create(
            experiment_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comparative = await response.parse()
            assert_matches_type(ComparativeCreateResponse, comparative, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLangsmith) -> None:
        comparative = await async_client.datasets.comparative.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, comparative, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.datasets.comparative.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        comparative = await response.parse()
        assert_matches_type(object, comparative, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLangsmith) -> None:
        async with async_client.datasets.comparative.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            comparative = await response.parse()
            assert_matches_type(object, comparative, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `comparative_experiment_id` but received ''"
        ):
            await async_client.datasets.comparative.with_raw_response.delete(
                "",
            )
