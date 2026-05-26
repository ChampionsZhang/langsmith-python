# Sessions

Types:

```python
from langsmith_api.types import (
    CustomChartsSection,
    CustomChartsSectionRequest,
    RunStatsGroupBy,
    SessionSortableColumns,
    TimedeltaInput,
    TracerSession,
    TracerSessionWithoutVirtualFields,
)
```

Methods:

- <code title="post /api/v1/sessions">client.sessions.<a href="./src/langsmith_api/resources/sessions/sessions.py">create</a>(\*\*<a href="src/langsmith_api/types/session_create_params.py">params</a>) -> <a href="./src/langsmith_api/types/tracer_session_without_virtual_fields.py">TracerSessionWithoutVirtualFields</a></code>
- <code title="get /api/v1/sessions/{session_id}">client.sessions.<a href="./src/langsmith_api/resources/sessions/sessions.py">retrieve</a>(session_id, \*\*<a href="src/langsmith_api/types/session_retrieve_params.py">params</a>) -> <a href="./src/langsmith_api/types/tracer_session.py">TracerSession</a></code>
- <code title="patch /api/v1/sessions/{session_id}">client.sessions.<a href="./src/langsmith_api/resources/sessions/sessions.py">update</a>(session_id, \*\*<a href="src/langsmith_api/types/session_update_params.py">params</a>) -> <a href="./src/langsmith_api/types/tracer_session_without_virtual_fields.py">TracerSessionWithoutVirtualFields</a></code>
- <code title="get /api/v1/sessions">client.sessions.<a href="./src/langsmith_api/resources/sessions/sessions.py">list</a>(\*\*<a href="src/langsmith_api/types/session_list_params.py">params</a>) -> <a href="./src/langsmith_api/types/tracer_session.py">SyncOffsetPaginationTopLevelArray[TracerSession]</a></code>
- <code title="delete /api/v1/sessions/{session_id}">client.sessions.<a href="./src/langsmith_api/resources/sessions/sessions.py">delete</a>(session_id) -> object</code>
- <code title="post /api/v1/sessions/{session_id}/dashboard">client.sessions.<a href="./src/langsmith_api/resources/sessions/sessions.py">dashboard</a>(session_id, \*\*<a href="src/langsmith_api/types/session_dashboard_params.py">params</a>) -> <a href="./src/langsmith_api/types/custom_charts_section.py">CustomChartsSection</a></code>

## Insights

Types:

```python
from langsmith_api.types.sessions import (
    CreateRunClusteringJobRequest,
    InsightCreateResponse,
    InsightUpdateResponse,
    InsightListResponse,
    InsightDeleteResponse,
    InsightRetrieveJobResponse,
    InsightRetrieveRunsResponse,
)
```

Methods:

- <code title="post /api/v1/sessions/{session_id}/insights">client.sessions.insights.<a href="./src/langsmith_api/resources/sessions/insights.py">create</a>(session_id, \*\*<a href="src/langsmith_api/types/sessions/insight_create_params.py">params</a>) -> <a href="./src/langsmith_api/types/sessions/insight_create_response.py">InsightCreateResponse</a></code>
- <code title="patch /api/v1/sessions/{session_id}/insights/{job_id}">client.sessions.insights.<a href="./src/langsmith_api/resources/sessions/insights.py">update</a>(job_id, \*, session_id, \*\*<a href="src/langsmith_api/types/sessions/insight_update_params.py">params</a>) -> <a href="./src/langsmith_api/types/sessions/insight_update_response.py">InsightUpdateResponse</a></code>
- <code title="get /api/v1/sessions/{session_id}/insights">client.sessions.insights.<a href="./src/langsmith_api/resources/sessions/insights.py">list</a>(session_id, \*\*<a href="src/langsmith_api/types/sessions/insight_list_params.py">params</a>) -> <a href="./src/langsmith_api/types/sessions/insight_list_response.py">SyncOffsetPaginationInsightsClusteringJobs[InsightListResponse]</a></code>
- <code title="delete /api/v1/sessions/{session_id}/insights/{job_id}">client.sessions.insights.<a href="./src/langsmith_api/resources/sessions/insights.py">delete</a>(job_id, \*, session_id) -> <a href="./src/langsmith_api/types/sessions/insight_delete_response.py">InsightDeleteResponse</a></code>
- <code title="get /api/v1/sessions/{session_id}/insights/{job_id}">client.sessions.insights.<a href="./src/langsmith_api/resources/sessions/insights.py">retrieve_job</a>(job_id, \*, session_id) -> <a href="./src/langsmith_api/types/sessions/insight_retrieve_job_response.py">InsightRetrieveJobResponse</a></code>
- <code title="get /api/v1/sessions/{session_id}/insights/{job_id}/runs">client.sessions.insights.<a href="./src/langsmith_api/resources/sessions/insights.py">retrieve_runs</a>(job_id, \*, session_id, \*\*<a href="src/langsmith_api/types/sessions/insight_retrieve_runs_params.py">params</a>) -> <a href="./src/langsmith_api/types/sessions/insight_retrieve_runs_response.py">InsightRetrieveRunsResponse</a></code>

# Examples

Types:

```python
from langsmith_api.types import (
    AttachmentsOperations,
    Example,
    ExampleSelect,
    ExampleRetrieveCountResponse,
    ExampleUploadFromCsvResponse,
)
```

Methods:

