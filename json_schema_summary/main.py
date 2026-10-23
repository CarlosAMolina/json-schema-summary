from json_schema_summary.analyzer import analyze_json_schema
from json_schema_summary.cli import parse_arguments


def main() -> None:
    args = parse_arguments()
    if not args.json_path.is_file():
        raise FileNotFoundError(args.json_path)
    schema = analyze_json_schema(args)
    print(schema)


if __name__ == "__main__":
    main()
