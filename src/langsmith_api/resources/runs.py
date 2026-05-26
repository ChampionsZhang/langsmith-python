# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, List, Union, Iterable, Optional, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ..types import (
    RunTypeEnum,
    RunsFilterDataSourceTypeEnum,
    run_query_params,
    run_stats_params,
    run_create_params,
    run_update_params,
    run_retrieve_params,
    run_ingest_batch_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.run_param import RunParam
from ..types.run_schema import RunSchema
from ..types.run_type_enum import RunTypeEnum
from ..types.run_query_response import RunQueryResponse
from ..types.run_stats_response import RunStatsResponse
from ..types.run_create_response import RunCreateResponse
from ..types.run_update_response import RunUpdateResponse
from ..types.run_stats_group_by_param import RunStatsGroupByParam
from ..types.run_ingest_batch_response import RunIngestBatchResponse
from ..types.runs_filter_data_source_type_enum import RunsFilterDataSourceTypeEnum

__all__ = ["RunsResource", "AsyncRunsResource"]


class RunsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/langchain-python#accessing-raw-response-data-eg-headers
        """
        return RunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/langchain-python#with_streaming_response
        """
        return RunsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        id: str | Omit = omit,
        dotted_order: str | Omit = omit,
        end_time: str | Omit = omit,
        error: str | Omit = omit,
        events: Iterable[Dict[str, object]] | Omit = omit,
        extra: Dict[str, object] | Omit = omit,
        input_attachments: Dict[str, object] | Omit = omit,
        inputs: Dict[str, object] | Omit = omit,
        name: str | Omit = omit,
        output_attachments: Dict[str, object] | Omit = omit,
        outputs: Dict[str, object] | Omit = omit,
        parent_run_id: str | Omit = omit,
        reference_example_id: str | Omit = omit,
        run_type: Literal["tool", "chain", "llm", "retriever", "embedding", "prompt", "parser"] | Omit = omit,
        serialized: Dict[str, object] | Omit = omit,
        session_id: str | Omit = omit,
        session_name: str | Omit = omit,
        start_time: str | Omit = omit,
        status: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunCreateResponse:
        """Queues a single run for ingestion.

        The request body must be a JSON-encoded run
        object that follows the Run schema.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/runs",
            body=maybe_transform(
                {
                    "id": id,
                    "dotted_order": dotted_order,
                    "end_time": end_time,
                    "error": error,
                    "events": events,
                    "extra": extra,
                    "input_attachments": input_attachments,
                    "inputs": inputs,
                    "name": name,
                    "output_attachments": output_attachments,
                    "outputs": outputs,
                    "parent_run_id": parent_run_id,
                    "reference_example_id": reference_example_id,
                    "run_type": run_type,
                    "serialized": serialized,
                    "session_id": session_id,
                    "session_name": session_name,
                    "start_time": start_time,
                    "status": status,
                    "tags": tags,
                    "trace_id": trace_id,
                },
                run_create_params.RunCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunCreateResponse,
        )

    def retrieve(
        self,
        run_id: str,
        *,
        exclude_s3_stored_attributes: bool | Omit = omit,
        exclude_serialized: bool | Omit = omit,
        include_messages: bool | Omit = omit,
        session_id: Optional[str] | Omit = omit,
        start_time: Union[str, datetime, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunSchema:
        """
        Get a specific run.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._get(
            path_template("/api/v1/runs/{run_id}", run_id=run_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "exclude_s3_stored_attributes": exclude_s3_stored_attributes,
                        "exclude_serialized": exclude_serialized,
                        "include_messages": include_messages,
                        "session_id": session_id,
                        "start_time": start_time,
                    },
                    run_retrieve_params.RunRetrieveParams,
                ),
            ),
            cast_to=RunSchema,
        )

    def update(
        self,
        run_id: str,
        *,
        id: str | Omit = omit,
        dotted_order: str | Omit = omit,
        end_time: str | Omit = omit,
        error: str | Omit = omit,
        events: Iterable[Dict[str, object]] | Omit = omit,
        extra: Dict[str, object] | Omit = omit,
        input_attachments: Dict[str, object] | Omit = omit,
        inputs: Dict[str, object] | Omit = omit,
        name: str | Omit = omit,
        output_attachments: Dict[str, object] | Omit = omit,
        outputs: Dict[str, object] | Omit = omit,
        parent_run_id: str | Omit = omit,
        reference_example_id: str | Omit = omit,
        run_type: Literal["tool", "chain", "llm", "retriever", "embedding", "prompt", "parser"] | Omit = omit,
        serialized: Dict[str, object] | Omit = omit,
        session_id: str | Omit = omit,
        session_name: str | Omit = omit,
        start_time: str | Omit = omit,
        status: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunUpdateResponse:
        """Updates a run identified by its ID.

        The body should contain only the fields to
        be changed; unknown fields are ignored.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._patch(
            path_template("/runs/{run_id}", run_id=run_id),
            body=maybe_transform(
                {
                    "id": id,
                    "dotted_order": dotted_order,
                    "end_time": end_time,
                    "error": error,
                    "events": events,
                    "extra": extra,
                    "input_attachments": input_attachments,
                    "inputs": inputs,
                    "name": name,
                    "output_attachments": output_attachments,
                    "outputs": outputs,
                    "parent_run_id": parent_run_id,
                    "reference_example_id": reference_example_id,
                    "run_type": run_type,
                    "serialized": serialized,
                    "session_id": session_id,
                    "session_name": session_name,
                    "start_time": start_time,
                    "status": status,
                    "tags": tags,
                    "trace_id": trace_id,
                },
                run_update_params.RunUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunUpdateResponse,
        )

    def ingest_batch(
        self,
        *,
        patch: Iterable[RunParam] | Omit = omit,
        post: Iterable[RunParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunIngestBatchResponse:
        """Ingests a batch of runs in a single JSON payload.

        The payload must have `post`
        and/or `patch` arrays containing run objects. Prefer this endpoint over
        single‑run ingestion when submitting hundreds of runs, but `/runs/multipart`
        offers better handling for very large fields and attachments.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/runs/batch",
            body=maybe_transform(
                {
                    "patch": patch,
                    "post": post,
                },
                run_ingest_batch_params.RunIngestBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunIngestBatchResponse,
        )

    def query(
        self,
        *,
        id: Optional[SequenceNotStr[str]] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        data_source_type: Optional[RunsFilterDataSourceTypeEnum] | Omit = omit,
        end_time: Union[str, datetime, None] | Omit = omit,
        error: Optional[bool] | Omit = omit,
        execution_order: Optional[int] | Omit = omit,
        filter: Optional[str] | Omit = omit,
        is_root: Optional[bool] | Omit = omit,
        limit: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        parent_run: Optional[str] | Omit = omit,
        query: Optional[str] | Omit = omit,
        reference_example: Optional[SequenceNotStr[str]] | Omit = omit,
        run_type: Optional[RunTypeEnum] | Omit = omit,
        search_filter: Optional[str] | Omit = omit,
        select: List[
            Literal[
                "id",
                "name",
                "run_type",
                "start_time",
                "end_time",
                "status",
                "error",
                "extra",
                "events",
                "inputs",
                "inputs_preview",
                "inputs_s3_urls",
                "inputs_or_signed_url",
                "outputs",
                "outputs_preview",
                "outputs_s3_urls",
                "outputs_or_signed_url",
                "s3_urls",
                "error_or_signed_url",
                "events_or_signed_url",
                "extra_or_signed_url",
                "serialized_or_signed_url",
                "parent_run_id",
                "manifest_id",
                "manifest_s3_id",
                "manifest",
                "session_id",
                "serialized",
                "reference_example_id",
                "reference_dataset_id",
                "total_tokens",
                "prompt_tokens",
                "prompt_token_details",
                "completion_tokens",
                "completion_token_details",
                "total_cost",
                "prompt_cost",
                "prompt_cost_details",
                "completion_cost",
                "completion_cost_details",
                "price_model_id",
                "first_token_time",
                "trace_id",
                "dotted_order",
                "last_queued_at",
                "feedback_stats",
                "child_run_ids",
                "parent_run_ids",
                "tags",
                "in_dataset",
                "app_path",
                "share_token",
                "trace_tier",
                "trace_first_received_at",
                "ttl_seconds",
                "trace_upgrade",
                "thread_id",
                "trace_min_max_start_time",
                "messages",
                "inserted_at",
            ]
        ]
        | Omit = omit,
        session: Optional[SequenceNotStr[str]] | Omit = omit,
        skip_pagination: Optional[bool] | Omit = omit,
        skip_prev_cursor: bool | Omit = omit,
        start_time: Union[str, datetime, None] | Omit = omit,
        trace: Optional[str] | Omit = omit,
        trace_filter: Optional[str] | Omit = omit,
        tree_filter: Optional[str] | Omit = omit,
        use_experimental_search: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunQueryResponse:
        """
        Query Runs

        Args:
          data_source_type: Enum for run data source types.

          order: Enum for run start date order.

          run_type: Enum for run types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/api/v1/runs/query",
            body=maybe_transform(
                {
                    "id": id,
                    "cursor": cursor,
                    "data_source_type": data_source_type,
                    "end_time": end_time,
                    "error": error,
                    "execution_order": execution_order,
                    "filter": filter,
                    "is_root": is_root,
                    "limit": limit,
                    "order": order,
                    "parent_run": parent_run,
                    "query": query,
                    "reference_example": reference_example,
                    "run_type": run_type,
                    "search_filter": search_filter,
                    "select": select,
                    "session": session,
                    "skip_pagination": skip_pagination,
                    "skip_prev_cursor": skip_prev_cursor,
                    "start_time": start_time,
                    "trace": trace,
                    "trace_filter": trace_filter,
                    "tree_filter": tree_filter,
                    "use_experimental_search": use_experimental_search,
                },
                run_query_params.RunQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunQueryResponse,
        )

    def stats(
        self,
        *,
        id: Optional[SequenceNotStr[str]] | Omit = omit,
        data_source_type: Optional[RunsFilterDataSourceTypeEnum] | Omit = omit,
        end_time: Union[str, datetime, None] | Omit = omit,
        error: Optional[bool] | Omit = omit,
        execution_order: Optional[int] | Omit = omit,
        filter: Optional[str] | Omit = omit,
        group_by: Optional[RunStatsGroupByParam] | Omit = omit,
        groups: Optional[SequenceNotStr[Optional[str]]] | Omit = omit,
        is_root: Optional[bool] | Omit = omit,
        parent_run: Optional[str] | Omit = omit,
        query: Optional[str] | Omit = omit,
        reference_example: Optional[SequenceNotStr[str]] | Omit = omit,
        run_type: Optional[RunTypeEnum] | Omit = omit,
        search_filter: Optional[str] | Omit = omit,
        select: Optional[
            List[
                Literal[
                    "run_count",
                    "latency_p50",
                    "latency_p99",
                    "latency_avg",
                    "first_token_p50",
                    "first_token_p99",
                    "total_tokens",
                    "prompt_tokens",
                    "completion_tokens",
                    "median_tokens",
                    "completion_tokens_p50",
                    "prompt_tokens_p50",
                    "tokens_p99",
                    "completion_tokens_p99",
                    "prompt_tokens_p99",
                    "last_run_start_time",
                    "feedback_stats",
                    "thread_feedback_stats",
                    "run_facets",
                    "error_rate",
                    "streaming_rate",
                    "total_cost",
                    "prompt_cost",
                    "completion_cost",
                    "cost_p50",
                    "cost_p99",
                    "session_feedback_stats",
                    "all_run_stats",
                    "all_token_stats",
                    "prompt_token_details",
                    "completion_token_details",
                    "prompt_cost_details",
                    "completion_cost_details",
                ]
            ]
        ]
        | Omit = omit,
        session: Optional[SequenceNotStr[str]] | Omit = omit,
        skip_pagination: Optional[bool] | Omit = omit,
        start_time: Union[str, datetime, None] | Omit = omit,
        trace: Optional[str] | Omit = omit,
        trace_filter: Optional[str] | Omit = omit,
        tree_filter: Optional[str] | Omit = omit,
        use_experimental_search: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunStatsResponse:
        """
        Get all runs by query in body payload.

        Args:
          data_source_type: Enum for run data source types.

          group_by: Group by param for run stats.

          run_type: Enum for run types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            RunStatsResponse,
            self._post(
                "/api/v1/runs/stats",
                body=maybe_transform(
                    {
                        "id": id,
                        "data_source_type": data_source_type,
                        "end_time": end_time,
                        "error": error,
                        "execution_order": execution_order,
                        "filter": filter,
                        "group_by": group_by,
                        "groups": groups,
                        "is_root": is_root,
                        "parent_run": parent_run,
                        "query": query,
                        "reference_example": reference_example,
                        "run_type": run_type,
                        "search_filter": search_filter,
                        "select": select,
                        "session": session,
                        "skip_pagination": skip_pagination,
                        "start_time": start_time,
                        "trace": trace,
                        "trace_filter": trace_filter,
                        "tree_filter": tree_filter,
                        "use_experimental_search": use_experimental_search,
                    },
                    run_stats_params.RunStatsParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, RunStatsResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def update_2(
        self,
        run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Update a run.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return self._patch(
            path_template("/api/v1/runs/{run_id}", run_id=run_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncRunsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRunsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/langchain-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRunsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRunsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/langchain-python#with_streaming_response
        """
        return AsyncRunsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        id: str | Omit = omit,
        dotted_order: str | Omit = omit,
        end_time: str | Omit = omit,
        error: str | Omit = omit,
        events: Iterable[Dict[str, object]] | Omit = omit,
        extra: Dict[str, object] | Omit = omit,
        input_attachments: Dict[str, object] | Omit = omit,
        inputs: Dict[str, object] | Omit = omit,
        name: str | Omit = omit,
        output_attachments: Dict[str, object] | Omit = omit,
        outputs: Dict[str, object] | Omit = omit,
        parent_run_id: str | Omit = omit,
        reference_example_id: str | Omit = omit,
        run_type: Literal["tool", "chain", "llm", "retriever", "embedding", "prompt", "parser"] | Omit = omit,
        serialized: Dict[str, object] | Omit = omit,
        session_id: str | Omit = omit,
        session_name: str | Omit = omit,
        start_time: str | Omit = omit,
        status: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunCreateResponse:
        """Queues a single run for ingestion.

        The request body must be a JSON-encoded run
        object that follows the Run schema.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/runs",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "dotted_order": dotted_order,
                    "end_time": end_time,
                    "error": error,
                    "events": events,
                    "extra": extra,
                    "input_attachments": input_attachments,
                    "inputs": inputs,
                    "name": name,
                    "output_attachments": output_attachments,
                    "outputs": outputs,
                    "parent_run_id": parent_run_id,
                    "reference_example_id": reference_example_id,
                    "run_type": run_type,
                    "serialized": serialized,
                    "session_id": session_id,
                    "session_name": session_name,
                    "start_time": start_time,
                    "status": status,
                    "tags": tags,
                    "trace_id": trace_id,
                },
                run_create_params.RunCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunCreateResponse,
        )

    async def retrieve(
        self,
        run_id: str,
        *,
        exclude_s3_stored_attributes: bool | Omit = omit,
        exclude_serialized: bool | Omit = omit,
        include_messages: bool | Omit = omit,
        session_id: Optional[str] | Omit = omit,
        start_time: Union[str, datetime, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunSchema:
        """
        Get a specific run.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._get(
            path_template("/api/v1/runs/{run_id}", run_id=run_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "exclude_s3_stored_attributes": exclude_s3_stored_attributes,
                        "exclude_serialized": exclude_serialized,
                        "include_messages": include_messages,
                        "session_id": session_id,
                        "start_time": start_time,
                    },
                    run_retrieve_params.RunRetrieveParams,
                ),
            ),
            cast_to=RunSchema,
        )

    async def update(
        self,
        run_id: str,
        *,
        id: str | Omit = omit,
        dotted_order: str | Omit = omit,
        end_time: str | Omit = omit,
        error: str | Omit = omit,
        events: Iterable[Dict[str, object]] | Omit = omit,
        extra: Dict[str, object] | Omit = omit,
        input_attachments: Dict[str, object] | Omit = omit,
        inputs: Dict[str, object] | Omit = omit,
        name: str | Omit = omit,
        output_attachments: Dict[str, object] | Omit = omit,
        outputs: Dict[str, object] | Omit = omit,
        parent_run_id: str | Omit = omit,
        reference_example_id: str | Omit = omit,
        run_type: Literal["tool", "chain", "llm", "retriever", "embedding", "prompt", "parser"] | Omit = omit,
        serialized: Dict[str, object] | Omit = omit,
        session_id: str | Omit = omit,
        session_name: str | Omit = omit,
        start_time: str | Omit = omit,
        status: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        trace_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunUpdateResponse:
        """Updates a run identified by its ID.

        The body should contain only the fields to
        be changed; unknown fields are ignored.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._patch(
            path_template("/runs/{run_id}", run_id=run_id),
            body=await async_maybe_transform(
                {
                    "id": id,
                    "dotted_order": dotted_order,
                    "end_time": end_time,
                    "error": error,
                    "events": events,
                    "extra": extra,
                    "input_attachments": input_attachments,
                    "inputs": inputs,
                    "name": name,
                    "output_attachments": output_attachments,
                    "outputs": outputs,
                    "parent_run_id": parent_run_id,
                    "reference_example_id": reference_example_id,
                    "run_type": run_type,
                    "serialized": serialized,
                    "session_id": session_id,
                    "session_name": session_name,
                    "start_time": start_time,
                    "status": status,
                    "tags": tags,
                    "trace_id": trace_id,
                },
                run_update_params.RunUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunUpdateResponse,
        )

    async def ingest_batch(
        self,
        *,
        patch: Iterable[RunParam] | Omit = omit,
        post: Iterable[RunParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunIngestBatchResponse:
        """Ingests a batch of runs in a single JSON payload.

        The payload must have `post`
        and/or `patch` arrays containing run objects. Prefer this endpoint over
        single‑run ingestion when submitting hundreds of runs, but `/runs/multipart`
        offers better handling for very large fields and attachments.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/runs/batch",
            body=await async_maybe_transform(
                {
                    "patch": patch,
                    "post": post,
                },
                run_ingest_batch_params.RunIngestBatchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunIngestBatchResponse,
        )

    async def query(
        self,
        *,
        id: Optional[SequenceNotStr[str]] | Omit = omit,
        cursor: Optional[str] | Omit = omit,
        data_source_type: Optional[RunsFilterDataSourceTypeEnum] | Omit = omit,
        end_time: Union[str, datetime, None] | Omit = omit,
        error: Optional[bool] | Omit = omit,
        execution_order: Optional[int] | Omit = omit,
        filter: Optional[str] | Omit = omit,
        is_root: Optional[bool] | Omit = omit,
        limit: int | Omit = omit,
        order: Literal["asc", "desc"] | Omit = omit,
        parent_run: Optional[str] | Omit = omit,
        query: Optional[str] | Omit = omit,
        reference_example: Optional[SequenceNotStr[str]] | Omit = omit,
        run_type: Optional[RunTypeEnum] | Omit = omit,
        search_filter: Optional[str] | Omit = omit,
        select: List[
            Literal[
                "id",
                "name",
                "run_type",
                "start_time",
                "end_time",
                "status",
                "error",
                "extra",
                "events",
                "inputs",
                "inputs_preview",
                "inputs_s3_urls",
                "inputs_or_signed_url",
                "outputs",
                "outputs_preview",
                "outputs_s3_urls",
                "outputs_or_signed_url",
                "s3_urls",
                "error_or_signed_url",
                "events_or_signed_url",
                "extra_or_signed_url",
                "serialized_or_signed_url",
                "parent_run_id",
                "manifest_id",
                "manifest_s3_id",
                "manifest",
                "session_id",
                "serialized",
                "reference_example_id",
                "reference_dataset_id",
                "total_tokens",
                "prompt_tokens",
                "prompt_token_details",
                "completion_tokens",
                "completion_token_details",
                "total_cost",
                "prompt_cost",
                "prompt_cost_details",
                "completion_cost",
                "completion_cost_details",
                "price_model_id",
                "first_token_time",
                "trace_id",
                "dotted_order",
                "last_queued_at",
                "feedback_stats",
                "child_run_ids",
                "parent_run_ids",
                "tags",
                "in_dataset",
                "app_path",
                "share_token",
                "trace_tier",
                "trace_first_received_at",
                "ttl_seconds",
                "trace_upgrade",
                "thread_id",
                "trace_min_max_start_time",
                "messages",
                "inserted_at",
            ]
        ]
        | Omit = omit,
        session: Optional[SequenceNotStr[str]] | Omit = omit,
        skip_pagination: Optional[bool] | Omit = omit,
        skip_prev_cursor: bool | Omit = omit,
        start_time: Union[str, datetime, None] | Omit = omit,
        trace: Optional[str] | Omit = omit,
        trace_filter: Optional[str] | Omit = omit,
        tree_filter: Optional[str] | Omit = omit,
        use_experimental_search: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunQueryResponse:
        """
        Query Runs

        Args:
          data_source_type: Enum for run data source types.

          order: Enum for run start date order.

          run_type: Enum for run types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/api/v1/runs/query",
            body=await async_maybe_transform(
                {
                    "id": id,
                    "cursor": cursor,
                    "data_source_type": data_source_type,
                    "end_time": end_time,
                    "error": error,
                    "execution_order": execution_order,
                    "filter": filter,
                    "is_root": is_root,
                    "limit": limit,
                    "order": order,
                    "parent_run": parent_run,
                    "query": query,
                    "reference_example": reference_example,
                    "run_type": run_type,
                    "search_filter": search_filter,
                    "select": select,
                    "session": session,
                    "skip_pagination": skip_pagination,
                    "skip_prev_cursor": skip_prev_cursor,
                    "start_time": start_time,
                    "trace": trace,
                    "trace_filter": trace_filter,
                    "tree_filter": tree_filter,
                    "use_experimental_search": use_experimental_search,
                },
                run_query_params.RunQueryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RunQueryResponse,
        )

    async def stats(
        self,
        *,
        id: Optional[SequenceNotStr[str]] | Omit = omit,
        data_source_type: Optional[RunsFilterDataSourceTypeEnum] | Omit = omit,
        end_time: Union[str, datetime, None] | Omit = omit,
        error: Optional[bool] | Omit = omit,
        execution_order: Optional[int] | Omit = omit,
        filter: Optional[str] | Omit = omit,
        group_by: Optional[RunStatsGroupByParam] | Omit = omit,
        groups: Optional[SequenceNotStr[Optional[str]]] | Omit = omit,
        is_root: Optional[bool] | Omit = omit,
        parent_run: Optional[str] | Omit = omit,
        query: Optional[str] | Omit = omit,
        reference_example: Optional[SequenceNotStr[str]] | Omit = omit,
        run_type: Optional[RunTypeEnum] | Omit = omit,
        search_filter: Optional[str] | Omit = omit,
        select: Optional[
            List[
                Literal[
                    "run_count",
                    "latency_p50",
                    "latency_p99",
                    "latency_avg",
                    "first_token_p50",
                    "first_token_p99",
                    "total_tokens",
                    "prompt_tokens",
                    "completion_tokens",
                    "median_tokens",
                    "completion_tokens_p50",
                    "prompt_tokens_p50",
                    "tokens_p99",
                    "completion_tokens_p99",
                    "prompt_tokens_p99",
                    "last_run_start_time",
                    "feedback_stats",
                    "thread_feedback_stats",
                    "run_facets",
                    "error_rate",
                    "streaming_rate",
                    "total_cost",
                    "prompt_cost",
                    "completion_cost",
                    "cost_p50",
                    "cost_p99",
                    "session_feedback_stats",
                    "all_run_stats",
                    "all_token_stats",
                    "prompt_token_details",
                    "completion_token_details",
                    "prompt_cost_details",
                    "completion_cost_details",
                ]
            ]
        ]
        | Omit = omit,
        session: Optional[SequenceNotStr[str]] | Omit = omit,
        skip_pagination: Optional[bool] | Omit = omit,
        start_time: Union[str, datetime, None] | Omit = omit,
        trace: Optional[str] | Omit = omit,
        trace_filter: Optional[str] | Omit = omit,
        tree_filter: Optional[str] | Omit = omit,
        use_experimental_search: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RunStatsResponse:
        """
        Get all runs by query in body payload.

        Args:
          data_source_type: Enum for run data source types.

          group_by: Group by param for run stats.

          run_type: Enum for run types.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return cast(
            RunStatsResponse,
            await self._post(
                "/api/v1/runs/stats",
                body=await async_maybe_transform(
                    {
                        "id": id,
                        "data_source_type": data_source_type,
                        "end_time": end_time,
                        "error": error,
                        "execution_order": execution_order,
                        "filter": filter,
                        "group_by": group_by,
                        "groups": groups,
                        "is_root": is_root,
                        "parent_run": parent_run,
                        "query": query,
                        "reference_example": reference_example,
                        "run_type": run_type,
                        "search_filter": search_filter,
                        "select": select,
                        "session": session,
                        "skip_pagination": skip_pagination,
                        "start_time": start_time,
                        "trace": trace,
                        "trace_filter": trace_filter,
                        "tree_filter": tree_filter,
                        "use_experimental_search": use_experimental_search,
                    },
                    run_stats_params.RunStatsParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, RunStatsResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def update_2(
        self,
        run_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Update a run.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not run_id:
            raise ValueError(f"Expected a non-empty value for `run_id` but received {run_id!r}")
        return await self._patch(
            path_template("/api/v1/runs/{run_id}", run_id=run_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class RunsResourceWithRawResponse:
    def __init__(self, runs: RunsResource) -> None:
        self._runs = runs

        self.create = to_raw_response_wrapper(
            runs.create,
        )
        self.retrieve = to_raw_response_wrapper(
            runs.retrieve,
        )
        self.update = to_raw_response_wrapper(
            runs.update,
        )
        self.ingest_batch = to_raw_response_wrapper(
            runs.ingest_batch,
        )
        self.query = to_raw_response_wrapper(
            runs.query,
        )
        self.stats = to_raw_response_wrapper(
            runs.stats,
        )
        self.update_2 = to_raw_response_wrapper(
            runs.update_2,
        )


class AsyncRunsResourceWithRawResponse:
    def __init__(self, runs: AsyncRunsResource) -> None:
        self._runs = runs

        self.create = async_to_raw_response_wrapper(
            runs.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            runs.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            runs.update,
        )
        self.ingest_batch = async_to_raw_response_wrapper(
            runs.ingest_batch,
        )
        self.query = async_to_raw_response_wrapper(
            runs.query,
        )
        self.stats = async_to_raw_response_wrapper(
            runs.stats,
        )
        self.update_2 = async_to_raw_response_wrapper(
            runs.update_2,
        )


class RunsResourceWithStreamingResponse:
    def __init__(self, runs: RunsResource) -> None:
        self._runs = runs

        self.create = to_streamed_response_wrapper(
            runs.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            runs.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            runs.update,
        )
        self.ingest_batch = to_streamed_response_wrapper(
            runs.ingest_batch,
        )
        self.query = to_streamed_response_wrapper(
            runs.query,
        )
        self.stats = to_streamed_response_wrapper(
            runs.stats,
        )
        self.update_2 = to_streamed_response_wrapper(
            runs.update_2,
        )


class AsyncRunsResourceWithStreamingResponse:
    def __init__(self, runs: AsyncRunsResource) -> None:
        self._runs = runs

        self.create = async_to_streamed_response_wrapper(
            runs.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            runs.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            runs.update,
        )
        self.ingest_batch = async_to_streamed_response_wrapper(
            runs.ingest_batch,
        )
        self.query = async_to_streamed_response_wrapper(
            runs.query,
        )
        self.stats = async_to_streamed_response_wrapper(
            runs.stats,
        )
        self.update_2 = async_to_streamed_response_wrapper(
            runs.update_2,
        )