- <code title="post /api/v1/examples">client.examples.<a href="./src/langsmith_api/resources/examples/examples.py">create</a>(\*\*<a href="src/langsmith_api/types/example_create_params.py">params</a>) -> <a href="./src/langsmith_api/types/example.py">Example</a></code>
- <code title="get /api/v1/examples/{example_id}">client.examples.<a href="./src/langsmith_api/resources/examples/examples.py">retrieve</a>(example_id, \*\*<a href="src/langsmith_api/types/example_retrieve_params.py">params</a>) -> <a href="./src/langsmith_api/types/example.py">Example</a></code>
- <code title="patch /api/v1/examples/{example_id}">client.examples.<a href="./src/langsmith_api/resources/examples/examples.py">update</a>(example_id, \*\*<a href="src/langsmith_api/types/example_update_params.py">params</a>) -> object</code>
- <code title="get /api/v1/examples">client.examples.<a href="./src/langsmith_api/resources/examples/examples.py">list</a>(\*\*<a href="src/langsmith_api/types/example_list_params.py">params</a>) -> <a href="./src/langsmith_api/types/example.py">SyncOffsetPaginationTopLevelArray[Example]</a></code>
- <code title="delete /api/v1/examples/{example_id}">client.examples.<a href="./src/langsmith_api/resources/examples/examples.py">delete</a>(example_id) -> object</code>
- <code title="delete /api/v1/examples">client.examples.<a href="./src/langsmith_api/resources/examples/examples.py">delete_all</a>(\*\*<a href="src/langsmith_api/types/example_delete_all_params.py">params</a>) -> object</code>
- <code title="get /api/v1/examples/count">client.examples.<a href="./src/langsmith_api/resources/examples/examples.py">retrieve_count</a>(\*\*<a href="src/langsmith_api/types/example_retrieve_count_params.py">params</a>) -> <a href="./src/langsmith_api/types/example_retrieve_count_response.py">ExampleRetrieveCountResponse</a></code>
- <code title="post /api/v1/examples/upload/{dataset_id}">client.examples.<a href="./src/langsmith_api/resources/examples/examples.py">upload_from_csv</a>(dataset_id, \*\*<a href="src/langsmith_api/types/example_upload_from_csv_params.py">params</a>) -> <a href="./src/langsmith_api/types/example_upload_from_csv_response.py">ExampleUploadFromCsvResponse</a></code>

## Bulk

Types:

```python
from langsmith_api.types.examples import BulkCreateResponse
```

Methods:

- <code title="post /api/v1/examples/bulk">client.examples.bulk.<a href="./src/langsmith_api/resources/examples/bulk.py">create</a>(\*\*<a href="src/langsmith_api/types/examples/bulk_create_params.py">params</a>) -> <a href="./src/langsmith_api/types/examples/bulk_create_response.py">BulkCreateResponse</a></code>
- <code title="patch /api/v1/examples/bulk">client.examples.bulk.<a href="./src/langsmith_api/resources/examples/bulk.py">patch_all</a>(\*\*<a href="src/langsmith_api/types/examples/bulk_patch_all_params.py">params</a>) -> object</code>

## Validate

Types:

```python
from langsmith_api.types.examples import ExampleValidationResult, ValidateBulkResponse
```

Methods:

- <code title="post /api/v1/examples/validate">client.examples.validate.<a href="./src/langsmith_api/resources/examples/validate.py">create</a>() -> <a href="./src/langsmith_api/types/examples/example_validation_result.py">ExampleValidationResult</a></code>
- <code title="post /api/v1/examples/validate/bulk">client.examples.validate.<a href="./src/langsmith_api/resources/examples/validate.py">bulk</a>() -> <a href="./src/langsmith_api/types/examples/validate_bulk_response.py">ValidateBulkResponse</a></code>

# Datasets

Types:

```python
from langsmith_api.types import (
    DataType,
    Dataset,
    DatasetTransformation,
    DatasetVersion,
    FeedbackCreateCoreSchema,
    Missing,
    SortByDatasetColumn,
    DatasetUpdateResponse,
    DatasetCloneResponse,
)
```

Methods:

- <code title="post /api/v1/datasets">client.datasets.<a href="./src/langsmith_api/resources/datasets/datasets.py">create</a>(\*\*<a href="src/langsmith_api/types/dataset_create_params.py">params</a>) -> <a href="./src/langsmith_api/types/dataset.py">Dataset</a></code>
- <code title="get /api/v1/datasets/{dataset_id}">client.datasets.<a href="./src/langsmith_api/resources/datasets/datasets.py">retrieve</a>(dataset_id) -> <a href="./src/langsmith_api/types/dataset.py">Dataset</a></code>
- <code title="patch /api/v1/datasets/{dataset_id}">client.datasets.<a href="./src/langsmith_api/resources/datasets/datasets.py">update</a>(dataset_id, \*\*<a href="src/langsmith_api/types/dataset_update_params.py">params</a>) -> <a href="./src/langsmith_api/types/dataset_update_response.py">DatasetUpdateResponse</a></code>
- <code title="get /api/v1/datasets">client.datasets.<a href="./src/langsmith_api/resources/datasets/datasets.py">list</a>(\*\*<a href="src/langsmith_api/types/dataset_list_params.py">params</a>) -> <a href="./src/langsmith_api/types/dataset.py">SyncOffsetPaginationTopLevelArray[Dataset]</a></code>
- <code title="delete /api/v1/datasets/{dataset_id}">client.datasets.<a href="./src/langsmith_api/resources/datasets/datasets.py">delete</a>(dataset_id) -> object</code>
- <code title="post /api/v1/datasets/clone">client.datasets.<a href="./src/langsmith_api/resources/datasets/datasets.py">clone</a>(\*\*<a href="src/langsmith_api/types/dataset_clone_params.py">params</a>) -> <a href="./src/langsmith_api/types/dataset_clone_response.py">DatasetCloneResponse</a></code>
- <code title="get /api/v1/datasets/{dataset_id}/csv">client.datasets.<a href="./src/langsmith_api/resources/datasets/datasets.py">retrieve_csv</a>(dataset_id, \*\*<a href="src/langsmith_api/types/dataset_retrieve_csv_params.py">params</a>) -> object</code>
- <code title="get /api/v1/datasets/{dataset_id}/jsonl">client.datasets.<a href="./src/langsmith_api/resources/datasets/datasets.py">retrieve_jsonl</a>(dataset_id, \*\*<a href="src/langsmith_api/types/dataset_retrieve_jsonl_params.py">params</a>) -> object</code>
- <code title="get /api/v1/datasets/{dataset_id}/openai">client.datasets.<a href="./src/langsmith_api/resources/datasets/datasets.py">retrieve_openai</a>(dataset_id, \*\*<a href="src/langsmith_api/types/dataset_retrieve_openai_params.py">params</a>) -> object</code>
- <code title="get /api/v1/datasets/{dataset_id}/openai_ft">client.datasets.<a href="./src/langsmith_api/resources/datasets/datasets.py">retrieve_openai_ft</a>(dataset_id, \*\*<a href="src/langsmith_api/types/dataset_retrieve_openai_ft_params.py">params</a>) -> object</code>
- <code title="get /api/v1/datasets/{dataset_id}/version">client.datasets.<a href="./src/langsmith_api/resources/datasets/datasets.py">retrieve_version</a>(dataset_id, \*\*<a href="src/langsmith_api/types/dataset_retrieve_version_params.py">params</a>) -> <a href="./src/langsmith_api/types/dataset_version.py">DatasetVersion</a></code>
- <code title="put /api/v1/datasets/{dataset_id}/tags">client.datasets.<a href="./src/langsmith_api/resources/datasets/datasets.py">update_tags</a>(dataset_id, \*\*<a href="src/langsmith_api/types/dataset_update_tags_params.py">params</a>) -> <a href="./src/langsmith_api/types/dataset_version.py">DatasetVersion</a></code>
- <code title="post /api/v1/datasets/upload">client.datasets.<a href="./src/langsmith_api/resources/datasets/datasets.py">upload</a>(\*\*<a href="src/langsmith_api/types/dataset_upload_params.py">params</a>) -> <a href="./src/langsmith_api/types/dataset.py">Dataset</a></code>

