#
# Copyright (c) 2020 Xilinx, Inc. All rights reserved.
# SPDX-License-Identifier: MIT
#

from box import Box

git = Box(default_box=True, box_intact_types=[list, tuple])
zynqmp = Box(default_box=True, box_intact_types=[list, tuple])


# ATF Repo configurations
git.atf.url = "https://github.com/Xilinx/arm-trusted-firmware.git"
git.atf.branch = "master"
atf_arch = "arm64"
atf_compiler = "aarch64-linux-gnu-"
atf_artifacts = []

# Set atf configs for zynqmp
zynqmp.atf_compile_flags = (
    "RESET_TO_BL31=1 PLAT=zynqmp bl31 ZYNQMP_PLATFORM=silicon BUILD_BASE=../atf-build"
)
zynqmp.atf_artifacts = ["zynqmp/release/bl31/bl31.elf"]
