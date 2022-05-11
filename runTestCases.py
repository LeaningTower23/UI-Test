import unittest
from Testcases.test_Dispatch import TestDispatch
from Testcases.test_ProcessCancel import TestProcess
from Testcases.test_ProcessEdit import TestEditProcess


if __name__ == "__main__":
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestDispatch)
    # suite2 = unittest.TestLoader().loadTestsFromTestCase(TestProcess)
    # suite3 = unittest.TestLoader().loadTestsFromTestCase(TestEditProcess)
    # suite = unittest.TestSuite([suite1, suite2, suite3])
    suite = unittest.TestSuite([suite1])
    unittest.TextTestRunner(verbosity=2).run(suite)
