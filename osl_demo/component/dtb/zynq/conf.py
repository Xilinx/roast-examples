#
# Copyright (c) 2020 Xilinx, Inc. All rights reserved.
# SPDX-License-Identifier: MIT
#

from box import Box

static_data = Box(default_box=True, box_intact_types=[list, tuple])

deploy_artifacts = "{buildDir}/{machine}/deploy/"

##Declare Board specific config data for zynq dtb build
static_data.dtb_arch = "arm"
static_data.dtb_compiler = "arm-linux-gnueabihf-"
static_data.dtb_defconfig = "xilinx_zynq_virt_defconfig"
static_data.zc706.dtb_artifacts = ["arch/arm/dts/zynq-zc706.dtb"]
