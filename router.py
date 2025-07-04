import asyncio
from typing import Dict, List, Tuple, Optional, Callable, Any
from dataclasses import dataclass
import json

@dataclass
class Route:
    method: str
    path: str
    handler: Callable
    middleware: List[Callable] = None

    def __post_init__(self):
        if self.middleware is None:
            self.middleware = []


@dataclass
class Request:
    method: str
    path: str
    headers: Dict[str, str]
    body: bytes


class Response:
    def __init__(self, body: Any = "", status: int = 200, headers: Dict[str, str] = None) -> None:
        self.body = body
        self.status = status
        self.headers = headers or {}

    def json(self, data: Any):
        self.body = json.dumps(data)
        self.headers['Content-Type'] = 'application/json'
        return self


class SpeedyRouter:
    def __init__(self, app: Any) -> None:
        self.routes: List[Route] = []

    def add_route(self, method: str, path: str, handler: Callable, middleware: List[Callable]) -> None:
        self.routes.append(Route(method, path, handler, middleware))


        

