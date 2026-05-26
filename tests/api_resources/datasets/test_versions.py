# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from langsmith_api import Langsmith, AsyncLangsmith
from langsmith_api.types import DatasetVersion
from langsmith_api._utils import parse_datetime
from langsmith_api.pagination import SyncOffsetPaginationTopLevelArray, AsyncOffsetPaginationTopLevelArray
from langsmith_api.types.datasets import VersionRetrieveDiffResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVersions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Langsmith) -> None:
        version = client.datasets.versions.list(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncOffsetPaginationTopLevelArray[DatasetVersion], version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Langsmith) -> None:
        version = client.datasets.versions.list(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            example="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
            offset=0,
            search="search",
        )
        assert_matches_type(SyncOffsetPaginationTopLevelArray[DatasetVersion], version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Langsmith) -> None:
        response = client.datasets.versions.with_raw_response.list(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(SyncOffsetPaginationTopLevelArray[DatasetVersion], version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Langsmith) -> None:
        with client.datasets.versions.with_streaming_response.list(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(SyncOffsetPaginationTopLevelArray[DatasetVersion], version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.datasets.versions.with_raw_response.list(
                dataset_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_diff(self, client: Langsmith) -> None:
        version = client.datasets.versions.retrieve_diff(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            from_version=parse_datetime("2019-12-27T18:11:19.117Z"),
            to_version=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(VersionRetrieveDiffResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_diff(self, client: Langsmith) -> None:
        response = client.datasets.versions.with_raw_response.retrieve_diff(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            from_version=parse_datetime("2019-12-27T18:11:19.117Z"),
            to_version=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(VersionRetrieveDiffResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_diff(self, client: Langsmith) -> None:
        with client.datasets.versions.with_streaming_response.retrieve_diff(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            from_version=parse_datetime("2019-12-27T18:11:19.117Z"),
            to_version=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(VersionRetrieveDiffResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_diff(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.datasets.versions.with_raw_response.retrieve_diff(
                dataset_id="",
                from_version=parse_datetime("2019-12-27T18:11:19.117Z"),
                to_version=parse_datetime("2019-12-27T18:11:19.117Z"),
            )


class TestAsyncVersions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLangsmith) -> None:
        version = await async_client.datasets.versions.list(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(AsyncOffsetPaginationTopLevelArray[DatasetVersion], version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLangsmith) -> None:
        version = await async_client.datasets.versions.list(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            example="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
            offset=0,
            search="search",
        )
        assert_matches_type(AsyncOffsetPaginationTopLevelArray[DatasetVersion], version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.datasets.versions.with_raw_response.list(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(AsyncOffsetPaginationTopLevelArray[DatasetVersion], version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLangsmith) -> None:
        async with async_client.datasets.versions.with_streaming_response.list(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(AsyncOffsetPaginationTopLevelArray[DatasetVersion], version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.datasets.versions.with_raw_response.list(
                dataset_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_diff(self, async_client: AsyncLangsmith) -> None:
        version = await async_client.datasets.versions.retrieve_diff(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            from_version=parse_datetime("2019-12-27T18:11:19.117Z"),
            to_version=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(VersionRetrieveDiffResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_diff(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.datasets.versions.with_raw_response.retrieve_diff(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            from_version=parse_datetime("2019-12-27T18:11:19.117Z"),
            to_version=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(VersionRetrieveDiffResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_diff(self, async_client: AsyncLangsmith) -> None:
        async with async_client.datasets.versions.with_streaming_response.retrieve_diff(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            from_version=parse_datetime("2019-12-27T18:11:19.117Z"),
            to_version=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(VersionRetrieveDiffResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_diff(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.datasets.versions.with_raw_response.retrieve_diff(
                dataset_id="",
                from_version=parse_datetime("2019-12-27T18:11:19.117Z"),
                to_version=parse_datetime("2019-12-27T18:11:19.117Z"),
            )
