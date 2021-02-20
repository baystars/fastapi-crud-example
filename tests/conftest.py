# -*- mode: python -*- -*- coding: utf-8 -*-
import json
import os

from fastapi.testclient import TestClient
import pytest

from app import config
from app.main import app

@pytest.fixture(scope='session', autouse=True)
def cmdopt(request):
    set_environment()

@pytest.fixture(scope='session', autouse=True)
def judge():
    data = {
        'section': os.getenv('TEST_SECTION'),
        'id': os.getenv('TEST_JUDGE_ID'),
        'team': os.getenv('TEST_JUDGE_TEAM'),
        'token': os.getenv('TEST_JUDGE_TOKEN'),
        'entry': os.getenv('TEST_JUDGE_ENTRY')
   }
    return data

def set_environment(filename='env.json'):
    env_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), filename)
    with open(env_file) as f:
        for key, value in json.load(f).items():
            os.environ[key] = value

@pytest.fixture(scope='module')
def test_app():
    client = TestClient(app)
    yield client  # testing happens here
