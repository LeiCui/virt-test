#!/usr/bin/python

import unittest
import common
from virttest import utils_libvirtd

class UtilsLibvirtdTest(unittest.TestCase):
    @unittest.skipIf(not utils_libvirtd.LIBVIRTD, "skip if libvirtd is not available")
    def test_service_libvirtd_control(self):
        service_libvirtd_control = utils_libvirtd.service_libvirtd_control
        self.assertRaises(utils_libvirtd.LibvirtdActionUnknownError,
                          service_libvirtd_control, 'UnknowAction')
        self.assertTrue(service_libvirtd_control('status') in (True, False))

    def test_libvirtd_error(self):
        action_list = ["restart", "start", "stop", "status"]

        for action in action_list:
            self.assertRaises(utils_libvirtd.LibvirtdActionError,
                              utils_libvirtd.service_libvirtd_control,
                              action=action, libvirtd="")
if __name__ == "__main__":
    unittest.main()
