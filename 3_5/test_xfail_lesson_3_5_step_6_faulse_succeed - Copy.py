import pytest

@pytest.mark.xfail(strict=True)
def test_succeed():
    print("test_succeed ____________")
    assert True


@pytest.mark.xfail
def test_not_succeed():
    print("mark.xfail test_not_succeed ____________")
    assert False


@pytest.mark.skip
def test_skipped():
    print("mark.skip test_skipped ____________")
    assert False
