"""
total(spam, 1, 2, a=3, b=4, _reps=1000) calls and times spam(1, 2, a=3, b=4)
_reps times, and returns total time for all runs, with final result.

bestof(spam, 1, 2, a=3, b=4, _reps=5) runs best-of-N timer to attempt to
filter out system load variation, and returns best time among _reps tests.

bestoftotal(spam 1, 2, a=3, b=4, _rep1=5, reps=1000) runs best-of-totals
test, which takes the best among _reps1 runs of (the total of _reps runs);
"""

import time, sys

# Check python version and platform type
if sys.version_info[0] >= 3 and sys.version_info[1] >= 3:
    timer = time.perf_counter
else:
    timer = time.clock if sys.platform[:3] == 'win' else time.time


def total(func, *pargs, **kargs):
    """
    Total time to run func() reps times.
    Returns (total time, last result)
    """
    _reps = kargs.pop('_reps', 1000)
    repslist = list(range(_reps))
    start = timer()               # Or perf_counter/other in 3.3+
    for i in repslist:
        ret = func(*pargs, **kargs)

    elapsed = timer() - start
    return elapsed, ret


def bestof(func, *pargs, **kargs):
    """Quickest func() among reps runs.    Returns (best time, last result)    """
    _reps = kargs.pop('_reps', 1000)
    best = 2 ** 32                  # 136 years seems large enough
    for i in range(_reps):           # range usage not timed here
        start = timer()
        ret = func(*pargs, **kargs)
        elapsed = timer() - start   # Or call total() with reps=1
        if elapsed < best:
            best = elapsed          # Or add to list and take min()
    return best, ret


def bestoftotal(func, *pargs, **kargs):
    """
    Best of totals:
    (best of reps1 runs of (total of reps2 runs of func))
    """
    _reps1 = kargs.pop('_reps1', 1000)
    return min(total(func, *pargs, **kargs) for i in range(_reps1))

