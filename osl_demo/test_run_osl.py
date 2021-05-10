#
# Copyright (c) 2020 Xilinx, Inc. All rights reserved.
# SPDX-License-Identifier: MIT
#

import pytest
import os
import time
import logging
from box import Box
from roast.utils import TestCollect, setup_logger
from tests import get_board_list, Board_List, get_variant
from roast.component.board.boot import (
    linux_login_cons,
    uboot_login,
    jtag_boot,
)

osl_tests = TestCollect()
bootmode = ["jtagboot"]


def generate_tests():
    # This api generates test cases by mapping components and machine values
    global osl_tests
    machines = (
        [pytest.machine] if pytest.machine else None or get_board_list(Board_List)
    )
    test_collect = Box(default_box=True)
    for machine in machines:
        test_collect[machine] = {}
        test_collect[machine]["tests"] = bootmode

    for machine in machines:
        osl_tests.add_tests(machine=machine, test=test_collect[machine].tests)


generate_tests()


@pytest.mark.parametrize("test", osl_tests.get_tests())
def test_run_jtagboot(board, test):
    test_dict = osl_tests.get_test_params(test)
    machine = test_dict["machine"]
    variant = get_variant(machine)
    board = board(
        test_name=test_dict["test"],
        params=[variant, machine],
        machine=machine,
    )
    setup_logger(board.config.logDir, console_level=logging.DEBUG)
    config = board.config
    images_dir = config["deployDir"]

    jtag_boot(board.serial, board.xsdb, config, images_dir, variant)

    linux_login_cons(
        board.serial, user="root", password="root", login=True, timeout=300
    )
