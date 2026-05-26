# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from langsmith_api import Langsmith, AsyncLangsmith
from langsmith_api.types import (
    FeedbackSchema,
)
from langsmith_api._utils import parse_datetime
from langsmith_api.pagination import SyncOffsetPaginationTopLevelArray, AsyncOffsetPaginationTopLevelArray

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFeedback:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Langsmith) -> None:
        feedback = client.feedback.create(
            key="key",
        )
        assert_matches_type(FeedbackSchema, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Langsmith) -> None:
        feedback = client.feedback.create(
            key="key",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            comment="comment",
            comparative_experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            correction={"foo": "bar"},
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            error=True,
            feedback_config={
                "type": "continuous",
                "categories": [
                    {
                        "value": 0,
                        "label": "x",
                    }
                ],
                "max": 0,
                "min": 0,
            },
            feedback_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback_source={
                "metadata": {"foo": "bar"},
                "type": "app",
            },
            modified_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            score=0,
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            trace_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            value=0,
        )
        assert_matches_type(FeedbackSchema, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Langsmith) -> None:
        response = client.feedback.with_raw_response.create(
            key="key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = response.parse()
        assert_matches_type(FeedbackSchema, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Langsmith) -> None:
        with client.feedback.with_streaming_response.create(
            key="key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = response.parse()
            assert_matches_type(FeedbackSchema, feedback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Langsmith) -> None:
        feedback = client.feedback.retrieve(
            feedback_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FeedbackSchema, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Langsmith) -> None:
        feedback = client.feedback.retrieve(
            feedback_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            include_user_names=True,
        )
        assert_matches_type(FeedbackSchema, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Langsmith) -> None:
        response = client.feedback.with_raw_response.retrieve(
            feedback_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = response.parse()
        assert_matches_type(FeedbackSchema, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Langsmith) -> None:
        with client.feedback.with_streaming_response.retrieve(
            feedback_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = response.parse()
            assert_matches_type(FeedbackSchema, feedback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `feedback_id` but received ''"):
            client.feedback.with_raw_response.retrieve(
                feedback_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Langsmith) -> None:
        feedback = client.feedback.update(
            feedback_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FeedbackSchema, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Langsmith) -> None:
        feedback = client.feedback.update(
            feedback_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            comment="comment",
            correction={"foo": "bar"},
            feedback_config={
                "type": "continuous",
                "categories": [
                    {
                        "value": 0,
                        "label": "x",
                    }
                ],
                "max": 0,
                "min": 0,
            },
            score=0,
            value=0,
        )
        assert_matches_type(FeedbackSchema, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Langsmith) -> None:
        response = client.feedback.with_raw_response.update(
            feedback_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = response.parse()
        assert_matches_type(FeedbackSchema, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Langsmith) -> None:
        with client.feedback.with_streaming_response.update(
            feedback_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = response.parse()
            assert_matches_type(FeedbackSchema, feedback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `feedback_id` but received ''"):
            client.feedback.with_raw_response.update(
                feedback_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Langsmith) -> None:
        feedback = client.feedback.list()
        assert_matches_type(SyncOffsetPaginationTopLevelArray[FeedbackSchema], feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Langsmith) -> None:
        feedback = client.feedback.list(
            comparative_experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            has_comment=True,
            has_score=True,
            include_user_names=True,
            key=["string"],
            level="run",
            limit=1,
            max_created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            min_created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            offset=0,
            run=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            session=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            source=["api"],
            user=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(SyncOffsetPaginationTopLevelArray[FeedbackSchema], feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Langsmith) -> None:
        response = client.feedback.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = response.parse()
        assert_matches_type(SyncOffsetPaginationTopLevelArray[FeedbackSchema], feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Langsmith) -> None:
        with client.feedback.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = response.parse()
            assert_matches_type(SyncOffsetPaginationTopLevelArray[FeedbackSchema], feedback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Langsmith) -> None:
        feedback = client.feedback.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Langsmith) -> None:
        response = client.feedback.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = response.parse()
        assert_matches_type(object, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Langsmith) -> None:
        with client.feedback.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = response.parse()
            assert_matches_type(object, feedback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `feedback_id` but received ''"):
            client.feedback.with_raw_response.delete(
                "",
            )


class TestAsyncFeedback:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLangsmith) -> None:
        feedback = await async_client.feedback.create(
            key="key",
        )
        assert_matches_type(FeedbackSchema, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLangsmith) -> None:
        feedback = await async_client.feedback.create(
            key="key",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            comment="comment",
            comparative_experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            correction={"foo": "bar"},
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            error=True,
            feedback_config={
                "type": "continuous",
                "categories": [
                    {
                        "value": 0,
                        "label": "x",
                    }
                ],
                "max": 0,
                "min": 0,
            },
            feedback_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            feedback_source={
                "metadata": {"foo": "bar"},
                "type": "app",
            },
            modified_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            run_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            score=0,
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            trace_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            value=0,
        )
        assert_matches_type(FeedbackSchema, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.feedback.with_raw_response.create(
            key="key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = await response.parse()
        assert_matches_type(FeedbackSchema, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLangsmith) -> None:
        async with async_client.feedback.with_streaming_response.create(
            key="key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = await response.parse()
            assert_matches_type(FeedbackSchema, feedback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLangsmith) -> None:
        feedback = await async_client.feedback.retrieve(
            feedback_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FeedbackSchema, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncLangsmith) -> None:
        feedback = await async_client.feedback.retrieve(
            feedback_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            include_user_names=True,
        )
        assert_matches_type(FeedbackSchema, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.feedback.with_raw_response.retrieve(
            feedback_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = await response.parse()
        assert_matches_type(FeedbackSchema, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLangsmith) -> None:
        async with async_client.feedback.with_streaming_response.retrieve(
            feedback_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = await response.parse()
            assert_matches_type(FeedbackSchema, feedback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `feedback_id` but received ''"):
            await async_client.feedback.with_raw_response.retrieve(
                feedback_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncLangsmith) -> None:
        feedback = await async_client.feedback.update(
            feedback_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FeedbackSchema, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLangsmith) -> None:
        feedback = await async_client.feedback.update(
            feedback_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            comment="comment",
            correction={"foo": "bar"},
            feedback_config={
                "type": "continuous",
                "categories": [
                    {
                        "value": 0,
                        "label": "x",
                    }
                ],
                "max": 0,
                "min": 0,
            },
            score=0,
            value=0,
        )
        assert_matches_type(FeedbackSchema, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.feedback.with_raw_response.update(
            feedback_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = await response.parse()
        assert_matches_type(FeedbackSchema, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLangsmith) -> None:
        async with async_client.feedback.with_streaming_response.update(
            feedback_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = await response.parse()
            assert_matches_type(FeedbackSchema, feedback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `feedback_id` but received ''"):
            await async_client.feedback.with_raw_response.update(
                feedback_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLangsmith) -> None:
        feedback = await async_client.feedback.list()
        assert_matches_type(AsyncOffsetPaginationTopLevelArray[FeedbackSchema], feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLangsmith) -> None:
        feedback = await async_client.feedback.list(
            comparative_experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            has_comment=True,
            has_score=True,
            include_user_names=True,
            key=["string"],
            level="run",
            limit=1,
            max_created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            min_created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            offset=0,
            run=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            session=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            source=["api"],
            user=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(AsyncOffsetPaginationTopLevelArray[FeedbackSchema], feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.feedback.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = await response.parse()
        assert_matches_type(AsyncOffsetPaginationTopLevelArray[FeedbackSchema], feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLangsmith) -> None:
        async with async_client.feedback.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = await response.parse()
            assert_matches_type(AsyncOffsetPaginationTopLevelArray[FeedbackSchema], feedback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLangsmith) -> None:
        feedback = await async_client.feedback.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.feedback.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = await response.parse()
        assert_matches_type(object, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLangsmith) -> None:
        async with async_client.feedback.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = await response.parse()
            assert_matches_type(object, feedback, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `feedback_id` but received ''"):
            await async_client.feedback.with_raw_response.delete(
                "",
            )
