#
# Copyright (c) 2020 Xilinx, Inc. All rights reserved.
# SPDX-License-Identifier: MIT
#

from box import Box

# Create DotDictify object to assign config variables for
# each platform in Dot Dictionary notation

git = Box(default_box=True, box_intact_types=[list, tuple])
zynq = Box(default_box=True, box_intact_types=[list, tuple])
zynqmp = Box(default_box=True, box_intact_types=[list, tuple])

# Linux Kernel Repo configurations
git.kernel.url = "https://github.com/Xilinx/linux-xlnx.git"
git.kernel.branch = "master"
kernel_arch = "arm64"
kernel_compiler = "aarch64-linux-gnu-"
kernel_defconfig = "xilinx_defconfig"
kernel_artifacts = ["arch/arm64/boot/Image"]
kernel_loadaddr = 0x80000

deploy_artifacts = "{buildDir}/{machine}/deploy/"

# Declare board specific config vars for zynq linux build
zynq.kernel_defconfig = "xilinx_zynq_defconfig"
zynq.kernel_artifacts = ["arch/arm/boot/uImage"]
zynq.kernel_arch = "arm"
zynq.kernel_compiler = "arm-linux-gnueabihf-"
zynq.kernel_loadaddr = "0x200000"
zynq.kernel_compile_flags = "uImage LOADADDR=" + zynq.kernel_loadaddr

# Declare board specific config vars for zynqmp linux build
zynqmp.kernel_defconfig = "xilinx_defconfig"
zynqmp.kernel_artifacts = ["arch/arm64/boot/Image"]
zynqmp.kernel_arch = "arm64"
zynqmp.kernel_compiler = "aarch64-linux-gnu-"
