"""
pytest-orchestrated tests for pgc_ortho.py
"""

# std modules:
from unittest import TestCase
from unittest.mock import patch
import os
import pytest


class Test_pgc_ortho(TestCase):
    test_output_path = './tests/output'

    def set_up(self):
        os.makedirs(os.path.dirname(self.test_output_path), exist_ok=True)

    @pytest.mark.testdata_required
    @patch('os.stat')  # patch to collect info instead of actually calling
    def test_pgc_doesnt_raise(self, mock_os_stat):
        from pgc_ortho import main
        import sys
        testargs = [
            '-p', '4326',
            '-c', 'ns',
            '-t', 'UInt16',
            '-f', 'GTiff',
            (
                './tests/testdata/ortho/tests/testdata/ortho'
                '/GE01_20110307105821_1050410001518E00_11MAR07105821-M1BS'
                '-500657359080_01_P008.ntf'
            ),
            self.test_output_path
        ]
        with patch.object(sys, 'argv', testargs):
            main()
