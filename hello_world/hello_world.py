#
# Copyright (c) 2020 Xilinx, Inc. All rights reserved.
# SPDX-License-Identifier: MIT
#

# building hello world application specific configurations
component = "empty_application_legacy"  # Use this setting, if user wants to provide his own src code
xsct_import_sources = (
    "{ROOT}/hello_world/src/hello_world.c"  # Hello World Demo Src Code
)