## Versions

Types:

```python
from langsmith_api.types.datasets import VersionRetrieveDiffResponse
```

Methods:

- <code title="get /api/v1/datasets/{dataset_id}/versions">client.datasets.versions.<a href="./src/langsmith_api/resources/datasets/versions.py">list</a>(dataset_id, \*\*<a href="src/langsmith_api/types/datasets/version_list_params.py">params</a>) -> <a href="./src/langsmith_api/types/dataset_version.py">SyncOffsetPaginationTopLevelArray[DatasetVersion]</a></code>
- <code title="get /api/v1/datasets/{dataset_id}/versions/diff">client.datasets.versions.<a href="./src/langsmith_api/resources/datasets/versions.py">retrieve_diff</a>(dataset_id, \*\*<a href="src/langsmith_api/types/datasets/version_retrieve_diff_params.py">params</a>) -> <a href="./src/langsmith_api/types/datasets/version_retrieve_diff_response.py">VersionRetrieveDiffResponse</a></code>

## Runs

Types:

```python
from langsmith_api.types.datasets import (
    ExampleWithRunsCh,
    QueryExampleSchemaWithRuns,
    QueryFeedbackDelta,
    SessionFeedbackDelta,
    SortParamsForRunsComparisonView,
    RunCreateResponse,
)
```

Methods:

- <code title="post /api/v1/datasets/{dataset_id}/runs">client.datasets.runs.<a href="./src/langsmith_api/resources/datasets/runs.py">create</a>(dataset_id, \*\*<a href="src/langsmith_api/types/datasets/run_create_params.py">params</a>) -> <a href="./src/langsmith_api/types/datasets/run_create_response.py">Optional[RunCreateResponse]</a></code>
- <code title="post /api/v1/datasets/{dataset_id}/runs/delta">client.datasets.runs.<a href="./src/langsmith_api/resources/datasets/runs.py">delta</a>(dataset_id, \*\*<a href="src/langsmith_api/types/datasets/run_delta_params.py">params</a>) -> <a href="./src/langsmith_api/types/datasets/session_feedback_delta.py">SessionFeedbackDelta</a></code>

## Group

Types:

```python
from langsmith_api.types.datasets import GroupRunsResponse
```

Methods:

- <code title="post /api/v1/datasets/{dataset_id}/group/runs">client.datasets.group.<a href="./src/langsmith_api/resources/datasets/group.py">runs</a>(dataset_id, \*\*<a href="src/langsmith_api/types/datasets/group_runs_params.py">params</a>) -> <a href="./src/langsmith_api/types/datasets/group_runs_response.py">GroupRunsResponse</a></code>

## Experiments

Methods:

- <code title="post /api/v1/datasets/{dataset_id}/experiments/grouped">client.datasets.experiments.<a href="./src/langsmith_api/resources/datasets/experiments.py">grouped</a>(dataset_id, \*\*<a href="src/langsmith_api/types/datasets/experiment_grouped_params.py">params</a>) -> object</code>

## Share

Types:

```python
from langsmith_api.types.datasets import DatasetShareSchema
```

Methods:

- <code title="put /api/v1/datasets/{dataset_id}/share">client.datasets.share.<a href="./src/langsmith_api/resources/datasets/share.py">create</a>(dataset_id, \*\*<a href="src/langsmith_api/types/datasets/share_create_params.py">params</a>) -> <a href="./src/langsmith_api/types/datasets/dataset_share_schema.py">DatasetShareSchema</a></code>
- <code title="get /api/v1/datasets/{dataset_id}/share">client.datasets.share.<a href="./src/langsmith_api/resources/datasets/share.py">retrieve</a>(dataset_id) -> <a href="./src/langsmith_api/types/datasets/dataset_share_schema.py">Optional[DatasetShareSchema]</a></code>
- <code title="delete /api/v1/datasets/{dataset_id}/share">client.datasets.share.<a href="./src/langsmith_api/resources/datasets/share.py">delete_all</a>(dataset_id) -> object</code>

## Comparative

Types:

```python
from langsmith_api.types.datasets import (
    SimpleExperimentInfo,
    SortByComparativeExperimentColumn,
    ComparativeCreateResponse,
)
```

Methods:

- <code title="post /api/v1/datasets/comparative">client.datasets.comparative.<a href="./src/langsmith_api/resources/datasets/comparative.py">create</a>(\*\*<a href="src/langsmith_api/types/datasets/comparative_create_params.py">params</a>) -> <a href="./src/langsmith_api/types/datasets/comparative_create_response.py">ComparativeCreateResponse</a></code>
- <code title="delete /api/v1/datasets/comparative/{comparative_experiment_id}">client.datasets.comparative.<a href="./src/langsmith_api/resources/datasets/comparative.py">delete</a>(comparative_experiment_id) -> object</code>

