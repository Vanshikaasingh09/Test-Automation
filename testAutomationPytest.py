import pytest
import requests

testcases = [
    ("http://localhost:8000/add/2/2", 4, "Addition of 2 and 2"),
    ("http://localhost:8000/subtract/5/3", 2, "Subtraction of 3 from 5"),
    ("http://localhost:8000/multiply/2/3", 6, "Multiplication of 2 and 3"),
    ("http://localhost:8000/add/-1/1", 0, "Addition of -1 and 1"),
    ("http://localhost:8000/multiply/0/5", 0, "Multiplication by zero"),
]

@pytest.mark.parametrize("url, expected, description", testcases)
def test_api(url, expected, description):
    response = requests.get(url)
    result = response.json()["result"]
    assert result == expected, f"{description}. Expected {expected}, got {result}"
