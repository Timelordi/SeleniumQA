import unittest

from PackageManipulation.Package1.TC_Login import LoginTest
from PackageManipulation.Package1.TC_signup_Test import SignupTest

from PackageManipulation.Package2.TC_payment_Test import PaymentTest
from PackageManipulation.Package2.TC_payment_written_test import PaymentReturnsTest

# now we can get all tests from all external Packages
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)

#creating test suites
sanityTestSuite = unittest.TestSuite([tc1, tc2])
#unittest.TextTestRunner().run(sanityTestSuite)

#categorizing test suits
functionalTestSuite = unittest.TestSuite([tc3, tc4])
#unittest.TextTestRunner().run(functionalTestSuite)

#big test suit with all test cases
masterTestSuite = unittest.TestSuite([tc1, tc2, tc3, tc4])
unittest.TextTestRunner().run(masterTestSuite)