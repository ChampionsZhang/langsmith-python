# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from langsmith_api import Langsmith, AsyncLangsmith
from langsmith_api._utils import parse_datetime
from langsmith_api.pagination import (
    SyncOffsetPaginationInsightsClusteringJobs,
    AsyncOffsetPaginationInsightsClusteringJobs,
)
from langsmith_api.types.sessions import (
    InsightListResponse,
    InsightCreateResponse,
    InsightDeleteResponse,
    InsightUpdateResponse,
    InsightRetrieveJobResponse,
    InsightRetrieveRunsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInsights:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Langsmith) -> None:
        insight = client.sessions.insights.create(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InsightCreateResponse, insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Langsmith) -> None:
        insight = client.sessions.insights.create(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            attribute_schemas={"foo": "bar"},
            cluster_model="cluster_model",
            config_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            filter="filter",
            hierarchy=[0],
            is_scheduled=True,
            last_n_hours=0,
            model="openai",
            name="name",
            partitions={"foo": "string"},
            sample=0,
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            summary_model="summary_model",
            summary_prompt="summary_prompt",
            user_context={"foo": "string"},
            validate_model_secrets=True,
        )
        assert_matches_type(InsightCreateResponse, insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Langsmith) -> None:
        response = client.sessions.insights.with_raw_response.create(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight = response.parse()
        assert_matches_type(InsightCreateResponse, insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Langsmith) -> None:
        with client.sessions.insights.with_streaming_response.create(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight = response.parse()
            assert_matches_type(InsightCreateResponse, insight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.sessions.insights.with_raw_response.create(
                session_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Langsmith) -> None:
        insight = client.sessions.insights.update(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )
        assert_matches_type(InsightUpdateResponse, insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Langsmith) -> None:
        response = client.sessions.insights.with_raw_response.update(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight = response.parse()
        assert_matches_type(InsightUpdateResponse, insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Langsmith) -> None:
        with client.sessions.insights.with_streaming_response.update(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight = response.parse()
            assert_matches_type(InsightUpdateResponse, insight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.sessions.insights.with_raw_response.update(
                job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                session_id="",
                name="name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.sessions.insights.with_raw_response.update(
                job_id="",
                session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                name="name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Langsmith) -> None:
        insight = client.sessions.insights.list(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SyncOffsetPaginationInsightsClusteringJobs[InsightListResponse], insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Langsmith) -> None:
        insight = client.sessions.insights.list(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            config_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            legacy=True,
            limit=1,
            offset=0,
        )
        assert_matches_type(SyncOffsetPaginationInsightsClusteringJobs[InsightListResponse], insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Langsmith) -> None:
        response = client.sessions.insights.with_raw_response.list(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight = response.parse()
        assert_matches_type(SyncOffsetPaginationInsightsClusteringJobs[InsightListResponse], insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Langsmith) -> None:
        with client.sessions.insights.with_streaming_response.list(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight = response.parse()
            assert_matches_type(
                SyncOffsetPaginationInsightsClusteringJobs[InsightListResponse], insight, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.sessions.insights.with_raw_response.list(
                session_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Langsmith) -> None:
        insight = client.sessions.insights.delete(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InsightDeleteResponse, insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Langsmith) -> None:
        response = client.sessions.insights.with_raw_response.delete(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight = response.parse()
        assert_matches_type(InsightDeleteResponse, insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Langsmith) -> None:
        with client.sessions.insights.with_streaming_response.delete(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight = response.parse()
            assert_matches_type(InsightDeleteResponse, insight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.sessions.insights.with_raw_response.delete(
                job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.sessions.insights.with_raw_response.delete(
                job_id="",
                session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_job(self, client: Langsmith) -> None:
        insight = client.sessions.insights.retrieve_job(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InsightRetrieveJobResponse, insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_job(self, client: Langsmith) -> None:
        response = client.sessions.insights.with_raw_response.retrieve_job(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight = response.parse()
        assert_matches_type(InsightRetrieveJobResponse, insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_job(self, client: Langsmith) -> None:
        with client.sessions.insights.with_streaming_response.retrieve_job(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight = response.parse()
            assert_matches_type(InsightRetrieveJobResponse, insight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_job(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.sessions.insights.with_raw_response.retrieve_job(
                job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.sessions.insights.with_raw_response.retrieve_job(
                job_id="",
                session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_runs(self, client: Langsmith) -> None:
        insight = client.sessions.insights.retrieve_runs(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InsightRetrieveRunsResponse, insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_runs_with_all_params(self, client: Langsmith) -> None:
        insight = client.sessions.insights.retrieve_runs(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            attribute_sort_key="attribute_sort_key",
            attribute_sort_order="asc",
            cluster_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
            offset=0,
        )
        assert_matches_type(InsightRetrieveRunsResponse, insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_runs(self, client: Langsmith) -> None:
        response = client.sessions.insights.with_raw_response.retrieve_runs(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight = response.parse()
        assert_matches_type(InsightRetrieveRunsResponse, insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_runs(self, client: Langsmith) -> None:
        with client.sessions.insights.with_streaming_response.retrieve_runs(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight = response.parse()
            assert_matches_type(InsightRetrieveRunsResponse, insight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_runs(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.sessions.insights.with_raw_response.retrieve_runs(
                job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.sessions.insights.with_raw_response.retrieve_runs(
                job_id="",
                session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncInsights:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLangsmith) -> None:
        insight = await async_client.sessions.insights.create(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InsightCreateResponse, insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLangsmith) -> None:
        insight = await async_client.sessions.insights.create(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            attribute_schemas={"foo": "bar"},
            cluster_model="cluster_model",
            config_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            filter="filter",
            hierarchy=[0],
            is_scheduled=True,
            last_n_hours=0,
            model="openai",
            name="name",
            partitions={"foo": "string"},
            sample=0,
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            summary_model="summary_model",
            summary_prompt="summary_prompt",
            user_context={"foo": "string"},
            validate_model_secrets=True,
        )
        assert_matches_type(InsightCreateResponse, insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.sessions.insights.with_raw_response.create(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight = await response.parse()
        assert_matches_type(InsightCreateResponse, insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLangsmith) -> None:
        async with async_client.sessions.insights.with_streaming_response.create(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight = await response.parse()
            assert_matches_type(InsightCreateResponse, insight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.sessions.insights.with_raw_response.create(
                session_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncLangsmith) -> None:
        insight = await async_client.sessions.insights.update(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )
        assert_matches_type(InsightUpdateResponse, insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.sessions.insights.with_raw_response.update(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight = await response.parse()
        assert_matches_type(InsightUpdateResponse, insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLangsmith) -> None:
        async with async_client.sessions.insights.with_streaming_response.update(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight = await response.parse()
            assert_matches_type(InsightUpdateResponse, insight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.sessions.insights.with_raw_response.update(
                job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                session_id="",
                name="name",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.sessions.insights.with_raw_response.update(
                job_id="",
                session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                name="name",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLangsmith) -> None:
        insight = await async_client.sessions.insights.list(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(
            AsyncOffsetPaginationInsightsClusteringJobs[InsightListResponse], insight, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLangsmith) -> None:
        insight = await async_client.sessions.insights.list(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            config_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            legacy=True,
            limit=1,
            offset=0,
        )
        assert_matches_type(
            AsyncOffsetPaginationInsightsClusteringJobs[InsightListResponse], insight, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.sessions.insights.with_raw_response.list(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight = await response.parse()
        assert_matches_type(
            AsyncOffsetPaginationInsightsClusteringJobs[InsightListResponse], insight, path=["response"]
        )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLangsmith) -> None:
        async with async_client.sessions.insights.with_streaming_response.list(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight = await response.parse()
            assert_matches_type(
                AsyncOffsetPaginationInsightsClusteringJobs[InsightListResponse], insight, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.sessions.insights.with_raw_response.list(
                session_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLangsmith) -> None:
        insight = await async_client.sessions.insights.delete(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InsightDeleteResponse, insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.sessions.insights.with_raw_response.delete(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight = await response.parse()
        assert_matches_type(InsightDeleteResponse, insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLangsmith) -> None:
        async with async_client.sessions.insights.with_streaming_response.delete(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight = await response.parse()
            assert_matches_type(InsightDeleteResponse, insight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.sessions.insights.with_raw_response.delete(
                job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.sessions.insights.with_raw_response.delete(
                job_id="",
                session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_job(self, async_client: AsyncLangsmith) -> None:
        insight = await async_client.sessions.insights.retrieve_job(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InsightRetrieveJobResponse, insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_job(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.sessions.insights.with_raw_response.retrieve_job(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight = await response.parse()
        assert_matches_type(InsightRetrieveJobResponse, insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_job(self, async_client: AsyncLangsmith) -> None:
        async with async_client.sessions.insights.with_streaming_response.retrieve_job(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight = await response.parse()
            assert_matches_type(InsightRetrieveJobResponse, insight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_job(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.sessions.insights.with_raw_response.retrieve_job(
                job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.sessions.insights.with_raw_response.retrieve_job(
                job_id="",
                session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_runs(self, async_client: AsyncLangsmith) -> None:
        insight = await async_client.sessions.insights.retrieve_runs(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(InsightRetrieveRunsResponse, insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_runs_with_all_params(self, async_client: AsyncLangsmith) -> None:
        insight = await async_client.sessions.insights.retrieve_runs(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            attribute_sort_key="attribute_sort_key",
            attribute_sort_order="asc",
            cluster_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            limit=1,
            offset=0,
        )
        assert_matches_type(InsightRetrieveRunsResponse, insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_runs(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.sessions.insights.with_raw_response.retrieve_runs(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        insight = await response.parse()
        assert_matches_type(InsightRetrieveRunsResponse, insight, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_runs(self, async_client: AsyncLangsmith) -> None:
        async with async_client.sessions.insights.with_streaming_response.retrieve_runs(
            job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            insight = await response.parse()
            assert_matches_type(InsightRetrieveRunsResponse, insight, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_runs(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.sessions.insights.with_raw_response.retrieve_runs(
                job_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                session_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.sessions.insights.with_raw_response.retrieve_runs(
                job_id="",
                session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
