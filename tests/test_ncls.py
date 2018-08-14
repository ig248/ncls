
from ncls import NCLS
import pandas as pd

def test_ncls():
    starts = pd.Series(range(0, 5))
    ends = starts + 100
    ids = starts

    ncls = NCLS(starts.values, ends.values, ids.values)

    it = ncls.find_overlap(0, 2)

    assert next(it) == (0, 100, 0)


def test_next_nonoverlapping():

    starts = pd.Series(range(0, 5))
    ends = starts + 100
    ids = starts

    ncls = NCLS(starts.values, ends.values, ids.values)

    result = ncls.find_k_next_nonoverlapping(0, 2, 2)

    print(result)

    assert 0
