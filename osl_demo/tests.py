#
# Copyright (c) 2020 Xilinx, Inc. All rights reserved.
# SPDX-License-Identifier: MIT
#

from box import Box
import pytest
from roast.utils import TestCollect

Board_List = Box(default_box=True)
Board_List.zynqmp = ["zcu106"]
Board_List.zynq = ["zc706"]
zynqmp_elf = ["pmufw", "zynqmp_fsbl"]
zynq_elf = ["zynq_fsbl", "fsbl_a9_rsa"]
components = ["dtb", "uboot", "atf", "kernel", "rootfs"]

osl_tests = TestCollect()


def get_board_list(BoardList):
    board_list = []
    for variant, board in BoardList.items():
        for board_name in board:
            board_list.append(board_name)
    return board_list


def generate_tests():
    # This api generates test cases by mapping components and machine values
    global osl_tests
    machines = (
        [pytest.machine] if pytest.machine else None or get_board_list(Board_List)
    )
    test_collect = Box(default_box=True)
    for machine in machines:
        test_collect[machine] = {}
        test_collect[machine]["tests"] = components
        if machine in Board_List.zynqmp:
            test_collect[machine]["tests"] = zynqmp_elf + components
        elif machine in Board_List.zynq:
            test_collect[machine]["tests"] = zynq_elf + components

    for machine in machines:
        osl_tests.add_tests(machine=machine, test=test_collect[machine].tests)


def get_variant(board):
    for key, value in Board_List.items():
        if board in value:
            return key


generate_tests()
