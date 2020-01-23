# Testing
Tests are divided into two testing methodologies.

## PGC manual tests
To run PGC manual tests, call the files within `./tests/` directly:

```
python tests/unit_test_taskhandler.py
```

Most of these tests require additional files at `./tests/testadata/`.
These files cannot be publically distributed but can be requested from PGC.

## pytest tests
Tests set up to be run with pytest can be run via the following command:

```
python3 -m pytest
```

Some pytest-orchestrated tests also require additional files at `./tests/testdata`.
These tests are marked as `testdata_required`.
To run all tests except those marked as `testdata_required` use the following:

```
python3 -m pytest -m "not testdata_required"
```
