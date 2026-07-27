#!/usr/bin/env python3
"""Gộp `changelog/*.json` thành `changelog.json` ở root.

Nguồn sự thật là **thư mục `changelog/`** — mỗi bản phát hành một file, dễ
review và không đụng nhau khi hai người sửa hai bản khác nhau. File
`changelog.json` ở root là **bản build**, tồn tại chỉ vì web đọc thẳng qua
`raw.githubusercontent` lúc chạy: raw không liệt kê được nội dung thư mục, mà
liệt kê bằng GitHub API thì dính giới hạn 60 request/giờ cho khách ẩn danh.

Chạy sau mỗi lần sửa `changelog/`, commit kèm bản build:

    python3 scripts/build_changelog.py

`--check` chỉ so, không ghi (CI dùng): khác nhau → thoát mã 1.

Thứ tự: mới→cũ theo `date`, cùng ngày thì `seq` lớn hơn đứng trước (`seq` mặc
định 0). `seq` là chuyện xếp thứ tự nội bộ nên **bị loại khỏi bản build** —
schema web thấy đúng như `docs`/AGENTS.md mô tả.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = ROOT / 'changelog'
OUT = ROOT / 'changelog.json'

KINDS = {'new', 'improve', 'fix'}


def fail(path: Path, msg: str) -> None:
    print(f'{path.relative_to(ROOT)}: {msg}', file=sys.stderr)
    sys.exit(1)


def load_release(path: Path) -> dict:
    """Đọc một file bản phát hành + kiểm những chỗ làm hỏng trang web."""
    try:
        rel = json.loads(path.read_text(encoding='utf-8'))
    except json.JSONDecodeError as e:
        fail(path, f'JSON hỏng: {e}')
    if not isinstance(rel, dict):
        fail(path, 'phải là một object JSON')
    if not isinstance(rel.get('date'), str):
        fail(path, 'thiếu "date" (chuỗi ISO yyyy-mm-dd)')
    if not isinstance(rel.get('title'), dict):
        fail(path, 'thiếu "title"')
    for key in ('title', 'note'):
        val = rel.get(key)
        if key in rel and not (isinstance(val, dict) and isinstance(val.get('en'), str)):
            fail(path, f'"{key}" thiếu bản tiếng Anh ("en")')
    entries = rel.get('entries')
    if not isinstance(entries, list) or not entries:
        fail(path, '"entries" phải có ít nhất 1 mục')
    for e in entries:
        if not isinstance(e, dict):
            fail(path, 'mỗi mục trong "entries" phải là object JSON')
        if e.get('kind') not in KINDS:
            fail(path, f'"kind" phải là một trong {sorted(KINDS)}, gặp {e.get("kind")!r}')
        if not isinstance(e.get('text'), dict) or not isinstance(e['text'].get('en'), str):
            fail(path, '"text" của mục thiếu bản tiếng Anh ("en")')
    return rel


def build() -> list[dict]:
    if not SRC_DIR.is_dir():
        print(f'không thấy thư mục {SRC_DIR}', file=sys.stderr)
        sys.exit(1)
    releases = []
    for path in sorted(SRC_DIR.glob('*.json')):
        rel = load_release(path)
        seq = rel.pop('seq', 0)
        releases.append((rel['date'], seq, rel))
    if not releases:
        print(f'{SRC_DIR} rỗng', file=sys.stderr)
        sys.exit(1)
    releases.sort(key=lambda r: (r[0], r[1]), reverse=True)
    return [rel for _, _, rel in releases]


def dump(releases: list[dict]) -> str:
    return json.dumps(releases, ensure_ascii=False, indent=2) + '\n'


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--check', action='store_true',
                    help='chỉ so changelog.json với bản build, không ghi')
    args = ap.parse_args()

    releases = build()
    text = dump(releases)
    if args.check:
        current = OUT.read_text(encoding='utf-8') if OUT.exists() else ''
        if current != text:
            print('changelog.json lệch với thư mục changelog/.\n'
                  'Chạy: python3 scripts/build_changelog.py rồi commit lại.',
                  file=sys.stderr)
            sys.exit(1)
        print('changelog.json khớp thư mục changelog/.')
        return

    OUT.write_text(text, encoding='utf-8')
    print(f'ghi {OUT.relative_to(ROOT)} — {len(releases)} bản phát hành.')


if __name__ == '__main__':
    main()
