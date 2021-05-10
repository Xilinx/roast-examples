#
# Copyright (c) 2020 Xilinx, Inc. All rights reserved.
# SPDX-License-Identifier: MIT
#

from box import Box

deploy_artifacts = "{buildDir}/{machine}/deploy/"

xsct_xsa = "{ROOT}/osl_demo/component/elf/src/{variant}/{machine}/system.xsa"
xsct_outDir = "{deploy_artifacts}"
xsct_os_name = "standalone"
FSBL_CFLAGS = ""
PMUFW_CFLAGS = ""

zynqmp = Box(default_box=True, box_intact_types=[list, tuple])
zynq = Box(default_box=True, box_intact_types=[list, tuple])

# Set Elf configs for zynqmp
zynqmp.component = "zynqmp_fsbl"

zynqmp.pmufw.xsct_proc_name = "psu_pmu_0"
zynqmp.pmufw.component = "zynqmp_pmufw"
zynqmp.pmufw.extra_args = "compiler-optimization:set:Optimize for size (-Os),\
                           define-compiler-symbols:add:DEBUG_MODE,define-compiler-symbols:add:XPFW_DEBUG_DETAILED,\
                           compiler-misc:add:{PMUFW_CFLAGS}"

zynqmp.zynqmp_fsbl.xsct_proc_name = "psu_cortexa53_0"
zynqmp.zynqmp_fsbl.extra_args = (
    "define-compiler-symbols:add:FSBL_DEBUG_INFO,compiler-misc:add:{FSBL_CFLAGS}"
)


# Set Elf configs for zynq
zynq.xsct_proc_name = "ps7_cortexa9_0"
zynq.component = "zynq_fsbl"
zynq.zynq_fsbl.extra_args = (
    "define-compiler-symbols:add:FSBL_DEBUG_INFO,compiler-misc:add:{FSBL_CFLAGS}"
)
zynq.fsbl_a9_rsa.extra_args = "define-compiler-symbols:add:FSBL_DEBUG_INFO,define-compiler-symbols:add:RSA_SUPPORT"
