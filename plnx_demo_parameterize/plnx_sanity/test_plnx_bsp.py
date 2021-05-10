#
# Copyright (c) 2020 Xilinx, Inc. All rights reserved.
# SPDX-License-Identifier: MIT
#

import pytest
import time
import socket
from roast.utils import TestCollect
from roast.component.petalinux import petalinux_build, petalinux_boot
from roast.component.board.boot import linux_login_cons, uboot_login

platforms = ["zynqmp"]
bsp = {"zynqmp": ["zcu106_bsp"]}
plnx_sanity = ["prebuilt-2", "uboot", "prebuilt-3", "kernel"]

bsptests = TestCollect()
sanity_tests = TestCollect()

for platform in platforms:
    bsptests.add_tests(platform=platform, bsp=bsp[platform])
    sanity_tests.add_tests(platform=platform, bsp=bsp[platform], sanity=plnx_sanity)


@pytest.mark.parametrize("test", bsptests.get_tests())
def test_build_petalinux(create_configuration, test):
    """Building BSP based on board and platform define"""

    test_dict = bsptests.get_test_params(test)
    config = create_configuration(
        test_name=test_dict["platform"], params=[test_dict["bsp"]]
    )
    assert petalinux_build(config)


@pytest.mark.parametrize("test", sanity_tests.get_tests())
def test_run_jtag_sanity(test, board):
    """Executing jtag boot sanity tests"""

    test_dict = sanity_tests.get_test_params(test)
    boot = sanity = test_dict["sanity"].replace("-", " ")
    board = board(
        test_name=test_dict["platform"], params=[test_dict["bsp"]], xsdb=False
    )
    petalinux_boot(
        board.config, boottype=boot, hwserver=socket.gethostbyname("localhost")
    )

    if sanity in ("prebuilt 2", "uboot"):
        uboot_login(board.serial)
    else:
        linux_login_cons(board.serial)
        board.serial.runcmd(cmd="ifconfig")
