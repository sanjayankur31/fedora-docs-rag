# Welcome {#_welcome}

This is the documentation for &#42;Fedora Minimal&#42;, a Fedora Spin
that focuses on having:

- A small set of packages.

- A small size footprint.

- A small amount of complexity.

- A large amount of
  [customizability](user-guide/customization/index.xml).

This makes &#42;Fedora Minimal&#42; well suited to be used when you want
to often rebuild, or redeploy, your system. &#42;Fedora Minimal&#42;
also tries to serve well as a base for further customization.

## Differences {#_differences}

While there is no over-arching definition of what makes Fedora there are
things that the large majority of Fedora variants share. &#42;Fedora
Minimal&#42; deviates from some of them. Due to the expectation that
end-users will often [customize](user-guide/customization/index.xml)
their images at build-, or provision time these differences only apply
to the images downloaded from the [Fedora
Website](https://fedoraproject.org/spins/minimal/download).

These are the differences we feel are the most important and users
should be aware of before choosing to base their install on &#42;Fedora
Minimal&#42;.

### No &#96;firewalld&#96; {#_no_96firewalld96}

Many Fedora variants have *firewalld* installed and enabled by default.
&#42;Fedora Minimal&#42; does not ship with &#96;firewalld&#96; nor any
other firewall by default allowing you to pick and choose instead.

&#42;Starting from&#42;: Fedora 43.

### &#96;ext4&#96; on &#96;/&#96; {#_96ext496_on_9696}

Most Fedora variants have *btrfs* on their root partition. It is
something Fedora is well known for. &#42;Fedora Minimal&#42; opts to
have the &#96;ext4&#96; filesystem on its root partition:

- Our images want to require minimal support from firmware to be booted.
  This means that sometimes we have to deal with situations where
  firmware wants to read directly from the root filesystem. btrfs
  support exists in firmware such as u-boot, however it is often turned
  off or not available.

- We want to support &#96;systemd-firstboot \--image=&#96; for our users
  to provision images before booting them. &#96;systemd-firstboot
  \--image=&#96; does not currently understand a *btrfs* root partition.

Because &#42;Fedora Minimal&#42; focuses on customizability it can be
[built](user-guide/installation.xml) with btrfs, see our
[blueprints](user-guide/customization/blueprint.adoc&#35;_btrfs).

&#42;Starting from&#42;: Fedora 38.

### No &#96;/etc/fstab&#96; {#_no_96etcfstab96}

&#42;Fedora Minimal&#42; uses mount units and the discoverable partition
specification by default. This means it ships without an
&#96;/etc/fstab&#96; file. You can still create one if you prefer it.

&#42;Starting from&#42;: Fedora 43.

# Community {#_community}

## Matrix {#_matrix}

Quick questions and chat with other users of &#42;Fedora Minimal&#42;
mostly takes place in our &#35;minimal:fedoraproject.org\[Matrix
channel\].

## Bugs {#_bugs}

### Documentation {#_documentation}

Have you found a typo, a link that doesn't work, or do you feel
something should be written down when it isn't? Any issues with the
documentation or pull requests to improve documentation should be filed
at [its
repository](https://github.com/fedora-minimal/documentation-minimal).

### Distribution {#_distribution}

The distribution concerns itself with what &#42;Fedora Minimal&#42; is
and its base setup. Its default configuration files, default
partitioning, and the default set of packages. Some examples of
distribution bugs would be:

1.  &#96;systemd-firstboot&#96; is not letting me set a root password on
    first boot.

2.  &#42;Fedora Minimal&#42; doesn't boot on my Pi 5.

If you find bugs of this sort, or want to discuss package removals and
default configuration don't hesistate to file an issue at the
[distribution
repository](https://github.com/fedora-minimal/distribution-minimal).

# Changelog {#_changelog}

## Fedora 43 {#_fedora_43}

During this release we focused on minimizing the package set that is
installed by default in &#42;Fedora Minimal&#42;.

- Disabled rescue kernel generation on boot. This was accidentally
  enabled again in one of the previous versions but turned off again in
  Fedora 43. See
  [discussion](https://github.com/fedora-minimal/distribution-minimal/issues/10).

- Removed &#96;firewalld&#96; from the package set. See
  [discussion](https://github.com/fedora-minimal/distribution-minimal/issues/1).

- Disabled &#96;/etc/fstab&#96;, only mount units are available by
  default. See
  [discussion](https://github.com/fedora-minimal/distribution-minimal/issues/15).

## Fedora 42 {#_fedora_42}

The &#42;Fedora Minimal SIG&#42; was created to outline better what
&#42;Fedora Minimal&#42; is, its usecases, and its differences from
other Fedora variants.

## Fedora 38 {#_fedora_38}

The &#42;Fedora Minimal&#42; aarch64 image became a [Release
Blocking](https://docs.fedoraproject.org/en-US/releases/f38/blocking/)
artifact.

## History {#_history}

&#42;Fedora Minimal&#42; has been around in some way or shape since
around Fedora 11 or 12. There are a few wiki pages around for the spin.

# User Guide {#_user_guide}

Information for users of &#42;Fedora Minimal&#42;. To be expanded.

# Installation {#_installation}

## Getting an Image {#_getting_an_image}

### Download {#_download}

Pre-built uncustomized images of &#42;Fedora Minimal&#42; are available
from the [Fedora Spins
page](https://fedoraproject.org/spins/minimal/download).

You can get disk images or installers.

### Build {#_build}

You can build a &#42;Fedora Minimal&#42; image locally. Doing so ensures
that it is built with the latest available packages and that you can
apply your [build-time
customizations](user-guide/customization/index.xml) directly.

To build &#42;Fedora Minimal&#42; you'll need access to a
&#42;Fedora&#42; system:

``` console
$ sudo dnf install -y image-builder
$ sudo image-builder build --distro fedora-43 minimal-raw-zst
\&#35; \&#8230;
```

You can [customize](user-guide/customization/index.xml) your build as
well by adding packages, changing partitions, including containers, or
other things.

# Customization {#_customization}

&#42;Fedora Minimal&#42; is a great base Fedora to start layering your
own choices on top of. Since it comes with very little, and doesn't do
much you're free to do whatever you want with it. When customizing your
&#42;Fedora Minimal&#42; you need to decide what you want to change, or
add, and when you want to do that.

Generally speaking you likely want to do your customizations at
&lt;&lt;Build Time,build&gt;&gt; time leaving only deployment specific
things to be configured later. For example you pick your packages,
partitioning, and services at build time but let your users choose the
locale, keyboard layout, and timezone during first boot of the system.

## Why? {#_why}

## When? {#_when}

It is possible to customize &#42;Fedora Minimal&#42; at various stages.

### Build Time {#_build_time}

Configuration at build time is the preferred way to customize
&#42;Fedora Minimal&#42;. It makes it easy to rebuild your image with
the latest software, share your customizations, and to share the built
image itself for consumption by other users.

When [building](user-guide/installation.xml) an image it is possible to
pass a blueprint file describing what you want to change. For example,
using the following blueprint file:

``` toml
packages = [
{ name = 'tmux' },
{ name = 'firewalld' },
]

customizations.user = [
{ name = 'user', 'key' = 'ssh-ed25519 XXX user@localhost', groups = ['wheel'] }
]
```

With the following command:

``` console
$ sudo dnf install -y image-builder
$ sudo image-builder build --distro fedora-43 --blueprint my-changes.toml minimal-raw-zst
\&#35; \&#8230;
```

Will get you a &#42;Fedora Minimal&#42; with &#96;tmux&#96;, and
&#96;firewalld&#96; installed and a user called &#96;user&#96; with the
given SSH key in its authorized keys.

We have a list of [blueprint
examples](user-guide/customization/blueprint.xml) handy for you if you
want some inspiration of what is possible. If you want to know more you
can also read the &#96;image-builder&#96; [documentation on the
blueprint
format](https://osbuild.org/docs/user-guide/blueprint-reference/).

### Provision Time {#_provision_time}

The provisioning time is the span between when you &lt;&lt;Build
Time,build&gt;&gt; your image and the time that the image is running on
a system. We can further divide the provision time in a few stages.

#### Image {#_image}

It is possible to customize an image after it is built. The most common
use cause would be to set up some values that would normally be prompted
for when the machine &lt;&lt;First-boot,boots for the first
time&gt;&gt;. We generally recommend against customizing an image
directly unless it's to do what is written here. Any other
customizations that need to happen are better done during &lt;&lt;Build
Time,build&gt;&gt; as they are error prone and can interfere with your
systems operation, or its deployment otherwise.

&#42;Fedora Minimal&#42; uses &#96;systemd-firstboot&#96; for its
&lt;&lt;First-boot,first-boot&gt;&gt; setup. &#96;systemd-firstboot&#96;
can also be used to customize an image directly. You can do so like
this:

``` console
$ sudo systemd-firstboot --image=disk.img --prompt
\&#35; \&#8230;
```

When executed this command will prompt for information that is not yet
stored inside the image. It can configure:

1.  locale

2.  timezone

3.  keymap

4.  hostname

5.  &#96;root&#96; password

If you have customized any of these during &lt;&lt;Build
Time,build&gt;&gt; then &#96;systemd-firstboot&#96; will not prompt for
them when customizing the image.

#### First-boot {#_first_boot}

First boot customizations take place during the first boot of the
system. &#42;Fedora Minimal&#42; is set up so that any unconfigured
values that are necessary for the system to progress into runtime can be
configured on the console. This only happens once: on the first boot of
the system. The customizations for first boot can be skipped by
configuring them in the &lt;&lt;Image,image&gt;&gt; or
&lt;&lt;Pre-boot,pre-boot&gt;&gt; stages.

&#42;Fedora Minimal&#42; uses &#96;systemd-firstboot&#96; for its
&lt;&lt;First-boot,first-boot&gt;&gt; setup. When the system detects
that it is booting for the first time &#96;systemd-firstboot&#96;
verifies if the following information is available:

1.  locale

2.  timezone

3.  keymap

4.  hostname

5.  &#96;root&#96; password

If you have customized any of these during &lt;&lt;Build
Time,build&gt;&gt;, or &lt;&lt;Image,image&gt;&gt; then
&#96;systemd-firstboot&#96; will not prompt for them. When all
information has been previously provided the prompt will be skipped
entirely.

### Run Time {#_run_time}

Runtime customizations are those that take place after the system has
booted and entered its running state. Any changes you make after this
state has been reached are called run time customizations. There's
nothing special in &#42;Fedora Minimal&#42; for this.

## Suggestions {#_suggestions}

It can be a bit difficult to figure out which customizations should be
done when. In general we recommend to do as much as possible at
&lt;&lt;Build Time,build time&gt;&gt; with very little happening in the
later lifecycle of an image. Following this suggestion means it is easy
for you to distribute your image and install it on varied systems,
leaving only what is absolutely necessary to be done on a per-deployment
basis.

Some examples of things you might want to do at &lt;&lt;Build Time,build
time&gt;&gt;:

1.  Installing packages.

2.  Changing configuration files.

3.  Adding system user accounts for run time management.

4.  Picking a partition layout if your deployment permits.

5.  Switching the kernel for another one.

Some examples of things you might want to leave to the &lt;&lt;Provision
Time,provisioning time&gt;&gt; of a system:

1.  Setting the timezone of the system.

2.  Picking a keyboard layout.

3.  Growing partitions and filesystems to fill a disk.

4.  Setting network configuration.

5.  Creating a personal user account.

# Blueprints {#_blueprints}

Blueprints are the format used by &#96;image-builder&#96;, which is a
tool you can use to build your &#42;Fedora Minimal&#42; with [build
time](./index.xml) customizations. The below examples are short, use
case specific, examples of blueprints. You can find more about
blueprints at the [upstream
documentation](https://osbuild.org/docs/user-guide/partitioning/) for
&#96;image-builder&#96;.

The below examples can be put into a file called
&#96;my-minimal.toml&#96; (or any filename you prefer) and passed to
&#96;image-builder&#96;:

``` console
$ sudo dnf install -y image-builder
$ sudo image-builder build --blueprint my-minimal.toml minimal-raw-zst
\&#35; \&#8230;
```

## Packages {#_packages}

Adding some packages to &#42;Fedora Minimal&#42; to make it yours is the
customization most people make. If you want to have your packages come
from custom repositories such as RPMfusion, COPR, or vendor
repositories, take a look at &lt;&lt;Repositories,repository
customization&gt;&gt; as well.

``` toml
packages = [
{ name = 'tmux' },
{ name = 'python3' },
]
```

It's also possible to refer to composition groups, which are used to
group relevant packages together. The following setup mimicks Fedora
KDE. Note that this does &#42;not&#42; turn your built image into Fedora
KDE. Fedora KDE artifacts are tested by a group of people, while
customizations applied on top of Fedora Minimal are not.

``` toml
packages = [
{ name = '@kde-desktop-environment' },
{ name = '@kde-apps' },
{ name = '@kde-media' },
{ name = '@kde-pim' },
{ name = '@kde-spin-initial-setup' },
{ name = '@firefox' },
{ name = '@libreoffice' },
{ name = 'libreoffice-draw' },
{ name = 'libreoffice-math' },
{ name = 'fuse' },
{ name = 'kde-l10n' },
]

\&#35; We need a bit more space than the default 4 GiB for the
\&#35; disk image.
customizations.disk.minsize = '10 GiB'
```

You might be wondering why packages are objects with a &#96;name&#96;
key. That's because you can also supply &#96;version&#96; to install a
package at a specific version, given that it is available in the
repositories.

## Repositories {#_repositories}

Sometimes you'll want additional repositories to be used by your image.
These values are (mostly) the same as what you would find in a
repository configuration for &#96;dnf&#96;.

``` toml
[[customizations.repositories]]
id = 'example'
name = 'An example repository'
baseurls = ['https://example.com/']
enabled = true
install_from = true
```

This example will add the &#96;example&#96; repository to be used when
installing packages from your &lt;&lt;Packages,package
customization&gt;&gt; and be configured in the resulting image to be
available to &#96;dnf&#96;.

It is important to note that &#96;image-builder&#96; makes a distinction
between repositories used to assemble the system and those used for the
&lt;&lt;Packages,package customization&gt;&gt;. If you want to enable,
or replace, repositories used to assemble the system itself then read
the [advanced customization](./advanced.xml) page.

## Users {#_users}

You can add, or modify users in the image you are building with the
&#96;users&#96; customization. Users are identified by name. If the user
already exists (for example, because one of the packages you installed
created the user) it will be modified. If the user doesn't exist it will
be created.

``` toml
[[customizations.users]]
name = 'myuser'
key = 'ssh-ed25519 AAxxxAA user@host'
```

Will create or update the user by the name of &#96;myuser&#96; setting
their SSH authorized keys to the given key. For more options read the
[upstream
documentation](https://osbuild.org/docs/user-guide/blueprint-reference/&#35;additional-users)
for &#96;image-builder&#96;.

## Partitioning {#_partitioning}

By default &#42;Fedora Minimal&#42; uses \'raw\' GPT partitioning with
an &#96;ext4&#96; root partition mounted at &#96;/&#96;. This can be
changed in the following ways. If you want to know more about
partitioning and how it behaves you can read the [upstream
documentation](https://osbuild.org/docs/user-guide/partitioning/) for
&#96;image-builder&#96;.

### btrfs {#_btrfs}

To build an image that uses btrfs you can use the following blueprint.
This mimicks the Fedora Workstation subvolumes.

``` toml
[[customizations.disk.partitions]]
type = 'btrfs'
minsize = '3 GiB'
subvolumes = [
{ name = 'root', mountpoint = '/' },
{ name = 'home', mountpoint = '/home' },
]
```

It can be wise to also have &#96;/var&#96; on a separate subvolume.

### lvm {#_lvm}

To build an image that uses LVM:

``` toml
[[customizations.disk.partitions]]
type = 'lvm'
minsize = '3 GiB'
```

This will convert the partition that contains the root mountpoint
&#96;/&#96; to an LVM Volume Group containing a root Logical Volume.

### Using a DOS partition table {#_using_a_dos_partition_table}

You can switch from a GPT partitioned disk to one that uses DOS
partitioning. This might be necessary to be able to boot on some
machines such as the Raspberry Pi 3. For more tricks for specific
hardware take a look at [hardware
support](../user-guide/hardware-support.xml).

``` toml
[customizations.disk]
type = 'dos'
```

# Advanced Customization {#_advanced_customization}

Some customizations aren't available, or easy, with
[blueprints](./blueprint.xml). This is because while some care is taken
to not break builds when using blueprints there are things which have a
larger chance of breaking a build.

## Repositories {#_repositories_2}

While you can configure [repositories](./blueprint.xml) that are used
for additional packages these repositories do not affect those used for
the system itself. If you want to change where packages used to assemble
the system itself come from you can do so in the following ways.

### Extra {#_extra}

Adding an additional repository allows you to enable (for example) COPR
repositories for other kernels. Packages available in the repository are
used as normal, if they have higher versions they are preferred to those
from other repositories.

``` console
$ sudo image-builder --extra-repo https://copr/ minimal-raw-zst
\&#35; \&#8230;
```

### Force {#_force}

You can also replace all repositories used to assemble the base system,
this is more useful if you want to for example build a repository from a
specific compose. The repository will need to contain all packages that
&#42;Fedora Minimal&#42; requires.

``` console
$ sudo image-builder --force-repo https://copr/ minimal-raw-zst
\&#35; \&#8230;
```

# Hardware Support {#_hardware_support}

&#42;Fedora Minimal&#42; by default works well with UEFI speaking
bootloaders. Disks are partitioned with GPT.

## Specific {#_specific}

Some platforms require specific customizations to boot or work well.

### Raspberry Pi 3 {#_raspberry_pi_3}

The Raspberry Pi 3 does not understand the default GPT disk layouts that
&#42;Fedora Minimal&#42; uses. You can use the following [partition
customization](./customization/blueprint.xml) to build an image that
supports it.

``` toml
[customizations.disk]
type = 'dos'
```

Note that this changes the partition table to the DOS format which has
implications for any further partitioning you might want to do.

### Raspberry Pi 5 {#_raspberry_pi_5}

The Raspberry Pi 5 does not yet have good upstream support in the
kernel. This means that in general Fedora variants don't work on it, or
work partially. There are kernels available in COPR which have
additional potential patches which aren't yet available in the kernels
Fedora uses. While these won't make *everything* work, more things will
work.

With the following [blueprint](./customization/blueprint.xml) to enable
the repository for updates after the system has booted.

``` toml
[[customizations.repositories]]
id = 'copr:copr.fedorainfracloud.org:pbrobinson:a64-kernel'
name = 'Copr repo for a64-kernel owned by pbrobinson'
baseurls = ['https://download.copr.fedorainfracloud.org/results/pbrobinson/a64-kernel/fedora-$releasever-$basearch/']
enabled = true
```

And the following [build command](./customization/advanced.xml) to use
the repository for system build. Note the single quotes around the
repository URL to prevent shell expansion of variables.

``` console
$ sudo image-builder build --extra-repo 'https://download.copr.fedorainfracloud.org/results/pbrobinson/a64-kernel/fedora-$releasever-$basearch/' minimal-raw-zst
\&#35; \&#8230;
```

You get a &#42;Fedora Minimal&#42; with the kernel and patches from the
COPR repository which gives you the highest chance of the most things
working. If you're only testing hardware bringup then the blueprint part
can be skipped but you won't get updates to the kernel on the system
after it has booted.
