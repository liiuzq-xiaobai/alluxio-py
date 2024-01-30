ALLUXIO_PAGE_SIZE_KEY = "alluxio.worker.page.store.page.size"
ALLUXIO_PAGE_SIZE_DEFAULT_VALUE = "1MB"
ALLUXIO_SUCCESS_IDENTIFIER = "success"
LIST_URL_FORMAT = "http://{worker_host}:{http_port}/v1/files"
FULL_PAGE_URL_FORMAT = (
    "http://{worker_host}:{http_port}/v1/file/{path_id}/page/{page_index}"
)
PAGE_URL_FORMAT = "http://{worker_host}:{http_port}/v1/file/{path_id}/page/{page_index}?offset={page_offset}&length={page_length}"
WRITE_PAGE_URL_FORMAT = (
    "http://{worker_host}:{http_port}/v1/file/{path_id}/page/{page_index}"
)
GET_FILE_STATUS_URL_FORMAT = "http://{worker_host}:{http_port}/v1/info"
LOAD_SUBMIT_URL_FORMAT = (
    "http://{worker_host}:{http_port}/v1/load?path={path}&opType=submit"
)
LOAD_PROGRESS_URL_FORMAT = (
    "http://{worker_host}:{http_port}/v1/load?path={path}&opType=progress"
)
LOAD_STOP_URL_FORMAT = (
    "http://{worker_host}:{http_port}/v1/load?path={path}&opType=stop"
)