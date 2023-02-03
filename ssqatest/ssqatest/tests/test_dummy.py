import pytest
@pytest.mark.usefixtures("init_driver")
class TestDummy():
    def test_dummy_func(self):
        print('I am dummy test line 1')
        print('I am dummy test line 2')
        self.driver.get('http://demostore.supersqa.com/')
        import pdb; pdb.set_trace()

#terminal: python -m pytest
#fixture is something that runs along every test/class/module ...
#fixture can be inside of the test file or they can be in their own file or in a conf test file
