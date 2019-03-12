# PerspicuOS

## Introduction:

PerspicuOS is a prototype operating system that realizes the Nested Kernel, a
new operating architecture that restricts access to a device's memory
management unit so that it can then perform memory isolation within the kernel.
The key challenge that PerspicuOS addresses is how to virtualize the MMU on
real hardware, AMD64, in a real operating system, FreeBSD 9.0, while not
assuming any hardware privilege separation or kernel integrity properties such
as control flow integrity. PerspicuOS presents a technique that allows both
trusted and untrusted code to operate at the same hardware privilege level,
thereby virtualizing Ring 0 supervisor privilege.

PerspicuOS does this by virtualizing the MMU, which requires memory protections
for Page Tables and CPU protections for control register isolation. PerspicuOS
protects the page tables by intializing all mappings in the system so that Page
Table Pages are mapped as read-only, and then introduces a technique that we
call de-privileging to ensure those privileges are never bypassed at runtime.
PerspicuOS de-previleges the untrusted portion of the kernel by removing all
MMU modifying instructions from the untrusted code's source, which statically
reduces its privilege. Then PerspicuOS enforces lifetime kernel code integrity
(mapping all code pages as read-only), denies execution of kernel data (using
no-execute hardware), and denies execution of user mode code and data pages
while in supervisor mode (using supervisor mode execution prevention).

By design PerspicuOS defends against a large class of attacks in code injection
because of it's code integrity properties. We also use PerspicuOS to explore
protection of the system call vector table, recording modifications of the
allproc processor list data structure, and to invoke a security monitor that
records audit records to a protected log. For more details on the design of
PerspicuOS please read our recent ASPLOS publication here.

## Authors and Contributors

PerspicuOS has several contributors: Nathan Dautenhahn, Theodoras Kasampalis,
Will Dietz, John Criswell, and Vikram Adve. This work was accomplished while
working at the University of Illinois at Urbana-Champaign in the LLVM research
group under the supervision of Vikram Adve.

## Build Instructions

Our current nested kernel implementation is for x86-64 FreeBSD is called
PerspicuOS.

1. Install FreeBSD 9.0: 

For installing on physical machine: http://ftp.sun.ac.za/ftp/pub/iso-images/freebsd/9.0/amd64/FreeBSD-9.0-RELEASE-amd64-memstick.img
For installing on virtual Machine: http://ftp.sun.ac.za/ftp/pub/iso-images/freebsd/9.0/amd64/FreeBSD-9.0-RELEASE-amd64-dvd1.iso


2. In FreeBSD 9.0 System, clone Nested Kernel PerspicuOS from GitHub

Unfortunately, FreeBSD 9.0 is out of date and thus the system cann't update its software.
Therefore, we need to use the FTP client to get the repository of PerspicuOS


3. Build the LLVM before the kernel

LLVM should be built in a machine installing FreeBSD 9.3 or higher.
Install FreeBSD 9.3 is easy as it is still alive. Get the ISO from http://ftp.freebsd.org/pub/FreeBSD/releases/ISO-IMAGES/9.3/

Pack the bin and lib directories togehter as a tar-file, and then copy it to 9.0 with FTP client.


4. Build the nested kernel (assumes clang is in /usr/bin/clang) 
	```
	$ cd REPO_DIR/nk 
	$ make
	```

5. Configure FreeBSD for buiding

    Get a copy of build-config/src.conf, and modify as following:
    Suppose the root path of PerspicuOS is "/usr/home/nk/project/PerspicuOS"
    Meanwhile the path of clang is "llvm/release/bin/clang"
 
	```
	# This setting to build world without -Werror: 
	NO_WERROR= 
	# This setting to build kernel without -Werror: 
	WERROR= 
    SVA_HOME=/PATH/TO/REPO_DIR 
    NK_HOME=/PATH/TO/REPO_DIR 
    
    # Build SVA kernel by default
    KERNCONF=SVA

	# Configure the system to use clang 
    SVA_INST_FLAGS=-mllvm -x86-add-cfi
	CC=/PATH/TO/CLANG  -I${SVA_HOME}/nk/include ${SVA_INST_FLAGS}
	CXX=/PATH/TO/CLANG++  -I${SVA_HOME}/nk/include ${SVA_INST_FLAGS}
	#CPP=/PATH/TO/CLANG++  -I${SVA_HOME}/nk/include ${SVA_INST_FLAGS}
	# Export the nested kernel library directory for the linker script in FreeBSD. 
	
	# Set the library path to the nested kernel lib 
	CFLAGS+=-I/PATH/TO/REPO_DIR/nk/include
	```

6. Make PerspicuOS
Traditionally, a customized FreeBSD kernel is build under directory /usr/src
So we first backup the old /usr/src as /usr/src.org
Then make a link to the nested kernel like this:
cd /usr && ln -sf /usr/home/nk/project/PerspicuOS/FreeBSD9 src

However, things is not straight forward. The clang binary we built in FreeBSD 9.3 cannot run in FreeBSD 9.0.
We need to copy all the dependent libraries (use ldd to check) in FreeBSD 9.3 to FreeBSD 9.0.
Suppose we put them in /usr/svalib. Then we use command "setenv LD_LIBRARY_PATH /usr/svalib" to tell the linker use these libraries.

At this time, all the preparing is done and we can compile the kernel in FreeBSD fashion:)
Before that, backup the /boot/kernel use command "cp -Rp kernel kernel.backup".

make buildkernel KERNCONF=SVA -j10
make installkernel KERNCONF=SVA



6. Install and Boot (you can use either the base harddrive or a VM
tool Like Qemu, VirtualBox, or VMWare)

On a physical machine, if have problems, we can mount FreeBSD9.0 driver and use command "mv kernel.backup kernel" to restore the original kernel.

We have a tool that automates the kernel compile and install process in
"REPO_DIR/scripts/compile_install_test_sva.rb". You can use this, but make sure
to read the code to understand how it operates.

## Implementation Needs

  PerspicuOS does not implement the full nested kernel design. Make sure to
  review the paper to see a list of currently implemented features.  

  A few key features requiring further development include: 
    - SMP functionality
    - Complete NX configuration for non-code pages
    - Finish IDT, SMM, IOMMU

## Comment on PerspicuOS Repo

PerspicuOS was derived from a few other research projects and as such reflects
an odd arangement of naming conventions and unused functionality. The nested
kernel shared a similar interface as previous work using the SVA compiler based
virtual machine (SVA Github), but only includes a small subset of the entire
interface, namely the MMU, and modifies the functionality of the internal
policies for page-translation updates.

## Support or Contact

Having trouble with PerspicuOS? We are currently setting up a suitable method
for contact. Otherwise, submit a pull request to start some code specific
dialog.
