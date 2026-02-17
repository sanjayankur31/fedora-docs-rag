Fedora Server Edition uses the Fedora installation program, Anaconda, as
several other editions and spins.

While Fedora Server Edition uses the same rpm package repository as all
Fedora editions, the composition of the packages and especially the
defaults of the runtime environment are different and more tailored to a
server requirements. The following paragraphs describe some of the most
important ones. Of course, the administrator can override any of them.

The installation planning depends on the details of the target
environment. Anaconda can install on \'bare metal\' directly on server
hardware as well as in a virtual environment on a virtual machine (VM).
While both targets are similar in many ways, they also differ in key
technical details. As an example, on both targets, the storage
organization is a very important planning item, but on a virtual machine
the system administrator does not need to worry about a RAID system.

Having done various decisions and some preparations, the installation
itself is an easy step-by-step procedure, selecting one of various
available methods.

# Planning ahead {#_planning_ahead}

## Minimum requirements {#_minimum_requirements}

The question of the minimum requirements is always raised, even though
it is obvious to anybody that it depends entirely on the deployment
plan.

Nevertheless, technically, you can run a default Fedora Server on a
storage space of about 5 GiB. The installed system occupies about 2.5
GiB. Of course, such a server would hardly be useful for anything. The
smallest disc currently available for purchase is 64 GiB. With that, you
could satisfactorily run a small to medium server for web and mail
services. For virtual machines, we currently use 40 GiB as default.

Again, from a purely technical point of view, a standard Fedora server
would get by with about 1 GiB of memory. Again, without being able to do
anything useful. The smallest memory chip currently available is 4GiB.
In at least a dual channel server system you need 2, so you have at
least 8 GiB of RAM. For a small to medium sized server for web and mail
services, this is perfectly adequate.

So, with today's smallest possible purchasable hardware, a Fedora server
can be run perfectly for a small to medium deployment.

## Storage organization {#_storage_organization}

Technically, a specific storage organization on a server itself will
result in a specific partitioning of the built-in hard disk(s) and,
beyond that, to the provision of external resources such as a SAN.
However, this is about server installation and therefore only about
partitioning the internal hard disk(s).

If you ask 3 system administrators about the best practice for hard disk
partitioning, you will get at least 5 different answers. There is no
clear, best way to partition your disks. A discussion of the details is
beyond the scope of this article. Talk to your friends, read up on the
subject, search for articles, and make your own judgment.

The Fedora Server Edition working group has also discussed this topic
and agreed on a recommended default configuration. This is explained in
the following sections. It prioritizes the highest possible reliability
and fault tolerance for servers, as well as the lowest possible service
interruption, and accepts a higher level of system administration, for
example.

### What default partitioning does {#_what_default_partitioning_does}

A new Fedora installation creates a (modern) GPT partition table by
default.

On a *BIOSboot* machine, Anaconda creates at first a small (1 MiB)
&#96;&#96;&#96;BIOS boot&#96;&#96;&#96; system partition on the first
drive. It stores the second stage bootloader which is required by
GNU/Grub. Subsequently, it creates a &#96;&#96;/boot&#96;&#96;&#96;
partition of 1 GiB. It contains all the files necessary for booting
Linux, especially the kernel. The remaining area is completely filled
with a third partition containing one large volume group (LVM VG) named
&#96;fedora&#96; by default. You end up with 3 primary partitions on the
hard disk that use all the available space.

Fedora can still use the (legacy) MBR partition scheme, provided that
the disc is not larger than 2 TB. It then omits the
&#96;&#96;&#96;BIOSboot&#96;&#96;&#96; partition and uses only the other
two partitions.

In the case of a *UEFI* boot system, Anaconda creates first the required
\'EFI System\' partition and then adds the aforementioned
&#96;&#96;&#96;/boot&#96;&#96;&#96; partition and one large LVM
partition and Volume Group (VG) as described above. You will end up with
3 partitions on the hard disk that completely occupy the available
space.

In *each* of these alternatives, Anaconda creates one logical volume of
approximately 15 GiB (the exact value depends on the disk capacity of
your system) named &#96;root&#96; for the operating system and its
software. The remaining available space is at the disposal of the system
administrator for free use to store user data.

### The rationale {#_the_rationale}

The rationale behind this is a separation of system and user data, which
eases system administration, increases security, and decreases the
likelihood of errors and data loss. The system area (i.e. the operating
system including installed software) must be maintainable completely
independently of the storage of user data. System maintenance must not
jeopardize user data under any circumstances. If necessary, it must be
possible to unmount user data.

Following this principle, the system administrator would later set up
*additional logical volumes* for storing an application's data and mount
them at an appropriate location in the directory tree. In case of a
PostgreSQL database, for example, a system administrator would create a
logical volume of appropriate size, assign a descriptive name, such as
&#96;pgdata&#96;, and mount it in the directory tree at
&#96;/var/lib/pgsql&#96;, where Fedora PostgreSQL expects the data to
reside.

In this way, any error that may occur in the file system should have as
little impact as possible and jeopardize as little valuable data as at
all possible. For this, the additional effort in system administration
is purposely accepted.

### Taking the rationale further {#_taking_the_rationale_further}

If you are a more experienced administrator, you may wish to further the
rationale above with increased separation.

You will select &#96;Custom&#96; and create the &#96;BIOSboot&#96;,
&#96;efi&#96; and &#96;/boot&#96; partitions as required and a small
partition and VG dedicated to the operating system. A good size for this
VG (eg. &#96;&#96;&#96;sysvg&#96;&#96;&#96;) is, approximately, 30 GiB.
Occupying the remaining space, you will create a dedicated partition and
Volume group (eg. &#96;&#96;&#96;usrvg&#96;&#96;&#96;) for user data.
You will end up with 4 partitions on the hard disk (boot, sysvg, usrvg
with Bios boot machines and hard disks up to 2 TB) rsp. 4 partitions
(BIOSboot/efi, boot, sysvg, usrvg for all other machines) that use all
the available space.

Create a LV (e.g. &#96;&#96;&#96;sys_root&#96;&#96;&#96;) of about 15
GiB for the operating system and maybe additional LVs for the runtime
environment, e.g. a LV &#96;&#96;&#96;sys_log&#96;&#96;&#96; of about 5
GB. Mount it at &#96;&#96;&#96;/var/log&#96;&#96;&#96; to prevent log
files from flooding and blocking the system and, vice versa, prevent
that any other space issue on the root partition block your logs and
complicate error analysis. The remaining free space is left for
distribution as needed over time. Similar to the default partitioning,
all user data is created as LVs in &#96;&#96;&#96;usrvg&#96;&#96;&#96;
and mounted in the corresponding directories of the system. This is the
maximum possible separation of system and user data with only one hard
disk available. And with today's typical hard drive size of 2 TB and
more, those dedicated 30 GBs don't interfere with the effective use of
disk space anymore.

### Raid system {#_raid_system}

If there is more than one disk available, the default partitioning
creates, on each of the other disks, one big partition with a Physical
Volume (PV) and adds it to the VG.

On a server, this is usually not optimal. Rather, several disks should
store data redundantly in order to maintain operation in the event of a
hardware failure. [Configuring a RAID
system](installation/sw-raid-upon-installation.xml) is one such
solution.

## Network connection {#_network_connection}

Anaconda analyzes the hardware and generates at least a basic
configuration file for each network interface found, regardless of
whether a carrier is present. If a DHCP service is detected, anaconda
creates a corresponding complete configuration.

Some system administrators prefer a static configuration even if there
is DHCP available, suspicious as they are of any possible source of
failure. The network configuration is nevertheless a customization
option during the installation.

# Preparations {#_preparations}

## Choosing the right installation medium {#_choosing_the_right_installation_medium}

Fedora Server comes with its own special installation ISO image, either
as a full local installation or as a network installation. If at all
possible, use one of the two [Fedora Server
Edition](https://getfedora.org/en/server/download/) alternatives
(\'Standard\' or \'Netinstall\') and avoid booting from another image.
Anaconda, the installation program and the GUI look alike for any
edition or spin, but are tailored differently under the hood, e.g. with
different configuration defaults.

That's why you don't get a \'Fedora Server Edition\' as a result with
the \'*Everything*\' installation medium, even if you select \'Fedora
Server\' as a software package. This can lead to various problems during
operation and is *not supported*.

## Download the proper installation media {#_download_the_proper_installation_media}

Wether on hardware or on a virtual machine, an installation requires the
download and the verification of an appropriate installation medium. On
your Workstation, you can either use the web browser to download the
image file or open a terminal window and perform the download via CLI
commands.

In the former case, navigate your browser to
*<https://fedoraproject.org/server/download>*, select your hardware
architecture, and follow the instructions to download and verify the
image.

In the latter, navigate to the directory where you want to keep the
files. We will assume your home directory here. For x86_64 systems, type
the following commands line by line.

    […]$ mkdir -p ~/tmp  \&amp;\&amp; cd ~/tmp
    […]$ wget https://download.fedoraproject.org/pub/fedora/linux/releases/41/Server/x86_64/iso/Fedora-Server-dvd-x86_64-41-1.4.iso
    […]$ wget https://download.fedoraproject.org/pub/fedora/linux/releases/41/Server/x86_64/iso/Fedora-Server-41-1.4-x86_64-CHECKSUM
    […]$ wget https://fedoraproject.org/fedora.gpg
    […]$ gpgv --keyring ./fedora.gpg Fedora-Server-41-1.4-x86_64-CHECKSUM
    […]\&#35; sha256sum  --ignore-missing -c Fedora-Server-41-1.4-x86_64-CHECKSUM
    Fedora-Server-dvd-x86_64-41-1.4.iso: OK
    sha256sum: WARNING: 17 lines are improperly formatted

You can safely ignore the last command's warning about incorrectly
formatted lines.

## Create a bootable installation medium {#_create_a_bootable_installation_medium}

A installation on bare metal requires to transfer the installation file
to a bootable media, mostly an USB memory stick. There are several
option:

1.  As a (typically hands-off) server sysadmin, you can use the \'Media
    Writer\' graphical utility provided by the Fedora Project to
    accomplish this task. See [Creating and using a live installation
    image - Using Fedora Media
    Writer](https://docs.fedoraproject.org/en-US/quick-docs/creating-and-using-a-live-installation-image/&#35;using-fedora-media-writer)
    for guidance on using this program.

2.  As a (hard core) server sysadmin to be, you might prefer a fast and
    efficiont CLI tool, the &#96;dd&#96; command. If you are already in
    a terminal window, connect the USB stick and enter the following
    command to get a list of connected devices.

        […]\&#35; lsblk

    Determine the USB device, e.g. &#96;/dev/sdc&#96;

    Just in case, umount the device and transfer the downloaded
    installation file to the device in one go. On the above example use

        […]$ sudo umount /dev/sdc\&#42;
        […]$ dd if=Fedora-Server-dvd-x86_64-41-1.3.iso of=/dev/sdc bs=8M status=progress

    Of course, adjust file and device accordingly! You may receive an
    error message about parameter &#96;status=progress&#96; not
    supported. Then you still have an older dd version and have to leave
    that option off.

3.  And as a (typically busy) server sysadmin to be, you might
    appreciate a tool provided by the Open Source
    [ventoy](https://www.ventoy.net/) project. A small utility on a USB
    stick of any size takes over the presentation of the device to the
    hardware as bootable, and reads itself the ISO file, which is stored
    on a data partition of the stick. Depending on it's size, it can
    accomodate multiple ISO files. The server sysadmin can choose
    between them at boot time in a selection menu. With a new version
    simply copy the ISO file as it is on the stick and ready to go. No
    more dd and no Media Writer.

With everything done proceed with one of the available installation
procedures.

# Fedora Server interactive local installation {#_fedora_server_interactive_local_installation}

Peter Boy; Stephen Daley; Kevin Fenzi :page-authors: Peter Boy, Kevin
Fenzi, Jan Kuparinen

> This is the default method for manually installing Fedora if console
> access is available. The graphical interface is designed with the goal
> of making the installation as simple and speedy as possible. It is
> intended to facilitate the work of the system administrator by
> preassigning as many installation options as possible after analyzing
> the hardware.

With all [preparations and installation plans](index.xml) complete,
insert the prepared installation medium and boot the server. After some
time you get the boot menu screen.

<figure>
<img src="installation/interactive-local-010.png"
alt="The boot screen" />
<figcaption>The Fedora boot screen</figcaption>
</figure>

The second option, *Test this media &amp; install Fedora Server*, is
selected as default. Before the first usage, testing the installation
media is strongly recommended. Subsequent installations can dispense
with this and select the first option.

After a successful test, the routine automatically starts *Anaconda*,
the actual *Fedora installation program*.

First, the program asks for the language to be used during the
installation phase. Anaconda automatically selects a corresponding
keyboard mapping (you can adjust it in the next step). Both are also
adopted as default settings for the system to be installed.

Anaconda will display the following installation overview, with all
available configuration options.

![Anaconda Installation Summary](installation/interactive-local-020.png)

## Server installation steps {#_server_installation_steps}

Anaconda assigns default values to the installation steps based on a
system analysis and the runtime environment. However, the overview marks
3 steps that absolutely require editing:

&#42; *Installation Destination*, i.e. the storage &#42; *Root account*
&#42; *User Creation*

Anaconda does not allow the installation to begin until all marked items
have been processed. The *Begin Installation* button is grayed out until
then.

The default values assigned are usually acceptable. However, two items
deserve the administrator's attention:

&#42; *Keyboard* in case on a non-US runtime environment &#42; *Network
&amp; Host Name*

:::: tip
::: title
:::

While working with Anaconda, help functions are available to you, which
are indicated briefly at the beginning.

&#42; Function key &lt;ctrl&gt;+&lt;alt&gt;+F1: main &#42; Function key
&lt;ctrl&gt;+&lt;alt&gt;+F2: shell &#42; Function key
&lt;ctrl&gt;+&lt;alt&gt;+F3: log &#42; Function key
&lt;ctrl&gt;+&lt;alt&gt;+F4: storage-log &#42; Function key
&lt;ctrl&gt;+&lt;alt&gt;+F5: program-log &#42; Function key
&lt;ctrl&gt;+&lt;alt&gt;+F6: packing-log \| Back to GUI
::::

### Keyboard {#_keyboard}

*Non-US users* should specifically check the keyboard layout. Selecting
this item opens a form where you can set the keyboard layout, even
several ones and their order. A change immediately affects the installer
as well.

### Installation Source {#_installation_source}

In a standard installation (using the \'Standard ISO image\'), Anaconda
uses \'Local media\' which will pull packages from the ISO image on your
install media.

In a network installation select the item and edit the form
appropriately.

*Select Network*. Its default is Mirror List. Anaconda searches an
appropriate mirror and comes up with *everything repository*. In this
case, *everything repository* causes no issues, because the system uses
the anaconda configuration of the server medium booted from. So it gets
the correct default configuration.

When everything repo is active, the \'Software Selection\' item becomes
active, and you have to select \'Fedora Server Edition\'.

Alternatively, you may manually select a server repository directly.

### Installation Destination {#_installation_destination}

![Anaconda Installation
Destination](installation/interactive-local-050.png)

Select one or more disks on which to install Fedora Server. You have
several options.

&#42; &#42;Automatic configuration&#42;

\+ Anaconda defaults to Automatic, which follows the recommended default
storage organization and partitioning.

&#42; &#42;Software raid configuration&#42;

\+ If there is more than one disk available, the default partitioning
creates, on each of the other disks, one big partition with a Physical
Volume (PV) and adds it to the Volume Group (VG). On a server, this is
usually not optimal. Rather, you would use the opportunity to store data
redundantly and open up the opportunity to maintain operation in the
event of a disk failure.

\+ If your machine doesn't include a hardware raid capability, you may
configure a software RAID system. Switch to [Exkurs: Configuring a
software RAID during
installation](installation/sw-raid-upon-installation.xml) and then
continue here with the Network section.

&#42; &#42;Custom configuration&#42;

\+ This option allows you to overwrite the default partitioning
according to your requirements. You just have to specify a mountpoint
and some properties, Anaconda takes care of all the required
configuration steps.

\+ The Advanced Custom option also opens up this option, but you have to
perform all the necessary configuration steps manually by yourself.

&#42; &#42;External storage&#42;

\+ The *Add a disk* enables you to include external storages, e.g. a SAN
(Storage Attached Network) or other network attached drives as part of
your Fedora Server install in this same configuration screen. However,
this configuration is not covered here in this installation guide.

#### Automatic default configuration {#_automatic_default_configuration}

If you are satisfied with the Fedora Server default hard disk
partitioning as described in the [Server
installation](installation/index.adoc&#35;_what_default_partitioning_does)
introduction, you can leave *Automatic* checked under *Storage
Configuration*.

:::: tip
::: title
:::

Fedora Server uses LVM by default and creates a Volume Group to enclose
the root filesystem. The default name is &#96;fedora&#96;. When you
first edit the network configuration and specify a custom hostname, it
is appended, i.e. the VG name becomes
&#96;fedora\_&lt;hostname&gt;&#96;. This is often useful if managing
multiple Fedora servers in a federation, as it avoids duplicate VG
names. In any case, you can edit the Volume Group name later in
*Installation Destination*.
::::

No further steps are required besides the disks already contain
partitions and file systems. In this case you may want to select the
option \'Free up space by removing or shrinking existing partitions\'.
Then select *Done* in the upper bar and you are \'done\'.

::: informalexample
If you selected the option to free up space, a window will open after
you click *Done* giving you the opportunity to confirm to delete
partitions and file systems to make space for your Fedora Server
installation or to retain one or more partition.
:::

#### Custom storage organization {#_custom_storage_organization}

Select *Custom* Storage Configuration instead of *Automatic* and select
*Done* in the upper bar. Anaconda will take you to the *Manual
Partitioning* form.

![Anaconda Manual Partitioning
form](installation/interactive-local-070.png)

By clicking onto the + sign you can add partitions according to your
storage concept.

Fedora uses a GPT partitioning scheme. Thus, on a BIOSboot system you
must add a BIOSboot partion, preferrably as the first one. On a UEFIboot
system you have to add a EFI system partition, preferrably as the first
one. If you forget it, Anaconda will remind you.

##### How to find out if firmware is efi-boot or bios-boot {#_how_to_find_out_if_firmware_is_efi_boot_or_bios_boot}

Open a temporay shell by using
&#96;&lt;alt&gt;+&lt;ctrl&gt;+&lt;F2&gt;&#96; and type into the terminal
window:

    \&#35; [ -d /sys/firmware/efi ] \&amp;\&amp; echo UEFI || echo BIOS

The command shows in the next line either UEFI or BIOS. Use
&#96;&lt;alt&gt;+&lt;ctrl&gt;+&lt;F6&gt;&#96; to return to the
installation screen.

### Networking {#_networking}

Before configuring the Installation Destination configure the Network
&amp; Host Name to give your server a hostname. The new hostname can be
entered at the bottom of this screen and then pressing the *Apply*
button.

The hostname is important for smooth functioning of various services.
Unless the server is integrated into a cluster, a fully qualified static
hostname (FQN) is used, i.e. server name and the domain
(\'my-server.example.com\'). Enter the hostname and confirm with
\'Apply\'.

In a cluster, the hostname is often assigned by DHCP and MAC address. In
this case, leave the field untouched.

By default the installation program creates a DHCP configuration for
each network interface. In the case of an active connection it is
automatically started during boot.

In case of servers it is often preferable to configure a static IP
address. This ensures a valid network connection at system start even if
the DHCP server is defective. Select the network interface, activate the
IPv4 or IPv6 tab. Switch from \'Automatic (DHCP)\' to \'Manual\' and add
an IP specification.

:::: note
::: title
:::

Post Fedora 36, NetworkManager stores the configuration exclusively in
*/etc/NetworkManager/connected_systems/&#42;.network*. The former
/etc/sysconfig/network-scripts directory is no longer supported at all.
::::

### Creating users {#_creating_users}

First, decide if you desire to have a root account on Fedora Server.
Anaconda's default configuration disables the root account to prevent
malicious actors from logging in as root. Instead, Anaconda requires a
user account that can acquire administrative privileges using sudo.

It is possible to secure root access using an ssh key file, but server
administrators may desire to retain the ability to have root access with
a password through an attached console or Cockpit login. If you decide
that you would like to have password access to the root account, select
Root Account, then Enable root account, and enter a password for the
root account in the form that appears. For security reasons, ssh login
as root is only allowed with an ssh key file by default. You are not
encouraged to modify this security setting by clicking on the option,
\'Allow root SSH login with password\'.

Second, select User Creation to create a user account for Fedora Server.
You are encouraged to keep the default options of \'Add administrative
privileges to this user account\' and \'Require a password to use this
account\' checked. Unless you have decided against the security practice
of not allowing root access with a password, your user account will need
these options to have administrative access to the server after
installation of Fedora Server.

### Time zone and time synchronization {#_time_zone_and_time_synchronization}

You may want to check Time &amp; Date on the Installation Summary page
to ensure that you have the correct time zone and Network Time is
activated. These settings ensure that your server will regularly
synchronize its time with a trusted source. Having the correct time on
your server will make tasks like finding events at a specific time and
date in your log files easier.

On the \'Installation Summary\' page select \'Time &amp; Date\' and
check time, time zone and activation of time synchronization.

## Start Installation {#_start_installation}

Finally, check the default assignments of all options that have not been
edited.

Then, when all settings and configurations fit, select *Begin
Installation* and lean back (or get a coffee!). When finished, confirm
the option to restart the computer. Log in and follow the [post
installation suggestions](installation/postinstallation-tasks.xml).

# Fedora Server remote interactive installation guide {#_fedora_server_remote_interactive_installation_guide}

Peter Boy; Kevin Fenzi; Jan Kuparinen; Jiri Konecny :page-authors: Peter
Boy, Kevin Fenzi, Jan Kuparinen, {author_4}

> With this method, the server is usually residing in a remote location,
> such as a data center. It boots from a prepared installation media
> into the Anaconda installation program configured to start and use a
> \'remote desktop protocol\' (RDP) server instead of a local physical
> console. The system administrator connects using a RDP client on a
> local desktop to the server and runs through the Anaconda graphical
> installer. This method is best suited for servers without any or just
> cumbersome available direct console access.

## Prerequisites {#_prerequisites}

Proper install media available

:   You need one of the installation media variants ready to use as
    described in [Server Installation](installation/index.xml)

RDP client

:   Performing an RDP installation requires an RDP client running on
    your workstation or another terminal computer. RDP clients are
    available in the repositories of most Linux distributions; free RDP
    clients are also available for other operating systems, such as
    Windows. On Linux systems, use your package manager to search for a
    RDP for your distribution.

    The following RDP clients are available in Fedora:

    &#42; GNOME Connections - Connections is a remote desktop client for
    the GNOME desktop environment. &#42; freerdp - Free implementation
    of the Remote Desktop Protocol (RDP)

    To install any of the clients listed above, execute the following
    command as root:

        [\&#8230;]\&#35; dnf install PACKAGE_NAME

    Replace package with the package name of the client you want to use
    (for example, freerdp).

## Booting the server {#_booting_the_server}

There are several options to boot the server, depending on the ethernet
connection method and availability of at least some, maybe cumbersome
and short living local console access.

### Console access available {#_console_access_available}

1.  Boot the server to be installed and wait for the *boot menu* to
    appear.

    ![Boot Menu](installation/interactive-remote-010.png)

2.  In the menu, select the kernel you want to boot and type *e* to get
    access to the boot options and append

    inst.rdp inst.rdp.username=USER inst.rdp.password=PASSWORD

    to the end of the command line. Optionally, it is possible to set a
    password (inst.rdp.password) and/or username (inst.rdp.username).
    Replace PASSWORD and USER with the password and username of your
    choice. Password must be at least 6 characters long. If password
    and/or username is not set the Anaconda installer will ask
    interactively.

    :::: important
    ::: title
    :::

    For security considerations, use a temporary password for the
    inst.rdp.password= option. It should not be a real or root password
    you use on any system.
    ::::

    The above configuration requires an active DHCP server. With none
    available, you must provide a static interface configuration as
    well.

    ip=ip::gateway:netmask:hostname:interface:none inst.rdp
    inst.rdp.password=PASSWORD inst.rdp.username=USER

3.  Leave the editing mode by &lt;ctrl&gt;-x or F10 to continue to boot
    and to start the installation using the selected kernel and the
    edited options. You get the message

        Booting a command list

    The system will initialize the installation program and start the
    necessary services. It takes some time. And after a lot of boot
    messages, when the system is ready, you get:

        Starting installer, one moment
        \&#8230;
        hh:mm:ss Starting GNOME remote desktop in RDP mode\&#8230;
        hh:mm:ss GNOME remote desktop RDP: SSL certificates generated \&amp; set
        hh:mm:ss GNOME remote desktop RDP: user name and password set
        hh:mm:ss Starting GNOME remote desktop.
        hh:mm:ss GNOME remote desktop is now running.
        hh:mm:ss GNOME remote desktop RDP IP: 192.168.122.247
        hh:mm:ss GNOME remote desktop RDP host name: fedora

    Continue with *3.2. Connecting to the server*.

#### No console access available -- patch installation medium {#_no_console_access_available_patch_installation_medium}

If none of the above options work with your server and network
configuration, you could patch the installation media as a last resort.
As an example, you can change the grub boot lines in
/isolinux/grub.conf. You would need to add the RDP parameter and remove
the integrity test, as this is the default line but would fail after
patching.

We won't go into this matter any further here. This is really the very
last resort and is not recommended.

## Connecting to the server {#_connecting_to_the_server}

1.  In case of a server without a console attached determine the IP
    address.

    a.  If possible, check the DHCP server for the IP of the server.

    b.  Scan the network subnet the server is connected to for open
        port 3389. Adjust the network IP address accordingly!

        ``` bash
        […]\&#35; dnf install nmap
        […]\&#35; nmap -Pn -p3389 192.168.158.0/24
        Starting Nmap 7.80 ( https://nmap.org ) at 2021-05-23 08:18 CEST
        Nmap scan report for example.com (192.168.158.1)
        Host is up (0.00052s latency).

        PORT     STATE  SERVICE
        3389/tcp closed nn-admin
        MAC Address: 34:81:C4:14:21:B4 (AVM GmbH)

        Nmap scan report for iMac.fritz.box (192.168.158.111)
        Host is up (0.00051s latency).
        \&#8230;
        \&#8230;
        PORT     STATE SERVICE
        3389/tcp open
        MAC Address: B8:27:EB:5A:EC:84

        Nmap scan report for 192.168.158.200
        Host is up (0.00068s latency).
        \&#8230;
        \&#8230;
        Nmap done: 256 IP addresses (12 hosts up) scanned in 2.38 seconds
        ```

        Look for an entry with open state of port 3389 and no hostname
        or unknown hostname. Among them you will probably find the
        device you are looking for. In the example above it is
        192.168.158.200.

2.  On the desktop start the GNOME connections, add new connection with
    a plus symbol, enter the IP address obtained in the previous step.
    You will be asked to confirm certificates. These are generated by
    Anaconda and they are different for each installation.

    Alternatively, use freerdp client with

        xfreerdp /v:192.168.158.200 /u:USER /p:PASSWORD

3.  When the connection is successfully established, a new window will
    open on the system running the RDP client, displaying the
    installation menu. You will be presented with the familiar language
    selection menu.

    :::: formalpara
    ::: title
    The language selection installation window
    :::

    ![interactive remote 015](installation/interactive-remote-015.png)
    ::::

    This window will provide full remote access to the installer until
    the installation finishes and the system reboots for the first time.

    :::: tip
    ::: title
    :::

    If the screen freezes after some mouse or keyboard actions, add the
    kernel option *nomodeset* before the term *inst.rdp* to the kernel
    commad line in step *3.1.1*.
    ::::

You can then proceed with [Fedora Server interactive local
installation](:installation/interactive-local.xml).

# Excursus: Configuring a software RAID upon interactive installation {#_excursus_configuring_a_software_raid_upon_interactive_installation}

Peter Boy; Stephen Daley; Kevin Fenzi :page-authors: Peter Boy, Kevin
Fenzi, Jan Kuparinen

> This Exkurs describes the configuration of a *software RAID* as part
> of an interactive Fedora Server Edition installation. In this case,
> the RAID capability is provided by operating system drivers and
> processed bei the computer CPU. It does not cover firmware raid (also
> called Windows RAID), which provide this capability via the computer
> internal firmware, nor hardware raid, where dedicated integrated
> hardware modules or adapters completely relieve the computer CPU of
> the raid processing.

The RAID configuraton starts at the \'Installation Destination\' window.

:::: formalpara
::: title
The Installation Destination window
:::

![001
installationdestination](installation/sw-raid/001-installationdestination.png)
::::

The *Local Standard Disk* list must include at least two hard disks. And
please, ignore the USB drive that provides the installation system, in
case Anaconda doesn't hide the installation media anyway.

Before you start with partitioning, you have to determine the boot type
of your system, UEFI boot or BIOS (or legacy) boot system. Fedora
defaults to the GPT partitioning scheme which was created with UEFI boot
systems in mind. On a BIOS boot system, it requires a special partition.

:::: note
::: title
:::

Just in case you need a DOS/MBR partitioning scheme for some good
reason, you can override the GPT default by adding \'inst.mbr\' to the
kernel boot parameter at the initial boot screen.
::::

If you don't know the type of your system for sure, you can check the
system now. Open a temporay shell by using
&#96;&lt;alt&gt;+&lt;ctrl&gt;+&lt;F2&gt;&#96; and type into the terminal
window:

    \&#35; [ -d /sys/firmware/efi ] \&amp;\&amp; echo UEFI || echo BIOS

The command shows in the next line either UEFI or BIOS. Use
&#96;&lt;alt&gt;+&lt;ctrl&gt;+&lt;F6&gt;&#96; to return to the
installation screen.

There are then two installation options:

&#42; The \'&#42;&#42;Custom&#42;&#42;\' option

\+ This way you just specify the mountpoints and Anaconda performs all
the necessary steps for you. If needed you can adjust some properties
afterwards. That's the comfortable way.

\+ Unfortunately, Anaconda does not necessarily keep the arrangement of
the partitions that you have chosen, but sorts the partitions as it sees
fit. This causes no problems at all in everyday operation. But if, for
example, you have placed a partition at the end to preserve the
possibility of making adjustments later, that could go wrong.

&#42; the \'&#42;&#42;Advanced Custom (Blivet-GUI)&#42;&#42;\' option

\+ This way, you can and must perform each individual step of
partitioning, configuring LVM volumes and creating file systems by
yourself. This is the more laborious way.

\+ The advantage is that you can define every detail and you will get a
partitioning exactly according to your plan. And the GUI supports the
work very effectively.

Select all drives you want to include in the prospective RAID drive,
click on the partitioning option you want to use and then on Done in the
uper left corner.

## Custom partitioning {#_custom_partitioning}

Anaconda opens a new window:

:::: formalpara
::: title
The custom partitioning start up screen
:::

![101 custom start](installation/sw-raid/101-custom-start.png)
::::

1.  &#42;Check all disks for existing partitions&#42;

    If the area beyond *Unknown* contains one or more partition, check
    whether you want to retain, reuse, or delete it. Mind that you can
    only reuse partitions that are set up identically on all disks.

    To delete a partition, click on it and then on the \'-\' sign at the
    bottom. At the end, all disks must either be empty or identically
    partitioned.

2.  &#42;On a BIOS boot system only, create a biosboot partition on each
    disk&#42;

    On a BIOS boot system, a GPT partition table as used by Fedora
    requires a small BIOSBoot partition for the Grub boot loader. Create
    it at the beginning of each disk to keep the system operational when
    one disk fails. Skip this step, if your host uses UEFI!

    Use the \'+\' sign to add a partition. In the Mount Point field
    select \'biosboot\' and set a size of 1 MiB.

    A biosboot entry appears in the left *New Fedora 41 Installation*
    section on one of he disks.

    Repeat it and you see a second entry, usually on the same disk.

    :::: formalpara
    ::: title
    The BiosBoot installation
    :::

    ![105 custom biosboot
    1](installation/sw-raid/105-custom-biosboot-1.png)
    ::::

    Select the new entry and click on *Modify* at *Device(s)*. In the
    device list select one of the other disks. Then select *Update
    Settings*.

    Anaconda updates the list of partitions in the *New Fedora 41
    installation* section so that the biosboot partition is now the
    first partition on different disks.

    :::: formalpara
    ::: title
    The adjusted BiosBoot installation
    :::

    ![110 custom biosboot
    2](installation/sw-raid/110-custom-biosboot-2.png)
    ::::

    Repeat the step until all disks have a biosboot partition. This is
    necessary so that the system can boot from any of the other disks if
    the first disk fails.

3.  &#42;On a UEFI boot system only, create an EFI partition&#42;

    Use the \'+\' sign to add a partition. The \'*Add a new Mount Point
    form*\' form opens up

    &#42; select /boot/efi as the mount point &#42; enter 600 Mib as
    size &#42; Tick \'Add Mount Point\'

    The installation window refreshes and now shows a /boot/efi
    partition on the left side under SYSTEM and a number of properties
    for this partition on the right side.

    :::: formalpara
    ::: title
    Initial EFI system partition
    :::

    ![120 custom efi 1](installation/sw-raid/120-custom-efi-1.png)
    ::::

    Anaconda sets up an EFI partition on the first disk. But a RAID
    system must be able to boot from any of the available disks, not
    just the first one. Otherwise, the system would be paralyzed if that
    failed. One solution is to set up the EFI partition as a RAID as
    well.

    Find the property Device Type and use the drop down list to change
    Standard partition to RAID. In the right side shows up a new
    selection box RAID level showing initially RAID1 (mirroring) in this
    example, because we have just 2 disks. Leave the file system as "EFI
    System Partition". Choose an optional label, e.g. sysefi, and And
    trigger "Update Settings" further below.

    :::: formalpara
    ::: title
    Final EFI system partition properties
    :::

    ![125 custom efi 2](installation/sw-raid/125-custom-efi-2.png)
    ::::

4.  &#42;Add a *boot* Partition&#42;

    Tick the \'+\' sign and a form \'Add a new Mount Point\' opens
    again.

    &#42; select /boot as the mount point &#42; enter 1 Gib as size
    &#42; Tick \'Add Mount Point\'

    A new mount point is created on sda1. On the right side there is a
    form to show and modify some properties. Find the property *Device
    Type* and use the drop down list to change Standard partition to
    *RAID*. In the right side shows up a new selection box *RAID level*
    showing initially RAID1 (mirroring) in this example, because we have
    just 2 disks. Choose the RAID level you wish and then click on
    *Update Settings* further down.

    Anaconda updates the form and the list beyond *New Fedora 41
    Installation*. The sdx partition is gone and replaced by a (device)
    name, the same one you find in the property form on the right side.
    In the form you can add a label, e.g. sysboot, if you like, and
    *Update Settings* again.

    :::: formalpara
    ::: title
    Final properties of the boot device (raid partition)
    :::

    ![130 custom
    finalbootform](installation/sw-raid/130-custom-finalbootform.png)
    ::::

5.  &#42;Add a *root* mount point&#42;

    Use the \'+\' sign to add another Moint Point

    &#42; select / as the mount point &#42; enter 15 Gib as size &#42;
    Tick \'Add Mount Point\'

    Anaconda creates a new mount point. From the context Anaconda
    guesses to assign the device type LVM, to create a Volume Group
    using the default name *fedora* appending the systems hostname, if
    you already configured the network, and to assign the device name
    root. The size of 15 GiB is the same as a default configuration
    would do. That's a lot of work that Anaconda saves you.

    :::: formalpara
    ::: title
    Anaconda generated LVM root volume and filesystem
    :::

    ![140 custom generated
    root](installation/sw-raid/140-custom-generated-root.png)
    ::::

    Now you have the opportunity the adjust Anacondas guessings.

    The most important one is to adjust the RAID level. Anaconda
    configures a LVM without RAID by default. Tick the modify button of
    the LVM property.

    :::: formalpara
    ::: title
    Anaconda LVM properties form
    :::

    ![145 custom lvm
    properties](installation/sw-raid/145-custom-lvm-properties.png)
    ::::

    Select a proper RAID level and check the size policy.

&#42; *Automatic* means that the size of the partition and the Volume
Group is just as large as the Logical Volumes you create with Anaconda
here. That provides you a maximum of flexibilty to later adjust the
storage organisation but also involves some additional steps to handle
the Volume Group and its partition when you want do add a Logical Volume
and file system. &#42; *Maximum size* expands the Volume Group to fill
up the complete hard disk, so you can add Logical Volumes with a minimum
of effort. That is the recommended way for medium size disks. &#42;
*Fixed size* lets you specify a size that fulfills your foreseeable
requirements and leaving some space for later adjustments that come up
as a surprise.

\+ This option also allows for an *even stronger separation of system
and user data*. Specify a fixed size of 20-30 GiB for a system volume
group (named e.g. fedora_sysvg). This contains the root file system and,
if applicable, further system-related logical volumes. In the remaining
space you will later set up a user volume group (correspondingly named
fedora_usrvg) and logical volumes for user data. This gives you the
greatest possible flexibility to adapt the system area to changes in
demand or technical developments without touching the precious user data
at all. This is recommended for large hard disks, servers with a planned
longtime lifespan, or remotely located servers.

1.  &#42;Customize the storage organisation to your requirements&#42;

    Finally, you can further customize the storage organization to your
    requirements.

    Some adminmistrators like to confine the /var/log subdirectory in
    its own Logical Volume. This prevents excessive logging from filling
    up the root file system. But also vice versa, that excessive outputs
    of a program fill up the root file system to such an extent that no
    more log outputs can be saved and troubleshooting is made more
    difficult.

Finally, click on Done, in the upcomming list accept the Changes and
return now to the original guide, probably [Fedora Server interactive
local
installation](:installation/interactive-local.adoc&#35;_networking)
guide.

## Advanced Custom partitioning {#_advanced_custom_partitioning}

Anaconda opens a new window:

:::: formalpara
::: title
The advancced custom partitioning start up screen
:::

![201 adv custom start](installation/sw-raid/201-adv-custom-start.png)
::::

1.  &#42;Check all disks for existing partitions&#42;

    If there are partitions on any of the hard disks, delete the
    partitions if they are no longer needed. Note that you can only
    reuse partitions that are set up identically on all hard disks.

    To delete a partition, click on it and then on the circled \'x\'
    sign below. In the end, all hard disks must either be empty or
    identically partitioned. In the following, we assume that the hard
    disks are empty.

2.  &#42;On a BIOS boot system only, create a biosboot partition on each
    disk&#42;

    On a BIOS boot system, a GPT partition table as used by Fedora
    requires a small BIOSBoot partition for the Grub boot loader. Create
    it at the beginning of each disk to keep the system operational when
    one disk fails. Skip this step, if your host uses UEFI!

    Usually, the first Disk is sda and already selected. A large blue
    bar at the top represents the disk. Otherwise, click onto the left
    side onto the sda symbol. With the \'plus\' symbol just beyond the
    central sda area you start to create a partition.

    :::: formalpara
    ::: title
    Create a BIOS Boot partition
    :::

    ![205 adv custom
    biosboot](installation/sw-raid/205-adv-custom-biosboot.png)
    ::::

    First select \'Bios Boot\' in the „Filesystem" selection field and
    then enter 1 MiB as the size. An OK creates the partition and
    updates the free space area. 1 MiB is quite sufficient, but
    sometimes the dialogue insists on 2 MiB and corrects the entry
    accordingly. That's fine, too.

    Next, click on sdb and thus activate it for editing. Repeat the
    process to create a BIOSBoot partition as before.

    When both BIOSBoot partitions have been created, check again whether
    the size and position are actually the same in both cases! You can
    switch between the two disk views by clicking on the sda1 and sda2
    icons respectively.

3.  &#42;On a UEFI boot system only, create an EFI partition&#42;

    If you have not already done so, activate the first hard disk,
    usually sda, by clicking on the icon in the left column. With the
    \'plus\' symbol just beyond the central sda area you start to create
    a partition.

    :::: formalpara
    ::: title
    Creating EFI system partition
    :::

    ![210 adv custom uefi](installation/sw-raid/210-adv-custom-uefi.png)
    ::::

    Anaconda sets up an EFI partition on the first disk. But a RAID
    system must be able to boot from any of the available disks, not
    just the first one. Otherwise, the system would be paralyzed if that
    failed. One solution is to set up the EFI partition as a RAID as
    well. Therefore, select \'Software RAID\' in the \'Device type\'
    selection box and replace \'partition\'. Then fill out the rest of
    the form as indicated.

    &#42; select sda and sdb as RAID members &#42; select RAID level
    raid1 &#42; enter 0.6 GiB size &#42; select Filesystem \'EFI System
    Partition\' &#42; enter Label \'sysefi\' &#42; enter Name
    \'boot_efi\' &#42; Enter Mountpoint /boot/efi &#42; Tick \'OK\'

    The installation window refreshes and now shows a new RAID entry in
    the left column and a boot_efi partition in the sda disk.

    :::: formalpara
    ::: title
    Partitions list including EFI system partition
    :::

    ![212 adv custom
    uefilist](installation/sw-raid/212-adv-custom-uefilist.png)
    ::::

4.  &#42;Creating a *boot* Partition&#42;

    Click into the free space on sda to activate it and tick the \'+\'
    sign again to open a new device form.

    :::: formalpara
    ::: title
    Creating a boot partition
    :::

    ![215 adv custom boot](installation/sw-raid/215-adv-custom-boot.png)
    ::::

    In the "Device type" selection box, select "Software RAID" . The
    form changes. Then fill out the rest of the form as indicated.

    &#42; select sda and sdb as RAID members &#42; select RAID level
    raid1 &#42; enter 1.0 GiB size &#42; keep Filesystem \'xfs\' &#42;
    enter Label \'sysboot\' &#42; enter Name \'boot\' &#42; Enter
    Mountpoint /boot &#42; Tick \'OK\'

    The installation window refreshes and now shows another new RAID
    entry in the left column and a boot partition in the sda disk.

    :::: formalpara
    ::: title
    Partitions list including EFI and boot partitions
    :::

    ![217 adv custom
    bootlist](installation/sw-raid/217-adv-custom-bootlist.png)
    ::::

5.  &#42;Creating a system Volume Group&#42;

    Click into the free space on sda to activate it and tick the \'+\'
    sign again to open a new device form.

    :::: formalpara
    ::: title
    Creating a system Volme Group partition
    :::

    ![220 adv custom
    syspv](installation/sw-raid/220-adv-custom-syspv.png)
    ::::

    Again, in the "Device type" selection box, select "Software RAID"
    and then fill out the rest of the form as indicated.

    &#42; select sda and sdb as RAID members &#42; select RAID level
    raid1 &#42; Specify the size of the partition. There are basically
    three options. &#42;&#42; *Leave the size as suggested by the form*,
    which fills the rest of the hard disk. Both system and user data are
    stored in a common volume group. This is appropriate for hosts with
    a planned lifespan of a few years or less and/or a disk capacity of
    less than 0.5 - 1 TB. &#42;&#42; *Set aside a 20--30/50 GiB
    partition for the system area* and, in the next step, another
    partition exclusively for user data. This is particulary recommended
    for systems with a planned longtime lifespan, a hard disk capacity
    of more than 1--2 TiB, and especially for systems in remote data
    centers where there is never any possibility of accessing the system
    console. In the latter case, it is especially important to keep
    system and user areas strictly separated as far as possible on the
    same hard disk, in order to be able to carry out any system work
    without ever having to touch the precious user data. &#42;&#42; In
    either case, *leave some free space at the end* to allow for
    possible future adjustments to changing and unpredictable needs.

    In this example, we use a 30 GiB system area and the entire rest for
    a dedicated user area.

    &#42; Select \'physical volume (LVM)\' for Filesystem. &#42; enter
    Name \'syspv\' &#42; Tick \'OK\'

    The list view refreshes and shows the harddisks with the 3
    partitions and on the left column an additional RAID device.

    :::: formalpara
    ::: title
    Partitions list including EFI, boot and physical volume partitions
    :::

    ![222 adv custom
    syspvlist](installation/sw-raid/222-adv-custom-syspvlist.png)
    ::::

    In contrast to other GUIs, a volume group (VG) is not created
    immediately, but a \'physical volume\' is created first. Many other
    GUIs perform this step implicitly and automatically.

    Double-click onto the syspv icon in the left bar to activate it and
    then on the Plus sign to open a device creation form.

    :::: formalpara
    ::: title
    Partitions list including EFI, boot and physical volume partitions
    :::

    ![224 adv custom
    sysvgform](installation/sw-raid/224-adv-custom-sysvgform.png)
    ::::

    Leave the Device type and Size field as is und enter \'sysvg\' into
    the Name field. Tick OK to submit the form.

    The overview list screen now shows a new Volume Group device
    \'sysvg\' beyond a new category \'LVM\'.

    :::: formalpara
    ::: title
    Devices list showing partitions, volume groups and RAID devices
    :::

    ![226 adv custom
    sysgvlist](installation/sw-raid/226-adv-custom-sysgvlist.png)
    ::::

6.  &#42;Optional: Creating a user Volume Group&#42;

    If you have opted for a separate user area as recommended, you
    should now create a corresponding volume group. Repeat the steps
    from the previous section accordingly.

&#42; Double-click on sda and into the free space to activate it and
tick the \'+\' sign again to create an additional RAID partition and
physical volume.

\+ .Creating a user physical volume on RAID ![230 adv custom
usrpv](installation/sw-raid/230-adv-custom-usrpv.png)

\+ Either leave the suggested size value as it is to set up the entire
free area for user data, or choose a smaller value to keep free
disposition storage.

&#42; Double-click onto the usrpv icon in the left bar to activate it
and then on the Plus sign to open a device creation form.

\+ .Partitions list including EFI, boot and physical volume partitions
![234 adv custom usrvg](installation/sw-raid/234-adv-custom-usrvg.png)

\+ Leave the Device type and Size field as is und enter \'usrvg\' into
the Name field. Tick OK to submit the form.

\+ The overview list screen now shows a new Volume Group device
\'sysvg\' beyond a new category \'LVM\'.

\+ .Devices list showing partitions, two volume groups and RAID devices
![236 adv custom
usrvglist](installation/sw-raid/236-adv-custom-usrvglist.png)

1.  &#42;Creating the ROOT file system&#42;

    As in the previous steps, clicking on symbol sysvg activates the
    unit for editing and clicking on the free area releases the plus
    sign. A click on the plus sign opens the dialogue for setting up a
    file system.

    :::: formalpara
    ::: title
    Creating the ROOT file system
    :::

    ![240 adv custom
    rootfsform](installation/sw-raid/240-adv-custom-rootfsform.png)
    ::::

    Leave the Device type and Avalable devices as is.

&#42; Specify the size of the root file system. A value of 12 GiB for
the mere system files is large enough for the usual use cases and still
has a lot of leeway for unusual situations. &#42; Complete the other
fields as indicated and tick OK.

\+ .Devices list showing partitions, two volume groups and RAID devices
![244 adv custom
rootfslist](installation/sw-raid/244-adv-custom-rootfslist.png)

1.  &#42;Some typical optional adjustments to the storage
    organization&#42;

    Finally, you can further customize the storage organization to your
    requirements.

&#42; *Optional: Create a separate log file system*

\+ Some adminmistrators like to confine the /var/log subdirectory in its
own Logical Volume. This prevents excessive logging from filling up the
root file system. But also vice versa, that excessive outputs of a
program fill up the root file system to such an extent that no more log
outputs can be saved and troubleshooting is made more difficult.

\+ As in the previous steps, clicking on symbol sysvg activates the unit
for editing and clicking on the free area releases the plus sign. A
click on the plus sign opens the dialogue for setting up a file system.

\+ .Creating log file system ![250 adv custom
varlogform](installation/sw-raid/250-adv-custom-varlogform.png)

\+ Leave the Device type and Avalable devices as is

\+ &#42;&#42; Specify the size of the file system. A value of 3 or 5 GiB
is usually large enough. &#42;&#42; Complete the form as indicated

\+ .Devices list showing the /var/log file system ![254 adv custom
varloglist](installation/sw-raid/254-adv-custom-varloglist.png)

\+

&#42; *Optional: Setting up a home directory storage space*

\+ An Internet server that only provides web and e-mail services usually
only allows administrative users that do not use the server to store
important personal data. A separate file system is often superfluous.

\+ But sometimes they need to upload some data for further processing on
the server. You may want to keep those separate from the system files
and create a small home file system, maybe just in the system Volume
Group if you decided for a strict separation as recommended above.

\+ For a large number of users, use the user area, if available

\+ &#42;&#42; Select a siutable Volume Group, double-click on the device
in the left column (sysvg or usrvg), and then into the free space to
release the \'plus\' button.

\+ .Creating a home file system ![260 adv custom
usrhomeform](installation/sw-raid/260-adv-custom-usrhomeform.png)

&#42;&#42; Leave the Device type and Avalable devices as is &#42;&#42;
Specify a reasonable size of the home file system. For a system with
only administravie users, a value of 3 or 5 GiB is usually large enough.
&#42;&#42; Complete the form as indicated

\+ .Storage overview including a home file system ![264 adv custom
usrhomelist](installation/sw-raid/264-adv-custom-usrhomelist.png)

&#42; *Optional: Setting up a server (/srv) storage space*

\+ According to the Filesystem Hierarchy Standard (FHS), a system should
store site-specific data served by the server, such as data and scripts
for web servers, data offered by FTP servers, etc. in /srv. These belong
into a separate file system.

&#42;&#42; Select a suitable Volume Group, in this example usrvg if
available. Double-click on the device in the left column and then into
the free space to release the \'plus\' button.

\+ .Creating a srv file system ![270 adv custom
srvform](installation/sw-raid/270-adv-custom-srvform.png)

&#42;&#42; Leave the Device type and Avalable devices as is. &#42;&#42;
Specify a reasonable size depending on your system plannings. &#42;&#42;
Complete the form as indicated.

\+ .Devices list showing the srv file system ![274 adv custom
srvlist](installation/sw-raid/274-adv-custom-srvlist.png)

&#42; *If applicable: Setting up a virtual machine's storage space*

\+

&#42;&#42; Select a suitable Volume Group, in this example usrvg if
available. Double-click on the device in the left column and then into
the free space to release the \'plus\' button.

\+ .Creating a libvirt file system ![280 adv
libvirtform](installation/sw-raid/280-adv-libvirtform.png)

&#42;&#42; Leave the Device type and Avalable devices as is. &#42;&#42;
Specify a reasonable size depending on your system plannings. &#42;&#42;
Complete the form as indicated.

\+ .Devices list showing libvirt file system ![284 adv custom
libvirtlist](installation/sw-raid/284-adv-custom-libvirtlist.png)

Finally, click on Done, in the upcomming list accept the Changes and
return now to the original guide, probably [Fedora Server interactive
local
installation](:installation/interactive-local.adoc&#35;_networking)
guide.

# Post Installation Tasks {#_post_installation_tasks}

Peter Boy; Stephen Daley; Kevin Fenzi :page-authors: Peter Boy, Kevin
Fenzi, Jan Kuparinen

> This guide offers a recommended checklist of tasks to ensure the safe
> and reliable operation of Fedora Server. System administrators may
> choose whether these tasks apply to their specific use case.

To perform the administrative tasks described here, you need either any
Linux or any macOS desktop or laptop. On Windows computers, you need at
least Windows 10 1809 or additional programs such as Putty.

## Simplified access for the administrative account {#_simplified_access_for_the_administrative_account}

In a default installation, the root account is locked and administrative
work is delegated to a user account that is entitled to root privileges
(sudo). It is convenient to make the login process as comfortabe as
possible.

A key file for SSH saves the annoying and error-prone typing of the
hopefully secure and sufficiently long password. Additionally, you may
prepare your local desktop to use a short name instead of having to type
in a complete FQN hostname.

a.  On your desktop (Linux or macOS), create a SSH keyfile if not
    already available. It should not be secured by password to enable
    automatic processing.

        […]\&#35; mkdir ~/.ssh
        […]\&#35; cd ~/.ssh
        […]\&#35; ssh-keygen -b 4096 -C \&lt;YOUR_ACCOUNT\&gt;@example.com' -f id_\&lt;outputkeyfile\&gt;

b.  Transfer the key file to your server.

        […]$ ssh-copy-id -i $outputkeyfile.pub \&lt;YOUR_ACCOUNT\&gt;@host.example.com

c.  Create a config file on your desktop with a convenient host name for
    your server.

        […]$ vi ~/.ssh/config
        Host \&lt;MYHOST\&gt;
        Hostname host.example.com
        User \&lt;YOUR_ACCOUNT\&gt;
        ProxyCommand none
        ForwardAgent no
        ForwardX11 no
        Port 22
        KeepAlive yes
        IdentityFile ~/.ssh/$outputkeyfile

d.  Test the configuration

        […]$ ssh \&lt;MYHOST\&gt;

## Check Cockpit access {#_check_cockpit_access}

Open Cockpit in your desktops browser
&#96;[https://host.example.com:9090&#96](https://host.example.com:9090&#96);.
Accept the security warning of your browser. Cockpit uses a self signed
certificate.

If you disabled root access during installation (recommended), login as
root is not possible.

Login with your administrative user account. At the top you will see a
warning that the Web Console is running with limited permissions. Enable
administrator access so that all administrative privileges are
automatically available after login.

## Disable SSH Login with passwords for system users {#_disable_ssh_login_with_passwords_for_system_users}

System users are a systematic weak point in defending a server against
compromise attacks. This is certainly unintentional on the part of the
users. It is due to lack of understanding, insecure passwords, falling
for phishing attacks, and alike. On the other hand, it is precisely the
users that a server is operated for.

Therefore, it is best practice to minimize the number of system users
and instead use virtual accounts or offload applications that require
system users to virtual machines or containers. In case of an intrusion,
this is a kind of second line of defense, trying to keep the server
itself from being infected even then.

In addition, it is a small effort to generally prevent password-based
login and to enforce key files. An exception can be defined for
individual, selected users. If a server is located in a data center and
can only be remotely accessed without much additional effort, it may
make sense to set up a \'fallback user\' if key-based authentication is
no longer available for some reason.

As a side effect it saves a lot of warning messages in the log file and
makes it easier to check them.

a.  On the server, create a configuration file and edit

        […]\&#35; vi /etc/ssh/sshd_config.d/60-local.conf

        \&#35; Local custimization: disable password login except for
        \&#35; one (optionally add some more) user as a fallback option.
        PasswordAuthentication no

        Match User hostmin
        PasswordAuthentication yes
        \&#35;Match User hostmin2
        \&#35;    PasswordAuthentication yes

b.  Reload the sshd daemon

        […]\&#35; systemctl reload sshd

c.  Test that everything works as expected

    &#42; Is an authorised user able to log in? &#42; Are other users
    rejected with the message \'Permission denied
    (publickey,gssapi-keyex,gssapi-with-mic)\'? &#42; If this does not
    work and/or other users are able to log in with a password besides
    your known authorized user, &#42;&#42; install the latest updates.
    &#42;&#42; check the file */etc/ssh/sshd_config.d/50-redhat.conf* to
    make sure that it does not include the line \'PasswordAuthentication
    yes\' (as this is already the default and should not be repeated or
    else it could hinder other configurations).

## Increase security of Cockpit access {#_increase_security_of_cockpit_access}

Cockpit relies on a password based login to its web interface, even for
root (unless the root account is completely locked, locking the account
as part of ssh does not help here). And thus it is a potential target
for brute-force attacks. In most cases, it is rarely used in daily
operations and it may be a good practice to remove the general
accessibility in the firewall. Instead, access Cockpit in one of the
three secure alternatives described below.

There are several ways to improve the security of Cockpit axxess. All of
them are based on permanently withdrawing access to Cockpit in the
firewall. So, reconfigure the firewall permanently.

    […]\&#35; firewall-cmd --permanent --remove-service=cockpit
    […]\&#35; firewall-cmd --reload

Use one of the following alternatives to access Cockpit.

a.  Access Cockpit via ssh tunnel &#42; Login to the server via ssh and
    setup a tunnel in one go

        ssh host.example.com -L 9090:host.example.com:9090

    &#42; While you remain logged in, open in your local browser
    *localhost:9090*

b.  Add Cockpit service temporarily on demand &#42; Login to the server
    and reconfigure firewall

        firewall-cmd –add-service=cockpit

    &#42; When finished remove cockpit again

        firewall-cmd –remove-service=cockpit

c.  Use a secure local proxy

    &#42; Install Cockpit on your local Fedora workstation or on a lab
    server shielded by a firewall. Configure this instance to access any
    of your remote Cockpit instances using Cockpits remote
    administration capability. It uses a protected ssh connection in the
    public network.

    &#42; In the upper left corner of Cockpit you will see the name of
    the logged in user and the desktop rsp. the (local) lab server name,
    along with an expand icon. This opens a box where you can switch to
    another server or add a new one.

    &#42; The &#96;Add new host&#96; link opens a simple form to fill in
    hostname and user. Use your administrative user name on the (remote)
    server. And you can assign a color. Select automatic login via ssh
    keyfile. Cockpit will create one for you if none exists or otherwise
    uses an existing one. For a newly created key, Cockpit installs the
    public key on the remote server, too.

## Optionally: Set up root login via key file {#_optionally_set_up_root_login_via_key_file}

Even if you activated root access during installation, you have
hopefully kept the default option to restrict root to key file
authentification. So you have to set up a key file prior to any ssh
login. But be aware! You can still log in to Cockpit's web interface.
Therefore, in this case, be sure to implement the additional security
measures described in the previous chapter!

### Prepare a pair of private / public keys {#_prepare_a_pair_of_private_public_keys}

This step is to be performed only if a pair of keys does not already
exist. It is best to create the key in the *.ssh* directory of the
desktop user. It should not be secured by password to enable automatic
processing. The naming with leading \'id\_\' und trailing types
abbreviation, e.g. \'\_rsa\' is just a common convention, yet helpful.

a.  Execute on the local desktop

        […]$ mkdir ~/.ssh
        […]$ cd ~/.ssh
        […]$ ssh-keygen -t rsa -b 4096  -C 'root@example.com' -f \&lt;outputkeyfile\&gt;

Although the type rsa is widely used, you may adjust your key type
accordingly.

### Transfer and install the public key onto the server {#_transfer_and_install_the_public_key_onto_the_server}

You normally use *ssh-copy-id* to install the public key on the server.
However, this requires a password login, which was disabled for root
during installation. Therefore, a detour is now required.

a.  Log in to your server via sftp using the unprivileged administration
    account and transfer the public key file

        […]$ sftp hostmin@example.com
        sftp\&gt; put ~/.ssh/\&lt;outputkeyfile\&gt;.pub
        sftp\&gt; quit

b.  Log in to your server via ssh using the unprivileged administration
    account again

        […]$ ssh  hostmin@example.com

c.  On the server acquire root permissions, move the key file and adjust
    permissions

        […]$ sudo su -
        […]\&#35; mkdir /root/.ssh
        […]\&#35; cd  /root/.ssh
        […]\&#35; mv /home/hostmin/\&lt;outputkeyfile\&gt;.pub /root/.ssh/authorized_keys
        […]\&#35; chown  -R  root:root  /root/.ssh
        […]\&#35; chmod 700 /root/.ssh
        […]\&#35; chmod 600 ~/.ssh/\&#42;
        […]\&#35; restorecon  -R  -vF  /root/.ssh

### Test and Simplify Access {#_test_and_simplify_access}

a.  On your local workstation test key file based access:

        […]\&#35; ssh -i ~/.ssh/\&lt;outputkeyfile\&gt;  root@example.com

    adjust file, file type, and domain name as appropriate.

b.  To simplify access create a configuration file on your desktop and
    define a short name for the connection:

        […]\&#35; vi ~/.ssh/config
        \&#35;  \&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;
        \&#35;  my remote server, root account
        \&#35;  \&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;
        Host myhost
        Hostname myhost.example.com
        User root
        ProxyCommand none
        ForwardAgent no
        ForwardX11 no
        Port 22
        KeepAlive yes
        IdentityFile ~/.ssh/\&lt;outputkeyfile\&gt;

    again, replace names accordingly.

c.  Check if everything works:

        […]\&#35; ssh myhost

## Double check hostname and time synchronisation {#_double_check_hostname_and_time_synchronisation}

Both are important for trouble-free server operation. Just in case you
missed its configuration during installation or it is incorrect, now is
the opportunity to fix it.

a.  Check for correct hostname

        […]\&#35; hostnamectl

    &#42; Set hostname if required:

        […]\&#35; hostnamectl  set-hostname  \&lt;YourFQDN\&gt;

b.  Control of time zone, time synchronisation, time

        […]\&#35; timedatectl

    &#42; Correct time zone if necessary:

        […]\&#35; timedatectl set-timezone  \&lt;ZONE\&gt;

    &#42; If necessary, activate time synchronisation:

        timedatectl set-ntp true

    &#42; Correct time if necessary:

        […]\&#35; timedatectl set-time  \&lt;TIME\&gt;

## Consolidate network configuration {#_consolidate_network_configuration}

Depending on installation efforts, network configuration consolidation
may be required.

It sounds trivial, but before any change of the network configuration
make sure that the entries in the DNS are correct. If you change from
DHCP to fixed addresses, you may need to adjust the DNS and vice versa!

a.  Check IP addresses, interface and which protocol stack is used

        […]\&#35; ip a
        1:  lo: \&lt;LOOPBACK,UP,LOWER_UP\&gt; mtu 65536 qdisc n
        \&#8230;
        2:  enp3s0: \&lt;BROADCAST,MULTICAST,UP,LOWER
        \&#8230;

        […]\&#35; nmcli con
        NAME    UUID                                  TYPE      DEVICE
        enp3s0  dabaa33b-25b0-3bfd-8a74-b6b40847a7a4  ethernet  enp3s0

        […]\&#35; who am i
        root     pts/5        2021-04-09 21:07 (2003:ca:7f05:xx00:yyyy:zzzz:479a:b36e)

        […]\&#35; nmcli -p -f ipv4.method,ipv6.method con show 'enp3s0'
        =====================================================================
        Connection details (enp3s0)
        =====================================================================
        ipv4.method:              manual
        ---------------------------------------------------------------------
        ipv6.method:              manual
        ---------------------------------------------------------------------

    Adjust interface names to your custom config

b.  Just in case IPv6 is configured as local only (fe80::&#8230;.) or
    not static, you may set up a fixed IPv6

        […]\&#35; nmcli con mod 'enp3s0' ipv6.method manual \
        ipv6.addresses \&lt;YOUR_IPv6_PREFIX\&gt;::2/64 \
        ipv6.gateway fe80::1 \
        ipv6.dns '2a01:4f8:xx:yy::zzz:8888 2a01:4f8:xx:yy::zzz:9999'
        […]\&#35; nmcli con up 'enp3s0'
        […]\&#35; nmcli con reload

    Again, don't forget to adjust names, prefix, and DNS IP addresses.
    Pay special attention to the gateway. Using a local address of 1
    (fe80::1) is a widely used convention.Another is the IPV6 prefix
    with the address 1. But each provider may have an even different
    approach.

    Check connectivity from your local workstation. If that fails, the
    gateway configuration is the first suspected culprit.

        […]\&#35; ping6 \&lt;YOUR_IPv6_PREFIX\&gt;::2
        […]\&#35; \&#35; e.g. ping6  2a01:xxx:yyy:zzz::2

c.  Optionally reconfigure IPv4 as static. But make sure the IPv6
    address works and don't change both protocol stacks at the same time
    (and in the worst case drop connectivity at all):

        […]\&#35; nmcli con mod 'enp3s0' ipv4.method manual \
        ipv4.addresses \&lt;YOUR_IPv4\&gt;/27 \
        ipv4.gateway \&lt;GATEWAY\&gt; \
        ipv4.dns '\&lt;DNS1_IPv4\&gt; \&lt;DNS2_IPv4\&gt;'
        […]\&#35; nmcli con up'enp3s0'
        […]\&#35; nmcli con reload

    Again, don't forget to adjust names, prefix, and DNS IP addresses
    and check connectivity from your local workstation:

        […]\&#35; ping \&lt;YOUR_IPv4\&gt;

d.  Optionally you may have a look at the NetworkManager configuration
    file

        […]\&#35; less /etc/NetworkManager/system-connections/enp3s0.nmconnection

Finally reboot now to check everything from ground up

## Check LVM storage devices {#_check_lvm_storage_devices}

With Fedora 39 the default LVM configuration has changed. The various
LVM management commands now only process registered, \'legitimate\'
block devices connected to the system. It is essential to check the
correctness of the devices file list.

Listing the registered devices

:   Check the list to see whether all expected devices are included, but
    also whether each device should actually be part of the current
    system.

        […]$ sudo lvmdevices
        Device /dev/sda3 IDTYPE=sys_wwid IDNAME=naa.5000000000000000 DEVNAME=/dev/sda3 PVID=IoUGXYfv74B3YrmCoPfh9ZsWZsDrVKAN PART=3

Adding a device (permanently)

:   This modifies the devices file in /etc/lvm/devices

        […]$ sudo lvmdevices --adddev /dev/\&lt;PART\&gt;

Removing a device (permanently)

:   This modifies the devices file in /etc/lvm/devices

        […]$ sudo lvmdevices --deldev /dev/\&lt;PART\&gt;

## Consolidate storage configuration {#_consolidate_storage_configuration}

Depending on how you decided on data storage during installation,
different supplementary configuration may be required.

a.  If you have chosen the *Default* partitioning and are content with
    the basic principle of creating logical volumes for user and any
    other payload data, there is nothing to do at the moment. The
    creation of these logical volumes happens in the context of the
    installation of the corresponding application software.

    You may ensure that the volume group -- default name
    &#96;fedora&#96; -- fills the complete disk. Using Cockpit, in the
    section &#96;Devices&#96; choose the volume group. At the top of the
    new window it shows its total capacity.

b.  If you have chosen the *Default* partitioning but are *not content*
    with the basic principle of creating Logical volumes for user and
    any other payload data you have now to extend the existing root
    logical volume to accomodate your data. Cockpit provides an easy way
    for this. Choose *Grow*. Determine the new size as needed.

    :::: caution
    ::: title
    :::

    This is not a recommended procedure! Don't complain in case of
    issues.
    ::::

c.  If you have decided for a stricter *separation of system and payload
    data* and created a small Volume Group for system data, you may have
    already created an additional partition and Volume Group in
    Anaconda. Otherwise you have to create it here.

    Select &#96;Storage&#96; in Cockpit's main menu and then your drive
    in the right column. Select &#96;Create new partition&#96; and fill
    in the upcomming form accordingly. In the box \'Devices\' select
    from the Menu \'Create LVM2 volume group\' and fill in the upcomming
    form accordingly.

## Install fail2ban {#_install_fail2ban}

If a general disabling of the password login is not an option, the
installation of fail2ban is worth considering.

The software monitors the log files for authentication errors. In case
of multiple retries from the same IP address, it reconfigures the
firewall on the fly to block the source IP This is to prevent brute
force methods for cracking passwords and bots checking for weak
passwords. However, a system administrator may also lock himself out, if
if they happen to make a mistake. Therefore, you can exclude destinct IP
addresses, e.g. the administrators desktop, from blocking.

a.  Installation of the software and the required Postfix

        […]\&#35; dnf install fail2ban

b.  Create and fill configuration file

        […]\&#35; vi /etc/fail2ban/jail.local
        \&#35; Jail configuration additions for local installation

        \&#35; Adjust the default configuration's default values
        [DEFAULT]
        \&#35; Optional enter an trusted IP never to ban
        \&#35;ignoreip = www.xxx.yyy.zzz/32
        bantime  = 6600
        backend = auto

        \&#35; The main configuration file defines all services but
        \&#35; deactivates them by default. We have to activate those neeeded
        [sshd]
        enabled = true

c.  Activate software

        […]\&#35; systemctl  enable  fail2ban  --now

d.  Control in the log

        […]\&#35; tail -f /var/log/fail2ban.log

## Install and configure Logwatch {#_install_and_configure_logwatch}

The software checks log files for anomalies and compiles a daily report
that can optionally be sent to system administrators via email. It is
something like a minimal defensive effort. More powerful, but much more
involved would be the installation of a monitor software.

a.  Install software

        […]\&#35; dnf install  logwatch

b.  The only configuration required is to enter a real email address for
    root, the recipient of the report. It is added at the end of the
    file.

        […]\&#35; vi /etc/aliases
        \&#8230;
        \&#35; Person who should get root's mail
        \&#35;root:          marc
        root:          real@address.for.root

        […]\&#35; newaliases

## Disable systemd-resolved LLMNR and/or mDNS {#_disable_systemd_resolved_llmnr_andor_mdns}

You may want to disable LLMNR and/or mDNS depending on your environment.
Both protocols are subject to trivial DNS poisoning attacks by a rogue
responder.

    sudo mkdir -p /etc/systemd/resolved.conf.d
    sudo touch /etc/systemd/resolved.conf.d/20-disable-llmnr-mdns.conf
    sudo tee -a /etc/systemd/resolved.conf.d/20-disable-llmnr-mdns.conf \&gt; /dev/null \&lt;\&lt; EOF
    \&#35; see man resolved.conf for details
    [Resolve]
    \&#35; false = disable, true = resolve AND respond, resolve = resolve only
    LLMNR=false
    MulticastDNS=false
    EOF
    sudo systemctl restart systemd-resolved

You can view the status of LLMNR and mDNS with the following command:
&#96;sudo systemd-resolve \--status&#96;

## Manage system updates {#_manage_system_updates}

It is common sense among system administrators,that regular installation
of bug fixes and closing of security vulnerabilities is essential, i.e.
applying updates in a systremtatic way. An important step is to automate
the process as much as it is reasonable.

Fedora includes a tool, dnf-automatic, which supports several modes of
update automation: do not apply, notify admin, apply and notify admin,
apply without notification. In particular, alternatives 2 and 3 are
definitely worth considering. A general principle might be: Alternative
2 is the minimum choice for almost any system, alternative 3 is not at
all suitable for critical systems that must not fail under any
circumstances.

We recommend to install at least alternative 2:

    […]\&#35; dnf install dnf-automatic

    […]\&#35; vi /etc/dnf/automatic.conf
    \&#35;\&#35;emit_via = stdio
    emit_via = email
    \&#35;\&#35;email_from = root@example.com
    email_from = root@host.example.com
    \&#35;\&#35;

    […]\&#35; vi /etc/aliases
    \&#8230;
    \&#35; Person who should get root's mail
    \&#35;root:        marc
    root:         real@address.for.root

    […]\&#35; newaliases
    […]\&#35; systemctl enable --now dnf-automatic-notifyonly.timer

If you want to automatically install, activate the corresponding timer
instead.

    […]\&#35; systemctl enable --now dnf-automatic-install.timer

## Finally update system and install additional software {#_finally_update_system_and_install_additional_software}

Now that secure administrative access is in place, it's time to update
the system and install some useful software. Of course, \'useful
software\' varies depending on the use case or applications that will be
run on Fedora Server. Anyway, a good choice might be vim. With vimdiff
e.g. a comparison of updates of configuration files (&#42;.rpmnew) is
very comfortable and straightforward.

    […]\&#35; dnf install vim-default-editor  --allowerasing
    […]\&#35; dnf update

Add to the software list as needed.

Finally reboot the server.

# Fedora Server Edition Basic Administration Guide {#_fedora_server_edition_basic_administration_guide}

Peter Boy; Jan Kuparinen; Emmanuel Seyman :page-authors: Peter Boy,
Kevin Fenzi, Jan Kuparinen

## What You Find Here {#_what_you_find_here}

General basic system administration is covered in Fedora's overall
System Administrator's Guide. However, there are some Fedora
Server-specific topics that are not included therein.

This section covers topics like name resolution tools, DHCP support,
special network configuration, local disk space management, and similar
topics. Other sections address specific topics such as
[virtualization](virtualization/index.xml) or
[containerization](containerization/index.xml).

*Currently, the compilation and description of administrative tasks is
still under construction. It will be continuously expanded.*

## Administrative Tools {#_administrative_tools}

Fedora Server Edition is designed as a headless device, i.e. without a
graphical user interface. Corresponding packages are not even installed.
Accordingly, only a simple text-based terminal is available on the box
by default, which is somewhat euphemistically called a *Command Line
Interface* (CLI).

Very many servers do not even have a monitor and keyboard permanently
connected. The administrator works over the network from his desktop. In
this case, a graphical tool is also available, *Cockpit*, a lightweight
web-based graphical user interface. It is very powerful and greatly
simplifies administration even for experienced and CLI-savvy (\'hard
core\') administrators.

## System security {#_system_security}

Fedora is very concerned about security. Accordingly, as part of the
installation, the system is already fitted with many security-relevant
configurations. Thus, by default, a firewall is installed and also
activated, which only allows an ssh as well as a cockpit connection. SSH
uses the latest encryption algorithms and blocks outdated, insecure
methods.

There is not much left for the system administrator to do. Measures that
may be required are described together with the corresponding service.

However, the installation process cannot perform all security-related
configurations automatically.The system manager must weigh the pros and
cons and make a decision. Admins should process these items immediately
after the installation. For detailed information see [Post Installation
Tasks](installation/postinstallation-tasks.xml).

# Setting up dnsmasq - a lightweight DHCP and DNS server {#_setting_up_dnsmasq_a_lightweight_dhcp_and_dns_server}

Peter Boy; Emmmanuel Seyman :page-authors: Peter Boy, Kevin Fenzi
:page-aliases: sysadmin-dnsmasq.adoc

> Fedora Server Edition recommends the lightweight dnsmasq program to
> provide DHCP, DDNS and DNS caching service for a server and a small to
> medium-sized local network. It works as a NetworkManager plugin to
> ensure a seamless interlocking of the components. It is the
> preconfigured default configuration and specifically supported.

## Introduction {#_introduction}

A typical usage of dnsmasq is to provide a DHCP service for a private
network. It is optionally supplemented by dynamic DNS, whereby a DHCP
assigned IP address gets a temporary DNS entry with the hostname of the
device. Additionally, it supports static hostnames, too. Another typical
use case is to provide DHCP for a public subdomain, while an official
public DNS server still provides the subdomain's name resolution. Of
course, devices with such an address cannot be found via DNS. They are
primarily used for the initial system installation, for
network-supported booting (PXE), or dynamically assigning machines,
identified by their MAC address, a specific IP address. And sometimes
dnsmasq is used as a caching DNS proxy without any DHCP or DDNS
functionality. But since release 33, Fedora uses systemd-resolved as DNS
client which includes a versatile caching. Thus, dnsmasq is no longer
needed for this use case.

The dnsmasq DHCP and DNS is the default and recommend way to provide
these services in Fedora Server Edition. Each of the components is
optional. A system can use only the DHCP part without DNS, or only DNS
without DHCP, or only DHCP caching, or any combination. Each component
is configured separately. It is preconfigured as a NetworkManager plugin
to ensure a seamless interlocking of the components.

The target is a small to middle-sized subnet. Usually, a server performs
this task as a "side job" so to speak, and the main tasks involve other
services.

A general determination of the upper limit is practically impossible.
But as a rule of thumb, dnsmasq can easily handle 100 or more machines.
Significantly larger networks primarily require better management and
structuring capabilities. The *ISC DHCP Server* would then be a more
suitable choice.

For additional information, see the *Fedora Magazine* article [Using the
NetworkManager's DNSMasq
plugin](https://fedoramagazine.org/using-the-networkmanagers-dnsmasq-plugin/)
(2019).

## Installation {#_installation}

The NetworkManager dnsmasq plugin included by default provides a basic
configuration skeleton, but does not install the dnsmasq package. Thus,
it avoids to uselessly occupy space and to introduce a superfluous and
unused binary in case dnsmasq is not going to be in use on the
particular server.

In case dnsmasq is not already installed

    […]\&#35; dnf install  dnsmasq

:::: important
::: title
:::

Do &#42;not&#42; use systemctl directly on dnsmasq! It is used as a
NetworkManager plugin, therefore NetworkManager starts and manages
dnsmasq and adjusts &#96;resolv.conf&#96; accordingly. It uses its own
set of parameters and ignores the packages\' configuration file
/etc/dnsmasq.conf.

Calling systemctl directly would be ineffective and would rather start
yet another dnsmasq instance, which leads to conflicts.
::::

## Basic configuration {#_basic_configuration}

NetworkManager takes care of the dnsmasq plugin operation. Configuration
files in the &#96;/etc/NetworkManager/dnsmasq.d&#96; directory specify
the custom configuration requirements, preferably one configuration file
per task. The only exception in this example is the file containing the
IP - hostname mapping of for static DNS names,
&#96;/etc/dnsmasq.hosts&#96;.

:::: tip
::: title
:::

NetworkManager reads all files in that directory, independantly of the
file extension. So you can't temporarily deactivate a configuration by
renaming it.
::::

The example here uses 2 interfaces, an external public interface enp1s0
(example.com) and an internal private interface enp2s0 (example.lan).
You may add any number of additional interfaces by adding corresponding
config files as in the examples here.

1.  Activate the dnsmasq NetworkManager plugin

        […]\&#35; vim /etc/NetworkManager/conf.d/00-use-dnsmasq.conf
        \&lt;i\&gt;
        \&#35; /etc/NetworkManager/conf.d/00-use-dnsmasq.conf \&#35;
        \&#35; This enabled the dnsmasq plugin.
        [main]
        dns=dnsmasq
        \&lt;esc\&gt;\&lt;:wq\&gt;

2.  Configuration of the name resolution (DNS) for the private network
    (example.lan)

        […]\&#35; vim /etc/NetworkManager/dnsmasq.d/01-DNS-example-lan.conf
        \&lt;i\&gt;
        \&#35; /etc/NetworkManager/dnsmasq.d/01-DNS-example-lan.conf
        \&#35; This file sets up DNS for the private local net domain example.lan
        local=/example.lan/
        \&#35; file where to find the list of IP - hostname mapping
        addn-hosts=/etc/dnsmasq.hosts

        domain-needed
        bogus-priv

        \&#35; Automatically add \&lt;domain\&gt; to simple names in a hosts-file.
        expand-hosts

        \&#35; interfaces to listen on
        interface=lo
        interface=enp2s0
        \&#35; in case of a bridge don't use the attached server virtual ethernet interface

        \&#35; The below defines a Wildcard DNS Entry.
        \&#35;address=/.localnet/10.10.10.zzz

        \&#35; Upstream public net DNS server (max.three)
        no-poll
        server=134.102.xx.yy
        server=134.102.uu.vv
        server=2001:638:xxx:yyy::zz
        \&lt;esc\&gt;\&lt;:wq\&gt;

3.  Configuration of the DHCP service for the private network
    (example.lan)

        […]\&#35; vim /etc/NetworkManager/dnsmasq.d/02-DHCP-example-lan.conf
        \&#35; etc/NetworkManager/dnsmasq.d/02-DHCP-example-lan.conf
        \&#35; This file sets up DHCP for the private local net domain example.lan

        \&#35; The domain the DHCP part of dnsmasq is responsible for:
        domain=example.lan,10.10.10.0/24,local

        \&#35; interfaces to listen on
        interface=enp2s0

        \&#35; general DHCP stuff (options, see RFC 2132)
        \&#35; 1: subnet masq
        \&#35; 3: default router
        \&#35; 6: DNS server
        \&#35; 12: hostname
        \&#35; 15: DNS domain (unneeded with option 'domain')
        \&#35; 28: broadcast address

        dhcp-authoritative
        dhcp-option=1,255.255.255.0
        dhcp-option=3,10.10.10.10
        dhcp-option=6,10.10.10.1

        \&#35; Assign fixed IP addresses based on MAC address
        \&#35; dhcp-host=00:1a:64:ce:89:4a,NAME01,10.10.10.50,infinite
        \&#35; dhcp-host=52:54:00:42:6a:43,NAME02,10.10.10.51,infinite

        \&#35; Assign dynamically IP addresses to interface to listen on
        \&#35; Range for distributed addresses, tagged \&lt;int\&gt; for further references dhcp-range=tag:enp2s0,10.10.10.150,10.10.10.200,24h

4.  Configuration of the DHCP service for the public network
    (example.com)

        […]\&#35; vim /etc/NetworkManager/dnsmasq.d/03-DHCP-example-com.conf
        \&#35; etc/NetworkManager/dnsmasq.d/03-DHCP-example-com.conf
        \&#35; This file sets up DNCP for the public example.com domain interface

        \&#35; The domain the DHCP part of dnsmasq is responsible for:
        domain=example.com,134.102.xx.yy/27

        \&#35; interfaces to listen on
        interface=enp1s0

        \&#35; general DHCP stuff (options, see RFC 2132)
        \&#35; 1: subnet masq
        \&#35; 3: default router
        \&#35; 6: DNS server
        \&#35; 12: hostname
        \&#35; 15: DNS domain (unneeded with option 'domain')
        \&#35; 28: broadcast address

        \&#35;\&#35;dhcp-authoritative
        \&#35;\&#35; we just send the bare minimum, e.g. no DNS server
        \&#35;\&#35;dhcp-option=1,255.255.255.224
        dhcp-option=tag:enp1s0,option=router,134.102.3.30

        \&#35; Assign fixed IP addresses based on MAC address
        \&#35; dhcp-host=00:1a:64:ce:89:4a,thootes,10.10.10.50,infinite
        \&#35; dhcp-host=52:54:00:42:6a:43,apollon,10.10.10.51,infinite
        \&#35; Assign dynamically IP addresses to interface to listen on
        \&#35; Range for distributed addresses, tagged \&lt;int\&gt; for further references dhcp-range=tag:enp1s0,134.102.3.19,134.102.3.26,1h

    There is no DNS configuration for the external interface following,
    assuming that a official public DNS server is used to resolve all
    public facing interfaces of the domain example.com.

5.  Adjusting the firewall

    Allow ports for DHCP and DNS (53) service on the public interface.

        […]\&#35; firewall-cmd --get-services
        […]\&#35; firewall-cmd --zone=FedoraServer --permanent --add-service=dhcp
        […]\&#35; firewall-cmd --zone=FedoraServer --permanent --add-service=dns
        […]\&#35; firewall-cmd --reload
        […]\&#35; firewall-cmd --list-all

6.  Disabling the systemd-resolved stub resolver

    Inhibit the stub resolver and remove the symlink /etc/resolv.conf so
    that Network Manager will generate a new resolv.conf directing
    queries to dnsmasq. For more info, see the man page for
    \'systemd-resolved\' under the heading \'/ETC/RESOLV.CONF\'.

        […]\&#35; find /etc/resolv.conf -printf '%p -\&gt; %l\n'
        /etc/resolv.conf -\&gt; ../run/systemd/resolve/stub-resolv.conf
        […]\&#35; rm -f /etc/resolv.conf
        […]\&#35; mkdir -p /etc/systemd/resolved.conf.d
        […]\&#35; echo -e '[Resolve]\nDNSStubListener=no' \&gt; /etc/systemd/resolved.conf.d/no-stub-listener.conf

7.  Restart systemd-resolved and restart NetworkManager to start dnsmasq

    The first time we restart systemd-resolved, it will no longer be
    running the stub resolver. The second time, we are reloading the
    configuration to prompt systemd-resolved to re-assess the
    /etc/resolv.conf generated by NetworkManager, but systemd-resolved
    does not support the \'reload\' unit command.

        […]\&#35; systemctl restart systemd-resolved
        […]\&#35; systemctl restart NetworkManager
        […]\&#35; systemctl restart systemd-resolved

    NetworkManager adjusts now the nameserver entries in /etc/resolv.
    They are replaced by 127.0.0.1 and processed via dnsmasq.

8.  Test the installation

    a.  The dnsmasq internal self test

            […]\&#35; dnsmasq --test

    b.  Test DHCP in the public using a machine without IP address

            […]\&#35; ip a   \&#35; no IPv4 address associated with interface
            […]\&#35; dhclient -4 -1 -v eth0
            […]\&#35; ip a  \&#35; expect new IPv4 address associated with interface
            […]\&#35; dhclient -4 -1 -r -v eth0  \&#35; expected: no IPv4 again
            […]\&#35; ip a  \&#35; expect no IPv4 address associated with interface again

    c.  Try on an other server

            […]\&#35; dig app1 @10.10.10.1
            […]\&#35; nslookup app1 10.10.10.1
            […]\&#35; dhclient -v -d -s 10.10.10.1 enp6s0

## Masquerading / NAT {#_masquerading_nat}

If machines in the private network need access to the public network,
add masquerading / NAT to the firewall.

1.  Enabling masquerading for the public zone and for the internal
    (trusted) trusted zone

        […]\&#35; firewall-cmd --zone=FedoraServer --add-masquerade --permanent
        success
        […]\&#35; firewall-cmd --zone=trusted --add-masquerade --permanent
        success
        […]\&#35; firewall-cmd --reload

        […]\&#35; firewall-cmd --zone=FedoraServer --query-masquerade
        yes
        […]\&#35; firewall-cmd --zone=trusted --query-masquerade
        yes

2.  Allowing forwarding from the internal, private network to the
    external interface and further to the public network.

    a.  A commonly used way to accomplish this is to set \'rules\' in
        the firewall configuration. Corresponding tutorials are very
        widespread. And those who are familiar with it may want to
        continue using it.

            […]\&#35; firewall-cmd --get-active-zones
            FedoraServer
            interfaces: enp1s0
            trusted
            interfaces: vbr2s0 enp2s0
            […]\&#35; firewall-cmd --direct --add-rule ipv4 nat POSTROUTING 0 -o enp1s0 -j MASQUERADE
            success
            […]\&#35; firewall-cmd --direct --add-rule ipv4 filter FORWARD 0 -i vbr2s0 -o enp2s0 -j ACCEPT
            success
            […]\&#35; firewall-cmd --direct --add-rule ipv4 filter FORWARD 0 -i enp1s0 -o vbr2s0 -m state --state RELATED,ESTABLISHED -j ACCEPT
            success

    b.  Fedora's firewall daemon, however, offers with release 35 and
        beyond a more elegant option, so-called \'policies\'. These
        abstract typical targets previously configured by rules.

            […]\&#35; firewall-cmd --get-active-zones
            FedoraServer
            interfaces: enp1s0
            trusted
            interfaces: vbr2s0 enp2s0
            […]\&#35; firewall-cmd --permanent --new-policy trustedToExt
            success
            […]\&#35; firewall-cmd --permanent --policy trustedToExt --add-ingress-zone trusted
            success
            […]\&#35; firewall-cmd --permanent --policy trustedToExt --add-egress-zone FedoraServer
            success
            […]\&#35; firewall-cmd --permanent --policy trustedToExt --set-target ACCEPT
            success
            […]\&#35; firewall-cmd --reload
            success

        This method is much clearer, improves maintainability and
        reduces sources of potential errors. The documentation of the
        upstream project provides [more
        information](https://firewalld.org/2020/09/policy-objects-introduction).

## Integrate libvirt's virtual interface {#_integrate_libvirts_virtual_interface}

In case libvirt and virualization including a virtual network for the
virtual machines, libvirt installs and configures its own dnsmasq
instance. In most cases it is just convenient, instead of replacing the
libvirt *default* network to integrate it in NetworkManagers dnsmasq
plugin. Thus, two instances of dnsmasq operate along each other.

To make it work, just add onother configuration file. The example uses
libvirt.lan as the libvirt virtual network domain name. Adjust as
appropriate.

We just add the name resolution (DNS) for the libvirt virtual network
(libvirt.lan), leaving the DHCP functionality untouched.

    […]\&#35; vim /etc/NetworkManager/dnsmasq.d/20-DNS-libvirt-lan.conf
    \&lt;i\&gt;
    \&#35; /etc/NetworkManager/dnsmasq.d/20-DNS-libvirt-lan.conf

    \&#35; This file directs dnsmasq to forward any request to resolve
    \&#35; names under the .libvirt.lan domain to 192.168.122.1, the
    \&#35; local libvirt DNS server default address.
    server=/libvirt.lan/192.168.122.1
    \&lt;esc\&gt;\&lt;:\&gt;\&lt;w\&gt;\&lt;q\&gt;

## Managing static DNS Entries {#_managing_static_dns_entries}

1.  Edit the dnsmasq host file

    The format is the same as /etc/hosts .

        […]\&#35; vim /etc/dnsmasq.hosts

2.  Restart NetworkManager to read the modified file.

        […]\&#35; systemctl restart NetworkManager

3.  Test the modification

        […]\&#35; nslookup {NAME}
        […]\&#35; nslookup {NAME}.example.lan

# Setting Up a Virtual Routing Bridge (brouter) {#_setting_up_a_virtual_routing_bridge_brouter}

Peter Boy; Kevin Fenzi :page-authors: Peter Boy, Kevin Fenzi

> A virtual bridge is a convenient means of providing the virtual
> machines hosted on a server with access to the public network by
> sharing its physical interface. More complex configurations are also
> possible, such as setting up an internal local network of several
> servers via one or more additional physical interfaces. But the basic
> structure of a virtual bridge remains the same.

Basically there a two ways to set up a virtual bridge.

The virtual (plain) bridge

:   Typically, the bridge \'captures\' the physical interface of the
    server and assigns the server as a slave device. To attach Virtual
    Machines, virtual interfaces are added as needed. The bridge
    operates at layer 2 of the OSI model and uses unique MAC addresses
    to determine the recipient of a data packet.

The virtual routing bridge

:   This bridge leaves the host's interface untouched and instead
    creates an independent bridge to which VMs are attached. It uses the
    forwarding capability to forward incoming packets that are not
    destined for the host to the bridge. The destination of data packets
    is determined locally to the bridge based on IP addresses and
    routing tables.

This article deals with the latter variant.

## Prerequisites {#_prerequisites_2}

1.  Fully updated Fedora Server, any version of F33 or newer,
    preferrable F38.

2.  Installed virtualization support according to the [Adding
    Virtualization Support](virtualization/installation.xml) guide.

3.  Completed preparations for installing VMs according to the
    [Provisioning the Server VM
    image](virtualization/vm-install-diskimg-fedoraserver.adoc&#35;_provisioning_the_server_vm_image)
    guide.

4.  Set up DNS entries for the projected VMs

## Steps to configure a basic routing bridge {#_steps_to_configure_a_basic_routing_bridge}

1.  Check the forwarding configuration

        […]\&#35; cat /proc/sys/net/ipv4/ip_forward
        […]\&#35; cat /proc/sys/net/ipv6/conf/default/forwarding

    In both cases a value of 1 must be returned. Libvirt will activate
    IPv4 forwarding, but probably not IPv6. If necessary, activate
    forwarding temporarily

        […]\&#35; echo 1 \&gt; /proc/sys/net/ipv4/ip_forward
        […]\&#35; echo 1 \&gt; /proc/sys/net/ipv6/conf/all/forwarding

    The following file must be set up for permanent setup.

        […]\&#35; vim /etc/sysctl.d/50-enable-forwarding.conf
        \&#35; local customizations
        \&#35;
        \&#35; enable forwarding for dual stack
        net.ipv4.ip_forward=1
        net.ipv6.conf.all.forwarding=1

2.  Checking the existing interfaces

        […]\&#35; ip a
        1: lo: \&lt;LOOPBACK,UP,LOWER_UP\&gt; mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
        …
        2: enp2s0: \&lt;BROADCAST,MULTICAST,UP,LOWER_UP\&gt; …  state UP group default qlen 1000
        inet 148.251.152.29/32 scope global noprefixroute enp2s0
        …
        inet6 2a01:xxx:yyy:zzz::2/64 scope global noprefixroute
        …
        3: virbr0: \&lt;BROADCAST,MULTICAST,UP,LOWER_UP\&gt; …  state UP group default qlen 1000
        …

3.  Adjusting the IPv6 subnet

    As the listing indicates, the external IPv6 subnet is a common full
    /64 network. This must be changed to trigger IPv6 forwarding.

        […]\&#35; nmcli con mod enp2s0 ipv6.addresses '2a01:4f8:210:512d::2/128'
        […]\&#35; nmcli con up  enp2s0

4.  Creating a routing bridge

    The (public) bridge is named vbr1s0, based on the name of the
    accompanying (public) interface.The IP addresses are the same, but
    with a different subnet range to trigger forwarding.

    In the listing of interfaces, the IPv4 address is a point-to-point
    connection. Therefore, the bridge uses a subnet, if any, the range
    that is also assigned in DNS. If the IPv4 interface is also created
    as a subnet, the bridge would be created as a p2p connection
    instead.

        […]\&#35; nmcli con add  con-name vbr1s0  ifname vbr1s0  type bridge  stp off \
        ipv4.method manual  ipv4.addresses '148.251.152.29/27'  \
        ipv6.method manual ipv6.addresses '2a01:4f8:210:512d::2/64' ipv6.addr-gen-mode eui64

    No zone is specified! Thus the bridge is assigned to the default
    zone (FedoraServer), to which the Ethernet interface also belongs by
    default. This is very important for the firewall permissions!

    Finally, for IPv4, the routes must be created and the public
    addresses of all VMs must be listed

        […]\&#35; nmcli con mod vbr2s0 +ipv4.routes '148.251.152.49/32'
        […]\&#35; nmcli con mod vbr2s0 +ipv4.routes '148.251.152.52/32'
        […]\&#35; nmcli con mod vbr2s0 +ipv4.routes '148.251.152.56/32'

5.  Double check your entries, especially the IP addresses, to avoid
    incorrect configuration and time-consuming troubleshooting.

6.  Activate the routing bridge

        […]\&#35; nmcli con up vbr1s0

7.  Installing a VM

    Use Cockpit or the command line

        […]\&#35; cp /var/lib/libvirt/boot/Fedora-Server-KVM-37-custom.qcow2 /var/lib/libvirt/images/vm-01.qcow2
        […]\&#35; virt-install --name vm-01 --memory 4096 --cpu host --vcpus 4 --graphics none \
        --os-variant fedora37 --import  --disk /var/lib/libvirt/images/vm-01.qcow2,format=qcow2,bus=virtio \
        --network bridge=vbr1s0,model=virtio --network bridge=virbr0,model=virtio

    Complete the First Boot Sceen. Leave the network configuration as it
    is. It is easier to configure it after the first login.

8.  Login to the VM and configure the public interface

        […]\&#35; nmcli con mod 'Wired connection 1' ipv4.method manual ipv4.addresses '148.251.152.49/32' \
        ipv4.gateway '148.251.152.29'  ipv4.dns '213.133.98.98' ipv6.method 'manual' \
        ipv6.addresses '2a01:4f8:210:512d::10/64' ipv6.gateway '2a01:4f8:210:512d::2'  connection.id enp1s0
        […]\&#35; nmcli con up  enp1s0

9.  If exist adjust the internal interface.

    ``` bash
    […]\&#35; nmcli con mod 'Wired connection 2'  ipv4.method auto ipv6.method disabled connection.zone 'internal' connection.id enp2s0
    […]\&#35; nmcli con up  enp2s0
    ```

10. Optionally reboot to reinitialize everything

    ``` bash
    […]\&#35; reboot
    ```

### Testing the configuration {#_testing_the_configuration}

1.  Check the forwarding configuration

        […]\&#35; cat /proc/sys/net/ipv4/ip_forward
        […]\&#35; cat /proc/sys/net/ipv6/conf/default/forwarding

    In both cases a value of 1 must be returned.

2.  Check the host configuration SELinux should be in enforcing mode and
    firewalld active with zone FedoraServer with both the external
    interface and the virtual bridge attached.

    ``` bash
    […]\&#35; getenforce
    […]\&#35; firewall-cmd  --list-all
    […]\&#35; firewall-cmd  --get-active-zones
    ```

3.  Check IPv6

\(a\) ping6 external desktop → host (using ipv6 notation) (b) ping6 host
→ VM (c) ping6 external desktop → VM (d) ssh external desktop → VM (e)
traceroute6 external desktop → host (f) traceroute6 external desktop →
VM

1.  Check IPv4

\(a\) ping external desktop → host (using ipv4 notation) (b) ping host →
VM (c) ping external desktop → VM (d) ssh external desktop → VM (e)
traceroute external desktop → host (f) traceroute external desktop → VM

# Setting Up a Point-to-Point Network Connection {#_setting_up_a_point_to_point_network_connection}

Peter Boy :page-authors: Peter Boy

> This configuration is a special case for environments with specific
> security requirements, where the connection of network nodes to each
> other is subject to limitation and control.

## How it works {#_how_it_works}

Typically, a server (or desktop) is directly connected to a local
network and all devices can connect directly to each other. In some
environments, this is exactly what is not desired. Instead, each server
(or desktop) is limited to connect directly only to a network access
device, which can filter, block, or allow the data stream according to a
variety of criteria. Typical use cases are high-security environments or
data centers that offer collocation or dedicated, self-administered
servers. In the latter case, the aim is simply to prevent administrators
from inadvertently \'hijacking\' other customer's IP addresses by typing
errors.

The limiting is handled exclusively in the network connection device
mimicking an ordinary switch, bridge or router, completely uninfluenced
by and independent of the individual servers or desktops. On the
surface, they use a completely normal IP network structure.

In a IPv4 network, a server unaware of the underlying limitation tries
to establish connections as usual and fails at destinations within the
same subnet. Instead, the IPv4 address of the server must be configured
as a /32 address, i.e. a network with only one node. However, the
gateway is then located outside of the own network and must be
configured explicitly in order to be reachable. If the other nodes of
the own subnet do not need to be reachable, a usual network
configuration can be used.

For an IPv6 configuration, it is sufficient to specify the link address
of the gateway.

## Configuration of current Fedora releases {#_configuration_of_current_fedora_releases}

Given an interface enp1s0 with IPv4 address of 192.168.133.100 and the
gateway 192.168.133.1 you may configure the interface

    […]\&#35; nmcli con mod enp1s0 ipv4.method manual ipv4.addresses '192.168.133.100/32' \
    ipv4.gateway '192.168.133.1' ipv4.dns '192.172.1.1'

This will result in a configuration file like

    […]\&#35; less /etc/NetworkManager/system-connections/enp1s0.nmconnection
    [connection]
    id=enp1s0
    uuid=xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    type=ethernet
    interface-name=enp1s0
    timestamp=1671717608

    [ethernet]

    [ipv4]
    address1=192.168.133.100/32,192.168.133.1
    dns=192.172.1.1
    method=manual

    [ipv6]
    addr-gen-mode=eui64
    address1=2a01:4f8:xxx:yyyy::2/64,fe80::1
    dns=2a01:4f8:xxx:yy::zzz:1010;
    method=manual

    [proxy]

An alternative notation for the IPv4 part is

    [ipv4]
    address1=192.168.133.100/32
    method=manual
    route1=0.0.0.0/0,192.168.133.1

In any case you get a

    […]\&#35; ip r
    default via 192.168.133.1 dev enp1s0 proto static metric 100
    192.168.133.1 dev enp1s0 proto static scope link metric 100

## Pre Fedora 35 configuration {#_pre_fedora_35_configuration}

These Fedora releases used *ifcfg-IF_NAME* files in
/etc/sysconfig/network-scripts/. This method dates back to the time
before NetworkManager was introduced and network connections were
managed with a collection of shell scripts. The shell scripts
disappeared with the introduction of NetworkManager, but the
configuration files if cfg-NAME was retained as the default
configuration method in Release 36 for backward compatibility.

Usually, you configure the interface using a text editor, eg given the
above example

    […]\&#35; vim /etc/sysconfig/network-scripts/ifcfg-enp1s0
    DEVICE=enp1s0
    ONBOOT=yes
    BOOTPROTO=none
    IPADDR=192.168.133.100
    PREFIX=32
    SCOPE='peer 192.168.133.1'
    DEFROUTE=yes

    IPV6INIT=yes
    IPV6ADDR=2a01:4f8:xxx:yyyy::2/64
    IPV6_DEFAULTGW=fe80::1
    IPV6_DEFROUTE=yes
    IPV6_DEFAULTDEV=enp1s0

Additionally you need a routing table.

    […]\&#35; vim /etc/sysconfig/network-scripts/route-enp1s0
    ADDRESS0=0.0.0.0
    NETMASK0=0.0.0.0
    GATEWAY0=192.168.133.1

Both variants result again in a

    […]\&#35; ip r
    default via 192.168.133.1 dev enp1s0 proto static metric 100
    192.168.133.1 dev enp1s0 proto static scope link metric 100

## Using systemd-networkd {#_using_systemd_networkd}

Some server administrators might prefer systemd-network over
NetworkManager. Many of the NetworkManager features are very useful for
desktops and laptops, but rather superfluous for servers. The
configuration tool is a plain text editor.

    […]\&#35; vim /etc/systemd/network/10-public.network
    [Match]
    MACAddress=12:34:56:78:9a:bc \&#35; or another identifier

    [Network]
    Gateway=192.168.133.1

    [Address]
    Address=192.168.133.100/32  \&#35;  /32 suffix is optional here
    Peer=192.168.133.1/32       \&#35; Gateway, /32 suffix mandatory here

Configuration of IPv6 is done as usual by specifying the address and the
gateway.

# Virtualization {#_virtualization}

Fredrik Arneving; Peter Boy; Jan Kuparinen :page-authors: Peter Boy,
Kevin Fenzi, Jan Kuparinen

> For more than a decade now, server hardware has been powerful enough
> to run not only one operating system, but many of them simultaneously.
> This inspired software developers to create virtualisation solutions
> for affordable (Intel) server architecture, as was already common on
> mainframes at the time.

Virtualization means that several complete and probably different
operating systems -- the virtual guest machines (guest VM) -- run on one
and the same hardware, even if intended for a different hardware
architecture (full virtualization). In any case, each guest VM uses its
own kernel und operates as far as possible independently and isolated
from each other and the host system. The basis is a \'hypervisor\' that
manages hardware resources and assigns them to the individual operating
systems rsp. virtual guest machines.

Containers are an alternative often discussed. Here, several containers
use the kernel of the host system simultaneously. The mutual isolation
is lower, but the performance overhead is also lower.

## Virtualization options in Fedora {#_virtualization_options_in_fedora}

### XEN {#_xen}

XEN was the first virtualisation technique suitable for inclusion in a
open source distribution as Fedora. This solution first boots a
hypervisor that manages resource access and then subsequently loads the
distribution kernel, which in the case of XEN takes on a special
management function (Dom0). This technology is called \'Type-1\'
hypervisor and is the basis of many commercial virtualisation solutions,
especially in the mainframe world.

Xen initially involved considerable administration and development
effort, as special kernel extensions were necessary. Licensing problems
also contributed to this.

Fedora was an early adoptor of XEN but preferred later KVM as
virtualization solution.

&#42;XEN&#42; is still &#42;natively supported by Fedora Server&#42;

### KVM {#_kvm}

The development of KVM began later, when the issues with kernel
additions were largely settled. It also benefited from being a true open
source project, which made it easier to integrate modules into the
kernel.

Technically, KVM follows a different approach as XEN. It requires an
already installed complete operating system and uses kernel capabilities
that are already part of its standard scope. And there is a tight
cooperation with Qemu, the open source emulation Software (hence the
naming kvm/qemu). It is thus more like a \'Type-2\' hypervisor, whose
typical characterisation is the prerequisite of a complete operating
system. The well-known Virtual Box is an example of a \'Type-2\'
hypervisor.

Fedora was an early adoptor of &#42;&#42;KVM/Qemu&#42;&#42; and it is
&#42;natively supported by Fedora Server&#42;.

### Fedora recommended Virtualization {#_fedora_recommended_virtualization}

Fedora Project decided some time ago to replace XEN as the preferred
virtualization and use KVM as default instead.

Due to the \'Type-2\'-like concept of KVM, Fedora Server Edition is
first installed and configured as usual. System software required for
virtualization is not automatically installed. In a second step,
virtualization capabilities are added (it can be added as an option
during installation to combine both into one step on the surface.
However, a subsequent, precisely fitting installation is very much
preferrable).

## Adding Virtualization Support {#_adding_virtualization_support}

This step includes the [installation of the libvirt software and further
configuration](virtualization/installation.xml) steps. For example,
external connectivity must be set up for virtual machines, e.g. through
a virtual bridge or mac-vlan. Often, an internal network is also
required for protected communication between the virtual machines or
with the host system.

After Fedora Server is enabled for virtualization, one or more virtual
machines can be installed. This might be Fedora Server, or any other
Linux distribution.

## Adding Virtual Machines {#_adding_virtual_machines}

There are two common ways to install virtual machines:

- Use of the *distribution's native installer*, often a bootable iso
  file originally intended for burning to DVD or transferring to a USB
  stick. A utility boots this iso file into an initially temporary
  virtual machine that runs the native installer, permanently setting up
  the virtual machine with the desired system.

- Use of a *virtual disk image* containing a preconfigurated, ready to
  boot operational system, often optimized for virtualization. A special
  case are cloud (base) images.

### Distribution's native installer {#_distributions_native_installer}

With this method, the distribution's own installation procedure of the
targeted distribution is executed in a virtual machine. In the case of
Fedora, this is Anaconda, which most administrators are already familiar
with from the host server installation. The learning curve is therefore
very flat.

In most cases, the installation procedure is *interactive*, as in the
case of Anaconda on Fedora Server installation media. Advantages are the
familiarity of administrators with the tool, the customizability in all
the details that the installation of each distribution offers, and the
perfect replication of all the features and capabilities that are
offered.

The big disadvantage is that this process is very time-consuming. If
several VMs have to be installed or you only need a test instance
\'quickly\', this is not an efficient solution.

As the tool to run the distribution's native installer, Fedora
recommends *Cockpit*, a web-based graphical and comfortable
administration tool. An alternative is Virt-Manager, also a graphical
utility. However, it must be installed on the local workstation (Linux
only) and then works via a ssh connection. Execution on Fedora Server
itself is not supported, as Fedora Server is designed to be
\'headless\', i.e. without a graphical user interface.

Experienced administrators can also initialize an installation via the
command line using VNC and virt-install. However, if you don't have a
routine for this and no stock of configuration snippets to build on,
this is also quite time-consuming and, moreover, then error-prone.

### Virtual disk image {#_virtual_disk_image}

The basic idea is not to always create a virtual disk anew when a new VM
is to be installed. This involves going through the same configuration
steps in Anaconda over and over again and let Anaconda copying the same
rpm packages one by one from the installation media to the virtual disk.
Instead, the administrator resorts to a preconfigured, bootable generic
disk image and \'imports\' it in its entirety unchanged into the virtual
machine as a virtual hard disk on one go.

This import is unproblematic, since the virtualized central hardware
elements of a QEMU/kvm Linux virtual machine of the same architecture
hardly differ. Any remaining differences can be adjusted in the course
of post-installation tasks. In this way, an installation that would
otherwise easily take about a quarter of an hour is reduced to a few
minutes.

#### Fedora Server KVM virtual disk images {#_fedora_server_kvm_virtual_disk_images}

Fedora provides on the Fedora Server download page with \'Fedora Server
39 QEMU\' a VM disk image in the qcow2 format. This format allocates
dynamically only the amount of disk space which it actually required.

This VM resembles a Fedora Server installed on hardware as complete as
possible.

The article [Creating a virtual machine using Fedora Server Edition disk
image](:virtualization/vm-install-diskimg-fedoraserver.xml) describes
the process in detail.

#### Custom virtual disk image repositories and generation tools {#_custom_virtual_disk_image_repositories_and_generation_tools}

There are several offerings available

&#42; &#42;ImageFactory&#42;

\+ This is the tool that Fedora Release Engineering currently uses to
create the various Fedora VM images. You can install the program on your
local hard drive and use it to create your own Fedora VM image. By
default, it uses Fedora rpm packages and the various Fedora VM images
are available in source code, which you can copy and customize to your
specific requirements. This way you get an image that is as close as
possible to the images provided by Fedora.

\+ The article [ImageFactory -- How to Create a Virtual Machine Disk
Image](:tutorials/imagefactory.xml) describes the process in detail.

&#42; &#42;Virtual Builder&#42;

\+ The guestfs-tools, included in the [Adding Virtualization
Support](:virtualization/installation.adoc&#35;_installing_libvirt_virtualization_software)
installation task, include the *virt-builder* tool to create a partly
customized disk image (e.g. root password). You get a disk image file
pretty quickly and importing it into KVM is easy and fast as well.

\+ The tools uses prebuild-images on a third-party server that provides
images for many distributions.

\+ If you specify \'Fedora Server\' as your target, you will not get a
resemblance of Fedora Server virtualized, contrary to the description in
virt-builder. Cockpit is not installed, filesystem is without LVM, many
software packages are missing (vim, tar, sshfs, etc), firewall without
Fedora Server zone - just to name a few. The image is generated on an
external server and imported as a binary.

\+ With all the effort we put into Fedora to build even the smallest rpm
package completely from source on Fedora infrastructure, it seems pretty
absurd to use a complete VM binary from a third party source or to rely
on an external binary image. Therefore, to create a Fedora image this is
probably not a suitable solution.

\+ But you can easily get VM images of other distributions and install
it on a Fedora Server host. However, it remains to be seen how closely
the corresponding distribution system will be replicated.

&#42; &#42;Image Builder Tool&#42;

\+ The tool creates an elaborated image file. But in the current
implementation it requires almost a similar effort as an Anaconda
installation. And as in the case of virt-builder, a binary is imported
from an external source.

\+ The extent to which the VM images created replicate the respective
distribution is similarly questionable as with Virtual Builder.

#### Cloud base images {#_cloud_base_images}

Most distributions provide \'cloud images\'. These are virtual disk
images, each custom built for easy installation in one of the cloud
systems, e.g. Amazon's AWS or Google's GCP. They use cloud system
specific features for configuration and administration provided by the
respective cloud system, e.g. cloud-init for initialization at the first
boot. These are not readily available on an autonomous server.

In addition, most distributions also provide a \'cloud base image\', a
base system built like the specific cloud images, but without the
respective configuration and administrative tools. For example, it
supports the \'no-cloud\' option for cloud-init. These are installable
(i.e. \'imported\') in an autonomous server as a VM.

It is very different to what extent these cloud base images resemble an
autonomous server of the respective distribution. In the case of Fedora,
there is intentionally a fairly low resemblance to Fedora Server
Edition. This path might be considered to be of limited usefulness.

Installation is accomplished on the command line with a single and
simple invocation of the virt-install program. The article [Creating a
virtual machine using a distribution's Cloud base image -- the example
of CentOS](:virtualization/vm-install-cloudimg-centos9.xml) describes
the work to do in detrail for CentOS 9 stream.

# Adding Virtualization Support {#_adding_virtualization_support_2}

Fredrik Arneving; Peter Boy; Jerry James :page-authors: Peter Boy, Kevin
Fenzi, Jan Kuparinen

> Qemu-kvm in combination with Libvirt management toolkit is the
> standard virtualization methodology in Fedora. This optionally
> includes a local virtual network that you may use for protected
> communication between the virtual guest systems and between the guests
> and the host. Its default configuration enables access to the public
> network via NAT, which is useful for virtual machines or containers
> without direct access to the public network interface.

## Preparation {#_preparation}

### Hardware requirements {#_hardware_requirements}

QEMU / KVM require hardware virtualization support. The first thing to
do is to make sure that it is available.

``` bash
[…]\&#35; grep -E --color 'vmx|svm' /proc/cpuinfo
```

The command will return one line per cpu core if virtualization is
enabled. If not, you should first check in the BIOS whether
virtualization is disabled.

### Storage set up {#_storage_set_up}

Libvirt stores its data including the image files of the virtual hard
disk(s) for the guest systems in /var/lib/libvirt. If you adhere to the
default partitioning layout, the libvirt application data is stored in
its own logical volume that you have to create in advance. You need to
specify the size of the storage area, a unique name, and the
accommodating VG (fedora in case of default partitioning). In the new
logical volume, create an xfs file system and mount it at
/var/lib/libvirt.

#### Cockpit {#_cockpit}

The easiest way is to use Cockpit. Start your favorite browser and
navigate to your server, named example.com here.

``` bash
https://example.com:9090
```

If there is no valid public certificate installed so far, a browser
warning appears and you have to accept an exception for the self-signed
certificate. The subsequent login can use either the root account or an
unprivileged administrative user account.

In Cockpit select \'Storage\' in the left navigation column and then the
target volume group in the device list at the top of the right column of
the opening window. The center content area changes to show the selected
volume group at the top and a list of existing logical volumes below it
that may be empty for now.

To create a logical volume select \'Create logical volume\' next to the
\'Logical volumes\' section title. In the form that opens, fill in the
name of the new logical volume at the top, e.g. in this case
\'libvirt\'. Leave the usage field as \'File system\' and adjust the
size at the bottom, e.g. 500 GiB. Then create the LV.

In the \'Logical volumes\' list, a new line appears with the LV name,
libvirt in this example, as part of the device part on the right side.
Expand that line and select \'format\' on the right side. In the form
that opens, fill in the name of the new file system, e.g. in this case
\'libvirt\', and the mount point, /var/lib/libvirt in this case. Leave
the other fields at their default values. Select \'Format\' and Cockpit
will handle everything else.

After completion, the file system is immediately available and is also
permanently configured in the system accordingly.

#### Command line {#_command_line}

Some administrators may prefer the command line for easy scripting.
Create a Logical Volume of appropriate size, 50 GiB in this esample,
either in the system Volume Group (named fedora by default) or in the
user data VG if created during installation. Adjust size and VG name as
required.

    […]\&#35; lvcreate -L 50G -n libvirt  fedora
    […]\&#35; mkfs.xfs /dev/fedora/libvirt
    […]\&#35; mkdir -p /var/lib/libvirt
    […]\&#35; echo 'UUID=$(blkid -s UUID -o value /dev/mapper/fedora-libvirt) /var/lib/libvirt        xfs     defaults        0 0'  \&gt;\&gt; /etc/fstab

## Installing libvirt virtualization software {#_installing_libvirt_virtualization_software}

Installing the software is quite simple.

    […]\&#35; dnf install qemu-kvm-core libvirt virt-install cockpit-machines guestfs-tools

Be sure to install &#96;guestfs-tools&#96;, not
&#96;libguestfs-tools&#96; (unless you need additional windows guest
related software). The package &#96;guestfs-tools&#96; provides a basic
set of various useful tools to maintain virtual disks. Additional
packages provide support for specific use cases, e.g. various file
systems or forensic support. Use &#96;dnf search guestfs&#96; to get a
list of available packages.

Do not install the group &#96;@virtualization&#96; onto a Fedora Server.
It includes various graphical programs and libraries that are not usable
on headless servers.

Next check the SELinux labels

``` bash
[…]\&#35; ls -alZ /var/lib/libvirt
```

Usually, installation sets the SELinux labels properly. Otherwise, set
them manually.

``` bash
[…]\&#35; restorecon -R -vF /var/lib/libvirt
```

If everything is correct, the next step is to activate autostart after
re-boot and start KVM and libvirtd.

With Fedora 35 libvirt switched to a *modular archtecture* (since
version 7.6.0-3) while used a single monolithic libvirt daemon up to
Fedora 34 (version 7.0.0-x). The installation procedure is the same
because the packaging system takes care of the differences. But
activation and start up differs as well as installation and
configuration of an internal protected virtual network between VMs and
the host.

### Activation and startup with Fedora 34 {#_activation_and_startup_with_fedora_34}

Enable automatic startup at boot and start libvirt.

``` bash
[…]\&#35; systemctl enable libvirtd  --now
```

By default, libvirt creates a (virtual) bridge with an interface virbr0,
the IP 192.168.122.1 and the libvirt-internal name as default. In
addition, a separate firewall zone libvirt is set up and assigned to the
internal interface. Check if everything is running as expected.

``` bash
[…]\&#35; ip a
[…]\&#35; firewall-cmd --get-active-zones
```

### Activation and startup with Fedora 35 and up {#_activation_and_startup_with_fedora_35_and_up}

The libvirt Fedora installation procedure provides systemd startup
scripts that take care of enabling and starting the various unix sockets
and services as needed. This includes support for qemu, xen and lxc.
Configuration of vbox is disabled by default. The drivers determine
during startup whether the required prerequisites are met and abort
otherwise. The default services, qemu and lxc in case of Fedora Server,
are started at boot time. If not used for about one minute they are
deactivated, but will restart on demand as soon as a virtual machine is
started (either by command line or Cockpit service). There is no need
for administrator intervention at all.

The network configuration is slightly different. The services don't
start at boot time, like qemu, lxc, etc., but on demand at first access.
Therefore, you won't get an interface virbr0 until some libvirt service
requests it. That's sometimes inconvenient, e.g. if you use that
interface for non-libvirt services, too (e.g. lxd or nspawn container).
You may prefer to enable the virt-network service anyway:

1.  &#42;Optionally, activate libvirt's internal network&#42;

    if you are planning to use the virtual network independently from
    starting virtual machines or you need the virbr0 interface at boot
    time anyway, enable libvirt's internal network. Otherwise you may
    skip this step.

    ``` bash
    […]\&#35; systemctl enable virtnetworkd.service --now
    ```

    Alternatively, you may want to completely discard libvirt's internal
    network. You'll take this path if you set up an internal network
    with NetworkManager tools.

    ``` bash
    […]\&#35; systemctl disable virtnetworkd.socket  --now
    ```

2.  &#42;&#42;Activate (start) the required libvirt modular
    drivers&#42;&#42;

        […]\&#35; for drv in qemu interface network nodedev nwfilter secret storage ; \
        do systemctl start virt${drv}d{,-ro,-admin}.socket ;  done

    The virtualization functionality can be used immediately. An
    interface virbr0 as well as a dnsmasq server is now available,
    regardless of when and if a libvirt service is started. The
    virtnetwork service will terminate if no libvirt service starts up
    within the first 1-2 minutes (and later restart automatically if
    needed). But the interface and the dnsmasq server remain regardless.

    The virtualization services virtqemud.service, etc will be dormant
    it no VM has been started as well. But the socket is active and will
    start the corresponding service on demand.

    The boot process now starts virtualization automatically without
    administrative intervention.

3.  &#42;Check successful start via a status query&#42;

        […]\&#35;  for drv in qemu interface network nodedev nwfilter secret storage ; \
        do systemctl status virt${drv}d{,-ro,-admin}.socket ;  done
        ● virtqemud.socket - libvirt QEMU daemon socket
        Loaded: loaded (/usr/lib/systemd/system/virtqemud.socket; enabled; preset: enabled)
        Active: active (listening) since Wed 2024-04-\&#8230;
        Triggers: ● virtqemud.service
        Listen: /run/libvirt/virtqemud-sock (Stream)
        CGroup: /system.slice/virtqemud.socket

        Apr 10 13:51:33 example.com systemd[1]: Listening on virtqemud.socket - libvirt QEMU daemon socket.

        ● virtqemud-ro.socket - libvirt QEMU daemon read-only socket
        Loaded: loaded (/usr/lib/systemd/system/virtqemud-ro.socket; enabled; preset: enabled)
        Active: active (listening) since Wed 2024-04-\&#8230;
        Triggers: ● virtqemud.service
        Listen: /run/libvirt/virtqemud-sock-ro (Stream)
        CGroup: /system.slice/virtqemud-ro.socket

        Apr 10 13:51:33 example.com systemd[1]: Listening on virtqemud-ro.socket - libvirt QEMU daemon read-only socket.

        ● virtqemud-admin.socket - libvirt QEMU daemon admin socket
        Loaded: loaded (/usr/lib/systemd/system/virtqemud-admin.socket; enabled; preset: enabled)
        Active: active (listening) since Wed \&#8230;
        Triggers: ● virtqemud.service
        Listen: /run/libvirt/virtqemud-admin-sock (Stream)
        lines 1-23 \&#8230;
        \&#8230;

## Adjusting libvirt internal network configuration {#_adjusting_libvirt_internal_network_configuration}

The default configuration of the internal network (virbr0) activates
just a DHCP Server. If the virtual machines should also be able to
communicate with each other and the host, then adding a DNS server is at
least very advantageous. It is easier and less error-prone to address
VMs and the host by name instead of IP numbers.

The first step is to choose a domain name. A top-level \'.local\' is
explicitly not recommended, nor taking one of the official top-level
names. But for example, you can take the official domain name and
replace the last, top-level part with \'lan\' or \'internal\' or
&#96;localnet&#96;. An official domain example.com would translate to an
internal domain example.lan. We use that one throughout this tutorial.
The host gets the internal name host.example.lan.

Use the libvirt tool to adjust the default network. Replace names and
placeholders as required. Delete the line with \'forward mode =
\'nat\'\' if you do not want to allow access to the public network via
the virtual network.

``` xml
[…]\&#35; virsh  net-edit  default
\&lt;network\&gt;
\&lt;name\&gt;default\&lt;/name\&gt;
\&lt;uuid\&gt;aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee\&lt;/uuid\&gt;
\&lt;bridge name='virbr0' stp='on' delay='0'/\&gt;
\&lt;mac address='52:54:00:xx:yy:zz'/\&gt;
\&lt;forward mode='nat'/\&gt;
\&lt;mtu size='8000'/\&gt;
\&lt;domain name='example.lan' localOnly='yes'/\&gt;
\&lt;dns forwardPlainNames='no'\&gt;
\&lt;forwarder domain='example.lan' /\&gt;
\&lt;host ip='192.168.122.1'\&gt;
\&lt;hostname\&gt;host\&lt;/hostname\&gt;
\&lt;hostname\&gt;host.example.lan\&lt;/hostname\&gt;
\&lt;/host\&gt;
\&lt;/dns\&gt;
\&lt;ip address='192.168.122.1' netmask='255.255.255.0'\&gt;
\&lt;dhcp\&gt;
\&lt;range start='192.168.122.2' end='192.168.122.254'/\&gt;
\&lt;/dhcp\&gt;
\&lt;/ip\&gt;
\&lt;/network\&gt;
```

Activate the modified configuration.

``` bash
[…]\&#35; virsh net-destroy default
[…]\&#35; virsh net-start default
```

Check if the DNS resolution works.

``` bash
[…]\&#35; nslookup host  192.168.122.1
[…]\&#35; dig  @192.168.122.1  host.example.com
```

## Adjusting the hosts DNS resolution configuration {#_adjusting_the_hosts_dns_resolution_configuration}

In order for the host to initiate communication with its virtual
machines, it must query the name server set up in the previous step for
internal domains. So we need Split DNS. The default systemd-resolved DNS
client in Fedora is basically split-DNS capable. Unfortunately it
currently doesn't cooperate well with libvirt's virtual network and
needs additional administrative efforts.. and its usage is quite
unstable. Therefore we recommend switching to dnsmasq for the time being
to provide stable split DNS.

:::: warning
::: title
:::

The following procedure doesn't work for Fedora 35-39. Don't use it with
these releases. Switch to dnsmasq for the time being as described in the
next chapter instead.
::::

1.  The name resolver service *systemd-resolved* introduced with Fedora
    33 can do this automatically. But libvirt handles its interfaces on
    its own and must therefore inform systemd-resolved about it. A
    script in a hook provided by libvirt can take care of this. You have
    to adjust the local domain name (\${example.lan} in the script
    below) accordingly!

        […]\&#35; mkdir -p /etc/libvirt/hooks/network.d/
        […]\&#35; vim /etc/libvirt/hooks/network.d/40-config-resolved.sh
        \&#35;\&gt;--INSERT--\&lt;\&#35;
        \&#35;!/bin/bash
        \&#35; Add the internal libvirt interface virbr0 to the
        \&#35; systemd-resolved configuration.
        \&#35; Its automatic configuration of systemd-resolved cannot
        \&#35; (yet) detect a libvirt DNS server.

        network='$1'
        operation='$2'
        suboperation='$3'

        \&#35; $1 : network name, eg. default
        \&#35; $2 : one of 'start' | 'started' | 'port-created'
        \&#35; $3 : always 'begin'
        \&#35; see  https://libvirt.org/hooks.html

        ctstartlog='/var/log/resolve-fix.log'

        echo ' P1: $1 - P2: $2 - P3: $3   @  $(date)  '
        echo '                                        '  \&gt;  $ctstartlog
        echo '======================================= '  \&gt;\&gt;  $ctstartlog
        echo ' P1: $1 - P2: $2 - P3: $3   @  $(date)  '  \&gt;\&gt; $ctstartlog

        if [ '$network' == 'default' ]; then
        if [ '$operation' == 'started' ] \&amp;\&amp; [ '$suboperation' == 'begin' ]; then

        echo ' Start fixing \&#8230;.      '  \&gt;\&gt; $ctstartlog
        resolvectl dns virbr0 192.168.122.1
        resolvectl default-route virbr0 false
        resolvectl domain virbr0 example.lan
        resolvectl domain virbr0 example.lan
        echo '              \&#8230;. done '  \&gt;\&gt; $ctstartlog
        echo ' Checking \&#8230;.          '  \&gt;\&gt; $ctstartlog
        echo ' Executing resolvectl   '  \&gt;\&gt; $ctstartlog
        resolvectl status                \&gt;\&gt; $ctstartlog
        echo '                        '  \&gt;\&gt; $ctstartlog
        echo ' Executing cat resolve  '  \&gt;\&gt; $ctstartlog
        cat  /etc/resolv.conf            \&gt;\&gt; $ctstartlog
        echo '              \&#8230;. done '  \&gt;\&gt; $ctstartlog

        fi
        fi
        \&#35;\&gt;--SAVE\&amp;QUIT--\&lt;\&#35;

        […]\&#35; chmod +x /etc/libvirt/hooks/network.d/40-config-resolved.sh

2.  Check if /etc/resolv.conf is a link and not a file. Activate
    modified local DNS resolving

    ``` bash
    […]\&#35; ls -al /etc/resolv.conf
    ```

    In case it is a file, fix it:

    ``` bash
    […]\&#35; cd /etc
    […]\&#35; rm -f resolv.con
    […]\&#35; systemctl  restart  systemd-resolved
    […]\&#35; ln -s ../run/systemd/resolve/stub-resolv.conf  resolv.conf
    ```

3.  Test the hook file

    ``` bash
    […]\&#35; /etc/libvirt/hooks/network.d/40-config-resolved.sh  default started begin
    P1: default - P2: started - P3: begin   @  Mon Mar \&#8230;
    ```

4.  It is useful to modify the host's search path to resolve a short
    single hostname to the internal network.

    ``` bash
    […]\&#35; /etc/libvirt/hooks/network.d/40-config-resolved.sh  default started begin
    P1: default - P2: started - P3: begin   @  Mon Mar \&#8230;
    ```

5.  Check the functionality of name resolution with internal and
    external addresses.

<!-- -->

    […]\&#35; ping host
    […]\&#35; ping host.example.lan
    […]\&#35; ping host.example.com
    […]\&#35; ping guardian.co.uk

\+ Everything should work fine now.

## Switch to NetworkManager's dnsmasq plugin {#_switch_to_networkmanagers_dnsmasq_plugin}

The NetworkManager Dnsmasq plugin is an easy way to add a local caching
DNS server which is split DNS enabled. It provides the host with a
lightweight, capable DNS server as an alternative to using
systemd-resolve. By default it forwards all queries to an external,
\'official\' DNS server. We just have to configure the local libvirt
domain.

Activate dnsmasq plugin

``` bash
[…]\&#35; vim /etc/NetworkManager/conf.d/00-use-dnsmasq.conf
\&#35; /etc/NetworkManager/conf.d/00-use-dnsmasq.conf
\&#35;
\&#35; This enabled the dnsmasq plugin.
[main]
dns=dnsmasq
```

Define the local domain and DNS service

``` bash
[…]\&#35; vim /etc/NetworkManager/dnsmasq.d/00-example-lan.conf
\&#35; /etc/NetworkManager/dnsmasq.d/00-example-lan.conf
\&#35;
\&#35; This file directs dnsmasq to forward any request to resolve
\&#35; names under the .example.lan domain to 192.168.122.1, the
\&#35; local libvirt DNS server.
server=/example.lan/192.168.122.1
```

Activate modified local DNS resolving

``` bash
[…]\&#35; systemctl  stop  systemd-resolved
[…]\&#35; systemctl  disable  systemd-resolved
[…]\&#35; rm /etc/resolv.conf
[…]\&#35; nmcli con mod enp3s0 ipv4.dns-search 'example.lan'
[…]\&#35; nmcli con mod enp3s0 ipv6.dns-search 'example.lan'
[…]\&#35; systemctl  restart  NetworkManager
```

Check the functionality of name resolution with internal and external
addresses.

``` bash
[…]\&#35; ping host
[…]\&#35; ping host.example.lan
[…]\&#35; ping host.example.com
[…]\&#35; ping guardian.co.uk
```

## Finishing Cockpit-machines configuration {#_finishing_cockpit_machines_configuration}

Open your browser and connect to the Cockpit instance of your host
server. Consult the [post-installation
guide](installation/postinstallation-tasks.xml) to learn about the
possible connection paths. Log in as root or with your administrative
account. In the overview (start) page select &#96;*Virtual
Machines*&#96; in the left navigation column.

If there is no entry &#96;*Virtual Machines*&#96; in the navigation
column, the cockpit-machines module was left off in the installation
step above. Select &#96;*Applications*&#96; further down and then
&#96;*Machines*&#96; for installation.

:::: tip
::: title
:::

Currently, it sometimes takes a long time to display additional
installation options. You may install the module with
&#96;\[&#8230;\]&#35; dnf install cockpit-machines&#96; instead.
::::

![Cockpit Virtual Machines Page first
used](virtualization/vm-install-cockpit-010.png)

### Storage pools {#_storage_pools}

When first used, the list of virtual machines displayed in the center of
the page is empty, of course. A box left above that list displays 0
Storage pools. Libvirt uses pools to determine the location of typical
files. The installer has already created the directories. Only the pools
need to be defined here.

Typically you use one Pool for installation media, stored at
/var/lib/libvirt/boot. \'Installation media\' would be a suitable
descriptive pool name. Select 0 Storage pools in the box and then Create
storage pool. A new form opens.

If you are logged in as an adminstrative user (even if having used sudo
su - ), you are asked to select a connection type, \'system\' or
\'session\'. This selection is presented in various configuration forms,
so we explain here. Use \'system\' for production deployments, the
common case. Select \'session\' in the special case of testing,
development, and experimentation. The \'session\' option does not
support any custom or advanced networking, but works pretty much
everwhere (including containers) and without any privileges. The libvirt
project provides additional information for developers. If you are
logged in directly as root, this line doesn't show up. Instead,
everything is treated as system; i.e. production deployment (never do
development or experimentation as root).

Next enter \'Installation media\' as the name, \'Filesystem directory\'
as the type, and /var/lib/libvirt/boot as the target path.

In most cases, the (virtual) hard disk used for a virtual machine is a
disk image file stored in /var/lib/libvirt/images. Define another pool
named \'Disk images\' accordingly.

Activate both pools in the drop down menu of each pool.

You may create additional pools as needed, e.g. disk images via iSCSI in
a SAN or as a logical volume in a volume group (LVM) on the host's local
disk. The latter offers better performance in theory, but the practical
gain is usually rather small, if any. We will not go into further detail
here for the time being.

### Networks {#_networks}

A box on the right above the virtual machines list shows &#96;*1
Network*&#96; and lists the networks managed by libvirt. By default, it
contains the internal network *default* with the interface *virbr0*. The
list does not contain the external interface. It is managed by the
server. Nevertheless, it is available for virtual machines.

## Completed {#_completed}

Virtualization is now ready to use on the server and you can start
setting up guest VMs.

This guide just describes the Fedora specific way to use libvirt. For
further information please use the [libvirt project
documentation](https://libvirt.org/docs.html).

# Creating a virtual machine using Fedora Server Edition disk image {#_creating_a_virtual_machine_using_fedora_server_edition_disk_image}

Peter Boy :page-authors: Peter Boy :page-aliases:
pages/virtualization-vm-install-diskimg-fedoraserver.adoc

> Installation of Fedora Server Edition in a virtual machine is a
> supported way for a long time by using the standard installation
> program in a Virtual Machine. Another option is to download a prebuild
> Fedora Server Edition virtual disk image and mount that in a virtual
> machine. The former can be quite flexibly adapted to a specific,
> individual requirement. The latter entails a default installation, but
> requires much less time and effort. It is the scope of this guidance.

There are 2 ways to create a Fedora Server in a virtual machine. System
administrators can use the standard installation program as described in
[Installing a Fedora Server virtual machine using
Cockpit](virtualization/vm-install-fedoraserver-cockpit.xml). In this
process, a number of properties and functionalities can be adapted to
local requirements. Or they can download a Fedora Server virtual disk
image containing an already preinstalled, pre-configured and
ready-to-run operating system and mount it in a virtual machine.

There exist a multitude of virtual disk images that claim to provide a
server based on the Fedora distribution. An example of this is the
[virt-builder](virtualization/vm-install-diskimg-virtbuilder.xml)
system. However, it is not a Fedora Server, but its own, deviating
concept for the configuration of a server. And accordingly, e.g., the
Fedora Server administration tools and principles may not fit. System
administrators can also create their own disk images using tools such as
*[Image Factory](:tutorials/imagefactory.xml)* or *Image Builder*.

## What you get {#_what_you_get}

To begin with, you gain time. Instantiating a virtual disk image takes
only a few minutes, as opposed to running through the standard
installation routines. The workload is significantly lower and
correspondingly faster.

Fedora Server KVM image resembles all features and properties of a
Fedora Server as close as possible, except for directly hardware-related
measures, of course. In general, the system administrator of a virtual
server (guest system) can perform configuration and administration
largely independently and autonomously from the system administrator of
the host system. Ideally, they should not notice any difference in
everyday practice. As the system administrator of the host is limited by
the available hardware resources, the administrator of the guest system
is just limited only by the virtual hardware resources.

Unlike a cloud image, Fedora Server VM is designed to run like any
self-sustaining server, albeit optimized for a generic hypervisor (here
QEMU/KVM/libvirt) rather than bare-metal hardware.

*Fedora Cloud Image* and *Fedora Server Image* have in common that they
adhere to the build process and control of the distribution.

## How it works {#_how_it_works_2}

The creation of a virtual machine image involves two steps.

1.  &#42;Provisioning the server VM image&#42;

    Basically you will download the distributed image file and keep it
    available for creating one or mostly several virtual servers. The
    appropriate location for this is &#96;/var/lib/libvirt/boot&#96;.

2.  &#42;Instantiation of a Server virtual machine&#42;

    To do this, first create a copy of the distribution image in the
    pool of disk images (&#96;/var/lib/libvirt/images&#96;) with the
    name of the VM to be instantiated. This image is then imported into
    Libvirt using one of the following methods.

    a.  *Import via CLI using minimal integrated initial configuration*

    b.  *Import via Cockpit with comfortable minimal initial
        configuration*

        Each of these alternatives then follows a more detailed,
        mission-specific follow-up customization.

Overall, the process is very straightforward and efficient.

## Provisioning the Server VM image {#_provisioning_the_server_vm_image}

We assume a complete installation of virtualization support according to
the [Adding Virtualization Support](virtualization/installation.xml)
guide.

1.  If not already done, &#42;download the Fedora Server Edition&#42;
    virtual disk image into the *Installation media* storage pool and
    verify the image. This involves the following steps.

        […]$ sudo -i
        […]\&#35; cd /var/lib/libvirt/boot
        […]\&#35; wget https://download.fedoraproject.org/pub/fedora/linux/releases/41/Server/x86_64/images/Fedora-Server-KVM-41-1.4.x86_64.qcow2
        […]\&#35; wget https://download.fedoraproject.org/pub/fedora/linux/releases/41/Server/x86_64/images/Fedora-Server-41-1.4-x86_64-CHECKSUM
        […]\&#35; curl -O https://fedoraproject.org/fedora.gpg
        […]\&#35; gpgv --keyring ./fedora.gpg Fedora-Server-41-1.4-x86_64-CHECKSUM
        […]\&#35; sh -c ' cd /var/lib/libvirt/boot/  \&amp;\&amp;  sha256sum --ignore-missing -c \&#42;-CHECKSUM '
        Fedora-Server-KVM-41-1.4.x86_64.qcow2: OK

    If you copy or move files directly from elsewhere, you should check
    the correct SELinux label and correct it if necessary.

        […]\&#35; ls -alZ /var/lib/libvirt/boot/\&#42;
        […]\&#35; restorecon -R -vF /var/lib/libvirt/boot/\&#42;

2.  &#42;Adjust the image file&#42; to your needs. The maximum disk size
    of the server VM image file is 7GB, of which about 6GB in the root
    file system is free. This is not intended for pro­ductive operation,
    but as a starting point for customization. The minimal recommended
    size is about 20G. To save these adjustment steps for further
    instantiations, create a customized base image. Copy the disk image
    to an intermediate file and adjust the maximum disk size.

        […]\&#35; cd /var/lib/libvirt/boot
        […]\&#35; cp Fedora-Server-KVM-41-1.4.x86_64.qcow2  Fedora-Server-KVM-41-custom.qcow2
        […]\&#35; qemu-img info   /var/lib/libvirt/boot/Fedora-Server-KVM-41-custom.qcow2
        […]\&#35; qemu-img resize /var/lib/libvirt/boot/Fedora-Server-KVM-41-custom.qcow2 40G
        […]\&#35; qemu-img info   /var/lib/libvirt/boot/Fedora-Server-KVM-41-custom.qcow2

    The example above expands the maximal capacity to 40 GiB. You can
    resize the virtual disk later, too. Therefore, there is no reason to
    plan too generously in terms of size now. Due to the qcow2 format
    resizing does not affect the current image file size. It is
    dynamically adjusted as needed up to the maximum specified.

    If you intend to create multiple VMs with similar structure, it may
    be useful to customize the customised file in detail. See section
    *Import via CLI and elaborated initial configuration* further down.

## Instantiation of a Server virtual machine {#_instantiation_of_a_server_virtual_machine}

### Alternative 1: Import efficiently via CLI {#_alternative_1_import_efficiently_via_cli}

Copy the customized distribution file into the disk image pool and use
virt-install to instantiate the new virtual machine. In the example, we
assume that the VM has 2 interfaces, one for connecting to the public
network and another for connecting to the internal protected network.

    […]\&#35; cp /var/lib/libvirt/boot/Fedora-Server-KVM-41-custom.qcow2  /var/lib/libvirt/images/{VM_NAME}.qcow2
    […]\&#35; virt-install  --name \&lt;VM_NAME\&gt; \
    --memory 4096  --cpu host --vcpus 2 --graphics none \
    --os-variant fedora41 \
    --import  \
    --disk /var/lib/libvirt/images/\&lt;VM_NAME\&gt;.qcow2,format=qcow2,bus=virtio \
    --network type=direct,source=enp1s0,source_mode=bridge,model=virtio \
    --network bridge=virbr0,model=virtio

:::: important
::: title
:::

If a message \'Unknown OS name \'fedora41\'\' appears, the list has not
yet been updated in virt-install. You can then use \'fedora-unknown\'
without any problems.
::::

The parameters are quite descriptive and are to be adjusted accordingly.
You will find a more detailed explanation in the appendix.

A lot of messages then scroll across the screen. If the network
interface doesn't provide DHCP, in includes a NetworkManager error
message. You can safely ignore it for now. It finally ends with a
simple, text-based input mask for the first boot configuration.

    Starting install\&#8230;
    Running text console command: virsh --connect qemu:///system console vm1-test
    Connected to domain 'vm1-test'
    Escape character is ^] (Ctrl + ])
    \&#8230;
    [  OK  ] Reached target User and Group Name Lookups.
    Starting User Login Management\&#8230;
    [  OK  ] Started NTP client/server.
    [   21.523663] NET: Registered PF_QIPCRTR protocol family
    ================================================================================
    ================================================================================

    1) [x] Language settings                 2) [x] Time settings
    (English (United States))                (Etc/UTC timezone)
    3) [x] Network configuration             4) [x] Root password
    (Connected: enp2s0, enp1s0)              (Root account is disabled)
    5) [ ] User creation
    (No user will be created)

    Please make a selection from the above ['c' to continue, 'q' to quit, 'r' to
    refresh]:

Specifically, with networks without DHCP you may get a *\[FAILED\]
Failed to start NetworkMan...\[0m - Network Manager Wait Online.* which
you safely can ignore for now.

We continue with this form in the step after describing the Cockpit way
of instantiation.

### Alternative 2: Import comfortably via Cockpit {#_alternative_2_import_comfortably_via_cockpit}

1.  Open Cockpit on your *host system*. The import expects the virtual
    hard disk at the final location. Therefore, copy the prepared
    customized disk image into the disk image pool, as you did in
    alternative 1 (CLI import). Select *Terminal* in the left navigation
    column to perform this step.

    ![Cockpit initial
    terminal](virtualization/diskimg-fedoraserver-01.png)

2.  Select \'*Virtual Machines*\' in the left navigation column and
    select \'*Import VM*\' at the right top of the central window area.

    ![Cockpit import screen](virtualization/diskimg-fedoraserver-02.png)

    Fill in the input fields as appropriate and leave \'*Connection*\'
    on \'*System*\' as preselected.

3.  If the VM to be created should only have one network interface
    connected to the internal libvirt bridge (virbr0), select *Import
    and run*. In *all other cases*, select *Import and edit* to set up
    the correct network connection before the first boot.

4.  Adjust the network connection setup. The screen changes and the VM
    overview page. Scroll down to *Network interfaces*. You see one
    Interface with Source default, i.e. virbr0. In order to easily
    manage the default route, this interface - the first one created -
    should connect to the public external network. Select *Edit* to
    modify the Source.

    ![Network
    re-configuration](virtualization/diskimg-fedoraserver-03.png)

    Modify Interface type to Direct attachment and Source to the
    physical host external interface. Leave Model and MAC address
    unchanged! Save brings you back to the Overview screen.

5.  In the row \'Network interfaces\' select Add network interface on
    the right side.

    ![Add network interface](virtualization/diskimg-fedoraserver-04.png)

    In the window that opens, the internal virtual network is already
    selected and correctly configured. Select Add to add the interface.

6.  Scroll up and select *Run* In the console window you will see the
    creation and startup of the virtual machine. Expand the console
    window.

    ![Final User
    Configuration](virtualization/diskimg-fedoraserver-05.png)

    Finally, the screen displays the same configuration menu as with a
    CLI setup. Continue with the minimal initial configuration.

### Minimal initial configuration {#_minimal_initial_configuration}

You have to use the terminal for this step, whether you performed the
instantiation via CLI or via Cockpit.

1.  &#42;Complete the first boot configuration&#42;

        ================================================================================
        ================================================================================

        1) [x] Language settings                 2) [x] Time settings
        (English (United States))                (Etc/UTC timezone)
        3) [x] Network configuration             4) [x] Root password
        (Connected: enp2s0, enp1s0)              (Root account is disabled)
        5) [ ] User creation
        (No user will be created)

        Please make a selection from the above ['c' to continue, 'q' to quit, 'r' to
        refresh]:

    The clear majority of the input options are already preset with
    values that correspond exactly to a default installation using the
    Anaconda Fedora Server Edition installation program. The ROOT
    account is locked, as is common security practice. The only
    mandatory remaining task is the creation of a user account granted
    with administrator privileges.

    The selection of a menu item to be edited is made via the digit in
    front of it. Somewhat unusual in these days and age. The process is
    unfortunately a bit cumbersome. A \'5\' navigates to the item \'User
    creation\' and a \'1\' then to the creation of a new user.

        ================================================================================
        ================================================================================

        User creation

        1) [x] Create user
        2) Full name
        3) User name
        4) [x] Use password
        5) Password
        6) [x] Administrator
        7) Groups
        wheel

        Please make a selection from the above ['c' to continue, 'h' to help, 'q' to
        quit, 'r' to refresh]:

    The \'\[x\]\' in front of Create user indicates that the user
    creation process is activ. Accordingly, password authentication is
    enabled for the new user as well as administrator privileges. Fill
    in the required information and in any case ensure to activate the
    adminstrator privileges! It automatically adds \'wheel\' to Groups.

        ================================================================================
        ================================================================================

        User creation

        1) [x] Create user
        2) Full name
        Peter
        3) User name
        peter
        4) [x] Use password
        5) Password
        Password set.
        6) [x] Administrator
        7) Groups
        wheel

        Please make a selection from the above ['c' to continue, 'h' to help, 'q' to
        quit, 'r' to refresh]:

    With all user options set, the \'c\' returns back to the overview
    screen.

    All non-British users may grab the opportunity to adjust the time
    zone using option 2 now.

    Another \'c\' continues with the execution of the entire
    configuration process. The operation takes some time and then ends
    in a login prompt.

        \&#8230;
        \&#8230;
        [  OK  ] Finished Initial Setup configuration program.
        [  OK  ] Reached target Preparation for Logins.
        [  OK  ] Started Getty on tty1.
        [  OK  ] Started Serial Getty on ttyS0.
        [  OK  ] Reached target Login Prompts.
        [  OK  ] Reached target Multi-User System.
        Starting Record Runlevel Change in UTMP\&#8230;
        [  OK  ] Finished Record Runlevel Change in UTMP.

        Fedora Linux 41 (Server Edition)
        Kernel 6.11.4-301.fc41.x86_64 on an x86_64 (ttyS0)

        Web console: https://localhost:9090/ or https://192.168.158.155:9090/

        linux login:

    In the first lines you may get 2 SELinux messages alike
    \'systemd-gpt-auto-generator\[xxxx\]: Failed to dissect: Permission
    denied\'. You can savely ignore those messages.

    The virtual server is up and running now, and ready for log in. The
    initial configuration process is a bit idiosyncratic for these
    times. But eventually simple and straightforward.

2.  &#42;Optionally: Adjust locale and non-US keyboard layout&#42;

    Users of a non-US keyboard layout probably want to customize the
    keyboard layout first of all. This facilitates any subsequent
    operation. First, check the current locale configuration

        […]\&#35; sudo -i
        […]\&#35; localectl
        System Locale: LANG=en_US.UTF-8
        VC Keymap: us
        X11 Layout: us

    List available keyboard mappings filtered by your short county code
    part

        […]\&#35; localectl list-keymaps  | grep de-
        de-T3
        de-deadacute
        de-deadgraveacute
        de-deadtilde
        de-mac
        de-mac_nodeadkeys
        de-neo
        de-nodeadkeys
        \&#8230;

    Determine applicable key mapping and apply it

    ``` bash
    […]\&#35; localectl set-keymap de-nodeadkeys
    ```

    The setting is immediately active.

3.  &#42;Set hostname&#42;

    A correct hostname is specifically important for DHCP of the
    internal network to work properly. A correct time is important for
    various tasks, specifically synchronization.

    a.  *Check hostname*. You need a correct static hostname.

            […]\&#35; hostnamectl

    b.  *Set hostname* if required:

            […]\&#35; hostnamectl  set-hostname  \&lt;YourFQDN\&gt;

4.  &#42;Check time zone and time synchronisation&#42; if you missed
    that previously

    a.  *Check time settings*

            […]\&#35; timedatectl

    b.  Correct time zone if necessary:

            […]\&#35; timedatectl set-timezone  \&lt;ZONE\&gt;

    c.  If necessary, activate time synchronisation:

            […]\&#35; timedatectl set-ntp true

    d.  Correct time if necessary:

            […]\&#35; timedatectl set-time  \&lt;TIME\&gt;

5.  &#42;Consolidate the network configuration&#42;

    a.  At first &#42;check your interfaces&#42;

        If you followed the example installation above you should find

            […]\&#35; ip a
            1: lo: \&lt;LOOPBACK,UP,LOWER_UP\&gt; mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
            link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
            inet 127.0.0.1/8 scope host lo
            \&#8230;.
            2: enp1s0: \&lt;BROADCAST,MULTICAST,UP,LOWER_UP\&gt; mtu 1500 qdisc fq_codel state \&#8230;
            link/ether 52:54:00:3e:0e:f0 brd ff:ff:ff:ff:ff:ff
            \&#8230;
            3: enp2s0: \&lt;BROADCAST,MULTICAST,UP,LOWER_UP\&gt; mtu 8000 qdisc fq_codel state \&#8230;
            link/ether 52:54:00:cc:e7:ba brd ff:ff:ff:ff:ff:ff
            inet 192.168.122.42/24 brd 192.168.122.255 scope global dynamic noprefixroute enp2s0
            \&#8230;

        If the external interface doesn't provide DHCP you won't find an
        assigned IP address for enp1s0. That's what we would need to fix
        next.

    b.  Next let's &#42;check and fix NetworkManager naming&#42;

            […]\&#35; nmcli con
            NAME    UUID                                  TYPE      DEVICE
            'Wired connection 2'  8d971f49-033f-398a-9714-3a4e848178fb  ethernet  enp2s0
            'Wired connection 1'  8d971f49-033f-398a-9714-3a4e848178fb  ethernet  ---

        Most likely your interfaces are a named somewhat awkward way.
        Let's fix that to make administration of network easier and more
        comfortable. Don't forget to adjust the naming to your specific
        installation!

            […]\&#35; nmcli con mod 'Wired connection 1' connection.id enp1s0
            […]\&#35; nmcli con mod 'Wired connection 2' connection.id enp2s0

    c.  In case DHCP is missing on an interface, configure a static
        network connection

        We take the external interface as an example here.

            […]\&#35; nmcli con mod enp1s0 ipv4.method manual \
            ipv4.address 'xxx.xxx.xxx.xxx/yy' \
            ipv4.gateway 'xxx.xxx.xxx.zzz' \
            ipv4.dns 'xxx.xxx.xxx.vvv' \
            ipv6.method manual \
            ipv6.addresses xxxx:xxxx:xxxx:xxxx::yyyy/64 \
            ipv6.gateway xxxx:xxxx:xxxx:xxxx::zz \
            ipv6.dns 'xxxx.xxxx.xxxx.xxxx::vvv'  \
            connection.zone 'FedoraServer'
            […]\&#35; nmcli con up enp1s0
            […]\&#35; systemctl  restart  NetworkManager

    d.  The interface enp2s0 for the internal libvirt network may show
        an IPv6 IP, which we don't use. Therefore, you should disable
        IPv6 on the internal interface

            […]\&#35; nmcli con mod enp2s0 ipv6.method disabled \
            connection.zone 'trusted'
            […]\&#35; nmcli con up enp2s0
            […]\&#35; systemctl  restart  NetworkManager

    e.  Check the default routes if you have 2 interfaces, one with an
        external public connection, one with the internal network, which
        uses NAT by default. So you have 2 parallel connection paths to
        access the public network and will find something like

            […]\&#35; ip r
            default via 192.168.158.1 dev enp1s0 proto dhcp src 192.168.158.160 metric 100
            default via 192.168.122.1 dev enp2s0 proto dhcp src 192.168.122.107 metric 101
            192.168.122.0/24 dev enp2s0 proto kernel scope link src 192.168.122.107 metric 101
            192.168.158.0/24 dev enp1s0 proto kernel scope link src 192.168.158.160 metric 100

        Delete the NAT route to avoid issues because of ambigous routes
        by some application software.

            […]\&#35; nmcli con mod enp2s0 ipv4.never-default yes
            […]\&#35; nmcli con down enp2s0
            […]\&#35; nmcli con up enp2s0
            […]\&#35; systemctl reload NetworkManager
            […]\&#35; ip r
            default via 192.168.158.1 dev enp1s0 proto dhcp src 192.168.158.160 metric 100
            192.168.122.0/24 dev enp2s0 proto kernel scope link src 192.168.122.107 metric 101
            192.168.158.0/24 dev enp1s0 proto kernel scope link src 192.168.158.160 metric 100

6.  &#42;Adjust firewall setting of the internal interface&#42;

    The installer assigns all interfaces to the *FedoraServer* zone,
    which limits access to ssh (and Cockpit). For the internal,
    protected network a broader accessibility may be appropriate,
    depending on the use case. If appropriate, modify the configuration
    (check alternative zone and select a suitable one).

        […]\&#35; firewall-cmd   --get-active-zones
        […]\&#35; firewall-cmd   --permanent  --zone=trusted  --change-interface=\&lt;internalIF\&gt;
        […]\&#35; firewall-cmd   --reload
        […]\&#35; firewall-cmd   --get-active-zones

7.  Optionally &#42;adjust default editor&#42;

    By default nano is the default system editor in Fedora. Many
    experienced system administrators prefer vim. If you are among the
    latter, adjust the default editor.

        […]\&#35; dnf install vim-default-editor --allowerasing

8.  &#42;Finally perform an update and reboot&#42;

        […]\&#35; dnf update
        […]\&#35; reboot

If you opted for Cockpit to instantiate the VM you may use Cockpits
graphical interface for the last 4 steps.

Anyway, you should now test to connect via ssh to the system, if it
provides an external interface.

## Set up storage {#_set_up_storage}

Fedora Server KVM follows the same storage organization principles as
the base installation. The [Fedora Server Installation
Guide](installation/index.adoc&#35;Planning_ahead) explains the
principles and the available choices. You have to make the same choice
here.

The distributed disk image features a disk size of about 7 gb. This is
not intended as a default value to use but as a starting value for
adaptation to the specific installation requirement. You have probably
already adjusted the total desired size at the
xref:&#35;instantiation_of_a_server_virtual_machine\[begin of
installation\]. If not, shutdown the virtual machine and adjust the size
now. As already noted, you need not to be too sparing in the choice. You
can easiy enlarge the maximum size later. And thanks to the qcow2
format, it allocates just the space that is actually needed and doesn't
waste resources. On the other hand, there is also no reason to be overly
generous.

At this point, we have to specify the allocation and adjustment of the
intended maximum disc size. Unfortunately, Cockpit doesn't provide
graphical support for editing an existing partition table. So we are
bound to CLI for the first step.

Login to the virtual machine and use the cfdisk utility to display the
space allocation as distributed and adjusted pre installation.

    […]\&#35; cfdisk /dev/vda
    Disk: /dev/vda
    Size: 37 GiB, 39728447488 bytes, 77594624 sectors
    Label: gpt, identifier: BAD551E3-F483-4FB3-BF4C-EF516A914C13

    Device              Start         End     Sectors    Size Type
    \&gt;\&gt;  /dev/vda1            2048        4095        2048      1M BIOS boot
    /dev/vda2            4096     2052095     2048000   1000M Linux filesystem
    /dev/vda3         2052096    14678015    12625920      6G Linux LVM
    Free space       14678016    77594590    62916575     30G


    ┌────────────────────────────────────────────────────────────────────────────┐
    │Partition UUID: 0534CD20-25E4-481A-AD28-E643E5328FDE                        │
    │Partition type: BIOS boot (21686148-6449-6E6F-744E-656564454649)            │
    └────────────────────────────────────────────────────────────────────────────┘
    [_Delete_]__[_Resize_]__[__Quit__]__[__Type__]__[__Help__]__[__Write_]
    [__Dump__]
    Device is currently in use, repartitioning is probably a bad idea.
    Quit program without writing changes

As you see, on the disk there is unused space, not associated to any
partition. Quit cfdisk for now.

Partition vda3 contains a Volume Group (VG).

    […]\&#35; vgdisplay
    --- Volume group ---
    VG Name               sysvg
    System ID
    Format                lvm2
    \&#8230;
    VG Size               \&lt;6.02 GiB
    PE Size               4.00 MiB
    Total PE              1541
    Alloc PE / Size       1541 / \&lt;6.02 GiB
    Free  PE / Size       0 / 0
    VG UUID               ybQrEj-xSeB-SWxw-4BMM-VXAG-3re7-2rt3xr

As you see, the complete space is occupied by a Logical Volume (LV).

Check the logical volume

    […]\&#35; lvdisplay
    --- Logical volume ---
    LV Path                /dev/sysvg/root
    LV Name                root
    VG Name                sysvg
    \&#8230;
    LV Size                \&lt;6.02 GiB
    Current LE             1541
    Segments               1
    Allocation             inherit
    Read ahead sectors     auto
    - currently set to     256
    Block device           253:0

As you see, the Logical Volume is of the same size as the Volume Group,
about 6 GiB.

### Available alternatives {#_available_alternatives}

1.  Enlarge the LVM partition to file all of the free space and enlarge
    the root file system alike. In this way, there is no separation of
    system and user data. This is convenient, but in no way
    recommendable.

2.  Enlarge the LVM partition to file all of the free space and enlarge
    the root file system to a reasonable value between 10 and 15 gb,
    depending on the intended total size of the disc. The remaining
    space in the Volume Group remains free for now. Later, the
    administrator creates logical volumes for user data or applications
    as needed. This is the recommended way.

3.  Enlarge the existing VG and the root file system to a reasonable
    size. Create a new VG in the remaining region, which later
    accommodates LVs for user data. This pushes the separation even
    further.

4.  Enlarge the distributed virtual disk to a reasonable size to
    accommodate the root file system only and create one or more
    separate virtual disk(s) to accommodate user data.

#### Alternative 2: Enlarge the VG to fill the disk, and root LV to a reasonable size {#_alternative_2_enlarge_the_vg_to_fill_the_disk_and_root_lv_to_a_reasonable_size}

1.  Enlarge the LVM partition to fill the disk

        […]\&#35; cfdisk /dev/vda
        Disk: /dev/vda
        Size: 37 GiB, 39728447488 bytes, 77594624 sectors
        Label: gpt, identifier: BAD551E3-F483-4FB3-BF4C-EF516A914C13

        Device              Start         End     Sectors    Size Type
        /dev/vda1            2048        4095        2048      1M BIOS boot
        /dev/vda2            4096     2052095     2048000   1000M Linux filesystem
        \&gt;\&gt;  /dev/vda3         2052096    14678015    12625920      6G Linux LVM
        Free space       14678016    77594590    62916575     30G


        ┌────────────────────────────────────────────────────────────────────────────┐
        │ Partition UUID: AFADA0EB-4F01-46DE-A0F1-27A8FE850500                       │
        │ Partition type: Linux LVM (E6D6D379-F507-44C2-A23C-238F2A3DF928)           │
        │Filesystem UUID: 4X9IKV-1Qmj-KTYT-aRlj-G1sJ-vr3Y-SdTIhJ                     │
        │     Filesystem: LVM2_member                                                │
        └────────────────────────────────────────────────────────────────────────────┘
        [_Delete_]__[_Resize_]__[__Quit__]__[__Type__]__[__Help__]__[__Write_]
        [__Dump__]

        Reduce or enlarge the current partition

    Select resize, confirm the suggested maximum size, and then write
    the change to disk.

2.  Enlarge the VG to fill up the partition

        […]\&#35; pvresize    /dev/vda3
        Physical volume '/dev/vda3' changed
        1 physical volume(s) resized or updated / 0 physical volume(s) not resized
        […]\&#35; vgdisplay  sysvg
        --- Volume group ---
        VG Name               sysvg
        System ID
        Format                lvm2
        \&#8230;
        VG Size               \&lt;36.00 GiB
        PE Size               4.00 MiB
        Total PE              9215
        Alloc PE / Size       1535 / \&lt;6.00 GiB
        Free  PE / Size       7680 / 30.00 GiB
        \&#8230;
        […]\&#35;

3.  Enlarge the LV. A recommended size is 8 - 15G max, depending on the
    total disk size. As an example, the new size is 12 G which leaves
    the rest free for further user data LVs.

        […]\&#35; lvextend -L 12G  /dev/mapper/sysvg-root
        Size of logical volume sysvg/root changed from \&lt;6.00 GiB (1535 extents) to 12.00 GiB (3072 extents).
        [ 1337.365631] dm-0: detected capacity change from 12574720 to 25165824
        Logical volume sysvg/root successfully resized.

4.  Enlarge the XFS root filesystem to fill the LV

        […]\&#35; xfs_growfs /dev/mapper/sysvg-root
        meta-data=/dev/mapper/sysvg-root isize=512    agcount=4, agsize=392960 blks
        =                       sectsz=512   attr=2, projid32bit=1
        \&#8230;
        data blocks changed from 1571840 to 3145728

        […]\&#35; df -h
        Filesystem              Size  Used Avail Use% Mounted on
        \&#8230;
        /dev/mapper/sysvg-root   12G  1.8G   11G  15% /
        \&#8230;

For the last 2 steps you can also switch to *Cockpit*. But the 2 lines
may not be worth it unless you use the Cockpit terminal anyway.

#### Alternative 3: Create a separate Volume Group for user data {#_alternative_3_create_a_separate_volume_group_for_user_data}

1.  Perform the steps described in alternative 2, but specify the size
    of the LVM partition by e.g. 20G and the root LV to 12G. In this
    way, there is still some room for disposition in case of surprises.

2.  Use cfdisk to create a *new partition*, */dev/vda4* in this example,
    of type \'Linux LVM\' using the complete remaining diskspace.

3.  Create a Physical Volume (PV) in the new partition

        […]\&#35; pvcreate /dev/vda4
        Physical volume '/dev/vda4' successfully created.

4.  Create a Volume Group (VG) in the new Physical Volume

        […]\&#35; vgcreate usrvg /dev/vda4
        Volume group 'usrvg' successfully created

        […]\&#35; vgs
        VG    \&#35;PV \&#35;LV \&#35;SN Attr   VSize   VFree
        sysvg   1   1   0 wz--n- \&lt;20.00g  \&lt;8.00g
        usrvg   1   0   0 wz--n- \&lt;16.00g \&lt;16.00g

Later, use usrvg to create LVs for user data as needed.

#### Alternative 4: Create a separate virtual disk for user data {#_alternative_4_create_a_separate_virtual_disk_for_user_data}

The prerequisite is that the configuration of the system disk has been
completed. Perform the steps described in alternative 2, but enlarge the
distributed system virtual diskimage and correspondingly the VG to e.g.
20G and the root LV to 12G. In this way, there is still some room for
disposition in case of surprises. With a separate data disk, alternative
1 would be an option, too.

You can use either *CLI* or *Cockpit* for this step.

#### Using CLI {#_using_cli}

1.  On the host system, create a *new virtual disk* in
    /var/lib/libvirt/images

        […]\&#35; qemu-img create -f qcow2 /var/lib/libvirt/images/${VM_NAME}-usr.qcow2  20G
        Formatting '/var/lib/libvirt/images/vm01-test-usr.qcow2', fmt=qcow2 cluster_size=65536 extended_l2=off compression_type=zlib size=21474836480 lazy_refcounts=off refcount_bits=16

        […]\&#35; qemu-img info  /var/lib/libvirt/images/${VM_NAME}-usr.qcow2
        file format: qcow2
        virtual size: 20 GiB (21474836480 bytes)
        disk size: 196 KiB
        cluster_size: 65536
        Format specific information:
        compat: 1.1
        compression type: zlib
        lazy refcounts: false
        refcount bits: 16
        corrupt: false
        extended l2: false

2.  Continue on the host and add the disk to the virtual machine. Use
    the first available diskname. The system disk is vda, so the next
    available disk name is vdb. If you are unsure check in the virtual
    machine, e.g. using \'*lsblk*\'.

        […]\&#35; virsh attach-disk ${VM_NAME} /var/lib/libvirt/images/${VM_NAME}-usr.qcow2  vdb --cache default --persistent --targetbus=virtio --subdriver qcow2
        Disk attached successfully

    The command needs the absolute path to the image file as noted.
    Otherwise it will fail. The disk is available immediately.

    If you want to modify something, detach the file first.

        […]\&#35; virsh detach-disk ${VM_NAME}   vdb  --persistent
        Disk detached successfully

3.  On the virtual machine, use cfdisk to partition the disk according
    to your requirements. The example creates one partition spanning the
    entire disk capacity.

    First, cfdisk displays a list for selecting the partitioning type.
    Select GPT.

        […]\&#35; cfdisk  /dev/vdb
        Disk: /dev/vdb
        Size: 192.5 KiB, 197120 bytes, 385 sectors
        Label: gpt, identifier: 2842C26B-A2F1-4946-9D89-AB8832E5FCEC

        Device                 Start        End      Sectors       Size Type
        \&gt;\&gt;  Free space                34        351          318       159K



        [___New__]__[__Quit__]__[__Help__]__[__Write_]__[__Dump__]


        Create new partition from free space

4.  Create a Physical Volume (PV) in the new partition (adjust the
    device accordingly!)

        […]\&#35; pvcreate /dev/vdb1
        Physical volume '/dev/vdb1' successfully created.

5.  Create a Volume Group (VG) in the new Physical Volume (adjust the
    device accordingly!)

        […]\&#35; vgcreate  usrvg  /dev/vdb1

Later, use usrvg to create LVs for user data as needed.

#### Using Cockpit {#_using_cockpit}

1.  Open Cockpit on your host system, select *Virtual Machines* in the
    navigation column, and then select the machine to which you want to
    add a disk. Scroll down until you see the disk section. Finally,
    select *Add disk* on the right side of the subtitle bar.

    ![Cockpit add disk form](virtualization/diskimg-fedoraserver-30.png)

    Most of the input fields are suitably preconfigured. Enter a (file)
    name for the disk image. Use a consistent naming scheme to
    facilitate long-term system maintenance. Specify the intended
    maximum size of the disk and decide on \'Always attach\'. It is best
    to leave the other properties untouched.

    Select *Add* to complete the task.

2.  Open Cockpit on the virtual machine you added the device to and
    select *Storage*. Cockpit assigns automatically the next disk
    identifier, /dev/vdb in case of Server VM.

    ![VM storage view](virtualization/diskimg-fedoraserver-32.png)

3.  Select the new disk and create a partition table and file system as
    needed.

    ![VM disk partitioning](virtualization/diskimg-fedoraserver-35.png)

## Follow-up customization {#_follow_up_customization}

It is advisable to review all the tasks in the general
[post-installation guide](installation/postinstallation-tasks.xml) for
virtual machines as well.

# Installing the Fedora Server Edition as a virtual machine using Cockpit {#_installing_the_fedora_server_edition_as_a_virtual_machine_using_cockpit}

Peter Boy; Jan Kuparinen :page-authors: Peter Boy, Kevin Fenzi

> The objective here is to install a Fedora Server in a virtual machine
> using the deployed generic installation media. An underlying
> assumption is that the processor architecture is the same as that of
> the host. The other case is also possible, but requires additional
> configuration.

The descriptions can also be used as a blueprint for installing other
distributions with the respective distribution&amp;&#35;8217;s own
installation media.

## Why Cockpit {#_why_cockpit}

Fedora Server is designed as a \'headless\' system, i.e. it comes
without an elaborate graphical user interface and corresponding
hardware. Only a simple text console is available. A system
administrator has to perform all work on the machine using the command
line.

Cockpit offers an alternative \'remote\' graphical interface. It
operates in the web browser of the system administrator&amp;&#35;8217;s
desktop and executes the required commands on the server on behalf of
them.

First hand, Cockpit saves the memorization of the complex parameter zoo
of *virt-install*, the CLI installation tool. It saves long typing on
the keyboard including the correction of accidental typos. But even
those who \'speak *virt-install*\' fluently, can benefit from Cockpit.
It automatically provides a lot of status information about
configuration and resource usage, which you would otherwise have to
collect manually. And this information is always present, no need to
keep this information in mind.

Therefore, Cockpit is useful for a beginner in server administration,
for the part-time administrator as well as for experienced
administrators. Particularly impressive is, that Cockpit does not
require its own specific configuration organization, but strictly uses
the standard configuration methods. So you can mix and match Cockpit
based and CLI based administration work. This makes it pleasantly
different from the popular NAS devices or even professional interfaces
such as the old Sun Cobalt appliances or ISP Config.

## Preparations {#_preparations_2}

We assume a complete installation of virtualization support according to
the [Adding Virtualization Support](virtualization/installation.xml)
guide.

Open your browser and connect to the Cockpit instance of your host
server. Consult the [post-installation
guide](installation/postinstallation-tasks.xml) to find out the possible
connection paths. Log in as root or with your administrative account. In
the overview (start) page select &#96;*Virtual Machines*&#96; in the
left navigation column.

If there is no entry &#96;*Virtual Machines*&#96; follow the before
mentioned guide for completion.

![Cockpit Virtual Machines Page first
used](virtualization/vm-install-fedoraserver-cockpit-010.png)

### Provisioning installation media {#_provisioning_installation_media}

Cockpit offers the option to load an installation medium not only
locally, but also from a remote location. Especially if several virtual
machines are to be installed, it is more efficient to keep the
installation medium locally.

Select &#96;*Terminal*&#96; in the left navigation bar and issue the
commands line by line:

    […]\&#35; sudo wget -P /var/lib/libvirt/boot/  https://download.fedoraproject.org/pub/fedora/linux/releases/41/Server/x86_64/iso/Fedora-Server-dvd-x86_64-41-1.4.iso
    […]\&#35; sudo wget -P /var/lib/libvirt/boot/ https://download.fedoraproject.org/pub/fedora/linux/releases/41/Server/x86_64/iso/Fedora-Server-41-1.4-x86_64-CHECKSUM
    […]\&#35; sudo curl -O https://fedoraproject.org/fedora.gpg | gpg --import
    […]\&#35; sudo gpgv --keyring ./fedora.gpg  /var/lib/libvirt/boot/\&#42;-CHECKSUM
    […]\&#35; sudo sh -c ' cd /var/lib/libvirt/boot/  \&amp;\&amp;  sha256sum --ignore-missing -c \&#42;-CHECKSUM '

You can safely ignore the warning of the last command about not
correctly formated lines.

You can provide additional installation media in an analog way. With
everything necessary in place, we can start installing a virtual
machine.

## Basic configuration of the virtual machine to get installed {#_basic_configuration_of_the_virtual_machine_to_get_installed}

:::: important
::: title
:::

This guide uses Cockpit, version 326, and Cockpit machines, version 321.
On updated systems, you may have an updated version and see slightly
different screens.
::::

To start a VM installation, connect your desktop browser to the Cockpit
instance of your host server. Consult the [post-installation
guide](installation/postinstallation-tasks.xml) to find out the possible
connection paths. Log in as root or with your administrative account. In
the overview (start) page select &#96;*Virtual Machines*&#96; in the
left navigation column and then &#96;*Create VM*&#96; (the button
&#96;*Import VM*&#96; next to it refers to the other alternative, using
disk images) and fill in the form that opens..

![Cockpit &#96;\_\_Create new virtual machine\_\_&#96;
form](virtualization/vm-install-fedoraserver-cockpit-020.png)

First, specify a name for the virtual machine to be created. It must be
unique in the host server's name space. Select an connection type,
usually system. See explanation in the [Adding Virtualization
Support](virtualization/installation.xml) guide.

Then select the installation type to be used. The drop down menu offers
several alternatives:

Download an OS

:   Download from a remote location. You have to choose the Distribution
    from a drop down menu in the next field. It includes various
    distributions and version. But you can&amp;&#35;8217;t select the
    Fedora edition. Not an recommendable option.

Cloud base image

:   That refers to the special case of cloud disk images. That is not
    covered here.

Local install media

:   Use a ISO image or a distro install tree stored on the local disk.
    This is the option we want to use here. Select this option and
    specify in the next field the fully qulified path and filename.

URL (ISO image or distro install tree)

:   The same as \'Download an OS\', but you can freely specify the exact
    distribution by download URL in the next field and do not depend on
    a preset list

Network boot (PXE)

:   That&amp;&#35;8217;s another special case we don&amp;&#35;8217;t
    cover here. You need to set up a special install server beforehand.

As mentioned above choose &#96;*Local install media*&#96; and select in
the drop down menu of the following row the fully qualified file name.
In our example of Fedora Server 41 it is
&#96;/var/lib/libvirt/boot/Fedora-Server-dvd-x86_64-41-1.3.iso&#96;. The
drop down menu works a bit unfamiliar. You have to select the target
file step by step from subdirectory to subdirectory up to the file name.

In the next line, \'Operating system\', Cockpit should display the
correct OS \'Fedora\' and release, in this example \'41\'. Otherwise use
the drop down menu to select the correct operating system. Use
&#96;*(unkown)*&#96; or &#96;*Fedora (unkown)*&#96; as fallback, if the
exact version and edition is not included in the selection list.

In the next fields, leave &#96;*Storage*&#96; at the default value
*Create new volume*, and select an appropriate size of virtual hard disk
and memory.

Finally, check all entries again and then select &#96;*Create and
edit*&#96; option. This allows us to perform further configurations,
especially the network connections. This saves additional administration
work later on.

It takes a short time and then the virtual machine's details page is
displayed.

![Cockpit &#96;\_\_Virtual machine details\_\_&#96; configuration
form](virtualization/vm-install-fedoraserver-cockpit-030.png)

The upper part offers the opportunity to configure a number of general
properties of the virtual hardware, including the size of the memory and
the number of CPUs. The Autostart option defines whether the server
should start the virtual machine automatically at system startup -
important for reliable everyday operation.

Adjust the options according to your need.

### Disks {#_disks}

The disk list shows that Cockpit has created a virtual disk in the pool
*Disk images*, which resides in the &#96;\~/libvirt/images&#96;
directory. The virtual machine name is used as the name of the disk
image file. The file extension qcow2 indicates a dynamic image format
that occupies only as much space as the available data require and grows
as needed to the maximum set size. This can be seen clearly in the
*Used* and *Capacity* columns.

The administrator does not need to worry about all these details. A
clear benefit of Cockpit.

### Network connections {#_network_connections}

The list of network interfaces shows only one interface, the internal
network managed by libvirt. However, virtual machines are mostly used
for tasks that require access to the public network and also require
reachability *from* the public network. Examples are web and mail
servers or other custom services. The key part is to isolate these
accesses from the host server for security reasons.

So, the virtual machine must access the public interface of the host. To
do this, you can either bind a virtual bridge to the interface or use
Mac-vlan. The latter adds virtual interfaces to the physical interface,
each with its own Mac address and its own IP (and alias IPs if needed).
The libvirt toolkit refers to this as &#96;*direct attachment*&#96;. It
is now the recommended approach. It acts similar to a bridge, but with
less system load. The disadvantage is that direct communication between
the host and the VMS is not possible, but between the VMs it is. Hosts
and VMs can only communicate via the internal, protected network. For
administrators of remote, not directly accessible servers, the
additional big advantage is that after the initial configuration, there
is no need to touch the precious network connection again.

An administrator who sticks to the habit that the first network adapter
in the device list establishes the external connection will now edit and
rearrange the existing network configuration. Select &#96;*Edit*&#96; to
access the Configuration form.

![Cockpit &#96;\_\_Virtual ethernet configuration
form\_\_&#96;](virtualization/vm-install-fedoraserver-cockpit-040.png)

Replace the interface type by &#96;*Direct attachment*&#96; and select
the external physical interface of the host in the &#96;*Source*&#96;
field. Leave &#96;*model*&#96; and &#96;*MAC address*&#96; unchanged.

Next, if you also want an internal network, select &#96;*Add network
interface*&#96;. A nearly identical form pops up. Select &#96;*Interface
tpye*&#96; as *Virtual network* if it is not already preselected and
*default* as &#96;*Source*&#96;. Again, leave &#96;*model*&#96; *virtio
(Linux, perf)* and &#96;*MAC address*&#96; *Generate automatically*
unchanged.

Now everything is ready and the installation can begin.

## Interactive installation {#_interactive_installation}

Select &#96;*Install*&#96; at the top of the form. After a short time
you see the well known initial screen of the install procedure.

![Cockpit Initial screen of installation
procedure](virtualization/vm-install-fedoraserver-cockpit-050.png)

After a test of the installation media the installation program,
Anaconda, shows up and displays the familiar overview screen. You may
select &#96;*Expand*&#96; at the right top to increase readability.
There is no collapse button, you have to click on the VM name in the
breadcrumb displayed at the top.

Start with installation as usual. You may basically follow the [Server
installation guide](installation/index.xml).

The installation process will take some time.

If you want to save the disk image for future VM creation, select
shutdown, copy the image to &#96;*\~/libvirt/boot/*&#96;, and then start
the VM anew for post-installation steps. Otherwise restart according the
installation program&amp;&#35;8217;s advise and procede with
post-install.

> &#42;*Excursus*: Save generated virual machine for later reuse&#42;
>
> Sometimes, after selecting *Shutdown* the machine automatically start
> again. Login with your administrativ account and perform a shutdown:
> &#96;sudo shutdown -h now&#96;. Then switch to a host's terminal
> window and execute:
>
>     […]\&#35; qemu-img convert -O qcow2 /var/lib/libvirt/images/{VM_NAME}.qcow2 /var/lib/libvirt/boot/fedora-servervm-img.qcow2
>
> A comparison of the two image files reveals that the originally
> created image is about 20 GiB in size, as specified while creating the
> virtual machine. Thus the dynamic capabilities of the qcow2 format are
> not used during the installation process. The copied image is only a
> fraction of that. The conversion process automatically re-uses the
> dynamic capability and creates a sparse image by masking out unused
> parts (thin provisioning). The copy could be made even smaller by
> using the -c parameter and additionally compressing the copied image.
> However, this may reduce the performance somewhat. In any way, the
> image will grow during later reuse in the course of operation
> depending on actual needs.
>
> Follow the accompanying tutorial to prepare the copied image for
> reuse.

## Virtual machines post installation tasks {#_virtual_machines_post_installation_tasks}

There are some post-install task that are specific for a virtual
machine. Otherwise, it is the same tasks that are performed after a
bare-metal installation.

> Before you start the post installation tasks you may consider to
> \'sparsify\' the image, i.d. to mask out currently unused space and
> convert the image to thin provisioning (and so using the dynamic
> capabilities of the qcow2 image format). You must use a host terminal
> window. Cockpit doesn't currently support such an operation.
>
>     […]\&#35; qemu-img convert -O qcow2 /var/lib/libvirt/images/{VM_NAME}.qcow2 /var/lib/libvirt/images/{VM_NAME}-sparse.qcow2
>     […]\&#35; mv  /var/lib/libvirt/images/{VM_NAME}-sparse.qcow2  /var/lib/libvirt/images/{VM_NAME}.qcow2

If you have not already done so, start the virtual machine and log in
with the administrator account. You can select *expand* at a top of the
terminal window to increase readability. Selecting \'Serial console\' on
the left above the terminal window instead of \'VNC console\' further
improves readability in some cases. However, on some devices this does
not work at all.

All subsequent tasks must be executed with ROOT privileges. If the root
account is locked, ROOT privileges should generally be acquired for the
sake of simplicity.

    […]\&#35; sudo -i
    [sudo] password for \&lt;user\&gt;:

### Mandatory post-installation tasks {#_mandatory_post_installation_tasks}

1.  &#42;Check hostname and time synchronisation&#42;

    A correct hostname is specifically important for DHCP of the
    internal network to work properly. A correct time is important vor
    various tasks, sopecifically syncronization.

    a.  *Check hostname*. You need a correct static hostname.

            […]\&#35; hostnamectl

        &#42; Set hostname if required:

            […]\&#35; hostnamectl  set-hostname  \&lt;YourFQDN\&gt;

    b.  *Check time zone, time synchronisation, time*

            […]\&#35; timedatectl

        &#42; Correct time zone if necessary:

            […]\&#35; timedatectl set-timezone  \&lt;ZONE\&gt;

        &#42; If necessary, activate time synchronisation:

            […]\&#35; timedatectl set-ntp true

        &#42; Correct time if necessary:

            […]\&#35; timedatectl set-time  \&lt;TIME\&gt;

2.  &#42;Consolidate internal network configuration&#42;

    The internal network must use DHCP. Don&amp;&#35;8217;t change that
    unless you are sure, what you are doing.

    Usually, it is useful to resolve a single member name to the
    internal network, in the example here vm1 to vm1.example.lan instead
    of vm1.example.com. For this purpose it is necessary to explicitly
    set the DNS search path of the internal interface.

    a.  List the interfaces and determine the name of the internal
        interface

            […]\&#35; nmcli con
            NAME    UUID                                  TYPE      DEVICE
            enp1  47df4730-171e-3bfe-b5d9-4238137e0f70  ethernet  enp1
            enp2  7627fc10-f1bf-3220-99e2-3bd369837439  ethernet  enp2

    b.  Set the DNS serach path for the internal interface

        If enp2 it the internal interface, set dns search and deactivate
        IPv6 that is not used internally

            […]\&#35; nmcli con mod enp2  ipv4.dns-search example.lan   ipv6.method disabled
            […]\&#35; nmcli con up enp2
            […]\&#35; systemctl  restart  NetworkManager

3.  &#42;Check name resolution&#42;

    Check /etc/resolv.conf

        […]\&#35; ls -al /etc/resolv.conf

    If it is a file instead of a link, you have to fix it.

        […]\&#35; rm -f /etc/resolv.conf
        […]\&#35; ln -s  /run/systemd/resolve/stub-resolv.conf   /etc/resolv.conf
        […]\&#35; ls -l /etc/resolv.conf
        […]\&#35; systemctl  restart  NetworkManager
        […]\&#35; systemctl  restart  systemd-resolved

    Check whether the name resolution works as desired.

        […]\&#35; host vm1.example.com
        […]\&#35; host vm1.example.lan
        […]\&#35; host vm1

4.  &#42;Adjust firewall setting of the internal interface&#42;

    The installer assigns all interfaces to the *FedoraServer* zone,
    which limits access to ssh (and Cockpit). For the internal,
    protected network a broader accessibility may be appropriate,
    depending on the use case. If appropriate, modify the configuration
    (check alternative zone and select a suitable one).

        […]\&#35; firewall-cmd   --get-active-zones
        […]\&#35; firewall-cmd   --permanent  --zone=trusted  --change-interface=\&lt;internalIF\&gt;
        […]\&#35; firewall-cmd   --reload
        […]\&#35; firewall-cmd   --get-active-zones

5.  &#42;Increase security of Cockpit access&#42;

    Refer to the corresponding section in the [post-installation
    guide](installation/postinstallation-tasks.adoc&#35;_4_increase_security_of_cockpit_access)
    to find options to enhance security of Cockpit access.

### Optional post-installation tasks {#_optional_post_installation_tasks}

1.  &#42;Making vim the default editor&#42;

    If you are a somewhat experienced administrator, you are probably
    annoyed that Namo, default editor since Fedora 34, always pops up
    when you want to edit crontab or similar. It is therefore worth
    reconfiguring right from the start.

        […]\&#35; dnf install --allowerasing vim-default-editor

2.  &#42;Reconfiguring the external interface as static&#42;

    Many administrators prefer to configure the external interface
    statically to ensure connectivity even if the DHCP server fails or
    is corrupted. Adjust the following example as needed.

        […]\&#35; nmcli con mod \&lt;IF_NAME\&gt; ipv4.method static \clear
        ipv4.address 'xxx.xxx.xxx.xxx/yy' \
        ipv4.gateway 'xxx.xxx.xxx.zzz' \
        ipv4.dns 'xxx.xxx.xxx.vvv' \
        ipv6.method manual \
        ipv6.addresses xxxx:xxxx:xxxx:xxxx::yyyy/64 \
        ipv6.gateway xxxx:xxxx:xxxx:xxxx::zz \
        ipv6.dns 'xxxx.xxxx.xxxx.xxxx::vvv'  \
        connection.zone 'FedoraServer'

    Ensure, parameter search-domain is empty!

3.  &#42;Remove unnecessary hardware packages&#42;

        […]\&#35; dnf remove iwl\&#42;  linux-firmware\&#42;  zd1211-firmware\&#42;  ipw\&#42;  atmel\&#42;  alsa-sof-firmware\&#42;

It is also advisable to review all the tasks in the general
[post-installation guide](installation/postinstallation-tasks.xml) for
virtual machines as well.

# Creating a virtual machine using a generic disk image -- the example of virt-builder {#_creating_a_virtual_machine_using_a_generic_disk_image_the_example_of_virt_builder}

Peter Boy :page-authors: Peter Boy :page-aliases:
virtualization-vm-install-diskimg-virtbuilder.adoc

> Many people and professional journals describe virt-builder as a way
> to \'*quickly build virtual machine images*\'. *This is simply wrong*.
> Instead, the program picks up an already *existing machine image*,
> referred to as a \'template\', and *customizes* it according to the
> parameters that the system administrator has specified. The
> virt-builder program does literally build nothing at all. The
> differentiation may be subtle. But those phrases distract from the
> fact that the entire process depends entirely on a large binary blob.
> And for a system built and trusted on free software, the question of
> how that blob is created deserves attention.

## How it works {#_how_it_works_3}

The creation of a virtual machine image involves two steps.

1.  The System Administrator invokes virt-builder and specifies the
    desired virtual machine properties via parameters. This includes in
    particular a user account, if necessary a password for root,
    hostname, and if desired additional programs to be installed,
    network configuration and other options. The program usually invoked
    in a way to save the created image right away in the machine images
    pool &#96;/var/lib/libvirt/images&#96;.

    Unless explicitly configured otherwise, virt-builder downloads a
    (binary) disk image built by the fsguest-tools project and infuses
    modification into the image according to the specified parameters.
    This binary is created along whatever rules the fsguest-tools
    project or one of its developers deems useful. The project also
    provides tools enabling a system administrator to build a local
    repository, with custom-created images. This is not the subject of
    this guide.

    This step is where the main work is done and it largely determines
    the final result.

2.  The next step is to run either virt-install or cockpit to merely
    instantiate the prebuilt image in QEMU/kvm. Post-installation work
    is limited to checking the functionality and viability of the
    configuration, and, of course, further customizing the system for
    individual purposes, as with any system installation.

Overall, the process is very straightforward and efficient.

## Select and customize a virtual machine binary -- the example of CentOS {#_select_and_customize_a_virtual_machine_binary_the_example_of_centos}

This step does the main work.

To get a CentOS virtual machine image, we use the default image
repository, which is maintained by the guests-tools project. First, we
need a list of available (CentOS) prebuilt machine images.

``` bash
[…]$ virt-builder --list  |  grep centos

gpg: checking the trustdb
gpg: marginals needed: 3  completes needed: 1  trust model: pgp
\&#8230;
centos-6                 x86_64     CentOS 6.6
centos-7.0               x86_64     CentOS 7.0
centos-7.1               x86_64     CentOS 7.1
centos-7.2               aarch64    CentOS 7.2 (aarch64)
centos-7.2               x86_64     CentOS 7.2
centos-7.3               x86_64     CentOS 7.3
centos-7.4               x86_64     CentOS 7.4
centos-7.5               x86_64     CentOS 7.5
centos-7.6               x86_64     CentOS 7.6
centos-7.7               x86_64     CentOS 7.7
centos-7.8               x86_64     CentOS 7.8
centos-8.0               x86_64     CentOS 8.0
centos-8.2               x86_64     CentOS 8.2
centosstream-8           x86_64     CentOS Stream 8
centosstream-9           x86_64     CentOS Stream 9
```

The guestfs-tools project provides a fairly complete set of variants
available in recent years. Omitting the grep term reveals an impressive
list of of distribution images provided.

We want the latest and greatest CentOS release and would like to get
some info about details.

``` bash
[…]$  virt-builder --notes   centosstream-9
gpg: checking the trustdb
\&#8230;
CentOS Stream 9

This CentOS Stream image contains only unmodified @Core group packages.

This template was generated by a script in the libguestfs source tree:
builder/templates/make-template.ml
Associated files used to prepare this template can be found in the
same directory.
```

Some system administrator may not know off the top of their head what
the \@core module leaves off. And the abbreviated link provided
doesn&amp;&#35;8217;t help much either.

### Minimal effort customization {#_minimal_effort_customization}

Even a quick and experimental setup should take the opportunity to set a
number of configurations for the virtual machine very easily right from
the start. These include

&#42; Either set up or block (recommended) the ROOT account &#42;
Setting up another administrative user &#42; Configure the hostname
&#42; Configuration of the keyboard layout in case of a non-US user

``` text
[…]$ sudo su -
[…]\&#35; virt-builder centosstream-9 \
--format qcow2 --output /var/lib/libvirt/images/vm1-el9vb.qcow2 \
--root-password locked:disabled \
--hostname vm1-el9vb.example.com \
--selinux-relabel \
--firstboot-command 'localectl set-keymap de-nodeadkeys' \
--firstboot-command 'useradd -m -G wheel -p '' hostmin ; chage -d 0 hostmin'
```

Please, adjust the above example as apropriate!

Specifically, *US users* will omit the 6. line (\'\--firstboot-command
\'localectl&amp;&#35;8230;&amp;&#35;8203;&#96;) of the virt-builder
command, other will have to adjust the keyboard layout. On your local
Fedora Server run &#96;localectl list-keymaps&#96;to get a list of
supported keyboard layouts and their identifiers.

If you really are to install a *short term test installation* you may
omit the third line (&#96;\--root-password
&amp;&#35;8230;&amp;&#35;8203;&#96;) of the virt-builder command for
connvenience and work directly as root. The app will automatically
generate a password and display it. Don&amp;&#35;8217;t forget to copy
and store it safely.

You get a lot ot output. The process takes some time. Be patient.

``` bash
gpg: checking the trustdb
\&#8230;
[   1.4] Downloading: http://builder.libguestfs.org/centosstream-9.xz
[   2.8] Planning how to build this image
\&#8230;
[  26.2] Setting passwords
[  27.4] SELinux relabelling
[  36.6] Finishing off
Output file: /var/lib/libvirt/images/vm1-el9vb.qcow2
Output size: 6.0G
Output format: qcow2
Total usable space: 5.4G
Free space: 4.3G (80%)
```

As you see, the virtual disk size is 6.0 G with 4.3 G at your
disposition.

### Some optional additional customization {#_some_optional_additional_customization}

1.  As noted above, the maximum disk size is 6 G with about 4 G at your
    disposition (you may not fill the space 100%). That is not too much
    and you might want to enlarge it.

        […]\&#35; qemu-img  info   /var/lib/libvirt/images/vm1-el9vb.qcow2
        […]\&#35; qemu-img resize  /var/lib/libvirt/images/vm1-el9vb.qcow2  +10G
        […]\&#35; qemu-img  info   /var/lib/libvirt/images/vm1-el9vb.qcow2

    The example above adds 10 GiB. The maximum virtual disk size of the
    CentOS image is 16 GiB now. The current (physical) disk size is
    still about 1 GB, due to the dynamic properties of the qcow2 file
    format.

    You can resize the virtual disk later, too. Therefore, there is no
    reason to plan too generously in terms of size now.

    You should *not* increase the maximum virtual disk image size by the
    *virt-builder parameter* &#96;\--size&#96;. It would increase the
    physical disk size to the same amount, which you probably
    don&amp;&#35;8217;t want.

2.  Additional information provides the virt-install [man
    page](https://libguestfs.org/virt-builder.1.html).

## Using virt-install CLI to instantiate the VM {#_using_virt_install_cli_to_instantiate_the_vm}

Use a terminal window. First, you may check the correct naming for the
parameter os-variant.

    […]\&#35; virt-install  --osinfo list

Import the virtual disk image.

    […]\&#35; virt-install  --name vm1-el9vb \
    --memory 2048  --cpu host --vcpus 2 --graphics none\
    --os-variant centos-stream9\
    --import  \
    --disk /var/lib/libvirt/images/vm1-el9vb.qcow2,format=qcow2,bus=virtio \
    --network type=direct,source=enp0s25,source_mode=bridge,model=virtio \
    --network bridge=virbr0,model=virtio

The parameters are quite descriptive. You will find a more detailed
explanation in the appendix.

You see a lot of output:

``` text
Starting install\&#8230;;
Creating domain\&#8230;;
Running text console command: virsh --connect qemu:///system console vm1-el9vb
Connected to domain 'vm1-el9vb'
Escape character is ^] (Ctrl + ])

[    0.000000] Linux version 5.14.0-71.el9.x86_64 (mockbuild@x86-05.stream.rdu2.redhat.com) \&amp;\&#35;8230;\&amp;\&#35;8203;
[    0.000000] The list of certified hardware and cloud instances for Red Hat \&amp;\&#35;8230;\&amp;\&#35;8203;
\&#8230;
[  OK  ] Finished Record Runlevel Change in UTMP.
[  OK  ] Finished Network Manager Wait Online.
[  OK  ] Reached target Network is Online.
Starting Crash recovery kernel arming\&amp;\&#35;8230;\&amp;\&#35;8203;

CentOS Stream 9
Kernel 5.14.0-71.el9.x86_64 on an x86_64

localhost login:
```

Log in with the administrative user account (hostmin in this example).
You can log in without a password, but you must create a (new) password
immediately.

### Adjust the new VM instance {#_adjust_the_new_vm_instance}

You did a minimal customization so var and need to do some further
adjustments.

#### Network consolidation {#_network_consolidation}

1.  Check the available network connections

        […]\&#35; ip a
        […]\&#35; nmcli con

    Depending on your runtime environment you may have to consolidate
    the network configuration. In the above example you get 2
    connections, one to the public network and another to the internal
    server network. For details see [Adding Virtualization
    Support](virtualization/installation.xml).

2.  Recommended: Adjust the naming

    Sometimes a connection gets named something like \'Wired connection
    1\'. For ease of administration, change the name, e.g. the device
    name.

        […]\&#35; nmcli con mod 'Wired connection 1' connection.id enp1s0

    In case of your internal network (virbr0), which provides DHCP, this
    step persists the network configuration. So you can assign a
    specific zone. Otherwise the system would create the connection anew
    with each boot.

3.  On demand: Adapt the external interface

    If the external network does not provide DHCP, you get just a
    minimal configuration without IP addresses. Adjust as appropriate.

        […]\&#35; nmcli con mod enp1s0 ipv6.method manual ipv6.addresses '2a01:xxx:yyy:zzz::uu/88' \
        ipv6.gateway 'fe80::1' \
        ipv6.dns '2a01:xxx:yyy:zzz::uuu:vvv 2a01:xxx:yyy:zzz::uuu:vvv 2a01:xx:yy:zz::uu:vv'

        […]\&#35; nmcli con mod enp1s0 ipv4.method manual ipv4.addresses 'xx.yy.zz.ww/vv' ipv4.gateway 'xx.yy.zz.ww' ipv4.dns 'xx.yy.zz.uu xx.yy.zz.vv xx.yy.zz.ww'

4.  On demand: assign a firewall zone

    Specifically for the internal interface (usually enp2s0) you might
    want to assign a specific zone, e.g. trusted or internal. And for
    the internal interface you might disable IPv6, Adjust as appropriate

        […]\&#35; nmcli con mod enp2s0 connection.zone 'internal'
        […]\&#35; nmcli con mod enp2s0 ipv6.method 'disabled'

5.  Finally restart the connections

        […]\&#35; nmcli con up enp1s0
        […]\&#35; nmcli con up enp2s0

## Using Cockpit's graphical UI to instantiate the VM {#_using_cockpits_graphical_ui_to_instantiate_the_vm}

Select *Virtual Machines* in the left navigation bar und click on
*Import VM*. A new form will open up

![Cockpit &#96;\_\_Import a virtual machine\_\_&#96;
form](virtualization/vm-install-diskimg-virtbuilder-010.png)

Specify a name for the virtual machine to be created. It must be unique
at least in the host server's namespace and at best in the designated
domain namespace. Select a connection type, use system for production
deployments. Consult the guide [Installing a Fedora Server virtual
machine using
Cockpit](virtualization/vm-install-fedoraserver-cockpit.xml) for details
about connection type.

Fill the remaining fields accordingly. Finally, deactivate *Immediately
start VM*. Otherwise, you will not be able to specify the network
environment and the first boot autoconfiguration can not configure the
network.

Select *Import* to create the basic virtual VM definition. It takes a
short time and then the Virtual machines page is displayed again. It's
list of virtual machines now shows an entry with the just defined VM in
the status \'Shut off\' and as next action \'Run\'.

### Extended definition of the virtual machine {#_extended_definition_of_the_virtual_machine}

Clicking the virtual machine name in the list opens a detailed
configuration page.

![Cockpit &#96;\_\_Virtual machin overview
form\_\_&#96;](virtualization/vm-install-diskimg-virtbuilder-020.png)

### Autostart {#_autostart}

Adjust the autostart option in the upper part according to your need.

### Network connections {#_network_connections_2}

The list of network interfaces shows only one interface, the internal
network managed by libvirt. However, you want to have external access,
too. The key part of most VMs is to isolate public accesse from the host
server for security reasons.

To enable public access, you can either bind a virtual bridge to the
interface or use Mac-vlan. The latter adds virtual interfaces to the
physical interface, each with its own Mac address and its own IP (and
alias IPs if needed). The libvirt toolkit refers to this as &#96;*direct
attachment*&#96;. It is now the recommended approach. It acts similar to
a bridge, but with less system load. The disadvantage is that direct
communication between the host and the VMS is not possible, but between
the VMs it is. Hosts and VMs can only communicate via the internal,
protected network. For administrators of remote, not directly accessible
servers, the additional big advantage is that after the initial
configuration, there is no need to touch the precious network connection
again.

An administrator who sticks to the habit that the first network adapter
in the device list establishes the external connection will now edit and
rearrange the existing network configuration. Select &#96;*Edit*&#96; to
access the Configuration form.

![Cockpit &#96;\_\_Virtual ethernet configuration
form\_\_&#96;](virtualization/vm-install-diskimg-virtbuilder-030.png)

Replace the interface type by &#96;*Direct attachment*&#96; and select
the external physical interface of the host in the &#96;*Source*&#96;
field. Leave &#96;*model*&#96; and &#96;*MAC address*&#96; unchanged.

Next, if you also want an internal network, select &#96;*Add network
interface*&#96;. A nearly identical form pops up. Select &#96;*Interface
tpye*&#96; as *Virtual network* if it is not already preselected and
*default* as &#96;*Source*&#96;. Again, leave &#96;*model*&#96; (*Linux,
perf*) and &#96;*MAC address*&#96; (*Generate automatically*) unchanged.

Now everything is ready. Select \'Run\' at the top to complete the
import and to start the VM.

The Console window shows the startup process and finally the login
prompt. Log in with the administrative user account (hostmin in this
example). You can log in without a password, but you must create a (new)
password immediately.

## Post instantiation tasks {#_post_instantiation_tasks}

If you look around, you will find

&#42; The hostname is already properly defined &#42; If DHCP is on all
interfaces available, network connection is working perfectly. However,
the interfaces are not configured permanently, but transiently. &#42;
Firewall is active. All interfaces belong to the default zone
\'public\'. &#42; The system uses a gpt partition table. It contains a
1GB XFS /boot partition, a swap partition, and an XFS root partition
that fills the rest. &#42; However, Cockpit is not even installed.

The resemblance of a CentOS server is not perfect, but fairly well done.

## Conclusion {#_conclusion}

Overall, the virt-builder/guestfs-tools-project provides an amazing
opportunity to quickly and straightforwardly create a well-crafted
virtual machine, instantiating various different distributions.
Fortunately, it is an open source project, but unfortunately the
\'openness\' did not receive detailed attention. It is very hard to
figure out how to access the source code. So, it is difficult to learn
how the virtual machine is built in detail and to check for potential
malicious ingredients. The provided information is quite scanty and
sometimes misleading. For example, the information on Fedora reads:
\'Fedora® 35 Server\'. However, the virtual machine created does not
have much to do with \'Fedora Server Edition\'. More appropriate would
be something like \'Some server based on Fedora RPM's\'. Sponsored by
Red Hat, a lot of Red Hat engineers are engaged in the project. So you
may (and should) pay some leap of faith, anyway.

A system administrator cannot expect to get a differently built, but
otherwise identical build of a distribution. This will need a closer
assessment and more or less detailed rework.

An alternative is an [instantiating using a cloud base
image](virtualization/vm-install-cloudimg-centos9.xml). In the end, both
ways produce a similar result that requires some reworking anyway. If
available, neither can replace a virtual machine disk image created
directly by the distribution itself.

## Appendix {#_appendix}

### Short explanation of the virt-install parameter used {#_short_explanation_of_the_virt_install_parameter_used}

\--name VM_NAME

:   Unique name of the VM to install as shown e.g.in VM list

\--memory 3074

:   Amount of memory to allocate, adjust as appropriate

\--cpu host

:   same cpu type as host

\--vcpus 3

:   number of cpus for VM, adjust as appropriate

\--os-variant centos-stream9

:   Target operating system. Adjust distribution and version as needed

\--import

:   Fixed, skips installation procedure and boots from the first
    (virtual) disk as specified by the first disk parameter.

\--graphics none

:   Fixed, enforces a redirect of the VM login prompt to the host
    terminal window for immediate access. Enables to login either via
    Cockpit terminal window or via host terminal using &#96;virsh
    console &lt;VM_NAME&gt;&#96; (you may have to issue one or two
    additional &lt;enter&gt;)

\--disk /var/lib/libvirt/images/VM_NAME.qcow2, format=qcow2,bus=virtio

:   disk image file, adjust VM_NAME

\--network direct,source=enpXsY,source_mode=bridge, model=virtio

:   specify *external* netwok (macvlan) *first*, it will get the name
    eth0 as usual. Adjust interface name as appropriate.

\--network bridge=virbr0,model=virtio

:   specify the *internal* network (libvirt generated bridge) *second*.
    It will get the name eth1 as usual.

### Virt-install in Fedora or CentOS {#_virt_install_in_fedora_or_centos}

Critical for customization to work is SELinux relabeling, not only in
the case of installing additional software, but for virtually any
customization.

# Creating a virtual machine using a distribution&amp;&#35;8217;s Cloud base image -- the example of CentOS {#_creating_a_virtual_machine_using_a_distributionamp358217s_cloud_base_image_the_example_of_centos}

Peter Boy; Jan Kuparinen; :page-authors: Peter Boy, Kevin Fenzi
:page-aliases: virtualization-vm-install-cloudimg-centoos9.adoc
:page-aliases: virtualization-vm-install-cloudimg-centos9.adoc

> The objective here is to create a virtual machine based on any
> distribution. But instead of going through the distribution-specific
> installer, a cloud image is to be used. This reduces the installation
> process to copying a disk image with subsequent initial adaptation to
> the concrete runtime environment. The workload shrinks to a few
> minutes.

## Cloud Images {#_cloud_images}

A Cloud Image is a virtual machine disk image containing the operating
system of a specific distribution. It is ready to run in a virtual
runtime environment, customized to one of the cloud-platforms such as
Openstack, Amazon EC2, Google GCE etc. Most distributions also provide a
*generic image* or *base image* with a runtime environment without
additions to a specific cloud system. Such a generic image is (usually)
suitable for a QEMU/KVM/libvirt runtime environment.

*The procedure described here is therefore only suitable for
distributions that provide such a generic image*.

Depending on the distribution, cloud images may differ more or less from
a default installation using the distribution&amp;&#35;8217;s
installation media. There are also distributions, e.g.
[Ubuntu](https://serverfault.com/questions/438611/what-are-ubuntu-cloud-images),
that explicitly distinguish between [cloud
images](http://cloud-images.ubuntu.com/) and [server
images](https://ubuntu.com/download/server). Documentation about goals
and differences are mostly sparse or non-existent. *Debian* at least
makes an attempt to [document
differences](https://wiki.debian.org/Cloud/SystemsComparison).

*The system administrator must investigate whether the cloud image does
meet the requirements and expectations associated with using a VM of the
distribution*.

## How it works {#_how_it_works_4}

A cloud image is a kind of template, a runtime agnostic bootable generic
operating system directory tree. It is used directly as a bootable
(virtual) system disk in a virtual machine to be created, although still
practically unusable due to lack of concrete runtime-specific
configuration.

The challenge is to initially inject the specific runtime configuration
into the image. This includes first of all a user account with password
and administration authorization. In addition, network configuration,
console or other devices may be required. Only then does a cloud image
gets the ability to run in a specific environment and, above all, become
usable. This is the prerequisite for being able to perform detailed and
more extensive configurations later on, if necessary.

In a standard installation this basic configuration is part of the
distribution-specific installer. In case of a cloud image there are two
widely used *disk image modification tools* for Cloud images

&#42; *cloud-init* &#42; *ignition*

Both are designed to get the configuration data from the cloud system at
the first boot and apply it to the image. The developers fortunately had
some foresight and provided a \'nocloud\' procedure, too. So, the system
administrator of an autonomous server can provide a replacement. As you
may guess, in a cloud centric development a nocloud option has a tough
time. It remains somewhat of a challenge.

A third option is

&#42; *virt-customize*

a generic tool to modify any non-running virtual machine, provided by
&#96;guestfs-tools&#96;. It allows to install cloud images of older
distributions like CentOS 7 or earlier Ubuntu editions.

## What you get {#_what_you_get_2}

In particular, you get time. The workload is significantly lower and
correspondingly faster.

But by cloud base image you (usually) don't get an alternatively built
but otherwise identical build of a (server) distribution. There are some
subtle differences. Some are conceptual. For example, most cloud images
do not install a firewall. The cloud system usually provides this
function. The use concept for the persistent storage is also different
due to technical differences. And last but not least, cloud image
developers may have different goals than the developers of the server
variant installation of a distribution.

*It is up to the system administrator to decide whether the
functionality is identical to the extent that the advantages outweigh
the disadvantages and it makes sense to use a specific cloud image as a
virtual machine.*

## How to proceed {#_how_to_proceed}

First of all you need a working Fedora Server Edition including
virtualization support added and libvirtd daemon active. We assume an
internal network \'default\' with virbr0, DHCP, and DNS set up as well
(see section \'Add Virtualization Support\'). External network
connectivity will be provided by macvlan (ethernet interface) rsp.
macvtap (libvirt naming).

You have various options:

&#42; Using Cockpit graphical interactive tool to perform a quick
minimal VM setup &#42; Using virt-install CLI interactive tool to
perform a quick mminimal VM setup based on cloud-init &#42; Using
virt-install CLI interactive tool to perform a elaborate VM setup based
on cloud-init &#42; virt-customize and virt-install CLI tools for a
fairly easy, interactive VM setup &#42; Using any of the CLI tools to
perform a script based automated installation

We will only cover the former two variants here. They are so universal
that they are applicable to virtually all distributions. The latter ones
are heavily dependent on details of a particular distribution.

## General preparations {#_general_preparations}

Whichever of the presented installation methods is chosen, a cloud image
always has to be downloaded and verified. In the case of CentOS, this
involves the following steps.

1.  Check on the CentOS project site the lastest release of GenericCloud
    image: <https://cloud.centos.org/centos/9-stream/x86_64/images/> At
    the time of this writing it was
    CentOS-Stream-GenericCloud-9-20220315.0.x86_64.qcow2

2.  In the Cockpit terminal window, fetch a CentOS 9-stream generic
    image file and store it into the directory
    &#96;/var/lib/libvirt/boot&#96;. This is by convention the libvirt
    default location of images for installation. Check the integrity of
    the download.

        […]$ sudo su -
        […]\&#35; cd /var/lib/libvirt/boot
        […]\&#35; wget https://cloud.centos.org/centos/9-stream/x86_64/images/CentOS-Stream-GenericCloud-9-20220315.0.x86_64.qcow2
        […]\&#35; wget https://cloud.centos.org/centos/9-stream/x86_64/images/CentOS-Stream-GenericCloud-9-20220315.0.x86_64.qcow2.SHA256SUM
        […]\&#35; sha256sum --ignore-missing -c \&#42;.SHA256SUM

    You may want to gather some information about the image

    ``` bash
    […]\&#35; qemu-img  info CentOS-Stream-GenericCloud-9-20220315.0.x86_64.qcow2

    image: CentOS-Stream-GenericCloud-9-20220315.0.x86_64.qcow2
    file format: qcow2
    virtual size: 10 GiB (10737418240 bytes)
    disk size: 777 MiB
    cluster_size: 65536
    Format specific information:
    compat: 0.10
    compression type: zlib
    refcount bits: 16
    ```

    The virtual size, i.e. the amount of storage available to a VM at
    runtime, is 10 GiB. The actual file size is much smaller, due to the
    dynamic property of the qcow2 format. It grows on demand while
    executing.

## Using Cockpit for a graphical interactive installation {#_using_cockpit_for_a_graphical_interactive_installation}

You can start without any additional preparations.

### Installation {#_installation_2}

Select *Virtual Machines* in the left navigation bar und click on
*Create VM*. A new form will open up

![Cockpit &#96;\_\_Create new virtual machine\_\_&#96;
form](virtualization/vm-install-cloudimg-centos9-010.png)

When the form first opens, it looks a bit different from the above
screenshot. Specify a name for the virtual machine to be created. It
must be unique at least in the host server's namespace and at best in
the designated domain namespace. Select a connection type, use system
for production deployments. Consult the guide [Adding Virtualization
Support](virtualization/installation.xml) for details about connection
type.

Then select the installation type *Cloud base image* from the drop down
menu. The bottom part of the form changes and now resembles the
screenshot above except for the last 3 lines. Fill in Installation
source and Operating system and specify disk size and amount of RAM.

Finally tick *Set cloud init parameters*. The form changes again and
reveals the last 3 lines. Enter a root password, optionally an
additional user name and password.

:::: important
::: title
:::

You *must* enter a root password. This will activate the root account at
the same time. Otherwise, you can not obtain administrative privileges.
The additional user account doesn&amp;&#35;8217;t help!
::::

:::: important
::: title
:::

*NON-US system administrators*: Cloud image usually configures inially a
US keyboard, and you can adjust the keyboard layout after the first
login at the earliest. Limit the password to matching key positions (and
change it later if you want)
::::

Select *Create* to start the installation.

*After some seconds the VM is up and running.*

### Post installation tasks {#_post_installation_tasks_2}

In the list of running virtual machines click on the newly created box.

![Cockpit &#96;\_\_Create new virtual machine\_\_&#96;
form](virtualization/vm-install-cloudimg-centos9-020.png)

The created runtime environment is rather basic. With cloud image
installation, you cannot defer the creation process and fine-tune the
runtime configuration, as you can with other installation options. There
is a default disk configuration, e.g. a default CDrom and one disk as
configured. And there is just one network connection, which uses
libvirt&amp;&#35;8217;s default virtual network.

Log in with the root account. If you look around, you will find some
resemblance to a CentOS server configuration. Cockpit is installed, but
not activated. Firewall installation is completely missing. The virtual
disk contains one flat XFS file system. The active network configuration
resides in &#96;/etc/sysconfig/network-scripts&#96; (due to cloud-init
limitations). Residues of a NetworkManager network configuration exist
in &#96;/etc/NetworkManager/system-connections&#96;.

So there is some post-installation work to do.

#### Adjust locale and non-US keyboard layout {#_adjust_locale_and_non_us_keyboard_layout}

Users of a non-US keyborad layout probably want to customize the
keyboard layout first of all.

1.  Check the current locale configuration

        […]\&#35; localectl
        System Locale: LANG=en_US.UTF-8
        VC Keymap: us
        X11 Layout: us

2.  List available keyboard mappings filtered by your short county code
    part

        […]\&#35; localectl list-keymaps  | grep de-
        de-T3
        de-deadacute
        de-deadgraveacute
        de-deadtilde
        de-mac
        de-mac_nodeadkeys
        de-neo
        de-nodeadkeys
        \&#8230;

3.  Determine applicable key mapping and apply it

    ``` bash
    […]\&#35; localectl set-keymap de-nodeadkeys
    \&#8230;
    ```

    The setting is immediately activ.

#### Network configuration {#_network_configuration}

As noted, there is only one internal network connection. If the VM is
only to take over internal services, this is perfect. Skip this section.

However, virtual machines mostly provide public services and require
access to the public network and also require reachability *from* the
public network. The key part is to isolate these accesses from the host
server for security reasons.

One option is to bind a virtual bridge to the physical interface and
attach a VM to that bridge. The other option is Mac-vlan, where a VM
adds a virtual interface to the physical host interface. It gets its own
Mac address and its own IP (and alias IPs if needed). The libvirt
toolkit refers to this as &#96;*direct attachment*&#96;.

The latter is now the recommended approach. It acts similar to a bridge,
but with less system load. The disadvantage is that direct communication
between the host and the VMS is not possible, but between the VMs it is.
Hosts and VMs can only communicate via the internal, protected network.
For administrators of remote, not directly accessible servers, the
additional big advantage is that after the basic installation and
initial network configuration, there is no need to touch the precious
network connection again.

1.  While logged in use the terminal window to set the static hostname.
    It ensures a correct DNS setup in a DHCP environment.

        […]$ hostnamectl set-hostname vm1-el9.example.com
        […]$ hostnamectl

2.  If you expanded the terminal window click on the VM name in the
    breadcrumb to get the default view. Select shutdown to stop the
    virtual machine.

3.  An administrator who sticks to the habit that the first network
    adapter in the device list establishes the external connection will
    now edit and rearrange the existing network configuration. Select
    &#96;*Edit*&#96; to access the Configuration form.

    ![Cockpit &#96;\_\_Virtual ethernet configuration
    form\_\_&#96;](virtualization/vm-install-cloudimg-centos9-030.png)

    Replace the interface type by &#96;*Direct attachment*&#96; and
    select the external physical interface of the host in the
    &#96;*Source*&#96; field. Leave &#96;*model*&#96; and &#96;*MAC
    address*&#96; unchanged.

4.  If you also want an internal network (and you definitely should in
    most cases), select &#96;*Add network interface*&#96;. A nearly
    identical form pops up. Select &#96;*Interface tpye*&#96; as
    *Virtual network* if it is not already preselected and *default* as
    &#96;*Source*&#96;. Again, leave &#96;*model*&#96; (*Linux, perf*)
    and &#96;*MAC address*&#96; (*Generate automatically*) unchanged.
    Click Create to finish to create the network configuration.

5.  Start the virtual machine again.

#### Check network connections {#_check_network_connections}

1.  &#42;Check internal connections&#42;

    From a terminal window in the host system you should be able to ping
    your VM using the internal virtual network.

        […]$ ping  vm1-el9

    If the name service setup in the host is correct, the short name
    should work. Otherwise try the internal FQDN name (i.e. something
    like vm1-el9.example.lan). If name resolution doesn&amp;&#35;8217;t
    work, switch to the VM&amp;&#35;8217;s Cockpit terminal window. Use
    &#96;ip a&#96; to determine the internal IP and use this to ping the
    VM.

    If pinging the IP address works, fix the name resolution. Otherwise
    check again network configuration.

2.  &#42;Check external connections&#42;

    From a machine on your network try to ping the virtual machinge

        […]$ ping  vm1-el9.example.com

    In case of issues proceed analog to the internal connection.

### Security Enhancement {#_security_enhancement}

A Cockpit installation cannot implement the widely used security concept
of locking the root account. It requires additional administrative
modifications later on. In the CentOS default configuration, however,
root can log in via ssh and password. A certain protection of the root
account exists nevertheless.

1.  If there is already another user and this user is to be granted
    administrative rights, the account must be assigned to the wheel
    group.

        […]\&#35; usermod -aG wheel \&lt;USERNAME\&gt;

    Test if login and sudo work!

2.  If you decide to lock the root account, login as your administrative
    user and execute

        […]\&#35; sudo passwd -l root

    Log off and try to login as root (e.g. using the host's Cockpit
    instance). The system should respong with \'Login incorrect\'.

3.  If you decide to use the root account and you chose a simple
    password during installation, you should set a long and secure
    password. Log in as root and execute

        […]\&#35; passwd

    If root also needs access via ssh, a key-based login must be set up.
    Follow step 5 of the [post-installation
    guide](installation/postinstallation-tasks.xml).

4.  Install and activate the firewall

        […]\&#35; dnf install firewalld
        […]\&#35; systemctl  enable  firewalld   --now
        […]\&#35; firewall-cmd  --list-all

5.  If you want to use Cockpit you have to enable it

        […]\&#35; systemctl  enable  cockpit.socket   --now

    Cockpit should start up as soon as you connect with your browser.

6.  Finally, if you want the virtual machine to start automatically at
    system startup, check the corresponding box in the Cockpit VM
    overview. Alternatively execute

        […]\&#35; virsh autostart vm1-el9

## Using virt-install for a CLI interactive minimal effort installation {#_using_virt_install_for_a_cli_interactive_minimal_effort_installation}

This type of installation uses the &#96;\--cloud-init&#96; parameter of
&#96;virt-install&#96; without any value or subparameters. The approach
causes the generation and display of a root password shortly after the
start of installation, enabling a one-time login. You have to note or
copy it, of course.

Apart from that, the configuration is limited to configuring and
starting DHCP-supported Ethernet interfaces. Other interfaces are
basically defined but not dealt with further.

### Addition preparations {#_addition_preparations}

Essentially, you need to copy the downloaded image file to the libvirt
disk images pool yourself and name it as needed.

1.  Copy the disk image from the installation media pool to the disk
    images pool and choose the intended VM name as target.

        […]$ sudo su -
        […]\&#35; cd /var/lib/libvirt/boot
        […]\&#35; cp CentOS-Stream-GenericCloud-9-20220315.0.x86_64.qcow2  ../images/vm2-el9.qcow2

2.  Inspect the disk size and optionally adjust it. The default is about
    10 GiB.

        […]\&#35; qemu-img  info   /var/lib/libvirt/images/vm2-el9.qcow2
        […]\&#35; qemu-img resize  /var/lib/libvirt/images/vm2-el9.qcow2  +10G

    The example above adds 10 GiB to a total size of about 20 GiB.

    You can resize the virtual disk later, too. Therefore, there is no
    reason to plan too generously in terms of size now. Due to the qcow2
    format resizing does not affect the current image file size. It is
    dynamically adjusted as needed up to the maximum specified.

### Installation {#_installation_3}

Use a terminal window to execute

    […]\&#35; virt-install  --name vm2-el9\
    --memory 2048  --cpu host --vcpus 2 --graphics none\
    --os-variant centos-stream9\
    --import  \
    --disk /var/lib/libvirt/images/vm2-el9.qcow2,format=qcow2,bus=virtio \
    --network type=direct,source=enp0s25,source_mode=bridge,model=virtio \
    --network bridge=virbr0,model=virtio  \
    --cloud-init

The parameters are quite descriptive. You will find a more detailed
explanation in the appendix.

You see a lot of output:

``` text
WARNING  Defaulting to --cloud-init root-password-generate=yes,disable=yes

Starting install\&#8230;
Password for first root login is: YFlTBHprYYDh5gZ7
Creating domain\&#8230;                                                                                            |    0 B  00:00:00

Running text console command: virsh --connect qemu:///system console vm2-el9
Connected to domain 'vm2-el9'
Escape character is ^] (Ctrl + ])

[    0.000000] Linux version 5.14.0-71.el9.x86_64 (mockbuild@x86-05\&#8230;..
\&#8230;
\&#8230;
\&#8230;
[  OK  ] Finished Execute cloud user/final scripts.
[  OK  ] Reached target Cloud-init target.
[  OK  ] Created slice Slice \&#8230;
[  OK  ] Started dbus-:1.2-org\&#8230;

CentOS Stream 9
Kernel 5.14.0-71.el9.x86_64 on an x86_64

Activate the web console with: systemctl enable --now cockpit.socket

localhost login:
```

The installation ends with an active open terminal into the created VM!

Log in to the root account giving the password displayed early in the
installation process (YFlTBHprYYDh5gZ7 in this example). This password
is single use and must be replace during the first login.

:::: important
::: title
:::

*&#42;&#42;NON-US system administrators&#42;&#42;*: Cloud Image usually
configures a *US keyboard* first! The easiest way is to copy &amp; paste
the password. Limit the new password to matching key positions, choose a
rather simple one to minimize the chance ot typos, and change it to a
secure password later after keyboard configuration..
::::

#### Post-Installation Tasks {#_post_installation_tasks_3}

As usual, also in computer science the \'law of conservation of energy\'
applies. The lower the installation effort, the greater the
post-installation requirements.

1.  Non-US system administrators should adjust the layout first.

    a.  Check the current locale configuration

            […]\&#35; localectl
            System Locale: LANG=en_US.UTF-8
            VC Keymap: us
            X11 Layout: us

    b.  List available keyboard mappings filtered by your short county
        code part. Replaye \'de-\' by your country, i.e.
        \'&lt;COUNTRYCODE&gt;-\'

            […]\&#35; localectl list-keymaps  | grep de-
            de-T3
            de-deadacute
            de-deadgraveacute
            de-deadtilde
            de-mac
            de-mac_nodeadkeys
            de-neo
            de-nodeadkeys
            \&#8230;

    c.  Determine applicable key mapping and apply it

            […]\&#35; localectl set-keymap de-nodeadkeys
            \&#8230;

        The setting is immediately activ.

2.  Check network connection

        \&#35; ip a
        1: lo: \&lt;LOOPBACK,UP,LOWER_UP\&gt; mtu 65536 \&#8230;.
        \&#8230;
        2: eth0: \&lt;BROADCAST,MULTICAST,UP,LOWER_UP\&gt; \&#8230;
        link/ether \&#8230;.
        altname enp1s0
        inet uuu.vvv.www.xxx/zz \&#8230;\&#8230;
        \&#8230;
        3: eth1: \&lt;BROADCAST,MULTICAST,UP,LOWER_UP\&gt; \&#8230;
        link/ether \&#8230;.
        altname enp2s0
        inet uuu.vvv.www.xxx/zz \&#8230;
        \&#8230;

    If DHCP was available for all interfaces, a complete interface
    configuration is displayed.

    Check for connectivity:

        […]\&#35; ping guardian.co.uk
        […]\&#35; ping \&lt;YOUR_EXTERNAL_DEFAULT_GATEWAY_ADDRESS\&gt;
        […]\&#35; ping 192.168.122.1  \&#35; your host system internal virtual network address

    The VM can connect to internal and external destinations. The name
    resolution for the vm itself can&amp;&#35;8217;t work because the
    static hostname is not set yet. The external host address is not
    responding due to Mac vlan technology and the internal name
    resolution is not working yet.

    Check the interface devices.

        […]\&#35; nmcli dev
        DEVICE  TYPE      STATE      CONNECTION
        eth0    ethernet  connected  System eth0
        eth1    ethernet  connected  Wired connection 1
        lo      loopback  unmanaged  --

    The active (authoritative) configuration of the external network
    connection is &#96;/etc/sysconfig/network-scripts/ifcfg-eth0&#96;.
    The file
    &#96;/etc/NetworkManager/system-connections/ens3.nmconnection&#96;
    is a leftover from the pre cloud-init default system configuration.
    Currently cloud-init sticks to the deprecated filesystem position.
    There is no persistent configuration file for the internal interface
    to libvirt virbr0. The configuration is auto-generated with every
    boot process.

    Probably you want to have a persistent configuration file, so can
    assign a firewall zone to the connection. Just rename the
    connection.

        […]\&#35; nmcli con mod 'Wired connection 1' connection.id eth1

    The renaming triggers NetworkManager to create a file
    &#96;/etc/sysconfig/network-scripts/ifcfg-eth1&#96; with the current
    configuration.

    If DHCP is not available for the external interface, the
    configuration file is just a stub. Use the NetworkManager nmcli
    utility to define a static configuration.

3.  In case the virtual disk size has been changed, the partition sizes
    must be adjusted.

        […]\&#35; cfdisk  /dev/vda

    The only partition should already have the adjusted size. Otherwise
    select resize and then write.

    Next resize the file system, if not already done. First check the
    size of the file system, e.g. using df.

        […]\&#35; df -h
        […]\&#35; resize2fs -p /dev/vda1

4.  Finally, let&amp;&#35;8217;s set the hostname

    ``` bash
    […]\&#35; \&#35;\&#35;hostnamectl set-hostname  VM_NAME.example.com
    […]\&#35; hostnamectl set-hostname  vm2-el9.example.com
    ```

Exit and close the console typing &lt;ctrl&gt;+\].

You may reboot the VM and than check
/var/lib/libvirt/dnsmasq/virbr0.status again. It's now listing a
hostname, internal name resolution is working now.

If your external DHCP server provides dynamic DNS as well, you should be
able to connect to your VM from the public network:

``` batch
[…]\&#35; ping VM_NAME.example.com
```

Last action is to enable autostart of the VM.

    […]\&#35; virsh  autostart  VM_NAME

Everything is working fine now, nearly out of the box. You would now
start configuring the VM in detail according to its intended use. Just
as it would be required after a standard installation.

&#42;In the end it takes only some 5 minutes to set up a fully
functional system with minimal effort.&#42; It is ideal to quickly
create a virtual machine for an ad-hoc solution or as an interim
solution for a test.

## Conclusion {#_conclusion_2}

Using any of the described installation methods, provides an quite
comfortable installation and configuration process that would otherwise
consume a lot of time. It is this performance that makes the use of
cloud images so attractive.

The use of Cloud Base Images to create a distribution's virtual machine
installation comes with some inevitable inconveniences and shortcomings
due to the different nature of the techniques. So, in a production
deployment you may be better off with dedicated virtual machine images,
if available. But for experimentation and testing it should be viable
and suitable.

## Appendix {#_appendix_2}

### Short explanation of the virt-install parameter used {#_short_explanation_of_the_virt_install_parameter_used_2}

\--name VM_NAME

:   Unique name of the VM to install as shown e.g.in VM list

\--memory 3074

:   Amount of memory to allocate, adjust as appropriate

\--cpu host

:   same cpu type as host

\--vcpus 3

:   number of cpus for VM, adjust as appropriate

\--os-variant centos-stream9

:   Target operating system. Adjust distribution and version as needed

\--import

:   Fixed, skips installation procedure and boots from the first
    (virtual) disk as specified by the first disk parameter.

\--graphics none

:   Fixed, enforces a redirect of the VM login prompt to the host
    terminal window for immediate access.

\--disk /var/lib/libvirt/images/VM_NAME.qcow2, format=qcow2,bus=virtio

:   disk image file, adjust VM_NAME

\--network direct,source=enpXsY,source_mode=bridge, model=virtio

:   specify *external* netwok (macvlan) *first*, it will get the name
    eth0 as usual. Adjust interface name as appropriate.

\--network bridge=virbr0,model=virtio

:   specify the *internal* network (libvirt generated bridge) *second*.
    It will get the name eth1 as usual.

\--cloud-init

:   Deal with nocloud configuration using defaults

# Managing virtual machines with Cockpit {#_managing_virtual_machines_with_cockpit}

Peter Boy :page-authors: Peter Boy :page-aliases:
virtualization-vm-management-cockpit.adoc

> A virtual machine is created under certain assumptions about required
> memory, data storage, processing capacity, and so on. All too often,
> these assumptions need to be adjusted based on actual use practices,
> and require additional configuration work by a system administrator.
> Cockpit greatly simplifies and facilitates this work, especially for
> the Fedora Server Edition which does not include a graphical
> interface.
>
> The article describes selected often recurring reconfiguration tasks.

## Manage virtual machines configurations {#_manage_virtual_machines_configurations}

In your local browser, open Cockpit on the host system using port 9090,
e.g. &#96;[https://example.com:9090&#96](https://example.com:9090&#96);.
Log in either as root or with your administrative account. Select
\'Virtual Machines\' in the left navigation column.

![Cockpit Virtual Machines
Overview](virtualization/vm-management-cockpit-001.png)

If there is no tab \'Virtual Machines\' the corresponding Cockpit
module, cockpit-machines, is not installed yet. Consult the guide
[Adding Virtualization
Support](virtualization/installation&.xml#35;_finishing_cockpit_machines_configuration)
for information how to install and prepare the module.

The virtual machines *overview page* lists in the central area all
virtual machines installed along with their current state. In the
example above there are 3 virtual machines, 2 of them running. The most
frequently executed action, shutdown rsp. launch, is directly accessible
as a button. Additional commonly needed functions are offered in a
drop-down menu to the right of it. It even offers a (simple) migration
to another machine.

### Manage a virtual machines basic host runtime environment {#_manage_a_virtual_machines_basic_host_runtime_environment}

If you click onto a VMs name, a details page opens. In the top half it
shows the basic runtime parameter along with a terminal window into the
VM.

![Cockpit basic virtual machines runtime
parameter](virtualization/vm-management-cockpit-003.png)

Some of the parameters displayed are mostly informative, e.g. the
hypervisor details, or you will hardly ever want to change them, e.g.
the CPU type. These things can become useful when it comes to diagnosing
issues.

More interesting is the option to quickly enable and disable
*auto-start* on host reboot \[1\]. An example would be a (inactive)
backup VM that can take over when problems with the main VM arise. A
kind of \'cold-standby\', maybe the only possibility in case of tight
CPU and RAM resources on a machine. The action is taken immediately and
is effective (on the next host reboot), no need for an explicit submit.

Very useful in everyday operations are the real-time information about
the *resource consumption* for CPU and RAM \[2\] and the simultaneous
ability to adjust these parameters \[3\]. Although you will need to
reboot the VM to make these changes or have them take effect.

And of course, especially convenient is the *terminal window* into the
virtual machine. An uncomplicated way to quickly perform a CLI operation
in the graphical interface - the best of both worlds.

### Manage a virtual machines storage {#_manage_a_virtual_machines_storage}

A VM usually uses a (virtual) disk provided as a disk image file in the
Libvirt pool *images* (/var/lib/libvirt/images), either in qcow2 or raw
format. And managing storage means manipulation of the respective file.

#### Increase a virtual disk {#_increase_a_virtual_disk}

Cockpit is powerful but not (yet) perfect. The current version does not
provide a graphical tool for that purpose. The system administrator
still has to rely on CLI tools like *qemu-img* or the *virt-&#42;*
utilities of *guestsfs-tools*. Fortunately, we just have to use the CLI
tool to increase the virtual disk image while the VM is stopped.
Afterwards, we can start the VM again and use the VM's Cockpit to
reconfigure the storage.

As an example, use vm2 Cockpit to display the current configuration of
storage. Open <http://vm2:9090> (again, adjust the address as
appropriate) in your browser, log in, and select *Storage* from the left
navigation column.

![Cockpit filesystems
overview](virtualization/vm-management-cockpit-005.png)

In the *Filesystems* section of the central content area \[1\] there are
2 file systems: *root* of 11 GiB and *boot* of 1 GiB. Additional
information is in the right column. The *Devices* section indicates a
Volume group of 11 GiB \[2\]. This implies that the root file system
completely fills this Volume group. The *Drives* section lists a virtual
disk of 12 GiB \[3\]. This implies that this disk is completely filled
with the two file systems.

After shutting down vm2, we can increase the virtual disk by 20 GiB to a
total of 32 GiB in the *hosts* Cockpit terminal.

``` text
[…]\&#35; qemu-img  resize  /var/lib/libvirt/images/vm2.qcow2  +20G
Image resized.
[…]\&#35; qemu-img  info  /var/lib/libvirt/images/vm2.qcow2
file format: qcow2
virtual size: 32 GiB (34359738368 bytes)
disk size: 2.01 GiB
\&#8230;
```

As the info shows, the virtual disk size is now 32 GiB. The file still
occupies only 2.01 GiB in the directory, due to the qcow2 dynamic file
format.

This is due to the qcow2 file format, which dynamically occupies the
necessary space as needed. Therefore, the size of the extension should
be chosen quite generously to potentially save the work of a later
re-extension. In the case of multiple virtual machines, the sum of their
size can also exceed the real available space. This is not a problem as
long as not all virtual machines at the same time grow to a much greater
extent than planned. However, flexibility is gained in the case of
disproportionate growth of some single virtual machines.

#### Reconfigure an increased virtual disk {#_reconfigure_an_increased_virtual_disk}

After starting vm2 again the *Storage* page now shows unsurprisingly a
disk of 32 GiB, but nothing else changed. So the disk has now 20 GiB
unallocated space.

Fedora Servers default storage setup is based on the concept of
*segmenting storage* to facilitate system administration, prevent
spillover of errors, and others. For details, see the [Fedora Server
Installation
Guide](https://docs.fedoraproject.org/en-US/fedora-server/server-installation/).
Therefore, if you need additional space for an application or service,
e.g. web service, you would create a separate Logical volume in Fedora
Server following that rationale.

You have three options now:

1.  Enlarge the existing partition and Volume group to add logical
    Volume as needed. That's the way of Fedora Server's default
    partitioning scheme. Unfortunately, you can't enlarge partition and
    VG using Cockpit but have to use the terminal CLI in a one time
    action. Later, you can use to add or enlarge Logical volumes as
    needed using Cockpit.

2.  Avoid using the terminal and create an additional partition and
    Volume Group using just Cockpit. As with 1. you can use Cockpit
    again to add or enlarge Logical volumes as needed.

3.  Ignore the Fedora Server storage rationale and extend just
    everything to its maximal size.

We will continue with alternative 2 here. It is just as committed to the
Fedora Server rationale as alternative 1, if not even stricter. It is
with Cockpit the more comfortable variant and in the end implements the
same actions, i.e. creating a Logical volume with file system and
mounting it at a fitting position in the directory tree. And alternative
3 is conceptually the worst of all.

On the vm2 *Storage* page select the 32 Gib virtual disk and in the new
page that opens click on the \'Create partition\' button right below the
/dev/vda2 partition \[1\].

![Cockpit create partition
form](virtualization/vm-management-cockpit-006.png)

You only have to change the type to \'No filesystem\' \[2\] and create
the partition. It takes some time before a third partition is displayed
in the list.

Go back to the *Storage* page. At the top of the right column, activate
the menu icon next to *Devices* and select \'Create volume group\'.

![Cockpit create volume group
form](virtualization/vm-management-cockpit-007.png)

In the form that opens, enter a name for the Volume group, here in
analogy to fedora_fedora of the system area *fedora_user*, select the
newly created partition */dev/vda3*, and create the Volume group. The
form closes and on the *Storage* page you find a new device, the
fedora_user Volume group of 20.0 GiB.

#### Setup separated disk space for user data {#_setup_separated_disk_space_for_user_data}

As already mentioned, in compliance with the Fedora Server storage
concept, a data area separate from system data should contain the
service and user data. One FSH-compatible way is to mount the */srv*
directory in a separate Logical volume and store therein the respective
data for all services. Another way is to mount a well-known dedicated
application directory into its own Logical volume. For example, in
Fedora Server, PostgreSQL stores all its data into */var/lib/pgsql* or
Apache httpd in */var/www*. These directories are each mounted in their
own Logical volumes, preferably before the software is installed.

As an example we install httpd data into a separate logical volume. Just
in case the software is already installed, stop httpd and move the data
temporarily out of the way. We will restore them later. The directory
*/var/www* should be empty.

The *Storage* page of the virtual machine (vm2) displays the *Devices*
section in the top right column, and within the volume group fedora_user
that we configured earlier. Clicking fedora_user opens the volume group
configuration page. Below the box with details of the volume group is a
list of the existing logical volumes of this volume group.It provides a
link \'Create new logical volume\' to the right of the title, which
opens a configuration form.

![Cockpit create logical volume
form](virtualization/vm-management-cockpit-008.png)

Replace the preset name by a descriptive term, here e.g. webservice, and
choose a suitable size. Due to the dynamic space allocation of the qcow2
format you may choose the size definitely a bit generous. However, a
later extension with Cockpit is very easy to perform.

With *Purpose* the form also offers the option to create a pool for
\'thinly provisioned volumes\', which in turn accommodates logical
volumes allocating space dynamically. In case of a VM this is usually
not as helpful as on physical machines, because the qcow2 disk image
files already provide for a kind of thin provisioning. But your mileage
may vary.

After creating the Logical volume you find an entry in the list
\'Logical volumes\'. Expand the line using the triangle icon. You will
find a *Format* Button. The associated form allows you to create and
mount a file system in one pass.

![Cockpit file system
creation](virtualization/vm-management-cockpit-009.png)

You just have to provide a (descriptive) name and the mount point. After
formatting you will find the volume group mounted and ready to use.

``` bash
[…]\&#35; df -h
Filesystem                          Size  Used Avail Use% Mounted on
\&#8230;
/dev/mapper/fedora_fedora-root       11G  1.8G  9.3G  16% /
tmpfs                               1.5G  4.0K  1.5G   1% /tmp
/dev/vda1                          1014M  187M  828M  19% /boot
/dev/mapper/fedora_user-webservice  8.0G   90M  8.0G   2% /var/www
```

Cockpit handled all the various configuration steps involved on its own.
This saves the system administrator quite a bit of effort. It even
includes creating the mount directory if it does not already exist. At
the end of the day, Cockpit makes it very easy for the system
administrator to implement the elaborate storage concept of Fedora
Server.

If you moved files out of the way at the beginning, you can restore them
now. To be on the safe side, restore the SELinux labels.

``` bash
[…]\&#35; /sbin/restorecon -R -vF /var/www
```

Now is the time to install the appropriate programs. Software provided
by Fedora distribution as rpm installs into the appropriate system
directories via dnf tool. External software should install in either
&#96;/opt&#96; or &#96;/usr/local&#96; to keep it separated from
distribution files to prevent any potential mutual interference. In
accordance with the storage rationale, you should also create a separate
logical volume and mount it under /opt. An example of this would be
Wildfly application server, which stores program, configuration and
possibly data in a common place.

#### Add a virtual disk {#_add_a_virtual_disk}

Expanding the virtual (system) disk is not the only way to provide
additional storage, nor is it necessarily the best way. In the case of
virtual disk images, creating a dedicated virtual disk instead of
creating Logical volumes is a solid, often better alternative. It adds
more flexibility. For example, in case of the \'cold standby\' VM
mentioned above, the system administrator can assign the (virtual) disk
with the entire current dataset to the other VM in less than a minute.

Cockpit supports the creation of additional virtual disks (but
unfortunately not to modify an existing one). On the virtual machine
details page in the section Disks you find an *Add Disk* button. It
opens a form to fill in.

![Cockpit add a virtual disk
form](virtualization/vm-management-cockpit-010.png)

In the example above we create a 30gb disk for Web service. *Add*
creates a disk image in /var/lib/libvirt/images and adds it to the
Cockpit VM details page. You may check in the terminal window using
*lsblk*. It shows a disk vdb without any partition so far.

The Host Cockpit simply creates a new (virtual) hard disk and \'plugs\'
it into the virtual machine. Configuration and setup of the hard disk
occurs within the VM. Their Cockpit can perform that very easily. Open a
new tab in your browser, open Cockpit of the VM and select *Storage*
over there.

![Cockpit additional virtual
disk](virtualization/vm-management-cockpit-015.png)

On the right side you see the newly created disk listed as part of the
(virtual hardware) equipment of the VM. You can work on this disk like
on any other. A click opens a corresponding dialog form.

The system administrator can create a partition table and one or more
partitions, can create a Volume group and Logical Volumes the same way
as described in the previous section. It is also possible to set up and
mount a file system directly without a partition table. Cockpit enables
and supports all these options comfortably and efficiently.

## Manage Libvirt disk pool {#_manage_libvirt_disk_pool}

It is not only the disk images of virtual machines that need to be
adjusted at times. The space on the host for these files can also run
out and require expansion.

A system administrator committed to the Fedora Server storage rationale
has set up a dedicated separate file system for the image pool or
overall for the libvirt directory. On the Storage page of the hosts
Cockpit identify that file system and select it. Enlarge the row using
the triangle icon.

![Cockpit enlarge libvirt
pool](virtualization/vm-management-cockpit-020.png)

In the example above, the system administrator choose to provide a
separate storage for the dedicated libvirt directory tree in
*/dev/usrvg/libvirt*. Selecting &#96;Grow&#96; you get a form where you
have to enter just the desired new size. Cockpit does everything else,
including the adjustment of the file system, completely on its own.

It couldn't be simpler or faster.

## Manage network connectivity {#_manage_network_connectivity}

### Manage libvirt virtual network {#_manage_libvirt_virtual_network}

The current version of Cockpit (255) doesn't offer such many
configuration options for a libvirt managed virtual network so far.
Cockpit lists the existing virtual networks under the \'Network\' link
at the top line by line. Mostly this is only the default network. By
expanding the line, the editing options become visible.

![Cockpit libvirt virtual networks
overview](virtualization/vm-management-cockpit-025.png)

For a production operation the most important one might be to ensure or
to be able to check the start of the network on a reboot of the host.
All other configuration options, in particular e.g. switching NAT on and
off, require the use of \' virsh net-edit default\' on the command line.

Quite interesting is the option to create a new virtual network. It
opens a simple form collecting the most important options

![Cockpit create a libvirt virtual
network](virtualization/vm-management-cockpit-027.png)

The system administrator can select a *Forward mode*, either NAT, Open,
or none (isolated), which can be very convenient. The default *Device*
is automatic, alternatively you can select an existing device. The
automatic option creates a new device virbr&lt;x&gt;. More advanced
configuration such as domain name and name resolution would require
working with CLI tools over here as well.

All in all, a system administrator will be rather reluctant to modify
anything on the network infrastructure frequently, if at all. So nothing
important for daily operation is missing here.

### Manage a virtual machines network connectivity {#_manage_a_virtual_machines_network_connectivity}

Cockpit offers a broader support for the network configuration of
virtual machines. You can add and delete a network interface, but fully
edit its properties as well.

The network options are located at the bottom of the screen of the
respective virtual machine, in most cases outside the viewable pane, and
are easy to overlook.

#### Add an interface {#_add_an_interface}

You may have configured a virtual machine with just a public interface
in order to provide some public service. According to the general
recommendations it uses mac-vlan as an efficient connection type. In the
virtual machines Cockpit GUI it shows up as \'type: direct\' and
\'Source: enp1s0\', the host's physical interface \[1\].

![Cockpit public libvirt virtual
interface](virtualization/vm-management-cockpit-030.png)

After some time you may need to access a service provided by the host,
e.g. a database service. Because the public interface uses mac-vlan, a
direct communication between host and virtual machine is not possible
(due to technical limitations of that type). Additionally, you may want
to protect that communication and its data from the public. The solution
is to add an interface to the virtual machine that connects to the
libvirt internal virtual network, named default and using virbr0.

With Cockpit it is just a click on the \'Add network interface\' link
right of the section title \[2\] and to fill in a simple form.

![Cockpit add internal libvirt virtual
interface](virtualization/vm-management-cockpit-031.png)

In case of an internal interface leave everything as suggested, but just
activate \'*Always attach*\' to make it automatically available after
reboot. Use the button \'Add\' to create the interface.

The interface shows up below the public interface. And inside the
virtual machine a \'*ip a*\' shows and additional connection \'enp7s0\'.
Cockpit sets everything up on its own, no further involvement of the
system administrator required.

#### Modify an interface {#_modify_an_interface}

You may have configured a virtual machine with just an internal
interface, which works perfectly as (the only) interface enp1s0. Now you
need public access instead. The easiest way is to edit the interface
definition in Cockpit.

In the network section of the VMs detail page there is just one
interface with 3 buttons: Delete, Unplug, and Edit. The latter opens a
interface properties form.

![Cockpit edit libvirt virtual
interface](virtualization/vm-management-cockpit-033.png)

The form shows the definition of the current internal network. Just
modify the *Interface type* from \'Virtual network\' to \'Direct
attachement\' and *Source* from \'default\' to \'enp1s0\', the host
physical interface. Save your selection and reboot. Assuming DHCP works,
the virtual machine has a perfectly working connection to the public
network, including name resolution and default firewall configuration.
Otherwise you have to define a static network configuration.

Even if you need a public interface in addition to the existing internal
interface you may prefer to edit the existing interface and later add a
new internal interface. That way you follow the common practice of
always setting up the public interface as the \'first\' one, i.e. enp1s0
or eth0.

#### Delete an interface {#_delete_an_interface}

As an example, the virtual maschine is equipped with two interfaces, a
public (enp1s0) and an internal (enp7s0).

![Cockpit delete a libvirt virtual
interface](virtualization/vm-management-cockpit-034.png)

Probably you don't want a public interface but that machine well
protected from the public network. So you delete the public interface. A
simple click on *Delete* will remove that interface from the virtual
machine (after confirmation). If you check the network configuration
inside the machine an *nmcli device show* lists only one device as
attached to the still existing connection. And *ip a* lists just lo and
enp7s0.

An *nmcli conn show* still lists the connection enp1s0, but without an
attached device. The reason is that it was the first interface
explicitly set up during installation. Therefore it was persisted in
/etc/NetworkManager/system-connected and the file is still there
(allthough without any device configuration options). Cockpit does not
delete a configuration file.

## Simplified Access to VMs Cockpit {#_simplified_access_to_vms_cockpit}

Typically, a (physical) server does host not only one, but several or
even a huge number of VMs. Each VM will have a running Cockpit Web
Interface. To access it, you have to open a Browser window, connect and
login to respective VM you want to work with separately - even if you
only want to do the most minimalist of tasks. It's certainly not
difficult, but it is cumbersome.

For convenience, Cockpit provides the option to access the Cockpit
instance of the VMs from the web interface of one instance, conveniently
the host. The communication between the involved Cockpit instances is
not handled via HTTP protocol but via SSH. Therefore, authentication can
also be done via a key file. This is more secure and also more
convenient.

In the upper left corner you will see the name of the logged in user and
the server, along with an expand icon. This opens a box where you can
switch to another server or add a new one.

![Cockpit select of add a Cockpit
instance](virtualization/vm-management-cockpit-036.png)

The *Add new host* link opens a simple form to fill in hostname and
user. And you can assign a color. If you connect the VM using a direct
public interface (mac-vlan) you can't use that interface because a
direct access from host to vm via mac-vlan is not supported for
technical reasons. You have to use the internal interface (usually
libvirt provided &#96;virbr0&#96;). As a user, you should select the
unprivileged administrative account that can be created during the VM
installation by Anaconda.

Cockpit will then connect and ask for the user's password.

![Cockpit login to remote
instance](virtualization/vm-management-cockpit-038.png)

On this occasion, select automatic login via ssh keyfile. Cockpit will
create one for you if none exists or otherwise uses an existing one
created previously for another Cockpit connection. Cockpit installs the
public key in the VM, too. You don't have to bother with all these
details.

You can also log in as root. However, the default configuration does
block a password-supported root ssh login. You have to generate a
keyfile pair manually in advance and also install the public part in the
VM. You can then select it for a root connection.

## Security Considerations {#_security_considerations}

A Fedora installation makes several efforts to minimize public exposure.
One of these is to prevent password-based root login via public
interface. At the same time, Fedora Server installs by default Cockpit
and opens the firewall accordingly. That way it introduces a
password-based login again, including terminal access. That counteracts
in a way the ssh measure.

It's OK to make the post installation tasks as easy and painless as
possible. But securing Cockpit access has to be one of the post
installation tasks. All the more so as Cockpit is usually not used on a
daily basis, but runs largely unused and unattended in the background.

There are several options.

1.  The easiest way is to close the Cockpit firewall port.

    ``` BatchFile
    […]\&#35; firewall-cmd  --permanent --remove-service=cockpit
    […]\&#35; firewall-cmd  --reload
    ```

    To use Cockpit you have to ssh into the server and temporarily open
    the port.

    ``` BatchFile
    […]\&#35; firewall-cmd   --add-service=cockpit
    ```

2.  Since you log in via ssh anyway, you can also initialize an ssh
    tunnel in pone go and use it for Cockpit if needed. As described
    above you have the Cockpit service from the firewall removed.

    To use Cockpit log into the server and temporarily open the port.

    ``` BatchFile
    […]\&#35; ssh $user@example.com -i $key  -L 9090:example.com:9090
    ```

    You can access the Cockpit interface using
    &#96;[https://localhost:9090&#96](https://localhost:9090&#96); in
    your favorite browser.

3.  You can install Cockpit on your local Fedora workstation or on a lab
    server shielded by a firewall. Configure this instance to access any
    of your Cockpit instances as described in the previous section. Use
    this shielded instance as a proxy to your public servers. As
    described,it uses a protected ssh connection in the public network.
    Of course, you have the Cockpit service removed from the firewall as
    well.

## Concluding remarks {#_concluding_remarks}

The examples here cover only the most common administrative tasks in
virtual machine management. Currently, Cockpit can not completely
replace the terminal window CLI. But the software is regularly updated
and extended. A task that is currently not supported might be included
in the next release. It's worth getting into the habit of briefly
checking Cockpit's support for each new task.

# Setting up Nested Virtualization {#_setting_up_nested_virtualization}

Peter Boy; Christopher Klooz :page-authors: Peter Boy

> This technique uses virtual machines - or more generally
> virtualization techniques - within an (already) virtualized machine.
> In Fedora, this works by default \'out of the box\' and basically
> requires no further configuration - provided that hardware support is
> available. This is true for nearly all Intel Core-i processors
> released in the last decade.

## Introduction {#_introduction_2}

With this technique, you can create a (nested) virtual machine running
on an already virtualized Fedora Server (referred to as Level 1), which
in turn runs on a physical Fedora Server host hypervisor (referred to as
Level 0). The level 1 virtualized Fedora Server acts itself as
hypervisor for a level 2 virtualized Fedora Server (or comparable
virtualization).

Nested virtualization relies on host hardware virtualization extensions
to work. For the Intel architecture, this has been a given for the
Core-i processor family for more than a decade.

However, that does not mean it should be used as a standard
configuration. The technology generates a high processor load and
requires very powerful processors to work flawlessly. With older Intel
processors, it is more suitable for exceptional cases or for testing and
development.

## Checking out the current configuration {#_checking_out_the_current_configuration}

1.  The (physical) host CPU must support nested virtualization.

        […]$ sudo egrep --color 'vmx|svm|ept' /proc/cpuinfo

    The output must include the &#96;vmx&#96; and &#96;ept&#96; flags.
    This is generally the case on Intel Core-i based CPUs.

2.  Ensure that nested virtualization is enabled in the (physical) hosts
    kernel:

        […]$ sudo cat /sys/module/kvm_intel/parameters/nested

    If the command *returns 1 or Y*, the feature is enabled. Continue
    with xref:&#35;\_setting_up_a_vm_for_nested_virtualization\[Setting
    up a VM for nested virtualization\]

    If the command *returns 0 or N* but your system supports nested
    virtualization, continue *here*.

    a.  Execute the following commands to enable the nested
        virtualization feature

            […]$ sudo modprobe -r kvm_intel
            […]$ sudo modprobe kvm_intel nested=1

    b.  Ensure the operation is successfull

            […]$ sudo cat /sys/module/kvm_intel/parameters/nested

    c.  To make the change permanent and cope with a restart, edit

            […]$ sudo vim /etc/modprobe.d/kvm.conf
            options kvm_intel nested=1

## Setting up a VM for nested virtualization {#_setting_up_a_vm_for_nested_virtualization}

1.  If not already done, create a Fedora Server Edition VM you want to
    use with nested virtualization. Follow the steps as described in
    [Creating a virtual machine using Fedora Server Edition disk
    image](virtualization/vm-install-diskimg-fedoraserver.xml).

    Log in to the virtual server that is to host additional virtual
    machines.

2.  Add virtualization support to this virtual Maschine. Follow the
    steps as described in [Adding Virtualization
    Support](virtualization/installation.xml).

3.  Check the installation

        […]$ sudo  virt-host-validate qemu
        QEMU: Checking for hardware virtualization                                 : PASS
        QEMU: Checking if device /dev/kvm exists                                   : PASS
        QEMU: Checking if device /dev/kvm is accessible                            : PASS
        QEMU: Checking if device /dev/vhost-net exists                             : PASS
        QEMU: Checking if device /dev/net/tun exists                               : PASS
        \&#8230;

    There may be 2 warings about IOMMU and secure guest support, which
    you can savely ignore.

4.  Finally, create a Fedora Server Edition VM following the steps as
    described in [Creating a virtual machine using Fedora Server Edition
    disk image](virtualization/vm-install-diskimg-fedoraserver.xml) and
    configure it as needed.

### Optional: Customize the processor configuration {#_optional_customize_the_processor_configuration}

By default, the Prozessor of a virtual machine is a virtualized version
of the host processor type. This way, nested virtualization works, but
possibly with too large performance losses. A remedy may be a changed
kernel configuration, especially a passthrough configuration.

The easiest way is to use the cockpit. Open a Cockpit session to the
host system (l0 host), select Virtual machines and open the virtual host
you want to optimize for nested virtualization, select \'CPU type\'
edit.

![passthrough CPU selectionl](virtualization/nested-cpu-type.png)

Select *host-passthrough* in the *mode* drop down menu and then *Apply*.

:::: caution
::: title
:::

The passthrough mode might resolve a performance issue for nested VMs,
but usually comes with performance penalties in other areas. Be aware
and review the entire system carefully.
::::

This is also the place where you can configure a specific processor for
the VM, if that is required.

## Additional documentations {#_additional_documentations}

RHEL 8 docs: [Chapter 18. Creating nested virtual
machines](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/configuring_and_managing_virtualization/creating-nested-virtual-machines_configuring-and-managing-virtualization&#35;doc-wrapper)

# Installing Fedora Server Edition as a Virtual Machine using Proxmox Virtual Environment {#_installing_fedora_server_edition_as_a_virtual_machine_using_proxmox_virtual_environment}

Paul Maconi :page-authors: Peter Boy, Kevin Fenzi

> This document outlines a method for installing [Fedora Server from the
> qcow2 image](https://fedoraproject.org/server/download) as a virtual
> machine in the Proxmox Virtual Environment, henceforth simply Proxmox.
> VMs can be spun up very quickly after importing the disk image, saving
> much time and frustration. The setup used when writing this document
> may not match what yours, so certain details like file paths for the
> disk images may vary.

## Why Fedora Server on Proxmox {#_why_fedora_server_on_proxmox}

Proxmox is an open source server virtualization management solution
based on QEMU/KVM and LXC with a web interface for managing most aspects
of the VM workflow. It is also popular with homelab enthusiasts. The
Fedora Server disk image shortcuts the provisioning process by providing
a pre-installed disk image that boots straight into the final setup
menu. You can have a fresh Fedora Server VM provisioned in just a couple
of minutes using this method.

## Brief summary for experienced Proxmox users {#_brief_summary_for_experienced_proxmox_users}

Here are the key details if you're already familiar with creating
virtual machines in Proxmox.

&#42; The VM does not need installation media (ISO) mounted. &#42; The
VM must be in BIOS mode (SeaBIOS) with a VirtIO SCSI Single controller.
Be sure to enable the Qemu Agent if you plan on using it. &#42; This
document omits the initial disk creation because we import the disk
image later in the process. &#42;&#42; &#96;qm disk import \[vm_number\]
\[image_name.qcow2\] \[target_storage\] \--format qcow2&#96; &#42; You
must attach the disk and ensure it is selected in the boot order under
&#96;options&#96; for the VM before you try to boot the system.

## Procedure {#_procedure}

Note: This document assumes that you have ssh access to a Proxmox node
and that you have already downloaded the Fedora Server qcow2 disk image.
It also assumes centralized storage on an NFS mount, but your storage
configuration may differ if you use local LVM storage or Ceph. We
provided screenshots for each step of the VM configuration process, but
the overall procedure comes from the [Proxmox
Wiki](https://pve.proxmox.com/wiki/Migrate_to_Proxmox_VE&#35;Import_Disk).

### Locate the image file and upload it to Proxmox {#_locate_the_image_file_and_upload_it_to_proxmox}

Before we create the VM, we will need to find and upload our disk image
to the Proxmox node. In the screenshot below you can see that we
explored the system to determine that it is using centralized NFS
storage mounted at /mnt/pve/nfs-kraken, and we made a directory at some
point called osimages to contain our disk images.

Once you create a directory to house your disk images, you will need to
upload the disk image file via scp into the Proxmox node. &#96;scp
\[image_filename\]
root@\[node_name\]:/path/to/images/\[image_filename\]&#96;

``` shell
aggraxis@whirlwind:~$ cd Desktop/osimages/
aggraxis@whirlwind:~/Desktop/osimages$ ls
Fedora-Server-KVM-41-1.4.x86_64.qcow2
aggraxis@whirlwind:~/Desktop/osimages$ ssh root@pve-m-0
root@pve-m-0's password:
Linux pve-m-0 6.8.12-2-pve \&#35;1 SMP PREEMPT_DYNAMIC PMX 6.8.12-2 (2024-09-05T10:03Z) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/\&#42;/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Sat Nov  9 11:03:50 2024
root@pve-m-0:~\&#35; ls -alh /mnt/pve/nfs-kraken/osimages/
drwxrwxrwx 1 1026 users  462 Nov 11 08:20 .
drwxrwxrwx 1 root root   294 Apr 16  2024 ..
-rwxrwxrwx 1 1026 users 1.6G Apr 20  2024 fedora-coreos-39.20240322.3.1-qemu.x86_64.qcow2
-rwxrwxrwx 1 1026 users 1.6G May  9  2024 fedora-coreos-40.20240416.3.1-qemu.x86_64.qcow2
-rwxrwxrwx 1 1026 users 574M Apr 16  2024 Fedora-Server-KVM-39-1.5.x86_64.qcow2
-rwxrwxrwx 1 1026 users 629M Apr 24  2024 Fedora-Server-KVM-40-1.14.x86_64.qcow2
-rwxrwxrwx 1 1027 users 913M Aug 30 13:44 rhel-9.4-x86_64-kvm.qcow2
root@pve-m-0:~\&#35; exit
logout
Connection to pve-m-0 closed.
aggraxis@whirlwind:~/Desktop/osimages$ scp Fedora-Server-KVM-41-1.4.x86_64.qcow2 \
root@pve-m-0:/mnt/pve/nfs-kraken/osimages/Fedora-Server-KVM-41-1.4.x86_64.qcow2
root@pve-m-0's password:
Fedora-Server-KVM-41-1.4.x86_64.qcow2          100%  659MB 110.7MB/s   00:05
aggraxis@whirlwind:~/Desktop/osimages$
```

### Verify the image is in place {#_verify_the_image_is_in_place}

While not completely necessary, we logged back in to the Proxmox node
and verified that the file had actually uploaded to the target
directory. We'll come back to this path later when it is time to import
the disk image to a VM.

``` shell
aggraxis@whirlwind:~/Desktop/osimages$ ssh root@pve-m-0
root@pve-m-0's password:
Linux pve-m-0 6.8.12-2-pve \&#35;1 SMP PREEMPT_DYNAMIC PMX 6.8.12-2 (2024-09-05T10:03Z) x86_64

The programs included with the Debian GNU/Linux system are free software;
the exact distribution terms for each program are described in the
individual files in /usr/share/doc/\&#42;/copyright.

Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
permitted by applicable law.
Last login: Mon Nov 11 08:18:31 2024 from 192.168.218.217
root@pve-m-0:~\&#35; ls -alh /mnt/pve/nfs-kraken/osimages/
total 5.8G
drwxrwxrwx 1 1026 users  462 Nov 11 08:20 .
drwxrwxrwx 1 root root   294 Apr 16  2024 ..
-rwxrwxrwx 1 1026 users 1.6G Apr 20  2024 fedora-coreos-39.20240322.3.1-qemu.x86_64.qcow2
-rwxrwxrwx 1 1026 users 1.6G May  9  2024 fedora-coreos-40.20240416.3.1-qemu.x86_64.qcow2
-rwxrwxrwx 1 1026 users 574M Apr 16  2024 Fedora-Server-KVM-39-1.5.x86_64.qcow2
-rwxrwxrwx 1 1026 users 629M Apr 24  2024 Fedora-Server-KVM-40-1.14.x86_64.qcow2
-rwxrwxrwx 1 1024 users 660M Nov 11 08:20 Fedora-Server-KVM-41-1.4.x86_64.qcow2
-rwxrwxrwx 1 1027 users 913M Aug 30 13:44 rhel-9.4-x86_64-kvm.qcow2
root@pve-m-0:~\&#35;
```

### VM Creation: General {#_vm_creation_general}

Click on the &#96;Create VM&#96; button in the Proxmox UI, and the VM
creation wizard should start. Select a node and give the VM a name. Note
the VM ID. We will need this later. Click &#96;Next&#96;.

![VM General](virtualization/vm-proxmox-03.png)

### VM Creation: OS {#_vm_creation_os}

We will not need to use an ISO to install the system, so change the
radio button to &#96;Do not use any media&#96; and click &#96;Next&#96;.

![VM OS](virtualization/vm-proxmox-04.png)

### VM Creation: System {#_vm_creation_system}

We get a handful of options to play with on this screen.

&#42; The &#96;Machine&#96; is whatever you prefer. &#96;q35&#96;
presents hardware in the PCIe topology, while &#96;i440fx&#96; will give
you the older PCI topology.

&#42; The &#96;BIOS&#96; option needs to be &#96;SeaBIOS&#96; because
the disk image will not boot under &#96;UEFI&#96;.

&#42; The &#96;SCSI Controller&#96; option should be set as &#96;VirtIO
SCSI Single&#96;. The default option &#96;LSI 53C895A&#96; would not
boot the disk image.

&#42; Also, remember to enable the &#96;Qemu Agent&#96; option if you
intend to use it. You can safely enable this option if you are unsure.

Click &#96;Next&#96;.

![VM System](virtualization/vm-proxmox-05.png)

### VM Creation: Disks {#_vm_creation_disks}

Click the little trash can to the left of the disk it pre-populates for
you. We will be importing the disk image as our primary disk. Click
&#96;Next&#96;.

![VM Disks](virtualization/vm-proxmox-06.png)

### VM Creation: CPU {#_vm_creation_cpu}

Set the CPU settings as you need them. The test cluster used when
writing this documentation had identical processors across the cluster,
so &#96;host&#96; was safe to use while still enabling live migration.
Click &#96;Next&#96;.

![VM CPU](virtualization/vm-proxmox-07.png)

### VM Creation: Memory {#_vm_creation_memory}

Set the memory the amount you want assigned to the VM. Click
&#96;Next&#96;.

![VM Memory](virtualization/vm-proxmox-08.png)

### VM Creation: Network {#_vm_creation_network}

Select the network details. The test article had an Open vSwitch
configured with VLAN port groups. &#96;VirtIO (paravirtualized)&#96;
should yield the best performance. Click &#96;Next&#96;.

![VM Network](virtualization/vm-proxmox-09.png)

### VM Creation: Confirm {#_vm_creation_confirm}

The wizard should end with a summary of the hardware settings. Click
&#96;Finish&#96; to create the VM.

![VM Confirm](virtualization/vm-proxmox-10.png)

### VM Disk Import {#_vm_disk_import}

Now that the VM itself has been built, we need to log in to the Proxmox
node via the console feature or via SSH to import the disk image we
uploaded earlier.

&#42; Log in to the Proxmox node

&#42; Navigate to the directory where you uploaded the disk image
earlier.

&#42;&#42; This test article has storage mounted at
/mnt/pve/nfs-kraken/osimages/, but your path will be different.

&#42; Use the qm disk import command to import your disk image.

&#42;&#42; &#96;qm disk import \[vm_number\] \[image_name.qcow2\]
\[target_storage\] \--format qcow2&#96;

&#42;&#42;&#42; \[vm_number\] is the vm number of the vm you just
created in the previous steps.

&#42;&#42;&#42; \[image_name.qcow2\] is the file name of your Fedora
Server image that you uploaded earlier.

&#42;&#42;&#42; \[target_storage\] is the storage volume where you want
the disk image for the vm stored. For this test article, I told Proxmox
to continue using a volume named &#96;nfs-kraken&#96;.

&#42;&#42;&#42; The format may vary depending on where you are storing
the VM. The test articule uses an NFS mount, and qcow2 formatted images
are preferred in this usage scenario.

``` shell
root@pve-m-0:~\&#35; cd /mnt/pve/nfs-kraken/osimages/
root@pve-m-0:/mnt/pve/nfs-kraken/osimages\&#35; qm disk import 106 \
Fedora-Server-KVM-41-1.4.x86_64.qcow2 nfs-kraken --format qcow2
importing disk 'Fedora-Server-KVM-41-1.4.x86_64.qcow2' to VM 106 \&#8230;
Formatting '/mnt/pve/nfs-kraken/images/106/vm-106-disk-1.qcow2',
fmt=qcow2 cluster_size=65536 extended_l2=off preallocation=metadata
compression_type=zlib size=7516192768 lazy_refcounts=off
refcount_bits=16
transferred 0.0 B of 7.0 GiB (0.00%)
transferred 76.7 MiB of 7.0 GiB (1.07%)
transferred 148.4 MiB of 7.0 GiB (2.07%)
--SNIP--
transferred 7.0 GiB of 7.0 GiB (99.33%)
transferred 7.0 GiB of 7.0 GiB (100.00%)
transferred 7.0 GiB of 7.0 GiB (100.00%)
Successfully imported disk as 'unused0:nfs-kraken:106/vm-106-disk-1.qcow2'
root@pve-m-0:/mnt/pve/nfs-kraken/osimages\&#35;
```

When the import process finishes you should get a success message like
the one shown above. This process was done on a storage array with
rotational hard disks, and it still only took a few seconds to complete.

### VM Configuration: Disk {#_vm_configuration_disk}

Now that the disk is part of the VM, we can go back to the hardware tab,
highlight the new unused disk, and click edit. You shouldn't need to
change anything and can safely just click &#96;Add&#96;.

![VM Configuration: Disk](virtualization/vm-proxmox-13.png)

### VM Configuration: Boot Order {#_vm_configuration_boot_order}

The final step before powering on the VM is to navigate to the VM's
&#96;Options&#96; tab, click on &#96;Boot Order&#96;, and ensure that
the imported disk, typically &#96;scsi0&#96;, is selected for boot. Note
that in the following screenshot, the other boot options are disabled
and &#96;scsi0&#96; is moved to the top of the list.

![VM Configuration: Boot Order](virtualization/vm-proxmox-14.png)

### VM Console: First Boot {#_vm_console_first_boot}

Now we're ready open up the console and boot the VM for the first time.
You should see the normal GRUB boot loader and kernel messages stream
across the console until you are presented with the final setup menu.

![VM Console: First Boot](virtualization/vm-proxmox-15.png)

### End Result {#_end_result}

After you complete this process the VM is running just as if you had
booted off of the ISO and went through the full server install process,
only now it only takes a fraction of the time!

### Next Steps {#_next_steps}

Be sure to check out the tasks in the general [post-installation
guide](installation/postinstallation-tasks.xml) for virtual machines as
well.

# Containerization {#_containerization}

Peter Boy :page-authors: Peter Boy :page-aliases:
container-an-introduction.adoc

Since some years \'Container\' are on everyone's lips. It's a prominent
subject of public dicsussion. Complete operating systems are rebuilt to
serve primarily as runtime environments for containers. And in public
discussion \'container\' are mostly equated with \'Docker\'. It is hard
to find software that is not at least also offered as a Docker image.
And it didn't take long for the disadvantages of such a monopolization
to become apparent, e.g. in the form of serious security risks.

As we learn time and time again, one size does not fit all. A number of
the advantages of containerization are widely agreed upon. But the needs
and requirements in IT are so diverse that not all of them can be
optimally realized by one implementation. Therefore, there are
alternative container implementations with different application
profiles. And containerization is not always helpful either.

&#42;Fedora Server supports and allows several alternatives that can be
used depending on the local context and/or user's requirement
profile.&#42;

## Containerization options in Fedora Server {#_containerization_options_in_fedora_server}

A common feature of all container systems is the sharing of the host
kernel and the use of kernel capabilities (e.g. cnames) to achieve a
certain mutual isolation and autonomy.

They differ in implementation, architecture principles, toolset, runtime
environment and community. A rough classification is the distinction
between \'system container\' and \'application container\', roughly
determined by the existence and scope of an init system.

### Podman {#_podman}

Its characteristics are

&#42; Application container &#42; Security enhancement: no root
privileges and no central controlling daemon required &#42; Optimized
for the interaction of multiple, coordinated containers (a \'pod\'),
each dedicated to a specific task and cooperating with others to
accomplish a complex overall task (e.g. customer management with
connection to a specific database system). Reinforces the architecture
principle: one and only one application per container. &#42; Binary
compatible container image as Docker, mutually usable &#42; Free open
source software

Podman is &#42;natively supported by Fedora Server&#42; and the
recommended solution for application containers.

### Docker {#_docker}

Its characteristics are

&#42; Application container &#42; Dependent on a daemon with ROOT
privileges &#42; Huge trove of pre-built containers for all sorts of
software &#42; Mixture of a free community edition and a commercial
product

Docker releases it own Community Edition for various distributions.
Therefore there is &#42;no native support&#42; for Fedora Server, but a
&#42;vendor repository&#42; maintained for Fedora.

### LXC (libvirt) {#_lxc_libvirt}

Its characteristics are

&#42; System container, kind of \'lightweight virtual machine\' &#42;
Administration of container runtimes supported by Libvirt management
routines for virtual machines as well as by Cockpit libvirt module &#42;
Container runtime solely dependent on kernel capabilities, no own
toolset &#42; Creation of a container disk image is not considered a
task of libvirt, but a matter for the administrator. It includes
composing a xml-based descriptor file. Therefore, the toolset is rated
as somewhat \'rough\'. &#42; Free open source software

Libvirt LXC is &#42;natively supported by Fedora Server&#42; (via
libvirt as default virtualization tool)

### LXC (linux containers) {#_lxc_linux_containers}

Its characteristics are

&#42; System container &#42; One of the first implementations of
containers and the \'progenitor\' of (meanwhile emancipated) Docker and
Podman &#42; Complete toolset, container images, community. Its
designated successor is LXD (see next). &#42; Free open source software

Linux Container's LXC is &#42;natively supported by Fedora Server&#42;
(in its LTS versions)

### LXD (linux containers) {#_lxd_linux_containers}

Its characteristics are

&#42; System container, kind of \'lightweight virtual machine\' &#42;
LXC with advanced toolset &#42; Complete versatile toolset, including
container images and active supportive community. &#42; Free open source
software

LXD is &#42;not natively supported&#42; by Fedora Server, but there is a
&#42;COPR project&#42; available, Additionally there is &#42;vendor
support&#42; for Fedora by a third party package manager.

### systemd-nspawn container {#_systemd_nspawn_container}

Its characteristics are

&#42; System container as a \'lightweight virtual machine\' and also
configurable as a kind of application container (with a stub init
system) &#42; Toolset highly integrated into systemd system management
and thus a strong simplification of administration and maintenance.
&#42; Both technically stringent and systematic documentation as well as
stringent naming and structuring of the toolset, which facilitates
administration. &#42; Rather new development and currently still
somewhat rough SELinux support (so far its weakest point). &#42; Free
open source software

The systemd-nspawn container is &#42;natively supported by Fedora
Server&#42;.

### Linux Vserver {#_linux_vserver}

It requires a modified kernel and is &#42;not supported by Fedora
Server&#42;

### OpenVZ {#_openvz}

It uses a self customized version of RHEL / CentOS and is &#42;not
supported by Fedora Server&#42;

# Setting up Systemd Nspawn Container {#_setting_up_systemd_nspawn_container}

Peter Boy; Jan Kuparinen :page-authors: Peter Boy, Kevin Fenzi
:page-aliases: container-nspawn-install.adoc

The systemd-nspawn container runtime is part of the systemd system
software. It has been offloaded into its own package, systemd-container,
a while ago.

The prerequisite is a fully installed basic system. A standard interface
of the host to the public network is assumed, via which the container
receives independent access (own IP). In addition an interface for an
internal, protected net between containers and host is assumed, usually
a bridge. It may be a virtual network within the host, e.g. libvirts
virbr0, or a physical interface connecting multiple hosts.

But of course a container can also be operated with other variations of
a network connection or even without a network connection at all.

## 1. Setting up the nspawn container infrastructure {#_1_setting_up_the_nspawn_container_infrastructure}

1.  &#42;Create a container storage area&#42;

    The systemd-nspawn tools like machinctl look for containers in
    &#96;/var/lib/machines&#96; first. This directory is also created
    during the installation of the programs if it does not exist.

    Following the Fedora server storage scheme, create a logical volume,
    create a file system and mount it to &#96;/var/lib/machines&#96;.
    The tools can use BTRFS properties, so this can be used as a
    filesystem in this case. If you don't want to follow the Fedora
    Server rationale, skip this step.

        […]\&#35; dnf install btrfs-progs
        […]\&#35; lvcreate -L 20G -n machines  {VGNAME}
        […]\&#35; mkfs.btrfs -L machines /dev/mapper/{VGNAME}-machines
        […]\&#35; mkdir /var/lib/machines
        […]\&#35; vim /etc/fstab
        (insert)
        /dev/mapper/{VGNAME}-machines   /var/lib/machines  auto  0 0

        […]\&#35; mount -a

2.  &#42;Check and, if necessary, correct the SELinux labels&#42;

    Ensure that the directory belongs to root and can only be accessed
    by root (should be done by the installer).

        […]\&#35; restorecon  -vFr /var/lib/machines
        […]\&#35; chown root:root /var/lib/machines
        […]\&#35; chmod 700 /var/lib/machines

3.  &#42;Adding configuration for nspawn to the &#96;etc/systemd&#96;
    directory&#42;

        […]\&#35; mkdir /etc/systemd/nspawn

## 2. Creating a nspawn container {#_2_creating_a_nspawn_container}

### 2.1 Creating a container directory tree {#_2_1_creating_a_container_directory_tree}

The creation of a container filesystem or the provision of a
corresponding image is treated as \'out of scope\' by systemd-nspawn.
There are a number of alternative options. By far the easiest and most
efficient way is simply to use the distribution specific bootstrap tool,
DNF in case of fedora, in the container's directory. This is the
recommended procedure.

1.  Creating a BTRFS subvolume with the name of the container

        […]\&#35; cd /var/lib/machines
        […]\&#35; btrfs subvolume create {ctname}

2.  Creating a minimal container directory tree

    &#42;&#42;*Fedora 34 / 35*&#42;&#42;

        […]\&#35; dnf --releasever=35 --best --setopt=install_weak_deps=False --installroot=/var/lib/machines/{CTNAME}/ \
        install dhcp-client dnf fedora-release glibc glibc-langpack-en glibc-langpack-de iputils less ncurses passwd systemd systemd-networkd systemd-resolved vim-default-editor

    F34 installs 165 packages (247M) and allocates 557M in the file
    system. F35 installs 174 packages (270M) and allocates 527M in the
    file system.

    &#42;&#42;*Fedora 36*&#42;&#42;

        […]\&#35; dnf --releasever=36 --best --setopt=install_weak_deps=False --installroot=/var/lib/machines/{CTNAME}/ \
        install dhcp-client dnf fedora-release glibc glibc-langpack-en glibc-langpack-de iputils less ncurses passwd systemd systemd-networkd systemd-resolved util-linux vim-default-editor

    F36 installs 171 packages (247M) and allocates 550M in the file
    system.

    &#42;&#42;*CentOS 8-stream*&#42;&#42;

    First create a separate CentOS repository file (e.g.
    /root/centos.repo) and import CentOS keys.On this basis, perform a
    standard installation using DNF.

        […]\&#35; vim  /root/centos8.repo
        \&lt;insert\&gt;
        [centos8-chroot-base]
        name=CentOS-8-Base
        baseurl=http://mirror.centos.org/centos/8/BaseOS/x86_64/os/
        gpgcheck=1
        gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-centosofficial
        \&#35;
        [centos8-chroot-appstream]
        name=CentOS-8-stream-AppStream
        \&#35;baseurl=http://mirror.centos.org/$contentdir/$stream/AppStream/$basearch/os/
        baseurl=http://mirror.centos.org/centos/8-stream/AppStream/x86_64/os/
        gpgcheck=1
        gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-centosofficial
        \&#35;
        [epel8-chroot]
        name=Epel-8
        baseurl=https://ftp.halifax.rwth-aachen.de/fedora-epel/8/Everything/x86_64/
        gpgcheck=1
        gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-8

        […]\&#35; dnf install http://mirror.centos.org/centos/8-stream/BaseOS/x86_64/os/Packages/centos-gpg-keys-8-2.el8.noarch.rpm

        […]\&#35; rpm -Uvh --nodeps https:/dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm

        […]\&#35; dnf -c /root/centos8.repo --releasever=8-stream --best  --disablerepo=\&#42;    --setopt=install_weak_deps=False --enablerepo=centos8-chroot-base --enablerepo=centos8-chroot-appstream --enablerepo=epel8-chroot --installroot=/var/lib/machines/{CTNAME}  install  centos-release dhcp-client dnf glibc-langpack-en glibc-langpack-de  iproute iputils less passwd systemd  systemd-networkd  vim-enhanced

    This installs 165 packages that occupy 435 M in the file system. The
    message: &#96;install-info: File or directory not found for
    /dev/null&#96; appears several times. The cause is that the
    &#96;/dev/&#96; file system is not yet initialized at this point.
    You may savely ignore the message.

### 2.2 Configuration and commissioning of a system container {#_2_2_configuration_and_commissioning_of_a_system_container}

1.  Setting the password for root

    This requires temporarily setting SELinux to permissive, otherwise
    passwd will not make any changes.

        […]\&#35; setenforce 0
        […]\&#35; systemd-nspawn -D /var/lib/machines/{ctname}   passwd
        […]\&#35; setenforce 1

2.  Provision of network interfaces for the container within the host

    If only a connection to an internal, protected network is needed
    (replace the host bridge interface name accordingly):

        […]\&#35; vim /etc/systemd/nspawn/{ctname}.nspawn
        (insert)
        [Network]
        Bridge=vbr6s0

    If a connection to the external, public network is also required,
    two corresponding interfaces must be provided, whereby a mac-vlan is
    used on the interface of the host for the external connection
    (again, replace the host interface names accordingly).

        […]\&#35; vim /etc/systemd/nspawn/{ctname}.nspawn
        (insert)
        [Network]
        MACVLAN=enp4s0
        Bridge=vbr6s0

3.  Configuration of the connection to the internal network within the
    container

        […]\&#35; vim /var/lib/machines/{ctname}/etc/systemd/network/20-host0.network
        (insert)
        \&#35; {ctname}.localnet
        \&#35; internal network interface via bridge
        \&#35; static configuration, no dhcp defined
        [Match]
        Name=host0\&#42;

        [Network]
        DHCP=no
        Address=10.10.10.yy/24
        \&#35;Gateway=10.10.10.10

        LinkLocalAddressing=no
        IPv6AcceptRA=no

    If the internal network is also to be used for external access via
    NAT, the gateway entry must be commented in. Otherwise do not!

4.  Optionally, configure an additional connection to the public network
    via Mac Vlan

    In this case, the gateway entry *must* be commented *out* in the
    configuration of the internal network, as mentioned in item 3.

        […]\&#35; vim /var/lib/machinec/{ctname}/etc/systemd/network/10-mv.network
        (insert)
        \&#35; {ctname}.sowi.uni-bremen.de
        \&#35; public interface via mac-vlan
        \&#35; static configuration, no dhcp available
        [Match]
        Name=mv-enp\&#42;

        [Link]
        ARP=True

        [Network]
        DHCP=no

        \&#35; IPv4 static configuration, no DHCP configured!
        Address=134.102.3.zz/27
        Gateway=134.102.3.30
        \&#35; without Destination specification
        \&#35; treated as default!
        \&#35;Destination=

        \&#35; IPv6 static configuration
        Address=2001:638:708:f010::zzz/64
        IPv6AcceptRA=True
        Gateway=2001:638:708:f010::1
        \&#35; in case of issues possible workaround
        \&#35; cf https://github.com/systemd/systemd/issues/1850
        \&#35;GatewayOnlink=yes

        [IPv6AcceptRA]
        UseOnLinkPrefix=False
        UseAutonomousPrefix=False

    Don't forget to adjust interface names and IP addresses accordingly!

5.  Boot the container and log in

    Check if container boots without error messages

        […]\&#35; systemd-nspawn -D /var/lib/machines/{ctname}  -b
        OK Spawning container {ctname} on /var/l…01.
        OK …
        {ctname} login:

6.  Checking the status of systemd-networkd

    If inactive, activate and start the service.

        […]\&#35; systemctl  status  systemd-networkd
        …
        […]\&#35; systemctl  enable  systemd-networkd
        […]\&#35; systemctl  start   systemd-networkd
        […]\&#35; systemctl  status  systemd-networkd

7.  Check if all network interfaces are available

        […]\&#35; ip a

8.  Check for correct routing

        […]\&#35; ip route show

9.  Configure default DNS search path

    Specify a search domain to appended to a unary hostname without
    domain part, usually the internal network domain name, e.g.
    example.lan. Adjust the config file according to the pattern below:

        […]\&#35; vim /etc/systemd/resolved.conf

        [Resolve]
        \&#8230;
        \&#35;dns.quad9.net
        \&#35;DNS=
        \&#35;FallbackDNS=
        \&#35;Domains=
        Domains=example.lan
        \&#35;DNSSEC=no
        \&#8230;

10. Check if name resolution is configured correctly

        […]\&#35; ls  -al  /etc/resolv.conf
        lrwxrwxrwx. 1 root root 39 29. Dez 12:15 /etc/resolv.conf -\&gt; ../run/systemd/resolve/stub-resolv.conf

    If the file is missing or is a text file, correct it.

        […]\&#35; cd  /etc
        […]\&#35; rm  -f  resolv.conf
        […]\&#35; ln  -s  ../run/systemd/resolve/stub-resolv.conf  resolv.conf
        […]\&#35; ls  -al  /etc/resolv.conf
        […]\&#35; cd

    Ensure that systemd-resolved service is enabled.

        […]\&#35; systemctl status systemd-resolved

    Activate the service if necessary.

        […]\&#35; systemctl enable systemd-resolved

11. Set the intended hostname

        […]\&#35; hostnamectl
        […]\&#35; hostnamectl set-hostname \&lt;FQDN\&gt;

12. Terminate the container

        […]\&#35;_\&lt;CTRL\&gt;+]]]
        Container \&lt;CTNAME\&gt; terminated by signal KILL.

### 2.2 Configuration and commissioning of an application container {#_2_2_configuration_and_commissioning_of_an_application_container}

1.  Setting the password for root

    This requires temporarily setting SELinux to permissive, otherwise
    passwd will not make any changes.

        […]\&#35; setenforce 0
        […]\&#35; systemd-nspawn -D /var/lib/machines/{ctname}   passwd
        […]\&#35; setenforce 1

2.  Configuration of container properties

    Specifying private user configuration and shared network access.

        […]\&#35; vim /etc/systemd/nspawn/{ctname}.nspawn
        (insert)
        [Exec]
        PrivateUsers=false
        [Network]
        Private=off
        VirtualEthernet=false

3.  Boot the container and log in

    Check if container boots without error messages

        […]\&#35; systemd-nspawn -b -D /var/lib/machines/{ctname}
        OK Spawning container {ctname} on /var/l…01.
        OK …
        {ctname} login:

4.  Checking the status of systemd-networkd

    If active, deactivate the service.

        […]\&#35; systemctl  status  systemd-networkd
        …
        […]\&#35; systemctl  disable  systemd-networkd
        […]\&#35; systemctl  stop   systemd-networkd
        […]\&#35; systemctl  status  systemd-networkd
        […]\&#35; systemctl  status  systemd-resolved
        …
        […]\&#35; systemctl  disable  systemd-resolved
        […]\&#35; systemctl  stop   systemd-resolved
        […]\&#35; systemctl  status  systemd-resolved

    If file /etc/resolv.conf is a link, remove it.

        […]\&#35; rm /etc/resolv.conf

    Create (or edit an existing) file /etc/resolv.conf

        […]\&#35; vim /etc/resolv.conf

        nameserver 127.0.0.53
        options edns0 trust-ad
        search \&lt;YOUR_DOMAIN\&gt;

5.  Check if all network interfaces are available

        […]\&#35; ip a

    You should see the same interfaces and IP addresses as on the host
    system.

6.  Check if name resolution is working correctly

        […]\&#35; ping spiegel.de
        PING spiegel.de (128.65.210.8) 56(84) bytes of data.
        64 bytes from 128.65.210.8 (128.65.210.8): icmp_seq=1 ttl=59 time=19.8 ms
        \&#8230;

7.  Set the intended hostname

        […]\&#35; hostnamectl
        […]\&#35; hostnamectl set-hostname \&lt;FQDN\&gt;

8.  Terminate the container

        […]\&#35;_\&lt;CTRL\&gt;+]]]
        Container \&lt;CTNAME\&gt; terminated by signal KILL.

## 3. Starting the container as a system service for productive operation {#_3_starting_the_container_as_a_system_service_for_productive_operation}

1.  Booting the container using systemctl

    In this step, a separate UID/GID range is automatically created for
    the container.

        […]\&#35; systemctl  enable systemd-nspawn@{ctname}
        […]\&#35; systemctl  start  systemd-nspawn@{ctname}
        […]\&#35; systemctl  status systemd-nspawn@{ctname}

    On first boot after installing systemd-container, a SELinux bug
    currently (Fedora 34/35) blocks execution. The solution is to fix
    the SELinux label(s).

    &#42; Select the SELinux tab in Cockpit, preferably before booting
    the container for the first time. &#42; There, the AVCs are listed
    and solutions are offered, such as:

    &#96;type=AVC msg=audit(1602592088.91:50075): avc: denied { search }
    for pid=35673 comm=\'systemd-machine\' name=\'48865\' dev=\'proc\'
    ino=1070782 scontext=system_u:system_r:systemd_machined_t:s0
    tcontext=system_u:system_r:unconfined_service_t:s0 tclass=dir
    permissive=0&#96;

    The proposed solution is roughly as follows:

        […]\&#35; ausearch -c 'systemd-machine' --raw | audit2allow -M my-systemdmachine
        […]\&#35; semodule -i my-systemdmachine.pp

    &#42; The operation must be repeated until no SELinux error is
    reported and the container starts as a service.

    Alternatively, the SELinux CLI tool can be used, which also suggests
    these solutions.

2.  Enable automatic start of the container at system startup

        […]\&#35; systemctl enable systemd-nspawn@{ctname}
        […]\&#35; systemctl status systemd-nspawn@{ctname}

3.  Log in to the container

        […]\&#35; setenforce 0
        […]\&#35; machinectl  login  {ctname}

    When machinectl is called with parameters for the first time, an
    SELinux bug (Fedora 34/35) also blocks execution. The correction is
    done in the same way as for the container start.

4.  Completing and finalizing the container configuration

    Within the container, perform other designated software
    installations and customizations.

    In case of a CentOS 8-stream container, the epel repository should
    be installed (dnf install epel-release-latest-8) so that
    systemd-networkd is provided with updates.

5.  Logging off from the container

    After finishing all further work inside the container press
    &lt;ctrl&gt;\]\]\] ( Mac: &lt;ctrl&gt;&lt;alt&gt;666) to exit the
    container and reactivate SELinux.

        […]\&#35; setenforce 1

### 3.1 Autostart of the container on reboot of the host {#_3_1_autostart_of_the_container_on_reboot_of_the_host}

An autostart of the container in the \'enabled\' state fails on Fedora
35 and older. The cause can be seen in a status query after rebooting
the host, which issues an error message according to the following
example:

    […]\&#35; systemctl status systemd-nspawn@CT_NAME
    systemd-nspawn[802]: Failed to add interface vb-{CT_NAME} to bridge vbr6s0: No such device

This means that systemd starts the container before all required network
interfaces are available.

#### Resolution for (physical) interfaces managed by NetworkManager {#_resolution_for_physical_interfaces_managed_by_networkmanager}

1.  The service file requires an amendment (Bug &#35;2001631). In
    section \[Unit\], for the &#96;Wants=&#96; and &#96;After=&#96;
    configurations, add a target &#96;network-online.target&#96; at the
    end of each line. The file must then look like this (ignore the
    commented out marker rows):

        […]\&#35; systemctl  edit systemd-nspawn@  --full
        \&#8230;
        [Unit]
        Description=Container %i
        Documentation=man:systemd-nspawn(1)
        Wants=modprobe@tun.service modprobe@loop.service modprobe@dm-mod.service network-online.target
        \&#35;\&#35;\&#35;                                                                      ^^^^^^^^^^^^^^^^^^^^^
        PartOf=machines.target
        Before=machines.target
        After=network.target systemd-resolved.service modprobe@tun.service  modprobe@loop.service  modprobe@dm-mod.service network-online.target
        \&#35;\&#35;\&#35;                                                                                                                ^^^^^^^^^^^^^^^^^^^^^
        RequiresMountsFor=/var/lib/machines/%i
        \&#8230;

    Important is the character \'@\' after &#96;nspawn&#96;! In the
    opening editor make the insertions and save them.

2.  Then execute

        […]\&#35; systemctl daemon-reload

At the next reboot the containers will be started automatically.

#### Resolution for virtual interfaces managed by libvirt {#_resolution_for_virtual_interfaces_managed_by_libvirt}

For such interfaces (usually the bridge virbr0) the addition mentioned
above does not help. The container must be started by script in an extra
step after Libvirt initialization is complete. For this you can use a
hook that Libvirt provides.

    […]\&#35; mkdir -p /etc/libvirt/hooks/network.d/
    […]\&#35; vim /etc/libvirt/hooks/network.d/50-start-nspawn-container.sh
    (INSERT)
    \&#35;!/bin/bash
    \&#35; Check defined nspawn container in /var/lib/machines and
    \&#35; start every container that is enabled.
    \&#35; The network-online.target in systemd-nspawn@ service file
    \&#35; does not (yet) wait for libvirt managed interfaces.
    \&#35; We need to start it decidely when the libvirt bridge is ready.

    \&#35; $1 : network name, eg. Default
    \&#35; $2 : one of 'start' | 'started' | 'port-created'
    \&#35; $3 : always 'begin'
    \&#35; see  https://libvirt.org/hooks.html

    set -o nounset

    network='$1'
    operation='$2'
    suboperation='$3'

    ctdir='/var/lib/machines/'
    ctstartlog='/var/log/nspawn-ct-startup.log'

    echo ' P1: $1 - P2: $2 - P3: $3   @  $(date)  '
    echo '     '                                    \&gt;  $ctstartlog
    echo '======================================='  \&gt;\&gt;  $ctstartlog
    echo ' Begin  $(date)  '                        \&gt;\&gt;  $ctstartlog
    echo ' P1: $1 - P2: $2 - P3: $3 '               \&gt;\&gt; $ctstartlog

    if [ '$network' == 'default' ]; then
    if [ '$operation' == 'started' ] \&amp;\&amp; [ '$suboperation' == 'begin' ]; then
    for file in  $ctdir/\&#42; ; do
    echo 'Checking: $file '  \&gt;\&gt; $ctstartlog
    echo ' Filename: $(basename  $file)  '   \&gt;\&gt; $ctstartlog
    echo ' Status: $(systemctl is-enabled systemd-nspawn@$(basename $file) ) '  \&gt;\&gt; $ctstartlog

    if [ '$(systemctl is-enabled systemd-nspawn@$(basename $file) )' == 'enabled' ]; then
    echo ' Starting Container $(basename  $file) \&#8230;  '  \&gt;\&gt; $ctstartlog
    systemctl  start  systemd-nspawn@$(basename $file)
    echo 'Container $(basename  $file) started'  \&gt;\&gt; $ctstartlog
    fi
    done
    fi
    fi

    […]\&#35; chmod +x /etc/libvirt/hooks/network.d/50-start-nspawn-container.sh

You may also use the [attached
script]({attachmentsdir}/nspawn-autostart-libvirt-hook.tgz) instead of
typing.

## 4. Troubleshooting {#_4_troubleshooting}

### 4.1 RPM DB problem in a CentOS 8-stream container on Fedora host {#_4_1_rpm_db_problem_in_a_centos_8_stream_container_on_fedora_host}

For dnf / rpm queries the error message is displayed: &#96;warning:
Found SQLITE rpmdb.sqlite database while attempting bdb backend: using
sqlite backend&#96;

The cause is that Fedora's dfn, which is used for the installation, uses
sqlite while CentOS/RHEL use the Berkeley (bdb) format.

Check configuration within the running container:

    […]\&#35; rpm -E '%{_db_backend}'

The output must be &#96;bdb&#96;. Then fix it executing

    […]\&#35; rpmdb  --rebuilddb

### 4.2 Error message dev-hugepages {#_4_2_error_message_dev_hugepages}

You will find message such as

    dev-hugepages.mount: Mount process exited, code=exited, status=32/n/a
    dev-hugepages.mount: Failed with result 'exit-code'.
    [FAILED] Failed to mount Huge Pages File System.
    See 'systemctl status dev-hugepages.mount' for details.

DFN installs this by default, but it is not applicable inside a
container. It is a general kernel configuration that cannot be changed
by a container (at least as long as it is not configurable within
namespaces).

The messages can be safely ignored.

### 4.3 Package update may fail {#_4_3_package_update_may_fail}

Some packages, e.g. the &#96;filesystem&#96; package, may not get
updated in a container (error message \'Error: Transaction failed\'),
see also <https://bugzilla.redhat.com/show_bug.cgi?id=1548403> and
<https://bugzilla.redhat.com/show_bug.cgi?id=1912155>.

Workaround: Run before update:

    […]\&#35; echo '%_netsharedpath /sys:/proc' \&gt; /etc/rpm/macros.netshared

When an update has already been performed, execute this command and
update the package again.

As of Fedora 35, the bug should be fixed.

&#42; Providing services = Setting up PostgreSQL Database Server Peter
Boy :page-authors: Peter Boy :page-aliases:
service-postgresql-installation.adoc :page-aliases:
services/postgresql-installation.adoc

> Postgresql is the recommended database management system of Fedora. It
> is a key functionality that is part of the Release criteria.

Fedora 43 includes PostgreSQL 18.1 If you update from F42, read the
release notes or the [update description on Server home
page](index.adoc&#35;_updating_to_fedora_43) for detailed instructions.

## 1. Storage preparation {#_1_storage_preparation}

In Fedora, PostgreSQL stores the databases and other runtime files in
the &#96;/var/lib/pgsql&#96; directory.

Following the Fedora storage concept, a dedicated file system on a
logical volume, mounted at the appropriate position in the directory
tree, takes over this function.

A convenient descriptive name for both the logical volume and the file
system is &#96;pgsql&#96;. The volume group that contains the logical
volume is called &#96;fedora&#96; or &#96;systemVG&#96; in a default
installation. A suitable initial size is likely to be 50 GiB in many
cases.

In any case, the system administrator must adapt the following command
sequence according to the local requirements! With a Linux LVM and
Software raid, XFS can autonomously determine its optimal configuration
values. With some hardware raids, intervention by the administrator can
also be useful for this.

First, check for the VG name and then adjust the following commands.

    […]\&#35; vgs
    VG       \&#35;PV \&#35;LV \&#35;SN Attr   VSize VFree
    systemVG   1   1   0 wz--n- 7.55g \&lt;4.42g
    […]\&#35; lvcreate -L 50G -n pgsql  systemVG
    Logical volume 'pgsql' created.
    […]\&#35; mkfs.xfs -L pgsql /dev/mapper/systemVG-pgsql
    meta-data=/dev/mapper/systemVG-pgsql isize=512    agcount=4, agsize=655360 blks
    \&#8230;
    Discarding blocks\&#8230;Done.
    […]\&#35; mkdir /var/lib/pgsql
    […]\&#35; echo 'UUID=$(blkid -s UUID -o value /dev/systemVG/pgsql) /var/lib/pgsql              auto    defaults    0 0'  \&gt;\&gt; /etc/fstab
    […]\&#35; mount -a
    […]\&#35; df -h

## 2. Basic installation {#_2_basic_installation}

Just one package - postgresql-server - already provides a complete and
comprehensive server at your disposal. All the many other Postgresql
related packages provide additional options that are only useful or
needed for specific special needs.

The package provides the pure server functionality. Fedora additionally
loads the packages *postgresql*, a CLI client program granting
interactive access to the server, and *postgresql-private-libs*,
containing shared libraries used by each of those packages, as
dependencies.

    […]\&#35; dnf install postgresql-server
    \&#8230;
    ==============================================================================
    Package                              Architectur     Version
    ==============================================================================
    Installing:
    postgresql-server                   x86_64          18.0-1.fc43
    Installing dependencies
    postgresql                          x86_64          18.0-1.fc43
    postgresql-private-libs             x86_64          18.0-1.fc43

    Transaction Summary
    ==============================================================================
    Install  3 packages

The installer should have adjusted all SELinux labels in the pgsql
directory already created. Check:

    […]\&#35; ls -alZ  /var/lib/pgsql/
    drwx------.  4 postgres postgres system_u:object_r:postgresql_db_t:s0   54  \&#8230;  .
    drwxr-xr-x. 45 root     root     system_u:object_r:var_lib_t:s0       4096  \&#8230;  ..
    drwx------.  2 postgres postgres system_u:object_r:postgresql_db_t:s0       \&#8230;  backups
    -rw-r--r--.  1 postgres postgres system_u:object_r:postgresql_db_t:s0       \&#8230;  .bash_profile
    drwx------.  2 postgres postgres system_u:object_r:postgresql_db_t:s0       \&#8230;  data

If the installation program missed something, fix it executing

    […]\&#35; restorecon  -vFr /var/lib/pgsql
    […]\&#35; ls -alZ  /var/lib/pgsql/

It is also a prerequisite that exclusively the user postgres has access
to the directory pgsql and its subdirectories. Usually the installer
takes care of it. Fix it if necessary.

    […]\&#35; chown -R  postgres:postgres /var/lib/pgsql
    […]\&#35; chmod -R  700 /var/lib/pgsql

When all the requirements are met, perform the initialization of the
database cluster. This is a prerequisite for all further activities.

    […]\&#35; postgresql-setup --initdb

## 3. Configuration and initialization {#_3_configuration_and_initialization}

Fedora preconfigures Postgresql in a way that in any case ensures
reliable and maintainable operation on the one hand and secure operation
as far as possible on the other.

### Database connection paths {#_database_connection_paths}

A client can connect to the server either by a Unix socket connection or
a TCP/IP connection.

If the client does not specify a hostname parameter (-h), a Unix socket
connection is established. Postgres uses this method to ensure that root
can always securely establish a connection, regardless of password loss,
for example. The root user always has permission to assume the identity
of the postgresql master user (su - postgres). By default, no other user
has this option. As root, you get in any circumstances administrative
access to the database.

    […]\&#35; su - postgres
    […]$ psql

Specifying the host parameter results in an attempt to establish a
TCP/IP connection. Postgresql uses port 5432 by default for this
purpose. In Fedora, all interfaces are protected by a firewall by
default, except for localhost. A connection therefore requires opening a
suitable port.

Fedora abstracts the technical details with Firewalld, so that the
administrator does not need to bother with details. For most common uses
there are predefined services. So, if you want the database to be
accessible via the internal interface assigned to the internal zone, for
example, you need just two simple instructions.

    […]$ sudo firewall-cmd --zone=internal --permanent --add-service=postgresql
    […]$ sudo firewall-cmd --reload

:::: tip
::: title
:::

In case of connection issues there is most probably a SELinux
configuration missing, in most case a \'*name_connect access on the
tcp_socket*\' issue. Check the SELinux module in Cockpit. It helps you
in detail to establish a local policy to fix it. It is easy, just a
matter of 2 instructions.
::::

### Authentification options {#_authentification_options}

#### Administrative access {#_administrative_access}

For admin access Fedora postgresql is configured to obtain the host's
operating system user name from the kernel and using it as the allowed
database user name. Therefore, as soon as someone can authentiate on the
host as user *postgres*, that person has administrative privileges on
the postgresql server without any additional password prompt. The only
one who can do that by default, is root. Root can configure additional
users to be able to su to postgres. In any case, in a whatever
emergency, if any then the system administrator is able to quickly
access postgresql server unhindered and salvage what can still get
salvaged.

This capability is configured in the \~/data/pg_hba file, together with
other properties.

    […]\&#35; vim  /var/lib/pgsql/data/pg_hba.conf
    \&#8230;
    \&#35; PostgreSQL Client Authentication Configuration File
    \&#35; ===================================================
    \&#8230;

    \&#35; TYPE  DATABASE        USER        ADDRESS             METHOD
    \&#35; 'local' is for Unix domain socket connections only
    local   all             all                             peer

It is really not a good idea to change the entry in the line 'local all
&#8230;' in any way. Whatever you configure later in this file, do not
change this line, or only do so if you are absolutely sure of what you
are doing.

If local regulations make it necessary to replace these procedures with
a dedicated authentication by postgresql itself, one of the other
procedures can be configured later. In general, however, it is not
advisable to make any changes. Once root is compromised, there are a lot
of completely different problems to get tackled.

#### Client user access {#_client_user_access}

In the initial configuration postgresql restricts any authentication to
peer as above described or ident (i.e. asking an ident server, that
Fedora doesn't install). In most cases you need an authentication based
on a password. The details depend on the prospective clients. As a
typical use case we will accept connections from the internal network to
VMs, by default 192.169.122.0/24.

The configuration is done in the file &#96;pg_hba.conf&#96; in the
&#96;data&#96; subdirectory. Edit the file to match the pattern below.

    […]\&#35; vim  /var/lib/pgsql/data/pg_hba.conf
    \&#35; PostgreSQL Client Authentication Configuration File
    \&#35; ===================================================
    \&#8230;
    \&#8230;

    \&#35; TYPE  DATABASE        USER        ADDRESS             METHOD
    \&#8230;
    \&#8230;
    \&#35; IPv4 local connections:
    host    all             all         127.0.0.1/32        ident
    \&#35; IPv4 internal network connections:                         \&#35; \&lt;- modification!
    host    all             all         192.168.122.1/24    scram-sha-256   \&#35; \&lt;- modification!
    \&#35; IPv6 local connections:
    host    all             all         ::1/128             ident
    \&#35; Allow replication connections from localhost, by a user with the

Add further entries according to the need, as far as they are already
known. Additions are possible at any time later, but require a reload of
the server, i.e. at least a short service interruption.

To make access via the 192.168.122.1/24 host interface really work, you
have to add the host's IP address on that network to postgresql.conf.

For further details see the PostgreSQL documentation, chapter [20.1. The
pg_hba.conf
File](https://www.postgresql.org/docs/current/auth-pg-hba-conf.html).

:::: tip
::: title
:::

Some of the possible authentication methods require additional settings
for SELinux. For example, the *PAM* method requires unix_chkpwd access
permissions. A typical error message is "*SELinux is preventing auth
from name_connect access on the tcp_socket port 5432*". The easiest way
to fix this is to use the SELinux module from Cockpit..
::::

### Connection options {#_connection_options}

Now you are allowed to authenticate from machines on the internal
network, but you still can't connect from the internal network to the
PostgreSQL server. The default configuration restricts connection
initially to the local host to avoid any security vulnerabilities in the
first place.

Connections granted are configured in \~/data/postgresql.conf. To grant
access to VMs on the internal network as well as from local host, edit
the file near the beginning to match the pattern below.

    […]\&#35; vim  /var/lib/pgsql/data/postgresql.conf
    \&#8230;
    \&#35;------------------------------------------------------------------------------
    \&#35; CONNECTIONS AND AUTHENTICATION
    \&#35;------------------------------------------------------------------------------

    \&#35; - Connection Settings -

    \&#35;listen_addresses = 'localhost'         \&#35; what IP address(es) to listen on;
    \&#35; comma-separated list of addresses;
    \&#35; defaults to 'localhost'; use '\&#42;' for all
    \&#35; (change requires restart)
    listen_addresses = 'localhost, 192.168.122.1/24'
    \&#35;port = 5432                            \&#35; (change requires restart)
    max_connections = 100                   \&#35; (change requires restart)
    \&#8230;

An entry of &#96;listen_addresses = \'&#42;\'&#96; enables connections
from any address. It is probably rather a bad idea and relies solely on
authentication restrictions and, if present, a supporting firewall
configuration.

## 4. Using PostgreSQL as permanent service {#_4_using_postgresql_as_permanent_service}

You are now ready to start the PostgreSQL server.

    […]\&#35; systemctl start postgresql
    […]\&#35; systemctl status postgresql
    \&#8230;
    \&#8230; systemd[1]: Started postgresql.service - PostgreSQL database server.

If no errors are reported, try to connect as user postgres using the
psql cli client. Once connected, start commands with backslash, e.g. \\?
to get help or \\q to quit.

    […]\&#35; su - postgres
    […]$ psql
    psql (18.0)
    Enter »help« \&#8230;

    postgres=\&#35; \dg
    List of roles
    Role name |                            attributes                       | member of
    -----------+-------------------------------------------------------------+--------------
    postgres  | Superuser, Create role, Create DB, Replication, Bypass RLS  | {}

    postgres-\&#35; \q
    […]$ exit
    […]\&#35;

If everything works as expected, enable autostart of postgresql,

    […]\&#35; systemctl enable postgresql

Enjoy a powerful DBMS.

# Fedora Server System Administrators Cheat Sheet: PostgreSQL {#_fedora_server_system_administrators_cheat_sheet_postgresql}

Peter Boy :page-authors: Peter Boy

> The Fedora System Administrator's Cheat Sheet series compiles typical,
> frequently used instructions for various application programs, most of
> which can be used with minor modifications via copy&amp;paste. They
> also contain direct links to the relevant sections of the upstream
> documentation.

## Basic Commands {#_basic_commands}

Get administrative access to a postgresql database and get a postgres terminal prompt

:   [\&#8230;]\&#35; sudo -i -u postgres psql
        psql (18.1)
        Type 'help' for help.

        postgres=\&#35;

List all databases

:   postgres=\&#35; \l

Connect to a database

:   postgres=\&#35; \c \&lt;database_name_from_above_list\&gt;

List all tables in the database connected to

:   postgres=\&#35; \dt

List all users / roles

:   postgres=\&#35; \du

Create a new user / role

:   postgres=\&#35; CREATE USER new_user_name WITH PASSWORD 'password';

Change password of a user / role

:   postgres=\&#35; ALTER USER user_name WITH PASSWORD 'new_password';

# Setting up a basic web server {#_setting_up_a_basic_web_server}

Peter Boy (pboy); Emmanuel Seyman (eseyman)

> The recommended and fully supported Fedora Web server is Apache, named
> httpd in the distribution. It is a Fedora Server key functionality
> that is part of the services specified in the technical specification.
> This article is about setting up a basic server to serve static html
> pages. Further articles build on this and describe additional
> deployment configurations.

:::: note
::: title
:::

This article has not yet been *finally* reviewed. Some content may still
be subject to change.
::::

The Fedora Web server httpd is basically an Apache web server. This
document covers in detail especially the setup and maintenance of
certificates for secure, encrypted connections, which are standard
today. It also covers various other configurations such as access
restriction via authentication or WebDAV for uploading and modifying
files. It also focuses on the delivery of static web pages. Further
articles describe how httpd can be configured for other usage scenarios
such as frontend for application servers, proxy for containers,
integration of dynamic languages and other deployment options.

## How it works {#_how_it_works_5}

A Fedora Web Server installation stores the *configuration* in
subdirectories of /etc/httpd. Only 2 subdirectories are relevant for the
system administrator. The directory /etc/httpd/conf.d is the more
important one and stores especially the configuration of the different
web sites. This directory is where the system administrator works the
most. The directory /etc/httpd/conf.modules.d contains the modules to be
loaded dynamically and their configuration. Only very rarely does
anything need to be changed here.

The *data* for the default web site (or \'main\' site) is by default
located in &#96;/var/www&#96;, the html-files in its subdirectory
&#96;html&#96;. Additional directories are provided for extended
configurations, e.g. the &#96;cgi-bin&#96; subdirectory for storing
(classic) CGI files.

This structure dates back to the early days of Linux systems, when the
server hardware was capable to serve only one site (i.e. one Domain). As
the hardware got more powerful, and became capable of serving more than
one domain, \'virtual servers\' were added that provided additional
domains -- distinguished either by name (virtual named hosts) or by IP.
This situation is still virulent in the term \'main" site or \'main"
server.

All these distinctions have now been abandoned. Today, it is widespread
for a server to host several domains as a matter of course. And it is
now best practice to configure *everything* as a virtual host, even if a
server only serves one domain.

In the Apache software, the \'main\' server is still present and serves
as the default configuration of the most important parameters, which are
inherited as default settings by the virtual host(s).

This development has consequences for the organization of data storage.

If you only serve one domain, you still could simply use that \'main\'\'
site directory and put files into the &#96;/var/www/html&#96;
subdirectory and use it for your single virtual host. And this directory
ensures, that the httpd server is fully functional out of the box for
such a purpose. The mod_ssl module even provides a working https
configuration based on an also provided self-signed certificate.

But in all cases you need a more appropriate alternative data
organization. The first structuring level should be the domain, not the
technology (like html and cgi-bin in the default).

*One option* is to use the &#96;/var/www/&#96; directory to create
domain-specific subdirectories and additional appropriate subdirectory
within. The advantage of this procedure is that it uses many default
httpd configurations, e.g. the SELinux labels. The disadvantage is that
the default configuration of the distribution is modified. It is
generally better to leave this untouched.

*An alternative option*, in many cases a better fit to FHS compliance is
the &#96;/srv&#96; directory. Today you would have many Domains, which
are served by one or more applications. According to the FHS, the
&#96;/srv&#96; directory is the appropriate place for storing data. You
create a domain-specific directory, e.g. example.com, and therein a
&#96;htdocs&#96; subdirectory for static html files, a &#96;webapps&#96;
subdirectory for your web applicaion, e.g Ruby on Rails, a
&#96;mail&#96; subdirectory for a postfix/dovecot mail hub, etc.

In this guide we use the latter option. Therefore, we use directories
like &#96;/srv/&lt;DOMAINNAME&gt;/&#96; to store all data relevant to a
domain, and &#96;/srv/&lt;DOMAINMANE&gt;/htdocs/&#96; for static HTML
pages. If you want to use the former option, you can replace
&#96;/srv/&#96; by &#96;/var/www/&#96;.

## Storage preparation {#_storage_preparation}

*Before* installing the Software you have to prepare the storage. The
Fedora Server Edition storage concept requires the creation of an LVM
logical volume to hold the user data. There are at least two reasonable
options:

a.  Create a logical volume of a suitable size and mount it on /srv (or
    /var/www).

b.  Create a logical volume Pool for thinly provisioned Volumes and
    therein one thin provisioned volume per domain.

*The former* is a good choice if there are many domains, each with a
small amount of data, e.g. if the web server is mainly used as a front
end for web application servers that manage their data in their own way,
e.g. Apache Tomcat in &#96;/var/lib/tomcat/webapps&#96; or
&#96;/var/lib/tomcats/&lt;domain&gt;/webapps&#96; or if they are stored
in a database or a *central* GIT repository (Jamstack CMS).

*The latter* is a good choice if a large amount of data is generated in
each domain (or most of them) because the data consists of extensive
static HTML files, or an application server created directly in the http
document root, usually with Ruby on Rails, for example, or a Jamstack
based CMS with *decentralized* GIT repositories.

And of course you can also combine both.

The easiest way is to create the required volumes with *Cockpit*, the
web-based server administration tool.

## Installation {#_installation_4}

1.  Install the Apache httpd web server. Today, you will almost always
    need the modules for managing SSL connections and the module for
    domain monitoring. Everything now runs via https.

        […]$ sudo dnf install httpd mod_ssl mod_md
        […]$ sudo firewall-cmd --add-service=https --permanent
        […]$ sudo firewall-cmd --add-service=http  --permanent
        […]$ sudo firewall-cmd --reload

2.  Start the web server

        […]$ sudo systemctl start httpd
        […]$ sudo systemctl status httpd
        […]$ sudo systemctl enable httpd
        Created symlink /etc/systemd/system/multi-user.target.wants/httpd.service → /usr/lib/systemd/system/httpd.service.

3.  The Web server should already answer to requests and show the Fedora
    test page. Enter your server's address into your browser's address
    input field.

    ![Fedora test page](services/httpd-basic-setup-030.png)

4.  If you plan to manage Let's Encrypt certificates using certbot
    install

        […]$ sudo dnf install letsencrypt

## Setup a web site {#_setup_a_web_site}

1.  &#42;Setup the web site Document Root directory&#42;

    As discussed above there are several options. In this example we use
    the /srv alternative and the website base name as base directory.

        […]$ sudo -i
        […]\&#35; mkdir -p  /srv/SITENAME/htdocs

    It you opt for thinly provisioned volumes use Cockpit to create the
    volume, format the filesystem and permanently mount it at the base
    location &#96;/srv/SITEMANE/&#96;. Cockpit performs all these steps,
    you just need to create the htdocs subdirectory.

    With /srv/ as the base directory you must adjust the SELinux labels.

        […]\&#35; /usr/sbin/semanage fcontext -a -t httpd_sys_content_t  -s system_u  '/srv/SITENAME/htdocs(/.\&#42;)?'
        […]\&#35; /sbin/restorecon -R -vF /srv/SITENAME/htdocs
        Relabeled /srv/SITENAME/htdocs from unconfined_u:object_r:var_t:s0 to system_u:object_r:httpd_sys_content_t:s0

    Create a very basic index page in your document root directory

        […]\&#35; vim /srv/SITENAME/htdocs/index.html
        \&lt;h1\&gt;\&lt;center\&gt;It works!\&lt;/center\&gt;\&lt;/h1\&gt;

2.  &#42;Configure a Virtual Host for the domain&#42;

    To make it easier for you we provide a [reasonably detailed
    template.
    Download](attachment$services/httpd-basic-setup/zvhost-static-html.template)
    and save it into the directory &#96;/etc/httpd/conf.d/&#96;. Copy
    the template e.g. as &#96;zvhost-SITENAME.conf&#96; and adapt it to
    your requirements.

    It is *good practice* to follow a systematic *naming convention*. In
    the example, we use the prefix \'vhost\' to clearly distinguish the
    domain virtual host configurations from other configurations.

    The configuration files are read in alphabetically order. The order
    is significant. The first virtual host found, becomes the default
    host. It is always used if no suitable host name is found for a
    request (e.g. because the IP address is used).

    :::: caution
    ::: title
    :::

    A website using the same name as the server's hostname or its DNS
    entry, requires special measures. See section Troubleshooting.
    ::::

    Edit the copied template file and adjust it as appropriate.

        […]$ sudo vi /etc/httpd/conf.d/zvhost-SITENAME.conf
        \&#35; Apache vhost configuration for a static html server.
        \&#35; It manages SSL connections including certificates.
        \&#35; Initially, a self-signed certificate is active.
        \&#35; Incoming http traffic is automatically redirected to https.
        \&#35; Version 2.1

        \&#35;==\&gt; To adjust in vi/vim copy and adjust to the vi command line:
        \&#35; : %s/SHORT_DESCR/real_short_descr/g    e.g. my-domain.org production server
        \&#35; : %s/FQN_NAME/your_domain/g            e.g. my-domain.org
        \&#35; : %s/BASE_NAME/your_shortname/g        e.g. my-domain
        \&#35; : %s/OPTIONAL_ALIAS/your_alias/g       e.g. www.my-domain.org
        \&#35; afterwards delete these lines


        \&#35; Certificates are managed by Apache md module.
        \&#35;==\&gt; To activate, remove the leading '\&#35;' character and comment out the
        \&#35; the default distribution provided certificates further down.
        \&#35;==\&gt; Adjust the mail address as appropriate!
        \&#35;MDContactEmail root@FQN_NAME
        \&#35;MDCertificateAgreement accepted
        \&#35;MDomain FQN_NAME

        \&lt;VirtualHost \&#42;:443\&gt;
        \&#35; Secure virtual WEB host configuration for
        \&#35; SHORT_DESCR

        \&#35; The site can be accessed by https/ssl only. Without a valid certificate
        \&#35; you have to use a self-signed certificate as a quick temporary fix.

        ServerName      FQN_NAME
        ServerAlias OPTIONAL_ALIAS

        \&#35;==\&gt; Adjust the mail address as appropriate!
        ServerAdmin     root@FQN_NAME

        \&#35; \&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;
        \&#35; NOTE: We re-route everything from the insecure site to this secure site!
        \&#35; \&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;

        \&#35; Optional: Ensure that all registered domain names are rewritten to the
        \&#35; official base name
        \&#35;RewriteEngine   On
        \&#35;RewriteCond     %{HTTP_HOST}    !^FQN_NAME [NC]
        \&#35;RewriteCond     %{HTTP_HOST}    !^$
        \&#35;RewriteRule     ^(.\&#42;)$          https://FQN_NAME$1  [R=301,L]

        \&#35; ====================================================================
        \&#35; Certificates configuration
        \&#35; ====================================================================
        SSLEngine on
        \&#35; We rely on Fedora's systemwide configuration of SSL security.

        \&#35; By default, certificates are managed by Apache md module (see above)
        \&#35; In this case, no certificates needs bo be configured here.
        \&#35; Otherwise, insert proper certificate configuration.

        \&#35; DEFAULT mod_ssl provided, needed for initial startup.
        \&#35;==\&gt; Comment OUT when module md created a certificate or you use
        \&#35; custom certificates.
        SSLCertificateFile  /etc/pki/tls/certs/localhost.crt
        SSLCertificateKeyFile   /etc/pki/tls/private/localhost.key

        \&#35; LetsEncrypt certificates managed by certbot (NOT by module md!)
        \&#35;SSLCertificateFile      /etc/letsencrypt/live/DOMAIN_NAME/cert.pem
        \&#35;SSLCertificateKeyFile   /etc/letsencrypt/live/DOMAIN_NAME/privkey.pem
        \&#35;SSLCertificateChainFile /etc/letsencrypt/live/DOMAIN_NAME/chain.pem

        \&#35; ===============================================================
        \&#35; Directory Locations
        \&#35; ===============================================================
        DirectoryIndex  index.html
        DocumentRoot    /srv/BASE_NAME/htdocs
        \&#35; Specific to default 2.4 configuration:
        \&#35; Enable access to server-specific base file location
        \&lt;Directory '/srv/BASE_NAME'\&gt;
        AllowOverride None
        \&#35; Allow open access:
        Require all granted
        \&lt;/Directory\&gt;
        \&#35; Further relax access to the default document root
        \&lt;Directory '/srv/BASE_NAME/htdocs'\&gt;
        \&#35;
        \&#35; Possible values for the Options directive are 'None', 'All',
        \&#35; or any combination of:
        \&#35;   Indexes Includes FollowSymLinks SymLinksifOwnerMatch ExecCGI MultiViews
        \&#35;
        \&#35; Note that 'MultiViews' must be named \&#42;explicitly\&#42; --- 'Options All'
        \&#35; doesn't give it to you.
        \&#35;
        \&#35; The Options directive is both complicated and important.  Please see
        \&#35; http://httpd.apache.org/docs/2.4/mod/core.html\&#35;options
        \&#35; for more information.
        \&#35;
        Options Indexes FollowSymLinks

        \&#35;
        \&#35; AllowOverride controls what directives may be placed in .htaccess files.
        \&#35; It can be 'All', 'None', or any combination of the keywords:
        \&#35;   Options FileInfo AuthConfig Limit
        \&#35;
        AllowOverride None

        \&#35;
        \&#35; Controls who can get stuff from this server:
        \&#35; Allow open access:
        Require all granted

        \&lt;/Directory\&gt;


        \&#35; ===============================================================
        \&#35; Optional: Protect access to start page (and subsequent pages)
        \&#35;==\&gt;        Ensure you created the additional auth.d directory
        \&#35;           including SELinux labels
        \&#35; ===============================================================
        \&#35;\&lt;Location /\&gt;
        \&#35;  AuthType Basic
        \&#35;  AuthName 'Access start page'
        \&#35;  AuthUserFile /srv/BASE_NAME/auth.d/htuser
        \&#35;  Require valid-user
        \&#35;\&lt;/Location\&gt;


        \&#35; ===============================================================
        \&#35; Optional: Configure webDAV access
        \&#35;==\&gt;        Ensure you created the additional davlock directory
        \&#35;           including SELinux labels
        \&#35; ===============================================================
        \&#35;DavLockDB /srv/SERVER_SHORT_NAME/davlock/dav_lock_db

        \&#35;\&lt;Location /dav\&gt;
        \&#35;  DAV On
        \&#35;  ForceType text/plain

        \&#35;  Order Allow,Deny
        \&#35;  Allow from all
        \&#35;  Options all
        \&#35;  DirectoryIndex none

        \&#35; Optional: Protect basic dav page (and all subsequent page)
        \&#35;AuthType Basic
        \&#35;AuthName 'Application Server WebDAV access'
        \&#35;AuthUserFile /srv/SERVER_SHORT_NAME/auth.d/htdavuser
        \&#35;Require valid-user
        \&#35;\&lt;/Location\&gt;


        \&#35; ===============================================================
        \&#35; Logging configuration
        \&#35; ===============================================================
        \&#35; Use separate log files for the SSL virtual host; note that LogLevel
        \&#35; is not inherited from httpd.conf.
        \&#35; NOTE: fail2ban searches for ~/logs/\&#42;access_log and  ~/logs/\&#42;error_log
        \&#35;       to access log files to watch and analyze!
        ErrorLog        logs/BASE_NAME-ssl_error_log
        CustomLog       logs/BASE_NAME-ssl_access_log combined
        LogLevel warn

        \&lt;/VirtualHost\&gt;

        \&lt;VirtualHost \&#42;:80\&gt;
        \&#35; INSECURE virtual WEB host configuration for
        \&#35; SHORT_DESCR

        \&#35; NOTE: Everything from the insecure port 80 is redirected to this instance'
        \&#35;       SECURE site

        ServerName      FQN_NAME
        ServerAlias OPTIONAL_ALIAS

        ServerAdmin     root@FQN_NAME

        \&#35; \&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;
        \&#35; NOTE: We re-route everything to the secure site!
        \&#35;       We retain all aliase names for now.
        \&#35;       There is no need for an exception for Let's Encrypt anymore.
        \&#35;       Version 2.x can deal with self-signed certificates and https
        \&#35; \&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;
        RewriteEngine   On
        RewriteRule (.\&#42;)   https://%{HTTP_HOST}%{REQUEST_URI} [R=301,L]


        \&#35; ===============================================================
        \&#35; Logging configuration
        \&#35; ===============================================================
        \&#35; Use separate log files for the SSL virtual host; note that LogLevel
        \&#35; is not inherited from httpd.conf.
        \&#35; NOTE: fail2ban searches for ~/logs/\&#42;access_log and  ~/logs/\&#42;error_log
        \&#35;       to access log files to watch and analyze!
        ErrorLog        logs/BASE_NAME-error_log
        CustomLog       logs/BASE_NAME-access_log combined

        \&lt;/VirtualHost\&gt;

3.  &#42;Restart and check the web server&#42;

    ``` text
    […]\&#35; systemctl  restart  httpd
    […]\&#35; systemctl  status  httpd
    ● httpd.service - The Apache HTTP Server
    Loaded: loaded (/usr/lib/systemd/system/httpd.service; enabled; preset: disabled)
    Active: active (running) since \&#8230;
    \&#8230;
    \&#8230;
    ```

4.  &#42;Test the configuration&#42;

    Again, enter your server's address into your browser's address input
    field. Because we already re-route everything to the secure site
    which uses a self-signed certificate so far, you get a warning
    message. Select \'Advanced\' and accept the \'risk\' here. You'll
    see the provisional test page.

5.  &#42;Final commissioning&#42;

    Delete the provisional &#96;index.html&#96; file and fill your Web
    content into the Document Root &#96;/srv/SITENAME/htdocs/&#96;.

## Troubleshooting {#_troubleshooting}

### The website shares the same name as the server {#_the_website_shares_the_same_name_as_the_server}

#### The phenomenon {#_the_phenomenon}

1.  If the website uses a DocumentRoot directory different from
    /var/www/html, then the Servers http protocol variant will display
    the correct content and the https variant will use /var/www/html or
    the distribution provided default page instead.

2.  If you use Let's encrypt certbot to manage certificates, it installs
    a valid certificate, but a https request results in an invalid
    certificate complain.

#### The cause {#_the_cause}

The httpd service always sets a \'default\' server. The intended use is
to answer requests for which the httpd service can not identify a web
server configuration. Typically, this happens when a client addresses
the web page by the server's IP address instead of its name or there is
still an old DNS entry. The distribution provides a default ssl
configuration as part of mod_ssl. This default gets associated with the
server's hostname or DNS record and takes precedence over the
user-created configuration.

#### The solution {#_the_solution}

Unfortunately, the only way to fix this is to modify the distribution
provided mod_ssl configuration file and remove the default server
configuration. First, make a backup copy of the file and then modify it
as indicated.

``` text
[…]\&#35; cp /etc/httpd/conf.d/ssl.conf  /etc/httpd/conf.d/ssl.conf.fc
[…]\&#35; vi /etc/httpd/conf.d/ssl.conf
\&#35;
\&#35; When we also provide SSL we have to listen to the
\&#35; standard HTTPS port in addition.
\&#35;
Listen 443 https

\&#35;\&#35;
\&#35;\&#35;  SSL Global Context
\&#35;\&#35;
\&#35;\&#35;  All SSL configuration in this context applies both to
\&#35;\&#35;  the main server and all SSL-enabled virtual hosts.
\&#35;\&#35;
\&#8230;
\&#8230;
\&#35;\&#35;
\&#35;\&#35; SSL Virtual Host Context
\&#35;\&#35;

\&#35;\&#35;\&#35;\&#35; \&lt;VirtualHost _default_:443\&gt;     \&#35;\&lt;======= comment out this line (near line 56)

\&#35; General setup for the virtual host, inherited from global configuration
\&#35;DocumentRoot '/var/www/html'
\&#35;ServerName www.example.com:443
\&#8230;
\&#8230;
\&#35;   SSL Engine Switch:
\&#35;   Enable/Disable SSL for this virtual host.
\&#35;\&#35;\&#35;\&#35;SSLEngine on                     \&#35;\&lt;======= comment out this line (near line 70)

\&#35;   List the protocol versions which clients are allowed to connect with.
\&#35;   The OpenSSL system profile is configured by default.  See
\&#8230;
\&#8230;
\&#35;   Point SSLCertificateFile at a PEM encoded certificate.  If
\&#35;   \&#8230;
\&#35;\&#35;\&#35;\&#35;SSLCertificateFile /etc/pki/tls/certs/localhost.crt  \&#35;\&lt;======= comment out (near line 101)
\&#8230;
\&#8230;
\&#35;\&#35;\&#35;\&#35;SSLCertificateKeyFile /etc/pki/tls/private/localhost.key   \&#35;\&lt;======= comment out (near line 110)
\&#35;   Per-Server Logging:
\&#35;   The home of a custom SSL log file. Use this when you want a
\&#35;   compact non-error SSL logfile on a virtual host basis.
CustomLog logs/ssl_request_log \
'%t %h %{SSL_PROTOCOL}x %{SSL_CIPHER}x \'%r\' %b'

\&#35;\&#35;\&#35;\&#35; \&lt;/VirtualHost\&gt;     \&#35;\&lt;======= comment out this line (last line, usually 218)

[…]\&#35; systemctl  restart  httpd
```

When the httpd service is up again, everything should work as expected.

# File sharing with NFS -- Installation {#_file_sharing_with_nfs_installation}

Peter Boy (pboy);Emmanuel Seyman (eseyman); Jason Beard (cooltshirtguy);
Otto Liljalaakso; Jocelyn Gould (korora)

> NFS, the Network File System, is a mature protocol designed to share
> files between Unix-type systems over TCP/IP networks. Fedora Server
> Edition installs by default the kernel space NFS server, but without
> configuration and activation. This article describes its configuration
> and activation.

The objective of this guide is how to setup *NFS Server* on a Fedora
Server Edition. For information on how to setup the client part, consult
your OS's documentation.

NFS is a Network service in Linux used to share the files and
directories of the Server to users (clients) on the network. It allows
clients to *mount* a remote directory or complete filesystem over a
network and interact with it much like local storage is accessed. It is
the same principle as Map Drive in Windows Systems. One of it most used
benefits is to store and access data on central location.

The NFS Protocol was first introduced by Sun Microsystem in 1984. The
protocol has evolved from its origins. Over the years, new versions have
been released, adding new features. Currently, NFS v4.2 is the current
version. Perhaps most practically significant is the optional user
identification as well as a virtual ROOT.

NFS protocol is not encrypted by default, and unlike Samba, unless you
activate the optional feature it does not provide user authentication.
Access to the server is restricted by the clients' IP addresses or
hostnames.

The kernel space NFS server features high performance and is therefore
selected as default. Fedora Server also supports user space NFS server.
However, this is not the subject of this article.

## Preparation {#_preparation_2}

There are three packages which provide basic support for kernel space
NFS:

nfs-utils

:   is the main package and provides a daemon for the kernel NFS server
    and related tools. It also contains the *showmount* program to query
    the mount daemon on a remote host for available ressources, eg
    listing the clients which are mounted on that host. It also contains
    the mount.nfs and umount.nfs programs.

libnfsidmap

:   NFSv4 User and Group ID Mapping Library that handles mapping between
    names and ids for NFSv4.

sssd-nfs-idmap

:   SSSD plug-in provides a way for rpc.idmapd to call SSSD to map
    UIDs/GIDs to names and vice versa. It can be also used for mapping
    principal (user) name to IDs(UID or GID) or to obtain groups which
    user are member of.

Ensure that these packages are really installed.

    […]$ rpm -qa | grep nfs
    libnfsidmap-2.8.4-0.fc43
    sssd-nfs-idmap-2.11.1-4.fc43
    nfs-utils-2.8.4-0.fc43

If a package missing, then a system administrator can simply reinstall
it.

### Organizing storage {#_organizing_storage}

In principle, NFS can share any directory on the server. However, it
makes sense to concentrate at least generally shared files in a central
location instead of scattering everything around.

Furthermore, it is a best practice is to use a global NFS root directory
and bind mount those directories which are holding specific data at
specific locations to the share mount point.

In accordance to the Filesystem Hierarchie Standard (FSH), using a
/srv/nfs4 directory as the NFS root is a good choice.

Following Fedora Server storage rationale, a system administrator will
create a logical volume and mount it to either &#96;/srv&#96; to create
a Logical Volume as a pool for various services, or &#96;/srv/nfs&#96;
to create a Logical Volume, probably thin provisioned, for each service.
In case of systematic extensive utilization, a static LVM volume of
fixed size is advisable. For occasional usage, a thin provisioned
logical LVM volume might be the better choice.

In this guide we will demontrate the latter and create a thin
provisioned LV for each service in /srv.

1.  &#42;Create a nfs export directory in /srv&#42;

        […]$ sudo mkdir /srv/nfs

    The created directory is by default readable for everyone, but not
    writable.

2.  &#42;Create a user and group nfs&#42;

    As already stated, nfs does not provide user authentication. A
    common way is to either use the same UID/GID for a given user on all
    devices on the network or to map every client to user nobody and
    make the export files read- and writable for everybody, i.e. for any
    user of the system. The former is difficult to achieve without a
    central logon instance, and the latter is at best inconvenient from
    a security point of view. So we use a pseudo user without a home
    directory and without a login shell, who owns all exported files and
    directories by default.

        […]$ sudo adduser -c 'nfs pseudo user' -b /nonexisting -M -r -s /sbin/nologin nfs

3.  &#42;Create and mount the required Logical Volumes&#42;

    The easiest way is to use Cockpit with its storage module. Select on
    the right side the root Volume Group and select \'Add logical
    volume\' in the new window.

    ![Create logical volume](services/nfs-server-inst-001.png)

    Fill in the form as needed. It is useful to name the LV to reflect
    the content or directory you want to store. Select \'Pool for thinly
    provisioned volumes\' and choose an appropriate size to accommodate
    all the data you plan to store.

    In the list of logical volumes that is then displayed, the line with
    the newly created LV contains the option \'Create thin volume\'. It
    opens a new form to create a LV to store data. We will use it for
    nfs exports.

    ![Create thin volume](services/nfs-server-inst-005.png)

    Fill in the form appropriately. Keep in mind that you are specifying
    the maximum value for the size of the volume. The system starts with
    a much smaller initial value and expands it as needed.

    After the creation of the volume the list of logical volumes
    contains a new entry for the logical Volume just created with an
    option \'Format\'. It opens a new form.

    ![Format the new logical volume](services/nfs-server-inst-009.png)

    Again, fill in the form and you are done.

    For hardcore system administrators with mouse allergy, the whole
    thing via CLI.

        […]\&#35; lvcreate -L 40G -T fedora/srv -V 30G -T fedora/srv -n nfs
        […]\&#35; lvs
        […]\&#35; mkfs.xfs /dev/fedora/nfs
        […]\&#35; mkdir -p /srv/nfs
        […]\&#35; vim /etc/fstab
        \&#8230;
        /dev/mapper/fedora-root     /                  xfs   defaults    0 0
        /dev/mapper/fedora-nfs      /srv/nfs           xfs   defaults    0 0
        \&#8230;

    Finallly mount the created filesystem.

        […]\&#35; mount -a

4.  &#42;Create and configure the directories to share&#42;

    In a typical use case you may create a directory \'common\' to
    widely share data and a directory \'project\', in which a team
    member shares data located in the home directory with the team.

        […]\&#35; sudo mkdir -p /srv/nfs/{common,project}
        […]\&#35; sudo chown -R nfs.nfs /srv/nfs/\&#42;
        […]\&#35; sudo mount --bind /home/USER/PROJECT /srv/nfs/project

    To make the bind mount(s) permanent, add the following entries to
    the /etc/fstab file:

        […]\&#35; vi /etc/fstab
        /home/USER/PROJECT  /srv/nfs/PROJECT   none   bind   0   0

## Optional server configuration {#_optional_server_configuration}

NFS server configuration uses 3 files

&#42; /etc/nfs.conf &#42; /etc/nfsmount.conf &#42; /etc/idmapd.conf

The commented out lines describe the default built in configuration.

1.  Configure the NFS basic directory

        […]$ sudo vi /etc/nfs.conf
        /home/USER/PROJECT  /srv/nfs/PROJECT   none   bind   0   0

## Activation {#_activation}

1.  &#42;Firewall configuration&#42;

    NFS uses port 2049 which is blocked in a Fedora standard
    installation by defaut.

        […]\&#35; firewall-cmd --permanent --add-service=nfs
        […]\&#35; firewall-cmd --reload

2.  &#42;Start NFS enabling autostart at boot time&#42;

        […]\&#35; systemctl enable nfs-server --now
        […]\&#35; systemctl status nfs-server

    This starts the NFS server only, but not the NFS client. Therefore,
    the server can not mount file ressources provided by another server.
    If required, additionally execute at first *&#96;systemctl enable
    nfs-client.target \--now&#96;*. For additional details you may look
    at *&#96;man 7 nfs.systemd&#96;*.

3.  Check availabe NFS capabilities

    Fedora enables versions 3 and 4.x, version 2 is disabled. The latter
    is pretty old now. Every machine should provide at least version 3.

        […]\&#35; cat /proc/fs/nfsd/versions
        -2 +3 +4 +4.1 +4.2

    So the NFS server supports versions 3 and all version 4
    capabilities.

## File resource configuration {#_file_resource_configuration}

NFS provides 2 options to configure which directores and files to share

/etc/exports

:   the \'traditional\' grand all-in-one configuration file

/etc/exports.d

:   the new way, a directory to collect a set of specific configuration
    files, which is read file by file at startup. These files must have
    the extension &#42;.exports. The format is the same as the grand
    configuration file.

You can use both options in parallel with the grand configuration file
read in first. We will use the modern form only.

### Configuration by example {#_configuration_by_example}

Example 1

:   Export the directory /srv/nfs/common with everyone, i.e. every
    network device and every user, can access with Read/Write and
    Synchronize access

        […]$ sudo vi /etc/exports.d/common.exports
        \&lt;i(nsert)\&gt;
        /srv/nfs/common \&#42;(rw,sync)

Example 2

:   Export the directory /srv/nfs/common with everyone, i.e. every
    network device and every user, can access with Read/Write and
    Synchronize access

        […]$ sudo vi /etc/exports.d/common.exports
        \&lt;i(nsert)\&gt;
        /srv/nfs/common \&#42;(rw,sync)

Example 3

:   Export the directory /srv/nfs/common with everyone, i.e. every
    network device and every user, can access with Read/Write and
    Synchronize access

        […]$ sudo vi /etc/exports.d/common.exports
        \&lt;i(nsert)\&gt;
        /srv/nfs/common \&#42;(rw,sync)

Example 4

:   Export the directory /srv/nfs/common with everyone, i.e. every
    network device and every user, can access with Read/Write and
    Synchronize access

        […]$ sudo vi /etc/exports.d/common.exports
        \&lt;i(nsert)\&gt;
        /srv/nfs/common \&#42;(rw,sync)

Example 6

:   Export the directory /srv/nfs/projects with all users of a specific
    network device with Read/Write and Synchronize access

        […]$ sudo vi /etc/exports.d/projects.exports
        \&lt;i(nsert)\&gt;
        /srv/nfs/common \&#42;(rw,sync)

#### Connection options {#_connection_options_2}

Each default for every exported file system must be explicitly
overridden. For example, if the rw option is not specified, then the
exported file system is shared as read-only.

For basic options of exports Option Description

rw/wo

:   Allow both read and write requests / only read requests on a NFS
    volume.

sync/async

:   Reply to requests only after the changes have been committed to
    stable storage (Default) / allow the NFS server to violate the NFS
    protocol and reply to requests before any changes made by that
    request have been committed to stable storage.

secure/insecure

:   Require that requests originate on an Internet port less than
    IPPORT_RESERVED (1024). (Default) / accepts all ports. using the
    insecure option allows clients such as Mac OS X to connect on ports
    above 1024. This option is not otherwise \'insecure\'.

wdelay/no_wdelay

:   Delay committing a write request to disc slightly if it suspects
    that another related write request may be in progress or may arrive
    soon. (Default) This option has no effect if async is also set. The
    NFS server will normally delay committing a write request to disc
    slightly if it suspects that another related write request may be in
    progress or may arrive soon. This allows multiple write requests to
    be committed to disc with the one operation which can improve
    performance. If an NFS server received mainly small unrelated
    requests, this behaviour could actually reduce performance, so
    no_wdelay is available to turn it off.

subtree_check/no_subtree_check

:   This option enables subtree checking. (Default) This option disables
    subtree checking, which has mild security implications, but can
    improve reliability in some circumstances.

root_squash/no_root_squash

:   Map requests from uid/gid 0 to the anonymous uid/gid. Note that this
    does not apply to any other uids or gids that might be equally
    sensitive, such as user bin or group staff. Turn off root squashing.
    This option is mainly useful for disk-less clients.

all_squash/no_all_squash

:   Map all uids and gids to the anonymous user. Useful for NFS exported
    public FTP directories, news spool directories, etc. Turn off all
    squashing. (Default)

anonuid=UID

:   These options explicitly set the uid and gid of the anonymous
    account. This option is primarily useful for PC/NFS clients, where
    you might want all requests appear to be from one user. As an
    example, consider the export entry for /home/joe in the example
    section below, which maps all requests to uid 150.

anongid=GID

:   Read above (anonuid=UID)

Setting the crossmnt option on the main psuedo mountpoint has the same
effect as setting nohide on the sub-exports: It allows the client to map
the sub-exports within the psuedo filesystem. These two options are
mutually exclusive.

### Administration {#_administration}

When the nfs service starts, the /usr/sbin/exportfs command launches and
reads this file, passes control to rpc.mountd (if NFSv2 or NFSv3) for
the actual mounting process, then to rpc.nfsd where the file systems are
then available to remote users.

When issued manually, the /usr/sbin/exportfs command allows the root
user to selectively export or unexport directories without restarting
the NFS service. When given the proper options, the /usr/sbin/exportfs
command writes the exported file systems to /var/lib/nfs/xtab. Since
rpc.mountd refers to the xtab file when deciding access privileges to a
file system, changes to the list of exported file systems take effect
immediately.

The following is a list of commonly used options available for
/usr/sbin/exportfs:

-r --- Causes all directories listed in /etc/exports to be exported by
constructing a new export list in /etc/lib/nfs/xtab. This option
effectively refreshes the export list with any changes that have been
made to /etc/exports.

-a --- Causes all directories to be exported or unexported, depending on
what other options are passed to /usr/sbin/exportfs. If no other options
are specified, /usr/sbin/exportfs exports all file systems specified in
/etc/exports.

-o file-systems --- Specifies directories to be exported that are not
listed in /etc/exports. Replace file-systems with additional file
systems to be exported. These file systems must be formatted in the same
way they are specified in /etc/exports. Refer to Section 18.7, "The
/etc/exports Configuration File" for more information on /etc/exports
syntax. This option is often used to test an exported file system before
adding it permanently to the list of file systems to be exported.

-i --- Ignores /etc/exports; only options given from the command line
are used to define exported file systems.

-u --- Unexports all shared directories. The command /usr/sbin/exportfs
-ua suspends NFS file sharing while keeping all NFS daemons up. To
re-enable NFS sharing, type exportfs -r.

-v --- Verbose operation, where the file systems being exported or
unexported are displayed in greater detail when the exportfs command is
executed.

If no options are passed to the /usr/sbin/exportfs command, it displays
a list of currently exported file systems.

#### Using exportfs with NFSv4 {#_using_exportfs_with_nfsv4}

The exportfs command is used in maintaining the NFS table of exported
file systems. When typed in a terminal with no arguments, the exportfs
command shows all the exported directories.

Since NFSv4 no longer utilizes the rpc.mountd protocol as was used in
NFSv2 and NFSv3, the mounting of file systems has changed.

An NFSv4 client now has the ability to see all of the exports served by
the NFSv4 server as a single file system, called the NFSv4 pseudo-file
system. On Red Hat Enterprise Linux, the pseudo-file system is
identified as a single, real file system, identified at export with the
fsid=0 option.

For example, the following commands could be executed on an NFSv4
server:

    mkdir /exports
    mkdir /exports/opt
    mkdir /exports/etc
    mount --bind /usr/local/opt /exports/opt
    mount --bind /usr/local/etc /exports/etc
    exportfs -o fsid=0,insecure,no_subtree_check gss/krb5p:/exports
    exportfs -o rw,nohide,insecure,no_subtree_check gss/krb5p:/exports/opt
    exportfs -o rw,nohide,insecure,no_subtree_check gss/krb5p:/exports/etc

In this example, clients are provided with multiple file systems to
mount, by using the \--bind option which creates unbreakeable links.

Because of the pseudo-file systems feature, NFS version 2, 3 and 4
export configurations are not always compatible. For example, given the
following directory tree:

    /home
    /home/sam
    /home/john
    /home/joe

and the export:

    /home \&#42;(rw,fsid=0,sync)

Using NFS version 2,3 and 4 the following would work:

    mount server:/home /mnt/home
    ls /mnt/home/joe

Using v4 the following would work:

    mount -t nfs4 server:/ /mnt/home
    ls /mnt/home/joe

The difference being \'server:/home\' and \'server:/\'. To make the
exports configurations compatible for all version, one needs to export
(read only) the root filesystem with an fsid=0. The fsid=0 signals the
NFS server that this export is the root.

    / \&#42;(ro,fsid=0)
    /home \&#42;(rw,sync,nohide)

Now with these exports, both \'mount server:/home /mnt/home\' and
\'mount -t nfs server:/home /mnt/home\' will work as expected.

## Testing the configuration {#_testing_the_configuration_2}

On client side:

    […]\&#35; showmount -e 192.168.12.200

On client side, try to mount an exported subdirectory:

    […]\&#35; mount 192.168.1.200:/nfsfileshare /mnt/nfsfileshare

Display the active mounts

    […]\&#35; mount | grep nfs
    sunrpc on /var/lib/nfs/rpc_pipefs type rpc_pipefs (rw,relatime)
    nfsd on /proc/fs/nfsd type nfsd (rw,relatime)
    192.168.12.5:/nfsfileshare on /mnt/nfsfileshare type nfs4 (rw,relatime,vers=4.1,rsize=262144,wsize=262144,namlen=255,hard,proto=tcp,port=0,timeo=600,retrans=2,sec=sys,clientaddr=192.168.12.7,local_lock=none,addr=192.168.12.5)

Check if the NFS mount is writable

    […]\&#35; touch /mnt/nfsfileshare/test

## Adding user identification and encryption (NFS 4) {#_adding_user_identification_and_encryption_nfs_4}

TBD

## Further reading {#_further_reading}

&#42; Upstream documentation:
<http://linux-nfs.org/wiki/index.php/Main_Page> &#42; Linux manual page:
<https://man7.org/linux/man-pages/man5/exports.5.html>

&#42; Example Use Cases = Adding a graphical interface Peter Boy; Jan
Kuparinen :page-authors: Peter Boy, Kevin Fenzi

Some users install Fedora Server Edition and then manually add a
graphical user interface. Sometimes it is a matter of more convenient
administration of a locally accessible server, sometimes it is a kind of
off-label use, and desire for a server hardened runtime environment as a
workstation with special requirements.

1.  &#42;Determine available graphical desktops&#42;

    To get an overview of available graphical user interfaces, simply
    list all installation groups and search through them. Unfortunately,
    the current naming is not consistent enough to allow a simple
    filtering by term.

    ``` bash
    […]\&#35; dnf group list
    ```

    You will find &#42; KDE Plasma Workspaces &#42; Xfce
    Desktop (@xfce-desktop-environment) &#42; LXDE Desktop &#42;
    LXQt-Desktop &#42; Cinnamon Desktop &#42; MATE Desktop &#42; Sugar
    Desktop Environment &#42; Deepin Desktop &#42; i3 desktop &#42;
    Pantheon Desktop

2.  &#42;Installation of a graphical desktop&#42;

    You may either use the groups pretty name as shown in the group
    listing or the canonical name. As an example, to install the
    Cinnamon desktop you can use either use

    ``` bash
    […]\&#35; dnf groupinstall 'Cinnamon Desktop'
    ```

    or

    ``` bash
    […]\&#35; dnf install @cinnamon-desktop-environment
    ```

3.  &#42;Adjustment of systemd to start in graphic mode&#42;

    To boot into graphical mode by default, you have to adjust the
    default target.

    ``` bash
    […]\&#35; systemctl set-default graphical.target
    ```

    With some desktop you may also need:

    ``` bash
    […]\&#35; systemctl enable gdm.service
    ```

    Try it, but you may get a \'Service not found\' message with some
    desktops. No need to worry, the installed desktop will come up
    without that.

4.  &#42;Reboot your server&#42;

    ``` bash
    […]\&#35; reboot
    ```

    Your system will start with the selected graphical desktop.

## Additional options {#_additional_options}

You may install multiple desktops. The utilities &#96;switchdesk&#96;
and &#96;switchdesk-gui&#96; can be used to switch the desktop GUI.

``` bash
[…]\&#35; dnf install switchdesk switchdesk-gui
```

In a terminal window, you can directly switch to another desktop:

``` bash
[…]\&#35; switchdesk cinnamon
```

Without naming the new desktop, a window with the available options will
be displayed.

The graphical &#96;\_Desktop Switcher\_&#96; is included in the
Systemadministration menu group. It always displayx a list of available
desktops you can choose from.

You can switch back to booting to a text console:

``` bash
[…]\&#35; systemctl set-default multi-user.target
[…]\&#35; reboot
```

After having switched back into text mode, you can switch to the
selected desktop just for the current session using

\[...\]&#35; startx

However, this does not work flawlessly for every available desktop.

&#42; Tutorials = ImageFactory -- How to Create a Virtual Machine Disk
Image Peter Boy (pboy); Jason Beard (cooltshirtguy) :page-authors: Peter
Boy

> The objective here is to learn to create a standard Fedora Server
> Edition bootable virtual disk image to be used as a base for further
> customization. The tool chain is the same as used by Fedora release
> engineering team. It ensures compatibility as much as possible and is
> making the installation as simple and speedy as possible.

The goal is to set up a working environment to create customized,
bootable and ready to be used Fedora Server virtual machine disk images.
The tool to be used, ImageFactory, is a bit of a challenge. Therefore,
we start with setting up a complete and known to work base setting. On
this solid basis, they can then start modifying and adapting the
configuration to their needs. That way, in case of bugs, it is quite
easy to locate the probable cause.

## Why ImageFactory {#_why_imagefactory}

There are many tools to create a VM virtual disk image. ImageFactory is
probably one of the oldest and not necessarily in the best of shape. Its
key advantage is that it is also used for building Fedora releases. You
can use a variety of resources maintained by the Fedora Release
Engineering team. This greatly facilitates the work and makes up for the
aforementioned disadvantage.

## Requirements {#_requirements}

There are some items to take into account.

&#42; You use ImageFactory exclusively via *CLI*. There is no graphical
interface. So you should be *familiar with the terminal*.

&#42; We use *Fedora Server* here, but in principle any of the Fedora
desktop systems is usable as well.

&#42; In this example, you need root permissions to execute the build
process (sudo is sufficient, of course).

&#42; ImageFactory is completely based on a \'*Kickstart*\' file that
controls the whole process. We provide a Kickstart file for download in
the appendix, which creates a complete Fedora Server Edition VM. It
serves here as a "Hello World" example, but is also suitable as a
starting point for your own development.

\+ Getting a Kickstart file to work correctly according to your goals is
the hardest (and only) challenge to meet.

&#42; And it requires a *template* file that provides metadata about the
image to be created. The content is pretty standard and doesn't need any
special attention. We provide a template file for download in the
appendix.

## Preparation {#_preparation_3}

### Create a working environment {#_create_a_working_environment}

ImageFactory uses a virtual machine to tailor the image, so you need
virtualization capabilities. If you work directly with your host (i.e.
on hardware), you need to [install
Virtualisation](virtualization/vm-install-diskimg-fedoraserver.xml).
Furthermore, ImageFactory installs a variety of software that an admin
would not necessarily want to see in the everyday working environment.
It is therefore recommended to create a dedicated virtual machine for
this purpose if possible and use nested virtualization in it.

1.  *On your host (on hardware) if not already done*: Add virtualization
    capability as described in [Adding Virtualization
    Support](virtualization/installation.xml).

2.  *Optional: Install a dedicated Fedora Server virtual machine*,
    follow the steps as described in [Creating a virtual machine using
    Fedora Server Edition disk
    image](virtualization/vm-install-diskimg-fedoraserver.xml) and add
    virtualization capability as described in [Adding Virtualization
    Support](virtualization/installation.xml), too.

    *Nested virtualization* should already work in Fedora, check as
    described in [Setting up Nested
    Virtualization](virtualization/nested-virtualization.xml).

3.  Ensure the *Guestfish suite is installed* to get the utilities to
    access and modify generated disk image files. If you follow [Adding
    Virtualization Support](virtualization/installation.xml) exactly, it
    is. Otherwise install it.

        […]$ sudo dnf install guestfs-tools

    Check to really install &#96;guestfs-tools&#96;, not
    &#96;libguestfs-tools&#96; (unless you need additional windows
    guests related software).

4.  Ensure that you have at least about 25 GB space available in your
    working environment.

5.  If you want to make use of Fedora Kickstart files you need to have
    &#96;git&#96; installed.

### Install ImageFactory {#_install_imagefactory}

ImageFactory includes the base package and various plugins for different
target platforms. To be able to use ImageFactory practically, all
plugins should be installed, regardless of the target format.
Additionally, the package pykickstart provides several helper programs,
among others ksflatten to check and optimize the kickstart file.

1.  *Create logical volumes* for ImageFactory working files. To make it
    easy use *Cockpit*.

    a.  First create a thin image pool of about 25 G wherein you can
        create the file systems actually to be used. This allows you to
        use the available space flexibly. In the *Storage* tab select
        the system volume group in the *Devices* box on the right side.
        In the list of *Logical volumes* select *Create new logical
        volume*.

        ![Cockpit Create thin
        pool](tutorials/imagefactory-kvm/030-create-thinpool-en.png)

        The list of logical volumes show a thin pool and a button to
        create thin volumes inside.

        ![Cockpit show thin
        pool](tutorials/imagefactory-kvm/035-show-thinpool-en.png)

    b.  Create a thin volume named *imagefactory* of max. 20 G for the
        working directory of ImageFactory and format an XFS filesystem
        to be mounted at /var/lib/imagefactory.

        ![Cockpit show thin
        pool](tutorials/imagefactory-kvm/040-create-thinvolume-en.png)

        Now, the list of logical volumes includes a new volume below
        imgfact_pool

        ![Cockpit show thin
        pool](tutorials/imagefactory-kvm/045-show-thinvolume-en.png)

    c.  Repeat the step b to create a logical volume of maximal 10 G
        named *oz* to be mounted at /var/lib/oz

        ![Cockpit list
        volumes](tutorials/imagefactory-kvm/059-list-volumes-en.png)

2.  *Install Imagefactory*

        […]$ sudo dnf install imagefactory  imagefactory-plugins\&#42; pykickstart

    This installs about 209 packages (in F38). To be sure, check and
    restore the SELinux labels for the installation directories.

        […]$ sudo  /sbin/restorecon  -R -vF /var/lib/imagefactory
        […]$ sudo  /sbin/restorecon  -R -vF /var/lib/oz

3.  *Adjust Imagefactory configuration*

    a.  *Enlarge the amount of working memory* for OZ, the backend used
        by ImageFactory.

            […]$ sudo  sed -i -e 's/\&#35; memory = 1024/memory = 2048/' /etc/oz/oz.cfg

    b.  Optional: *Switch the image output format* from the default
        \'raw\' type to qcow2 to save disk space. If you have plenty
        thereof, leave it as is.

            […]$ sudo vim /etc/oz/oz.cfg
            (edit)
            \&#35;image_type = raw
            image_type = qcow2

### Set up a working directory {#_set_up_a_working_directory}

At a convenient location, create a directory where you will store all
your working files, for example, in your home directory.

    […]$mkdir ~/imagefactory

It will primarly used to store the kickstart and the template files. You
may use your personal accout and use sudo for all commands. However, it
is more convenient to work as root. However, this is only advisable in a
dedicated VM as explained above.

#### The kickstart file {#_the_kickstart_file}

The kickstart file describes the content of the disk image to create.
Fetch the [basic kickstart file
\'fedora-server-kvm-dev.ks\']({attachmentsdir}/tutorials/imagefactory/fedora-server-kvm-dev.ks).
Probably it is a good idea to clone the [Fedora kickstart
repository](https://pagure.io/fedora-kickstarts) as well. It may be
advantageous to check for a file with a similiar target you want to
create and start with that. In any case, a look at the various Kickstart
files can give you ideas on how to achieve your goal.

1.  Fetch the [basic kickstart
    file]({attachmentsdir}/tutorials/imagefactory/fedora-server-kvm-dev.ks)
    and store it into this working directory. In many cases klicking the
    link stores the file into you default download directory,
    \~/Downloads in case of Fedora desktops or Macs.

        […]$ mv ~/Downloads/fedora-server-kvm-dev.ks  ~/imagefactory/

2.  Optional: *Clone the Fedora kickstart repository* for easy access to
    reference material.

        […]$ mkdir ~/imagefactory/FedoraKickstarts
        […]$ git  clone https://pagure.io/fedora-kickstarts.git -o upstream ~/imagefactory/FedoraKickstarts

    If you are planning to contribute your VM you should create a fork,
    too, so you can provide a pull request.

#### The download URL helper file {#_the_download_url_helper_file}

ImageFactory uses Anaconda to create the disk image. It uses the network
installatin method and needs appropriate URLs for Download. Anaconda
expects this information as part of the installation specification, i.e.
within the corresponding section of the Kickstat file. To simplify the
management of the download URLs, they are offloaded to an include file
named \'fedora-repo.ks\'. In this file you can easily manage different
Fedora versions and download sources without disturbing the flow in the
Kickstart file.

You have to create this file in your working directoy. In this example
we name it &#96;fedora-repo.ks&#96; which is the same name as Fedora is
using. This way you can contribute your work as you go.

The exact content depends entirely on local conditions. The basis is the
following sample:

    […]$ vim ~/imagefactory/fedora-repo.ks

    \&#35; Include the appropriate repo definitions
    \&#35; uncomment the repo specification to use.

    \&#35; Fedora Release mirrors
    \&#35;repo --name=fedora  --mirrorlist=https://mirrors.fedoraproject.org/mirrorlist?repo=fedora-37\&amp;arch=x86_64
    \&#35;repo --name=updates --mirrorlist=https://mirrors.fedoraproject.org/mirrorlist?repo=updates-released-f37\&amp;arch=x86_64
    \&#35;url                 --mirrorlist=https://mirrors.fedoraproject.org/mirrorlist?repo=fedora-37\&amp;arch=x86_64


    \&#35;\&#35; Regional Fedora release mirror (F37 / x86_64)
    \&#35;repo --name='fedora-rwth'  --baseurl=http://ftp.halifax.rwth-aachen.de/fedora/linux/releases/37/Server/x86_64/os
    \&#35;repo --name='updates-rwth'  --baseurl=http://ftp.halifax.rwth-aachen.de/fedora/linux/updates/37/Everything/x86_64/
    \&#35; Use network installation
    \&#35;url --url='http://ftp.halifax.rwth-aachen.de/fedora/linux/releases/37/Everything/x86_64/os/'


    \&#35;\&#35; Koji image creation (branched development tree)
    repo --name='koji-override-0' --baseurl=https://kojipkgs.fedoraproject.org/compose/branched/Fedora-38-20230312.n.0/compose/Everything/x86_64/os
    repo --name='koji-override-1' --baseurl=https://kojipkgs.fedoraproject.org/compose/branched/Fedora-38-20230312.n.0/compose/Server/x86_64/os
    \&#35; Use network installation
    url --url='https://kojipkgs.fedoraproject.org/compose/branched/Fedora-38-20230312.n.0/compose/Everything/x86_64/os'

#### The template file {#_the_template_file}

The template file describes meta data of the disk image to create. That
includes the repository to download and the size of the disk image.
Don't worry too much about the download URL. It will be overwritten by
the kickstart file.

Fetch the corresponding [basic template
file]({attachmentsdir}/tutorials/imagefactory/fedora-server-kvm-dev.tdl)
and store it into the working directory. In many cases klicking the link
stores the file into you default download directory, \~/Downloads in
case of Fedora desktops or Macs.

    […]$ mv ~/Downloads/fedora-server-kvm-dev.tdl  ~/imagefactory/

The version number inside the template file (22) is not necessarily the
Fedora target version. For some reason it is best to leave it untouched!
But you have to adjust the download URL!

## Working with FactoryImage {#_working_with_factoryimage}

### Create an image file {#_create_an_image_file}

1.  prepare and optimize kickstart file with ksflatten:

        […]$ ksflatten  -c fedora-server-kvm-dev.ks -o fedora-server-kvm-dev-fl.ks

2.  Check using ksvalidator

        […]$ ksvalidator -i fedora-server-kvm-dev-fl.ks

3.  Create the image

    Using a vm and guestfs-tools to adapt the image. This is the
    *preferred operation* mode.

        […]$ sudo imagefactory --debug base_image --file-parameter install_script \
        fedora-server-kvm-dev-fl.ks  fedora-server-kvm-dev.tdl \
        --parameter offline_icicle true

    The creation process takes some time. Therefore, the debug option
    provides some feedback about the progress.

    ImageFactory creates a non-system temporary VM to build the image,
    which is visible in Cockpit's VM list. It is usefull to watch the
    terminal window of this instance during the build. It shows a log of
    all the building steps and specifically errors or warnings.
    Unfortunately, the VM gets destroyed when Imagefactory finishes.

    Additionally, you find loging output in the /var/lib/oz directory.
    Often specifically useful are the (virtual) screenshots in the
    respective subdirectory.

4.  Output in case of a successful generation

        ============ Final Image Details ============
        UUID: 4ebde351-e81b-427f-96b7-5acd5680013d
        Type: base_image
        Image filename: /var/lib/imagefactory/storage/4ebde351-e81b-427f-96b7-5acd5680013d.body
        Image build completed SUCCESSFULLY!

### Check out a created image file {#_check_out_a_created_image_file}

To access the filesystem inside a generated image, use guestfs-tools.
Ensure that the image in *not used* in an active VM.

1.  Copy the generated vm into the libvirt installation media pool

        […]\&#35; qemu-img convert -c -O qcow2 /var/lib/imagefactory/storage/xxx-yyy-zzz.body /var/lib/libvirt/boot/fedora-server-kvm-dev.qcow2

2.  Check and analyze the file system

        […]\&#35; cd /var/lib/libvirt/boot
        […]\&#35; guestfish -a fedora-server-kvm-dev.qcow2
        Welcome ….
        \&gt;\&lt;fs\&gt; run
        \&#8230;(wait)
        \&gt;\&lt;fs\&gt; list-filesystems
        /dev/\&#8230;
        \&gt;\&lt;fs\&gt; quit

3.  Mount the file system(s)

    Following the list of file systems above, mount each filesystem and
    check

        […]\&#35; mkdir /mnt/test
        […]\&#35; guestmount -a fedora-server-kvm-dev.qcow2  -m /dev/xxx/yyy  /mnt/test

4.  Clean up

        […]\&#35; mkdir /mnt/test
        […]\&#35; guestmount -a fedora-server-kvm-dev.qcow2  -m /dev/xxx/yyy  /mnt/test

### Instantiate and test a created image {#_instantiate_and_test_a_created_image}

1.  Copy the generated vm into the libvirt disk image pool

        […]\&#35; cp  /var/lib/libvirt/boot/fedora-server-kvm-dev.qcow2 /var/lib/libvirt/images/vm-test.qcow2

2.  Instantiate a VM

        […]\&#35; virt-install  --name vm-test \
        --memory 4096  --cpu host --vcpus 2 --graphics none\
        --os-variant fedora-unknown\
        --import  \
        --disk /var/lib/libvirt/images/vm-test.qcow2,format=qcow2,bus=virtio \
        --network type=direct,source=enp1s0,source_mode=bridge,model=virtio \
        --network bridge=virbr0,model=virtio

Follow the steps as specified in [Creating a virtual machine using
Fedora Server Edition disk image -- Minimal initial
configuration](virtualization/vm-install-diskimg-fedoraserver.adoc&#35;_minimal_initial_configuration).

### Adjust the Kickstart file {#_adjust_the_kickstart_file}

You are ready now to modify the Kickstart file according your local
requirements and create an image and test it again and again.

# Installing Wordpress CMS {#_installing_wordpress_cms}

Peter Boy (pboy) :page-authors: Peter Boy

> Wordpress is a common blog system that can also be used for simple
> websites. Fedora includes an RPM package, so the installation is very
> simplified. This article focuses on Fedora-specific implementation
> details.

*Wordpress* is a widely used application and there is a corresponding
amount of information on the Internet. The Wordpress project itself
provides extensive [upstream
documentation](https://wordpress.org/documentation/).

:::: tip
::: title
:::

*For the sake of completeness*: Even though Wordpress is widely used,
you should carefully consider whether you really need a dynamic CMS that
generates every page with every request anew.

&#42; If your pages remain largely unchanged once they have been
created, various static site generators are probably more practical and
less time-consuming to maintain. &#42; Be prepared for the fact that the
ongoing operation of Wordpress requires considerable effort. Wordpress
is known for recurring security issues and requires ongoing attention
and maintenance.

\+ At minimum, Wordpress should be installed in a container. Fedora
Server offers several options for this, including some with little
additional management effort.
::::

The Fedora Wordpress RPM installs a closely upstream Wordpress while
integrating as smoothly as possible into the Fedora runtime environment.

Another good first overview provides the [*Fedora
Magazine*](https://fedoramagazine.org/) article [How to install
WordPress on Fedora
(2017)](https://fedoramagazine.org/howto-install-wordpress-fedora/).

## Prerequisites {#_prerequisites_3}

&#42; We assume a correctly installed Fedora Server Edition release 38
or 39. For details see [Fedora Server Installation
Guide](:installation/index.xml).

&#42; Wordpress stores most of the content in a database. Accordingly,
it requires access to a working database system and doesn't even startup
without. Currently, it [no longer enables to use
PostgreSQL](https://wordpress.org/plugins/postgresql-for-wordpress/),
the Fedora Server Edition preferred and specifically supported database
system. It just supports MariaDB or MySQL, which are included in Fedora
as well.

\+ So you have to install either MariaDB or MySQL following [Installing
MySQL/MariaDB](:quickdocs/installing-mysql-mariadb.xml). In terms of
Wordpress, both systems work equally smoothly. Following Fedoras
preferrence for truely OSS software we use MariaDB here.

\+ Before you start installation, create the [required
storage](:installation/index.adoc&#35;_storage_organization). The
easiest and quickest way is to use Cockpit (select the storage tab and
then the appropriate Volume Group in the upper right corner).

&#42; Furthermore, Wordpress needs a web server to deliver the pages.
Fedora Server Edition and the Fedora WordPress package support *httpd*,
the Fedora version of the Apache Web server. Of course, other Web
servers are also possible here. You will then have to do the adaptation
to Wordpress yourself.

\+ If not already done install the [Fedora Web Server
package](services/httpd-basic-setup.xml). If your server will just
server the Wordpress site, you may omit the section \'Setup a Web
site\'.

## Installing Wordpress {#_installing_wordpress}

1.  Install the WordPress Package. It automatically installs PHP as a
    dependency, too.

    ``` bash
    […]\&#35; dnf install  wordpress
    ```

2.  Add a database and a database user for Wordpress to the MariaDB DB.

    ``` bash
    […]\&#35; mysql -u root
    MariaDB [(none)]\&gt; show databases;
    MariaDB [(none)]\&gt; CREATE DATABASE wordpress ;
    MariaDB [(none)]\&gt; CREATE USER 'wordpress'   IDENTIFIED BY 'wp-test-proj';
    MariaDB [(none)]\&gt; GRANT ALL PRIVILEGES ON wordpress.\&#42;  TO 'wordpress';
    MariaDB [(none)]\&gt; quit;
    […]\&#35;
    ```

3.  Check the database connectivity via TCP/IP

    ``` bash
    […]$ mysql -u wordpress wordpress  -p
    Enter password:
    Welcome to the MariaDB monitor.  Commands end with ; or \g.
    Your MariaDB connection id is 18
    Server version: 10.5.20-MariaDB MariaDB Server

    Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

    Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.‘

    MariaDB [wordpress]\&gt; quit
    […]$
    ```

4.  Configure Wordpress to access the database defined above

    Edit the Wordpress configuration file which is *in Fedora* stored at
    /etc/wordpress (to achieve full Fedora integration).

    ``` bash
    […]\&#35; vim /etc/wordpress/wp-config.php
    define( 'DB_NAME', 'xxxxx' );
    define( 'DB_USER', 'xxxx' );
    define( 'DB_PASSWORD', 'xxxxxxxx' );
    define( 'DB_HOST', 'xxxx' );
    ```

5.  Enabling public access

    For security reasons, the default configuration restricts access to
    the local system, which is usually not why you install Wordpress.
    You have to edit the cpnfiguration file.

    ``` bash
    […]\&#35; vim /etc/httpd/conf.d/wordpress.conf

    Alias /wordpress /usr/share/wordpress

    \&#35; Access is only allowed via local access
    \&#35; Change this once configured

    \&lt;Directory /usr/share/wordpress\&gt;
    AllowOverride Options
    \&#35;Require local                       \&#35; \&lt;== mod
    Require all granted                  \&#35; \&lt;== add
    \&lt;/Directory\&gt;
    ```

6.  Protect your site during configuration and development

    Usually, it takes some time to configure the site and especially to
    develop the content. During this period you may want to restrict
    access to developers and peers only.

    Modify the configuration file further and append at the end:

    ``` bash
    […]\&#35; vim /etc/httpd/conf.d/wordpress.conf

    Alias /wordpress /usr/share/wordpress

    \&#35; Access is only allowed via local access
    \&#35; Change this once configured
    \&#8230;
    \&#8230;
    \&lt;/FilesMatch\&gt;
    \&lt;/Directory\&gt;

    \&#35;\&#35; Append the following lines to temporarily
    \&#35;\&#35; protect access to the wordpress page
    \&lt;Location /wordpress\&gt;
    AuthType Basic
    AuthName 'Access for developers only'
    AuthUserFile auth.d/validusers
    Require valid-user
    \&lt;/Location\&gt;
    ```

    Provide authentication information

    ``` bash
    […]\&#35; mkdir /etc/httpd/auth.d
    […]\&#35; htpasswd -c /etc/httpd/auth.d/validusers {USER}
    New password:
    Re-type new password:
    ```

7.  Finally start the Web Server

    ``` bash
    […]\&#35; systemctl enable httpd
    […]\&#35; systemctl start httpd
    […]\&#35; systemctl status httpd
    ```

## Check out and configure your site {#_check_out_and_configure_your_site}

1.  On your desktop open a Broser and navigate to the base address of
    the site you just configured:

    ``` bash
    http://example.com
    ```

    Note: Currently no SSL access is defined, only http protocol is
    available.

    The Fedora default page is displayed.

    ![Fedora default page](tutorials/wordpress/fedora-default-page.png)

2.  Your wordpress installation is available at

    ``` bash
    http://example.com/wordpress
    ```

    If you implemented the access restriction as proposed, you get the
    default Apache login screen. Otherwise and after authentication you
    see the basic Wordpress graphical configuration page.

    ![Fedora default
    page](tutorials/wordpress/initial-installation-page.png)

    Complete the various items as appropriate.

## Final fine tuning {#_final_fine_tuning}

After completing the site design and content and launching the site, you
may want to adjust various parameters to your liking. Among others

&#42; Customize the base address

\+ Specifically you want to modify the base address of your Wordpress
site, from wordpress to e.g. mycuteblog. Edit the Wordpress Apache
configuration file:

\+

``` bash
[…]\&#35; vim /etc/httpd/conf.d/wordpress.conf
\&#35;\&#35; Alias /wordpress /usr/share/wordpress  \&#35; \&lt;== Mod
Alias /mycuteblog  /usr/share/wordpress   \&#35; \&lt;== Add

[…]\&#35; systemctl restart httpd
```

&#42; Alternatively you may want to access the Wordpress pages at your
servers base address, example.com in this guide. Again, modify the
Wordpress Apache configuration file.

\+

``` bash
[…]\&#35; vim /etc/httpd/conf.d/wordpress.conf
\&#35;\&#35; Alias /wordpress /usr/share/wordpress  \&#35; \&lt;== Mod
\&#35;\&#35; Access wordpress via base address instead \&#35; \&lt;== Add
DocumentRoot /usr/share/wordpress            \&#35; \&lt;== Add

[…]\&#35; systemctl restart httpd
```

# Fedora Server on ARM Single Board Computers - the Raspberry Pi &amp; Co. {#_fedora_server_on_arm_single_board_computers_the_raspberry_pi_amp_co}

Fredrik Arneving; Peter Boy; Jan Kuparinen :page-authors: Peter Boy,
Kevin Fenzi, Jan Kuparinen

> Fedora has already supported the ARM architecture, and specifically
> ARM Single Board Computers (SBCs), for quite some time. Especially for
> these there is also a Fedora Server Edition installation medium
> available. But there are a number of pitfalls to be aware of.

Once started as an experimentation and education tool, the technology
evolved into an affordable but sufficiently powerful tool for many tasks
of everyday life. Even though these devices are very miniature and
limited in power, they offer enough strength, to install a dedicated
modern, solid Linux system. This is especially true for the newer
alternatives to the well known Raspberry Pi.

SBC Fedora Server Edition takes advantage of the power available on SBC
today to install a dedicated modern, solid server system. In the end
Fedora Server works on application level exactly as otherwise familiar.

But not all SBC models are equally or similarly capable for a Fedora
Server deployment.

## Required Device capabilities {#_required_device_capabilities}

&#42; The Fedora Server Edition is only available for ARMv8/aarch64.

&#42; A fast wired network adapter is needed. Some SBCs do not have a
dedicated Ethernet interface, but you need a USB adapter. Often only USB
2.0 is available for this or the Ethernet interface is connected
internally via a USB 2.0 hub.

&#42; A fast, internal mass storage is required. The always available
mSD card is sufficient for installation, but not for operation. An NVMe
board connected via PCIe is optimal.

&#42; Finally, a solid casing is also necessary so that the device
cannot suffer accidental damage during operation. The common DIY
housings are not enough.

These are just a few criteria that certainly need to be expanded.

## Supported by Fedora {#_supported_by_fedora}

Almost all board makers are very enthusiastic about using the open
source Linux system to make their hardware usable at all and attractive
to a wider audience, saving them the development of their own operating
system or the licensing costs for a commercial system. They focus on the
development of device drivers for their hardware, instead. In fact, to
even boot, many of them require device specific software.

Unfortunately, manufacturers are sometimes much less enthusiastic to
make these drivers freely available under an open source license and to
integrate them into the mainline kernel. Their models are working with
Linux, but only in a proprietary tainted version, propriarily customized
by the manufacturer.

Fedora is dedicated and uncompromisingly Free Software, for good reason.
All software involved must be open source and freely available. Fedora
uncompromisingly insists on the reproducibility of all software
components on their own hardware and under their complete control -
especially for security and anti-fraud reasons.

*Therefore, Fedora cannot and will not support boards that rely on
proprietary software.*

*Fedora compatible* are only those SBCs for whose components either the
manufacturer contributes open source drivers or alternate community
developed drivers are available.

[Arm SIG](https://fedoraproject.org/wiki/Architectures/ARM) provides a
list of devices that are operable with Fedora.

## Appropriate for Fedora Server Edition {#_appropriate_for_fedora_server_edition}

Supported by Fedora is not a true/false alternative but a matter of
degree and intended purpose. A specific SBC model may be able to boot
with Fedora and pure free software, but e.g. graphics acceleration or
WiFi does not work. As a graphical device, this is not usable, but
Fedora Server wouldn't bother because it is not used anyway. If PCIe and
an m.2 interface are then available, the model would be more suitable
for Fedora Server than a fully compatible device including accelerated
graphics, but without a PCIe-attached m.2 interface.

Thus, the question of appropriateness depends much on several criteria
and intentions of use.

## How Fedora supports the diversity of Single Board Computers {#_how_fedora_supports_the_diversity_of_single_board_computers}

Fedora distributes a generic Fedora Server Edition image, preconfigured
for Raspberry Pi. Additionally, it provides a utility to transfer the
image to the prospective boot medium, usually an SD card. To support
multiplemodels, the transfer program is able to (re-)configure the disk
image for an alternative SBC model. Optionally, it can also make some
adjustments to the initial configuration.

## Conclusion {#_conclusion_3}

The choice of an SBC model therefore requires careful consideration if
you do not want to end up in a dead end. Fedora IoT Edition provides a
concise list of references. A detailed reference list is also in
preparation for Fedora Server.

:::: warning
::: title
:::

When choosing a device for Fedora Server, check carefully if the
available hardware capabilities are compatible with the intended use and
are actually supported by Fedora. Take everything with a grain of salt.
Don't expect everything to work just smoothly with SBCs. It is best to
ask in advance on the arm mailing list.
::::

# Installation based on *u-boot* {#_installation_based_on_u_boot}

Fredrik Arneving; Peter Boy; Emmanuel Seyman :page-authors: Peter Boy,
Kevin Fenzi, Jan Kuparinen

> ARM Single Board Computers originally had only *one data storage
> medium*, an SD card. And they use to have no BIOS or equivalent
> firmware to initialize the hardware at boot time and make it
> accessible. The operating system has to provide this function, too.
> The u-boot bootloader is one of several options for providing this
> function. Therefore, the installation method for SBC devices works
> quite differently from what is otherwise known from Fedora.

## How it works {#_how_it_works_6}

Even though many SBC devices now also feature eMMC modules or m.2 NVMe
interfaces, the boot process remains very simple. The minimal firmware
continues to boot from the SD card, and possibly supplementally from
eMMC or an SPI flash module. The device expects a ready-to-use operating
system, configured precisely for the respective hardware, including
low-level hardware initialization.

A widely used software that provides this functionality is the
bootloader *u-boot*. It is basically a collection of low-level,
model-specific device drivers.

Instead of creating a separate distribution file for each model, Fedora
Server Edition is distributed as an *unified basic image file*. The
installation program *arm-image-installer*, transfers this image file to
the designated storage medium and then adds model-specific u-boot
bootloader files.

Even though the installation works quite differently, Fedora Server
ultimately functions just like usual at the application level.

## Prerequisites {#_prerequisites_4}

&#42; Of course, you need a &#42;suitable single board computer&#42;
model, *supported by Fedora* and with a network connection, keyboard and
display. A simple text console is perfectly sufficient.

\+

:::: warning
::: title
:::

The critical passage is \'supported by Fedora\'. When choosing a device
for Fedora Server, check carefully if it is really actually supported.
Unlike the x86 universe, don't expect everything to work just as
smoothly in ARM rsp. aarch64. Take everything with a grain of salt. It
is best to ask in advance on the arm mailing list or Matrix room.
::::

&#42; A &#42;Fedora system&#42;, which provides the Fedora utility
program, *arm-image-installer*.

\+ The utility should basically be usable with any Linux desktop, but
not with Windows or MacOS. You have to install VirtualBox or any other
virtualization software that is able to provide direct access to the
physical USB port or SD card slot, and install Fedora as a guest system.

&#42; A &#42;pluggable disk&#42; of suitable size, practically, this is
either an SD card or eMMC storage on a removable daughter board. The
absolute minimum capacity is 8 GB, but a capacity of 32 GB should be
fine and affordable nowadays.

## Special considerations: Organization of the storage area {#_special_considerations_organization_of_the_storage_area}

Basically, Fedora Server on SBC follows the same storage configuration
principles as on \'full-blown\' Server Hardware. Please, read the
section \'Storage organization\' in the [installation
overview](installation/index.adoc&#35;_storage_organization) and the
supplementary information in the [Post installation
tasks](installation/postinstallation-tasks.adoc&#35;_consolidate_storage_configuration)
section. Fedora Server Edition implements this principle, which
originated in professional IT, *on SBCs* as well.

Fedora uses UEFI as the boot system, but on SBCs it still uses a DOS/MBR
partition table. Therefore, it first creates a FAT partition for EFI and
a small /boot partition, used by grub2 bootloader. Thereafter, it
creates another partition including one LVM volume group (VG) as
described in the forementioned guide.

For practical reasons, the downloaded deliverable is limited to just
under 8 GB in total. During or after installation, the size is adjusted
to the existing hardware.

## Handling different boot media {#_handling_different_boot_media}

Many SBC models today offer additionally alternative storage media,
especially eMMC memory, either pluggable or soldered. Nevertheless, the
installation procedure remains basically the same.

These SBCs can alternatively boot and operate directly from this
remarkable faster memory. A pluggable memory can be connected to the
desktop with an adapter. It is then the target for the image transfer,
instead of the SD card. instead of the SD card. In case of soldered
memory, you must first go through the installation process with the SD
card, and then use that system to copy an installation image to the
internal eMMC memory in a second step.

Some models provide a special flash module (SPI) to store a custom
bootloader. For these cases, the u-boot bootloader offers a special
format that is flashed onto the SPI module. This requires a
board-specific tool independent from Fedora. The Fedora Server unified
basic image file is transferred to the installation medium unchanged.

These bootloaders quite often support extended options to boot from,
e.g. NVMe boards, SATA drives, or USB sticks.

Here we describe the basic steps for creating a customized boot medium
(SD card or eMMC module).

## Steps to install Fedora Server Edition on a Single Board Computer {#_steps_to_install_fedora_server_edition_on_a_single_board_computer}

### Preparations {#_preparations_3}

1.  On your Fedora system, install arm-image-installer

    ``` bash
    […]$ sudo dnf -y install  arm-image-installer uboot-images-armv8.noarch
    ```

2.  Set the download directory as default, fetch a Fedora Server aarch64
    system disk raw image, here F43, and check the integrity of the
    download.

    ``` bash
    […]$ cd ~/Downloads
    […]$ wget https://download.fedoraproject.org/pub/fedora/linux/releases/43/Server/aarch64/images/Fedora-Server-Host-Generic-43-1.6.aarch64.raw.xz
    […]$ wget https://download.fedoraproject.org/pub/fedora/linux/releases/43/Server/aarch64/images/Fedora-Server-43-1.6-aarch64-CHECKSUM
    […]$ sha256sum -c \&#42;-CHECKSUM  --ignore-missing
    Fedora-Server-Host-Generic-43-1.6.aarch64.raw.xz: OK
    sha256sum: WARNING: 17 lines are improperly formatted
    ```

    The result message includes a complain about some not correct
    formated lines. It can savely be ignored.

3.  Connect your Micro SD card to your desktop. Identify the device
    name.

    ``` text
    […]$ lsblk
    NAME              MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
    sda                 8:0    0 596,2G  0 disk
    ├─sda1              8:1    0   600M  0 part /boot/efi
    ├─sda2              8:2    0     1G  0 part /boot
    ├─sda3              8:3    0    30G  0 part
    │ └─sysvg-root    253:0    0    15G  0 lvm  /
    └─sda4              8:4    0 564,6G  0 part
    ├─usrvg-var_log 253:1    0     5G  0 lvm  /var/log
    └─usrvg-libvirt 253:2    0   200G  0 lvm  /var/lib/libvirt
    mmcblk0           179:0    0  29,5G  0 disk
    └─mmcblk0p1       179:1    0  29,5G  0 part
    zram0             252:0    0   7,5G  0 disk [SWAP]
    ```

4.  In the above example the device is obviously */dev/mmcblk0* and its
    partition (mmcblk0p1) is not mounted anywhere. If it were, you would
    have to unmount the device.

    ``` bash
    […]$ sudo umount /dev/mmcblk0p1
    ```

5.  Identify the name of the support files for your board

    ``` bash
    […]$ sudo arm-image-installer --supported
    AllWinner Devices:
    A10-OLinuXino-Lime A10s-OLinuXino-M A13-OLinuXino A13-OLinuXinoM A20-OLinuXino-Lime A20-OLinuXino-Lime2
    A20-OLinuXino-Lime2-eMMC A20-OLinuXino_MICRO A20-Olimex-SOM-EVB Ampe_A76 Auxtek-T003 Auxtek-T004 Bananapi
    \&#8230;
    TI Devices:
    am335x_evm am57xx_evm kc1 omap3_beagle omap5_uevm omap4_panda
    Note: For the am33xx BeagleBone devices use 'am335x_evm', BeagleBone AI use 'am57xx_evm'

    MVEBU Devices:
    clearfog helios4

    ST Devices:
    stih410-b2260

    Other Devices:
    arndale chiliboard cl-som-am57x rpi2 rpi3 rpi4 olpc_xo175
    ```

    If you don't find your board, check the *boards.d* directory
    directly just in case the list is not up to date.

    ``` bash
    […]$ ls -al /usr/share/arm-image-installer/boards.d  |  less
    ```

    As an example., you will find the PINE64 \'ROCKPro64\' model as
    \'rockpro64-rk3399\'

6.  Transfer the raw disk image to the micro SD card

    ``` bash
    […]$ sudo arm-image-installer --image=Fedora-Server-Host-Generic-43-1.6.aarch64.raw.xz --target=rockpro64-rk3399  --media=/dev/mmcblk0
    ```

    Just in case you already decided to fill the complete space on disk
    with the root file system and to dispense with segmentation, you may
    add the resizefs parameter which would result in an *alternative
    command line*:

    ``` bash
    […]$ arm-image-installer --image=Fedora-Server-Host-Generic-43-1.6.aarch64.raw.xz --target=rockpro64-rk3399 --resizefs --media=/dev/mmcblk0
    ```

    Remember, this is definitely *not a recommended option* for serious
    production server operation!

    Consult the [ARM Installation
    Guide](https://fedoraproject.org/wiki/Architectures/ARM/Installation&#35;Arm_Image_Installer)
    for a complete description of the available options.

7.  After the transfer is complete, unmount the SD card again if it was
    automatically re-mounted, and disconnect it.

### Basic installation and configuration {#_basic_installation_and_configuration}

At the SBC terminal, we perform only the minimum, absolutely necessary
configuration, namely the creation of a user including password and
administrative privileges. Just in case your network doesn't provide
DHCP, you have to configure the IP address as well. Everything else can
be more conveniently accomplished via ssh or Cockpit from the desktop.

1.  make sure that the SBC is disconnected from power.

2.  Connect monitor, keyboard and network cable, insert the micro SD
    card.

3.  Connect the SBC to power and wait. After some time a lot of messages
    scroll across the screen. If the network interface doesn't provide
    DHCP, in includes a NetworkManager error message. You can safely
    ignore it for now. It finally ends with a simple, text-based input
    mask for the first boot configuration.

        SoC Rockchip rk3399
        Reset cause: POR
        Model: Pine64 RockPro64 v2.1
        \&#8230;
        \&#8230;
        [  OK  ] Reached target nss-user-lo \&#8230; User and Group Name Lookups.
        Starting systemd-logind.se\&#8230; User Login Management \&#8230;
        [  OK  ] Finished dreacut-shutdown,s \&#8230;. /run/initramfs on shurtdown.
        ================================================================================
        ================================================================================

        1) [x] Language settings                 2) [x] Time settings
        (English (United States))                (US/Eastern timezone)
        3) [x] Network configuration             4) [x] Root password
        (Connected: end0)              (Root account is disabled)
        5) [ ] User creation
        (No user will be created)

        Please make a selection from the above ['c' to continue, 'q' to quit, 'r' to
        refresh]:

    The menu is quite simple and a bit old-fashioned, but effective and
    straightforward. Select the item you want to configure by entering
    the digit in front of it and then follow the corresponding submenu
    displayed in the same way. An \'X\' in the square bracket indicates
    that an item is already configured or preconfigured with default
    values.

4.  The most important item is the configuration of an admin user and
    their password. Type 5 to enter the submenu.

        ================================================================================
        ================================================================================

        User creation

        1) [ ] Create user

        Please make a selection from the above ['c' to continue, 'h' to help, 'q' to
        quit, 'r' to refresh]:

        1

        ================================================================================
        ================================================================================

        User creation

        1) [x] Create user
        2) Full name
        3) User name
        4) [x] Use password
        5) Password
        6) [x] Administrator
        7) Groups
        wheel

        Please make a selection from the above ['c' to continue, 'h' to help, 'q' to
        quit, 'r' to refresh]:

    The \'\[x\]\' in front of Create user indicates that you entered
    \'1\' (to create user) and now the user creation process is active.
    Accordingly, password authentication is enabled for the new user as
    well as administrator privileges and membership of the wheel group.

    Fill in the full name, the user name and the password. If you are on
    a non-US keyboard note that no keyboard mapping is active and limit
    yourself to universal standard ASCII characters and avoid special
    characters for now. Otherwise, you might later not be able to enter
    the password correctly, because a different keyboard mapping
    applies. You can change the password to a more secure value later.
    In any case ensure that you keep administrator privileges unchanged!

    If you enter a \'c\', the user configuration will be closed and you
    will return to the original main menu.

5.  If you do not live in the US/Eastern time zone, it would be wise to
    set it here as well. It is very simple and straight forward in the
    menu. Type \'2\' and select the correct values from the lists. Enter
    \'c\' to close it.

    Usually, leave the ntp server as is.

    If you are uncomfortable with the entry here, you can also enter
    this and all the following information later comforatbly with the
    Web interface.

6.  If you don't have a DHCP server on your LAN you may configure
    network connection in this menu or use the command line in the next
    stage. Specifically it you use a non-US keyboard it may be tedious
    and error prone to use this menu.

    Even with DHCP active, it may be useful to set the hostname here, so
    that an internal DHCP-based name server receives the correct name
    immediately. Type \'3\' and fill in your hostname.

7.  Finally, type \'c\' to exit the first-boot configuration menu and
    complete the basic configuration. After some waiting, the Fedora
    Server login prompt appears.

    ``` teyt
    Fedora Linux 43 (Server Edition)
    Kernel x.y.z-rrr.fc43.aarch64 on an aarch64 (tty1)

    Web console: https://localhost:9090/ or https://uuu.vvv.www.xxx:9090/

    rockpro login:
    ```

    The hostname here is default, because the box didn't receive a name
    from DHCP during first boot. Please note the IP address to use next
    with ssh or Cockpit.

    :::: important
    ::: title
    :::

    Always complete this step and close with \'c\'. Otherwise this
    installation routine can on reboot again and again conflict with the
    subsequent configuration.
    ::::

8.  If you have the network connection ready, you can now disconnect
    monitor and keyboard. The next steps all happen on the desktop.

    Otherwise configure the network connection now.

    a.  Login with your administrative account

    b.  If you are a non-US keyboard user, configure your keyboard
        mapping. Fist list the available keyboard mappings and note the
        name of a suitable mapping, e.g. de-nodeadkeys. Then configure
        it.

        ``` bash
        […]$ localectl list-keymaps
        […]$ sudo localectl setkeymap de-nodeadkeys
        ```

        The mapping is imediately active.

    c.  Configure and activate the network. Adjust the IP, gateway and
        network settings accordingly.

        First, check the existing interfaces.

            […]\&#35; nmcli con
            NAME                  UUID                                  TYPE      DEVICE
            'Wired connection 2'  8d971f49-033f-398a-9714-3a4e848178fb  ethernet  enp2s0

        Most likely your interfaces are named somewhat awkward way.
        Let's fix that to make administration of network easier and more
        comfortable. Don't forget to adjust the naming to your specific
        installation!

            […]$ sudo nmcli con mod 'Wired connection 1' connection.id end0

            […]$ sudo nmcli con mod end0 \
            ipv4.method manual \
            ipv4.address 'xxx.xxx.xxx.xxx/yy' \
            ipv4.gateway 'xxx.xxx.xxx.zzz' \
            ipv4.dns 'xxx.xxx.xxx.vvv' \
            ipv6.method manual \
            ipv6.addresses xxxx:xxxx:xxxx:xxxx::yyyy/64 \
            ipv6.gateway xxxx:xxxx:xxxx:xxxx::zz \
            ipv6.dns 'xxxx.xxxx.xxxx.xxxx::vvv'  \
            connection.zone 'FedoraServer'

            […]$ sudo nmcli con up end0
            […]$ sudo systemctl  restart  NetworkManager

    d.  Reboot. You can then disconnect monitor and keyboard. The next
        steps all happen on the desktop.

### Final Configuration {#_final_configuration}

1.  On your desktop open a Browser. If you already set the correct
    hostname and DNS entry, use that. Otherwise, use the IP address for
    now. In the example above it is *<http://192.168.158.172:9090>*.
    After accepting a warning message due to a missing certificate,
    voilà, the Cockpit administration interface of your SBC appears.

    ![Cockpit Login Screen](installation/on-sbc-020.png)

2.  Login with your administrative account to continue configuration.

    ![Cockpit Overview Screen](installation/on-sbc-030.png)

    Activate administrative permissins in the top bar.

3.  First &#42;adjust hostname&#42;

    In the Box \'Configuration\' click on \'*edit*\' beside the hostname
    and enter a short name (display name) and a fqdn name.

4.  &#42;Adjust time and time zone&#42; if necessary and not already
    done. Click on system time and select the time zone. Automatic time
    synchronization should already be enabled.

    If a local time server is available in your network, it can be
    entered here. Many routers offer such a function and relieve the
    infrastructure.

5.  If you are non-US you may want to &#42;&#42;set your
    language&#42;&#42;. In any case, you should choose the
    &#42;&#42;keyboard layout&#42;&#42; correctly. Otherwise, in case of
    an emergency you may have to use a directly attached monitor and
    keyboard again, you need a correct mapping to act efficiently.

    Select \'Terminal\' in the left navigation menu. You get a terminal
    access to your device, already logged in with your account.

    a.  List available languages by \'*localectl list-locales*\'. Find
        your locale in the list and note the token, e.g. de_DE.UTF-8.
        Set the language with \'*sudo localeectl set-locale
        LANG=TOKEN*\', e.g. \'*sudo localeectl set-locale
        LANG=de_DE.UTF-8*\'.

    b.  List available keyboard mappings by \'*localectl
        list-keymaps*\'. Find your keymap in the list and note the
        token, e.g. de-nodeadkeys. Set the keymap with \'*sudo localectl
        set-keymap MAP_TOKEN*\', e.g. \'*sudo localectl set-keymap
        de-nodeadkeys*\'.

    c.  Finally check by \'*localeectl*\'

6.  To be able to access your account via ssh, you should install your
    public ssh key.

    Select \'accounts\' in the left navigation column and choose your
    account. At the bottom select \'Add Key\'. Copy&amp;paste your
    public key into the input field.

    If you chose a simple password during the basic installation, you
    should replace it with a more complex one at this occasion.

7.  Most likely, the packages of the distributed file image are not up
    to date. In the menu bar on the left, you will probably see an
    exclamation mark next to \'&#42;&#42;Software Updates&#42;&#42;\'.
    Select this menu item. A search for updates starts and after some
    time a list of updates appears. Select \'Install all updates\' and
    sit back. It will take a while.

    If the cockpit packages are also updated, the connection is
    interrupted. You must then reconnect.

    With everything done reboot the system. In the overview screen
    select either reboot or shutdown in the upper right corner. You can
    now use a shutdown to disconnect keyboard and monitor, if desired.
    You may also put the device in a different, final place. Start the
    device afterwards.

8.  When the device is up again it is time to &#42;&#42;test the
    installation&#42;&#42;.

    a.  If your DHCP is correctly configured, you should be able to
        &#42;find your device by name&#42; now. Close your browser
        window and start again. Write the device name and port number in
        the address field, e.g. <http://rockpro.example.com:9090> and
        Cockpit should come up again (after the usual warning about an
        insecure connection).

    b.  You should be able to log in via &#42;&#42;ssh and your
        key&#42;&#42;. Try *ssh -i .ssh/MYKEY rockpi.example.com* and
        after answering a question to accept the fingerprint you should
        gain access.

9.  Finally, depending on the use case, you may need to ensure you can
    always track which person was logged in and when. Use Cockpits
    account management feature to comfortably create additional users
    and grant them administrativ permissions (\'sudo\').

## Configuration of the storage area {#_configuration_of_the_storage_area}

As explained at the beginning, there are at least three alternatives to
organize the storage area.

1.  Filling all the space left after the base installation with the ROOT
    file system.

    This is the simplest solution and the only sensible one for disks of
    up to 16gb.

2.  Extend the partition and volume group to the remaining available
    disk space, extend the logical volume with the ROOT file system to
    about 12gb and leave the remaining area for logical volumes for
    dedicated payloads (database, libraries, etc.).

    This is the most flexible solution and preserves all options for the
    system administrator depending on the actual progression of usage.
    It is especially recommended for disks of 64gb and more, but should
    also be considered with a size of 32 gb.

3.  You may reinforce the rationale of separating system and user data
    even further and create a separate partition and volume group for
    user data. This seems a bit far-fetched for a (small) SBC, but is
    nevertheless worth considering if a very large volume and
    correspondingly a large amount of data are present (a rule of thumb:
    larger 500 GB).

### Enlarge partition and volume group to fill the disk space {#_enlarge_partition_and_volume_group_to_fill_the_disk_space}

Any of the alternatives as above start with the same administrative
tasks.

1.  Login via ssh or switch to terminal in Cockpit

2.  Use lsblk to determine the device name of your disk storage, most
    likely mmcblk1

3.  Invoke *sudo cfdisk* with that device name:

    ``` bash
    […]$ sudo cfdisk /dev/mmcblk1
    ```

4.  Select partition 3 (Type 8e Linux LVM) using &lt;Cursor down&gt; and
    then Resize using &lt;Curser left&gt;

    ![Partition resize](installation/on-sbc-090.png)

5.  The suggested size fills the complete disk.

    In case of &#42;alternative 1 or 2&#42; confirm with &lt;Return&gt;.

    In case of &#42;alternative 3&#42; select a size for system VG, as a
    rule of thumb at least 10GB, max. 30 GB.

    Select \'Write\', confirm resizing and quit the program.

6.  Resize the volume group

    ``` bash
    […]$ sudo pvresize  /dev/mmcblk1p3
    Physical volume '/dev/mmcblk1p3' changed
    1 physical volume(s) resized or updated / 0 physical volume(s) not resized
    ```

7.  Select \'Storage\' in Cockpit and inspect the Volume Group *fedora*
    in the upper right corner. The displayed size now shows an amount
    that indicates a complete fill of the entire disc rsp. as
    configured.

8.  A click onto the fedora volume group brings up the logical volume
    view. In the \'Logical volumes\' list expand the root LV
    (/dev/fedora/root).

    ![Volume resize](installation/on-sbc-100.png)

    For &#42;alternative 1.&#42; select \'Grow\' and expand the volume
    to fill the complete available space.

    For &#42;alternative 2.&#42; select \'Grow\' and expand the volume
    to sensible size. 10gb would be good to start with.

    For &#42;alternative 3.&#42; select \'Grow\' and expand the volume
    to a size that still leaves room for the unanticipated. An initial
    size for root between 8 and 12 GB would be good to start with.

9.  Go back to the terminal.

        […]$ sudo df -h

    Confirm that the size of the root file system is now of the
    specified value.

10. In case of alternative 3 use Cockpits storage to create an
    additional partition and volume group.

Later, when you install applications and services you will use Cockpit
storage to create logiocal volumes and mount them at the appropriate
location. As an example you may create a logical volume
\'*postgresdata*\', create an XFS filesystem and mount it at
*/var/lib/pgsql* before actually installing postgresql.

After all the major modifications to the file system, it is now
advisable to reboot before any further work is done.

## Troubleshooting {#_troubleshooting_2}

1.  At the first system start the grub2 boot screen is displayed
    briefly, then the monitor remains dark.

    Check if the network interface indicates a connection (the LEDs are
    on or blinking). In this case, it is likely that the device is fully
    booted and just the console interface is broken.

    Because in this case Cockpit is started and active on the device,
    use your Fedora desktop and search the network segment, e.g.
    192.168.158.0/24 for devices with active port 9090.

    ``` bash
    […]$ sudo dnf install nmap
    […]$ sudo nmap -Pn -p9090 192.168.158.0/24
    Starting Nmap 7.80 ( https://nmap.org ) at 2023-03-23 08:18 CEST
    Nmap scan report for fritz.box (192.168.158.1)
    Host is up (0.00052s latency).

    PORT     STATE  SERVICE
    9090/tcp closed nn-admin
    MAC Address: 34:81:C4:14:21:B4 (AVM GmbH)

    Nmap scan report for iMac.fritz.box (192.168.158.111)
    Host is up (0.00051s latency).

    PORT     STATE  SERVICE
    9090/tcp closed nn-admin
    MAC Address: 68:5B:35:97:9F:33 (Apple)
    \&#8230;
    \&#8230;
    Nmap scan report for raspi3.fritz.box (192.168.158.116)
    Host is up (0.00075s latency).

    PORT     STATE SERVICE
    9090/tcp open  nn-admin
    MAC Address: B8:27:EB:5A:EC:84 (Raspberry Pi Foundation)

    Nmap scan report for 192.168.158.172
    Host is up (0.00068s latency).

    PORT     STATE SERVICE
    9090/tcp open  nn-admin
    MAC Address: 06:BE:DE:31:C6:E2 (Unknown)
    \&#8230;
    \&#8230;
    Nmap done: 256 IP addresses (12 hosts up) scanned in 2.38 seconds
    ```

    Look for an entry with open state of port 9090 and no hostname or
    unknown hostname. Among them you will probably find the device you
    are looking for. In the example above it is 192.168.158.172.

    Enter the address *<https://192.168.158.172:9090>* into your
    browser. If successful, a cockpit login page opens, which simply
    outputs \'fedora\' as the hostname (in the lower part of the login
    widget). Otherwise, check the other suitable addresses.

    ![Cockpit Overview Screen](installation/on-sbc-060.png)

    Unfortunately you can't log in right now because you don't know the
    password.

    You have to rebuild the device operating system on SD card and add a
    SSH public key to be able to login via SSH as user root.

    Beforehand you need to create pair of SSH keys if not already exist.
    It is best to create the key in the .ssh subdirectory of your home
    dir. It should not be secured by password to enable automatic
    processing. The naming with leading \'id\_\' und trailing types
    abbreviation, e.g. \'\_rsa\' is just a common convention, yet
    helpful. Execute on the local desktop and adjust appropriately:

    ``` bash
    […]$ cd
    […]$ mkdir ~/.ssh
    […]$ ssh-keygen -t rsa -b 4096  -C 'root@example.com' -f ~/.ssh/\&lt;outputkeyfile\&gt;
    ```

    As an example you may use the name \'*id_mysbc_rsa*\'. Although the
    type rsa is widely used, you may adjust your key type accordingly.

    Turn off the SBC, remove the SD card and connect it to your desktop
    again as in section \'Preparations\'. Transfer the operating system
    image file again as in step 5 of that section but use an additional
    option:

    ``` bash
    […]$ cd
    […]$ sudo arm-image-installer --image=Fedora-Server-Host-Generic-43-1.6.aarch64.raw.xz --target=rockpro-rk3399 --addkey=~/.ssh/id_mysbc_rsa.pub  --media=/dev/mmcblk0
    ```

    When the process has finished, reinstall the CD card in the SBC, and
    connect to power to start the device again.

    Ping the address and as soon as you are connected, use ssh to log
    in.

    ``` bash
    […]$ ping 192.168.158.120
    […]$ ssh -i .ssh/id_mysbc_rsa  root@192.168.158.172
    ```

    You can now create an user account, set the password and add it to
    group wheel to grant administrative sudo privileges.

    In your browser open again <https://192.168.158.172:9090>, login
    with your account and proceed with section \'Final configuration\'.

# Frequently Asked Questions (FAQ) {#_frequently_asked_questions_faq}

Peter Boy; Jan Kuparinen :page-authors: Peter Boy, Kevin Fenzi

**Q:** Can I see a built preview of this template to get a better idea
about the result?

**A:** Of course you can! Just look at the README of the repository ---
it should tell you everything.

**Q:** Is writing documentation hard and dreadful?

**A:** Absolutely not (OK, just joking). Writing documentation in
asciidoc is very simple and straightforward. And in fact, writing
documentation makes you very happy. Just try and see for yourself!

**Q:** How do I manage SELinux issues?

**A:** First of all: Don't deactivate but resolve issues - (Link to
Server Sysadmin Cockpit page and Quick Docs)

# Communicating and Getting Help {#_communicating_and_getting_help}

Peter Boy; Jan Kuparinen :page-authors: Peter Boy, Kevin Fenzi

For general troubleshooting help related to Fedora, please refer to [Ask
Fedora Forum](https://ask.fedoraproject.org).

If you found a bug, report it!

&#42; [How to file a
bug](https://docs.fedoraproject.org/en-US/quick-docs/howto-file-a-bug/).

&#42; Issues about a server can be filed at [the ticketing repository on
Pagure](https://pagure.io/fedora-server/issues).

&#42; You can chat with us at [&#35;fedora-server on
libera.chat](https://web.libera.chat/?channels=&#35;fedora-server).

&#42; You can discuss server issues at [Server Discussion
Forum](https://discussion.fedoraproject.org/c/server).

&#42; You can e-mail us on the Server mailing list at
[server@lists.fedoraproject.org](https://lists.fedoraproject.org/admin/lists/server@lists.fedoraproject.org/).
