#
# Copyright (c) 2020 Xilinx, Inc. All rights reserved.
# SPDX-License-Identifier: MIT
#

import pytest
import time
import logging
from roast.utils import TestCollect
from roast.component.xsct import buildapp as xsct
from roast.utils import setup_logger


build_base_tests = ["hello_world", "fsbl"]
run_base_tests = ["execute_hello_world"]

def_machine = ["zcu106"]
# Use command line machine option in test case
machines = [pytest.machine] if pytest.machine else None or def_machine

# Use of test Collector class
build_tests = TestCollect()
run_tests = TestCollect()

for machine in machines:
    build_tests.add_tests(machine=machine, test=build_base_tests)
    run_tests.add_tests(machine=machine, test=run_base_tests)


@pytest.mark.parametrize("test", build_tests.get_tests())
def test_build(create_configuration, test):
    """Building and compiling of hello world application from src code, FSBL build which is needed to run any zynqmp application on board"""

    test_params = build_tests.get_test_params(test)
    # Create configurations using fixture
    config = create_configuration(
        test_name=test_params["test"], machine=test_params["machine"]
    )
    assert xsct.xsct_builder(config, setup=False)


@pytest.mark.parametrize("test", run_tests.get_tests())
def test_run(board, test):
    """Running hello world application demo"""

    test_params = run_tests.get_test_params(test)
    # Use board fixture to acquired board object
    my_board = board(test_name=test_params["test"], machine=test_params["machine"])
    setup_logger(my_board.config.logDir, console_level=logging.DEBUG)

    # Set the processor
    my_board.xsdb.set_proc(my_board.config.proc)
    my_board.xsdb.rst_proc()
    # Load FSBL
    my_board.xsdb.load_elf(my_board.config.fsbl_path)
    my_board.xsdb.runcmd("con")
    # Load ELF
    time.sleep(60)
    my_board.xsdb.load_elf(my_board.config.elf_path)
    my_board.xsdb.runcmd("con")
    expected_list = ["Successfully", "PASSED"]
    my_board.serial.expect(expected=expected_list, timeout=300)
