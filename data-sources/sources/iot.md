Welcome to Fedora Internet of Things homepage. Fedora Internet of Things
is a Fedora Edition to provide a strong foundation for IoT ecosystems.
Whether you're working on a project at home, industrial gateways, smart
cities or analytics with AI/ML, Fedora IoT can provide a trusted open
source platform to build on. Fedora IoT rolling releases help you keep
your ecosystem up-to-date.

# Why use Fedora IoT? {#_why_use_fedora_iot}

The operating system (OS) for IoT systems needs to be immutable and
image based, where the image is fully tested centrally and signed before
being deployed at scale to IoT systems. As these IoT systems are often
located remotely, the OS should support atomic updates so nothing
changes until the device is rebooted and rollback capability so it is
easy to recover remotely if there is a failure during upgrade.

The Fedora IoT images work with
[rpm-ostree](https://coreos.github.io/rpm-ostree/), a hybrid
image/package system. It supports package layering, which allows
installation of RPMs for additional hardware support or applications.
The GPG signed image based deployments scale well to very large numbers
of clients. Updates are atomic with easy rollback capability.

The Fedora IoT images also have excellent support for container-focused
workflows. Containers allow you to separate core OS updates from
application updates as well as test and deploy different versions of
applications. The [podman](https://podman.io/) container engine is light
weight and ready for you to download or create containers for your home
assistant, industrial gateways, or data storage and analytics.

# Is Fedora IoT for you? {#_is_fedora_iot_for_you}

If you are looking for a graphical desktop environment based on OSTree
and designed for developers, look at [Fedora
Silverblue](https://fedoraproject.org/atomic-desktops/silverblue/).

If you are looking for a traditional dnf based operating system for your
device, visit [Fedora](https://fedoraproject.org/).

If you are after an OS for Kubernetes, there is [Fedora
CoreOS](https://fedoraproject.org/en/coreos/).

If you are looking for a lightweight yet powerful and scalable core OS
for your Internet of Things project, you came to the right place! [Get
Started with Fedora IoT](getting-started.xml)!

# Contribute to Fedora IoT Edition {#_contribute_to_fedora_iot_edition}

For communication and contributing please see the [Contributing and
Reporting Bugs](contributing.xml) section.

![SoC board](iot-fedora.svg)

# Getting Started {#_getting_started}

Welcome to the getting started guide for Fedora IoT. Both this guide and
Fedora IoT images are in the very early stages, so please report any
issues to [the mailing
list](https://lists.fedoraproject.org/admin/lists/iot.lists.fedoraproject.org/).

![SoC board](iot-fedora.svg)

## Supported Platforms {#_supported_platforms}

Fedora IoT supports the x86_64 and aarch64 architectures.

Refer to the list of currently tested [Reference
Platforms](reference-platforms.xml). The list of supported reference
platforms will expand over time. Other x86_64 or aarch64 platforms
should work just fine but haven't been widely tested in the IoT context
so your milage may vary.

If you're a hardware vendor and would like to have a device become a
reference platform by actively participating and testing Fedora IoT,
please reach out to [Peter
Robinson](https://fedoraproject.org/wiki/User:Pbrobinson), the Fedora
IoT Lead.

## Required Resources {#_required_resources}

The current images are 4GB in size and tested with 1GB of RAM. The
Fedora IoT base image should be able to run with less resources, but of
course this will limit the amount of container applications that can be
run on top of the base OS.

## Download Image {#_download_image}

Fedora IoT images are available for download at the [Download Fedora IoT
page](https://fedoraproject.org/iot/download). There are three options
available to install IoT on your device:

&#42; Anaconda installer ISO (Fedora-IoT-ostree-XX.XX.iso ) - The
traditional Fedora installer, offers an interactive graphical
installation tool to configure most aspects of the system including
filesystem, users and passwords. &#42; Disk image
(Fedora-IoT-raw-XX.XX.raw.xz) - A pre-built disk image suitable for
single board computers (SBC's) like the Raspberry Pi 4. &#42; Simplified
Provisioning ISO (Fedora-IoT-provisioner-XX.iso) - A new tool offering
zero touch installation leveraging [FIDO Device
Onboarding](fdo-device-setup.xml) or
[Ignition](ignition-device-setup.xml) for configuration.

## Setup VM or Physical Device {#_setup_vm_or_physical_device}

- Follow these steps to [setup virtual
  machine](virtual-machine-setup.xml)

- Follow these steps to [setup physical
  device](physical-device-setup.xml)

Follow the setup instructions from [ignition](ignition-device-setup.xml)

# Obtaining Images {#_obtaining_images}

Available images for download are described on the [Download Fedora IoT
page](https://fedoraproject.org/iot/download).

## Why the Fedora IoT Image {#_why_the_fedora_iot_image}

The use of [OSTree](https://ostree.readthedocs.io/en/latest/) brings
fully atomic upgrades, easy rollbacks and workflows that are familiar to
users of immutable, image based servers.

An OS image that is composed on the server side allows for testing the
exact bits before they reach client systems, leading to more reliable
updates. The GPG signed image based deployments scale well to very large
numbers of clients. Updates are atomic so nothing changes until the
device is rebooted and the rollback capability makes it easy to recover
remotely if there is a failure during upgrade.

The Fedora IoT images work with
[rpm-ostree](https://rpm-ostree.readthedocs.io/en/latest/) which is a
hybrid image/package system. It supports package layering, which allows
installation of RPMs for additional hardware support or applications.

The Fedora IoT images also have excellent support for container-focused
workflows. Containers allow you to separate core OS updates from
application updates as well as test and deploy different versions of
applications. The [podman](https://podman.io/) daemon is light weight
and ready for you to download or create containers for your home
assistant, industrial gateways, or data storage and analytics.

## Pick the Right Tool for the Job {#_pick_the_right_tool_for_the_job}

If you are looking for a graphical desktop environment based on OSTree
and designed for developers, look at [Fedora
Silverblue](https://silverblue.fedoraproject.org/).

If you are looking for a traditional dnf based operating system for your
ARM device, visit [Fedora](https://fedoraproject.org/).

If you are looking for a lightweight yet powerful and scalable core OS
for your Internet of Things project, you came to the right place!
[Download the images now](https://fedoraproject.org/iot/download)!

# Building Custom Fedora IoT Images with image-builder {#_building_custom_fedora_iot_images_with_image_builder}

[image-builder](https://github.com/osbuild/image-builder-cli) is a
command-line tool for building custom operating system images for
Fedora, CentOS, and RHEL. This guide explains how to use image-builder
to create customized Fedora IoT images with your own package selections,
user configurations, and settings.

:::: note
::: title
:::

For pre-built Fedora IoT images without customization, see [Obtaining
Images](obtaining-images.xml).
::::

## Installing image-builder {#_installing_image_builder}

To install image-builder on Fedora:

    $ sudo dnf install image-builder ostree

## Available Fedora IoT Image Types {#_available_fedora_iot_image_types}

image-builder supports several IoT-specific image types for x86_64 and
aarch64 architectures:

&#42; &#96;iot-commit&#96; - OSTree commit tarball (the foundation for
custom images) &#42; &#96;iot-installer&#96; - Anaconda installer ISO
for interactive installation &#42; &#96;iot-simplified-installer&#96; -
Zero-touch installer using FDO or Ignition &#42; &#96;iot-raw-xz&#96; -
Compressed raw disk image for physical devices (e.g., Raspberry Pi)
&#42; &#96;iot-qcow2&#96; - QCOW2 disk image for virtual machines &#42;
&#96;iot-container&#96; - OCI container with OSTree commit &#42;
&#96;iot-bootable-container&#96; - Bootable container image

To list all available IoT image types:

    $ image-builder list | grep iot

## Building Custom Fedora IoT Images {#_building_custom_fedora_iot_images}

The typical workflow for creating custom Fedora IoT images is:

1.  Create a blueprint describing your customizations

2.  Build a custom OSTree commit with your changes

3.  Serve the OSTree commit locally

4.  Build installation media or disk images from your custom commit

### Step 1: Creating a Blueprint {#_step_1_creating_a_blueprint}

Blueprints are TOML files that describe customizations for your image.
They allow you to:

&#42; Add or remove packages &#42; Configure users and groups &#42; Set
up SSH keys &#42; Configure system settings

Create a blueprint file (example: &#96;iot-custom.toml&#96;):

    name = 'iot-custom'
    description = 'Custom Fedora IoT Image'
    version = '0.0.1'

    [[packages]]
    name = 'vim-enhanced'

    [[packages]]
    name = 'htop'

    [[packages]]
    name = 'tmux'

    [[customizations.user]]
    name = 'admin'
    description = 'Admin User'
    password = '$6$rounds=4096$saltsalt$encrypted_password_hash'
    groups = ['wheel']

    [[customizations.sshkey]]
    user = 'admin'
    key = 'ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIExample admin@workstation'

:::: note
::: title
:::

Generate encrypted passwords with &#96;openssl passwd -6&#96; (will
prompt for password interactively)
::::

### Step 2: Building a Custom OSTree Commit {#_step_2_building_a_custom_ostree_commit}

Build an OSTree commit tarball with your customizations. Use the
official ref naming pattern (&#96;fedora/stable&#96;,
&#96;fedora/devel&#96;, or &#96;fedora/rawhide&#96;):

    $ sudo image-builder build iot-commit \
    --distro fedora-43 \
    --blueprint iot-custom.toml \
    --ostree-ref fedora/stable/x86_64/iot \
    --output-dir ./iot-commit-output

    \&#35; Note For aarch64 use \&#96;fedora/stable/aarch64/iot\&#96;

This creates a tarball containing your customized OSTree commit.

### Step 3: Setting Up a Local OSTree Repository {#_step_3_setting_up_a_local_ostree_repository}

Extract the commit tarball and serve the OSTree repository:

    $ tar -xf ./iot-commit-output/\&#42;.tar
    $ mv repo ostree-repo
    $ cd ostree-repo
    $ python3 -m http.server 8000

The tarball contains a &#96;repo/&#96; directory with the complete
OSTree repository. To run the HTTP server in the background, add
&#96;&amp;&#96; at the end:

    $ python3 -m http.server 8000 \&amp;

Your custom OSTree repository is now available at
&#96;[http://localhost:8000&#96](http://localhost:8000&#96);

To verify the repository is properly set up:

    $ ostree --repo=./ostree-repo refs
    $ curl http://localhost:8000/refs/heads/fedora/stable/x86_64/iot

## Building Images from Your Custom OSTree {#_building_images_from_your_custom_ostree}

With your custom OSTree commit served locally, you can now build various
image types.

### Building an Installer ISO {#_building_an_installer_iso}

Create an Anaconda installer ISO that will install your customized
Fedora IoT:

    $ sudo image-builder build iot-installer \
    --distro fedora-43 \
    --ostree-url http://localhost:8000 \
    --ostree-ref fedora/stable/x86_64/iot \
    --output-dir ./images

### Building a Simplified Installer {#_building_a_simplified_installer}

The simplified installer provides zero-touch provisioning using FDO or
Ignition:

    $ sudo image-builder build iot-simplified-installer \
    --distro fedora-43 \
    --ostree-url http://localhost:8000 \
    --ostree-ref fedora/stable/x86_64/iot \
    --output-dir ./images

See [Booting the Simplified
Provisioner](booting-the-simplified-provisioner.xml) for more details.

### Building Raw Disk Images {#_building_raw_disk_images}

For single-board computers like Raspberry Pi, create a compressed raw
disk image:

    $ sudo image-builder build iot-raw-xz \
    --distro fedora-43 \
    --arch aarch64 \
    --ostree-url http://localhost:8000 \
    --ostree-ref fedora/stable/aarch64/iot \
    --output-dir ./images

These images can be written directly to SD cards or other storage media.

### Building QCOW2 Images for VMs {#_building_qcow2_images_for_vms}

For testing in virtual machines:

    $ sudo image-builder build iot-qcow2 \
    --distro fedora-43 \
    --ostree-url http://localhost:8000 \
    --ostree-ref fedora/stable/x86_64/iot \
    --output-dir ./images

### Building Container Images {#_building_container_images}

Create an OCI container with your OSTree commit:

    $ sudo image-builder build iot-container \
    --distro fedora-43 \
    --ostree-url http://localhost:8000 \
    --ostree-ref fedora/stable/x86_64/iot \
    --output-dir ./images

Create a bootable container image for modern container-native workflows:

    $ sudo image-builder build iot-bootable-container \
    --distro fedora-43 \
    --ostree-url http://localhost:8000 \
    --ostree-ref fedora/stable/x86_64/iot \
    --output-dir ./images

See [Fedora IoT Bootc](fedora-iot-bootc.xml) for more information on
bootable containers.

## Serving Your OSTree Repository to Other Machines {#_serving_your_ostree_repository_to_other_machines}

To make your custom OSTree repository available to other machines on
your network:

    $ cd ostree-repo
    $ python3 -m http.server 8000 --bind 0.0.0.0 \&amp;

:::: note
::: title
:::

The &#96;&amp;&#96; runs the server in background. To stop it later, use
&#96;pkill -f \'http.server 8000\'&#96;
::::

Then use your machine's IP address when building images on other
systems:

    $ sudo image-builder build iot-installer \
    --distro fedora-43 \
    --ostree-url http://192.168.1.100:8000 \
    --ostree-ref fedora/stable/x86_64/iot \
    --output-dir ./images

## Advanced Options {#_advanced_options}

### Adding Extra Repositories {#_adding_extra_repositories}

Add additional package repositories during the OSTree commit build (not
included in final image):

    $ sudo image-builder build iot-commit \
    --distro fedora-43 \
    --blueprint iot-custom.toml \
    --ostree-ref fedora/stable/x86_64/iot \
    --extra-repo 'https://example.com/repo/fedora/43/x86_64' \
    --output-dir ./iot-commit-output

:::: warning
::: title
:::

Extra repositories are not GPG checked and only used during the commit
build.
::::

### Customizing Output Names {#_customizing_output_names}

Customize the output filename for your images:

    $ sudo image-builder build iot-installer \
    --distro fedora-43 \
    --ostree-url http://localhost:8000 \
    --ostree-ref fedora/stable/x86_64/iot \
    --output-name my-custom-installer \
    --output-dir ./images

### Verbose Output for Debugging {#_verbose_output_for_debugging}

Enable verbose mode to see detailed build information:

    $ sudo image-builder build iot-commit \
    --distro fedora-43 \
    --blueprint iot-custom.toml \
    --ostree-ref fedora/stable/x86_64/iot \
    --verbose \
    --output-dir ./iot-commit-output

### Exporting Build Artifacts {#_exporting_build_artifacts}

Export the OSBuild manifest and build log for troubleshooting:

    $ sudo image-builder build iot-commit \
    --distro fedora-43 \
    --blueprint iot-custom.toml \
    --ostree-ref fedora/stable/x86_64/iot \
    --with-manifest \
    --with-buildlog \
    --output-dir ./iot-commit-output

## Describing Image Types {#_describing_image_types}

To see detailed information about any IoT image type:

    $ image-builder describe iot-installer --distro fedora-43
    $ image-builder describe iot-qcow2 --distro fedora-43 --arch aarch64
    $ image-builder describe iot-simplified-installer --distro fedora-43

This shows the packages, pipelines, and configuration options for each
image type.

## Best Practices {#_best_practices}

1.  &#42;Test with QCOW2 First&#42; - Build and test iot-qcow2 images in
    VMs before creating installation media

2.  &#42;Use Version Control for Blueprints&#42; - Keep blueprint files
    in git to track customizations

3.  &#42;Minimize Package Additions&#42; - Only add essential packages;
    use containers for applications

4.  &#42;Use Encrypted Passwords&#42; - Never use plain text passwords
    in blueprints

5.  &#42;Enable Verbose Mode for Troubleshooting&#42; - Use
    &#96;\--verbose&#96; when debugging build issues

## Troubleshooting {#_troubleshooting}

### Build Fails with OSTree Errors {#_build_fails_with_ostree_errors}

Verify your local OSTree repository is properly set up and the ref
exists:

    $ ostree --repo=./ostree-repo refs
    $ ostree --repo=./ostree-repo show fedora/stable/x86_64/iot

Ensure your HTTP server is running and accessible:

    $ curl http://localhost:8000/config
    $ curl http://localhost:8000/refs/heads/fedora/stable/x86_64/iot

### Permission Denied Errors {#_permission_denied_errors}

Most image-builder operations require root privileges:

    $ sudo image-builder build iot-installer \&#8230;

### Insufficient Disk Space {#_insufficient_disk_space}

Building images requires significant disk space. Ensure at least 10GB
free in:

&#42; &#96;/var/cache/image-builder/&#96; (build cache) &#42; Output
directory

Clear cache if needed:

    $ sudo rm -rf /var/cache/image-builder/store/\&#42;

## Additional Resources {#_additional_resources}

&#42; [Obtaining Images](obtaining-images.xml) - Download pre-built
Fedora IoT images &#42; [Booting the Simplified
Provisioner](booting-the-simplified-provisioner.xml) - Using simplified
installer &#42; [Fedora IoT Bootc](fedora-iot-bootc.xml) - Bootable
container workflows &#42; [image-builder
CLI](https://github.com/osbuild/image-builder-cli) - Source code,
documentation, and issue tracker &#42; [OSBuild Project
Documentation](https://www.osbuild.org/) &#42; [OSTree
Documentation](https://ostreedev.github.io/ostree/)

# Setting up a Virtual Machine {#_setting_up_a_virtual_machine}

## Enable UEFI support for KVM virtual machines {#_enable_uefi_support_for_kvm_virtual_machines}

Fedora IoT requires UEFI, take a look at this wiki page on how to make
it available for your VM:
<https://docs.fedoraproject.org/en-US/quick-docs/uefi-with-qemu/>

Once everything's set, make sure you enable UEFI for the new VM:

- If using virt-install, add the &#96;\--boot uefi&#96; flag

- If using Virtual Machine Manager, check &#96;Customize configuration
  before install&#96; before finishing the initial setup -&gt; Overview
  -&gt; Firmware: UEFI -&gt; Begin Installation

- If using plain &#96;qemu-kvm&#96; make sure to point the
  &#96;-bios&#96; flag to the OVMF binary

## Setup with QEMU/KVM Tools {#_setup_with_qemukvm_tools}

The images generated are compressed raw disk images. They can be
utilized both on physical devices and used as disks on a virtualization
platform. The images work without change on QEMU/KVM.

On QEMU/KVM the tools that can be used to run the image in a VM include
[Virtual Machine Manager](http://virt-manager.org/) or &#96;virsh&#96;
command line utility. These tools are available in most Linux
distributions.

Decompress the image as below and then choose an option to import
virtual machine.

    $ xz -d Fedora-IoT-[version].raw.xz

:::: tip
::: title
:::

If using iso image, choose the option to create virtual machine and
follow the installation steps.
::::

When asked for an installation source or storage location, point to the
downloaded disk image.

![virt-manager create new dialog](virt-manager-create_new-20190204.png)

As your image begins booting, continue with the
[Ignition](ignition-device-setup.xml) instructions.

To learn more about the libvirt family of tools used in Fedora, visit
the [Getting started with
virtualization](https://docs.fedoraproject.org/en-US/quick-docs/getting-started-with-virtualization/)
section of the Fedora Documentation.

QEMU (on Linux hosts only) also supports user mode emulation. In this
mode, QEMU can launch Linux processes compiled for one CPU on another
CPU. Learn more in the [How to use
QEMU](https://docs.fedoraproject.org/en-US/quick-docs/qemu/) section of
the Fedora Documentation.

## Setup with virt-install {#_setup_with_virt_install}

For fast iterations on the raw image, you can use
&#96;virt-install&#96;:

    $ xz -d Fedora-IoT-[version].raw.xz
    $ qemu-img convert -f raw Fedora-IoT-[version].raw -O qcow2 Fedora-IoT-[version].qcow2
    $ virt-install --name FedoraIoT --memory 2048 --vcpus 2 --boot uefi \
    --disk /path/to/Fedora-IoT-[version].qcow2 \
    --import --os-variant fedora[version]

## Setup with GNOME Boxes {#_setup_with_gnome_boxes}

While GNOME Boxes is based on &#96;libvirt&#96;, it does not support all
of the features and it does not recognize the raw image format. The
images we produce need to be converted to to a QCOW2 format. This can be
done with the &#96;qemu-img&#96; command found in the &#96;qemu-img&#96;
package.

Decompress and convert the image as below and then create a new virtual
machine.

    $ xz -d Fedora-IoT-[version].raw.xz
    $ qemu-img convert -f raw Fedora-IoT-[version].raw -O qcow2 Fedora-IoT-[version].qcow2

When asked for an installation source or storage location, point the
tool at the existing disk image.

![GNOME Boxes create new dialog](new-box-dialog-20190204.png)

As your image begins booting, continue with the
[Ignition](ignition-device-setup.xml) instructions.

Alternately, you can install a new box from the ISO image.

![GNOME Boxes New Virtual Machine](gnome-boxes-install-00.png)

When installing from the ISO image, after selecting the ISO from your
filesystem, you'll see that the Operating System has not been found.

![GNOME Boxes Selecting Fedora](gnome-boxes-install-01.png)

To continue with the installation, type \'Fedora\' in the \'Search for
an operating system&#8230;\' box and select the \'Fedora\' option.

![GNOME Boxes Selecting UEFI](gnome-boxes-install-02.png)

Once the Fedora Operating System option has been selected, an option to
select the Firmware type will appear, select \'UEFI\' and continue with
the Virtual Machine creation.

More information on using GNOME Boxes can be found in the [GNOME
HELP](https://help.gnome.org/users/gnome-boxes/stable/index.html.en)
pages.

## Setup with VirtualBox {#_setup_with_virtualbox}

The images we produce need to be converted to be used with VirtualBox.
This can be done with the &#96;qemu-img&#96; command found in the
&#96;qemu-img&#96; package.

Decompress and convert the image as below and then create a new virtual
machine.

    $ xz -d Fedora-IoT-[version].raw.xz
    $ qemu-img convert -f raw Fedora-IoT-[version].raw -O vdi Fedora-IoT-[version].vdi

When asked for an installation source or storage location, point the
tool at the existing disk image.

![VirtualBox create new hard disk
dialog](virtualbox-new-dialog-20190204.png)

As your image begins booting, continue with the
[Ignition](ignition-device-setup.xml) instructions.

More information for using Virtual Box can be found at
[VirtualBox.org](https://www.virtualbox.org/)

# Setting up a Physical Device {#_setting_up_a_physical_device}

## Gather the Physical Components {#_gather_the_physical_components}

A list of currently tested devices is maintained in the [Reference
Platforms](reference-platforms.xml) page.

Always reference the documentation of the board you have selected for
assembly instructions and requirements. At a minimum you will need the
board, a power source, and a microSD card.

### Network connection {#_network_connection}

If support for your wireless network devices are not available in the
Fedora image, it will have to be added after installation. You will need
a wired connection to complete the install of the [layered
package](add-layered.xml).

For the Fedora disk images:

&#42; The Raspberry Pi WiFi is supported in the base image.

### SD Card {#_sd_card}

The Fedora IoT image is currently 4GB in size. The best speed class
depends on the usage. A faster speed class is better for writes but the
trade off is slower read speed.

Documentation for your board may also recommend specific SD Card choices
as well as required physical sizes for each device.

&#42; Raspberry Pi discusses card size and speed class in their [SD Card
Documentation](https://www.raspberrypi.org/documentation/installation/sd-cards.md).

:::: warning
::: title
:::

The following procedures will overwrite everything on the micro SD card.
Be sure to backup any data before continuing!
::::

## Create a Bootable SD Card {#_create_a_bootable_sd_card}

If you have not already [downloaded the image](obtaining-images.xml), do
so now and make a note of the download location and filename.

### Determine the SD Card Device name {#_determine_the_sd_card_device_name}

There are several options for determining the media device name.

&#42; Run the &#96;lsblk&#96; command before and after inserting the
card. The new device that appears on the list is the device for the
media. If your microSD card has partitions, locate the name from the
line that is type \'disk\'. In this example the device name is
&#96;mmcblk0&#96; and will be referenced later as
&#96;/dev/mmcblk0&#96;:

    $ lsblk
    NAME            MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
    mmcblk0         179:0    0  14.9G  0 disk
    ├─mmcblk0p1     179:1    0   142M  0 part /run/media/user/22DA-CAE8
    ├─mmcblk0p2     179:2    0     1G  0 part /run/media/user/8b87a5af-12c7-4990-940e-5b457336b11f
    └─mmcblk0p3     179:3    0   2.9G  0 part /run/media/user/cce2e189-9aee-4b3e-b031-aac9bdc632c9
    \&#8230;output omitted\&#8230;

&#42; If you have the &#96;udisks2&#96; package installed you may find
the &#96;udisksctl&#96; command helpful in determining the media device
name. It will show the model and only the device name without the extra
partition information. In this example, a 16GB SanDisk Ultra shows as
\'SL16G\':

    $ udisksctl status
    MODEL                     REVISION  SERIAL               DEVICE
    ----------------------------------------------------
    SAMSUNG MZSLW1T0HMLH-000L1           S308NAAH501124       nvme0n1
    SL16G                               0x51821336           mmcblk0

&#42; Finally, the kernel messages will show the addition of a device.
In a terminal window before inserting the device run:

    $ dmesg -w

### Scripted image transfer with &#96;arm-image-installer&#96; {#_scripted_image_transfer_with_96arm_image_installer96}

&lt;&lt;arm-image-installer&gt;&gt; Install the
&#96;arm-image-installer&#96; package:

    $ sudo dnf install arm-image-installer

Display the usage for the utility. This will display an example command:

    $ sudo arm-image-installer

    Usage: arm-image-installer \&lt;options\&gt;

    --image=IMAGE   - xz compressed image file name
    --media=DEVICE  - media device file (/dev/[sdX|mmcblkX])
    Optional
    --addconsole    - Add system console kernel parameter for the target
    --addkey        - /path/to/ssh-public-key
    --args          - Optional kernel parameters listed in quotes
    --norootpass    - Remove the root password
    --relabel       - SELinux relabel root filesystem on first boot
    --resizefs      - Resize root filesystem to fill media device
    --sysrq     - Enable System Request debugging of the kernel
    --target=TARGET - target board for uboot
    -y      - Assumes yes, will not wait for confirmation
    Help
    --supported     - List of supported hardware
    --version       - Display version and exit

    Example: arm-image-installer --image=Fedora-Rawhide.xz --target=Bananapi --media=/dev/mmcblk0

For the Raspberry Pi Model 3 B/B+ use:

    --target=rpi3

Provide the correct path for the downloaded image and the microSD media.
Replace &#96;XXX&#96; with the location of your media. It will be
&#96;sdX&#96; or &#96;mmcblkX&#96; depending on hardware:

    $ sudo arm-image-installer --image=Fedora-IoT-[version].raw.xz --target=rpi3 --media=/dev/XXX

Other options of interest:

&#42; The &#96;\--addkey=&#96; option will place a specified ssh public
key into the &#96;/root/authorized_keys&#96; file (the option expects
the path to the key). &#42; The &#96;\--resizefs&#96; options will
expand the &#96;/sysroot&#96; partition to use all remaining space on
the microSD card.

### Manual Image Transfer with &#96;dd&#96; {#_manual_image_transfer_with_96dd96}

Replace &#96;XXX&#96; with the location of your media. It will be
&#96;sdX&#96; or &#96;mmcblkX&#96; depending on hardware.

    xzcat Fedora-IoT-[version].raw.xz | sudo dd status=progress bs=4M of=/dev/XXX

## Configure a Serial Console (Optional) {#_configure_a_serial_console_optional}

If you wish to use a serial console you'll need to configure it. Details
for the [Raspberry PI are
here](https://fedoraproject.org/wiki/Architectures/ARM/Raspberry_Pi?rd=Raspberry_Pi&#35;How_do_I_use_a_serial_console.3F).

## Setup a device by using Ignition and a Raw disk image {#_setup_a_device_by_using_ignition_and_a_raw_disk_image}

### Prerequisites {#_prerequisites}

&#42; You have [created an Ignition configuration
file](creating-an-ignition-configuration-file.xml) and is accessible via
HTTP/HTTPS. &#42; You have downloaded a [Raw disk
image](https://fedoraproject.org/iot/download) and copied to media for
your device.

### Edit the boot parameters {#_edit_the_boot_parameters}

As the device boots, edit the kernel args and add the url to your
ignition config, for example:
&#96;ignition.config.url=http://192.168.122.1/fiot.ign&#96;

## Setup a device by using Ignition and the Simplified Provisioner {#_setup_a_device_by_using_ignition_and_the_simplified_provisioner}

### Prerequisites {#_prerequisites_2}

&#42; You have [created an Ignition configuration
file](creating-an-ignition-configuration-file.xml) and is accessible via
HTTP/HTTPS. &#42; You have downloaded the [Simplified Provisioner ISO
image](https://fedoraproject.org/iot/download) and booted the device
from it by using one of the methods described in [Booting the Simplified
Provisioner](booting-the-simplified-provisioner.xml).

### Edit the boot parameters {#_edit_the_boot_parameters_2}

Once device has been booted from the Simplified Provisioner the boot
menu shows the following options:

\\.... Install Fedora {FedoraVersion} Test this media \\& install Fedora
{FedoraVersion} Troubleshooting \--\\\> \\....

&#42; Select &#42;\'Install Fedora {FedoraVersion}\'&#42; and press the
&#42;\'\[e\]\'&#42; key to edit the menu entry. &#42; Make sure the
installation device variable (&#96;coreos.inst.install_dev&#96;) is
correct and append the ignition parameters (e.g.:
&#96;{SimplifiedProvisionerKernelIgnitionConfigURL}
{SimplifiedProvisionerKernelRdNeedNet}&#96;) to the &#96;linux&#96; line
if not present (e.g.:):

\+

\\.... \\#\\#\\# BEGIN /etc/grub.d/10_linux \\#\\#\\# menuentry
\'Install Fedora {FedoraVersion}\' \--class fedora \--class gnu-linux
\--class gnu \--class os { linux images/pxeboot/vmlinuz rd.neednet=1
coreos.inst.crypt_root=1
coreos.inst.isoroot=Fedora-{FedoraVersion}-IoT-x86_64
coreos.inst.install_dev=/dev/vda
coreos.inst.image_file=/run/media/iso/image.raw.xz coreos.inst.insecure
quiet {SimplifiedProvisionerKernelIgnitionConfigURL}
{SimplifiedProvisionerKernelRdNeedNet} initrd images/pxeboot/initrd.img
} \\.... \\\* Boot the menu entry by pressing \\\*\'\[Ctrl-x\]\'\\\* to
boot and install the IoT device

## Verifying the installation {#_verifying_the_installation}

Once the installation has finished and the device has rebooted you
should be able to login with the user configured within the ignition
file:

\\.... ssh core@{DefaultIoTDeviceIP} \\....

# Setup a device by using FDO and the Simplified Provisioner {#_setup_a_device_by_using_fdo_and_the_simplified_provisioner}

## Prerequisites {#_prerequisites_3}

&#42; You have installed and configured the FDO services as described
in: &#42;&#42; [Installing and configuring the Manufacturing
server](fdo-installing-the-manufacturing-server-package.xml) &#42;&#42;
[Installing and configuring the Rendezvous
Server](fdo-installing-configuring-and-running-the-rendezvous-server.xml)
&#42;&#42; [Installing and configuring the Owner's Onboarding
Server](fdo-installing-configuring-and-running-the-owner-server.xml)
&#42; If using libvirt make sure the FDO server ports are reachable from
the VMs

\+

\\.... \\# firewall-cmd \--zone libvirt \\
\--add-port={ManufacturingServerPort}/tcp \\
\--add-port={OwnerOnboardingServerPort}/tcp \\
\--add-port={RendezvousServerPort}/tcp \\ \--permanent \\# systemctl
restart firewalld \\.... \\\* You have downloaded the
link:https://fedoraproject.org/iot/download\[Simplified Provisioner ISO
image\] and booted the device from it by using one of the methods
described in xref:booting-the-simplified-provisioner.adoc\[Booting the
Simplified Provisioner\].

## Edit the boot parameters {#_edit_the_boot_parameters_3}

Once device has been booted from the Simplified Provisioner the boot
menu shows the following options:

\\.... Install Fedora {FedoraVersion} Test this media \\& install Fedora
{FedoraVersion} Troubleshooting \--\\\> \\....

&#42; Select &#42;\'Install Fedora {FedoraVersion}\'&#42; and press the
&#42;\'\[e\]\'&#42; key to edit the menu entry. &#42; Make sure the
installation device variable (&#96;coreos.inst.install_dev&#96;) is
correct and append the manufacturing parameters
(&#96;fdo.manufacturing_server_url=http://{ManufacturingServerIP}:{ManufacturingServerPort}
fdo.diun_pub_key_insecure=true&#96;) to the &#96;linux&#96; line if not
present:

\+

\\.... \\#\\#\\# BEGIN /etc/grub.d/10_linux \\#\\#\\# menuentry
\'Install Fedora {FedoraVersion}\' \--class fedora \--class gnu-linux
\--class gnu \--class os { linux images/pxeboot/vmlinuz rd.neednet=1
coreos.inst.crypt_root=1
coreos.inst.isoroot=Fedora-{FedoraVersion}-IoT-x86_64
coreos.inst.install_dev=/dev/vda
coreos.inst.image_file=/run/media/iso/image.raw.xz coreos.inst.insecure
quiet
fdo.manufacturing_server_url=http://{ManufacturingServerIP}:{ManufacturingServerPort}
fdo.diun_pub_key_insecure=true initrd images/pxeboot/initrd.img } \\....
\\\* Boot the menu entry by pressing \\\*\'\[Ctrl-x\]\'\\\* \\\* Once
the IoT device has been installed and performed the manufacturing
process it will reboot and perform the FDO Onboarding in the next boot.

## Verifying the Onboarding {#_verifying_the_onboarding}

If the onboarding finished successfully you sould be able to login with
the initial user configured in the Service Info API server.

When using libvirt in the same host where the FDO services are running
you can use the following command to connect to the VM:

\\.... \\#! /bin/bash

export LIBVIRT_DEFAULT_URI=qemu:///system export
LIBVIRT_DOMAIN_NAME={VMName} export LIBVIRT_NETWORK=default

MAC=\$(virsh domiflist \'\${LIBVIRT_DOMAIN_NAME}\' \| grep
\'\${LIBVIRT_NETWORK}\' \| awk \'{print \$5}\') IP=\$(virsh
net-dhcp-leases \'\${LIBVIRT_NETWORK}\'\| grep \'\${MAC}\' \| awk
\'{print \$5}\'\| cut -f1 -d/) ssh admin@\${IP} &#8230;.

# The FIDO Device Onboarding (FDO) process {#_the_fido_device_onboarding_fdo_process}

The FIDO Device Onboarding (FDO) is the process that:

&#42; Provisions and onboards a device. &#42; Automatically configures
credentials for this device. The FDO process is an automatic onboarding
mechanism that is triggered by the installation of a new device. &#42;
Enables this device to securely connect and interact on the network.

With FIDO Device Onboarding (FDO), you can perform a secure device
onboarding by adding new devices into your IoT architecture. This
includes the specified device configuration that needs to be trusted and
integrated with the rest of the running systems. The FDO process is an
automatic onboarding mechanism that is triggered by the installation of
a new device.

The FDO protocol performs the following tasks:

&#42; Solves the trust and chain of ownership along with the automation
needed to securely onboard a device at scale. &#42; Performs device
initialization at the manufacturing stage and late device binding for
its actual use. This means that actual binding of the device to a
management system happens on the first boot of the device without
requiring manual configuration on the device. &#42; Supports automated
secure devices onboarding, that is, zero touch installation and
onboarding that does not need any specialized person at the edge
location. After the device is onboarded, the management platform can
connect to it and apply patches, updates, and rollbacks.

With FDO, you can benefit from the following:

&#42; FDO is a secure and simple way to enroll a device to a management
platform. Instead of embedding a Kickstart configuration to the image,
FDO applies the device credentials during the device first boot directly
to the ISO image. &#42; FDO solves the issue of late binding to a
device, enabling any sensitive data to be shared over a secure FDO
channel. &#42; FDO cryptographically identifies the system identity and
ownership before enrolling and passing the configuration and other
secrets to the system. That enables non-technical users to power-on the
system.

To build a Fedora IoT Simplified Provisioner image and automatically
onboard it, provide an existing OSTree commit. The resulting simplified
image contains a raw image that has the OSTree commit deployed. After
you boot the Simplified installer ISO image, it provisions a Fedora IoT
system that you can use on a hard disk or as a boot image in a virtual
machine.

The Fedora IoT Simplified Provisioner image is optimized for unattended
installation to a device and supports both network-based deployment and
non-network-based deployments. However, for network-based deployment, it
supports only UEFI HTTP boot.

The FDO protocol is based on the following servers:

Manufacturing server

:   1.  Generates the device credentials.

    2.  Creates an Ownership voucher that is used to set the ownership
        of the device, later in the process.

    3.  Binds the device to a specific management platform.

Owner management system

:   1.  Receives the Ownership voucher from the Manufacturing server and
        becomes the owner of the associated device.

    2.  Later in the process, it creates a secure channel between the
        device and the owner onboarding server after the device
        authentication.

    3.  Uses the secure channel to send the required information, such
        as files and scripts for the onboarding automation to the
        device.

Service-info API server

:   Based on Service-info API server's configuration and modules
    available on the client, it performs the final steps of onboarding
    on target client devices, such as copying SSH keys and files,
    executing commands, creating users, encrypting disks and so on

Rendezvous server

:   1.  Gets the Ownership voucher from the Owner management system and
        makes a mapping of the device UUID to the Owner server IP. Then,
        the Rendezvous server matches the device UUID with a target
        platform and informs the device about which Owner onboarding
        server endpoint this device must use.

    2.  During the first boot, the Rendezvous server will be the contact
        point for the device and it will direct the device to the owner,
        so that the device and the owner can establish a secure channel.

Device client

:   This is installed on the device. The Device client performs the
    following actions:

    1.  Starts the queries to the multiple servers where the onboarding
        automation will be executed.

    2.  Uses TCP/IP protocols to communicate with the servers.

The following diagram represents the FIDO device onboarding workflow:
.Deploying Fedora IoT in non-network environment

![FDO device onboarding](FDO_Process.png)

At the &#42;Device Initialization&#42;, the device contacts the
Manufacturing server to get the FDO credentials, a set of certificates
and keys to be installed on the operating system with the Rendezvous
server endpoint (URL). It also gets the Ownership Voucher, that is
maintained separately in case you need to change the owner assignment.

1.  The Device contacts the Manufacturing server

2.  The Manufacturing server generates an Ownership Voucher and the
    Device Credentials for the Device.

3.  The Ownership Voucher is transferred to the Owner onboarding server.

At the &#42;On-site onboarding&#42;, the Device gets the Rendezvous
server endpoint (URL) from its device credentials and contacts
Rendezvous server endpoint to start the onboarding process, which will
redirect it to the Owner management system, that is formed by the Owner
onboarding server and the Service Info API server.

1.  The Owner onboarding server transfers the Ownership Voucher to the
    Rendezvous server, which makes a mapping of the Ownership Voucher to
    the Owner.

2.  The device client reads device credentials.

3.  The device client connects to the network.

4.  After connecting to the network, the Device client contacts the
    Rendezvous server.

5.  The Rendezvous server sends the owner endpoint URL to the Device
    Client, and registers the device.

6.  The Device client connects to the Owner onboarding server shared by
    the Rendezvous server.

7.  The Device proves that it is the correct device by signing a
    statement with a device key.

8.  The Owner onboarding server proves itself correct by signing a
    statement with the last key of the Owner Voucher.

9.  The Owner onboarding server transfers the information of the Device
    to the Service Info API server.

10. The Service info API server sends the configuration for the Device.

11. The Device is onboarded.

# Generating key and certificates {#_generating_key_and_certificates}

To run the FIDO Device Onboarding (FDO) infrastructure, you need to
generate keys and certificates. FDO generates these keys and
certificates to configure the manufacturing server. FDO automatically
generates the certificates and &#96;.yaml&#96; configuration files when
you install the services, and re-creating them is optional. After you
install and start the services, it runs with the default settings.

:::: formalpara
::: title
Prerequisites
:::

&#42; You installed the &#96;fdo-admin-cli&#96; RPM package
::::

<div>

::: title
Procedure
:::

1.  Generate the keys and certificates in the &#96;/etc/fdo&#96;
    directory:

        $ for i in 'diun' 'manufacturer' 'device-ca' 'owner'; do
        fdo-admin-tool generate-key-and-cert $i;
        done

2.  Check the key and certificates that were created in the
    &#96;/etc/fdo/keys&#96; directory:

        $ tree keys

    You can see the following output:

        keys/
        ├── device_ca_cert.pem
        ├── device_ca_key.der
        ├── diun_cert.pem
        ├── diun_key.der
        ├── manufacturer_cert.pem
        ├── manufacturer_key.der
        ├── owner_cert.pem
        └── owner_key.der

</div>

:::: formalpara
::: title
Additional resources
:::

&#42; See the &#96;fdo-admin-tool generate-key-and-cert ---help&#96;
manual page
::::

# Installing and running the manufacturing server {#_installing_and_running_the_manufacturing_server}

The &#96;fdo-manufacturing-server&#96; RPM package enables you to run
the Manufacturing Server component of the FDO protocol. It also stores
other components, such as the owner vouchers, the manufacturer keys, and
information about the manufacturing sessions. During the device
installation, the Manufacturing server generates the device credentials
for the specific device, including its GUID, rendezvous information and
other metadata. Later on in the process, the device uses this rendezvous
information to contact the Rendezvous server.

To install the &#96;manufacturing server&#96; RPM package, complete the
following steps:

<div>

::: title
Procedure
:::

1.  Install the &#96;fdo-admin-cli&#96; package:

        \# dnf install -y fdo-admin-cli

2.  Check if the &#96;fdo-manufacturing-server&#96; RPM package is
    installed:

        $ rpm -qa | grep fdo-manufacturing-server --refresh

3.  Check if the files were correctly installed:

        $ ls /usr/share/doc/fdo

    You can see the following output:

        manufacturing-server.yml
        owner-onboarding-server.yml
        rendezvous-info.yml
        rendezvous-server.yml
        serviceinfo-api-server.yml

4.  Optional: Check the content of each file, for example:

        $ cat /usr/share/doc/fdo/manufacturing-server.yml

5.  Configure the Manufacturing server. You must provide the following
    information:

</div>

&#42; The Manufacturing server URL &#42; The IP address or DNS name for
the Rendezvous server &#42; The path to the keys and certificates you
generated. See [Generating key and
certificates](fdo-generating-key-and-certificates.xml).

\+ You can find an example of a Manufacturing server configuration file
in the &#96;/usr/share/doc/fdo/manufacturing-server.yml&#96; directory.
The following is a &#96;manufacturing server.yml&#96; example that is
created and saved in the &#96;/etc/fdo&#96; directory. It contains paths
to the directories, certificates, keys that you created, the Rendezvous
server IP address and the default port.

\+

    session_store_driver:
    Directory:
    path: /etc/fdo/stores/manufacturing_sessions/
    ownership_voucher_store_driver:
    Directory:
    path: /etc/fdo/stores/owner_vouchers
    public_key_store_driver:
    Directory:
    path: /etc/fdo/stores/manufacturer_keys
    bind: '0.0.0.0:{ManufacturingServerPort}'
    protocols:
    plain_di: false
    diun:
    mfg_string_type: SerialNumber
    key_type: SECP384R1
    allowed_key_storage_types:
    - Tpm
    - FileSystem
    key_path: /etc/fdo/keys/diun_key.der
    cert_path: /etc/fdo/keys/diun_cert.pem
    rendezvous_info:
    - deviceport: {RendezvousServerPort}
    ip_address: {RendezvousServerIP}
    ownerport: {RendezvousServerPort}
    protocol: http
    manufacturing:
    manufacturer_cert_path: /etc/fdo/keys/manufacturer_cert.pem
    device_cert_ca_private_key: /etc/fdo/keys/device_ca_key.der
    device_cert_ca_chain: /etc/fdo/keys/device_ca_cert.pem
    owner_cert_path: /etc/fdo/keys/owner_cert.pem
    manufacturer_private_key: /etc/fdo/keys/manufacturer_key.der

1.  Start the Manufacturing server.

    a.  Check if the systemd unit file are in the server:

            \# systemctl list-unit-files | grep fdo | grep manufacturing
            fdo-manufacturing-server.service disabled disabled

    b.  Enable and start the manufacturing server.

            \# systemctl enable --now fdo-manufacturing-server.service

    c.  Open the default ports in your firewall:

            \# firewall-cmd --add-port={ManufacturingServerPort}/tcp --permanent
            \# systemctl restart firewalld

    d.  Ensure that the service is listening on the port 8080:

            \# ss -ltn

2.  Install Fedora IoT onto your system using the Simplified
    Provisioner. See [Setting up a Device with
    FDO](fdo-device-setup.xml).

:::: formalpara
::: title
Additional resources
:::

&#42; The [manufacturing-server.yml
example](https://github.com/fedora-iot/fido-device-onboard-rs/blob/main/examples/config/manufacturing-server.yml)
&#42; [FIDO device onboarding glossary](fdo-glossary.xml)
::::

# Installing, configuring, and running the Rendezvous server {#_installing_configuring_and_running_the_rendezvous_server}

Install the &#96;fdo-rendezvous-server&#96; RPM package to enable the
systems to receive the voucher generated by the Manufacturing server
during the first device boot. The Rendezvous server then matches the
device UUID with the target platform or cloud and informs the device
about which Owner server endpoint the device must use.

:::: formalpara
::: title
Prerequisites
:::

&#42; You created a &#96;manufacturer_cert.pem&#96; certificate. See
[Generating key and
certificates](fdo-generating-key-and-certificates.xml). &#42; You copied
the &#96;manufacturer_cert.pem&#96; certificate to the
&#96;/etc/fdo/keys&#96; directory in the Rendezvous server.
::::

<div>

::: title
Procedure
:::

1.  Install the &#96;fdo-rendezvous-server&#96; RPM packages:

        \&#35; dnf install -y fdo-rendezvous-server

2.  Create the &#96;rendezvous-server.yml&#96; configuration file,
    including the path to the manufacturer certificate. You can find an
    example in &#96;/usr/share/doc/fdo/rendezvous-server.yml&#96;. The
    following example shows a configuration file that is saved in
    &#96;/etc/fdo/rendezvous-server.yml&#96;.

        storage_driver:
        Directory:
        path: /etc/fdo/stores/rendezvous_registered
        session_store_driver:
        Directory:
        path: /etc/fdo/stores/rendezvous_sessions
        trusted_manufacturer_keys_path: /etc/fdo/keys/manufacturer_cert.pem
        max_wait_seconds: ~
        bind: '0.0.0.0:8082'

3.  Check the Rendezvous server service status:

        \&#35; systemctl list-unit-files | grep fdo | grep rende
        fdo-rendezvous-server.service disabled disabled

    a.  If the service is stopped and disabled, enable and start it:

            \&#35; systemctl enable --now fdo-rendezvous-server.service

4.  Check that the server is listening on the default configured port
    8082:

        \&#35; ss -ltn

5.  Open the port if you have a firewall configured on this server:

        \&#35; firewall-cmd --add-port=8082/tcp --permanent
        \&#35; systemctl restart firewalld

</div>

# Installing, configuring, and running the Owner server {#_installing_configuring_and_running_the_owner_server}

Install the &#96;fdo-owner-cli&#96; and
&#96;fdo-owner-onboarding-server&#96; RPM package to enable the systems
to receive the voucher generated by the Manufacturing server during the
first device boot. The Rendezvous server then matches the device UUID
with the target platform or cloud and informs the device about which
Owner server endpoint the device must use.

:::: formalpara
::: title
Prerequisites
:::

&#42; The device where the server will be deployed has a Trusted
Platform Module (TPM) device to encrypt the disk. If not, you will get
an error when booting the Fedora IoT device. &#42; You created the
&#96;device_ca_cert.pem&#96;, &#96;owner_key.der&#96;, and
&#96;owner_cert.pem&#96; with keys and certificates and copied them into
the &#96;/etc/fdo/keys&#96; directory.
::::

<div>

::: title
Procedure
:::

1.  Install the required RPMs in this server:

        \# dnf install -y fdo-owner-cli fdo-owner-onboarding-server

2.  Prepare the &#96;owner-onboarding-server.yml&#96; configuration file
    and save it to the &#96;/etc/fdo/&#96; directory. Include the path
    to the certificates you already copied and information about where
    to publish the Owner server service in this file.

    The following is an example available in
    &#96;/usr/share/doc/fdo/owner-onboarding-server.yml&#96;. You can
    find references to the Service Info API, such as the URL or the
    authentication token.

        ---
        ownership_voucher_store_driver:
        Directory:
        path: /etc/fdo/stores/owner_vouchers
        session_store_driver:
        Directory:
        path: /etc/fdo/stores/owner_onboarding_sessions
        trusted_device_keys_path: /etc/fdo/keys/device_ca_cert.pem
        owner_private_key_path: /etc/fdo/keys/owner_key.der
        owner_public_key_path: /etc/fdo/keys/owner_cert.pem
        bind: '0.0.0.0:{OwnerOnboardingServerPort}'
        service_info_api_url: 'http://{ServiceInfoServerIP}:{ServiceInfoServerPort}/device_info'
        service_info_api_authentication:
        BearerToken:
        token: Kpt5P/5flBkaiNSvDYS3cEdBQXJn2Zv9n1D50431/lo=
        owner_addresses:
        - transport: http
        addresses:
        - ip_address: {OwnerOnboardingServerIP}
        port: {OwnerOnboardingServerPort}

3.  Create and configure the Service Info API.

    a.  Add the automated information for onboarding, such as user
        creation, files to be copied or created, commands to be
        executed, disk to be encrypted, and so on. Use the Service Info
        API configuration file example in
        &#96;/usr/share/doc/fdo/serviceinfo-api-server.yml&#96; as a
        template to create the configuration file under
        &#96;/etc/fdo/&#96;.

            ---
            service_info:
            initial_user:
            username: admin
            sshkeys:
            - 'ssh-rsa AAAA\….'
            diskencryption_clevis:
            - disk_label: /dev/vda3
            binding:
            pin: tpm2
            config: '{}'
            reencrypt: true
            bind: '0.0.0.0:{ServiceInfoServerPort}'
            device_specific_store_driver:
            Directory:
            path: /etc/fdo/stores/serviceinfo_api_devices
            service_info_auth_token: Kpt5P/5flBkaiNSvDYS3cEdBQXJn2Zv9n1D50431/lo=
            admin_auth_token: zJNoErq7aa0RusJ1w0tkTjdITdMCWYkndzVv7F0V42Q=

4.  Check the status of the systemd units:

        \# systemctl list-unit-files | grep fdo
        fdo-owner-onboarding-server.service        disabled        disabled
        fdo-serviceinfo-api-server.service         disabled        disabled

    a.  If the service is stopped and disabled, enable and start it:

            \# systemctl enable --now fdo-owner-onboarding-server.service
            \# systemctl enable --now fdo-serviceinfo-api-server.service

        :::: note
        ::: title
        :::

        You must restart the &#96;systemd&#96; services every time you
        change the configuration files.
        ::::

5.  Check that the server is listening on the default configured port
    8083:

        \# ss -ltn

6.  Open the port if you have a firewall configured on this server:

        \# firewall-cmd --add-port={OwnerOnboardingServerPort}/tcp --permanent
        \# firewall-cmd --add-port={ServiceInfoServerPort}/tcp --permanent
        \# systemctl restart firewalld

</div>

# FIDO device onboarding glossary {#_fido_device_onboarding_glossary}

Learn more about the FIDO device onboarding terminology.

+-----------------------------------+-----------------------------------+
| Term                              | Description                       |
+===================================+===================================+
| FDO                               | FIDO Device Onboarding.           |
+-----------------------------------+-----------------------------------+
| Device                            | Any hardware, device, or          |
|                                   | computer.                         |
+-----------------------------------+-----------------------------------+
| Device Credential (DC)            | Key credential and rendezvous     |
|                                   | stored in the device at           |
|                                   | manufacture.                      |
+-----------------------------------+-----------------------------------+
| Keys                              | Keys to configure the             |
|                                   | manufacturing server              |
|                                   |                                   |
|                                   | &#42; key_path                    |
|                                   |                                   |
|                                   | &#42; cert_path                   |
|                                   |                                   |
|                                   | &#42; key_type                    |
|                                   |                                   |
|                                   | &#42; mfg_string_type: device     |
|                                   | serial number                     |
|                                   |                                   |
|                                   | &#42; allowed_key_storage_types:  |
|                                   | Filesystem and Trusted Platform   |
|                                   | Module (TPM) that protects the    |
|                                   | data used to authenticate the     |
|                                   | device you are using.             |
+-----------------------------------+-----------------------------------+
| Manufacturer                      | The device manufacturer.          |
+-----------------------------------+-----------------------------------+
| Manufacturer server               | Creates the device credentials    |
|                                   | for the device.                   |
+-----------------------------------+-----------------------------------+
| Manufacturer client               | Informs the location of the       |
|                                   | manufacturing server.             |
+-----------------------------------+-----------------------------------+
| Owner                             | The final owner of the device - a |
|                                   | company or an IT department.      |
+-----------------------------------+-----------------------------------+
| Ownership Voucher (OV)            | Record of ownership of an         |
|                                   | individual device.                |
|                                   |                                   |
|                                   | Contains the following            |
|                                   | information:                      |
|                                   |                                   |
|                                   | &#42; Owner                       |
|                                   | (&#96;f                           |
|                                   | do-owner-onboarding-service&#96;) |
|                                   |                                   |
|                                   | &#42; Rendezvous Server - FIDO    |
|                                   | server                            |
|                                   | (&#96;fdo-rendezvous-server&#96;) |
|                                   |                                   |
|                                   | &#42; Device (at least one        |
|                                   | combination)                      |
|                                   | (&#9                              |
|                                   | 6;fdo-manufacturing-service&#96;) |
+-----------------------------------+-----------------------------------+
| Rendezvous server                 | Link to a server used by the      |
|                                   | device and later on, used on the  |
|                                   | process to find out who is the    |
|                                   | owner of the device               |
+-----------------------------------+-----------------------------------+

: FDO glossary

:::: formalpara
::: title
Additional resources
:::

&#42; [FIDO IoT
spec](https://fidoalliance.org/specs/fidoiot/FIDO-IoT-spec-v1.0-wd-20200730.html&#35;OV)
::::

# Network Access {#_network_access}

Before removing the serial console or HDMI monitor and USB keyboard,
verify network connectivity. The provided images default to obtaining
network settings from a DHCP server.

## Verify Network Configuration {#_verify_network_configuration}

Determine your IP address:

    $ ip addr

Check that you have a default gateway:

    $ ip route

Ping a known host:

    $ ping -c3 iot.fedoraproject.org

:::: note
::: title
:::

The sample above requires name resolution and a route to the internet.
If your device is located on an isolated network, ping another host on
your network.
::::

Verify that &#96;sshd&#96; is running:

    $ systemctl is-active sshd

View the default firewall configuration:

    $ sudo firewall-cmd --list-all

:::: note
::: title
:::

Information on adding support for specific devices can be found in the
[User Guide](user-guide.xml).
::::

## Configure Remote Access {#_configure_remote_access}

Once the initial setup is complete, the serial console or HDMI monitor
and USB keyboard are no longer required to access the device. The device
can be left in a headless state and accessed remotely.

The released images are configured to run an SSH server and accept
outside connections. The default configuration allows root login if a
password is set. This is a good reason to leave the root account locked.
The default configuration also allows standard users to login and the
user can then sudo if they were made an administrator as a member of the
wheel group.

    $ ssh testuser@11.22.33.44

:::: tip
::: title
Authentication Failures
:::

If receive a \'Too many authentication failures\' message such as:

    Received disconnect from 11.22.33.44 port 22:2: Too many authentication failures

you may have too many different ssh keys in your personal ssh
configuration directory. Since the image does not have your key, try
connecting with a password first using:

    $ ssh -o PreferredAuthentications=password testuser@11.22.33.44

If this works, you can customize your ssh configuration to specify
either this option or options to use a specific key once you have added
your keys.
::::

:::: note
::: title
:::

More information on managing accounts, keys, and remote access can be
found in the [User Guide](user-guide.xml).
::::

# Boot the Simplified Provisioner {#_boot_the_simplified_provisioner}

## Boot from the Simplified Provisioner ISO {#_boot_from_the_simplified_provisioner_iso}

&#42; If you are using physical devices with a CD-ROM unit: &#42;&#42;
Burn the downloaded Simplified Provisioner ISO to a CD-ROM &#42;&#42;
Use the CD-ROM to boot the IoT device from it. &#42; If you are using
Virtual Machines, you can use the &#96;virt-install&#96; command to boot
from the Simplified Provisioner ISO.

\+

\\.... \\# virt-install \--connect qemu:///system \\ \--name
\'{VMName}\' \\ \--os-variant \'{OSVariant}\' \\ \--boot
uefi,loader.secure=false \\ \--vcpus {VMCPUs} \--memory {VMMemory} \\
\--network network=default,model=virtio \\ \--disk pool=default,size=30
\\ \--cdrom {FedoraSimplifiedProvisionerISO} \\....

## Boot the Simplified Provisioner from an USB Flash Drive {#_boot_the_simplified_provisioner_from_an_usb_flash_drive}

&#42; Copy the ISO image file to a USB flash drive (You will need a 8 GB
USB flash drive at least) &#42; Connect the USB flash drive to the port
of the computer you want to boot. &#42; Boot the device from the USB
flash drive.

## Boot the Simplified Provisioner from UEFI HTTP Boot {#_boot_the_simplified_provisioner_from_uefi_http_boot}

&#42; Copy the contents of the Simplified Provisioner ISO to a directory

\+

\\.... mount {FedoraSimplifiedProvisionerISO} /mnt cp -r /mnt
Fedora-{FedoraVersion}-IoT-Simplified-Provisioner cd
Fedora-{FedoraVersion}-IoT-Simplified-Provisioner \\.... \\\* Modify the
\\\`grub.cfg\\\` file in \\\`EFI/BOOT\\\` directory and replace all the
instances of \\\`linux\\\` and \\\`initrd\\\` with \\\`linuxefi\\\` and
\\\`initrdefi\\\` respectively.

\+

\\.... sed -i -e \'s\|linux /\|linuxefi /\|\' \\ -e \'s\|initrd
/\|initrdefi /\|\' \\ EFI/BOOT/grub.cfg \\.... \\\* Use an HTTP Server
to serve the contents over the network, e.g.:

\+

\\.... python3 -m http.server {UEFIHTTPBootServerPort} firewall-cmd
\--add-port={UEFIHTTPBootServerPort}/tcp \\....

&#42; The correct URL to perform UEFI HTTPBoot depends on the ISO
architecture (&#96;x86_64&#96; or &#96;aarch64&#96;) &#42;&#42; For
&#96;x86_64&#96; hardware the corresponding HTTP URL of
&#96;EFI/BOOT/BOOTX86.EFI&#96; file will be used to boot (e.g.
&#96;[http://{UEFIHTTPBootServerIP}:{UEFIHTTPBootServerPort}/EFI/BOOT/BOOTX86.EFI&#96](http://{UEFIHTTPBootServerIP}:{UEFIHTTPBootServerPort}/EFI/BOOT/BOOTX86.EFI&#96);)
&#42;&#42; For &#96;aarch64&#96; hardware the corresponding HTTP URL of
&#96;EFI/BOOT/BOOTAA64.EFI&#96; file will be used to boot (e.g.
&#96;[http://{UEFIHTTPBootServerIP}:{UEFIHTTPBootServerPort}/EFI/BOOT/BOOTAA64.EFI&#96](http://{UEFIHTTPBootServerIP}:{UEFIHTTPBootServerPort}/EFI/BOOT/BOOTAA64.EFI&#96);)

### Booting Physical Servers {#_booting_physical_servers}

&#42; If using a physical server please check the manual or Management
UI interface to see if the system supports UEFI HTTPBoot and follow the
steps in the manual to boot it manually or in an automated way from the
boot URL (see above)

### Booting Virtual Machines {#_booting_virtual_machines}

&#42; Use the &#96;virt-install&#96; command (or any other tool that
supports booting UEFI VMs) to boot a VM. E.g.:

\+

\\.... virt-install \--connect qemu:///system \\ \--name \'{VMName}\' \\
\--os-variant \'{OSVariant}\' \\ \--boot uefi,loader.secure=false \\
\--vcpus {VMCPUs} \--memory {VMMemory} \\ \--network
network=default,model=virtio \\ \--disk pool=default,size=30 \\
\--import \\....

&#42; Press &#42;\'\[Esc\]\'&#42; key repeately to enter the UEFI
management interface &#42; Select &#42;\'Device Manager\'&#42; and press
&#42;\'\[Enter\]\'&#42; &#42; Select &#42;\'Network Device List\'&#42;
and press &#42;\'\[Enter\]\'&#42; &#42; Select the MAC address
corresponding to the interface you wan to use to perform UEFI HTTPBoot
and press &#42;\'\[Enter\]\'&#42; &#42; Select &#42;\'HTTP Boot
Configuration\'&#42; and press &#42;\'\[Enter\]\'&#42; &#42; Select
&#42;\'Boot URI\'&#42; and press &#42;\'\[Enter\]\'&#42; &#42; Enter the
HTTPBoot URL (see above) (e.g.:
&#42;[http://{UEFIHTTPBootServerIP}:{UEFIHTTPBootServerPort}/EFI/BOOT/BOOTX86.EFI&#42](http://{UEFIHTTPBootServerIP}:{UEFIHTTPBootServerPort}/EFI/BOOT/BOOTX86.EFI&#42);)
and press &#42;\'\[Enter\]\'&#42; &#42; Press &#42;\'\[F10\]\'&#42; key
to save the changes and then press &#42;\'\[Y\]\'&#42; to confirm the
action &#42; Press &#42;\'\[Esc\]\'&#42; four times until you return to
the main screen &#42; Select &#42;\'Boot Manager\'&#42; &#42; Select
&#42;\'UEFI HTTP\'&#42; and press &#42;\'\[Enter\]\'&#42; &#42; The VM
should perform the UEFI HTTPBoot.

It's also possible to perform the same steps in an automated way by
modifying the UEFI vars after creating the virtual machine. For that we
will need to install the &#96;qemu-img&#96; and
&#96;python3-virt-firmware&#96; packages:

\\.... dnf install -y python3-virt-firmware qemu-img \\....

&#42; Create an unitialized and stopped virtual machine (make sure it
supports UEFI), e.g.:

\+

\\.... virt-install \--connect qemu:///system \\ \--name \'{VMName}\' \\
\--os-variant \'{OSVariant}\' \\ \--boot uefi,loader.secure=false \\
\--vcpus {VMCPUs} \--memory {VMMemory} \\ \--network
network=default,model=virtio \\ \--disk pool=default,size=30 \\
\--import \--noautoconsole \--noreboot \\.... \\\* Connect the QCOW2
containing the VM\'s UEFI variables to an NBD disk so we can modify them
inplace:

\+

\\.... modprobe nbd qemu-nbd \--connect /dev/nbd0
/var/lib/libvirt/qemu/nvram/{VMName}\_VARS.qcow2 \\.... \\\* Use the
\\\`virt-fw-vars\\\` tool to modify the UEFI variables and configure the
VM to boot from the HTTP URL, e.g.:

\+

\\.... virt-fw-vars \--input /dev/nbd0 \--set-boot-uri
http://{UEFIHTTPBootServerIP}:{UEFIHTTPBootServerPort}/EFI/BOOT/BOOTX64.EFI
\\.... \\\* Disconnect the NBD device:

\+

\\.... qemu-nbd \--disconnect /dev/nbd0 \\.... \\\* Start the VM:

\+

\\.... virsh \--connect qemu:///system \\ start {VMName} \\.... \\\* The
VM should perform an UEFI HTTPBoot from the configured URL

## Customizing the Simplified Provisioner ISO {#_customizing_the_simplified_provisioner_iso}

Fedora IoT provides a generic Simplified Provisioning ISO that is by
default configured to install to a virtual disk (&#96;/dev/vda&#96;).
This can be customized for your device depending on what hardware you
have (nvme0, sda, mmcblk0) and configuration option you would like to
leverage - FDO or Ignition.

### Prerequisites {#_prerequisites_4}

&#42; Recent simplified-provisioning ISO &#42; Fedora system with
&#96;lorax&#96; installed, which provides the &#96;mkksiso&#96; tool
(sudo dnf install lorax). &#42; To use FDO, you have installed and
configured the FDO services as described in: &#42;&#42; [Installing and
configuring the Manufacturing
server](fdo-installing-the-manufacturing-server-package.xml) &#42;&#42;
[Installing and configuring the Rendezvous
Server](fdo-installing-configuring-and-running-the-rendezvous-server.xml)
&#42;&#42; [Installing and configuring the Owner's Onboarding
Server](fdo-installing-configuring-and-running-the-owner-server.xml)
&#42; To use Ignition, you have created a configuration file as
described in: &#42;&#42; [Creating an Ignition configuration
file](creating-an-ignition-configuration-file.xml)

## Creating a custom Simplified Provisioner {#_creating_a_custom_simplified_provisioner}

With use of the &#96;mkksiso&#96; tool its possible to create a
customized installer that can be used to install and configure most
devices.

### Example with FIDO Device Onboard {#_example_with_fido_device_onboard}

This example:

&#42; Uses the &#96;\--cmdline&#96; option to add the
&#96;fdo.manufacturing_server_url&#96; to specify the FDO Manufacturing
server to be used during the installation. NOTE: Replace the URL with
that of your FDO Manufacturing server url. &#42; Uses the
&#96;\--replace&#96; option to update the installation device and remove
the &#96;quiet&#96; option from the kernel arguments so boot message are
shown on screen &#42; Uses the generic ISO -
&#96;Fedora-IoT-provisioner-42-20250618.0.x86_64.iso&#96; creating a new
ISO named &#96;Fedora-IoT-provisioner-FDO-42-20250618.0.x86_64.iso&#96;

\\.... sudo mkksiso \--cmdline
\'fdo.manufacturing_server_url=http://192.168.1.26:8080
fdo.diun_pub_key_insecure=true\' \\ \--replace quiet \'\' \\ \--replace
vda sda \\ Fedora-IoT-provisioner-42-20250618.0.x86_64.iso
Fedora-IoT-provisioner-FDO-42-20250618.0.x86_64.iso \\....

### Example with Ignition {#_example_with_ignition}

This example:

&#42; Uses the &#96;\--cmdline&#96; option to add the
&#96;ignition.config.url&#96; to specify the location of the Ignition
configuration file. NOTE: Replace the URL with that of your Ignition
file. &#42; Uses the &#96;\--replace&#96; option to update the
installation device to use &#96;nvme0&#96; &#42; Uses the generic ISO -
&#96;Fedora-IoT-provisioner-42-20250618.0.x86_64.iso&#96; creating a new
ISO named &#96;Fedora-IoT-provisioner-IGN-42-20250618.0.x86_64.iso&#96;

\\.... sudo mkksiso \--cmdline
\'coreos.inst.append=ignition.config.url=http://192.168.1.25/configs/ignition/config.ign\'
\\ \--replace vda nvme0 \\
Fedora-IoT-provisioner-42-20250618.0.x86_64.iso
Fedora-IoT-provisioner-IGN-42-20250618.0.x86_64.iso \\....

## Troubleshooting issues {#_troubleshooting_issues}

When troubleshooting issues with the Simplified-Provisioner it may be
helpful to use the \\\`coreos.inst.skip_reboot\\\` option to prevent
automatic reboot after installation completes.

# Creating an Ignition configuration file {#_creating_an_ignition_configuration_file}

The &#96;Butane&#96; tool is the preferred option to create an Ignition
configuration file. &#96;Butane&#96; consumes a &#96;Butane Config
YAML&#96; file and produces an &#96;Ignition Config&#96; in the JSON
format. The JSON file is used by a system on its first boot. The
&#96;Ignition Config&#96; applies the configuration in the image, such
as user creation, and &#96;systemd&#96; units installation.

:::: formalpara
::: title
Prerequisites
:::

&#42; You have installed podman or [Butane
v0.20.0](https://github.com/coreos/butane/releases/tag/v0.20.0) or
later:
::::

<div>

::: title
Procedure
:::

1.  Create a &#96;Butane Config&#96; file and save it in the
    &#96;.bu&#96; format. You must specify the &#96;variant&#96; entry
    as &#96;fiot&#96;, and the &#96;version&#96; entry as
    &#96;1.0.0&#96;, for Fedora IoT images. The butane &#96;fiot&#96;
    variant on version 1.0.0 targets Ignition spec version
    &#96;3.3.0&#96;. The following is a Butane Config YAML file example:

        variant: fiot
        version: 1.0.0
        ignition:
        config:
        merge:
        - source: http://{DefaultServerIP}/config.ign
        passwd:
        users:
        - name: core
        groups:
        - wheel
        password_hash: password_hash_here
        ssh_authorized_keys:
        - ssh-ed25519 some-ssh-key-here
        storage:
        files:
        - path: /etc/NetworkManager/system-connections/enp1s0.nmconnection
        contents:
        inline: |
        [connection]
        id=enp1s0
        type=ethernet
        interface-name=enp1s0
        [ipv4]
        address1={DefaultIotDeviceIP}/{DefaultNetworkPrefix},{DefaultGateway}
        dns=8.8.8.8;
        dns-search=
        may-fail=false
        method=manual
        mode: 0600
        - path: /usr/local/bin/startup.sh
        contents:
        inline: |
        \#!/bin/bash
        echo 'Hello, World!'
        mode: 0755
        systemd:
        units:
        - name: hello.service
        contents: |
        [Unit]
        Description=A hello world
        [Install]
        WantedBy=multi-user.target
        enabled: true
        - name: fdo-client-linuxapp.service
        dropins:
        - name: log_trace.conf
        contents: |
        [Service]
        Environment=LOG_LEVEL=trace

2.  Run the following command to consume the &#96;Butane Config
    YAML&#96; file and generate an Ignition Config in the JSON format:

        $ podman run -i --rm quay.io/coreos/butane --pretty --strict \< fiot.bu | tee fiot.ign
        {
        'ignition': {
        'config': {
        'merge': [
        {
        'source': 'http://192.168.122.1/config.ign'
        }
        ]
        },
        'version': '3.4.0'
        },
        'passwd': {
        'users': [
        {
        'groups': [
        'wheel'
        ],
        'name': 'core',
        'passwordHash': 'password_hash_here',
        'sshAuthorizedKeys': [
        'ssh-ed25519 some-ssh-key-here'
        ]
        }
        ]
        },
        'storage': {
        'files': [
        {
        'path': '/etc/NetworkManager/system-connections/enp1s0.nmconnection',
        'contents': {
        'compression': 'gzip',
        'source': 'data:;base64,H4sIAAAAAAAC/1SKwQrCMBAF7/stNjahSEX2S0oPS/JKA822JKvQvxcFDzKnGWaKuyqi5V1nyomhh2892XmAYSuqwiiroS4S0akU/J4pH69hJkmpojXP/h6cv43Oh+B8fw3D5a9Q0saj+/L4SNcgNa5MRc5ukbzxIlsDFdi6Jy6iT9noHQAA//9IedCQoQAAAA=='
        },
        'mode': 384
        },
        {
        'path': '/usr/local/bin/startup.sh',
        'contents': {
        'compression': '',
        'source': 'data:;base64,IyEvYmluL2Jhc2gKZWNobyAiSGVsbG8sIFdvcmxkISIK'
        },
        'mode': 493
        }
        ]
        },
        'systemd': {
        'units': [
        {
        'contents': '[Unit]\nDescription=A hello world\n[Install]\nWantedBy=multi-user.target\n',
        'enabled': true,
        'name': 'hello.service'
        },
        {
        'dropins': [
        {
        'contents': '[Service]\nEnvironment=LOG_LEVEL=trace\n',
        'name': 'log_trace.conf'
        }
        ],
        'name': 'fdo-client-linuxapp.service'
        }
        ]
        }
        }

    After you run the &#96;Butane Config YAML&#96; file to check and
    generate the &#96;Ignition Config JSON&#96; file, you might get
    warnings when using unsupported fields, like partitions, for
    example. You can fix those fields and rerun the check.

</div>

You have now an Ignition JSON configuration file that you can use to
customize your installation.

:::: formalpara
::: title
Additional resources
:::

&#42; [Fedora IOT Specification
v1.0.0](https://coreos.github.io/butane/config-fiot-v1_0/).
::::

# User Guide {#_user_guide}

Welcome to the user guide for Fedora IoT. Both this guide and Fedora IoT
images are in the very early stages, so please report any issues to [the
mailing
list](https://lists.fedoraproject.org/admin/lists/iot.lists.fedoraproject.org/).

![SoC board](iot-fedora.svg)

## Supported Platforms {#_supported_platforms_2}

Fedora IoT supports the x86_64 and aarch64 architectures.

We have a page covering the currently tested [Reference
Platforms](reference-platforms.xml). Other devices supported by Fedora
on x86_64, aarch64 or ARMv7 should work just fine but haven't been
widely tested in the IoT context so your milage may vary.

The list of supported reference devices will expand with time. If you're
a hardware vendor and would like to have a device become a reference
platform by actively participating and testing Fedora IoT, please reach
out to [Peter Robinson](https://fedoraproject.org/wiki/User:Pbrobinson),
the Fedora IoT Lead.

## Required resources {#_required_resources_2}

The images being created are currently 4GB in size. The current memory
used for testing is 1GB of RAM. The Fedora IoT base image should run
with less, but of course this limits the amount of container
applications can be run on top of the base OS.

# Updates and Rollbacks {#_updates_and_rollbacks}

:::: note
::: title
:::

The latest image builds are available
[here](https://download.fedoraproject.org/pub/alt/iot/).
::::

## Upgrade to the Latest Image {#_upgrade_to_the_latest_image}

Display the status of the currently running deployment:

    $ rpm-ostree status

The &#96;rpm-ostree&#96; command is used to manage the atomic system
tree used by the Fedora IoT images. The &#96;update&#96; command is an
alias for the &#96;upgrade&#96; command.

View the options with:

    $ rpm-ostree upgrade --help
    Usage:
    rpm-ostree upgrade [OPTION…]

    Perform a system upgrade

    Help Options:
    -h, --help                      Show help options

    Application Options:
    --os=OSNAME                     Operate on provided OSNAME
    -r, --reboot                    Initiate a reboot after operation is complete
    --allow-downgrade               Permit deployment of chronologically older trees
    --preview                       Just preview package differences
    --check                         Just check if an upgrade is available
    -C, --cache-only                Do not download latest ostree and RPM data
    --download-only                 Just download latest ostree and RPM data, don't deploy
    --upgrade-unchanged-exit-77     If no upgrade is available, exit 77
    --sysroot=SYSROOT               Use system root SYSROOT (default: /)
    --peer                          Force a peer-to-peer connection instead of using the system message bus
    --install=PKG                   Overlay additional package
    --uninstall=PKG                 Remove overlayed additional package
    --version                       Print version information and exit

Check for available updates:

    $ sudo rpm-ostree upgrade --check
    Receiving metadata objects: 0/(estimating) -/s 0 bytes\&#8230; done
    AvailableUpdate:
    Version: 29.20190211.0 (2019-02-11T13:18:27Z)
    Commit: 5eb0553c02a8035a02f030c7fb8d5c6727d1ecb2700dade4b767363acfcab8e4
    GPGSignature: Valid signature by C2A3FA9DC67F68B98BB543F47BB90722DBBDCF7C
    Diff: 25 upgraded

Preview the package differences:

    $ sudo rpm-ostree upgrade --preview

If you wish, you can download the packages only and not deploy them
with:

    $ sudo rpm-ostree upgrade --download-only

To apply the OSTree update deltas available on CDN use the following
command:

    $ sudo rpm-ostree upgrade

Due to the atomic nature of the OS, you will have to reboot into the new
image to have the updates take effect:

    $ systemctl reboot

## Rollback to a previous tree {#_rollback_to_a_previous_tree}

The &#96;rpm-ostree&#96; utility keeps two deployments available. Both
have an entry in the bootloader menu. The new updated entry with be the
default. If necessary, you can choose the other entry to boot into the
previous deployment.

:::: tip
::: title
:::

The timeout for GRUB2 to display the menu is very short at only one
second. Pressing the space bar or an arrow key when the menu appears
will interrupt the timeout and allow you to choose another entry. The
ENTER key will boot the selected image.
::::

To permanently switch back to the previous deployment:

    $ sudo rpm-ostree rollback

Like with the upgrade, a system reboot will be required. You can use the
&#96;systemctl reboot&#96; command or you can include the
&#96;\--reboot&#96; option when you issue the rollback command:

    $ sudo rpm-ostree rollback --reboot

:::: note
::: title
:::

More information about [Bootloading with
GRUB2](https://docs.fedoraproject.org/en-US/quick-docs/bootloading-with-grub2/)
can be found in the Fedora Quick Docs.
::::

:::: note
::: title
:::

More information about the &#96;rpm-ostree&#96; command can be found in
the upstream [Administrator
Handbook](https://coreos.github.io/rpm-ostree/administrator-handbook/)
::::

## Automatic updates {#_automatic_updates}

A &#96;rpm-ostreed&#96; service is available to monitor for upgrades
automatically.

To enable automated updates edit the &#96;/etc/rpm-ostreed.conf&#96;
file. The options available are as follow:

&#42; The \'none\' option disables automatic updates. This is the
default policy. &#42; The \'check\' option downloads enough metadata to
display available updates with &#96;rpm-ostree status&#96;. &#42; The
\'stage\' option downloads, unpacks and stages the update which will be
finalized on a reboot. &#42; The \'apply\' option is the same as stage
but also initiates the reboot to the new version.

    \&#35; cat /etc/rpm-ostreed.conf
    \&#35; Entries in this file show the compile time defaults.
    \&#35; You can change settings by editing this file.
    \&#35; For option meanings, see rpm-ostreed.conf(5).

    [Daemon]
    AutomaticUpdatePolicy=check
    \&#35;IdleExitTimeout=60

Next we need to enable the appropriate services:

    systemctl reload rpm-ostreed
    systemctl enable rpm-ostreed-automatic.timer --now

We should now be able to see the state of automatic updates in the
status:

    \&#35; rpm-ostree status
    State: idle
    AutomaticUpdates: stage; rpm-ostreed-automatic.timer: last run 4min 22s ago

The rpm-ostreed-automatic.service and rpm-ostreed-automatic.timer
control frequency of checks and upgrades. More information is available
in the man pages or this [blog
post](https://miabbott.github.io/2018/06/13/rpm-ostree-automatic-updates.html)

# Layered Packages {#_layered_packages}

The Fedora IoT images utilize &#96;rpm-ostree&#96; which is a hybrid
image/package system. This allows layering a package on an existing
image which produces a new versioned deployment. Similarly, removing a
layered package creates a new versioned image. The rpm-ostree utility
keeps two deployments available so a rollback procedure can be used to
revert to a previous deployment.

Display the status of the currently running deployment:

    $ rpm-ostree status
    State: idle
    AutomaticUpdates: disabled
    Deployments:
    ● ostree://fedora-iot:fedora/stable/x86_64/iot  \&lt;1\&gt;
    Version: 29.20190214.0 (2019-02-14T18:11:32Z)
    BaseCommit: 007f24873c04fea4ee96024f6ebb6e56a29f634ab2a9e9218b15444666dd719c
    GPGSignature: Valid signature by C2A3FA9DC67F68B98BB543F47BB90722DBBDCF7C
    LayeredPackages: asciiquarium git  \&lt;2\&gt;

    ostree://fedora-iot:fedora/stable/x86_64/iot  \&lt;3\&gt;
    Version: 29.20190214.0 (2019-02-14T18:11:32Z)
    Commit: 007f24873c04fea4ee96024f6ebb6e56a29f634ab2a9e9218b15444666dd719c
    GPGSignature: Valid signature by C2A3FA9DC67F68B98BB543F47BB90722DBBDCF7C

&lt;1&gt; The currently running deployment is marked with a ●. &lt;2&gt;
The layered packages are listed in the description. &lt;3&gt; The
previous deployment is also available in the boot menu or for a rollback
procedure.

# Adding Layered Packages {#_adding_layered_packages}

Add a layered package with the &#96;rpm-ostree install&#96; command:

    $ rpm-ostree install --help
    Usage:
    rpm-ostree install [OPTION…] PACKAGE [PACKAGE\&#8230;]

    Overlay additional packages

    Help Options:
    -h, --help              Show help options

    Application Options:
    --uninstall=PKG         Remove overlayed additional package
    -C, --cache-only        Do not download latest ostree and RPM data
    --download-only         Just download latest ostree and RPM data, don't deploy
    --os=OSNAME             Operate on provided OSNAME
    -r, --reboot            Initiate a reboot after operation is complete
    -n, --dry-run           Exit after printing the transaction
    --allow-inactive        Allow inactive package requests
    --idempotent            Do nothing if package already (un)installed
    --unchanged-exit-77     If no overlays were changed, exit 77
    --sysroot=SYSROOT       Use system root SYSROOT (default: /)
    --peer                  Force a peer-to-peer connection instead of using the system message bus
    --version               Print version information and exit

## Install multiple packages {#_install_multiple_packages}

This command accepts multiple package names. To create less images,
consider grouping compatable packages into a single command. This will
create a single new layered image.

    $ sudo rpm-ostree install git asciiquarium

Alternately, consider [using containers](container-support.xml) for your
applications. A container workflow can be managed separately from the OS
update cycle.

## Be sure to Reboot {#_be_sure_to_reboot}

At this point a new layer is available but not yet active. For example,
the git command installed above is not yet found.

    $ git --version
    bash: git: command not found

Display the current status of the images:

    $ rpm-ostree status
    State: idle
    AutomaticUpdates: disabled
    Deployments:
    ostree://fedora-iot:fedora/stable/x86_64/iot
    Version: 29.20190214.0 (2019-02-14T18:11:32Z)
    BaseCommit: 007f24873c04fea4ee96024f6ebb6e56a29f634ab2a9e9218b15444666dd719c
    GPGSignature: Valid signature by C2A3FA9DC67F68B98BB543F47BB90722DBBDCF7C
    LayeredPackages: asciiquarium git \&lt;1\&gt;

    ● ostree://fedora-iot:fedora/stable/x86_64/iot  \&lt;2\&gt;
    Version: 29.20190214.0 (2019-02-14T18:11:32Z)
    Commit: 007f24873c04fea4ee96024f6ebb6e56a29f634ab2a9e9218b15444666dd719c
    GPGSignature: Valid signature by C2A3FA9DC67F68B98BB543F47BB90722DBBDCF7C

    ostree://fedora-iot:fedora/29/x86_64/iot  \&lt;3\&gt;
    Version: 29.20181128.1 (2018-11-28T09:16:42Z)
    Commit: f40b0a24b9c11ee859d4cb323222d0b979873d8d11f63fcb848cba6ab8a2515e
    GPGSignature: Can't check signature: public key A20AA56B429476B4 not found

&lt;1&gt; The new image indicates layered packages. &lt;2&gt; The second
image listed is the active image as indicated by the ●. &lt;3&gt; Any
older images will be removed when the system is rebooted.

Due to the atomic nature of the OS, you will have to reboot into the new
image to have the layered image take effect:

    $ sudo systemctl reboot

Display the status of the images:

    $ rpm-ostree status
    State: idle
    AutomaticUpdates: disabled
    Deployments:
    ● ostree://fedora-iot:fedora/stable/x86_64/iot
    Version: 29.20190214.0 (2019-02-14T18:11:32Z)
    BaseCommit: 007f24873c04fea4ee96024f6ebb6e56a29f634ab2a9e9218b15444666dd719c
    GPGSignature: Valid signature by C2A3FA9DC67F68B98BB543F47BB90722DBBDCF7C
    LayeredPackages: asciiquarium git

    ostree://fedora-iot:fedora/stable/x86_64/iot
    Version: 29.20190214.0 (2019-02-14T18:11:32Z)
    Commit: 007f24873c04fea4ee96024f6ebb6e56a29f634ab2a9e9218b15444666dd719c
    GPGSignature: Valid signature by C2A3FA9DC67F68B98BB543F47BB90722DBBDCF7C

After the reboot, the git command will be available:

    $ git --version
    git version 2.20.1

# Removing Layered Packages {#_removing_layered_packages}

## Revert All Changes with a Rollback {#_revert_all_changes_with_a_rollback}

If the entire image needs to be reverted to a pristine or known state,
you can rollback to the previous version.

    $ sudo rpm-ostree rollback --reboot

## Remove Select Layered Packages {#_remove_select_layered_packages}

The &#96;rpm-ostree&#96; utility also has an uninstall option to remove
individual layered packages:

    $ rpm-ostree uninstall --help
    Usage:
    rpm-ostree uninstall [OPTION…] PACKAGE [PACKAGE\&#8230;]

    Remove overlayed additional packages

    Help Options:
    -h, --help              Show help options

    Application Options:
    --install=PKG           Overlay additional package
    --all                   Remove all overlayed additional packages
    --os=OSNAME             Operate on provided OSNAME
    -r, --reboot            Initiate a reboot after operation is complete
    -n, --dry-run           Exit after printing the transaction
    --allow-inactive        Allow inactive package requests
    --idempotent            Do nothing if package already (un)installed
    --unchanged-exit-77     If no overlays were changed, exit 77
    --sysroot=SYSROOT       Use system root SYSROOT (default: /)
    --peer                  Force a peer-to-peer connection instead of using the system message bus
    --version               Print version information and exit

Like the install or rollback, a system reboot will be required to
activate the new image.

# Configuring Package Repositories {#_configuring_package_repositories}

The &#96;rpm-ostree&#96; utility uses repositories configured in the
&#96;/etc/yum.repos.d&#96; directory.

To enable a specific repository, edit the configuration files in
/etc/yum.repos.d and for each desired repository, change the enabled=
line to &#96;enabled=1&#96;

You can add additional repository configuration files to enable third
party or local package repositories.

Some repositories provide an RPM package to assist in the configuration.
For example, to enable the RPM Fusion Free repository you can use:

    $ sudo rpm-ostree install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm

This method of configuration will require a reboot to enable the new
image.

    $ rpm-ostree status
    State: idle
    AutomaticUpdates: check; rpm-ostreed-automatic.timer: no runs since boot
    Deployments:
    ● ostree://fedora-iot:fedora/stable/aarch64/iot
    Version: 29.20190214.0 (2019-02-14T18:18:52Z)
    BaseCommit: 68b1f6c99a678f45e3de04f1252b271cce687a246c0004e45858b343d3637556
    GPGSignature: Valid signature by C2A3FA9DC67F68B98BB543F47BB90722DBBDCF7C
    LayeredPackages: git
    LocalPackages: rpmfusion-free-release-29-1.noarch \&lt;1\&gt;

&lt;1&gt; The package installed from a URL instead of a configured
repository will appear with \'LocalPackages\'

Additional resources:

&#42; Fedora Quick Docs includes a description of [Fedora
Repositories](https://docs.fedoraproject.org/en-US/quick-docs/repositories/).
&#42; Fedora Quick Docs describes third party repositories for
[Installing plugins for playing movies and
music](https://docs.fedoraproject.org/en-US/quick-docs/assembly_installing-plugins-for-playing-movies-and-music/).
Replace the &#96;dnf install&#96; commands with &#96;rpm-ostree
install&#96; for enabling on Fedora IoT images. &#42; The
[yum.conf(5)](https://linux.die.net/man/5/yum.conf) man page describes
options for creating your own file in the \[repository\] OPTIONS
section.

# Container Support {#_container_support}

Fedora IoT has excellent support for container-focused workflows.
Containers provide for separation of OS updates from application
updates, as well as allow testing and deployment of different versions
of applications. Fedora IoT uses podman, a daemonless container engine
to develop, download, manage, and run containers to support your home
assistant, industrial gateways, or data storage and analytics.

With &#96;podman&#96;, images and containers can be managed and used by
a non-privileged user. Commands are very similar to those used with
&#96;docker&#96;.

Show the version of podman and other configuration settings:

    $ podman info

Run as a user, the storage location is under the
&#96;\~/.local/share/containers&#96; directory. You can customize podman
with files in the &#96;\~/.config/containers&#96; directory.

Run as root, the storage location is defined in the
\'/etc/containers/storage.conf\' file and defaults to
\'/var/run/containers/storage\'.

    $ sudo podman info

Any of the &#96;podman&#96; commands have help available for several
levels of commands.

Show all the commands available:

    $ podman --help

Show the options for the pull command:

    $ podman pull --help

Some commands have other sub commands. Show the options for the image
command:

    $ podman image --help

To show more specific options, keep adding commands before the help
request. Show the options for listing images:

    $ podman image ls --help

[Podman](https://podman.io/) has a lot of well written documentation and
articles. You can find a number of them at the following links:

&#42; [getting started
tutorial](https://github.com/projectatomic/libpod/blob/master/docs/tutorials/podman_tutorial.md)
&#42; [docker to podman command
mapping](https://github.com/projectatomic/libpod/blob/master/transfer.md)
&#42; [Podman news and releases](https://medium.com/cri-o)

# Images and Containers {#_images_and_containers}

## Finding Images {#_finding_images}

Search for images with a keyword:

    $ podman search fedora
    $ podman search homeassistant

The registries which will be searched are configured in the
/etc/containers/registry.conf file.

The search result will include both the registry location and the name
of the image.

&#42; The registry name may include a port number. &#42; The image name
consists of USER/REPO. The user can be an individual, team, or company
that uploads the images to the registry. &#42; The image repository
contains tagged images and hidden layers. Most repositories contain an
image with the tag of \'latest\'. &#42; When downloading an image with
pull, run, or build commands, you may specify a specific tag image. The
default is to pull the image tagged \'latest\'.

The [&#96;skopeo&#96;](https://github.com/containers/skopeo) command is
a utility to work with images in many different container environments.
It was created to view information in remote registries and is now a
command and library for copying images with different transports. It is
used to manage container images and image storage remotely and locally
and all without requiring root. It can also pass authentication
credentials when required by the repository.

View creation dates, architectures, labels, tags, and layer checksums of
a remote image repository:

    $ skopeo inspect docker://registry.fedoraproject.org/fedora-minimal

## Manage Local Images {#_manage_local_images}

When you run a container, the image is first downloaded to the local
system. It can be helpful to go ahead and download an image as a
separate command.

The default is to pull the latest image from the default registry:

    $ podman pull fedora

You can also specify the registry, user, tag, or, as in the following
example, some combination:

    $ podman pull registry.fedoraproject.org/fedora-minimal:rawhide

List the local images:

    $ podman images
    REPOSITORY                                           TAG       IMAGE ID       CREATED       SIZE
    registry.fedoraproject.org/fedora-minimal            rawhide   8ecda3b9bc0d   2 days ago    164MB
    docker.io/homeassistant/raspberrypi3-homeassistant   latest    3c74046ca2a7   3 days ago    1.05GB
    docker.io/library/fedora                             latest    8b38e3af7237   4 weeks ago   315MB

The same output is show with &#96;podman image ls&#96;. Note the
singular \'image\' command before the additional \'ls\' command. If you
have a lot of images, you may want to specify filters or sort by a value
other than the creation date.

As a user, the local images will be stored under the
&#96;\~/.local/share/containers/&#96; directory. Each user has their own
namespace so these are separate from containers run as root. Listing the
images available to root displays a different or empty list:

    $ sudo podman images

Some actions can not be done with rootless containers. Some devices and
volumes will require that you pull and run containers in the root
namespace. The current podman v1.0 also requires root for port
publishing. The next version will allow rootless port publishing.

Like remote images, local images can also be inspected:

    $ podman inspect fedora

To inspect an image with a tag other than \'latest\', include the tag:

    $ podman inspect fedora-minimal:rawhide

## Running Containers {#_running_containers}

To launch the container use:

    $ podman run fedora

With the fedora image, the container will start and then it exits since
there is nothing left running. Some images are configured to run an
application in the foreground and the container will not terminate until
the application terminates.

To list the running containers use:

    $ podman container ls

To see all containers, including those that have exited:

    $ podman container ls -a
    CONTAINER ID   IMAGE                             COMMAND     CREATED              STATUS                      PORTS   NAMES            IS INFRA
    7835aaadd2d1   docker.io/library/fedora:latest   /bin/bash   About a minute ago   Exited (0) 14 seconds ago           hopeful_beaver   false

The exited containers are kept so that any data, including logs, can be
investigated before they are lost. You can start an exited container but
a typical workflow normally deletes used containers, launching new
containers when needed.

Options on the run command can change the behavior of launching a
container:

    $ podman run -it \ \&lt;1\&gt;
    \&gt; --name demo \ \&lt;2\&gt;
    \&gt; --rm \ \&lt;3\&gt;
    \&gt; fedora /bin/bash \&lt;4\&gt;
    bash-4.4\&#35;  \&lt;5\&gt;

&lt;1&gt; The -it options enable interactive mode and allocates a
pseudo-TTY. &lt;2&gt; You can name your container. Without this option,
a random name will be generated. &lt;3&gt; The \--rm option causes the
container to be deleted when it is terminated. This preserves space and
allows a new container to be started with the same name. &lt;4&gt; The
command to run. The command must be in the image. Not all images include
bash. &lt;5&gt; The /bin/bash process is running in the foreground. When
you exit the shell, the container will terminate.

## Publishing Ports {#_publishing_ports}

If your application listens on the network, you will need to map the
container port to a local port on your device. In the current version,
publishing ports requires root so the image must be available in the
root namespace.

Add the &#96;-p&#96; option when you launch the container:

    $ sudo podman run -p 127.0.0.1:8080:80 --name demo mydemohttp:latest

You can then connect to your application via 127.0.0.1:8080

The format is &#96;ip:hostPort:containerPort \| ip::containerPort \|
hostPort:containerPort \| containerPort&#96;.

Other options for publishing ports and many other run options are
available and well documented in the podman-run man page.

## Mapping a local directory {#_mapping_a_local_directory}

You may want to have your application write logs or collect data to a
directory on the host. Some containers expect that customized
configuration files are on the host device. In both cases, you can
create a bind mount with the &#96;\--volume&#96; option. Specify the
host directory, the mount point inside the container, and any mount
options.

For example, [Home
Assistant](https://www.home-assistant.io/docs/installation/docker/)
expects the configuration files to be on the host device:

    $ podman run -d --name='home-assistant' -v /home/pi/homeassistant:/config -v /etc/localtime:/etc/localtime:ro --net=host homeassistant/raspberrypi3-homeassistant

## Mapping a local device {#_mapping_a_local_device}

The &#96;\--device&#96; option will add a host device to the container.
Specify the host device name and optionally, the device name on the
container and any permissions. Some devices, like the GPIO device, will
require root.

To access the host GPIO device from the container:

    $ sudo podman run -it --rm --name demo-gpio --device=/dev/gpiochip0 fedora:latest /bin/bash

## Connect to a Running Container {#_connect_to_a_running_container}

You can also connect to a running container. Specify the container name
or ID and the command to execute:

    $ podman exec -it demo /bin/bash

You can also view container logs directly with podman:

    $ podman logs demo

Both the &#96;exec&#96; and &#96;logs&#96; commands are also part of the
&#96;podman container&#96; command.

## Removing Containers and Images {#_removing_containers_and_images}

List the containers to see the \'Container ID\' and \'name\' of each
container. Remove a container by specifying either the container ID or
name:

    $ podman container rm demo

Removing a container happens automatically when a container terminates
if the container was started with the &#96;\--rm&#96; option.

Removing a container does not remove the image. List the local images
with &#96;podman images&#96; or &#96;podman image ls&#96;. Remove the
image using either the \'IMAGE ID\' or the repository name and tag:

    $ podman rmi registry.fedoraproject.org/fedora-minimal:rawhide

You can also remove an image with the &#96;image&#96; command:

    $ podman image rm registry.fedoraproject.org/fedora-minimal:rawhide

# Build a Container with a Containerfile {#_build_a_container_with_a_containerfile}

## Creating the Containerfile {#_creating_the_containerfile}

If a container does not already exist for your application, one can be
built for your device.

It is common to create images from a working directory which holds the
Containerfile and any supporting files. This may be a version controlled
directory to facilitate sharing.

    $ mkdir container-demo \&amp;\&amp; cd container-demo

There are many examples of building containers using a Containerfile. A
simple Containerfile will contain some of the following elements:

&#42; The FROM line indicates the base, or starting, container, such as
a latest Fedora image. This image will be pulled if it is not already
available locally. Specify details for which image the same as you would
with a &#96;podman pull&#96; command. &#42; Creates layers with each RUN
command. Try to minimize the number of layers with multiple commands on
the same line using &amp;&amp; between commands. Also include any
cleanup commands such as &#96;dnf clean all&#96; to reduce the final
image size. &#42; Copy content from the working directory into the
container. &#42; Specify any ports to listen on with EXPOSE &#42; Start
your application &#42;&#42; CMD can be over written with podman run
command &#42;&#42; ENTRYPOINT often base command and default options.
Can be coupled with CMD for additional options.

## Example: Web application {#_example_web_application}

Create a working directory with some content for a web server:

    $ mkdir demo-httpd \&amp;\&amp; cd demo-httpd \&amp;\&amp; echo 'sample container' \&gt; index.html

Start the Containerfile with a FROM command to indicate the base image:

    $ echo 'FROM fedora:latest' \&gt;\&gt; Containerfile

Add a RUN command to update the image and add any application and
utilities:

    $ echo 'RUN dnf -y update \&amp;\&amp; dnf -y install httpd git  \&amp;\&amp; dnf clean all' \&gt;\&gt; Containerfile

The above example installs git. If your web content is hosted in a
version control system, you can add a RUN statement to clone that data
to the container. If your content is available in the build working
directory, you can use the COPY command to add it to the container.

Copy to the sample index.html file into the container:

    $ echo 'COPY index.html /var/www/html/index.html' \&gt;\&gt; Containerfile

The EXPOSE line specifies that the container listens on specified
network ports. It is used by the &#96;\--publish-all&#96; option on the
&#96;podman run&#96; command.

Document what ports are available to publish:

    $ echo 'EXPOSE 80' \&gt;\&gt; Containerfile

Specify the command to run when the container starts:

    $ echo 'ENTRYPOINT /usr/sbin/httpd -DFOREGROUND' \&gt;\&gt; Containerfile

:::: note
::: title
:::

Port bindings are not yet supported by rootless containers. If your
container needs to be available on the network, build it in the root
namespace. Port bindings for rootless containers is available in
upstream testing for podman 1.1.0 with slirp4netns v0.3.0.
::::

Build the image with a descriptive tag:

    $ sudo podman build --tag fedora:myhttpd -f ./Containerfile

The image will appear in the local registry:

    $ sudo podman images
    REPOSITORY                 TAG       IMAGE ID       CREATED         SIZE
    localhost/fedora           myhttpd   223534b48a9c   3 minutes ago   474MB
    docker.io/library/fedora   latest    8b38e3af7237   4 weeks ago     315MB

To make the application port available to the host device use the
&#96;\--publish&#96; or &#96;-p&#96; option with
&#96;hostPort:containerPort&#96; numbers. An IP can also be specified as
well as ranges of ports. See the [man
page](https://github.com/containers/libpod/blob/master/docs/source/markdown/podman-run.1.md)
for more options.

Run the container and publish the port:

    $ sudo podman run -p 8080:80 --name myhttpd --rm fedora:myhttpd

View the port information:

    $ sudo podman port myhttpd
    80/tcp -\&gt; 0.0.0.0:8080

Access the web page from the host device:

    $ curl localhost:8080

Access the web page from a remote location using the IP address of the
host device and the published port number.

Open firewall ports, services, or sources as needed. The Fedora IoT
image defaults to allowing any source on the same network through the
interfaces option:

    $ sudo firewall-cmd --list-all
    public (active)
    target: default
    icmp-block-inversion: no
    interfaces: eth0
    sources:
    services: dhcpv6-client mdns ssh
    ports:
    protocols:
    masquerade: no
    forward-ports:
    source-ports:
    icmp-blocks:
    rich rules:

Add a port with:

    $ sudo firewall-cmd --add-port 8080/tcp

More information on the &#96;firewall-cmd&#96; command can be found at
[firewalld.org](https://firewalld.org/documentation/man-pages/firewall-cmd.html).

## Example: Interaction with GPIO interface {#_example_interaction_with_gpio_interface}

To interact with the GPIO interface, layer the &#96;libgpiod-utils&#96;
package on the existing image or use with a container.

To layer the package:

    $ sudo rpm-ostree install libgpiod-utils python3-libgpiod
    $ sudo gpiodetect

To create a container for an application that works with the GPIO
interface in the root namespace.

Start the Containerfile with a FROM command to indicate the base image:

    $ echo 'FROM fedora:latest' \&gt;\&gt; Containerfile

Add a RUN command to update the image and add any application and
utilities:

    $ echo 'RUN dnf -y update \&amp;\&amp; dnf -y install git libgpiod-utils python3-libgpiod \&amp;\&amp; dnf clean all' \&gt;\&gt; Containerfile

The fedora:latest image includes bash so we can go ahead and build the
container without any specific applications to start or ports to expose.
The command can be specified when we run the container.

Build the image with a descriptive tag:

    $ sudo podman build --tag fedora:gpio -f ./Containerfile

The image will appear in the localhost registry for the root namespace:

    $ sudo podman images
    REPOSITORY                 TAG      IMAGE ID       CREATED         SIZE
    localhost/fedora           gpio     655abf78e6b9   4 minutes ago   542MB
    docker.io/library/fedora   latest   8b38e3af7237   4 weeks ago     315MB

To access the host GPIO device from the container, use the
&#96;\--device&#96; option when you start the container:

    $ sudo podman run -it --name demo-gpio --device=/dev/gpiochip0 localhost/fedora:gpio /bin/bash

Verify you can see the GPIO device:

    [root@167f31750fdb /]\&#35; gpiodetect
    gpiochip0 [pinctrl-bcm2835] (54 lines)

Now that the device is available from the container, continue to use the
installed tools or add addition applications.

Examples for using &#96;gpioset&#96; can be found in a 2018 Fedora
Magazine article: [How to turn on an LED with Fedora
IoT](https://fedoramagazine.org/turnon-led-fedora-iot/)

Automate additional steps by modifying the Containerfile and building a
new container.

The images do not have to be built from a Fedora container. This
Containerfile uses a raspbian image and clones the
[lightshowpi](http://lightshowpi.org/) project:

    $ cat Containerfile
    FROM raspbian/stretch:latest
    RUN apt-get -y update \&amp;\&amp; apt-get -y install git-core \&amp;\&amp; apt-get -y clean
    WORKDIR /
    RUN git clone https://togiles@bitbucket.org/togiles/lightshowpi.git \&amp;\&amp; \
    cd lightshowpi \&amp;\&amp; git fetch \&amp;\&amp; git checkout stable

The Docker documentation includes [Containerfile best
practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/).

## Reusing and Sharing the Containers {#_reusing_and_sharing_the_containers}

Once the container image is created it can be deployed to multiple
devices by uploading it to a registry.

Most registries require a naming convention of the
\'useraccount/description:tag\' and the default for most pull commands
is to look for a container with a tag of \'latest\'. An image can have
multiple tags and these tags are used to help identify architecture
compatibility and version control.

To rename or add a tag to a local image:

    $ podman tag fedora:myhttpd testuser/fedora-myhttpd:latest
    $ podman tag fedora:myhttpd quay.io/testuser/fedora-myhttpd:latest

Both names will appear in the list of images but the image ID will be
the same for each:

    $ podman images
    REPOSITORY                               TAG       IMAGE ID       CREATED        SIZE
    localhost/fedora                         myhttpd   d52cbe4136e8   24 hours ago   428 MB
    localhost/testuser/fedora-myhttpd        latest    d52cbe4136e8   24 hours ago   428 MB
    quay.io/testuser/fedora-myhttpd          latest    d52cbe4136e8   24 hours ago   428 MB
    docker.io/library/fedora                 latest    26ffec5b4a8a   4 weeks ago    283 MB

You can then push an image to a registry with &#96;podman push imageID
destination&#96;.

To extract the image to a local directory in a docker format:

    $ podman push quay.io/testuser/fedora-myhttpd dir:/tmp/fedora-myhttpd

For more exporting options, see the
[podman-push](https://github.com/containers/libpod/blob/main/docs/source/markdown/podman-push.1.md)
man page.

# Build a Container with Buildah {#_build_a_container_with_buildah}

Buildah is a tool that facilitates building OCI container images. You
can build images from scratch, from a container pulled from a registry,
or using a Dockerfile.

To use buildah in the Fedora IoT you will need to install the layered
packages:

    $ sudo rpm-ostree install buildah

More commonly buildah is used in a developer environment and the
resulting containers are then uploaded to a registry for use on any
device.

The commands for building a container from a base image are similar to
the lines in a Dockerfile. The first step is to pull the base images and
create the working container:

    $ buildah from fedora
    fedora-working-container

Add packages to the working container:

    $ buildah run fedora-working-container dnf install httpd -y

Create a working directory with some content for a web server:

    $ mkdir demo-httpd \&amp;\&amp; cd demo-httpd \&amp;\&amp; echo 'sample container' \&gt; index.html

Copy local files into the working container:

    $ buildah copy fedora-working-container index.html /var/www/html/index.html

Define the container entrypoint to start the application:

    $ buildah config --entrypoint '/usr/sbin/httpd -DFOREGROUND' fedora-working-container

Once configured, save the image:

    $ buildah commit fedora-working-container fedora-myhttpd

You can list the local images:

    $ buildah images

The buildah images are the same as the podman images. You can run now
the container locally with podman:

    $ podman run fedora-myhttpd

To make the image available on other devices, push the image to a
registry. The default image has a tag of \'latest\'. Use &#96;buildah
tag&#96; to add additional tags to the image before pushing to a
repository.

To push the image to a local Docker registry:

    $ buildah push --tls-verify=false fedora-myhttpd docker://localhost:5000/testuser/fedora-myhttpd:latest

To push to a remote registry provide the correct URL and any required
credentials:

    $ buildah push --creds testuser:5bbb9990-1234-1234-1234-aaa80066887c fedora-myhttpd docker://testuser/fedora-myhttpd

Skopeo can be used to inspect the results:

    $ skopeo inspect --tls-verify=false docker://localhost:5000/testuser/fedora-myhttpd:latest

Test the portability of the container with &#96;docker pull&#96; or
&#96;podman pull&#96; or &#96;buildah from&#96; commands.

Learn more about using buildah from:

&#42; Fedora Magazine: [How to build container images with Buildah
(2018)](https://fedoramagazine.org/daemon-less-container-management-buildah/)
&#42; buildah.io:
[Tutorials](https://github.com/containers/buildah/tree/master/docs/tutorials)

# Updating Packages and Applications {#_updating_packages_and_applications}

## Updating Layered Packages {#_updating_layered_packages}

Packages added to the Fedora IoT image with &#96;rpm-ostree install&#96;
will be updated along with the base operating system when
&#96;rpm-ostree upgrade&#96; is run as described in [Updates and
Rollbacks](applying-updates-UG.xml).

The &#96;rpm-ostree&#96; utility uses repositories configured in the
/etc/yum.repos.d directory. The Fedora IoT image is configured to check
for packages from several Fedora repositories including the
fedora-updates and fedora-updates-modular repositories.

In Fedora, before updates are generally available, they are tested in
the fedora-updates-testing and fedora-updates-testing-modular
repositories. The configuration files and gpg keys for these
repositories are included in the Fedora IoT image but are not enabled by
default.

To enable the testing repos, edit the configuration files in
/etc/yum.repos.d and for each desired repository, change the enabled=
line to &#96;enabled=1&#96;

    $ cat /etc/yum.repos.d/fedora-updates-testing-modular.repo
    [updates-testing-modular] \&lt;1\&gt;
    name=Fedora Modular $releasever - $basearch - Test Updates
    failovermethod=priority
    \&#35;baseurl=http://download.fedoraproject.org/pub/fedora/linux/updates/testing/$releasever/Modular/$basearch/
    metalink=https://mirrors.fedoraproject.org/metalink?repo=updates-testing-modular-f$releasever\&amp;arch=$basearch
    enabled=1  \&lt;2\&gt;
    repo_gpgcheck=0
    type=rpm
    gpgcheck=1
    metadata_expire=6h
    gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-fedora-$releasever-$basearch
    skip_if_unavailable=False

    [updates-testing-modular-debuginfo]  \&lt;3\&gt;
    name=Fedora Modular $releasever - $basearch - Test Updates Debug
    failovermethod=priority

    \&#8230; Output Truncated \&#8230;

&lt;1&gt; Each repository has a name in square brackets &lt;2&gt; The
enabled parameter takes a boolean value &lt;3&gt; A configuration file
can contain multiple repository configurations.

You can [add additional repository](add-repos.xml) configuration files
to enable other update, testing, or development repositories.

## Updating Containers {#_updating_containers}

By placing applications in containers, the host operating system can be
updated quickly without affecting package versions inside the container.
But what about when the fix needs to be applied to packages that are a
part of the container?

Containers are supposed to be lightweight, interchangeable, and
ephemeral. When an container is in need of an update, it is removed and
a new container is deployed in its place.

If your containers are built from another base image, you need to
monitor that base image for updates and to rebuild your containers using
the updated image.

The industry has a variety of services available to assist with
vulnerability scanning, update notifications, build systems, and other
CD/CI tools for containers.

It's a good practice to not patch inside of a container as it does not
scale well. Instead, build a new container and then deploy that
container to many devices. A container available in a shared registry
and tagged as \'latest\' will be used the next time podman run requests
that image.

# Rebasing to New Versions {#_rebasing_to_new_versions}

The &#96;rpm-ostree rebase&#96; command allows you to switch between
multiple branches. The &#96;ostree remote&#96; command allows you to
view and change repository options.

## Listing Remote Repositories {#_listing_remote_repositories}

The &#96;ostree remote&#96; command has several options:

    $ ostree remote --help
    Usage:
    ostree remote [OPTION…] COMMAND

    Remote commands that may involve internet access

    Builtin 'remote' Commands:
    add               Add a remote repository
    delete            Delete a remote repository
    show-url          Show remote repository URL
    list              List remote repository names
    gpg-import        Import GPG keys
    add-cookie        Add a cookie to remote
    delete-cookie     Remove one cookie from remote
    list-cookies      Show remote repository cookies
    refs              List remote refs
    summary           Show remote summary

    Help Options:
    -h, --help        Show help options

    Application Options:
    -v, --verbose     Print debug information during command processing
    --version         Print version information and exit

List remote repository names:

    $ ostree remote list
    fedora-iot

Show the remote URL:

    $ ostree remote show-url fedora-iot
    https://ostree.fedoraproject.org/iot

List the remote reference branches:

    $ ostree remote refs fedora-iot
    fedora-iot:fedora/stable/aarch64/iot
    fedora-iot:fedora/stable/x86_64/iot
    fedora-iot:fedora/devel/aarch64/iot
    fedora-iot:fedora/devel/x86_64/iot
    fedora-iot:fedora/rawhide/aarch64/iot
    fedora-iot:fedora/rawhide/x86_64/iot

## Adding and Removing Remote Repositories {#_adding_and_removing_remote_repositories}

The ostree remote repository configuration files are located in the
&#96;/etc/ostree/remotes.d&#96; directory.

    $ cat /etc/ostree/remotes.d/fedora-iot.conf
    [remote_'fedora-iot']
    url=https://ostree.fedoraproject.org/iot
    gpg-verify=true
    gpgkeypath=/etc/pki/rpm-gpg/
    contenturl=mirrorlist=https://ostree.fedoraproject.org/iot/mirrorlist

The first line specifies the name of the remote that will be shown with
&#96;ostree remote list&#96;. The additional lines are in the format of
\'KEY=VALUE\'.

To add a remote repository use the &#96;ostree remote add&#96; command:

    $ ostree remote add --help
    Usage:
    ostree remote add [OPTION…] NAME [metalink=|mirrorlist=]URL [BRANCH\&#8230;]

    Add a remote repository

    Help Options:
    -h, --help                        Show help options

    Application Options:
    --set=KEY=VALUE                   Set config option KEY=VALUE for remote
    --no-gpg-verify                   Disable GPG verification
    --if-not-exists                   Do nothing if the provided remote exists
    --gpg-import=FILE                 Import GPG key from FILE
    --contenturl=URL                  Use URL when fetching content
    --collection-id=COLLECTION-ID     Globally unique ID for this repository as an collection of refs for redistribution to other repositories
    --repo=PATH                       Path to OSTree repository (defaults to /sysroot/ostree/repo)
    --sysroot=PATH                    Use sysroot at PATH (overrides --repo)
    -v, --verbose                     Print debug information during command processing
    --version                         Print version information and exit

The &#96;\--set&#96; option can be used multiple times to configure any
KEY=VALUE pair. Some of the more common or required keys have their own
options. For example, the following two commands result in identical
configuration files. They differ only in how the contenturl is
specified:

    $ sudo ostree remote add --set=contenturl=mirrorlist=https://ostree.fedoraproject.org/iot/mirrorlist --set=gpgkeypath=/etc/pki/rpm-gpg/ fedora-iot 'https://ostree.fedoraproject.org/iot'

    $ sudo ostree remote add --contenturl=mirrorlist=https://ostree.fedoraproject.org/iot/mirrorlist --set=gpgkeypath=/etc/pki/rpm-gpg/ fedora-iot 'https://ostree.fedoraproject.org/iot'

To delete a remote repository use:

    $ sudo ostree remote delete fedora-iot

## Moving between Build Trees {#_moving_between_build_trees}

Currently there are three branches, the stable, develop, and rawhide
branches. Each branch corresponds to the Fedora release that's the
latest stable (stable), rawhide and if Fedora currently has a branched
version that is undergoing stablisation in preparaiton for release
(devel).

You need to specify the architecture as part of the branch option. At
the moment the options are aarch64 or x86_64.

To rebase to stable:

    $ sudo rpm-ostree rebase -b fedora/stable/\&lt;ARCH\&gt;/iot

To rebase to devel:

    $ sudo rpm-ostree rebase -b fedora/devel/\&lt;ARCH\&gt;/iot

To rebase to rawhide:

    $ sudo rpm-ostree rebase -b fedora/rawhide/\&lt;ARCH\&gt;/iot

Once ready, reboot the system to use the new image:

    $ sudo systemctl reboot

## Rebase to any New Version {#_rebase_to_any_new_version}

Recent releases will automatically import the release keys in the
specified directory if they are present on a rebase.

    Usage:
    ostree remote gpg-import [OPTIONS\&#8230;] NAME [KEY-ID\&#8230;]

Provide the reference path for the new version in the rebase command:

    $ sudo rpm-ostree rebase VERSION

The process is very similar to a system update. The new OS is downloaded
and installed in the background. Once ready, reboot the system to use
the new image:

    $ sudo systemctl reboot

Just like system updates, rebases can be reversed. The previous
deployment is still available, and you can boot back into it if there
are any problems with the new OS.

:::: note
::: title
:::

More information is available in the upstream documentation for
[libostree](https://ostree.readthedocs.io) and
[rpm-ostree](https://rpm-ostree.readthedocs.io).
::::

# Administration Tasks {#_administration_tasks}

Additional tasks mimic any other Linux administration tasks and use
available utilities included in the Fedora distribution. Some tasks are
described below with specific links to other Fedora Documentation or
upstream documentation.

General Resources:

&#42; [Fedora Quick
Docs](https://docs.fedoraproject.org/en-US/quick-docs/) &#42; Man pages

## User Management {#_user_management}

The initial image includes a locked root account without a password, ssh
keys can be added using [ignition](ignition-device-setup.xml).

    $ id testuser
    uid=1000(testuser) gid=1000(testuser) groups=1000(testuser),10(wheel)
    $ getent passwd testuser
    testuser:x:1000:1000::/home/testuser:/bin/bash

Package installation may add additional users to own files and processes
on the system. For example the httpd package installation scripts will
create a user apache if one does not already exist.

    $ id apache
    uid=48(apache) gid=48(apache) groups=48(apache)
    $ getent passwd apache
    apache:x:48:48:Apache:/usr/share/httpd:/sbin/nologin

This account is typically a system account with a UID below 1000, no
password, and a shell of &#96;/sbin/nologin&#96;. Accounts with a
nologin shell cannot be used interactively. These accounts also do not
have a home directory created in &#96;/home&#96;

To manually create a system account for your application use the useradd
command:

    $ sudo useradd -r -s /sbin/nologin appuser
    $ getent passwd appuser
    appuser:x:992:981::/var/home/appuser:/sbin/nologin

Centralized users accounts (LDAP, Kerberos) can be configured with
&#96;authconfig&#96; after the client packages, including
&#96;sssd&#96;, have been installed. The &#96;/etc/nsswitch.conf&#96;
file is already configured to look for sss as well as files and altfiles
for account information.

User accounts which are members of the wheel group automatically have
full privileges with the &#96;sudo&#96; command. This is from the
following lines in the sudo configuration file:

    $ sudo grep wheel /etc/sudoers
    \&#35;\&#35; Allows people in group wheel to run all commands
    %wheel  ALL=(ALL)   ALL
    \&#35; %wheel   ALL=(ALL)   NOPASSWD: ALL

Edits to this configuration file should be made with the
&#96;visudo&#96; command so that syntax is checked on exit. Instead of
editing the main configuration file, grant other users the ability to
issue specific commands as a different user by adding a configuration
file to the &#96;/etc/sudoers.d/&#96; directory.

&#42; Fedora Quick Docs: [Performing administration tasks using
sudo](https://docs.fedoraproject.org/en-US/quick-docs/performing-administration-tasks-using-sudo/)

Use &#96;ssh-keygen&#96; to generate an ssh key pair then add the public
key to the user account on your Fedora IoT device:

    $ ssh-copy-id testuser@10.11.12.13

Replace the username and IP address with that of your device. Use the
&#96;-i&#96; option to specify a key file other than the default of the
most recently modified &#96;\~/.ssh/id\_&#42;pub&#96; file. The
&#96;ssh-copy-id&#96; command will append the public key to the user's
authorized keys file on the device. It will create the &#96;\~/.ssh&#96;
directory if it does not already exist and ensure the permission on the
files are correct.

## Group Management {#_group_management}

Due to how &#96;rpm-ostree&#96; handles user + group entries, it may not
be possible to use &#96;usermod -a -G&#96; to add a user to a group
successfully. Until &#96;rpm-ostree&#96; moves to using &#96;systemd
sysusers&#96;, users will have to populate the &#96;/etc/group&#96; file
from the &#96;/usr/lib/group&#96; file before they can add themselves to
the group.

For example, if you wanted to add a user to the &#96;libvirt&#96; group:

\$ grep -E \'\^libvirt:\' /usr/lib/group \| sudo tee -a /etc/group \$
sudo usermod -aG libvirt \$USER

:::: note
::: title
:::

You will need to log off and log back in to apply these changes.
::::

This issue is tracked in
[rpm-ostree&#35;29](https://github.com/coreos/rpm-ostree/issues/29) and
[rpm-ostree&#35;49](https://github.com/coreos/rpm-ostree/issues/49).

*(Text copied from the [Fedora Silverblue
documentation](https://docs.fedoraproject.org/en-US/fedora-silverblue/troubleshooting/&#35;_unable_to_add_user_to_group))*

## Network Configuration {#_network_configuration}

List the network devices:

    $ nmcli dev
    DEVICE  TYPE      STATE      CONNECTION
    eth0    ethernet  connected  System eth0
    lo      loopback  unmanaged  --

Show details of a device:

    $ nmcli dev show eth0
    GENERAL.DEVICE:                         eth0
    GENERAL.TYPE:                           ethernet
    GENERAL.HWADDR:                         B8:27:EB:B4:93:D8
    GENERAL.MTU:                            1500
    \&#8230;Output Omitted\&#8230;

List the connection configurations:

    $ nmcli con
    NAME         UUID                                  TYPE      DEVICE
    System eth0  5fb06bd0-0bb0-7ffb-45f1-d6edd65f3e03  ethernet  eth0
    enp1s0       8a6006ff-a1b5-4048-be93-258087a1853f  ethernet  --

Only one connection per device can be UP but multiple connections can be
defined.

Show connection information:

    $ nmcli con show enp1s0
    connection.id:                          enp1s0
    connection.uuid:                        8a6006ff-a1b5-4048-be93-258087a1853f
    connection.stable-id:                   --
    connection.type:                        802-3-ethernet
    \&#8230; Output Omitted \&#8230;

The &#96;nmcli conn&#96; command has a variety of options including
edit, modify, up, down, add, and delete. Use the &#96;nmcli conn
help&#96; command to view the syntax.

The default configurations will try to obtain connection information
from a DHCP service on your network. If no DHCP service is available on
your network, you can add a static connection:

    $ nmcli connection add con-name cable ipv4.addresses \
    192.168.0.10/24 ipv4.gateway 192.168.0.1 \
    connection.autoconnect true ipv4.dns '8.8.8.8,1.1.1.1' \
    type ethernet ifname eth0 ipv4.method manual

Connect a device to a wifi SSID, prompting for the password:

    $ sudo nmcli –ask device wifi connect SSID-Name

For more wifi options look at:

    $ nmcli device wifi help

&#42; Fedora Quick Docs: [Configuring ip networking with
nmcli](https://docs.fedoraproject.org/en-US/quick-docs/configuring-ip-networking-with-nmcli/)

## Securing remote access {#_securing_remote_access}

The root account is locked by default with no password set. The SSH
daemon is configured with password authentication disabled for the root
account and only allows access remotely if an ssh key has been added.

Disable remote ssh access for root by editing the following line in the
&#96;/etc/ssh/sshd_config&#96; file:

    PermitRootLogin no

To disable password authentication for all users, edit
&#96;/etc/ssh/sshd_config&#96; file and add the following:

    PasswordAuthentication no

View the default firewall configuration:

    $ sudo firewall-cmd --list-all

The &#96;firewalld&#96; services are different than &#96;systemd&#96;
services. To see what configuration a &#96;firewalld&#96; service
includes use:

    $ sudo firewall-cmd --info-service=mdns
    mdns
    ports: 5353/udp
    protocols:
    source-ports:
    modules:
    destination: ipv4:224.0.0.251 ipv6:ff02::fb

Use the &#96;\--add-service&#96; or &#96;\--add-port&#96; options to
open ports in the firewall:

    $ sudo firewall-cmd --add-port=8080/tcp --add-port=8081/tcp --permanent
    $ sudo firewall-cmd --reload

The &#96;\--permanent&#96; option saves the setting to files so that
they will be loaded the next time &#96;firewalld&#96; is loaded. The
&#96;\--reload&#96; option reloads the configuration from the saved
files. If you add a port or service without the &#96;\--permanent&#96;
option, it will modify the runtime firewalld settings but it will not
save your changes to survive a reboot of the system.

&#42; Fedora Quick Docs: [Using
firewalld](https://docs.fedoraproject.org/en-US/quick-docs/firewalld/)

## Service Management {#_service_management}

Services are managed by &#96;systemd&#96; and they can be started and
enabled with &#96;systemctl&#96;.

The Fedora IoT image boots to a multi-user target by default.

    $ systemctl get-default
    multi-user.target

A small number of services are enabled:

    $ systemctl list-unit-files  --state enabled

Package installation does not usually start or enable a service:

    $ systemctl status httpd
    ● httpd.service - The Apache HTTP Server
    Loaded: loaded (/usr/lib/systemd/system/httpd.service; disabled; vendor preset: disabl\&gt;
    Active: inactive (dead)
    Docs: man:httpd.service(8)

The &#96;\--now&#96; option allows you to start a service on the enable
command:

    $ sudo systemctl enable httpd --now
    Created symlink /etc/systemd/system/multi-user.target.wants/httpd.service → /usr/lib/systemd/system/httpd.service.

&#42; Fedora Quick Docs: [Understanding and administering
systemd](https://docs.fedoraproject.org/en-US/quick-docs/systemd-understanding-and-administering/)

## Viewing Logs {#_viewing_logs}

Log files are generally located in the &#96;/var/log&#96; directory.
System logs can be viewed and searched with &#96;journalctl&#96;.

&#42; Fedora Quick Docs: [Viewing logs in
Fedora](https://docs.fedoraproject.org/en-US/quick-docs/viewing-logs/)

## Editing Kernel Command Line Arguments {#_editing_kernel_command_line_arguments}

Sometimes it's useful to be able to edit the kernel command line
arguments, whether to add a serial console or some options for
debugging.

View the current kernel command line:

    $ sudo rpm-ostree kargs

Edit the kernel command line arguments with the default editor (the
default for editor is vim) to adjust such as adding a serial console:

    $ sudo rpm-ostree kargs --editor

Reboot the system:

    $ sudo systemctl reboot

## Remote Administration with Ansible {#_remote_administration_with_ansible}

The Fedora IoT image includes python3 and Ansible versions 2.5 and above
have support for Python 3 (python 3.5 and above only). To use Ansible to
configure your Fedora IoT device, set the ansible_python_interpreter
configuration option use the python3 binary &#96;/usr/bin/python3&#96;.
This is done with an inventory variable as described in the [Ansible
Python 3
Support](https://docs.ansible.com/ansible/latest/reference_appendices/python_3_support.html)
documentation.

The [Ansible User
Guide](https://docs.ansible.com/ansible/latest/user_guide/index.html)
covers how to work with Ansible. Some useful
[modules](https://docs.ansible.com/ansible/latest/user_guide/modules.html)
include:

&#42; Networks: nmcli &#42; Users: user, authorized_key, htpasswd &#42;
Packages, services and ports: yum_repository, service, firewalld &#42;
Files and directories: file, copy, template, get_url, unarchive &#42;
Interact with HTTP and HTTPS web services: uri &#42; System: timezone,
reboot

There is a community supported module for rpm-ostree,
[community.general.rpm_ostree_pkg](https://docs.ansible.com/ansible/latest/collections/community/general/rpm_ostree_pkg_module.html&#35;),
which can be used to add and remove overlays. You must install the
community.general collection to use this module.

    $ ansible-galaxy collection install community.general

Then the module can be used like so:

    - name: install cockpit
    community.general.rpm_ostree_pkg:
    name:
    - cockpit
    - cockpit-podman
    - cockpit-storaged
    - cockpit-ostree
    state: present
    register: result

    - name: reboot if new stuff was installed
    reboot:
    reboot_timeout: 300
    when: result.changed

    - name: start and enable cockpit
    service:
    name: cockpit.socket
    state: started
    enabled: true

    - name: allow cockpit through firewall
    firewalld:
    service: cockpit
    permanent: yes
    immediate: yes
    state: enabled

# Fedora IoT Bootc Images {#_fedora_iot_bootc_images}

As part of Fedora's initiative towards bootable containers, you can now
create Fedora IoT &#96;bootc&#96; images. These images use standard
OCI/Docker containers as transport but contain all components needed to
boot a Fedora IoT system. This allows you to ship updates to your Fedora
IoT system using container images.

&#96;bootc&#96; is part of the standard Fedora IoT distribution. After
[setting up a Physical Device](physical-device-setup.xml) you can use
the &#96;bootc&#96; tools to update the system.

Essentially, Fedora IoT &#96;bootc&#96; images retain all the
functionality you're used to in Fedora IoT, while leveraging the
flexibility and ease of maintenance provided by &#96;bootc&#96;.

For more information, please check out the [official bootc
documentation](https://docs.fedoraproject.org/en-US/bootc/), as well as
the [Fedora Bootc Base Images Git
repository](https://gitlab.com/fedora/bootc/base-images).

# Fedora IoT Bootc Image Example with Podman Machine {#_fedora_iot_bootc_image_example_with_podman_machine}

This example walks through building and booting a Fedora IoT
&#96;bootc&#96; image in a Podman machine.

:::: note
::: title
:::

This example is based on the Fedora &#96;bootc&#96; documentation about
building scratch images; reference the upstream docs
[here](https://docs.fedoraproject.org/en-US/bootc/building-from-scratch/&#35;_using_bootc_base_imagectl_build_rootfs)
for the latest version/information.
::::

To start, create a &#96;Containerfile.custom&#96; with the following
contents:

``` dockerfile
FROM quay.io/fedora-testing/fedora-bootc:rawhide-standard as builder
RUN /usr/libexec/bootc-base-imagectl build-rootfs --manifest=fedora-iot /target-rootfs

FROM scratch
COPY --from=builder /target-rootfs/ /
LABEL containers.bootc 1
ENV container=oci
STOPSIGNAL SIGRTMIN+3
CMD ['/sbin/init']
```

Initialize your Podman machine using the following command. You may skip
this step if you already have a Podman machine.

``` bash
podman machine init
```

Grant your Podman machine the permissions necessary to run your Fedora
IoT &#96;bootc&#96; image using:

``` bash
podman machine set --rootful
```

Start your Podman machine using:

``` bash
podman machine start
```

Use the following command to build your &#96;fedora-iot&#96; image:

``` bash
podman -c podman-machine-default-root build --cap-add=all --security-opt=label=disable \
--device /dev/fuse -t localhost/fedora-iot -f Containerfile.custom .
```

After building the &#96;localhost/fedora-iot&#96; image, you should be
able to see it in your Podman machine's list of images. Use the
following command to check:

``` bash
podman -c podman-machine-default-root images
```

:::: note
::: title
:::

The next step uses &#96;podman-bootc&#96;. If you need to install
&#96;podman-bootc&#96;, please follow the instructions in the
[podman-bootc repository](https://github.com/containers/podman-bootc)
::::

You're now ready to boot a virtual machine using your new Fedora IoT
&#96;bootc&#96; image. The command below will boot a VM in your current
terminal window, allowing you to test everything that Fedora IoT
&#96;bootc&#96; images have to offer:

``` bash
podman-bootc run --filesystem=ext4 localhost/fedora-iot
```

# Fedora IoT Bootc Image Example with Quay {#_fedora_iot_bootc_image_example_with_quay}

## Building and Booting a Fedora IoT Bootc Image {#_building_and_booting_a_fedora_iot_bootc_image}

This example walks through building and booting a Fedora IoT
&#96;bootc&#96; image using Quay.io, as well as pushing an update to a
booted Fedora IoT system.

:::: note
::: title
:::

This example is based on the Fedora &#96;bootc&#96; documentation about
building scratch images; reference the upstream docs
[here](https://docs.fedoraproject.org/en-US/bootc/building-from-scratch/&#35;_using_bootc_base_imagectl_build_rootfs)
for the latest version/information.
::::

:::: note
::: title
:::

This example assumes the user has a Quay account with the ability to
create custom repositories.
::::

To start, create a &#96;Containerfile.custom&#96; with the following
contents:

``` dockerfile
FROM quay.io/fedora-testing/fedora-bootc:rawhide-standard as builder
RUN /usr/libexec/bootc-base-imagectl build-rootfs --manifest=fedora-iot /target-rootfs

FROM scratch
COPY --from=builder /target-rootfs/ /
LABEL containers.bootc 1
ENV container=oci
STOPSIGNAL SIGRTMIN+3
CMD ['/sbin/init']
```

You're now ready to build a Fedora IoT &#96;bootc&#96; image using the
custom Containerfile you made earlier. Use this command:

``` bash
podman build --cap-add=all --security-opt=label=type:container_runtime_t \
--device /dev/fuse -t localhost/fedora-iot -f Containerfile.custom .
```

Then, tag your Fedora IoT &#96;bootc&#96; image:

``` bash
podman tag localhost/fedora-iot:latest quay.io/[quay repository name]:fedora-iot
```

Before pushing to Quay.io, you may need to log in:

``` bash
podman login quay.io
```

Push your new Fedora IoT &#96;bootc&#96; image to Quay.io using the
following command. Note that you may need to log in again:

``` bash
podman push quay.io/[quay repository name]:fedora-iot
```

:::: note
::: title
:::

The next step uses &#96;podman-bootc&#96;. If you need to install
&#96;podman-bootc&#96;, please follow the instructions in the
[podman-bootc repository](https://github.com/containers/podman-bootc)
::::

Now, boot your Fedora IoT &#96;bootc&#96; image. Open a new terminal
window and run:

``` bash
podman-bootc run --filesystem=ext4 quay.io/[quay repository name]:fedora-iot
```

&#96;podman-bootc&#96; will pull your image and boot it inside a VM in
the terminal window, allowing you to test everything Fedora IoT
&#96;bootc&#96; images have to offer.

## Pushing an Update to your Fedora IoT bootc system {#_pushing_an_update_to_your_fedora_iot_bootc_system}

After completing the tutorial above, you now have a functional Fedora
IoT &#96;bootc&#96; system! But what if you need to make a change?
Updating a &#96;bootc&#96; system is remarkably simple --- just follow
the steps below.

:::: note
::: title
:::

This tutorial assumes you have just completed the above tutorial, and
have access to a booted Fedora IoT &#96;bootc&#96; system.
::::

First, navigate to your cloned Fedora Bootc Base Images repository and
create a Containerfile named &#96;Containerfile.fix&#96; with your
desired changes.

Next, rebuild your &#96;localhost/fedora-iot&#96; image using the new
Containerfile:

``` bash
podman build --cap-add=all --security-opt=label=type:container_runtime_t \
--device /dev/fuse -t localhost/fedora-iot -f Containerfile.fix .
```

Tag your updated Fedora IoT &#96;bootc&#96; image:

``` bash
podman tag localhost/fedora-iot:latest quay.io/[quay repository name]:fedora-iot
```

Before pushing to Quay.io, you may need to log in:

``` bash
podman login quay.io
```

Push your updated Fedora IoT &#96;bootc&#96; image to Quay.io, using the
command below:

``` bash
podman push quay.io/[quay repository name]:fedora-iot
```

After successfully pushing, switch back to your virtual machine running
your Fedora IoT &#96;bootc&#96; image. Download and queue the updated
image for your next reboot:

``` bash
bootc upgrade
```

Run the following command to see your updated image staged for the next
reboot:

``` bash
bootc status
```

Reboot your Fedora IoT &#96;bootc&#96; system and use your new updated
image:

``` bash
reboot
```

After rebooting, you may need to SSH back into your Fedora IoT
&#96;bootc&#96; system. To do so, first list all &#96;podman-bootc&#96;
VMs:

``` bash
podman-bootc list
```

Then find the ID of your desired machine and run the following:

``` bash
podman-bootc ssh [ID]
```

After reconnecting, run check the status again:

``` bash
bootc status
```

Your updated image should now show up as &#96;Booted&#96;, and the
previous image as &#96;Rollback&#96;. You have successfully updated your
Fedora IoT bootc system!

# Fedora IoT Bootc Example with Raspberry Pi {#_fedora_iot_bootc_example_with_raspberry_pi}

Using &#96;bootc&#96; with Fedora IoT currently requires that you have
already provisioned a device with Fedora IoT.

Follow the instructions in [Physical Device
Setup](physical-device-setup.xml) to provision Fedora IoT to your
Raspberry Pi.

Once the Raspberry Pi is provisioned successfully, you can create a
custom Fedora &#96;bootc&#96; image.

## Build a custom Fedora Bootc image and push it to a registry {#_build_a_custom_fedora_bootc_image_and_push_it_to_a_registry}

To build your own image on your host you can create a Containerfile.
This example just copies a file to &#96;/etc&#96;.

:::: note
::: title
:::

this example uses the Fedora &#96;bootc&#96; base image and does not
include all of the RPMs included as part of Fedora IoT.
::::

``` dockerfile
FROM quay.io/fedora/fedora-bootc:latest
COPY files/secret /etc
```

To build and push the image with &#96;podman&#96; run the following on
the host:

``` bash
podman build --platform linux/arm64 -t quay.io/username/bootc-test-image:latest
podman push quay.io/username/bootc-test-image:latest
```

This example uses [Quay.io](https://quay.io/) as the registry; you may
need additional configuration to push to the registry you are using.

## Switch the Raspberry Pi to your custom image {#_switch_the_raspberry_pi_to_your_custom_image}

On the Raspberry Pi you can now switch to your custom image with the
&#96;bootc switch&#96; command.

``` bash
bootc switch quay.io/username/bootc-test-image:latest
```

After rebooting the Raspberry Pi, the file copied as part of the
Containerfile should be present in the filesystem:

``` bash
cat /etc/secret
```

# Contribute to Fedora IoT Edition {#_contribute_to_fedora_iot_edition_2}

Fedora IoT is made up of many components, including a lot that are part
of the main Fedora project, so there is a number of places where you may
contribute. This is by no means a canonical source for contribution, if
you don't see an area where which seems to match please see the getting
help section for general ways to engage with us to get answers to your
questions.

If you're interested in joining the Fedora IoT Working Group, check out
the [IoT WG docs](iot-wg::index.xml).

## Reporting IoT bugs {#_reporting_iot_bugs}

If you are seeing issues with software that is included in the Fedora
IoT Edition that is not necessarily specific to IoT the bug should be
reported against the specific Fedora component. There's details on how
to do that in the [how to file a
bug](https://docs.fedoraproject.org/en-US/quick-docs/bugzilla-file-a-bug/)
doc.

If you know which component the bug is in, file a bug in [Red Hat
Bugzilla](https://bugzilla.redhat.com) against the *Fedora* product and
the component in question. Set the bug to block the [IoT Bugzilla
tracker](https://bugzilla.redhat.com/show_bug.cgi?id=IoT).

If you don't know which component to use or would to request a new
package or feature be added to Fedora IoT, you can file an issue in the
[IoT Distro](https://github.com/fedora-iot/iot-distro/issues/new/choose)
Issue tracker in Github.

## Getting IoT help {#_getting_iot_help}

We primarily communicate by the [Fedora IoT mailing
list](https://lists.fedoraproject.org/admin/lists/iot.lists.fedoraproject.org/)
and the [&#35;fedora-iot IRC channel on
Libera.Chat](https://web.libera.chat/?channel=&#35;fedora-iot) (bridged
to [&#35;iot on
chat.fedoraproject.org](https://matrix.to/&#35;/&#35;iot:fedoraproject.org)).

## Weekly meetings {#_weekly_meetings}

We meet every Wednesday 14:00UTC (10:00EST) in the [Fedora meeting room
on Matrix](https://matrix.to/&#35;/%23meeting:fedoraproject.org). Feel
free to hop in and join the discussion!

# Reference Platforms {#_reference_platforms}

Fedora IoT supports the aarch64 (arm64) and x86_64 architectures.

We only actively support UEFI plaforms so if your device doesn't boot
with UEFI it probably won't work.

These reference platforms have been tested and are known to work with
Fedora IoT, however their inclusion on this list does not necessarily
constitute a release-blocking issue should a bug that is specific to the
hardware below be found.

The currently tested reference devices are as follows:

## aarch64 (arm64) architecture {#_aarch64_arm64_architecture}

+-----------------------------------------------------------------------+
| <figure>                                                              |
| <img src="ARM1605_SystemReadyStandardStamplogo_SR_V1.png"             |
| alt="ARM1605 SystemReadyStandardStamplogo SR V1" />                   |
| <figcaption>SystemReady-SR Server Ready (SBSA/SBBR)</figcaption>      |
| </figure>                                                             |
+-----------------------------------------------------------------------+
| <figure>                                                              |
| <img src="ARM1605_SystemReadyStandardStamplogo_ES_V1.png"             |
| alt="ARM1605 SystemReadyStandardStamplogo ES V1" />                   |
| <figcaption>SystemReady-ES Embedded System Ready</figcaption>         |
| </figure>                                                             |
+-----------------------------------------------------------------------+
| <figure>                                                              |
| <img src="ARM1605_SystemReady_logo_IR_V1.png"                         |
| alt="ARM1605 SystemReady logo IR V1" />                               |
| <figcaption>SystemReady-IR IoT Ready</figcaption>                     |
| </figure>                                                             |
+-----------------------------------------------------------------------+
| <figure>                                                              |
| <img src="tianocore-logo.svg" alt="tianocore logo" />                 |
| <figcaption>KVM based VM (TianoCore UEFI)</figcaption>                |
| </figure>                                                             |
+-----------------------------------------------------------------------+
| <figure>                                                              |
| <img src="nvidia-jetson-agx-xavier-devkit.png"                        |
| alt="nvidia jetson agx xavier devkit" />                              |
| <figcaption>NVidia Jetson Xavier Series</figcaption>                  |
| </figure>                                                             |
+-----------------------------------------------------------------------+
| <figure>                                                              |
| <img src="nvidia-jetson-agx-orin-devkit.png"                          |
| alt="nvidia jetson agx orin devkit" />                                |
| <figcaption>NVidia Jetson Orin Series</figcaption>                    |
| </figure>                                                             |
+-----------------------------------------------------------------------+
| <figure>                                                              |
| <img src="raspberry-pi4.png" alt="raspberry pi4" />                   |
| <figcaption>Raspberry Pi 4 (4B/CM4)</figcaption>                      |
| </figure>                                                             |
+-----------------------------------------------------------------------+
| <figure>                                                              |
| <img src="raspberry-pi3b.png" alt="raspberry pi3b" />                 |
| <figcaption>Raspberry Pi 3 (3B/3B+/3CM)</figcaption>                  |
| </figure>                                                             |
+-----------------------------------------------------------------------+
| <figure>                                                              |
| <img src="ROCK960_Front_SD.png" alt="ROCK960 Front SD" />             |
| <figcaption>96boards Rock960 Consumer Edition</figcaption>            |
| </figure>                                                             |
+-----------------------------------------------------------------------+
| <figure>                                                              |
| <img src="hummingboard-pulse.png" alt="hummingboard pulse" />         |
| <figcaption>Solid Run HummingBoard-M (i.MX8 based)</figcaption>       |
| </figure>                                                             |
+-----------------------------------------------------------------------+
| <figure>                                                              |
| <img src="ROCKPro64-SBC-3.jpg" alt="ROCKPro64 SBC 3" />               |
| <figcaption>Pine64 Rockpro64 and Rock64</figcaption>                  |
| </figure>                                                             |
+-----------------------------------------------------------------------+
| <figure>                                                              |
| <img src="PINEA64_LTS_board_front.jpg"                                |
| alt="PINEA64 LTS board front" />                                      |
| <figcaption>Pine64 A64-LTS and SoPine</figcaption>                    |
| </figure>                                                             |
+-----------------------------------------------------------------------+

## x86_64 architecture {#_x86_64_architecture}

+-----------------------------------------------------------------------+
| <figure>                                                              |
| <img src="tianocore-logo.svg" alt="tianocore logo" />                 |
| <figcaption>KVM based VM (TianoCore UEFI)</figcaption>                |
| </figure>                                                             |
+-----------------------------------------------------------------------+
| <figure>                                                              |
| <img src="fitlet2.png" alt="fitlet2" />                               |
| <figcaption>Compulabs Fitlet2</figcaption>                            |
| </figure>                                                             |
+-----------------------------------------------------------------------+
| <figure>                                                              |
| <img src="up_squared.png" alt="up squared" />                         |
| <figcaption>Up Squared</figcaption>                                   |
| </figure>                                                             |
+-----------------------------------------------------------------------+
| <figure>                                                              |
| <img src="intel-x86.png" alt="intel x86" />                           |
| <figcaption>Generic Intel x86-64 products with UEFI</figcaption>      |
| </figure>                                                             |
+-----------------------------------------------------------------------+
|                                                                       |
+-----------------------------------------------------------------------+
|                                                                       |
+-----------------------------------------------------------------------+

Other devices should work, but aren't being actively tested in the
context of IoT. The list of supported reference devices will expand with
time.

## Required resources {#_required_resources_3}

The images being created are currently 4GB in size. The current memory
used for testing is 1GB of RAM. The Fedora IoT base image should run
with less, but of course this limits the amount of container
applications that can be run on top of the base OS.

# IoT Product Requirement Document {#_iot_product_requirement_document}

## Document Purpose and Overview {#_document_purpose_and_overview}

## What this document describes {#_what_this_document_describes}

This is the [Product Requirements
Document](http://en.wikipedia.org/wiki/Product_requirements_document)
for Fedora IoT. It:

&#42; Provides a high-level market overview of the IoT market as it
pertains to Fedora IoT; this includes items which may not be within our
actual scope/ability to accomplish at the current time. &#42; Provides
deeper understanding of the types of users who could use Fedora for
their IoT needs. This includes describing their main day-to-day tasks,
common problems, etc. The perspective here is not necessarily limited to
system administrators, or developers, but a combination of many types of
users and roles. &#42; Ties common issues and needs of potential
users/consumers of Fedora IoT to high-level product needs, from a
\'functional\' standpoint.

This document does not dictate implementation details. The goals in this
document will drive the continued implementation of this Edition.

### Fedora IoT Vision Statement {#_fedora_iot_vision_statement}

Fedora is the default platform in the IoT space. Anyone starting an IoT
project, from cute embedded hacks all the way up to a multi-million
device deployment will start with Fedora.

### Fedora IoT Mission Statement {#_fedora_iot_mission_statement}

Fedora IoT makes Fedora the default for open source innovation on IoT
hardware, endpoint, edge, middleware, cloud, and backend platforms.

## Market Opportunity {#_market_opportunity}

The IoT market is relatively immature and rapidly expanding. [Analysts
predict](https://www.forbes.com/sites/louiscolumbus/2017/12/10/2017-roundup-of-internet-of-things-forecasts/&#35;5af4bc1b1480)
the global market will grow to \$457B in 2020, representing an
annualized growth rate of nearly 30%. Fedora IoT has opportunity for
adoption as the market expands to in number and innovation.

IoT uses span from trivial toy projects to home automation to industrial
control to autonomous driving. IoT devices present several challenges
compared to general-purpose computing:

&#42; Resource-constrained devices &#42; Security risks due to default
passwords and short maintenance lifecycles &#42; Data management and AI
requirements at the edge

## Edition Objectives {#_edition_objectives}

### Primary Objective {#_primary_objective}

The initial Fedora IoT Objective consists of a base edition released on
a regular monthly cycle that can be used for running IoT devices:

&#42; Endpoint &#42; Edge &#42; Middleware &#42; Gateway &#42; Network,
storage and other appliances

The base edition will support multiple architectures, initially
including x86_64, aarch64 and ARMv7, and include the ability to produce
supported containers across all architectures for various IoT use-cases
and verticals. These containers will be capable of running on the Fedora
IoT base edition, and subsequently also running on Kubernetes platforms
such as OpenShift to provide end to end IoT platforms.

Demos for a number of use cases will be provided including orchestration
to deploy demos, container recipe example to create IoT application
stacks to run on Fedora IoT.

Future plans for the IoT Objective include complex End to end IoT use
cases including end points, messaging, data lakes and analysis,
including appropriate orchestration.

### Secondary Objectives {#_secondary_objectives}

Aside from the adoption and development of applications on top of the
Fedora IoT platform, we have a few secondary goals that should be helped
by wider adoption:

&#42; Encourage engagement in the Fedora ecosystem from the wider IoT
audience, including hardware vendors, other open source projects,
hobbyists, and students &#42; Positive press coverage from general media
and IoT-specific media &#42; Improvements to projects and technologies
used by the Fedora IoT objective that can benefit the upstream projects
and Fedora as a whole

## User Profiles, Primary Use Cases and Goals {#_user_profiles_primary_use_cases_and_goals}

### Personas {#_personas}

We will use a set of personas to describe our target users and their
respective needs. This document will list the personas in their
simplified forms, with detailed explanations of each one available on
their respective wiki pages.

&#42; IoT hobbyist and systems administrator &#42;&#42; Uses IoT devices
to experiment with technology. This could be a home user using platforms
such as Mozilla Web of Things Gateway or Home Assistant to do home
automation or a systems administrator experimenting with IoT
technologies. &#42; Makers and hobbyists &#42;&#42; Uses SBCs such as
the Raspberry Pi to experiment with robotics, control of devices or to
retrofit and improve other technologies. &#42; Partners &#42;&#42;
Companies that wish to support Fedora IoT on their devices to provide
options for their customers when building IoT platforms and products
&#42; Companies &#42;&#42; Companies that wish to use Fedora IoT as a
basis for their IoT product or platform &#42; Security and Data
Protection &#42;&#42; Security and data protection officers. &#42;&#42;
End to end traceability and demonstrable security at every level
&#42;&#42; Security researchers

### Use Cases {#_use_cases}

There's a lot of possible use-cases that Fedora IoT will need to
address. IoT is a vast array of verticals and it's impossible to address
all of them with a small community. The aim for Fedora IoT is to provide
a good and generic base for which to build any IoT platform. Fedora IoT
will need to address the following use-cases:

&#42; Base platform &#42;&#42; Extremely thin profile &#42;&#42; Use
CoreOS/ostree technologies to provide thin update deltas with roll back
capability to provide as close to a non brickable platform as possible.
&#42;&#42; Uses the latest linux technologies to tighten the security as
possible &#42;&#42; Provides low resource industry standard container
platform &#42;&#42; Supports a wide variety of hardware including
reference platforms, wired and wireless interfaces, and other hardware
interfaces such as FPGA and cameras &#42;&#42; pluggable system to
detect success/failure of upgrades and to role back to ensure system is
always working &#42; Home gateway &#42;&#42; Mozilla Web of Things
Gateway &#42;&#42; Home assistant &#42; Industrial Gateway &#42;&#42;
Numerous options available. &#42;&#42; EdgeX &#42;&#42; OPC UA open62541
&#42; Data storage and representation &#42;&#42; Open Source data lake
for IoT ingestion &#42;&#42; Open alternatives to some of the cloud
providers &#42;&#42; Messaging support such as MQTT and AMQP &#42;&#42;
Data analytics

### Core services and features {#_core_services_and_features}

&#42; Greenboot

### Core applications {#_core_applications}

None

### Unique policies for installation, updates, etc {#_unique_policies_for_installation_updates_etc}

None

## Logistical Concerns {#_logistical_concerns}

### Delivery Mechanisms {#_delivery_mechanisms}

Fedora IoT will produce a rolling release with monthly snapshots using
Fedora Core OS. The working group will coordinate with Fedora Release
Engineering to ensure monthly snapshots are produced and distributed in
a supportable manner.

### Documentation {#_documentation}

The IoT working group will work with the Documentation team to produce
IoT-specific documentation for users and developers.

#### Where to obtain {#_where_to_obtain}

Users will be able to obtain these images from the Fedora Project
website and mirror networks.

### Measuring Success {#_measuring_success}

In order to measure success we will monitor (somewhat arbitrary) numbers
over time. The list of metrics we take in account will be adapted over
time to measure specific efforts within the framework of the Server
Working Group goals.

The initial basic set of metrics will be:

&#42; At least one large hardware vendor uses Fedora IoT as the basis
for their platform.

### Scope of hardware support {#_scope_of_hardware_support}

See [Reference Platforms](../reference-platforms.xml).

### Release deliverables {#_release_deliverables}

+-----------------+-----------------+-----------------+-----------------+
| &               | &#              | &#              | &#42;&#42;Max   |
| #42;&#42;Delive | 42;&#42;Release | 42;&#42;Optical | size&#42;&#42;  |
| rable&#42;&#42; | blo             | boot is         |                 |
|                 | cking&#42;&#42; | blo             |                 |
|                 |                 | cking&#42;&#42; |                 |
+-----------------+-----------------+-----------------+-----------------+
| IoT/            | yes             | no              | N/A             |
| aarch64/images/ |                 |                 |                 |
| Fedora-IoT-*REL |                 |                 |                 |
| EASE_MILESTONE* |                 |                 |                 |
| .aarch64.raw.xz |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| IoT/aarch       | yes             | no              | N/A             |
| 64/iso/Fedora-I |                 |                 |                 |
| oT-IoT-ostree-a |                 |                 |                 |
| arch64-*RELEASE |                 |                 |                 |
| _MILESTONE*.iso |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| IoT/arm         | no              | no              | N/A             |
| hfp/iso/Fedora- |                 |                 |                 |
| IoT-IoT-ostree- |                 |                 |                 |
| armhfp-*RELEASE |                 |                 |                 |
| _MILESTONE*.iso |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| Io              | yes             | no              | N/A             |
| T/x86_64/images |                 |                 |                 |
| /Fedora-IoT-*RE |                 |                 |                 |
| LEASE_MILESTONE |                 |                 |                 |
| *.x86_64.raw.xz |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| IoT/x86         | yes             | no              | N/A             |
| _64/iso/Fedora- |                 |                 |                 |
| IoT-IoT-ostree- |                 |                 |                 |
| x86_64-*RELEASE |                 |                 |                 |
| _MILESTONE*.iso |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

## About this Document {#_about_this_document}

### Authors {#_authors}

Contributors to this document include:

&#42; bcotton &#42; mattdm &#42; pbrobinson

# Fedora IoT Working Group {#_fedora_iot_working_group}

This page documents the Standard Operating Procedures for the IoT
working group in Fedora.

## Standard Operating Procedures {#_standard_operating_procedures}

&#42; [Branching Fedora IoT](sop-branching-fedora-iot.xml) &#42;
[Attending/Running IoT WG Weekly Meetings](iot-weekly-meetings-sop.xml)

# Branching Fedora IoT {#_branching_fedora_iot}

Branched is the name given to a version of Fedora that has \'branched\'
from the rolling Rawhide tree and will become the next stable Fedora
release. This document will detail the steps for branching Fedora IoT
from Rawhide.

To complete these steps and open any pull requests you need a valid
[Fedora
account](https://docs.fedoraproject.org/en-US/fedora-accounts/user/).

## Working with the pungi-iot repository {#_working_with_the_pungi_iot_repository}

Clone and fork the Fedora IoT Pungi repository to make changes to the
configuration files used to build Fedora IoT.

    git clone https://pagure.io/fedora-iot/pungi-iot.git

Create the new branch and push to the upstream repository. Change
&#96;\$release&#96; to the new numeric branch of Fedora. This is not
done as a PR and should be pushed directly to the upstream repository,
to do so you will need commit permissions.

    git checkout main; git pull; git checkout -b f$release; git push --set-upstream upstream f$release

Example, used for Fedora 40:

    git checkout main; git pull; git checkout -b f40 ; git push --set-upstream upstream f40

### Rawhide (main) {#_rawhide_main}

On your local fork, create a new branch for changes to Rawhide (main).

Update the signing key for Rawhide from the main [Fedora Pungi
repo](https://pagure.io/pungi-fedora/commits/main). As of Fedora 40
branching you can find this
[here](https://pagure.io/pungi-fedora/blob/main/f/fedora.conf&#35;_21).

Copy the key used in Rawhide to &#96;fedora-iot.conf&#96;, replacing the
previous key.

Example:

    sed -i 's|$OLD_SIGNING_KEY|$NEW_RAWHIDE_KEY|g' fedora-iot.conf

Example used in Fedora 40 branching:

    sed -i 's|a15B79cc|e99d6ad1]|g' fedora-iot.conf

Main will remain as \'Rawhide\', but we need to update the release to
the next version of Fedora.

    sed -i 's|40|41|g' fedora-iot.conf nightly.sh sync-release.sh twoweek-nightly.sh

Commit the changes:

    git commit -a -m 'F-41: Update for branching' -s

Review the changes and if satisfied, push to your fork and open a pull
request for others to review. [Example
PR](https://pagure.io/fedora-iot/pungi-iot/c/db00b44a9ddf0eb37c4194b089bbea799cb3ecb6?branch=main)

### Branched (the next stable fedora release) {#_branched_the_next_stable_fedora_release}

Now we need to work on the new release, or branch of Fedora that we
created at the beginning, and specify the release number (eg \'40\')
rather than \'Rawhide\'.

Example:

    git checkout f$release

Used in Fedora 40 branching:

    git checkout f40

On your local fork, create a new branch for changes.

Update symlinks to ensure we are using the latest completed upstream
compose in Fedora

    sed -i 's|latest-Fedora-Rawhide|latest-Fedora-40|g' fedora-iot.conf

Update Fedora URLS with \'branched\':

    sed -i 's|compose/rawhide|compose/branched|g' fedora-iot.conf

Update iot repos to use \'devel\' rather than \'rawhide\':

    sed -i 's|fedora/rawhide/|fedora/devel/|g' fedora-iot.conf

Update instances of \'main\' to the release:

    sed -i 's|main|f40|g' fedora-iot.conf

:::: important
::: title
:::

You will need to manually change the comps and bootc
&#96;base-images&#96; repos back to main. There are no branches in comps
or &#96;base-images&#96;. (comps files are XML files used by various
Fedora tools to perform grouping of packages into functional groups. For
more information visit [click here](https://pagure.io/fedora-comps).
::::

Update the \'global_ksurl\':

    sed -i 's|=HEAD|=origin/f40|g' fedora-iot.conf

Update the location of where the release is copied to during the compose
process, and hosted for download and rsync'ing to the various Fedora
mirrors. This path is created when the &#96;twoweek-nightly.sh&#96; is
executed and can be found on the [Fedora Project master
mirror](https://dl.fedoraproject.org/pub/alt/iot/).

    sed -i 's|/pub/alt/iot/rawhide/|/pub/alt/iot/branched/|g' twoweek-nightly.sh

Commit the changes:

    git commit -a -m 'F-40: Update for branching' -s

Review the changes and if satisfied, push to your fork and open a pull
request for others to review. [Example
PR](https://pagure.io/fedora-iot/pungi-iot/c/8793fd5b80e3c269bac84cda175f5bf9987eea99?branch=f40)

## Working with the OStree repository {#_working_with_the_ostree_repository}

This repository is used to configure the Fedora IoT ostree and includes
the packages, services and various settings including selinux and
unified-core.

Clone and fork the upstream ostree repository:

    git clone https://pagure.io/fedora-iot/ostree.git

Create the new branch and push to the upstream repository. Change
&#96;\$release&#96; to the new numeric branch of Fedora:

    git checkout main; git pull; git checkout -b f$release; git push --set-upstream upstream f$release

Example, used for Fedora 40 (the next stable release of Fedora):

    git checkout main; git pull; git checkout -b f40 ; git push --set-upstream upstream f40

### Rawhide (main) {#_rawhide_main_2}

Create a branch in your local fork and make the following changes for
Rawhide:

    sed -i 's|40|41|g' config.ini fedora-40.repo fedora-iot-base.yaml fedora-iot.yaml
    mv fedora-40.repo fedora-41.repo
    git add fedora-41.repo
    git commit -a -m 'IoT: Update rawhide for F-41' -s

Review the changes and if satisfied, push to your fork and open a pull
request for others to review.

### Branched (the next stable fedora release) {#_branched_the_next_stable_fedora_release_2}

Checkout the newly created branch for the next stable Fedora and create
a branch in your fork for the PR.

Change the urls from &#96;development/rawhide&#96; to
&#96;development/40&#96;:

    sed -i 's|development/rawhide|development/40|g' config.ini

Update instances of &#96;rawhide&#96;, replacing with &#96;devel&#96;:

    sed -i 's|rawhide|devel|g' config.ini fedora-40.repo fedora-iot-base.yaml fedora-iot.yaml fedora-iot-updates-stable.yaml fedora-iot-updates-testing.yaml

Write the commit message:

    git commit -a -m 'Setup for F-40 branched' -s

Review the changes and if satisfied, push to your fork and open a pull
request for others to review.

## Additional Checks {#_additional_checks}

&#42; check to make sure the Fedora IoT tag has been created in koji. To
verify you will need to install the &#96;koji&#96; package in Fedora
&#42;&#42; Verify the tags are listed for the new branches &#96;koji
list-tags\|grep f&#42;-iot&#96;

&#42; ensure the signing key has been updated in Ansible (look for the
iot portion) &#42;&#42; <https://pagure.io/fedora-infra/ansible>
&#42;&#42; As of Fedora 40 you can find the relevant section
[here](https://pagure.io/fedora-infra/ansible/blob/main/f/roles/robosignatory/templates/robosignatory.toml.j2=_434).
&#42; Make sure to update Ansible and create a cron job for the
development (devel) release. You can find cron jobs
[here](https://pagure.io/fedora-infra/ansible/blob/main/f/roles/releng/files).
&#42; Create a treefile in the &#96;base-images&#96; and
&#96;fedora-iot-bootc&#96; repositories pointing to the newly branched
release. This may be obsolete with the move to Konflux. An example of
the treefile used for Fedora 41 composes can be found
[here](https://gitlab.com/fedora/bootc/base-images/-/blob/main/fedora-41.yaml?ref_type=heads).
Branched composes use &#96;fedora-devel&#96;.

You will need to create the file as it gets removed at Final. Example
for &#96;devel-iot&#96; (IMPORTANT - Make sure to update the branched
used, in the example it's &#96;f41&#96;):

    \&#35; IoT devel compose
    MAILTO=releng-cron@lists.fedoraproject.org
    00 14 \&#42; \&#42; \&#42; root touch /tmp/fedora-compose-devel-iot \&amp;\&amp; TMPDIR=\&#96;mktemp -d /tmp/devel.XXXXXX\&#96; \&amp;\&amp; cd $TMPDIR \&amp;\&amp; git clone https://pagure.io/fedora-iot/pungi-iot.git \&amp;\&amp; cd pungi-iot \&amp;\&amp; git checkout f41 \&amp;\&amp; ./twoweek-nightly.sh RC-$(date '+\%Y\%m\%d').0 \&amp;\&amp; rm /tmp/fedora-compose-devel-iot

Add it to the IoT section of main.yml found
[here](https://pagure.io/fedora-infra/ansible/blob/main/f/roles/releng/tasks/main.yml):

    \&#35; put cron job in for IoT devel compose
    - name: IoT devel compose cron
    ansible.builtin.copy:
    src: devel-iot
    dest: /etc/cron.d/devel-iot
    mode: '644'
    when: inventory_hostname.startswith('compose-iot01.iad2')

# Create Fedora IoT Release Candidates {#_create_fedora_iot_release_candidates}

To complete these steps you will need a valid [Fedora
account](https://docs.fedoraproject.org/en-US/fedora-accounts/user/),
with appropriate permissions in
[Koji](https://koji.fedoraproject.org/koji/), the Fedora buildsystem.

Review the current compose tag used for Fedora IoT and what is currently
tagged and included.

    koji list-tagged f[release_version]-iot

Untag any builds currently included:

    koji untag-build --all f[release_version]-iot [build1 build2 \&#8230;]

Review the upstream Fedora ticket requesting the Release Candidates for
a listing of all Fedora release Blockers and Freeze Exceptions that are
needed for the compose. &#42; An example ticket for [Fedora 40 Beta
Candidate Request](https://pagure.io/releng/issue/12007). &#42; An
example ticket for [Fedora 40 Final Candidate
Request](https://pagure.io/releng/issue/12060).

Add any builds specified by the Fedora QE team.

    koji tag-build f[release_version]-iot [build1 build2 \&#8230;]

Compare the tagged builds with the Fedora compose tag (f40-compose):

    koji list-tagged f[release_version]-compose

Log into the Fedora IoT compose host and run the compose for the pending
release. Once the compose is complete, review the results for any
outstanding deliverables.

## Once the release has been declared &#96;Go!&#96; {#_once_the_release_has_been_declared_96go96}

### Beta {#_beta}

When the release is signed off on Thursday after the Go/No-Go meeting.
Open a ticket with [Release
Engineering](https://pagure.io/releng/issues) to sign the deliverables.
A request [example](https://pagure.io/releng/issue/11677) from Fedora
39.

Once the release is signed, from the compose host create the directory
and run the script to copy the release so it can be sync'd to the Fedora
mirrors.

For the Beta release, note the destintation is the &#96;test&#96;
directory:

    mkdir /pub/alt/iot/test/[release_version]
    ./sync-release.sh

### Final {#_final}

The final release requires an additional compose moving the
&#96;development&#96; release to &#96;stable&#96;.

#### Update the signing key {#_update_the_signing_key}

Open a pull request to update the signing key for the specified release.
Example from [Fedora 41
GA](https://pagure.io/fedora-infra/ansible/pull-request/2325).

#### Update Pungi configuration {#_update_pungi_configuration}

Create a local fork of the Fedora [IoT Pungi
repository](https://pagure.io/fedora-iot/pungi-iot.git) to make changes
to the configuration files used to build Fedora IoT.

Update the the URL used for the compose, moving from &#96;latest&#96; to
the compose declared Gold in the Go/NoGo meeting. This example uses the
Fedora 41 GA compose:

    sed -i 's|branched/latest-Fedora-41/|41/Fedora-41-20241024.0/|g' fedora-iot.conf

Next update the branch from &#96;devel&#96; to &#96;stable&#96;:

    sed -i 's|fedora/devel/|fedora/stable/|g' fedora-iot.conf

Update the &#96;sync-bootc-base-containers.sh&#96; script, moving the
development release to stable.

    sed -i 's|current_stable='40'|current_stable='41'|g' sync-bootc-base-containers.sh
    sed -i 's|current_devel='41'|\&#35;current_devel='41'|g' sync-bootc-base-containers.sh

Review changes and open a pull request for peer review.

#### Update the ostree repository {#_update_the_ostree_repository}

Update the [Fedora IoT ostree
repository](https://pagure.io/fedora-iot/pungi-iot.git) for the final
compose. Update the branch from &#96;devel&#96; to &#96;stable&#96; and
the release URL from branched to the release directory. The examples
below were used for Fedora 41 GA.

    sed -i 's|s/devel/%(arch)s/|s/stable/%(arch)s/|g' config.ini
    sed -i 's|fedora/devel/|fedora/stable/|g' \&#42;.yaml
    sed -i 's|fedora/linux/development/41|fedora/linux/releases/41|g' config.ini

Review changes and open a pull request for peer review.

#### Update Automated compose {#_update_automated_compose}

Ensure the cron job used to automate the compose for
&#96;stable-iot&#96; is updated to point to the correct
[branch](https://pagure.io/fedora-infra/ansible/blob/main/f/roles/releng/files/stable-iot)
for the new stable release and delete the cronjob used for the
development release, &#96;devel-iot&#96;.

#### Release compose {#_release_compose}

After the changes have been merged, complete the GA compose. Once
completed, open a ticket with [Release
Engineering](https://pagure.io/releng/issues) to sign the deliverables.
A request [example](https://pagure.io/releng/issue/11677) from Fedora
39.

#### Sync the Release {#_sync_the_release}

Once the release is signed, from the compose host create the directory
and run the script to copy the release so it can be sync'd to the Fedora
mirrors.

    mkdir /pub/alt/iot/[release_version]
    ./sync-release.sh
