This page includes information about the software formats, tools and
repositories that are included in Fedora Workstation.

# Default Software Repositories {#_default_software_repositories}

Workstation comes with a set of software repositories enabled out of the
box. These allow preinstalled software to be updated, as well as new
packages and apps to be installed.

Workstation's default software repositories are:

&#42; Official Fedora RPM repositories. Workstation system components
and applications are provided in RPM format, using the main Fedora
repositories. &#42; Fedora Flatpaks. Workstation comes with the Flatpak
app distribution tool installed by default. It also includes a
repository of Flatpak apps, which are built and hosted by the Fedora
project, and which are available to be installed. &#42; Linux Vendor
Firmware Service (LVFS). Workstation uses fwupd to provide firmware
updates from LVFS. This is enabled by default.

# Third-Party Repositories {#_third_party_repositories}

Fedora Workstation also includes a set of [third-party
repositories](https://docs.fedoraproject.org/en-US/workstation-working-group/third-party-repos/).
These software repositories are provided by projects and organizations
other than Fedora, and provide access to a wider range of software than
the default offering. They can be enabled with the click of a button
during initial setup, or in the Software app.

# Installing &amp; Updating Software {#_installing_amp_updating_software}

Workstation includes the GNOME Software app, which makes it easy to find
and install apps, and to install software updates.

Workstation also comes with a set of command line tools that can be used
for software management. These are:

&#42; &#96;dnf&#96;: Fedora's default package manager. See [this
guide](https://docs.fedoraproject.org/en-US/quick-docs/dnf/) for
information on how to get started with DNF. &#42; &#96;flatpak&#96;: the
Flatpak tool can be used to install and update graphical applications
that are provided as Flatpaks. See [this
guide](https://docs.flatpak.org/en/latest/using-flatpak.html) to get
started with the Flatpak CLI. &#42; &#96;fwupdmgr&#96;: the command line
utility for fwupd. This can be used to update firmware.

# Release Schedule, Updates &amp; Upgrades {#_release_schedule_updates_amp_upgrades}

Fedora Workstation follows the [standard Fedora release
schedule](https://docs.fedoraproject.org/en-US/releases/): a new version
is produced every six months, and each version receives updates for 13
months.

Fedora's smooth upgrade process means that it's easy to stay up to date,
and transitioning from one version to the next is easy and pain free
(though we still recommend that you backup before upgrading). Upgrading
can be done using the Software app, which shows a notification when a
new version is available. You can also [upgrade using the command
line](https://docs.fedoraproject.org/en-US/quick-docs/dnf-system-upgrade/).

# Proprietary &amp; Patent Encumbered Software {#_proprietary_amp_patent_encumbered_software}

In accordance with Fedora principles and policy, Fedora Workstation only
includes open source software. Workstation is also prevented from
including patent-encumbered software. This poses challenges in cases
where such software is required by particular hardware or multimedia
formats.

Open source technologies are always the preferred option for
Workstation. However, in important cases where no viable open source
option exists, and where it is safe to do so, mechanisms are provided to
gain access to particular proprietary and patent encumbered software.

## NVIDIA Graphics {#_nvidia_graphics}

Fedora Workstation works to ensure that the open source Nouveau driver
provides an excellent experience for NVIDIA hardware. However, when
features that are exclusive to the proprietary driver are required, it
can be installed by enabling the Third Party Repositories.

## H.264 Codecs {#_h_264_codecs}

Due to patent issues, Fedora cannot distribute the H.264 multimedia
codec itself. However, Workstation does automatically install this codec
for users, from a non-Fedora source.

# Disk Configuration {#_disk_configuration}

Fedora Workstation uses a different default disk configuration from
other Fedora Editions and Spins. This page describes that configuration
along with the motivations behind it.

Other, non-default, disk configuration options are available to be used
with Workstation, and can be configured during the disk partitioning
step in the installer.

## Btrfs {#_btrfs}

Btrfs is the default filesystem used by Fedora Workstation. Btrfs has
two key advantages for users using the default filesystem configuration:

1.  Transparent compression means that data stored on disk uses less
    space

2.  System reinstallation while preserving user data can be supported,
    while avoiding the issue of volumes running out of space. This is
    due to the fact that Btrfs subvolumes are not limited to a static
    predefined size.

Btrfs also provides a range of other features, such as snapshotting and
online shrinking, which can be useful for those who want to use them,
and can potentially be the basis of future user-facing features.

Fedora Magazine contains a number of [excellent articles about
Btrfs](https://fedoramagazine.org/?s=btrfs).

## Default Disk Layout {#_default_disk_layout}

By default, a Workstation installation has the following disk layout:

+----------------------+----------------------+-----------------------+
| Role                 | Filesystem           | Mount Point           |
+======================+======================+=======================+
| EFI System Partition | FAT 32               | &#96;/boot/efi&#96;   |
+----------------------+----------------------+-----------------------+
| Boot Partition       | ext4                 | &#96;/boot&#96;       |
+----------------------+----------------------+-----------------------+
| Root Subvolume       | Btrfs                | &#96;/&#96;           |
+----------------------+----------------------+-----------------------+
| Home Subvolume       | Btrfs                | &#96;/home&#96;       |
+----------------------+----------------------+-----------------------+

The first two partitions are common to all Fedora installations, and are
required for booting the system. The root subvolume contains the system
installation, and the home subvolume contains user data and settings.

## Swap on ZRAM {#_swap_on_zram}

Fedora Workstation does not use a dedicated swap partition. Instead, it
uses zram: an emulated drive that uses RAM for its storage. RAM-based
swap is faster than disk-based swap, which avoids the extreme system
slowdown and thrashing that can happen with a traditional swap
partition.

The zram drive is compressed, to make efficient use of the available
memory, and is assigned memory dynamically, meaning that it only uses
system RAM when swap is needed.

# Problem Solving &amp; Issue Reporting {#_problem_solving_amp_issue_reporting}

This page includes general information on how to investigate and report
issues with Fedora Workstation.

## Diagnostic Tools {#_diagnostic_tools}

Workstation includes a set of graphical and command line tools which can
be used to investigate and diagnose issues, if they happen.

Graphical tools include:

&#42; &#42;System Monitor&#42;: can be used to see if system resources
are being exceeded, and which processes are using the most resources.
&#42; &#42;Logs&#42;: a graphical viewer app for system and application
logs. &#42; &#42;Problem Reporting&#42;: automatically detects crashes,
and allows reporting of crash data. In some cases the Problem Reporting
tool will link to existing issue reports for a crash.

Command line diagnostic tools which are preinstalled in Fedora
Workstation include:

&#42; &#96;top&#96;: command line system monitor. &#42;
&#96;journalctl&#96;: command line interface for viewing systemd logs.
Learn [how to get started with
journalctl](https://docs.fedoraproject.org/en-US/quick-docs/viewing-logs/).
&#42; &#96;coredumpctl&#96;: command line interface for analyzing
software crashes. [Fedora Magazine has a good article on getting started
with
coredumpctl](https://fedoramagazine.org/file-better-bugs-coredumpctl/).

&#35;&#35;&#35; Issue Reporting

Issues that need to be tracked as part of the Fedora release process,
such as potential release blockers, should be reported against the
correct component in [Red Hat Bugzilla](https://bugzilla.redhat.com/).

For other issues, it is recommended to create reports directly with the
relevant upstream project. The GNOME Project is the upstream for much of
the software that makes up Fedora Workstation. Issues with GNOME
components can be reported using [GNOME's Gitlab
instance](https://gitlab.gnome.org).

&#35;&#35;&#35; Out Of Memory (OOM) Handling

When the system is running out of memory, Fedora Workstation
automatically forces processes to quit, in order to ensure that the
system can continue to function.

If applications or processes suddenly close, it could be due to memory
pressure. Check the logs to see if a OOM event was recorded, and check
system resources to see if your system is approaching its memory limits.
