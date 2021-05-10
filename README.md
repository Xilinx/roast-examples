# roast-examples
This repo contains Test suites for roast-examples.

## Getting Started

## Pre-requisites

User needs to install Python3 version >=3.6 along with pip3 and virtual environments python package. 

- Python3.6 +
- pip3
- virtualenv 
- picocom  ( Terminal emulator for serial port access and communication)
- xvfb


The PetaLinux tools need to be installed as a non-root user.

This repo has been tested with below version along with dependent Xilinx tools/packages/libraries on Ubuntu 18.04 machine as mentioned below:

--------------------------------------------------------------------
- **roast - 2.1.0**
- **pytest-roast - 1.2.0.post1**
- **roast-xilinx - 2.1.0**
- **Petalinux - 2020.2**
- **Vitis - 2020.2**
--------------------------------------------------------------------

                                                                                                                                               
[Xilinx PetaLinux installation user guide](docs/PetaLinux_installation_user_guide.txt)                                                                                                                                                                                                                                                                                     
[Xilinx Vitis installation user guide](docs/Xilinx_Vitis_installation_user_guide.txt)
                                                                                                                                                         
[Common issues user guide](docs/Common_issues_user_guide.txt)


In ROAST, picocom application has been used for connecting and disconnecting local board support.
https://github.com/npat-efault/picocom


### USING PYPI TO SETUP ROAST ENVIRONMENT:

```bash
#Install all pre-requisites ROAST environment
pip3 install roast
pip3 install pytest-roast
pip3 install roast-xilinx
```

OR

### USING PYPI TO SETUP ROAST WITH PYTHON VIRTUAL ENVIRONMENT:

```bash
#Setup virtual env
python3 -m venv ./.venv

#Source venv
source ./.venv/bin/activate

#Install all pre-requisites ROAST environment
pip3 install roast
pip3 install pytest-roast
pip3 install roast-xilinx
```

### Execute sample examples repository test cases 
```bash
git clone <any test repo>
cd <any test repo name>/

# To list all test cases
pytest --collect-only

# To run all test cases and if user wants to display log on stdout use "-s" 
pytest -s -vv

#To filter and run specific test case based on test function name use "-k"
pytest -s -k "build" -vv
pytest -s -k "run" -vv
```

## Execute Test Suite

### Fetch the repository roast_examples tests repo:

```bash
#Cloning roast_examples regression to be tested
git clone https://github.com/Xilinx/roast_examples.git

#Go to roast_examples directory
cd roast_examples
```

### hello_world Tests Execution

- **For Running build test cases from hello_world directory**
```bash
pytest hello_world/test_hello_world.py -k "build" -vv
```
- **For Running Run test cases from hello_world directory**
```bash
pytest hello_world/test_hello_world.py -k "run" -vv
```


### hello_world_parameterize Tests Execution

- **For Running build test cases from hello_world_parameterize directory**
```bash
pytest hello_world_parameterize/test_hello_world_parameterize.py -k "build" -vv
```
- **For Running Run test cases from hello_world_parameterize directory**
```bash
pytest hello_world_parameterize/test_hello_world_parameterize.py -k "run" -vv
```


### hello_world_parameterize2 Tests Execution

- **For Running build test cases from hello_world_parameterize2 directory**
```bash
pytest hello_world_parameterize2/test_hello_world_parameterize2.py -k "build" -vv
```
- **For Running Run test cases from hello_world_parameterize2 directory**
```bash
pytest hello_world_parameterize2/test_hello_world_parameterize2.py -k "run" -vv
```

### Pre-requisites plnx_demo and plnx_demo_parameterize :
-> This is xilinx-petalinux download page link where you find packages/BSPs for petalinux test cases.

    Download link:- https://www.xilinx.com/support/download/index.html/content/xilinx/en/downloadNav/embedded-design-tools/2020-2.html

