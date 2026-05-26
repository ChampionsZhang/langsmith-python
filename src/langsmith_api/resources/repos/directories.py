# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.repos import directory_list_params, directory_commit_params
from ..._base_client import make_request_options
from ...types.repos.directory_list_response import DirectoryListResponse
from ...types.repos.directory_commit_response import DirectoryCommitResponse

__all__ = ["DirectoriesResource", "AsyncDirectoriesResource"]


class DirectoriesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DirectoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/langchain-python#accessing-raw-response-data-eg-headers
        """
        return DirectoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DirectoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/langchain-python#with_streaming_response
        """
        return DirectoriesResourceWithStreamingResponse(self)

    def list(
        self,
        repo: str,
        *,
        owner: str,
        commit: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DirectoryListResponse:
        """
        Resolves the flattened file tree for an agent or skill repository at a specific
        commit, tag, or latest.

        Args:
          commit: Commit hash/tag to resolve (defaults to latest)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._get(
            path_template("/v1/platform/hub/repos/{owner}/{repo}/directories", owner=owner, repo=repo),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"commit": commit}, directory_list_params.DirectoryListParams),
            ),
            cast_to=DirectoryListResponse,
        )

    def delete(
        self,
        repo: str,
        *,
        owner: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes an agent or skill repository and its owned child file repositories.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/platform/hub/repos/{owner}/{repo}/directories", owner=owner, repo=repo),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def commit(
        self,
        repo: str,
        *,
        owner: str,
        files: Dict[str, object] | Omit = omit,
        parent_commit: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DirectoryCommitResponse:
        """
        Creates a new directory commit for an agent or skill repository by applying
        file/link create, update, and delete operations.

        Args:
          files: Files maps path to an Entry (object = create/update/link, null = delete/unlink).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._post(
            path_template("/v1/platform/hub/repos/{owner}/{repo}/directories/commits", owner=owner, repo=repo),
            body=maybe_transform(
                {
                    "files": files,
                    "parent_commit": parent_commit,
                },
                directory_commit_params.DirectoryCommitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DirectoryCommitResponse,
        )


class AsyncDirectoriesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDirectoriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/langchain-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDirectoriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDirectoriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/langchain-python#with_streaming_response
        """
        return AsyncDirectoriesResourceWithStreamingResponse(self)

    async def list(
        self,
        repo: str,
        *,
        owner: str,
        commit: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DirectoryListResponse:
        """
        Resolves the flattened file tree for an agent or skill repository at a specific
        commit, tag, or latest.

        Args:
          commit: Commit hash/tag to resolve (defaults to latest)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._get(
            path_template("/v1/platform/hub/repos/{owner}/{repo}/directories", owner=owner, repo=repo),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"commit": commit}, directory_list_params.DirectoryListParams),
            ),
            cast_to=DirectoryListResponse,
        )

    async def delete(
        self,
        repo: str,
        *,
        owner: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes an agent or skill repository and its owned child file repositories.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/platform/hub/repos/{owner}/{repo}/directories", owner=owner, repo=repo),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def commit(
        self,
        repo: str,
        *,
        owner: str,
        files: Dict[str, object] | Omit = omit,
        parent_commit: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DirectoryCommitResponse:
        """
        Creates a new directory commit for an agent or skill repository by applying
        file/link create, update, and delete operations.

        Args:
          files: Files maps path to an Entry (object = create/update/link, null = delete/unlink).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._post(
            path_template("/v1/platform/hub/repos/{owner}/{repo}/directories/commits", owner=owner, repo=repo),
            body=await async_maybe_transform(
                {
                    "files": files,
                    "parent_commit": parent_commit,
                },
                directory_commit_params.DirectoryCommitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DirectoryCommitResponse,
        )


class DirectoriesResourceWithRawResponse:
    def __init__(self, directories: DirectoriesResource) -> None:
        self._directories = directories

        self.list = to_raw_response_wrapper(
            directories.list,
        )
        self.delete = to_raw_response_wrapper(
            directories.delete,
        )
        self.commit = to_raw_response_wrapper(
            directories.commit,
        )


class AsyncDirectoriesResourceWithRawResponse:
    def __init__(self, directories: AsyncDirectoriesResource) -> None:
        self._directories = directories

        self.list = async_to_raw_response_wrapper(
            directories.list,
        )
        self.delete = async_to_raw_response_wrapper(
            directories.delete,
        )
        self.commit = async_to_raw_response_wrapper(
            directories.commit,
        )


class DirectoriesResourceWithStreamingResponse:
    def __init__(self, directories: DirectoriesResource) -> None:
        self._directories = directories

        self.list = to_streamed_response_wrapper(
            directories.list,
        )
        self.delete = to_streamed_response_wrapper(
            directories.delete,
        )
        self.commit = to_streamed_response_wrapper(
            directories.commit,
        )


class AsyncDirectoriesResourceWithStreamingResponse:
    def __init__(self, directories: AsyncDirectoriesResource) -> None:
        self._directories = directories

        self.list = async_to_streamed_response_wrapper(
            directories.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            directories.delete,
        )
        self.commit = async_to_streamed_response_wrapper(
            directories.commit,
        )
