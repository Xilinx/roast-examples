#
# Copyright (c) 2020 Xilinx, Inc. All rights reserved.
# SPDX-License-Identifier: MIT
#

# Mandatory Common Configuration required
sharedWs = "{buildDir}/shared_ws"
XSCT_BUILD_SOURCE = ""  # build source type whether to be used XSCT default or git source (i.e. XSCT_BUILD_SOURCE="git")
version = "2020.2"  # Vitis version installed and to be used
vitisPath = ""  # user needs to mentioned Vitispath path where vitis is installed in user's system
outoftreebuild = True

# Parallel Threads
parallel_make = 20

# delpoy artifacts
deploy_artifacts = "{wsDir}/../deploy/"


# Run test configuration
rootfs_path = "{ROOT}/build/{machine}/deploy/rootfs.cpio.gz.u-boot"
boot_scr_path = ""
deployDir = "{ROOT}/build/{machine}/deploy"


# local board configuration
# Serial communication configurations
"""
These below configurations will used to communicate,
with board which was connected to your host machine by using serial uart
"""
board_interface = "host_target"
com = "/dev/ttyUSB0"  # Allocate proper com port(ttyUSB0/ttyUSB1/ttyUSB2/ttyUSB3)
baudrate = "115200"


# Remote host configuration
"""
This below configuration need to enable if target connected to remote host machine.
remote_host = ""
"""
