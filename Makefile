test-unit:
	uv run --frozen pytest --cov=package_name/ test/unit --cov-report=html --cov-report=term --cov-report=xml --junitxml=junit.xml -o junit_family=legacy

test-functional:
	uv run --frozen pytest test/functional

test-integration:
	uv run --frozen pytest test/integration

.PHONY: test
test:
	uv run --frozen pytest -s test/

doctest:
	uv run --frozen pytest package_name/ docs/ --doctest-modules

test-all:
	uv run --frozen pytest package_name/ docs/ test/ --doctest-modules

.PHONY: docs
docs:
	uv run sphinx-build -M html docs/ docs/_build/

autodocs:
	uv run sphinx-autobuild docs/ docs/_build/

mypy:
	uv run mypy package_name/ --check-untyped-defs

pylint:
	uv run pylint package_name/

black:
	uv run black package_name/ test/  --line-length=79

black-check:
	uv run black package_name/ --line-length=79 --check

lint: black-check mypy pylint

lock:
	uv lock
	uv sync --no-editable
	uv export --frozen --format=requirements-txt --no-emit-project --output-file=docs/requirements.txt
