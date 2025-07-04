from typing import TypeVar, Generic, List, Optional, Union, Dict, Any, Literal, overload
from typing_extensions import Self
from pydantic import BaseModel
import inspect
from dataclasses import dataclass

T = TypeVar('T', bound=BaseModel)

class FieldFilter(Generic[T]):

    def __init__(self, model_class: type[T]):
        self._model_class = model_class
        self._field_names = set(model_class.model_fields.keys())

    def __getattr__(self, name: str) -> :


