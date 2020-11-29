import pprint
import math
import sys


def generate():
    """
    Generates a dict of midi note codes with their corresponding
        frequency ranges.
    """

    base = [7.946362749, 8.1757989155, 8.4188780665]
    # 12th root of 2
    multiplier = 1.05946309436

    notes = {0: base}
    for i in range(1, 127):
        mid = multiplier * notes[i - 1][1]
        low = (mid + notes[i - 1][1]) / 2.0
        high = (mid + (multiplier * mid)) / 2.0
        notes.update({i: [low, mid, high]})

    return notes
