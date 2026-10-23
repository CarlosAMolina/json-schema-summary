import json
from copy import deepcopy
from enum import StrEnum
from pathlib import Path

from json_schema_summary.cli import Arguments


class _Types(StrEnum):
    FLOAT = "float"
    INT = "int"
    LIST = "list"
    STR = "str"


type _Schema = dict[str, _Types]


def analyze_json_schema(args: Arguments) -> str:
    content = _read_json(args.json_path)
    schema = _build_schema(content, args.key)
    return _summaryze(schema)


def _read_json(json_path: Path) -> dict:
    return json.loads(json_path.read_text())


def _build_schema(content: dict, key: str | None) -> _Schema:
    content = deepcopy(content)
    if key:
        content = content[key]
    type_ = _get_type(content)
    if type_ == _Types.LIST:
        content = content[0]  # TODO analyze all items, not only the first one
        # TODO if different types for same key, summaryze all types
    return _build_schema_of_dict(content)


def _build_schema_of_dict(content: dict) -> _Schema:
    result = {}
    for key, value in content.items():
        if key not in result:
            type_ = _get_type(value)
            result[key] = type_
    return result


def _get_type(value: object) -> _Types:
    if isinstance(value, float):
        return _Types.FLOAT
    if isinstance(value, int):
        return _Types.INT
    if isinstance(value, list):
        return _Types.LIST
    if isinstance(value, str):
        return _Types.STR
    raise ValueError(value)


def _summaryze(schema: _Schema) -> str:
    rows = [f"{name}: {type_}" for name, type_ in schema.items()]
    rows.sort()
    return "\n".join(rows)
