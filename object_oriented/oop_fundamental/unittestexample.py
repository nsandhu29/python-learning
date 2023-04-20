import types
import unittest

class TestAccess(unittest.TestCase):
    """ This class defines a few test we expect class to pass.
    The actual object tested is omitted. It's referenced as self.object, but no
    definition is provided, making this class abstract. A setup() method is required
    by each concrete subclass"""

    def test_should_add_and_get_attribute(self):
        self.object.new_attribute = True
        self.assertTrue(self.object.new_attribute)
    
    def test_should_fail_on_missing(self):
        self.assertRaises(AttributeError, lambda: self.object.undefined)

# The following are three TestAccess subclasses that will exercise three different kinds of object

class SomeClass:
    pass


class Test_EmptyClass(TestAccess):
    def setUp(self) -> None:
        self.object = SomeClass()

class TestNamespace(TestAccess):
    def setUp(self) -> None:
        self.object = types.SimpleNamespace()

class TestObject(TestAccess):
    def setUp(self) -> None:
        self.object = object()


def suite():
    s = unittest.TestSuite()
    s.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(Test_EmptyClass))
    s.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestNamespace))
    s.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestObject))
    return s

if __name__ == "__main__":
    t = unittest.TextTestRunner()
    t.run(suite())
    
