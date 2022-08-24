import pytest
from app import app, models

def test_answer():
    assert inc(4) == 5