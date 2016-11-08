#!/usr/bin/env bash
set -e 

. ~/. flask_env/bin/activate

PYTHONPATH=. py.test --junitxml=python_tests.xml
PYTHONPATH=. py.test --cov-report xml --cov=../
PYTHONPATH=. py.test --cov-report html --cov=../
