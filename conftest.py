#
# Copyright (c) 2020 Xilinx, Inc. All rights reserved.
# SPDX-License-Identifier: MIT
#

# Import the 'modules' that are required for test cases execution
import pytest
import os
import logging
from roast.utils import teardown_logger

log = logging.getLogger(__name__)


@pytest.fixture(scope="function")
def setup_env(request):
    name = request.config.rootdir.strpath
    yield
    teardown_logger()
    os.chdir(name)
    log.info("workdir changes to rootdir")
