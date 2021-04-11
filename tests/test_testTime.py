import pytest
from testTime import EpochTime

def test_EpochTime():
    newtime = EpochTime(t=1605679892756, unit='milliseconds_since_epoch', divide_by=1000)
    assert isinstance(newtime, EpochTime)