## Splits

Types:

```python
from langsmith_api.types.datasets import SplitCreateResponse, SplitRetrieveResponse
```

Methods:

- <code title="put /api/v1/datasets/{dataset_id}/splits">client.datasets.splits.<a href="./src/langsmith_api/resources/datasets/splits.py">create</a>(dataset_id, \*\*<a href="src/langsmith_api/types/datasets/split_create_params.py">params</a>) -> <a href="./src/langsmith_api/types/datasets/split_create_response.py">SplitCreateResponse</a></code>
- <code title="get /api/v1/datasets/{dataset_id}/splits">client.datasets.splits.<a href="./src/langsmith_api/resources/datasets/splits.py">retrieve</a>(dataset_id, \*\*<a href="src/langsmith_api/types/datasets/split_retrieve_params.py">params</a>) -> <a href="./src/langsmith_api/types/datasets/split_retrieve_response.py">SplitRetrieveResponse</a></code>

## PlaygroundExperiment

Types:

```python
from langsmith_api.types.datasets import RunnableConfig, RunnerContextEnum
```

Methods:

- <code title="post /api/v1/datasets/playground_experiment/batch">client.datasets.playground_experiment.<a href="./src/langsmith_api/resources/datasets/playground_experiment.py">batch</a>(\*\*<a href="src/langsmith_api/types/datasets/playground_experiment_batch_params.py">params</a>) -> object</code>
- <code title="post /api/v1/datasets/playground_experiment/stream">client.datasets.playground_experiment.<a href="./src/langsmith_api/resources/datasets/playground_experiment.py">stream</a>(\*\*<a href="src/langsmith_api/types/datasets/playground_experiment_stream_params.py">params</a>) -> object</code>

# Runs

Types:

```python
from langsmith_api.types import (
    BodyParamsForRunSchema,
    RequestBodyForRunsGenerateQuery,
    ResponseBodyForRunsGenerateQuery,
    Run,
    RunSchema,
    RunStatsQueryParams,
    RunTypeEnum,
    RunsFilterDataSourceTypeEnum,
    RunCreateResponse,
    RunUpdateResponse,
    RunIngestBatchResponse,
    RunQueryResponse,
    RunStatsResponse,
)
```

Methods:

- <code title="post /runs">client.runs.<a href="./src/langsmith_api/resources/runs.py">create</a>(\*\*<a href="src/langsmith_api/types/run_create_params.py">params</a>) -> <a href="./src/langsmith_api/types/run_create_response.py">RunCreateResponse</a></code>
- <code title="get /api/v1/runs/{run_id}">client.runs.<a href="./src/langsmith_api/resources/runs.py">retrieve</a>(run_id, \*\*<a href="src/langsmith_api/types/run_retrieve_params.py">params</a>) -> <a href="./src/langsmith_api/types/run_schema.py">RunSchema</a></code>
- <code title="patch /runs/{run_id}">client.runs.<a href="./src/langsmith_api/resources/runs.py">update</a>(run_id, \*\*<a href="src/langsmith_api/types/run_update_params.py">params</a>) -> <a href="./src/langsmith_api/types/run_update_response.py">RunUpdateResponse</a></code>
- <code title="post /runs/batch">client.runs.<a href="./src/langsmith_api/resources/runs.py">ingest_batch</a>(\*\*<a href="src/langsmith_api/types/run_ingest_batch_params.py">params</a>) -> <a href="./src/langsmith_api/types/run_ingest_batch_response.py">RunIngestBatchResponse</a></code>
- <code title="post /api/v1/runs/query">client.runs.<a href="./src/langsmith_api/resources/runs.py">query</a>(\*\*<a href="src/langsmith_api/types/run_query_params.py">params</a>) -> <a href="./src/langsmith_api/types/run_query_response.py">RunQueryResponse</a></code>
- <code title="post /api/v1/runs/stats">client.runs.<a href="./src/langsmith_api/resources/runs.py">stats</a>(\*\*<a href="src/langsmith_api/types/run_stats_params.py">params</a>) -> <a href="./src/langsmith_api/types/run_stats_response.py">RunStatsResponse</a></code>
- <code title="patch /api/v1/runs/{run_id}">client.runs.<a href="./src/langsmith_api/resources/runs.py">update_2</a>(run_id) -> object</code>

# Evaluators

Types:

```python
from langsmith_api.types import (
    CodeEvaluatorTopLevel,
    Evaluator,
    EvaluatorPagerdutyAlert,
    EvaluatorTopLevel,
    EvaluatorWebhook,
    EvaluatorListResponse,
)
```

Methods:

- <code title="get /api/v1/runs/rules">client.evaluators.<a href="./src/langsmith_api/resources/evaluators.py">list</a>(\*\*<a href="src/langsmith_api/types/evaluator_list_params.py">params</a>) -> <a href="./src/langsmith_api/types/evaluator_list_response.py">EvaluatorListResponse</a></code>

# Feedback

Types:

```python
from langsmith_api.types import (
    APIFeedbackSource,
    AppFeedbackSource,
    AutoEvalFeedbackSource,
    FeedbackCreateSchema,
    FeedbackLevel,
    FeedbackSchema,
    ModelFeedbackSource,
    SourceType,
)
```

Methods:

- <code title="post /api/v1/feedback">client.feedback.<a href="./src/langsmith_api/resources/feedback/feedback.py">create</a>(\*\*<a href="src/langsmith_api/types/feedback_create_params.py">params</a>) -> <a href="./src/langsmith_api/types/feedback_schema.py">FeedbackSchema</a></code>
- <code title="get /api/v1/feedback/{feedback_id}">client.feedback.<a href="./src/langsmith_api/resources/feedback/feedback.py">retrieve</a>(feedback_id, \*\*<a href="src/langsmith_api/types/feedback_retrieve_params.py">params</a>) -> <a href="./src/langsmith_api/types/feedback_schema.py">FeedbackSchema</a></code>
- <code title="patch /api/v1/feedback/{feedback_id}">client.feedback.<a href="./src/langsmith_api/resources/feedback/feedback.py">update</a>(feedback_id, \*\*<a href="src/langsmith_api/types/feedback_update_params.py">params</a>) -> <a href="./src/langsmith_api/types/feedback_schema.py">FeedbackSchema</a></code>
- <code title="get /api/v1/feedback">client.feedback.<a href="./src/langsmith_api/resources/feedback/feedback.py">list</a>(\*\*<a href="src/langsmith_api/types/feedback_list_params.py">params</a>) -> <a href="./src/langsmith_api/types/feedback_schema.py">SyncOffsetPaginationTopLevelArray[FeedbackSchema]</a></code>
- <code title="delete /api/v1/feedback/{feedback_id}">client.feedback.<a href="./src/langsmith_api/resources/feedback/feedback.py">delete</a>(feedback_id) -> object</code>

