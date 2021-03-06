import datetime

DEFAULT_KEY_PREFIX = "cwlfastapi-test"


def prefixed_key(f):
    """
    A method decorator that prefixes return values.
    Prefixes any string that the decorated method `f` returns with the value of
    the `prefix` attribute on the owner object `self`.
    """

    def prefixed_method(self, *args, **kwargs):
        key = f(self, *args, **kwargs)
        return f"{self.prefix}:{key}"

    return prefixed_method


class KeySchema:
    """
    Methods to generate key names for Redis data structures.
    These key names are used by the DAO classes. This class therefore contains
    a reference to all possible key names used by this application.
    """

    def __init__(self, prefix: str = DEFAULT_KEY_PREFIX):
        self.prefix = prefix

    @prefixed_key
    def site_hash_key(self, site_id: int) -> str:
        """
        sites:info:[site_id]
        Redis type: hash
        """
        return f"sites:info:{site_id}"

    @prefixed_key
    def workflows_key(self) -> str:
        """
        Redis type: sorted set
        """
        return f"workflows"
    
    @prefixed_key
    def workflow_key(self, workflow_id: int) -> str:
        """
        workflows:[wf_id]
        Redis type: json
        """
        return f"workflows:{workflow_id}"

    @prefixed_key
    def capacity_ranking_key(self):
        """
        sites:capacity:ranking
        Redis type: sorted set
        """
        return "sites:capacity:ranking"

    # @prefixed_key
    # def day_metric_key(self, site_id: int, unit: MetricUnit,
    #                    time: datetime.datetime) -> str:
    #     """
    #     metric:[unit-name]:[year-month-day]:[site_id]
    #     Redis type: sorted set
    #     """
    #     return f"metric:{unit.value}:{time.strftime('%Y-%m-%d')}:{site_id}"

    @prefixed_key
    def global_feed_key(self) -> str:
        """
        sites:feed
        Redis type: stream
        """
        return "sites:feed"

    @prefixed_key
    def feed_key(self, site_id: int) -> str:
        """
        sites:feed:[site_id]
        Redis type: stream
        """
        return f"sites:feed:{site_id}"
