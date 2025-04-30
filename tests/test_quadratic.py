import pytest
import numpy as np
from polysolve.quadexm import quadratic

def test_quadratic():
    """ Test """
    params = [3., 0., -1.]
    roots = quadratic(*params)
    assert all (np.isclose(np.polyval(params, root), 0.) for root in roots)

