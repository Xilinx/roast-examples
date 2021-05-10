#
# Copyright (c) 2020 Xilinx, Inc. All rights reserved.
# SPDX-License-Identifier: MIT
#

from box import Box

git = Box(default_box=True, box_intact_types=[list, tuple])

# DTG Repo configurations
# git.dtb.url = "https://github.com/Xilinx/device-tree-xlnx.git"
git.dtb.url = "https://github.com/Xilinx/u-boot-xlnx.git"
git.dtb.branch = "master"
dtb_arch = "aarch64"
dtb_compiler = "aarch64-linux-gnu-"
dtb_defconfig = "xilinx_zynqmp_virt_defconfig"
dtb_artifacts = ["arch/arm/dts/system.dtb"]

dtb_buildtype = "static"
