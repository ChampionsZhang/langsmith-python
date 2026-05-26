# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from langsmith_api import Langsmith, AsyncLangsmith
from langsmith_api.types import (
    Dataset,
    DatasetVersion,
    DatasetCloneResponse,
    DatasetUpdateResponse,
)
from langsmith_api._utils import parse_datetime
from langsmith_api.pagination import SyncOffsetPaginationTopLevelArray, AsyncOffsetPaginationTopLevelArray

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDatasets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Langsmith) -> None:
        dataset = client.datasets.create(
            name="name",
        )
        assert_matches_type(Dataset, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Langsmith) -> None:
        dataset = client.datasets.create(
            name="name",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            data_type="kv",
            description="description",
            externally_managed=True,
            extra={"foo": "bar"},
            inputs_schema_definition={"foo": "bar"},
            outputs_schema_definition={"foo": "bar"},
            transformations=[
                {
                    "path": ["string"],
                    "transformation_type": "convert_to_openai_message",
                }
            ],
        )
        assert_matches_type(Dataset, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Langsmith) -> None:
        response = client.datasets.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(Dataset, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Langsmith) -> None:
        with client.datasets.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(Dataset, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Langsmith) -> None:
        dataset = client.datasets.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Dataset, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Langsmith) -> None:
        response = client.datasets.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(Dataset, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Langsmith) -> None:
        with client.datasets.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(Dataset, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.datasets.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Langsmith) -> None:
        dataset = client.datasets.update(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DatasetUpdateResponse, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Langsmith) -> None:
        dataset = client.datasets.update(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            baseline_experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="string",
            inputs_schema_definition={"foo": "bar"},
            metadata={"foo": "bar"},
            name="string",
            outputs_schema_definition={"foo": "bar"},
            patch_examples={
                "foo": {
                    "attachments_operations": {
                        "rename": {"foo": "string"},
                        "retain": ["string"],
                    },
                    "dataset_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "inputs": {"foo": "bar"},
                    "metadata": {"foo": "bar"},
                    "outputs": {"foo": "bar"},
                    "overwrite": True,
                    "split": ["string"],
                }
            },
            transformations=[
                {
                    "path": ["string"],
                    "transformation_type": "convert_to_openai_message",
                }
            ],
        )
        assert_matches_type(DatasetUpdateResponse, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Langsmith) -> None:
        response = client.datasets.with_raw_response.update(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(DatasetUpdateResponse, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Langsmith) -> None:
        with client.datasets.with_streaming_response.update(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(DatasetUpdateResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.datasets.with_raw_response.update(
                dataset_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Langsmith) -> None:
        dataset = client.datasets.list()
        assert_matches_type(SyncOffsetPaginationTopLevelArray[Dataset], dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Langsmith) -> None:
        dataset = client.datasets.list(
            id=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            datatype="kv",
            exclude=["example_count"],
            exclude_corrections_datasets=True,
            limit=1,
            metadata="metadata",
            name="name",
            name_contains="name_contains",
            offset=0,
            sort_by="name",
            sort_by_desc=True,
            tag_value_id=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(SyncOffsetPaginationTopLevelArray[Dataset], dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Langsmith) -> None:
        response = client.datasets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(SyncOffsetPaginationTopLevelArray[Dataset], dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Langsmith) -> None:
        with client.datasets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(SyncOffsetPaginationTopLevelArray[Dataset], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Langsmith) -> None:
        dataset = client.datasets.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Langsmith) -> None:
        response = client.datasets.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Langsmith) -> None:
        with client.datasets.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(object, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.datasets.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_clone(self, client: Langsmith) -> None:
        dataset = client.datasets.clone(
            source_dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DatasetCloneResponse, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_clone_with_all_params(self, client: Langsmith) -> None:
        dataset = client.datasets.clone(
            source_dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            as_of=parse_datetime("2019-12-27T18:11:19.117Z"),
            examples=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            split="string",
        )
        assert_matches_type(DatasetCloneResponse, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_clone(self, client: Langsmith) -> None:
        response = client.datasets.with_raw_response.clone(
            source_dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(DatasetCloneResponse, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_clone(self, client: Langsmith) -> None:
        with client.datasets.with_streaming_response.clone(
            source_dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(DatasetCloneResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_csv(self, client: Langsmith) -> None:
        dataset = client.datasets.retrieve_csv(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_csv_with_all_params(self, client: Langsmith) -> None:
        dataset = client.datasets.retrieve_csv(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            as_of=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_csv(self, client: Langsmith) -> None:
        response = client.datasets.with_raw_response.retrieve_csv(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_csv(self, client: Langsmith) -> None:
        with client.datasets.with_streaming_response.retrieve_csv(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(object, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_csv(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.datasets.with_raw_response.retrieve_csv(
                dataset_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_jsonl(self, client: Langsmith) -> None:
        dataset = client.datasets.retrieve_jsonl(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_jsonl_with_all_params(self, client: Langsmith) -> None:
        dataset = client.datasets.retrieve_jsonl(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            as_of=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_jsonl(self, client: Langsmith) -> None:
        response = client.datasets.with_raw_response.retrieve_jsonl(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_jsonl(self, client: Langsmith) -> None:
        with client.datasets.with_streaming_response.retrieve_jsonl(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(object, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_jsonl(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.datasets.with_raw_response.retrieve_jsonl(
                dataset_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_openai(self, client: Langsmith) -> None:
        dataset = client.datasets.retrieve_openai(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_openai_with_all_params(self, client: Langsmith) -> None:
        dataset = client.datasets.retrieve_openai(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            as_of=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_openai(self, client: Langsmith) -> None:
        response = client.datasets.with_raw_response.retrieve_openai(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_openai(self, client: Langsmith) -> None:
        with client.datasets.with_streaming_response.retrieve_openai(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(object, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_openai(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.datasets.with_raw_response.retrieve_openai(
                dataset_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_openai_ft(self, client: Langsmith) -> None:
        dataset = client.datasets.retrieve_openai_ft(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_openai_ft_with_all_params(self, client: Langsmith) -> None:
        dataset = client.datasets.retrieve_openai_ft(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            as_of=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_openai_ft(self, client: Langsmith) -> None:
        response = client.datasets.with_raw_response.retrieve_openai_ft(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_openai_ft(self, client: Langsmith) -> None:
        with client.datasets.with_streaming_response.retrieve_openai_ft(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(object, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_openai_ft(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.datasets.with_raw_response.retrieve_openai_ft(
                dataset_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_version(self, client: Langsmith) -> None:
        dataset = client.datasets.retrieve_version(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DatasetVersion, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_version_with_all_params(self, client: Langsmith) -> None:
        dataset = client.datasets.retrieve_version(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            as_of=parse_datetime("2019-12-27T18:11:19.117Z"),
            tag="tag",
        )
        assert_matches_type(DatasetVersion, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_version(self, client: Langsmith) -> None:
        response = client.datasets.with_raw_response.retrieve_version(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(DatasetVersion, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_version(self, client: Langsmith) -> None:
        with client.datasets.with_streaming_response.retrieve_version(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(DatasetVersion, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_version(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.datasets.with_raw_response.retrieve_version(
                dataset_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_tags(self, client: Langsmith) -> None:
        dataset = client.datasets.update_tags(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            as_of=parse_datetime("2019-12-27T18:11:19.117Z"),
            tag="tag",
        )
        assert_matches_type(DatasetVersion, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update_tags(self, client: Langsmith) -> None:
        response = client.datasets.with_raw_response.update_tags(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            as_of=parse_datetime("2019-12-27T18:11:19.117Z"),
            tag="tag",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(DatasetVersion, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update_tags(self, client: Langsmith) -> None:
        with client.datasets.with_streaming_response.update_tags(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            as_of=parse_datetime("2019-12-27T18:11:19.117Z"),
            tag="tag",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(DatasetVersion, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update_tags(self, client: Langsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            client.datasets.with_raw_response.update_tags(
                dataset_id="",
                as_of=parse_datetime("2019-12-27T18:11:19.117Z"),
                tag="tag",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upload(self, client: Langsmith) -> None:
        dataset = client.datasets.upload(
            file=b"Example data",
            input_keys=["string"],
        )
        assert_matches_type(Dataset, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upload_with_all_params(self, client: Langsmith) -> None:
        dataset = client.datasets.upload(
            file=b"Example data",
            input_keys=["string"],
            data_type="kv",
            description="description",
            input_key_mappings="input_key_mappings",
            inputs_schema_definition="inputs_schema_definition",
            metadata_key_mappings="metadata_key_mappings",
            metadata_keys=["string"],
            name="name",
            output_key_mappings="output_key_mappings",
            output_keys=["string"],
            outputs_schema_definition="outputs_schema_definition",
            transformations="transformations",
        )
        assert_matches_type(Dataset, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upload(self, client: Langsmith) -> None:
        response = client.datasets.with_raw_response.upload(
            file=b"Example data",
            input_keys=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = response.parse()
        assert_matches_type(Dataset, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upload(self, client: Langsmith) -> None:
        with client.datasets.with_streaming_response.upload(
            file=b"Example data",
            input_keys=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = response.parse()
            assert_matches_type(Dataset, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDatasets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncLangsmith) -> None:
        dataset = await async_client.datasets.create(
            name="name",
        )
        assert_matches_type(Dataset, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncLangsmith) -> None:
        dataset = await async_client.datasets.create(
            name="name",
            id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            created_at=parse_datetime("2019-12-27T18:11:19.117Z"),
            data_type="kv",
            description="description",
            externally_managed=True,
            extra={"foo": "bar"},
            inputs_schema_definition={"foo": "bar"},
            outputs_schema_definition={"foo": "bar"},
            transformations=[
                {
                    "path": ["string"],
                    "transformation_type": "convert_to_openai_message",
                }
            ],
        )
        assert_matches_type(Dataset, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.datasets.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(Dataset, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncLangsmith) -> None:
        async with async_client.datasets.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(Dataset, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncLangsmith) -> None:
        dataset = await async_client.datasets.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Dataset, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.datasets.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(Dataset, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncLangsmith) -> None:
        async with async_client.datasets.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(Dataset, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.datasets.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncLangsmith) -> None:
        dataset = await async_client.datasets.update(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DatasetUpdateResponse, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncLangsmith) -> None:
        dataset = await async_client.datasets.update(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            baseline_experiment_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            description="string",
            inputs_schema_definition={"foo": "bar"},
            metadata={"foo": "bar"},
            name="string",
            outputs_schema_definition={"foo": "bar"},
            patch_examples={
                "foo": {
                    "attachments_operations": {
                        "rename": {"foo": "string"},
                        "retain": ["string"],
                    },
                    "dataset_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    "inputs": {"foo": "bar"},
                    "metadata": {"foo": "bar"},
                    "outputs": {"foo": "bar"},
                    "overwrite": True,
                    "split": ["string"],
                }
            },
            transformations=[
                {
                    "path": ["string"],
                    "transformation_type": "convert_to_openai_message",
                }
            ],
        )
        assert_matches_type(DatasetUpdateResponse, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.datasets.with_raw_response.update(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(DatasetUpdateResponse, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncLangsmith) -> None:
        async with async_client.datasets.with_streaming_response.update(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(DatasetUpdateResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.datasets.with_raw_response.update(
                dataset_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncLangsmith) -> None:
        dataset = await async_client.datasets.list()
        assert_matches_type(AsyncOffsetPaginationTopLevelArray[Dataset], dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncLangsmith) -> None:
        dataset = await async_client.datasets.list(
            id=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            datatype="kv",
            exclude=["example_count"],
            exclude_corrections_datasets=True,
            limit=1,
            metadata="metadata",
            name="name",
            name_contains="name_contains",
            offset=0,
            sort_by="name",
            sort_by_desc=True,
            tag_value_id=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(AsyncOffsetPaginationTopLevelArray[Dataset], dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.datasets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(AsyncOffsetPaginationTopLevelArray[Dataset], dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncLangsmith) -> None:
        async with async_client.datasets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(AsyncOffsetPaginationTopLevelArray[Dataset], dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncLangsmith) -> None:
        dataset = await async_client.datasets.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.datasets.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncLangsmith) -> None:
        async with async_client.datasets.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(object, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.datasets.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_clone(self, async_client: AsyncLangsmith) -> None:
        dataset = await async_client.datasets.clone(
            source_dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DatasetCloneResponse, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_clone_with_all_params(self, async_client: AsyncLangsmith) -> None:
        dataset = await async_client.datasets.clone(
            source_dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            as_of=parse_datetime("2019-12-27T18:11:19.117Z"),
            examples=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            split="string",
        )
        assert_matches_type(DatasetCloneResponse, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_clone(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.datasets.with_raw_response.clone(
            source_dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(DatasetCloneResponse, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_clone(self, async_client: AsyncLangsmith) -> None:
        async with async_client.datasets.with_streaming_response.clone(
            source_dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            target_dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(DatasetCloneResponse, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_csv(self, async_client: AsyncLangsmith) -> None:
        dataset = await async_client.datasets.retrieve_csv(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_csv_with_all_params(self, async_client: AsyncLangsmith) -> None:
        dataset = await async_client.datasets.retrieve_csv(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            as_of=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_csv(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.datasets.with_raw_response.retrieve_csv(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_csv(self, async_client: AsyncLangsmith) -> None:
        async with async_client.datasets.with_streaming_response.retrieve_csv(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(object, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_csv(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.datasets.with_raw_response.retrieve_csv(
                dataset_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_jsonl(self, async_client: AsyncLangsmith) -> None:
        dataset = await async_client.datasets.retrieve_jsonl(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_jsonl_with_all_params(self, async_client: AsyncLangsmith) -> None:
        dataset = await async_client.datasets.retrieve_jsonl(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            as_of=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_jsonl(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.datasets.with_raw_response.retrieve_jsonl(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_jsonl(self, async_client: AsyncLangsmith) -> None:
        async with async_client.datasets.with_streaming_response.retrieve_jsonl(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(object, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_jsonl(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.datasets.with_raw_response.retrieve_jsonl(
                dataset_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_openai(self, async_client: AsyncLangsmith) -> None:
        dataset = await async_client.datasets.retrieve_openai(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_openai_with_all_params(self, async_client: AsyncLangsmith) -> None:
        dataset = await async_client.datasets.retrieve_openai(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            as_of=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_openai(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.datasets.with_raw_response.retrieve_openai(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_openai(self, async_client: AsyncLangsmith) -> None:
        async with async_client.datasets.with_streaming_response.retrieve_openai(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(object, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_openai(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.datasets.with_raw_response.retrieve_openai(
                dataset_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_openai_ft(self, async_client: AsyncLangsmith) -> None:
        dataset = await async_client.datasets.retrieve_openai_ft(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_openai_ft_with_all_params(self, async_client: AsyncLangsmith) -> None:
        dataset = await async_client.datasets.retrieve_openai_ft(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            as_of=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_openai_ft(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.datasets.with_raw_response.retrieve_openai_ft(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(object, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_openai_ft(self, async_client: AsyncLangsmith) -> None:
        async with async_client.datasets.with_streaming_response.retrieve_openai_ft(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(object, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_openai_ft(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.datasets.with_raw_response.retrieve_openai_ft(
                dataset_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_version(self, async_client: AsyncLangsmith) -> None:
        dataset = await async_client.datasets.retrieve_version(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(DatasetVersion, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_version_with_all_params(self, async_client: AsyncLangsmith) -> None:
        dataset = await async_client.datasets.retrieve_version(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            as_of=parse_datetime("2019-12-27T18:11:19.117Z"),
            tag="tag",
        )
        assert_matches_type(DatasetVersion, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_version(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.datasets.with_raw_response.retrieve_version(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(DatasetVersion, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_version(self, async_client: AsyncLangsmith) -> None:
        async with async_client.datasets.with_streaming_response.retrieve_version(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(DatasetVersion, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_version(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.datasets.with_raw_response.retrieve_version(
                dataset_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_tags(self, async_client: AsyncLangsmith) -> None:
        dataset = await async_client.datasets.update_tags(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            as_of=parse_datetime("2019-12-27T18:11:19.117Z"),
            tag="tag",
        )
        assert_matches_type(DatasetVersion, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update_tags(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.datasets.with_raw_response.update_tags(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            as_of=parse_datetime("2019-12-27T18:11:19.117Z"),
            tag="tag",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(DatasetVersion, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update_tags(self, async_client: AsyncLangsmith) -> None:
        async with async_client.datasets.with_streaming_response.update_tags(
            dataset_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            as_of=parse_datetime("2019-12-27T18:11:19.117Z"),
            tag="tag",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(DatasetVersion, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update_tags(self, async_client: AsyncLangsmith) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `dataset_id` but received ''"):
            await async_client.datasets.with_raw_response.update_tags(
                dataset_id="",
                as_of=parse_datetime("2019-12-27T18:11:19.117Z"),
                tag="tag",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upload(self, async_client: AsyncLangsmith) -> None:
        dataset = await async_client.datasets.upload(
            file=b"Example data",
            input_keys=["string"],
        )
        assert_matches_type(Dataset, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upload_with_all_params(self, async_client: AsyncLangsmith) -> None:
        dataset = await async_client.datasets.upload(
            file=b"Example data",
            input_keys=["string"],
            data_type="kv",
            description="description",
            input_key_mappings="input_key_mappings",
            inputs_schema_definition="inputs_schema_definition",
            metadata_key_mappings="metadata_key_mappings",
            metadata_keys=["string"],
            name="name",
            output_key_mappings="output_key_mappings",
            output_keys=["string"],
            outputs_schema_definition="outputs_schema_definition",
            transformations="transformations",
        )
        assert_matches_type(Dataset, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncLangsmith) -> None:
        response = await async_client.datasets.with_raw_response.upload(
            file=b"Example data",
            input_keys=["string"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        dataset = await response.parse()
        assert_matches_type(Dataset, dataset, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncLangsmith) -> None:
        async with async_client.datasets.with_streaming_response.upload(
            file=b"Example data",
            input_keys=["string"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            dataset = await response.parse()
            assert_matches_type(Dataset, dataset, path=["response"])

        assert cast(Any, response.is_closed) is True