## Tokens

Types:

```python
from langsmith_api.types.feedback import (
    FeedbackIngestTokenCreateSchema,
    FeedbackIngestTokenSchema,
    TokenCreateResponse,
    TokenListResponse,
)
```

Methods:

- <code title="post /api/v1/feedback/tokens">client.feedback.tokens.<a href="./src/langsmith_api/resources/feedback/tokens.py">create</a>(\*\*<a href="src/langsmith_api/types/feedback/token_create_params.py">params</a>) -> <a href="./src/langsmith_api/types/feedback/token_create_response.py">TokenCreateResponse</a></code>
- <code title="get /api/v1/feedback/tokens/{token}">client.feedback.tokens.<a href="./src/langsmith_api/resources/feedback/tokens.py">retrieve</a>(token, \*\*<a href="src/langsmith_api/types/feedback/token_retrieve_params.py">params</a>) -> object</code>
- <code title="post /api/v1/feedback/tokens/{token}">client.feedback.tokens.<a href="./src/langsmith_api/resources/feedback/tokens.py">update</a>(token, \*\*<a href="src/langsmith_api/types/feedback/token_update_params.py">params</a>) -> object</code>
- <code title="get /api/v1/feedback/tokens">client.feedback.tokens.<a href="./src/langsmith_api/resources/feedback/tokens.py">list</a>(\*\*<a href="src/langsmith_api/types/feedback/token_list_params.py">params</a>) -> <a href="./src/langsmith_api/types/feedback/token_list_response.py">TokenListResponse</a></code>

## Configs

Methods:

- <code title="delete /api/v1/feedback-configs">client.feedback.configs.<a href="./src/langsmith_api/resources/feedback/configs.py">delete</a>(\*\*<a href="src/langsmith_api/types/feedback/config_delete_params.py">params</a>) -> None</code>

# Public

Methods:

- <code title="get /api/v1/public/{share_token}/feedbacks">client.public.<a href="./src/langsmith_api/resources/public/public.py">retrieve_feedbacks</a>(share_token, \*\*<a href="src/langsmith_api/types/public_retrieve_feedbacks_params.py">params</a>) -> <a href="./src/langsmith_api/types/feedback_schema.py">SyncOffsetPaginationTopLevelArray[FeedbackSchema]</a></code>

## Datasets

Types:

```python
from langsmith_api.types.public import (
    DatasetListResponse,
    DatasetListComparativeResponse,
    DatasetRetrieveSessionsBulkResponse,
)
```

Methods:

- <code title="get /api/v1/public/{share_token}/datasets">client.public.datasets.<a href="./src/langsmith_api/resources/public/datasets.py">list</a>(share_token, \*\*<a href="src/langsmith_api/types/public/dataset_list_params.py">params</a>) -> <a href="./src/langsmith_api/types/public/dataset_list_response.py">DatasetListResponse</a></code>
- <code title="get /api/v1/public/{share_token}/datasets/comparative">client.public.datasets.<a href="./src/langsmith_api/resources/public/datasets.py">list_comparative</a>(share_token, \*\*<a href="src/langsmith_api/types/public/dataset_list_comparative_params.py">params</a>) -> <a href="./src/langsmith_api/types/public/dataset_list_comparative_response.py">SyncOffsetPaginationTopLevelArray[DatasetListComparativeResponse]</a></code>
- <code title="get /api/v1/public/{share_token}/datasets/feedback">client.public.datasets.<a href="./src/langsmith_api/resources/public/datasets.py">list_feedback</a>(share_token, \*\*<a href="src/langsmith_api/types/public/dataset_list_feedback_params.py">params</a>) -> <a href="./src/langsmith_api/types/feedback_schema.py">SyncOffsetPaginationTopLevelArray[FeedbackSchema]</a></code>
- <code title="get /api/v1/public/{share_token}/datasets/sessions">client.public.datasets.<a href="./src/langsmith_api/resources/public/datasets.py">list_sessions</a>(share_token, \*\*<a href="src/langsmith_api/types/public/dataset_list_sessions_params.py">params</a>) -> <a href="./src/langsmith_api/types/tracer_session.py">SyncOffsetPaginationTopLevelArray[TracerSession]</a></code>
- <code title="get /api/v1/public/datasets/sessions-bulk">client.public.datasets.<a href="./src/langsmith_api/resources/public/datasets.py">retrieve_sessions_bulk</a>(\*\*<a href="src/langsmith_api/types/public/dataset_retrieve_sessions_bulk_params.py">params</a>) -> <a href="./src/langsmith_api/types/public/dataset_retrieve_sessions_bulk_response.py">DatasetRetrieveSessionsBulkResponse</a></code>

# AnnotationQueues

Types:

```python
from langsmith_api.types import (
    AnnotationQueueRubricItemSchema,
    AnnotationQueueSchema,
    AnnotationQueueSizeSchema,
    RunSchemaWithAnnotationQueueInfo,
    AnnotationQueueRetrieveResponse,
    AnnotationQueueRetrieveAnnotationQueuesResponse,
    AnnotationQueueRetrieveQueuesResponse,
)
```

Methods:

