#
# Copyright (c) 2020 Xilinx, Inc. All rights reserved.
# SPDX-License-Identifier: MIT
#

import pytest
import time
import socket
from roast.component.petalinux import petalinux_build, petalinux_boot
from roast.component.board.boot import linux_login_cons, uboot_login

plnx_sanity = ["prebuilt-2", "uboot", "prebuilt-3", "kernel"]


def test_build_zynqmp_petalinux(create_configuration):
    """Building BSP based on board and platform define"""

    config = create_configuration(test_name="zynqmp", params=["zcu106_bsp"])
    assert petalinux_build(config)


@pytest.mark.parametrize("test", plnx_sanity)
def test_run_jtag_sanity(test, board):
    """Executing jtag boot sanity tests"""

    boot = sanity = test.replace("-", " ")
    board = board(test_name="zynqmp", params=["zcu106_bsp"], xsdb=False)
    petalinux_boot(
        board.config, boottype=boot, hwserver=socket.gethostbyname("localhost")
    )

    if sanity in ("prebuilt 2", "uboot"):
        uboot_login(board.serial)
    else:
        linux_login_cons(board.serial)
        board.serial.runcmd(cmd="ifconfig")
