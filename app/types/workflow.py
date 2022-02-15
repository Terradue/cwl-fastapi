import json
from typing import Any, List, Optional, Tuple
from urllib.parse import urljoin, urlsplit

import redis
import requests
from cwltool.process import Process
from cwltool.workflow import Workflow
from cwltool.context import LoadingContext
from cwltool.workflow import default_make_tool
from cwltool.load_tool import load_tool as cwl_load_tool
from ruamel import yaml
from schema_salad.fetcher import Fetcher
from schema_salad.utils import CacheType, yaml_no_ts

from app.core.connections import get_redis_connection

yaml = yaml_no_ts()

class WorkflowFactory:
    """Workflow factory

    Factory for loading all registered workflows in the app.

    """

    loading_context: LoadingContext

    def __init__(self) -> None:
        self.loading_context = LoadingContext(
            {
                "construct_tool_object": default_make_tool,
                "resolver": self.cwl_resolver,
                "fetcher_constructor": CWLRedisFetcher,
            }
        )

    def cwl_resolver(d: Any, a: str) -> str:
        return a

    def get_workflows(self) -> list[str]:
        return None

    def get_workflow_by_name(self, name: str) -> Process:
        return cwl_load_tool(name, self.loading_context)

    def save_workflow(self, process: Process) -> Tuple[str, Process]:
        client = get_redis_connection()
        wf_id = self.get_workflow_id(process)
        return (wf_id, process)

    def get_workflow_id(self, process: Process) -> str:
        if isinstance(process, Workflow):
            return process.tool["id"]
        return process.tool["id"]


class CWLRedisFetcher(Fetcher):
    def __init__(
        self,
        cache: CacheType,
        session: Optional[requests.sessions.Session],
    ) -> None:
        """Create a Fetcher that reads CWL from redis."""
        self.client: redis.Redis = get_redis_connection()

    def fetch_text(self, url: str, content_types: Optional[List[str]] = None) -> str:
        try:
            json_wf = json.load(self.client.json().get(url))
            yaml.dump(json_wf)
        except Exception as e:
            raise RuntimeError("Workflow id %s cannot be fetched" % url)

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
