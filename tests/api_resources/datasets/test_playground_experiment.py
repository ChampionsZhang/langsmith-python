# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from langsmith_api import Langsmith, AsyncLangsmith

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPlaygroundExperiment:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_batch(self, client: Langsmith) -> None:
        playground_experiment = client.datasets.playground_experiment.batch(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            manifest={},
            options={},
            project_name="project_name",
            secrets={"foo": "string"},
        )
        assert_matches_type(object, playground_experiment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_batch_with_all_params(self, client: Langsmith) -> None:
        playground_experiment = client.datasets.playground_experiment.batch(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            manifest={},
            options={
                "callbacks": [{}],
                "configurable": {"foo": "bar"},
                "max_concurrency": 0,
                "metadata": {"foo": "bar"},
                "recursion_limit": 0,
                "run_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "run_name": "run_name",
                "tags": ["string"],
            },
            project_name="project_name",
            secrets={"foo": "string"},
            batch_size=1,
            commit="commit",
            dataset_splits=["string"],
            evaluator_rules=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            metadata={"foo": "bar"},
            owner="owner",
            parallel_tool_calls=True,
            repetitions=1,
            repo_handle="repo_handle",
            repo_id="repo_id",
            requests_per_second=0,
            run_id="run_id",
            runner_context="langsmith_ui",
            tool_choice="tool_choice",
            tools=[{}],
            use_or_fallback_to_workspace_secrets=True,
        )
        assert_matches_type(object, playground_experiment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_batch(self, client: Langsmith) -> None:
        response = client.datasets.playground_experiment.with_raw_response.batch(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            manifest={},
            options={},
            project_name="project_name",
            secrets={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        playground_experiment = response.parse()
        assert_matches_type(object, playground_experiment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_batch(self, client: Langsmith) -> None:
        with client.datasets.playground_experiment.with_streaming_response.batch(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            manifest={},
            options={},
            project_name="project_name",
            secrets={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            playground_experiment = response.parse()
            assert_matches_type(object, playground_experiment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream(self, client: Langsmith) -> None:
        playground_experiment = client.datasets.playground_experiment.stream(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            manifest={},
            options={},
            project_name="project_name",
            secrets={"foo": "string"},
        )
        assert_matches_type(object, playground_experiment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_stream_with_all_params(self, client: Langsmith) -> None:
        playground_experiment = client.datasets.playground_experiment.stream(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            manifest={},
            options={
                "callbacks": [{}],
                "configurable": {"foo": "bar"},
                "max_concurrency": 0,
                "metadata": {"foo": "bar"},
                "recursion_limit": 0,
                "run_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "run_name": "run_name",
                "tags": ["string"],
            },
            project_name="project_name",
            secrets={"foo": "string"},
            commit="commit",
            dataset_splits=["string"],
            evaluator_rules=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            metadata={"foo": "bar"},
            owner="owner",
            parallel_tool_calls=True,
            repetitions=1,
            repo_handle="repo_handle",
            repo_id="repo_id",
            requests_per_second=0,
            run_id="run_id",
            runner_context="langsmith_ui",
            tool_choice="tool_choice",
            tools=[{}],
            use_or_fallback_to_workspace_secrets=True,
        )
        assert_matches_type(object, playground_experiment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_stream(self, client: Langsmith) -> None:
        response = client.datasets.playground_experiment.with_raw_response.stream(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            manifest={},
            options={},
            project_name="project_name",
            secrets={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        playground_experiment = response.parse()
        assert_matches_type(object, playground_experiment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_stream(self, client: Langsmith) -> None:
        with client.datasets.playground_experiment.with_streaming_response.stream(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            manifest={},
            options={},
            project_name="project_name",
            secrets={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            playground_experiment = response.parse()
            assert_matches_type(object, playground_experiment, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPlaygroundExperiment:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_batch(self, async_client: AsyncLangsmith) -> None:
        playground_experiment = await async_client.datasets.playground_experiment.batch(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            manifest={},
            options={},
            project_name="project_name",
            secrets={"foo": "string"},
        )
        assert_matches_type(object, playground_experiment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_batch_with_all_params(self, async_client: AsyncLangsmith) -> None:
        playground_experiment = await async_client.datasets.playground_experiment.batch(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            manifest={},
            options={
                "callbacks": [{}],
                "configurable": {"foo": "bar"},
                "max_concurrency": 0,
                "metadata": {"foo": "bar"},
                "recursion_limit": 0,
                "run_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "run_name": "run_name",
                "tags": ["string"],
            },
            project_name="project_name",
            secrets={"foo": "string"},
            batch_size=1,
            commit="commit",
            dataset_splits=["string"],
            evaluator_rules=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            metadata={"foo": "bar"},
            owner="owner",
            parallel_tool_calls=True,
            repetitions=1,
            repo_handle="repo_handle",
            repo_id="repo_id",
            requests_per_second=0,
            run_id="run_id",
            runner_context="langsmith_ui",
            tool_choice="tool_choice",
            tools=[{}],
            use_or_fallback_to_workspace_secrets=True,
        )
        assert_matches_type(object, playground_experiment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_batch(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.datasets.playground_experiment.with_raw_response.batch(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            manifest={},
            options={},
            project_name="project_name",
            secrets={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        playground_experiment = await response.parse()
        assert_matches_type(object, playground_experiment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_batch(self, async_client: AsyncLangsmith) -> None:
        async with async_client.datasets.playground_experiment.with_streaming_response.batch(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            manifest={},
            options={},
            project_name="project_name",
            secrets={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            playground_experiment = await response.parse()
            assert_matches_type(object, playground_experiment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream(self, async_client: AsyncLangsmith) -> None:
        playground_experiment = await async_client.datasets.playground_experiment.stream(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            manifest={},
            options={},
            project_name="project_name",
            secrets={"foo": "string"},
        )
        assert_matches_type(object, playground_experiment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_stream_with_all_params(self, async_client: AsyncLangsmith) -> None:
        playground_experiment = await async_client.datasets.playground_experiment.stream(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            manifest={},
            options={
                "callbacks": [{}],
                "configurable": {"foo": "bar"},
                "max_concurrency": 0,
                "metadata": {"foo": "bar"},
                "recursion_limit": 0,
                "run_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "run_name": "run_name",
                "tags": ["string"],
            },
            project_name="project_name",
            secrets={"foo": "string"},
            commit="commit",
            dataset_splits=["string"],
            evaluator_rules=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            metadata={"foo": "bar"},
            owner="owner",
            parallel_tool_calls=True,
            repetitions=1,
            repo_handle="repo_handle",
            repo_id="repo_id",
            requests_per_second=0,
            run_id="run_id",
            runner_context="langsmith_ui",
            tool_choice="tool_choice",
            tools=[{}],
            use_or_fallback_to_workspace_secrets=True,
        )
        assert_matches_type(object, playground_experiment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_stream(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.datasets.playground_experiment.with_raw_response.stream(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            manifest={},
            options={},
            project_name="project_name",
            secrets={"foo": "string"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        playground_experiment = await response.parse()
        assert_matches_type(object, playground_experiment, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_stream(self, async_client: AsyncLangsmith) -> None:
        async with async_client.datasets.playground_experiment.with_streaming_response.stream(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            manifest={},
            options={},
            project_name="project_name",
            secrets={"foo": "string"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            playground_experiment = await response.parse()
            assert_matches_type(object, playground_experiment, path=["response"])

        assert cast(Any, response.is_closed) is True
