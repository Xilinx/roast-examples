#
# Copyright (c) 2020 Xilinx, Inc. All rights reserved.
# SPDX-License-Identifier: MIT
#

import pytest
import time
import logging
from roast.utils import setup_logger
from test_build_osl_basic import get_variant
from roast.component.board.boot import linux_login_cons, uboot_login, jtag_boot

test_cases = ["zcu106-jtagboot", "zc706-jtagboot"]


@pytest.mark.parametrize("test_case", test_cases)
def test_run_jtagboot(board, test_case):
    board_name, component = test_case.split("-")
    machine = board_name
    variant = get_variant(machine)
    board = board(test_name=component, params=[variant, machine], machine=machine)
    setup_logger(board.config.logDir, console_level=logging.DEBUG)
    config = board.config
    images_dir = config["deployDir"]

    jtag_boot(board.serial, board.xsdb, config, images_dir, variant)

    linux_login_cons(
        board.serial, user="root", password="root", login=True, timeout=300
    )
