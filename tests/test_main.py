import sys
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from unittest.mock import patch

from json_schema_summary.main import main


def test_main_analyzes_the_contacts_json_correctly():
    fake_path = Path("tests/fake")
    json_path = fake_path / "contacts.json"
    expected_result = (fake_path / "contacts-schema.txt").read_text()
    output = StringIO()
    args = ["main.py", str(json_path), "contacts"]
    with (
        patch.object(sys, "argv", args),
        redirect_stdout(output),
    ):
        main()
    assert output.getvalue() == expected_result
