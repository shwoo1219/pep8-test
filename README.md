# pep8-test

Demonstrates PEP8 enforcement via GitHub Actions CI using flake8.

## How it works

- **`.flake8`** — configures flake8 with Google-style 80-char line length
- **`.github/workflows/lint.yml`** — runs flake8 on every push and pull request

## Branches

| Branch | Code | CI result |
|--------|------|-----------|
| `main` | `src/good_code.py` only | green |
| `test/bad-code` | adds `src/bad_code.py` | red (intentional violations) |

## Running locally

```sh
pip install flake8
flake8 .
```
