import json
from typing import Set
from app.redis.base import RedisBase
from cwltool.process import Process


class WorkflowRedis(RedisBase):
    """WorkflowRedis persists workflows to Redis.
    This class allows persisting (and querying for) Workflows in Redis.
    """
    def insert(self, workflow_id: str, process: Process, **kwargs):
        """Insert a Site into Redis."""
        workflow_id_key = self.key_schema.workflow_key(workflow_id)
        workflows_id_key = self.key_schema.workflows_key()
        client = kwargs.get('pipeline', self.redis)
        client.json().set(workflow_id_key, json.dumps(process))
        client.sadd(workflows_id_key, workflow_id_key)

    def find_by_id(self, site_id: int, **kwargs) -> Process:
        """Find a Site by ID in Redis."""
        hash_key = self.key_schema.site_hash_key(site_id)
        process_json = self.redis.json().get(hash_key)

        if not process_json:
            raise WorkflowNotFound()

        return json.load(process_json)

    def find_all(self, **kwargs) -> Set[Process]:
        """Find all Sites in Redis."""
        # START Challenge #1
        # Remove this line when you've written code to build `site_hashes`.
        site_hashes = []  # type: ignore
        # END Challenge #1

        return {FlatSiteSchema().load(site_hash) for site_hash in site_hashes}