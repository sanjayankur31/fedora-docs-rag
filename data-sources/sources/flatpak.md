# Setup on Fedora Linux {#_setup_on_fedora_linux}

Just install the &#96;flatpak&#96; package, if not already installed:

\$ sudo dnf install flatpak

(You may need to log out and log back in.)

:::: note
::: title
:::

On Fedora systems, installing the &#96;flatpak&#96; package also
installs the &#96;fedora-testing&#96; remote, but in disabled state. To
enable it, run:

&#8230;. \$ flatpak remote-modify \--enable fedora-testing &#8230;.
::::

# Setup on Other Systems {#_setup_on_other_systems}

First, install the &#96;flatpak&#96; package through your system's
native package manager.

Then, add the Fedora stable flatpak remote:

\$ flatpak remote-add \--title \'Fedora Flatpaks\' fedora
oci+https://registry.fedoraproject.org

Optionally, add the Fedora testing flatpak remote:

\$ flatpak remote-add \--title \'Fedora Flatpaks (testing)\'
fedora-testing oci+https://registry.fedoraproject.org&#35;testing

# Usage {#_usage}

If installation succeeded, you can now install runtimes, SDKs, or
applications:

\$ flatpak install fedora APP_ID

Graphical package managers (such as GNOME Software or KDE Plasma
Discover) also allow for installation of applications by selecting the
\'Fedora Flatpaks\' software source.

# Flatpak Concepts {#_flatpak_concepts}

## Application ID {#_application_id}

