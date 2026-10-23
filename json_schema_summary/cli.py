from argparse import ArgumentParser
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Arguments:
    json_path: Path
    key: str | None = None


def parse_arguments() -> Arguments:
    parser = ArgumentParser(description="Analyze the structure of a JSON file.")
    parser.add_argument("json_path", type=Path, help="Path to the JSON file")
    parser.add_argument("key", nargs="?", help="Optional key to analyze")
    args = parser.parse_args()
    return Arguments(args.json_path, args.key)
