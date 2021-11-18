# -*- coding: utf-8 -*-

import numpy as np
import pytest

from banana.data import genpdf
from banana.utils import lhapdf_path, test_pdf

# try:
#     import lhapdf
# except ImportError:
#     pytest.skip("No LHAPDF interface around", allow_module_level=True)
# TODO mark file skipped in coverage.py
lhapdf = pytest.importorskip("lhapdf")


def test_load_data_ct14():
    with lhapdf_path(test_pdf):
        blocks = genpdf.load.load_blocks_from_file("myCT14llo_NF3", 0)[1]
        assert len(blocks) == 1
        b0 = blocks[0]
        assert isinstance(b0, dict)
        assert sorted(b0.keys()) == sorted(["pids", "xgrid", "Q2grid", "data"])
        assert sorted(b0["pids"]) == sorted([-3, -2, -1, 21, 1, 2, 3])
        assert len(b0["data"].T) == 7
        np.testing.assert_allclose(b0["xgrid"][0], 1e-9)


def test_load_data_mstw():
    with lhapdf_path(test_pdf):
        blocks = genpdf.load.load_blocks_from_file("myMSTW2008nlo90cl", 0)[1]
        assert len(blocks) == 3
        b0 = blocks[0]
        assert isinstance(b0, dict)
        assert sorted(b0.keys()) == sorted(["pids", "xgrid", "Q2grid", "data"])
        assert sorted(b0["pids"]) == sorted([-5, -4, -3, -2, -1, 21, 1, 2, 3, 4, 5])
        np.testing.assert_allclose(b0["xgrid"][0], 1e-6)


def test_load_info():
    with lhapdf_path(test_pdf):
        info = genpdf.load.load_info_from_file("myCT14llo_NF3")
        assert "SetDesc" in info
        assert "fake" in info["SetDesc"]
        assert sorted(info["Flavors"]) == sorted([-3, -2, -1, 21, 1, 2, 3])


def test_load_head():
    with lhapdf_path(test_pdf):
        head_zero = genpdf.load.load_blocks_from_file("myMSTW2008nlo90cl", 0)[0]
        head_one = genpdf.load.load_blocks_from_file("myMSTW2008nlo90cl", 1)[0]
        assert head_zero == "PdfType: central\n"
        assert head_one == "PdfType: error\n"
