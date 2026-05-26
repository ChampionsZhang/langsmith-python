# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from langsmith_api import Langsmith, AsyncLangsmith
from langsmith_api.types import (
    TracerSession,
    CustomChartsSection,
    TracerSessionWithoutVirtualFields,
)
from langsmith_api._utils import parse_datetime
from langsmith_api.pagination import SyncOffsetPaginationTopLevelArray, AsyncOffsetPaginationTopLevelArray

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSessions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Langsmith) -> None:
        session = client.sessions.create()
        assert_matches_type(TracerSessionWithoutVirtualFields, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Langsmith) -> None:
        session = client.sessions.create(
            upsert=True,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            default_dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            extra={"foo": "bar"},
            name="name",
            reference_dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            trace_tier="longlived",
        )
        assert_matches_type(TracerSessionWithoutVirtualFields, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Langsmith) -> None:
        response = client.sessions.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(TracerSessionWithoutVirtualFields, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Langsmith) -> None:
        with client.sessions.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(TracerSessionWithoutVirtualFields, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Langsmith) -> None:
        session = client.sessions.retrieve(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TracerSession, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Langsmith) -> None:
        session = client.sessions.retrieve(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            include_stats=True,
            stats_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            accept="accept",
        )
        assert_matches_type(TracerSession, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Langsmith) -> None:
        response = client.sessions.with_raw_response.retrieve(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(TracerSession, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Langsmith) -> None:
        with client.sessions.with_streaming_response.retrieve(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(TracerSession, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.sessions.with_raw_response.retrieve(
                session_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Langsmith) -> None:
        session = client.sessions.update(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TracerSessionWithoutVirtualFields, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Langsmith) -> None:
        session = client.sessions.update(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            default_dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            extra={"foo": "bar"},
            name="name",
            trace_tier="longlived",
        )
        assert_matches_type(TracerSessionWithoutVirtualFields, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Langsmith) -> None:
        response = client.sessions.with_raw_response.update(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(TracerSessionWithoutVirtualFields, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Langsmith) -> None:
        with client.sessions.with_streaming_response.update(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(TracerSessionWithoutVirtualFields, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.sessions.with_raw_response.update(
                session_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Langsmith) -> None:
        session = client.sessions.list()
        assert_matches_type(SyncOffsetPaginationTopLevelArray[TracerSession], session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Langsmith) -> None:
        session = client.sessions.list(
            id=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            dataset_version="dataset_version",
            facets=True,
            filter="filter",
            include_stats=True,
            limit=1,
            metadata="metadata",
            name="name",
            name_contains="name_contains",
            offset=0,
            reference_dataset=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            reference_free=True,
            sort_by="name",
            sort_by_desc=True,
            sort_by_feedback_key="sort_by_feedback_key",
            sort_by_feedback_source="session",
            stats_filter="stats_filter",
            stats_select=["string"],
            stats_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            tag_value_id=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            use_approx_stats=True,
            accept="accept",
        )
        assert_matches_type(SyncOffsetPaginationTopLevelArray[TracerSession], session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Langsmith) -> None:
        response = client.sessions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(SyncOffsetPaginationTopLevelArray[TracerSession], session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Langsmith) -> None:
        with client.sessions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(SyncOffsetPaginationTopLevelArray[TracerSession], session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Langsmith) -> None:
        session = client.sessions.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Langsmith) -> None:
        response = client.sessions.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(object, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Langsmith) -> None:
        with client.sessions.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(object, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.sessions.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_dashboard(self, client: Langsmith) -> None:
        session = client.sessions.dashboard(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomChartsSection, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_dashboard_with_all_params(self, client: Langsmith) -> None:
        session = client.sessions.dashboard(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            group_by={
                "attribute": "name",
                "max_groups": 0,
                "path": "path",
            },
            omit_data=True,
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            stride={
                "days": 0,
                "hours": 0,
                "minutes": 0,
            },
            timezone="timezone",
            accept="accept",
        )
        assert_matches_type(CustomChartsSection, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_dashboard(self, client: Langsmith) -> None:
        response = client.sessions.with_raw_response.dashboard(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = response.parse()
        assert_matches_type(CustomChartsSection, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_dashboard(self, client: Langsmith) -> None:
        with client.sessions.with_streaming_response.dashboard(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = response.parse()
            assert_matches_type(CustomChartsSection, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_dashboard(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            client.sessions.with_raw_response.dashboard(
                session_id="",
            )


class TestAsyncSessions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLangsmith) -> None:
        session = await async_client.sessions.create()
        assert_matches_type(TracerSessionWithoutVirtualFields, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLangsmith) -> None:
        session = await async_client.sessions.create(
            upsert=True,
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            default_dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            extra={"foo": "bar"},
            name="name",
            reference_dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            trace_tier="longlived",
        )
        assert_matches_type(TracerSessionWithoutVirtualFields, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.sessions.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(TracerSessionWithoutVirtualFields, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLangsmith) -> None:
        async with async_client.sessions.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(TracerSessionWithoutVirtualFields, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLangsmith) -> None:
        session = await async_client.sessions.retrieve(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TracerSession, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncLangsmith) -> None:
        session = await async_client.sessions.retrieve(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            include_stats=True,
            stats_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            accept="accept",
        )
        assert_matches_type(TracerSession, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.sessions.with_raw_response.retrieve(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(TracerSession, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLangsmith) -> None:
        async with async_client.sessions.with_streaming_response.retrieve(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(TracerSession, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.sessions.with_raw_response.retrieve(
                session_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncLangsmith) -> None:
        session = await async_client.sessions.update(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(TracerSessionWithoutVirtualFields, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLangsmith) -> None:
        session = await async_client.sessions.update(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            default_dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="description",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            extra={"foo": "bar"},
            name="name",
            trace_tier="longlived",
        )
        assert_matches_type(TracerSessionWithoutVirtualFields, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.sessions.with_raw_response.update(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(TracerSessionWithoutVirtualFields, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLangsmith) -> None:
        async with async_client.sessions.with_streaming_response.update(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(TracerSessionWithoutVirtualFields, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.sessions.with_raw_response.update(
                session_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLangsmith) -> None:
        session = await async_client.sessions.list()
        assert_matches_type(AsyncOffsetPaginationTopLevelArray[TracerSession], session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLangsmith) -> None:
        session = await async_client.sessions.list(
            id=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            dataset_version="dataset_version",
            facets=True,
            filter="filter",
            include_stats=True,
            limit=1,
            metadata="metadata",
            name="name",
            name_contains="name_contains",
            offset=0,
            reference_dataset=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            reference_free=True,
            sort_by="name",
            sort_by_desc=True,
            sort_by_feedback_key="sort_by_feedback_key",
            sort_by_feedback_source="session",
            stats_filter="stats_filter",
            stats_select=["string"],
            stats_start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            tag_value_id=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            use_approx_stats=True,
            accept="accept",
        )
        assert_matches_type(AsyncOffsetPaginationTopLevelArray[TracerSession], session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.sessions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(AsyncOffsetPaginationTopLevelArray[TracerSession], session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLangsmith) -> None:
        async with async_client.sessions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(AsyncOffsetPaginationTopLevelArray[TracerSession], session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLangsmith) -> None:
        session = await async_client.sessions.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.sessions.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(object, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLangsmith) -> None:
        async with async_client.sessions.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(object, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.sessions.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_dashboard(self, async_client: AsyncLangsmith) -> None:
        session = await async_client.sessions.dashboard(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(CustomChartsSection, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_dashboard_with_all_params(self, async_client: AsyncLangsmith) -> None:
        session = await async_client.sessions.dashboard(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            end_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            group_by={
                "attribute": "name",
                "max_groups": 0,
                "path": "path",
            },
            omit_data=True,
            start_time=parse_datetime("2019-12-27T18:11:19.117Z"),
            stride={
                "days": 0,
                "hours": 0,
                "minutes": 0,
            },
            timezone="timezone",
            accept="accept",
        )
        assert_matches_type(CustomChartsSection, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_dashboard(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.sessions.with_raw_response.dashboard(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        session = await response.parse()
        assert_matches_type(CustomChartsSection, session, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_dashboard(self, async_client: AsyncLangsmith) -> None:
        async with async_client.sessions.with_streaming_response.dashboard(
            session_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            session = await response.parse()
            assert_matches_type(CustomChartsSection, session, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_dashboard(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `session_id` but received ''"):
            await async_client.sessions.with_raw_response.dashboard(
                session_id="",
            )