-> Zynq UltraScale+ MPSoC Board Support Packages - <version>                                                                                                                     
   ---> Download:- ZCU106 BSP (BSP - 1.74 GB)

-> Zynq-7000 SoC Board Support Packages - <version>                                                                                                                               
   ---> Download:- ZC706 BSP (BSP - 110.74 MB)

Note:- 
Once plnx build test case is run successfully, you can use rootfs.cpio file from "build/zynqmp/<zcu106_bsp/zc706_bsp>/images/" and 
rename osl_demo's required file. Also alternately, you can use xilinx open source base rootfs file.  

Incase if you have issue running multiple test cases, use usb_relay to auto power on and off board.

Replace <version> with your requirement. Also note that size of each file may be different depends on version.


### plnx_demo Tests Execution
- **For Running build test cases from plnx_demo directory**
```bash
pytest plnx_demo/test_zynqmq_bsp.py -k "build" -vv
```
- **For Running Run test cases from plnx_demo directory**
```bash
pytest plnx_demo/test_zynqmq_bsp.py -k "run" -vv
```

### plnx_demo_parameterize Tests Execution

- **For Running build test cases from plnx_demo_parameterize directory**
```bash
pytest plnx_demo_parameterize/plnx_sanity/test_plnx_bsp.py -k "build" -vv
```
- **For Running Run test cases from plnx_demo_parameterize directory**
```bash
pytest plnx_demo_parameterize/plnx_sanity/test_plnx_bsp.py -k "run" -vv
```

### osl_demo_basic Tests Execution
### Pre-requisites
User has to copy respective base-rootfs files based on platform from tar/zip folder to osl_demo_basic/component/src path directory structure as mentioned below:                                     
component                                                                                                                                                    
│   └── src                                                                                                                                                                     
│       ├── mkimage                                                                                                                                          
│       ├── zynq                                                                                                                                             
│       │   └── petalinux-image-minimal-zynq-generic.rootfs.cpio                                                                                             
│       └── zynqmp                                                                                                                                           
│           └── petalinux-image-minimal-zynqmp-generic.rootfs.cpio                                                                                           


i.e.  
osl_demo_basic/component/src/zynqmp/petalinux-image-minimal-zynqmp-generic.rootfs.cpio
osl_demo_basic/component/src/zynq/petalinux-image-minimal-zynq-generic.rootfs.cpio

- **For Running build test cases from osl_demo_basic directory**
```bash
pytest osl_demo_basic/test_build_osl_basic.py -k zcu106 -vv
```
- **For Running Run test cases from osl_demo_basic directory**
```bash
pytest osl_demo_basic/test_run_osl_basic.py -k zcu106 -vv
```


### osl_demo Advance Tests Execution
## Pre-requisites
User has to create two folder namely zynqmp and zynq under component/rootfs/src path directory structure as mentioned below:                                                            
And copy respective base-rootfs files based on platform from tar/zip folder.

component                                                                                                                                                                           
├── rootfs                                                                                                                                                                        
│   ├── conf.py                                                                                                                                                                    
│   └── src                                                                  
│       ├── mkimage                                                                                                                                                               
│       ├── zynq                                                                                                                                                                   
│       │   └── petalinux-image-minimal-zynq-generic.rootfs.cpio                                                                                                                     
│       └── zynqmp                                                                                                                                                                   
│           └── petalinux-image-minimal-zynqmp-generic.rootfs.cpio                                                                                                                   

i.e.  
osl_demo/component/rootfs/src/zynqmp/petalinux-image-minimal-zynqmp-generic.rootfs.cpio
osl_demo/component/rootfs/src/zynq/petalinux-image-minimal-zynq-generic.rootfs.cpio

- **For Running build test cases from osl_demo directory**
```bash
pytest osl_demo/test_build_osl.py --machine=zcu106 -vv
```
- **For Running Run test cases from osl_demo directory**
```bash
pytest osl_demo/test_run_osl.py --machine="zcu106" -vv
```
