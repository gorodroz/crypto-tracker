.PHONY: rum install lint test clean

run:
    python3 crypto_tracker/main.py

install:
    pip install -r requirements.txt

lint:
    ruff crypto_tracker

test:
    pytest tests

clean:
    rm -rf __pycache__ .pytest_cache *.log *.csv