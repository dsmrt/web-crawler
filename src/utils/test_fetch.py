from fetch import fetch_url
import pytest

def test_fetch_url():
    assert isinstance(fetch_url("https://www.dsmrt.com"), str)

def test_fetch_bad_url():
    with pytest.raises(Exception):
        # setting wait to 0 because these are test and we want them to run fast.
        fetch_url(url="https://willnotresolve.dsmrt.com", max_retries=2, wait_seconds=0)
