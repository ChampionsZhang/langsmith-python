# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from langsmith_api import Langsmith, AsyncLangsmith
from langsmith_api.types import (
    Example,
    ExampleRetrieveCountResponse,
    ExampleUploadFromCsvResponse,
)
from langsmith_api._utils import parse_datetime
from langsmith_api.pagination import SyncOffsetPaginationTopLevelArray, AsyncOffsetPaginationTopLevelArray

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExamples:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Langsmith) -> None:
        example = client.examples.create(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Example, example, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Langsmith) -> None:
        example = client.examples.create(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            created_at="created_at",
            inputs={"foo": "bar"},
            metadata={"foo": "bar"},
            outputs={"foo": "bar"},
            source_run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            split=["string"],
            use_legacy_message_format=True,
            use_source_run_attachments=["string"],
            use_source_run_io=True,
        )
        assert_matches_type(Example, example, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Langsmith) -> None:
        response = client.examples.with_raw_response.create(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        example = response.parse()
        assert_matches_type(Example, example, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Langsmith) -> None:
        with client.examples.with_streaming_response.create(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            example = response.parse()
            assert_matches_type(Example, example, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Langsmith) -> None:
        example = client.examples.retrieve(
            example_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Example, example, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Langsmith) -> None:
        example = client.examples.retrieve(
            example_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            as_of=parse_datetime("2019-12-27T18:11:19.117Z"),
            dataset="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Example, example, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Langsmith) -> None:
        response = client.examples.with_raw_response.retrieve(
            example_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        example = response.parse()
        assert_matches_type(Example, example, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Langsmith) -> None:
        with client.examples.with_streaming_response.retrieve(
            example_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            example = response.parse()
            assert_matches_type(Example, example, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `example_id` but received ''"):
            client.examples.with_raw_response.retrieve(
                example_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Langsmith) -> None:
        example = client.examples.update(
            example_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, example, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Langsmith) -> None:
        example = client.examples.update(
            example_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            attachments_operations={
                "rename": {"foo": "string"},
                "retain": ["string"],
            },
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inputs={"foo": "bar"},
            metadata={"foo": "bar"},
            outputs={"foo": "bar"},
            overwrite=True,
            split=["string"],
        )
        assert_matches_type(object, example, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Langsmith) -> None:
        response = client.examples.with_raw_response.update(
            example_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        example = response.parse()
        assert_matches_type(object, example, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Langsmith) -> None:
        with client.examples.with_streaming_response.update(
            example_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            example = response.parse()
            assert_matches_type(object, example, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `example_id` but received ''"):
            client.examples.with_raw_response.update(
                example_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Langsmith) -> None:
        example = client.examples.list()
        assert_matches_type(SyncOffsetPaginationTopLevelArray[Example], example, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Langsmith) -> None:
        example = client.examples.list(
            id=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            as_of=parse_datetime("2019-12-27T18:11:19.117Z"),
            dataset="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            descending=True,
            filter="filter",
            full_text_contains=["string"],
            limit=1,
            metadata="metadata",
            offset=0,
            order="recent",
            random_seed=0,
            select=["id"],
            splits=["string"],
        )
        assert_matches_type(SyncOffsetPaginationTopLevelArray[Example], example, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Langsmith) -> None:
        response = client.examples.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        example = response.parse()
        assert_matches_type(SyncOffsetPaginationTopLevelArray[Example], example, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Langsmith) -> None:
        with client.examples.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            example = response.parse()
            assert_matches_type(SyncOffsetPaginationTopLevelArray[Example], example, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Langsmith) -> None:
        example = client.examples.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, example, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Langsmith) -> None:
        response = client.examples.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        example = response.parse()
        assert_matches_type(object, example, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Langsmith) -> None:
        with client.examples.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            example = response.parse()
            assert_matches_type(object, example, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `example_id` but received ''"):
            client.examples.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_all(self, client: Langsmith) -> None:
        example = client.examples.delete_all(
            example_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(object, example, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_all(self, client: Langsmith) -> None:
        response = client.examples.with_raw_response.delete_all(
            example_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        example = response.parse()
        assert_matches_type(object, example, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_all(self, client: Langsmith) -> None:
        with client.examples.with_streaming_response.delete_all(
            example_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            example = response.parse()
            assert_matches_type(object, example, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_count(self, client: Langsmith) -> None:
        example = client.examples.retrieve_count()
        assert_matches_type(ExampleRetrieveCountResponse, example, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_count_with_all_params(self, client: Langsmith) -> None:
        example = client.examples.retrieve_count(
            id=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            as_of=parse_datetime("2019-12-27T18:11:19.117Z"),
            dataset="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            filter="filter",
            full_text_contains=["string"],
            metadata="metadata",
            splits=["string"],
        )
        assert_matches_type(ExampleRetrieveCountResponse, example, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_count(self, client: Langsmith) -> None:
        response = client.examples.with_raw_response.retrieve_count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        example = response.parse()
        assert_matches_type(ExampleRetrieveCountResponse, example, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_count(self, client: Langsmith) -> None:
        with client.examples.with_streaming_response.retrieve_count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            example = response.parse()
            assert_matches_type(ExampleRetrieveCountResponse, example, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upload_from_csv(self, client: Langsmith) -> None:
        example = client.examples.upload_from_csv(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file=b"Example data",
            input_keys=["string"],
        )
        assert_matches_type(ExampleUploadFromCsvResponse, example, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upload_from_csv_with_all_params(self, client: Langsmith) -> None:
        example = client.examples.upload_from_csv(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file=b"Example data",
            input_keys=["string"],
            metadata_keys=["string"],
            output_keys=["string"],
        )
        assert_matches_type(ExampleUploadFromCsvResponse, example, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upload_from_csv(self, client: Langsmith) -> None:
        response = client.examples.with_raw_response.upload_from_csv(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file=b"Example data",
            input_keys=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        example = response.parse()
        assert_matches_type(ExampleUploadFromCsvResponse, example, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upload_from_csv(self, client: Langsmith) -> None:
        with client.examples.with_streaming_response.upload_from_csv(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file=b"Example data",
            input_keys=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            example = response.parse()
            assert_matches_type(ExampleUploadFromCsvResponse, example, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_upload_from_csv(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.examples.with_raw_response.upload_from_csv(
                dataset_id="",
                file=b"Example data",
                input_keys=["string"],
            )


class TestAsyncExamples:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLangsmith) -> None:
        example = await async_client.examples.create(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Example, example, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLangsmith) -> None:
        example = await async_client.examples.create(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            created_at="created_at",
            inputs={"foo": "bar"},
            metadata={"foo": "bar"},
            outputs={"foo": "bar"},
            source_run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            split=["string"],
            use_legacy_message_format=True,
            use_source_run_attachments=["string"],
            use_source_run_io=True,
        )
        assert_matches_type(Example, example, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.examples.with_raw_response.create(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        example = await response.parse()
        assert_matches_type(Example, example, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLangsmith) -> None:
        async with async_client.examples.with_streaming_response.create(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            example = await response.parse()
            assert_matches_type(Example, example, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLangsmith) -> None:
        example = await async_client.examples.retrieve(
            example_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Example, example, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncLangsmith) -> None:
        example = await async_client.examples.retrieve(
            example_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            as_of=parse_datetime("2019-12-27T18:11:19.117Z"),
            dataset="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Example, example, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.examples.with_raw_response.retrieve(
            example_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        example = await response.parse()
        assert_matches_type(Example, example, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLangsmith) -> None:
        async with async_client.examples.with_streaming_response.retrieve(
            example_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            example = await response.parse()
            assert_matches_type(Example, example, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `example_id` but received ''"):
            await async_client.examples.with_raw_response.retrieve(
                example_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncLangsmith) -> None:
        example = await async_client.examples.update(
            example_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, example, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLangsmith) -> None:
        example = await async_client.examples.update(
            example_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            attachments_operations={
                "rename": {"foo": "string"},
                "retain": ["string"],
            },
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            inputs={"foo": "bar"},
            metadata={"foo": "bar"},
            outputs={"foo": "bar"},
            overwrite=True,
            split=["string"],
        )
        assert_matches_type(object, example, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.examples.with_raw_response.update(
            example_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        example = await response.parse()
        assert_matches_type(object, example, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLangsmith) -> None:
        async with async_client.examples.with_streaming_response.update(
            example_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            example = await response.parse()
            assert_matches_type(object, example, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `example_id` but received ''"):
            await async_client.examples.with_raw_response.update(
                example_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLangsmith) -> None:
        example = await async_client.examples.list()
        assert_matches_type(AsyncOffsetPaginationTopLevelArray[Example], example, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLangsmith) -> None:
        example = await async_client.examples.list(
            id=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            as_of=parse_datetime("2019-12-27T18:11:19.117Z"),
            dataset="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            descending=True,
            filter="filter",
            full_text_contains=["string"],
            limit=1,
            metadata="metadata",
            offset=0,
            order="recent",
            random_seed=0,
            select=["id"],
            splits=["string"],
        )
        assert_matches_type(AsyncOffsetPaginationTopLevelArray[Example], example, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.examples.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        example = await response.parse()
        assert_matches_type(AsyncOffsetPaginationTopLevelArray[Example], example, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLangsmith) -> None:
        async with async_client.examples.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            example = await response.parse()
            assert_matches_type(AsyncOffsetPaginationTopLevelArray[Example], example, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLangsmith) -> None:
        example = await async_client.examples.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, example, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.examples.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        example = await response.parse()
        assert_matches_type(object, example, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLangsmith) -> None:
        async with async_client.examples.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            example = await response.parse()
            assert_matches_type(object, example, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `example_id` but received ''"):
            await async_client.examples.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_all(self, async_client: AsyncLangsmith) -> None:
        example = await async_client.examples.delete_all(
            example_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(object, example, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_all(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.examples.with_raw_response.delete_all(
            example_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        example = await response.parse()
        assert_matches_type(object, example, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_all(self, async_client: AsyncLangsmith) -> None:
        async with async_client.examples.with_streaming_response.delete_all(
            example_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            example = await response.parse()
            assert_matches_type(object, example, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_count(self, async_client: AsyncLangsmith) -> None:
        example = await async_client.examples.retrieve_count()
        assert_matches_type(ExampleRetrieveCountResponse, example, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_count_with_all_params(self, async_client: AsyncLangsmith) -> None:
        example = await async_client.examples.retrieve_count(
            id=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            as_of=parse_datetime("2019-12-27T18:11:19.117Z"),
            dataset="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            filter="filter",
            full_text_contains=["string"],
            metadata="metadata",
            splits=["string"],
        )
        assert_matches_type(ExampleRetrieveCountResponse, example, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_count(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.examples.with_raw_response.retrieve_count()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        example = await response.parse()
        assert_matches_type(ExampleRetrieveCountResponse, example, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_count(self, async_client: AsyncLangsmith) -> None:
        async with async_client.examples.with_streaming_response.retrieve_count() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            example = await response.parse()
            assert_matches_type(ExampleRetrieveCountResponse, example, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upload_from_csv(self, async_client: AsyncLangsmith) -> None:
        example = await async_client.examples.upload_from_csv(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file=b"Example data",
            input_keys=["string"],
        )
        assert_matches_type(ExampleUploadFromCsvResponse, example, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upload_from_csv_with_all_params(self, async_client: AsyncLangsmith) -> None:
        example = await async_client.examples.upload_from_csv(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file=b"Example data",
            input_keys=["string"],
            metadata_keys=["string"],
            output_keys=["string"],
        )
        assert_matches_type(ExampleUploadFromCsvResponse, example, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upload_from_csv(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.examples.with_raw_response.upload_from_csv(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file=b"Example data",
            input_keys=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        example = await response.parse()
        assert_matches_type(ExampleUploadFromCsvResponse, example, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upload_from_csv(self, async_client: AsyncLangsmith) -> None:
        async with async_client.examples.with_streaming_response.upload_from_csv(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            file=b"Example data",
            input_keys=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            example = await response.parse()
            assert_matches_type(ExampleUploadFromCsvResponse, example, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_upload_from_csv(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.examples.with_raw_response.upload_from_csv(
                dataset_id="",
                file=b"Example data",
                input_keys=["string"],
            )
