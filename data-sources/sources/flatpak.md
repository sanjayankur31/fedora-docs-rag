# Setup on Fedora Linux {#_setup_on_fedora_linux}

Just install the `flatpak` package, if not already installed:

\$ sudo dnf install flatpak

(You may need to log out and log back in.)

:::: note
::: title
:::

On Fedora systems, installing the `flatpak` package also installs the
`fedora-testing` remote, but in disabled state. To enable it, run:

    $ flatpak remote-modify --enable fedora-testing
::::

# Setup on Other Systems {#_setup_on_other_systems}

First, install the `flatpak` package through your system's native
package manager.

Then, add the Fedora stable flatpak remote:

\$ flatpak remote-add \--title \"Fedora Flatpaks\" fedora
oci+https://registry.fedoraproject.org

Optionally, add the Fedora testing flatpak remote:

\$ flatpak remote-add \--title \"Fedora Flatpaks (testing)\"
fedora-testing oci+https://registry.fedoraproject.org#testing

# Usage {#_usage}

If installation succeeded, you can now install runtimes, SDKs, or
applications:

\$ flatpak install fedora APP_ID

Graphical package managers (such as GNOME Software or KDE Plasma
Discover) also allow for installation of applications by selecting the
\"Fedora Flatpaks\" software source.

# Flatpak Concepts {#_flatpak_concepts}

## Application ID {#_application_id}

