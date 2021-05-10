#
# Copyright (c) 2020 Xilinx, Inc. All rights reserved.
# SPDX-License-Identifier: MIT
#

import pytest
import time
import logging
from roast.component.xsct import buildapp as xsct
from roast.utils import setup_logger
from roast.utils import overrides


@pytest.mark.parametrize("component", ["hello_world", "fsbl"])
def test_build(create_configuration, component):
    """Building and compiling of hello world application from src code, FSBL build which is needed to run any zynqmp application on board"""

    # Create configurations using fixture
    config = create_configuration(params=[component])
    # override hello world and fsbl specific parameters from conf based on component passed
    config = overrides(config, component)
    assert xsct.xsct_builder(config, setup=False)


def test_run(board):
    """Running hello world application demo"""

    # Use board fixture to acquired board object
    my_board = board()
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