- <code title="get /api/v1/annotation-queues/{queue_id}">client.annotation_queues.<a href="./src/langsmith_api/resources/annotation_queues/annotation_queues.py">retrieve</a>(queue_id) -> <a href="./src/langsmith_api/types/annotation_queue_retrieve_response.py">AnnotationQueueRetrieveResponse</a></code>
- <code title="patch /api/v1/annotation-queues/{queue_id}">client.annotation_queues.<a href="./src/langsmith_api/resources/annotation_queues/annotation_queues.py">update</a>(queue_id, \*\*<a href="src/langsmith_api/types/annotation_queue_update_params.py">params</a>) -> object</code>
- <code title="delete /api/v1/annotation-queues/{queue_id}">client.annotation_queues.<a href="./src/langsmith_api/resources/annotation_queues/annotation_queues.py">delete</a>(queue_id) -> object</code>
- <code title="post /api/v1/annotation-queues">client.annotation_queues.<a href="./src/langsmith_api/resources/annotation_queues/annotation_queues.py">annotation_queues</a>(\*\*<a href="src/langsmith_api/types/annotation_queue_annotation_queues_params.py">params</a>) -> <a href="./src/langsmith_api/types/annotation_queue_schema.py">AnnotationQueueSchema</a></code>
- <code title="post /api/v1/annotation-queues/status/{annotation_queue_run_id}">client.annotation_queues.<a href="./src/langsmith_api/resources/annotation_queues/annotation_queues.py">create_run_status</a>(annotation_queue_run_id, \*\*<a href="src/langsmith_api/types/annotation_queue_create_run_status_params.py">params</a>) -> object</code>
- <code title="post /api/v1/annotation-queues/{queue_id}/export">client.annotation_queues.<a href="./src/langsmith_api/resources/annotation_queues/annotation_queues.py">export</a>(queue_id, \*\*<a href="src/langsmith_api/types/annotation_queue_export_params.py">params</a>) -> object</code>
- <code title="post /api/v1/annotation-queues/populate">client.annotation_queues.<a href="./src/langsmith_api/resources/annotation_queues/annotation_queues.py">populate</a>(\*\*<a href="src/langsmith_api/types/annotation_queue_populate_params.py">params</a>) -> object</code>
- <code title="get /api/v1/annotation-queues">client.annotation_queues.<a href="./src/langsmith_api/resources/annotation_queues/annotation_queues.py">retrieve_annotation_queues</a>(\*\*<a href="src/langsmith_api/types/annotation_queue_retrieve_annotation_queues_params.py">params</a>) -> <a href="./src/langsmith_api/types/annotation_queue_retrieve_annotation_queues_response.py">SyncOffsetPaginationTopLevelArray[AnnotationQueueRetrieveAnnotationQueuesResponse]</a></code>
- <code title="get /api/v1/annotation-queues/{run_id}/queues">client.annotation_queues.<a href="./src/langsmith_api/resources/annotation_queues/annotation_queues.py">retrieve_queues</a>(run_id) -> <a href="./src/langsmith_api/types/annotation_queue_retrieve_queues_response.py">AnnotationQueueRetrieveQueuesResponse</a></code>
- <code title="get /api/v1/annotation-queues/{queue_id}/run/{index}">client.annotation_queues.<a href="./src/langsmith_api/resources/annotation_queues/annotation_queues.py">retrieve_run</a>(index, \*, queue_id, \*\*<a href="src/langsmith_api/types/annotation_queue_retrieve_run_params.py">params</a>) -> <a href="./src/langsmith_api/types/run_schema_with_annotation_queue_info.py">RunSchemaWithAnnotationQueueInfo</a></code>
- <code title="get /api/v1/annotation-queues/{queue_id}/size">client.annotation_queues.<a href="./src/langsmith_api/resources/annotation_queues/annotation_queues.py">retrieve_size</a>(queue_id, \*\*<a href="src/langsmith_api/types/annotation_queue_retrieve_size_params.py">params</a>) -> <a href="./src/langsmith_api/types/annotation_queue_size_schema.py">AnnotationQueueSizeSchema</a></code>
- <code title="get /api/v1/annotation-queues/{queue_id}/total_archived">client.annotation_queues.<a href="./src/langsmith_api/resources/annotation_queues/annotation_queues.py">retrieve_total_archived</a>(queue_id, \*\*<a href="src/langsmith_api/types/annotation_queue_retrieve_total_archived_params.py">params</a>) -> <a href="./src/langsmith_api/types/annotation_queue_size_schema.py">AnnotationQueueSizeSchema</a></code>
- <code title="get /api/v1/annotation-queues/{queue_id}/total_size">client.annotation_queues.<a href="./src/langsmith_api/resources/annotation_queues/annotation_queues.py">retrieve_total_size</a>(queue_id) -> <a href="./src/langsmith_api/types/annotation_queue_size_schema.py">AnnotationQueueSizeSchema</a></code>

## Runs

Types:

```python
from langsmith_api.types.annotation_queues import RunCreateResponse, RunListResponse
```

Methods:

- <code title="post /api/v1/annotation-queues/{queue_id}/runs">client.annotation_queues.runs.<a href="./src/langsmith_api/resources/annotation_queues/runs.py">create</a>(queue_id, \*\*<a href="src/langsmith_api/types/annotation_queues/run_create_params.py">params</a>) -> <a href="./src/langsmith_api/types/annotation_queues/run_create_response.py">RunCreateResponse</a></code>
- <code title="patch /api/v1/annotation-queues/{queue_id}/runs/{queue_run_id}">client.annotation_queues.runs.<a href="./src/langsmith_api/resources/annotation_queues/runs.py">update</a>(queue_run_id, \*, queue_id, \*\*<a href="src/langsmith_api/types/annotation_queues/run_update_params.py">params</a>) -> object</code>
- <code title="get /api/v1/annotation-queues/{queue_id}/runs">client.annotation_queues.runs.<a href="./src/langsmith_api/resources/annotation_queues/runs.py">list</a>(queue_id, \*\*<a href="src/langsmith_api/types/annotation_queues/run_list_params.py">params</a>) -> <a href="./src/langsmith_api/types/annotation_queues/run_list_response.py">RunListResponse</a></code>
- <code title="post /api/v1/annotation-queues/{queue_id}/runs/delete">client.annotation_queues.runs.<a href="./src/langsmith_api/resources/annotation_queues/runs.py">delete_all</a>(queue_id, \*\*<a href="src/langsmith_api/types/annotation_queues/run_delete_all_params.py">params</a>) -> object</code>
- <code title="delete /api/v1/annotation-queues/{queue_id}/runs/{queue_run_id}">client.annotation_queues.runs.<a href="./src/langsmith_api/resources/annotation_queues/runs.py">delete_queue</a>(queue_run_id, \*, queue_id) -> object</code>