Every application needs a unique application ID, based on a reversed
domain name. For example `org.gnome.Maps`. All resources exported by the
application must be prefixed by this identifier. This includes the
[desktop
file](https://standards.freedesktop.org/desktop-entry-spec/latest/), the
appdata file for the application, and any icons referenced by the
desktop file.

See [Picking an application
ID](in-depth.xml#_picking_an_application_id).

## Appdata {#_appdata}

The appdata file for a Flatpak is used for displaying information about
the application prior to installation. See [Fedora Packaging Guidelines
for AppData Files](https://fedoraproject.org/wiki/Packaging:AppData).

## Runtimes and bundled libraries {#_runtimes_and_bundled_libraries}

When a Flatpak is executed, the files that the application see come from
two places:

- The Flatpak *runtime*, mounted at `/usr`. This contains libraries and
  data files shared by all Fedora Flatpaks. There are runtimes for each
  Fedora release.

- The Flatpak *application*, mounted at `/app`. This contains the
  application code itself, but also contains any libraries that are
  bundled with the application. The application and libraries must be
  rebuilt with this prefix - this is done by rebuilding them for
  flatpaks.

## RPM builds {#_rpm_builds}

Packaging flatpaks in Fedora makes use of RPM builds. The application
and bundled libraries are rebuilt in Fedora's build system (Koji) with a
special build target - this gives a couple of advantages:

- The same RPM spec file used to create the regular RPM build is also
  used to create the Flatpak RPM build.

- The Flatpak RPM build target has a different buildroot configuration
  with macros that result in RPMs being built with a prefix of `/app`.

Note that Flatpak RPM builds will not work outside the Flatpak context,
since they are rebuilt with a prefix of `/app` with the same name as
system libraries - you cannot use `dnf install` to install them.

## OCI Images {#_oci_images}

For Fedora, Flatpak runtimes and applications are built as [OCI
Images](https://github.com/opencontainers/image-spec/blob/master/spec.md)
and distributed via <https://registry.fedoraproject.org>. This allows
Flatpaks to be handled in a very similar way to server side containers.
(Flatpaks are also commonly distributed via
[ostree](https://ostree.readthedocs.io/en/latest/).)

# Packaging Tutorial {#_packaging_tutorial}

Creating a Flatpak of an application that is already packaged in Fedora
involves two steps. First you need to rebuild the application RPMs along
with any dependencies which are not included in the runtime. Then you
need to create a container out of the application. In the Fedora
context, flatpaks are just another form of container, and are handled
very similar to the Docker containers used for server applications.

Just as for packages, the instructions for building flatpak RPMs and
containers are stored in git on <https://src.fedoraproject.org> and
builds are coordinated by <https://koji.fedoraproject.org>. The flatpak
for a an application can be found on <https://src.fedoraproject.org> in
the repository `flatpaks/<application>`; this git repository contains a
`container.yaml` file, which defines how the package is turned into a
Flatpak container.

## Setup {#_setup}

Install the necessary tools:

\$ sudo dnf install flatpak-module-tools

Make sure that your user is in the `mock` group (both local RPM builds
and local container builds use
[mock](https://github.com/rpm-software-management/mock/wiki)).

\$ sudo usermod -a -G mock \$USER

(You may need to log out and log back in.)

Add Fedora testing flatpak remote:

\$ flatpak remote-add fedora-testing
oci+https://registry.fedoraproject.org#testing

:::: note
::: title
:::

On Fedora, the testing remote should be already installed, but in
disabled state. To enable it run:

    $ flatpak remote-modify --enable fedora-testing

And install the Fedora Flatpak Runtime if you don't already have it
installed:

    $ flatpak install fedora-testing org.fedoraproject.Platform/x86_64/f{MAJOROSVER}
::::

## Creating `container.yaml` {#_creating_container_yaml}

\$ mkdir lagrange && cd lagrange \$ flatpak-module init
\--flathub=lagrange lagrange

This generates an initial version of `container.yaml`. The
`--flathub=lagrange` option searches Flathub for an application whose
name or application ID matches `lagrange`, and uses the Flathub manifest
to initialize `container.yaml`. If multiple matches are found, they are
displayed, and you'll need to re-run `flatpak-module init` with a more
specific search string.

Let's look at the `container.yaml` file.

:::: formalpara
::: title
container.yaml
:::

``` yaml
flatpak:
id: fi.skyjake.Lagrange
branch: stable
runtime-name: flatpak-runtime
runtime-version: f{MAJOROSVER}
packages:
- lagrange
command: lagrange
finish-args: |-
--socket=wayland
--socket=fallback-x11
--socket=pulseaudio
--share=ipc
--share=network
--device=dri
--filesystem=xdg-download
--filesystem=home:ro
```
::::

This `container.yaml` file can be used as is, but often modifications
are necessary.

If there is no existing build of the application on Flathub, you can
omit the `--flathub` option to `flatpak-module init`. In this case
you'll need to [pick an application
ID](in-depth.xml#_picking_an_application_id) and [edit
`container.yaml`](in-depth.xml#_container_yaml).

## Doing a local build {#_doing_a_local_build}

\$ flatpak-module build-rpms-local \--auto \$ flatpak-module
build-container-local \--install

If building the RPMs succeeds but building the container fails, and you
need to change `container.yaml` and try again, you can repeat just the
last step.

## Testing {#_testing}

If installation succeeded, you can now do:

\$ flatpak run fi.skyjake.Lagrange

To try it out.

## src.fedoraproject.org request {#_src_fedoraproject_org_request}

Please request a new Git repository as follows:

\$ fedpkg request-repo \--namespace=flatpaks \<application\>

## Importing your flatpak content {#_importing_your_flatpak_content}

Once the repository has been created:

\$ mv \<application\> \<application\>.old \$ fedpkg clone
flatpaks/\<application\> \$ cd \<application\> \$ cp
../application.old/container.yaml . \$ git add container.yaml \$ git
commit -m \"Initial import\" \$ git push origin stable

## Building in Koji {#_building_in_koji}

First build the packages:

\$ flatpak-module build-rpms \--auto

If that completes successfully, you can then do:

\$ flatpak-module build-container

## Testing the build {#_testing_the_build}

To install the latest successful build from Koji, run:

\$ flatpak-module install \--koji \<application\>-flatpak

## Creating an update {#_creating_an_update}

Find the NVR of your Flatpak build - if you don't have it in your
terminal scrollback go to <https://koji.fedoraproject.org/> and search
in \"Packages\" for the `<application>-flatpak` name.

Go to <https://bodhi.fedoraproject.org/updates/new> and enter the
flatpak NVR under Candidate Builds (ignore "Packages"). Enter text under
"Update notes" like "Initial Flatpak of \<application\>", and hit
\<Submit\>.

# Packaging In Depth {#_packaging_in_depth}

## Is your application suitable? {#_is_your_application_suitable}

Most graphical applications can be made into a Flatpak without
modification, though creating a sandboxed Flatpak that prevents the
application from doing arbitrary things to the user's account is more
likely to require code changes.

Some things that could make an application not work well as a Flatpak:

- If it installs system services or changes system configuration files

- If it needs access to binaries or other files in `/usr` that can't be
  bundled with the application

## Picking an application ID {#_picking_an_application_id}

To select an appropriate an [application
ID](concepts.xml#application_id):

- If the application already has a desktop file of this form, that is
  the application ID.

- If the application exports any D-Bus services (Look for files in
  `/usr/share/dbus-1/services/` - though an application can export D-Bus
  services without installing a service file) then the prefix of the
  D-Bus name should match the application ID.

- If the application is already packaged on
  [Flathub](https://flathub.org) please use the same application ID.

- Otherwise, you need to make up an application ID. This should be your
  best possible guess as to what the upstream would use - if they have
  their own domain name, that should be the basis, otherwise base it on
  the hosting - e.g. `com.github.<user/organization>.<Application>`.
  Note that the original idea of an application ID is that it is in a
  reversed name that is under your control, so if possible, please
  coordinate with the upstream, ask them if your choice is OK, and ask
  them to rename their desktop file and icon to match that.

Applications can only export resources under their application ID, so
the desktop file and icon for the application need the appropriate name.
The best place to implement this is upstream. The second best place is
in the Fedora application package. But if this isn't possible, you can
do this in your container.yaml. See the [Renames](#_renames) section
below.

## Versioning {#_versioning}

Flatpaks in Fedora are different from packages in that there isn't a
separate application version for F{PREVIOUSOSVER}, F{MAJOROSVER},
rawhide, etc. Instead there is a single version that is the latest
stable version for all versions of Fedora.

A flatpak targets a particular runtime. Your stable version should
ideally target the runtime corresponding to the latest released version
of Fedora. If the application cannot yet be built for the latest
released version of Fedora, then it's acceptable to temporarily use the
previous version of the Fedora runtime, but this should be an unusual
case.

:::: note
::: title
:::

In general, previous versions of the runtime are supported only as long
as Fedora flatpaks still require them. Once all Fedora flatpak have been
migrated to the latest runtime version, the previous versions are no
longer supported or updated.
::::

The container version for your stable release should be in the stable
branch of your git repository.

## container.yaml {#_container_yaml}

### finish-args {#_finish_args}

The flatpak/finish-args: section of your container.yaml determines what
permissions the application will have.

:::: formalpara
::: title
Non-sandboxed application, application requires X, and accesses the
network
:::

``` yaml
flatpak:
finish-args: |-
--share=network
--socket=x11
--filesystem=user
```
::::

:::: formalpara
::: title
Sandboxed application
:::

``` yaml
flatpak:
finish-args: |-
--socket=wayland
--socket=fallback-x11
```
::::

:::: formalpara
::: title
Non-sandboxed application, application has wayland support, and uses the
host DConf
:::

``` yaml
flatpak:
finish-args: |-
--filesystem=host
--share=ipc
--socket=fallback-x11
--socket=wayland
--socket=session-bus
--filesystem=~/.config/dconf:ro
--filesystem=xdg-run/dconf
--talk-name=ca.desrt.dconf
--env=DCONF_USER_CONFIG_DIR=.config/dconf
```
::::

See [Sandbox
Permissions](https://docs.flatpak.org/en/latest/sandbox-permissions.html)
documentation and the
[flatpak-build(1)](https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-build)
manual page.

### Renames {#_renames}

Many existing applications in Fedora do not have an application in
standard form. You can add keys to your container.yaml to rename
exported resources to match the application ID.

``` yaml
flatpak:
rename-appdata-file: eog.appdata.xml
rename-desktop-file: eog.desktop
rename-icon: eog
```

The preferred way, however, is to fix the application ID in the RPM
packaging, or even better, upstream. The reason this is better is that
the system can understand the relationship between the two applications,
and won't show duplicate entries in GNOME Software or the installed
application list.

### Other keys {#_other_keys}

The complete list of supported keys from the Flatpak builder manifest
file that you can add to the `flatpak:` section of `container.yaml` is:

- `add-extensions`

- `appdata-license`

- `appstream-compose`

- `copy-icon`

- `desktop-file-name-prefix`

- `desktop-file-name-suffix`

- `end-of-life`

- `end-of-life-rebase`

- `rename-appdata-file`

- `rename-desktop-file`

- `rename-icon`

- `rename-mime-file`

- `rename-mime-icons`

See the
[flatpak-manifest(5)](https://docs.flatpak.org/en/latest/flatpak-builder-command-reference.html#flatpak-manifest)
manual page for documentation. = Packaging Runtimes

As we've seen, each Flatpak targets a particular runtime, which provides
shared binaries, libraries, and data files, and is mounted at `/usr`
when the Flatpak is run.

Most Flatpaks in Fedora target the `org.fedoraproject.Platform` runtime,
which is referred to as `runtime-name: flatpak-runtime` in
`container.yaml`. It is similar to the latest version of the upstream
`org.gnome.Platform` runtime, with some additions. In general, you will
not need to modify this runtime when creating an application, since any
additional packages you need will be bundled with the application.
However, if you find a bug in the runtime and want to help fix it, or
want to help participate in maintainance of the Fedora runtimes, then
it's useful to know how runtimes are built.

In addition to the `org.fedoraproject.Platform`, five other runtimes are
built in Fedora infrastructure:

`org.fedoraproject.Sdk`

:   This is a SDK that extends `org.fedoraproject.Platform` with
    compilers and header files to enable building applications against
    it using the flatpak-builder tool.

`org.fedoraproject.KDE6Platform`

:   This runtime includes Qt 6 and KDE Frameworks 6. It is similar to
    the latest 6.x version of the upstream `org.kde.Platform` runtime.
    Referred to as `runtime-name: flatpak-kde6-runtime` in
    `container.yaml`.

`org.fedoraproject.KDE6Sdk`

:   The SDK corresponding to `org.fedoraproject.KDE6Platform`

`org.fedoraproject.KDE5Platform`

:   This runtime includes Qt 5 and KDE Frameworks 5. It is similar to
    the latest 5.15-YY.MM version of the upstream `org.kde.Platform`
    runtime. Referred to as `runtime-name: flatpak-kde5-runtime` in
    `container.yaml`.

`org.fedoraproject.KDE5Sdk`

:   The SDK corresponding to `org.fedoraproject.KDE5Platform`

Runtimes are defined in a similar way to Flatpaks. The content of the
runtimes is defined in each runtime's `container.yaml` file:
[`flatpaks/flatpak-runtime`](https://src.fedoraproject.org/flatpaks/flatpak-runtime).
[`flatpaks/flatpak-sdk`](https://src.fedoraproject.org/flatpaks/flatpak-sdk).
[`flatpaks/flatpak-kde6-runtime`](https://src.fedoraproject.org/flatpaks/flatpak-kde6-runtime).
[`flatpaks/flatpak-kde6-sdk`](https://src.fedoraproject.org/flatpaks/flatpak-kde6-sdk).
[`flatpaks/flatpak-kde5-runtime`](https://src.fedoraproject.org/flatpaks/flatpak-kde5-runtime).
[`flatpaks/flatpak-kde5-sdk`](https://src.fedoraproject.org/flatpaks/flatpak-kde5-sdk).
These git repositories should be kept tightly in sync with each other,
but don't need to be modified very often.

The package lists in each `container.yaml` are maintained with scripts
which generate definitions for a runtime and SDK in tandem. For more
information about the maintenance scripts, see the
[README.md](https://github.com/owtaylor/flatpak-runtime-scripts/) for
flatpak-runtime and flatpak-sdk, or the
[README.md](https://src.fedoraproject.org/flatpaks/flatpak-kde6-runtime/)
for the KDE runtime and SDK.

# Troubleshooting {#_troubleshooting}

## Package build problems {#_package_build_problems}

### Rebuilding a flatpak against a local component {#_rebuilding_a_flatpak_against_a_local_component}

If you find a build problem with a package in your flatpak, you'll want
to build the flatpak using a local git checkout for the package, so you
can put fixes in there:

- Checkout the package from dist-git using `fedpkg clone`

- Use `fedpkg switch-branch` to switch to the f{MAJOROSVER} branch (if
  significantly different from `rawhide`)

- Make your changes, and make sure that sources are downloaded with
  `fedpkg sources`

- Build locally with `flatpak-module build-rpms-local /path/to/checkout`

- As needed, build any further packages with
  `flatpak-module build-rpms-local --auto`

- Once successful, install locally with
  `flatpak-module build-container-local --install`

### Quickly debugging prefix=/app builds {#_quickly_debugging_prefixapp_builds}

If you hit a problem where a package fails to build with `prefix=/app`
and you need to debug in detail,

- Build locally with `flatpak-module build-rpms-local --auto` (or
  specify the failing package by SRPM name)

- If the build fails, the console output will display the log files and
  also include directions for entering the buildroot:

:::: formalpara
::: title
console output
:::

    python-pyside6: Build failed
    x86_64/work/rpms/python-pyside6/build.log
    x86_64/work/rpms/python-pyside6/hw_info.log
    x86_64/work/rpms/python-pyside6/installed_pkgs.log
    x86_64/work/rpms/python-pyside6/mock_output.log
    x86_64/work/rpms/python-pyside6/root.log
    x86_64/work/rpms/python-pyside6/state.log
    chroot: /var/lib/mock/flatpak-module-f{MAJOROSVER}-x86_64-0/root/
    Enter chroot: mock -r x86_64/work/rpms/mock.cfg --uniqueext 0 --shell
::::

### Files outside of `/app` {#_files_outside_of_app}

The most common reason for a packaging failing to build is that some
file in the package is installed with a hard-coded path of `/usr` rather
than respecting the macros such as `%{_prefix}`, `%{_libdir}`, etc. This
might require adjustment of the spec file, passing additional variables
into the make command, or in rare cases, patching the Makefiles.

## Container build problems {#_container_build_problems}

### Package installation failures {#_package_installation_failures}

During installation of packages to build a Flatpak container, the set of
packages is restricted to packages in the runtime and packages rebuilt
for flatpaks. Other packages in Fedora will be ignored. If you see a
message about missing dependencies that you know are in Fedora, this is
because they are being ignored because of this restriction.

`flatpak-module build-rpms --auto` should build all necessary
dependencies not in the runtime for the flatpak. However, subsequent
packaging changes might add new dependencies, in which case you may need
to run this multiple times.

You could also see failures if a package in the runtime grew a new
dependency and the runtime hasn't been updated. If the package with the
dependency causing the dnf failure isn't part of your flatpak, please
file an issue in the [Fedora Flatpaks issue
tracker](https://gitlab.com/fedora/sigs/flatpak/fedora-flatpaks/-/issues).
