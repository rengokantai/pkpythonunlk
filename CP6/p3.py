__author__ = 'Hernan Y.Ke'

import unittest
import sys
import time
from xml.etree import ElementTree as ET
from unittest import TextTestRunner

class XMLTestResult(unittest.TestResult):

    def __init__(self, *args, **kwargs):
        unittest.TestResult.__init__(self,*args,**kwargs)
        self.xmldoc = ET.fromstring('<testsuite/>')

    def startTest(self, test):
        test.starttime = time.time()
        test.testxml = ET.SubElement(self.xmldoc,
                                     'testcase',
                                     attrib={'name': test._testMethodName,
                                             'classname': test.__class__.__name__,
                                             'module': test.__module__})

    def stopTest(self, test):
        et = time.time()
        time_elapsed = et - test.starttime
        test.testxml.attrib['time'] = str(time_elapsed)

    def addSuccess(self, test):
        test.testxml.attrib['result']='ok'

    def addError(self, test, err):
        unittest.TestResult.addError(self,test,err)
        test.testxml.attrib['result']='error'
