import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

from get_config import get_environment
from robot import run_cli

environment = get_environment()

if __name__ == "__main__":
    cli_args = [
        "--outputdir", str(PROJECT_ROOT / "results"),
        "--variable", f"ENV:{environment}",
        str(PROJECT_ROOT / "tests")
    ]

    run_cli(cli_args)