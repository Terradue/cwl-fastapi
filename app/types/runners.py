import abc
import argparse
import importlib
import sys
from typing import IO, Any, Callable, List, Optional, Union

import cwltool
from cwltool.argparser import arg_parser
from cwltool.context import LoadingContext, RuntimeContext
from cwltool.executors import JobExecutor
from cwltool.main import main as cwlmain
from pydantic import BaseModel

from app.core.config import Configuration


class RunnerDefinition(BaseModel):
    name: str
    module: str


class RunnerFactory:
    """Runner factory

    Factory for loading all available runners in the app.

    """

    def get_runners(self) -> list[RunnerDefinition]:
        cfg = Configuration.load()
        return [RunnerDefinition.parse_obj(r) for r in cfg.runners]

    def get_runner_by_name(self, name: str) -> RunnerDefinition:
        return next(r for r in self.get_runners() if r.name == name)

    def load_runner_by_name(self, name: str) -> Any:
        """Load runner by name

        Loads a runner by name and returns it.

        Args:
            name (str): Name of the runner to load

        Returns:
            Any: Loaded runner

        """
        runner = self.get_runner_by_name(name)
        module = importlib.import_module(runner.module)
        return module.init_runner()


class Runner(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, "load_data_source")
            and callable(subclass.load_data_source)
            and hasattr(subclass, "extract_text")
            and callable(subclass.extract_text)
            or NotImplemented
        )

    @abc.abstractmethod
    def get_arguments(self, path: str, file_name: str) -> dict:
        """Get the arguments supported by the runner"""
        raise NotImplementedError

    # @abc.abstractmethod
    # def run(
    #     args: Optional[argparse.Namespace] = None,
    #     job_order_object: Optional[CWLObjectType] = None,
    #     custom_schema_callback: Optional[Callable[[], None]] = None,
    #     executor: Optional[JobExecutor] = None,
    #     loadingContext: Optional[LoadingContext] = None,
    #     runtimeContext: Optional[RuntimeContext] = None,
    # ) -> int:
    #     """Extract text from the data set"""
    #     try:
    #         result = cwlmain(
    #             args=parsed_args,
    #             executor=executor,
    #             loadingContext=CalrissianLoadingContext(),
    #             runtimeContext=runtime_context,
    #         )
    #     finally:
    #         # Always clean up after cwlmain
    #         delete_pods()
    #         if parsed_args.usage_report:
    #             write_report(parsed_args.usage_report)
    #         flush_tees()

    #     return result
