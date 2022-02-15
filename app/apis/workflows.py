from __future__ import annotations
import encodings
import hashlib
from urllib.parse import urljoin, urlsplit
from fastapi import Request
from encodings import utf_8

import requests

from typing import Any, List, Optional, Tuple

from app.types.workflow import WorkflowFactory
from schema_salad.fetcher import Fetcher
from schema_salad.utils import CacheType, FetcherCallableType, yaml_no_ts

from cwltool.context import LoadingContext
from cwltool.process import Process
from cwltool.workflow import default_make_tool
from cwltool.load_tool import load_tool as cwl_load_tool

from app.core import config

workflow_factory = WorkflowFactory()
yaml = yaml_no_ts()


def get_workflows_ids() -> list[str]:
    return workflow_factory.get_workflows()

def get_workflow_by_name(name: str) -> Any:
    return workflow_factory.get_workflow_by_name(name)

def get_raw_loading_context(data: bytes) -> None:
    return LoadingContext(
        {
            "construct_tool_object": default_make_tool,
            "resolver": lambda d, a: a,
            "fetcher_constructor": get_cwl_bytes_fetcher_callable(data)
        }
    )

async def post_workflow_from_body(name: str, request: Request) -> Tuple[str, Process]:
    raw_body = await request.body()
    process = cwl_load_tool(request.url_for("workflow_by_name", wf_name=name), get_raw_loading_context(raw_body))
    return workflow_factory.save_workflow(process)

def get_cwl_bytes_fetcher_callable(data: bytes) -> FetcherCallableType:
    def wrapper(cache: CacheType, session: Optional[requests.sessions.Session]) -> CWLBytesFetcher:
        return CWLBytesFetcher(cache, session, data)
    return wrapper

def get_md5_checksum_from_bytes(data: bytes) -> str:
    md5_hash = hashlib.md5()
    md5_hash.update(data)
    return md5_hash.hexdigest()

class CWLBytesFetcher(Fetcher):
    def __init__(
        self,
        cache: CacheType,
        session: Optional[requests.sessions.Session],
        cwl: bytes
    ) -> None:
        super().__init__(cache, session)
        self.cwl_bytes = cwl

    def fetch_text(self, url: str, content_types: Optional[List[str]] = None) -> str:
        cwl_data = yaml.load(self.cwl_bytes)
        return utf_8.decode(self.cwl_bytes)[0]

    def check_exists(self, url):  # type: (str) -> bool
        return self.client.exists(url)

    def urljoin(self, base: str, url: str) -> str:
        urlsp = urlsplit(url)
        if urlsp.scheme:
            return url
        basesp = urlsplit(base)

        if basesp.scheme == "keep":
            return base + "/" + url
        return urljoin(base, url)