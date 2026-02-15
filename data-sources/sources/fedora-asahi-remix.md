{variant-name} is installed from macOS. The minimum supported macOS
versions are 13.5 and 14.2. Due to macOS issues outside of our control,
you may be prompted to upgrade to 14.2 if you have an intermediate
version.

To install the latest release build, open up the terminal and run the
following as a regular user:

    $ curl https://fedora-asahi-remix.org/install | sh

Follow the prompts from the script and you'll have Fedora Asahi Remix
installed in no time.

If you want to install a nightly build and have more options available
(e.g. beta and previous releases), use this command instead:

    $ curl https://fedora-asahi-remix.org/builds | sh

# Troubleshooting {#_troubleshooting}

If your Mac is having trouble booting, here are some steps you can take
to identify the problem and resolve it.

First, identify what happens when you power on the computer and jump to
the appropriate section:

- The computer boots into macOS: [Changing the startup operating
  system](#boot-picker)

- The boot process fails in the U-Boot console screen with an error
  message mentioning a kernel or initramfs: [Entering the GRUB boot
  menu](#entering-grub)

- The boot process gets stuck in the U-Boot console: [Troubleshooting
  U-Boot issues](#uboot-troubleshoot)

- The boot process gets stuck in the m1n1 console, ending with
  `Running proxy…​`: [Troubleshooting m1n1 stage 2
  issues](#stage2-troubleshoot)

- The computer shows the Apple logo and then goes blank (laptops, iMacs)
  or there is no display output (desktops) but it does not reboot:
  [Upgrading or repairing m1n1 stage 1](#stage1-repair)

- The computer shows the Apple logo and a progress bar (laptops, iMacs)
  or no display output (desktops) and then reboots repeatedly, finally
  showing a recovery screen: [Upgrading or repairing m1n1 stage
  1](#stage1-repair)

- The computer shows an exclamation point icon and a support URL
  (laptops, iMacs) or the power LED blinks in an SOS pattern (desktops):
  [Recovering an unbootable machine](#machine-recovery)

## Changing the startup operating system {#boot-picker}

You can select which OS boots, either temporarily or permanently, by
using the system's built in Boot Picker. To do this, with the machine
fully powered down:

- Press and hold the power button

- Keep holding until the screen reads \"Entering startup options\"
  (laptops, iMacs) or the power LED dims slightly (desktops), then
  release.

This will display the Boot Picker, where you can select the next
operating system to boot. By default, the selection will be temporary.
To make your choice permanent for all subsequent boots, click on the
desired boot option while holding down the Option key on the keyboard.

You can also choose the rightmost \"Options\" icon to enter recoveryOS,
which you can use to perform recovery operations. You may be prompted
for your macOS login credentials, depending on the security state of
your machine. Once at the main recoveryOS options screen, you can open a
Terminal window by pressing Shift-Command-T.

## Entering the GRUB boot menu {#entering-grub}

If there is a problem during a kernel package upgrade or some other
issue that prevents the kernel from booting properly, you may need to
enter the GRUB menu to select a different kernel or alter boot options.

Server and Minimal installs should show the GRUB menu by default. For
desktop installs, you have to press Escape at the right time to enter
the GRUB menu. When the system boots, you will see the display cycle
through m1n1 (Asahi Linux or Fedora logos) and U-Boot (text screen with
U-Boot logo on the top right). The U-Boot screen will show a brief
countdown. Press Escape immediately **after** the countdown reaches 0 to
enter the GRUB boot menu.

From there, you can choose an older kernel version (e.g. to recover from
a failed kernel install), or change the boot options (e.g. to reset your
password or recover from other system issues).

## Troubleshooting U-Boot issues {#uboot-troubleshoot}

U-Boot can have trouble with certain kinds of USB devices. If you are
seeing strange behavior or logs from U-Boot, try disconnecting all USB
devices (except a single keyboard, for desktop machines).

If you are having trouble getting an external keyboard to work in the
U-Boot or GRUB menus, you may want to try using another USB port (e.g.
Type C with an adapter instead of Type A) or a different keyboard. As
U-Boot can only support a single keyboard, make sure no other USB
devices that emulate a keyboard are connected. This includes some USB
mice as well as certain USB tokens, barcode readers, etc. (YubiKeys
should already be excluded and ignored in U-Boot).

## Troubleshooting m1n1 stage 2 issues {#stage2-troubleshoot}

If the m1n1 console is displayed and shows a `Running proxy…​` message,
this typically means that m1n1 stage 1 had trouble loading m1n1 stage 2.

If this occurred after a system update, it is possible that the new
updated stage 2 binary was not installed correctly. You can boot into
macOS or recoveryOS (see the [Changing the startup operating
system](#boot-picker) section) and perform the following steps to revert
to the previous version of m1n1 stage 2 and U-Boot.

1.  Open a Terminal

2.  Type `diskutil list | grep EFI` to see the available EFI partitions

3.  The EFI partition will be named something similar to `EFI - FEDOR`.
    Make note of the identifier on the right, e.g. `disk0sX`.

4.  Type `sudo diskutil mount disk0sX` with the identifier you obtained
    above to mount the partition.

5.  Navigate to the mountpoint with `cd "/Volumes/EFI - FEDOR"`
    (replacing `EFI - FEDOR` with your volume name).

6.  Navigate to the `m1n1` subdirectory: `cd m1n1`.

7.  List the files with `ls`. There should be a `boot.bin` file and a
    `boot.bin.old` file.

8.  Rename the current file to an inactive name:
    `mv boot.bin boot.bin.new`.

9.  Rename the old file to the active name: `mv boot.bin.old boot.bin`.

If you are running under macOS, you may also perform the file management
steps with Finder. After mounting the partition with `diskutil`, it will
appear in the Finder sidebar.

After reverting `m1n1.bin`, boot back into {variant-name} to test the
reverted version of m1n1 stage 2 and U-Boot.

Note that reverting the m1n1 stage 2 binary to the previous version is
not guaranteed to work correctly, as sometimes there are incompatible
device tree changes that accompany kernel version updates. You may find
that some hardware does not work properly after the reversion. After a
successful boot into Linux, you should run `sudo update-m1n1` to update
to the current version, and reboot again.

## Upgrading or repairing m1n1 stage 1 {#stage1-repair}

Sometimes, the system's Boot Policy for {variant-name} might become
corrupted. This sometimes occurs after macOS upgrades (due to bugs in
Apple's upgrade process). If this happens, attempting to boot that
operating system will instead immediately reboot. If that OS is the
default boot OS, the computer will reboot repeatedly until it triggers
an OS recovery screen. If this happens, you need to restore m1n1 stage 1
and the associated Boot Policy.

It is also possible for a system firmware upgrade to trigger an
incompatibility in m1n1 stage 1, requiring an update. This can happen if
you update to macOS Sonoma 14.5 or later, with a m1n1 stage 1 older than
1.4.13 (released May 2024), due to a bug in those older m1n1 versions.
To resolve this, update m1n1 stage 1.

The process for both of the above situations is the same. First, follow
the steps in [Changing the startup operating system](#boot-picker) to
boot into recoveryOS (preferred) or macOS, and open a Terminal. Ensure
you are connected to the internet, and then run the {variant-name}
installer again, using the instructions in the
[Installation](installation.xml) page (or the steps available on
[asahilinux.org](https://asahilinux.org)). Once the installer starts,
one of the available options should be to
`Repair an incomplete installation` (`p`) or
`Upgrade m1n1 on an existing OS` (`m`). Choose the appropriate option
and follow the instructions to upgrade or reinstall m1n1 stage 1.

If you need to reinstall m1n1 stage 1 or otherwise reset the Boot Policy
but the installer does not prompt with either of the above two options,
you can run `bputil -f` and then select the UUID corresponding to the
installation that you wish to repair (this will be displayed when you
start up the installer, in the partition list). Follow the prompts to
reset your Boot Policy, which will erase the m1n1 bootloader and place
the installation into the \"incomplete\" state. Once this is complete,
you may follow the steps above again to launch the installer and select
the \"Repair\" option, which should now be available. We have heard some
reports that this situation can occur after machines are sent to Apple
for servicing.

## Recovering an unbootable machine {#machine-recovery}

If your machine is stuck displaying an exclamation mark icon (laptops
and iMacs) or SOS LED blink pattern (desktops), you may need to perform
a DFU Revive or Restore. To determine if this is necessary, first try to
boot using both the current paired recoveryOS and the System recoveryOS.

To boot using the current recoveryOS:

- Fully power down the machine

- Press and hold the power button

- Keep holding until the screen reads \"Entering startup options\"
  (laptops, iMacs) or the power LED dims slightly (desktops), then
  release.

To boot using the System RecoveryOS:

- Fully power down the machine

- Quickly press, release, and then press and hold the power button (the
  whole action should take less than half a second)

- Keep holding until the screen reads \"Entering startup options\"
  (laptops, iMacs) or the power LED dims slightly (desktops), then
  release.

If either of those processes succeeds and shows the Boot Picker, you can
choose an alternate OS to boot or select the \"Options\" icon to boot
recoveryOS and troubleshoot the issue or reinstall another OS from that
environment.

## Performing a DFU revive or restore {#dfu}

If your machine fails to boot or enter Startup Options, you may have to
perform a DFU Revive or Restore.

A DFU Revive will restore and update System Firmware and Recovery (SFR),
while leaving operating systems and data intact. This may be able to
resolve some issues, but is not guaranteed to work (e.g. a DFU Revive
cannot recover a missing System Recovery partition, but it **can**
reinstall recoveryOS into an existing but blank System Recovery
partition with the appropriate subvolume).

A DFU Restore will completely wipe all data on the internal storage and
restore the machine to factory condition. It is also the only way to
downgrade System Firmware to a prior version. This process can recover
from any kind of corruption or problem with the internal NVMe storage,
and even corruption of the internal NOR Flash storage and several other
firmware components. Note that if you perform a DFU Restore, you will
lose all data stored on the machine, and it will be returned to its
factory condition.

To perform a DFU Revive or Restore, you will need either another Mac
running macOS, or a Fedora Linux machine (any hardware) with an
available USB port. You will also need an appropriate USB cable to
connect both machines together.

### Performing a DFU revive or restore using another Mac running macOS {#_performing_a_dfu_revive_or_restore_using_another_mac_running_macos}

Follow [Apple's documentation](https://support.apple.com/en-us/108900)
to learn how to perform a restore using another Mac, using the macOS
Finder or Apple Configurator.

If you have trouble putting the machine into DFU mode, you may also wish
to refer to the instructions below.

### Performing a DFU revive or restore using a machine running Fedora Linux {#dfu-fedora}

You can also boot Fedora Linux on another machine (Intel compatible or
Apple Silicon both work), and then use `idevicerestore` to perform the
DFU Revive or Restore process.

If you have a spare x86-64 (Intel/AMD) machine that does not currently
have Fedora installed, you can follow the steps in the [next
section](#fedora-live-dfu) to temporarily live boot Fedora from a USB
stick and set up the environment to be able to perform the DFU
Revive/Restore. Once the system is up and running, return to this
section to continue the process.

You will need a compatible USB cable. If your host machine has Type A
ports, use a Type A to Type C cable. If your host machine has Type C
ports, use a Type C to Type C cable. You may also use a Type A to Type C
cable together with a female Type A to male Type C adapter. Your cable
must support data transfer (USB 2.0 480Mbps is sufficient, though USB 3
cables also work). Thunderboot 3 cables will not work, nor will
charge-only cables.

To perform a DFU Revive using a second Fedora machine, follow these
steps:

1.  Ensure you are connected to the Internet.

    - On Fedora Workstation, click on the top right menu bar icon to
      select a WiFi network (if not using wired Ethernet).

2.  Open a Terminal.

    - On Fedora Workstation, click on the top left menu icon, type
      \'terminal\' and hit Enter.

3.  Ensure you have at least 40GB of available disk space in the current
    working directory. If not, change to another directory that does or
    add additional storage as needed.

    - If you have followed the below steps to perform a live boot and
      configure your environment, this is already the case.

4.  Run the command `sudo dnf install -y idevicerestore usbmuxd` to
    install `idevicerestore`.

    - If the output indicates that `usbmuxd` was also installed as a
      dependency (and was not already installed), run
      `sudo udevadm control --reload` to reload the udev rules. Fedora
      Workstation live images should already have `usbmuxd` installed.

5.  Run the command `sudo dmesg -w` to show the live kernel log.

6.  Connect the USB cable between your host machine and the target
    machine to be restored. The cable must be connected to a specific
    USB port on the target machine:

    - For laptops, use the **leftmost** (rearmost) Type C port on the
      **left** side.

    - For iMacs, facing the rear of the machine, use the **rightmost**
      Type C port (closest to the power connector).

    - For Mac Mini machines, facing the rear of the machine, use the
      **leftmost** Type C port.

    - For Mac Studio machines, facing the rear of the machine, use the
      **rightmost** Type C port.

    - For Mac Pro desktop machines, facing the top of the machine, use
      the Type C port **farthest** from the power button.

    - For Mac Pro rackmount machines, facing the front of the machine,
      use the Type C port **closest** to the power button.

    If you are using a Type A to Type C cable, connect the Type C end to
    the target machine. The Type A end may be directly connected to the
    host machine, or to a Type C port via a Type A to Type C adapter.
    USB hubs may also be used on the host machine side (but not the
    target machine side).

7.  Enter DFU mode. The process is different for desktops and laptops
    (you can pick one of two options for laptops; try both if you have
    trouble getting it to work).

    - For desktops:

      a.  Start with the machine fully powered down.

      b.  Unplug the machine from the mains power and wait 30 seconds.

      c.  Press and hold down the power button.

      d.  While holding down the power button, connect mains power to
          the machine.

      e.  Continue holding down the power button and watch the kernel
          log. Look for a USB device log that mentions
          `Product: Apple Mobile Device (DFU Mode)`.

      f.  Once you see the log, release the power button.

    - For laptops (method 1):

      a.  Start with laptop fully powered down.

      b.  Press and release the power button quickly.

      c.  **Immediately** press and hold the following keys: Left
          control, left option, right shift, and the power button.

      d.  Count down 10 seconds, then release everything except the
          power button.

      e.  Continue holding down the power button and watch the kernel
          log. Look for a USB device log that mentions
          `Product: Apple Mobile Device (DFU Mode)`.

      f.  Once you see the log, release the power button.

    - For laptops (method 2):

      a.  Start with laptop powered **up** (make sure something is
          visible on the display).

      b.  Press and hold the following keys: Left control, left option,
          right shift, and the power button.

      c.  Wait until the screen turns off, then count down 5 additional
          seconds, then release everything except the power button.

      d.  Continue holding down the power button and watch the kernel
          log. Look for a USB device log that mentions
          `Product: Apple Mobile Device (DFU Mode)`.

      e.  Once you see the log, release the power button.

    If you don't see the DFU device in the log, or the Product mentions
    \"Recovery Mode\" instead, something went wrong. Retry the steps
    again. The display of the target machine will remain blank in DFU
    mode.

8.  On your host machine, press Ctrl-C to stop the dmesg command.

9.  Run the following command:
    `systemd-inhibit sudo -s TMPDIR=$PWD idevicerestore -l`.

10. When prompted, type \'1\' to select the latest available
    macOS/firmware version.

During the Restore process, the target machine will display an Apple
logo and a progress bar, while the host machine running `idevicerestore`
will print out progress log information. Note that this process involves
connecting to Apple's CDN and servers to download system firmware
components and authenticate them for your specific machine.

After the process completes successfully, the machine will reboot into
the Recovery Assistant. Follow the prompts to select a macOS volume to
recover, and enter your macOS authentication credentials. After this
process succeeds, your machine will boot into the Boot Picker. From
here, you can choose which OS to boot next.

It is likely that any existing {variant-name} installations will become
unbootable as a result of the Revive process. If attempting to boot a
Linux install triggers a reboot or a Recovery screen, follow the steps
in the [Upgrading or repairing m1n1 stage 1](#stage1-repair) section to
reinstall m1n1 stage 1 and make the OS bootable again.

If the DFU Revive fails, you will have to perform a DFU Restore. To do
so, follow the above steps again, but add the `-e` option to the
`idevicerestore` command:

`systemd-inhibit sudo -s TMPDIR=$PWD idevicerestore -l -e`

:::: caution
::: title
:::

This will **irreversibly** wipe all data on the target machine.
::::

After a DFU Restore, your machine will be reset to its factory condition
and boot into the macOS first-time setup wizard.

### Live booting Fedora Linux on an x86 (Intel/AMD) compatible machine to perform a DFU restore {#fedora-live-dfu}

You can use a USB disk to live-boot Fedora Workstation on any x86-64
machine and perform the DFU restore from that environment, without
having to install to local disk. You will need a USB disk with at least
**64GB** of capacity.

:::: note
::: title
:::

All existing data on the USB disk will be erased.
::::

To set up the USB disk, we recommend using [Fedora Media
Writer](release-docs-home::preparing-boot-media.xml#fedora_media_writer).
Follow the steps on that page to download it and write the image to your
USB disk, and then boot it on your target machine.

Once the system is booted, follow the following steps to open up a
terminal:

1.  On \'Welcome to Fedora\' screen, click \'Not Now\'.

2.  Click on the top right menu bar icon and connect to a WiFi network
    (if not using wired Ethernet).

3.  Click on the top left menu icon, type \'terminal\' and hit enter.

To perform the DFU Restore process, `idevicerestore` needs a large
amount of temporary disk space. Since the live image runs from RAM, it
does not have enough temporary space available. To create and use a
temporary partition in the remaining free space on the USB disk, run the
following commands one by one:

    device=$(grep /run/initramfs/live /proc/mounts | awk '{ print $1 }' | sed 's/[0-9]*$//')
    echo "size=40G" | sudo sfdisk -a $device
    sudo partprobe $device
    part=$(ls ${device}[0-9] | tail -n 1)
    sudo mkfs.ext4 $part
    sudo mkdir -p /mnt/tmp
    sudo mount $part /mnt/tmp
    sudo chmod 777 /mnt/tmp
    cd /mnt/tmp

Next, continue with the steps in the [Performing a DFU revive or restore
using a machine running Fedora Linux](#dfu-fedora) section (you have
already performed steps 1-3 and do not need to do them again). =
Deviations

This page documents where Fedora Asahi Remix deviates from Fedora Linux
and the reasoning behind.

We are using a [Remix](https://fedoraproject.org/wiki/Remix) as opposed
to delivering Apple Silicon support in Fedora Linux proper because this
ecosystem is still very fast moving and we believe a Remix will offer
the best user experience for the time being.

Building a Remix allow us to integrate hardware support as it becomes
available and bring it to users as quickly as possible. Nonetheless, as
much of this work as possible is being conducted upstream, with most
components being developed, maintained and packaged in Fedora Linux
proper. Ultimately, we expect Apple Silicon support to be integrated in
Fedora Workstation and Fedora Server in a future release, and are
working towards this goal. This approach is in line with the overarching
goal of the Asahi project itself to integrate support for these systems
in the relevant upstream projects.

## Edition mapping {#_edition_mapping}

We provide Fedora Asahi Remix in four editions, which map to the stock
Fedora Linux deliverables as follows:

- Fedora Linux with KDE Plasma → Fedora KDE Plasma Desktop

- Fedora Linux with GNOME → Fedora Workstation

- Fedora Server → Fedora Server

- Fedora Minimal → Fedora Everything

The flagship edition for Fedora Asahi Remix is Fedora Linux with KDE
Plasma.

## Deviations {#_deviations}

### Installation does not use Anaconda {#_installation_does_not_use_anaconda}

Apple Silicon Macs have a bespoke [boot
process](https://asahilinux.org/docs/Introduction-to-Apple-Silicon) that
requires special considerations to support [alternative operating
systems](https://asahilinux.org/docs/Open-OS-Ecosystem-on-Apple-Silicon-Macs).
Currently, Fedora Asahi Remix is installed from macOS via the [Asahi
Installer](https://github.com/AsahiLinux/asahi-installer), which takes
care of preparing the system for the installation, downloading an image
for Fedora Asahi Remix and laying it on disk.

The Asahi Installer has also the ability to prepare the system and
install the supporting components for a barebone UEFI-enabled system.
This could potentially be used in the future to support Anaconda-based
installation using regular Fedora Linux install media, but it is not
currently supported. The work required is tracked in our issue tracker
([Anaconda](https://pagure.io/fedora-asahi/project/issue/9), [disk
management tools](https://pagure.io/fedora-asahi/project/issue/10)).

### No official support for full disk encryption {#_no_official_support_for_full_disk_encryption}

The Asahi Installer does not currently support installing systems using
full disk encryption. There is no technical limitation preventing the
use of encryption, but currently it is not a supported configuration,
and the installer does not provide any facility to set it up. A number
of approaches to resolve this (including [implementing installer
suppport](https://github.com/AsahiLinux/asahi-installer/pull/240)) are
currently being discussed upstream in the Asahi Linux project.

### Installation images are built with Kiwi {#_installation_images_are_built_with_kiwi}

Fedora Asahi Remix installation images are built using
[Kiwi](https://osinside.github.io/kiwi/) from the published [Kiwi
descriptions](https://pagure.io/fedora-asahi/kiwi-descriptions).

### Installation images are built and hosted outside of Fedora infrastructure {#_installation_images_are_built_and_hosted_outside_of_fedora_infrastructure}

Because the installation images include additional components that are
not part of stock Fedora Linux, they cannot currently be built or hosted
on Fedora Infrastructure. We are instead leveraging AWS for this, and
more details on the infrastructure deployment are available on our [how
it's made
page](https://docs.fedoraproject.org/en-US/fedora-asahi-remix/how-its-made/#_installation_images).

Since Fedora Linux 40 it is possible to [build Kiwi images in
Koji](https://fedoraproject.org/wiki/Changes/KiwiBuiltCloudImages); this
will enable the future efforts to build stock Fedora Linux images with
Apple Silicon support.

### No support for legacy X11 desktops {#_no_support_for_legacy_x11_desktops}

Fedora Asahi Remix comes out of the box with a 100%
[Wayland](https://wayland.freedesktop.org/) environment. Wayland is
required to provide a good experience on this platform, and the legacy
Xorg server is not supported. Existing X11 applications are fully
supported out of the box thanks to XWayland.

### Downstream packages required for platform enablement are included {#_downstream_packages_required_for_platform_enablement_are_included}

Fedora Asahi Remix includes a number of components that are not part of
stock Fedora Linux; these are preinstalled and delivered via our [copr
repositories](https://copr.fedorainfracloud.org/groups/g/asahi/coprs/).

These components include `mesa`
([source](https://pagure.io/fedora-asahi/mesa/),
[copr](https://copr.fedorainfracloud.org/coprs/g/asahi/mesa/)), which is
tightly coupled to the kernel AGX driver and in active development, and
`u-boot` ([source](https://pagure.io/fedora-asahi/uboot-tools),
[copr](https://copr.fedorainfracloud.org/coprs/g/asahi/u-boot/)), which
requires patches in the process of being upstreamed.

The kernel is also maintained downstream in a
[fork](https://gitlab.com/fedora-asahi/kernel-asahi) of the main
[kernel-ark](https://gitlab.com/cki-project/kernel-ark) repository. The
kernel is in active development --- while platform enablement for Apple
Silicon is [in the process](https://asahilinux.org/docs/Feature-Support)
of being upstreamed, currently a downstream kernel is required for the
best experience.

Finally, a number of packages specific to the Remix implementation are
also maintained downstream; more details on these are available on our
[how it's made
page](https://docs.fedoraproject.org/en-US/fedora-asahi-remix/how-its-made/#_remix_specific_plumbing).

### Fedora Asahi Remix uses 16K pages {#_fedora_asahi_remix_uses_16k_pages}

Apple Silicon hardware native page-size is 16K; consequently, this is
also the Fedora Asahi Remix default, and we deploy the `kernel-16k`
variant. While a 4K page-size kernel is available in the `kernel`
package, this is completely unsupported and should not be used.

### Fedora Linux with KDE Plasma uses Calamares for first-boot setup {#_fedora_linux_with_kde_plasma_uses_calamares_for_first_boot_setup}

We provide a custom Calamares-based first-boot setup wizard to simplify
user onboarding. This is only available on the Fedora Linux with KDE
Plasma edition and is used in place of `initial-setup`.

### Fedora Server uses btrfs as the filesystem for the installed system {#_fedora_server_uses_btrfs_as_the_filesystem_for_the_installed_system}

Fedora Asahi Remix uses btrfs for all of the deliverables. This matches
what Fedora Linux does since Fedora Linux 33, with the exception of
Fedora Server, which still defaults to XFS. We use btrfs everywhere
because we need the ability to online resize the filesystem, so that it
can be expanded to fill the available space on the first boot after the
installation, and so that users can shrink it as needed if they want to
deploy custom layouts.

### OpenH264 is automatically installed on first-boot {#_openh264_is_automatically_installed_on_first_boot}

Fedora Asahi Remix automatically installs openh264 on the first boot,
enabling playback of H.264-encoded content out of the box. This is
possible because of the two-step install process --- the Asahi Installer
downloads the necessary packages from Cisco's server and makes them
available to the deployed system to the perform the installation via a
one-off systemd service.

### GNOME Software does not support updates between major releases {#_gnome_software_does_not_support_updates_between_major_releases}

Fedora Asahi Remix provides AppStream metadata that is required to
support updates between major releases via PackageKit via
`fedora-asahi-remix-appstream-metadata`
([source](https://pagure.io/fedora-asahi/fedora-asahi-remix-appstream-metadata),
[copr](https://copr.fedorainfracloud.org/coprs/g/asahi/fedora-remix-branding/)).
However, GNOME Software does not currently support reading this
metadata, so it will not present major release updates for Fedora Asahi
Remix with GNOME to the user. Instead, one needs to use the DNF [System
Upgrade](https://docs.fedoraproject.org/en-US/quick-docs/upgrading-fedora-offline/)
plugin to perform the update. It is possible to support this properly in
GNOME Software by implementing a
[plugin](https://gitlab.gnome.org/GNOME/gnome-software/-/tree/main/plugins)
to consume the AppStream metadata, akin to what [KDE
Discover](https://invent.kde.org/plasma/discover/-/tree/master/libdiscover/appstream)
does. = How it's made

This page attempts to document how Fedora Asahi Remix is put together.
Useful prerequisites to read before this:

- our [Deviations](deviations.xml) page, documenting where the Remix
  deviates from Fedora Linux and why

- [Introduction to Apple
  Silicon](https://asahilinux.org/docs/platform/introduction/), which
  covers some of this platform peculiarities

- [Open OS Ecosystem on Apple Silicon
  Macs](https://asahilinux.org/docs/platform/open-os-interop/), which
  explains the boot process and how the OS is laid out

Throughout this document, components hosted outside of Fedora
infrastructure will be marked with a ⚠️.

## Packages {#_packages}

The [Fedora Asahi SIG](https://fedoraproject.org/wiki/SIGs/Asahi)
maintains a number of packages that are required for plaform enablement,
integration and implementation. As many of these as possible are
maintained in Fedora itself under the
[`asahi-sig`](https://src.fedoraproject.org/group/asahi-sig) FAS group.
This isn't an option for [some
packages](https://docs.fedoraproject.org/en-US/fedora-asahi-remix/deviations/#_downstream_packages_required_for_platform_enablement_are_included)
⚠️, and those are maintained in
[copr](https://copr.fedorainfracloud.org) instead, under the
[`@asahi`](https://copr.fedorainfracloud.org/groups/g/asahi/coprs/)
group.

### Installation {#_installation}

Fedora Asahi Remix is installed by the
[`asahi-installer`](https://src.fedoraproject.org/rpms/asahi-installer),
which runs from macOS and guides the user through the installation
process. The installation involves resizing partitions, installing a
stripped-down standalone copy of macOS and laying the Remix image on
disk; the system is then rebooted into recoveryOS, where the the
installer second stage takes over and guides the user to adjusting the
security settings for the standalone macOS and replacing its kernel with
the bundled m1n1 (which comes from the `m1n1-stage1` package), which
will later act as a first stage bootloader for the installed system.

The installer is delivered in `asahi-installer-package`; its build
process relies on two prebuilt macOS binary artifacts (Python and
libffi), which have received a [FESCo
exception](https://pagure.io/fesco/issue/3212) to the [prebuilt
policy](https://docs.fedoraproject.org/en-US/packaging-guidelines/what-can-be-packaged/#prebuilt-binaries-or-libraries).
The
[`asahi-installer`](https://src.fedoraproject.org/rpms/asahi-installer)
source package also provides `python3-asahi_firmware`, which is used by
[`asahi-scripts`](https://src.fedoraproject.org/rpms/asahi-scripts) for
firmware management in userspace.

### Boot process ⚠️ {#_boot_process_️}

After the installation the system boots into Linux by default. The boot
flow starts with [`m1n1`](https://src.fedoraproject.org/rpms/m1n1); its
stage 1, which was placed by the installer, is responsible for finding
and executing the stage 2 from the EFI partition. The main difference
between stage 1 and stage 2 is that the former is rarely updated (as the
process requires running the installer again and going through
recoveryOS), while the latter is distributed by Fedora in the `m1n1`
binary package and updated together with the distro (via `update-m1n1`
in [`asahi-scripts`](https://src.fedoraproject.org/rpms/asahi-scripts)).

Once it's done with platform initialization, `m1n1` will find
[`u-boot`](https://pagure.io/fedora-asahi/uboot-tools) ⚠️ and pass
control to it. U-Boot acts as the third stage bootloader, performing
some more platform initialization and providing a minimal preboot
environment. In the default flow, U-Boot is setup to provide an emulated
UEFI environment, which is used to load GRUB. From here on the boot flow
is the standard Fedora Linux one.

### Firmware {#_firmware}

Apple Silicon machines rely on a large number of firmware blobs to work.
Firmware collection is implemented in
[`asahi-installer`](https://src.fedoraproject.org/rpms/asahi-installer).
Firmware is then loaded as needed in the initramfs via `dracut-asahi`,
which is part of
[`asahi-scripts`](https://src.fedoraproject.org/rpms/asahi-scripts). An
`asahi-fwupdate` package is also provided (also from
[`asahi-scripts`](https://src.fedoraproject.org/rpms/asahi-scripts)) to
apply firmware updates on the Linux side in case new firmware becomes
available.

The Asahi Linux project has [in-depth
documentation](https://asahilinux.org/docs/Open-OS-Ecosystem-on-Apple-Silicon-Macs#firmware-provisioning)
of the firmare provisioning process, which is meant to be standardized
between distributions.

### Kernel and userspace drivers ⚠️ {#_kernel_and_userspace_drivers_️}

The [kernel package](https://gitlab.com/fedora-asahi/kernel-asahi) ⚠️
for Fedora Asahi Remix is maintained as a downstream fork of
[kernel-ark](https://gitlab.com/cki-project/kernel-ark), including
patches from the upstream [Asahi Linux
tree](https://github.com/AsahiLinux/linux). Asahi Linux also maintains a
[detailed tracker](https://asahilinux.org/docs/Feature-Support) of the
upstreaming status for every component.

The GPU driver also has a userspace counterpart in the [asahi
driver](https://docs.mesa3d.org/drivers/asahi.html) in
[mesa](https://pagure.io/fedora-asahi/mesa/) ⚠️. This is tightly coupled
with the AGX driver in the kernel.

### Audio {#_audio}

Apple Silicon machines have a complex speaker setup that requires
speaker protection to be safe and a dedicated DSP chain to sound good.
This is implemented by
[`asahi-audio`](https://src.fedoraproject.org/rpms/asahi-audio), which
leverages
[`rust-bankstown-lv2`](https://src.fedoraproject.org/rpms/rust-bankstown-lv2)
for bass enhancement,
[`rust-speakersafetyd`](https://src.fedoraproject.org/rpms/rust-speakersafetyd)
for speaker protection and
[`rust-triforce-lv2`](https://src.fedoraproject.org/rpms/rust-triforce-lv2/)
for microphone support, plus
[`alsa-ucm-asahi`](https://src.fedoraproject.org/rpms/alsa-ucm-asahi)
and [`rust-alsa`](https://src.fedoraproject.org/rpms/rust-alsa).
PipeWire and WirePlumber have also been enhanced to create the correct
virtual audio devices and present them to the user in an understandable
way.

### Touch Bar {#_touch_bar}

Some Apple Silicon Macbooks have a [Touch
Bar](https://developer.apple.com/design/human-interface-guidelines/touch-bar)
taking the place of the first row of the keyboard. On Linux this is
presented as a regular (albeit odd-sized) display, and it can be driven
as such. To make it useful
[`rust-tiny-dfr`](https://src.fedoraproject.org/rpms/rust-tiny-dfr)
renders a set of function keys on it, mimicking what would be available
on a physical keyboard.

### Media playback and codecs {#_media_playback_and_codecs}

Fedora Asahi Remix ships with out of the box support for H.264-encoded
content. This is implemented by having
[`asahi-installer`](https://src.fedoraproject.org/rpms/asahi-installer)
download the RPMs and putting them onto the EFI partition; a systemd
unit in
[`fedora-asahi-remix-scripts`](https://pagure.io/fedora-asahi/fedora-asahi-remix-scripts)
then installs them on the first boot.

We also provide
[`widevine-installer`](https://src.fedoraproject.org/rpms/widevine-installer)
to automatically enable Widevine playback by downloading and extracting
the necessary bits from a ChromeOS image.

### NVram and default boot entry {#_nvram_and_default_boot_entry}

Apple Silicon systems store some low-level system configuration settings
in NVram. We provide a set of packages to interact with this, but they
are not installed by default as there is currently no safe way to
enforce a single writer (concurrent writes can be racy and lead to
corruption).

The default boot entry can be changed using
[`rust-asahi-bless`](https://src.fedoraproject.org/rpms/rust-asahi-bless)
(a CLI tool) or
[`rust-startup-disk`](https://src.fedoraproject.org/rpms/rust-startup-disk)
(a GUI). Two experimental tools are also provided to sync Bluetooth
([`rust-asahi-btsync`](https://src.fedoraproject.org/rpms/rust-asahi-btsync))
and Wi-Fi
([`rust-wifisync`](https://src.fedoraproject.org/rpms/rust-asahi-wifisync))
settings between macOS and Linux. All of these tools are implemented on
top of
[`rust-apple-nvram`](https://src.fedoraproject.org/rpms/rust-apple-nvram)
and
[`rust-asahi-nvram`](https://src.fedoraproject.org/rpms/rust-asahi-nvram).

### Emulation {#_emulation}

We provide a full emulation stack which allows [running x86/x86-64
applications](https://docs.fedoraproject.org/en-US/fedora-asahi-remix/x86-support/),
including Steam. As of Fedora Linux 42, some of this has been
[integrated](https://fedoraproject.org/wiki/Changes/FEX) into Fedora
Linux proper. As part of this work, we also include
[`rust-binfmt-dispatcher`](https://src.fedoraproject.org/rpms/rust-binfmt-dispatcher/),
which provides a simple dispatcher for binfmt_misc that dynamically
picks the best interpreter to use at runtime, and prompts the user to
install any necessary dependencies if required.

### Apple ecosystem integration {#_apple_ecosystem_integration}

We maintain packages for the
[libimobiledevice](https://libimobiledevice.org/) stack, which
implements protocols and tools to communicate with Apple devices. Among
other things, this includes
[`idevicerestore`](https://src.fedoraproject.org/rpms/idevicerestore),
which can be used to DFU an Apple Silicon laptop from another Linux
system (instead of having to rely on another Mac with Apple Configurator
2). Other components of this stack are
[`libimobiledevice`](https://src.fedoraproject.org/rpms/libimobiledevice),
[`libimobiledevice-glue`](https://src.fedoraproject.org/rpms/libimobiledevice-glue),
[`libtatsu`](https://src.fedoraproject.org/rpms/libtatsu),
[`libplist`](https://src.fedoraproject.org/rpms/libplist),
[`libusbmuxd`](https://src.fedoraproject.org/rpms/libusbmuxd), and
[`usbmuxd`](https://src.fedoraproject.org/rpms/usbmuxd).

We also maintain a handful of ecosystem-related tools:
[`apfs-fuse`](https://src.fedoraproject.org/rpms/apfs-fuse) is a
work-in-progress read-only userspace driver for APFS filesystems, and
[`uxplay`](https://src.fedoraproject.org/rpms/uxplay) is an AirPlay2
implementation.

### Remix-specific plumbing ⚠️ {#_remix_specific_plumbing_️}

We maintain a number of packages that are specific to the implementation
of the Remix:

- `asahi-platform-metapackage`
  ([source](https://pagure.io/fedora-asahi/asahi-platform-metapackage),
  [copr](https://copr.fedorainfracloud.org/coprs/g/asahi/fedora-remix-scripts/))
  provides a metapackage that declares all other Asahi platform package
  dependencies

- `asahi-repos` ([source](https://pagure.io/fedora-asahi/asahi-repos),
  [copr](https://copr.fedorainfracloud.org/coprs/g/asahi/fedora-remix-branding/))
  provides Yum repository definitions for our copr-provided packages

- `calamares-firstboot-configs`
  ([source](https://pagure.io/fedora-asahi/calamares-firstboot-config),
  [copr](https://copr.fedorainfracloud.org/coprs/g/asahi/fedora-remix-scripts/))
  provides the Calamares configuration used for the first-boot installer
  on the KDE edition

- `fedora-asahi-remix-appstream-metadata`
  ([source](https://pagure.io/fedora-asahi/fedora-asahi-remix-appstream-metadata),
  [copr](https://copr.fedorainfracloud.org/coprs/g/asahi/fedora-remix-branding/))
  provides the Remix-specific AppStream metadata that is required to
  support updates between major releases via PackageKit

- `fedora-asahi-remix-release`
  ([source](https://pagure.io/fedora-asahi/fedora-asahi-remix-release),
  [copr](https://copr.fedorainfracloud.org/coprs/g/asahi/fedora-remix-branding/))
  provides the distribution branding for the Remix; Fedora Asahi Remix
  has [trademark
  approval](https://pagure.io/Fedora-Council/tickets/issue/432) from the
  Fedora Council to use its current name and branding (which includes
  the use of the Fedora logo)

- `fedora-asahi-remix-scripts`
  ([source](https://pagure.io/fedora-asahi/fedora-asahi-remix-scripts),
  [copr](https://copr.fedorainfracloud.org/coprs/g/asahi/fedora-remix-scripts/))
  provides various utility scripts and systemd services used in the
  Remix

## Infrastructure {#_infrastructure}

### Installation images ⚠️ {#_installation_images_️}

Fedora Asahi Remix installation images are built using
[Kiwi](https://osinside.github.io/kiwi/) from our [Kiwi
descriptions](https://pagure.io/fedora-asahi/kiwi-descriptions) and are
outside of Fedora Infrastructure.

We are using AWS EC2 instances to perform builds and upload them to AWS
S3, triggered by an [AWS
Lambda](https://gitlab.com/fedora/sigs/asahi/overseer) (which runs
daily). We use another
[Lambda](https://gitlab.com/fedora/sigs/asahi/manifest-generator) to
generate the manifest for these [daily
builds](https://fedora-asahi-remix.org/builds.html) to be consumed by
the Asahi Installer.

We host our [website](https://fedora-asahi-remix.org/) on AWS S3,
fronted by AWS Cloudfront; we use [another
Lambda](https://gitlab.com/fedora/sigs/asahi/cdn-invalidation) to handle
CDN invalidation. The website is automatically deployed from its [GitLab
repository](https://gitlab.com/fedora/sigs/asahi/website); this is also
where the manually-maintained [installer
manifest](https://gitlab.com/fedora/sigs/asahi/website/-/blob/main/installer_data_stable.json)
for release images (as opposed to dailies) lives. The Lambdas are also
automatically deployed via Gitlab Pipelines using AWS Chalice.

### Documentation {#_documentation}

Our [documentation
site](https://docs.fedoraproject.org/en-US/fedora-asahi-remix/) is
generated with [Antora](https://antora.org) from its
[repository](https://pagure.io/fedora-asahi/docs-site), and is
[integrated](https://gitlab.com/fedora/docs/docs-website/docs-fp-o/-/commit/afc54fdc8d8a94ba72ab35f1d65ea535055f7b87)
into the Fedora Docs Website.

### Project and bug tracking {#_project_and_bug_tracking}

We maintain a [project planning
tracker](https://pagure.io/fedora-asahi/project) and a [bugs
tracker](https://pagure.io/fedora-asahi/remix-bugs). = Running
x86/x86-64 applications on {variant-name}

There are lots of lots of legacy x86/x86-64 applications that users want
to run on arm64 platforms, including Windows applications and games. To
support this in {variant-name}, we have integrated a stack of existing
and bespoke components to make it possible to transparently run
x86/x86-64 apps directly on arm64 Linux.

Since Apple platforms use a 16K page size natively and x86/x86-64
processors use a 4K page size, this is especially tricky, as x86/x86-64
applications generally do not work when presented with a host kernel
that requires 16K page alignment. To bridge this gap, we are using a
microVM to run an entirely separate guest Linux kernel in 4K page size
mode. To keep it as seamless as possible, the guest environment is
designed to be as close as possible to the host environment, and we use
native context GPU passthrough to have high-performance graphics inside
the guest.

The stack consists of these components:

- [muvm](https://github.com/AsahiLinux/muvm) (package: `muvm`), our
  bespoke microVM runner based on
  [libkrun](https://github.com/containers/libkrun). This also includes
  components for X11 forwarding and HID input device proxying.

- [FEX-emu](https://fex-emu.com) (package: `fex-emu`), a fast userspace
  x86/x86-64 emulator focused on correctness.

- The [Fedora FEX
  RootFS](https://src.fedoraproject.org/rpms/fex-emu-rootfs-fedora)
  (package: `fex-emu-rootfs-fedora`), which provides common x86/x86-64
  library dependencies to be used by emulated applications.

- [mesa](https://gitlab.freedesktop.org/asahi/mesa) (packages:
  `mesa-fex-emu-overlay-i386` and `mesa-fex-emu-overlay-x86-64`), built
  for the x86/x86-64 architectures and packaged as a FEX RootFS overlay.
  This provides the OpenGL/OpenCL/Vulkan support for Apple GPUs.

We also have our own [Steam
wrapper](https://pagure.io/fedora-asahi/steam) that automates the
process of installing and launching Steam inside the microVM stack. When
running Windows games using Steam, these open-source components are used
behind the scenes:

- [Proton](https://github.com/ValveSoftware/Proton), a Wine distribution
  aimed at gaming.

- [dxvk](https://github.com/doitsujin/dxvk), a translation layer that
  converts the Windows DirectX 8 - DirectX 11 APIs to Vulkan.

- [vkd3d-proton](https://github.com/HansKristian-Work/vkd3d-proton), a
  translation layer that converts the Windows DirectX 12 API to Vulkan.

## Scope {#_scope}

This technology stack is primarily aimed at running x86 and x86-64
games, but it can also be used to run non-game productivity
applications. When possible, you should prefer native alternatives over
emulation. Please read [this FAQ entry](faq.xml#x86) for more
information.

The scope of this solution is limited to *portable x86 and x86-64
applications* that are intended to be run from your home directory (or,
at most, manually unpacked into `/opt` by the user), including
AppImages. It is *not* intended to run x86-64 applications that must be
installed as system packages, which are built for a specific Linux
distribution or require installation of complex system dependencies, or
which require running dedicated installers as root.

In particular, the x86-64 environment is *not* a self-contained root
filesystem, but rather a minimal, immutable overlay on top of your
existing arm64 root filesystem. That means that you cannot make changes
to it, install additional packages, etc. There is no root access
available at all within the x86-64 environment.

## Usage {#_usage}

### Steam {#_steam}

Just use `dnf install steam` to install our Steam wrapper, and then run
Steam from your desktop's launcher (or the `steam` command) to download
and install Steam. This will install all necessary dependencies
automatically.

### Other applications {#_other_applications}

To install the emulation stack by itself, use `dnf install fex-emu`.
This will pull in the required dependencies automatically.

You cannot run x86-64 applications directly from the host (yet), as they
must be launched from the microVM. To do so, run
`muvm -- /path/to/executable`. You must use an absolute path, as `muvm`
does not currently preserve the current working directory. In this
environment, the kernel's binfmt support is already configured to use
FEX to run x86/x86-64 applications, so you should be able to just run
them.

If your application uses a launcher shell script instead of directly
running its main binary, you should run it through `FEXBash`. For
example, use `muvm -- FEXBash /path/to/launcher.sh`. Doing so ensures
that the shell runs in the emulated environment and a few critical shell
commands behave as they would for x86-64 applications, which makes it
more likely that the shell script will work as intended.

You can also use `muvm -- bash` to launch an arm64 shell within the 4K
MicroVM, or `muvm -- FEXBash` to launch an x86-64 shell. The x86-64
shell will behave similarly to the arm64 shell and most commands will
run as arm64 binaries, but a few (such as `ls`) will run under
emulation, which lets you \"see\" the world as x86-64 apps do.

## How it works {#_how_it_works}

`muvm` creates a virtual machine that shares as much with the host OS as
possible. Within the VM, the root filesystem is *the same as the host
root filesystem*, with the following exceptions:

- `/dev`, `/sys`, and `/proc` are guest-private, except for `/dev/shm`
  which is shared with the host, allowing host apps and guest apps to
  coherently share memory.

- `/run` is also private to the guest

- The FEX-emu rootfs and overlay images are mounted under
  `/run/fex-emu/`, with the combined overlay rootfs available at
  `/run/fex-emu/rootfs`.

- `/usr/share/fex-emu` and `/usr/local/share/fex-emu` are overmounted
  with a tmpfs to inject a FEX `Config.json` suitable for use within the
  VM

- A tmpfs is also mounted on `/tmp/.X11-unix`, so X11 server sockets are
  private to the VM

- The entire host filesystem view is available at `/run/muvm-host`,
  including any overlaid mounts. For example, you can access the host's
  `/run` at `/run/muvm-host/run`. (Note: `/run/muvm-host/dev` exists but
  will not do what you might hope it does. Host devices are not
  available in the guest.)

This means that `/usr`, `/home`, `/etc`, `/opt`, `/var`, `/tmp`, and any
other directories in your filesystem root are *shared between the guest
and the host*. The aarch64 guest OS does not run its own root
filesystem, but rather *runs exactly the same binaries as your host OS
does*.

Additionally, FEX itself uses the filesystem mounted at
`/run/fex-emu/rootfs` as its virtual RootFS. This means that x86/x86-64
applications (and only those) will see the contents of that directory
overlaid on top of the root filesystem. This is how we make x86/x86-64
libraries available to those applications, while still sharing most of
the filesystem contents.

When muvm starts, it registers FEX as a binfmt provider, so x86/x86-64
applications will be transparently run through it. On startup, FEX will
detect that TSO support is available on the Apple Silicon platform (even
within the VM), and automatically enable it for faster accurate
emulation.

:::: tip
::: title
:::

Mountpoints in the host are propagated to the guest *when they are first
accessed*, automagically. This allows guest apps to distinguish
different filesystems, which keeps device/inode semantics correct. If
you have a partition mounted on the host at `/mnt/steam` and you run
`mount` within the guest, you won't see it at first. If you run
`ls /mnt/steam` and then run `mount` again, the mount will have
magically been added to the mount list. This is normal and working as
intended!
::::

## Known issues {#_known_issues}

### Performance isn't very good {#_performance_isnt_very_good}

As this project is still in its early stages, we aimed for correctness
for the initial release. Performance optimization will happen over time.
We're aware of several changes that should bring significant performance
improvements, and we're actively working on it!

For Windows DX8-DX11 games under Proton in particular, you might want to
try WineD3D instead of DXVK. WineD3D uses OpenGL instead of Vulkan as
its backend, and it *may* have better performance thanks to
optimizations in our OpenGL driver that are not available on Vulkan. To
enable it, change the Steam launch options to
`PROTON_USE_WINED3D=1 %command%`. Note that DXVK tends to have better
compatibility, so this is a trade-off. Let us know what games work
better using either backend!

Older 32-bit games may run very slowly if they make heavy use of the
80-bit x87 floating-point unit, since these operations have to be
emulated in software for full compatibility (the same issue exists in
Rosetta on macOS). You can run these games with hardware-based 64-bit
floating-point emulation, which is less accurate but much faster. To do
so, change the Steam launch options to
`FEX_X87REDUCEDPRECISION=1 %command%`. This mode can cause subtle issues
in some games due to the reduced accuracy, but most games should run
fine (and much faster).

### The VM uses a lot of RAM {#_the_vm_uses_a_lot_of_ram}

To allow guest apps to use a large amount of RAM (as some modern games
require), by default `muvm` allows the guest to use up to 80% of the
system RAM. This also means that some of that will be taken up by guest
page cache, appearing to the host as if the VM is taking up most of
system RAM. `muvm` has the ability to reduce guest page cache usage as
host memory pressure increases, so if you increase host memory usage,
the VM should reduce its usage accordingly (as long as it is able to
discard unused cache RAM).

On lower RAM size machines (16GB or lower), we recommend not running any
heavy host applications while the VM is in use. We don't recommend
running complex games on 8GB machines.

To inspect VM memory usage while it is running, use `muvm -ti -- free`.
You can also run `muvm -ti -- htop` (if you have `htop` installed) to
get more detailed information, or substitute your system information
tool of choice.

If you wish to limit the maximum memory usage of the MicroVM, you can
configure the guest RAM allocation with the `muvm --mem=SIZE` parameter.

### I can't access media mounted under `/run/media` within the VM {#_i_cant_access_media_mounted_under_runmedia_within_the_vm}

This does not work (not even via `/run/muvm-host/run/media`) due to
missing POSIX ACL support in libkrun at this time. You must manually
mount any disks that you wish to use within the VM, e.g. under `/mnt`.

## FAQ {#_faq}

### Is this like Rosetta on macOS? {#_is_this_like_rosetta_on_macos}

This is as close to Rosetta as we can get! The main difference is that
Rosetta side-steps the page size issue by instead relying on the XNU
kernel's multiple page size support for user processes, so it doesn't
need a VM. While making Linux support mixed page sizes would not be
completely impossible in theory, it would be an enormous project that
would likely take years to complete, and it isn't at all clear whether
such a change would be accepted upstream (Linux doesn't even have
boot-time page size selection within a single kernel yet!).

Other than the page size issue, FEX and Rosetta are comparable
technologies (both are emulators, despite what Apple marketing might
have you believe). Both FEX and Rosetta use the unique Apple Silicon CPU
feature that is most important for x86/x86-64 emulation performance: TSO
mode. Thanks to this feature, FEX can offer fast *and* accurate
x86/x86-64 emulation on Apple Silicon systems.

### Why not just use a 4K host kernel? {#_why_not_just_use_a_4k_host_kernel}

While Apple Silicon systems support 4K CPU pages, the rest of the
hardware (IOMMUs, GPU) runs with 16K pages only. The Linux kernel does
not play nicely in this environment, as it generally assumes that the
CPU page size is at least as large or larger than the IOMMU page size.
In the past we had some kernel patches to make this partially work, but
they were buggy and incomplete, so we abandoned the approach. Even if it
did work well, running the whole system using 4K pages has a measurable
performance impact, so we would never ship 4K kernels by default.
Therefore, running x86/x86-64 apps would require that users manually
change their kernel and reboot, which is quite cumbersome.

### Why not box64? {#_why_not_box64}

box64 and FEX-Emu have different approaches to emulation, with FEX-Emu
aiming for better correctness by default (but requiring a more complex
setup) while box64 aims to cover more \"out of the box\" use cases (like
running a subset of applications directly on a 16K kernel without a VM
using some tricks). We have chosen FEX-Emu for our stack because we
believe it will have higher compatibility with its approach, but both
have their uses. box64 is [packaged in
Fedora](https://src.fedoraproject.org/rpms/box64), so we encourage users
to try it (both natively and within muvm) and let us know how it
compares!

### My x86-64 or x86 application is missing some system libraries, what do I do? {#_my_x86_64_or_x86_application_is_missing_some_system_libraries_what_do_i_do}

Our immutable RootFS contains a large set of common x86-64 and x86
libraries that are commonly used as dependencies, but we cannot ship
every possible library. You can view the package list
[here](https://pagure.io/fedora-kiwi-descriptions/blob/rawhide/f/teams/asahi.xml).

If the missing library is a relatively simple, common library with no or
very simple dependencies, and which would not add much size to our
RootFS images, please submit a PR to the repo linked above so we can
include it in future releases of the RootFS. Make sure to note what
application requires the library, and why you think we should include
it.

If your app requires a complicated framework (such as Qt) or an
uncommon, niche library, then the application is not built as a
\"portable\" application and not expected to work out-of-the-box on most
systems. To work around the issue, you can manually download the missing
libraries, extract them into your home directory, and use
`LD_LIBRARY_PATH` to make your application find them. You can use the
following command to download x86-64 RPMs from your arm64 Fedora
installation:

    dnf download --repo=fedora --repo=updates --forcearch=x86_64 --best [package1] [package2]...

You can then use `rpmdev-extract` to extract the contents of the RPM,
and then configure `LD_LIBRARY_PATH` as appropriate.

It is also possible to overlay RPMs into the existing RootFS, though
this should be considered advanced functionality. Once you have an RPM,
you can convert it to an erofs image using these commands:

    rpm2archive -n mypackage.rpm
    mkfs.erofs --tar=f mypackage.rpm.erofs mypackage.rpm.tar

Then, you can manually launch `muvm` with the base erofs images and your
custom erofs image on top, like this:

    muvm \
    -f /usr/share/fex-emu/RootFS/default.erofs \
    -f /usr/share/fex-emu/overlays/mesa-x86_64.erofs \
    -f /usr/share/fex-emu/overlays/mesa-i386.erofs \
    -f mypackage.rpm.erofs \
    <your muvm arguments here>

This will overlay the add-on package onto the RootFS used for FEX.
Please keep in mind that this may or may not work as intended, and it
should not be considered a supported solution.

### Steam says steamwebhelper crashed, what do I do? {#_steam_says_steamwebhelper_crashed_what_do_i_do}

Just let it restart, and it should work on the second try. Steam has a
timeout for steamwebhelper, and when running under emulation, startup is
slow enough that the timeout expires. This usually only happens on a
cold startup.

### I am unable to download/run certain games in Steam {#_i_am_unable_to_downloadrun_certain_games_in_steam}

Ensure Steam Play is enabled for all games. It should be under Menu \>
Settings \> Compatibility \> Enable Steam Play for all other titles.
Restart Steam once enabled.

### Pressing keys makes the touchpad stop responding {#_pressing_keys_makes_the_touchpad_stop_responding}

This is caused by the \"Disable while typing\" touchpad feature. You can
turn it off in the touchpad/input settings for your desktop environment.

### Can I run Windows applications outside of Steam? {#_can_i_run_windows_applications_outside_of_steam}

At this point, we do not support running Windows apps outside of Steam
as non-proton Wine not yet work on Fedora. We are working on resolving
the underlying [FEX issue](https://github.com/FEX-Emu/FEX/pull/4225), so
we expect to support this relatively soon.

In the meantime, you can use Steam's Proton to run non-Steam Windows
applications directly from Steam.

### Can I run x86-64/x86 Linux applications? {#_can_i_run_x86_64x86_linux_applications}

Native Linux games should generally work under muvm, as long as they are
self-contained and do not depend on complex host system libraries (we
ship a large selection of common dependencies, but not everything under
the sun).

### Is Wayland supported? {#_is_wayland_supported}

Wayland is not supported inside the VM at this time. As most of the
legacy x86/x86-64 applications people want to run are X11 applications,
we are focusing on X11 support first. This means that you cannot run
native Wayland apps inside the VM at this time. Of course, the host
desktop is still a Wayland desktop, and X11 support is provided by
XWayland.

### Can I access hardware from applications running within the microVM? {#_can_i_access_hardware_from_applications_running_within_the_microvm}

As the VM does not pass through any host hardware other than the GPU and
the virtual filesystem, you will not be able to use applications that
require direct hardware access. We use software passthrough for the
following interfaces:

- X11 protocol (display, keyboard, mouse)

- Gamepads via hid/uinput passthrough

- Sound I/O via the PulseAudio socket protocol [^1]

We are researching the possibility of passing through PipeWire, which
will allow webcams to be used within the VM.

### Can I use input methods (IMEs) in applications within the microVM? {#_can_i_use_input_methods_imes_in_applications_within_the_microvm}

You can use the classic *xim* input method system used in X11. muvm
should already configure the environment variables appropriately to make
this work for Qt and GTK applications (loading the \"xim\" plugin), as
long as the input method framework you are using on your host system
supports it. We have tested this with *fcitx5* and Steam running on KDE
Plasma.

In the future, once Wayland passthrough is supported, the native Wayland
input protocol mechanism should work with any host input method
framework (through a plugin usually called \"wayland\"). There are no
plans to support non-window-system-based input methods (such as the
direct \"ibus\" and \"fcitx\" plugins), since they would require us to
ship x86-64 shared libraries for all possible input methods in the
immutable virtual x86-64 system, and would also require proxying of
their bespoke protocols, which is infeasible.

### Is this like a Qemu/libvirt/UTM/Parallels/VMWare/VirtualBox/etc. VM? {#_is_this_like_a_qemulibvirtutmparallelsvmwarevirtualboxetc_vm}

No, muvm does not work like a traditional whole-system VM. While it does
also use KVM as a backend for efficient virtualization, the concept is
very different to traditional VMs running entirely separate guest
operating systems. The guest kernel is a [special
kernel](https://github.com/containers/libkrunfw) optimized to start up
in a fraction of a second, and the VM monitor passes through the host
filesystem mostly as-is. There is no low-level hardware passthrough
(USB, etc.) and instead we focus on higher-level software protocol
passthrough, like X11/Wayland. The VM does not run its own standalone
init system, only some minimal startup code. This means that the
environment within the VM should \"feel\" the same as the host OS from
the point of view of applications, just with a 4K page size instead of a
16K page size.

### Do browsers work within the VM guest? {#_do_browsers_work_within_the_vm_guest}

Yes, but they will run in X11 mode. However, there is one caveat:
**browser instances within the guest cannot communicate with browser
instances outside the guest, and it is dangerous to run the same browser
profile in both the guest and the host**.

To avoid these problems, muvm configures an environment variable to
force Firefox to use a dedicated profile when launched within the VM.
This means that applications that launch a browser (such as for login or
documentation purposes) will work as intended, but Firefox will launch
using a dedicated profile without access to your cookies, history, etc.

:::: caution
::: title
:::

If you launch the same browser profile in the guest and the host
simultaneously, your profile data may become corrupted. If your default
browser is not Firefox, and you are using emulated apps that might
launch your default browser inadvertently, we strongly recommend closing
all browser windows before using muvm or manually configuring separate
profiles.
::::

### Can I sudo inside the VM? {#_can_i_sudo_inside_the_vm}

Since the VM monitor runs as your own user identity, it cannot gain root
privileges. \"root\" inside the VM still only has the privileges of your
own user, so sudo doesn't make much sense (and in fact doesn't work). We
recommend installing software that you want to use with muvm+FEX under
your home directory. For software that is designed to be installed under
/opt or similar, we recommend performing the installation steps manually
on the host OS, and then just running the app under muvm.

If you need access to a root shell within the VM for debugging purposes,
you can run `muvm -tip 3335 -- bash`. Keep in mind that, despite being
\"root\", you will not be able to modify most system files owned by
root, and any files you create will actually be owned by your non-root
user identity. A root shell is mainly useful to do things like `strace`
other processes or change guest kernel or network configuration settings
(but these changes will not persist across a VM restart).

### Can applications within the VM communicate with applications outside the VM? {#_can_applications_within_the_vm_communicate_with_applications_outside_the_vm}

Communication is mostly limited to the host filesystem. The VM shares
your home directory (and in fact most of the filesystem) with the host,
so any files you create on one side will be visible on the other.

Thanks to virtiofs-DAX, shared memory communication (`/dev/shm`) is also
available between guest apps and host apps. This is used, for example,
by the X11 forwarding code.

It is also possible to share audio between host and guest apps by using
the PulseAudio forwarding support. For example, you can record guest
audio by using a recording app on the host and recording from the system
\"Monitor\" device. You can also configure virtual sinks/sources in the
host using the normal PipeWire mechanisms, and direct guest apps to use
those for audio I/O to have custom audio routing and processing. Note
that the native PipeWire protocol is not passed through, only the
PulseAudio protocol which is more limited (but more commonly used by
applications). ALSA applications are supported via the `pulse` plug-in.

If you are using a host compositor that supports XWayland video bridging
(such as KDE Plasma / KWin), you will be able to screen share / screen
capture from the VM, including full host screens and Wayland windows.
Make sure the app you are running supports \"classic\" XComposite
window/screen capture. When you initiate screen sharing, you will be
able to directly select X11 application windows, or choose the virtual
\"Xwayland Video Bridge\" window. When you do so, KDE will automatically
prompt you for the actual window or screen you wish to share.

### Why do I have fewer CPU cores inside the VM? {#_why_do_i_have_fewer_cpu_cores_inside_the_vm}

By default, `muvm` passes through as many CPUs as there are performance
cores on your host machine, and pins those vCPUs to the physical
performance cores. Since the host CPU scheduler has no visibility into
the guest CPU scheduler, this ensures that performance is consistent.
You can modify this behavior with the `muvm --cpu-list=CPU_LIST` option.

### How do I use an external drive as a Steam library folder? {#_how_do_i_use_an_external_drive_as_a_steam_library_folder}

Follow these steps to get an external drive set up for Steam:

1.  Format your external drive using a Linux-native filesystem such as
    ext4.

    :::: note
    ::: title
    :::

    FAT32, exFAT, and other filesystems without support for Linux
    permissions will not work.
    ::::

2.  Mount your drive manually under a directory accessible to muvm, such
    as `/mnt/steam`.

    :::: note
    ::: title
    :::

    We recommend mounting the drive manually (e.g.
    `sudo mount /dev/sdX1 /mnt/steam`, where `sdX1` is your drive's
    device file). If you configure the drive to mount automatically
    using `/etc/fstab`, then your system will not boot if that drive is
    not connected.
    ::::

    :::: note
    ::: title
    :::

    The default mountpoint for drives mounted via the desktop
    environment (udisks) will not work at this time.
    ::::

3.  Ensure that the filesystem root is accessible to your regular user:

    `sudo chown ${USER}: /mnt/steam`

4.  Create an empty folder named `steamapps` at the root of the mount:

    `mkdir /mnt/steam/steamapps`

5.  Start up Steam normally

6.  Click on the Library tab, then click the gear (settings) icon

7.  Select **Storage** on the left menu, click on the combo box at the
    top of the panel, and select **Add Drive**.

8.  Browse to your drive mountmount (`/mnt/steam`), such that the only
    folder visible in the file picker list window is the empty
    `steamapps` folder within, then (without making any further
    selections) click on the **Select** button.

You should now be able to select the new download location, make it the
default, and download games to it. = Conference talks

This page collects conference talks and other public presentations
around the Fedora Asahi Remix, Asahi Linux and adjacent topics.

## Fedora Asahi Remix {#_fedora_asahi_remix}

- [Fedora Asahi Remix: a year
  later](https://www.youtube.com/watch?v=PiPLDDgtEek) (Davide Cavalca,
  Neal Gompa) at [Flock to Fedora
  2024](https://cfp.fedoraproject.org/flock-2024/talk/FZEL8Q/)

- [Fedora Asahi Remix 40](https://www.youtube.com/watch?v=koyixgJZagU)
  (Davide Cavalca, Neal Gompa) at [Fedora Linux 40 Release
  Party](https://fedoraproject.org/wiki/Fedora_Linux_40_Release_Party_Schedule)

- Bringing Fedora Linux to Apple Silicon Macs with Asahi Linux (Davide
  Cavalca, Neal Gompa) at [Texas Linux Festival
  2024](https://2024.texaslinuxfest.org/talks/bringing-fedora-linux-to-apple-silicon-macs-with-asahi-linux/)

- Bringing Fedora Linux to Apple Silicon Macs with Asahi Linux (Davide
  Cavalca, Neal Gompa) at [SCALE
  21x](https://www.socallinuxexpo.org/scale/21x/presentations/bringing-fedora-linux-apple-silicon-macs-asahi-linux)

- [Bringing Fedora Linux to Apple Silicon Macs with Asahi
  Linux](https://www.youtube.com/watch?v=r0hd15MPMok) (Davide Cavalca,
  Neal Gompa) at [LinuxFest Northwest 2023
  Minifest](https://2023.linuxfestnorthwest.org/)

- [Fedora Asahi Remix: Bringing Fedora to Apple Silicon
  Macs](https://www.youtube.com/watch?v=zuxIElSqC3Y) (Davide Cavalca,
  Neal Gompa) at [Flock to Fedora
  2023](https://flock2023.sched.com/event/1Or2q/fedora-asahi-remix-bringing-fedora-to-apple-silicon-macs)

- [Fedora Asahi Remix](https://www.youtube.com/watch?v=NbCbHGqUl1E)
  (Eric Curtin) at [DevConf.CZ
  2023](https://devconfcz2023.sched.com/event/1MYko/fedora-asahi-remix)

- [Fedora
  Asahi](https://archive.fosdem.org/2023/schedule/event/fedora_asahi/)
  (Eric Curtin) at [FOSDEM 2023](https://archive.fosdem.org/2023)

## Asahi Linux {#_asahi_linux}

- [Linux on Apple Silicon with Alyssa
  Rosenzweig](https://softwareengineeringdaily.com/2024/10/15/linux-apple-silicon-alyssa-rosenzweig/)
  on [Software Engineering
  Daily](https://softwareengineeringdaily.com/category/all-episodes/exclusive-content/Podcast/)

- [AAA!! She's a witch!](https://www.youtube.com/watch?v=TtLP5sAXYKo)
  (Alyssa Rosenzweig) at [XDC
  2024](https://indico.freedesktop.org/event/6/contributions/284/)

- [Escape the walled garden: Freeing the Apple
  GPU](https://media.libreplanet.org/u/libreplanet/m/escape-the-walled-garden-freeing-the-apple-gpu/)
  (Alyssa Rosenzweig) at [LibrePlanet
  2024](https://libreplanet.org/2024/speakers/#6922)

- [From Asahi Linux to Ubuntu: Running Linux on Apple
  Silicon](https://www.youtube.com/watch?v=EJ8hdpXkkMI) (Hector Martin,
  Tobias Heider) at [Ubuntu Summit
  2023](https://events.canonical.com/event/31/contributions/177/)

- [Unleash the (graphics)
  magic](https://www.youtube.com/watch?v=O36VFNdQHsE) (Alyssa
  Rosenzweig, Lina Asahi) at [XDC
  2023](https://indico.freedesktop.org/event/4/contributions/184/)

- [Asahi Linux - One chip, no docs, and lots of
  fun](https://www.youtube.com/watch?v=COlvP4hODpY) (Hector Martin) at
  [Akademy 2023](https://conf.kde.org/event/4/contributions/118/)

- [Tasting the Forbidden
  Apple](https://www.youtube.com/watch?v=SDJCzJ1ETsM) (Alyssa
  Rosenzweig, Lina Asahi) at [XDC
  2022](https://indico.freedesktop.org/event/2/contributions/66/)

- [The Occult and the Apple
  GPU](https://www.youtube.com/watch?v=ObS6sdfus2w) (Alyssa Rosenzweig)
  at [XDC
  2021](https://indico.freedesktop.org/event/1/contributions/10/) =
  Frequently Asked Questions (FAQ)

## About the project {#_about_the_project}

### What is {variant-name}\'s relationship with Fedora KDE, Fedora Workstation, and Fedora Server? {#_what_is_variant_names_relationship_with_fedora_kde_fedora_workstation_and_fedora_server}

{variant-name} provides similar experiences to upstream Fedora Linux,
just tailored to the Apple Silicon Mac hardware platform.

### What variant should I choose? {#_what_variant_should_i_choose}

The KDE Plasma variant receives the most testing and platform
integration work and is the recommended option for users new to Fedora
Linux and Linux on Apple Silicon platforms. The GNOME variant is also
fully supported, for users who prefer that desktop environment. Advanced
users who want an alternate desktop environment may choose the Minimal
variant and manually configure their system to their liking, while those
who want to set up an Apple Silicon-based Linux server may prefer the
Server variant.

### Is Xorg supported? {#_is_xorg_supported}

The native Xorg server is available as a manual install, but its use is
not recommended as it has several known bugs and deficencies when used
on Apple Silicon platforms. As upstream Xorg development has slowed
down, we only support Wayland-based desktop environments. Please do not
file bugs related to usage of the Xorg server.

XWayland is fully supported as a transition technology to use native X11
apps on a Wayland desktop.

### Why is this a Remix? {#_why_is_this_a_remix}

We are using a [Remix](https://fedoraproject.org/wiki/Remix) as opposed
to delivering Apple Silicon support in Fedora Linux proper because this
ecosystem is still very fast moving and we believe a Remix will offer
the best user experience for the time being. Also, the Remix allows us
to integrate hardware support as it becomes available. Nonetheless, as
much of this work as possible is being conducted upstream, with several
key components being developed, maintained and packaged in Fedora Linux
upstream. The Remix image build infrastructure and the installer are
currently hosted outside of Fedora Infrastructure due to technical
limitations. The infrastructure is entirely open source (see our
[GitLab](https://gitlab.com/fedora/sigs/asahi) and
[Pagure](https://pagure.io/projects/fedora-asahi/%2A) repos), and we
will eventually migrate to Fedora Infrastucture once it becomes
possible.

Ultimately, we expect Apple Silicon support to be integrated in Fedora
Linux in a future release, and are working towards this goal. This
approach is in line with the overarching goal of the Asahi project
itself to integrate support for these systems in the relevant upstream
projects.

### What is the difference between alx.sh and fedora-asahi-remix.org? {#_what_is_the_difference_between_alx_sh_and_fedora_asahi_remix_org}

Fedora Asahi Remix can be installed from
<https://fedora-asahi-remix.org> or from <https://asahilinux.org> (which
points to alx.sh). These are functionally equivalent, with the only
differences being:

- fedora-asahi-remix.org is maintained by the Fedora Asahi SIG,
  asahilinux.org and alx.sh are maintained by the Asahi Linux project

- fedora-asahi-remix.org uses a Fedora-built version of the installer
  package, which includes a Fedora-built version of the m1n1 stage1
  (with the Fedora logo and branding), while alx.sh uses the upstream
  builds (with the Asahi logo and branding)

- fedora-asahi-remix.org and alx.sh are backed by different CDN
  providers; depending on where you are in the world, one may be a bit
  faster than the other

- alx.sh can offer additional installation options that are not related
  to Fedora Asahi Remix

Both endpoints serve the same installation images, so there is no
difference in the resulting system if the same installation option is
chosen.

### What devices and hardware are supported? {#_what_devices_and_hardware_are_supported}

The Asahi Linux project website maintains a [landing
page](https://asahilinux.org/fedora/) with device support information,
which is kept up to date as features and new devices are added.
{variant-name} closely follows the upstream kernels and support
packages, so you can expect support to be on par with that page.

For more detailed information on specific driver and kernel support, see
the [Feature Support](https://asahilinux.org/docs/Feature-Support/) page
on the Asahi Linux [documentation
website](https://asahilinux.org/docs/).

### Is {variant-name} safe to install and use? {#_is_variant_name_safe_to_install_and_use}

We strive to make sure that our platform support packages and the
installation process are completely safe and cannot cause any damage to
your computer. In general, it is safe to install and use {variant-name}
on any supported machine (the installer will refuse to work on
unsupported machines). As with all Free Software, please be aware that
{variant-name} is offered with no warranty.

As a Linux distribution, {variant-name} gives users much more control
over their computers than the stock macOS system does. This also means
that there are fewer safeguards against dangerous operations. In
general, Apple Silicon systems are very resilient against permanent
hardware damage, so it is very unlikely that anything you do will cause
any physical, unrecoverable harm to your machine. However, these
machines are less resilient against becoming unbootable than typical x86
machines, and this can happen if important boot partitions on disk are
corrupted or destroyed. You should be careful if you are using
partitioning or disk formatting tools on the internal NVMe storage
device:

- Never change, move, or format the first partition on disk
  (`/dev/nvme0n1p1`, identified as type `Apple Silicon boot` and label
  `iBootSystemContainer`).

- Never change, move, or format the last partition on disk
  (`/dev/nvme0n1pX` for the largest value of X, identified as type
  `Apple Silicon recovery` and label `RecoveryOSContainer`)

- If you make partitioning changes, ensure that the partition table
  remains sorted by disk offset. This can be achieved by using
  `sudo sfdisk -r /dev/nvme0n1`.

If you do end up with trouble booting your machine after making changes
to the disk, please see the [Troubleshooting](troubleshooting.xml)
section for recovery and restore steps. Note that in the worst case this
may involve a full factory reset and loss of all data (on both macOS and
Linux partitions), so users are advised to have up-to-date backups
before doing any disk management operations.

In addition, you should avoid making any changes to the existing macOS
container partition (usually `/dev/nvme0n1p2`, identified as type
`Apple APFS` and typically label `Container` on stock systems). Changes
to this partition may make macOS unbootable, which will make it
difficult to perform system firmware upgrades or recover, upgrade, or
reinstall any Linux installations. At this time, {variant-name} users
are expected to have and maintain a working macOS installation, as the
installation and bootloader upgrade process relies on the macOS admin
user credentials to provision the bootloader. This requirement may be
relaxed in the future, once we support system user management and
firmware upgrades directly from Linux.

### Can I install to external storage? {#_can_i_install_to_external_storage}

We currently do not have a supported process to install to external
storage. The Apple Silicon platform in general cannot boot from external
storage at all, so some components must always be installed to internal
storage. It is possible to manually move the root filesystem to external
storage, but there are limitations (e.g. sleep mode is not currently
supported as it causes external disks to re-enumerate) and therefore
this is left as an exercise for the advanced user.

In the future, we expect to have a supported process for
external-storage installs that does not require re-partitioning the
internal disk (taking advantage of the same mechanism used for macOS
installs to external storage), but this is not ready yet. Note that such
external installs will still be tied to the machine they were installed
on (since some components would still be installed to the internal disk,
as the platform requires this to boot).

### Can I run software built for x86-64 (Intel/AMD)? {#x86}

{variant-name} now includes support for emulating x86 and x86-64
software. For more details, please see [Running x86/x86-64 applications
on {variant-name}](x86-support.xml).

For Free/Open Source Software, it is always preferable to make a build
for aarch64 (ARM64) instead of trying to emulate an x86-64 build. If
your favorite software package is not yet available for this
architecture, please request it from its developers! Users comfortable
with building software may want to try building it themselves. If you do
so, consider [becoming a package
maintainer](package-maintainers::Joining_the_Package_Maintainers.xml) to
help bring the software to all Fedora users.

Sometimes there are options other than running x86-64 software, such as
native third-party alternatives or web versions. See the [How do I
download software?](#download-software) section for some examples.

## HOWTOs {#_howtos}

### How do I access the GRUB menu? {#_how_do_i_access_the_grub_menu}

See [Entering the GRUB boot menu](troubleshooting.xml#entering-grub).

### How do I access protected content in browsers (Widevine DRM) {#widevine}

Run `sudo widevine-installer` and follow the prompts. Note that Widevine
is third-party software not officially affiliated nor endorsed by the
Fedora Project or Asahi Linux.

Netflix will still complain though: \"This title is not available to
watch instantly\", E100. You need to install a browser extension to
override your User-Agent for specific sites (such as [this
one](https://addons.mozilla.org/en-US/firefox/addon/uaswitcher)), and
set the user agent for Netflix to:

Mozilla/5.0 (X11; CrOS aarch64 15329.44.0) AppleWebKit/537.36 (KHTML,
like Gecko) Chrome/111.0.0.0 Safari/537.36

In User-Agent Switcher head to \'Preferences\' and add manually a new
entry with the above String. You may also want to check the option
\"Override for Domain\", to avoid having that User-Agent messing with
other sites, such as Youtube, Slack, etc.

### How do I enable playback of restricted codecs (H.265/HEVC, AC-4, etc.) {#_how_do_i_enable_playback_of_restricted_codecs_h_265hevc_ac_4_etc}

See [Enabling the RPM Fusion
repositories](quick-docs::rpmfusion-setup.xml).

### How do I download software? {#download-software}

A large amount of free and open source software is available in the
Fedora repositories. Just install it directly from your desktop
environment's software management tool or use `dnf`!

Some free software is not packaged directly in Fedora, but aarch64
builds may be available officially or from third parties. Look for
instructions for **Fedora** users and **aarch64** builds. **AppImage**
or **Flatpak** versions may also work as long as they are built for
aarch64.

For example:

- **Visual Studio Code**: Aarch64 builds are available by following the
  [instructions for Fedora
  users](https://code.visualstudio.com/docs/setup/linux#_rhel-fedora-and-centos-based-distributions).

- **Telegram Desktop**: Available in the [RPM Fusion Free
  repository](quick-docs::rpmfusion-setup.xml).

Third-party Fedora builds of software are also available in [Fedora
Copr](https://copr.fedorainfracloud.org/).

Most proprietary software is only available for x86-64 (Intel/AMD)
machines and will not run natively on {variant-name}, but often web
versions or third-party clients are available that do work:

- **Discord**: Use the web version, or try
  [Legcord](https://github.com/Legcord/Legcord/releases/latest) (the
  aarch64 RPM, Flatpak, or AppImage should all work).

- **Spotify**: Follow the instructions in the [How do I access protected
  content in browsers (Widevine DRM)](#widevine) section, and then use
  the web version.

- **Zoom**: Use the [Progressive Web App](https://app.zoom.us/wc).

Note: Fedora does not endorse nor offer support for third-party software
packages or COPR repositories. Make sure you trust the software and
repository you install it from.

## Common issues {#_common_issues}

### Chromium and Chromium/Electron-based apps stop working after an upgrade {#_chromium_and_chromiumelectron_based_apps_stop_working_after_an_upgrade}

Run the following command to resolve the issue:

find \$HOME/.config -name GPUCache -type d -exec /bin/rm -rf {}\

This is caused by an [upstream Chromium
bug](https://bugs.chromium.org/p/chromium/issues/detail?id=1442633).
This step will be necessary after certain upgrades until the fix is
released for the various Chromium-based frameworks and applications
built on them.

## Known bugs {#_known_bugs}

Please see our [bug
tracker](https://pagure.io/fedora-asahi/remix-bugs/issues) for a list of
major known issues.

[^1]: This works with PipeWire running on the host with pipewire-pulse,
    as installed by default. You do **not** need to and should not
    install PulseAudio proper, as that will break your speaker support!
