from pydantic import BaseModel


class JobDefinition(BaseModel):
    cwl_document: dict
    inputs_object: dict
