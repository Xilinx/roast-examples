#
# Copyright (c) 2020 Xilinx, Inc. All rights reserved.
# SPDX-License-Identifier: MIT
#

from box import Box

# Create Box object to assign config variables for
# each platform in Dot Dictionary notation


zynq = Box(default_box=True, box_intact_types=[list, tuple])
zynqmp = Box(default_box=True, box_intact_types=[list, tuple])
git = Box(default_box=True, box_intact_types=[list, tuple])

git.rootfs.url = "https://github.com/Xilinx/linux-xlnx.git"
git.rootfs.branch = "master"
rootfs_artifacts = []

deploy_artifacts = "{buildDir}/{machine}/deploy/"
linux_module = "{buildDir}/{machine}/{variant}"
rootfs_path = "{ROOT}/osl_demo/component/rootfs/src"

# Usage of mkimage binaries for rootfs build component
sysroot_tool = "{ROOT}/osl_demo/component/rootfs/src/"

# Set rootfs configs for zynq
zynq.rootfs_defconfig = "xilinx_zynq_defconfig"
zynq.rootfs_arch = "arm"
zynq.rootfs_compiler = "arm-linux-gnueabihf-"
zynq.kernel_loadaddr = "0x200000"
zynq.rootfs_compile_flags = "uImage LOADADDR=" + zynq.kernel_loadaddr

# Set rootfs configs for zynqmp
zynqmp.rootfs_defconfig = "xilinx_defconfig"
zynqmp.rootfs_arch = "arm64"
zynqmp.rootfs_compiler = "aarch64-linux-gnu-"
