#
# Copyright (c) 2020 Xilinx, Inc. All rights reserved.
# SPDX-License-Identifier: MIT
#

import pytest
import re
import os
from box import Box
from roast.utils import mkdir, copy_file, overrides
from roast.component.xsct import buildapp as xsct
from roast.component.osl.build_component import BuildOsl, BuildDtb, BuildRootfsModule


components = ["dtb", "uboot", "atf", "kernel", "rootfs"]
test_cases = [
    "zcu106-pmufw",
    "zcu106-zynqmp_fsbl",
    "zcu106-dtb",
    "zcu106-uboot",
    "zcu106-atf",
    "zcu106-kernel",
    "zcu106-rootfs",
    "zc706-zynq_fsbl",
    "zc706-fsbl_a9_rsa",
    "zc706-dtb",
    "zc706-uboot",
    "zc706-atf",
    "zc706-kernel",
    "zc706-rootfs",
]

Board_List = Box(default_box=True)
Board_List.zynqmp = ["zcu106"]
Board_List.zynq = ["zc706"]


def get_variant(board):
    for key, value in Board_List.items():
        if board in value:
            return key


def opensource_builder(config, component, variant=None, board=None):
    config["component"] = component
    if component == "dtb":
        overrides(
            config,
            ["{config['dtb_buildtype']}_data", "static_data", variant, board],
        )
        builder = BuildDtb(config, board=board, variant=variant)
    elif component == "rootfs":
        builder = BuildRootfsModule(config, board=board, variant=variant)
    else:
        builder = BuildOsl(config)

    builder.setup_src()
    builder.configure()
    builder.compile()
    builder.deploy()


@pytest.mark.parametrize("test_case", test_cases)
def test_component(test_case, create_configuration):
    board, component = test_case.split("-")
    machine = board
    variant = get_variant(machine)

    if component not in components:
        elf = component
        if variant:
            config = create_configuration(
                params=["elf", variant, elf],
                overrides=[f"osl_demo_basic/component/elf.py"],
                machine=machine,
            )
            overrides(config, variant)

        if elf:
            overrides(config, elf)
        else:
            config = create_configuration(
                params=[component], overrides=[f"osl_demo_basic/component/elf.py"]
            )

        config["variant"] = variant
        config["xsct_elf_name"] = elf
        mkdir(config["deploy_artifacts"])
        # Call Buildapp
        assert xsct.xsct_builder(config)
    else:
        if variant != None:
            config = create_configuration(
                params=[component, variant],
                overrides=[f"osl_demo_basic/component/{component}.py"],
                machine=machine,
            )
            config["variant"] = variant
            overrides(config, variant)
            overrides(config, board)

        else:
            config = create_configuration(
                params=[component],
                overrides=[f"osl_demo_basic/component/{component}.py"],
                machine=machine,
            )
        opensource_builder(config, component, variant, board)
