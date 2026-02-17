&#42; &#42;&#42;What is Modularity&#42;&#42; = Introduction

:::: warning
::: title
:::

&#42;&#42;The Modularity project has been retired&#42;&#42; and there
are [no modules in Fedora 39 or
newer](https://fedoraproject.org/wiki/Changes/RetireModularity) or [in
EPEL](https://lists.fedoraproject.org/archives/list/epel-announce@lists.fedoraproject.org/thread/KA3JQUZW63A4V7OQ7ZVDFCM32EQUSOXH/).
This page is only retained for historical reference.
::::

Welcome to the Modularity project documentation.

The &#42;&#42;Modularity&#42;&#42; project has been created for the
purpose of enabling additional versions/flavours of RPM packages in one
RPM repository. A standard RPM repository contains RPM packages which
are uniquely identified by their name. Of course the package name is not
the only package identifier, we have more identifiers (NEVRA) for more
granular identification of packages. Basically it was not possible to
have multiple RPM packages of the same name in one RPM repository. When
we say multiple RPM packages with the same name, we mean RPM packages
which are not updates, but RPM packages which are built with different
options and features or are built from different source code. In
general, Fedora tends to ship the latest stable versions of software
available. At the same time, packages need to maintain a certain API/ABI
stability throughout the life cycle of the release they are part of. The
problem with this approach is finding the right balance of being too
fast vs. too slow. For example, developers in general tend to prefer the
newest versions of software, while server administrators want API/ABI
stability for a longer period of time. Modularity removes this
limitation of a RPM repository with the addition of Module streams.

\+

\+

# Modular Repository {#_modular_repository}

In the picture below you can see a classic example of official RPM
repositories in the Fedora linux distribution. Fedora Linux is providing
one major version of RPM packages for each Fedora release. This is
simple view of a "classic" or a non-modular repository.

![fedora without modularity](fedora-without-modularity.png)

In the following picture we describe a [modular
repository](glossary.adoc&#35;_modular_repository). A modular repository
provides multiple module streams which contain additional RPM packages
which can have the same name. A [modular
repository](glossary.adoc&#35;_modular_repository) can still provide RPM
packages which are not part of any module but are part of the RPM
repository.

![fedora with modularity](fedora-with-modularity.png)

So in short, Modularity can expand a RPM repository with following
features:

&#42; Module streams add additional packages with the same name, but
built from different sources and with different build configurations.
&#42; Module streams can have different life cycles. For example a
package in a distribution can have a different life cycle than the life
cycle of the distribution. &#42; Module streams can have different
installation profiles of its components i. e. you can define one or
several module stream profiles which will contain groups of RPMs which
should be installed together.

# When should you use Modularity? {#_when_should_you_use_modularity}

Any RPM repository can be converted into a modular RPM repository with
the inclusion of modular metadata and corresponding binary RPMs. The
following points will help you to decide if Modularity can be useful to
you.

&#42; You need/want to provide additional major versions of your
existing RPM packages i. e. postgresql 10, postgresql 11 within one
Fedora release or a custom RPM repository. &#42; You need/want to
provide additional custom flavours of your existing RPM packages i. e.
custom build RPM packages with a variety of features. &#42; You
need/want to have different life cycles of your packages in a RPM
repository. &#42; You are building Flatpaks. RPM package dependencies
installed into Flatpak sandoxes are module streams. &#42; In general
Modularity is a good fit for providing alternative RPM packages for
sandbox environments which use RPM based distributions. (Flatpak, linux
containers etc.)

## Examples {#_examples}

&#42;&#42;Scenario 1&#42;&#42;: Some users install packages coming from
a different Fedora release in order to consume a specific version of a
database that is compatible with their application. But thanks to
Modularity they might not need to do that anymore, because multiple
versions of the database can be available in each Fedora release. All
they need to do is to consume the specific stream of that database right
from the Fedora repositories for their system.

&#42;&#42;Scenario 2:&#42;&#42; There were cases when users couldn't
upgrade their system to a new Fedora release because their application
wouldn't function with the new version of a language runtime coming with
the upgrade. Modularity can fix this problem by providing the same
language versions in both Fedora releases. With that, the user can
consume a specific stream of the language and keep it even when they
upgrade their system. And when the application is ready for the new
language version, it can be upgraded later, independently from the OS,
by switching to a different stream.

# Community {#_community}

:::: warning
::: title
:::

&#42;&#42;The Modularity project has been retired&#42;&#42; and there
are [no modules in Fedora 39 or
newer](https://fedoraproject.org/wiki/Changes/RetireModularity) or [in
EPEL](https://lists.fedoraproject.org/archives/list/epel-announce@lists.fedoraproject.org/thread/KA3JQUZW63A4V7OQ7ZVDFCM32EQUSOXH/).
This page is only retained for historical reference.
::::

This page lists the communication channels of members of the Modularity
Working Group (Modularity WG), related projects and also how you can
contribute to the project.

\+

\+

## Channels {#_channels}

There are two main communication channels the Modularity WG uses:

IRC channel [&#35;fedora-devel](https://web.libera.chat/&#35;fedora-devel) on Libera.Chat

:   Most of the discussions happen on this IRC channel.

[devel@lists.fedoraproject.org](https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/) mailing list

:   The Modularity WG doesn't have a dedicated mailing list. Instead,
    the Fedora Devel mailing list is used time to time for more complex
    decisions or announcements.

Related channels:

[server@lists.fedoraproject.org](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/)

:   The [Server SIG](https://fedoraproject.org/wiki/Server) also
    discusses Modularity at times as the Server Edition is a primary
    stakeholder in the goals of the [Modularity
    Objective](https://fedoraproject.org/wiki/Objectives&#35;Current).

## Working Groups and Teams {#_working_groups_and_teams}

Modularity is driven by the Modularity and DNF team.

&#42; Martin Čurlej <mcurlej@redhat.com> --- Modularity product owner
and tech lead &#42; Petr Písař <ppisar@redhat.com> --- Developer and
libmodulemd maintainer &#42; Marek Kulik <mkulik@redhat.com> ---
Developer and infrastructure &#42; Jaroslav Mráček <jmracek@redhat.com>
--- Modularity in DNF

However, Modularity couldn't happen without other working groups
contributing a significant portion of effort into it, i.e.:

&#42; [Server Working Group](https://fedoraproject.org/wiki/Server)
&#42; [Fedora Release Engineering](https://docs.pagure.org/releng/)
&#42; [Fedora
Infrastructure](https://fedoraproject.org/wiki/Infrastructure)

## Reporting Issues {#_reporting_issues}

General issues such as bugs or feature requests for the Modularity
project can be created by anyone in the [General Modularity issue
tracker](https://pagure.io/modularity/issues)[]{#gerneral_tracker}. This
issue tracker is then processed by the team and new issues or even
issues against other projects may be created as a result.

### Issues with Content {#_issues_with_content}

&#42; [Fedora Modules product in
Bugzilla](https://bugzilla.redhat.com/enter_bug.cgi?product=Fedora%20Modules)
--- Bugs in concrete Fedora modules. &#42; [fedora-module-defaults issue
tracker](https://pagure.io/releng/fedora-module-defaults/issues) ---
Setting default profiles, default streams, stream end of lives,
obsoleted and replacing streams.

### Tools Related to Modularity: {#_tools_related_to_modularity}

&#42; [Fedora Infrastructure issue
tracker](https://pagure.io/fedora-infrastructure/) --- Issues related to
[Module Build Service
(MBS)](https://mbs.fedoraproject.org/module-build-service/2/module-builds/)
and particular MBS module builds (started with &#96;fedpkg
module-build&#96;). Use this tracker, for instance, if your build hangs
without finishing or failing. &#42; [Module Build Service issue
tracker](https://pagure.io/fm-orchestrator/issues) --- Issues regarding
MBS source code. If your want to propose changing a syntax or semantics
of the MBS input (modulemd documents) or the MBS output (RPM packages
built in a module or resulting modular metadata), it does belong to the
&lt;&lt;general_tracker, general tracker&gt;&gt;. &#42; [libmodulemd
issue tracker](https://github.com/fedora-modularity/libmodulemd/issues)
--- Issues regarding the modulemd specification, libmodulemd library,
and modulemd-validator tool. &#42; [modulemd-tools issue
tracker](https://github.com/rpm-software-management/modulemd-tools/issues)
--- A collection of tools for module maintainers. &#42; [DNF component
in
Bugzilla](https://bugzilla.redhat.com/enter_bug.cgi?product=Fedora&amp;short_desc=%5Bmodularity%5D&amp;component=dnf)
--- Issues regarding the &#96;dnf module&#96; command.

# Glossary {#_glossary}

:::: warning
::: title
:::

&#42;&#42;The Modularity project has been retired&#42;&#42; and there
are [no modules in Fedora 39 or
newer](https://fedoraproject.org/wiki/Changes/RetireModularity) or [in
EPEL](https://lists.fedoraproject.org/archives/list/epel-announce@lists.fedoraproject.org/thread/KA3JQUZW63A4V7OQ7ZVDFCM32EQUSOXH/).
This page is only retained for historical reference.
::::

Modularity introduces a lot of new keywords to the established packaging
ecosystem. This is a short glossary to get you started on the basic
terms.

\+

\+

## Modularity Project {#_modularity_project}

&#42; Modularity project is an extension to the RPM ecosystem that
allows to distribute and consume &lt;&lt;Modular Repository,Modular
Repositories&gt;&gt; with alternative content.

## Modular Repository {#_modular_repository_2}

&#42; Modular repository is an RPM repository extended with
&lt;&lt;Module Metadata (modulemd),Module Metadata&gt;&gt;. It allows
users to query and fetch information about the available Module Streams
as well as RPM packages from them.

## Module Stream {#_module_stream}

&#42; Module Stream is a collection of RPM packages as defined by the
&lt;&lt;Module Metadata (modulemd),Module Metadata&gt;&gt;. &#42;
Usually, a Module Stream represents a certain major version or a
specific build configuration of RPM packages grouped together by
purpose. More specific example would be postgres:12: a Module Stream of
the postgres Module with PostgreSQL version 12 and PostgreSQL-12-related
packages.

## Module {#_module}

&#42; Collection of Module Streams with the same name. &#42; For
example: postgresql module consists of postgresql:10 and postgresql:12
&lt;&lt;Module Strea,Module Streams&gt;&gt;. "Module" is also frequently
used as an informal reference to &lt;&lt;Module Artifact&gt;&gt;. For
example: Hey buddy, I've just built the
postgresql:12:20200101:aabbccdd:x86_64 module, go check it out!

## Default Module Stream {#_default_module_stream}

&#42; Default Module Stream is a &lt;&lt;Module Stream&gt;&gt;
pre-selected by the software distributor (such as Fedora or RHEL
authorities) to be implicitly considered for package installation and
dependency resolution and automatically enabled when packages from the
stream are needed. One Module can only have zero or one Default Module
Stream. &#42; Example: The nodejs:14 &lt;&lt;Module Stream&gt;&gt; is
the Default Module Stream of the nodejs &lt;&lt;Module&gt;&gt; and the
stream contains a libuv package. When the user installs libuv (directly
or indirectly), the nodejs:14 &lt;&lt;Module Stream&gt;&gt; is
automatically enabled without an explicit user action. Installation of
the libuv package from any other &lt;&lt;Module Stream&gt;&gt; or from a
non-module repository requires explicit action (such as disabling the
nodejs:14 stream).

## Module Artifact {#_module_artifact}

&#42; &lt;&lt;Module Metadata (modulemd),Module Metadata&gt;&gt; + built
RPMs identified by &lt;&lt;NSVCA,N:S:V:C:A&gt;&gt;.

## Module Build {#_module_build}

&#42; Module Build is a collection of &lt;&lt;Module Artifact,Module
Artifacts&gt;&gt; with the same &lt;&lt;NSVCA,NSVC&gt;&gt;

## Module Metadata (modulemd) {#_module_metadata_modulemd}

&#42; Module Metadata is a modulemd yaml document that contains
information about a &lt;&lt;Module Artifact,Module Artifact&gt;&gt;.
Module Metadata can be found in modules.yaml in the repodata. &#42; For
more information see [this
topic](building-modules/fedora/defining-modules.xml). &#42; The standard
for yaml modulemd files is defined
[here](https://github.com/fedora-modularity/libmodulemd/tree/main/yaml_specs).

## NSVCA {#_nsvca}

&#42; This abbreviation describes the new naming conventions for
&lt;&lt;Module,modules&gt;&gt; i. e.
Name:Stream:Version:Context:Architecture. &#42; For more information see
[this section](core-concepts/nsvca.xml).

&#42; &#42;&#42;Consuming Modules&#42;&#42; = Using modules in Fedora

:::: warning
::: title
:::

&#42;&#42;The Modularity project has been retired&#42;&#42; and there
are [no modules in Fedora 39 or
newer](https://fedoraproject.org/wiki/Changes/RetireModularity) or [in
EPEL](https://lists.fedoraproject.org/archives/list/epel-announce@lists.fedoraproject.org/thread/KA3JQUZW63A4V7OQ7ZVDFCM32EQUSOXH/).
This page is only retained for historical reference.
::::

&#42;&#42;Modules&#42;&#42; are special package groups usually
representing an application, a language runtime, or a set of tools. They
are available in one or &#42;&#42;multiple streams&#42;&#42; which
usually represent a major version of a piece of software, giving you an
option to choose what versions of packages you want to consume.

To simplify installation, modules usually define one or more
&#42;&#42;installation profiles&#42;&#42; that represent a specific use
case. For example a &#96;server&#96; or a &#96;client&#96; profile in a
database module.

This is a quick overview how to use modules and module streams with the
package manager DNF.

\+

\+

## Module stream installation and discovery {#_module_stream_installation_and_discovery}

### Listing packages {#_listing_packages}

Packages available to the system can be discovered by the usual commands
such as &#96;dnf search NAME&#96;, &#96;dnf list NAME&#96;, or by using
the &#96;dnf repoquery QUERY&#96; command for more complex queries.
However, it is important to note that those commands will, apart from
traditional packages, only list modular packages coming from already
*enabled* module stream.

### Listing modules {#_listing_modules}

To list modules available to your system, and to see what streams are
*default* or have been *enabled*, use the following command:

``` console
$ dnf module list
```

### Installing packages {#_installing_packages}

Packages can be installed the usual way by running the &#96;dnf install
NAME&#96; command. Any traditional package, or a modular package coming
from an *enabled* module can be installed this way.

Packages from other module streams can be consumed by either *enabling a
module* stream and then installing individual packages, or by
*installing a module* directly.

### Enabling modules {#_enabling_modules}

To &#42;&#42;enable a module stream&#42;&#42; and make its packages
available for installation, run the following command:

``` console
$ dnf module enable NAME:STREAM
```

For example, to make Node.js 8 packages available for installation, run:

``` console
$ dnf module enable nodejs:8
```

Packages from enabled module streams can be then installed by the
&#96;dnf install NAME&#96; command.

### Installing modules {#_installing_modules}

To install a module, use one of the following commands. Not specifying a
*stream* or a *profile* causes DNF to choose the *default*. However, not
every module has a *default stream* or a *default profile*. In that case
you need to specify the stream or the profile explicitly.

``` console
$ dnf module install NAME
$ dnf module install NAME:STREAM
$ dnf module install NAME/PROFILE
$ dnf module install NAME:STREAM/PROFILE
```

For example, to install the Node.js 8 runtime and the client tooling of
the default stream of MongoDB, run:

``` console
$ dnf module install nodejs:8
$ dnf module install mongodb/client
```

### Switching module streams {#_switching_module_streams}

:::: note
::: title
:::

Switching streams is a risky operation that might not be always
supported in packages, especially downgrades.
::::

Switching to a different stream than the one that is installed on a
system done with the &#96;switch-to&#96; argument.

``` console
$ dnf module switch-to NAME:STREAM
```

An example, to switch from Node.js 8 to Node.js 10, run:

``` console
$ dnf module switch-to nodejs:10
```

An example, to switch from Node.js 10 to Node.js 8, run:

``` console
$ dnf module switch-to nodejs:8
```

:::: note
::: title
:::

The &#96;switch-to&#96; argument is the recommended and prefered way to
switch streams.
::::

The &#96;switch-to&#96; argument includes multiple actions which need to
be executed to safetly switch to another module stream.

In this example we show a manual switch from Node.js 8 to Node.js 10
without the &#96;switch-to&#96; argument run:

``` console
$ dnf remove nodejs
$ dnf module reset nodejs:8
$ dnf module enable nodejs:10
$ dnf install nodejs
```

:::: note
::: title
:::

The &#96;dnf module info NAME:STREAM&#96; command is helpful to check
RPMs in a module stream.
::::

## Updating the system {#_updating_the_system}

Updating a system by running the &#96;dnf update&#96; command causes all
packages to be upgraded to their latest version provided by their module
stream.

## Removing modules {#_removing_modules}

In general, to remove a module installed on your system, use the
following command:

``` console
$ dnf module remove MODULE:STREAM/PROFILE
```

## Advanced {#_advanced}

There is a situation when a specific package has been installed first,
and then a module has been installed after that. Example:

``` console
$ dnf install ruby
$ dnf module install ruby:2.6/default
```

In this case, running the &#96;dnf module remove&#96; command would not
remove the &#96;ruby&#96; package, as DNF remembers that package has
been explicitly installed.

To make the &#96;ruby&#96; package uninstalled with the &#96;dnf module
remove&#96; command, run the following:

``` console
$ dnf mark group ruby
$ dnf module remove ruby:2.6/default
```

That is because DNF remembers a reason why a package has been installed.
There are three, sorted from the strongest:

&#42; *user* &#42; *group* &#42; *dependency*

Because modules use the *group* reason, which is weaker than *user* used
by the &#96;dnf install&#96; command, the package stays on the system
after running the &#96;dnf module remove&#96; command. \'Downgrading\'
it to *group*, however, makes the &#96;dnf module remove&#96; remove it
as well.

## Modular filtering and conflicts {#_modular_filtering_and_conflicts}

When consuming module streams a lot of operations are being executed. A
module stream contains alternative modular RPM packages which can have
the same name as already existing non-modular RPM packages, a lot of
conflicts can arise. In the next few examples we will show you some of
the conflicts.

### Switching a module stream without removing the RPM packages from the old module stream {#_switching_a_module_stream_without_removing_the_rpm_packages_from_the_old_module_stream}

:::: formalpara
::: title
broken dependencies when switching module streams without removing the
installed content
:::

``` console
[root@5e7d134a8883 /]\&#35; dnf module install nodejs:14/common
Last metadata expiration check: 0:02:38 ago on Thu Mar  3 08:57:00 2022.
Dependencies resolved.

Problem 1: cannot install the best candidate for the job
- nothing provides /usr/bin/pwsh needed by nodejs-1:14.19.0-2.module_f35+13766+ad18d3e5.x86_64
Problem 2: package npm-1:6.14.16-1.14.19.0.2.module_f35+13766+ad18d3e5.x86_64 requires nodejs = 1:14.19.0-2.module_f35+13766+ad18d3e5, but none of the providers can be installed
- cannot install the best candidate for the job
- nothing provides /usr/bin/pwsh needed by nodejs-1:14.19.0-2.module_f35+13766+ad18d3e5.x86_64
===========================================================================================================================================================================
Package                             Architecture              Version                                                            Repository                          Size
===========================================================================================================================================================================
Upgrading:
nodejs                              x86_64                    1:14.17.2-2.module_f35+12348+fe4be0bd                              fedora-modular                      93 k
nodejs-docs                         noarch                    1:14.17.2-2.module_f35+12348+fe4be0bd                              fedora-modular                     6.0 M
nodejs-full-i18n                    x86_64                    1:14.17.2-2.module_f35+12348+fe4be0bd                              fedora-modular                     7.8 M
nodejs-libs                         x86_64                    1:14.17.2-2.module_f35+12348+fe4be0bd                              fedora-modular                      13 M
Downgrading:
npm                                 x86_64                    1:6.14.13-1.14.17.2.2.module_f35+12348+fe4be0bd                    fedora-modular                     3.3 M
Installing module profiles:
nodejs/common
Skipping packages with broken dependencies:
nodejs                              x86_64                    1:14.19.0-2.module_f35+13766+ad18d3e5                              updates-modular                    199 k
npm                                 x86_64                    1:6.14.16-1.14.19.0.2.module_f35+13766+ad18d3e5                    updates-modular                    3.3 M

Transaction Summary
===========================================================================================================================================================================
Upgrade    4 Packages
Downgrade  1 Package
Skip       2 Packages

Total download size: 30 M
Is this ok [y/N]:
```
::::

In this situation we enabled and installed the &#96;nodejs:12&#96;
module stream on Fedora 35. Then we reset the &#96;12&#96; stream and
enabled the &#96;14&#96; stream. After that we wanted to install the
&#96;nodejs:14&#96; module stream.

First DNF is trying to upgrade or downgrade the existing installed
software. It will not remove the existing software during the execution
of the &#96;reset&#96; argument. The &#96;reset&#96; only disables the
enabled stream of a module. The NEVRAs of the RPM files in the module
stream can have different versions from the installed software (newer or
older) and also from other streams from the same module. The runtime
dependencies can be different between RPM packages from different module
streams.

This conflict is correct and is not a bug. As you are trying to update
installed RPM packages from the &#96;12&#96; stream with RPM packages
from the &#96;14&#96; stream. Module streams from the same module are
mutually exclusive and only one stream at a time should be enabled and
installed.

If you are switching streams and not sure about the manual process,
please use the &#96;switch-to&#96; argument as this is the recommended
way.

### Installing a RPM package from a wrong module stream. {#_installing_a_rpm_package_from_a_wrong_module_stream}

:::: formalpara
::: title
of a RPM package requested to be installed from the wrong module stream
:::

``` console
[root@bdaeaab947e6 /]\&#35; dnf module enable perl:5.30
Fedora 35 - x86_64                                                                                                                         6.8 MB/s |  79 MB     00:11
Fedora 35 openh264 (From Cisco) - x86_64                                                                                                   3.1 kB/s | 2.5 kB     00:00
Fedora Modular 35 - x86_64                                                                                                                 2.8 MB/s | 3.3 MB     00:01
Fedora 35 - x86_64 - Updates                                                                                                               7.3 MB/s |  27 MB     00:03
Fedora Modular 35 - x86_64 - Updates                                                                                                       2.3 MB/s | 2.8 MB     00:01
Dependencies resolved.
===========================================================================================================================================================================
Package                                  Architecture                            Version                                   Repository                                Size
===========================================================================================================================================================================
Enabling module streams:
perl                                                                             5.30

Transaction Summary
===========================================================================================================================================================================

Is this ok [y/N]: y
Complete!
[root@bdaeaab947e6 /]\&#35; dnf install perl-Tie-RefHash
Last metadata expiration check: 0:00:22 ago on Thu Mar  3 09:41:23 2022.
Error:
Problem: package perl-Tie-RefHash-1.40-478.fc35.noarch requires perl(:MODULE_COMPAT_5.34.0), but none of the providers can be installed
- conflicting requests
- package perl-libs-4:5.34.0-481.fc35.i686 is filtered out by modular filtering
- package perl-libs-4:5.34.0-481.fc35.x86_64 is filtered out by modular filtering
- package perl-libs-4:5.34.0-482.fc35.i686 is filtered out by modular filtering
- package perl-libs-4:5.34.0-482.fc35.x86_64 is filtered out by modular filtering
(try to add '--skip-broken' to skip uninstallable packages)
[root@bdaeaab947e6 /]\&#35;
```
::::

The example describes a situation when you try to install a RPM package
which is not provided from the enabled &#96;perl:5.30&#96; module
stream. We first enable the &#96;perl:5.30&#96; module stream. After
that we are trying to install the package &#96;perl-Tie-RefHash&#96;.
The DNF package manager is trying to tell you that the
&#96;perl-Tie-RefHash&#96; cannot be installed because it is not
provided by any of the enabled module streams. Modular filtering will
automatically filter out all the RPM packages which are not provided by
the actual enabled module streams.

To fix this conflict you have to enable the correct module stream. In
our case it is the &#96;perl:5.32&#96; module stream.

### Installing a RPM package without enabling the module stream which provides it. {#_installing_a_rpm_package_without_enabling_the_module_stream_which_provides_it}

:::: formalpara
::: title
of a installation conflict when installing a package without enabling
the correct module stream
:::

``` console
[root@bdaeaab947e6 /]\&#35; dnf install perl-DBI
Last metadata expiration check: 3:13:30 ago on Thu Mar  3 09:41:23 2022.
Error:
Problem: package perl-DBI-1.643-10.fc35.x86_64 requires libperl.so.5.34()(64bit), but none of the providers can be installed
- conflicting requests
- package perl-libs-4:5.34.0-481.fc35.x86_64 is filtered out by modular filtering
- package perl-libs-4:5.34.0-482.fc35.x86_64 is filtered out by modular filtering
(try to add '--skip-broken' to skip uninstallable packages)
[root@bdaeaab947e6 /]\&#35; dnf module enable perl-DBI
Last metadata expiration check: 3:14:38 ago on Thu Mar  3 09:41:23 2022.
Dependencies resolved.
===========================================================================================================================================================================
Package                                  Architecture                            Version                                   Repository                                Size
===========================================================================================================================================================================
Enabling module streams:
perl-DBI                                                                         1.643

Transaction Summary
===========================================================================================================================================================================

Is this ok [y/N]: y
Complete!
[root@bdaeaab947e6 /]\&#35; dnf install perl-DBI
Last metadata expiration check: 3:14:46 ago on Thu Mar  3 09:41:23 2022.
Dependencies resolved.
===========================================================================================================================================================================
Package                          Architecture                   Version                                                      Repository                              Size
===========================================================================================================================================================================
Installing:
perl-DBI                         x86_64                         1.643-7.module_f35+12493+425c54a8                            fedora-modular                         700 k

Transaction Summary
===========================================================================================================================================================================
Install  1 Package

Total download size: 700 k
Installed size: 1.9 M
Is this ok [y/N]:
```
::::

In this example we are trying to install the &#96;perl-DBI&#96; package.
On our system we have previously enabled and installed the
&#96;perl:5.32&#96; module stream. The conflict tells us that we are
trying to install non-modular &#96;perl-DBI&#96; which depends on the
non-modular &#96;perl&#96; but the non-modular &#96;perl&#96; package is
not available due to modular filtering. The only RPM packages which are
available for dependency resolution are the RPM packages from the
&#96;5.32&#96; stream.

:::: warning
::: title
:::

Non-modular RPM packages can not depend on modular content. If your
non-modular package needs a modular dependency please modularize your
content.
::::

To fix this we need to enable the &#96;perl-DBI:1.643&#96; module
stream. When enabling the &#96;perl-DBI:1.643&#96; we are satisfying the
modular dependency for the &#96;perl&#96; module. The non-modular
&#96;perl-DBI&#96; RPM package is now filtered by modular filtering and
it is not considered in dependency resolution and content set creation.

# Building Modules {#_building_modules}

:::: warning
::: title
:::

&#42;&#42;The Modularity project has been retired&#42;&#42; and there
are [no modules in Fedora 39 or
newer](https://fedoraproject.org/wiki/Changes/RetireModularity) or [in
EPEL](https://lists.fedoraproject.org/archives/list/epel-announce@lists.fedoraproject.org/thread/KA3JQUZW63A4V7OQ7ZVDFCM32EQUSOXH/).
This page is only retained for historical reference.
::::

1.  &#42;&#42;[Fedora](:building-modules/fedora/index.xml)&#42;&#42;

2.  &#42;&#42;[COPR](:building-modules/copr/building-modules-in-copr.xml)&#42;&#42;

3.  &#42;&#42;[Localhost](:building-modules/local/building-modules-locally.xml)&#42;&#42;

# Building Modules for Fedora {#_building_modules_for_fedora}

:::: warning
::: title
:::

&#42;&#42;The Modularity project has been retired&#42;&#42; and there
are [no modules in Fedora 39 or
newer](https://fedoraproject.org/wiki/Changes/RetireModularity) or [in
EPEL](https://lists.fedoraproject.org/archives/list/epel-announce@lists.fedoraproject.org/thread/KA3JQUZW63A4V7OQ7ZVDFCM32EQUSOXH/).
This page is only retained for historical reference.
::::

If you wish to maintain an additional version of an application,
language stack, or any other piece of software, modules might be the way
to go for you.

The [Adding New Modules](building-modules/fedora/adding-new-modules.xml)
covers the whole process of adding a new module to Fedora.

The [Module Obsoletes](building-modules/fedora/module-obsoletes.xml)
covers the process of a module stream EOLing/obsoleting.

# Adding new modules to Fedora {#_adding_new_modules_to_fedora}

:::: warning
::: title
:::

&#42;&#42;The Modularity project has been retired&#42;&#42; and there
are [no modules in Fedora 39 or
newer](https://fedoraproject.org/wiki/Changes/RetireModularity) or [in
EPEL](https://lists.fedoraproject.org/archives/list/epel-announce@lists.fedoraproject.org/thread/KA3JQUZW63A4V7OQ7ZVDFCM32EQUSOXH/).
This page is only retained for historical reference.
::::

This page will guide you through the whole process of adding a new
module to Fedora:

1.  &#42;&#42;&lt;&lt;RPM Sources&gt;&gt;&#42;&#42; --- To
    &#96;dist-git/rpms&#96; using stream branches.

2.  &#42;&#42;&lt;&lt;Module Definition&gt;&gt;&#42;&#42; --- To
    &#96;dist-git/modules&#96; using stream branches.

3.  &#42;&#42;&lt;&lt;Module Build&gt;&gt;&#42;&#42; --- Module is built
    as a unit. No individual package builds are done.

4.  &#42;&#42;&lt;&lt;Publishing the Module&gt;&gt;&#42;&#42; ---
    Submitting a Bodhi update.

## RPM Sources {#_rpm_sources}

For each package in your module, you need to have a Fedora Distribution
Git (dist-git) &#42;&#42;repository&#42;&#42; under
&#96;dist-git/rpms&#96; with an appropriate &#42;&#42;stream
branch&#42;&#42;. New packages need to go through a &#42;&#42;package
review&#42;&#42;.

### Repositories and Stream Branches --- New packages {#_repositories_and_stream_branches_new_packages}

The [Fedora Package Review
Process](https://docs.fedoraproject.org/en-US/package-maintainers/Package_Review_Process/&#35;_contributor)
covers all the steps you need to take, except for stream branches. For
that, please continue below to Existing packages.

### Repositories and Stream Branches --- Existing packages {#_repositories_and_stream_branches_existing_packages}

Requesting new stream branches for existing packages is done with
&#96;fedpkg&#96;, and it doesn't require a package review.

To create a new branch for a package that shares a name with the module
(e.g. \'postgresql\'), run the following command which will create the
package stream branch as well as the module and its stream branch
together:

    $ fedpkg request-branch --repo=NAME BRANCH --sl SERVICE_LEVEL:YYYY-MM-DD

&#42; &#96;NAME&#96; --- name of the package and the module &#42;
&#96;BRANCH&#96; --- name of the stream branch of the package and the
module &#42; &#96;SERVICE_LEVEL:YYYY-MM-DD&#96;[]{#SLA} --- expected end
of life (e.g. &#96;bug_fixes:2020-12-01&#96;). The date must end with
either &#96;12-01&#96; or &#96;06-01&#96;. There are various service
levels like &#96;bug_fixes&#96;, &#96;security_fixes&#96;, and
&#96;rawhide&#96;. Right now, this is used for locking the branch from
pushing new commits there. You can change the date later with a [releng
ticket](https://pagure.io/releng/new_issue?template=module_eol). Current
dates are stored in [Product Definition
Center](https://pdc.fedoraproject.org/rest_api/v1/component-branch-slas/?branch_type=rpm).
Other option is to choose a date far in the future so you're not
affected. ([Work to fix this is in
progress](https://tree.taiga.io/project/modularity-wg/epic/3).)

If this package does not share a name with the module (such as for
dependencies), then only request the stream branch for this package:

    $ fedpkg request-branch --repo=NAME BRANCH --no-auto-module --sl SERVICE_LEVEL:YYYY-MM-DD

&#42; &#96;\--no-auto-module&#96; --- Skip the creation of a module of
the same name

Creation of the module and its stream branches separately will be
covered later.

### Importing the RPM sources into dist-git {#_importing_the_rpm_sources_into_dist_git}

The last thing to do is to import the RPM sources into dist-git. Please
refer to the [New package process for existing contributors
](https://docs.fedoraproject.org/en-US/package-maintainers/New_Package_Process_for_Existing_Contributors/)
for the complete steps.

## Module Definition {#_module_definition}

For your module definition, you also need to have a dist-git
&#42;&#42;repository&#42;&#42;, this time under
&#96;dist-git/modules&#96;, with an appropriate &#42;&#42;stream
branch&#42;&#42;. New modules also need to go through a [module review
in
Bugzilla](https://bugzilla.redhat.com/buglist.cgi?component=Module%20Review&amp;product=Fedora%20Modules)
adhering to [Fedora Packagining Guidelines for
Modules](policies/packaging-guidelines.xml).

### Repositories and Stream Branches --- New modules {#_repositories_and_stream_branches_new_modules}

To request a new module repository in dist-git run:

    $ fedpkg request-repo --namespace modules NAME BUG
    $ fedpkg request-branch --namespace modules --repo NAME BRANCH --sl SERVICE_LEVEL:YYYY-MM-DD

&#42; &#96;NAME&#96; --- name of the module &#42; &#96;BUG&#96; --- bug
number with an approved [module review in
Bugzilla](https://bugzilla.redhat.com/buglist.cgi?component=Module%20Review&amp;product=Fedora%20Modules)
&#42; &#96;BRANCH&#96; --- name of the stream branch of the module &#42;
&#96;SERVICE_LEVEL:YYYY-MM-DD&#96; --- expected end of life. See
&lt;&lt;SLA,above&gt;&gt; for more details. Stream end of lives are
available in [Product Definition
Center](https://pdc.fedoraproject.org/rest_api/v1/component-branch-slas/?branch_type=module).

### Repositories and Stream Branches --- Existing modules {#_repositories_and_stream_branches_existing_modules}

to request a new stream branch, run:

    $ fedpkg request-branch --namespace modules --repo NAME BRANCH --sl SERVICE_LEVEL:YYYY-MM-DD

&#42; &#96;NAME&#96; --- name of the module &#42; &#96;BRANCH&#96; ---
name of the stream branch of the module &#42;
&#96;SERVICE_LEVEL:YYYY-MM-DD&#96; --- expected end of life. See
&lt;&lt;SLA,above&gt;&gt; for more details.

### Write and push the modulemd {#_write_and_push_the_modulemd}

Writing a modulemd is covered in detail in the [Defining Modules in
modulemd](building-modules/fedora/defining-modules.xml) section.

:::: note
::: title
:::

The name of the modulemd must match the name of the repository. Remember
to replace every &#96;NAME&#96; in the following example.
::::

    $ fedpkg clone modules/NAME
    $ cd NAME
    $ fedpkg switch-branch BRANCH
    $ vim NAME.yaml
    $ git add NAME.yaml
    $ git commit -m 'add the initial modulemd'
    $ git push

&#42; &#96;NAME&#96; --- name of the module &#42; &#96;BRANCH&#96; ---
name of the stream branch of the module

## Module Build {#_module_build_2}

:::: note
::: title
:::

NOTE: With Modularity, you no longer build individual packages. Instead,
you need to submit a module build.
::::

Submitting module builds is done using &#96;fedpkg&#96; and is covered
in the [Building modules](building-modules/fedora/building-modules.xml)
section.

## Publishing the Module {#_publishing_the_module}

## Module Stream EOLing/Obsoleting {#_module_stream_eolingobsoleting}

When a stream should not be used any longer, a user can be instructed to
migrate by adding a [Module
obsoletes](building-modules/fedora/module-obsoletes.xml) document.

# Updating modules in Fedora {#_updating_modules_in_fedora}

:::: warning
::: title
:::

&#42;&#42;The Modularity project has been retired&#42;&#42; and there
are [no modules in Fedora 39 or
newer](https://fedoraproject.org/wiki/Changes/RetireModularity) or [in
EPEL](https://lists.fedoraproject.org/archives/list/epel-announce@lists.fedoraproject.org/thread/KA3JQUZW63A4V7OQ7ZVDFCM32EQUSOXH/).
This page is only retained for historical reference.
::::

This page will guide you through the process of updating an existing
module.

1.  &#42;&#42;&lt;&lt;Updating RPM Packages&gt;&gt;&#42;&#42; ---
    Pushing new sources.

2.  &#42;&#42;&lt;&lt;Updating the Module&gt;&gt;&#42;&#42; --- Pushing
    a new version of the modulemd.

3.  &#42;&#42;&lt;&lt;Module Build&gt;&gt;&#42;&#42; --- Module is built
    as a unit. No individual package builds are done.

4.  &#42;&#42;&lt;&lt;Publishing the Module&gt;&gt;&#42;&#42; ---
    Submitting a Bodhi update.

## Updating RPM Packages {#_updating_rpm_packages}

Update your RPM packages the same way you would do traditionally, except
submitting individual package builds.

Useful resources:

&#42; [Fedora Packaging
Guidelines](https://docs.fedoraproject.org/en-US/packaging-guidelines/)
&#42; [Fedora Package Maintenance
Guide](https://docs.fedoraproject.org/en-US/package-maintainers/Package_Maintenance_Guide/)

## Updating the Module {#_updating_the_module}

Here are the common changes you might want to apply to your modules.

### Migrating from modulemd to modulemd-packager format {#_migrating_from_modulemd_to_modulemd_packager_format}

In the past there was [modulemd, version
2,](https://raw.githubusercontent.com/fedora-modularity/libmodulemd/main/yaml_specs/modulemd_stream_v2.yaml)
format used for building modules. That format featured stream expansion
and dynamic contexts. However, these features were proved impossible to
be handled correctly by DNF and thus a new format, [modulemd-packager,
version
3,](https://raw.githubusercontent.com/fedora-modularity/libmodulemd/main/yaml_specs/modulemd_packager_v3.yaml)
was
[introduced](https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/KG7L5WE5IYC5CQMS6XOVTPYBJ57AFMF3/&#35;UWQSMM5JANB7MS6XJBLJRGA7N4KIAEIH)
which features a static context.

Modules built from modulemd-packager format are supported since Fedora
34 and RHEL 9.

Changes in the format include:

&#42; New document type and version:

``` yaml
document: modulemd-packager
version: 3
```

&#42; A &#96;module&#96; middle-field was removed from the
&#96;license&#96; section:

``` yaml
license:
- MIT
```

&#42; A &#96;dependencies&#96; section:

``` yaml
dependencies:
buildrequires:
platform: ['f34', 'f35']
perl: ['5.30', '5.32']
requires:
platform: ['f34', 'f35']
perl: ['5.30', '5.32']
```

was replaced with a &#96;configurations&#96; section:

``` yaml
configurations:
- context: A
platform: f34
buildrequires:
perl: ['5.30']
requires:
perl: ['5.30']
- context: B
platform: f34
buildrequires:
perl: ['5.32']
requires:
perl: ['5.32']
- context: C
platform: f35
buildrequires:
perl: ['5.30']
requires:
perl: ['5.30']
- context: D
platform: f35
buildrequires:
perl: ['5.32']
requires:
perl: ['5.32']
```

The []{#context} value is a string and its alphabet and length is
limited. All the contexts must be unique inside a module stream.

When migrating your modules, you will have to come up with the context
value. To preserve a compatibility with the old builds and to preserve
the upgrade path, I strongly recommend reusing the old context values.
Use Koji <https://admin.fedoraproject.org/pkgdb/package/MODULE/>, or MBS
<https://mbs.fedoraproject.org/module-build-service/2/module-builds/?name=MODULE&amp;stream=STREAM&amp;state=5>,
or &#96;dnf module info MODULE:STREAM&#96; command (substitute
&#96;MODULE&#96; and &#96;STREAM&#96; with identifiers of your module)
to locate the lastest version of the module, and pick a context matching
the desired dependencies as depicted here:

    $ dnf -q module info perl-DBI:1.643
    Name             : perl-DBI
    Stream           : 1.643
    Version          : 3520210722203952
    Context          : e12b6f3a        ------+
    […]                                      |
    Requires         : perl:[5.32]     ----+ |
    platform:[f35]  --+ | |
    | | |
    The new YAML file:                   | | |
    | | |
    data:                                | | |
    configurations:                  | | |
    - context: 'e12b6f3a'   \&lt;----|-|-+
    platform: f35         \&lt;----+ |
    buildrequires:               |
    perl: ['5.32']           |
    requires:                    |
    perl: ['5.32']    \&lt;------+
    buildopts:

The plaform field is a scalar now. However, the stream values of the
&#96;buildrequires&#96; and &#96;requires&#96; dependencies are a list.
Although the specification requires a single value.

A &#96;buildopts&#96; section was moved from &#96;/data&#96; to
&#96;/data/configurations/&#42;/context&#96; section. Therefore it's
specific to a context and should be repeated if needed any time:

``` yaml
configurations:
- context: A
platform: f34
buildrequires:
perl: ['5.30']
requires:
perl: ['5.30']
buildopts:
rpms:
macros: |
%this_is_my_module A
- context: B
platform: f34
buildrequires:
perl: ['5.32']
requires:
perl: ['5.32']
buildopts:
rpms:
macros: |
%this_is_my_module B
```

And that's all.

Modules built from this format can be recognized by &#96;static_context:
true&#96; field in their output YAML document.

For a real example of the migration look at any perl&#42; module. For
instance, this
[commit](https://src.fedoraproject.org/modules/perl-DBI/c/2200d21f0fab5295226d915c24e49063d226e777?branch=1.643).

### Migrating from a dynamic context to a static context {#_migrating_from_a_dynamic_context_to_a_static_context}

If you do not want to migrate to modulemd-packager format now and you
plan to build only for one platform (e.g. only for EPEL 9), but if you
still need a static context for better handling in DNF, you should set
the context statically by adding into &#96;data&#96; section:

``` YAML
static_context: true
context: CTX \&lt;1\&gt;
```

&lt;1&gt; Choose a context value as &lt;&lt;context,decribed&gt;&gt; in
the previous section about migration to a modulemd-packager format.

Static-context modules are supported since Fedora 34 and RHEL 9.

Static-context modules can be recognized by &#96;static_context:
true&#96; field in their output YAML document.

### Updating a module for a new Fedora release {#_updating_a_module_for_a_new_fedora_release}

Modules in modulemd-packager format statically define a context for each
supported Fedora release:

``` yaml
configurations:
- context: CTX1
platform: f32
```

When a new Fedora release is branched and Rawhide becomes the next
Fedora release, modulemd-packager document is required to be updated to
contain a context for the new release. Otherwise, your module won't be
built for the new Rawhide. For instance the above module needs this
update:

``` yaml
configurations:
- context: CTX1
platform: f32
- context: CTX2
platform: f33
```

You can use &#96;modulemd-add-platform&#96; tool from
&#96;modulemd-tools&#96; package to do the change for you:

    $ modulemd-add-platform --old f32 --new f33 foo.yaml
    $ git diff
    diff --git a/foo.yaml b/foo.yaml
    index b21b921..38cabe8 100644
    --- a/foo.yaml
    +++ b/foo.yaml
    @@ -4,3 +4,5 @@ data:
    configurations:
    - context: CTX1
    platform: f32
    +      - context: f33
    +        platform: f33

### Rebuilding a module for updated RPM packages {#_rebuilding_a_module_for_updated_rpm_packages}

Even when you don't need to make any changes to the modulemd, you still
need to push a new commit to build a new version.

    $ fedpkg clone modules/NAME
    $ cd NAME
    $ fedpkg switch-branch BRANCH
    $ git commit --allow-empty -m 'update'
    $ git push

&#42; &#96;NAME&#96; --- name of the module &#42; &#96;BRANCH&#96; ---
name of the stream branch of the module

## Module Build {#_module_build_3}

:::: note
::: title
:::

NOTE: With Modularity, you no longer build individual packages. Instead,
you need to submit a module build.
::::

Submitting module builds is done using &#96;fedpkg&#96; and is covered
in the [Building modules](building-modules/fedora/building-modules.xml)
section.

## Publishing the Module {#_publishing_the_module_2}

# Defining modules in modulemd {#_defining_modules_in_modulemd}

:::: warning
::: title
:::

&#42;&#42;The Modularity project has been retired&#42;&#42; and there
are [no modules in Fedora 39 or
newer](https://fedoraproject.org/wiki/Changes/RetireModularity) or [in
EPEL](https://lists.fedoraproject.org/archives/list/epel-announce@lists.fedoraproject.org/thread/KA3JQUZW63A4V7OQ7ZVDFCM32EQUSOXH/).
This page is only retained for historical reference.
::::

Simply put, &#42;&#42;modulemd is a file that defines which packages get
built for which releases&#42;&#42;. It includes a summary and a
description, a list of source RPM packages, build information i.e. build
order and macros, and usage information i.e. installation profiles and
licenses.

## A typical modulemd example {#_a_typical_modulemd_example}

A typical modulemd file looks similar to the following examples. Read on
for more details about each part of the modulemd file.

Feel free to copy/paste this example when creating your new module.

``` yaml
document: modulemd-packager
version: 3
data:
\&#35; === Information about this module ==================================
\&#35; (Can be copied from the main RPM package, but doesn't need to be)
summary: An example module
description: \&gt;-
A module for the demonstration of the metadata format. Also,
it can span multiple lines.

\&#35; === License of this modulemd file ==================================
license:
- MIT
\&#35; === Module context configurations ===========================================
\&#35; (For which Fedora releases to build?)
configurations:
\&#35; context:
\&#35; A string of up to ten [a-zA-Z0-9] characters representing a
\&#35; a build and runtime configuration for this stream. This string is
\&#35; arbitrary but must be unique in this module stream.
\&#35; Type: MANDATORY
- context: CTX1
\&#35; platform:
\&#35; Defines the distribution and release to build on and run against.
\&#35; Type: MANDATORY
platform: f32
\&#35; buildrequires:
\&#35; A dictionary of the build-time dependencies on other module streams.
\&#35; Each configuration may depend on a single stream of a dependency.
\&#35; The dictionary key is the name of the module and the dictionary value
\&#35; is a single-element list containing the name of the stream.
\&#35;
\&#35; Type: Optional
buildrequires:
appframework: [v1]
\&#35; requires:
\&#35; A dictionary of the run-time dependencies on other module streams.
\&#35; Each configuration may depend on a single stream of a dependency.
\&#35; The dictionary key is the name of the module and the dictionary value
\&#35; is a single-element list containing the name of the stream.
\&#35;
\&#35; Type: Optional
requires:
appframework: [v1]
\&#35; buildopts:
\&#35; Component build options
\&#35; Additional per component type module-wide build options.
\&#35;
\&#35; IMPORTANT: Due to limitations in the modulemd-stream v2 format, the
\&#35; buildopts from the first configuration in the list will apply to
\&#35; ALL configurations when building for modulemd-stream v2. They will
\&#35; apply separately when building for module-stream v3.
\&#35;
\&#35; Type: OPTIONAL
buildopts:
\&#35; rpms:
\&#35; RPM-specific build options
\&#35;
\&#35; Type: OPTIONAL
rpms:
\&#35; macros:
\&#35; Additional macros that should be defined in the
\&#35; RPM buildroot, appended to the default set.  Care should be
\&#35; taken so that the newlines are preserved.  Literal style
\&#35; block is recommended, with or without the trailing newline.
\&#35;
\&#35; Type: OPTIONAL
macros: |
%demomacro 1
%demomacro2 %{demomacro}23

\&#35; whitelist:
\&#35; Explicit list of package build names this module will produce.
\&#35; By default the build system only allows components listed under
\&#35; data.components.rpms to be built as part of this module.
\&#35; In case the expected RPM build names do not match the component
\&#35; names, the list can be defined here.
\&#35; This list overrides rather then just extends the default.
\&#35; List of package build names without versions.
\&#35;
\&#35; Type: OPTIONAL
whitelist:
- fooscl-1-bar
- fooscl-1-baz
- xxx
- xyz
\&#35; arches:
\&#35; Instructs the build system to only build the
\&#35; module on this specific set of architectures.
\&#35; Includes specific hardware architectures, not families.
\&#35; See the data.arch field in the modulemd-stream spec for details.
\&#35; Defaults to all available arches.
\&#35;
\&#35; Type: OPTIONAL
arches: [i686, x86_64]

\&#35; Alternate example with no dependencies
- context: CTX2
platform: f33
\&#35; === Module API (optional, but encouraged) ==========================
\&#35; (Which packages are API-stable?)
api:
rpms:
- package-one        \&#35; \&lt;- Binary RPM package name
- package-one-extras \&#35; \&lt;- Binary RPM package name
- package-one-cli    \&#35; \&lt;- Binary RPM package name
- package-one-devel  \&#35; \&lt;- Binary RPM package name
- package-two        \&#35; \&lt;- Binary RPM package name

\&#35; === Package filtering ==============================================
\&#35; (Which packages should not be included into the resulting module)
filter:
rpms:
- subpackage-one     \&#35; \&lt;- Binary RPM package name

\&#35; === Installation profiles (optional, but encouraged) ===============
\&#35; (Helping users with installation by providing predefined groups)
profiles:
default:  \&#35; \&lt;- Name of the profile
description: A standard installation.
rpms:
- package-one         \&#35; \&lt;- Binary RPM package name
- package-one-extras  \&#35; \&lt;- Binary RPM package name
- package-two         \&#35; \&lt;- Binary RPM package name
cli:      \&#35; \&lt;- Name of the profile
description: A command-line client.
rpms:
- package-one-cli     \&#35; \&lt;- Binary RPM package name

\&#35; === Packages in this module ========================================
\&#35; (Referenced by their dist-git repo name + branch name)
components:
rpms:
first-package:  \&#35; \&lt;- Source RPM package name
ref: 3.0    \&#35; \&lt;- Branch name in dist-git
rationale: Provides the core functionality.
second-package: \&#35; \&lt;- Source RPM package name
ref: latest \&#35; \&lt;- Branch name in dist-git
rationale: Web UI for the first-package.
```

## Common modulemd definitions {#_common_modulemd_definitions}

These are the common parts of a modulemd file, used in the example
above. Advanced definitions, including a complex example of Module
Stream Expansion (MSE), are towards the end of this page.

### Document header {#_document_header}

Every modulemd starts with these three lines:

``` yaml
document: modulemd-packager
version: 3
data:
\&#8230; \&lt;1\&gt;
```

&lt;1&gt; All the following definitions go here, under *data*.

### Information about this module {#_information_about_this_module}

Tell users what this module represents by writing a summary and a
description.

``` yaml
summary: An example module
description: \&gt;-  \&lt;1\&gt;
A module for the demonstration of the metadata format. Also,
it can span multiple lines.
```

&lt;1&gt; The &#96;&gt;-&#96; means new line in YAML. Useful for longer
blocks of text, such as the description!

### License of this modulemd file {#_license_of_this_modulemd_file}

This is a license of this very modulemd file and it doesn't need to be
modified. The build system adds licenses of all packages to this list
automatically.

``` yaml
license:
- MIT  \&lt;1\&gt;
```

&lt;1&gt; A license for this modulemd file. Fedora content, such as SPEC
files or patches not included upstream, uses the MIT license by default,
unless the component packager declares otherwise.

### []{#context}Module context configurations {#_module_context_configurations}

Each context configuration describes how a module stream and its
components should be build and run. A single-context example:

``` yaml
configurations:
- context: CTX1   \&lt;1\&gt;
platform: f32   \&lt;2\&gt;
buildrequires:
appframework: [v1]    \&lt;3\&gt;
requires:
appframework: [v1]    \&lt;4\&gt;
```

&lt;1&gt; A context name for the single configuration. &lt;2&gt; An
identifier of a major release of a distribution this context will be
built and it will run on. &lt;3&gt; Module streams to enable when
building this context (build-time modular dependencies). &lt;4&gt;
Module streams to enable when installing this context (run-time modular
dependencies).

The &#96;context&#96; field is mandatory and must be unique inside a
single stream. The value is an arbitrary string with a limited length
and alphabet. The context value is used by DNF for establishing an
upgrade path among multiple module versions and contexts. Thus once the
value is set, it should not change.

The platform identifier is mandatory and it matches a Fedora release.
E.g. &#96;f32&#96; means Fedora 32. Rawhide also uses a numerical value.
Technically, it's [a stream of &#96;platform&#96;
module](https://mbs.fedoraproject.org/module-build-service/2/module-builds/?state=5&amp;name=platform).

[Modular dependencies at run
time](core-concepts/module-dependency-resolution.xml) can differ from
those [at build
time](https://pagure.io/fm-orchestrator/blob/master/f/docs/DEPENDENCY_RESOLUTION.rst).
There can be multiple modules listed, but always exactly one stream.
E.g. &#96;appframework: \[v1\]&#96; means &#96;appframework:v1&#96;
module stream.

Here is a complex example with multiple contexts:

``` yaml
configurations:
- context: CTX1
platform: f32
buildrequires:
appframework: [v1]
requires:
appframework: [v1]
frameworkext: [v3]
- context: CTX2
platform: f33
buildrequires:
appframework: [v1]
requires:
appframework: [v1]
frameworkext: [v3]
- context: CTX3
platform: f33
buildrequires:
appframework: [v2]
requires:
appframework: [v2]
```

This example will produce one module build for Fedora 32 and two builds
for Fedora 33. The Fedora 32 module will depend on
&#96;appframework:v1&#96; and &#96;frameworkext:v3&#96;, while Fedora 33
module will support both &#96;appframework:v1&#96; and
&#96;appframework:v2&#96; streams. The context &#96;CTX3&#96; does not
depenend on &#96;frameworkext:v3&#96; because it was merged into
&#96;appframework:v2&#96;.

### Installation profiles (optional, but encouraged) {#_installation_profiles_optional_but_encouraged}

To help users install your module, define installation profiles. These
profiles represent a specific use case of your module. Most modules have
at least a default profile. But you can specify more. For example, a
database module can have a server and a client profile.

``` yaml
profiles:
default:  \&lt;1\&gt;
description: A standard installation.  \&lt;2\&gt;
rpms:
- package-one         \&lt;3\&gt;
- package-one-extras  \&lt;3\&gt;
- package-two         \&lt;3\&gt;
cli:
description: A command-line client.
rpms:
- package-one-cli
\&#8230;  \&lt;4\&gt;
```

&lt;1&gt; Name of the profile. &lt;2&gt; A quick summary of the profile.
&lt;3&gt; Binary packages to be installed with this profile. &lt;4&gt;
List as many profiles as you need.

### Module API (optional, but encouraged) {#_module_api_optional_but_encouraged}

List all binary RPM packages in your module that you consider to be the
main stable feature of the module. Other (unlisted) packages should be
considered unsupported, or an implementation detail.

``` yaml
api:
rpms:
- package-one
- package-one-extras
- package-one-cli
- package-one-devel
- package-two
```

### Packages in this module {#_packages_in_this_module}

List all source SRPM packages this module should include, referenced
them by their dist-git repo name + branch name.

``` yaml
components:
rpms:
first-package:  \&lt;1\&gt;
rationale: Provides the core functionality.  \&lt;2\&gt;
ref: 3.0  \&lt;3\&gt;
second-package:
rationale: Web UI for the first-package.
ref: latest
\&#8230;  \&lt;4\&gt;
```

&lt;1&gt; Name of the package --- maps to a DistGit repository name.
&lt;2&gt; The reason why is this package here. Mostly for humans.
&lt;3&gt; DistGit branch, tag, or a commit --- so the right version of
the package gets included. &lt;4&gt; List as many packages as you need.

## Advanced definitions {#_advanced_definitions}

### References to the upstream (optional) {#_references_to_the_upstream_optional}

You can also provide references to the upstream community,
documentation, or to an issue tracker.

``` yaml
references:
community: http://www.example.com/  \&lt;1\&gt;
documentation: http://www.example.com/  \&lt;2\&gt;
tracker: http://www.example.com/  \&lt;3\&gt;
```

&lt;1&gt; Upstream community website, if it exists. &lt;2&gt; Upstream
documentation, if it exists. &lt;3&gt; Upstream bug tracker, if it
exists.

### Building in a specific order (optional) {#_building_in_a_specific_order_optional}

Packages are built in batches. By default, all packages are part of a
single group, and therefore built concurrently.

To build packages in a specific order, assign them to multiple build
groups. Build groups are identified by an integer. Groups with lower
number are built first. Negative values are allowed, &#96;0&#96; is the
implicit default value.

In this specific example, &#96;first-package&#96; gets built first, and
&#96;second-package&#96; gets built second.

``` yaml
components:
rpms:
first-package:
rationale: Provides the core functionality.
ref: 3.0
buildorder: 0  \&lt;1\&gt;
second-package:
rationale: Web UI for the first-package.
ref: latest
buildorder: 10  \&lt;1\&gt;
```

&lt;1&gt; A number of the build group.

For even more complex scenarios, please study the [modulemd-packager
specification](https://github.com/fedora-modularity/libmodulemd/blob/main/yaml_specs/modulemd_packager_v3.yaml).

### RPM macros (optional) {#_rpm_macros_optional}

RPM packages while being built as part of a module have the following
RPM macros available:

    %dist .scrmod+f37+14301+76d220e4    \&lt;.\&gt;
    %modularitylabel perl-Module-Install:master:3720220414092112:dd3c6e0e \&lt;.\&gt;
    %_module_build 1    \&lt;.\&gt;
    %_module_name perl-Module-Install   \&lt;.\&gt;
    %_module_stream master  \&lt;.\&gt;
    %_module_version 3720220414092112   \&lt;.\&gt;
    %_module_context dd3c6e0e   \&lt;.\&gt;

&lt;.&gt; A &#96;%dist&#96; macro of a unique value used in
&#96;Release&#96; RPM specification tags. &lt;.&gt; An RPM tag stored
into binary RPM packages. DNF uses it to distinguish modular packages
from nonmodular ones. &lt;.&gt; A macro denoting that a modular package
is being built. &lt;.&gt; A name of the module being built. &lt;.&gt; A
stream of the module being built. &lt;.&gt; A version of the module
being built. &lt;.&gt; A context of the module being built.

You can use these macros in RPM specification files of your RPM
components to modify building of the packages.

If you need additional RPM macros, you can define them in a
&#96;buildopts&#96; section of your modulemd file:

``` yaml
buildopts:
rpms:
macros: |
%perl_bootstrap 1
```

This section belongs into an item of &#96;configurations&#96; list in
case of v3 modulemd format. In case of v2 format it belongs directly
into &#96;data&#96; section.

### Filtered Packages (optional, defaults to no filters) {#_filtered_packages_optional_defaults_to_no_filters}

The build process of a RPM packages can result in a subpackages which
complement the build of the package (docs, additional build requires
etc.). One source RPM package might produce multiple binary RPM
packages. Those subpackages are not always desired to be shipped with
the Module. Modules enable you to filter out those undesirable packages
with the &#96;filter&#96; build option. After the build is finished the
filtered packages will be not included in the &#96;artifacts&#96;
property in the result modulemd yaml file. The &#96;artifacts&#96;
property is added by the build system post build. For an example please
refer to the [modulemd spec
files](https://github.com/fedora-modularity/libmodulemd/tree/main/yaml_specs).

Filtered RPMs are still available to use as build dependencies in
subsequent stages of the module build, but are not included in the
composed repository for users.

``` yaml
filter:
rpms:
- first-package-debuginfo
- second-package-nope
```

### []{#demodularized}Demodularized packages (optional, defaults to none) {#_demodularized_packages_optional_defaults_to_none}

If you decide to remove a binary package from your module stream, you
will probably stop building it, or you will filter it out with a
&#96;filter&#96; option. But that's not enough if you want to move the
package back to nonmodular packages: Because the package remains listed
among artifacts in the previous version of the stream and a package
manager could see both the updated and the historical version. (The
previous version can be available in GA and updates repositories, while
your updated module will first appear in an updates-testing repository.)

To return the package back to nonmodular package set, you need to write
it on a list of demodularized packages. A package manager checks the
demodularized list of the very latest version of the module stream over
all repositories and if it only sees a package name there, it will stop
hiding the same-named nonmodular packages while the stream is enabled.

The list of demodularized packages is defined in &#96;demodularized&#96;
field:

``` yaml
demodularized:
rpms:
- first-removed-package
- second-removed-package
```

With this explicit mechanism, called demodularization, a package can be
demoted from a module. If you ever revert your decision and make the
package modular again, the only thing necessary is remove it from the
demodularized list.

### Creating build-only components (optional) {#_creating_build_only_components_optional}

In addition to filtering subpackages, it's possible to filter out all of
the artifacts produced by a component in a module. This is useful in
cases where your module's primary packages have a build-time dependency
that you do not want to ship. An example of such a case would be if you
need to build with a specially-patched documentation-generator that
would conflict with the version used as the default in Fedora.

``` yaml
components:
rpms:
customdocgen:
rationale: A patched version of docgen that enables an experimental feature.
ref: experimental
buildorder: 0
buildonly: 1
myapp:
rationale: My application
ref: latest
buildorder: 10
```

In this example, &#96;customdocgen&#96; would be built first and made
available in the buildroot for &#96;myapp&#96; to use during its build.
Once the module build is finished and it is composed into a DNF
repository, only the unfiltered artifacts from &#96;myapp&#96; will be
available. All of the &#96;customdocgen&#96; artifacts will be
automatically added to the &#96;data.filters.rpms&#96; section of the
module metadata.

## A minimal modulemd {#_a_minimal_modulemd}

### An absolute minimum {#_an_absolute_minimum}

This module includes two source RPM packages built for the Fedora 35
releases.

``` yaml
document: modulemd-packager
version: 3
data:
summary: An example module
description: \&gt;-
A module for the demonstration of the metadata format.
license:
- MIT
configurations:
- context: CTX1
platform: f35
components:
rpms:
first-package:
rationale: Provides the core functionality.
ref: 3.0
second-package:
rationale: Web UI for the first-package.
ref: latest
```

### Including profiles and API (recommended) {#_including_profiles_and_api_recommended}

This module includes two source RPM packages built for the Fedora 35
releas. It makes clear which packages are considered the API, and helps
users with installation thanks to the profiles.

``` yaml
document: modulemd-packager
version: 3
data:
summary: An example module
description: \&gt;-
A module for the demonstration of the metadata format.
license:
- MIT
configurations:
- context: CTX1
platform: f35
api:
rpms:
- package-one
- package-one-extras
- package-one-cli
- package-one-devel
- package-two
profiles:
default:
description: A standard installation.
rpms:
- package-one
- package-one-extras
- package-two
cli:
description: A command-line client.
rpms:
- package-one-cli
components:
rpms:
first-package:
rationale: Provides the core functionality.
ref: 3.0
second-package:
rationale: Web UI for the first-package.
ref: latest
```

# Submitting module builds in Fedora {#_submitting_module_builds_in_fedora}

:::: warning
::: title
:::

&#42;&#42;The Modularity project has been retired&#42;&#42; and there
are [no modules in Fedora 39 or
newer](https://fedoraproject.org/wiki/Changes/RetireModularity) or [in
EPEL](https://lists.fedoraproject.org/archives/list/epel-announce@lists.fedoraproject.org/thread/KA3JQUZW63A4V7OQ7ZVDFCM32EQUSOXH/).
This page is only retained for historical reference.
::::

:::: note
::: title
:::

With Modularity, you no longer build individual packages. Instead, you
need to submit a module build.
::::

Module builds are triggered using &#96;fedpkg&#96; from within your
dist-git repository.

    $ fedpkg clone modules/NAME
    $ cd NAME
    $ fedpkg switch-branch BRANCH
    $ fedpkg module-build

&#42; &#96;NAME&#96; --- name of the module &#42; &#96;BRANCH&#96; ---
name of the stream branch of the module

:::: note
::: title
:::

Please note the module build ID. You will need it to verify the build
state and to publish the module later.
::::

## Submitting module builds from a system without a web browser {#_submitting_module_builds_from_a_system_without_a_web_browser}

&#96;fedpkg module-build&#96; requires an authorization to MBS. [Fedora
infrastructure uses OpenID Connect
(OIDC)](https://fedoraproject.org/wiki/Infrastructure/Authentication)
for authorizing to web applications. This authorization needs a web
browser. If you are submitting a build from a system without a browser,
e.g. from a virtual machine or a container, please follow this
procedure:

&#96;fedpkg module-build&#96; prints a message with a URL to your
terminal, like this:

    Please visit https://id.fedoraproject.org/openidc/Authorization?scope=openid+https%3A%2F%2Fid.fedoraproject.org%2Fscope%2Fgroups+https%3A%2F%2Fmbs.fedoraproject.org%2Foidc%2Fsubmit-build\&amp;response_type=code\&amp;client_id=mbs-authorizer\&amp;redirect_uri=http%3A%2F%2Flocalhost%3A12345%2F\&amp;response_mode=query to grant authorization

You must open it in your web browser. After succeeding an authentication
step, your browser will complain with:

    This site can’t be reached localhost refused to connect.
    Search Google for localhost 12345
    ERR_CONNECTION_REFUSED

Your browser at this point have a &#96;localhost&#96; URL in its address
bar, like this:

    http://localhost:12345/?code=7c35ded4-054b-4df0-9151-7ef12c7fb838_xe3JWkvf_sL1UyLOzftHJZ3uIlfOo00N

At this point &#96;fedpkg&#96; waits on port 12345 of your system for an
incoming connection from your web browser. While &#96;fedpkg&#96; waits
for an incoming OIDC answer from your browser, imitate the answer with
&#96;curl&#96; tool in a parallel terminal using the very same URL:

    $ curl 'http://localhost:12345/?code=7c35ded4-054b-4df0-9151-7ef12c7fb838_xe3JWkvf_sL1UyLOzftHJZ3uIlfOo00N'

That will unblock &#96;fedpkg module-build&#96; command and it will
resume with submitting the module build.

## Common failures when submitting a module build {#_common_failures_when_submitting_a_module_build}

If a &#96;fedpkg module-build&#96; command fails immediatelly before
reporting the identifiers of spawned module build tasks, there could be
a mistake in the YAML file. Here is is an explanation of some nonobvious
error messages:

&#42; &#96;&#96;None of the base module (platform or bootstrap) streams
in the buildrequires section could be found&#96;&#96; --- one of the
dependency configurations requires a &#96;&#96;platform&#96;&#96; stream
which does not exist in MBS. That often happens when an old Fedora
release is removed from the build infrastructure. A remedy is removing a
configuration block referring to that platform stream from the YAML
file.

&#42; &#96;&#96;Required platform:f36 and platform:f37&#96;&#96; --- a
build-required module stream does not exist in a context for the same
platform stream as a module you submitted for building. This happens
when you forget to build the dependent module for the new platform. A
remedy is either building the dependent module first, or remove a
configuration for that platform.

## Module build progress {#_module_build_progress}

To watch the state of your module build, run:

    $ fedpkg module-build-watch BUILD_ID

When the module is in a \'ready\' state, the build has successfully
completed.

You can also watch the build(s) on Fedora Module build service:

<https://release-engineering.github.io/mbs-ui/modules>

## Module build results {#_module_build_results}

All the packages built in the module are tagged in Koji tag named as
&#96;&#96;module-\$name-\$stream-\$version-\$context&#96;&#96;. The link
to this tag is also available in Fedora Module build service UI
mentioned earlier.

There are also two Koji Builds representing single module build.

&#42; &#96;&#96;\$name-\$stream-\$version.\$context&#96;&#96; - Contains
the metadata with final RPMs which will be included in a compose and
will be therefore visible by the end user. &#42;
&#96;&#96;\$name-devel-\$stream-\$version.\$context&#96;&#96; - Contains
the metadata with filtered RPMs which are not normally visible to end
user, but might be sometimes useful when building other packages against
the module. Generally, in Fedora we do not ship the -devel modules.

:::: note
::: title
:::

You will not find &#96;&#96;\$name-devel&#96;&#96; module build in
Module Build Service, because this is only another representation of
non-devel module build. It is not separate module build on its own and
it only exists as Koji build.
::::

Both Koji module builds contains various metadata files:

- &#96;&#96;modulemd.src.txt&#96;&#96; - The unchanged input modulemd
  metadata used to build a module as stored in dist-git.

- &#96;&#96;modulemd.txt&#96;&#96; - The expanded modulemd metadata
  which was used by Module Build Service to build this particular
  module. This for example contains the right build requirements based
  on the Module Stream Expansion.

- &#96;&#96;modulemd.\$arch.txt&#96;&#96; - The per-architecture
  modulemd metadata listing the RPMs which will end up in a compose and
  therefore be visible to end user. This for example respects filters or
  multilib modulemd options.

## Rebuild strategies {#_rebuild_strategies}

In case you want to control which packages get rebuilt and which get
reused, you can enforce a specific rebuild strategy while submitting a
build.

There are different rebuild strategies to choose from:

&#42; &#96;&#96;all&#96;&#96; --- All packages in the module get
rebuilt. &#42; &#96;&#96;only-changed&#96;&#96; --- Only packages that
have changed since the last successful build get rebuilt. This is the
&#42;&#42;default&#42;&#42; in Fedora. &#42;
&#96;&#96;changed-and-after&#96;&#96; --- This one leverages [build
groups
(buildorder)](building-modules/fedora/defining-modules.adoc&#35;_building_in_a_specific_order_optional).
Packages that have changed since the last successful build get rebuilt,
and also all packages with a buildorder higher than any of the changed
ones get rebuilt as well.

For more detailed information, please see the [MBS rebuild strategies
documentation](https://pagure.io/fm-orchestrator/blob/master/f/docs/REBUILD_STRATEGIES.rst).

To enforce a specific rebuild strategy, submit the module build with the
following command:

    $ fedpkg module-build --optional rebuild_strategy=STRATEGY

&#42; &#96;STRATEGY&#96; --- name of a specific build strategy (listed
above)

# Managing module defaults in Fedora {#_managing_module_defaults_in_fedora}

:::: warning
::: title
:::

&#42;&#42;The Modularity project has been retired&#42;&#42; and there
are [no modules in Fedora 39 or
newer](https://fedoraproject.org/wiki/Changes/RetireModularity) or [in
EPEL](https://lists.fedoraproject.org/archives/list/epel-announce@lists.fedoraproject.org/thread/KA3JQUZW63A4V7OQ7ZVDFCM32EQUSOXH/).
This page is only retained for historical reference.
::::

:::: note
::: title
:::

Default streams are &#42;NOT&#42; allowed in Fedora right now according
to policy. Please check the [Policy section](policies/index.xml) for
more information.
::::

Setting or changing a default stream or a default installation profile
of a module constitutes a major behavior change as defined in the Fedora
Updates Policy. The following rules apply:

1.  Module stream defaults MUST be only changed in an upcoming Fedora
    release

2.  Changes of stream defaults should be communicated by a Fedora Change
    based on the change's significance and its maintainer's best
    judgement. When in doubt, file a Change.

3.  Changes of the default stream of a module are not permitted within a
    released Fedora without the approval of FESCo.

4.  Introducing a new default stream not replacing any existing default
    stream or a traditional package is not considered a change. That
    means it can be done.

## Setting or changing a default {#_setting_or_changing_a_default}

Submit an issue to the Fedora Engineering Steering Committee in
[pagure.io/fesco](https://pagure.io/fesco/issues). This ticket must
provide the following information:

&#42; The list of SRPM components in the module &#42; Whether the
contents of this module will obsolete and replace non-modular RPMs.
&#42; Which releases of Fedora will this new default apply to.

When requesting a change of default stream, strongly consider
[submitting a Fedora
Change](https://fedoraproject.org/wiki/Changes/Policy&#35;For_developers).
This will help ensure that the change is communicated to the rest of the
Fedora community.

To check the current defaults, have a look at the [fedora module
defaults repository](https://pagure.io/releng/fedora-module-defaults).

Please note that if the module stream masks part of the Traditional RPM
repos (e.g it replaces an existing RPM or it introduces a non-trivial
set of conflicts) it may not be made a default stream without the
express permission of FESCo. Release Engineering will be responsible for
escalating any PR that is questionable on this point to FESCo for a
final decision.

# Module Obsoletes {#_module_obsoletes}

:::: warning
::: title
:::

&#42;&#42;The Modularity project has been retired&#42;&#42; and there
are [no modules in Fedora 39 or
newer](https://fedoraproject.org/wiki/Changes/RetireModularity) or [in
EPEL](https://lists.fedoraproject.org/archives/list/epel-announce@lists.fedoraproject.org/thread/KA3JQUZW63A4V7OQ7ZVDFCM32EQUSOXH/).
This page is only retained for historical reference.
::::

Module obsoletes allow for stream obsoleting another module or a stream
being EOLed.

The feature has been introduced in
[libmodulemd-2.10.0](https://github.com/fedora-modularity/libmodulemd/releases/tag/2.10.0).

\+

\+

## Module Obsoletes in the Pipeline (Quick Start) {#_module_obsoletes_in_the_pipeline_quick_start}

1.  Add obsoletes in the
    [module-defaults](https://pagure.io/releng/fedora-module-defaults)
    repository.

2.  Configure pungi to use the obsoletes and create a modular compose
    using pungi.

3.  The obsoletes metadata will appear in the &#96;modules.yaml&#96;
    file of the resulting repodata.

## Individual Steps {#_individual_steps}

### Prepare module obsoletes metadata {#_prepare_module_obsoletes_metadata}

Follow the [module obsoletes
specification](https://github.com/fedora-modularity/libmodulemd/blob/main/yaml_specs/)
for an up-to-date format. As of the time of writing this article
(January 2022), there's been v1 specification available and supported in
the pipeline.

Examples:

1.  &#42;EOLed stream nodejs:11 as of a specified date/time&#42;

    ``` yaml
    document: modulemd-obsoletes
    version: 1
    data:
    modified: 2018-05-23T14:25Z
    module: nodejs
    stream: '11'
    \&#35; A string representing UTC date in ISO 8601 format: YYYY-MM-DDTHH:MMZ
    \&#35; It is strongly recommended to keep HH:MM to 00:00.
    \&#35; If not specified, the module is EOLed immediately.
    \&#35; OPTIONAL
    eol_date: 2020-03-19T00:00Z
    message: 'Module stream nodejs:11 is no longer supported.'
    ```

2.  &#42;Immediately obsoleted stream nodejs:11 with a new stream
    nodejs:12 available&#42;

    ``` yaml
    document: modulemd-obsoletes
    version: 1
    data:
    modified: 2018-05-23T14:25Z
    module: nodejs
    stream: '11'
    message: 'Module stream nodejs:11 is no longer supported. Please switch to nodejs:12'
    obsoleted_by:
    module: nodejs
    stream: '12'
    ```

Theses are perhaps the most common scanarios, but check the
specification for other workflows:

- Resetting a previously EOLed/obsoleted stream.

- Obsoleting/EOLing a specific module stream context.

### Add the metadata into &#96;fedora-module-defaults.git&#96; repository {#_add_the_metadata_into_96fedora_module_defaults_git96_repository}

1.  Clone the repository and &#42;add the module obsoletes metadata&#42;
    into the &#96;obsoletes/&#96; directory.

    Use &#96;&lt;name&gt;:&lt;stream&gt;.yaml&#96; convention as each
    file can contain only a single module obsoletes document for the
    subsequent processing to be successful.

    :::: important
    ::: title
    :::

    Make sure to commit your changes before going to the next step.
    ::::

2.  Execute &#96;run_tests.sh&#96; in the root of the repository to
    &#42;validate the metadata locally&#42;.

    First, testing metadata are checked to make sure your libmodulemd is
    able to handle module obsoletes. Then the actual metadata in the
    &#96;obsoletes/&#96; directory are validated.

3.  &#42;After a successful validation&#42;, file a [pull
    request](https://pagure.io/releng/fedora-module-defaults/pull-requests)
    for the module obsolete to be included in the repository. Use branch
    *main* for including module obsoletes into Fedora Rawhide. Check
    fedora-module-defaults repository for all the branches.

### Configure pungi for module obsoletes and create a modular compose {#_configure_pungi_for_module_obsoletes_and_create_a_modular_compose}

1.  Add the following snippet to pungi configuration.

        \&#35; Optional module obsoletes configuration which is merged
        \&#35; into the module index and gets resolved
        module_obsoletes_dir = {
        'scm': 'git',
        'repo': 'https://pagure.io/releng/fedora-module-defaults.git',
        'branch': 'main',  \&#35; main for Rawhide, otherwise must match the fedora-module-defaults branch
        'dir': 'obsoletes'
        }

    :::: note
    ::: title
    :::

    Check [pungi-fedora](https://pagure.io/pungi-fedora) for all the
    branches.
    ::::

2.  Follow [pungi docs](https://docs.pagure.org/pungi) on how to create
    a modular compose.

    :::: tip
    ::: title
    :::

    Check the [gathering phase of a modular
    compose](https://docs.pagure.org/pungi/gathering.html&#35;modular-compose)
    and the corresponding configuration reference.
    ::::

### Final repodata contain module obsoletes {#_final_repodata_contain_module_obsoletes}

There are several paths how module obsoletes can appear in the compose
metadata:

1.  Forward: Just follow the steps above and wait for a next modular
    compose of Fedora Rawhide to appear.

2.  Backward (backporting): Since the module obsoletes are checked
    within any modular compose build, you may wait for some other
    module's update to push the changes through. This can be an issue in
    case of an already EOLed/dead module. Again, follow the steps above
    and contact releng team requesting manual modular compose build.

When the obsoletes metadata appear in the repodata
(&#96;modules.yaml&#96; file), DNF is expected to handle the information
regarding obsoletes and react accordingly.

:::: note
::: title
:::

If in doubt, check
<https://github.com/rpm-software-management/ci-dnf-stack/blob/master/dnf-behave-tests/dnf/module/obsoletes.feature>
for what's the expected behavior.
::::

# Inspecting module build failures in Fedora {#_inspecting_module_build_failures_in_fedora}

:::: warning
::: title
:::

&#42;&#42;The Modularity project has been retired&#42;&#42; and there
are [no modules in Fedora 39 or
newer](https://fedoraproject.org/wiki/Changes/RetireModularity) or [in
EPEL](https://lists.fedoraproject.org/archives/list/epel-announce@lists.fedoraproject.org/thread/KA3JQUZW63A4V7OQ7ZVDFCM32EQUSOXH/).
This page is only retained for historical reference.
::::

Have you submitted a build which failed? This page will point you to the
right places to get all the information about build failures.

## Inspecting build failures {#_inspecting_build_failures}

Run the following command using the BUILD_ID from the previous step:

:::: note
::: title
:::

Reminder: You got the BUILD_ID when you [submitted a module
build](building-modules/fedora/building-modules.xml).
::::

    $ fedpkg module-build-info BUILD_ID

which shows you \'State Reason\' --- a short summary of the build
failure regarding the whole module, as well as a list of individual
packages in the module. Find the ones that failed and go to the \'Koji
Task\' URL. There, click on the \'Build\' link which gets you to the
module build page. On this page, inspect the &#96;root.log&#96;,
&#96;build.log&#96;, and other files to get the build error.

# Building modules in Copr {#_building_modules_in_copr}

:::: warning
::: title
:::

&#42;&#42;The Modularity project has been retired&#42;&#42; and there
are [no modules in Fedora 39 or
newer](https://fedoraproject.org/wiki/Changes/RetireModularity) or [in
EPEL](https://lists.fedoraproject.org/archives/list/epel-announce@lists.fedoraproject.org/thread/KA3JQUZW63A4V7OQ7ZVDFCM32EQUSOXH/).
This page is only retained for historical reference.
::::

## Introduction {#_introduction}

Copr (\'Community projects\') is a service that builds your open-source
projects and creates your own RPM repositories. Read the
[documentation](https://docs.pagure.org/copr.copr/user_documentation.html)
to find out more or see it in action
[here](https://copr.fedorainfracloud.org/).

There are multiple ways how to build modules in Copr and it is up to
each user to choose the most suitable one for their specific use-case.

1.  Do you know what modulemd yaml file is and do you have it written
    for your module? Then &lt;&lt;Submit an existing modulemd
    yaml,submit an existing modulemd yaml&gt;&gt; to Copr.

2.  Do you have a Copr project providing some RPM packages and want to
    make module from them? Then don't write a modulemd yaml file
    manually and &lt;&lt;Generate modulemd from a Copr project,generate
    it from a Copr project&gt;&gt;.

Discover more advanced topics such as &lt;&lt;Modules with Copr
packages,requiring Copr packages&gt;&gt; from an existing modulemd yaml
file, &lt;&lt;Modules in Copr as dependencies,depending on modules from
Copr&gt;&gt;, and &lt;&lt;Override module packages,overriding module
packages by regular ones&gt;&gt;.

## Disclaimer {#_disclaimer}

Copr is a third-party service with its own implementation of the module
build process. It does not rely on the [Module Build
Service](https://pagure.io/fm-orchestrator) and it is not governed by
[Fedora Modularity team](community.xml). As a consequence, some features
might behave differently.

Some features are also in rather experimental or proof-of-concept state
(e.g. depending on other Copr modules) and therefore might be cumbersome
to use. Feedback from users is more than welcome and it is the deciding
factor of what is going to be implemented or improved. Please submit
your requests to [pagure issue
tracker](https://pagure.io/copr/copr/issues).

Additionally, only version 1 of the modulemd format is supported.
Version 2 is not supported yet (with an exception of version 2 files
that are compatible with the older format).

## Submit an existing modulemd yaml {#_submit_an_existing_modulemd_yaml}

Currently, there is no web UI for submitting a module build from an
existing modulemd yaml file. The only way is to use &#96;copr-cli&#96;
package. Make sure it is installed.

    dnf install copr-cli

And make sure that an [API token is properly
configured](https://copr.fedorainfracloud.org/api/).

To submit a build from locally stored modulemd yaml file, use:

    copr-cli build-module --yaml /some/path/testmodule.yaml \&lt;COPR project name\&gt;

If the modulemd yaml file is available on a URL accessible for public,
use following:

    copr-cli build-module --url https://example/some/path/testmodule.yaml \&lt;COPR project name\&gt;

To specify a different project owner (e.g. when building into a group
project), use:

    copr-cli build-module --yaml /some/path/testmodule.yaml @mygroup/testmodule

For more information, see &#96;copr-cli build-module \--help&#96; or
&#96;man copr-cli&#96;.

## Generate modulemd from a Copr project {#_generate_modulemd_from_a_copr_project}

This method aims to provide modularity features with the lowest entry
barrier possible. It doesn't demand a user to know either how to write
modulemd yaml file nor using the command line. The only prerequisite is
to have a Copr project with some package successfully built in it.

Open your project, click on &#96;Modules&#96;, then click to &#96;New
Module&#96;. The input page looks like this.

![copr build new module](copr-build-new-module.png)

It provides a list of all successfully built packages in the project. By
default, they are all selected to become part of the module. Uncheck
those that are not wanted. Optionally specify [a module
API](https://pagure.io/modulemd/blob/ade28f3f3b39fcddcb626ca915df1a6ce35c14fd/f/spec.yaml&#35;_137)
or its
[profiles](https://pagure.io/modulemd/blob/ade28f3f3b39fcddcb626ca915df1a6ce35c14fd/f/spec.yaml&#35;_90).

## Modules with Copr packages {#_modules_with_copr_packages}

It is trivial to achieve when generating modulemd from Copr project.
This section describes a special case of how to add a Copr package into
an existing custom modulemd yaml file.

Update &#96;components.rpms&#96; section and add a new package
definition.

    hello:
    rationale: Showing how to use a package from Copr
    ref: \&#8230;
    repository: \&#8230;

The &#96;&#8230;&#96; placeholders need to be replaced with real values.
Open a web browser and navigate to a build detail whose results should
be used by the module. The build needs to be finished successfully.
Scroll down to the &#96;Results&#96; section.

![copr build result](copr-build-result.png)

- Use the hash value from the &#96;Dist Git Source&#96; column as a
  &#96;ref&#96; in the modulemd.

- Follow the link of the &#96;Dist Git Source&#96; value to a Copr
  distgit instance. Use the URL as a &#96;repository&#96; in modulemd -
  with some small adjustments. &#42; Trim everything after
  &#96;.git&#96; &#42; Replace &#96;/cgit/&#96; with &#96;/git/&#96;

![copr disgit](copr-disgit.png)

To avoid confusion, here are some example values.

    hello:
    rationale: Showing how to use a package from Copr
    ref: 9d1ced1
    repository: http://copr-dist-git.fedorainfracloud.org/git/frostyx/hello/hello.git

## Modules in Copr as dependencies {#_modules_in_copr_as_dependencies}

At this moment, Copr doesn't properly parse module dependencies from
modulemd yaml file. They need to be explicitly enabled in the project
settings - more precisely chroot settings within a project.

When the dependency comes from Fedora repositories, simply edit
&#96;Enable module&#96; field and append the module in
&#96;name:stream&#96; format.

If the dependency was built in Copr, it is necessary to edit also the
&#96;Repos&#96; field and provide a repository URL from which the module
can be installed. See the &lt;&lt;Installing modules from Copr&gt;&gt;
section to learn how to find a repofile for a module (in this case the
module that is used as a dependency). Use it's &#96;baseurl&#96; as the
value for &#96;Repos&#96; field.

## Installing modules from Copr {#_installing_modules_from_copr}

Currently &#96;dnf copr&#96; plugin does not support enabling module
repositories and therefore it needs to be done manually. Navigate to a
Copr project in a web browser, see the &#96;Modules&#96; page, and open
detail of a module that is to be installed. If the build is still
running, wait until it finishes. For successfully built modules, a \'How
to use\' section is displayed. Follow its instructions. After that,
standard DNF commands for manipulation with modules can be used.

See
<https://docs.fedoraproject.org/en-US/modularity/installing-modules/>

## Override module packages {#_override_module_packages}

The package version resolution was straightforward in the pre-modularity
era. If multiple repositories provided the same package, the one with
the highest version was preferred. It is [more complicated
now](https://dnf.readthedocs.io/en/latest/modularity.html&#35;package-filtering).
If there is a module stream enabled within the system and this stream
provides a package, it is preferred over its non-modular variant
regardless of its version.

To suppress this behavior, &#96;module_hotfixes&#96; repositories were
invented. For them, DNF upgrades to a higher version of a package
regardless of where it comes from. Enable them in Copr by going to
project settings and turning on this checkbox.

    [ ] This repository contains module hotfixes
    This will make packages from this project available on along with
    packages from the active module streams.

Or in a command line

    copr-cli modify frostyx/foo --module-hotfixes on

## Examples {#_examples_2}

Build a module from a modulemd yaml file hosted online:

    copr-cli create testproject1 --chroot fedora-rawhide-x86_64
    copr-cli build-module testproject1 \
    --url https://src.fedoraproject.org/modules/httpd/raw/2.4/f/httpd.yaml

Alternatively, build a module from a localy stored modulemd yaml file:

    fedpkg clone -a modules/httpd
    cd httpd
    copr-cli create testproject2 --chroot fedora-rawhide-x86_64
    copr-cli build-module testproject2 --yaml httpd.yaml

## External resources {#_external_resources}

- <http://frostyx.cz/posts/how-to-build-modules-in-copr>

- <http://frostyx.cz/posts/modules-with-copr-packages>

- <http://frostyx.cz/posts/copr-loves-modularity>

- <http://frostyx.cz/posts/module-hotfixes-in-copr>

- <http://frostyx.cz/posts/copr-modularity-in-retrospect>

# Building modules locally {#_building_modules_locally}

:::: warning
::: title
:::

&#42;&#42;The Modularity project has been retired&#42;&#42; and there
are [no modules in Fedora 39 or
newer](https://fedoraproject.org/wiki/Changes/RetireModularity) or [in
EPEL](https://lists.fedoraproject.org/archives/list/epel-announce@lists.fedoraproject.org/thread/KA3JQUZW63A4V7OQ7ZVDFCM32EQUSOXH/).
This page is only retained for historical reference.
::::

This page walks you through building modules locally on your machine.

## Prerequisites {#_prerequisites}

Before you can start building modules locally, you have to install the
dependencies below:

    $ sudo dnf install module-build-service fedpkg rpkg

If you are not running the build commands as root you have to add your
user to the &#96;mock&#96; group:

    $ sudo usermod -a -G mock USERNAME
    $ newgrp

## Build your module from distgit {#_build_your_module_from_distgit}

Local builds are started using &#96;fedpkg&#96; from within your
dist-git repository.

For example, to submit a build of the &#96;testmodule:master&#96;
module, run:

:::: note
::: title
:::

Local builds don't support stream expansion. If your module depends on
multiple streams of another module, such as &#96;platform&#96;, you need
to specify what stream you want to build against. For example:
&#96;fedpkg module-build-local -s platform:f28&#96;.
::::

    $ fedpkg clone modules/testmodule
    $ cd testmodule
    $ git checkout master
    $ fedpkg module-build-local

When the build finishes, you'll be able to find the results in:

    ~/modulebuild/builds/MODULE/results/

where MODULE is \'module-NAME-STREAM-VERSION\', so for example
\'module-testmodule-master-20180612122805\'.

## Build your module with other SCM {#_build_your_module_with_other_scm}

:::: warning
::: title
:::

This feature is experimental use it at own risk. If you can use distgit
for building your packages.
::::

Building modules from other SCM (github, gitlab etc.) is more
complicated then disgit. The installation prerequisities are the same as
for disgit.

When all the prerequisities where installed we need to configure MBS
and.

### MBS configuration {#_mbs_configuration}

We need to set a configuration option in main MBS configuration file so
it will accept other SCM urls not only disgit. In the file
&#96;/etc/module-build-service/config.py&#96; we add the
&#96;DISTGITS&#96; property to the &#96;BaseConfiguration&#96; class.

    class BaseConfiguration(object):
    .
    .
    .
    DISTGITS = {'\&lt;scm_url_you_want_to_build_from\&gt;': (\&lt;cmd_that_clones_your_repo\&gt;, \&lt;cmd_which_gets_your_package_source\&gt;)}
    .
    .
    .

The defaults for the &#96;DISTGITS&#96; property can be found
[here](https://pagure.io/fm-orchestrator/blob/master/f/module_build_service/common/config.py).
The &#96;DISTGITS&#96; repository is a python dictionary. Each
&#96;key&#96; of the &#96;DISTGITS&#96; property represents an SCM url.
When MBS resolves where from to download the spec files and sources for
the build process, it will look into the &#96;DISGITS&#96; property and
try to match package urls with the keys of the dictionary. When a match
is found then MBS knows this SCM is enabled.

The &#96;value&#96; part of each &#96;key&#96; in the &#96;DISTGIT&#96;
property represents a python tuple with 2 elements. First element
represents a bash command which clones your package repository into the
package buildroot. Second element represents a bash command which
downloads sources of your package into the SOURCE dir in the package
buildroot at build time.

For example if the packages are hosted on github and we use rpmbuild
built-in feature to download sources, the &#96;DISTGITS&#96; would look
like this:

    class BaseConfiguration(object):
    .
    .
    .
    DISTGITS = {'https://github.com/user/package': ('git clone {repo_path}', None)}
    .
    .
    .

The &#96;{repo_path}&#96; will be replaced during runtime with url you
provided in your modulemd yaml file when defining packages, but only for
the first element of the tuple. The second element is set to
&#96;None&#96; as it won't be downloading package sources through MBS
but through rpmbuild. Although this needs to be enabled in your spec
files. If you don't want to modify your spec files, then you have to
define a bash command which will download your package sources.

### Spec file configuration (Optional) {#_spec_file_configuration_optional}

To enable downloading package sources through rpmbuild, you have to
modify the spec file of your RPM packages. By default rpmbuild does not
download your sources from &#96;Source0&#96;. To enable this feature you
need to define the &#96;\_disable_source_fetch&#96; property to 0
somewhere before the &#96;Source0&#96; directive:

    %define _disable_source_fetch 0
    Source0:        \&lt;url_to_your_source\&gt;

### MBS Mock configuration {#_mbs_mock_configuration}

MBS has its own configuration file for Mock. The file can be found in
&#96;/etc/module-build-service/mock.cfg&#96;. To be able to download
package sources from the buildroot chroot environment we need to enable
networking for mock. Just add this into the
&#96;/etc/module-build-service/mock.cfg&#96;:

    config_opts['rpmbuild_networking'] = True

### Building the module {#_building_the_module}

When the initial setup has been done you can build the module stream
with the following command:

    mbs-manager build_module_locally --offline -r /etc/yum.repos.d/fedora.repo --file \&lt;path_to_modulemd_file\&gt; --stream \&lt;name_of_module_stream\&gt;

The logs and artifacts can be found in:

    ~/modulebuild/builds/MODULE/results/

Where &#96;MODULE&#96; is \'module-NAME-STREAM-VERSION\', so for example
\'module-testmodule-master-20180612122805\'.

The &#96;MODULE&#96; directory holds the MBS main log. Further in the
&#96;results/&#96; directory you will find logs for each package
buildroot and the build artifacts.

## Testing your module {#_testing_your_module}

:::: warning
::: title
:::

This requires Fedora 28 or higher.
::::

To test your module, add the repository to your system by creating an
entry similar to this in &#96;/etc/yum.repos.d/test.repo&#96;:

    [local]
    name=My Local Repository
    baseurl=file:///home/adam/modulebuild/builds/module-testmodule-master-20180612122805/results/
    gpgcheck=0
    enabled=1

Please replace \'adam\' with your user name, and
\'module-testmodule-master-20180612122805\' with the actual value for
your module.

Now, when you list the available modules on your system, you should be
able to see it and install it:

    $ dnf module list
    $ dnf module install testmodule:master

# Policies Regarding Modules in Fedora, Fedora ELN and EPEL {#_policies_regarding_modules_in_fedora_fedora_eln_and_epel}

:::: warning
::: title
:::

&#42;&#42;The Modularity project has been retired&#42;&#42; and there
are [no modules in Fedora 39 or
newer](https://fedoraproject.org/wiki/Changes/RetireModularity) or [in
EPEL](https://lists.fedoraproject.org/archives/list/epel-announce@lists.fedoraproject.org/thread/KA3JQUZW63A4V7OQ7ZVDFCM32EQUSOXH/).
This page is only retained for historical reference.
::::

## Modularity was retired from Fedora 39+ and EPEL {#_modularity_was_retired_from_fedora_39_and_epel}

There are [no modules in Fedora 39 or
newer](https://fedoraproject.org/wiki/Changes/RetireModularity). There
are [no modules in
EPEL](https://lists.fedoraproject.org/archives/list/epel-announce@lists.fedoraproject.org/thread/KA3JQUZW63A4V7OQ7ZVDFCM32EQUSOXH/).
The rest of this page serves as a policy for older Fedora releases only
(Fedora 37 and 38).

## Requirements for All Module Streams {#_requirements_for_all_module_streams}

&#42; The module maintainer &#42;MUST&#42; have explicit commit
privileges to all packages included in the module stream. The
provenpackager privilege in Fedora is not sufficient.[^1] &#42;
Components built into a module &#42;MUST&#42; be associated with a
reachable commit in Fedora dist-git.[^2] &#42; If a stream of a module
has build-time-only components, all such components &#42;MUST&#42; be
marked as &#96;buildonly: True&#96; in the module metadata to avoid
shipping them to users and polluting their repository.

## Requirements for Modules in Fedora {#_requirements_for_modules_in_fedora}

&#42; Modular-only packages &#42;MUST NOT&#42; exist in Fedora. Modular
versions &#42;MAY&#42; exist as alternatives to non-modular packages
only. There is an exception to this rule: if the package does not
function in non-modular Fedora (with a reasonable amount of work), it is
permitted to have it in module only.[^3] For the time being, such
exceptions can be granted by FESCo. &#42; Default streams &#42;MUST
NOT&#42; be used in Fedora.[^4] &#42; Packagers &#42;SHOULD&#42; prefer
compatibility packages rather than modules wherever reasonable (e.g.,
libraries, language interpreters, ..., and anything that can benefit
from parallel installability).

## Requirements for Default Streams in Fedora ELN {#_requirements_for_default_streams_in_fedora_eln}

&#42; &#42;Default streams are not permitted in Fedora or EPEL 8.&#42;
Fedora ELN permits defaults streams that adhere to the policy below.
&#42; All RPMs in default module streams are required to conform to the
same [requirements around
Conflicts](https://docs.fedoraproject.org/en-US/packaging-guidelines/Conflicts/)
as non-modular RPMs. &#42; Packages provided at runtime by the default
stream of a module &#42;MUST&#42; depend only on packages provided by
packages from default module streams or the non-modular package set. By
extension, default streams of a module &#42;MUST NOT&#42; have a
dependency on any non-default stream.[^5] &#42; Packages provided from
default streams &#42;MAY&#42; depend on content from other default
streams. If they do so, this dependency &#42;MUST&#42; be encoded in the
module metadata.[^6] &#42; All packages provided at runtime by the
default stream of a module &#42;MUST&#42; provide all the same
functionality that a downstream consumer would expect from a package in
the non-modular package set.[^7] &#42; All packages provided at runtime
by the default stream of a module &#42;SHOULD&#42; be declared as a
module API or bundled appropriately.[^8] &#42; The default stream of a
module &#42;MUST NOT&#42; change to a different stream within a released
Fedora version.[^9] The default stream &#42;MAY&#42; be changed in
Rawhide or during Fedora upgrades. Changes to default streams
&#42;MUST&#42; be approved via a [Fedora Change
proposal](https://docs.fedoraproject.org/en-US/program_management/changes_policy/&#35;_change_process).
&#42; Packages &#42;MAY&#42; convert from a non-modular package to a
modular default stream (or the reverse) only in Rawhide or during Fedora
upgrades. &#42; Default streams &#42;MUST NOT&#42; provide a binary RPM
with the same package name as a non-modular RPM in the same release
except in the case of a transition from one to the other.[^10] &#42;
Default streams &#42;MUST NOT&#42; provide a binary RPM with the same
package name as an RPM in a default stream of another module in the same
release.[^11] &#42; Multiple default streams &#42;MUST NOT&#42; provide
the same binary package names at runtime.[^12] &#42; Default streams
&#42;MUST NOT&#42; provide a package that overrides a package of the
same name in the non-modular content except in approved cases of
migration between modular and non-modular delivery. &#42; Default
streams &#42;MUST NOT&#42; use the &#96;data.buildopts.rpm.macros&#96;
metadata section without approval by FESCo.[^13]

# Fedora Packaging Guidelines for Modules {#_fedora_packaging_guidelines_for_modules}

:::: warning
::: title
:::

&#42;&#42;The Modularity project has been retired&#42;&#42; and there
are [no modules in Fedora 39 or
newer](https://fedoraproject.org/wiki/Changes/RetireModularity) or [in
EPEL](https://lists.fedoraproject.org/archives/list/epel-announce@lists.fedoraproject.org/thread/KA3JQUZW63A4V7OQ7ZVDFCM32EQUSOXH/).
This page is only retained for historical reference.
::::

These guidelines specify restrictions and guidance for [defining modules
in modulemd](building-modules/fedora/defining-modules.xml).

## Short Overview {#_short_overview}

&#42; Packager &#42;&#42;MUST&#42;&#42; specify &#96;summary&#96; &#42;
Packager &#42;&#42;MUST&#42;&#42; specify &#96;description&#96; &#42;
Packager &#42;&#42;MUST&#42;&#42; specify &#96;license/module&#96;
license(s) based on allowed licenses in Fedora &#42; Packager
&#42;&#42;MUST&#42;&#42; specify &#96;dependencies&#96; &#42; Packager
&#42;&#42;MUST&#42;&#42; specify &#96;components&#96; &#42; Packager
&#42;&#42;SHOULD&#42;&#42; specify &#96;profiles&#96; &#42; Packager
&#42;&#42;SHOULD&#42;&#42; specify &#96;api&#96; &#42; Packager
&#42;&#42;MAY&#42;&#42; specify &#96;data&#96; in key-value format in
xmd &#42; Packager &#42;&#42;MAY&#42;&#42; specify &#96;references&#96;
&#42; Packager &#42;&#42;MAY&#42;&#42; specify &#96;filter&#96; &#42;
Packager &#42;&#42;MAY&#42;&#42; specify &#96;buildopts&#96; &#42;
Packager &#42;&#42;MUST NOT&#42;&#42; specify &#96;name&#96;, name is
taken from name of dist-git repository &#42; Packager &#42;&#42;MUST
NOT&#42;&#42; specify &#96;stream&#96;, stream is taken from branch of
dist-git repository &#42; Packager &#42;&#42;MUST NOT&#42;&#42; specify
&#96;version&#96;, it is automatically generated by buildsystem &#42;
Packager &#42;&#42;MUST NOT&#42;&#42; specify &#96;arch&#96;, it is
automatically filled in by buildsystem &#42; Packager &#42;&#42;MUST
NOT&#42;&#42; specify &#96;servicelevels&#96;, they are automatically
filled in by buildsystem from PDC &#42; Packager &#42;&#42;MUST
NOT&#42;&#42; specify &#96;license/content&#96; license(s), they are
picked up from components which are built &#42; Packager &#42;&#42;MUST
NOT&#42;&#42; specify &#96;artifacts&#96;

## Long Overview {#_long_overview}

### Document header and the data block {#_document_header_and_the_data_block}

Every modulemd file &#42;&#42;MUST&#42;&#42; contain a modulemd document
header which consists of the document type tag and the document format
version, and a data block holding the module data.

    document: modulemd
    version: 2
    data:
    (\&#8230;)

The version is an integer and denotes the version of the metadata format
the rest of the document is written in. Packagers
&#42;&#42;SHOULD&#42;&#42; use latest available version of
specification.

### Summary and description {#_summary_and_description}

Every module &#42;&#42;MUST&#42;&#42; include human-readable short
summary and description. Both should be written in US English.

    summary: An example module
    description: \&gt;-
    An example long description of an example module, written just
    to demonstrate the purpose of this field.

The summary is a one sentence concise description of the module and
&#42;&#42;SHOULD NOT&#42;&#42; end in a period.

The description expands on this and &#42;&#42;SHOULD&#42;&#42; end in a
period. Description &#42;&#42;SHOULD NOT&#42;&#42; contain installation
instructions or configuration manuals.

### Licensing {#_licensing}

Every module &#42;&#42;MUST&#42;&#42; contain a license block and
declare a list of the module's licenses. Note these aren't the module's
components\' licenses.

    license:
    module:
    - MIT

Fedora content, such as SPEC files or patches not included upstream,
uses the MIT license by default, unless the component packager declares
otherwise. Therefore MIT might be a reasonable default for most module
authors as well.

### Dependencies {#_dependencies}

Modules &#42;&#42;MAY&#42;&#42; depend on other modules. These module
relationships are listed in the dependencies block. However, none of
modules are buildable without &#96;platform&#96; module hence packagers
are required to specify it.

Packagers &#42;&#42;SHOULD&#42;&#42; be using stream name expansion to
make their modules compatible with other existing modules. The following
example builds and runs the module on any &#96;platform:&#96;

    dependencies:
    - buildrequires:
    platform: []
    requires:
    platform: []

Note the stream name expansion is only supported by the second version
of the format. Unlike in the first version, the &#96;dependencies&#96;
block is a list of dictionaries.

### Extensible module metadata block {#_extensible_module_metadata_block}

Modules &#42;&#42;MAY&#42;&#42; also contain an extensible metadata
block, a list of vendor-defined key-value pairs.

    xmd:
    user-defined-key: 42
    another-user-defined-key:
    - the first value of the list
    - the second value of the list

### References {#_references}

Modules &#42;&#42;MAY&#42;&#42; define links referencing various
upstream resources, such as community website, project documentation or
upstream bug tracker.

    references:
    community: http://www.example.com/
    documentation: http://www.example.com/docs/1.23/
    tracker: http://www.example.com/bugs/

### Profiles {#_profiles}

The module author &#42;&#42;MAY&#42;&#42; define lists of packages that
would be installed when the module is enabled and the particular profile
is selected. Whether the packages actually get installed depends on the
user's configuration. It is possible to define a profile that doesn't
install any packages.

Profile names are arbitrary strings. There are currently few
special-purpose profile names defined, see specification for details.

If the module includes one or more profile definition, [module
defaults](building-modules/fedora/managing-defaults.xml)
&#42;&#42;SHOULD&#42;&#42; also be defined.

In the case of RPM content, the profile package lists reference binary
RPM package names.

### API {#_api}

Module API are components, symbols, files or abstract features the
module explicitly declares to be its supported interface. Everything
else is considered an internal detail and shouldn't be relied on by any
other module.

Every module &#42;&#42;SHOULD&#42;&#42; define its public API.

### Filters {#_filters}

Module filters define lists of components or other content that should
not be part of the resulting, composed module deliverable. They can be
used to only ship a limited subset of generated RPM packages, for
instance.

    filter:
    rpms:
    - mypackage-plugins

Currently the only supported type of filter are binary RPM packages.

# Modularity Naming Guidelines {#_modularity_naming_guidelines}

:::: warning
::: title
:::

&#42;&#42;The Modularity project has been retired&#42;&#42; and there
are [no modules in Fedora 39 or
newer](https://fedoraproject.org/wiki/Changes/RetireModularity) or [in
EPEL](https://lists.fedoraproject.org/archives/list/epel-announce@lists.fedoraproject.org/thread/KA3JQUZW63A4V7OQ7ZVDFCM32EQUSOXH/).
This page is only retained for historical reference.
::::

Each module has a &#42;&#42;name&#42;&#42;, and one or more
&#42;&#42;streams&#42;&#42; that usually represent a major version of
the application, language stack, or other software in the module. To
simplify their installation, modules can define
&#42;&#42;profiles&#42;&#42; representing a specific use case. Modules
are built out of SRPM packages that have a name and one or more
branches.

&#42;&#42;Example 1:&#42;&#42; A Node.js module could be named
\'nodejs\', with three streams \'6\', \'8\' and \'10\', and two profiles
\'default\' and \'devel\'. This module would include a single package in
each stream named \'nodejs\', branched as \'6\', \'8\', and \'10\'.

&#42;&#42;Example 2:&#42;&#42; Another one, PostgreSQL, could be named
as \'postgresql\', its two streams could be \'9.6\' and \'10\', because
that's where the upstream compatibility is, and its profiles could
include \'client\' and \'server\'. Both streams could be built out of
two packages. One named \'postgresql\', having branches \'9.6\' and
\'10\', which would be the main package; and another one named
\'python-pgsql\', having a single branch \'latest\', which would always
bind to the right version of the database during build, and would
provide Python bindings.

## Module name {#_module_name}

A module usually represents an application, a language stack, or any
other logical collection of packages. Module name should represent the
name of the software it ships. Using lowercase, hyphen-separated names
is preferable. Some examples could include \'nodejs\', \'golang\',
\'golang-ecosystem\', or \'cri-o\'.

A module name maps to its repository name in DistGit.

## Module stream name {#_module_stream_name}

The module stream name is assigned by creating a branch of that name in
DistGit and building from it. The Module Build Service will
automatically set the stream name of the resulting module to match.

### Option 1: Major version {#_option_1_major_version}

A stream usually represents a major version of the software, and should
follow the versioning of the major upstream component included in the
module. Consideration should be given to the upstream community's
adherence to API (or even ABI) stability on the versions of their
software. In other words, some communities will maintain stability on
the X branch, many the Y branch, and some even the Z branch. As a
result, the branch names should reflect that stability. For example,
most communities are stable on the Y branch so the branch name should be
\'X.Y\'. (e.g. mariadb:10.2) included in the module.

Compatibility on non-technical factors should be also considered. For
example, a package that maintains exactly the same API but has a
significant visual and UX overhaul probably belongs in a new stream. Or
to put it another way, human interaction is an interface too.

### Option 2: CalVer {#_option_2_calver}

If your module is a \'collection of items\' with no primary piece of
software (e.g. container-tools), the versioning scheme should use the
CalVer (<http://calver.org/>) scheme with YYYY.MINOR where the YYYY is
the year of the release and MINOR version is an integer starting at 0.
In other words, if I released a system-tools module in November of 2017
we would expect to see 2017.0. My next release, in May of 2018, which
does not break ABI/API, is also 2017.0. However, in October of 2018 we
want to introduce a new stream so we name it 2018.0. The month is
omitted as ideally these modules won't be breaking API/ABI more than
once a year.

### Option 3: Rolling and unstable streams {#_option_3_rolling_and_unstable_streams}

For streams that don't guarantee an API/ABI stability over time and just
roll forward, we suggest packagers use one of the following stream
names.

&#42; \'rolling\' for user-focused content meant for general use &#42;
\'unstable\' for pre-release content or content in active development
meant for preview and testing rather than general use

We mandate a good use of the description and/or summary field to clearly
state what this particular stream represents.

This policy doesn't enforce changes in existing branch names, however,
packagers are welcome to do so in order to bring more consistency to the
distribution.

### Option 4: Upstream conventions {#_option_4_upstream_conventions}

In case there are well-established upstream conventions, using them is
also a good option.

Again, especially in this case, we mandate a good use of the description
and/or summary field to clearly state what this particular stream
represents.

## Module profile name and description {#_module_profile_name_and_description}

Profiles make installation easier by giving the user some predefined
package groups that represent a common installation for a specific use
case. Profiles have name and a description --- using both is mandatory.

Profile name should be a one word that best represent the use case. Some
examples could include \'client\' or \'server\' for database modules,
\'default\' or \'devel\' for language runtime modules, but also
\'minimal\' and others. There some reserved profile names for specific
purposes e.g. setting up a buildroot. Please see the [modulemd
spec](https://github.com/fedora-modularity/libmodulemd/blob/master/spec.v2.yaml)
for a complete list.

Descriptions should be a short summary describing the profile. Including
it is important especially for potential translations, as profile names
won't be translated.

### Unified profile names {#_unified_profile_names}

In some cases, there are many suitable alternatives for for one meaning
i.e. \'dev\', \'devel\', and \'development\'. We believe that choosing
one that would be consistently used across all modules that need such
profile would lead to a better user experience. The ones identified are
listed below:

&#42; \'default\' a default profile for a \'standard\' installation,
should the module have something like this &#42; \'devel\' for
development-related profiles &#42; \'client\' only the client component
of a piece of software (e.g. database client) &#42; \'server\' only the
server component of a piece of software (e.g. database server)

## Package name {#_package_name}

No changes for package names with Modularity. Please refer to the
official [Guidelines for Naming Fedora
Packages](https://docs.fedoraproject.org/en-US/packaging-guidelines/Naming/).

## Package branch name {#_package_branch_name}

Packages included in modules should be branched in a similar manner as
modules. So instead of having one branch for release (such as \'f27\',
\'f28, etc.), using upstream major versions as branches is recommended.
Please read the Module stream name section above for guidance.

The exact branching should be chosen with consideration given to the
upstream community's adherence to API/ABI stability on the versions of
their software. In other words, in the context of X.Y.Z style naming,
some communities will maintain stability on the X branch, many the Y
branch, and some even the Z branch. As a result, the branch names should
reflect that stability. For example, most communities are stable on the
Y branch so the branch name should be \'X.Y\'. While this rule is
focusing on examples using X.Y.Z style naming, CalVer
(<http://calver.org/>), or other versioning schemes, should be
faithfully reflected using the same guidance regarding which branches to
create.

For \'rolling release\' projects that don't change their API/ABI (e.g.
Python's timezone database, &#96;pytz&#96;) a single \'stable\' branch
is appropriate.

# Frequently Asked Questions (FAQ) {#_frequently_asked_questions_faq}

:::: warning
::: title
:::

&#42;&#42;The Modularity project has been retired&#42;&#42; and there
are [no modules in Fedora 39 or
newer](https://fedoraproject.org/wiki/Changes/RetireModularity) or [in
EPEL](https://lists.fedoraproject.org/archives/list/epel-announce@lists.fedoraproject.org/thread/KA3JQUZW63A4V7OQ7ZVDFCM32EQUSOXH/).
This page is only retained for historical reference.
::::

**Q:** Exactly what problem are you trying to solve?

**A:** Deploying software has many solutions, but what gets deployed
often plays out as a fight between developers and operators. Developers
want the latest (or at least later) features. Operators want software in
packages, certified, with a known period of support. Fedora Modularity
provides multiple versions of packages in a Linux distribution with the
qualities expected from a Linux distribution: transparently built and
delivered, actively maintained, and easy to install --- making both
happy.

**Q:** How is this different from containers?

**A:** Containers are a solution to a very different problem. They allow
you to bundle your application and all of its dependencies in a
container image that you can run in isolation on basically any Linux
system with a container runtime.\

Modularity provides multiple versions of packages in a Linux
distribution with the qualities expected from a Linux distribution:
transparently built and delivered, actively maintained, and easy to
install.\

Modularity and containers work nicely together --- since you need to get
the software (such as your app's dependencies) from somewhere. Getting
them from a Linux distribution (and now with the choice of version
thanks to Modularity) makes building and updating containers (with
security updates for example) easier.

**Q:** How does this differ from Software Collections (SCLs)?

**A:** SCLs use a different method of packaging allowing for multiple
versions of the same piece of software to be installed on one system, by
putting them into separate namespaced paths. Modularity on the other
hand uses standard RPM packaging --- so things are where you expect them
to be --- but you can only install one version at a time.\

SCLs have proven to be hard to maintain and hard to use (Special macros
in spec files, package name mangling, running \'scl enable\' in order to
make them visible). And the ability to install multiple versions in
parallel has turned out not to be a common use case. The real benefit of
SCLs was the ability to choose a specific version of software --- and
that's exactly what Modularity offers.

**Q:** Couldn't we solve this with having compat packages, or putting
versions into package names for different version streams?

**A:** That could work for some scenarios, however, it would introduce
an unnecessary complexity to the whole system by adding even more
packages to choose from. You would also need to encode information such
as the major version (stream) in the package name, in a similar way how
SCLs do that. How would you distinguish packages built against different
versions of runtimes or other dependencies?\

Modularity groups packages into modules --- a representation of an
application, a language runtime, or any logical group. That makes the
content more granular and easier to navigate. Modules can be available
in multiple streams --- usually representing a major version of the
software they ship.

**Q:** Can I install more versions at once?

**A:** As modularity uses standard RPM packaging in order to install
software in the usual places, the answer is no. However, there are other
existing technologies --- such as containers --- allowing exactly that
and work well with Modularity.

**Q:** How is this different from RPM? Why not just different repos?

**A:** Modularity uses RPM as the core building block. From the user
perspective, replacing modules with repositories could be technically
possible, however:\
A) Modules as a core concept in the client tooling significantly
simplifies usage. Users can easily query for the modules available and
install them with a simple command, without the need of manually
enabling repositories.\
B) From our perspective, a repository is a source of software provided
by a vendor, not necessarily representing a single application. We want
to keep this principal and allow multiple applications to be present in
a repository.\
C) Modularity also helps packagers to automatically submit multiple
module builds at once based on their context configurations.

**Q:** Are you going to produce all versions? What life cycles and
versions are envisioned?

**A:** We are developing the technology such as the build pipeline and
client tooling to enable contributors to build multiple versions. We
envision longer life cycles of stacks mainly for server, and
devel/rolling releases of some stacks for developers. However,
contributors to the Fedora project will be the deciders and maintainers
of any versions that are available.

**Q:** I can just 'dnf downgrade' to get an older version.. Why do we
need modularity?

**A:** Using an older version that is no longer maintained can be
dangerous, mostly because of the lack of security updates. Modules, on
the other hand, represent a major version that is still being actively
maintained by the upstream and therefore should receive updates.

**Q:** Is this different from single app VMs with custom versions?

**A:** This helps with a single app VM with custom versions. But instead
of getting them from somewhere and maintaining them yourself, there is a
good chance a module with the version you need already exists and is
maintained --- so you can just install it. Same as with containers, it
helps users to get the right version for their system.

&#42; &#42;&#42;Advanced&#42;&#42; = Hosting modules for Fedora

:::: warning
::: title
:::

&#42;&#42;The Modularity project has been retired&#42;&#42; and there
are [no modules in Fedora 39 or
newer](https://fedoraproject.org/wiki/Changes/RetireModularity) or [in
EPEL](https://lists.fedoraproject.org/archives/list/epel-announce@lists.fedoraproject.org/thread/KA3JQUZW63A4V7OQ7ZVDFCM32EQUSOXH/).
This page is only retained for historical reference.
::::

Since modules are technically collections of RPM packages with metadata,
they are hosted the same way as traditional RPM packages are --- in a
repository. Apart from the packages, such repository must also contain
the modular metadata (modulemd) that come with the modules.

## Creating a modular repository {#_creating_a_modular_repository}

Modular repositories are created in two steps:

1.  Creating the repository using &#96;createrepo_c&#96;

2.  Adding modular metadata (modulemd) using &#96;modifyrepo_c&#96;

:::: warning
::: title
:::

Modular repository must contain the modular metadata (modulemd) in the
repodata. Excluding the metadata will cause all the modular packages to
become nonmodular packages which could have negative consequences.
::::

To create a repository out of RPM packages, run:

    $ createrepo_c DIRECTORY

&#42; &#96;DIRECTORY&#96; --- path to a directory with RPM packages that
will be converted into a repository

To add the modular metadata (modulemd), run:

    $ modifyrepo_c --mdtype=modules modules.yaml REPO

&#42; &#96;modules.yaml&#96; --- YAML multidocument containing all
modulemds --- the final form of modulemd produced by the build system
&#42; &#96;REPO&#96; --- path to the repository --- the directory from
the previous step

# NSVCA vs NEVRA {#_nsvca_vs_nevra}

\+

\+

:::: warning
::: title
:::

&#42;&#42;The Modularity project has been retired&#42;&#42; and there
are [no modules in Fedora 39 or
newer](https://fedoraproject.org/wiki/Changes/RetireModularity) or [in
EPEL](https://lists.fedoraproject.org/archives/list/epel-announce@lists.fedoraproject.org/thread/KA3JQUZW63A4V7OQ7ZVDFCM32EQUSOXH/).
This page is only retained for historical reference.
::::

## Naming and identifying modules in Fedora {#_naming_and_identifying_modules_in_fedora}

With the introduction of Modularity to the packager ecosystem it also
introduced several challenges. First was that the NEVRA
(name-epoch-version-release-architecture) package naming convention used
in Fedora was insufficient. Modules are uniquely identified by the NSVCA
naming convention, which stands for *name*, *stream*, *version*,
*context*, and *architecture*. This page describes both the source-level
ID (NSV) and the binary-level ID (NSVCA).

## Source-level module ID (NSV) {#_source_level_module_id_nsv}

At the source level, modules are only identified by the first three:
*name*, *stream*, and *version*. Name is defined as a name of the
module's repository in [DistGit](https://src.fedoraproject.org/), stream
is a name of the branch in [DistGit](https://src.fedoraproject.org/),
and version is the timestamp of a commit.

### Name {#_name}

Name of the module corresponds to the name of the application or the
language stack it represents. An example of a name could be postgresql
for a PostgreSQL database module, or nodejs for a Node.js runtime.

### Stream {#_stream}

Streams are variants of a module with a certain promise.

In most cases, streams promise backwards compatibility with a major
version of the application or the language stack they provide. For
example, let's say the Node.js runtime is supported in two major
versions: 6 and 8. In this case, the module nodejs would have two
streams: 6 and 8.

However, streams can also promise different things such as stability. A
good example of this is the calc package in Fedora which is maintained
in two upstream branches: stable for the latest stable release and
unstable for the latest development version. Using modularity, this
package could be built as a calc module in two different streams: stable
and unstable.

In addition to the version promise, streams are also a way for packagers
to communicate the level of maintenance. Does the maintainer plan to
apply every minor patch? Will they apply security fixes quickly? Or is
the module updated only twice a year? This can also be part of the
promise.

Another different example could be a stream that provides the software
compiled using some experimental flags increasing the performance.

Anyway, you get the idea. Streams are a very flexible and powerful tool.
Use them wisely.

### Version {#_version}

Versions are just updates of a given stream. Technically, version is a
number generated by the build system. Higher number always wins. This
means that version does not identify a major/minor version of the
software but the update/commit to a particular stream.

## Binary-level ID (NSVCA) {#_binary_level_id_nsvca}

Building a module from one source can result in multiple different
binaries. Different binaries are typically produced for different
architectures (i.e. x86_64, armv7hl, etc.) and different Fedora releases
(i.e. Fedora 28, Fedora 29, EPEL 7, etc.).

Module binaries use the full NSVCA --- so in addition to the name,
stream, and version fields described above, there are two more for
binaries: architecture and context.

### Architecture {#_architecture}

Fedora is built for many different architectures. The architecture field
simply distinguishes architecture-specific binaries from each other. The
value is typically the same as with RPM packages, i.e. x86_64, armv7hl,
etc.

### Context {#_context}

Context is used to distinguish binaries built for different Fedora
releases. Thanks to stream expansion, modules can also be built against
multiple streams of other modules, i.e. different versions of a language
runtime etc.

The value is generated by the build system and is usually hidden from
the user as it doesn't have any informational value by itself --- it is
a hash. However, the client tooling consuming this value can present it
in a useful way.

One way of representing the context could be listing the Fedora releases
for which a certain module has been built.

## NSVCA Definition {#_nsvca_definition}

This defines naming policy for modulemd metadata of final (built)
modules. This policy does &#42;&#42;NOT&#42;&#42; apply on sources such
as modulemd yaml in dist-git.

The goal is to provide unique identifiers for modules that are both
human readable and also suitable for machine processing.

## Fields {#_fields}

&#42; &#42;&#42;N&#42;&#42; - Name &#42; &#42;&#42;S&#42;&#42; - Stream
&#42; &#42;&#42;V&#42;&#42; - Version &#42; &#42;&#42;C&#42;&#42; -
Context &#42; &#42;&#42;A&#42;&#42; - Arch &#42; &#42;&#42;P&#42;&#42; -
Profile

## Separators {#_separators}

Fields are separated with \':\' (colon): N:S:V:C:A.

If P is specified, it's separated from N:S:V:C:A with \'/\' (forward
slash): N:S:V:C:A/P.

### Examples {#_examples_3}

    \&#35; N:S:V:C:A
    mariadb:3.6:1:0123abcd:x86_64
    \&#35; N:S:V:C:A/P
    mariadb:3.6:1:0123abcd:x86_64/server

## Forms {#_forms}

A form is a sequence of fields that fully or partially identifies a
module.

### Full Forms {#_full_forms}

N:S:V:C:A

:   Unique identifier of a module.

N:S:V:C:A/P

:   Unique identifier of a module profile.

### Partial Forms {#_partial_forms}

Supported partial forms are: &#96;N \[ : S \[ :V \[ :C \] \] \] \[ :A \]
\[ /P \]&#96;

Namely:

&#42; &#96;N&#96; &#42; &#96;N::A&#96; &#42; &#96;N:S&#96; &#42;
&#96;N:S::A&#96; &#42; &#96;N:S:V&#96; &#42; &#96;N:S:V::A&#96; &#42;
&#96;N:S:V:C&#96; &#42; &#96;N:S:V:C:A&#96; (identical to
&#96;N:S:V:C::A&#96;) &#42; and all combinations with &#96;/P&#96;

Missing fields &#42;&#42;SHOULD&#42;&#42; be populated with recommended
defaults:

Stream

:   defaults to the enabled or system default stream for the module in
    this particular order

Version

:   defaults to the latest available version in the module stream

Context

:   defaults to a value matching with already installed modules or
    modules involved in the transaction (not yet installed)

Arch

:   defaults to the system arch (e.g. DNF's \$basearch)

Profile

:   defaults to the system default or \'default\' profile

### Allowed Characters {#_allowed_characters}

&#42;&#42;N&#42;&#42; - Name

:   a-z A-Z 0-9 . - \_\

&#42;&#42;S&#42;&#42; - Stream

:   a-z A-Z 0-9 . - \_\

&#42;&#42;V&#42;&#42; - Version

:   0-9

&#42;&#42;C&#42;&#42; - Context

:   0-9 a-f

&#42;&#42;A&#42;&#42; - Arch

:   a-z A-Z 0-9 . - \_\

&#42;&#42;P&#42;&#42; - Profile

:   a-z A-Z 0-9 . - \_\

All fields &#42;&#42;MUST&#42;&#42; start and end with an alphanumeric
character: a-z A-Z 0-9

### Forbidden Characters {#_forbidden_characters}

This paragraph serves as a design decision for future changes.

Following characters &#42;&#42;MUST NOT&#42;&#42; be part of any field:

&#42; &#96;:&#96; (colon) - separator &#42; &#96;/&#96; (forward
slash) - profile separator &#42; &#96;\\&#96; (backslash) - comon
control character &#42; &#96;&#42;&#96; (asterisk) - common wildcard
&#42; &#96;?&#96; (question mark) - common wildcard &#42; &#96;@&#96;
(at) - grpspec in YUM and DNF &#42; &#96; &#96; (space) - common
separator

&#42; &#42;&#42;Other&#42;&#42; = References

:::: warning
::: title
:::

&#42;&#42;The Modularity project has been retired&#42;&#42; and there
are [no modules in Fedora 39 or
newer](https://fedoraproject.org/wiki/Changes/RetireModularity) or [in
EPEL](https://lists.fedoraproject.org/archives/list/epel-announce@lists.fedoraproject.org/thread/KA3JQUZW63A4V7OQ7ZVDFCM32EQUSOXH/).
This page is only retained for historical reference.
::::

[Module metadata definitions](https://github.com/fedora-modularity/libmodulemd/tree/main/yaml_specs)

:   A modulemd-packager format is used to define how to build a module.\
    A modulemd format, (a.k.a. modulemd-stream) is used to define the
    end result which is distributed to end user systems.\
    A modulemd-defaults is used to defined a default stream and default
    profiles.\
    A modulemd-obsoletes is used to define an end of life of a module
    and its replacement.\
    A modulemd-translaations is used to define localized descriptions of
    modules and other human-directed messages.

[General issue tracker for Modularity](https://pagure.io/modularity/issues)

:   General issues that are tracked here.

[Modularity on Pagure](https://pagure.io/group/modularity)

:   Pagure is the default place for most of our git repositories.

[Modularity on GitHub](https://github.com/fedora-modularity/)

:   GitHub is an alternative place for some of our repositories.

## Other teams and working groups {#_other_teams_and_working_groups}

[Modularity and SELinux](https://fedoraproject.org/wiki/SELinuxModularity)

:   Documents related to SELinux support in Modularity

# Modularity: History and Background {#_modularity_history_and_background}

:::: warning
::: title
:::

&#42;&#42;The Modularity project has been retired&#42;&#42; and there
are [no modules in Fedora 39 or
newer](https://fedoraproject.org/wiki/Changes/RetireModularity) or [in
EPEL](https://lists.fedoraproject.org/archives/list/epel-announce@lists.fedoraproject.org/thread/KA3JQUZW63A4V7OQ7ZVDFCM32EQUSOXH/).
This page is only retained for historical reference.
::::

Fedora Modularity is a new technology that tries to solve important and
complex user problems. From time to time other solutions are suggested
to solve these problems in different ways. Often those solutions fail to
address one or more intended use cases. These pages to enumerate these
cases in detail so as to serve as a common reference point for the
ongoing discussions.

It is important to note these are goals. There are numerous places where
the implementation of Modularity at the time of this writing is not yet
fully adherent to them.

## It's all about the apps! {#_its_all_about_the_apps}

Very few people install a Linux distribution for its own sake.
Ultimately, the goal is to "scratch a particular itch" that the user is
experiencing. The solutions may take many forms, but ultimately this
user wants to deploy some software that solves a problem for them.

This leads us to a classic problem that Linux distributions have faced:
the "Too Fast/Too Slow" problem. Linux distributions are traditionally
quite monolithic. The package collections they ship are generally
self-consistent, providing generally whatever the latest stable major
release of the software at the time of the distribution release. As the
release ages, it will receive bugfixes and enhancements, but usually
will remain on the same major version.

This is excellent for the maintainers of the distribution, because it
allows them to test that everything works together as a cohesive whole.
It means that there's one authoritative version to align to.

Users, on the other hand, are most concerned about solving their
problem. It matters less to them that the distribution is cohesive and
more that the tools they need are available to them.

The "Too Fast/Too Slow" problem is basically this: users want a solid,
stable, reliable, *unchanging* system. They want it to stay that way for
the life of their application. However, they also want their application
to run using the set of dependencies it was designed for. If that
doesn't happen to be the same version (newer or older) as the one
selected for the monolithic distribution, the user will now have to
resort to alternative means to get up and running. This may be as simple
as bundling a dependency or as drastic as selecting an entirely
different distribution that better fits their specific need.

## A little background {#_a_little_background}

One of the precursors to Fedora Modularity was [Software
Collections](https://www.softwarecollections.org/) (SCLs). This was a
first try at solving the Too Fast/Too Slow" problem in the Fedora/Red
Hat ecosystem. provides two basic advantages: *Parallel Availability*
and *Parallel Installability*.

*Parallel Availability* means that more than one major release of a
popular software project is available for installation. For example, the
"Developer Toolset" SCLs provide access to newer versions of GCC and its
related toolchain for building software. There are Python and Ruby SCLs
that provide assorted runtimes for those languages and so on.

*Parallel Installability* means that more than one major release of a
software project can be installed on the same userspace.

A few years back, the Product Management team inside Red Hat performed a
large-scale survey of customers and potential customers about the user
experience of Red Hat Enterprise Linux. In particular, they asked about
their level of satisfaction with the software available from the
enterprise distribution and their opinion on these Software Collections.

Perhaps unsurprisingly, the overwhelming majority of respondents were
thrilled to have supported versions of software beyond what had shipped
with the base operating system. What the survey team did come away with
that was an epiphany was that the respondents generally did not care
about the parallel installability of the SCLs. For the most part, they
maintained individual userspaces (using bare metal, traditional
virtualization or containers) for each of the applications they cared
about.

The most common problem reported for Software Collections was that using
them required changes to the applications they wanted to run. SCLs
install to a separate filesystem location from more traditional RPMs and
applications that rely on them need to know where to look for them. (In
SCL parlance, this is called "activating" the collection.)

The consequence of this relocation on disk is that users were unable to
take existing applications (either FOSS or proprietary) and simply use
them. Instead, they had to modify the projects to first activate the
collections. This was a consistent pain point.

Given this feedback, Red Hat came to the conclusion that parallel
installability, while nice to have, was not a critical user requirement.
Instead, the focus would be on the parallel *availability*. By dropping
this requirement, it became possible to create a solution that allowed
the different versions to be swapped in and take over the standard
locations on the disk.

## Meanwhile in Fedora {#_meanwhile_in_fedora}

Of course, it's not just Red Hat --- people in Fedora are also concerned
with solving this Too Fast / Too Slow problem for our users. Efforts
around this kicked off in seriousness with the [Fedora.next
initiative](https://fedoramagazine.org/fedora-present-and-future-a-fedora-next-2014-update-part-ii-whats-happening/)
and Fedora Project Leader Matthew Miller's
"[Rings](https://lwn.net/Articles/563395/)" talk at the first Flock
conference in 2013.

This led to the proposal and approval by the Fedora Council of the
[Modularity Prototype Fedora
Objective](https://fedoraproject.org/wiki/Objectives/Fedora_Modularization%2C_Prototype_Phase)
and its follow-up [Modularity Release Fedora
Objective](https://fedoraproject.org/wiki/Objectives/Fedora_Modularization_%E2%80%94_The_Release).

## Requirements and use cases {#_requirements_and_use_cases}

For more information on requirements and use cases, read on to the
[Modularity requirements and use cases](requirements.xml) page.

# Modularity: Requirements and use cases {#_modularity_requirements_and_use_cases}

:::: warning
::: title
:::

&#42;&#42;The Modularity project has been retired&#42;&#42; and there
are [no modules in Fedora 39 or
newer](https://fedoraproject.org/wiki/Changes/RetireModularity) or [in
EPEL](https://lists.fedoraproject.org/archives/list/epel-announce@lists.fedoraproject.org/thread/KA3JQUZW63A4V7OQ7ZVDFCM32EQUSOXH/).
This page is only retained for historical reference.
::::

If you haven't already read it, you should check out the first part of
this essay on the [history and background of modularity](history.xml).

## Critical use cases for consumers {#_critical_use_cases_for_consumers}

First and foremost, our primary driving goal is to make it easy for our
users to understand and interact with alternative software versions. In
any instance where choosing between the packager experience and the user
experience is in conflict, we elect to improve things for the user.

### Standard Locations {#_standard_locations}

In order to make deployment of users' applications simpler, we need to
make sure that software can be installed into the common, expected
locations on the system. This includes (but is not limited to):

&#42; Libraries must be installed to &#96;/usr/lib\[64\]&#96;. &#42;
Headers must be installed to &#96;/usr/include&#96;. &#42; Executables
must be installed to a location in the default system &#96;\$PATH&#96;
&#42; Other -devel functionality such as pkgconfig files must be
installed in their standard lookup locations. &#42; Installed services
may own a well-known DBUS address. &#42; Services may own the
appropriate standard TCP/UDP ports or local socket paths.

*Requirement*: Installation must occur in the same locations as
traditional RPM software delivery.

### Trust your containers {#_trust_your_containers}

As Linux containers grow more popular, the number of disreputable images
on container registries has also been rising. Delivering trustworthy
binaries to users is something that traditional distributions have
always done well. They provide assurance (in the form of signatures,
Secure Boot and other trusted delivery paths) that the software you're
running is the software you think it is.

*Requirement*: It must be possible for users to construct container
images based on Fedora content matching the software version they need
for their applications.

### Don't break the app! {#_dont_break_the_app}

It is very common for Fedora to update to the latest major version of
packages at each new semiannual release. This ensures that Fedora
remains at the leading edge of software development, but it can wreak
havoc on anyone trying to maintain a deployment on Fedora. If they are
running an app that is built for PostgreSQL 9.6 and Fedora switches to
carrying PostgreSQL 10 in the next major release, upgrading to that
release may break their app (possibly in ways undetectable by the
upgrade process).

However, staying on an old version of Fedora forever has its own
problems. Not least of these is the problem of security updates: Once a
release has been out for about 13 months, it stops receiving errata.
Moreover, new releases of the Fedora platform may have other useful
enhancements (better security defaults, increased performance thanks to
compiler improvements, etc.).

*Requirement*: We need to allow users to "lock" themselves onto certain
dependencies as long as the packager is maintaining them. These
dependencies must continue to receive updates.

*Requirement*: There must be appropriate and helpful UX for dealing with
when those dependencies go EOL.

### Support the developers {#_support_the_developers}

Developers often want to build their applications using the
latest-and-greatest version of their dependencies. However, that may not
have been released until after the most recent Fedora release. In
non-Modular Fedora, that means waiting up to six months to be able to
work on it there.

*Requirement*: It must be possible to gain access to newer software than
was available at the Fedora release GA.

Additionally, Dev/Ops people are rapidly switching to a new paradigm of
development and deployment (containers) to solve the above issue.
However, most containers today are retrieved from public repositories.
The public repositories are generally user-managed and have not been
verified and validated for security.

*Requirement*: Provide a mechanism for building &#42;trusted&#42;
container base and application images with content alternatives.

### Keep it updated {#_keep_it_updated}

It's not enough that other versions of software are available to
install. They also need to be kept up to date with bug fixes and
security updates. In non-Modular Fedora, users had the ability to force
DNF to lock to a specific RPM NEVRA, but they wouldn't get updates from
it.

*Requirement*: Alternative software must receive be able to recieve and
apply updates.

### Make it discoverable {#_make_it_discoverable}

Having alternative versions available is important but not sufficient.
It is also necessary for users to be able to locate these alternatives.
Some of our early explorations into this area failed this ease-of-use
test because they require the user to have knowledge of external sites
and then to search those sites for what they think they want.

*Requirement*: Users must be able to discover what alternative software
versions are available with tools that are shipped with the OS by
default. Ideally, these should be the same tools that they are already
comfortable with.

### Don't break existing package management workflows {#_dont_break_existing_package_management_workflows}

Users are slow to adapt to changes in the way they need to behave.
Requiring them to learn a new set of commands to interact with their
system will likely result in frustration and possibly exodus to other
distributions.

*Requirement*: It must remain possible to continue to operate with only
the package management commands used in traditional Fedora. We may
provide additional commands to support new functionality, but we must
not break the previous workflow.

*Requirement*: Existing automation tools such as anaconda's kickstart
and Ansible must continue to work.

## Critical use-cases for packagers {#_critical_use_cases_for_packagers}

### Dependencies {#_dependencies_2}

Because very little software today is wholly self-contained, it must be
possible for Modules to depend on each other.

*Requirement*: There must be a mechanism for packagers to explicitly
list dependencies on other software, including alternative versions.
This mechanism must support both build-time and run-time dependencies.

### Alternative dependencies {#_alternative_dependencies}

Some software is very restrictive about which dependencies it can work
with. Other software may work with several different major releases of a
dependency. For example, a user may ship two Ruby-based web
applications, one which is capable of running on Ruby 2.5 and the other
that can run on either Ruby 2.5 or Ruby 2.6. In non-modular Fedora, only
one version of Ruby would be available. If the system version was 2.5,
then both applications could run fine. But if in the next release of
Fedora the Ruby 2.6 release becomes the system copy, one of those
applications will have to be dropped (or patched) to work with it.

*Requirement*: It must be possible to build software that can be run
against multiple versions of its dependencies.

*Requirement*: The packaging process for creating software that supports
multiple versions of their dependencies must not be significantly more
difficult than packaging for a single dependency.

As more and more things become modules, there is concern that such
things will grow into an unbounded matrix. For this, we need to
establish policies on when the use of alternative dependencies is
preferable or when it is better to constrain it to a single version or
small set.

*Requirement*: Packaging guidelines need to provide advice on when to
use multiple alternative dependencies or to select a single one.

### Managing private dependencies {#_managing_private_dependencies}

When a person decides that they want Fedora to carry a particular
package and decides to do the work to accomplish this, it is not
uncommon to discover that the package they care about has additional
dependencies that are not yet packaged in Fedora. Traditionally, this
has meant that the packager has needed to package up those dependencies
and then continue to maintain them for anyone who may be using them for
other purposes. This can sometimes be a significant investment in time
and energy, all to support a package they don't necessarily care about
except for how it supports the primary package.

#### Build-time Dependencies {#_build_time_dependencies}

Sometimes, a package is needed only to build the software and is not
required at run-time. In such cases, Modularity should offer the ability
to keep those build-time dependencies entirely private and not exposed
to the Fedora Package Collection at large.

*Requirement*: Build-time only dependencies for an alternative version
may be excluded from the installable output artifacts. These excluded
artifacts may be preserved by the build-system for other purposes.

*Requirement*: All sources used for generating alternative versions,
regardless of final visibility, must be available to the community for
purposes of modification and reproducibility.

#### Defining the public API {#_defining_the_public_api}

Similarly, there are times when an application the packager cares about
depends on another package that is required at runtime, but sufficiently
complex that the packager would not want to maintain it for general use.
(For example, an application that links to a complicated library but
only uses a few functions.)

In this case, we want there to be a standard mechanism for the packager
to be able to indicate that some of the output artifacts are not
supported for use outside this module. If they are needed by others,
they should package it themselves and/or help maintain it in a shared
place.

*Requirement*: Packagers must be able to encode whether their output
artifacts are intended for use by other projects or if they are
effectively private to the alternative version. Packagers must also have
a way of finding this information out so they understand what they can
and cannot rely on as a dependency.

### Use-case-based installation {#_use_case_based_installation}

Since the earliest days of Linux, the "package" has been the fundamental
unit of installable software. If you want to have some functionality on
the system, you need to learn the name of the individual packages that
provide that functionality (not all of which are named obviously). As we
build modules, one of the goals is to try to focus installation around
use-cases rather than around upstream projects. A big piece of this is
that we want to have a way to install a subset of a module that supports
specific use-cases. A common example being "server" and "client" cases.

*Requirement*: It must be possible to install a subset of artifacts from
an alternative version. These installation groups should be easily
discoverable.

*Recommendation*: Installation groups should be named based on the
use-case they are intended to solve. This will provide a better user
experience.

### Lifecycle isolation {#_lifecycle_isolation}

Another of the major issues faced by Fedora is maintaining a release
schedule when all of the components within it follow vastly differing
schedules. There are two main aspects to this problem:

&#42; A major version of a popular piece of software is released just
after a Fedora release, so it doesn't land in Fedora for six months.
&#42; Some software does frequent major revisions (Django, Node.js,
etc.) and swapping them out every six months for the latest one means
that dependent projects are constantly needing to adapt to the new
breakage or find alternative mechanisms for retaining the older, working
version &#42; Some software does not handle multiple-version upgrades
(Nextcloud, for example). Attempting to go from version 15 to verison 19
requires first upgrading through 16, 17, and 18.

*Requirement*: It must be possible for new alternative versions of
software to become available to the Fedora Package Collection between
release dates.

*Requirement*: It must be possible for alternative versions of software
to go end-of-life during a Fedora release. This does not mean that the
software must disappear from the repositories, merely that an assertion
exists somewhere that after a certain date, the package will not receive
updates.

*Requirement*: For alternative versions whose lifecycle will continue
through at least part of the next Fedora release, it must be possible to
upgrade from one release to the next and remain with the
fully-compatible version.

### Third-party additions {#_third_party_additions}

Some third-party add-on repositories (particularly EPEL) have been
limited in the past by relying on the system copies of packages in the
base distribution of the release. In the particular case of EPEL, little
can be done to upgrade these system copies. In order to be able to
package much of the available FOSS software out there, it may be
necessary to override some of the content shipped in the base system
with packages known to work properly.

*Requirement*: It must be possible for third party repositories to
create alternative versions that override base distribution content at
the user's explicit choice.

*Requirement*: It must be possible for third party repositories to
create alternative versions of software that exist in the base
distribution.

### Reduce duplication in packaging work {#_reduce_duplication_in_packaging_work}

There is plenty of software out in the wild that maintains compatibility
over time and is therefore useful to carry in multiple releases of
Fedora. With traditional packaging, this means carrying and building
separate branches of the packages for each release of Fedora. In the
case of software "stacks" which are tightly bound, this means also
manually building each of its dependencies in each release of Fedora.

*Requirement*: It must be possible to build multiple component software
packages in the same build process.

*Requirement*: It must be possible for the packager to specify the order
in which packages must be built (and to indicate which ones can be built
in parallel).

*Requirement*: It must be possible to be build for all supported
platforms using the same specification and with a single build command.

## Non-Goals {#_non_goals}

### Parallel installability {#_parallel_installability}

As mentioned in the Background section, the goals of Modularity are
specifically to &#42;not&#42; implement parallel-installability. We
recommend instead that users should rely on other mechanisms such as
virtualization or containerization to accomplish this. If
parallel-installation is unavoidable, then Modularity is not the correct
tool for this job.

### Arbitrary stream switching {#_arbitrary_stream_switching}

Module streams are intended to be compatible update streams. That means
they must follow the same rules regarding RPM package-level updates
within the stream. By definition, two streams of the same module exist
because upgrades (or downgrades or cross-grades...) are not capable of
being done in a safe, automated fashion.

That does not mean that stream switching should be impossible, but it
does mean that we will not build any tools intended to handle such
switching in a generic manner. Stream switches should be handled on a
module-by-module basis and detailed instructions and/or tools written
for each such case.

[^1]: This ensures that the package in the module is being maintained by
    someone responsible for it.

[^2]: There are legal and licensing requirements for reproducibility of
    builds.

[^3]: As an example if non-modular Fedora has dnf 4, and there is module
    with dnf 5, a package that only works with dnf 5 can remain modular
    only, until dnf 5 is included in non-modular Fedora.

[^4]: This rule may be revised in the future, especially if the
    functionality of default streams is improved.

[^5]: It is highly recommended that default streams have no module
    dependencies besides the platform to avoid potential future
    conflicts during upgrades.

[^6]: This is so that if the maintainers of either module wishes to
    change its default stream, it is easy to see what other modules
    would be impacted and coordinate it.

[^7]: If a package is not filtered out from the default module stream,
    it is going to be part of the default-available content and
    therefore must be treated (and supported) just like a non-modular
    package.

[^8]: This ensures that all packages installable with &#96;dnf install
    package&#96; are fully supported as any non-modular package.

[^9]: This is an extension of the [stable updates
    policy](https://docs.fedoraproject.org/en-US/fesco/Updates_Policy/&#35;stable-releases).

[^10]: Modular packages shadow non-modular ones. This rule ensures that
    we don't have any shadowed packages in the default package set.

[^11]: In this situation, whichever has the highest NEVRA would win the
    depsolving and could break the other module.

[^12]: They &#42;MAY&#42; provide other well-known names in the same
    manner as permitted for non-modular content. For example, two
    different default streams &#42;MAY&#42; provide content to be used
    with the &#96;alternatives&#96; system or virtual &#96;Provides&#96;
    for capabilities.

[^13]: This feature allows for overriding the standard macros for
    building packages in Fedora and should be avoided entirely for
    default streams so they are built just like non-modular packages.
