
import pytest

@pytest.mark.smoke #smoke test

def test_login_page_valid_user():
    print(' ')
    print('Login with valid user')
@pytest.mark.smoke #smoke test
def test_login_wrong_passw():
    print('Login with wrong password')
    # forcing test fail
    assert 1==2, 'test failed'

'''
terminal commands:
# show all the command line options --> pytest -h
# remove unnecessary warnings --> pytest -W ignore::pytest.PytestUnknownMarkWarning 
'''