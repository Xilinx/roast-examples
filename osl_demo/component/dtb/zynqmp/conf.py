#
# Copyright (c) 2020 Xilinx, Inc. All rights reserved.
# SPDX-License-Identifier: MIT
#

from box import Box

static_data = Box(default_box=True, box_intact_types=[list, tuple])

deploy_artifacts = "{buildDir}/{machine}/deploy/"

##Declare Board specific config data for zynqmp dtb build
static_data.zcu106.dtb_artifacts = [
    "arch/arm/dts/zynqmp-zcu106-revA.dtb",
]
