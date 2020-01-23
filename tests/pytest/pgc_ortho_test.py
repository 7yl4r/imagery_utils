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

    def setUp(self):
        os.makedirs(os.path.dirname(self.test_output_path), exist_ok=True)

    # def tearDown(self):
    #     shutil.rmtree(os.path.dirname(self.test_output_path))

    @pytest.mark.testdata_required
    @patch('os.stat')  # patch to collect info instead of actually calling
    def test_pgc_doesnt_raise(self, mock_os_stat):
        """
        Functional test of pgc_ortho CLI usage.

        pgc_ortho.py -p 4326 -c ns -t UInt16 -f GTiff ./tests/testdata/ortho/WV02_20131005052802_10300100278D8500_13OCT05052802-P1BS-500099283010_01_P004.NTF ./tests/tesdata/output
        """
        from pgc_ortho import main
        import sys
        testargs = [
            'pgc_ortho.py',  # /media/tylar/filestore/git-repos/imars/imagery_utils/pgc_ortho.py
            '-p', '4326',
            '-c', 'ns',
            '-t', 'UInt16',
            '-f', 'GTiff',
            (
                './tests/testdata/ortho'
                '/WV02_20131005052802_10300100278D8500_13OCT05052802-P1BS-'
                '500099283010_01_P004.NTF'
            ),
            self.test_output_path
        ]
        with patch.object(sys, 'argv', testargs):
            main()
