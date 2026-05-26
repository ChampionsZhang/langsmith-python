# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from langsmith_api import Langsmith, AsyncLangsmith
from langsmith_api.types import (
    RunSchema,
    RunQueryResponse,
    RunStatsResponse,
    RunCreateResponse,
    RunUpdateResponse,
    RunIngestBatchResponse,
)
from langsmith_api._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRuns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Langsmith) -> None:
        run = client.runs.create()
        assert_matches_type(RunCreateResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Langsmith) -> None:
        run = client.runs.create(
            id="id",
            dotted_order="dotted_order",
            end_time="end_time",
            error="error",
            events=[{"foo": "bar"}],
            extra={"foo": "bar"},
            input_attachments={"foo": "bar"},
            inputs={"foo": "bar"},
            name="name",
            output_attachments={"foo": "bar"},
            outputs={"foo": "bar"},
            parent_run_id="parent_run_id",
            reference_example_id="reference_example_id",
            run_type="tool",
            serialized={"foo": "bar"},
            session_id="session_id",
            session_name="session_name",
            start_time="start_time",
            status="status",
            tags=["string"],
            trace_id="trace_id",
        )
        assert_matches_type(RunCreateResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Langsmith) -> None:
        response = client.runs.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunCreateResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Langsmith) -> None:
        with client.runs.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunCreateResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Langsmith) -> None:
        run = client.runs.retrieve(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RunSchema, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Langsmith) -> None:
        run = client.runs.retrieve(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            exclude_s3_stored_attributes=True,
            exclude_serialized=True,
            include_messages=True,
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(RunSchema, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Langsmith) -> None:
        response = client.runs.with_raw_response.retrieve(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunSchema, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Langsmith) -> None:
        with client.runs.with_streaming_response.retrieve(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunSchema, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.runs.with_raw_response.retrieve(
                run_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Langsmith) -> None:
        run = client.runs.update(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RunUpdateResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Langsmith) -> None:
        run = client.runs.update(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="id",
            dotted_order="dotted_order",
            end_time="end_time",
            error="error",
            events=[{"foo": "bar"}],
            extra={"foo": "bar"},
            input_attachments={"foo": "bar"},
            inputs={"foo": "bar"},
            name="name",
            output_attachments={"foo": "bar"},
            outputs={"foo": "bar"},
            parent_run_id="parent_run_id",
            reference_example_id="reference_example_id",
            run_type="tool",
            serialized={"foo": "bar"},
            session_id="session_id",
            session_name="session_name",
            start_time="start_time",
            status="status",
            tags=["string"],
            trace_id="trace_id",
        )
        assert_matches_type(RunUpdateResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Langsmith) -> None:
        response = client.runs.with_raw_response.update(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunUpdateResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Langsmith) -> None:
        with client.runs.with_streaming_response.update(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunUpdateResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.runs.with_raw_response.update(
                run_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_ingest_batch(self, client: Langsmith) -> None:
        run = client.runs.ingest_batch()
        assert_matches_type(RunIngestBatchResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_ingest_batch_with_all_params(self, client: Langsmith) -> None:
        run = client.runs.ingest_batch(
            patch=[
                {
                    "id": "id",
                    "dotted_order": "dotted_order",
                    "end_time": "end_time",
                    "error": "error",
                    "events": [{"foo": "bar"}],
                    "extra": {"foo": "bar"},
                    "input_attachments": {"foo": "bar"},
                    "inputs": {"foo": "bar"},
                    "name": "name",
                    "output_attachments": {"foo": "bar"},
                    "outputs": {"foo": "bar"},
                    "parent_run_id": "parent_run_id",
                    "reference_example_id": "reference_example_id",
                    "run_type": "tool",
                    "serialized": {"foo": "bar"},
                    "session_id": "session_id",
                    "session_name": "session_name",
                    "start_time": "start_time",
                    "status": "status",
                    "tags": ["string"],
                    "trace_id": "trace_id",
                }
            ],
            post=[
                {
                    "id": "id",
                    "dotted_order": "dotted_order",
                    "end_time": "end_time",
                    "error": "error",
                    "events": [{"foo": "bar"}],
                    "extra": {"foo": "bar"},
                    "input_attachments": {"foo": "bar"},
                    "inputs": {"foo": "bar"},
                    "name": "name",
                    "output_attachments": {"foo": "bar"},
                    "outputs": {"foo": "bar"},
                    "parent_run_id": "parent_run_id",
                    "reference_example_id": "reference_example_id",
                    "run_type": "tool",
                    "serialized": {"foo": "bar"},
                    "session_id": "session_id",
                    "session_name": "session_name",
                    "start_time": "start_time",
                    "status": "status",
                    "tags": ["string"],
                    "trace_id": "trace_id",
                }
            ],
        )
        assert_matches_type(RunIngestBatchResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_ingest_batch(self, client: Langsmith) -> None:
        response = client.runs.with_raw_response.ingest_batch()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunIngestBatchResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_ingest_batch(self, client: Langsmith) -> None:
        with client.runs.with_streaming_response.ingest_batch() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunIngestBatchResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_query(self, client: Langsmith) -> None:
        run = client.runs.query()
        assert_matches_type(RunQueryResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_query_with_all_params(self, client: Langsmith) -> None:
        run = client.runs.query(
            id=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            cursor="cursor",
            data_source_type="current",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            error=True,
            execution_order=1,
            filter="filter",
            is_root=True,
            limit=1,
            order="asc",
            parent_run="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="query",
            reference_example=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            run_type="tool",
            search_filter="search_filter",
            select=["id"],
            session=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            skip_pagination=True,
            skip_prev_cursor=True,
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            trace="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            trace_filter="trace_filter",
            tree_filter="tree_filter",
            use_experimental_search=True,
        )
        assert_matches_type(RunQueryResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_query(self, client: Langsmith) -> None:
        response = client.runs.with_raw_response.query()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunQueryResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_query(self, client: Langsmith) -> None:
        with client.runs.with_streaming_response.query() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunQueryResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stats(self, client: Langsmith) -> None:
        run = client.runs.stats()
        assert_matches_type(RunStatsResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stats_with_all_params(self, client: Langsmith) -> None:
        run = client.runs.stats(
            id=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            data_source_type="current",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            error=True,
            execution_order=1,
            filter="filter",
            group_by={
                "attribute": "name",
                "max_groups": 0,
                "path": "path",
            },
            groups=["string"],
            is_root=True,
            parent_run="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="query",
            reference_example=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            run_type="tool",
            search_filter="search_filter",
            select=["run_count"],
            session=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            skip_pagination=True,
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            trace="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            trace_filter="trace_filter",
            tree_filter="tree_filter",
            use_experimental_search=True,
        )
        assert_matches_type(RunStatsResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_stats(self, client: Langsmith) -> None:
        response = client.runs.with_raw_response.stats()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(RunStatsResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_stats(self, client: Langsmith) -> None:
        with client.runs.with_streaming_response.stats() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(RunStatsResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_2(self, client: Langsmith) -> None:
        run = client.runs.update_2(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_2(self, client: Langsmith) -> None:
        response = client.runs.with_raw_response.update_2(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(object, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_2(self, client: Langsmith) -> None:
        with client.runs.with_streaming_response.update_2(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(object, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_2(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            client.runs.with_raw_response.update_2(
                "",
            )


class TestAsyncRuns:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLangsmith) -> None:
        run = await async_client.runs.create()
        assert_matches_type(RunCreateResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLangsmith) -> None:
        run = await async_client.runs.create(
            id="id",
            dotted_order="dotted_order",
            end_time="end_time",
            error="error",
            events=[{"foo": "bar"}],
            extra={"foo": "bar"},
            input_attachments={"foo": "bar"},
            inputs={"foo": "bar"},
            name="name",
            output_attachments={"foo": "bar"},
            outputs={"foo": "bar"},
            parent_run_id="parent_run_id",
            reference_example_id="reference_example_id",
            run_type="tool",
            serialized={"foo": "bar"},
            session_id="session_id",
            session_name="session_name",
            start_time="start_time",
            status="status",
            tags=["string"],
            trace_id="trace_id",
        )
        assert_matches_type(RunCreateResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.runs.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunCreateResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLangsmith) -> None:
        async with async_client.runs.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunCreateResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLangsmith) -> None:
        run = await async_client.runs.retrieve(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RunSchema, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncLangsmith) -> None:
        run = await async_client.runs.retrieve(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            exclude_s3_stored_attributes=True,
            exclude_serialized=True,
            include_messages=True,
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(RunSchema, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.runs.with_raw_response.retrieve(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunSchema, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLangsmith) -> None:
        async with async_client.runs.with_streaming_response.retrieve(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunSchema, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.runs.with_raw_response.retrieve(
                run_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncLangsmith) -> None:
        run = await async_client.runs.update(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(RunUpdateResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLangsmith) -> None:
        run = await async_client.runs.update(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            id="id",
            dotted_order="dotted_order",
            end_time="end_time",
            error="error",
            events=[{"foo": "bar"}],
            extra={"foo": "bar"},
            input_attachments={"foo": "bar"},
            inputs={"foo": "bar"},
            name="name",
            output_attachments={"foo": "bar"},
            outputs={"foo": "bar"},
            parent_run_id="parent_run_id",
            reference_example_id="reference_example_id",
            run_type="tool",
            serialized={"foo": "bar"},
            session_id="session_id",
            session_name="session_name",
            start_time="start_time",
            status="status",
            tags=["string"],
            trace_id="trace_id",
        )
        assert_matches_type(RunUpdateResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.runs.with_raw_response.update(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunUpdateResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLangsmith) -> None:
        async with async_client.runs.with_streaming_response.update(
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunUpdateResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.runs.with_raw_response.update(
                run_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_ingest_batch(self, async_client: AsyncLangsmith) -> None:
        run = await async_client.runs.ingest_batch()
        assert_matches_type(RunIngestBatchResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_ingest_batch_with_all_params(self, async_client: AsyncLangsmith) -> None:
        run = await async_client.runs.ingest_batch(
            patch=[
                {
                    "id": "id",
                    "dotted_order": "dotted_order",
                    "end_time": "end_time",
                    "error": "error",
                    "events": [{"foo": "bar"}],
                    "extra": {"foo": "bar"},
                    "input_attachments": {"foo": "bar"},
                    "inputs": {"foo": "bar"},
                    "name": "name",
                    "output_attachments": {"foo": "bar"},
                    "outputs": {"foo": "bar"},
                    "parent_run_id": "parent_run_id",
                    "reference_example_id": "reference_example_id",
                    "run_type": "tool",
                    "serialized": {"foo": "bar"},
                    "session_id": "session_id",
                    "session_name": "session_name",
                    "start_time": "start_time",
                    "status": "status",
                    "tags": ["string"],
                    "trace_id": "trace_id",
                }
            ],
            post=[
                {
                    "id": "id",
                    "dotted_order": "dotted_order",
                    "end_time": "end_time",
                    "error": "error",
                    "events": [{"foo": "bar"}],
                    "extra": {"foo": "bar"},
                    "input_attachments": {"foo": "bar"},
                    "inputs": {"foo": "bar"},
                    "name": "name",
                    "output_attachments": {"foo": "bar"},
                    "outputs": {"foo": "bar"},
                    "parent_run_id": "parent_run_id",
                    "reference_example_id": "reference_example_id",
                    "run_type": "tool",
                    "serialized": {"foo": "bar"},
                    "session_id": "session_id",
                    "session_name": "session_name",
                    "start_time": "start_time",
                    "status": "status",
                    "tags": ["string"],
                    "trace_id": "trace_id",
                }
            ],
        )
        assert_matches_type(RunIngestBatchResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_ingest_batch(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.runs.with_raw_response.ingest_batch()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunIngestBatchResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_ingest_batch(self, async_client: AsyncLangsmith) -> None:
        async with async_client.runs.with_streaming_response.ingest_batch() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunIngestBatchResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_query(self, async_client: AsyncLangsmith) -> None:
        run = await async_client.runs.query()
        assert_matches_type(RunQueryResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncLangsmith) -> None:
        run = await async_client.runs.query(
            id=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            cursor="cursor",
            data_source_type="current",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            error=True,
            execution_order=1,
            filter="filter",
            is_root=True,
            limit=1,
            order="asc",
            parent_run="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="query",
            reference_example=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            run_type="tool",
            search_filter="search_filter",
            select=["id"],
            session=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            skip_pagination=True,
            skip_prev_cursor=True,
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            trace="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            trace_filter="trace_filter",
            tree_filter="tree_filter",
            use_experimental_search=True,
        )
        assert_matches_type(RunQueryResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_query(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.runs.with_raw_response.query()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunQueryResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncLangsmith) -> None:
        async with async_client.runs.with_streaming_response.query() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunQueryResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stats(self, async_client: AsyncLangsmith) -> None:
        run = await async_client.runs.stats()
        assert_matches_type(RunStatsResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stats_with_all_params(self, async_client: AsyncLangsmith) -> None:
        run = await async_client.runs.stats(
            id=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            data_source_type="current",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            error=True,
            execution_order=1,
            filter="filter",
            group_by={
                "attribute": "name",
                "max_groups": 0,
                "path": "path",
            },
            groups=["string"],
            is_root=True,
            parent_run="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            query="query",
            reference_example=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            run_type="tool",
            search_filter="search_filter",
            select=["run_count"],
            session=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            skip_pagination=True,
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            trace="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            trace_filter="trace_filter",
            tree_filter="tree_filter",
            use_experimental_search=True,
        )
        assert_matches_type(RunStatsResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_stats(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.runs.with_raw_response.stats()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(RunStatsResponse, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_stats(self, async_client: AsyncLangsmith) -> None:
        async with async_client.runs.with_streaming_response.stats() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(RunStatsResponse, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_2(self, async_client: AsyncLangsmith) -> None:
        run = await async_client.runs.update_2(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_2(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.runs.with_raw_response.update_2(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(object, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_2(self, async_client: AsyncLangsmith) -> None:
        async with async_client.runs.with_streaming_response.update_2(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(object, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_2(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `run_id` but received ''"):
            await async_client.runs.with_raw_response.update_2(
                "",
            )
