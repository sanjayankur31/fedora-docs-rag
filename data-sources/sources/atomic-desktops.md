Fedora Atomic Desktops can be installed in the same way as other Fedora
variants, and the official Fedora installation guide can be followed for
your Fedora version. See the [Fedora documentation
site](https://docs.fedoraproject.org/en-US/docs/) for more details.

# Before you begin

As with installing any new operating system, it is important to back up
any data that you want to save before starting, and have a clear
understanding of the consequences of what you are doing.

Fedora Atomic Desktops are intended to provide the full range of
capabilities that you would expect from an installation of Fedora.
However, there are some differences in terms of which applications can
be installed, and how the operating system environment works.

It is therefore recommended that you read this user guide before
deciding to install a Fedora Atomic Desktop. It is also recommended that
you determine whether a Fedora Atomic Desktop meets the specific needs
or requirements that you might have. If you are uncertain about this, a
Fedora Atomic Desktop can also be tested in a virtual machine prior to
installation.

# Known limitations

**Dual booting and manual partitioning is not fully functional.**

It is possible to make Fedora Atomic Desktops work for both dual boot
and manual partitioning, and some guidance is provided on manual
partitioning below. However, there are hazards involved in both cases,
and you should only attempt to use these features if you have done the
necessary research, and are confident that you can overcome any issues
that you might encounter.

This issue is tracked in [issue
#284](https://github.com/fedora-silverblue/issue-tracker/issues/284).

**Known issues for specific Fedora Atomic Desktop variants.**

For Fedora Kinoite, a list of currently known bugs, issues and missing
features is compiled in [issue
#112](https://pagure.io/fedora-kde/SIG/issue/112) in the [KDE SIG
tracker](https://pagure.io/fedora-kde/SIG/issues?status=Open&order_key=last_updated&order=desc).

# Getting a Fedora Atomic Desktop {#getting-atomic-desktop}

If you are using Fedora Media Writer, the Fedora Atomic Desktops should
be listed as a download option. However, if it isn't, or if you want to
download it manually, an install image can be downloaded from [the main
Fedora website](https://fedoraproject.org/atomic-desktops/).

See the individual download page for each Fedora Atomic Desktop variant:

- [Fedora
  Silverblue](https://fedoraproject.org/atomic-desktops/silverblue/download)

- [Fedora
  Kinoite](https://fedoraproject.org/atomic-desktops/kinoite/download)

- [Fedora Sway
  Atomic](https://fedoraproject.org/atomic-desktops/sway/download)

- [Fedora Budgie
  Atomic](https://fedoraproject.org/atomic-desktops/budgie/download)

- [Fedora COSMIC
  Atomic](https://fedoraproject.org/atomic-desktops/cosmic/download)

Once you have got your copy of a Fedora Atomic Desktop, it can be
installed in the usual manner. We hope that you love it!

# Preparing Boot Media

Fedora installation images are **Hybrid ISOs** and can be used to create
installation media with both optical and USB disks, for booting on both
BIOS and UEFI systems.

We recommend using Fedora Media Writer to make a bootable USB media to
install a Fedora Atomic Desktop. Other USB media creation software may
work as well but are not regularly tested.

See the [Fedora Media
Writer](https://docs.fedoraproject.org/en-US/fedora/latest/preparing-boot-media/#_fedora_media_writer)
section to learn how to use it.

# Manual Partitioning {#manual-partition}

As described above, there are known issues with manual partitioning on
Fedora Atomic Desktops, and it should be used with caution. The
following notes are intended as hints for those attempting it, and
should not be treated as recommended practice. Automatic partitioning is
recommended.

With Fedora Atomic Desktops, only certain mounts can be manually
specified as partitions. These include:

- `/boot/efi` (for the UEFI boot loaders)

- `/boot`

- `/var`

- Subdirectories under `/var`, including:

  - `/var/home` (there is a symlink from `/home` to `/var/home`)

  - `/var/log`

  - `/var/containers`

- The root filesystem: `/`

The Fedora installer is not aware of these restrictions and will accept
custom partitions without error, even if they are incompatible with
Fedora Atomic Desktops.

<figure>
<img src="faw-manual-partition-complete.png"
alt="faw manual partition complete" />
<figcaption>Partitioning Complete</figcaption>
</figure>

The above screenshot shows a typical configuration with manual
partitioning in UEFI firmware, with partitions for `/boot`, `/boot/efi`,
`/`, and `/var/home`.

Manual partitioning on Fedora Atomic Desktops can be done with `BTRFS`,
[LVM](https://en.wikipedia.org/wiki/Logical_Volume_Manager_%28Linux%29),
as well as standard partitions or an `XFS` filesystem.

:::: important
::: title
:::

BTRFS filesystems smaller than 5 GiB should be formatted using `--mixed`
(`-M`) flag. Currently neither `mkfs.btrfs` nor Blivet does this
automatically. See [BTRFS
documentation](https://btrfs.readthedocs.io/en/latest/mkfs.btrfs.html#mkfs-feature-mixed-bg)
for more details.
::::

# First Run

## Fedora Silverblue {#_fedora_silverblue}

On first startup you will be asked to enable third-party repositories,
location services, and to create a new user. You can enable third-party
repositories and location later, but you must create a new user by
entering your desired name and password.

<figure>
<img src="Fedora_40_new_user.png" alt="Fedora 40 new user" />
<figcaption>Silverblue - Create New User</figcaption>
</figure>

Once you have created the user you can start using your Fedora
Silverblue system.

## Fedora Kinoite {#_fedora_kinoite}

On first startup, you will be asked to enter the password for the user
created during installation. Depending on different personal needs,
there are several starting actions and installations that you could
perform on newly installed Fedora Kinoite for a customized user
experience.

<figure>
<img src="kinoite-first-run.png" alt="kinoite first run" />
<figcaption>Kinoite - Welcome Center</figcaption>
</figure>

## Fedora Sway Atomic {#_fedora_sway_atomic}

On first startup, you will be asked to enter the password for the user
created during installation. Then, you can start using Fedora Sway
Atomic.

<figure>
<img src="sway-atomic-first-run.png" alt="sway atomic first run" />
<figcaption>Sway Atomic - First Run</figcaption>
</figure>

## Fedora Budgie Atomic {#_fedora_budgie_atomic}

On first startup, you will be asked to enter the password for the user
created during installation. Then, you can start using Fedora Budgie
Atomic.

<figure>
<img src="budgie-atomic-first-run.png" alt="budgie atomic first run" />
<figcaption>Budgie Atomic - First Run</figcaption>
</figure>

# Where to go next? {#_where_to_go_next}

Depending on different personal needs, there are several starting
actions and installations that you could perform on a newly installed
Fedora Atomic Desktop for a customized user experience.

:::: important
::: title
:::

If you are new to Fedora Atomic Desktops and before installing software
in your newly installed system, you should read the [Getting
Started](getting-started.xml) section to learn about the difference
between **Flatpak**, **Toolbox** and **package layering** (rpm-ostree).
::::

For some tips about Fedora Atomic Desktops, see the [Tips and
Tricks](tips-and-tricks.xml) section. :experimental:

# Getting Started

Fedora Atomic Desktops are designed to be easy and straightforward to
use, and specialist knowledge should generally not be required. However,
Fedora Atomic Desktops are built differently from other operating
systems, and there are therefore some things that are useful to know.

Fedora Atomic Desktops have different options for installing software,
compared with a standard Fedora installation (or other package-based
Linux distributions). These include:

- Flatpak apps: This is the primary way that (GUI) apps get installed on
  Fedora Atomic Desktops.

- Toolbx: Used primarily for CLI apps; development, debugging tools,
  etc., but also has support for graphical apps.

- Package layering: Most Fedora packages can be installed on the system
  with the help of package layering. By default the system operates in
  pure image mode, but package layering is useful for things like
  libvirt, drivers, etc.

Although Flatpak is best suited for GUI apps, Toolbx for CLI apps and
package layering for system-level packages, it's ultimately up to you to
choose the method that best suits your needs. There's nothing wrong in
installing CLI apps with Flatpak, or GUI apps with Toolbx, or using
package layering only. Nevertheless, our examples stick to the
aforementioned recommendations throughout this documentation.

For information on [Flatpak](#flatpak) and [package
layering](#package-layering), see below.

See the dedicated [Toolbx](toolbox.xml) page to get started with it.

## Flatpak

Flatpak is the primary way that apps can be installed on Fedora Atomic
Desktops. For more information, see [Flatpak](http://flatpak.org).
Flatpak and Flathub work out of the box in Fedora Atomic Desktops
therefore Flathub nor Flatpak does not to be setup. Fedora provides a
collection of apps that can be installed through Flatpak.

The other main source of Flatpak apps is [Flathub](https://flathub.org),
which provides a large repository of Flatpak apps that can be installed.

## Setting up Flathub {#flathub-setup}

:::: note
::: title
:::

The following figures depict Flathub setup for Fedora Silverblue. The
steps may vary slightly depending on the Atomic Desktop variant, but the
overall process should be similar.
::::

To setup Flathub on Fedora Atomic Desktops, open the [Flathub setup page
for Fedora](https://flatpak.org/setup/Fedora) and click the
btn:\[Flathub repository file\] button to download the Flathub
configuration.

<figure>
<img src="sfg_flathub_fedora.png" alt="sfg flathub fedora" />
<figcaption>Fedora quick setup page</figcaption>
</figure>

A popup window will show a download option for the file. The "Open with"
option should show "Software Install (default)" or \"Discover
(default)\". Click on the btn:\[OK\] button to start the download.

<figure>
<img src="sfg_flathub_download.png" alt="sfg flathub download" />
<figcaption>Flathub download options</figcaption>
</figure>

After the download is complete, a new window will open showing the
Flathub repository. This window also shows the source location of the
repository to be installed, under the \"Details\" heading **(1)**. To
start the installation of the Flathub repository, click on the
btn:\[Install\] button **(2)**.

<figure>
<img src="sfg_flathub_install.png" alt="sfg flathub install" />
<figcaption>Flathub install window</figcaption>
</figure>

After the repository installation process is complete, the window will
be updated to show a btn:\[Remove\] button in place of the
btn:\[Install\] button.

Alternatively, you can use the following command from the terminal:

    $ flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo

### Installing Flatpak apps from Flathub {#_installing_flatpak_apps_from_flathub}

Once the Flathub repository has been setup, it can be used to install
Flatpak apps. This can be done directly from the GNOME Software or the
Plasma Discover applications, or apps can be browsed on the [Flathub
website](https://flathub.org).

If you choose to install apps from the Flathub website, clicking
btn:\[Install\] will download a file which will be opened by the GNOME
Software or Plasma Discover application, which can then be used to
install the app. For example, to install
[LibreOffice](https://www.libreoffice.org), you first search for and
open the LibreOffice page, and then press the btn:\[Install\] button.

After clicking the btn:\[Install\] button, a download information window
will be shown. Verify the correct Flatpak has been downloaded and then
click on the btn:\[OK\] button to begin installing the LibreOffice
application.

<figure>
<img src="sfg_libreoffice_install.png" alt="sfg libreoffice install" />
<figcaption>LibreOffice Flatpak download</figcaption>
</figure>

Once the Flatpak is downloaded, the GNOME Software or the Plasma
Discover application will open a new window with an btn:\[Install\]
button **(2)**. Click this button to begin installation.

Alternatively, each application on Flathub can be installed through the
terminal by running the installation command at the bottom of the page
that should look something like this:

    $ flatpak install flathub <package-name>

As an example, Firefox can be installed by running the following command
which can be found on Firefox's flathub page:

    $ flatpak install flathub org.mozilla.firefox

### Flatpak command line {#_flatpak_command_line}

Additional details about the flatpak command line interface can be found
in the official [Flatpak
documentation](http://docs.flatpak.org/en/latest/using-flatpak.html).

## Package layering

Package layering works by modifying your Fedora Atomic Desktop
installation. As the name implies, it works by extending the packages
from which the Fedora Atomic Desktop is composed.

Good examples of packages to be layered would be:

- `fish`: An alternative Unix shell

- `i3`: A X11 tiling compositor

- `libvirt`: The libvirt daemon

Most (but not all) RPM packages provided by Fedora can be installed on
Fedora Atomic Desktops using this method.

Using package layering creates a new deployment, or bootable filesystem
root. It does not affect your current root. This preserves rollback and
the transactional model, but means that the system must be rebooted
after a package has been layered or updated. You can alternatively use
`rpm-ostree install --apply-live <package-name>` to also temporarily
apply the change directly to your currently booted deployment. It's
generally expected that you use package layering sparingly, and use
[Flatpak](#flatpak) and [Toolbx](toolbox.xml) whenever possible.

Package layering is generally done from the command line. However, the
GNOME Software or the Plasma Discover application does rely on it for
installing a small number of apps that are currently difficult to
install as Flatpaks.

### Installing packages {#_installing_packages}

Packages can be installed on Fedora Atomic Desktops using:

    $ rpm-ostree install <package-name>

This will download the package and any required dependencies, and
recompose your Fedora Atomic Desktop image with them. `rpm-ostree` uses
standard Fedora package names, which can be searched with
`rpm-ostree search` since Fedora Atomic Desktops 39, or using DNF inside
a [Toolbx](toolbox.xml) for previous versions.

Once a package has been installed in this manner, it will be kept
up-to-date as new versions are released and as the base operating system
is updated.

By default, `rpm-ostree` will download both required and recommended
dependencies of layered packages. If you want dependency resolver to
stick to required dependencies only, then you have to append

    Recommends=false

line to the `/etc/rpm-ostreed.conf` file. There's no ad-hoc CLI flag to
do so because of how `rpm-ostree` works internally.

### Replacing packages {#_replacing_packages}

In some scenarios, you may want to test out a new version of `podman` or
`kernel` or other packages that live on the host. The
`rpm-ostree override` command can be used to replace a package with a
different version. You can download the package locally and run:

    $ rpm-ostree override replace <path/to/package>

Or you can override packages without downloading using links from Koji
or Bodhi. For example:

    $ rpm-ostree override replace https://kojipkgs.fedoraproject.org//packages/podman/5.7.0/1.fc43/x86_64/podman-5.7.0-1.fc43.x86_64.rpm

You may also use `rpm-ostree override remove` to effectively \"hide\"
packages. They will still exist in the underlying base layer, but will
not appear in the booted root.

Removing and replacing packages using package layering is not generally
recommended. For more information, see the [rpm-ostree
documentation](https://coreos.github.io/rpm-ostree/administrator-handbook/).

### Adding packages from external repositories {#_adding_packages_from_external_repositories}

See [Adding external package
repositories](troubleshooting.xml#_adding_external_package_repositories).

# Updates, Upgrades & Rollbacks

Installing updates on Fedora Atomic Desktops is easy and fast. It also
has a special rollback feature, in case anything goes wrong.
Additionally, you can choose to have multiple versions of your operating
system installed at all times, and you can choose which one to boot into
whenever you start up your system.

## Updating Fedora Atomic Desktops {#updating}

OS updates are fully integrated into the desktop; you will be
automatically notified when an update is available. On Silverblue and
Kinoite, updates are automatically downloaded. This behavior can be
changed in the settings. On Sway Atomic, Budgie Atomic and COSMIC
Atomic, updates need to be manually applied.

Once an update is ready, it is just a matter of rebooting to start using
the new version. There is no waiting for the update to be installed
during this reboot.

If you'd prefer, it is also possible to update using the command line.
To do this, run:

``` bash
$ rpm-ostree upgrade
```

This will check for new updates and download and install them if they
are available. Alternatively, to check for available updates without
downloading them, run:

``` bash
$ rpm-ostree upgrade --check
```

## Upgrading between major versions {#upgrading}

Upgrading between major versions (such as from Fedora
{version-oldstable} to Fedora {version-stable}) can be completed using
GNOME Software on Silverblue, Plasma Discover on Kinoite and Budgie
Atomic. Alternatively, Fedora Atomic Desktops can be upgraded between
major versions using the `rpm-ostree` command.

:::: warning
::: title
:::

Skipping major releases is currently untested and is thus not supported.
You should update only one major release at a time, i.e. from Fedora
{version-oldstable} to {version-stable}, etc.
::::

First, make sure that you are running the latest update for the current
version:

``` bash
$ rpm-ostree upgrade
```

Reboot your system if needed. Then, verify that the branch for the next
major version is available. You can print all available branches for the
Fedora Atomic Desktop variant that you are currently using with the
following commands:

``` bash
$ source /etc/os-release
$ ostree remote refs ${ID} | grep $(arch) | grep ${VARIANT_ID}
```

After you've verified the name of your branch, you are ready to proceed.
For example, to upgrade to Fedora Silverblue {version-stable}, the
command is:

``` bash
$ rpm-ostree rebase fedora:fedora/{version-stable}/x86_64/silverblue
```

The old variant name for Sway Atomic is `sericea` and for Budgie Atomic
it is `onyx`.

The process is very similar to a system update: the new OS is downloaded
and installed in the background, and you just boot into it when it is
ready.

:::: note
::: title
:::

If you are using the RPM Fusion repositories and are having issues
during major updates, see the [Enabling RPM Fusion
repos](tips-and-tricks.xml#_enabling_rpm_fusion_repos) section.
::::

## Rebasing to another Atomic Desktop {#rebasing}

Additionally, you can choose to rebase to a different variant of Fedora
Atomic. For example, if you are currently using Silverblue, you can
switch to Kinoite. Fedora Kinoite is similar to Fedora Silverblue,
except for the fact that it uses the KDE Plasma desktop instead of the
GNOME desktop.

What this means is, you can rebase to Fedora Kinoite to try it out,
without ever touching your current system. Because the two system images
are isolated from each other, the two desktop environments will never be
installed at the same time. All your flatpak apps and files in the
`/home` directory will remain persistent between rebases. Same applies
for testing out the development version of Fedora Atomic Desktops, which
is Rawhide.

:::: note
::: title
:::

By default, OSTree only keeps the two most recent deployments. If you
decide to rebase, make sure to [pin your current
deployment](#pinning-and-cleaning-deployments), so you don't
accidentally lose it.
::::

## Rolling back

Fedora Atomic Desktops keep a record of the previous OS version, which
can be switched to instead of the latest version. While this shouldn't
usually be necessary, it can be helpful if there is a problem with an
update or an upgrade (rollbacks work the same way for both), as well as
for development purposes.

There are two ways to roll back to the previous version:

1.  Temporary rollbacks: to temporarily roll back to a previous version,
    simply reboot and select the previous version from the boot menu
    (often known as the GRUB menu).

2.  Permanent rollbacks: to permanently switch back to the previous
    deployment, use the `rpm-ostree rollback` command.

After rolling back, you will technically be on an old OS version, and
may be prompted to update. Updating will undo the rollback, so it should
be avoided if you want the rollback to stay in effect.

`rpm-ostree` only keeps one rollback version available by default. If
you want to rollback to another version than the one currently available
on your system, you can do so with the following commands:

1.  Pull the ostree commit log from the remote repository:

    ``` bash
    $ source /etc/os-release
    $ sudo ostree pull --commit-metadata-only --depth=10 ${ID} ${ID}/{version-stable}/$(arch)/${VARIANT_ID}
    ```

2.  Display the log:

    ``` bash
    $ ostree log ${ID}:${ID}/{version-stable}/$(arch)/${VARIANT_ID}
    ```

3.  Deploy a specific commit:

    ``` bash
    $ rpm-ostree deploy {version-stable}.20251031.0
    ```

:::: note
::: title
:::

This will deploy the exact version as requested and will not include
overlayed packages and other changes.
::::

## Pinning and cleaning deployments

By default, the `rpm-ostree upgrade` or `rpm-ostree rebase` commands
will keep at most two bootable deployments, though the underlying
technology supports more. In some cases, such as a major version upgrade
or rebase, you may want to keep your current deployment as a guaranteed
fallback. OSTree allows you to pin deployments. Pinning ensures that
your deployment of choice is kept and not discarded. To pin an
deployment, you need to know its index number. To print the index
numbers of the deployments, run the following command:

``` bash
$ rpm-ostree status --verbose
```

If you want to pin your currently booted deployment, run the following
command:

``` bash
$ sudo ostree admin pin 0
```

If you pin many deployments, the `/boot` partition may run out of space
and as a consequence the system may not be able to be upgraded. In such
cases, it is necessary to unpin and clean up some deployments. To unpin
a deployment, run the following command:

``` bash
$ sudo ostree admin pin INDEX --unpin
```

You can run the above command multiple times to free up more space. Then
clean up unpinned deployments:

``` bash
$ rpm-ostree cleanup --rollback
```

:::: note
::: title
:::

The `rpm-ostree cleanup --rollback` command will not remove pinned
deployments. :experimental:
::::

# Toolbx {#toolbox}

:::: note
::: title
:::

Toolbx is not a typo, see the [project
page](https://containertoolbx.org).
::::

Fedora Atomic Desktops are an excellent platform for container-based
development and, for working with containers,
[buildah](https://buildah.io) and [podman](https://podman.io) are
recommended.

Fedora Atomic Desktops also comes with the
[toolbx](https://github.com/containers/toolbox) utility, which uses
containers to provide an environment where development tools and
libraries can be installed and used.

## Why use toolbx? {#toolbox-why-use}

Toolbx makes it easy to use a containerized environment for everyday
software development and debugging. On operating systems utilizing
read-only root filesystems, like [Fedora Atomic
Desktops](https://fedoraproject.org/atomic-desktops), it provides a
familiar package-based environment in which tools and libraries can be
installed and used. However, toolbx can also be used on package-based
systems.

Using Toolbx for running your workflows in a containerized manner brings
you several advantages:

- It keeps the host OS clean and stable, and helps to avoid the clutter
  that can happen after installing lots of development tools and
  packages.

- You get access to different versions of supported distributions
  independent of the version you are running.

- Containers are a good way to isolate and organise the dependencies
  needed for different projects.

- Containers are a safe space to experiment: if things go wrong, it's
  easy to throw a toolbox away and start again.

However, it is very important to note that toolbx containers are still
integrated with your host system, so you should not attempt to do things
or run software you otherwise wouldn't on your host system. Toolbx
containers are not completely isolated environments like virtual
machines.

## How it works {#toolbox-how-it-works}

Toolbx takes the work out of using containers, by providing a small
number of simple commands to create, enter, list and remove containers.
It also integrates toolbx containers into your regular working
environment, to make it easy for you to use them as an everyday
development space.

Containers are created from images and those are usually a very stripped
down version of distributions. In such images there are almost no tools
and documentation available. The team behind Toolbx maintains a Fedora
image where such tools and documentation are available, providing a good
out of the box experience.

Each toolbx container is an environment that you can enter from the
command line. Inside each one, you will find:

- Your existing username and permissions.

- Access to your home directory and several other locations.

- Access to both system and session D-Bus, system journal and Kerberos.

- Common command lines tools, including a package manager (e.g., DNF on
  Fedora).

In other words, toolbx containers look, feel and behave like a standard
Linux command line environment. By connecting all this information,
toolbx containers lose a certain amount of security gained by using the
containers technology. Therefore, you should not treat toolbx containers
as a sandbox where you can execute any script you would never run on any
other system.

In most cases, when a command is run inside a container, the program
from inside the container is used. However, there are a few special
cases where the program on the host is used instead (using
`flatpak-spawn`). One example of this is the `toolbox` command itself;
this makes it possible to use toolbx from inside toolbx containers.

## Installation {#toolbox-installation}

### Fedora Atomic Desktops {#_fedora_atomic_desktops}

Toolbx is preinstalled on Fedora Atomic Desktops.

### Other Fedora Editions {#_other_fedora_editions}

Toolbx can be installed on other Fedora Editions (or any package-based
version of Fedora) with the following command:

``` bash
$ sudo dnf install toolbox
```

## Your first toolbox {#toolbox-first-toolbox}

Once toolbx is installed, two simple commands are required to get
started:

``` bash
$ toolbox create
```

This will download an OCI image and create a toolbx container from it.
Once this is complete, run:

``` bash
$ toolbox enter
```

Once inside the toolbox, you can access common command line tools, and
install new ones using a package manager (e.g., DNF on Fedora).

:::: note
::: title
:::

When the prompt is inside a toolbox, it is prepended with a diamond:
this indicates that the prompt is inside a toolbx container. The diamond
symbol may not be present if you use a custom shell theme.
::::

## Commands and usage {#toolbox-commands}

### toolbox create \[options\] \<name\> {#toolbox-create}

Creates a toolbx container. This will download an OCI image if one isn't
available (this is required to create the container). By default an
image matching the version of the host is used. If the host system does
not have a matching image, a Fedora image is used instead.

Used without options, `toolbox create` will automatically name the
container it creates. To create additional toolboxes, use the `<name>`
argument.

To use a specific version of the host system (e.g., Fedora
{version-oldstable} on Fedora {version-stable}), use the
`--release <release> | -r <release>` option.

To use a different distribution to create a toolbx container (e.g., RHEL
on Fedora), use the `--distro <distro> | -d <distro>` option.

To use a different image, use the `--image <name> | -i <name>` option.

### toolbox enter \[options\] \<name\> {#toolbox-enter}

Enters a toolbox for interactive use. Used without options,
`toolbox enter` opens the default toolbox.

To enter a toolbox with specific name, use the `name` argument.

To enter a toolbox for a different distribution (e.g., Fedora on RHEL),
use the `--distro <distro> |-d <distro>` option.

To enter a toolbox with specific version (e.g., RHEL 9.6 on RHEL 10.0),
use the `--release <release> | -r <release>` option.

### toolbox run \[options\] \<cmd\> \<arg ...​\> {#toolbox-run}

Runs a command in a toolbox without entering it. Used without options,
`toolbox run` runs the command in the default toolbox.

To run a command in a toolbox with specific name, use the
`--container <name> | -c <name>` option.

To run a command in a toolbox for a different distribution (e.g., Fedora
on RHEL), use the `--distro <distro> |-d <distro>` option.

To run a command in a toolbox with specific version (e.g., RHEL 9.6 on
RHEL 10.0), use the `--release <release> | -r <release>` option.

### toolbox list \[options\] {#toolbox-list}

Lists local toolbx images and containers.

To only show containers, use the `--containers | -c` option.

To only show images, use the `--images | -i` option.

### toolbox rm \[options\] \<name ...​\> {#toolbox-rm}

Removes one or more toolbx containers.

The `--force | -f` option removes the marked containers even if they are
running.

The `--all | -a` option removes all toolbx containers.

### toolbox rmi \[options\] \<name ...​\> {#toolbox-rmi}

Removes one or more toolbx images.

The `--force | -f` option removes the marked images and all containers
that have been created using the marked images.

The `--all | -a` option removes all toolbx images.

### toolbox \--help {#toolbox-help}

Shows Toolbx's manual page.

### Exiting a toolbox {#toolbox-exiting}

To return to the host environment, either run `exit` or quit the current
shell (typically kbd:\[Ctrl+D\]).

## Under the hood {#toolbox-under-the-hood}

Toolbx uses the following technologies:

- [OCI container images](https://www.opencontainers.org)

- [Podman](https://podman.io)

## Contact and issues {#toolbox-contact}

To report issues, make suggestions, or contribute fixes, see [toolbx's
GitHub project](https://github.com/containers/toolbox).

To get in touch with toolbx users and developers, use the [Fedora
Discussion](https://discussion.fedoraproject.org/tag/toolbx), or join
the [Toolbx Matrix Room](https://matrix.to/#/#toolbx:matrix.org).

This page provides some background technical information on Fedora
Atomic Desktops, including information on the core technologies used to
build it, as well as the filesystem layout.

Users should not need to know this information. It is provided here for
those who are interested in the technical details or those who want to
use Fedora Atomic Desktops in a non-standard manner.

# ostree and rpm-ostree {#ostree-rpm-ostree}

[ostree](https://ostreedev.github.io/ostree/) is the core technology
that is used to compose, deploy and update Fedora Atomic Desktops.
ostree operates in a similar manner to a version control system, but it
operates on entire filesystem trees. It is often described as "Git for
operating system binaries".

For Fedora Atomic Desktops installations, ostree is responsible for
deploying and updating the OS image (including everything below `/` that
is not symlinked into `/var`). It also updates `grub.cfg` entries to
point to the current image.

[rpm-ostree](https://coreos.github.io/rpm-ostree/) builds on top of
ostree, and makes it possible to install RPMs as a "layer" on top of an
ostree image. This makes it possible to install RPMs on Fedora Atomic
Desktops.

When a package is installed with `rpm-ostree`, a new OS image is
composed by adding the RPM payload to the existing OS image, and
creating a new, combined image. To see the newly installed RPMs, the
system needs to be rebooted with the new image. rpm-ostree also takes
care of recreating the layered image whenever you update the base OS
image.

# Fedora Atomic Desktops filesystem layout {#filesystem-layout}

On Fedora Atomic Desktops, the root filesystem (`/`) is mounted
read-only. The `/usr` directory and everything below it is also
read-only.

The `/etc` and `/var` directories are respectively used to store
configuration files and runtime state and are thus writable. Symlinks
are used to make traditional state-carrying directories available in
their expected locations. This includes:

- `/home` → `/var/home`

- `/opt` → `/var/opt`

- `/srv` → `/var/srv`

- `/root` → `/var/roothome`

- `/usr/local` → `/var/usrlocal`

- `/mnt`→ `/var/mnt`

- `/tmp` → `/sysroot/tmp`

This means that separate home partitions should be mounted on
`/var/home`.

Since Fedora Linux 37, the `/sysroot` directory is also [mounted
read-only](https://fedoraproject.org/wiki/Changes/Silverblue_Kinoite_readonly_sysroot).

The `/boot` and `/boot/efi` directories are currently also mounted as
writable but there are plans to mount them read-only in the future or
even not mount them at all. See [Mount /boot as Read Only by
default](https://gitlab.com/fedora/ostree/sig/-/issues/21) and [Do not
mount /boot/efi by
default](https://gitlab.com/fedora/ostree/sig/-/issues/22).

For a more detailed explanation of Fedora Atomic Desktops\' filesystem
layout, refer to the [libostree
documentation](https://ostreedev.github.io/ostree/adapting-existing/). =
Reading & Resources

This page is a list of further reading and resources for Fedora Atomic
Desktops.

# Technology websites and documentation {#_technology_websites_and_documentation}

- [Buildah](https://buildah.io/) - build OCI container images

- [Flatpak](http://flatpak.org) - next-generation desktop app framework

- [ostree](https://ostreedev.github.io/ostree/) - OS image composition
  and updates

- [podman](https://podman.io/) - daemonless container engine

- [rpm-ostree](https://coreos.github.io/rpm-ostree/) - hybrid
  image/package system

# Documents {#_documents}

- [Team Silverblue - The
  Origins]({attachmentsdir}/team-silverblue-origins.pdf) - PDF that
  explains the motivations, goals, and history behind Fedora Silverblue,
  the first Fedora Atomic Desktop

- [Flatpak Cheat Sheet]({attachmentsdir}/flatpak-print-cheatsheet.pdf) -
  PDF with common flatpak commands

- [rpm-ostree Cheat Sheet]({attachmentsdir}/silverblue-cheatsheet.pdf) -
  PDF with common rpm-ostree commands, branded for Silverblue but
  applies to all Fedora Atomic Desktops

- [Container commandos]({attachmentsdir}/container-commandos.pdf) - a
  playful introduction to tools such as podman, cri-o and buildah by
  Máirín Duffy and Dan Walsh. Print it out, and learn as you color! =
  Contributing to Fedora Atomic Desktops

Help us improve Fedora Atomic Desktops by contributing to the project!

# Reporting Issues

You can report bugs and suggest features or improvements on the [issue
tracker](https://gitlab.com/fedora/ostree/sig/-/issues).

# Developing Fedora Atomic Desktops {#developing}

See the repositories in the
[atomic-desktops](https://forge.fedoraproject.org/atomic-desktops)
organization for the configuration used to create the Fedora Atomic
Desktops.

If you are a developer, you can contribute to one of the several
projects which make Fedora Atomic Desktops possible. Submit your pull
requests to:

- [bootc](https://github.com/bootc-dev/bootc)

- [rpm-ostree](https://github.com/coreos/rpm-ostree)

- [flatpak](https://github.com/flatpak/flatpak)

- [ostree](https://github.com/ostreedev/ostree)

- [toolbox](https://github.com/containers/toolbox)

- [podman](https://github.com/containers/podman)

Your contributions towards the main
[Fedora](https://docs.fedoraproject.org/en-US/project/join) project are
also very welcome.

# Writing Documentation

Head over to our
[documentation](https://forge.fedoraproject.org/atomic-desktops/docs)
repository, fork it and create a pull request.

If you are not comfortable with using git, create a new topic in our
[community](https://discussion.fedoraproject.org/tag/atomic-desktops) or
log an
[issue](https://forge.fedoraproject.org/atomic-desktops/docs/issues)
describing what needs to be changed. :experimental:

# Troubleshooting {#_troubleshooting}

Fedora Atomic Desktops use a new way of deploying and managing your
desktop operating system, so you may occasionally run into problems
while going through your day to day. Below are some of the more common
problems reported and any workarounds for those problems.

## \"Forbidden base package replacements\" {#_forbidden_base_package_replacements}

This can happen when a package that is being layered has a dependency on
a package that is in the base OS. In the problematic case, the layered
package requires a newer version of the dependent package which is not
available in the base OS.

In most cases, waiting for a newer OSTree compose will resolve this
problem. The dependent package will be updated in the compose and the
package that was going to be layered will be successful.

However, if you continue to encounter this problem with a newer compose,
you can try to cleanup the metadata with `rpm-ostree cleanup -m` and
then retrying the `rpm-ostree install`.

Alternatively, you can try rebasing to any `updates` ref, like
`fedora/{version-stable}/updates/x86_64` after the `cleanup` operation.

For more information, see
[rpm-ostree#415](https://github.com/coreos/rpm-ostree/issues/415).

## Installing packages to `/opt` or `/usr/local` {#_installing_packages_to_opt_or_usrlocal}

Installing into `/opt` was commonly raised as a problem when users where
trying to install Google Chrome. A [partial
solution](https://github.com/projectatomic/rpm-ostree/pull/1795) has
been implemented that allows users to layer Google Chrome, however it is
not a complete solution for applications that write mutable data to
`/opt`.

This issue is tracked in
[rpm-ostree#233](https://github.com/coreos/rpm-ostree/issues/233).

## Using NVIDIA drivers {#_using_nvidia_drivers}

:::: note
::: title
:::

The [Universal Blue](https://universal-blue.org/) project creates
operating system images with the NVIDIA drivers included. The Universal
Blue images are based on the Fedora Atomic Desktop images with
additional changes at their discretion. The Universal Blue images are
not officially endorsed by the Fedora Project. Use them at your own
discretion.
::::

You can install the official NVIDIA binary drivers from the RPM Fusion
repositories.

:::: caution
::: title
:::

The NVIDIA binary drivers are not maintained by the Fedora Project and
may sometimes not be available for the kernel version included in Fedora
Atomic Desktops.
::::

1.  First, ensure that your system is fully updated by running
    `sudo rpm-ostree upgrade` and rebooting.

2.  Then setup the RPM Fusion repositories following the
    [documentation](https://docs.fedoraproject.org/en-US/quick-docs/rpmfusion-setup/#_enabling_the_rpm_fusion_repositories_for_ostree_based_systems),
    including the two reboots.

3.  Finally, install the drivers:

        # rpm-ostree install kmod-nvidia xorg-x11-drv-nvidia
        # rpm-ostree kargs --append=rd.driver.blacklist=nouveau,nova-core \
        --append=modprobe.blacklist=nouveau,nova-core \
        --append=nvidia-drm.modeset=1 \
        --append=initcall_blacklist=simpledrm_platform_driver_init
        # systemctl reboot

:::: note
::: title
:::

When using Secure Boot, the locally installed NVIDIA drivers have to be
signed with a local key that is enrolled using `mokutil`. See the
[fedora-silverblue#499](https://github.com/fedora-silverblue/issue-tracker/issues/499)
issue for more details.
::::

You may also encounter the following issues during installation:
[#286](https://github.com/fedora-silverblue/issue-tracker/issues/286),
[#331](https://github.com/fedora-silverblue/issue-tracker/issues/331)

Thanks to [Alex Larsson](https://blogs.gnome.org/alexl/) who made the
required changes to the `akmods` and `kmodtools` packages. You can read
more about the work that Alex did on his
[blog](https://blogs.gnome.org/alexl/2019/03/06/nvidia-drivers-in-fedora-silverblue/).

## Out of tree kernel modules and drivers using DKMS {#_out_of_tree_kernel_modules_and_drivers_using_dkms}

Fedora Atomic Desktops currently do not have support for DKMS. See the
upstream issue
[rpm-ostree#1091](https://github.com/coreos/rpm-ostree/issues/1091).

Instead, we recommend that you make
[kmods](https://rpmfusion.org/Packaging/KernelModules/Kmods2) packages
for out of tree kernel modules and submit them to the [RPM
Fusion](https://rpmfusion.org/) repos. The kmods packages will then be
used by [akmods](https://rpmfusion.org/Packaging/KernelModules/Akmods)
which is supported on Fedora Atomic Desktops.

## Adding external package repositories {#_adding_external_package_repositories}

:::: caution
::: title
:::

This section discusses third-party software sources not officially
affiliated with or endorsed by the Fedora Project. Use them at your own
discretion.
::::

:::: note
::: title
:::

If you want to use RPM Fusion repositories, please follow the [Enabling
RPM Fusion repos](tips-and-tricks.xml#_enabling_rpm_fusion_repos)
section.
::::

Some sofware may only be available from a third-party repository. You
can add an external repository manually on Fedora Atomic Desktops by
placing the `.repo` file into `/etc/yum.repos.d/` and the GPG key into
`/etc/pki/rpm-gpg/`. The following is a full example for setting up the
Taiscale repo:

1.  Fetch and install the repo config:

        $ curl -O https://pkgs.tailscale.com/stable/fedora/tailscale.repo
        [tailscale-stable]
        name=Tailscale stable
        baseurl=https://pkgs.tailscale.com/stable/fedora/$basearch
        enabled=1
        type=rpm
        repo_gpgcheck=1
        gpgcheck=0
        gpgkey=https://pkgs.tailscale.com/stable/fedora/repo.gpg
        $ sudo install -o 0 -g 0 -m644 tailscale.repo /etc/yum.repos.d/tailscale.repo

2.  Fetch and install the GPG keys:

    ``` bash
    $ curl -O https://pkgs.tailscale.com/stable/fedora/repo.gpg
    $ sudo install -o 0 -g 0 -m644 repo.gpg /etc/pki/rpm-gpg/tailscale.gpg
    ```

3.  Replace the `gpgkey=` URL in the repo config by the path the GPG
    keys:

        $ sudoedit /etc/yum.repos.d/tailscale.repo
        $ cat /etc/yum.repos.d/tailscale.repo
        [tailscale-stable]
        name=Tailscale stable
        baseurl=https://pkgs.tailscale.com/stable/fedora/$basearch
        enabled=1
        type=rpm
        repo_gpgcheck=1
        gpgcheck=0
        ### Update this line
        gpgkey=file:///etc/pki/rpm-gpg/tailscale.gpg
        ###    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

4.  Install the new packages with:

        $ rpm-ostree install tailscale

Better support in `rpm-ostree` for this use case is tracked in
[rpm-ostree#4014](https://github.com/coreos/rpm-ostree/issues/4014).

## SELinux problems {#_selinux_problems}

As users work with Fedora Atomic Desktops day-to-day, it is possible
that they have modified the default SELinux policy in an effort to
workaround one or more problems related to SELinux. This is usually done
when a user sees a SELinux denial in the journal. If this is the case
and one wishes to revert back to the default SELinux policy, you can try
these set of actions.

1.  Check the state of the SELinux policy

    ``` bash
    $ sudo ostree admin config-diff | grep policy
    M    selinux/targeted/active/policy.linked
    M    selinux/targeted/active/policy.kern
    M    selinux/targeted/policy/policy.31
    A    selinux/targeted/policy/policy.30
    ```

    If anything is returned by this command, then your SELinux policy
    has been modified from the default.

2.  Copy the default SELinux policy shipped in the OSTree compose

    ``` bash
    $ sudo cp -al /etc/selinux{,.bak}
    $ sudo rsync -rlv /usr/etc/selinux/ /etc/selinux/
    ```

    After doing this, the output from
    `ostree admin config-diff | grep policy` should no longer indicate
    the policy is modified.

    If your policy still appears to be modified, you can try the
    following approach.

3.  Remove the SELinux policy; copy in the default policy

    ``` bash
    $ sudo rm -rf /etc/selinux
    $ sudo cp -aT /usr/etc/selinux /etc/selinux
    ```

    After this, the `ostree admin config-diff | grep policy` command
    should return no modifications.

## Unable to add user to group {#_unable_to_add_user_to_group}

Due to how `rpm-ostree` handles user + group entries, it may not be
possible to use `usermod -a -G` to add a user to a group successfully.
Until `rpm-ostree` moves to using `systemd sysusers`, users will have to
populate the `/etc/group` file from the `/usr/lib/group` file before
they can add themselves to the group.

For example, if you wanted to add a user to the `libvirt` group:

``` bash
$ grep -E '^libvirt:' /usr/lib/group | sudo tee -a /etc/group
$ sudo usermod -aG libvirt $USER
```

:::: note
::: title
:::

You will need to log off and log back in to apply these changes.
::::

This issue is tracked in
[rpm-ostree#29](https://github.com/coreos/rpm-ostree/issues/29) and
[rpm-ostree#49](https://github.com/coreos/rpm-ostree/issues/49).

## `ostree fsck` reports file corruption {#_ostree_fsck_reports_file_corruption}

It is possible to end up in a situation where one or more files on the
disk have become corrupted or missing. In this case, `ostree fsck` will
report errors in certain commits. The
[workaround](https://github.com/ostreedev/ostree/pull/345#issuecomment-262263824)
in this case is to mark the entire OSTree commit as partially retrieved
and then re-pull the commit.

## Read-only `/boot/efi` prevents any upgrades {#_read_only_bootefi_prevents_any_upgrades}

This issue is most commonly seen when users have installed Fedora Atomic
Desktops on Apple hardware. The `/boot/efi` partition on Apple hardware
is formatted as HFS+ and is not always resilient to power failures or
other kinds of hard power events.

Since Fedora Atomic Desktops now includes the `hfsplus-tools` package in
the base compose, it has become relatively easy for users to workaround
this kind of error.

    # umount /boot/efi
    # fsck.hfsplus /dev/sda1
    # mount -o rw /boot/efi

See the
[rpm-ostree#1380](https://github.com/coreos/rpm-ostree/issues/1380)
GitHub issue for additional details.

## Unable to install a Fedora Atomic Desktop on EFI systems {#_unable_to_install_a_fedora_atomic_desktop_on_efi_systems}

Users have reported that they cannot install a Fedora Atomic Desktop on
an EFI based system where they previously had another OS installed. The
error that is often observed looks like:

    ostree ['admin', '--sysroot=/mnt/sysimage', 'deploy', '--os=fedora-workstation', 'fedora-workstation:fedora/28/x86_64/workstation'] exited with code -6`

A couple of possible workarounds exist:

- During the install process, select \"Custom Partitioning\" and create
  an additional EFI partition. Assign the newly created EFI partition to
  `/boot/efi`. You will then be able to boot the previous OS(s)
  alongside your Fedora Atomic Desktop. If this workaround is not
  successful follow the below step.

- Reformat the EFI partition on the host during the install process.
  This can be done by selecting \"Custom Partitioning\" and checking the
  `Reformat` box when creating the `/boot/efi` partition.

:::: warning
::: title
:::

Choosing to reformat `/boot/efi` will likely result in the inability to
boot any other operating systems that were previously installed. Be sure
that you have backed up any important data before using this workaround.
::::

This issue is tracked in
[Bugzilla#1575957](https://bugzilla.redhat.com/show_bug.cgi?id=1575957).

## toolbox: failed to list images with com.redhat.component=fedora-toolbox {#_toolbox_failed_to_list_images_with_com_redhat_componentfedora_toolbox}

:::: important
::: title
:::

As of `podman` version `1.4.0` this workaround is not necessary. Ensure
`podman` is up to date by issuing `rpm-ostree upgrade` before attempting
this workaround.
::::

When issuing the `toolbox list` command, systems using `podman` versions
newer than `1.2.0`, will generate the following error:

``` bash
toolbox: failed to list images with com.redhat.component=fedora-toolbox
```

:::: tip
::: title
:::

The following workaround might be useful for other `toolbox` errors
caused by `podman` versions greater than `1.2.0`. See
[toolbox#169](https://github.com/containers/toolbox/issues/169#issuecomment-495193902).
::::

As a workaround, it is possible to override `podman` packages newer than
version `1.2.0` by issuing:

``` bash
$ rpm-ostree override --remove=podman-manpages \
replace https://kojipkgs.fedoraproject.org//packages/podman/1.2.0/2.git3bd528e.fc30/x86_64/podman-1.2.0-2.git3bd528e.fc30.x86_64.rpm
```

Reboot the system to apply the changes.

For reference, it is also possible to override the package by following
these steps:

1.  Download `podman-1.2.0-2.git3bd528e.fc30.x86_64.rpm` from
    [Koji](https://kojipkgs.fedoraproject.org//packages/podman/1.2.0/2.git3bd528e.fc30/x86_64/podman-1.2.0-2.git3bd528e.fc30.x86_64.rpm).

2.  Remove `podman-manpages` issuing:
    `rpm-ostree override remove podman-manpages`.

3.  Override the currently installed `podman` package (using the package
    you have downloaded on the first step) by:

    ``` bash
    $ rpm-ostree override replace podman-1.2.0-2.git3bd528e.fc30.x86_64.rpm
    ```

You can now reboot the system for the change to take effect.

To revert this workaround issue the following commands:

``` bash
$ rpm-ostree override reset podman
$ rpm-ostree override reset podman-manpages
```

## Unable to enter a toolbox due to permissions errors {#_unable_to_enter_a_toolbox_due_to_permissions_errors}

With certain versions of `podman`, trying to enter a toolbox will result
in errors. You can fix this by resetting the permissions on the
overlay-containers with the following command:

``` bash
$ sudo chown -R $USER ~/.local/share/containers/storage/overlay-containers
```

This will reset the permissions on your containers and allow you to
enter them again.

See the upstream podman issue:
[podman#3187](https://github.com/containers/podman/issues/3187).

## Running `restorecon` {#_running_restorecon}

:::: warning
::: title
:::

You should never run `restorecon` on a Fedora Atomic Desktop system. See
the following bug for details -
[Bugzilla#1259018](https://bugzilla.redhat.com/show_bug.cgi?id=1259018)
::::

However, if you happened to do this, it is possible to recover.

1.  Boot with `enforcing=0` on the kernel command line

2.  Create a new, \"fixed\" commit locally

3.  Deploy the new \"fixed\" commit

4.  Run `restorecon`

5.  Reboot

6.  Cleanup

``` bash
$ rpm-ostree status -b | grep BaseCommit
BaseCommit: 696991d589980aeaef5eda352dd7ad3d33c444c789c209f793a84bc6e7269aee
### If the above command does not display any output, try:
$ rpm-ostree status -b | grep Commit
Commit: 696991d589980aeaef5eda352dd7ad3d33c444c789c209f793a84bc6e7269aee
$ sudo ostree checkout \
-H 696991d589980aeaef5eda352dd7ad3d33c444c789c209f793a84bc6e7269aee \
/ostree/repo/tmp/selinux-fix
$ sudo ostree fsck --delete
$ sudo ostree commit --consume \
--link-checkout-speedup --orphan --selinux-policy=/ /ostree/repo/tmp/selinux-fix
$ sudo restorecon -Rv /var
$ sudo restorecon -Rv /etc
### In the command below, substitute:
### - x86_64 with your actual CPU architecture
### - silverblue with the name for your Fedora Atomic Desktop variant
$ sudo ostree admin deploy fedora:fedora/{version-stable}/x86_64/silverblue
$ sudo reboot
```

The caveat to this recovery is that your layered packages will be
removed; you'll need to relayer them after the recovery.

See this upstream comment for additional details:
[ostree#1265](https://github.com/ostreedev/ostree/issues/1265#issuecomment-484557615).

## Resetting passwords in Rescue Mode {#_resetting_passwords_in_rescue_mode}

In the case where you are unable to remember your user password or root
password, you can reset the password using the following steps:

1.  While the system is booting, interrupt the boot sequence at the
    [GRUB2](https://docs.fedoraproject.org/en-US/quick-docs/grub2-bootloader/)
    menu by using the kbd:\[Esc\] key.

2.  Select the boot entry that you wish to edit using the arrow keys.

3.  Edit the selected entry with the kbd:\[e\] key.

4.  Use the arrow keys to select the line beginning with `linux`,
    `linux16`, or `linuxefi`.

5.  Go to the end of that line (by pressing kbd:\[Ctrl\] + kbd:\[e\])
    and append `init=/bin/bash`.

6.  Press kbd:\[Ctrl\] + kbd:\[x\] or kbd:\[F10\] to boot the entry.

7.  At the resulting `bash` prompt, run the following commands:

<!-- -->

    # mount -t selinuxfs selinuxfs /sys/fs/selinux
    # /sbin/load_policy
    # passwd
    # sync
    # /sbin/reboot -ff

If you want to change the password for a user account, replace the
`passwd` command with `passwd <username>`.

After the system finishes rebooting, you should be able to login with
the username and new password. = Frequently Asked Questions (FAQ)

## About the Fedora Atomic Desktops projects {#_about_the_fedora_atomic_desktops_projects}

### Is it Team Silverblue, Silverblue, or Fedora Silverblue? {#_is_it_team_silverblue_silverblue_or_fedora_silverblue}

Team Silverblue was the name used to refer to the overall project.
Fedora Silverblue will be used for the OS, but calling it Silverblue in
its short version is fine as well.

### Why does the Silverblue logo look like a leaf? {#_why_does_the_silverblue_logo_look_like_a_leaf}

Our favorite choice for a project name was Silverleaf, but that sadly
did not work out. We just couldn't quite let go of the leaf. You could
also say that Silverblue is a new leaf on Fedora's OSTree. 😀

### Is Silverblue another GNOME OS? {#_is_silverblue_another_gnome_os}

GNOME OS was a codename that was used by the upstream GNOME project for
a while to refer to the idea of designing the entire desktop user
experience. By contrast, Silverblue is an effort inside the Fedora
project, and will be built with existing Fedora technologies. However,
the two efforts do share a desire to deliver a user experience that is
polished and coherent.

### Why is the project named Fedora Kinoite? {#_why_is_the_project_named_fedora_kinoite}

We chose the Kinoite name for the following reasons:

- KDE based projects traditionally start with a \"K\".

- Kinoite is a blue mineral
  ([Wikipedia](https://en.wikipedia.org/wiki/Kinoite)), thus referring
  to both the \"silver\" and \"blue\" part of Silverblue and the blue
  color of the KDE logo.

- \"Kinoite\" means \"There is a tree\" in Japanese ([Google
  Translate](https://translate.google.com/?sl=auto&tl=en&text=kinoite&op=translate)),
  thus referring to the \"tree\" in \"ostree\".

### What is Fedora Atomic Desktops\' relationship with Fedora IoT and Fedora CoreOS? {#_what_is_fedora_atomic_desktops_relationship_with_fedora_iot_and_fedora_coreos}

Fedora Atomic Desktops use the same core technology as Fedora IoT and
Fedora CoreOS. However, Fedora Atomic Desktops are specifically focused
on workstation and desktop use cases with the GNOME, KDE Plasma, Sway,
Budgie and COSMIC desktops.

## About using Fedora Atomic Desktops {#_about_using_fedora_atomic_desktops}

### How can I play more videos in Firefox, like YouTube? {#_how_can_i_play_more_videos_in_firefox_like_youtube}

Firefox is included in the OS image for now (see
[issue#3](https://gitlab.com/fedora/ostree/sig/-/issues/3) for progress
on moving to Flatpak by default). Until that changes, getting it to play
videos works the same way as it does for the regular package mode
Fedora: find a package with the needed codecs, and install it. The one
difference is that you use `rpm-ostree install` instead of
`dnf install`. An alternative solution is to install [Firefox from
Flathub](https://flathub.org/apps/details/org.mozilla.firefox).

### How do I create a VPN connection? {#_how_do_i_create_a_vpn_connection}

`/etc` is not part of the read-only root filesystem, so you can just
copy files into `/etc/NetworkManager/system-connections` (or let
NetworkManager store them there when you recreate your connections).
Certificates in `/etc/pki` need to be handled similarly.

### How can I install my preferred IDE on Fedora Atomic Desktops? {#_how_can_i_install_my_preferred_ide_on_fedora_atomic_desktops}

You can install most IDE directly in a toolbox where you can also
install all the developments tools from the Fedora repositories. To be
able to launch them directly from menus, you can copy the `.desktop`
file for the IDE from the toolbox to your home directory in
`~/.local/share/applications/`. You should then update the `Exec` line
in the `.desktop` file to prepend `toolbox run` to start it from the
toolbox. You can also use the IDEs packaged as Flatpaks from Flathub.

### How can I see what packages were updated between two commits? {#_how_can_i_see_what_packages_were_updated_between_two_commits}

- If you want to compare the booted deployment with the pending
  deployment (or rollback deployment), simply issue:

  ``` bash
  $ rpm-ostree db diff
  ```

  :::: tip
  ::: title
  :::

  You can also see the RPM changelog by adding the `-c` option like so:
  `rpm-ostree db diff -c`.
  ::::

- If you want to see which packages were updated between two specific
  commits:

  1.  Find out which two commits you want to compare by issuing:

          $ ostree log <ref>

  2.  You can now compare the two commits by issuing:

          $ rpm-ostree db diff <commit x> <commit y>

### How can I check the version number of an installed package? {#_how_can_i_check_the_version_number_of_an_installed_package}

You can simply use:

    $ rpm -q <package>

### How can I check if an `rpm` software package is available in the repository? {#_how_can_i_check_if_an_rpm_software_package_is_available_in_the_repository}

To search for packages in your enabled repositories, use:

    $ rpm-ostree search <package>

### How can I downgrade my system's kernel? {#_how_can_i_downgrade_my_systems_kernel}

If, for whatever reason, you need to downgrade the kernel, you can do so
by following these steps:

1.  For the version you need to downgrade, download `<kernel>`,
    `<kernel-core>`, `<kernel-modules>`, `<kernel-modules-core>` and
    `<kernel-modules-extra>` from
    [Koji](https://koji.fedoraproject.org/koji/packageinfo?packageID=8).

2.  Install the packages downloaded on the previous step by issuing:

        $ rpm-ostree override replace <kernel> <kernel-core> <kernel-modules> <kernel-modules-core> <kernel-modules-extra>

3.  Reboot the system to apply the changes.

### How can I upgrade my system to the next major version (for instance: rawhide or an upcoming Fedora release branch), while keeping my current deployment? {#pinning}

OSTree allows you to pin deployments (pinning ensures that your
deployment of choice is kept and not discarded).

1.  Assuming that you want to keep your default deployment, issue the
    following command:

    ``` bash
    $ sudo ostree admin pin 0
    ```

    :::: note
    ::: title
    :::

    `0` here refers to the first deployment listed by
    `rpm-ostree status`
    ::::

2.  Verify that you have pinned your deployment of choice by issuing:

    ``` bash
    $ rpm-ostree status
    ```

3.  After the deployment is pinned, you can upgrade your system by using
    the instructions found
    [here](updates-upgrades-rollbacks.xml#upgrading).

4.  When you have completed rebasing, reboot the system. The GRUB menu
    will now present you with both: the previous deployment major
    version entry (e.g.: **\"Fedora {version-oldstable}.YYYYMMDD.n\"**)
    and the new deployment major version entry (e.g.: **\"Fedora
    {version-stable}.YYYYMMDD.n\"**).

    :::: note
    ::: title
    :::

    At the moment it is not possible to name (pinned) deployments and
    their associated GRUB menu entries. = Tips and Tricks
    ::::

## Hiding the default browser (Firefox) {#_hiding_the_default_browser_firefox}

If you're using another browser than the one installed by default
(Firefox) then you can hide the default one from the interface via the
following commands:

    $ sudo cp /usr/share/applications/org.mozilla.firefox.desktop /usr/local/share/applications/
    $ sudo sed -i "2a\\NotShowIn=GNOME;KDE" /usr/local/share/applications/org.mozilla.firefox.desktop
    $ sudo update-desktop-database /usr/local/share/applications/

## Reenabling the default browser (Firefox) {#_reenabling_the_default_browser_firefox}

If you want to make the default browser (Firefox) visible again after
hiding it, you can follow these steps:

    $ sudo rm -f /usr/local/share/applications/*firefox*.desktop
    $ sudo update-desktop-database /usr/local/share/applications

## Enabling RPM Fusion repos {#_enabling_rpm_fusion_repos}

:::: caution
::: title
:::

This section discusses third-party software sources not officially
affiliated with or endorsed by the Fedora Project. Use them at your own
discretion. Fedora recommends the use of free and open source software
and avoidance of software encumbered by patents.
::::

Users may want to take advantage of the non-free software that is made
available via the [RPM Fusion](https://rpmfusion.org/) repos in order to
use the proprietary NVIDIA drivers, multimedia codecs, or other software
not distributed as part of Fedora.

### First installation {#_first_installation}

The first time you install the RPM Fusion repos, you need to install the
versioned RPMs:

``` bash
$ sudo rpm-ostree install \
https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm \
https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
$ reboot
```

Then continue with the next section to prepare your system for major
Fedora updates.

### Major Fedora updates {#_major_fedora_updates}

Once you have rebooted into the new deployment, you can run the
following command to remove the "lock" on the versioned packages that
were installed previously. This will enable the RPM Fusion repos to be
automatically updated and versioned correctly across major Fedora
version rebases:

``` bash
$ sudo rpm-ostree update \
--uninstall rpmfusion-free-release \
--uninstall rpmfusion-nonfree-release \
--install rpmfusion-free-release \
--install rpmfusion-nonfree-release
$ reboot
```

For more information, see [this
thread](https://discussion.fedoraproject.org/t/simplifying-updates-for-rpm-fusion-packages-and-other-packages-shipping-their-own-rpm-repos/30364)
on Fedora Discussion.

## Working with Toolbx {#_working_with_toolbx}

### Finding out if you are currently in a Toolbx container {#_finding_out_if_you_are_currently_in_a_toolbx_container}

If you frequently make use of Toolbx to perform various tasks and use
multiple Toolbx containers it can be hard to keep track of whether you
are currently executing commands on the host or in a Toolbx container.
Furthermore, there is currently no command to tell you in which Toolbx
container you are working.

To alleviate this, you can add the following shell alias at the end of
your `~/.bashrc`:

``` bash
alias istoolbx='[ -f "/run/.toolboxenv" ] && grep -oP "(?<=name=\")[^\";]+" /run/.containerenv'
```

When you open a new shell, you now have access to the new command
`istoolbx`. This will behave as follows:

- When run from the host, returns an exit code of 1.

- When run from a Toolbx container, returns an exit code of 0 and prints
  the current Toolbx containers name to the console.

If a more automated solution is your preference the following added to
your `~/.bashrc` will change your bash prompt to include \"\[toolbox
\<name\>\]\":

``` bash
function is_toolbox() {
if [ -f "/run/.toolboxenv" ]
then
TOOLBOX_NAME=$(cat /run/.containerenv | grep -oP "(?<=name=\")[^\";]+")
echo "[${HOSTNAME} ${TOOLBOX_NAME}]"
fi
}
```

Now you can include `is_toolbox` in your `PS1` variable and not need to
execute any extra commands in order to know whether or not your are in a
toolbox or host shell.

:::: formalpara
::: title
Example:
:::

``` bash
export PS1="\[\e[31m\]\`is_toolbox\`\]\e[m\]\[\e[32m\]\\$ \[\e[m\]\[\e[37m\]❱\[\e[m\] "
```
::::

This results in a prompt which appears as such when not in a toolbox:
`$ ❱`

However, when running in a toolbox named \"default\" looks like:
`[toolbox default]$ ❱`

### Running applications from inside Toolbx on the host {#_running_applications_from_inside_toolbx_on_the_host}

This can be necessary if you want to interact with tools available from
the host, for example `podman`, `nmcli` or `rpm-ostree` without leaving
the Toolbx container in between. You can use `flatpak-spawn`, included
in the base installation for this:

``` bash
$ flatpak-spawn --host podman --help
```

If the application you want to call requires `sudo` access, the `-S`
option must be supplied to `sudo` like below:

``` bash
$ flatpak-spawn --host sudo -S rpm-ostree status
```

If you find yourself using commands like these frequently to access e.g.
the flatpak command from inside the Toolbx container, you can create
yourself a short custom wrapper script (**inside the Toolbx
container**). To do this, perform the following steps:

1.  Define the `istoolbx` alias (for convenience) by executing the
    command mentioned above in your terminal.

2.  Make sure you are in a Toolbx container. If the following command
    doesn't produce any output, you are likely still working on the
    host!

    ``` bash
    [toolbx]$ istoolbx
    <Toolbx container name here>
    ```

3.  Once you have made sure you're in a Toolbx container, execute the
    following command:

    ``` bash
    [toolbx]$ echo -e '#!/bin/sh\nexec /usr/bin/flatpak-spawn --host flatpak "$@"' | \
    sudo tee /usr/local/bin/flatpak 1>/dev/null && sudo chmod +x /usr/local/bin/flatpak
    ```

You now have a `flatpak` command available that allows you to interact
with `flatpak` as if you were running the command on the host.

## Working with `ostree`/`rpm-ostree` {#_working_with_ostreerpm_ostree}

### Tracking changes to the base OS {#_tracking_changes_to_the_base_os}

Some directories in `ostree`-based operating systems are writable by the
user, like `/etc`. You can get a quick overview of the files changed
under `/etc` using the following command:

``` bash
$ sudo ostree admin config-diff
```

To get a more elaborate diff, you can use something like this:

``` bash
$ sudo diff -yrW200 --suppress-common-lines --color=always /usr/etc /etc 2>/dev/null
```

:::: note
::: title
:::

This works because ostree keeps an unmodified copy of the `/etc`
directory under `/usr/etc`. All of your changes go to `/etc` directly.
::::

## Working with Flatpak applications {#_working_with_flatpak_applications}

### Directly accessing Flatpak applications from the CLI {#_directly_accessing_flatpak_applications_from_the_cli}

The most noticable change when using Flatpak applications instead of
conventional installations is that the applications cannot be directly
called from the CLI any more, like so:

``` bash
$ evince
bash: command not found: evince
```

Instead, one can call them like this:

``` bash
$ flatpak run org.gnome.Evince
```

In addition, most Flatpak applications export their internal binaries
under an installation-dependent location:

- For Flatpak applications installed from `system` remotes, these can be
  found under `/var/lib/flatpak/exports/bin/`.

- For Flatpak applications installed from `user` remotes, these can be
  found under `$HOME/.local/share/flatpak/exports/bin/`.

:::: note
::: title
:::

If you're unsure to which installation a Flatpak application belongs,
you can use this command to print it out:

``` bash
$ flatpak list --app --columns=name,installation
```
::::

You can then either add these directories to your `$PATH`:

``` bash
$ org.gnome.Evince
```

or setup shell \`alias\`es as needed to make them available to the CLI
like so:

``` bash
$ alias evince="flatpak run org.gnome.Evince"
### or:
alias evince="org.gnome.Evince"
$ evince
```

- Configuration Guides

# Sway Configuration Guide {#_sway_configuration_guide}

:::: note
::: title
:::

This page provides a brief overview of configuration details specific
for Fedora, and is common to both the package-based Sway Spin and the
Sway Atomic variant. Important differences will be highlighted.
::::

If you are looking for more general resources, please check:

- man pages: [`sway(5)`](https://man.archlinux.org/man/sway.5)
  [`sway-bar(5)`](https://man.archlinux.org/man/sway-bar.5)
  [`sway-input(5)`](https://man.archlinux.org/man/sway-input.5)
  [`sway-output(5)`](https://man.archlinux.org/man/sway-output.5)

- [Official Sway wiki](https://github.com/swaywm/sway/wiki)

- [i3 User's Guide](https://i3wm.org/docs/userguide.html)---while it's
  written for i3, all the important concepts are the same for Sway.

## Configuration profiles {#_configuration_profiles}

The Sway package in Fedora defers most of the dependencies and the
config file ownership to the `sway-config-*` subpackages. This allows us
to ship different configuration profiles with different sets of runtime
dependencies.

The following profile packages are currently available in Fedora:

- **sway-config-upstream** - the upstream configuration as it comes with
  the Sway sources. The only permitted modifications to this profile's
  config file are adjustments for dependencies currently unavailable in
  Fedora.

- **sway-config-minimal** - minimal configuration with any optional
  dependencies excluded. The profile was created for headless servers,
  containers and buildroot usage. It is also suitable for building a
  very minimal installation from scratch.

- **sway-config-fedora** - customized configuration for Fedora Sway
  Spin.

The packages are mutually exclusive, and one of these must be present.
The one installed by default with `dnf install sway` is
**sway-config-upstream** and the one that will be installed with Sway
Spin/Sway Desktop Environment group is **sway-config-fedora**.

You can select the profile with following command:

``` shell
$ sudo dnf swap sway-config sway-config-upstream
$ sudo dnf swap sway-config sway-config-minimal
$ sudo dnf swap sway-config sway-config-fedora
```

The command will replace the default `/etc/sway/config` file and apply
the new set of dependencies. Packages unused by the new profile will be
autoremoved.

The corresponding incantation for Sway Atomic and other custom Sway
images is:

``` shell
$ sudo rpm-ostree override remove sway-config --install sway-config-upstream
```

Note, however, that it does not remove the original profile dependencies
from the base layer of a deployment.

## Fedora configuration {#_fedora_configuration}

[**sway-config-fedora**](https://gitlab.com/fedora/sigs/sway/sway-config-fedora)
contains the default configuration for Fedora Sway Spin. It is built on
top of the default Sway config with a few quality of life improvements
and opinionated changes.

Most of the additions are implemented as a standalone configuration
snippets stored at
[`/usr/share/sway/config.d/`](https://gitlab.com/fedora/sigs/sway/sway-config-fedora/-/tree/fedora/sway/config.d)
and automatically loaded from the main configuration file. Environment
configuration and logging interception are implemented in the
[`/usr/bin/start-sway`](https://gitlab.com/fedora/sigs/sway/sway-config-fedora/-/blob/fedora/sway/start-sway)
wrapper script.

### Environment variables {#_environment_variables}

If you are using a compatible Display Manager (GDM or SDDM), you should
be able to adjust the initial environment for Sway using a system-wide
configuration at `/etc/sway/environment` or per-user config at
`~/.config/sway/environment`. The variables set in the user
configuration overwrite matching variables set system-wide.

Please, check the comments and examples in
[`/etc/sway/environment`](https://gitlab.com/fedora/sigs/sway/sway-config-fedora/-/blob/fedora/sway/environment)
to learn more.

### Sections {#_sections}

The configuration snippets we provide are grouped into the following
sections:

50-59 (`50-rules-*.conf`)

:   Window rules (`for_window`, `assign` and related configuration).

60-69 (`60-bindings-*.conf`, `65-mode-*.conf`)

:   Key bindings and binding modes.

90-94 (`90-*.conf`)

:   System applications: bars, idle daemons and other components.

95-99 (`95-*.conf`)

:   Autostart applications.

### Overrides and load precedence {#_overrides_and_load_precedence}

Fedora configuration abuses the implementation details of the Sway
configuration parser
([`wordexp(3p)`](https://man7.org/linux/man-pages/man3/wordexp.3p.html))
to implement an overrides mechanism for the snippets.

The priority increases from the packaged configuration to a system-wide
configuration and an user configuration directories:

- `/usr/share/sway/config.d/*.conf`

- `/etc/sway/config.d/*.conf`

- `$XDG_CONFIG_HOME/sway/config.d/*.conf` (defaults to
  `~/.config/sway/config.d/*.conf`)

The includes are also sorted by a file name across all the directories.

By creating a file with the same name in `/etc/sway/config.d` you'll
force the config preprocessor to ignore the corresponding snippet from
`/usr` and load the one from `/etc`. Similarly, the configuration
snippet from a home directory wins over the earlier locations.

To put it even more simple: imagine the distribution configuration file
`/usr/share/sway/config.d/90-bar.conf` that sets `waybar` as a status
bar. If you want to prevent `waybar` from starting, you could create an
empty file in your home directory:

``` shell
$ mkdir -p ~/.config/sway/config.d
$ touch ~/.config/sway/config.d/90-bar.conf
```

If you want to use another bar, you just need to add some contents to
the file. For example, copy the default bar section from the upstream
Sway config:

    $ mkdir -p ~/.config/sway/config.d
    $ cat >~/.config/sway/config.d/90-bar.conf <<EOF
    ## Read `man 5 sway-bar` for more information about this section.
    bar {
    position top

    ## When the status_command prints a new line to stdout, swaybar updates.
    ## The default just shows the current date and time.
    status_command while date +'%Y-%m-%d %I:%M:%S %p'; do sleep 1; done

    colors {
    statusline #ffffff
    background #323232
    inactive_workspace #32323200 #32323200 #5c5c5c
    }
    }
    EOF

### Troubleshooting {#_troubleshooting_2}

Sometimes it's useful to know how the configuration loaded by Sway
actually looks. There are two ways to debug that:

- Run sway config validation:

  ``` shell
  $ sway --debug --validate [--config /path/to/config]
  ```

- Check intermediate files generated by the layered include script

      $ less $XDG_RUNTIME_DIR/sway/layered-include-*.conf
