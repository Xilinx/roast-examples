#
# Copyright (c) 2020 Xilinx, Inc. All rights reserved.
# SPDX-License-Identifier: MIT
#

from box import Box

# Create DotDictify object for each platform to assign
# config vars for each platform in Dot Dictionary Notation

git = Box(default_box=True, box_intact_types=[list, tuple])
zynqmp = Box(default_box=True, box_intact_types=[list, tuple])
zynq = Box(default_box=True, box_intact_types=[list, tuple])


# U-boot Repo configurations
git.uboot.url = "https://github.com/Xilinx/u-boot-xlnx.git"
git.uboot.branch = "master"
uboot_arch = "arm64"
uboot_compiler = "aarch64-linux-gnu-"
uboot_defconfig = "xilinx_versal_virt_defconfig"
uboot_artifacts = ["u-boot.elf"]

deploy_artifacts = "{buildDir}/{machine}/deploy/"

# Declare Board specific config data for zynqmp uboot build
zynqmp.uboot_arch = "aarch64"
zynqmp.uboot_defconfig = "xilinx_zynqmp_virt_defconfig"
zynqmp.zcu106.uboot_devicetree = "zynqmp-zcu106-revA"

# Declare Board specific config data for zynq uboot build
zynq.uboot_arch = "arm"
zynq.uboot_compiler = "arm-linux-gnueabihf-"
zynq.uboot_defconfig = "xilinx_zynq_virt_defconfig"
zynq.zc706.uboot_devicetree = "zynq-zc706"