Every application needs a unique application ID, based on a reversed
domain name. For example &#96;org.gnome.Maps&#96;. All resources
exported by the application must be prefixed by this identifier. This
includes the [desktop
file](https://standards.freedesktop.org/desktop-entry-spec/latest/), the
appdata file for the application, and any icons referenced by the
desktop file.

See [Picking an application
ID](in-depth.adoc&#35;_picking_an_application_id).

## Appdata {#_appdata}

The appdata file for a Flatpak is used for displaying information about
the application prior to installation. See [Fedora Packaging Guidelines
for AppData Files](https://fedoraproject.org/wiki/Packaging:AppData).

## Runtimes and bundled libraries {#_runtimes_and_bundled_libraries}

When a Flatpak is executed, the files that the application see come from
two places:

&#42; The Flatpak *runtime*, mounted at &#96;/usr&#96;. This contains
libraries and data files shared by all Fedora Flatpaks. There are
runtimes for each Fedora release. &#42; The Flatpak *application*,
mounted at &#96;/app&#96;. This contains the application code itself,
but also contains any libraries that are bundled with the application.
The application and libraries must be rebuilt with this prefix - this is
done by rebuilding them for flatpaks.

## RPM builds {#_rpm_builds}

Packaging flatpaks in Fedora makes use of RPM builds. The application
and bundled libraries are rebuilt in Fedora's build system (Koji) with a
special build target - this gives a couple of advantages:

&#42; The same RPM spec file used to create the regular RPM build is
also used to create the Flatpak RPM build. &#42; The Flatpak RPM build
target has a different buildroot configuration with macros that result
in RPMs being built with a prefix of &#96;/app&#96;.

Note that Flatpak RPM builds will not work outside the Flatpak context,
since they are rebuilt with a prefix of &#96;/app&#96; with the same
name as system libraries - you cannot use &#96;dnf install&#96; to
install them.

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

Just as for packages, the instructions for building flatpak RPMs and containers are stored in git on <https://src.fedoraproject.org> and builds are coordinated by <https://koji.fedoraproject.org>. The flatpak for a an application can be found on <https://src.fedoraproject.org> in the repository &#96;flatpaks/&lt;application&gt;\\&#96

:   this git repository contains a &#96;container.yaml&#96; file, which
    defines how the package is turned into a Flatpak container.

## Setup {#_setup}

Install the necessary tools:

\$ sudo dnf install flatpak-module-tools

Make sure that your user is in the &#96;mock&#96; group (both local RPM
builds and local container builds use
[mock](https://github.com/rpm-software-management/mock/wiki)).

\$ sudo usermod -a -G mock \$USER

(You may need to log out and log back in.)

Add Fedora testing flatpak remote:

\$ flatpak remote-add fedora-testing
oci+https://registry.fedoraproject.org&#35;testing

:::: note
::: title
:::

On Fedora, the testing remote should be already installed, but in
disabled state. To enable it run:

&#8230;. \$ flatpak remote-modify \--enable fedora-testing &#8230;.

And install the Fedora Flatpak Runtime if you don't already have it
installed:

&#8230;. \$ flatpak install fedora-testing
org.fedoraproject.Platform/x86_64/f{MAJOROSVER} &#8230;.
::::

## Creating &#96;container.yaml&#96; {#_creating_96container_yaml96}

\$ mkdir lagrange &amp;&amp; cd lagrange \$ flatpak-module init
\--flathub=lagrange lagrange

This generates an initial version of &#96;container.yaml&#96;. The
&#96;\--flathub=lagrange&#96; option searches Flathub for an application
whose name or application ID matches &#96;lagrange&#96;, and uses the
Flathub manifest to initialize &#96;container.yaml&#96;. If multiple
matches are found, they are displayed, and you'll need to re-run
&#96;flatpak-module init&#96; with a more specific search string.

Let's look at the &#96;container.yaml&#96; file.

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

This &#96;container.yaml&#96; file can be used as is, but often
modifications are necessary.

If there is no existing build of the application on Flathub, you can
omit the &#96;\--flathub&#96; option to &#96;flatpak-module init&#96;.
In this case you'll need to [pick an application
ID](in-depth.adoc&#35;_picking_an_application_id) and [edit
&#96;container.yaml&#96;](in-depth.adoc&#35;_container_yaml).

## Doing a local build {#_doing_a_local_build}

\$ flatpak-module build-rpms-local \--auto \$ flatpak-module
build-container-local \--install

If building the RPMs succeeds but building the container fails, and you
need to change &#96;container.yaml&#96; and try again, you can repeat
just the last step.

## Testing {#_testing}

If installation succeeded, you can now do:

\$ flatpak run fi.skyjake.Lagrange

To try it out.

## src.fedoraproject.org request {#_src_fedoraproject_org_request}

Please request a new Git repository as follows:

\$ fedpkg request-repo \--namespace=flatpaks &lt;application&gt;

## Importing your flatpak content {#_importing_your_flatpak_content}

Once the repository has been created:

\$ mv &lt;application&gt; &lt;application&gt;.old \$ fedpkg clone
flatpaks/&lt;application&gt; \$ cd &lt;application&gt; \$ cp
../application.old/container.yaml . \$ git add container.yaml \$ git
commit -m \'Initial import\' \$ git push origin stable

## Building in Koji {#_building_in_koji}

First build the packages:

\$ flatpak-module build-rpms \--auto

If that completes successfully, you can then do:

\$ flatpak-module build-container

## Testing the build {#_testing_the_build}

To install the latest successful build from Koji, run:

\$ flatpak-module install \--koji &lt;application&gt;-flatpak

## Creating an update {#_creating_an_update}

Find the NVR of your Flatpak build - if you don't have it in your
terminal scrollback go to <https://koji.fedoraproject.org/> and search
in \'Packages\' for the &#96;&lt;application&gt;-flatpak&#96; name.

Go to <https://bodhi.fedoraproject.org/updates/new> and enter the
flatpak NVR under Candidate Builds (ignore "Packages"). Enter text under
"Update notes" like "Initial Flatpak of &lt;application&gt;", and hit
&lt;Submit&gt;.

# Packaging In Depth {#_packaging_in_depth}

## Is your application suitable? {#_is_your_application_suitable}

Most graphical applications can be made into a Flatpak without
modification, though creating a sandboxed Flatpak that prevents the
application from doing arbitrary things to the user's account is more
likely to require code changes.

Some things that could make an application not work well as a Flatpak:

&#42; If it installs system services or changes system configuration
files &#42; If it needs access to binaries or other files in
&#96;/usr&#96; that can't be bundled with the application

## Picking an application ID {#_picking_an_application_id}

To select an appropriate an [application
ID](concepts.adoc&#35;application_id):

&#42; If the application already has a desktop file of this form, that
is the application ID. &#42; If the application exports any D-Bus
services (Look for files in &#96;/usr/share/dbus-1/services/&#96; -
though an application can export D-Bus services without installing a
service file) then the prefix of the D-Bus name should match the
application ID. &#42; If the application is already packaged on
[Flathub](https://flathub.org) please use the same application ID. &#42;
Otherwise, you need to make up an application ID. This should be your
best possible guess as to what the upstream would use - if they have
their own domain name, that should be the basis, otherwise base it on
the hosting - e.g.
&#96;com.github.&lt;user/organization&gt;.&lt;Application&gt;&#96;. Note
that the original idea of an application ID is that it is in a reversed
name that is under your control, so if possible, please coordinate with
the upstream, ask them if your choice is OK, and ask them to rename
their desktop file and icon to match that.

Applications can only export resources under their application ID, so
the desktop file and icon for the application need the appropriate name.
The best place to implement this is upstream. The second best place is
in the Fedora application package. But if this isn't possible, you can
do this in your container.yaml. See the &lt;&lt;Renames&gt;&gt; section
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
[flatpak-build(1)](https://docs.flatpak.org/en/latest/flatpak-command-reference.html&#35;flatpak-build)
manual page.

### Renames {#_renames}

Many existing applications in Fedora do not have an application in
standard form. You can add keys to your container.yaml to rename
exported resources to match the application ID.

``` yaml
\&#8230;.
flatpak:
rename-appdata-file: eog.appdata.xml
rename-desktop-file: eog.desktop
rename-icon: eog
\&#8230;.
```

The preferred way, however, is to fix the application ID in the RPM
packaging, or even better, upstream. The reason this is better is that
the system can understand the relationship between the two applications,
and won't show duplicate entries in GNOME Software or the installed
application list.

### Other keys {#_other_keys}

The complete list of supported keys from the Flatpak builder manifest
file that you can add to the &#96;flatpak:&#96; section of
&#96;container.yaml&#96; is:

&#42; &#96;add-extensions&#96; &#42; &#96;appdata-license&#96; &#42;
&#96;appstream-compose&#96; &#42; &#96;copy-icon&#96; &#42;
&#96;desktop-file-name-prefix&#96; &#42;
&#96;desktop-file-name-suffix&#96; &#42; &#96;end-of-life&#96; &#42;
&#96;end-of-life-rebase&#96; &#42; &#96;rename-appdata-file&#96; &#42;
&#96;rename-desktop-file&#96; &#42; &#96;rename-icon&#96; &#42;
&#96;rename-mime-file&#96; &#42; &#96;rename-mime-icons&#96;

See the
[flatpak-manifest(5)](https://docs.flatpak.org/en/latest/flatpak-builder-command-reference.html&#35;flatpak-manifest)
manual page for documentation.

# Packaging Runtimes {#_packaging_runtimes}

As we've seen, each Flatpak targets a particular runtime, which provides
shared binaries, libraries, and data files, and is mounted at
&#96;/usr&#96; when the Flatpak is run.

Most Flatpaks in Fedora target the &#96;org.fedoraproject.Platform&#96;
runtime, which is referred to as &#96;runtime-name: flatpak-runtime&#96;
in &#96;container.yaml&#96;. It is similar to the latest version of the
upstream &#96;org.gnome.Platform&#96; runtime, with some additions. In
general, you will not need to modify this runtime when creating an
application, since any additional packages you need will be bundled with
the application. However, if you find a bug in the runtime and want to
help fix it, or want to help participate in maintainance of the Fedora
runtimes, then it's useful to know how runtimes are built.

In addition to the &#96;org.fedoraproject.Platform&#96;, five other
runtimes are built in Fedora infrastructure:

&#96;org.fedoraproject.Sdk&#96;

:   This is a SDK that extends &#96;org.fedoraproject.Platform&#96; with
    compilers and header files to enable building applications against
    it using the flatpak-builder tool.

&#96;org.fedoraproject.KDE6Platform&#96;

:   This runtime includes Qt 6 and KDE Frameworks 6. It is similar to
    the latest 6.x version of the upstream &#96;org.kde.Platform&#96;
    runtime. Referred to as &#96;runtime-name: flatpak-kde6-runtime&#96;
    in &#96;container.yaml&#96;.

&#96;org.fedoraproject.KDE6Sdk&#96;

:   The SDK corresponding to &#96;org.fedoraproject.KDE6Platform&#96;

&#96;org.fedoraproject.KDE5Platform&#96;

:   This runtime includes Qt 5 and KDE Frameworks 5. It is similar to
    the latest 5.15-YY.MM version of the upstream
    &#96;org.kde.Platform&#96; runtime. Referred to as
    &#96;runtime-name: flatpak-kde5-runtime&#96; in
    &#96;container.yaml&#96;.

&#96;org.fedoraproject.KDE5Sdk&#96;

:   The SDK corresponding to &#96;org.fedoraproject.KDE5Platform&#96;

Runtimes are defined in a similar way to Flatpaks. The content of the
runtimes is defined in each runtime's &#96;container.yaml&#96; file:
[&#96;flatpaks/flatpak-runtime&#96;](https://src.fedoraproject.org/flatpaks/flatpak-runtime).
[&#96;flatpaks/flatpak-sdk&#96;](https://src.fedoraproject.org/flatpaks/flatpak-sdk).
[&#96;flatpaks/flatpak-kde6-runtime&#96;](https://src.fedoraproject.org/flatpaks/flatpak-kde6-runtime).
[&#96;flatpaks/flatpak-kde6-sdk&#96;](https://src.fedoraproject.org/flatpaks/flatpak-kde6-sdk).
[&#96;flatpaks/flatpak-kde5-runtime&#96;](https://src.fedoraproject.org/flatpaks/flatpak-kde5-runtime).
[&#96;flatpaks/flatpak-kde5-sdk&#96;](https://src.fedoraproject.org/flatpaks/flatpak-kde5-sdk).
These git repositories should be kept tightly in sync with each other,
but don't need to be modified very often.

The package lists in each &#96;container.yaml&#96; are maintained with
scripts which generate definitions for a runtime and SDK in tandem. For
more information about the maintenance scripts, see the
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

&#42; Checkout the package from dist-git using &#96;fedpkg clone&#96;
&#42; Use &#96;fedpkg switch-branch&#96; to switch to the f{MAJOROSVER}
branch (if significantly different from &#96;rawhide&#96;) &#42; Make
your changes, and make sure that sources are downloaded with &#96;fedpkg
sources&#96; &#42; Build locally with &#96;flatpak-module
build-rpms-local /path/to/checkout&#96; &#42; As needed, build any
further packages with &#96;flatpak-module build-rpms-local \--auto&#96;
&#42; Once successful, install locally with &#96;flatpak-module
build-container-local \--install&#96;

### Quickly debugging prefix=/app builds {#_quickly_debugging_prefixapp_builds}

If you hit a problem where a package fails to build with
&#96;prefix=/app&#96; and you need to debug in detail,

&#42; Build locally with &#96;flatpak-module build-rpms-local
\--auto&#96; (or specify the failing package by SRPM name) &#42; If the
build fails, the console output will display the log files and also
include directions for entering the buildroot:

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

### Files outside of &#96;/app&#96; {#_files_outside_of_96app96}

The most common reason for a packaging failing to build is that some
file in the package is installed with a hard-coded path of
&#96;/usr&#96; rather than respecting the macros such as
&#96;+%{\_prefix}\\&#96;, \\&#96;%{\_libdir}+&#96;, etc. This might
require adjustment of the spec file, passing additional variables into
the make command, or in rare cases, patching the Makefiles.

## Container build problems {#_container_build_problems}

### Package installation failures {#_package_installation_failures}

During installation of packages to build a Flatpak container, the set of
packages is restricted to packages in the runtime and packages rebuilt
for flatpaks. Other packages in Fedora will be ignored. If you see a
message about missing dependencies that you know are in Fedora, this is
because they are being ignored because of this restriction.

&#96;flatpak-module build-rpms \--auto&#96; should build all necessary
dependencies not in the runtime for the flatpak. However, subsequent
packaging changes might add new dependencies, in which case you may need
to run this multiple times.

You could also see failures if a package in the runtime grew a new
dependency and the runtime hasn't been updated. If the package with the
dependency causing the dnf failure isn't part of your flatpak, please
file an issue in the [Fedora Flatpaks issue
tracker](https://gitlab.com/fedora/sigs/flatpak/fedora-flatpaks/-/issues).
