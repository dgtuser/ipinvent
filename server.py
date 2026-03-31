from __future__ import annotations

import json
from pathlib import Path

PARTS = [
    "server.part1.txt",
    "server.part2.txt",
    "server.part3.txt",
    "server.part4.txt",
    "server.part5.txt",
    "server.part6.txt",
    "server.part7.txt",
]

APP_PARTS = [
    "/app.part1.txt",
    "/app.part2.txt",
    "/app.part3.txt",
    "/app.part4.txt",
    "/app.part5.txt",
    "/app.part6.txt",
]

BASE_DIR = Path(__file__).resolve().parent


def decode_chunk(path: Path) -> str:
    escaped = path.read_text(encoding="utf-8")
    return json.loads(f'"{escaped}"')


def main() -> None:
    namespace = {
        "__name__": "server_runtime",
        "__file__": str(Path(__file__).resolve()),
    }
    source = "".join(decode_chunk(BASE_DIR / name) for name in PARTS)
    exec(compile(source, str(BASE_DIR / "_server_runtime.py"), "exec"), namespace)

    static_files = namespace.get("STATIC_FILES")
    if isinstance(static_files, dict):
        for index in range(1, 7):
            static_files[f"/app.part{index}.txt"] = BASE_DIR / f"app.part{index}.txt"

    namespace["main"]()


if __name__ == "__main__":
    main()
