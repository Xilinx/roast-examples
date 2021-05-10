#
# Copyright (c) 2020 Xilinx, Inc. All rights reserved.
# SPDX-License-Identifier: MIT
#

import pytest
import re
from roast.utils import mkdir, copy_file, overrides
from roast.component.xsct import buildapp as xsct
from tests import osl_tests, get_variant
from roast.component.osl.build_component import BuildOsl, BuildDtb, BuildRootfsModule


components = ["dtb", "uboot", "atf", "kernel", "rootfs"]


def opensource_builder(config, component, variant=None, board=None, machine=None):
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


@pytest.mark.parametrize("test", osl_tests.get_tests())
def test_component(test, create_configuration):
    test_dict = osl_tests.get_test_params(test)
    component = test_dict["test"]
    machine = test_dict["machine"]
    variant = get_variant(machine)
    board = re.sub("_", "-", machine)

    if component not in components:
        elf = test_dict["test"]
        if variant:
            config = create_configuration(params=["elf", variant, elf], machine=machine)
            overrides(config, variant)

        if elf:
            overrides(config, elf)
        else:
            config = create_configuration(params=[component])

        config["variant"] = variant
        config["xsct_elf_name"] = elf
        mkdir(config["deploy_artifacts"])
        # Call Buildapp
        assert xsct.xsct_builder(config)
    else:
        if variant != None:
            config = create_configuration(params=[component, variant], machine=machine)
            config["variant"] = variant
            overrides(config, variant)
            overrides(config, board)
        else:
            config = create_configuration(params=[component], machine=machine)
        opensource_builder(config, component, variant, board, machine)
