ELN SIG is a Fedora Special Interest Group which is responsible for the
ELN project and its infrastructure.

The official SIG membership list is maintained as part of our Github
Organization and can be viewed
[here](https://github.com/orgs/fedora-eln/people).

# Responsibilities {#_responsibilities}

- Own the scope and configuration of the `eln` disttag and buildroot
  (see [ELN Buildroot](buildroot.xml)).

  - As the project evolves the scope might change. There might be
    additional features which will be included into the tag or excluded
    from it.

- Define ELN content set

- Own the configuration of the compose (see [ELN Compose](compose.xml)).

- Maintain infrastructure required to build packages and composes.

- Track the status of package builds and composes. Work with Fedora
  package maintainers to resolve the issues.

- Keep track of the [RHEL and ELN conditionals](eln-macros.xml) in RPM
  spec files.

- Investigate compose failures

- Own buildroot configuration

# Communication {#_communication}

- Mailing list: Add **\[ELN\]** to the subject of an email to the
  [devel@ mailing
  list](https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/)

- Matrix Room:
  [#eln:fedoraproject.org](https://matrix.to/#/#eln:fedoraproject.org)

## Issue tracker {#_issue_tracker}

- <https://github.com/fedora-eln/eln/issues>

## Meetings {#_meetings}

Meetings of the ELN Special Interest Group are held on Tuesdays at
12:00, US Eastern Time in the Fedora Meeting 1 room on Matrix. It is
listed on the [SIGs calendar](https://calendar.fedoraproject.org/SIGs/).

The meeting agenda will generally be prepared in advance by opening
tickets on the [issue tracker](https://github.com/fedora-eln/eln/issues)
and tagging them with the `Meeting` label.

# How to Join {#_how_to_join}

Anyone may join the SIG by asking to become a member. If no existing SIG
member **opposes** that request within a week, they're in. If an
existing SIG member opposes, we will hold a regular vote at the next
scheduled meeting as described above.

Prospective members may ask to join by filing a \"New Member Request\"
ticket on the [issue
tracker](https://github.com/fedora-eln/eln/issues/new/choose). =
Frequently Asked Questions =

Why ELN?

:   The Fedora distribution is, among other things, an
    [upstream](https://docs.fedoraproject.org/en-US/quick-docs/fedora-and-red-hat-enterprise-linux/)
    for Red Hat Enterprise Linux (RHEL). By adjusting buildroot and
    assorted configurations, ELN allows Fedora contributors who work on
    RHEL and other similarly targeted downstreams to judge the state of
    upstream from their perspective. The benefit for the Fedora
    distribution is that contributors who work on both upstream and
    downstream stay more continuously connected to the state of
    Fedora --- especially, but not exclusively, Rawhide.

What is the role of ELN with respect to CentOS Stream?

:   ELN is a continuous rebuild of Fedora Rawhide sources. Once in a
    while a certain snapshot of the ELN is used to bootstrap the new
    CentOS Stream for the new major RHEL release. There is no continuous
    sync between ELN and any version of the CentOS Stream. Bootstrap
    activity happens only once for each CentOS Stream version. See the
    picture:

![ROOT:fedora eln centos stream
rhel](ROOT:fedora-eln-centos-stream-rhel.png)

What are the differences between Rawhide and ELN?

:   For the majority of packages, there is little or no difference
    between Rawhide and ELN packages. They are the same versions,
    usually built on the same libraries. But there are some [buildroot
    differences](https://docs.fedoraproject.org/en-US/eln/buildroot/) in
    [compiler
    flags](https://docs.fedoraproject.org/en-US/eln/buildroot/#_compiler_flags_and_other_tweaks)
    and [global
    macros](https://docs.fedoraproject.org/en-US/eln/buildroot/#_distribution_related_macro_definitions)
    that can result in build differences.

Note: Many packages have %if fedora / rhel conditionals in their
specfiles that produce differences between the built Rawhide and ELN
packages. Listing all of those differences is beyond the scope of this
document.

What packaging guidelines does ELN follow?

:   Unless otherwise specified in this document, Fedora ELN is required
    to follow all published Fedora Packaging Guidelines. One common
    divergence is with the use of bundled dependencies. In general,
    Fedora packaging recommends that all packages unbundle their
    dependencies into separate packages. However, in some instances this
    can result in a single package requiring many (dozens or hundreds)
    of additional packages. Because of legal restrictions on Red Hat
    Enterprise Linux placed on it for distribution in major markets, it
    is preferred that such cases are instead packaged singly.

What are the differences between the Rawhide and ELN kernel?

:   Kernel is one of the packages that uses %if fedora conditionals
    extensively. While the source tree is the same, the Rawhide kernel
    uses a Fedora configuration and the ELN kernel is built with a RHEL
    kernel configuration. As a result, the Rawhide kernel tends to
    enable support for a much larger range of hardware and features. A
    notable difference is that the ELN kernel does not support btrfs at
    all, making it difficult to install and use on systems that were
    installed as Fedora Workstation edition, or in Fedora 35 or newer
    Cloud images which use btrfs by default. There are also differences
    in baseline supported hardware, meaning the ELN kernel may not run
    on older systems where the Rawhide kernel runs just fine.

When should I use the rpm macro %{eln}?

:   Never. In nearly all cases, you actually want to use the %{rhel}
    macro. See [ELN Macros](eln-macros.xml) for more information.

There is no browser preinstalled in ELN, what should I do?

:   RHEL 11 will only ship and preinstall the Firefox RHEL Flatpak and
    not its RPM version. Because ELN follows closely what RHEL 11 will
    be, it does not include a RPM version of Firefox by default, and
    also no Flatpaks are produced for ELN. To get your installed systems
    as close as possible to RHEL 11, we suggest you to install Firefox
    Fedora Flatpak by following the [installation guide for Fedora
    Flatpaks](https://docs.fedoraproject.org/en-US/flatpak/installation/)
    or Firefox RHEL Flatpak by following the [installation guide for
    RHEL
    Flatpaks](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/administering_the_system_using_the_gnome_desktop_environment/assembly_installing-applications-using-flatpak_administering-the-system-using-the-gnome-desktop-environment).
    Alternatively, there is a `firefox` RPM in the ELN Extras
    repository. KDE users may also wish to install `angelfish`,
    `falkon`, and/or `konqueror` RPMs, except on s390x where they are
    not available.

    - Docs

# Fedora ELN deliverables {#_fedora_eln_deliverables}

:::: warning
::: title
:::

Fedora ELN is a development environment. It is not intended for
production use.
::::

## Compose {#_compose}

The latest production compose of Fedora ELN packages is available at
<https://download.fedoraproject.org/pub/eln/1/>

Server installation media can be found here:
[x86_64](https://download.fedoraproject.org/pub/eln/1/BaseOS/x86_64/iso/)
[aarch64](https://download.fedoraproject.org/pub/eln/1/BaseOS/aarch64/iso/)
[ppc64le](https://download.fedoraproject.org/pub/eln/1/BaseOS/ppc64le/iso/)
[s390x](https://download.fedoraproject.org/pub/eln/1/BaseOS/s390x/iso/)

QEMU qcow2 images can be found here:
[x86_64](https://download.fedoraproject.org/pub/eln/1/BaseOS/x86_64/images/)
[aarch64](https://download.fedoraproject.org/pub/eln/1/BaseOS/aarch64/images/)
[ppc64le](https://download.fedoraproject.org/pub/eln/1/BaseOS/ppc64le/images/)
[s390x](https://download.fedoraproject.org/pub/eln/1/BaseOS/s390x/images/)

See also [Compose](compose.xml).

## Container image {#_container_image}

As a part of the compose, we build container images which are then
published to Quay.io image registry under the name `quay.io/fedora/eln`.

To create and use Fedora ELN container, run:

    podman run -it quay.io/fedora/eln

## Toolbx image {#_toolbx_image}

As a part of the compose, we build
[Toolbx](https://containertoolbx.org/) images which are then published
to Quay.io image registry under the name `quay.io/fedora/eln-toolbox`.

To run Fedora ELN with Toolbx, first create the container:

    toolbox create --image quay.io/fedora/eln-toolbox eln-toolbox

Then run:

    toolbox enter eln-toolbox

## Cloud images {#_cloud_images}

As a part of the compose, we build Cloud images for AWS, Azure, and GCP.
These are uploaded to each cloud provider on a regular basis as a
community offering.

To use, search for **ELN** among community images when creating a new
instance.

## WSL images {#_wsl_images}

As a part of the compose, we build WSL images for both Windows
architectures:
[x64](https://download.fedoraproject.org/pub/eln/1/BaseOS/x86_64/images/)
[arm64](https://download.fedoraproject.org/pub/eln/1/BaseOS/aarch64/images/)

To install and use the first time, download the .wsl image, double-click
the downloaded file, and follow the prompts in the terminal.

For subsequent usage, launch the **Fedora-ELN** entry in the Start Menu,
or run in the Command Prompt or PowerShell:

    wsl -d Fedora-ELN

For more details, see [the Fedora on WSL
documentation](https://docs.fedoraproject.org/en-US/cloud/wsl/).

## Live images {#_live_images}

As a part of the compose, we build GNOME, KDE, and COSMIC Live images
similar to [those produced by the CentOS Alternative Images
SIG](https://sigs.centos.org/altimages/live-images/). These images
contain content from the ELN Extras repository which will not
necessarily be in the next RHEL version but may end up in EPEL.

Live media can be found here:
[x86_64](https://download.fedoraproject.org/pub/eln/1/Extras/x86_64/iso/)
[aarch64](https://download.fedoraproject.org/pub/eln/1/Extras/aarch64/iso/)

## Mock environment {#_mock_environment}

To build custom packages for ELN you can setup Mock environment as
described at [Buildroot](buildroot.xml). = Buildroot configuration =

## Versioning {#_versioning}

In ELN project we work on the buildroot configuration rather than the
content of Fedora packages. As ELN buildroot configuration may change
frequently and independently from Fedora releases, it has its own
versioning.

This approach allows us to rebuild RPM packages on buildroot changes
without changing the spec file of a package in dist-git.

ELN Buildroot version is written as `XY`.

The `X` version refers to major changes in the ELN buildroot (generally
those events that necessitate a mass-rebuild). The `Y` version refers to
changes in the buildroot configuration that are compatible and will
apply to future builds in the ELN buildroot.

We start this number at `100`, where `1` is the X version and `00` is
the Y version.

## Distribution-related Macro Definitions {#_distribution_related_macro_definitions}

In ELN buildroot we build Fedora Rawhide packages in the EL-like
setting. Thus, following macro values are set by default:

+----------------------+----------------------+-----------------------+
| Macro                | Value                | Description           |
+======================+======================+=======================+
| `%{fedora}`          | `%{nil}`             | Unset                 |
+----------------------+----------------------+-----------------------+
| `%{rhel}`            | `11`                 | Integer value one     |
|                      |                      | higher than the most  |
|                      |                      | recently released     |
|                      |                      | major version of RHEL |
+----------------------+----------------------+-----------------------+
| `%{eln}`             | `XY`                 | Version of the eln    |
|                      |                      | buildroot. Not tied   |
|                      |                      | to any RHEL or Fedora |
|                      |                      | release.              |
+----------------------+----------------------+-----------------------+
| `%{dist}`            | `.eln%{eln}`         | eln-disttag, for      |
|                      |                      | example `.eln101`     |
+----------------------+----------------------+-----------------------+

: Macros values

We set these values in Koji for the eln-build tag as follows:

    koji edit-tag \
    -x rpm.macro.fedora=%{nil} \
    -x rpm.macro.rhel=9 \
    -x rpm.macro.eln=101 \
    -x 'rpm.macro.dist=%{!?distprefix0:%{?distprefix}}%{expand:%{lua:for i=0,9999 do print("%{?distprefix" .. i .."}") end}}.eln%{eln}%{?with_bootstrap:~bootstrap}' \
    eln-build

## Compiler flags and other tweaks {#_compiler_flags_and_other_tweaks}

+----------------------+----------------------+-----------------------+
| Arch                 | Rawhide              | ELN                   |
+======================+======================+=======================+
| aarch64              | \-                   | \-                    |
+----------------------+----------------------+-----------------------+
| ppc64le              | `-mcpu=p             | `-mcpu=p              |
|                      | ower8 -mtune=power8` | ower9 -mtune=power10` |
+----------------------+----------------------+-----------------------+
| s390x                | `-m                  | `-                    |
|                      | arch=z13 -mtune=z14` | march=z14 -mtune=z15` |
+----------------------+----------------------+-----------------------+
| x86_64               | `-march=x8           | `-march=x86-          |
|                      | 6-64 -mtune=generic` | 64-v3 -mtune=generic` |
+----------------------+----------------------+-----------------------+

: Compiler Flags

The compiler flag tweaks can be found in /usr/lib/rpm/redhat/macros The
above options are from redhat-rpm-config-200-1

## Building with the ELN buildroot {#building}

Simply specify `eln` as the release when kicking off a `koji` build
using `fedpkg`:

    fedpkg --release eln build [--scratch] [--srpm [SRPM]] [...]

`mock` can also be used to perform builds locally.

A supported `mock` configuration is available in the `mock-core-configs`
package version 33 or later. This enables the ELN environment to be used
locally by running (for arch `x86_64`):

    mock -r fedora-eln-x86_64 ...

:::: note
::: title
:::

If the official `mock` configuration is not yet available, an
unsupported configuration file can be downloaded
[here]({attachmentsdir}/fedora-eln-x86_64.cfg). See
[mock#649](https://github.com/rpm-software-management/mock/pull/649)
::::

# Resolving ELN build failures {#_resolving_eln_build_failures}

This page provides information to assist package maintainers remediate
ELN build failures.

## Background {#_background}

For general information about ELN, visit the [overview](index.xml).

Note what's different with the [buildroot](buildroot.xml) for ELN.

The set of packages that currently need to build for ELN can be found at
<https://tiny.distro.builders/view--view-eln.html>. The expanded package
set including build dependencies can be found at
<https://tiny.distro.builders/view--view-eln-and-buildroot.html>.

There is also an [ELN Build Status page](status.xml#_eln_builds) showing
which packages are currently failing to build for ELN, as well as those
that have a discrepancy between Fedora Rawhide and ELN builds.

## Debugging ELN build failures {#_debugging_eln_build_failures}

Check the details about [how to build](buildroot.xml#building) with
`koji` and `mock` using the ELN buildroot.

## Fixing ELN build failures {#_fixing_eln_build_failures}

### If the package doesn't build for Rawhide, fix that first! {#_if_the_package_doesnt_build_for_rawhide_fix_that_first}

:::: important
::: title
:::

If the package doesn't build for Rawhide, fix that first!
::::

If the package doesn't build for Rawhide, fix that first!

Is that message loud and clear enough? Getting the package build fixed
for Rawhide may very well be all that's needed to fix it for ELN as
well.

### Accounting for differences between Fedora and RHEL {#_accounting_for_differences_between_fedora_and_rhel}

Most build failures can be fixed by modifying the SPEC file. However,
such modifications should be kept to a minimum.

If your package needs to institute different code paths or package
dependencies between Fedora and RHEL, it is important to only account
for the difference for the releases where it is required.

Generally, this means limiting the difference in old versions of Fedora,
while letting the next version of RHEL adopt the Fedora code path.

As one common scenario where a difference is required, RHEL often ends
up with a smaller set of dependencies than Fedora. The `%{fedora}` and
`%{rhel}` macros, when defined, contain the major release versions per
distro.

Consider this SPEC file snippet:

    %if 0%{?fedora} >= 29 || 0%{?rhel} >= 9
    BuildRequires: SomePackage
    %endif

This conditional will be met when `%{rhel}` is defined as 9 or greater.
It is also shareable between earlier and later versions of Fedora and
RHEL. Often it is better to use `<` to limit behaviors to RHEL 8 and
earlier:

    %if 0%{?fedora} < 32 && 0%{?rhel} < 9
    %global rhel8orearlier 1
    %else
    %global rhel9orlater 1
    %endif

The best spec files alter default behavior only for released versions of
Fedora or RHEL, making the default policy the one applicable to the
current versions of Fedora or RHEL.

As a last resort, there is an `%{eln}` macro available. Using it should
be avoided if at all possible. However, if you find you do need to use
it you should only check if it is set to a non-zero value. For example:

    %if 0%{?eln}
    # something specific to ELN only
    ...
    %endif

    %if 0%{?fedora} || 0%{?eln}
    # something specific to Fedora or ELN
    ...
    %endif

    %if 0%{?rhel} && ! 0%{?eln}
    # something specific to RHEL only, not ELN.
    ...
    %endif

### Python 2 deprecation {#_python_2_deprecation}

Just as recent Fedora releases have deprecated Python 2, so have RHEL 9
and ELN. There has been a recurring pattern with ELN build failures that
can be resolved by adjusting the SPEC conditionals to disable Python 2.
For example, if you have something like this:

    %if 0%{?fedora} >= 30
    %global python2_enabled 0
    %else
    %global python2_enabled 1
    %endif

Change the conditional to:

    %if 0%{?fedora} >= 30 || 0%{?rhel} >= 9

### Architecture dependencies {#_architecture_dependencies}

ELN is built for the same set of architectures as Rawhide. However, the
kernel package in ELN no longer produces a full kernel for any 32-bit
architecture. Notably, there is no `kernel` package for architecture
`armv7hl`, only the `kernel-headers` package. To help address this
difference, there is a new `%{kernel_arches}` macro available that can
be used in the SPEC file. For example:

    %ifarch %{kernel_arches}
    BuildRequires: kernel
    %else
    BuildRequires: kernel-headers
    %fi

# ELN Branches {#_eln_branches}

Whenever possible, ELN work should be done in the Fedora rawhide
branches. But sometimes ELN work needs to be done in an Fedora eln
branch. Here are the steps for making that happen.

## Step 1: Request Permission {#_step_1_request_permission}

To prevent a large amount of unmaintained ELN branches as well as to
ensure that ELN's automation does not continue to overwrite changes with
builds from the Rawhide branch, the ELN SIG must approve each request
for a branch.

To request permission, create an [ELN
Issue](https://github.com/fedora-eln/eln/issues).

Be sure to include why you need an eln branch, as well as who will be
maintaining the eln branch.

## Step 2: Create Branch {#_step_2_create_branch}

### You ARE the Fedora maintainer {#_you_are_the_fedora_maintainer}

If you are a Fedora maintainer of the package needing a branch, then the
next step if fairly simple.

    fedpkg request-branch eln --no-auto-module --repo <package>

### You ARE NOT the Fedora maintainer {#_you_are_not_the_fedora_maintainer}

If you are not a Fedora maintainer for the package then you need to ask
one of the Fedora maintainers to create an ELN branch.

If you want to follow the formal route for requesting a branch, then
open a bugzilla ticket for the package.

:::: note
::: title
Bugzilla fields for an ELN branch request (alternative)
:::

- Classification: Fedora

- Product: Fedora

- Component: \<package\>

- Version: rawhide

- Summary: Please branch \<package\> in eln
::::

Clear out Description and put

    Please branch <package> in eln

    fedpkg request-branch eln --no-auto-module --repo <package>

    I will be maintaining the eln branch.

    If you do not think you will be able to do this in a timely manner
    and/or would like me to be a co-maintainer, please add me (FAS <your FAS Id>)
    as a co-maintaine through https://src.fedoraproject.org/rpms/<package>/adduser

## Step 3: Maintain Branch {#_step_3_maintain_branch}

After your branch has been created, remember that the ELN branch is your
responsibility. Do not create the branch, build it once, and then never
touch the branch again.

**If you decide that you no longer need the ELN branch Do not retire the
branch. You must tell the ELN SIG.** The ELN SIG will need to change
configurations as well as retire the branch properly. = ELN Macros

The ELN buildroot defines the %{rhel} macro as the next major version of
RHEL (currently, 11), and does not define the %{fedora} macro. For
almost all cases, this is sufficient for differentiating build behavior
between Fedora and ELN.

## Request Permission {#_request_permission}

To avoid unnecessary divergence between ELN and the next version of
RHEL, the ELN SIG must approve each request for use of the %{eln} macro.

To request permission, create an [ELN
Issue](https://github.com/fedora-eln/eln/issues).

Be sure to include why you need to distinguish ELN from RHEL and/or
CentOS Stream, and why use of the %{fedora}, %{rhel}, and/or %{centos}
macros does not suffice.

## Approved Uses of the %{eln} Macro {#_approved_uses_of_the_eln_macro}

+-----------------------------------+-----------------------------------+
| Package                           | Justification                     |
+===================================+===================================+
| anaconda                          | Package is partly provided in     |
|                                   | CS/RHEL and partly in EPEL, but   |
|                                   | ELN and ELN Extras are not that   |
|                                   | separated                         |
+-----------------------------------+-----------------------------------+
| fedora-eln-backgrounds            | ELN-specific package, not         |
|                                   | imported into CS/RHEL             |
+-----------------------------------+-----------------------------------+
| fedora-logos                      | Fedora-specific package, not      |
|                                   | imported into CS/RHEL             |
+-----------------------------------+-----------------------------------+
| fedora-release                    | Fedora-specific package, not      |
|                                   | imported into CS/RHEL             |
+-----------------------------------+-----------------------------------+
| fedora-repos                      | Fedora-specific package, not      |
|                                   | imported into CS/RHEL             |
+-----------------------------------+-----------------------------------+
| freeipa                           | RHEL-specific branding, does not  |
|                                   | exist in Fedora/ELN               |
+-----------------------------------+-----------------------------------+
| gpsd                              | Package is partly provided in     |
|                                   | CS/RHEL and partly in EPEL, but   |
|                                   | ELN and ELN Extras are not that   |
|                                   | separated                         |
+-----------------------------------+-----------------------------------+
| grub2                             | Secure boot signing differs       |
|                                   | between CS/RHEL and Fedora/ELN    |
+-----------------------------------+-----------------------------------+
| kernel                            | Secure boot signing differs       |
|                                   | between CS/RHEL and Fedora/ELN    |
+-----------------------------------+-----------------------------------+
| libreoffice                       | RHEL-specific branding, does not  |
|                                   | make sense for Fedora/ELN         |
+-----------------------------------+-----------------------------------+
| libreport                         | ELN bugs are to be reported to    |
|                                   | Fedora infrastructure, not        |
|                                   | CS/RHEL                           |
+-----------------------------------+-----------------------------------+
| libxcrypt                         | Package is partly provided in     |
|                                   | CS/RHEL and partly in EPEL, but   |
|                                   | ELN and ELN Extras are not that   |
|                                   | separated                         |
+-----------------------------------+-----------------------------------+
| lorax-templates-rhel              | Downstream repo used as Source    |
|                                   | URL                               |
+-----------------------------------+-----------------------------------+
| lynx                              | RHEL-specific branding, does not  |
|                                   | exist in Fedora/ELN               |
+-----------------------------------+-----------------------------------+
| mock-core-configs                 | ELN has separate mock configs     |
|                                   | from CS and RHEL                  |
+-----------------------------------+-----------------------------------+
| ncurses                           | Package is partly provided in     |
|                                   | CS/RHEL and partly in EPEL, but   |
|                                   | ELN and ELN Extras are not that   |
|                                   | separated                         |
+-----------------------------------+-----------------------------------+
| openssl                           | FIPS certification is for RHEL    |
|                                   | only, not for CS/ELN/Fedora       |
+-----------------------------------+-----------------------------------+
| python-build                      | Package will be partly provided   |
|                                   | in CS/RHEL and partly in EPEL,    |
|                                   | but ELN and ELN Extras are not    |
|                                   | that separated                    |
+-----------------------------------+-----------------------------------+
| python-novaclient                 | Package is built differently for  |
|                                   | OpenStack than for EPEL, and ELN  |
|                                   | Extras is mimicking the latter    |
+-----------------------------------+-----------------------------------+
| python-oslo-utils                 | Package is built differently for  |
|                                   | OpenStack than for EPEL, and ELN  |
|                                   | Extras is mimicking the latter    |
+-----------------------------------+-----------------------------------+
| python-rpm-macros                 | CS/RHEL support multiple Python   |
|                                   | versions, ELN only supports       |
|                                   | latest                            |
|                                   | ([#73](https://gith               |
|                                   | ub.com/fedora-eln/eln/issues/73)) |
+-----------------------------------+-----------------------------------+
| python-requests                   | Package is partly provided in     |
|                                   | CS/RHEL and partly in EPEL, but   |
|                                   | ELN and ELN Extras are not that   |
|                                   | separated                         |
+-----------------------------------+-----------------------------------+
| python-urllib3                    | Package is partly provided in     |
|                                   | CS/RHEL and partly in EPEL, but   |
|                                   | ELN and ELN Extras are not that   |
|                                   | separated                         |
+-----------------------------------+-----------------------------------+
| scap-security-guide               | RHEL-specific subpackage does not |
|                                   | exist in CS/ELN/Fedora            |
+-----------------------------------+-----------------------------------+
| virt-v2v                          | CS/RHEL-specific dependency does  |
|                                   | not exist in Fedora/ELN           |
+-----------------------------------+-----------------------------------+

# ELN Extras {#_eln_extras}

ELN-Extras is essentially an extension of Fedora ELN, with the primary
difference being that the content in ELN-Extras will be defined by the
Fedora/EPEL community, while ELN's content is largely decided upon by
Red Hat management. This will offer users the opportunity to make sure
their applications will work on upcoming releases of RHEL as well as
providing a bootstrapping mechanism for EPEL. It will be far easier and
quicker to get a compose of EPEL N+1 out the door if the initial
packages have already been built for ELN-Extras.

:::: note
::: title
:::

**You** are responsible when your package fails to build on ELN Extras.
Remember to check your packages on [the ELN Status
Page](https://sgallagh.fedorapeople.org/dbs_status.html). ELN Extras
packages get rebuilt much more frequently than in EPEL.
::::

## How to Add a Package to ELN Extras {#_how_to_add_a_package_to_eln_extras}

Adding packages to ELN Extras, is the same as adding them to ELN. The
only difference is that any Fedora packager can add packages to ELN
Extras, while only a handful of people can add packages to ELN.

You add binary packages by creating and submitting workloads for
[Content
Resolver](https://github.com/minimization/content-resolver#readme). You
submit them as pull requests at [content resolver
input](https://github.com/minimization/content-resolver-input). The
workloads go in the config directory.

Once the workloads have been merged, Content Resolver works through all
the dependencies of the workload, subtracts those packages that are
already in ELN, and displays it in its [ELN Extras
view](https://tiny.distro.builders/view--view-eln-extras.html).

After Content Resolver has worked it work, the ELN build process takes
that list and adds it to the ELN Extras build list.

### Workloads {#_workloads}

The full documentation on what goes in a workload yaml file can be found
as comments in the [example workload yaml
file](https://github.com/minimization/content-resolver/blob/master/config_specs/workload.yaml).

The create your initial workload yaml file, take that example yaml file,
rename it, edit it, then submit it as a pull request.

The example workload yaml has an example for everything. But we don't
need everything for ELN Extras.

#### Workload Required Sections {#_workload_required_sections}

- document: feedback-pipeline-workload

  - This exact line, do not change it

- version: 1

  - This exact line, do not change it

- name: \<workload name\>

  - Keep this short, spaces are allowed

- description: \<workload description\>

  - Longer description, but must be on one line

- maintainer: \<FAS and/or Github ID\>

  - Who will be the maintainer of the packages in this workload for ELN
    and EPEL.

  - Do not put someone elses name as maintainer without their
    permission.

- labels: eln-extras

  - Although multiple labels can be listed, for eln-extras, only list
    the one

- packages:

  - List of binary packages in the workgroup

  - DO NOT LIST SOURCE PACKAGE NAMES IN PACKAGES LIST.

  - LIST ALL THE BINARY PACKAGES YOU NEED.

  - If you are listing a package in the optional arch specific package
    list, do not list it here.

#### Workload Optional Sections {#_workload_optional_sections}

- arch_packages:

  - If you have a package that is not built on all arches, you need to
    list it on all the arches it it built on.

  - All noarch packages go in the regular package: section.

- options:

  - If you need to use the options, you can.

#### Workload Unused Sections {#_workload_unused_sections}

- modules_disable:

  - We do not have modules in ELN Extras

- groups:

  - We do not have groups in ELN Extras

- package_placeholders:

  - We do not process package_placeholders in ELN Extras

### ELN-only packages {#_eln_only_packages}

ELN-only packages can also be added to ELN Extras. One example is [-epel
packages](https://docs.fedoraproject.org/en-US/epel/epel-faq/#rhel_8_has_binaries_in_the_release_but_is_missing_some_corresponding__devel_package._how_do_i_build_a_package_that_needs_that_missing__devel_package)
which are often used to provide subpackages that have been unshipped or
otherwise excluded in RHEL. These packages can be added to ELN Extras,
with some additional caveats:

- similarly to regular -epel packages, the package needs to only produce
  the needed subpackages and nothing else

- the package needs to be manually built for ELN from the \"eln\" branch
  in dist-git

- the SRPM name has to be different from the corresponding Rawhide
  package ([example](https://src.fedoraproject.org/rpms/libxcrypt-epel))

- the SRPM name has to be added to the exclusion list in ELNBuildSync to
  avoid accidental rebuilds
  ([example](https://gitlab.com/redhat/centos-stream/ci-cd/distrosync/distrobuildsync-config/-/commit/f50f8d99596cee37fa2b15cd3c62f1c8e86e72fa))

- the needed subpackages need to be added to Content Resolver for ELN
  Extras as usual
  ([example](https://github.com/minimization/content-resolver-input/pull/1124))

## ELN Extras Frequently Asked Questions {#_eln_extras_frequently_asked_questions}

Can I add any or all Fedora packages to ELN-Extras?

:   You are attaching your name as the supporter of these packages. You
    will be submitting these workload packages as pull requests. The ELN
    SIG will review the pull requests and ask questions if things look
    strange or incorrect. So, yes, if you are willing to support a
    package, it can be any Fedora package not in ELN. And while we are
    not putting a firm limit on the number of packages you can add to
    ELN Extras, the SIG is reviewing them and will not merge requests
    that seem excessive for the person requesting them.

If someone has already added a package to their workload, can I have the same package in mine?

:   Yes. Content Resolver is setup to deal with a package in more than
    one workload, or a dependency in more than one workload. It will
    show what workloads list, or require what packages. It even takes a
    guess on who should be the owner of the package.

    - Infrastructure = Fedora ELN Branching Events =

## Fedora Branching {#_fedora_branching}

Fedora Branching happens every 6 months, when Fedora Rawhide branches
for the next release. All examples used in this portion of the document
will be for when Fedora Rawhide is branched for Fedora 41 and Rawhide
becomes Fedora 42.

### Branching Tasks {#_branching_tasks}

1.  Pause the Fedora ELN package rebuilds in ELNBuildSync

    - Set the `configuration.control.pause` value in the ELNBuildSync
      [distrobaker.yaml](https://gitlab.com/redhat/centos-stream/ci-cd/distrosync/distrobuildsync-config/-/blob/main/distrobaker.yaml)
      to `true`

2.  Wait for the Fedora ELN Buildroot to regenerate

\$ koji wait-repo eln-build \--request

1.  Update `configuration.trigger.rpms` in
    [distrobaker.yaml](https://gitlab.com/redhat/centos-stream/ci-cd/distrosync/distrobuildsync-config/-/blob/main/distrobaker.yaml)
    to the next Fedora tag (`f42`)

2.  Resume ELN package rebuilds in ELNBuildSync

    - Set the `configuration.control.pause` value in
      [distrobaker.yaml](https://gitlab.com/redhat/centos-stream/ci-cd/distrosync/distrobuildsync-config/-/blob/main/distrobaker.yaml)
      to `false`

3.  Once a new batch has been processed,[^1] then update `rpm.macro.eln`
    for the `eln-build` Koji tag with the next available number.[^2] For
    example, if the current value is 141

\$ koji edit-tag eln-build -x rpm.macro.eln=142

:::: note
::: title
:::

It's not necessary to wait for ongoing builds to complete before
updating the macro and trigger. The only reason for the pause is to
ensure that nothing else starts before the new trigger is set.
::::

## Fedora Branching and a new CentOS Stream {#_fedora_branching_and_a_new_centos_stream}

This event occurs at the Fedora Branching event that corresponds to the
launch of a new major release of CentOS Stream. Generally, this will be
every three years (or six Fedora releases). All examples used in this
portion of the document will be for when Fedora Rawhide is branched for
Fedora 40, Rawhide becomes Fedora 41 and CentOS Stream 10 is being
launched.

### Branching Tasks {#_branching_tasks_2}

#### On the Fedora Side {#_on_the_fedora_side}

1.  Pause the Fedora ELN package rebuilds in ELNBuildSync

    - Set the `configuration.control.pause` value in the ELNBuildSync
      [distrobaker.yaml](https://gitlab.com/redhat/centos-stream/ci-cd/distrosync/distrobuildsync-config/-/blob/main/distrobaker.yaml)
      to `true`

2.  Wait for any ongoing Fedora ELN builds to complete.

    - Detecting this requires access to the ELNBuildSync logs which are
      non-public at this time.

3.  Disable the DistroBuildSync from Fedora ELN to CentOS Stream

    - Set `enabled: false` in the CentOS Stream distrobaker.yaml [^3]

4.  Update `rpm.macro.eln` for the `eln-build` Koji tag with the next
    available number. For example, if the current value is 135

\$ koji edit-tag eln-build -x rpm.macro.eln=136

1.  Update `rpm.macro.rhel` for the `eln-build` Koji tag with the next
    major release value. For example, if the current value is 10

\$ koji edit-tag eln-build -x rpm.macro.rhel=11

1.  Wait for the Fedora ELN Buildroot to regenerate

\$ koji wait-repo eln-build \--request

1.  Update the
    [fedora-release](https://src.fedoraproject.org/rpms/fedora-release)
    package

    a.  Set `rhel_dist_version` to the same value as `rpm.macro.rhel`
        above.

    b.  Rebuild the `fedora-release` package, coordinating with Fedora
        Release Engineering

2.  Update `kiwibuild_version` in
    <https://pagure.io/pungi-fedora/blob/eln/f/fedora/override.conf> to
    the same value as `rpm.macro.rhel` above

3.  Update `configuration.trigger.rpms` in
    [distrobaker.yaml](https://gitlab.com/redhat/centos-stream/ci-cd/distrosync/distrobuildsync-config/-/blob/main/distrobaker.yaml)
    to the next Fedora tag (`f41`)

4.  Resume ELN package rebuilds in ELNBuildSync

    - Set the `configuration.control.pause` value in
      [distrobaker.yaml](https://gitlab.com/redhat/centos-stream/ci-cd/distrosync/distrobuildsync-config/-/blob/main/distrobaker.yaml)
      to `false`

5.  Schedule a mass-rebuild of Fedora ELN to pick up any pending RHEL
    X+1 changes.[^4] = Fedora ELN compose =

## Summary {#_summary}

The Fedora ELN compose is built using the
[Pungi](https://docs.pagure.org/pungi/) compose tool.

The compose is run automatically four times per day, at 0300, 1500, 1800
and 2100 UTC, though only the first successful compose each day is
normally synced to the mirrors. The [Content
Resolver](https://tiny.distro.builders/) uses each of the composes for
input processing to maintain an accurate view of the state of ELN
throughout the day. The additional composes also serve to provide an
early-warning system of trouble so it can be addressed before the next
day's synced compose.

## Compose configuration files {#_compose_configuration_files}

The main Fedora ELN compose configuration is stored in the official
<https://pagure.io/pungi-fedora/> repository in the `eln` branch.

The Fedora ELN compose uses the `comps-eln.xml` file stored in the
<https://pagure.io/fedora-comps> repository.

## Generating the Fedora ELN compose {#_generating_the_fedora_eln_compose}

Members of the
[sysadmin-eln](https://accounts.fedoraproject.org/group/sysadmin-eln/)
FAS group can manually generate a Fedora ELN compose by logging into the
compose host and performing the following steps:

:::: note
::: title
:::

The first time you need to log in to an infrastructure compose host, you
will need to set up your SSH configuration as described in [Fedora
Infrastructure
Documentation](https://docs.fedoraproject.org/en-US/infra/sysadmin_guide/sshaccess/#_ssh_configuration).
::::

1.  Log in to compose-eln01.iad2.fedoraproject.org

2.  Verify that no compose is already running with
    `ps -ef|grep pungi-koji` or a similar command.

3.  Edit the file `/etc/cron.d/eln`, copying the line containing
    `eln-nightly.sh` to a new line and modifying the cron syntax to
    start the compose two minutes in the future. For example, if the
    current time is 1520 UTC, you would set the cron configuration to
    `22 15 * * *`.

4.  Wait for the compose to start, verifying that it did so with
    `ps -ef|grep pungi-koji`

5.  Remove the additional entry in `/etc/cron.d/eln` so that it does not
    continue to trigger at the same time each day.

6.  (Optional) Monitor the overall compose progress with
    `tail -f /mnt/koji/compose/eln/<compose_id>/logs/global/pungi.global.log`

:::: note
::: title
:::

Normally, the ELN compose will only be synced to the mirror list the
first time that a compose succeeds for that day. In rare situations,
this may need to be overridden. In this case, you will need to modify
the command used to launch the compose to include a `-f` argument to
`eln-nightly.sh`.
::::

# ELN Status {#_eln_status}

## ELN Builds {#_eln_builds}

The table shows the discrepancy between Fedora Rawhide and ELN builds.

Source: <https://sgallagh.fedorapeople.org/dbs_status.html>

[^1]: This timing avoids an accidental mass rebuild from being started
    due to the mass retagging of rawhide builds with the new tag.

[^2]: Current settings are visible on the [eln-build koji
    page](https://koji.fedoraproject.org/koji/taginfo?tagID=22493)

[^3]: Requires access inside the Red Hat firewall

[^4]: For example, frame pointer enablement is conditionalized as
    `%if 0%{?rhel} >= 11`
