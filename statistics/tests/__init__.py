# -*- coding: UTF-8 -*-
import statistics
import unittest

def suite():

    import doctest
    suite = unittest.TestSuite()
    suite.addTests(doctest.DocTestSuite(statistics))
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())