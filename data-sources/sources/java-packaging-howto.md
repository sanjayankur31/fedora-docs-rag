# Manpages {#_manpages}

This section contains manpages for &#96;mvn\_&#42;&#96; and
&#96;pom\_&#42;&#96; macros.

# mvn_alias {#_mvn_alias}

# mvn_artifact {#_mvn_artifact}

# mvn_build {#_mvn_build}

# mvn_compat_version {#_mvn_compat_version}

# mvn_config {#_mvn_config}

# mvn_file {#_mvn_file}

# mvn_install {#_mvn_install}

# mvn_package {#_mvn_package}

# pom_add_dep {#_pom_add_dep}

# pom_add_parent {#_pom_add_parent}

# pom_add_plugin {#_pom_add_plugin}

# pom_change_dep {#_pom_change_dep}

# pom_disable_module {#_pom_disable_module}

# pom_remove_dep {#_pom_remove_dep}

# pom_remove_parent {#_pom_remove_parent}

# pom_remove_plugin {#_pom_remove_plugin}

# pom_set_parent {#_pom_set_parent}

# pom_xpath_disable {#_pom_xpath_disable}

# pom_xpath_inject {#_pom_xpath_inject}

# pom_xpath_remove {#_pom_xpath_remove}

# pom_xpath_replace {#_pom_xpath_replace}

# pom_xpath_set {#_pom_xpath_set}

# Ant {#_ant}

> Apache Ant is a Java library and command-line tool whose mission is to
> drive processes described in build files as targets and extension
> points dependent upon each other.
>
> ---  https://ant.apache.org/

Apache Ant is one of the most popular Java build tools after Apache
Maven. The main difference between these two tools is that Ant is
procedural and Maven is declarative. When using Ant, it is neccessary to
exactly describe the processes which lead to the result. It means that
one needs to specify where the source files are, what needs to be done
and when it needs to be done. On the other hand, Maven relies on
conventions and doesn't require specifying most of the process unless
you need to override the defaults.

If upstream ships a Maven POM file, it must be installed even if you
don't build with Maven. If not, you should try to search Maven Central
Repository for it, ship it as another source and install it.

:::: formalpara
::: title
Common spec file
:::

``` spec
BuildRequires: ant
BuildRequires: javapackages-local
\&#8230;
%build
ant test

%install
%mvn_artifact pom.xml lib/%{name}.jar

%mvn_install -J api/

%files -f .mfiles
%files javadoc -f .mfiles-javadoc
```
::::

<div>

::: title
Details
:::

- &#96;%build&#96; section uses &#96;ant&#96; command to build the
  project and run the tests. The used target(s) may vary depending on
  the &#96;build.xml&#96; file. You can use &#96;ant -p&#96; command to
  list the project info or manually look for &#96;&lt;target&gt;&#96;
  nodes in the &#96;build.xml&#96; file.

- &#96;%mvn_artifact&#96; macro is used to request installation of an
  artifact that was not built using Maven. It expects a POM file and a
  JAR file. For POM only artifacts, the JAR part is omitted. See
  &lt;&lt;\_installing_additional_artifacts&gt;&gt; for more
  information.

- &#96;%mvn_install&#96; performs the actual installation. Optional
  &#96;-J&#96; parameter requests installation of generated Javadoc from
  given directory.

- This method of artifact installation allows using other XMvn macros
  such as &#96;%mvn_alias&#96; or &#96;%mvn_package&#96;.

- &#96;%mvn_install&#96; generates &#96;.mfiles&#96; file which should
  be used to populate &#96;%files&#96; section with &#96;-f&#96; switch.
  For each subpackage there would be separate generated file named
  &#96;.mfiles-subpackage-name&#96;.

- All packages are required to own directories which they create (and
  which are not owned by other packages). JAR files are by default
  installed into subdirectory of &#96;%{\_javadir}&#96;. To override
  this behavior, use &#96;%mvn_file&#96;.

</div>

# Apache Ivy {#_apache_ivy}

Apache Ivy provides an automatic dependency management for Ant managed
builds. It uses Maven repositories for retrieving artifacts and supports
many declarative features of Maven such as handling transitive
dependencies.

XMvn supports local resolution of Ivy artifacts, their installation and
requires generation.

:::: formalpara
::: title
Spec file
:::

``` _spec
BuildRequires: ivy-local
\&#8230;
%build
ant -Divy.mode=local test

%install
%mvn_artifact ivy.xml lib/sample.jar

%mvn_install -J api/

%files -f .mfiles
%files -javadoc -f .mfiles-javadoc
```
::::

<div>

::: title
Details
:::

- &#96;-Divy.mode=local&#96; tells Ivy to use XMvn local artifact
  resolution instead of downloading from the Internet.

- If there is an &#96;ivy-settings.xml&#96; or similar file, which
  specifies remote repositories, it needs to be disabled, otherwise it
  would override local resolution.

- &#96;%mvn_artifact&#96; supports installing artifacts described by Ivy
  configuration files.

- &#96;%mvn_install&#96; performs the actual installation. Optional
  &#96;-J&#96; parameter requests installation of generated Javadoc from
  given directory.

</div>

:::: formalpara
::: title
Ivy files manipulation
:::

A subset of macros used to modify Maven POMs also work with
&#96;ivy.xml&#96; files allowing the maintainer to add / remove / change
dependencies without the need of making patches and rebasing them with
each change. You can use dependency handling macros
&#96;%pom_add_dep&#96;, &#96;%pom_remove_dep&#96;,
&#96;%pom_change_dep&#96; and generic &#96;%pom_xpath\_&#42;&#96;
macros. For more details, see corresponding manpages.
::::

``` spec
\&#35; Remove dependency on artifact with org='com.example' and
\&#35; name='java-project' from ivy.xml file in current directory
%pom_remove_dep com.example:java-project

\&#35; Add dependency on artifact with org='com.example' and
\&#35; name='foobar' to ./submodule/ivy.xml
%pom_add_dep com.example:foobar submodule
```

:::: formalpara
::: title
Using the &#96;ivy:publish&#96; task
:::

Ivy supports publishing built artifact with &#96;ivy:publish&#96; task.
If your &#96;build.xml&#96; file already contains a task that calls
&#96;ivy:publish&#96;, you can set the resolver attribute of the
&#96;ivy:publish&#96; element to &#96;xmvn&#96;. This can be done with
simple &#96;%pom_xpath_set&#96; call. Then when the task is run, XMvn
can pick the published artifacts and install them during the run of
&#96;%mvn_install&#96; without needing you to manually specify them with
&#96;%mvn_artifact&#96;.
::::

:::: formalpara
::: title
Spec file using the &#96;ivy:publish&#96; task
:::

``` spec
BuildRequires: ivy-local
\&#8230;
%prep
%pom_xpath_set ivy:publish/@resolver xmvn build.xml

%build
ant -Divy.mode=local test publish-local

%install
%mvn_install -J api/

%files -f .mfiles
%files -javadoc -f .mfiles-javadoc
```
::::

<div>

::: title
Details
:::

- The publish target may be named differently. Search the
  &#96;build.xml&#96; for occurences of &#96;ivy:publish&#96;.

- &#96;%mvn_install&#96; will install all the published artifacts. ==
  Common Errors This section contains explanations and
  solutions/workarounds for common errors which can be encountered
  during packaging.

</div>

