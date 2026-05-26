# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from tests.utils import assert_matches_type
from langsmith_api import Langsmith, AsyncLangsmith
from langsmith_api.types.datasets import (
    RunCreateResponse,
    SessionFeedbackDelta,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRuns:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Langsmith) -> None:
        run = client.datasets.runs.create(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(Optional[RunCreateResponse], run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Langsmith) -> None:
        run = client.datasets.runs.create(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            format="csv",
            comparative_experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            example_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            filters={"foo": ["string"]},
            include_annotator_detail=True,
            limit=1,
            offset=0,
            preview=True,
            sort_params={
                "sort_by": "sort_by",
                "sort_order": "ASC",
            },
        )
        assert_matches_type(Optional[RunCreateResponse], run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Langsmith) -> None:
        response = client.datasets.runs.with_raw_response.create(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(Optional[RunCreateResponse], run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Langsmith) -> None:
        with client.datasets.runs.with_streaming_response.create(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(Optional[RunCreateResponse], run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.datasets.runs.with_raw_response.create(
                dataset_id="",
                session_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delta(self, client: Langsmith) -> None:
        run = client.datasets.runs.delta(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            baseline_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            comparison_session_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            feedback_key="feedback_key",
        )
        assert_matches_type(SessionFeedbackDelta, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delta_with_all_params(self, client: Langsmith) -> None:
        run = client.datasets.runs.delta(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            baseline_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            comparison_session_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            feedback_key="feedback_key",
            comparative_experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            filters={"foo": ["string"]},
            limit=1,
            offset=0,
        )
        assert_matches_type(SessionFeedbackDelta, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delta(self, client: Langsmith) -> None:
        response = client.datasets.runs.with_raw_response.delta(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            baseline_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            comparison_session_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            feedback_key="feedback_key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = response.parse()
        assert_matches_type(SessionFeedbackDelta, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delta(self, client: Langsmith) -> None:
        with client.datasets.runs.with_streaming_response.delta(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            baseline_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            comparison_session_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            feedback_key="feedback_key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = response.parse()
            assert_matches_type(SessionFeedbackDelta, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delta(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.datasets.runs.with_raw_response.delta(
                dataset_id="",
                baseline_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                comparison_session_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                feedback_key="feedback_key",
            )


class TestAsyncRuns:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLangsmith) -> None:
        run = await async_client.datasets.runs.create(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(Optional[RunCreateResponse], run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLangsmith) -> None:
        run = await async_client.datasets.runs.create(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            format="csv",
            comparative_experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            example_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            filters={"foo": ["string"]},
            include_annotator_detail=True,
            limit=1,
            offset=0,
            preview=True,
            sort_params={
                "sort_by": "sort_by",
                "sort_order": "ASC",
            },
        )
        assert_matches_type(Optional[RunCreateResponse], run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.datasets.runs.with_raw_response.create(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(Optional[RunCreateResponse], run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLangsmith) -> None:
        async with async_client.datasets.runs.with_streaming_response.create(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(Optional[RunCreateResponse], run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.datasets.runs.with_raw_response.create(
                dataset_id="",
                session_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delta(self, async_client: AsyncLangsmith) -> None:
        run = await async_client.datasets.runs.delta(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            baseline_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            comparison_session_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            feedback_key="feedback_key",
        )
        assert_matches_type(SessionFeedbackDelta, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delta_with_all_params(self, async_client: AsyncLangsmith) -> None:
        run = await async_client.datasets.runs.delta(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            baseline_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            comparison_session_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            feedback_key="feedback_key",
            comparative_experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            filters={"foo": ["string"]},
            limit=1,
            offset=0,
        )
        assert_matches_type(SessionFeedbackDelta, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delta(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.datasets.runs.with_raw_response.delta(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            baseline_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            comparison_session_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            feedback_key="feedback_key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        run = await response.parse()
        assert_matches_type(SessionFeedbackDelta, run, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delta(self, async_client: AsyncLangsmith) -> None:
        async with async_client.datasets.runs.with_streaming_response.delta(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            baseline_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            comparison_session_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            feedback_key="feedback_key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            run = await response.parse()
            assert_matches_type(SessionFeedbackDelta, run, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delta(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.datasets.runs.with_raw_response.delta(
                dataset_id="",
                baseline_session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                comparison_session_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
                feedback_key="feedback_key",
            )
