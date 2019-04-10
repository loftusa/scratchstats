import random
from scratchstats import basics
import pytest


li_even = list(range(1, 11))
li_odd = list(range(1, 12))


class TestBasics(object):
    def test_mean(self):
        assert basics.mean(li_even) == 5.5

    def test_median(self):
        assert basics.median(li_even) == 5.5
        assert basics.median(li_odd) == 6.0
        assert type(basics.median(li_even)) == float
