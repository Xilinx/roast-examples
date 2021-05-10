#
# Copyright (c) 2020 Xilinx, Inc. All rights reserved.
# SPDX-License-Identifier: MIT
#

# Common Configuration required
version = "2020.2"  # Petalinux tool version installed and to be used
vitisPath = ""  # user needs to mentioned Vitispath path where vitis is installed in user's system

# Petalinux BSP Mandatory configurations
PLNX_TOOL = ""  # petalinux tool path (i.e. source the petalinux tool)
BSP_PATH = ""  # Using bsp or template flow to create petalinux project <path-to-bsp> and bsp path (default set to bsp flow)
PLNX_TMP_PATH = ""  # set temp path for petalinux project Default set to '/tmp/'
platform = "zynqmp"  # define platform (versal, zynqMP, zynq, microblaze)
plnx_package_boot = True  # Generate Package Boot Images
PLNX_BSP = "xilinx-zcu106-v{version}-final.bsp"  # BSP name
plnx_proj = "xilinx-zcu106-{version}"  # project name


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
