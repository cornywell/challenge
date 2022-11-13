import pandas as pd
from fastapi import HTTPException

from app.file_handler import get_sample

# TODO: WRITE TESTS FOR OTHER FILE HANDLER FUNCTIONS

def test_get_sample():
    column_values1 = ["a", "b", "b", "c", "d", "e", "f", "g"]
    sample1 = ["a", "b", "c", "d", "e"]
    column_values2 = [1, 2, 2, 3, 4, 5, 6, 7]
    sample2 = [1, 2, 3, 4, 5]
    column_values3 = ["yes","yes","no"]
    sample3 = ["yes", "no"]
    column_values4 = [0.1, 0.2, 0.3, 0.4, 0.4]
    sample4 = [0.1, 0.2, 0.3, 0.4]
    column_values5 = [200, 201, 203, 204, 205]
    sample5 = [200, 201, 203, 204, 205]

    assert get_sample(column_values1) == sample1
    assert get_sample(column_values2) == sample2
    assert get_sample(column_values3) == sample3
    assert get_sample(column_values4) == sample4
    assert get_sample(column_values5) == sample5