# Info

Types:

```python
from langsmith_api.types import InfoListResponse
```

Methods:

- <code title="get /api/v1/info">client.info.<a href="./src/langsmith_api/resources/info.py">list</a>() -> <a href="./src/langsmith_api/types/info_list_response.py">InfoListResponse</a></code>

# Workspaces

Types:

```python
from langsmith_api.types import (
    WorkspaceCreateResponse,
    WorkspaceUpdateResponse,
    WorkspaceListResponse,
)
```

Methods:

- <code title="post /api/v1/workspaces">client.workspaces.<a href="./src/langsmith_api/resources/workspaces.py">create</a>(\*\*<a href="src/langsmith_api/types/workspace_create_params.py">params</a>) -> <a href="./src/langsmith_api/types/workspace_create_response.py">WorkspaceCreateResponse</a></code>
- <code title="patch /api/v1/workspaces/{workspace_id}">client.workspaces.<a href="./src/langsmith_api/resources/workspaces.py">update</a>(workspace_id, \*\*<a href="src/langsmith_api/types/workspace_update_params.py">params</a>) -> <a href="./src/langsmith_api/types/workspace_update_response.py">WorkspaceUpdateResponse</a></code>
- <code title="get /api/v1/workspaces">client.workspaces.<a href="./src/langsmith_api/resources/workspaces.py">list</a>(\*\*<a href="src/langsmith_api/types/workspace_list_params.py">params</a>) -> <a href="./src/langsmith_api/types/workspace_list_response.py">WorkspaceListResponse</a></code>
- <code title="delete /api/v1/workspaces/{workspace_id}">client.workspaces.<a href="./src/langsmith_api/resources/workspaces.py">delete</a>(workspace_id) -> object</code>

# Repos

Types:

```python
from langsmith_api.types import (
    CreateRepoResponse,
    DemoConfig,
    EPromptOptimizationAlgorithm,
    GetRepoResponse,
    PromptimConfig,
    RepoWithLookups,
)
```

Methods:

- <code title="post /api/v1/repos">client.repos.<a href="./src/langsmith_api/resources/repos/repos.py">create</a>(\*\*<a href="src/langsmith_api/types/repo_create_params.py">params</a>) -> <a href="./src/langsmith_api/types/create_repo_response.py">CreateRepoResponse</a></code>
- <code title="get /api/v1/repos/{owner}/{repo}">client.repos.<a href="./src/langsmith_api/resources/repos/repos.py">retrieve</a>(repo, \*, owner) -> <a href="./src/langsmith_api/types/get_repo_response.py">GetRepoResponse</a></code>
- <code title="patch /api/v1/repos/{owner}/{repo}">client.repos.<a href="./src/langsmith_api/resources/repos/repos.py">update</a>(repo, \*, owner, \*\*<a href="src/langsmith_api/types/repo_update_params.py">params</a>) -> <a href="./src/langsmith_api/types/create_repo_response.py">CreateRepoResponse</a></code>
- <code title="get /api/v1/repos">client.repos.<a href="./src/langsmith_api/resources/repos/repos.py">list</a>(\*\*<a href="src/langsmith_api/types/repo_list_params.py">params</a>) -> <a href="./src/langsmith_api/types/repo_with_lookups.py">SyncOffsetPaginationRepos[RepoWithLookups]</a></code>
- <code title="delete /api/v1/repos/{owner}/{repo}">client.repos.<a href="./src/langsmith_api/resources/repos/repos.py">delete</a>(repo, \*, owner) -> object</code>

## Directories

Types:

```python
from langsmith_api.types.repos import DirectoryListResponse, DirectoryCommitResponse
```

Methods:

- <code title="get /v1/platform/hub/repos/{owner}/{repo}/directories">client.repos.directories.<a href="./src/langsmith_api/resources/repos/directories.py">list</a>(repo, \*, owner, \*\*<a href="src/langsmith_api/types/repos/directory_list_params.py">params</a>) -> <a href="./src/langsmith_api/types/repos/directory_list_response.py">DirectoryListResponse</a></code>
- <code title="delete /v1/platform/hub/repos/{owner}/{repo}/directories">client.repos.directories.<a href="./src/langsmith_api/resources/repos/directories.py">delete</a>(repo, \*, owner) -> None</code>
- <code title="post /v1/platform/hub/repos/{owner}/{repo}/directories/commits">client.repos.directories.<a href="./src/langsmith_api/resources/repos/directories.py">commit</a>(repo, \*, owner, \*\*<a href="src/langsmith_api/types/repos/directory_commit_params.py">params</a>) -> <a href="./src/langsmith_api/types/repos/directory_commit_response.py">DirectoryCommitResponse</a></code>

# Commits

Types:

```python
from langsmith_api.types import (
    CommitManifestResponse,
    CommitWithLookups,
    CommitCreateResponse,
    CommitRetrieveResponse,
)
```

Methods:

- <code title="post /commits/{owner}/{repo}">client.commits.<a href="./src/langsmith_api/resources/commits.py">create</a>(repo, \*, owner, \*\*<a href="src/langsmith_api/types/commit_create_params.py">params</a>) -> <a href="./src/langsmith_api/types/commit_create_response.py">CommitCreateResponse</a></code>
- <code title="get /commits/{owner}/{repo}/{commit}">client.commits.<a href="./src/langsmith_api/resources/commits.py">retrieve</a>(commit, \*, owner, repo, \*\*<a href="src/langsmith_api/types/commit_retrieve_params.py">params</a>) -> <a href="./src/langsmith_api/types/commit_retrieve_response.py">CommitRetrieveResponse</a></code>
- <code title="get /commits/{owner}/{repo}">client.commits.<a href="./src/langsmith_api/resources/commits.py">list</a>(repo, \*, owner, \*\*<a href="src/langsmith_api/types/commit_list_params.py">params</a>) -> <a href="./src/langsmith_api/types/commit_with_lookups.py">SyncOffsetPaginationCommits[CommitWithLookups]</a></code>

