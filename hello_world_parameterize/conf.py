#
# Copyright (c) 2020 Xilinx, Inc. All rights reserved.
# SPDX-License-Identifier: MIT
#

# Mandatory Common Configuration required
sharedWs = "{buildDir}/shared_ws"
XSCT_BUILD_SOURCE = "local"  # build source type whether to be used XSCT default or git source (i.e. XSCT_BUILD_SOURCE="git")
version = "2020.2"  # Vitis version installed and to be used
vitisPath = ""  # user needs to mentioned Vitispath path where vitis is installed in user's system

# building common image specific configurations
xsct_xsa = (
    "{ROOT}/hello_world_parameterize/src/system.xsa"  # ZynqMP HW Designs xsa file
)
xsct_proc_name = "psu_cortexa53_0"  # For ZynqMP Processor


# building hello world application specific configurations
hello_world = {
    "component": "empty_application_legacy",  # Use this setting, if user wants to provide his own src code
    "xsct_import_sources": "{ROOT}/hello_world_parameterize/src/hello_world.c",  # Hello World Demo Src Code
}


# building fsbl image specific configurations
fsbl = {
    "component": "zynqmp_fsbl",  # FSBL build is needed to run any zynqmp application on board
}


# running hello world application specific configurations
fsbl_path = "{ROOT}/build/hello_world_parameterize/build/fsbl/images/zynq_mp_fsbl.elf"
elf_path = "{ROOT}/build/hello_world_parameterize/build/hello_world/images/empty_application.elf"
proc = "Cortex-A53*#0"


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
