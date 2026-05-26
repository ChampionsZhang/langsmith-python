# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from langsmith_api import Langsmith, AsyncLangsmith
from langsmith_api._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExperiments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_grouped(self, client: Langsmith) -> None:
        experiment = client.datasets.experiments.grouped(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata_keys=["string"],
        )
        assert_matches_type(object, experiment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_grouped_with_all_params(self, client: Langsmith) -> None:
        experiment = client.datasets.experiments.grouped(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata_keys=["string"],
            dataset_version="dataset_version",
            experiment_limit=1,
            filter="filter",
            name_contains="name_contains",
            stats_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            tag_value_id=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            use_approx_stats=True,
        )
        assert_matches_type(object, experiment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_grouped(self, client: Langsmith) -> None:
        response = client.datasets.experiments.with_raw_response.grouped(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata_keys=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = response.parse()
        assert_matches_type(object, experiment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_grouped(self, client: Langsmith) -> None:
        with client.datasets.experiments.with_streaming_response.grouped(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata_keys=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = response.parse()
            assert_matches_type(object, experiment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_grouped(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.datasets.experiments.with_raw_response.grouped(
                dataset_id="",
                metadata_keys=["string"],
            )


class TestAsyncExperiments:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_grouped(self, async_client: AsyncLangsmith) -> None:
        experiment = await async_client.datasets.experiments.grouped(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata_keys=["string"],
        )
        assert_matches_type(object, experiment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_grouped_with_all_params(self, async_client: AsyncLangsmith) -> None:
        experiment = await async_client.datasets.experiments.grouped(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata_keys=["string"],
            dataset_version="dataset_version",
            experiment_limit=1,
            filter="filter",
            name_contains="name_contains",
            stats_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            tag_value_id=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            use_approx_stats=True,
        )
        assert_matches_type(object, experiment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_grouped(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.datasets.experiments.with_raw_response.grouped(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata_keys=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        experiment = await response.parse()
        assert_matches_type(object, experiment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_grouped(self, async_client: AsyncLangsmith) -> None:
        async with async_client.datasets.experiments.with_streaming_response.grouped(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            metadata_keys=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            experiment = await response.parse()
            assert_matches_type(object, experiment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_grouped(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.datasets.experiments.with_raw_response.grouped(
                dataset_id="",
                metadata_keys=["string"],
            )