# Settings

Types:

```python
from langsmith_api.types import AppHubCrudTenantsTenant
```

Methods:

- <code title="get /api/v1/settings">client.settings.<a href="./src/langsmith_api/resources/settings.py">list</a>() -> <a href="./src/langsmith_api/types/app_hub_crud_tenants_tenant.py">AppHubCrudTenantsTenant</a></code>

# Sandboxes

## Boxes

Types:

```python
from langsmith_api.types.sandboxes import (
    BoxCreateResponse,
    BoxRetrieveResponse,
    BoxUpdateResponse,
    BoxListResponse,
    BoxCreateSnapshotResponse,
    BoxGenerateServiceURLResponse,
    BoxGetStatusResponse,
    BoxStartResponse,
)
```

Methods:

- <code title="post /v2/sandboxes/boxes">client.sandboxes.boxes.<a href="./src/langsmith_api/resources/sandboxes/boxes.py">create</a>(\*\*<a href="src/langsmith_api/types/sandboxes/box_create_params.py">params</a>) -> <a href="./src/langsmith_api/types/sandboxes/box_create_response.py">BoxCreateResponse</a></code>
- <code title="get /v2/sandboxes/boxes/{name}">client.sandboxes.boxes.<a href="./src/langsmith_api/resources/sandboxes/boxes.py">retrieve</a>(name) -> <a href="./src/langsmith_api/types/sandboxes/box_retrieve_response.py">BoxRetrieveResponse</a></code>
- <code title="patch /v2/sandboxes/boxes/{name}">client.sandboxes.boxes.<a href="./src/langsmith_api/resources/sandboxes/boxes.py">update</a>(path_name, \*\*<a href="src/langsmith_api/types/sandboxes/box_update_params.py">params</a>) -> <a href="./src/langsmith_api/types/sandboxes/box_update_response.py">BoxUpdateResponse</a></code>
- <code title="get /v2/sandboxes/boxes">client.sandboxes.boxes.<a href="./src/langsmith_api/resources/sandboxes/boxes.py">list</a>(\*\*<a href="src/langsmith_api/types/sandboxes/box_list_params.py">params</a>) -> <a href="./src/langsmith_api/types/sandboxes/box_list_response.py">BoxListResponse</a></code>
- <code title="delete /v2/sandboxes/boxes/{name}">client.sandboxes.boxes.<a href="./src/langsmith_api/resources/sandboxes/boxes.py">delete</a>(name) -> None</code>
- <code title="post /v2/sandboxes/boxes/{name}/snapshot">client.sandboxes.boxes.<a href="./src/langsmith_api/resources/sandboxes/boxes.py">create_snapshot</a>(path_name, \*\*<a href="src/langsmith_api/types/sandboxes/box_create_snapshot_params.py">params</a>) -> <a href="./src/langsmith_api/types/sandboxes/box_create_snapshot_response.py">BoxCreateSnapshotResponse</a></code>
- <code title="post /v2/sandboxes/boxes/{name}/service-url">client.sandboxes.boxes.<a href="./src/langsmith_api/resources/sandboxes/boxes.py">generate_service_url</a>(name, \*\*<a href="src/langsmith_api/types/sandboxes/box_generate_service_url_params.py">params</a>) -> <a href="./src/langsmith_api/types/sandboxes/box_generate_service_url_response.py">BoxGenerateServiceURLResponse</a></code>
- <code title="get /v2/sandboxes/boxes/{name}/status">client.sandboxes.boxes.<a href="./src/langsmith_api/resources/sandboxes/boxes.py">get_status</a>(name) -> <a href="./src/langsmith_api/types/sandboxes/box_get_status_response.py">BoxGetStatusResponse</a></code>
- <code title="post /v2/sandboxes/boxes/{name}/start">client.sandboxes.boxes.<a href="./src/langsmith_api/resources/sandboxes/boxes.py">start</a>(name) -> <a href="./src/langsmith_api/types/sandboxes/box_start_response.py">BoxStartResponse</a></code>
- <code title="post /v2/sandboxes/boxes/{name}/stop">client.sandboxes.boxes.<a href="./src/langsmith_api/resources/sandboxes/boxes.py">stop</a>(name) -> None</code>

## Snapshots

Types:

```python
from langsmith_api.types.sandboxes import (
    SnapshotCreateResponse,
    SnapshotRetrieveResponse,
    SnapshotListResponse,
)
```

Methods:

- <code title="post /v2/sandboxes/snapshots">client.sandboxes.snapshots.<a href="./src/langsmith_api/resources/sandboxes/snapshots.py">create</a>(\*\*<a href="src/langsmith_api/types/sandboxes/snapshot_create_params.py">params</a>) -> <a href="./src/langsmith_api/types/sandboxes/snapshot_create_response.py">SnapshotCreateResponse</a></code>
- <code title="get /v2/sandboxes/snapshots/{snapshot_id}">client.sandboxes.snapshots.<a href="./src/langsmith_api/resources/sandboxes/snapshots.py">retrieve</a>(snapshot_id) -> <a href="./src/langsmith_api/types/sandboxes/snapshot_retrieve_response.py">SnapshotRetrieveResponse</a></code>
- <code title="get /v2/sandboxes/snapshots">client.sandboxes.snapshots.<a href="./src/langsmith_api/resources/sandboxes/snapshots.py">list</a>(\*\*<a href="src/langsmith_api/types/sandboxes/snapshot_list_params.py">params</a>) -> <a href="./src/langsmith_api/types/sandboxes/snapshot_list_response.py">SnapshotListResponse</a></code>
- <code title="delete /v2/sandboxes/snapshots/{snapshot_id}">client.sandboxes.snapshots.<a href="./src/langsmith_api/resources/sandboxes/snapshots.py">delete</a>(snapshot_id) -> None</code>