# Missing dependency {#_missing_dependency}

    [ERROR] Failed to execute goal on project simplemaven:
    Could not resolve dependencies for project com.example:simplemaven:jar:1.0:
    The following artifacts could not be resolved: commons-io:commons-io:jar:2.4, junit:junit:jar:4.11:
    Cannot access central (http://repo.maven.apache.org/maven2) in offline mode and the artifact commons-io:commons-io:jar:2.4 has not been downloaded from it before. -\&gt; [Help 1]

Maven wasn't able to build project &#96;com.example:simplemaven&#96;
because it couldn't find some dependencies (in this case
&#96;commons-io:commons-io:jar:2.4&#96; and
&#96;junit:junit:jar:4.11&#96;)

You have multiple options here:

- If you suspect that a dependency is not necessary, you can remove it
  from &#96;pom.xml&#96; file and Maven will stop complaining about it.
  You can use wide variety of &lt;&lt;\_macros_for_pom_modification,
  macros&gt;&gt; for modifying POM files. The one for removing
  dependencies is called &lt;&lt;\_dependency_manipulation_macros,
  &#96;%pom_remove_dep&#96;&gt;&gt;.

- There is a mock plugin that can automate installation of missing
  dependencies. When you're using mock, pass additional
  &#96;\--enable-plugin pm_request&#96; argument and the build process
  would be able to install missing dependencies by itself. You still
  need to add the &#96;BuildRequires&#96; later, because you need to
  build the package in Koji, where the plugin is not allowed. You should
  do so using &#96;xmvn-builddep build.log&#96;, where
  &#96;build.log&#96; is the path to mock's build log. It will print a
  list of &#96;BuildRequires&#96; lines, which you can directly paste
  into the specfile. To verify that the &#96;BuildRequires&#96; you just
  added are correct, you can rebuild the package once more without the
  plugin enabled.

- Add the artifacts to &#96;BuildRequires&#96; manually. Maven packages
  have virtual provides in a format &#96;mvn(artifact coordinates)&#96;,
  where artifact coordinates are in the format which Maven used in the
  error message, but without version for non-compat packages (most of
  the packages you encounter). Virtual provides can be used directly in
  &#96;BuildRequires&#96;, so in this case it would be:

<!-- -->

    BuildRequires:  mvn(commons-io:commons-io)
    BuildRequires:  mvn(junit:junit)

# Compilation failure {#_compilation_failure}

    [ERROR] Failed to execute goal
    org.apache.maven.plugins:maven-compiler-plugin:3.1:compile (default-compile)
    on project simplemaven: Compilation failure: Compilation failure:
    [ERROR] /builddir/build/BUILD/simplemaven-1.0/src/main/java/com/example/Main.java:[3,29] package org.apache.commons.io does not exist
    [ERROR] /builddir/build/BUILD/simplemaven-1.0/src/main/java/com/example/Main.java:[8,9] cannot find symbol
    [ERROR] symbol:   class FileUtils
    [ERROR] location: class com.example.Main
    [ERROR]_-\&gt;_[Help_1]

Java compiler couldn't find given class on classpath or incompatible
version was present. This could be caused by following reasons:

- &#96;pom.xml&#96; requires different version of the Maven artifact
  than the local repository provides

- &#96;pom.xml&#96; is missing a necessary dependency

Different versions of same library may provide slightly different API.
This means that project doesn't have to be buildable if different
version is provided. If the library in local repository is older than
the one required by project, then the library could be updated. If the
project requires older version, then the project should be ported to
latest stable version of the library (this may require cooperation with
project's upstream). If none of these is possible from some reason, it
is still possible to introduce new &#96;compat&#96; package. See
&lt;&lt;\_compatibility_versions, compat packages&gt;&gt; section for
more information on this topic.

Sometimes &#96;pom.xml&#96; doesn't list all the necessary dependencies,
even if it should. Dependencies can also depend on some other and
typically all these will be available to the project which is being
built. The problem is that local repository may contain different
versions of these dependencies. And even if these versions are fully
compatible with the project, they may require slightly different set of
dependencies. This could lead to build failure if &#96;pom.xml&#96;
doesn't specify all necessary dependencies and relies on transitive
dependencies. Such a missing dependency may be considered a bug in the
project. The solution is to explicitly add missing dependency to the
&#96;pom.xml&#96;. This may be easily done by using
&#96;%pom_add_dep&#96; macro. See the section about
&lt;&lt;\_macros_for_pom_modification, macros for POM
modification&gt;&gt; for more information.

# Requires cannot be generated {#_requires_cannot_be_generated}

    Following dependencies were not resolved and requires cannot be generated.
    Either remove the dependency from pom.xml or add proper packages to
    BuildRequires: org.apache.maven.doxia:doxia-core::tests:UNKNOWN

Most often this error happens when one part of the package depends on an
attached artifact which is not being installed. Automatic RPM requires
generator then tries to generate requires on artifact which is not being
installed. This would most likely result in a broken RPM package so
generator halts the build.

There are usually two possible solutions for this problem:

- Install attached artifact in question. For the above error following
  macro would install artifacts with &#96;tests&#96; classifiers into
  &#96;tests&#96; subpackage.

<!-- -->

    %mvn_package :::tests: %{name}-tests

- Remove dependency on problematic artifact. This can involve
  &#96;pom.xml&#96; modifications, disabling tests or even code changes
  so it is usually easier to install the dependency.

# Dependencies with scope &#96;system&#96; {#_dependencies_with_scope_96system96}

    [ERROR] Failed to execute goal org.fedoraproject.xmvn:xmvn-mojo:1.2.0:install (default-cli) on project pom: Some reactor artifacts have dependencies with scope 'system'.
    Such dependencies are not supported by XMvn installer.
    You should either remove any dependencies with scope 'system' before the build or not run XMvn instaler. -\&gt; [Help 1]

Some Maven artifacts try to depend on exact system paths. Most usually
this dependency is either on &#96;com.sun:tools&#96; or
&#96;sun.jdk:jconsole&#96;. Dependencies with system scope cause issues
with our tooling and requires generators so they are not supported.

Easiest way to solve this for above two dependencies is by removing and
adding back the dependency without &#96;&lt;scope&gt;&#96; or
&#96;&lt;systemPath&gt;&#96; nodes:

    %pom_remove_dep com.sun:tools
    %pom_add_dep com.sun:tools

# Core Java packages {#_core_java_packages}

## JVM {#_jvm}

Fedora allows multiple Java Virtual Machines (JVMs) to be packaged
independently. Java packages should not directly depend on any
particulat JVM, but instead require one of three virtual JVM packages
depending of what Java funtionality is required.

&#42;&#96;java-headless&#96;&#42;

:   This package provides a working Java Runtime Environment (JRE) with
    some functionality disabled. Graphics and audio support may be
    unavailable in this case. &#96;java-headless&#96; provides
    functionality that is enough for most of packages and avoids pulling
    in a number of graphics and audio libraries as dependencies.
    Requirement on &#96;java-headless&#96; is appropriate for most of
    Java packages.

&#42;&#96;java&#96;&#42;

:   Includes the same base functionality as &#96;java-headless&#96;, but
    also implements audio and graphics subsystems. Packages should
    require &#96;java&#96; if they need some functionality from these
    subsystems, for example creating GUI using AWT library.

&#42;&#96;java-devel&#96;&#42;

:   Provides full Java Development Kit (JDK). In most cases only
    packages related to Java development should have runtime
    dependencies on &#96;java-devel&#96;. Runtime packages should
    require &#96;java-headless&#96; or &#96;java&#96;. Some packages not
    strictly related to java development need access to libraries
    included with JDK, but not with JRE (for example
    &#96;tools.jar&#96;). That is one of few cases where requiring
    &#96;java-devel&#96; may be necessary.

Packages that require minimal Java standard version can add versioned
dependencies on one of virtual packages providing Java environment. For
example if packages depending on functionality of JDK 8 can require
&#96;java-headless &gt;= 1:1.8.0&#96;.

:::: note
::: title
Epoch in versions of JVM packages
:::

For compatibility with JPackage project packages providing Java 1.6.0 or
later use epoch equal to &#96;1&#96;. This was necessary because package
&#96;java-1.5.0-ibm&#96; from JPackage project had epoch &#96;1&#96; for
some reason. Therefore packages providing other implementations of JVM
also had to use non-zero epoch in order to keep version ordering
correct.
::::

## Java Packages Tools {#_java_packages_tools}

Java Packages Tools are packaged as several binary RPM packages:

&#42;&#96;maven-local&#96;&#42;

:   This package provides a complete environment which is required to
    build Java packages using Apache Maven build system. This includes a
    default system version of Java Development Kit (JDK), Maven, a
    number of Maven plugins commonly used to build packages, various
    macros and utlilty tools. &#96;maven-local&#96; is usually declared
    as build dependency of Maven packages.

&#42;&#96;ivy-local&#96;&#42;

:   Analogously to &#96;maven-local&#96;, this package provides an
    environment required to build Java packages using Apache Ivy as
    dependency manager.

&#42;&#96;javapackages-local&#96;&#42;

:   Package providing a basic environment necessary to generate and
    install metadata for system artifact repository.

&#42;&#96;javapackages-tools&#96;&#42;

:   Package owning basic Java directories and providing runtime support
    for Java packages. The great majority of Java packages depend on
    &#96;javapackages-tools&#96;. === Dependency Handling

RPM has multiple types of metadata to describe dependency relationships
between packages. The two basic types are &#96;Requires&#96; and
&#96;Provides&#96;. &#96;Requires&#96; denote that a package needs
something to be present at runtime to work correctly and the package
manager is supposed to ensure that requires are met. A single
&#96;Requires&#96; item can specify a package or a virtual provide. RPM
&#96;Provides&#96; are a way to express that a package provides certain
capability that other packages might need. In case of Maven packages,
the &#96;Provides&#96; are used to denote that a package contains
certain Maven artifact. They add more flexibility to the dependency
management as single package can have any number of provides, and they
can be moved across different packages without breaking other packages\'
requires. &#96;Provides&#96; are usually generated by automatic tools
based on the information from the built binaries or package source.

:::: formalpara
::: title
Dependency handling for Maven packages
:::

The Java packaging tooling on Fedora provides automatic
&#96;Requires&#96; and &#96;Provides&#96; generation for packages built
using XMvn. The &#96;Provides&#96; are based on Maven artifact
coordinates of artifacts that were installed by the currently being
built. They are generated for each subpackage separately. They follow a
general format
&#96;mvn(groupId:artifactId:extension:classifier:version)&#96;, where
the extension is omitted if its &#96;jar&#96; and classifier is omitted
if empty. &#96;Version&#96; is present only for compat artifacts, but
the trailing colon has to be present unless it is a Jar artifact with no
classifier.
::::

``` shell
\&#35; Example provide for Jar artifact
mvn(org.eclipse.jetty:jetty-server)
\&#35; Example provide for POM artifact
mvn(org.eclipse.jetty:jetty-parent:pom:)
\&#35; Example provide for Jar artifact with classifier
mvn(org.sonatype.sisu:sisu-guice::no_aop:)
```

The generated Requires are based on dependencies specified in Maven POMs
in the project. Only dependencies with &#96;scope&#96; set to either
&#96;compile&#96;, &#96;runtime&#96; or not set at all are used for
Requires generation. Requires do not rely on package names and instead
always use virtual provides that were described above, in exactly the
same format, in order to be satisfiable by the already existing
provides. For packages consisting of multiple subpackages,
&#96;Requires&#96; are generated separately for each subpackage.
Additionally, &#96;Requires&#96; that point to an artifact in a
different subpackage of the same source package are generated with exact
versions to prevent version mismatches between artifacts belonging to
the same project.

The requires generator also always generates &#96;Requires&#96; on
&#96;java-headless&#96; and &#96;javapackages-tools&#96;.

:::: formalpara
::: title
Dependency handling for non-Maven packages that ship POM files
:::

If the package is built built using different tool than Apache Maven,
but still ships Maven POM(s), the you will still get automatic provides
generation if you install the POM using &#96;%mvn_artifact&#96; and
&#96;%mvn_install&#96;. The requires generation will also be executed
but the outcome largely depends on whether the POM contains accurate
dependency insformation. If it contains dependency information, you
should double-check that it is correct and up-to-date. Otherwise you
need to add &#96;Requires&#96; tags manually as described in the next
section.
::::

:::: formalpara
::: title
Dependency handling for non-Maven packages that don't ship POM files
:::

For packages without POMs it is necessary to specify &#96;Requires&#96;
tags manually. In order to build the package you needed to specify
&#96;BuildRequires&#96; tags. Your &#96;Requires&#96; tags will
therefore likely be a subset of your &#96;BuildRequires&#96;, excluding
build tools and test only dependencies.
::::

:::: formalpara
::: title
Querying Requires and Provides of built packages
:::

The generated Requires and Provides of built packages can be queried
using &#96;rpm&#96;:
::::

``` shell
rpm -qp --provides path/to/example-1.0.noarch.rpm
rpm -qp --requires path/to/example-1.0.noarch.rpm
```

:::: tip
::: title
:::

See also &lt;&lt;\_querying_repositories, Querying Fedora
repositories&gt;&gt;
::::

:::: formalpara
::: title
Generating BuildRequires
:::

While &#96;Requires&#96; and &#96;Provides&#96; generation is automated
for Maven projects, &#96;BuildRequires&#96; still remains a manual task.
However, there are tools to simplify it to some extent. XMvn ships a
script &#96;xmvn-builddep&#96; that takes a &#96;build.log&#96; output
from mock and prints Maven-style &#96;BuildRequires&#96; on artifacts
that were actually used during the build. It does not help you to figure
out what the &#96;BuildRequires&#96; are before you actually build it,
but it may help you to have a minimal set of &#96;BuildRequires&#96;
that are less likely to break, as they do not rely on transitive
dependencies. === Directory Layout This section describes most of
directories used for Java packaging. Each directory is named in RPM
macro form, which shows how it should be used in RPM spec files.
Symbolic name is followed by usual macro expansion (i.e. physical
directory location in the file system) and short description.
::::

&#96;%{\_javadir}&#96; --- &#96;/usr/share/java&#96;

Directory that holds all JAR files that do not contain or use native
code and do not depend on a particular Java standard version. JAR files
can either be placed directly in this directory or one of its
subdirectories. Often packages create their own subdirectories there, in
this case subdirectory name should match package name.

&#96;%{\_jnidir}&#96; --- &#96;/usr/lib/java&#96;

Directory where architecture-specific JAR files are installed. In
particular, JAR files containing or using native code (Java Native
Interface, JNI) should be installed there.

&#96;%{\_javadocdir}&#96; --- &#96;/usr/share/javadoc&#96;

Root directory where all Java API documentation (Javadoc) is installed.
Each source package usually creates a single subdirectory containing
aggregated Javadocs for all binary packages it produces.

&#96;%{\_mavenpomdir}&#96; --- &#96;/usr/share/maven-poms&#96;

Directory where Project Object Model (POM) files used by Apache Maven
are installed. Each POM must have name that strictly corresponds to JAR
file in &#96;%{\_javadir}&#96; or &#96;%{\_jnidir}&#96;.

&#96;%{\_ivyxmldir}&#96; --- &#96;/usr/share/ivy-xmls&#96;

Directory where &#96;ivy.xml&#96; files used by Apache Ivy are
installed. Each XML must have name that strictly corresponds to JAR file
in &#96;%{\_javadir}&#96; or &#96;%{\_jnidir}&#96;.

&#96;%{\_jvmdir}&#96; --- &#96;/usr/lib/jvm&#96;

Root directory where different Java Virtual Machines (JVM) are
installed. Each JVM creates a subdirectory, possibly with several
alternative names implemented with symbolic links. Directories prefixed
with &#96;java&#96; contain Java Development Kit (JDK), while
directories which names start with &#96;jre&#96; hold Java Runtime
Environment (JRE).

&#96;%{\_jvmsysconfdir}&#96; --- &#96;/etc/jvm&#96;

&#96;%{\_jvmcommonsysconfdir}&#96; --- &#96;/etc/jvm-common&#96;

Directories containing configuration files for Java Virtual Machines
(JVM).

&#96;%{\_jvmprivdir}&#96; --- &#96;/usr/lib/jvm-private&#96;

&#96;%{\_jvmlibdir}&#96; --- &#96;/usr/lib/jvm&#96;

&#96;%{\_jvmdatadir}&#96; --- &#96;/usr/share/jvm&#96;

&#96;%{\_jvmcommonlibdir}&#96; --- &#96;/usr/lib/jvm-common&#96;

&#96;%{\_jvmcommondatadir}&#96; --- &#96;/usr/share/jvm-common&#96;

Directories containing implementation files of Java Virtual Machines
(JVM). Describing them in detail is out of scope for this document.
Purpose of each directory is commented briefly in
&#96;macros.jpackage&#96; file in &#96;/etc/rpm&#96;. More detailed
description can be found in JPackage policy.

&#96;%{\_javaconfdir}&#96; --- &#96;/etc/java&#96;

Directory containing Java configuration files. In particular it contains
main Java configuration file --- &#96;java.conf&#96;. == Java Specifics
in Fedora for Packagers

# Java Specifics in Fedora for Users and Developers {#_java_specifics_in_fedora_for_users_and_developers}

This section contains information about default Java implementation in
Fedora, switching between different Java runtime environments and about
few useful tools which can be used during packaging / development.

# Java implementation in Fedora {#_java_implementation_in_fedora}

Fedora ships with an open-source reference implementation of Java
Standard Edition called [OpenJDK](https://openjdk.java.net/). OpenJDK
provides Java Runtime Environment for Java applications and set of
development tools for Java developers.

From users point of view, &#96;java&#96; command is probably the most
interesting. It is a Java application launcher which spawns Java Virtual
Machine (JVM), loads specified &#96;.class&#96; file and executes its
main method.

Here is an example how to run sample Java project from section
&lt;&lt;\_example_java_project&gt;&gt;:

``` shell
$ java org/fedoraproject/helloworld/HelloWorld.class
```

OpenJDK provides a lot of interesting tools for Java developers:

- &#96;javac&#96; is a Java compiler which translates source files to
  Java bytecode, which can be later interpreted by JVM.

- &#96;jdb&#96; is a simple command-line debugger for Java applications.

- &#96;javadoc&#96; is a tool for generating Javadoc documentation.

- &#96;javap&#96; can be used for disassembling Java class files.

## Switching between different Java implementations {#_switching_between_different_java_implementations}

Users and developers may want to have multiple Java environments
installed at the same time. It is possible in Fedora, but only one of
them can be default Java environment in system. Fedora uses
&#96;alternatives&#96; for switching between different installed
JREs/JDKs.

    \&#35; alternatives --config java

    There are 3 programs which provide 'java'.

    Selection    Command
    -----------------------------------------------
    1           java-17-openjdk.x86_64 (/usr/lib/jvm/java-17-openjdk-17.0.2.0.8-1.fc35.x86_64/bin/java)
    \&#42;+ 2           java-11-openjdk.x86_64 (/usr/lib/jvm/java-11-openjdk-11.0.14.1.1-5.fc35.x86_64/bin/java)
    3           java-latest-openjdk.x86_64 (/usr/lib/jvm/java-18-openjdk-18.0.1.0.10-1.rolling.fc35.x86_64/bin/java)

    Enter to keep the current selection[+], or type selection number:

Example above shows how to chose default Java environment.
&#96;java&#96; command will then point to the Java implementation
provided by given JRE.

:::: tip
::: title
:::

See &#96;man alternatives&#96; for more information on how to use
&#96;alternatives&#96;.
::::

Developers may want to use Java compiler from different JDK. This can be
achieved with &#96;alternatives \--config javac&#96;.

# Building classpath with &#96;build-classpath&#96; {#_building_classpath_with_96build_classpath96}

Most of the Java application needs to specify classpath in order to work
correctly. Fedora contains several tools which make working with
classpaths easier.

&#96;build-classpath&#96; - this tool takes JAR filenames or artifact
coordinates as arguments and translates them to classpath-like string.
See the following example:

``` shell
$ build-classpath log4j junit org.ow2.asm:asm
/usr/share/java/log4j.jar:/usr/share/java/junit.jar:/usr/share/java/objectweb-asm4/asm.jar
```

&#96;log4j&#96; corresponds to &#96;log4j.jar&#96; stored in
&#96;%{\_javadir}&#96;. If the JAR file is stored in subdirectory under
&#96;%{\_javadir}&#96;, it is neccessary to pass
&#96;subdirectory/jarname&#96; as an argument to
&#96;build-classpath&#96;. Example:

``` shell
$ build-classpath httpcomponents/httpclient.jar
/usr/share/java/httpcomponents/httpclient.jar
```

# Building JAR repository with &#96;build-jar-repository&#96; {#_building_jar_repository_with_96build_jar_repository96}

Another tool is &#96;build-jar-repository&#96;. It can fill specified
directory with symbolic / hard links to specified JAR files. Similarly
to &#96;build-classpath&#96;, JARs can be identified by their names or
artifact coordintes.

``` shell
$ build-jar-repository my-repo log4j httpcomponents/httpclient junit:junit
$ ls -l my-repo/
total 0
lrwxrwxrwx. 1 msrb msrb 45 Oct 29 10:39 [httpcomponents][httpclient].jar -\&gt; /usr/share/java/httpcomponents/httpclient.jar
lrwxrwxrwx. 1 msrb msrb 25 Oct 29 10:39 [junit:junit].jar -\&gt; /usr/share/java/junit.jar
lrwxrwxrwx. 1 msrb msrb 25 Oct 29 10:39 [log4j].jar -\&gt; /usr/share/java/log4j.jar
```

Similar command &#96;rebuild-jar-repository&#96; can be used to rebuild
JAR repository previously built by &#96;build-jar-repository&#96;. See
&#96;man rebuild-jar-repository&#96; for more information.

&#96;build-classpath-directory&#96; is a small tool which can be used to
build classpath string from specified directory.

``` shell
$ build-classpath-directory /usr/share/java/xstream
/usr/share/java/xstream/xstream-benchmark.jar:/usr/share/java/xstream/xstream.jar
:/usr/share/java/xstream/xstream-hibernate.jar
```

# Generic Java Builds {#_generic_java_builds}

This chapter talks about basic build steps in Java such as invoking
&#96;javac&#96; and using spec macros like &#96;build-claspath&#96; and
&#96;build-jar-repository&#96;.

# Generating Application Shell Scripts {#_generating_application_shell_scripts}

As mentioned in section about &lt;&lt;\_for_packagers, Java packaging
basics&gt;&gt;, all Java applications need wrapper shell scripts to
setup the environment before running JVM and associated Java code.

The &#96;javapackages-tools&#96; package contains a convenience
&#96;%jpackage_script&#96; macro that can be used to create scripts that
work for the majority of packages. See its definition and documentation
in &#96;/usr/lib/rpm/macros.d/macros.jpackage&#96;. One thing to pay
attention to is the 6th argument to it - whether to prefer a JRE over a
full SDK when looking up a JVM to invoke. Most packages that do not
require the full Java SDK will want to set that to &#96;true&#96; to
avoid unexpected results when looking up a JVM when some of the
installed JREs do not have the corresponding SDK (&#96;&#42;-devel&#96;
package) installed.

``` spec
%install
\&#8230;
%jpackage_script msv.textui.Driver '' '' msv-msv:msv-xsdlib:relaxngDatatype:isorelax msv true
\&#8230;
```

The previous example installs the &#96;msv&#96; script (5th argument)
with main class being &#96;msv.textui.Driver&#96; (1st argument). No
optional flags (2nd argument) or options (3rd argument) are used. This
script will add several libraries to classpath before executing main
class (4th argument, JAR files separated with &#96;:&#96;).
&#96;build-classpath&#96; is run on every part of 4th argument to create
full classpaths.

# Replacing JARs with symlinks using &#96;xmvn-subst&#96; {#_replacing_jars_with_symlinks_using_96xmvn_subst96}

Sometimes it may be needed to replace all JAR files in current directory
with symlinks to the system JARs located in &#96;%{\_javadir}&#96;. This
task can be achieved using tool called &#96;xmvn-subst&#96;.

``` shell
$ ls -l
-rw-r--r--. 1 msrb msrb  40817 Oct 22 09:16 cli.jar
-rw-r--r--. 1 msrb msrb 289983 Oct 22 09:17 junit4.jar
-rw-r--r--. 1 msrb msrb 474276 Oct 22 09:14 log4j.jar
$ xmvn-subst .
[INFO] Linked ./cli.jar to /usr/share/java/commons-cli.jar
[INFO] Linked ./log4j.jar to /usr/share/java/log4j.jar
[INFO] Linked ./junit4.jar to /usr/share/java/junit.jar
$ ls -la
lrwxrwxrwx. 1 msrb msrb   22 Oct 22 10:08 cli.jar -\&gt; /usr/share/java/commons-cli.jar
lrwxrwxrwx. 1 msrb msrb   22 Oct 22 10:08 junit4.jar -\&gt; /usr/share/java/junit.jar
lrwxrwxrwx. 1 msrb msrb   22 Oct 22 10:08 log4j.jar -\&gt; /usr/share/java/log4j.jar
```

The example above shows how easy the symlinking can be. However, there
are some limitations. Original JAR files need to carry metadata which
tell &#96;xmvn-subst&#96; for what artifact given file should be
substituted. Otherwise &#96;xmvn-subst&#96; won't be able to identify
the Maven artifact from JAR file.

:::: tip
::: title
:::

See &#96;xmvn-subst -h&#96; for all available options.
::::

# Integration of Maven and XMvn Tools {#_integration_of_maven_and_xmvn_tools}

Describe common usage patterns of XMvn, xmvn-bisect and other tools with
links to upstream documentation where it makes sense

TODO - write content

# Introduction {#_introduction}

Clean Java packaging has historically been a daunting task. Lack of any
standard addressing the physical location of files on the system
combined with the common use of licensing terms that only allow free
redistribution of key components as a part of a greater ensemble has let
to the systematic release of self-sufficient applications with built-in
copies of external components.

As a consequence applications are only tested with the versions of the
components they bundle, a complete Java system suffers from endless
duplication of the same modules, and integrating multiple parts can be a
nightmare since they are bound to depend on the same elements - only
with different and subtly incompatible versions (different requirements,
different bugs). Any security or compatibility upgrade must be performed
for each of those duplicated elements.

This problem is compounded by the current practice of folding extensions
in the JVM itself after a while; an element that could safely be
embedded in a application will suddenly conflict with a JVM part and
cause subtle failures.

It is not surprising then that complex Java systems tend to fossilize
very quickly, with the cost of maintaining dependencies current growing
too high so fast people basically give up on it.

This situation is incompatible with typical fast-evolving Linux
platform. To attain the aim of user- and administrator-friendly RPM
packaging of Java applications a custom infrastructure and strict
packaging rules had to be evolved.

# Basic introduction to packaging, reasons, problems, rationale {#_basic_introduction_to_packaging_reasons_problems_rationale}

This section includes basic introduction to Java packaging world to
people coming from different backgrounds. The goal is to understand
language of all groups involved. If you are a Java developer coming into
contact with RPM packaging for the first time start reading
&lt;&lt;\_for_java_developers, Java developer&gt;&gt; section. On the
other hand if you are coming from RPM packaging background an
&lt;&lt;\_for_packagers, introduction to Java world&gt;&gt; is probably
a better starting point.

It should be noted that especially in this section we might sacrifice
correctness for simplicity. === For Java Developers Packaging Java
software has specifics which we will try to cover in this section aimed
at Java developers who are already familiar with Java language, JVM,
classpath handling, Maven, &#96;pom.xml&#96; file structure and
dependencies.

Instead we will focus on basic packaging tools and relationships between
Java and RPM world. One of the most important questions is: What is the
reason to package software in RPM (or other distribution-specific
formats). There are several reasons for it, among others:

- Unified way of installation of software for users of distribution
  regardless of upstream projects

- Verification of authenticity of software packages by signing them

- Simplified software updates

- Automatic handling of dependencies for users

- Common filesystem layout across distribution enforced by packaging
  standards

- Ability to administer, monitor and query packages installed on several
  machines through unified interfaces

- Distribution of additional metadata with the software itself such as
  licenses used, homepage for the project, changelogs and other
  information that users or administrators can find useful

## Example RPM Project {#_example_rpm_project}

RPM uses &#96;spec&#96; files as recipes for building software packages.
We will use it to package example project created in previous section.
If you did not read it you do not need to; the file listing is available
here and the rest is not necessary for this section.

:::: formalpara
::: title
Directory listing
:::

``` shell
Makefile
src
src/org
src/org/fedoraproject
src/org/fedoraproject/helloworld
src/org/fedoraproject/helloworld/output
src/org/fedoraproject/helloworld/output/Output.java
src/org/fedoraproject/helloworld/input
src/org/fedoraproject/helloworld/input/Input.java
src/org/fedoraproject/helloworld/HelloWorld.java
```
::::

We packed the project directory into file &#96;helloworld.tar.gz&#96;.

\[&#35;helloworld_spec\] .Example spec file

``` {.rpmspec .numberLines}
```

RPM &#96;spec&#96; files contain several basic sections:

Header, which contains:

:   &#42; Package metadata such as its name, version, release, license,
    &#8230; &#42; A &#96;Summary&#96; with basic one-line summary of
    package contents. &#42; Package source URLs denoted with
    &#96;Source0&#96; to &#96;SourceN&#96; directives. &#42;&#42; Source
    files can then be referenced by &#96;%SOURCE0&#96; to
    &#96;%SOURCEn&#96;, which expand to actual paths to given files.
    &#42;&#42; In practice, the source URL shouldn't point to a file in
    our filesystem, but to an upstream release on the web. &#42;
    Patches - using &#96;Patch0&#96; to &#96;PatchN&#96;. &#42; Project
    dependencies. &#42;&#42; Build dependencies specified by
    &#96;BuildRequires&#96;, which need to be determined manually.
    &#42;&#42; Run time dependencies will be detected automatically. If
    it fails, you have to specify them with &#96;Requires&#96;.
    &#42;&#42; More information on this topic can be found in the
    &lt;&lt;\_dependency_handling, dependency handling&gt;&gt; section.

&#96;%description&#96;

:   &#42; Few sentences about the project and its uses. It will be
    displayed by package management software.

&#96;%prep&#96; section

:   &#42; Unpacks the sources using &#96;setup -q&#96; or manually if
    needed. &#42; If a source file doesn't need to be extracted, it can
    be copied to build directory by &#96;cp -p %SOURCE0 .&#96;. &#42;
    Apply patches with &#96;%patch X&#96;, where &#96;X&#96; is the
    number of patch you want to apply. (You usually need the patch
    index, so it would be: &#96;%patch 0 -p1&#96;).

&#96;%build&#96; section

:   &#42; Contains project compilation instructions. Usually consists of
    calling the projects build system such as Ant, Maven or Make.

Optional &#96;%check&#96; section

:   &#42; Runs projects integration tests. Unit test are usually run in
    &#96;%build&#96; section, so if there are no integration tests
    available, this section is omitted.

&#96;%install&#96; section

:   &#42; Copies built files that are supposed to be installed into
    &#96;%{buildroot}&#96; directory, which represents target
    filesystem's root.

&#96;%files&#96; section

:   &#42; Lists all files, that should be installed from
    &#96;%{buildroot}&#96; to target system. &#42; Documentation files
    are prefixed by &#96;%doc&#96; and are taken from build directory
    instead of buildroot. &#42; Directories that this package should own
    are prefixed with &#96;%dir&#96;.

&#96;%changelog&#96;

:   &#42; Contains changes to this spec file (not upstream). &#42; Has
    prescribed format. To prevent mistakes in format, it is advised to
    use tool such as &#96;rpmdev-bumpspec&#96; from package rpmdevtools
    to append new changelog entries instead of editing it by hand.

To build RPM from &lt;&lt;helloworld_spec, this &#96;spec&#96;
file&gt;&gt; save it in your current directory and run
&#96;rpmbuild&#96;:

``` shell
$ rpmbuild -bb helloworld.spec
```

If everything worked OK, this should produce RPM file
&#96;\~/rpmbuild/RPMS/x86_64/helloworld-1.0-1.fc18.x86_64.rpm&#96;. You
can use &#96;rpm -i&#96; or &#96;dnf install&#96; commands to install
this package and it will add &#96;/usr/share/java/helloworld.jar&#96;
and &#96;/usr/bin/helloworld&#96; wrapper script to your system. Please
note that this specfile is simplified and lacks some additional parts,
such as license installation.

:::: note
::: title
:::

Paths and filenames might be slightly different depending on your
architecture and distribution. Output of the commands will tell you
exact paths.
::::

As you can see to build RPM files you can use &#96;rpmbuild&#96;
command. It has several other options, which we will cover later on.

Other than building binary RPMs (&#96;-bb&#96;), &#96;rpmbuild&#96; can
also be used to:

- build only source RPMs (SRPMs), the packages containing source files
  which can be later build to RPMs (option &#96;-bs&#96;)

- build all, both binary and source RPMs (option &#96;-ba&#96;)

See &#96;rpmbuild&#96; \'s manual page for all available options.

## Querying repositories {#_querying_repositories}

Fedora comes with several useful tools which can provide great
assistance in getting information from RPM repositories.

&#96;dnf repoquery&#96; is a tool for querying information from RPM
repositories. Maintainers of Java packages might typically query the
repository for information like \'which package contains the Maven
artifact &#96;&#96;groupId:artifactId&#96;&#96;\'.

:::: formalpara
::: title
Find out which package provides given artifact
:::

``` shell
$ dnf repoquery --whatprovides 'mvn(commons-io:commons-io)'
apache-commons-io-1:2.4-9.fc19.noarch
```
::::

The example above shows that one can get to
&#96;commons-io:commons-io&#96; artifact by installing
&#96;apache-commons-io&#96; package.

By default, &#96;dnf repoquery&#96; uses all enabled repositories in DNF
configuration, but it is possible to explicitly specify any other
repository. For example following command will query only Rawhide
repository:

``` shell
$ dnf repoquery --available --disablerepo \\&#42; --enablerepo rawhide --whatprovides 'mvn(commons-io:commons-io)'
apache-commons-io-1:2.4-10.fc20.noarch
```

Sometimes it may be useful to just list all the artifacts provided by
given package:

``` shell
$ dnf repoquery --provides apache-commons-io
apache-commons-io = 1:2.4-9.fc19
jakarta-commons-io = 1:2.4-9.fc19
mvn(commons-io:commons-io) = 2.4
mvn(org.apache.commons:commons-io) = 2.4
osgi(org.apache.commons.io) = 2.4.0
```

Output above means that package &#96;apache-commons-io&#96; provides two
Maven artifacts: previously mentioned &#96;commons-io:commons-io&#96;
and &#96;org.apache.commons:commons-io&#96;. In this case the second one
is just an alias for same JAR file. See section about &lt;&lt;\_aliases,
artifact aliases&gt;&gt; for more information on this topic.

Another useful tool is &#96;rpm&#96;. It can do a lot of stuff, but most
importantly it can replace &#96;dnf repoquery&#96; if one only needs to
query local RPM database. Only installed packages, or local
&#96;.rpm&#96; files, can be queried with this tool.

Common use case could be checking which Maven artifacts provide locally
built packages.

``` shell
$ rpm -qp --provides simplemaven-1.0-2.fc21.noarch.rpm
mvn(com.example:simplemaven) = 1.0
mvn(simplemaven:simplemaven) = 1.0
simplemaven = 1.0-2.fc21
```

## Quiz for Java Developers {#_quiz_for_java_developers}

1.  How would you build a binary RPM if you were given a source RPM?

2.  What is most common content of &#96;Source0&#96; &#96;spec&#96; file
    tag?

3.  What is the difference between &#96;Version&#96; and
    &#96;Release&#96; tags?

4.  How would you apply a patch in RPM?

5.  Where on filesystem should JAR files go?

6.  What is the format of RPM changelog or what tool would you use to
    produce it?

7.  How would you install an application that needs certain layout
    (think &#96;ANT_HOME&#96;) while honoring distribution filesystem
    layout guidelines?

8.  How would you generate script for running a application with main
    class &#96;org.project.MainClass&#96; which depends on
    &#96;commons-lang&#96; jar? === For Packagers Java is a programming
    language which is usually compiled into bytecode for JVM (Java
    Virtual Machine). For more details about the JVM and bytecode
    specification see [JVM
    documentation](http://docs.oracle.com/javase/specs/jvms/se8/html/index.html).

## Example Java Project {#_example_java_project}

To better illustrate various parts of Java packaging we will dissect
simple Java &#96;Hello world&#96; application. Java sources are usually
organized using directory hierarchies. Shared directory hierarchy
creates a namespace called &#96;package&#96; in Java terminology. To
understand naming mechanisms of Java &#96;packages&#96; see [Java
package naming
conventions](http://docs.oracle.com/javase/tutorial/java/package/namingpkgs.html).

Let's create a simple hello world application that will execute
following steps when run:

1.  Ask for a name.

2.  Print out &#96;Hello World from&#96; and the name from previous
    step.

To illustrate certain points we artificially complicate things by
creating:

- &#96;Input&#96; class used only for input of text from terminal.

- &#96;Output&#96; class used only for output on terminal.

- &#96;HelloWorldApp&#96; class used as main application.

:::: formalpara
::: title
Directory listing of example project
:::

``` shell
$ find .
.
./Makefile
./src
./src/org
./src/org/fedoraproject
./src/org/fedoraproject/helloworld
./src/org/fedoraproject/helloworld/output
./src/org/fedoraproject/helloworld/output/Output.java
./src/org/fedoraproject/helloworld/input
./src/org/fedoraproject/helloworld/input/Input.java
./src/org/fedoraproject/helloworld/HelloWorld.java
```
::::

In this project all packages are under &#96;src/&#96; directory
hierarchy.

:::: formalpara
::: title
HelloWorld.java listing
:::

``` java
```
::::

:::: formalpara
::: title
Java packages
:::

``` shell
org/fedoraproject/helloworld/input/Input.java
org/fedoraproject/helloworld/output/Output.java
org/fedoraproject/helloworld/HelloWorld.java
```
::::

Although the directory structure of our package is hierarchical, there
is no real parent-child relationship between packages. Each package is
therefore seen as independent. The above example makes use of three
separate packages:

- &#96;org.fedoraproject.helloworld.input&#96;

- &#96;org.fedoraproject.helloworld.output&#96;

- &#96;org.fedoraproject.helloworld&#96;

Environment setup consists of two main parts:

- Telling JVM which Java class contains &#96;main()&#96; method.

- Adding required JAR files on JVM classpath.

:::: formalpara
::: title
Compiling our project
:::

The sample project can be compiled to a bytecode by Java compiler. Java
compiler can be typically invoked from command line by command
&#96;javac&#96;.
::::

``` shell
javac $(find -name '\&#42;.java')
```

For every &#96;.java&#96; file corresponding &#96;.class&#96; file will
be created. The &#96;.class&#96; files contain Java bytecode which is
meant to be executed on JVM.

One could put invocation of &#96;javac&#96; to Makefile and simplify the
compilation a bit. It might be sufficient for such a simple project, but
it would quickly become hard to build more complex projects with this
approach. Java world knows several high-level build systems which can
highly simplify building of Java projects. Among others, probably the
most known are [Apache Maven](https://maven.apache.org/) and [Apache
Ant](https://ant.apache.org/).

:::: tip
::: title
:::

See also &lt;&lt;\_maven&gt;&gt; and &lt;&lt;\_ant&gt;&gt; sections.
::::

:::: formalpara
::: title
JAR files
:::

Having our application split across many &#96;.class&#96; files would
not be very practical, so those &#96;.class&#96; files are assembled
into ZIP files with specific layout and called JAR files. Most commonly
these special ZIP files have &#96;.jar&#96; suffix, but other variations
exist (&#96;.war&#96;, &#96;.ear&#96;). They contain:
::::

- Compiled bytecode of our project.

- Additional metadata stored in &#96;META-INF/MANIFEST.MF&#96; file.

- Resource files such as images or localisation data.

- Optionaly the source code of our project (called source JAR then).

They can also contain additional bundled software which is something we
do not want to have in packages. You can inspect the contents of given
JAR file by extracting it. That can be done with following command:

``` shell
jar -xf something.jar
```

The detailed description of JAR file format is in the [JAR File
Specification](https://docs.oracle.com/javase/8/docs/technotes/guides/jar/jar.html).

:::: formalpara
::: title
Classpath
:::

The classpath is a way of telling JVM where to look for user classes and
3rd party libraries. By default, only current directory is searched, all
other locations need to be specified explicitly by setting up
&#96;CLASSPATH&#96; environment variable, or via &#96;-cp&#96;
(&#96;-classpath&#96;) option of the Java Virtual Machine.
::::

:::: formalpara
::: title
Setting the classpath
:::

``` shell
java -cp /usr/share/java/log4j.jar:/usr/share/java/junit.jar mypackage/MyClass.class
CLASSPATH=/usr/share/java/log4j.jar:/usr/share/java/junit.jar java mypackage/MyClass.class
```
::::

Please note that two JAR files are separated by colon in a classpath
definition.

:::: tip
::: title
:::

See [official
documentation](https://docs.oracle.com/javase/8/docs/technotes/tools/windows/classpath.html)
for more information about classpath.
::::

:::: formalpara
::: title
Wrapper scripts
:::

Classic compiled applications use dynamic linker to find dependencies
(linked libraries), whereas dynamic languages such as Python, Ruby, Lua
have predefined directories where they search for imported modules. JVM
itself has no embedded knowledge of installation paths and thus no
automatic way to resolve dependencies of Java projects. This means that
all Java applications have to use wrapper shell scripts to setup the
environment before invoking the JVM and running the application itself.
Note that this is not necessary for libraries.
::::

## Build System Identification {#_build_system_identification}

The build system used by upstream can be usually identified by looking
at their configuration files, which reside in project directory
structure, usually in its root or in specialized directories with names
such as &#96;build&#96; or &#96;make&#96;.

:::: formalpara
::: title
Maven
:::

Build managed by Apache Maven is configured by an XML file that is by
default named &#96;pom.xml&#96;. In its simpler form it usually looks
like this:
::::

``` _xml
\&lt;project xmlns='http://maven.apache.org/POM/4.0.0'
xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance'
xsi:schemaLocation='http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd'\&gt;
\&lt;modelVersion\&gt;4.0.0\&lt;/modelVersion\&gt;
\&lt;groupId\&gt;com.example.myproject\&lt;/groupId\&gt;
\&lt;artifactId\&gt;myproject\&lt;/artifactId\&gt;
\&lt;packaging\&gt;jar\&lt;/packaging\&gt;
\&lt;version\&gt;1.0\&lt;/version\&gt;
\&lt;name\&gt;myproject\&lt;/name\&gt;
\&lt;dependencies\&gt;
\&lt;dependency\&gt;
\&lt;groupId\&gt;junit\&lt;/groupId\&gt;
\&lt;artifactId\&gt;junit\&lt;/artifactId\&gt;
\&lt;version\&gt;4.1\&lt;/version\&gt;
\&lt;scope\&gt;test\&lt;/scope\&gt;
\&lt;/dependency\&gt;
\&lt;/dependencies\&gt;
\&lt;/project\&gt;
```

It describes project's build process in a declarative way, without
explicitly specifying exact steps needed to compile sources and assemble
pieces together. It also specifies project's dependencies which are
usually the main point of interest for packagers. Another important
feature of Maven that packagers should know about are plugins. Plugins
extend Maven with some particular functionality, but unfortunately some
of them may get in the way of packaging and need to be altered or
removed. There are RPM macros provided to facilitate modifying Maven
dependencies and plugins.

:::: formalpara
::: title
Ant
:::

Apache Ant is also configured by an XML file. It is by convention named
&#96;build.xml&#96; and in its simple form it looks like this:
::::

``` _xml
\&lt;project name='MyProject' default='dist' basedir='.'\&gt;
\&lt;property name='src' location='src'/\&gt;
\&lt;property name='build' location='build'/\&gt;
\&lt;property name='dist' location='dist'/\&gt;

\&lt;target name='init' description='Create build directory'\&gt;
\&lt;mkdir dir='${build}'/\&gt;
\&lt;/target\&gt;

\&lt;target name='compile' depends='init'
description='Compile the source'\&gt;
\&lt;javac srcdir='${src}' destdir='${build}'/\&gt;
\&lt;/target\&gt;

\&lt;target name='dist' depends='compile'
description='Generate jar'\&gt;
\&lt;mkdir dir='${dist}/lib'/\&gt;

\&lt;jar jarfile='${dist}/myproject.jar' basedir='${build}'/\&gt;
\&lt;/target\&gt;

\&lt;target name='clean' description='Clean build files'\&gt;
\&lt;delete dir='${build}'/\&gt;
\&lt;delete dir='${dist}'/\&gt;
\&lt;/target\&gt;
\&lt;/project\&gt;
```

Ant build file consists mostly of targets, which are collections of
steps needed to accomplish intended task. They usually depend on each
other and are generally similar to Makefile targets. Available targets
can be listed by invoking &#96;ant -p&#96; in project directory
containing &#96;build.xml&#96; file. If the file is named differently
than &#96;build.xml&#96; you have to tell Ant which file should be used
by using &#96;-f&#96; option with the name of the actual build file.

Some projects that use Apache Ant also use Apache Ivy to simplify
dependency handling. Ivy is capable of resolving and downloading
artifacts from Maven repositories which are declaratively described in
XML. Project usually contains one or more &#96;ivy.xml&#96; files
specifying the module Maven coordinates and its dependencies. Ivy can
also be used directly from Ant build files. To detect whether the
project you wish to package is using Apache Ivy, look for files named
&#96;ivy.xml&#96; or nodes in the &#96;ivy&#96; namespace in project's
build file.

:::: formalpara
::: title
Make
:::

While unlikely, it is still possible that you encounter a project whose
build is managed by plain old Makefiles. They contain a list of targets
which consist of commands (marked with tab at the begining of line) and
are invoked by &#96;make&#96; *target* or simply &#96;make&#96; to run
the default target.
::::

## Quiz for Packagers {#_quiz_for_packagers}

At this point you should have enough knowledge about Java to start
packaging. If you are not able to answer following questions return back
to previous sections or ask experienced packagers for different
explanations of given topics.

1.  What is the difference between JVM and Java?

2.  What is a &#96;CLASSPATH&#96; environment variable and how can you
    use it?

3.  Name two typical Java build systems and how you can identify which
    one is being used

4.  What is the difference between &#96;java&#96; and &#96;javac&#96;
    comands?

5.  What are contents of a typical &#96;JAR&#96; file?

6.  What is a &#96;pom.xml&#96; file and what information it contains?

7.  How would you handle packaging software that contains
    &#96;lib/junit4.jar&#96; inside source tarball?

8.  Name at least three methods for bundling code in Java projects ===
    JAR File Identification Complex Java applications usually consist of
    multiple components. Each component can have multiple
    implementations, called *artifacts*. Artifacts in Java context are
    *usually* JAR files, but can also be WAR files or any other kind of
    file.

There are multiple incompatible ways of identifying (naming) Java
artifacts and each build system often encourages usage of specific
naming scheme. This means that Linux distributions also need to allow
each artifact to be located using several different identifiers,
possible using different schemes. On the other hand it is virtually
impossible to every naming scheme, so there are some simplifications.

This chapter describes artifact different ways to identify and locate
artifacts in system repository.

## Aliases {#_aliases}

Aliases working in two ways:

&#42; Symlinks for paths &#42; Additional mappings for artifact
specifications

In the real world the same project can appear under different names as
it was evolving or released differently. Therefore other projects may
refer to those alternative names instead of using the name currently
prefered by upstream.

### Artifact aliases {#_artifact_aliases}

XMvn provides a way to attach multiple artifact coordinates to a single
artifact. Dependent projects that use alternative coordinates can then
be built without the need to patch their POMs or alter the build by
other means. It will also generate virtual provides for the alias, so it
can be also used in &#96;Requires&#96; and &#96;BuildRequires&#96;.
Creating an alias is achieved by &#96;%mvn_alias&#96; macro.

:::: formalpara
::: title
Example invocation
:::

``` shell
\&#35; com.example.foo:bar (the actual artifact existing in the project) will also
\&#35; be available as com.example.foo:bar-all
%mvn_alias com.example.foo:bar com.example.foo:bar-all

\&#35; You don't need to repeat the part of coordinates that stays the same
\&#35; (groupID in this case)
%mvn_alias com.example.foo:bar :bar-all

\&#35; You can specify multiple aliases at once
%mvn_alias com.example.foo:bar :bar-all :bar-lib

\&#35; The macro supports several shortcuts to generate multiple alisaes.
\&#35; Braces - {} - capture their content, which can then be referenced in the
\&#35; alias part with @N, where N is the index of the capture group.
\&#35; \&#42; acts as a wildcard (matching anything)
\&#35; The following generates aliases ending with shaded for all artifacts in the
\&#35; project
%mvn_alias 'com.example.foo:{\&#42;}' :@1-shaded
```
::::

## Artifact specification {#_artifact_specification}

As noted in previous section, every artifact can be uniquely identified
by its file path. However this is not always the preferred way of
artifact identification.

Modern Java build systems provide a way of identifying artifacts with an
abstract identifier, or more often, a pair of identifiers. The first if
usually called &#42;group ID&#42; or &#42;organization ID&#42; while the
second is just &#42;artifact ID&#42;. This pair of identifiers will be
called &#42;artifact coordinates&#42; in this document. Besides group ID
and artifact ID, artifact coordinates may also include other optional
information about artifact, such as &#42;extension&#42;,
&#42;classifier&#42; and &#42;version&#42;.

In Linux distributions it is important to stay close to upstreams
providing software being packaged, so the ability to identify artifacts
in the same way as upstream does is very important from the packaging
point of view. Every artifact can optionally be identified by artifact
coordinates assigned during package build. Packages built with Maven
automatically use this feature, but all other packages, even these built
with pure &#96;javac&#96;, can use this feature too (see description of
&lt;&lt;\_installing_additional_artifacts,
&#96;%mvn_artifact&#96;&gt;&gt; and &lt;&lt;\_add_maven_depmap_macro,
&#96;%add_maven_depmap&#96;&gt;&gt; macros). ==== Compatibility versions
Handling of compatibility packages, versioned jars etc.

In Fedora we prefer to always have only the latest version of a given
project. Unfortunately, this is not always possible as some projects
change too much and it would be too hard to port dependent packages to
the current version. It is not possible to just update the package and
keep the old version around as the names, file paths and dependency
provides would clash. The recommended practice is to update the current
package to the new version and create new package representing the old
version (called compat package). The compat package needs to have the
version number (usually only the major number, unless further
distinction is necessary) appended to the name, thus effectivelly having
different name from RPM's point of view. Such compat package needs to
perform some additional steps to ensure that it can be installed and
used along the non-compat one.

:::: note
::: title
:::

You should always evaluate whether creating a compat package is really
necessary. Porting dependent projects to new versions of dependencies
may be a complicated task, but your effort would be appreciated and it
is likely that the patch will be accepted upstream at some point in
time. If the upstream is already inactive and the package is not
required by anything, you should also consider retiring it.
::::

### Maven Compat Versions {#_maven_compat_versions}

XMvn supports marking particular artifact as compat, performing the
necessary steps to avoid clashes with the non-compat version. An
artifact can be marked as compat by &#96;%mvn_compat_version&#96;. It
accepts an artifact argument which will determine which artifact will be
compat. The format for specifying artifact coordinates is the same as
with &lt;&lt;\_mvn_alias,&#96;%mvn_alias&#96;&gt;&gt;. In the common
case you will want to mark all artifacts as compat. You can specify
multiple compat versions at a time.

:::: formalpara
::: title
Dependency resolution of compat artifacts
:::

When XMvn performs dependency resolution for a dependency artifact in a
project, it checks the dependency version and compares it against all
versions of the artifact installed in the buildroot. If none of the
compat artifacts matches it will resolve the artifact to the non-compat
one. This has a few implications:
::::

- The versions are compared for exact match. The compat package should
  provide all applicable versions that are present in packages that are
  supposed to be used with this version.

- The dependent packages need to have correct &#96;BuildRequires&#96; on
  the compat package as the virtual provides is also different (see
  below).

:::: formalpara
::: title
File names and virtual provides
:::

In order to prevent file name clashes, compat artifacts have the first
specified compat version appended to the filename. Virtual provides for
compat artifacts also contain the version as the last part of the
coordinates. There are multiple provides for each specified compat
version. Non-compat artifact do not have any version in the virtual
provides.
::::

:::: formalpara
::: title
Example invocation of &#96;%mvn_compat_version&#96;
:::

``` shell
\&#35; Assuming the package has name bar and version 3
\&#35; Sets the compat version of foo:bar artifact to 3
%mvn_compat_version foo:bar 3
\&#35; The installed artifact file (assuming it's jar and there were no
\&#35; %mvn_file calls) will be at %{_javadir}/bar/bar-3.jar
\&#35; The generated provides for foo:bar will be
\&#35; mvn(foo:bar:3) = 3
\&#35; mvn(foo:bar:pom:3) = 3

\&#35; Sets the compat versions of all artifacts in the build to 3 and 3.2
%mvn_compat_version : 3 3.2
```
::::

## Relative paths {#_relative_paths}

JAR artifacts are installed in one of standard directory trees. Usually
this is either &#96;%{\_javadir}&#96; (&#96;/usr/share/java&#96;) or
&#96;%{\_jnidir}&#96; (&#96;/usr/lib/java&#96;).

The simplest way of identifying artifacts is using their relative path
from one of standard locations. All artifact can be identified this way
because each artifacts has a unique file name. Each path identifying
artifact will be called *artifact path* in this document.

To keep artifact paths simpler and more readable, extension can be
omitted if it is equal to &#96;jar&#96;. For non-JAR artifacts extension
cannot be omitted and must be retained.

Additionally, if artifact path points to a directory then it represents
all artifacts contained in this directory. This allows a whole set of
related artifacts to be referenced easily by specifying directory name
containing all of them.

If the same artifact path has valid expansions in two different root
directories then it is unspecified which artifacts will be located. ===
Javadoc packages Javadoc subpackages in Fedora provide automatically
generated API documentation for Java libraries and applications.
&lt;&lt;\_java_implementation_in_fedora, Java Development Kit&gt;&gt;
comes with tool called &#96;javadoc&#96;. This tool can be used for
generating the documentation from specially formated comments in Java
source files. Output of this tool, together with license files, usually
represents only content of javadoc subpackages. Note &#96;javadoc&#96;
invocation is typically handled by build system and package maintainer
does not need to deal with it directly.

Javadoc subpackage shouldn't depend on its base package and vice versa.
The rationale behind this rule is that documentation can usually be used
independently from application / library and therefore base package does
not need to be always installed. Users are given an option to install
application and documentation separately.

:::: tip
::: title
:::

You can learn more about &#96;javadoc&#96; from [official
documentation](https://www.oracle.com/technetwork/java/javase/documentation/index-137868.html).
::::

# Manpages {#_manpages_2}

This section contains manpages for &#96;mvn\_&#42;&#96; and
&#96;pom\_&#42;&#96; macros. == Maven

> Apache Maven is a software project management and comprehension tool.
> Based on the concept of a project object model (POM), Maven can manage
> a project's build, reporting and documentation from a central piece of
> information.
>
> ---  https://maven.apache.org

Maven is by far the most consistent Java build system, allowing large
amount of automation. In most common situations only following steps are
necessary:

1.  In &#96;%build&#96; section of the spec file use
    &#96;%mvn_build&#96; macro.

2.  In &#96;%install&#96; section, use &#96;%mvn_install&#96; macro.

3.  Use generated file &#96;.mfiles&#96; lists to populate
    &#96;%files&#96; section with &#96;-f&#96; switch.

:::: formalpara
::: title
Common spec file sections
:::

``` spec
BuildRequires:  maven-local
\&#8230;
%build
%mvn_build
\&#8230;

%install
%mvn_install
\&#8230;

%files -f .mfiles
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc
```
::::

The macros &#96;%mvn_build&#96; and &#96;%mvn_install&#96; automatically
handle building of the JAR files and their subsequent installation to
the correct directory. The corresponding POM and metadata files are also
installed. == Migration from older tools

This section describes how to migrate packages that use older deprecated
tools to current ones.

# &#96;%add_maven_depmap&#96; macro {#_96add_maven_depmap96_macro}

&#96;%add_maven_depmap&#96; macro was used to manually install Maven
artifacts that were built with Apache Ant or &#96;mvn-rpmbuild&#96;. It
is now deprecated and its invocations should be replaced with
&#96;%mvn_artifact&#96; and &#96;%mvn_install&#96;.

Artifact files, Maven POM files and their installation directories no
longer need to be manually installed, since that is done during run of
&#96;%mvn_install&#96;. The installed files also don't need to be
explicitly enumerated in &#96;%files&#96; section. Generated file
&#96;.mfiles&#96; should be used instead.

Relevant parts of specfile using &#96;%add_maven_depmap&#96;:

``` spec
BuildRequires:  javapackages-tools

Requires:       some-library
\&#8230;

%build
ant test

%install
install -d -m 755 $RPM_BUILD_ROOT%{_javadir}
install -m 644 target/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -m 644 %{name}.pom $RPM_BUILD_ROOT/%{_mavenpomdir}/JPP-%{name}.pom

\&#35; Note that the following call is equivalent to invoking the macro
\&#35; without any parameters
%add_maven_depmap JPP-%{name}.pom %{name}.jar

\&#35; javadoc
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr api/\&#42; $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_javadir}/\&#42;
%{_mavenpomdir}/\&#42;
%{_mavendepmapfragdir}/\&#42;

%files javadoc
%doc %{_javadocdir}/%{name}
```

The same specfile migrated to &#96;%mvn_artifact&#96; and
&#96;%mvn_install&#96;:

``` spec
\&#35; mvn_\&#42; macros are located in javapackages-local package
BuildRequires:  javapackages-local

\&#35; Since XMvn generates requires automatically, it is no longer needed
\&#35; nor recommended to specify manual Requires tags, unless the dependency
\&#35; information in the POM is incomplete or you need to depend on non-java
\&#35; packages
\&#8230;

%prep
\&#35; The default location for installing JAR files is %{_javadir}/%{name}/
\&#35; Because our original specfile put the JAR directly to %{_javadir}, we
\&#35; want to override this behavior. The folowing call tells XMvn to
\&#35; install the groupId:artifactId artifact as %{_javadir}/%{name}.jar
%mvn_file groupId:artifactId %{name}

%build
ant test

\&#35; Tell XMvn which artifact belongs to which POM
%mvn_artifact %{name}.pom target/%{name}.jar

%install
\&#35; It is not necessary to install directories and artifacts manually,
\&#35; mvn_install will take care of it

\&#35; Optionally use -J parameter to specify path to directory with built
\&#35; javadoc
%mvn_install -J api

\&#35; Use autogenerated .mfiles file instead of specifying individual files
%files -f .mfiles
%files javadoc -f .mfiles-javadoc
```

:::: formalpara
::: title
Aliases and subpackages
:::

&#96;%add_maven_depmap&#96; had &#96;-a&#96; switch to specify artifact
aliases and &#96;-f&#96; switch to support splitting artifacts across
multiple subpackages. To achieve the same things with
&#96;%mvn\_&#42;&#96; macros, see &lt;&lt;\_additional_mappings&gt;&gt;
and
&lt;&lt;\_assignment_of_the_maven_artifacts_to_the_subpackages&gt;&gt;.
::::

:::: tip
::: title
:::

If the project consists of multiple artifacts and parent POMs are among
them, call &#96;%mvn_artifact&#96; on these parent POMs first.
::::

# Macros for Maven build configuration {#_macros_for_maven_build_configuration}

Maven builds can be configured to produce alternative layout, include
additional aliases in package metadata or create separate subpackages
for certain artifacts.

## Installing additional artifacts {#_installing_additional_artifacts}

It is possible to explicitly request an installation of any Maven
artifact (JAR / POM file). Macro &#96;%mvn_install&#96; only knows about
Maven artifacts that were created during execution of
&#96;%mvn_build&#96;. Normally, any other artifacts which were built by
some other method would need to be installed manually.
&#96;%mvn_build&#96; macro does not even need to be used at all.
Luckily, all artifacts created outside of &#96;%mvn_build&#96; can be
marked for installation with &#96;%mvn_artifact&#96; macro. This macro
creates configuration for &#96;%mvn_install&#96;.

:::: formalpara
::: title
Requesting installation of Maven artifact
:::

``` spec
%prep
\&#8230;
\&#35; Request installation of POM and JAR file
%mvn_artifact subpackage/pom.xml target/artifact.jar
\&#35; Request installation of POM artifact (no JAR file)
%mvn_artifact pom.xml
\&#35; Request installation for JAR file specified by artifact coordinates
%mvn_artifact webapp:webapp:war:3.1 webapp.war
```
::::

## Additional Mappings {#_additional_mappings}

The macro &#96;%mvn_alias&#96; can be used to add additional mappings
for given POM / JAR file. For example, if the POM file indicates that it
contains &#96;groupId&#96; &#96;commons-lang&#96;, &#96;artifactId&#96;
&#96;commons-lang&#96;, this macro ensures that we also add a mapping
between &#96;groupId&#96; &#96;org.apache.commons&#96; and the installed
JAR / POM files. This is necessary in cases where the groupId or
artifactId may have changed, and other packages might require different
IDs than those reflected in the installed POM.

:::: formalpara
::: title
Adding more mappings for JAR/POM files example
:::

``` spec
%prep
\&#8230;
%mvn_alias 'commons-lang:commons-lang' 'org.apache.commons:commons-lang'
```
::::

## Alternative JAR File Names {#_alternative_jar_file_names}

In some cases, it may be important to be able to provide symbolic links
to actual JAR files. This can be achieved with &#96;%mvn_file&#96;
macro. This macro allows packager to specify names of the JAR files,
their location in &#96;%{\_javadir}&#96; directory and also can create
symbolic links to the JAR files. These links can be possibly located
outside of the &#96;%{\_javadir}&#96; directory.

:::: formalpara
::: title
Adding file symlinks to compatibility
:::

``` spec
%prep
\&#8230;
%mvn_file :guice google/guice guice
```
::::

This means that JAR file for artifact with ID \'guice\' (and any
&#96;groupId&#96;) will be installed in
&#96;%{\_javadir}/google/guice.jar&#96; and there also will be a
symbolic links to this JAR file located in
&#96;%{\_javadir}/guice.jar&#96;. Note the macro will add &#96;.jar&#96;
extensions automatically.

## Single Artifact Per Package {#_single_artifact_per_package}

If the project consists of multiple artifacts, it is recommended to
install each artifact to the separate subpackage. The macro
&#96;%mvn_build -s&#96; will generate separate &#96;.mfiles&#96; file
for every artifact in the project. This file contains list of files
related to specific artifact (typically JAR file, POM file and
metadata). It can be later used in &#96;%files&#96; section of the spec
file.

:::: formalpara
::: title
Creating one subpackage for each generated artifact
:::

``` spec
\&#8230;
%description
The Maven Plugin Tools contains\&#8230;

%package -n maven-plugin-annotations
Summary:        Maven Plugin Java 5 Annotations

%description -n maven-plugin-annotations
This package contains Java 5 annotations to use in Mojos.

%package -n maven-plugin-plugin
Summary:        Maven Plugin Plugin

%description -n maven-plugin-plugin
The Plugin Plugin is used to\&#8230;
\&#8230;

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-maven-plugin-tools
%doc LICENSE NOTICE
%files -n maven-plugin-annotations -f .mfiles-maven-plugin-annotations
%files -n maven-plugin-plugin      -f .mfiles-maven-plugin-plugin
%files -f .mfiles-javadoc
\&#8230;
```
::::

## Assignment of the Maven Artifacts to the Subpackages {#_assignment_of_the_maven_artifacts_to_the_subpackages}

The macro &#96;%mvn_package&#96; allows maintainer to specify in which
exact package the selected artifact will end up. It is something between
singleton packaging, when each artifact has its own subpackage and
default packaging, when all artifacts end up in the same package.

:::: formalpara
::: title
Assigning multiple artifacts to single subpackage
:::

``` spec
\&#8230;
%prep
%mvn_package ':plexus-compiler-jikes'   plexus-compiler-extras
%mvn_package ':plexus-compiler-eclipse' plexus-compiler-extras
%mvn_package ':plexus-compiler-csharp'  plexus-compiler-extras

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%files -f .mfiles-plexus-compiler-extras
%files -f .mfiles-javadoc
```
::::

In above example, the artifacts &#96;plexus-compiler-jikes&#96;,
&#96;plexus-compiler-eclipse&#96;, &#96;plexus-compiler-csharp&#96; will
end up in package named &#96;plexus-compiler-extras&#96;. If there are
some other artifacts beside these three mentioned (e.g. some parent
POMs), then these will all end up in package named &#96;%{name}&#96;.

:::: tip
::: title
:::

&#96;%mvn_package&#96; macro supports wildcards and brace expansions, so
whole &#96;%prep&#96; section from previous example can be replaced with
single line: &#96;%mvn_package
\':plexus-compiler-{jikes,eclipse,csharp}\' plexus-compiler-extras&#96;.
::::

It is possible to assign artifacts into a package called
&#96;\_\_noinstall&#96;. This package name has a special meaning. And as
you can guess, artifacts assigned into this package will not be
installed anywhere and the package itself will not be created.

:::: formalpara
::: title
Skipping installation of an artifact
:::

``` spec
%prep
\&#8230;
%mvn_package groupId:artifactId __noinstall
```
::::

## Modifying XMvn configuration from within spec file {#_modifying_xmvn_configuration_from_within_spec_file}

Some packages might need to modify XMvn's configuration in order to
build successfully or from other reasons. This can be achieved with
&#96;mvn_config&#96; macro. For example, some old package can use
&#96;enum&#96; as an identifier, but it is also keyword since Java 1.5.
Such package will probably fail to build on current systems. This
problem can be easily solved by passing &#96;-source 1.4&#96; to the
compiler, so one could add following line to the spec file:

:::: formalpara
::: title
Overriding default XMvn configuration
:::

``` spec
%prep
\&#8230;
%mvn_config buildSettings/compilerSource 1.4
```
::::

XMvn's configuration is quite complex, but well documented at the
project's [official
website](https://mizdebsk.fedorapeople.org/xmvn/site/). The website
should always be used as a primary source of information about XMvn
configuration.

:::: tip
::: title
:::

Read about XMvn's configuration
[basics](https://mizdebsk.fedorapeople.org/xmvn/site/configuration.html)
and see the full [configuration
reference](https://mizdebsk.fedorapeople.org/xmvn/site/config.html).
::::

:::: tip
::: title
:::

All &#96;%mvn\_&#96; macros have their own manual page which contains
details on how to use them. All possible options should be documented
there. These manual pages should be considered most up to date
documentation right after source code. Try for example &#96;man
mvn_file&#96;. These pages are also included in the &lt;&lt;\_manpages,
Appendix&gt;&gt;.
::::

# Packaging Best Practices {#_packaging_best_practices}

Packaging Java has certain specifics that will be covered in this
section which will cover basic packaging principles:

&#42; No bundling &#42; Working with upstreams &#42; Commenting
workarounds &#42; Single library version &#42; Links to other
appropriate documents &#42; &#8230; === Packaging Maven project This
step by step guide will show you how to package Maven project. Let's
start with probably the simplest spec file possible.

``` {.spec .numberLines}
```

The spec file above is a real world example how it may look like for
simple Maven project. Both &#96;%build&#96; and &#96;%install&#96;
sections consist only of one line.

Another interesting line:

``` spec
10: BuildRequires:  maven-local
```

All Maven projects need to have &#96;BuildRequires&#96; on
&#96;maven-local&#96;. They also need to have &#96;Requires&#96; and
&#96;BuildRequires&#96; on &#96;jpackages-utils&#96;, but build system
adds these automatically. The package maintainer does not need to list
them explicitly.

``` spec
31: %dir %{_javadir}/%{name}
```

By default, resulting JAR files will be installed in
&#96;%{\_javadir}/%{name}&#96;, therefore the package needs to own this
directory.

The build could fail from many reasons, but one probably most common is
build failure due to &lt;&lt;\_missing_dependency, missing
dependencies&gt;&gt;.

We can try to remove these missing dependencies from pom.xml and make
Maven stop complaining about them. However, these removed dependencies
may be crucial for building of the project and therefore it may be
needed to package them later. Let's remove the dependencies from
&#96;pom.xml&#96;.

:::: formalpara
::: title
Remove dependencies from pom.xml
:::

``` spec
\&#8230;
%prep
%setup -q

\&#35; Add following lines to %prep section of a spec file
%pom_remove_dep :commons-io
%pom_remove_dep :junit
```
::::

The package maintainer can use a wide variety of \'&#96;pom\_&#96;\'
macros for modifying &#96;pom.xml&#96; files. See the
&lt;&lt;\_macros_for_pom_modification&gt;&gt; section for more
information.

Now try to build the project again. The build will fail with a
&lt;&lt;\_compilation_failure, compilation failure&gt;&gt;.

Oops, another problem. This time Maven thought it had all the necessary
dependencies, but Java compiler found otherwise.

Now it is possible to either patch the source code not to depend on
missing libraries or to package them. The second approach is usually
correct. It is not necessary to package every dependency right away. The
maintainer could package compile time dependencies first and keep the
rest for later (test dependencies, etc.). But Maven needs to know that
it should not try to run tests now. This can be achieved by passing
&#96;-f&#96; option to &#96;%mvn_build&#96; macro. Maven will stop
complaining about missing test scoped dependencies from now on.

:::: tip
::: title
:::

Another reason to disable the test phase is to speed up the local build
process. This can also be achieved by specifying an additional switch
&#96;\--without=tests&#96; to the &#96;fedpkg&#96; or the &#96;mock&#96;
tool instead of adding a switch to &#96;%mvn_build&#96;.

Another switch &#96;\--without=javadoc&#96; causes the build to skip
Javadoc generation.
::::

:::: note
::: title
:::

It is always recommended to run all available test suites during build.
It greatly improves quality of the package.
::::

We already have package which provides &#96;commons-io:commons-io&#96;
artifact, let's add it to the &#96;BuildRequires&#96;. Also disable
tests for now.

``` spec
BuildRequires:  maven-local
BuildRequires:  apache-commons-io
\&#8230;
%prep
%setup -q

\&#35; Comment out following lines in %prep section
\&#35;%%pom_remove_dep :commons-io
\&#35;%%pom_remove_dep :junit

%build
\&#35; Skip tests for now, missing dependency junit:junit:4.11
%mvn_build -f
```

:::: tip
::: title
:::

One can easily search for package which provides the desired artifact.
Try &#96;dnf repoquery \--whatprovides
\'mvn(commons-io:commons-io)\'&#96;, or see how to
&lt;&lt;\_querying_repositories, query repositories&gt;&gt;.
::::

Now try to build the project one more time. The build should succeed
now. Congrats, you managed to create an RPM from Maven project!

There is plenty of other things maintainer may want to do. For example,
they may want to provide symbolic links to the JAR file in
&#96;%{\_javadir}&#96;.

This can be easily achieved with &#96;%mvn_file&#96; macro:

``` spec
%prep
%setup -q

%mvn_file : %{name}/%{name} %{name}
```

See &lt;&lt;\_alternative_jar_file_names&gt;&gt; section for more
information.

Another quite common thing to do is adding aliases to Maven artifact.
Try to run &#96;rpm -qp \--provides&#96; on your locally built RPM
package:

``` shell
$ rpm -qp --provides simplemaven-1.0-1.fc21.noarch.rpm
mvn(com.example:simplemaven) = 1.0
simplemaven = 1.0-1.fc21
```

The output above tells us that the RPM package provides Maven artifact
&#96;com.example:simplemaven:1.0&#96;. Upstream may change the
&#96;groupId:artifactId&#96; with any new release. And it happens. For
example &#96;org.apache.commons:commons-io&#96; changed to
&#96;commons-io:commons-io&#96; some time ago. It is not a big deal for
package itself, but it is a huge problem for other packages that depends
on that particular package. Some packages may still have dependencies on
old &#96;groupId:artifactId&#96;, which is suddenly unavailable.
Luckily, there is an easy way how to solve the problems like these.
Package maintainer can add aliases to actually provided Maven artifact.

:::: formalpara
::: title
Add alias to Maven artifact
:::

``` spec
%mvn_alias org.example:simplemaven simplemaven:simplemaven
```
::::

See &lt;&lt;\_additional_mappings&gt;&gt; for more information on
&#96;%mvn_alias&#96;.

Rebuild the pacakge and check &#96;rpm -qp \--provides&#96; output
again:

``` shell
$ rpm -qp --provides simplemaven-1.0-2.fc21.noarch.rpm
mvn(com.example:simplemaven) = 1.0
mvn(simplemaven:simplemaven) = 1.0
simplemaven = 1.0-2.fc21
```

Now it does not matter if some other package depends on either of these
listed artifact. Both dependencies will always be satisfied with your
package.

:::: note
::: title
:::

One could try to fix dependencies in all the dependent packages instead
of adding an alias to single package. It is almost always wrong thing to
do.
::::

# Macros for POM modification {#_macros_for_pom_modification}

Sometimes Maven &#96;pom.xml&#96; files need to be patched before they
are used to build packages. One could use traditional patches to
maintain changes, but package maintainers should use
&#96;%pom\_&#42;&#96; macros developed specially to ease this task.
Using &#96;%pom\_&#42;&#96; macros not only increases readability of the
spec file, but also improves maintainability of the package as there are
no patches that would need to be rebased with each upstream release.

There are two categories of macros:

- POM-specific macros - used to manipulate dependencies, modules, etc.
  Some of them also work on &#96;ivy.xml&#96; files.

- Generic XML manipulation macros - used to add / remove / replace XML
  nodes.

The macros are designed to be called from &#96;%prep&#96; section of
spec files. All the macros also have their own manual page. This
document provides an overview of how they are used. For the technical
details, refer to their respective &lt;&lt;\_manpages, manpages&gt;&gt;.

:::: formalpara
::: title
File specfication
:::

By default, a macro acts on a &#96;pom.xml&#96; file (or
&#96;ivy.xml&#96; file) in the current directory. Different path can be
explicitly specified via an argument (the last one, unless stated
otherwise). Multiple paths can be specified as multiple arguments. If a
path is a directory, it looks for a &#96;pom.xml&#96; file in that
directory. For example:
::::

``` spec
\&#35; The following works on pom.xml file in the current directory
%pom_remove_parent

\&#35; The following works on submodule/pom.xml
%pom_remove_parent submodule

\&#35; The following works on submodule/pom.xml as well
%pom_remove_parent submodule/pom.xml

\&#35; The following works on submodule2/pom.xml and submodule2/pom.xml
%pom_remove_parent submodule1 submodule2
```

:::: formalpara
::: title
Recursive mode
:::

Most macros also support &#42;recursive&#42; mode, where the change is
applied to the &#96;pom.xml&#96; and all its modules recursively. This
can be used, for example, to remove a dependency from the whole project.
It is activated by &#96;-r&#96; switch.
::::

## Dependency manipulation macros {#_dependency_manipulation_macros}

:::: formalpara
::: title
Removing dependencies
:::

Often dependencies specified in Maven &#96;pom.xml&#96; files need to be
removed because of different reasons. &#96;%pom_remove_dep&#96; macro
can be used to ease this task:
::::

``` spec
\&#35; Removes dependency with groupId 'foo' and artifactId 'bar' from pom.xml
%pom_remove_dep foo:bar

\&#35; Removes dependency on all artifacts with groupId 'foo' from pom.xml
%pom_remove_dep foo:

\&#35; Removes dependency on all artifacts with artifactId 'bar' from pom.xml
%pom_remove_dep :bar

\&#35; Removes dependency on all artifacts with artifactId 'bar' from submodule1/pom.xml
%pom_remove_dep :bar submodule1

\&#35; Removes dependency on all artifacts with artifactId 'bar' from pom.xml
\&#35; and all its submodules
%pom_remove_dep -r :bar

\&#35; Removes all dependencies from pom.xml
%pom_remove_dep :
```

:::: formalpara
::: title
Adding dependencies
:::

Dependencies can also be added to &#96;pom.xml&#96; with
&#96;%pom_add_dep&#96; macro. Usage is very similar to
&#96;%pom_remove_dep&#96;, see &#96;\$ man pom_add_dep&#96; for more
information.
::::

:::: formalpara
::: title
Changing dependencies
:::

Sometimes the artifact coordinates used in upstream &#96;pom.xml&#96; do
not correspond to ones used in Fedora and you need to modify them.
&#96;%pom_change_dep&#96; macro will modify all dependencies matching
the first argument to artifact coordinates specified by the second
argument. Note this macro also works in recursive mode.
::::

``` spec
\&#35; For all artifacts in pom.xml that have groupId 'example' change it to
\&#35; 'com.example' while leaving artifactId and other parts intact
%pom_change_dep example: com.example:
```

## Adding / removing plugins {#_adding_removing_plugins}

&#96;%pom_remove_plugin&#96; macro works exactly as
&#96;%pom_remove_dep&#96;, except it removes Maven plugin invocations.
Some examples:

:::: formalpara
::: title
Removing Maven plugins from pom.xml files
:::

``` spec
\&#35; Disables maven-jar-plugin so that classpath isn't included in manifests
%pom_remove_plugin :maven-jar-plugin

\&#35; Disable a proprietary plugin that isn't packaged for Fedora
%pom_remove_plugin com.example.mammon:useless-proprietary-plugin submodule
```
::::

Like in previous case, there is also a macro for adding plugins to
&#96;pom.xml&#96;. See its &lt;&lt;\_pom_add_plugin, manual page&gt;&gt;
for more information.

## Disabling unneeded modules {#_disabling_unneeded_modules}

Sometimes some submodules of upstream project cannot be built for
various reasons and there is a need to disable them. This can be
achieved by using &#96;%pom_disable_module&#96;, for example:

:::: formalpara
::: title
Disabling specific project modules
:::

``` spec
\&#35; Disables child-module-1, a submodule of the main pom.xml file
%pom_disable_module child-module-1

\&#35; Disables grandchild-module, a submodule of child-module-2/pom.xml
%pom_disable_module grandchild-module child-module-2
```
::::

## Working with parent POM references {#_working_with_parent_pom_references}

Macro &#96;%pom_remove_parent&#96; removes reference to a parent POM
from Maven POM files. This can be useful when parent POM is not yet
packaged (e.g. because of licensing issues) and at the same time it is
not really needed for building of the project. There are also macros for
adding parent POM reference (&#96;%pom_add_parent&#96;) and replacing
existing reference with new one (&#96;%pom_set_parent&#96;).

:::: formalpara
::: title
Manipulating parent POM references
:::

``` spec
\&#35; Remove reference to a parent POM from ./pom.xml
%pom_remove_parent

\&#35; Remove reference to a parent POM from ./submodule/pom.xml
%pom_remove_parent submodule

\&#35; Add parent POM reference to ./pom.xml
%pom_add_parent groupId:artifactId

\&#35; Replace existing parent POM reference in ./pom.xml
%pom_set_parent groupId:artifactId:version
```
::::

## Macros for performing generic modifications {#_macros_for_performing_generic_modifications}

The above macros cover the most common cases of modifying
&#96;pom.xml&#96; files, however if there is a need to apply some
less-common patches there are also three generic macros for modifying
&#96;pom.xml&#96; files. These generic macros can also be applied to
other XML files, such as Ant's &#96;build.xml&#96; files.

They all take a [XPath](https://www.w3.org/TR/xpath/) 1.0 expression
that selects XML nodes to be acted on (removed, replaced, etc.).

:::: note
::: title
Handling XML namespaces
:::

POM files use a specific namespace -
&#96;http://maven.apache.org/POM/4.0.0&#96;. The easiest way to respect
this namespace in XPath expressions is prefixing all node names with
&#96;pom:&#96;. For example, &#96;pom:environment/pom:os&#96; will work
because it selects nodes from &#96;pom&#96; namespace, but
&#96;environment/os&#96; won't find anything because it looks for nodes
that do not belong to any XML namespace. It is needed even if the
original POM file didn't contain proper POM namespace, since it will be
added automatically. Note that this requirement is due to limitation of
XPath 1.0 and we cannot work it around.
::::

:::: formalpara
::: title
Removing nodes
:::

&#96;%pom_xpath_remove&#96; can be used to remove arbitrary XML nodes.
::::

``` spec
\&#35; Removes extensions from the build
%pom_xpath_remove 'pom:build/pom:extensions' module/pom.xml
```

:::: formalpara
::: title
Injecting nodes
:::

&#96;%pom_xpath_inject&#96; macro is capable of injecting arbitrary XML
code to any &#96;pom.xml&#96; file. The injected code is the last
argument - optional file paths go before it (unlike most other macros).
To pass a multiline snippet, quote the argument as in the following
example.
::::

``` spec
\&#35; Add additional exclusion into maven-wagon dependency
%pom_xpath_inject 'pom:dependency[pom:artifactId='maven-wagon']/pom:exclusions' '
\&lt;exclusion\&gt;
\&lt;groupId\&gt;antlr\&lt;/groupId\&gt;
\&lt;artifactId\&gt;antlr\&lt;/artifactId\&gt;
\&lt;/exclusion\&gt;'
\&#35; The same thing, but with explicit file path
%pom_xpath_inject 'pom:dependency[pom:artifactId='maven-wagon']/pom:exclusions' pom.xml '
\&lt;exclusion\&gt;
\&lt;groupId\&gt;antlr\&lt;/groupId\&gt;
\&lt;artifactId\&gt;antlr\&lt;/artifactId\&gt;
\&lt;/exclusion\&gt;'
```

:::: formalpara
::: title
Changing nodes\' content
:::

&#96;%pom_xpath_set&#96; replaces content of the arbitrary XML nodes
with specified value (can contain XML nodes).
::::

``` spec
\&#35; Change groupId of a parent
%pom_xpath_set 'pom:parent/pom:groupId' 'org.apache'
```

:::: formalpara
::: title
Replacing nodes
:::

&#96;%pom_xpath_replace&#96; replaces a XML node with specified XML
code.
::::

``` spec
\&#35; Change groupId of a parent (note the difference from %pom_xpath_set)
%pom_xpath_replace 'pom:parent/pom:groupId' '\&lt;groupId\&gt;org.apache\&lt;/groupId\&gt;'
```

The authors of this document are:

&#42; Mikolaj Izdebski, Red Hat &#42; Nicolas Mailhot, JPackage Project
&#42; Stanislav Ochotnicky, Red Hat &#42; Ville Skyttä, JPackage Project
&#42; Michal Srb, Red Hat &#42; Michael Simacek, Red Hat &#42; Marián
Konček, Red Hat

This document is free software; see the
[license](https://github.com/fedora-java/howto/blob/master/LICENSE) for
terms of use, distribution and / or modification.

The source code for this document is available in [git
repository](https://github.com/fedora-java/howto). Instructions for
building it from sources are available in [README
file](https://github.com/fedora-java/howto/blob/master/README.md).

This document is developed as part of Javapackages community project,
which welcomes new contributors. Requests and comments related to this
document should be [reported at Red Hat
Bugzilla](https://bugzilla.redhat.com/enter_bug.cgi?product=fedora&amp;component=java-packaging-howto).

Before contributing please read the [README
file](https://github.com/fedora-java/howto/blob/master/README.md), which
among other things includes basic rules which should be followed when
working on this document. You can send patches to the [Red Hat
Bugzilla](https://bugzilla.redhat.com/). They should be in git format
and should be prepared against &#96;master&#96; branch in git.
Alternatively you can also send pull requests at [Github
repository](https://github.com/fedora-java/howto).
