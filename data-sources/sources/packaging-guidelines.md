&#42; [EPEL-specific
guidelines](https://fedoraproject.org/wiki/EPEL:Packaging)

# Alternatives {#_alternatives}

Alternatives provide means for parallel installation of packages which
provide the same functionality by maintaining sets of symlinks (one per
package) pointing to alternativized files like this:
&#96;+/path/original-file -&gt;
/etc/alternatives/packagename-original-file -&gt;
/path/original-file.suffix+&#96; For more information, see
&#96;+update-alternatives(8)+&#96; manpage.

## Usage within Fedora {#_usage_within_fedora}

Alternatives &#42;MAY&#42; be used to allow parallel installation of
software when:

&#42; the software can be used as a drop-in replacement and functions
with sufficient similarity that users and other programs would, within
reason, not need to know which variant is currently installed

&#42;AND&#42;

&#42; the selection of the software is only performed system-wide by the
system administrator and end users do not have a need to switch between
the variants.

Inversely, alternatives &#42;MUST NOT&#42; be used when:

&#42; The software is not a drop-in replacement. For instance, if common
command line arguments are different between the two variants,
alternatives &#42;MUST NOT&#42; be used.

&#42;OR&#42;

&#42; End users will care which variant they are using. If a non-root
user would gain value by switching between the variants then
alternatives &#42;MUST NOT&#42; be used.

A good example of using alternatives are the various MTAs which all
provide &#96;+/usr/bin/sendmail+&#96; with similar command line
arguments.

Bad examples of using alternatives include:

&#42; the various MPI environments where users care both about which MPI
environment they compile against and which one they run against

&#42; choice of editor when the user invokes \'vi\' where the user will
care about feature availability, compatibility with plugins, etc

Cases where parallel installation is desirable but alternatives is
unsuitable may be scenarios where [Environment
Modules](../EnvironmentModules/) are appropriate. MPI and python-sphinx
(until Fedora 31) are example packages using environment-modules for
this purpose.

## How to use alternatives {#_how_to_use_alternatives}

If a package is using alternatives, the files which would otherwise
conflict MUST be installed with an appropriate suffix (for example:
&#96;+%{\_bindir}/sendmail.postfix+&#96; instead of
&#96;+%{\_bindir}/sendmail+&#96;), the original locations MUST be
touched (for example: &#96;+touch %{\_bindir}/sendmail+&#96;), the links
set up by alternatives MUST be listed as %ghost in the file list and
proper Requires: MUST be added, like in the examples below.

Putting the alternativized files in the file list ensures that they are
owned by respective packages, which means that commands like:

&#42; rpm -qf /usr/bin/foo &#42; dnf install /usr/bin/foo &#42;
repoquery \--whatprovides /usr/bin/foo

all work properly. Using %ghost for this purpose allows using globs and
generated file lists.

## Examples {#_examples}

Example from antlr.spec:

``` _rpm-spec
Requires(post): %{_bindir}/update-alternatives
Requires(postun): %{_bindir}/update-alternatives
\&#8230;
%install
\&#8230;
touch %{buildroot}%{_bindir}/antlr

%post
update-alternatives --install %{_bindir}/antlr \
%{name} %{_bindir}/antlr-java 10

%postun
if [ $1 -eq 0 ] ; then
update-alternatives --remove %{name} %{_bindir}/antlr-java
fi
\&#8230;
%files
\&#8230;
%ghost %{_bindir}/antlr
%{_bindir}/antlr-java
```

And a more complex example of alternatives invocation from
sendmail.spec, slightly edited:

``` _rpm-spec
Requires(post): %{_bindir}/update-alternatives
Requires(postun): %{_bindir}/update-alternatives
Requires(preun): %{_bindir}/update-alternatives
\&#8230;
%install
\&#8230;
\&#35; rename files for alternative usage
mv %{buildroot}%{_bindir}/sendmail %{buildroot}%{_bindir}/sendmail.sendmail
touch %{buildroot}%{_bindir}/sendmail
for i in mailq newaliases rmail; do
mv %{buildroot}%{_bindir}/$i %{buildroot}%{_bindir}/$i.sendmail
touch %{buildroot}%{_bindir}/$i
done
mv %{buildroot}%{_mandir}/man1/mailq.1 %{buildroot}%{_mandir}/man1/mailq.sendmail.1
touch %{buildroot}%{_mandir}/man1/mailq.1
mv %{buildroot}%{_mandir}/man1/newaliases.1 %{buildroot}%{_mandir}/man1/newaliases.sendmail.1
touch %{buildroot}%{_mandir}/man1/newaliases.1
mv %{buildroot}%{_mandir}/man5/aliases.5 %{buildroot}%{_mandir}/man5/aliases.sendmail.5
touch %{buildroot}%{_mandir}/man5/aliases.5
mv %{buildroot}%{_mandir}/man8/sendmail.8 %{buildroot}%{_mandir}/man8/sendmail.sendmail.8
touch %{buildroot}%{_mandir}/man8/sendmail.8

%postun
if [ '$1' -ge '1' ]; then
if [ '\&#96;readlink %{_sysconfdir}/alternatives/mta\&#96;' == '%{_bindir}/sendmail.sendmail' ]; then
%{_bindir}/alternatives --set mta %{_bindir}/sendmail.sendmail
fi
fi

%post
\&#35; Set up the alternatives files for MTAs.
update-alternatives --install %{_bindir}/sendmail mta %{_bindir}/sendmail.sendmail 90 \
--slave %{_bindir}/mailq mta-mailq %{_bindir}/mailq.sendmail \
--slave %{_bindir}/newaliases mta-newaliases %{_bindir}/newaliases.sendmail \
--slave %{_bindir}/rmail mta-rmail %{_bindir}/rmail.sendmail \
--slave /usr/lib/sendmail mta-sendmail /usr/lib/sendmail.sendmail \
--slave %{_sysconfdir}/pam.d/smtp mta-pam %{_sysconfdir}/pam.d/smtp.sendmail \
--slave %{_mandir}/man8/sendmail.8.gz mta-sendmailman %{_mandir}/man8/sendmail.sendmail.8.gz \
--slave %{_mandir}/man1/mailq.1.gz mta-mailqman %{_mandir}/man1/mailq.sendmail.1.gz \
--slave %{_mandir}/man1/newaliases.1.gz mta-newaliasesman %{_mandir}/man1/newaliases.sendmail.1.gz \
--slave %{_mandir}/man5/aliases.5.gz mta-aliasesman %{_mandir}/man5/aliases.sendmail.5.gz \
--initscript sendmail
\&#8230;

%preun
if [ $1 = 0 ]; then
update-alternatives --remove mta %{_bindir}/sendmail.sendmail
fi
\&#8230;

%files
\&#8230;
%ghost %{_bindir}/sendmail
%ghost %{_bindir}/mailq
%ghost %{_bindir}/newaliases
%ghost %{_bindir}/rmail
%ghost /usr/lib/sendmail
%ghost %{_sysconfdir}/pam.d/smtp
%ghost %{_mandir}/man8/sendmail.8.gz
%ghost %{_mandir}/man1/mailq.1.gz
%ghost %{_mandir}/man1/newaliases.1.gz
%ghost %{_mandir}/man5/aliases.5.gz

%{_bindir}/sendmail.sendmail
%{_bindir}/mailq.sendmail
%{_bindir}/newaliases.sendmail
%{_bindir}/rmail.sendmail
/usr/lib/sendmail.sendmail
%config(noreplace) %{_sysconfdir}/pam.d/smtp.sendmail
%{_mandir}/man8/sendmail.sendmail.8.gz
%{_mandir}/man1/mailq.sendmail.1.gz
%{_mandir}/man1/newaliases.sendmail.1.gz
%{_mandir}/man5/aliases.sendmail.5.gz

%attr(0755,root,root) %{_initrddir}/sendmail
```

# Packaging Guidelines for AppData Files {#_packaging_guidelines_for_appdata_files}

If a package contains a GUI application, then it SHOULD install a
&#96;+.metainfo.xml+&#96; file into &#96;+%{\_metainfodir}\\&#96;.
Installed \\&#96;.metainfo.xml+&#96; files MUST follow the [AppStream
specification
page](https://www.freedesktop.org/software/appstream/docs/chap-Quickstart.html&#35;sect-Quickstart-DesktopApps).

If a package contains an add-on for GUI application, then it SHOULD
install a &#96;+.metainfo.xml+&#96; file into
&#96;+%{\_metainfodir}\\&#96;. Installed \\&#96;.metainfo.xml+&#96;
files MUST follow the [AppStream add-ons
specification](https://www.freedesktop.org/software/appstream/docs/sect-Quickstart-Addons.html).

The AppData files MUST correctly validate using &#96;+appstream-util
validate-relax+&#96;.

:::: note
::: title
appdata.xml files
:::

For historical reasons, AppStream specification also allows using
extension &#96;+.appdata.xml+&#96; for GUI applications. If upstream
provides metadata with &#96;+.appdata.xml+&#96; extension, it MAY be
used instead of &#96;+.metainfo.xml+&#96;.
::::

## .metainfo.xml file creation {#_metainfo_xml_file_creation}

If the package doesn't already include and install its own
&#96;+.metainfo.xml+&#96; file, you can make your own and send it
upstream. Some benefits of sending the file upstream are that upstream
can translate the file using the existing translation resources and can
also modify the screenshots and descriptions as the application changes
over time.

You may include an &#96;+.metainfo.xml+&#96; file you create as a
Source: (e.g. &#96;+Source3: %{name}.metainfo.xml+&#96;) or generate it
in the spec file.

Here are the contents of a sample application &#96;+.metainfo.xml+&#96;
file (comical.metainfo.xml):

``` xml
```

Application's AppData file MUST be named with the same root as the
.desktop file, so if the .desktop file is named
&#96;+org.gnome.SomeApp.desktop+&#96; then the AppData file MUST be
called &#96;+org.gnome.SomeApp.metainfo.xml+&#96;.

Here are the contents of a sample addon &#96;+.metainfo.xml+&#96; file
(gedit-bookmarks.metainfo.xml):

``` xml
\&#8230;.
\&#8230;.
```

You can use anything as the &#96;+&lt;id&gt;+&#96; but it needs to be
unique and sensible and also match the &#96;+.metainfo.xml+&#96;
filename prefix.

## app-data-validate usage {#_app_data_validate_usage}

Although you can just include the .metainfo.xml file in the package, you
MUST run &#96;+appstream-util validate-relax+&#96; (in
&#96;+%check+&#96; or &#96;+%install+&#96;) and have
&#96;+BuildRequires: libappstream-glib+&#96;, to help ensure the
validity and safety of the appdata files you're installing. An example:

&#8230;. appstream-util validate-relax \--nonet
%{buildroot}%{\_metainfodir}/&#42;.metainfo.xml &#8230;.

# Automatic Filtering of Provides and Requires {#_automatic_filtering_of_provides_and_requires}

## Summary {#_summary}

The auto requires and provides system contained in RPM is quite useful;
however, it sometimes picks up \'private\' package capabilities that
shouldn't be advertised as global, things that are \'just wrong\', or
things prohibited by policy (e.g. deps from inside
&#96;+%{\_docdir}+&#96;).

For example:

&#42; Various \'plugin\' packages (e.g. Pidgin, Perl, Apache, KDE) are
marked as \'providing\' private shared libraries outside the system
path. &#42; Files in &#96;+%{\_docdir}+&#96; are routinely scanned, and
can trigger prov/req when this is explicitly forbidden by policy.

This Guideline describes how to filter provides and requires on Fedora.

&#42; &#42;MUST:&#42; Packages must not provide RPM dependency
information when that information is not global in nature, or are
otherwise handled (e.g. through a virtual provides system). e.g. a
plugin package containing a binary shared library must not \'provide\'
that library unless it is accessible through the system library paths.
&#42; &#42;MUST:&#42; When filtering automatically generated RPM
dependency information, the filtering system implemented by Fedora must
be used, except where there is a compelling reason to deviate from it.

## Usage {#_usage}

### Location of macro invocation {#_location_of_macro_invocation}

It's strongly recommended that these filtering macros be invoked before
&#96;+%description+&#96;, but after any other definitions. This will
keep them in a consistent place across packages, and help prevent them
from being mixed up with other sections.

### Regular Expression Variant {#_regular_expression_variant}

These filters use regular expressions. The regular expression variant
used for these filters follows the &#96;POSIX.2&#96; regular expression
standard (see the &#96;+regex(7)\\&#96; manpage). In this variant, the
literal characters \\&#96;\^.\[\$()\|\\&#42;+?{\\&#96; need to be
backslash escaped. Because rpm interprets backslashes as part of its
parsing of spec files, you will need to use a \\&#42;double
backslash\\&#42; for any escapes. A literal backslash (\\&#96;\\+&#96;)
is represented by four backslashes.

The regex engine is only passed the final string, after RPM macro
expansion. So you can't use unescaped data via RPM macros. For instance,
if you generate a list of files to match in a macro and that list
contains &#96;+libfoo.so+&#96; you'll have to use
&#96;+libfoo\\\\.so+&#96; to escape the \'\\\`.\\\`\'. Example:

``` _rpm-spec
%global to_exclude libfoo\\.so
%global __requires_exclude_from ^%{_datadir}/%{to_exclude}$
```

### Preventing files/directories from being scanned for deps (pre-scan filtering) {#_preventing_filesdirectories_from_being_scanned_for_deps_pre_scan_filtering}

The macros &#96;+%*requires_exclude_from+&#96; and
&#96;+%*provides_exclude_from+&#96; can be defined in a spec file to
keep the dependency generator from scanning specific files or
directories for deps. These macros should be defined with a regular
expression that matches all of the directories or files. For instance:

``` _rpm-spec
\&#35; Do not check any files in docdir for requires
%global __requires_exclude_from ^%{_docdir}/.\&#42;$

\&#35; Do not check .so files in an application-specific library directory
\&#35; or any files in the application's data directory for provides
%global __provides_exclude_from ^(%{_libdir}/%{name}/.\&#42;\\.so.\&#42;|%{_datadir}/myapp/.\&#42;)$
```

Note that this macro replaces the &#96;+%filter_provides_in+&#96; macro
from the old filtering guidelines but it does not do the same thing. In
particular:

&#42; The old macro could be invoked multiple times. This one will only
use the regex defined last.

&#42; The old macro advised against anchoring the beginning of the regex
(Using &#96;+\^\\&#96;). This macro recommends anchoring as it doesn\'t
suffer from the compatibility problems of the old one. \\&#42; With the
old macro it was common to specify a directory name to match everything
in a directory recursively. With the new macro you may need to specify
\\&#96;.&#42;+&#96; because you should be anchoring your regular
expressions.

### Filtering provides and requires after scanning {#_filtering_provides_and_requires_after_scanning}

In addition to preventing RPM from scanning files and directories for
automatic dependency generation you can also tell RPM to discard a
discovered dependency before it records the dependency in the RPM
metadata. Use &#96;+*requires_exclude+&#96; and
&#96;+*provides_exclude+&#96; for this. These macros should be defined
as regular expressions. If an entry that RPM's automatic dependency
generator created matches the regular expression then it will be
filtered out of the requires or provides. For example:

``` _rpm-spec
\&#35; This might be useful if plugins are being picked up by the dependency generator
%global __provides_exclude ^libfoo-plugin\\.so.\&#42;$

\&#35; Something like this could be used to prevent excess deps from an
\&#35; example python script in %doc
%global __requires_exclude ^/usr/bin/python$
```

These macros serves a similar purpose to the old
&#96;+%filter_from_provides+&#96; macro but it has a different
implementation. In particular, that macro took sed expressions whereas
this one needs a regular expression.

### Simplified macros for common cases {#_simplified_macros_for_common_cases}

In some cases, the filtering of extraneous &#96;+Provides:+&#96; is
fairly generic to all packages which provide similar things. There are
simple macros that setup filters correctly for those cases so that you
can do the filtering with one line. If you need to filter a bit more
than the simple macro provides, you still have the option to use the
macros listed above.

#### Perl {#_perl}

Perl extension modules can be filtered using this macro:

``` _rpm-spec
%{?perl_default_filter}
```

Essentially, this filters dependencies arising from &#96;+%doc+&#96;
files, from non-Linux-related modules, and from errors in the automatic
dependency generator.

If you want to use both custom filters and
&#96;+%perl_default_filter+&#96; then define your filters first and call
&#96;+%perl_default_filter+&#96; afterwards. The default filter macro
will preserve the filters you previously defined. For example:

``` _rpm-spec
\&#35; Filter all provides from some directory
%global __provides_exclude_from %{_libexecdir}/autoinst
\&#35; Filter some specific requires by name
%global __requires_exclude ^perl\\((autotest|basetest)
\&#35; All of the default filters
%{?perl_default_filter}
```

## Examples {#_examples_2}

### Pidgin plugin package {#_pidgin_plugin_package}

On a x86_64 machine, the pidgin-libnotify provides
&#96;+pidgin-libnotify.so()(64bit)+&#96; which it shouldn't as this
library is not inside the paths searched by the system for libraries.
It's a private, not global, \'provides\' and as such must not be exposed
globally by RPM.

To filter this out, we could use:

``` _rpm-spec
%global __provides_exclude_from ^%{_libdir}/purple-2/.\&#42;\\.so$
```

### Private Libraries {#_private_libraries}

At this time, filtering of private libraries is non-trivial. This is
because the symbols you want to filter from the private libraries are
usually required by the public applications that the package ships. In
order to filter, you need to find out what symbols RPM is extracting for
the private library and then remove those in both
&#96;+%*provides_exclude+&#96; and &#96;+%*requires_exclude+&#96;.

As an example, pretend you are packaging an application foo that creates
&#96;+%{\_libdir}/foo/libprivate.so+&#96; that you want to filter and
&#96;+%{\_bindir}/foobar+&#96; that requires that private library. You
could:

&#42; First build the RPM: &#96;+\$ rpmbuild -ba foo.spec+&#96; &#42;
then determine what provides rpm decided for the private library:
&#96;+\$ rpm -qp foo-1.0-1.x86_64.rpm+&#96;:

&#8230;. libprivate.so()(64bit) foo = 1.0-1.fc19 foo(x86-64) =
1.0-1.fc19 &#8230;.

&#42; See that &#96;+libprivate.so()(64bit)\\&#96; appears to be the
only symbol that RPM extracted for this package. Note that on 32bit, the
provides will be \\&#96;+libprivate.so&#96; so your regex needs to
capture both.

\+ &#42; Add the excludes to the spec file for both requires and
provides:

``` _rpm-spec
[\&#8230;]
%global _privatelibs libprivate[.]so.\&#42;
%global __provides_exclude ^(%{_privatelibs})$
%global __requires_exclude ^(%{_privatelibs})$
[\&#8230;]
```

You can take a look at a [more complex
example](https://lists.fedoraproject.org/pipermail/devel/2012-June/169190.html)
on the mailing list. This can be a pain to maintain if the upstream
changes the names of its private libraries but it is the only way to
deal with this at present. There may be a better means in [the
future](https://lists.osuosl.org/pipermail/rpm-maint/2013-January/003349.html)
but there are no solid plans on when those might be coded as of yet..

### Arch-specific extensions to scripting languages {#_arch_specific_extensions_to_scripting_languages}

e.g. to ensure an arch-specific &#96;perl-&#42;&#96; package won't
provide or require things that it shouldn't, we could use an invocation
as such:

``` _rpm-spec
\&#35; we don't want to provide private Perl extension libs
%{?perl_default_filter}
```

### &#96;+%{\_docdir}+&#96; filtering {#_96_docdir96_filtering}

By policy, nothing under &#96;+%{\_docdir}\\&#96; is allowed to either
\'provide\' or \'require\' anything. We can prevent this from happening
by preventing anything under \\&#96;%{\_docdir}+&#96; from being
scanned:

``` _rpm-spec
\&#35; we don't want to either provide or require anything from _docdir, per policy
%global __provides_exclude_from ^%{_docdir}/.\&#42;$
%global __requires_exclude_from ^%{_docdir}/.\&#42;$
```

## Additional Information {#_additional_information}

Additional information about RPM's dependency generator can be found
here:
<https://rpm-software-management.github.io/rpm/manual/dependency_generators.html>

# Conflicts Guidelines {#_conflicts_guidelines}

&#42;Author:&#42; [ Tom \'spot\'
Callaway](https://fedoraproject.org/wiki/TomCallaway)\
&#42;Revision:&#42; 0.07\
&#42;Initial Draft:&#42; Tuesday Dec 5, 2006\
&#42;Last Revised:&#42; Wednesday Oct 31, 2012\

## Conflicts {#_conflicts}

Users should always be able to install the latest packages from Fedora's
repos regardless of what other Fedora packages are installed. Therefore,
whenever possible, the latest Fedora packages of a release should avoid
conflicting with each other. Conflicts result in a transaction set where
the user has to decipher the error message and make some sort of
decision. The transaction set doesn't provide information to the user
about why two packages conflict to help them make an informed decision.

As Fedora packagers, we try to make it so that any subset of latest
Fedora's packages will install and run. Unfortunately, this is not
always possible but we can usually make it so that conflicting packages
can be installed and the user can decide which package to enable
afterwards. In the few remaining cases, we have to use
&#96;+Conflicts:+&#96; tags. These guidelines illustrate how conflicts
should be handled in Fedora, specifically concerning when and when not
to use the &#96;+Conflicts:+&#96; field.

## Acceptable Uses of Conflicts: {#_acceptable_uses_of_conflicts}

As a general rule, Fedora packages must NOT contain any usage of the
&#96;+Conflicts:+&#96; field. This field is commonly misused, when a
&#96;+Requires:+&#96; would usually be more appropriate. It confuses
depsolvers and end-users for no good reason. However, there are some
cases in which using the &#96;+Conflicts:+&#96; field is appropriate and
acceptable.

### Implicit Conflicts {#_implicit_conflicts}

Keep in mind that implicit conflicts are NEVER acceptable. If your
package conflicts with another package, then you must either resolve the
conflict, or mark it with &#96;+Conflicts:+&#96;.

### Optional Functionality {#_optional_functionality}

Some software can utilize other optional software applications if
present, but do not require them to be installed. If they are not
installed, the software will still function properly. However, if those
other \'optional applications\' are too old, then the software won't
work. This is an acceptable use of the &#96;+Conflicts:+&#96; field. The
packager must document the reason in a comment above the
&#96;+Conflicts:+&#96; field:

&#42;Example:&#42;

``` _rpm-spec
Conflicts: unrar \&lt; 2.0
```

If the software links to the libraries of another package, it must use
&#96;+Requires:+&#96; instead of &#96;+Conflicts:+&#96; to mark that
dependency. Also, if the software does not function properly without
another package being installed, it must use &#96;+Requires:+&#96;
instead of &#96;+Conflicts:+&#96;.

The packager should ask:

*If the package (at the correct version) in Conflicts: is not present,
will my package be functional?*

If the answer is yes, then it is probably a valid use of
&#96;+Conflicts:+&#96;. If the answer is no, then it is almost certainly
a better case for &#96;+Requires:+&#96;.

For example, if foo-game needs libbar to run, but will not work with
libbar that is older than 1.2.3:

&#42;WRONG:&#42; Conflicts: libbar &lt; 1.2.3\
&#42;RIGHT:&#42; Requires: libbar &gt;= 1.2.3\
Packagers should keep usage of &#96;+Conflicts:+&#96; to a bare minimum.
Only upgrading from two previous release of Fedora is supported, so
Conflicts against older packages than that, while technically correct,
are unnecessary, and should not be included.

### Splitting Packages {#_splitting_packages}

If contents from one package are split into a separate package the new
package usually contains files that also appear in the original package
which might lead to a implicit conflict between the files in the new
package and the original package. Where the new package depends on the
original package, this can be resolved with a versioned Requires:

``` _rpm-spec
\&#35; In the new package's spec file:
Requires: original-package \&gt; EVR_BEFORE_SPLIT
```

If the new package should be installable independently of whether the
original package is installed, a versioned conflict is allowed:

``` _rpm-spec
\&#35; In the new package's spec file:
Conflicts: original-package \&lt;= EVR_BEFORE_SPLIT
```

In both of these cases, the new version of the original package should
be updated to not contain the conflicting files and to depend on the new
package (at least in all stable Fedora releases). This allows to install
the latest releases of both packages without any problem. The Conflicts
are only there to resolve the case where the new package is installed
and the older version of the original package was already installed.

### Compat Package Conflicts {#_compat_package_conflicts}

It is acceptable to use &#96;+Conflicts:+&#96; in some cases involving
compat packages. These are the cases where it is not feasible to patch
applications to look in alternate locations for the -compat files, so
the foo-devel and foo-compat-devel packages need to
&#96;+Conflict:+&#96;. Whenever possible, this should be avoided.

### Incompatible Binary Files with Conflicting Naming (and stubborn upstreams) {#_incompatible_binary_files_with_conflicting_naming_and_stubborn_upstreams}

In the specific case where multiple software components generate
identically named (but incompatible) binaries, Fedora Packagers should
make every effort to convince the upstreams to rename the binaries to
resolve the conflict (see: xref:&#35;\_binary_name_conflicts\[Binary
Name Conflicts\]). However, if neither upstream is willing to rename the
binaries to resolve the conflict, &#42;AND&#42; the binaries are not
viable candidates for alternatives or environment modules (incompatible
runtimes), as long as there are no clear cases for both packages to be
installed simultaneously, explicit Conflicts are permitted at the
packager's discretion. Both packages must carry Conflicts in this case.

Be aware, adding explicit Conflicts means that if any other packages
depend on your package, you may be creating a chain-of-conflicts that
could cause user pain. Please consider this as a last resort.

## Common Conflicting Files Cases and Solutions {#_common_conflicting_files_cases_and_solutions}

There are many types of files which can conflict between multiple
packages. Fedora strongly discourages using &#96;+Conflicts:+&#96; to
resolve these cases. Here are some suggestions which can be used to
resolve these conflicts (note that not all file conflict cases are
listed, nor are all possible solutions):

### Man Page Name Conflicts {#_man_page_name_conflicts}

&#42; Rename the man pages to slightly alter the suffix of the man page
(e.g man1/check.1.gz and man1/check.1foo.gz)

&#42; Rename the man pages to include a prefix of the providing package
(e.g. foo-check.1.gz and bar-check.1.gz)

### Library Name Conflicts {#_library_name_conflicts}

If the library is 100% ABI-compatible, you can use [Environment
Modules](EnvironmentModules.xml) to let the user switch between them. If
the library is not 100% ABI-compatible get one of the upstreams to
rename. See xref:&#35;\_approaching_upstream\[Approaching Upstream\] for
ideas on persuasion. If neither upstream will budge open a ticket for
the {packaging-committee} to evaluate what sort of hoops both packages
would need to implement to not conflict at runtime.

### Header Name Conflicts {#_header_name_conflicts}

&#42; Put the headers in a subdirectory of /usr/include.

### Binary Name Conflicts {#_binary_name_conflicts}

&#42; Convince upstream to rename the binaries to something less generic
(or just less conflicting). &#42; In the case where the conflicting
binaries provide the same functionality, you can then rename the
binaries with a prefix, and use [Alternatives](Alternatives.xml) to let
the system administrator select which generic name is the default. Note
that this is usually not the case.

&#42; In cases where the binaries provide similar functionality
[EnvironmentModules](EnvironmentModules.xml) may be an option. This is
more flexible than alternatives and is for things that each individual
on a system may want to choose between rather than a system
administrator.

### Approaching Upstream {#_approaching_upstream}

When renaming or putting files into subdirectories, it is a good idea to
try to get upstream to rename their conflicting files (for instance if
they both had commands named %{\_bindir}/trash). Doing some research
about which has been around longer may be useful in this case but may or
may not be persuasive to upstream.

If neither upstream renames, we would then approach other distributions
(distributions-list\[at\]freedesktop.org is a good place to discuss
this) about renaming that can be done in all distros. That helps end
users going from one distro to another to have consistency. Length of
time that the projects have been around, how popular each is, and
numerous other factors may play a role in this decision. Once a decision
is made, we would rename the Fedora packages to match.

## Potential Conflicting Files {#_potential_conflicting_files}

We don't just try to avoid conflicts with existing packages within
Fedora but also potential conflicts. This is because the first package
to enter Fedora is not always the one that should take on the name.
There are several scenarios in which this could come into play:

1.  There is a conflicting package that is not in Fedora yet (found by
    doing a web search, for instance)

2.  There is no conflict yet but the filename is likely to be used by
    another project (something like &#96;+/usr/bin/parser+&#96;)

In the first case, where a conflicting package is known to exist but is
not yet in Fedora, we should go through the process of determining which
package has a more valid claim to the name and rename the files in the
package we're including if it doesn't have the more valid claim. If you
think your situation is unique, please open a ticket with the
{packaging-committee}.

In the second case, where there is no known package to conflict with at
this time, it is up to the packager to make a decision. Note that it is
encouraged that you at least speak to upstream about the potential for
conflicts. However, we can hope that any later projects that attempt to
use that name can be persuaded to rename based on this project being
around longer.

### Standard Commands {#_standard_commands}

Common names are allowed for standard commands since those will be the
only commands to implement them. Standard commands include things
provided for in published and widely implemented standards like POSIX
and de facto standards such as a program that has traditionally been
shipped with a certain filename as part of a large number of Unix
variants. If in doubt, send a message to
fedora-devel-list\[at\]redhat.com with details of what standards the
command appears in, how long it's been available on what Unix systems,
and whether you've found any conflicting programs that implement a
substantially different command with the same filename.

## Conflicting Package Names {#_conflicting_package_names}

Just as files can conflict, package names can as well. Conflicting
package names &#42;MUST&#42; be resolved. Package names which differ
only in case are still considered to be conflicting. You should follow
the same basic steps outlined in
xref:&#35;\_approaching_upstream\[Approaching Upstream\].

Renaming packages and replacing them with others can be difficult if it
has to occur at a later time (for instance, upgrade paths can become
complex in these situations) so it is even more important to be aware of
potential conflicts here than it is with filenames.

## Other Uses of Conflicts: {#_other_uses_of_conflicts}

If you find yourself in a situation where you feel that your package has
to conflict with another package (either explicitly or implicitly), but
does not fit the documented accepted cases above, then you need to make
your case to the [Fedora Packaging
Committee](https://pagure.io/packaging-committee). If they agree, then,
and only then can you use &#96;+Conflicts:+&#96; in a Fedora package.
Remember, whenever you use &#96;+Conflicts:+&#96;, you are also required
to include the reasoning in a comment next to the &#96;+Conflicts:+&#96;
entry, so that it will be abundantly clear why it needed to exist.

# Crypto Policies {#_crypto_policies}

## Enforcing system crypto policies {#_enforcing_system_crypto_policies}

In Fedora there are policies for the usage of cryptographic protocols
such as TLS that are enforced system-wide. Each application being added
in Fedora must be checked to comply with the policies. Currently the
policies are restricted to major libraries such as GnuTLS, OpenSSL, NSS,
libkrb5, languages such as Java and major applications like OpenSSH and
bind. The rpmlint tool will warn when it detects that some action has to
be taken; that detection is based on heuristics and limited to C
programs, so manual inspection is recommended. Note however, that there
are applications which intentionally set weaker, or custom settings on a
purpose (e.g., postfix); those need not adhere to the policy. When in
doubt, discuss with the [Fedora crypto
team](https://lists.fedoraproject.org/admin/lists/crypto-team.lists.fedoraproject.org/).

### New crypto libraries {#_new_crypto_libraries}

New crypto libraries must comply with the crypto policies to enter
Fedora, unless an exception has been granted by Fedora packaging
committee. If you wish to submit a package which does not comply with
the crypto policies, you MUST first consult with the [Fedora crypto
team](https://lists.fedoraproject.org/admin/lists/crypto-team.lists.fedoraproject.org/).
Once their approval has been granted, open a ticket with the [Fedora
Packaging Committee](https://pagure.io/packaging-committee) requesting
an exemption. Please link to any relevant discussion.

### C/C++ applications {#_cc_applications}

&#42; &#42;OpenSSL applications&#42;: &#42;&#42; *If the application
provides a configuration file* that allows to modify the cipher list
string, ensure that the shipped file contains \'PROFILE=SYSTEM\' as
default. In that case no further action is required.

&#42;&#42; *If the application doesn't have a configuration file*,
ensure that there is no default cipher list specified, or that the
default list is set as \'PROFILE=SYSTEM\'. That is, check the source
code for &#42;SSL_CTX_set_cipher_list&#42;(). If it is not present then
nothing needs to be done (the default is used). Otherwise, if that call
is present and provided a fixed string which does not contain PSK or
SRP, replace the string with \'PROFILE=SYSTEM\', or remove the call.

&#42; &#42;GnuTLS applications&#42;: &#42;&#42; *If the application
provides a configuration file* that allows to modify the cipher priority
string, the shipped file contains \'@SYSTEM\' as default. In that case
no further action is required. &#42;&#42; *If the application doesn't
have a configuration file*, ensure that it uses
gnutls_set_default_priority(), or that the default priority string is
\'@SYSTEM\'. That is, check the source code for
&#42;gnutls_priority_set_direct&#42;(),
&#42;gnutls_priority_init&#42;(); if they are not present and
gnutls_set_default_priority() is used, nothing needs to be done.
Otherwise check the strings provided by the application. If it contains
PSK or SRP do nothing (these applications are not currently covered by
the default policy). If not, then replace gnutls_priority_set_direct()
with gnutls_set_default_priority(). If gnutls_priority_init() is used
instead with a fixed string, replace the string with \'@SYSTEM\'.

Applications utilizing other cryptographic libraries do not adhere to
the system wide crypto policies (note that adherence to the system-wide
policies is work in progress for NSS libraries) Applications in Fedora
should use one of these libraries when there is choice, and preferrably
the version recommended by upstream.

### Perl applications {#_perl_applications}

&#42; &#42;IO::Socket::SSL Perl applications&#42;: &#42;&#42; Check the
source code for passing &#42;SSL_cipher_list&#42; argument to
&#42;IO::Socket::SSL&#42;\'s methods like &#42;new()&#42;,
&#42;start_SSL()&#42;, &#42;new_from_fd()&#42;,
&#42;set_defaults()&#42;, &#42;set_client_defaults()&#42;, and
&#42;set_server_defaults()&#42;. If it is not present then nothing needs
to be done (the default is used). Otherwise, if that argument is
present, remove the argument or change its value as described in OpenSSL
section.

&#42; &#42;Net::SSLeay Perl applications&#42;: &#42;&#42; Check the
source code for &#42;CTX_set_cipher_list()&#42;,
&#42;set_cipher_list()&#42;, and &#42;set_pref_cipher()&#42; subroutine
calls from &#42;Net::SSLeay&#42; name space. If such a call presents,
follow instructions described in the OpenSSL section.

&#42; &#42;LWP::UserAgent Perl applications&#42;: &#42;&#42; Check the
source code for passing &#42;SSL_cipher_list&#42; argument to
&#42;ssl_opts()&#42; method call on a &#42;LWP::UserAgent&#42; object.
If such a call presents, follow instructions described in the OpenSSL
section.

# Debuginfo packages {#_debuginfo_packages}

This page contains information about debuginfo packages and common
pitfalls about them for packagers. For usage information and an
explanation why debuginfo packages are important, see
[StackTraces](https://fedoraproject.org/wiki/StackTraces).

## Checking your debuginfo package for usefulness {#_checking_your_debuginfo_package_for_usefulness}

A useful debuginfo package contains stripped symbols from ELF binaries
(&#96;+&#42;.debug+&#96; in &#96;+/usr/lib/debug+&#96;) as well as the
source code related to them (in &#96;+/usr/src/debug+&#96;). The script
that generates the packages is
&#96;+/usr/lib/rpm/find-debuginfo.sh+&#96;, read it through to get a
basic understanding of how they're generated. If your debuginfo package
doesn't contain any files, or is missing the sources or the size of the
&#96;+&#42;.debug+&#96; files in it is unexpectedly small (typically
&#96;+&#42;.debug+&#96; are larger than the corresponding binary it was
stripped from), it's likely that there's a flaw in your package. That's
not always the case though, read on.

### Useless or incomplete debuginfo packages due to packaging issues {#_useless_or_incomplete_debuginfo_packages_due_to_packaging_issues}

Useless or incomplete debuginfo packages are often a result of packaging
flaws. Typical flaws that often manifest themselves as debuginfo
packages containing no files:

&#42; The specfile or the package's build routines explicitly strip
symbols out of the binaries. Look for invocations of &#96;+strip+&#96;,
&#96;+install -s+&#96;, &#96;+ld -s+&#96;, or &#96;+gcc -s+&#96; etc and
get rid of them (or the &#96;+-s+&#96; flags). The method how to do that
varies, some examples cases include patching, using
&#96;+%configure+&#96; or a &#96;+make+&#96; target that prevents the
strip from happening, and/or overriding a strip command like for example
&#96;+make install STRIP=/bin/true+&#96; &#42; The package is not marked
as &#96;+noarch+&#96;, but does not contain any architecture dependent
things (native binaries, architecture dependent paths etc). True
&#96;+noarch+&#96; packages contain nothing rpmbuild could strip from
them, so it's expected that they're empty if &#96;+BuildArch:
noarch+&#96; is missing. If that's the case, make the package
&#96;+noarch+&#96;. &#42; &#96;+find-debuginfo.sh+&#96; processes only
files that are executable when it's run; for practical purposes one can
assume that happens under the hood after the &#96;+%install+&#96;
section. Make sure that all ELF binaries (executables, shared libraries,
DSO's) are executable at end of &#96;+%install+&#96;. &#42;
&#96;+find-debuginfo.sh+&#96; does not process setuid or setgid
binaries. There's a [bug filed against
rpmbuild](https://bugzilla.redhat.com/117858) about that, but until it
is fixed in the distros your package is targeted at, make sure that all
your binaries do *not* have the setuid/setgid bits at end of
&#96;+%install+&#96;, and restore them in the &#96;+%files+&#96; section
using &#96;+%attr(&#8230;) /path/to/file+&#96;

Flaws that manifest themselves as unexpectedly small
&#96;+&#42;.debug+&#96; in the debuginfo package and/or source files
missing:

&#42; The package was built without passing &#96;+-g+&#96; to
&#96;+gcc+&#96; or &#96;+g++\\&#96;. Without \\&#96;-g+&#96;, no or
insufficient information for debuginfo packages is generated, make sure
that it is being used. &#42; Note that the default &#96;+CFLAGS+&#96;
and &#96;+CXXFLAGS+&#96; of the distro already contain &#96;+-g+&#96;,
so if those flags are being honored, it should be already in use. If
not, suboptimal debuginfo packages are not the only problem; the package
is probably also compiled without the security enhancing options of
recent compiler versions. Make sure that &#96;+\$RPM_OPT_FLAGS+&#96; is
being honored and used. &#42; &#96;+strip -g+&#96; was used on the
binaries; see above for possible remedies.

### Useless or incomplete debuginfo packages due to other reasons {#_useless_or_incomplete_debuginfo_packages_due_to_other_reasons}

Empty debuginfo packages may also be generated in situations where there
are no obvious packaging flaws present. Sometimes these are because of
limitations of &#96;+find-debuginfo.sh+&#96;, sometimes not. Some usual
cases:

&#42; Packages whose only architecture dependent binary part is a static
library or many of them &#42; R and Mono packages &#42;TODO: people
knowledgeable of R and/or Mono, verify these&#42;

If you wish to disable generation of the useless debuginfo package while
waiting for improvements to &#96;+find-debuginfo.sh+&#96; or if it's
unlikely that it could be enhanced to produce a good debuginfo for your
package (for example no architecture dependent files, but package is not
noarch because of the installation paths it uses), use &#96;+%global
debug_package %{nil}+&#96; in the specfile, and be sure to add a comment
next to it explaining why it was done.

## Missing debuginfo packages {#_missing_debuginfo_packages}

It is normal for noarch package builds to not produce a debuginfo
package. If it's missing in other cases (where it has not been
explicitly disabled), something's wrong. One such case is a [missing
%build section](https://bugzilla.redhat.com/192422) with some rpmbuild
versions.

## Don't obsolete debuginfo packages {#_dont_obsolete_debuginfo_packages}

In case there is removed subpackage or the subpackage is changed from
arch to noarch, the associated -debuginfo package might be left behind.
This might be issue, when &#96;+fedora-debuginfo+&#96; repository is
enabled during system upgrade. Nevertheless, because the debuginfo
packages has no dependencies, they are parallel installable and useful
for coredump analysis, don't obsolete them anywhere.

## Resources {#_resources}

&#42; debuginfo package listings for Fedora, sorted by size. Most
debuginfo packages roughly up to 20kB in size are candidates that should
be examined - however significantly larger -debuginfo packages may
suffer from the same problems too, esp. in the \'missing -g\' case.
&#42;&#42; Note that due to the split repository, each directory must be
examined separately. &#42;&#42;
<https://dl.fedoraproject.org/pub/fedora/linux/development/rawhide/Everything/x86_64/debug/tree/Packages/a/?C=S;O=A>
&#42; [StackTraces](https://fedoraproject.org/wiki/StackTraces) &#42;
rpmlint &gt;= 0.77

# Default Services {#_default_services}

## What is a Service? {#_what_is_a_service}

For the purposes of this document, a \'service\' is defined as one or
more of:

&#42; A daemon or process started using a [systemd service
unit](https://www.freedesktop.org/software/systemd/man/systemd.service.html).
&#42; A daemon or process that is invoked by socket activation, either
by using a [systemd socket
unit](https://www.freedesktop.org/software/systemd/man/systemd.socket.html),
[D-BUS
activation](https://standards.freedesktop.org/desktop-entry-spec/1.1/ar01s07.html)
or similar behavior. &#42; A daemon or process that is invoked by
hardware activation (i.e. started via a udev rule). &#42; A [systemd
timer
unit](https://www.freedesktop.org/software/systemd/man/systemd.timer.html)
that runs periodically.

Note that this includes processes which are not persistent. If something
started by a systemd service unit runs for a short period of time and
then exits, it is still a service. An example would be
&#96;+iptables+&#96;. This also includes services in the user session
(i.e. started per-user by the &#96;systemd \--user&#96; manager).

## Enabling Services by Default {#_enabling_services_by_default}

Only services that meet all criteria below MAY be enabled by default on
package installation.

### Must not alter other services {#_must_not_alter_other_services}

Installation of the package providing the unit auto-started by this
preset MUST NOT change the behavior of any other service running (or
potentially running) on the system.

### Must not require manual configuration to function {#_must_not_require_manual_configuration_to_function}

The service MUST NOT require configuration before it starts properly. If
the end-user/administrator must make some specific configuration change
before the service is able to start without error then it MUST NOT be
enabled by default.

### Must not fail under normal operating conditions {#_must_not_fail_under_normal_operating_conditions}

The service MUST NOT, under normal operating conditions, exit with an
error causing systemd to mark the unit as failed. A service which is
started by default is permitted to fail under exceptional conditions.
For example, a service could start when appropriate hardware is present,
but would still be allowed to fail if that hardware is somehow
malfunctioning. Or a service could fail to start with an error if a
configuration file has been locally modified to be syntactically
incorrect.

### Must not listen for outside connections {#_must_not_listen_for_outside_connections}

The service MUST NOT listen on a network socket for connections
originating on a separate physical or virtual machine.

D-BUS services and hardware-activated services generally meet this
requirement.

## Hardware Support Services {#_hardware_support_services}

Some hardware requires some additional service to be started in order to
be useful. This may come in the form of a non-persistent setup process
or in the form of a continuously-running service. If the service can be
hardware activated to only start when the relevant hardware is present
and do nothing when not present, and otherwise it meets the above
requirements, then it SHOULD be enabled by default upon package
installation.

If the service cannot be hardware activated, but it is possible to
configure it such that it will exit without error and without marking
the service as \'failed\' according to systemd, then it SHOULD be
enabled by default upon package installation. This clean exit may be
accomplished through [systemd
conditionals](https://www.freedesktop.org/software/systemd/man/systemd.unit.html&#35;ConditionArchitecture=),
by having the service (or a wrapper script) perform hardware detection
and exit without indicating an error, or via other similar means.

## Approved Exceptions {#_approved_exceptions}

Some services which are permitted to be enabled by default as specific
exceptions. Services that should be enabled by default throughout all of
Fedora must be approved by [FESCo](https://pagure.io/fesco). Services
that should be enabled or disabled by default only on one or more of the
Fedora Editions must be approved by those Editions\' [Working
Groups](https://fedoraproject.org/wiki/Fedora.next&#35;Working_groups).

Example:

&#42; FESCo approves openssh-server to run by default on Fedora in
general. &#42; Workstation WG approves openssh-server to be disabled by
default on the Workstation Edition.

## Current list of enabled/disabled services {#_current_list_of_enableddisabled_services}

&#42; [Fedora
general](https://src.fedoraproject.org/rpms/fedora-release/blob/rawhide/f/90-default.preset)
&#42; [Fedora general
(per-user)](https://src.fedoraproject.org/rpms/fedora-release/blob/rawhide/f/90-default-user.preset)
&#42; [Fedora
Server](https://src.fedoraproject.org/rpms/fedora-release/blob/rawhide/f/80-server.preset)
&#42; [Fedora desktop (Workstation and
KDE)](https://src.fedoraproject.org/rpms/fedora-release/blob/rawhide/f/81-desktop.preset)
&#42; [Fedora
Workstation](https://src.fedoraproject.org/rpms/fedora-release/blob/rawhide/f/80-workstation.preset)

## How to enable a service by default {#_how_to_enable_a_service_by_default}

Unit files must correspond to the Fedora Packaging
[Guidelines](Scriptlets.adoc&#35;_systemd). Services are enabled or
disabled by default through [systemd preset
files](https://www.freedesktop.org/software/systemd/man/systemd.preset.html).
Preset files can be overridden by a local administrator, but a set of
defaults are provided by Fedora.

If the service should be enabled by default, it must be added to one of
the distribution presets files (see above).

For services which meet one of the conditions listed above, a ticket
should be filed in
[bugzilla](https://bugzilla.redhat.com/enter_bug.cgi?product=Fedora&amp;format=fedora-systemd-request).
If the preset should be changed for versions other than rawhide,
indicate that in the ticket.

# Defining source and build directories {#_defining_source_and_build_directories}

Build systems that support defining source/build directories via RPM
macros:

&#42; [CMake](CMake.xml) &#42; [Meson](Meson.xml)

Macros:

&#96;+%\_vpath_srcdir+&#96;

:   Path (relative to the RPM build directory) where the sources to be
    built are located (default: &#96;+.+&#96;).

&#96;+%\_vpath_builddir+&#96;

:   Path (relative to the RPM build directory) where the built objects
    are located (default: &#96;+%{\_target_platform}+&#96;).

# Deprecating Packages {#_deprecating_packages}

Sometimes a package is intended to be [removed from
Fedora](https://docs.fedoraproject.org/en-US/package-maintainers/Package_Retirement_Process/),
but it is kept in Fedora for some additional (often indeterminate) time
for various reasons including maintaining backwards compatibility. In
order to prevent new packages from depending on such a package, it can
be marked as &#42;deprecated&#42;.

## Prerequisites for deprecation {#_prerequisites_for_deprecation}

If nothing in Fedora depends on a package, a maintainer may deprecate it
at their leisure. A maintainer (or collection of maintainers) may also
deprecate a set of packages together if no package in that set is a
dependency of any package outside of that set.

If a package is a dependency of other packages in the distribution
(which are not to be deprecated) then deprecation requires a [FESCo
approved Fedora change](https://fedoraproject.org/wiki/Changes/Policy).
A packager SHOULD communicate package deprecation to other maintainers,
preferably via the
[devel](https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/)
or
[devel-announce](https://lists.fedoraproject.org/archives/list/devel-announce@lists.fedoraproject.org/)
mailing lists.

## Marking a package deprecated {#_marking_a_package_deprecated}

In order to mark a package deprecated, a special virtual provides is
added:

&#8230;. Provides: deprecated() &#8230;.

If the package has subpackages and the packager intends to deprecate the
package as a whole, packager MUST mark all subpackages as being
deprecated.

&#8230;. Name:      mainpackage &#8230; Provides:  deprecated()

&#8230;

%package subpackage &#8230; Provides:  deprecated() &#8230;.

Alternatively, a packager MAY decide to only deprecate some subpackages.

A packager SHOULD add a comment in the spec explaining why a package is
being deprecated. For example:

&#8230;.
&#35; net-tools (ifconfig etc.) have been obsoleted for \~20 years upstream.
&#35; We want to get rid of it from Fedora in favor of the iproute package,
&#35; however many sysadmins still expect ifconfig to be there, so we keep it
&#35; around as a deprecated package. Provides:  deprecated() &#8230;.

If a date for the final removal of the package from the distribution is
known, it MAY be included as follows:

&#8230;. Provides:  deprecated() = YYYYMMDD &#8230;.

The special &#96;+deprecated()\\&#96; provide MUST NOT be added in any
released branch of Fedora. It is acceptable to deprecate packages in
rawhide (the master branch), the branch for an upcoming Fedora release
(if one exists) up until the time of the
https://fedoraproject.org/wiki/Schedule\[Final Freeze\], and to EPEL
branches (at any time). Also note that because packages may exist in a
deprecated state for some time, those packages can eventually enter
release branches. The restriction is on the initial addition of the
\\&#96;+deprecated()&#96; tag.

## Consequences of a package being deprecated {#_consequences_of_a_package_being_deprecated}

Technically, nothing changes; a deprecated package works and behaves as
before. However, other packages in Fedora MUST NOT add a dependency on a
deprecated package (that includes Requires, BuildRequires, Recommends,
Suggests, etc.). This applies both for updates of existing packages and
new packages added to Fedora. Those submitting new packages, along with
package reviewers, MUST check to see if any dependencies of the package
they are submitting or reviewing have been deprecated. (It is, however,
acceptable for a deprecated package to be renamed.)

# Replacing a symlink with a directory or a directory with any type of file {#_replacing_a_symlink_with_a_directory_or_a_directory_with_any_type_of_file}

Due to a known limitation with RPM, it is not possible to replace a
directory with any kind of file or symlink, nor is it possible to
replace a symlink to a directory with a directory without RPM producing
file conflict errors while trying to install the package. For more
information on the issues involved, refer to [bug
447156](https://bugzilla.redhat.com/show_bug.cgi?id=447156) and [bug
646523](https://bugzilla.redhat.com/show_bug.cgi?id=646523).

## Try to avoid the problem in the first place {#_try_to_avoid_the_problem_in_the_first_place}

While it's obviously not possible to foresee all the cases where the
need might arise, when the need &#42;\_is\_&#42; foreseeable, such as
with bundled libraries, it is better to use a symlink from the
beginning, as the symlink target can be changed more easily. For
instance, if you have a bundled &#96;libfoo&#96; library inside the
package's directory structure, place it in, for example, a
&#96;libfoo.bundled&#96; directory and make libfoo a symlink to that.
When the bundling is eventually removed, you just need to drop the
directory and change the symlink to point to the corresponding system
library directory, without resorting to the scriptlets described below.

## Working around it with scriptlets {#_working_around_it_with_scriptlets}

To work around this problem, you must include a [%pretrans
scriptlet](Scriptlets.adoc&#35;pretrans) that manually performs the
conversion prior to RPM attempting to install the package.

Note that \'%pretrans\' scriptlets MUST be written in Lua and thus use
&#96;+-p &lt;lua&gt;+&#96; in order to function during initial system
installation when no shell has yet been installed.

Please use whichever of the two following snippets is necessary in
packages that need this transition, replacing &#96;+/path/to/dir+&#96;
with the path to the directory that is being converted.

### Scriptlet to replace a directory {#_scriptlet_to_replace_a_directory}

RPM cannot simply remove a directory when it is replaced by a file or
symlink, since users may have added or modified files to the directory.
To protect against accidental data loss, you MUST use the following
scriptlet which renames the directory with a &#96;+.rpmmoved+&#96;
suffix so that users can find the backed up directory if they need to
after the package is upgraded. (It also will append an integer to the
suffix in the rare event that directory also exists.)

&#8230;. %pretrans -p &lt;lua&gt; --- Define the path to directory being
replaced below. --- DO NOT add a trailing slash at the end. path =
\'/path/to/dir\' st = posix.stat(path) if st and st.type ==
\'directory\' then status = os.rename(path, path .. \'.rpmmoved\') if
not status then suffix = 0 while not status do suffix = suffix + 1
status = os.rename(path .. \'.rpmmoved\', path .. \'.rpmmoved.\' ..
suffix) end os.rename(path, path .. \'.rpmmoved\') end end &#8230;.

Additionally, you should define the &#96;+/path/to/dir.rpmmoved+&#96;
directory as a &#96;+%ghost+&#96; entry in the &#96;+%files+&#96; list
in the package's spec file, so that the directory is not entirely
orphaned and can be deleted if the package is ever uninstalled and the
directory is empty.

### Scriptlet to replace a symlink to a directory with a directory {#_scriptlet_to_replace_a_symlink_to_a_directory_with_a_directory}

Replacing a symlink to a directory with a regular directory is much
simpler, since there's no potential for accidentally removing files
added externally. The following scriptlet checks for and removes the
symlink. There is no need to create the directory here, as RPM will do
so later in the transaction when the package is installed.

&#8230;. %pretrans -p &lt;lua&gt; --- Define the path to the symlink
being replaced below. path = \'/path/to/dir\' st = posix.stat(path) if
st and st.type == \'link\' then os.remove(path) end &#8230;.

# Dist Tag Guidelines {#_dist_tag_guidelines}

Use of the &#96;+%{?dist}+&#96; tag is mandatory in Fedora.

You should consider this document as an addendum to the [Naming
Guidelines](Naming.xml).

## Purpose of the Dist Tag {#_purpose_of_the_dist_tag}

There are several uses for a &#96;+%{?dist}\\&#96; tag. The original
purpose was so that a single spec file could be used for multiple
distribution releases. In doing this, there are cases in which
BuildRequires: and Requires: will need to be different for different
distribution releases. Hence, \\&#96;%{?dist}+&#96; does double duty:

&#42; it differentiates multiple packages which would otherwise have the
same &#96;+%{name}-%{version}-%{release}+&#96;, but very different
dependencies.

&#42; it allows for a conditional check in the spec to deal with the
differing dependencies.

### Do I Have To Use the Dist Tag? {#_do_i_have_to_use_the_dist_tag}

Yes. It is very useful in maintaining proper ordering between Fedora
releases and consistency in release tags is very helpful to the
automated tools which are used to perform mass rebuilds.

## Using %{?dist} {#_using_dist}

Here is the important information to know:

### Possible values for %{dist} {#_possible_values_for_dist}

When you run fedpkg commands like &#96;+fedpkg build+&#96;, the values
for &#96;+%{dist}\\&#96; and its helper variables are assigned according
to the git branch that you are working in. You do NOT need to define
these variables in your spec file. fedpkg will magically set
\\&#96;%{?dist}+&#96; for you.

For reference purposes only, these are some possible values for
&#96;+%{dist}\\&#96;. Note that if \\&#96;%{dist}\\&#96; is undefined,
\\&#96;%{?dist}+&#96; simply becomes empty. Also note that Fedora
releases use \'fc\' and not \'f\' in the tag for historical reasons.

+-----------------------------------+-----------------------------------+
| OS                                | %{?dist} tag                      |
+===================================+===================================+
| RHEL 7 (all variants)             | &#96;.el7&#96;                    |
+-----------------------------------+-----------------------------------+
| RHEL 8 (all variants)             | &#96;.el8&#96;                    |
+-----------------------------------+-----------------------------------+
| RHEL 9 (all variants)             | &#96;.el9&#96;                    |
+-----------------------------------+-----------------------------------+
| Fedora {PREVVER}                  | &#96;.fc{PREVVER}&#96;            |
+-----------------------------------+-----------------------------------+
| Fedora {CURRENTVER}               | &#96;.fc{CURRENTVER}&#96;         |
+-----------------------------------+-----------------------------------+
| Fedora {NEXTVER}                  | &#96;.fc{NEXTVER}&#96;            |
+-----------------------------------+-----------------------------------+

Development:

The development branch takes the disttag of the next major unreleased
version of Fedora.

Note the leading period in the definition of &#96;+%{?dist}+&#96;. This
is present so that it can easily be used in the release field. These
definitions can be found in common/branches.

Note that RHEL dist tags are only defined for EPEL packages.

### %{?dist} in the Release: field {#_dist_in_the_release_field}

The &#96;+%{?dist}+&#96; tag is included in the Release field as
follows:

&#8230;. Release: 1%{?dist} &#8230;.

This translates into:

&#8230;. If %{dist} is defined, insert its value here. If not, do
nothing. &#8230;.

So, if we have the following in a spec file:

&#8230;. Name: logjam Version: 1.4 Release: 2%{?dist} &#8230;.

When this package is built in an i386 FC20 buildroot, it generates an
rpm named: &#96;+logjam-1.4-2.fc20.i386.rpm+&#96;.

Keep in mind that &#96;+%{?dist}+&#96; should &#42;never&#42; be used in
the Name or Version fields, nor in %changelog entries.

### Conditionals {#_conditionals}

Along with &#96;+%{?dist}+&#96;, there are several \'helper\' variables
defined by the buildsystem. These variables are:

&#96;+%{rhel}+&#96;: This variable is only defined on Red Hat Enterprise
Linux builds. If defined, it is set to the release number of Red Hat
Enterprise Linux present at build time.

&#96;+%{fedora}+&#96;: This variable is only defined on Fedora builds.
If defined, it is set to the release number of Fedora present at build
time.

&#96;+%{rhl}+&#96;: This variable is only defined on Red Hat Linux
builds. If defined, it is set to the release number of Red Hat Linux
present at build time.

&#96;+%{fc&#35;}+&#96;: This variable is only defined on Fedora builds.
For example, on Fedora {CURRENTVER} builds, &#96;%{fc{CURRENTVER}}&#96;
is defined to 1.

&#96;+%{el&#35;}\\&#96;: This variable is only defined on Red Hat
Enterprise Linux builds. For example, on RHEL 7 builds,
\\&#96;%{el7}+&#96; is defined to 1.

All of these variables, if defined, will have a purely numeric value.
With &#96;+%{dist}+&#96; and these additional variables, you can create
conditionals in a spec file to handle the differences between
distributions.

Here are some examples of how to use these variables in conditionals:

&#8230;. %if 0%{?rhel} %endif

%if 0%{?fedora} &gt;= 21 %endif

%{?fedora:%global \_with_xfce \--with-xfce}

%if 0%{?rhel} %if 0%{?rhl} %endif %endif

%if 0%{?rhl}%{?fedora} %endif

%{?fc20:Requires: foo} %{?fc21:Requires: bar} %{?fc22:Requires: baz}
&#8230;.

Keep in mind that if you are checking for a specific family of
distributions, that you need to use:

&#8230;. %if 0%{?rhel} &#8230;.

and &#42;NOT&#42;

&#8230;. %if %{?rhel} &#8230;.

Without the extra 0, if &#96;+%{rhel}\\&#96; is undefined, the
\\&#96;%if+&#96; conditional will cease to exist, and the rpm will fail
to build.

### Distribution-specific values {#_distribution_specific_values}

Fedora 37 onwards, a few helper macros are defined to help packagers
write distribution-agnostic spec files:

&#96;+%{dist_vendor}\\&#96;: The vendor of the distribution. For Fedora,
this is \\&#96;+Fedora&#96;.

&#96;+%{dist_name}\\&#96;: The name of the distribution. For Fedora,
this is \\&#96;+Fedora Linux&#96;.

&#96;+%{dist_home_url}\\&#96;: The URL of the homepage of the
distribution. For Fedora, this is
\\&#96;+https://fedoraproject.org/&#96;

&#96;+%{dist_bug_report_url}\\&#96;: The URL for reporting bugs. For
Fedora, this is \\&#96;+https://bugzilla.redhat.com/&#96;

&#96;+%{dist_debuginfod_url}\\&#96;: The URL where the debuginfod server
runs (if any). This is used in elfutils.spec. For Fedora, this is
\\&#96;+https://debuginfod.fedoraproject.org/&#96;.

These values are configured via the &#96;+fedora-release+&#96; package.
Downstream distributions of Fedora are expected to provide their
distribution-specific values here.

### Things that you cannot use %{?dist} for {#_things_that_you_cannot_use_dist_for}

&#42; You must not override the variables for &#96;+%{dist}\\&#96; (or
any of the related variables). \\&#42; You must not hardcode a value for
\\&#96;%{dist}\\&#96; (or any of the related variables) in your spec.
\\&#42; You must not hardcode a dist tag in the spec: \\&#42;BAD:\\&#42;
Release: 1.fc{CURRENTVER} \\&#42;GOOD:\\&#42; Release: 1%{?dist} \\&#42;
You cannot put any sort of \'tagging\' in \\&#96;%{dist}\\&#96; (or any
of the related variables). \\&#96;%{dist}\\&#96; (and its related
variables) exist ONLY to define the distribution that a package was
built against. \\&#42; \\&#96;%{?dist}\\&#96; must never be used in the
Name or Version fields, only Release, and only as documented above.
\\&#42; \\&#96;%{fedora}\\&#96;, \\&#96;%{rhel}\\&#96;,
\\&#96;%{rhl}\\&#96;, \\&#96;%{fc&#35;}\\&#96;, \\&#96;%{el&#35;}+&#96;
must never be used in the Name, Version, or Release fields.

## Common questions {#_common_questions}

Q: Why don't you just let the buildsystem (or packager) pass the value
for dist to rpm, e.g. &#96;+rpm \--with dist el7+&#96;?\
A: Actually, we do. The Fedora buildsystem defines the values for dist
when you run &#96;+fedpkg+&#96;.

Q: Why is use of &#96;+%{?dist}+&#96; mandatory?\
A: There are very few packages which didn't use it, the primary very old
reason for not using it (sharing large data packages across Fedora
releases) is no longer relevant because all Fedora releases are signed
with a different key, and having consistent Release: tags simplifies the
automated tools which may need to increment them.

# First-time Service Setup {#_first_time_service_setup}

Many system services require some amount of initial setup before they
can run properly for the first time. Common examples are the generation
of private keys and certificates or a unique, system-specific
identifier.

Traditionally, this was done by RPM scriptlets as part of the
installation or upgrade of a package. This was sensible for a time when
the majority of installations were performed by attended or unattended
installers (such as anaconda and kickstart).

Today we see an increased reliance on generating virtual machine images
for use in both traditional and cloud-computing environments. In those
cases, having system-specific data created at package installation time
is problematic. It means that the production of such images need to have
significant care applied to remove any system-specific information about
them and then additional tools written to apply the corrected
information post-deployment. &#42;The goal of this guideline is to
ensure that if a system clean-up service such as virt-sysprep is run on
the system and then the machine is rebooted, any service that requires
first-time configuration will re-run it.&#42; The mechanism by which we
will accomplish this is to remove such first-time configuration from RPM
scriptlets (e.g. &#96;+%post+&#96;) and instead execute this
configuration as part of service startup with systemd.

This guideline describes a mechanism that can be used for both
traditional and cloud-based deployment styles.

Note: this requirement can be waived if the equivalent functionality is
incorporated as part of the service's own standard startup. These
guidelines are meant to address services that require setup before the
service can be started.

## Defining System-Specific Setup {#_defining_system_specific_setup}

A particular setup task is defined thusly: \'Any action that must be
performed on the system where the service will be run whose output is
not identical for all systems running that service.\'

Some non-exhaustive examples of system-specific configuration:

&#42; The SSH daemon generates a public/private host key &#42; The
mod_ssl httpd module creates a self-signed certificate for the machine's
hostname &#42; A remote logging service creates a UUID to represent this
machine

A few examples that should &#42;not&#42; be considered system-specific
configuration:

&#42; Creating a service user and/or group. This is safe to copy to
clones of the system. &#42; Any content that is automatically
re-generated by the service upon deletion.

## Generating Self-Signed Certificates {#_generating_self_signed_certificates}

The sscg (Self-Signed Certificate Generator) tool should be used to
generate self-signed certificates in a secure manner. It is present in
all Fedora releases; online documentation can be found at
[1](https://github.com/sgallagher/sscg).

### More on self-signed certificates {#_more_on_self_signed_certificates}

If your service makes use of the SSL/TLS protocol for transport
security, your service will require a service certificate. Ideally the
administrator deploying a new service should obtain an X.509 certificate
from an appropriate Certificate Authority (CA), which should be from a
globally operating CA (such as a commercial SSL certificate vendor) if
your service will be available on the public Internet, or from a private
CA (such as a domain controller CA) if your service will run inside an
Intranet.

However, it is often desirable to start using a self-signed certificate,
which can be immediately created, and allows the administrator to
immediately proceed doing the installation tasks. This document will
explain how to obtain a self-signed certificate, but it is recommended
that it gets replaced prior to public deployment.

The disadvantage of self-signed certificates is that most client
software (like web browsers) will reject them as untrusted, and if at
all, will require the user to override and trust it explicitly. The way
this can be done varies depending on the client software. It is easier
to add a CA certificate to the system store and mark it as trusted.

Therefore, instead of creating a self-signed certificate, we will create
a temporary CA certificate and use it to sign the certificate used by
the service. Afterwards we will delete the private key of the CA
certificate, which will remove the ability to use it to create
additional certificates. Afterwards we can import the CA certificate as
trusted into the local system certificate store, and consequently every
local client software that respects the system CA store will accept the
service certificate as trusted. The sscg tool will handle all of this
for you.

## Common Guidelines {#_common_guidelines}

For all system-specific cases, we will take advantage of systemd's
[service](https://www.freedesktop.org/software/systemd/man/systemd.service.html)
functionality. Packagers will create a new service unit file for each
service unit in their package that requires per-system configuration.
This service unit will be named &#96;+-init.service+&#96; and installed
to &#96;+/usr/lib/systemd/system+&#96;. For example, the
&#96;+tog-pegasus.service+&#96; configuration unit would be
&#96;+/usr/lib/systemd/tog-pegasus-init.service+&#96;.

The contents of this service unit will be as follows:

&#8230;.

Description=One-time configuration for &lt;servicename&gt;

ConditionPathExists=\|!/path/to/generated/config
ConditionPathExists=\|!/path/to/other/generated/config (one or more
lines optional)

Type=oneshot RemainAfterExit=no

ExecStart=/path/to/config/script &#8230;.

The syntax for &#96;+ConditionPathExists=\\&#96; uses the ! to indicate
negation (the file is not present). The \| is used to create an OR
logical pairing (resulting in the lack of ANY of these files causing the
configuration to be run). Those are called \'triggering\' conditions,
for full explanation see
https://www.freedesktop.org/software/systemd/man/systemd.unit.html\\&#35;ConditionArchitecture=\[systemd.unit(5)\].
The \\&#96;/path/to/config/script+&#96; can be any executable script or
binary that will generate the initial configuration needed by this
service. It &#42;must&#42; generate the files tested by
&#96;+ConditionPathExists+&#96;. If the script is a single command, it
can be run directly by this service unit. If it needs to run multiple
commands, it is recommended to create a script file in the package's
&#96;+/usr/libexec/+&#96; directory and execute that.

To use &#96;+tog-pegasus.service+&#96; as an example:

&#8230;.

Description=One-time configuration for tog-pegasus

ConditionPathExists=\|!/etc/Pegasus/server.pem
ConditionPathExists=\|!/etc/Pegasus/file.pem
ConditionPathExists=\|!/etc/Pegasus/client.pem

Type=oneshot RemainAfterExit=no

ExecStart=/usr/bin/sscg \--package tog-pegasus \--ca-file
/etc/Pegasus/client.pem \--cert-file /etc/Pegasus/server.pem
\--cert-key-file /etc/Pegasus/file.pem &#8230;.

The &#96;+ExecStart+&#96; command may do anything, so long as it returns
0 on success. In this case, we are generating a self-signed certificate
for the service to use.

Packagers will also need to update their primary service unit to require
this one and run after it:

&#8230;.

&#8230; Requires=&lt;service&gt;-init.service
After=&lt;service&gt;-init.service &#8230;.

To continue the &#96;+tog-pegasus.service+&#96; example:

&#8230;.

Description=OpenPegasus CIM Server After=slpd.service

Requires=tog-pegasus-init.service After=tog-pegasus-init.service

Type=forking ExecStart=/usr/sbin/cimserver
PIDFile=/var/run/tog-pegasus/cimserver.pid

WantedBy=multi-user.target &#8230;.

# KDE Packaging {#_kde_packaging}

This document outlines the best practices for packaging software using
the KDE frameworks, for use in Fedora.

## Build Dependencies {#_build_dependencies}

If using cmake, the following BuildRequires are a &#42;MUST&#42;:

``` _rpm-spec
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros
```

&#96;kf6-rpm-macros&#96; needs to be changed to &#96;kf5-rpm-macros&#96;
if building for Plasma 5 instead of Plasma 6.

## Available Macros {#_available_macros}

The following macros are used in the building of KDE packages. Note that
the version of macros (i.e. &#96;%cmake_kf5&#96; and
&#96;%cmake_kf6&#96;) can be changed depending on which version of
Plasma you are building for.

&#96;+%cmake_kf6+&#96;

:   Not unlike &#96;+%cmake+&#96;, this macro defines CFLAGS, LDFLAGS,
    etc. and calls &#96;+%\_\_cmake+&#96; with appropriate parameters
    (&#96;+-DCMAKE_INSTALL_PREFIX:PATH=/usr+&#96; and such), but with
    additional KDE-specific flags and parameters. You can pass
    &#96;+-Doption=value+&#96; to this macro in order to set options for
    the buildsystem.

&#96;+%stable_kf6+&#96;

:   Used in the package's source links, if the package is released on
    the official KDE download server. Outputs either &#96;stable&#96; or
    &#96;unstable&#96; depending on the version of the package.

Here's an example of how it would look like:

    Source0: http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

&#96;+%find_lang_kf6+&#96;

:   This macro is sometimes used instead of &#96;+%find_lang+&#96; in
    packages using language files ending in &#96;\_qt.qm&#96;.

\[&#35;kde-file-macros\] == Macros for paths set and used by build
systems

The following table lists macros which are widely used in fedora
&#96;.spec&#96; files. Those macros are provided by the
&#96;kf5-rpm-macros&#96; (For Plasma 5) and &#96;kf6-rpm-macros&#96;
(For Plasma 6) packages.

For Plasma 5, the following macros can simply have their version number
changed to reflect the Plasma 5 version (For example,
&#96;+%{\_kf6_datadir}\\&#96; would become
\\&#96;%{\_kf5_datadir}+&#96;).

+-------------+--------------------+-----------------------------------+
| macro       | definition         | comment                           |
+=============+====================+===================================+
| `%{_k       | `%{_prefix}`       |                                   |
| f6_prefix}` |                    |                                   |
+-------------+--------------------+-----------------------------------+
| `%{_kf6_ar  | `%{                | default: &#96;/usr/lib64/qt6&#96; |
| chdatadir}` | _qt6_archdatadir}` |                                   |
+-------------+--------------------+-----------------------------------+
| `%{_k       | `%                 |                                   |
| f6_bindir}` | {_kf6_prefix}/bin` |                                   |
+-------------+--------------------+-----------------------------------+
| `%{_kf      | `%{_datadir}`      | default: &#96;/usr/share&#96;     |
| 6_datadir}` |                    |                                   |
+-------------+--------------------+-----------------------------------+
| `%{_kf6_i   | `%                 | default:                          |
| ncludedir}` | {_includedir}/KF6` | &#96;/usr/include/KF6&#96;        |
+-------------+--------------------+-----------------------------------+
| `%{_k       | `%{_exe            | default:                          |
| f6_libdir}` | c_prefix}/%{_lib}` | &#96;+/usr/%{\_lib}+&#96;         |
+-------------+--------------------+-----------------------------------+
| `%{_kf6_l   | `%                 | default:                          |
| ibexecdir}` | {_libexecdir}/kf6` | &#96;/usr/libexec/kf6&#96;        |
+-------------+--------------------+-----------------------------------+
| `%{_kf6_me  | `%{_metainfodir}`  | default:                          |
| tainfodir}` |                    | &#96;/usr/share/metainfo&#96;     |
+-------------+--------------------+-----------------------------------+
| `%{_kf6_qt  | `                  | default:                          |
| plugindir}` | %{_qt6_plugindir}` | &#96                              |
|             |                    | ;+/usr/%{\_lib}/qt6/plugins+&#96; |
+-------------+--------------------+-----------------------------------+
| `%{_kf6_    | `%{_q              | default:                          |
| plugindir}` | t6_plugindir}/kf6` | &#96;+/u                          |
|             |                    | sr/%{\_lib}/qt6/plugins/kf6+&#96; |
+-------------+--------------------+-----------------------------------+
| `%{_kf6_s   | `%{_sysconfdir}`   | default: &#96;/etc&#96;           |
| ysconfdir}` |                    |                                   |
+-------------+--------------------+-----------------------------------+
| `%{_k       | `%{                | default: &#96;/usr/share/man&#96; |
| f6_mandir}` | _kf6_datadir}/man` |                                   |
+-------------+--------------------+-----------------------------------+
| `%{_k       | `%{_kf6            | default:                          |
| f6_qmldir}` | _archdatadir}/qml` | &#96;/usr/lib64/qt6/qml&#96;      |
+-------------+--------------------+-----------------------------------+

# Language packages {#_language_packages}

The idea behind \'langpacks\' is to separate translations or language
specific content into subpackages in the case that the size of the files
is huge or the package is part of a core image that should be minimal.

Subpackages that exist solely to contain additional language
translations or content must be named in the form -langpack-, where is
the name of the package that the langpacks belong to and is a valid
language code from */usr/share/xml/iso-codes/iso_639_3.xml* or from
*/usr/share/i18n/locales/*. Specifically, the langcode value used in the
package name must agree with the langcode identifier used in the
directory path by upstream for the translation or language files.

The langpack ecosystem does not need any procedural logic in the form of
plugins. Instead it takes advantage of the weak and rich dependency
features provided by RPM. The necessary dependencies are computed by the
package manager (DNF or PackageKit) so it is essential to include the
following &#96;+Supplements:+&#96; tag relation in the langpack package
definition in the spec file:

&#96;+Supplements: (%{name} = %{version}-%{release} and langpacks-&lt;locale&gt;)+&#96;

## Example {#_example}

Suppose you have a package with following spec file:

&#96;+Name: php-horde-Horde-Perms+&#96;\
&#96;+&#8230;+&#96;\
&#96;+%files -f Horde_Perms.lang+&#96;\
&#96;+/usr/share/pear-data/Horde_Perms/locale/\\&#96; +
\\&#96;&#8230;+&#96;

In order to create langpacks for each language
(*/usr/share/pear-data/Horde_Perms/locale//LC_MESSAGES/Horde_Perms.mo*
translations), you would need to define a new subpackage for each
package. The snippet below shows a macro for automating the definition
of langpacks, along with the definition of langpacks for *bs* and *cs*
languages. This would replace the lines shown above. Note that this
macro definition is specific to the example package; you will need to
modify it as appropriate for your package.

&#96;+Name: php-horde-Horde-Perms+&#96;\
&#96;+&#8230;+&#96;\

\+ &#96;+%define lang_subpkg() +&#96;\
&#96;+%package langpack-%{1}+&#96;\
&#96;+Summary:       %{2} language data for %{name}\\+&#96;\
&#96;+BuildArch:     noarch+&#96;\
&#96;+Requires:      %{name} = %{version}-%{release}\\+&#96;\
&#96;+Supplements:   (%{name} = %{version}-%{release} and langpacks-%{1})+&#96;\
&#96;++&#96;\
&#96;+%description langpack-%{1}+&#96;\
&#96;+%{2} language data for %{name}.+&#96;\
&#96;++&#96;\
&#96;+%files langpack-%{1}+&#96;\
&#96;+%{\_datadir}/pear-data/Horde_Perms/locale/%{1}/\\&#96; +
\\&#96; %lang_subpkg bs Bosnian+&#96;\
&#96;+%lang_subpkg cs Czech+&#96;\
&#96;+&#8230;+&#96;\

\+ &#96;+%files+&#96;\
&#96;+&#8230;+&#96;

# Licensing Guidelines {#_licensing_guidelines}

## Fedora Licensing {#_fedora_licensing}

The goal of the Fedora Project is to work with the Linux community to
create a complete, general purpose operating system exclusively from
free and open source software.

All software in Fedora must be under licenses that have been determined
to be [allowed for
Fedora](https://docs.fedoraproject.org/en-US/legal/license-approval/).
This criteria is based on the licenses approved by the [Free Software
Foundation](https://www.gnu.org/philosophy/license-list.html&#35;GPLCompatibleLicenses),
[OSI](https://opensource.org/licenses/) and consultation with Red Hat
Legal.

For more details on the criteria for allowed and not-allowed licenses,
processes related to licensing, or other guidance related to Fedora
licensing, see [Licensing in Fedora](legal::index.xml).

The information here provides guidance on how to add license text in
&#96;+%license+&#96; and how to populate the &#96;+License:+&#96; field
of spec files for Fedora packages.

## License Text {#_license_text}

If the source package includes the text of the license(s) in its own
file, then that file, containing the text of the license(s) for the
package must be included in the &#96;+%files+&#96; list flagged with the
&#96;+%license+&#96; directive.

Note that the path so flagged can be either relative or absolute. For
relative paths, RPM will automatically copy them from the source
directory into a subdirectory of &#96;+%\_defaultlicensedir+&#96;
(&#96;+/usr/share/licenses+&#96;). For absolute paths, RPM will simply
tag the file in the final package as being a license file.

Note also that it is acceptable for license files to be so flagged in a
list which is generated programmatically and included using &#96;+%files
-f+&#96;. This tagging is often done automatically by macros and not
directly visible to the packager. What is important is not the visible
presence of the &#96;+%license+&#96; directive but instead that all
relevant license files included in a package appear when using &#96;+rpm
-q \--licensefiles+&#96;.

If the source package does not include the text of the license(s), the
packager should contact upstream and encourage them to correct this
mistake.

In cases where the upstream has chosen a license that requires that a
copy of the license text be distributed along with the binaries and/or
source code, but does not provide a copy of the license text (in the
source tree, or in some rare cases, anywhere), the packager should do
their best to point out this confusion to upstream. This sometimes
occurs when an upstream project's only reference to a license is in a
README (where they simply say \'licensed under the FOO license\'), on
their website, or when they simply do not check a copy of the license
into their Source tree. Packagers should point out to upstream that by
not including a proper full license text, they are making it difficult
or impossible for anyone to comply with their desired license terms.

However, in situations where upstream is unresponsive, unable, or
unwilling to provide proper full license text as part of the source
code, and the indicated license requires that the full license text be
included, Fedora Packagers must either:

&#42; Include a copy of what they believe the license text is intended
to be, as part of the Fedora package in &#96;+%license+&#96;, in order
to remain in compliance. It is worth noting that this may place some
additional risk on the packager, however, Fedora believes that this risk
is minimized by the fact that if the upstream disagrees with what we
have distributed as the full license text, they can easily remedy this
by making full license text available in the source code. Packagers who
choose to do this should ensure that they have exhausted all attempts to
work with upstream to include the license text as part of the source
code, or at least, to confirm the full license text explicitly with the
upstream, as this minimizes the risk on the packager. Packagers may also
take copies of license texts from reliable and canonical sources (such
as the original license text from the license steward, Fedora licenses
page, the FSF licenses page, or the OSI license list), whenever
possible.

&#42; Choose not to package that software for Fedora.

It is important to reiterate that in situations where the indicated
license does not imply a requirement that the license be distributed
along with the source/binaries, Fedora packagers are NOT required to
manually include the full license text when it is absent from the source
code, but are still encouraged to point out this issue to upstream and
encourage them to remedy it.

\[&#35;subpackage-licensing\] === Subpackage Licensing

If a subpackage is dependent (either implicitly or explicitly) upon a
base package (where a base package is defined as a resulting binary
package from the same source RPM which contains the appropriate license
texts as &#96;+%license+&#96;), it is not necessary for that subpackage
to also include those license texts as &#96;+%license+&#96;.

However, if a subpackage is independent of any base package (it does not
require it, either implicitly or explicitly), it must include copies of
any license texts (as present in the source) which are applicable to the
files contained within the subpackage.

### License Clarification {#_license_clarification}

In cases where the licensing is unclear, it may be necessary to contact
the copyright holders to confirm the licensing of code or content. In
those situations, it is *always* preferred to ask upstream to resolve
the licensing confusion by documenting the licensing and releasing an
updated tarball. However, this is not always possible to achieve.

## License: field {#_license_field}

Every Fedora package must contain a &#96;+License:+&#96; entry.
Maintainers should be aware that the contents of the
&#96;+License:+&#96; field are understood to not be legally binding
(only the source code itself is), but maintainers must make every
possible effort to be accurate when filling the &#96;+License:+&#96;
field.

The &#96;License:&#96; field refers to the licenses of the contents of
the &#42;\_binary\_&#42; rpm.

This policy and examples can be found at [License: field in spec
file](legal::license-field.xml).

### Valid License Short Names {#_valid_license_short_names}

The &#96;+License:+&#96; field for new packages as of July 2022 must be
filled with the appropriate SPDX license identifier or expression from
the list of [allowed licenses](legal::allowed-licenses.xml) for Fedora.
Note that some licenses may be allowed for only certain types of
material, e.g., fonts, content, or documentation.

The [SPDX License List](https://spdx.org/licenses/) provides identifiers
for each individual license or exception based on a set of matching
guidelines. SPDX license expressions cover situations where multiple
licenses apply to a package, where there is a choice of a license, and
where licenses are coupled with exceptions or additional permissions.

[License: field in Spec file](legal::license-field.xml) contains
examples and further explanations for using SPDX expressions in the
&#96;License:&#96; field.

For more information on what to do if you find a license that is not on
the Fedora list, does not have a corresponding SPDX license identifier
or expression, or other process questions, see [License Review
Process](legal::license-review-process.xml).

# Manual Changelog {#_manual_changelog}

This describes the traditional method of managing changelogs that
provides a separate text log of user-visible changes independently of
the git commit messages. This is an alternative for the recommended
method with &#96;+%autochangelog+&#96; described in
[Changelogs](index.adoc&#35;changelogs).

*Every time* you make changes, that is, whenever you increment the E-V-R
of a package, add a changelog entry in the &#96;+%changelog+&#96;
section.

Changelog entries should provide a brief summary of the changes done to
the package between releases. They must never simply contain an entire
copy of the source &#96;CHANGELOG&#96; entries. The same general rules
should be followed as described in
[Changelogs](index.adoc&#35;changelogs).

You must use one of the following formats:

``` _rpm-spec
%changelog
\&#42; Fri Jun 23 2006 Jesse Keating \&lt;jkeating@redhat.com\&gt; - 0.6-4
- And fix the link syntax.
```

``` _rpm-spec
%changelog
\&#42; Fri Jun 23 2006 Jesse Keating \&lt;jkeating@redhat.com\&gt; 0.6-4
- And fix the link syntax.
```

``` _rpm-spec
%changelog
\&#42; Fri Jun 23 2006 Jesse Keating \&lt;jkeating@redhat.com\&gt;
- 0.6-4
- And fix the link syntax.
```

If you wish to \'scramble\' or \'obfuscate\' your email address in the
changelog, you may do so, provided that it is still understandable by
humans.

## Multiple Changelog Entries per Release {#_multiple_changelog_entries_per_release}

In some situations, it may be useful for packagers to have multiple
changelog entries in the spec file, but not increment the release field
for each one. There are two supported methods for doing this:

## Updating and replacing the existing date line {#_updating_and_replacing_the_existing_date_line}

In this situation, you have added this changelog entry, but have not
built the package yet:

``` _rpm-spec
%changelog
\&#42; Nov 12 2010 Toshio Kuratomi \&lt;toshio_fedoraproject.org\&gt; - 1.0-1
- Fix spelling errors in package description
```

The next day, you make additional changes to the spec, and need to add a
new changelog line, then you would update the existing date line for
1.0-1, and append any new notes, making the changelog look like this:

``` _rpm-spec
%changelog
\&#42; Nov 13 2010 Toshio Kuratomi \&lt;toshio_fedoraproject.org\&gt; - 1.0-1
- Fix spelling errors in package description
- Add a patch to fix compilation problems on F15
```

Please remember that this is only acceptable if 1.0-1 has not yet been
built.

You can do this any number of times, until you actually build 1.0-1 in
the buildsystem. Once you've done that, you must change the E-V-R and
any new entries should be added as described in
[Changelogs](index.adoc&#35;changelogs).

## Repeat the old version release with a new entry {#_repeat_the_old_version_release_with_a_new_entry}

In this situation, you have added this changelog entry, but have not
built the package yet:

``` _rpm-spec
%changelog
\&#42; Nov 12 2010 Toshio Kuratomi \&lt;toshio_fedoraproject.org\&gt; - 1.0-1
- Fix spelling errors in package description
```

The next day, you make additional changes to the spec, and need to add a
new changelog line. Now, you can add an additional changelog item with
the new date, but the same Version-Release, so your new changelog looks
like this:

``` _rpm-spec
%changelog
\&#42; Nov 13 2010 Toshio Kuratomi \&lt;toshio_fedoraproject.org\&gt; - 1.0-1
- Add a patch to fix compilation problems on F15

\&#42; Nov 12 2010 Toshio Kuratomi \&lt;toshio_fedoraproject.org\&gt; - 1.0-1
- Fix spelling errors in package description
```

Please remember that this is only acceptable if 1.0-1 has not yet been
built.

You can do this any number of times, until you actually build 1.0-1 in
the buildsystem. Once you've done that, you must change the E-V-R and
any new entries should be added as described in
[Changelogs](index.adoc&#35;changelogs).

# Naming Guidelines {#_naming_guidelines}

:::: note
::: title
Versioning guidelines have moved
:::

This document previously contained information on both naming and
versioning. The versioning guidelines are now at
[Packaging:Versioning](Versioning.xml).
::::

## Common Character Set for Package Naming {#_common_character_set_for_package_naming}

While Fedora is an international community, for consistency and
usability, there needs to be a common character set for package naming.

Specifically, all Fedora packages must be named using only the following
ASCII characters. These characters are displayed here:

&#8230;. abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789-.\_+ &#8230;.

But do check &lt;&lt;Separators&gt;&gt; for additional restrictions on
using the &#96;+-.\_++&#96; characters.

### General Naming {#_general_naming}

Package names SHOULD be in lower case and use dashes in preference to
underscores. You can take some cues from the name of the upstream
tarball, the project name from which this software came, and the name
which has been used for this package by other distributions/packagers in
the past. You can also request guidance from the upstream developers. Do
not just blindly follow those examples, however, as package names SHOULD
strive to be consistent within Fedora more than consistent between
distributions.

Additionally, it is possible that the upstream name does not fall into
the &lt;&lt;Common Character Set for Package Naming&gt;&gt;. If this is
the case, refer to: &lt;&lt;When Upstream Naming is outside of the
specified character set&gt;&gt;.

Also remember to check whether the type of package you are packaging has
specific rules for naming. &lt;&lt;Font Packages&gt;&gt; and the various
sorts of &lt;&lt;Addon Packages&gt;&gt;, for instance.

### Separators {#_separators}

When naming packages for Fedora, the maintainer MUST use the dash
&#96;+-\\&#96; as the delimiter for name parts. The maintainer MUST NOT
use an underscore \\&#96;+\_&#96;, a plus &#96;++\\&#96;, or a period
\\&#96;.\\&#96; as a delimiter. Version numbers used in compat libraries
do not need to omit the dot \\&#96;.\\&#96; or change it into a dash
\\&#96;-+&#96; (see &lt;&lt;Multiple packages with the same base
name&gt;&gt; for more info on this case).

There are a few exceptions to the no underscore &#96;+\_+&#96; rule:

&#42; httpd, pam, and SDL addon packages are excluded, refer to
\'&#96;&lt;&lt;\_httpd_pam_and_sdl,Addon Packages (httpd, pam, and
SDL)&gt;&gt;&#96;\'. &#42; packages that are locale specific, and use
the locale in the name are excluded, refer to
\'&#96;&lt;&lt;\_locales,Addon Packages (locales)&gt;&gt;&#96;\'. &#42;
Compat packages where the base package name ends in a digit, refer to
\'&#96;&lt;&lt;Multiple packages with the same base name&gt;&gt;&#96;\'.
&#42; packages where the upstream name naturally contains an underscore
are excluded from this. Examples of these packages include:

\+ &#8230;. arptables_jf dhcpv6_client java_cup knm_new libart_lgpl
lm_sensors microcode_ctl nss_db nss_ldap sg3_utils tcp_wrappers &#8230;.

If in doubt, ask on <devel@lists.fedoraproject.org>.

### When Upstream Naming is outside of the specified character set {#_when_upstream_naming_is_outside_of_the_specified_character_set}

Fedora recognizes that the task of converting text to the specified
ASCII character set (aka transliteration) is difficult. Accordingly,
when the upstream name is outside of the specified ASCII character set,
the Fedora package maintainer SHOULD first contact the upstream for that
software and ask them for a transliteration of the name for Fedora to
use.

If (and only if) the upstream is unable, unwilling, or unavailable to
provide a transliterated name, the Fedora packager must choose to either
perform their own transliteration, or withdraw the package from
consideration in Fedora.

When deciding how to transliterate a package name, the Fedora packager
SHOULD look to see what (if any) other distributions have done for that
package's name, and take that into account.

### Extra Provides {#_extra_provides}

Transliterated packages MAY Provide: the original, non-transliterated
name, but are not required to do so.

## Conflicting Package Names {#_conflicting_package_names_2}

Conflicting package names, even if they differ by case alone, are not
allowed. Please see [Packaging:Conflicts&#35;Conflicting Package
Names](Conflicts.adoc&#35;_conflicting_package_names) for more details.

\[&#35;multiple\] == Multiple packages with the same base name

For many reasons, it is sometimes advantageous to keep multiple versions
of a package in Fedora to be installed simultaneously. When doing so,
the package name MUST reflect this fact. One package SHOULD use the base
name (with no version information). All other packages derived from it
MUST include the base name suffixed by either:

&#42; The package version, which SHOULD include the periods present in
the original version. &#42;&#42; If the base package name ends with a
digit, a single underscore (&#96;+\_+&#96;) MUST be appended to the
name, and the version MUST be appended to that, in order to avoid
confusion over where the name ends and the version begins. &#42;&#42; If
the base package name does not end with a digit, the version MUST be
directly appended to the package name with no intervening separator.
&#42; a hyphen (&#96;+-+&#96;) followed by a descriptive suffix such as
\'stable\' which provides some indication as to the nature of the
packaged version.

&#42;Examples:&#42;

&#42; The python-sqlalchemy package occasionally has multiple versions
in Fedora for backwards compatibility. The most current version of
python-sqlalchemy is named &#96;+python-sqlalchemy+&#96; and an older
supported version is &#96;+python-sqlalchemy0.5+&#96;. No delimiter is
used in this situation. &#42; The most current version of the v8 package
is named &#96;+v8+&#96;. In order to package version \'3.13\', the
package MUST be named &#96;+v8_3.13+&#96;.

Please also note that strings such as \'-latest\' can often become
misleading over time if the package (in &#42;all&#42; active Fedora
releases) is not kept updated with the latest upstream version.

### Documentation Packages with Embedded OS versioning {#_documentation_packages_with_embedded_os_versioning}

Documentation packages (as approved by the Fedora Documentation Project)
can be named with the OS version number in the package name to allow
parallel installation of multiple versions, in cases where the
documentation is specific to a release of Fedora and there is value in
having multiple versions simultaneously installed.

## Case Sensitivity {#_case_sensitivity}

In Fedora packaging, the maintainer uses their best judgement when
considering how to name the package. While case sensitivity is not a
mandatory requirement, case SHOULD only be used where necessary. Keep in
mind to respect the wishes of the upstream maintainers. If they refer to
their application as \'ORBit\', you SHOULD use &#96;+ORBit+&#96; as the
package name, and not &#96;+orbit+&#96;. However, if they do not express
any preference of case, you SHOULD default to lowercase naming.

The exception to this is for perl module packaging. The CPAN Group and
Type SHOULD be capitalized in the name, as if they were proper nouns.
(Refer to \'&#96;&lt;&lt;\_perl_modules,Addon Packages (Perl
modules)&gt;&gt;&#96;\' for details.)

## Renaming/replacing existing packages {#_renamingreplacing_existing_packages}

See: [Packaging:Guidelines&#35;Renaming/Replacing Existing
Packages](index.adoc&#35;renaming-or-replacing-existing-packages)

## Documentation Subpackages {#_documentation_subpackages}

Large documentation files SHOULD go in a subpackage. This subpackage
must be named with the format: &#96;+%{name}-doc+&#96; . The definition
of large is left up to the packager's best judgement, but is not
restricted to size. Large can refer to either size or quantity of files.

## Font Packages {#_font_packages}

Packages containing fonts must be named
&#96;+\[foundryname-\]projectname\[-fontfamilyname\]-fonts+&#96;, in
lowercase.

### Clarifications {#_clarifications}

1.  For Fedora purposes a "foundry" is an entity that publishes a set of
    fonts with consistent font QA rules. Thus a generic hosting service
    such as [Sourceforge](http://www.sf.net) is not a foundry, but the
    [Open Font Library](http://openfontlibrary.org/) is.

2.  It is good practice to contract *foundryname-* in a short prefix.

3.  The *foundryname-* prefix can optionally be skipped: &#42; for
    entities that never released more than one font family, or &#42;
    when the font project and the publishing entity are one and the
    same.

4.  If *projectname* or *foundryname* are repeated in *fontfamilyname*,
    they can be dropped from *fontfamilyname*.

5.  When *foundryname*, *projectname* or *fontfamilyname* contain the
    *font* or *fonts* affix, this affix should be dropped from them[^1].

6.  *-fontfamilyname* should not be included in the srpm name of a
    package that includes several different font families.

7.  If any element of the naming contains spaces, they should be
    replaced by "-".

8.  The use of the *-fonts* suffix is not dependant on the actual number
    of font files in the package.

When in doubt, ask the [mailing
list](https://fedoraproject.org/wiki/Fonts_SIG_mailing_lists) for
clarification.

## Addon Packages {#_addon_packages}

If a package is considered an \'addon\' package that enhances or adds
functionality to an existing Fedora package without being useful on its
own, its name SHOULD reflect this fact.

The new package (\'child\') SHOULD prepend the \'parent\' package in its
name, in the format: &#96;+%{parent}-%{child}+&#96;.

&#42;Examples:&#42;

&#8230;. gnome-applet-netmon (netmon applet for gnome, relies on gnome)
php-adodb (adodb functionality for php, relies on php) python3-twisted
(the twisted module for python3, relies on python3) xmms-cdread (direct
cd read functionality for xmms, relies on xmms) &#8230;.

When the addon package is a language binding, note that the language
itself is always the parent. Thus, a lua binding for the \'randomdb\'
database would be &#96;+lua-randomdb+&#96;, not
&#96;+randomdb-lua+&#96;. Also note that some packages may have
grandfathered names using the opposite ordering.

There are some exceptions to this general addon package naming policy,
and they are noted below.

### httpd, pam, and SDL {#_httpd_pam_and_sdl}

Packages that rely on Apache httpd, pam, or SDL as a parent use a
slightly different naming scheme. pam and SDL addons use the format:
&#96;+%{parent}\_%{child}\\&#96;, with an underscore \\&#96;+\_&#96; as
a delimiter. Apache httpd addons use the format:
&#96;+mod\_%{child}\\&#96;, with an underscore \\&#96;+\_&#96; as a
delimiter. This naming scheme is usually the same as used for the source
tarball name.

&#42;Examples:&#42;

&#8230;. mod_perl (Perl components for Apache httpd, relies on httpd)
pam_krb5 (krb5 components for pam, relies on pam) SDL_gfx (Additional
graphics components for SDL, relies on SDL) SDL_ttf (TrueType font
rendering support for SDL, relies on SDL) &#8230;.

### emacs components {#_emacs_components}

Packages of emacs add-on components (code that adds additional
functionality to emacs) SHOULD have a name that takes into account the
upstream name of the emacs component by being called
&#96;+emacs-\$NAME+&#96;.

&#42;Examples:&#42;

&#8230;. emacs-auctex (auctex component for GNU Emacs) emacs-deferred
(deferred component for GNU Emacs) emacs-flycheck (flycheck component
for GNU Emacs) &#8230;.

### Erlang modules {#_erlang_modules}

Packages of Erlang modules (thus they rely on Erlang as a parent) have
their own naming scheme. They SHOULD take into account the upstream name
of the Erlang module. This makes a package name format of
&#96;+erlang-\$NAME+&#96;. When in doubt, use the name of the module
that you use when importing it into a script.

&#42;Example:&#42;

&#8230;. erlang-esdl (Erlang module named esdl) &#8230;.

### GAP packages {#_gap_packages}

See the [GAP guidelines](GAP.adoc&#35;_naming) for the proper naming of
GAP addon packages.

### Gnome shell extensions {#_gnome_shell_extensions}

Packages that extend gnome shell SHOULD begin with the prefix
&#96;+gnome-shell-extension-\\&#96;. In particular, this prefix SHOULD
NOT be pluralized (i.e., it SHOULD NOT be
\\&#96;+gnome-shell-extensions&#96;).

### GStreamer plugins {#_gstreamer_plugins}

Packages that extend GStreamer SHOULD begin with the prefix
&#96;+gstreamer1-plugin-\\&#96;. In particular, this prefix SHOULD NOT
be pluralized (i.e., it SHOULD NOT be \\&#96;+gstreamer1-plugins&#96;)
unless it is a collection of plugins (i.e.,
&#96;+gstreamer1-plugins-good+&#96;).

### LibreOffice extensions {#_libreoffice_extensions}

Packages of LibreOffice extensions (thus they rely on LibreOffice as a
parent) have their own naming scheme. They must take into account the
upstream name of the LibreOffice extension. This makes a package name
format of &#96;+libreoffice-\$NAME+&#96;.

### Locales {#_locales}

If a package adds a locale to an existing parent package, then it can
use an underscore in the locale.

&#42;Examples:&#42;

&#8230;. ttfonts-zh_TW (adds zh_TW locale fonts in ttfonts family)
ttfonts-zh_CN (adds zh_CN locale fonts in ttfonts family) &#8230;.

### Lua modules {#_lua_modules}

It is common that multiple versions of Lua are packaged, and each may
have corresponding module packages. Of course the base Lua packages of
course MUST follow the relevant xref:&#35;multiple\[naming guidelines\]
resulting in package names such as &#96;+lua5.1+&#96;.

The module packages SHOULD carry the name of the corresponding base Lua
package (as mandated by the xref:&#35;multiple\[relevant guidelines\])
as a prefix. Some examples:

+----------------------+----------------------+-----------------------+
| module name          | base lua version     | package name          |
+----------------------+----------------------+-----------------------+
| argparse             | (default)            | &#9                   |
|                      |                      | 6;+lua-argparse+&#96; |
+----------------------+----------------------+-----------------------+
| argparse             | 5.1                  | &#96;+                |
|                      |                      | lua5.1-argparse+&#96; |
+----------------------+----------------------+-----------------------+
| sql                  | 5.2                  | &                     |
|                      |                      | #96;+lua5.2-sql+&#96; |
+----------------------+----------------------+-----------------------+

### NGINX modules {#_nginx_modules}

Packages of NGINX modules SHOULD begin with the prefix
&#96;+nginx-mod-\\&#96;. In particular, this prefix SHOULD NOT be
pluralized (i.e., it SHOULD NOT be \\&#96;+nginx-mods&#96;). Some
upstream projects may use &#96;+module+&#96; as a prefix, and this
should be accounted for and replaced accordingly in the package name.

### OBS Studio plugins {#_obs_studio_plugins}

Packages of OBS Studio plugins SHOULD begin with the prefix
&#96;+obs-studio-plugin-\\&#96;. In particular, this prefix SHOULD NOT
be pluralized (i.e., it SHOULD NOT be \\&#96;+obs-studio-plugins&#96;).

### OCaml modules {#_ocaml_modules}

OCaml modules, libraries and syntax extensions SHOULD be named
&#96;+ocaml-foo+&#96;. Examples include: &#96;+ocaml-extlib+&#96;,
&#96;+ocaml-ssl+&#96;.

This naming does not apply to applications written in OCaml, which can
be given their normal name. Examples include: &#96;+mldonkey+&#96;,
&#96;+virt-top+&#96;, &#96;+cduce+&#96;

### Perl modules {#_perl_modules}

Packages of Perl modules (thus they rely on Perl as a parent) use a
slightly different naming scheme. They SHOULD be named
&#96;+perl-CPANDIST+&#96; where &#96;+CPANDIST+&#96; is the name of the
packaged CPAN module distribution (which is almost always also the unit
of Perl module packaging). In the rare cases when a CPAN module
distribution needs to be split into smaller subpackages e.g., due to
dependencies, the extra subpackages SHOULD be named
&#96;+perl-CPANDIST-Something+&#96;.

&#42;Examples:&#42;

&#8230;. perl-Archive-Zip (Archive-Zip is the CPAN distribution name)
perl-Cache-Cache (Cache-Cache is the CPAN distribution name) &#8230;.

### PHP modules {#_php_modules}

For details on the PHP naming scheme, see [Naming
scheme](PHP.adoc&#35;_naming_scheme).

### Python modules {#_python_modules}

Naming of Python modules is fully covered in the [Naming
section](Python.adoc&#35;_naming) of the Python Packaging Guidelines.

In short: The package name SHOULD reflect the upstream name of the
Python module, and SHOULD generally take into account the name of the
module used when importing it in Python scripts. This name will be
prefixed depending on the type of the package.

&#42; A built (i.e. non-SRPM) package for a *Python library* MUST be
named with the prefix &#96;+python3-\\&#96;. \\&#42; A source package
containing primarily a \_Python library\_ MUST be named with the prefix
\\&#96;+python-&#96;.

The character &#96;+++&#96; is reserved for
[Extras](Python.adoc&#35;_extras).

#### Python2 binary package naming {#_python2_binary_package_naming}

Python 2 binary packages MUST be named using a &#96;+python2-+&#96;
prefix. Note that Python 2 is deprecated in Fedora and requires an
explicit exception.

### R modules {#_r_modules}

Packages of R modules (thus they rely on R as a parent) have their own
naming scheme. They SHOULD take into account the upstream name of the R
module. This makes a package name format of &#96;+R-\$NAME+&#96;. When
in doubt, use the name of the module that you type to import it in R.

&#42;Examples:&#42;

&#8230;. R-mAr (R module named mAr) R-RScaLAPACK (R module named
RScaLAPACK) R-waveslim (R module named waveslim) &#8230;.

### Sugar Activities {#_sugar_activities}

The name for all packaged Sugar activities must be prefixed with
&#96;+sugar-+&#96;. For more details, see
[Packaging/SugarActivityGuidelines](SugarActivityGuidelines.xml).

### Tcl/Tk extensions {#_tcltk_extensions}

The name for all packaged Tcl/Tk extensions must be prefixed with
&#96;+tcl-\\&#96;. This rule applies even for Tcl/Tk packages that are
already prefixed with \\&#96;+tcl&#96; in the name. For more details,
see
[Packaging/Tcl&#35;NamingConventions](Tcl.adoc&#35;_naming_conventions).

### TeX {#_tex}

As Fedora has switched TeX environments in the past, TeX packages SHOULD
not be named after the TeX environment (TeX Live or teTeX) but instead
SHOULD carry the prefix &#96;+tex-+&#96;.

## Authorship {#_authorship}

The original author of these guidelines was [Tom \'spot\'
Callaway](https://fedoraproject.org/wiki/TomCallaway). They are now
maintained by the [Packaging
Committee](https://fedoraproject.org/wiki/Packaging_Committee) with
input from the Fedora community.

# Patch status {#_patch_status}

## All patches should have an upstream bug link or comment {#_all_patches_should_have_an_upstream_bug_link_or_comment}

All patches in Fedora spec files &#42;SHOULD&#42; have a comment above
them about their upstream status. Any time you create a patch, it is
best practice to file it in an upstream bug tracker, and include a link
to that in the comment above the patch. For example:

&#8230;. &#35; <https://bugzilla.gnome.org/show_bug.cgi?id=12345> Patch:
gnome-panel-fix-frobnicator.patch &#8230;.

The above is perfectly acceptable; but if you prefer, a brief comment
about what the patch does above can be helpful:

&#8230;. &#35; Don't crash with frobnicator applet &#35;
<https://bugzilla.gnome.org/show_bug.cgi?id=12345> Patch:
gnome-panel-fix-frobnicator.patch &#8230;.

Sending patches upstream and adding this comment will help ensure that
Fedora is acting as a good FLOSS citizen (see [Staying Close to Upstream
Projects](https://docs.fedoraproject.org/en-US/package-maintainers/Staying_Close_to_Upstream_Projects/)).
It will help others (and even you) down the line in package maintenance
by knowing what patches are likely to appear in a new upstream release.

### If upstream doesn't have a bug tracker {#_if_upstream_doesnt_have_a_bug_tracker}

You can indicate that you have sent the patch upstream and any known
status:

&#8230;. &#35; Sent upstream via email 20080407 Patch:
foobar-fix-the-bar.patch &#8230;.

&#8230;. &#35; Upstream has applied this in SVN trunk Patch:
foobar-fix-the-baz.patch &#8230;.

### Fedora-specific (or rejected upstream) patches {#_fedora_specific_or_rejected_upstream_patches}

It may be that some patches truly are Fedora-specific; in that case, say
so:

&#8230;. &#35; This patch is temporary until we land the long term
System.loadLibrary fix in OpenJDK Patch: jna-jni-path.patch &#8230;.

## Why upstream? {#_why_upstream}

Refer [Staying Close to Upstream
Projects](https://docs.fedoraproject.org/en-US/package-maintainers/Staying_Close_to_Upstream_Projects/)

# Per-product Configuration Packaging {#_per_product_configuration_packaging}

In the Fedora.next world, we have a set of curated Fedora Products as
well as the availability of classic Fedora. Historically, we have
maintained a single set of configuration defaults for all Fedora
installs, but different target use-cases have different needs. The goal
of this document is to set out the guidelines for creating per-Product
configuration defaults.

We want to ensure that all packages have sensible defaults for whichever
Product on which they are installed, while also avoiding situations
where users would have some packages installed with one Product's
defaults and some packages with another.

## Requirements {#_requirements}

&#42; All packages MUST have a global default configuration. This
configuration will be used whenever a Product-specific default
configuration is not required. (For example, if a non-Product install is
in use or only Fedora Cloud has a custom configuration and Fedora
Workstation was installed). &#42; Any package that requires a
per-product default configuration MUST provide all alternate
configuration files in the same package. &#42; Any package that requires
a configuration that differs between Products MUST obtain permission
from that Product's Working Group before packaging it.

## Global Default Configuration {#_global_default_configuration}

&#42; The global default configuration MUST be provided by the package
that requires it. &#42; The global default configuration MUST be named
based on the package's normal naming scheme, with the main part of the
name being suffixed by -default. For example, if the package normally
uses &#96;+foo.conf+&#96;, then the global default configuration MUST be
named &#96;+foo-default.conf+&#96;.

## Per-Product Default Configuration {#_per_product_default_configuration}

&#42; For each Product requiring a unique default configuration, the
packager MUST provide a copy of the default configuration file, modified
as appropriate for the specific product. &#42; The product-specific
configuration file MUST be named based on the package's normal naming
scheme, with the main part of the name being suffixed by a dash followed
by the name of the product. For example, if the package normally uses
&#96;+foo.conf+&#96;, then the Server version MUST be named
&#96;+foo-server.conf+&#96;. &#42; If the configuration will be
symlinked in place, the product-specific configuration file MUST be
located in an appropriate part of the &#96;+/etc+&#96; hierarchy. The
divergent config file MUST be specified as
&#96;+%config(noreplace)\\&#96; in \\&#96;%files+&#96; as per the usual
&#96;+/etc+&#96; packaging guidelines. &#42; If the configuration will
be copied in place, the product-specific configuration file MUST be
located in an appropriate part of the &#96;+/usr/share+&#96; hierarchy.
The divergent config file MUST be specified as a normal file in the
&#96;+%files+&#96; section.

## Applying Configuration {#_applying_configuration}

In order to apply the configuration, the packager MUST implement a
mechanism in the &#96;+%posttrans+&#96; section of the specfile that
behaves as follows:

&#42; It MUST first check whether the final config file already exists.
If so, the script MUST make no changes.

\+

``` _rpm-spec
%posttrans
if [ ! -e %{_sysconfdir}/foo/foo.conf ]; then
\&#8230;
fi
```

&#42; Then it MUST use the value of the Fedora &#96;+VARIANT_ID+&#96; to
symlink or copy one of the divergent config files (or the default) to
the final config file location. It will get this value by importing the
contents of &#96;+/etc/os-release+&#96; as shell values. Known values of
this field at the time of this writing are \'atomichost\', \'cloud\',
\'server\' and \'workstation\'. For more detail, see [the os-release(5)
man
page](https://www.freedesktop.org/software/systemd/man/os-release.html&#35;VARIANT_ID=).

\+

``` _rpm-spec
. /etc/os-release || :
case '$VARIANT_ID' in
server)
ln -sf foo-server.conf %{_sysconfdir}/foo/foo.conf || :
;;
\&#42;)
ln -sf foo-default.conf %{_sysconfdir}/foo/foo.conf || :
;;
esac
```

&#42; Lastly, the final config file location MUST be listed in the
&#96;+%files+&#96; section with &#96;+%ghost+&#96;:

\+

``` _rpm-spec
%ghost %config(noreplace) %{_sysconfdir}/foo/foo.conf
```

&#42; For tracking purposes, the package providing the various
configuration files MUST also contain a virtual &#96;+Provides:+&#96;
for each variant configuration that may be applied:

\+

``` _rpm-spec
Provides: variant_config(Atomic.host)
Provides: variant_config(Cloud)
Provides: variant_config(Server)
Provides: variant_config(Workstation)
```

## Example (firewalld) {#_example_firewalld}

We will assume for the sake of demonstration that firewalld will need a
custom configuration for Fedora Server and Fedora Workstation, but that
Fedora Cloud will not require any changes from the global default.

``` _rpm-spec
\&#8230;
Provides: variant_config(Server)
Provides: variant_config(Workstation)
\&#8230;

%posttrans
\&#35; If we don't yet have a symlink or existing file for firewalld.conf,
\&#35; create it. Note: this will intentionally reset the policykit policy
\&#35; at the same time, so they are in sync.
if [ ! -e %{_sysconfdir}/firewalld/firewalld.conf ]; then
\&#35; Import /etc/os-release to get the variant definition
. /etc/os-release || :

case '$VARIANT_ID' in
server)
ln -sf firewalld-server.conf %{_sysconfdir}/firewalld/firewalld.conf || :
ln -sf org.fedoraproject.FirewallD1.server.policy \
%{_datadir}/polkit-1/actions/org.fedoraproject.FirewallD1.policy || :
;;
workstation)
ln -sf firewalld-workstation.conf %{_sysconfdir}/firewalld/firewalld.conf || :
ln -sf org.fedoraproject.FirewallD1.desktop.policy \
%{_datadir}/polkit-1/actions/org.fedoraproject.FirewallD1.policy || :
;;
\&#42;)
ln -sf firewalld-default.conf %{_sysconfdir}/firewalld/firewalld.conf || :
\&#35; The default firewall policy will be the same as Server
ln -sf org.fedoraproject.FirewallD1.server.policy \
%{_datadir}/polkit-1/actions/org.fedoraproject.FirewallD1.policy || :
;;
esac
fi

\&#8230;

%files -f %{name}.lang
\&#8230;
%attr(0750,root,root) %dir %{_sysconfdir}/firewalld
%ghost %config(noreplace) %{_sysconfdir}/firewalld/firewalld.conf
%config(noreplace) %{_sysconfdir}/firewalld/firewalld-default.conf
%config(noreplace) %{_sysconfdir}/firewalld/firewalld-server.conf
%config(noreplace) %{_sysconfdir}/firewalld/firewalld-workstation.conf
\&#8230;
%ghost %{_datadir}/polkit-1/actions/org.fedoraproject.FirewallD1.policy
%{_datadir}/polkit-1/actions/org.fedoraproject.FirewallD1.desktop.policy
%{_datadir}/polkit-1/actions/org.fedoraproject.FirewallD1.server.policy
```

# BuildRequires: pkgconfig(foo) vs. foo-devel {#_buildrequires_pkgconfigfoo_vs_foo_devel}

Fedora packages which use &#96;+pkg-config+&#96; to build against a
library (e.g. \'foo\') on which they depend, &#42;SHOULD&#42; express
their build dependency correctly as &#96;+pkgconfig(foo)+&#96;.

## Rationale {#_rationale}

The build infrastructure for a given package will often locate and use
required libraries by using &#96;+pkg-config+&#96;.

Thus, &#96;+pkgconfig(foo)+&#96; is the true statement of the build
dependency, and is how it should be expressed in the spec file.

For historical reasons, many packages seem to have a hard-coded
\'\\\`BuildRequires: foo-devel\\\`\', with the name of the package which
*currently* provides the required pkgconfig module. This is fragile and
less portable than simply expressing the real dependency. Where package
names change, and/or a required pkgconfig module is later provided by a
*different* package, these hard-coded dependencies break.

Note that it shall still be acceptable to require specific packages by
name if they are required for some reason *other* than a
&#96;+pkg-config+&#96; module that they provide.

## Example {#_example_2}

Packages which build against &#96;+libproxy+&#96; should contain the
following:

&#8230;. BuildRequires: pkgconfig(libproxy-1.0) &#8230;.

&#8230; and *not* the following:

&#8230;. BuildRequires: libproxy-devel &#8230;.

This way, if the &#96;+libproxy-1.0.pc+&#96; pkgconfig module is ever
provided from a differently-named package (such as by PacRunner once its
integration is complete, or by a \'&#96;+libproxy1+&#96;\'
backward-compatibility package as has happened to a number of other
libraries in the past), the dependency will continue to be correct.

# PKCS&#35;11 / Smart-Card Support Guidelines {#_pkcs3511_smart_card_support_guidelines}

These guidelines are relevant to maintainers of packages with smart
cards drivers (PKCS&#35;11 modules), or smart card related tooling. Its
purpose is to bring a consistency in smart card handling on the OS; for
background and motivation see the [current status of PKCS&#35;11 in
Fedora](https://fedoraproject.org/wiki/User:Nmav/Pkcs11Status).

## Registering the modules system-wide {#_registering_the_modules_system_wide}

Any package in Fedora containing a PKCS&#35;11 provider module, intended
to be used outside this package, MUST be registered with
[p11-kit](https://p11-glue.github.io/p11-glue/). For example, the
[OpenSC](https://github.com/OpenSC/OpenSC/wiki) module which supports
most major hardware smart cards, will automatically drop a config file
into the appropriate place and then its module will automatically appear
in well-behaved software which is integrated with the platform and uses
p11-kit properly. The appropriate place in Fedora can be obtained with
&#96;+pkg-config p11-kit-1 \--variable p11_module_configs+&#96; or
&#96;+%{\_datadir}/p11-kit/modules/+&#96;. The dropped file should have
the &#96;.module&#96; suffix and should contain something similar to the
contents below (which is the opensc example).

&#35; This file describes how to load the opensc module &#35; See:
<https://p11-glue.freedesktop.org/doc/p11-kit/config.html>

&#35; This is a relative path, which means it will be loaded from &#35;
the p11-kit default path which is usually \$(libdir)/pkcs11. &#35; Doing
it this way allows for packagers to package opensc for &#35; 32-bit and
64-bit and make them parallel installable module: opensc-pkcs11.so

The provider module, as mentioned in the example below should be
installed at &#96;+%{\_libdir}/pkcs11/+&#96;.

Once a module is registered the tokens/HSMs provided by it should be
listed in the &#96;p11tool&#96; output using the following command:

\$ p11tool \--list-tokens

The packages SHOULD NOT provide the package config &#96;&#42;.pc&#96;
files for the PKCS&#35;11 modules, since the applications are not
supposed to link directly against these libraries. The PKCS&#35;11
module shared object SHOULD NOT be in the -devel subpackage either.

\[&#35;registered\] == How applications take advantage of registered
provider modules

Packages which can potentially use PKCS&#35;11 tokens SHOULD
automatically use the tokens which are present in the system's p11-kit
configuration, rather than needing to have a PKCS&#35;11 provider
explicitly specified. That can be done by applications using the p11-kit
library to get the list of modules, or by applications defaulting to the
p11-kit proxy module (&#96;+%{\_libdir}/p11-kit-proxy.so+&#96;), if no
PKCS&#35;11 provider module was specified by the user. The proxy module,
is a single module wrapping all available registered modules.

\[&#35;specify-card\] == How to specify a specific smart card/HSM

[RFC7512](https://tools.ietf.org/html/rfc7512) defines a \'PKCS&#35;11
URI\' as a standard way to identify tokens and objects. Fedora follows
this standard and applications which refer to tokens such as smart cards
or HSMs, must use RFC7512 to refer to them. Note that an application
must not require the \'\'\'module-name\'\'\' and \'\'\'module-path\'\'\'
URI elements. Compliant with this policy applications should resolve
URIs which do not contain these elements based \[\[&#35;Registered\|on
the registered provider modules\]\]. Applications must not require the
\'slot\' attribute, nor print it, since it is an esoteric PKCS&#35;11
module implementation information that has no meaning for the end-user,
and in several modules its value is not guaranteed to be unique (and may
change for example after system reboot).

\[&#35;specify-object\] == How to specify an object stored in a smart
card/HSM

[RFC7512](https://tools.ietf.org/html/rfc7512) defines a \'PKCS&#35;11
URI\' as a standard way to identify tokens and objects. Fedora follows
this standard and applications which refer to objects stored in smart
cards or HSMs, must use RFC7512 to refer to certificates and private
keys.

In particular when PKCS&#35;11 objects are specified in a textual form
which is visible to the user \'\'(e.g. on the command line or in a
config file)\'\', objects SHOULD be specified in the form of a
PKCS&#35;11 URI as as described in
[RFC7512](https://tools.ietf.org/html/rfc7512).

This form is already accepted by some programs such as the OpenConnect
VPN client. The certificate used in the above examples can be simply
used as a client authentication certificate by adding the command-line
option &#96;-c \'pkcs11:manufacturer=piv_II;id=%01\'&#96;.

# Package Review Guidelines {#_package_review_guidelines}

This is a set of guidelines for Package Reviews. Note that a complete
list of things to check for would be impossible, but every attempt has
been made to make this document as comprehensive as possible. Reviewers
and contributors (packagers) should use their best judgement whenever
items are unclear, and if in doubt, ask on the [Fedora packaging
list](https://lists.fedoraproject.org/admin/lists/packaging.lists.fedoraproject.org/)
.

## Package Review Guidelines {#_package_review_guidelines_2}

Contributors and reviewers MUST follow the [Package Review
Process](https://docs.fedoraproject.org/en-US/package-maintainers/Package_Review_Process/),
with the exceptions listed in the next section

## Package Review Exceptions {#_package_review_exceptions}

The following exceptions apply to the review process linked above

&#42; FPC grants an explicit exemption from the process, as indicated
[here](https://fedoraproject.org/wiki/Packaging_Committee&#35;Review_Process_Exemption_Procedure).
&#42; The package is being created so that multiple versions of the same
package can coexist in the distribution (or coexist between EPEL and
RHEL). The package MUST be properly named according to the [naming
guidelines](Naming.adoc&#35;_multiple_packages_with_the_same_base_name)
and MUST NOT conflict with all other versions of the same package. &#42;
The package exists in both Fedora and RHEL, but the packager wants to
ship it in EPEL under an alternative name (as required by [EPEL
policy](https://fedoraproject.org/wiki/EPEL/GuidelinesAndPolicies&#35;Policy))
to provide a subpackage that exists in Fedora but does not exist (or is
not shipped) in RHEL.

:::: formalpara
::: title
Exemptions which have been explicitly granted:
:::

&#42; fXX-backgrounds
([ticket](https://pagure.io/packaging-committee/issue/1479)): This
package doesn't follow the usual naming conventions for versioned
packages, but a new one is created per Fedora release.
::::

## Relaxed rules for existing components {#_relaxed_rules_for_existing_components}

Some guidelines that apply to \'new\' packages do not need to be applied
when reviewing packages that are only *\'added\'* to the distribution in
the sense that the name of the *source package* is \'new\' but the
component was already available from an existing package, i.e. when

&#42; renaming an existing package, &#42; moving a subcomponent from an
existing package into a separate source package, &#42; adding an
alternative version (\'compat package\') of an existing package, or
&#42; adding an EPEL-only alternative version of an existing package.

For example, it is allowed for a *\'new\'* package like this to depend
on packages marked as &#96;+deprecated()+&#96; because no *actually new*
component will depend on the deprecated package.

## Things To Check On Review {#_things_to_check_on_review}

There are many many things to check for a review. This list is provided
to assist new reviewers in identifying areas that they should look for,
but is by no means complete. Reviewers should use their own good
judgement when reviewing packages. The items listed fall into two
categories: &#42;SHOULD&#42; and &#42;MUST&#42;.

&#42; []{#rpmlint} &#42;MUST&#42;: rpmlint must be run on the source rpm
and all binary rpms the build produces. The output should be posted in
the review. See [Packaging Guidelines: Use
rpmlint](index.adoc&#35;_use_rpmlint). &#42; []{#naming} &#42;MUST&#42;:
The package must be named according to the [Package Naming
Guidelines](Naming.xml). &#42; []{#spec-fie-name} &#42;MUST&#42;: The
spec file name must match the base package &#96;+%{name}\\&#96;, in the
format \\&#96;%{name}.spec+&#96; unless your package has an exemption.
See [Packaging Guidelines: Spec File
Naming](index.adoc&#35;_spec_file_naming). &#42;
[]{#packaging-guidelines} &#42;MUST&#42;: The package must meet the
[Packaging Guidelines](index.xml). &#42; []{#approved-license}
&#42;MUST&#42;: The package must be licensed with a Fedora approved
license and meet the [Licensing Guidelines](LicensingGuidelines.xml).
&#42; []{#license-field} &#42;MUST&#42;: The License field in the
package spec file must match the actual license. See [Licensing
Guidelines: Valid License Short
Names](LicensingGuidelines.adoc&#35;_valid_license_short_names). &#42;
[]{#license-file} &#42;MUST&#42;: If (and only if) the source package
includes the text of the license(s) in its own file, then that file,
containing the text of the license(s) for the package must be included
in &#96;+%license+&#96;. See [Licensing Guidelines: License
Text](LicensingGuidelines.adoc&#35;_license_text). &#42;
[]{#spec-in-american-english} &#42;MUST&#42;: The spec file must be
written in American English. See [Packaging Guidelines: Summary and
description](index.adoc&#35;_summary_and_description). &#42;
[]{#legible-spec} &#42;MUST&#42;: The spec file for the package
&#42;MUST&#42; be legible. See [Packaging Guidelines: Spec
Legibility](index.adoc&#35;_spec_legibility). &#42; []{#build-sources}
&#42;MUST&#42;: The sources used to build the package must match the
upstream source, as provided in the spec URL. Reviewers should use
sha256sum for this task as it is used by the &#96;+sources+&#96; file
once imported into git. If no upstream URL can be specified for this
package, please see the [Source URL Guidelines](SourceURL.xml) for how
to deal with this. &#42; []{#successful-build} &#42;MUST&#42;: The
package &#42;MUST&#42; successfully compile and build into binary rpms
on at least one primary architecture. See [Packaging Guidelines:
Architecture Support](index.adoc&#35;_architecture_support). &#42;
[]{#exclude-arch} &#42;MUST&#42;: If the package does not successfully
compile, build or work on an architecture, then those architectures
should be listed in the spec in &#96;+ExcludeArch+&#96;. Each
architecture listed in &#96;+ExcludeArch+&#96; &#42;MUST&#42; have a bug
filed in bugzilla, describing the reason that the package does not
compile/build/work on that architecture. The bug number &#42;MUST&#42;
be placed in a comment, next to the corresponding
&#96;+ExcludeArch+&#96; line. See [Packaging Guidelines: Architecture
Build Failures](index.adoc&#35;_architecture_build_failures). &#42;
[]{#build-dependencies} &#42;MUST&#42;: All build dependencies must be
listed in &#96;+BuildRequires+&#96;. See [Packaging Guidelines:
Build-Time Dependencies (BuildRequires)](index.adoc&#35;buildrequires).
&#42; []{#locales} &#42;MUST&#42;: The spec file MUST handle locales
properly. This is done by using the &#96;+%find_lang+&#96; macro. Using
&#96;+%{\_datadir}/locale/&#42;+&#96; is strictly forbidden. See
[Packaging Guidelines: Handling Locale
Files](index.adoc&#35;_handling_locale_files). &#42; []{#bundling}
&#42;MUST&#42;: Packages must NOT bundle copies of system libraries. See
[Packaging Guidelines: Bundling and Duplication of System
Libraries](index.adoc&#35;bundling). &#42; []{#relocatable-package}
&#42;MUST&#42;: If the package is designed to be relocatable, the
packager must state this fact in the request for review, along with the
rationalization for relocation of that specific package. Without this,
use of Prefix: /usr is considered a blocker. See [Packaging Guidelines:
Relocatable Packages](index.adoc&#35;_relocatable_packages). &#42;
[]{#directory-ownership} &#42;MUST&#42;: A package must own all
directories that it creates. If it does not create a directory that it
uses, then it should require a package which does create that directory.
See [Packaging Guidelines: File And Directory
Ownership](index.adoc&#35;_file_and_directory_ownership). &#42;
[]{#file-listed-once} &#42;MUST&#42;: A Fedora package must not list a
file more than once in the spec file's %files listings. (Notable
exception: license texts in specific situations)See [Packaging
Guidelines: Duplicate Files](index.adoc&#35;_duplicate_files). &#42;
[]{#premissions} &#42;MUST&#42;: Permissions on files must be set
properly. Executables should be set with executable permissions, for
example. See [Packaging Guidelines: File
Permissions](index.adoc&#35;_file_permissions). &#42;
[]{#consistent-macros} &#42;MUST&#42;: Each package must consistently
use macros. See [Packaging Guidelines: Macros](index.adoc&#35;_macros).
&#42; []{#permisible-content} &#42;MUST&#42;: The package must contain
code, or permissible content. See [What Can Be
Packaged](what-can-be-packaged.xml). &#42; []{#large-documentation}
&#42;MUST&#42;: Large documentation files must go in a -doc subpackage.
(The definition of large is left up to the packager's best judgement,
but is not restricted to size. Large can refer to either size or
quantity). See [Packaging Guidelines:
Documentation](index.adoc&#35;_documentation). &#42; []{#doc-runtime}
&#42;MUST&#42;: If a package includes something as %doc, it must not
affect the runtime of the application. To summarize: If it is in %doc,
the program must run properly if it is not present. See [Packaging
Guidelines: Documentation](index.adoc&#35;_documentation). &#42;
[]{#static-libraries} &#42;MUST&#42;: Static libraries must be in a
-static package. See [Packaging Guidelines: Packaging Static
Libraries](index.adoc&#35;packaging-static-libraries). &#42;
[]{#devel-subpackage} &#42;MUST&#42;: Development files must be in a
-devel package. See [Packaging Guidelines: Devel
Packages](index.adoc&#35;_devel_packages). &#42;
[]{#versioned-devel-require} &#42;MUST&#42;: In the vast majority of
cases, devel packages must require the base package using a fully
versioned dependency: &#96;+Requires: %{name}%{?\_isa} =
%{version}-%{release}\\&#96;. See
xref:index.adoc\\&#35;\_requiring_base_package\[Packaging Guidelines:
Requiring Base Package\]. \\&#42; \[\[la-archives\]\]
\\&#42;MUST\\&#42;: Packages must NOT contain any .la libtool archives,
these must be removed in the spec if they are built. See
xref:index.adoc\\&#35;packaging-static-libraries\[Packaging Guidelines:
Packaging Static Libraries\]. \\&#42; \[\[desktop-file\]\]
\\&#42;MUST\\&#42;: Packages containing GUI applications must include a
%\\{name}.desktop file, and that file must be properly installed with
\\&#96;desktop-file-install\\&#96; in the \\&#96;%install+&#96; section.
If you feel that your packaged GUI application does not need a .desktop
file, you must put a comment in the spec file with your explanation. See
[Packaging Guidelines: Desktop files](index.adoc&#35;_desktop_files).
&#42; []{#file-directory-ownership} &#42;MUST&#42;: Packages must not
own files or directories that are already owned by other packages. The
rule of thumb here is that the first package to be installed should own
the files or directories that other packages may rely upon. This means,
for example, that no package in Fedora should ever share ownership with
any of the files or directories owned by the &#96;+filesystem+&#96; or
&#96;+man+&#96; package. If you feel that you have a good reason to own
a file or directory that another package owns, then please present that
at package review time. See [Packaging Guidelines: File and Directory
Ownership](index.adoc&#35;_file_and_directory_ownership). &#42;
[]{#utf-8} &#42;MUST&#42;: All filenames in rpm packages must be valid
UTF-8. See [Packaging Guidelines: Non-ASCII
Filenames](index.adoc&#35;_non_ascii_filenames). &#42;
[]{#deprecated-packages} &#42;MUST&#42;: Packages being added to the
distribution MUST NOT depend on any packages which have been marked as
being deprecated. See [Deprecating Packages](deprecating-packages.xml).

&#42; []{#upstream-license-file} &#42;SHOULD&#42;: If the source package
does not include license text(s) as a separate file from upstream, the
packager SHOULD query upstream to include it. See [Licensing Guidelines:
License Text](LicensingGuidelines.adoc&#35;_license_text). &#42;
[]{#builds-in-mock} &#42;SHOULD&#42;: The reviewer should test that the
package builds in mock. See [Using Mock to test package
builds](https://fedoraproject.org/wiki/Using_Mock_to_test_package_builds).
&#42; []{#supports-all-architectures} &#42;SHOULD&#42;: The package
should compile and build into binary rpms on all supported
architectures. See [Packaging Guidelines: Architecture
Support](index.adoc&#35;_architecture_support). &#42;
[]{#symbols-are-versioned} &#42;SHOULD&#42;: Shared libraries should
provide versioned symbols (as in
\'libc.so.6(&#42;GLIBC_2.41&#42;)(64bit)\'. Maintainers are encouraged
to work with upstream projects that do not yet provide versioned symbols
to add them. See [Versioned Symbols](C_and_C++.xml) &#42;
[]{#functions-as-described} &#42;SHOULD&#42;: The reviewer should test
that the package functions as described. A package should not segfault
instead of running, for example. &#42; []{#sane-scriplets}
&#42;SHOULD&#42;: If scriptlets are used, those scriptlets must be sane.
This is vague, and left up to the reviewers judgement to determine
sanity. See [Packaging Guidelines:
Scriptlets](index.adoc&#35;_scriptlets). &#42;
[]{#subpackage-versioned-requires} &#42;SHOULD&#42;: Usually,
subpackages other than devel should require the base package using a
fully versioned dependency. See [Packaging Guidelines: Requiring Base
Package](index.adoc&#35;_requiring_base_package). &#42;
[]{#pkgconfig-in-devel} &#42;SHOULD&#42;: The placement of
pkgconfig(.pc) files depends on their usecase, and this is usually for
development purposes, so should be placed in a -devel pkg. A reasonable
exception is that the main pkg itself is a devel tool not installed in a
user runtime, e.g. gcc or gdb. See [Packaging Guidelines: Pkgconfig
Files](index.adoc&#35;_pkgconfig_files_foo_pc). &#42; []{#man-pages}
&#42;SHOULD&#42;: Your package should contain man pages for
binaries/scripts. If it doesn't, work with upstream to add them where
they make sense. See [Packaging Guidelines:
Manpages](index.adoc&#35;_manpages).

## A note on dependencies {#_a_note_on_dependencies}

It is often useful to submit a package for review along with its
dependencies in separate tickets. As long as the submitter sets up the
*Depends on:* and *Blocks:* fields in BugZilla properly, this is not an
issue, and it is perfectly possible to review these packages before the
full dependency chain is in the distribution (by maintaining a local
repository, building and installing the packages locally, or maintaining
a COPR).

However, please keep in mind that you cannot do koji builds unless all
of the build dependencies are met (because you cannot provide additional
dependencies to koji) and when the time comes to build these packages,
they must be built in order and you must wait between builds for the
dependencies to make it into the appropriate branch of the distribution.
This can be automated using side tags and chain builds.

Please also note that while you may actually be able to build a package
because all of its build-time dependencies are met, the package may
still be non-installable (and thus useless) if its *runtime*
dependencies are not met. A package &#42;MUST&#42; not be built if any
of its runtime dependencies are unsatisfied.

# RPM Macros {#_rpm_macros}

RPM provides a rich set of macros to make package maintenance simpler
and consistent across packages. For example, it includes a list of
default path definitions which are used by the build system macros, and
definitions for RPM package build specific directories. They usually
should be used instead of hard-coded directories. It also provides the
default set of compiler flags as macros, which should be used when
compiling manually and not relying on a build system.

## Getting and setting Macros on the command line {#_getting_and_setting_macros_on_the_command_line}

It's possible to let RPM evaluate arbitrary strings containing macros on
the command line by running &#96;rpm \--eval&#96; on the command line:

&#8230;. \$ rpm \--eval \'some text printed on %{\_arch}\' some text
printed on x86_64 &#8230;.

Additionally, values for macros can be temporarily provided (and
overridden) by providing command line options to &#96;rpm&#96; and
&#96;rpmbuild&#96;:

&#8230;. \$ rpm \--define \'test Hello, World!\' \--eval \'%{test}\'
Hello, World! &#8230;.

\[&#35;macros_installation\] == Macros for paths set and used by build
systems

The macros for build system invocations (for example,
&#96;%configure&#96;, &#96;%cmake&#96;, or &#96;%meson&#96;) use the
values defined by RPM to set installation paths for packages. So, it's
usually preferable to not hard-code these paths in spec files either,
but use the same macros for consistency.

The values for these macros can be inspected by looking at
&#96;/usr/lib/rpm/platform/&#42;/macros&#96; for the respective
platform.

The following table lists macros which are widely used in fedora
&#96;.spec&#96; files.

+----------------------+-------------------+---------------------------+
| macro                | definition        | comment                   |
+======================+===================+===========================+
| `%{_sysconfdir}`     | `/etc`            |                           |
+----------------------+-------------------+---------------------------+
| `%{_prefix}`         | `/usr`            | can be defined to         |
|                      |                   | &#96;/app&#96; for        |
|                      |                   | flatpak builds            |
+----------------------+-------------------+---------------------------+
| `%{_exec_prefix}`    | `%{_prefix}`      | default: &#96;/usr&#96;   |
+----------------------+-------------------+---------------------------+
| `%{_includedir}`     | `%{               | default:                  |
|                      | _prefix}/include` | &#96;/usr/include&#96;    |
+----------------------+-------------------+---------------------------+
| `%{_bindir}`         | `%{_              | default:                  |
|                      | exec_prefix}/bin` | &#96;/usr/bin&#96;        |
+----------------------+-------------------+---------------------------+
| `%{_libdir}`         | `%{_exec          | default:                  |
|                      | _prefix}/%{_lib}` | &#96;+/usr/%{\_lib}+&#96; |
+----------------------+-------------------+---------------------------+
| `%{_libexecdir}`     | `%{_exec          | default:                  |
|                      | _prefix}/libexec` | &#96;/usr/libexec&#96;    |
+----------------------+-------------------+---------------------------+
| `%{_datadir}`        | `%{_datarootdir}` | default:                  |
|                      |                   | &#96;/usr/share&#96;      |
+----------------------+-------------------+---------------------------+
| `%{_infodir}`        | `%{_d             | default:                  |
|                      | atarootdir}/info` | &#96;/usr/share/info&#96; |
+----------------------+-------------------+---------------------------+
| `%{_mandir}`         | `%{_              | default:                  |
|                      | datarootdir}/man` | &#96;/usr/share/man&#96;  |
+----------------------+-------------------+---------------------------+
| `%{_docdir}`         | `%{_datadir}/doc` | default:                  |
|                      |                   | &#96;/usr/share/doc&#96;  |
+----------------------+-------------------+---------------------------+
| `%{_rundir}`         | `/run`            |                           |
+----------------------+-------------------+---------------------------+
| `%{_localstatedir}`  | `/var`            |                           |
+----------------------+-------------------+---------------------------+
| `%{_sharedstatedir}` | `/var/lib`        |                           |
+----------------------+-------------------+---------------------------+
| `%{_lib}`            | `lib64`           | &#96;lib&#96; on 32bit    |
|                      |                   | platforms                 |
+----------------------+-------------------+---------------------------+

Some seldomly used macros are listed below for completeness. Old
&#96;.spec&#96; files might still use them, and there might be cases
where they are still needed.

+----------------------+-------------------+---------------------------+
| macro                | definition        | comment                   |
+======================+===================+===========================+
| `%{_datarootdir}`    | `                 | default:                  |
|                      | %{_prefix}/share` | &#96;/usr/share&#96;      |
+----------------------+-------------------+---------------------------+
| `%{_var}`            | `/var`            |                           |
+----------------------+-------------------+---------------------------+
| `%{_sbindir}`        | `sa               | historically              |
|                      | me as %{_bindir}` | &#96;/usr/sbin&#96;, now  |
|                      |                   | &#96;/usr/bin&#96;,       |
|                      |                   | provided for              |
|                      |                   | compatibility             |
+----------------------+-------------------+---------------------------+
| `%{_tmppath}`        | `%{_var}/tmp`     | default:                  |
|                      |                   | &#96;/var/tmp&#96;        |
+----------------------+-------------------+---------------------------+
| `%{_usr}`            | `/usr`            |                           |
+----------------------+-------------------+---------------------------+
| `%{_usrsrc}`         | `%{_usr}/src`     | default:                  |
|                      |                   | &#96;/usr/src&#96;        |
+----------------------+-------------------+---------------------------+
| `%{_initddir}`       | `%{_sysconf       | default:                  |
|                      | dir}/rc.d/init.d` | &                         |
|                      |                   | #96;/etc/rc.d/init.d&#96; |
+----------------------+-------------------+---------------------------+
| `%{_initrddir}`      | `%{_initddir}`    | old misspelling, provided |
|                      |                   | for compatiblity          |
+----------------------+-------------------+---------------------------+

## Macros set for the RPM (and SRPM) build process {#_macros_set_for_the_rpm_and_srpm_build_process}

RPM also exposes the locations of several directories that are relevant
to the package build process via macros.

The only macro that's widely used in &#96;.spec&#96; files is
&#96;+%{buildroot}+&#96;, which points to the root of the installation
target directory. It is used for setting &#96;DESTDIR&#96; in the
package's &#96;%install&#96; step.

The other macros are usually only used outside &#96;.spec&#96; files.
For example, they are set by &#96;fedpkg&#96; to override the default
directories.

+-----------------+------------------------------------------+---------+
| macro           | definition                               | comment |
+=================+==========================================+=========+
| `%{buildroot}`  | `%{_buildrootdir}                        | same as |
|                 | /%{name}-%{version}-%{release}.%{_arch}` | &#96;\$ |
|                 |                                          | BUILDRO |
|                 |                                          | OT&#96; |
+-----------------+------------------------------------------+---------+
| `%{_topdir}`    | `%{getenv:HOME}/rpmbuild`                |         |
+-----------------+------------------------------------------+---------+
| `%{_builddir}`  | `%{_topdir}/BUILD`                       |         |
+-----------------+------------------------------------------+---------+
| `%{_rpmdir}`    | `%{_topdir}/RPMS`                        |         |
+-----------------+------------------------------------------+---------+
| `%{_sourcedir}` | `%{_topdir}/SOURCES`                     |         |
+-----------------+------------------------------------------+---------+
| `%{_specdir}`   | `%{_topdir}/SPECS`                       |         |
+-----------------+------------------------------------------+---------+
| `%{_srcrpmdir}` | `%{_topdir}/SRPMS`                       |         |
+-----------------+------------------------------------------+---------+
| `%{             | `%{_topdir}/BUILDROOT`                   |         |
| _buildrootdir}` |                                          |         |
+-----------------+------------------------------------------+---------+

## Macros providing compiler and linker flags {#_macros_providing_compiler_and_linker_flags}

The default build flags for binaries on fedora are available via macros.
They are used by the build system macros to setup the build environment,
so it is usually not necessary to use them directly --- except, for
example, when doing bare bones compilation with &#96;gcc&#96; directly.

The set of flags listed below reflects the current state of fedora 42 on
a &#96;x86_64&#96; machine, as defined in the file
&#96;/usr/lib/rpm/redhat/macros&#96;.

The &#96;+%{optflags}+&#96; macro contains flags that determine
&#96;CFLAGS&#96;, &#96;CXXFLAGS&#96;, &#96;FFLAGS&#96;, etc.

The current definitions of these values can be found in the
&#96;redhat-rpm-config&#96; package, in the [build flags
documentation](https://src.fedoraproject.org/rpms/redhat-rpm-config/blob/master/f/buildflags.md).

&#8230;. \$ rpm \--eval \'%{optflags}\' -O2 -flto=auto -ffat-lto-objects
-fexceptions -g -grecord-gcc-switches -pipe -Wall
-Wno-complain-wrong-lang -Werror=format-security
-Wp,-U_FORTIFY_SOURCE,-D_FORTIFY_SOURCE=3 -Wp,-D_GLIBCXX_ASSERTIONS
-specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -fstack-protector-strong
-specs=/usr/lib/rpm/redhat/redhat-annobin-cc1 -m64 -march=x86-64
-mtune=generic -fasynchronous-unwind-tables -fstack-clash-protection
-fcf-protection -mtls-dialect=gnu2 -fno-omit-frame-pointer
-mno-omit-leaf-frame-pointer &#8230;.

The value of the &#96;LDFLAGS&#96; environment variable set by build
systems is determined by the &#96;+%{build_ldflags}+&#96; macro:

&#8230;. \$ rpm -E \'%{build_ldflags}\' -Wl,-z,relro -Wl,\--as-needed
-Wl,-z,pack-relative-relocs -Wl,-z,now
-specs=/usr/lib/rpm/redhat/redhat-hardened-ld
-specs=/usr/lib/rpm/redhat/redhat-annobin-cc1 -Wl,\--build-id=sha1
&#8230;.

# &#96;+\$RPM_SOURCE_DIR+&#96; or &#96;+%{\_sourcedir}+&#96; {#_96rpm_source_dir96_or_96_sourcedir96}

Packages which use files itemized as &#96;+Source&#35;+&#96; files, must
refer to those files by their &#96;+%{SOURCE&#35;}\\&#96; macro name,
and must not use \\&#96;\$RPM_SOURCE_DIR+&#96; or
&#96;+%{\_sourcedir}+&#96; to refer to those files.

This is done to ensure that Fedora SRPMS are properly generated. If a
&#96;+Source&#35;+&#96; item is renamed, a spec which refers to its old
name may succeed locally (because the file is still in
&#96;+%{\_sourcedir}+&#96; along with the new file), but the proper file
will not be included in the SRPM.

&#42;Incorrect Use:&#42;

&#8230;. Source: php.conf Source: php.ini Source: macros.php

&#8230;

install -m 644 \$RPM_SOURCE_DIR/php.conf
\$RPM_BUILD_ROOT/etc/httpd/conf.d sed -e
\'s/@PHP_APIVER@/%{apiver}/;s/@PHP_ZENDVER@/%{zendver}/;s/@PHP_PDOVER@/%{pdover}/\'
\\ &lt; \$RPM_SOURCE_DIR/macros.php &gt; macros.php &#8230;.

&#42;Correct Use:&#42;

&#8230;. Source1: php.conf Source2: php.ini Source3: macros.php

&#8230;

install -m 644 %{SOURCE1} \$RPM_BUILD_ROOT/etc/httpd/conf.d sed -e
\'s/@PHP_APIVER@/%{apiver}/;s/@PHP_ZENDVER@/%{zendver}/;s/@PHP_PDOVER@/%{pdover}/\'
\\ &lt; %{SOURCE3} &gt; macros.php &#8230;.

## Exceptions {#_exceptions}

When there is an available list of supplementary source files, it is
permissible to use this list in conjunction with
&#96;+%{\_sourcedir}+&#96; to simplify operations on those supplementary
source files.

An example of this from the kde-l10n package:

&#8230;. for i in \$(cat %{SOURCE1000}) ; do echo \$i \| grep -v
\'\^&#35;\' &amp;&amp; \\ bzip2 -dc
%{\_sourcedir}/%{name}-\$i-%{version}.tar.bz2 \| tar -xf - done &#8230;.

where &#96;+Source1000: subdirs-kde-l10n+&#96; is a list provided by
upstream of all the languages supported, and there are \~50
&#96;+SourceN:+&#96; tags, which can vary from version from version, but
match the languages listed in &#96;+Source1000+&#96;, for the tarballs
provided by upstream.

# Scriptlets {#_scriptlets}

RPM spec files have several sections which allow packages to run code on
installation and removal. These bits of code are called scriptlets and
are mostly used to update the running system with information from the
package. This page offers a quick overview of RPM scriptlets and a
number of common recipes for scriptlets in packages. For a more complete
treatment of scriptlets, please see the [Maximum RPM
book](https://ftp.osuosl.org/pub/rpm/max-rpm/).

The version of RPM in Fedora also has functionality to automatically run
scripts when files are placed in certain locations. (See
[1](https://rpm-software-management.github.io/rpm/manual/file_triggers.html).)
This potentially obviates the need for most of the scriptlets on this
page, but is not currently implemented in all cases where it could be.

Packages MUST NOT rely on writing to stdout / stderr in RPM scriptlets
for the purpose of communicating non-fatal issues, warnings, or other
messages to the user.

## Default Shell {#_default_shell}

In Fedora, all scriptlets can safely assume they are running under the
bash shell unless a different language has been specified.

## Syntax {#_syntax}

The basic syntax is similar to the %build, %install, and other sections
of the rpm spec file. The scripts support a special flag, &#96;+-p+&#96;
which allows the scriptlet to invoke a single program directly rather
than having to spawn a shell to invoke the programs. (i.e., &#96;+%post
-p /usr/bin/ldconfig+&#96;)

When scriptlets are called, they will be supplied with an argument. This
argument, accessed via \$1 (for shell scripts) is the number of packages
of this name which will be left on the system when the action completes.
So for the common case of install, upgrade, and uninstall we have:

+-----------------+-----------------+-----------------+-----------------+
|                 | install         | upgrade         | uninstall       |
+-----------------+-----------------+-----------------+-----------------+
| &#96;+          | &#96;+\$1 ==    | &#96;+\$1 ==    | (N/A)           |
| %pretrans+&#96; | 1+&#96;         | 2+&#96;         |                 |
+-----------------+-----------------+-----------------+-----------------+
| &               | &#96;+\$1 ==    | &#96;+\$1 ==    | (N/A)           |
| #96;+%pre+&#96; | 1+&#96;         | 2+&#96;         |                 |
+-----------------+-----------------+-----------------+-----------------+
| &#              | &#96;+\$1 ==    | &#96;+\$1 ==    | (N/A)           |
| 96;+%post+&#96; | 1+&#96;         | 2+&#96;         |                 |
+-----------------+-----------------+-----------------+-----------------+
| &#9             | (N/A)           | &#96;+\$1 ==    | &#96;+\$1 ==    |
| 6;+%preun+&#96; |                 | 1+&#96;         | 0+&#96;         |
+-----------------+-----------------+-----------------+-----------------+
| &#96            | (N/A)           | &#96;+\$1 ==    | &#96;+\$1 ==    |
| ;+%postun+&#96; |                 | 1+&#96;         | 0+&#96;         |
+-----------------+-----------------+-----------------+-----------------+
| &#96;+%         | &#96;+\$1 ==    | &#96;+\$1 ==    | (N/A)           |
| posttrans+&#96; | 1+&#96;         | 2+&#96;         |                 |
+-----------------+-----------------+-----------------+-----------------+

Note that these values will vary if there are multiple versions of the
same package installed (This mostly occurs with parallel installable
packages such as the kernel and multilib packages. However, it can also
occur when errors prevent a package upgrade from completing.) So it is a
good idea to use this construct:

``` rpm-spec
%pre
if [ $1 -gt 1 ] ; then
fi
```

for &#96;+%pre+&#96; and &#96;+%post+&#96; scripts rather than checking
that it equals 2.

All scriptlets MUST exit with the zero exit status. Because RPM in its
default configuration does not execute shell scriptlets with the
&#96;+-e+&#96; argument to the shell, excluding explicit
&#96;+exit+&#96; calls (frowned upon with a non-zero argument!), the
exit status of the last command in a scriptlet determines its exit
status. Most commands in the snippets in this document have a \'\\\`\|\|
:\\\`\' appended to them, which is a generic trick to force the zero
exit status for those commands whether they worked or not. Usually the
most important bit is to apply this to the last command executed in a
scriptlet, or to add a separate command such as plain \'\\\`:\\\`\' or
\'\\\`exit 0\\\`\' as the last one in a scriptlet. Note that depending
on the case, other error checking/prevention measures may be more
appropriate.

Non-zero exit codes from scriptlets can break installs/upgrades/erases
such that no further actions will be taken for that package in a
transaction (see &lt;&lt;Ordering&gt;&gt;), which may for example
prevent an old version of a package from being erased on upgrades,
leaving behind duplicate rpmdb entries and possibly stale, unowned files
on the filesystem. There are some cases where letting the transaction to
proceed when some things in scriptlets failed may result in partially
broken setup. It is however often limited to that package only whereas
letting a transaction to proceed with some packages dropped out on the
fly is more likely to result in broader system wide problems.

\[&#35;ordering\] == Ordering

The scriptlets in &#96;+%pre+&#96; and &#96;+%post+&#96; are
respectively run before and after a package is installed. The scriptlets
&#96;+%preun+&#96; and &#96;+%postun+&#96; are run before and after a
package is uninstalled. The scriptlets &#96;+%pretrans+&#96; and
&#96;+%posttrans+&#96; are run at start and end of a transaction. On
upgrade, the scripts are run in the following order:

1.  &#96;+%pretrans+&#96; of new package

2.  &#96;+%pre+&#96; of new package

3.  (package install)

4.  &#96;+%post+&#96; of new package

5.  &#96;+%triggerin+&#96; of other packages (set off by installing new
    package)

6.  &#96;+%triggerin+&#96; of new package (if any are true)

7.  &#96;+%triggerun+&#96; of old package (if it's set off by
    uninstalling the old package)

8.  &#96;+%triggerun+&#96; of other packages (set off by uninstalling
    old package)

9.  &#96;+%preun+&#96; of old package

10. (removal of old package)

11. &#96;+%postun+&#96; of old package

12. &#96;+%triggerpostun+&#96; of old package (if it's set off by
    uninstalling the old package)

13. &#96;+%triggerpostun+&#96; of other packages (if they're set off by
    uninstalling the old package)

14. &#96;+%posttrans+&#96; of new package

\[&#35;pretrans\] === The &#96;+%pretrans+&#96; Scriptlet

Note that the &#96;+%pretrans+&#96; scriptlet will, in the particular
case of system installation, run before anything at all has been
installed. This implies that it cannot have any dependencies at all. For
this reason, &#96;+%pretrans+&#96; is best avoided, but if used it MUST
(by necessity) be written in Lua. See
<https://rpm-software-management.github.io/rpm/manual/lua.html> for more
information.

## Writing Scriptlets {#_writing_scriptlets}

Here are some tips for writing good scriptlets:

### Saving state between scriptlets {#_saving_state_between_scriptlets}

Sometimes a scriptlet needs to save some state from an earlier running
scriptlet in order to use it at a later running scriptlet. This is
especially common when trying to optimize the scriptlets. Examples:

&#42; If a &#96;+%posttrans+&#96; needs to de-register some piece of
information when upgrading but the file that has that information is
removed when the old package is removed the scriptlets need to save that
file during &#96;+%pre+&#96; or &#96;+%post+&#96; so that the script in
&#96;+%posttrans+&#96; can access it.

&#42; If we only want the program in &#96;+%posttrans+&#96; to do its
work once per-transaction, we may need to write out a flag file so that
the &#96;+%posttrans+&#96; knows whether to perform an action.

To address these issues scriptlets that run earlier need to write out
information that is used in &#96;+%posttrans+&#96;. We recommend using a
subdirectory of &#96;+%{\_localstatedir}/lib/rpm-state/\\&#96; for that.
For instance, the eclipse plugin scripts touch a file in
\\&#96;%{\_localstatedir}/lib/rpm-state/eclipse/\\&#96; when they\'re
installed. The \\&#96;%posttrans+&#96; runs a script that checks if that
file exists. If it does, it performs its action and then deletes the
file. That way the script only performs its action once per transaction.

### Macros {#_macros}

If RPM file triggers are not appropriate, complex scriptlets which are
shared between multiple packages MAY be placed in RPM macros. This has
two benefits:

&#42; The standard package authors only have to remember the macros, not
the complex stuff that it does

&#42; The macros\' implementations may change without having to update
the package

When writing the macros, the FPC will still want to review the macros
(and perhaps include the implementation of the macros in the guideline
to show packagers what's happening behind the scenes).

One principle that the FPC follows is that macros generally don't
contain the start of scriptlet tags (for instance, &#96;+%pre+&#96;)
because this makes it difficult to do additional work in the scriptlet.
This also means that a single macro can not be defined to do things in
both &#96;+%pre+&#96; and &#96;+%post+&#96;. Instead, write one macro
that performs the actions in &#96;+%pre+&#96; and a separate macro that
performs the actions in &#96;+%post+&#96;. This principle makes it so
that all spec files can use your macros in the same manner even if they
already have a &#96;+%pre+&#96; or &#96;+%post+&#96; defined.

Of course, in the above situation it is better to use RPM file triggers
if at all possible.

## Snippets {#_snippets}

Some scriptlets to use in specific situations.

### Linker Configuration Files {#_linker_configuration_files}

Packages which place linker configuration files in
&#96;+/etc/ld.so.conf.d+&#96; MUST call ldconfig in &#96;+%post+&#96;
and &#96;+%postun+&#96; (on all Fedora releases) even if they install no
actual libraries. They MUST NOT use the &#96;+%ldconfig+&#96;,
&#96;+%ldconfig_post+&#96;, &#96;+%ldconfig_postun+&#96; or
&#96;+%ldconfig_scriptlets+&#96; macros to do this, since these macros
do not have any effect on Fedora. Instead simply call
&#96;+ldconfig+&#96; directly in both &#96;+%post+&#96; and
&#96;+%postun+&#96; as well as adding the necessary dependencies when
necessary:

``` rpm-spec
%post -p /usr/bin/ldconfig
%postun -p /usr/bin/ldconfig
```

or, as part of existing &#96;+%post+&#96; or &#96;+%postun+&#96;
scriptlets:

``` rpm-spec
Requires(post): /usr/bin/ldconfig
Requires(postun): /usr/bin/ldconfig
[\&#8230;]
%post
[\&#8230;]
ldconfig
[\&#8230;]
%postun
[\&#8230;]
ldconfig
[\&#8230;]
```

If the configuration file added to &#96;+/etc/ld.so.conf.d+&#96;
specifies a directory into which other packages may install files, and
that directory is not located in the directory hierarchy beneath one of
&#96;+/lib+&#96;, &#96;+/usr/lib+&#96;, &#96;+/lib64+&#96; or
&#96;+/usr/lib64+&#96;, then the package adding the configuration file
MUST also include the following file triggers which cause ldconfig to be
run automatically when necessary:

``` rpm-spec
%transfiletriggerin -P 2000000 -- DIRECTORIES
ldconfig

%transfiletriggerpostun -P 2000000 -- DIRECTORIES
ldconfig
```

Replace &#96;+DIRECTORIES+&#96; with the space-separated list of
directories which the package adds to the library search path via the
configuration files in &#96;+/etc/ld.so.conf.d+&#96;.

### Users and groups {#_users_and_groups}

These are discussed on a [separate page](UsersAndGroups.xml).

### GConf {#_gconf}

The legacy GNOME 2 configuration system (still used by only a handful of
packages) is documented for posterity on [another
page](ScriptletsGConf.xml).

### Systemd {#_systemd}

Packages containing systemd unit files need to use scriptlets to ensure
proper handling of those services. Services can either be enabled or
disabled by default. To determine which case your specific service falls
into, please refer to FESCo's policy [here](DefaultServices.xml). On
upgrade, a package may only restart a service if it is running; it may
not start it if it is off. Also, the service may not enable itself if it
is currently disabled.

#### Scriptlets {#_scriptlets_2}

The systemd package provides a set of helper macros to handle systemd
scriptlet operations. These macros support systemd \'presets\', as
documented in
[systemd.preset(5)](https://www.freedesktop.org/software/systemd/man/systemd.preset.html).

``` rpm-spec
BuildRequires: systemd-rpm-macros

[\&#8230;]
%post
%systemd_post apache-httpd.service

%preun
%systemd_preun apache-httpd.service

%postun
%systemd_postun_with_restart apache-httpd.service
```

Some services do not support being restarted (e.g. D-Bus and various
storage daemons). If your service should not be restarted upon upgrade,
but should be reloaded instead, then use the following
&#96;+%postun+&#96; scriptlet instead of the one shown above:

``` rpm-spec
%postun
%systemd_postun_with_reload apache-httpd.service
```

If your service should not be restarted or reloaded, then use the
following &#96;+%postun+&#96; scriptlet instead:

``` rpm-spec
%postun
%systemd_postun apache-httpd.service
```

Those macros accept multiple unit name arguments. It is better to use a
single invocation to reduce the number of calls.

If your package includes one or more systemd units that need to be
enabled by default on package installation, they MUST be covered by the
[Fedora preset policy](DefaultServices.xml).

##### User units {#_user_units}

There are additional macros for user units (those installed under
&#96;+%\_userunitdir+&#96;) that should be used similarly to those for
system units. These enable and disable user units according to presets,
and are &#96;+%systemd_user_post+&#96; (to be used in &#96;+%post+&#96;)
and &#96;+%systemd_user_preun+&#96; (to be used in &#96;+%preun+&#96;).

``` rpm-spec
BuildRequires: systemd-rpm-macros

[\&#8230;]
%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%postun
%systemd_user_postun_with_restart %{name}.service
%systemd_user_postun_with_reload %{name}.service
%systemd_user_postun %{name}.service
```

Macros &#96;+%systemd_user_postun_with_restart+&#96; and
&#96;+%systemd_user_postun_with_reload+&#96; iterate over the running
user manager instances and request the restart and reload operations for
the specified units in each one.

##### Dependencies on the systemd package {#_dependencies_on_the_systemd_package}

If package scriptlets call other systemd tools, for example
&#96;systemd-tmpfiles&#96;, the package SHOULD declare appropriate
dependencies. The &#96;+%{?systemd_requires}+&#96; macro is a shortcut
to require systemd for the &#96;%post&#96;, &#96;%preun&#96;, and
&#96;%postun&#96; scriptlets. Note that those dependencies are
&#42;&#42;not&#42;&#42; required for the
&#96;%systemd\_{post,preun,postun_with_restart,user_post,user_preun}&#96;
macros listed above.

If the package wants to use systemd tools if they are available, but
does not want to declare a dependency, then the
&#96;+%{?systemd_ordering}\\&#96; macro MAY be used as a weaker form of
\\&#96;%{?systemd_requires}+&#96; that only declares an ordering during
an RPM transaction.

:::: note
::: title
:::

The macros take the form &#96;+%{?systemd_requires}\\&#96; instead of
\\&#96;%systemd_requires+&#96; to allow the specfile to parse properly
in the case where the systemd macros have yet to be installed.
::::

##### Macro details {#_macro_details}

For details on what these macros evaluate to, refer to the following
sources:
[macros.systemd.in](https://github.com/systemd/systemd/blob/master/src/rpm/macros.systemd.in),
[triggers.systemd.in](https://github.com/systemd/systemd/blob/master/src/rpm/triggers.systemd.in)
and
[daemon(7)](https://www.freedesktop.org/software/systemd/man/daemon.html).

### Shells {#_shells}

&#96;+/etc/shells+&#96; is a text file which controls whether an
application can be used as a system login shell of users. It contains
the set of valid shells which can be used in the system. If you are
packaging a new shell, you need to add entries to this file that
reference the added shells. See: &#96;+man 5 SHELLS+&#96; for more
information.

As this file can be edited by sysadmins, we need to first determine if
relevant lines are already in the file. If they don't already exist then
we just need to echo the shell's binary path to the file. Since the
UsrMove Feature in Fedora 17 made &#96;+/bin+&#96; a symlink to
&#96;+/usr/bin+&#96; we need to place both paths into the
&#96;+/etc/shells+&#96; file. Here is an example of the scriptlet to
package with shell named \'foo\':

``` rpm-spec
%post
if [ '$1' = 1 ]; then
if [ ! -f %{_sysconfdir}/shells ] ; then
echo '%{_bindir}/foo' \&gt; %{_sysconfdir}/shells
echo '/bin/foo' \&gt;\&gt; %{_sysconfdir}/shells
else
grep -q '^%{_bindir}/foo$' %{_sysconfdir}/shells || echo '%{_bindir}/foo' \&gt;\&gt; %{_sysconfdir}/shells
grep -q '^/bin/foo$' %{_sysconfdir}/shells || echo '/bin/foo' \&gt;\&gt; %{_sysconfdir}/shells
fi

%postun
if [ '$1' = 0 ] \&amp;\&amp; [ -f %{_sysconfdir}/shells ] ; then
sed -i '\!^%{_bindir}/foo$!d' %{_sysconfdir}/shells
sed -i '\!^/bin/foo$!d' %{_sysconfdir}/shells
fi
```

# Referencing Source {#_referencing_source}

One of the design goals of rpm is to cleanly separate upstream source
from vendor modifications. For the Fedora packager, this means that
sources used to build a package should be the vanilla sources available
from upstream. To help reviewers and QA scripts verify this, the
packager needs to indicate where a reviewer can find the source that was
used to make the rpm.

The most common case is where upstream distributes source as a
&#96;tar.gz&#96;, &#96;tar.bz2&#96; or &#96;zip&#96; archive that we can
download from an upstream website. In these cases you must use a full
URL to the package in the &#96;Source:&#96; line. For example:

&#8230;. Source:
[https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz](https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz)

Source:
<https://ftp.gnome.org/pub/GNOME/sources/gnome-common/2.12/gnome-common-2.12.0.tar.bz2>
&#8230;.

:::: note
::: title
Smallest Compressed Archive
:::

If the upstream source archive is available in multiple compressed
formats that our tools can decompress, it's best to use the one that is
smallest in size. This ensures the smallest source rpm to save space on
the mirrors and downloads of source RPM packages.
::::

## Using Forges (Hosted Revision Control) {#_using_forges_hosted_revision_control}

Any software publishing website, permitting the download of source
archives via normalized URLs, that can be deduced from a project root
URL and version, commit, tag, scm, extension... values is a *"forge"*
that can be supported by the &#96;redhat-rpm-config&#96;
&#96;+%{forgemeta}\\&#96; macro. Common Forge examples are \_GitLab\_
and \_GitHub\_. \\&#96;%{forgemeta}+&#96; centralizes and abstracts our
knowledge about those forges, so packagers do not have to handle
download quirks manually.

&#96;+%{forgemeta}\\&#96; makes it easy to switch from release to tag to
commit source archives. Using \\&#96;%{forgemeta}+&#96;, forge download
URLs or guideline changes are propagated to spec files without manual
refactoring.

When those changes result in a different naming or structure of the
source archive, the source file needs to be uploaded to the build system
before rebuilding existing spec files. That is the main drawback of
using &#96;+%{forgemeta}+&#96;.

The following examples show how to use the Forge macros in various
situations.

### Release Example {#_release_example}

:::: formalpara
::: title
spectemplate-forge-release.spec
:::
::::

### Tag Example {#_tag_example}

:::: formalpara
::: title
spectemplate-forge-tag.spec
:::
::::

### Commit Example {#_commit_example}

:::: formalpara
::: title
spectemplate-forge-commit.spec
:::
::::

### Branch Example {#_branch_example}

:::: formalpara
::: title
spectemplate-forge-branch.spec
:::
::::

### Multiple Sources Example {#_multiple_sources_example}

:::: formalpara
::: title
spectemplate-forge-multi.spec
:::
::::

## Using Revision Control {#_using_revision_control}

In some cases you may want to pull sources from upstream's revision
control system because there have been many changes since the last
release and you think that a tarball that you generate from there will
more accurately show how the package relates to upstream's development.
Here's how you can use a comment to show where the source came from:

&#8230;. &#35; The source for this package was pulled from upstream's
vcs. Use the &#35; following commands to generate the tarball: &#35; svn
export -r 250 <https://www.example.com/svn/foo/trunk> foo-20070221 &#35;
tar -cJvf foo-20070221.tar.xz foo-20070221 Source: foo-20070221.tar.xz
&#8230;.

When pulling from revision control, please remember to use a
Name-version-release compatible with the [Versioning](Versioning.xml)
Guidelines. In particular, check the section on [Complex
versioning](Versioning.adoc&#35;_complex_versioning).

\[&#35;when-upstream-uses-prohibited-code\] == When Upstream uses
Prohibited Code

Some upstream packages include patents or trademarks that we are not
allowed to ship even as source code. In these cases you have to modify
the source tarball to remove this code before you even upload it to the
build system. Here's an example of using a script to document how you
went from the upstream tarball to the one included in the package:

From the spec:

&#8230;. Source: libfoo-1.0-nopatents.tar.gz &#35; libfoo contains
patented code that we cannot ship. Therefore we use &#35; this script to
remove the patented code before shipping it. &#35; Download the upstream
tarball and invoke this script while in the &#35; tarball's directory:
&#35; ./generate-tarball.sh 1.0 Source1: generate-tarball.sh &#8230;.

generate-tarball.sh:

&#8230;. &#35;!/bin/sh

VERSION=\$1

tar -xzvf libfoo-\$VERSION.tar.gz rm
libfoo-\$VERSION/src/patentedcodec.c sed -i -e \'s/patentedcodec.c//\'
libfoo-\$VERSION/src/Makefile

tar -czvf libfoo-\$VERSION-nopatents.tar.gz libfoo-\$VERSION &#8230;.

## Python Packages (pypi) {#_python_packages_pypi}

As PyPI has moved to storing files in directories which change depending
on the file being stored, it is rather unpleasant to use in a
&#96;Source:&#96; URL. Instead, files.pythonhosted.org can be used
trough the &#96;+%{pypi_source}+&#96; macro, followed by the project
name.

&#8230;. Source: %{pypi_source foo} &#8230;.

See more about the macro in the [Python
guidelines](Python.adoc&#35;_source_files_from_pypi).

## Sourceforge.net {#_sourceforge_net}

For packages hosted on sourceforge, use

&#8230;. Source:
[https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz](https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz)
&#8230;.

changing &#96;.tar.gz&#96; to whatever matches the upstream
distribution. Note that we are using &#96;downloads.sourceforge.net&#96;
instead of an arbitrarily chosen mirror. You may use the package
name/package version instead of the &#96;+%{name}\\&#96; and
\\&#96;%{version}+&#96; macros, of course.

Please note that the correct url is
&#96;+downloads.sourceforge.net+&#96;, and &#42;NOT&#42;
&#96;+download.sourceforge.net+&#96;.

## Git Hosting Services {#_git_hosting_services}

If the upstream &#42;does&#42; create tarballs you should use them as
tarballs provide an easier trail for people auditing the packages.

Git web-based hosting services provide a mechanism to create tarballs on
demand, either from a specific commit revision, or from a specific tag.
If the upstream does not create tarballs for releases, you can use this
mechanism to produce them.

The full 40-character hash and associated git tag may be obtained by
issuing the following git command:

[git ls-remote](https://git-scm.com/docs/git-ls-remote)
https://HOSTING-SERVICE/OWNER/%{name}.git

&#8230;. HOSTING-SERVICE: name of the service, i.e. \'github.com\',
\'bitbucket.org\', \'gitlab.com\', etc. OWNER: username for the
repository owner PROJECT: upstream project name (if it's identical to
the package name, use %{name} instead) &#8230;.

You may also obtain the 40-character hash and associated git tag via the
web-interface of the HOSTING-SERVICE, or by cloning the repository and
issuing the [git show-ref](https://git-scm.com/docs/git-show-ref)
command.

Once the commit hash and git tag are known, you can define them in your
spec file as follows:

&#8230;. %global commit 40-CHARACTER-HASH-VALUE %global gittag GIT-TAG
%global shortcommit %(c=%{commit}; echo \${c:0:7}) \[GitHub\] %global
shortcommit %(c=%{commit}; echo \${c:0:11}) \[Bitbucket\] %global
shortcommit %(c=%{commit}; echo \${c:0:7}) \[GitLab\] %global
shortcommit %(c=%{commit}; echo \${c:0:8}) \[Sourcehut\] &#8230;.

### Commit Revision {#_commit_revision}

For the source tarball, you can use the following syntax:

&#8230;. Source:
[https://github.com/OWNER/PROJECT/archive/%{commit}/%{name}-%{shortcommit}.tar.gz](https://github.com/OWNER/PROJECT/archive/%{commit}/%{name}-%{shortcommit}.tar.gz)
\[GitHub\] Source:
[https://bitbucket.org/OWNER/PROJECT/get/%{commit}.tar.gz&#35;/%{name}-%{shortcommit}.tar.gz](https://bitbucket.org/OWNER/PROJECT/get/%{commit}.tar.gz&#35;/%{name}-%{shortcommit}.tar.gz)
\[BitBucket\] Source:
[https://gitlab.com/OWNER/PROJECT/-/archive/%{commit}/%{name}-%{shortcommit}.tar.gz](https://gitlab.com/OWNER/PROJECT/-/archive/%{commit}/%{name}-%{shortcommit}.tar.gz)
\[GitLab\] Source:
[https://git.sr.ht/\~OWNER/PROJECT/archive/%{shortcommit}.tar.gz&#35;/PROJECT-%{shortcommit}.tar.gz](https://git.sr.ht/~OWNER/PROJECT/archive/%{shortcommit}.tar.gz&#35;/PROJECT-%{shortcommit}.tar.gz)
\[Sourcehut\] &#8230;

%prep %autosetup -n PROJECT-%{commit} \[GitHub\] %autosetup -n
OWNER-PROJECT-%{shortcommit} \[BitBucket\] %autosetup -n
PROJECT-%{commit} \[GitLab\] %autosetup -n PROJECT-%{shortcommit}
\[Sourcehut\] &#8230;.

If the release corresponds to a git tag with a sane numeric version, you
must use that version to populate the &#96;Version:&#96; tag in the spec
file. If it does not, look at the source code to see if a version is
indicated there, and use that value. If no numeric version is indicated
in the code, you may set &#96;Version&#96; to 0, and treat the package
as a \'pre-release\' package (and make use of the
&#96;+%{shortcommit}+&#96; macro). See [Prerelease
versions](Versioning.adoc&#35;_prerelease_versions) for details.

Alternately, if you are using a specific revision that is either a
pre-release revision or a post-release revision, you must follow the
\'snapshot\' guidelines. They are documented here:
[Snapshots](Versioning.adoc&#35;_snapshots). You can substitute
&#96;+%{shortcommit}\\&#96; for the git hash in \\&#96;%{checkout}+&#96;
in that section.

### Git Tags {#_git_tags}

[Git tags](https://git-scm.com/docs/git-tag) represent a particular code
point that upstream deems important; and are typically used to mark
release points.

Bitbucket uses the &#96;+%{shortcommit}+&#96; identifier as part of the
archive directory structure; regardless of whether you use git tag or
Commit Revision to retrieve it. This is shown in the %prep section
example.

For the source tarball, you can use the following syntax:

&#8230;. Source:
[https://github.com/OWNER/PROJECT/archive/%{gittag}/%{name}-%{version}.tar.gz](https://github.com/OWNER/PROJECT/archive/%{gittag}/%{name}-%{version}.tar.gz)
\[GitHub\] Source:
[https://bitbucket.org/OWNER/PROJECT/get/%{gittag}.tar.gz&#35;/%{name}-%{version}.tar.gz](https://bitbucket.org/OWNER/PROJECT/get/%{gittag}.tar.gz&#35;/%{name}-%{version}.tar.gz)
\[BitBucket\] Source:
[https://gitlab.com/OWNER/PROJECT/-/archive/%{gittag}/%{name}-%{version}.tar.gz](https://gitlab.com/OWNER/PROJECT/-/archive/%{gittag}/%{name}-%{version}.tar.gz)
\[GitLab\] Source:
[https://git.sr.ht/\~OWNER/PROJECT/archive/%{version}.tar.gz&#35;/PROJECT-%{version}.tar.gz](https://git.sr.ht/~OWNER/PROJECT/archive/%{version}.tar.gz&#35;/PROJECT-%{version}.tar.gz)
\[Sourcehut\] &#8230;

%prep %autosetup -n PROJECT-%{gittag} \[GitHub\] %autosetup -n
OWNER-PROJECT-%{shortcommit} \[BitBucket\] %autosetup -n
PROJECT-%{version} \[GitLab\] %autosetup -n PROJECT-%{version}
\[Sourcehut\] &#8230;.

## Using %{version} {#_using_version}

Using &#96;+%{version}+&#96; in the &#96;Source:&#96; makes it easier
for you to bump the version of a package, because most of the time you
do not need to edit &#96;Source:&#96; when editing the spec file for the
new package.

## Troublesome URLs {#_troublesome_urls}

When upstream has URLs for the download that do not end with the tarball
name rpm will be unable to parse the tarball out of the source URL. One
workaround for many cases is to construct a URL where the tarball is
listed in a \'URL fragment\':

&#8230;. Source:
[https://example.com/foo/1.0/download.cgi&#35;/%{name}-%{version}.tar.gz](https://example.com/foo/1.0/download.cgi&#35;/%{name}-%{version}.tar.gz)
&#8230;.

rpm will then use &#96;+%{name}-%{version}.tar.gz+&#96; as the tarball
name. If you use &#96;+spectool -g foo.spec+&#96; to download the
tarball, it will rename the tarball for you.

Sometimes this does not work because the upstream cgi tries to parse the
fragment or because you need to login or fill in a form to access the
tarball. In these cases, you have to put just the tarball's filename
into the &#96;Source:&#96; tag. To make clear where you got the tarball,
you should leave notes in comments above the &#96;Source:&#96; line to
explain the situation to reviewers and future packagers. For example:

&#8230;. &#35; Mysql has a mirror redirector for its downloads &#35; You
can get this tarball by following a link from: &#35;
<https://dev.mysql.com/downloads/mysql/5.1.html> Source:
mysql-5.1.31.tar.gz &#8230;.

## Do not conditionalize Sources {#_do_not_conditionalize_sources}

When building an SRPM, it is critical that all of the sources are
present, irrespective of the platform on which the SRPM is generated.
For example, the following code &#42;does not work&#42; (the way you
might expect):

&#8230;. %if 0%{?fedora} &lt; 35 Source1: mysource-old.tar.bz2 Patch1:
oldpatch.patch %else Source1: mysource-ng.tar.bz2 Patch1: ngpatch.patch
%endif &#8230;.

If you were to build this SRPM from a Fedora 34 host (&#96;rpmbuild -bs
mysource.spec&#96;), the resulting SRPM would carry
&#96;mysource-old.tar.bz2&#96; and &#96;oldpatch.patch&#96;. However, if
you then try to use this SRPM to build for Fedora 35, the operation
would fail because &#96;mysource-ng.tar.bz2&#96; is not available.

The correct behavior is to always carry all of the sources that might be
used in the build and then conditionalize the &#42;usage&#42; of them
instead. For example:

&#96;&#96;&#96; Source1: mysource-old.tar.bz2 Source2:
mysource-ng.tar.bz2

Patch1: oldpatch.patch Patch2: ngpatch.patch &#8230; %prep %autosetup -N
&#8230; %if 0%{?fedora} &lt; 35 tar xf %{SOURCE1} %patch 1 -p1 %else tar
xf %{SOURCE2} %patch 2 -p1 %endif &#96;&#96;&#96;

# Certificate Handling Guidelines {#_certificate_handling_guidelines}

These guidelines are relevant to maintainers of packages which utilize
smart cards for loading certificate or private key. Its purpose is to
bring a consistency in smart card handling on the OS; for background and
motivation see the [current status of PKCS&#35;11 in
Fedora](https://fedoraproject.org/wiki/User:Nmav/Pkcs11Status).

## How to specify a certificate or private key stored in a smart card or HSM {#_how_to_specify_a_certificate_or_private_key_stored_in_a_smart_card_or_hsm}

In April 2015, [RFC7512](https://tools.ietf.org/html/rfc7512) defined a
\'PKCS&#35;11 URI\' as a standard way to identify objects stored in
smart cards or HSMs. That form should be understood by programs when
specified in place of a certificate file. For non-interactive
applications which get information on the command line or configuration
file, there should not be a separate configuration option to load keys
and certificates stored in smart cards, the same option accepting files,
should additionally accept PKCS&#35;11 URIs.

## How to specify a specific PKCS&#35;11 provider module for the certificate or key {#_how_to_specify_a_specific_pkcs3511_provider_module_for_the_certificate_or_key}

Packages which can potentially use PKCS&#35;11 tokens SHOULD
automatically use the tokens which are present in the system's p11-kit
configuration, rather than needing to have a PKCS&#35;11 provider
explicitly specified. See [the PKCS&#35;11 packaging
page](Pkcs11Support.xml) for more information.

# Fedora systemd Services {#_fedora_systemd_services}

This document describes the guidelines for systemd services, for use and
inclusion in Fedora packages.

\[&#35;definitions\] == Definitions

Since systemd includes some concepts which are extensions of previous
concepts, the following definitions may be useful:

Service

:   A process or task executed and controlled by the init system (e.g.
    systemd).

Traditional Service

:   A service which is explicitly started or stopped, either by the init
    system at boot or manually by a superuser. In systemd, one of
    several types of service controlled by a &#96;+.service+&#96; file.

Activated service

:   A service that is not (or not necessarily) started explicitly by the
    user but start when certain other events happen or certain state
    becomes true.

Socket-activated Service

:   A service which is waiting for traffic across a socket before
    activating. In systemd, controlled by a &#96;+.socket+&#96; file.

D-Bus service

:   A service which activates in response to a message from the D-Bus
    system bus.

Unit file

:   The systemd equivalent of a SysV initscript. \[&#35;unit_files\] ==
    Unit Files

Each package that contains software that wants/needs to start a
traditional service at boot MUST have a systemd unit file.

Ideally, systemd unit files are reusable across distributions and
shipped with the upstream packages. Please consider working with
upstream to integrate the systemd files you prepare in the upstream
sources. Information for developers on how to integrate systemd support
best with their build system you may find in
[daemon(8)](https://www.freedesktop.org/software/systemd/man/daemon.html).

\[&#35;unit_files_naming\] === Naming

Unit files for traditional services have a naming scheme of
&#96;+foobar.service+&#96;. When considering what basename to use, keep
in mind that we'd like to use the same service names for software across
distributions. We'd also like to ship the &#96;+.service+&#96; files in
the upstream packages. These desires create a few guides for naming a
unit file:

&#42; Follow upstream if they're already distributing a
&#96;+.service+&#96; file and it's not likely to conflict with other
packages.

&#42; Look at packages in other distros or talk with the maintainers of
those packages and upstream to try to come up with a common name.

&#42; Unit files should be named after the software implementation that
they support as opposed to the generic type of software. So, a good name
would be &#96;+apache-httpd.service+&#96; and bad names would be
&#96;+httpd.service+&#96; or &#96;+apache.service+&#96; as there are
multiple httpd implementations and multiple projects produced by the
apache foundation.

For backwards compatibility you may also want to create a symlink from
an older, name to the new name. In the above example, for instance,
Fedora has always used &#96;+httpd+&#96; for the service. When creating
the new &#96;+apache-httpd.service+&#96; file, also create a symlink
named &#96;+httpd.service+&#96; that points at
&#96;+apache-httpd.service+&#96;. Then end users that are used to using
&#96;+service httpd+&#96; will have it continue to work.

\[&#35;unit_files_basic_format\] === Basic format

\[&#35;unit_files_basic_format_unit\] ==== \[Unit\]

Every &#96;+.service+&#96; file must begin with a &#96;+\[Unit\]+&#96;
section:

&#8230;.

Description=A brief human readable string describing the service (not
the .service file!) Documentation=man:foo.service(8) man:foo.conf(5)
<https://www.foo.org/docs/> &#8230;.

The &#96;+Description=\\&#96; line must not exceed 80 characters, and
must describe the service, and not the \\&#96;.service+&#96; file. For
example, \'Apache Web Server\' is a good description, but \'Starts and
Stops the Apache Web Server\' is a bad one.

\[&#35;unit_files_basic_format_unit_doc\] ===== Documentation field

Systemd has support for defining documentation in unit files via the
&#96;Documentation=&#96; field. System administrators will be looking at
the contents of the &#96;+Documentation=+&#96; field to determine what
the service is, how to configure it, and where to locate additional
documentation relating to the service. Accordingly, packagers are
strongly encouraged to include any available sources in the
&#96;Documentation=&#96; field which provide this information. If a man
page or info page is present in the package, refer to it using
&#96;man:manpage&#96; or &#96;info:infofile&#96; respectively. If the
documentation is in plaintext, use &#96;file://path/to/file&#96;.
Lastly, if no local documentation exists in the package, but it exists
at a URL, use the URL (with &#96;<https://&#96>;) in this field.
Multiple URIs can be added to the &#96;Documentation=&#96; field, as a
space separated list. For details on URI definitions and formatting,
please refer to the &#96;uri(7)&#96; manpage (&#96;man uri&#96;).

\[&#35;unit_files_basic_format_service\] ==== \[Service\]

Next, the &#96;+.service+&#96; file must have a &#96;+\[Service\]+&#96;
section:

&#8230;.

Type=&#8230; ExecStart=&#8230; ExecReload=&#8230; &#8230;.

The &#96;+Type=\\&#96; setting is very important. For D-Bus services
this should be \\&#96;+dbus&#96;, for traditional services
&#96;+forking+&#96; is usually a good idea, for services not offering
any interfaces to other services &#96;+simple+&#96; is best. For
\'one-shot\' scripts &#96;+oneshot+&#96; is ideal, often combined with
&#96;+RemainAfterExit=\\&#96;. See
https://www.freedesktop.org/software/systemd/man/systemd.service.html\[systemd.service(5)\]
for further discussion on the topic. Since \\&#96;+simple&#96; is the
default type, &#96;+.service+&#96; files which would normally set
&#96;+Type=simple+&#96; may simply omit the &#96;+Type+&#96; line
altogether.

&#96;+BusName=\\&#96; should be set for all services connecting to
D-Bus. (i.e. it is a must for those where \\&#96;+Type=dbus&#96;, but
might make sense otherwise, too) Omit this option if your service does
not take a name on the bus.

&#96;+ExecStart=+&#96; is necessary for all services. This line defines
the string that you would run to start the daemon, along with any
necessary options.

&#96;+ExecReload=\\&#96; should be specified for all services supporting
reload. It is highly recommended to add code here that synchronously
reloads the configuration file here (i.e. \\&#96;/bin/kill -HUP
\$MAINPID+&#96; is usually a poor choice, due to its asynchronous
nature). Omit this option if your service does not support reloading.

\[&#35;unit_files_basic_format_install\] ==== \[Install\]

Finally, the &#96;+.service+&#96; file should have an
&#96;+\[Install\]+&#96; section:

&#8230;.

WantedBy=&#8230; &#8230;.

The recommended parameters for &#96;+WantedBy=\\&#96; are either
\\&#96;+graphical.target&#96; (services related to the graphical user
interface) or &#96;+multi-user.target+&#96; (for everything else). When
the user (or our scriptlets) invoke &#96;+systemctl enable+&#96; the
service will be set to start in these targets.

For more information regarding these options see
[systemd.unit(5)](https://www.freedesktop.org/software/systemd/man/systemd.unit.html)
and
[systemd.service(5)](https://www.freedesktop.org/software/systemd/man/systemd.service.html).

\[&#35;unit_files_env\] === EnvironmentFiles and support for
/etc/sysconfig files

The &#96;+EnvironmentFiles=\\&#96; line in the \\&#96;\[Service\]\\&#96;
section of \\&#96;.service+&#96; files is used to support loading
environment variables that can be used in unit files. For instance, if
your sysv-initscript used a file in &#96;+/etc/sysconfig+&#96; to set
command line options, you can use &#96;+EnvironmentFiles=+&#96; like so:

Example:

&#8230;.

Type=forking EnvironmentFile=-/etc/sysconfig/httpd ExecStart=httpd
\$OPTIONS ExecReload=httpd \$OPTIONS -k restart &#8230;.

You may then refer to variables set in the
&#96;+/etc/sysconfig/httpd+&#96; file with &#96;+\${FOOBAR}\\&#96; and
\\&#96;\$FOOBAR+&#96;, in the &#96;+ExecStart=\\&#96; lines (and related
lines). (\\&#96;\${FOOBAR}\\&#96; expands the variable into one word,
\\&#96;\$FOOBAR+&#96; splits up the variable value at whitespace into
multiple words)

The &#96;+-\\&#96; on the \\&#96;+EnvironmentFile=&#96; line ensures
that no error messages is generated if the environment file does not
exist. Since many of these files were optional in sysvinit, you should
include the &#96;+-+&#96; when using this directive.

\[&#35;unit_files_avoid\] === Fields to avoid

For most services, we do not want to use requirement dependencies in the
&#96;+[\\&#96; section, such as \\&#96;+Requires=]{.Unit}&#96; or
&#96;+Wants=\\&#96;. Instead exclusively use ordering dependencies:
\\&#96;+Before=&#96; and &#96;+After=+&#96;. This is used to implement
loose coupling: if someone asks two services to start at the same time,
systemd will properly order their startup but not make it strictly
necessary to run one if the other is started.

If you use a requirement dependency, use &#96;+Wants=\\&#96; rather than
\\&#96;+Requires=&#96;, to make things a little bit more robust. If you
use a requirement dependency in almost all cases you should also add an
ordering dependency, as ordering and requirement dependencies are
orthogonal in systemd.

Here's an example of this common case:

1.  A web application needs postgresql to store its data.

2.  It is set to start &#96;+After+&#96; postgresql. On startup, the web
    application does not start until postgresql does.

3.  Once running, the system administrator needs to restart postgresql
    due to a config tweak.

4.  Since only &#96;+After+&#96; was used, the web application may be
    temporarily unable to serve some requests but it does not need to
    restart in order to serve pages after the database comes back up.

Avoid referring to &#96;+runlevelX.target+&#96; units in all lines
taking unit names (such as &#96;+WantedBy+&#96;), these are legacy names
existing for compatibility with SysV only.

Avoid &#96;+Names=\\&#96; (in the \\&#96;\[Unit\]\\&#96; section).
Usually it is a better idea to symlink an additional name in the file
system. Note that a name listed in \\&#96;+Names=&#96; is only useful
when a service file is already loaded. However, systemd loads only the
service files actually referred to in another loaded service, and uses
the filenames during the search. Hence a name in &#96;+Names=\\&#96; is
not useful as a search key, but a symlink in the file system is. Also do
not put a (redundant) \\&#96;+Names=foobar.service&#96; line into a file
called &#96;+foobar.service+&#96;. We want to keep our service files
short.

Unit files should avoid using &#96;+StandardOutput=\\&#96; or
\\&#96;+StandardError=&#96;. The default is the right choice for almost
all cases, and using the default allows users to change global defaults
in /etc/systemd/system.conf.

\[&#35;unit_files_example\] === Example Unit file

This is an example systemd unit &#96;+.service+&#96; file for ABRT:

&#8230;.

Description=ABRT Automated Bug Reporting Tool

Type=dbus BusName=com.redhat.abrt ExecStart=abrtd -d -s

WantedBy=multi-user.target &#8230;.

\[&#35;activation\] == Activation

Systemd allows for the following forms of activated services:
xref:&#35;activation_hardware\[Hardware activation\],
xref:&#35;activation_socket\[Socket activation\],
xref:&#35;activation_timer\[Timer activation\], and
xref:&#35;activation_dbus\[DBus activation\].

\[&#35;activation_hardware\] === Hardware activation

Hardware activation occurs when a service is installed but only turns on
if a certain type of hardware is installed. Enabling of the service is
normally done with a udev rule. At this time we do not have further
guidance on how to write those udev rules. The service itself installs
its &#96;+.service+&#96; files in the normal places and are installed by
the normal [systemd scriptlets](Scriptlets.adoc&#35;_systemd). These
services should never be enabled by the package as they will be enabled
by udev.

\[&#35;activation_socket\] === Socket activation

Socket activation occurs when a service allows systemd to listen for
connections to a specific socket and, when systemd receives a connection
on that socket, it starts the service. To do this, the upstream source
needs to have some minor coding work to let systemd listen for
connections on the socket and there needs to be a &#96;+.socket+&#96;
file in &#96;+%{\_lib}/systemd/system/+&#96; that tells systemd to
listen to that socket and what to start when a connection is received.
This is similar in function to inetd and some, but not all, services
coded to work with inetd will work with socket activation.

However, socket activation can also be used to allow parallel startup of
services. If a service supports systemd socket activation as described
above and we additionally start it explicitly on boot, then systemd will
start it but allow things that depend on it to startup at the same time.
If the dependent service makes a request to the socket activatable
service before it has come up, then systemd will cause the request to
wait until the socket activatable service has come up and can process
the request. To achieve this effect, the service must be socket
activatable as described above, the &#96;+.service+&#96; file for the
service needs to have a &#96;+Wants=\\&#96; line for the
\\&#96;.socket+&#96;, and the service must autostart.

Note that certain socket activated services (notably network listening
ones) require FESCo approval --- see [Default
Services](DefaultServices.xml) for details. Once you have permission,
you can package the &#96;+.socket+&#96; file and use the systemd
scriptlets that enable the service by default. You need to also check
the &#96;+.service+&#96; file to make sure it has a &#96;+Wants=\\&#96;
entry on the \\&#96;.socket+&#96; file as that ensures that starting the
service will also inform systemd of the socket.

\[&#35;activation_timer\] === Timer activation

All packages with timed execution which already depend on systemd (for
example because they contain systemd units) must use timer units instead
of cron jobs, with no dependency or requirements on a crontab.

Packages which do not already depend or require systemd must not use
timer units but instead depend and have requirement on crontabs, to
avoid introducing unnecessary new dependencies on systemd directly.

\[&#35;activation_dbus\] === DBus activation

In order to allow parallel startup of a D-Bus service and its consumers
it is essential that D-Bus services can be bus activated and the D-Bus
activation request is forwarded from the D-Bus system bus to systemd so
that you end up with only a single instance of the service, even if a
service is triggered by both boot-up and activation. If historically
your D-Bus service was not bus-activated but started via a SysV init
script, it should be updated to use bus activation. This may be
implemented by dropping a D-Bus &#96;+.service+&#96; file in
&#96;+/usr/share/dbus-1/system-services/\\&#96; and use the
\\&#96;+SystemdService=&#96; directive therein to redirect the
activation to systemd.

Here's an example for a D-Bus bus-activable service. The ConsoleKit bus
activation file
&#96;+/usr/share/dbus-1/system-services/org.freedesktop.ConsoleKit.service+&#96;:

&#8230;.

Name=org.freedesktop.ConsoleKit Exec=console-kit-daemon \--no-daemon
User=root SystemdService=console-kit-daemon.service &#8230;.

And the matching systemd unit file
/usr/lib/systemd/system/console-kit-daemon.service:

&#8230;.

Description=Console Manager

Type=dbus BusName=org.freedesktop.ConsoleKit
ExecStart=console-kit-daemon \--no-daemon &#8230;.

As you can see &#96;+SystemdService=+&#96; is used in the D-Bus
activation file to bind the systemd service to the D-Bus service.

Traditionally, bus activated D-Bus services could not be disabled
without uninstalling them entirely. systemd allows you to disable
services by making D-Bus invoke an alias systemd service name (that can
be created or removed to enable/disable activation) as an intermediary
for the real service.

You can easily implement disabling by directing the D-Bus service to an
alias name of the real service file (in the filesystem this shows up as
a symlink placed in &#96;+/etc/systemd/system+&#96; to the real service
file). This alias is then controlled via &#96;+systemctl enable+&#96;
and &#96;+systemctl disable+&#96;. It is a good idea (though technically
not necessary) to name this alias name after the D-Bus bus name of the
service, prefixed with &#96;+dbus-\\&#96;. Example for Avahi, a service
that the admin might need to disable: set
\\&#96;+SystemdService=dbus-org.freedesktop.Avahi.service&#96; instead
of &#96;+SystemdService=avahi-daemon.service+&#96; in the D-Bus
activation file, and then make
&#96;+dbus-org.freedesktop.Avahi.service+&#96; an optional alias of
avahi-daemon.service that can be controlled via the &#96;+Alias=\\&#96;
directive in the \\&#96;\[Install\]\\&#96; section of the systemd
service file. This directive is then read by \\&#96;+systemctl
enable&#96; and &#96;+systemctl disable+&#96; to create resp. remove a
symlink to make the service available resp. unavailable under this
additional name. A full example for the Avahi case:

Here is the D-Bus .service file for Avahi
(&#96;+/usr/share/dbus-1/system-services/org.freedesktop.Avahi.service+&#96;):

&#8230;.

Name=org.freedesktop.Avahi
SystemdService=dbus-org.freedesktop.Avahi.service

&#35; This service should not be bus activated if systemd isn't running,
&#35; so that activation won't conflict with the init script startup.
Exec=false &#8230;.

Here is the Avahi systemd unit &#96;+.service+&#96; file
(&#96;+/usr/lib/systemd/system/avahi-daemon.service+&#96;):

&#8230;.

Description=Avahi mDNS/DNS-SD Stack Requires=avahi-daemon.socket

Type=dbus BusName=org.freedesktop.Avahi ExecStart=avahi-daemon -s
ExecReload=avahi-daemon -r NotifyAccess=main

WantedBy=multi-user.target Also=avahi-daemon.socket
Alias=dbus-org.freedesktop.Avahi.service &#8230;.

The &#96;+Alias=\\&#96; line ensures that the existance of the
\\&#96;/etc/systemd/system/dbus-org.freedesktop.Avahi.service+&#96;
symlink can be controlled by &#96;+systemctl enable+&#96; and
&#96;+systemctl disable+&#96;.

Note that the creation/removal of the alias symlinks should be done with
&#96;+systemctl enable+&#96; and &#96;+systemctl disable+&#96; only. You
should not create these symlinks manually.

In general, it is also recommended to supply native systemd units for
all services that are already bus activatable, so that these services
can be controlled and supervised centrally like any other service with
tools such as systemctl. A similar logic like the one shown above should
apply.

See the D-Bus documentation for more information about bus activation:
<https://dbus.freedesktop.org/doc/dbus-specification.html&#35;message-bus-starting-services>

\[&#35;automatic_restart\] == Automatic restarting

If you package a long-running service, please consider enabling
systemd's automatic restart feature for it, to improve reliability by
making sure the system automatically attempts recovering a failing
daemon. Please use

&#8230;.

&#8230; Restart=on-failure &#8230;.

or

&#8230;.

&#8230; Restart=on-abnormal &#8230;.

in your unit's &#96;+.service+&#96; file for this.

The former will tell systemd to restart the daemon as soon as it fails
regardless of the precise reason. It's a good choice for most
long-running services. Some daemons require a way to escape constant
restarting by exiting with any non-zero exit code. For those services
use &#96;+Restart=on-abnormal+&#96;, which will still restart the daemon
when it fails \'abnormally\', on unclean signal, core dump, timeout or
watchdog exits, but not on unclean exit codes. It is recommended to to
enable automatic restarts for all long-running services, but which
setting is the right one, and whether it is useful at all depends on the
specific service. Please consult the
[systemd.service(5)](https://www.freedesktop.org/software/systemd/man/systemd.service.html)
man page for more information on the various settings.

\[&#35;private\] == Private devices and networking

If you package a long-running system service, please consider enabling
systemd's &#96;+PrivateDevices=\\&#96; and \\&#96;+PrivateNetwork=&#96;
settings for it, in order to improve security and minimize the attack
surface.

When &#96;+PrivateDevices=yes+&#96; is set in the &#96;+[\\&#96; section
of a systemd service unit file, the processes run for the service will
run in a private file system namespace where
\\&#96;]{.Service}/dev+&#96; is replaced by a minimal version that only
includes the device nodes &#96;+/dev/null+&#96;, &#96;+/dev/zero+&#96;,
&#96;+/dev/full+&#96;, &#96;+/dev/urandom+&#96;,
&#96;+/dev/random+&#96;, &#96;+/dev/tty+&#96; as well as the submounts
&#96;+/dev/shm+&#96;, &#96;+/dev/pts+&#96;, &#96;+/dev/mqueue+&#96;,
&#96;+/dev/hugepages+&#96;, and the &#96;+/dev/stdout+&#96;,
&#96;+/dev/stderr+&#96;, &#96;+/dev/stdin+&#96; symlinks. No device
nodes for physical devices will be included, however. Furthermore, the
CAP_MKNOD capability is removed. Finally, the &#96;+devices+&#96; cgroup
controller is used to ensure that no access to device nodes except the
listed ones is possible. This is an efficient way to take away physical
device access for services, thus minimizing the attack surface.

When &#96;+PrivateNetwork=yes+&#96; is set in the
&#96;+\[Service\]+&#96; section of a systemd service unit file, the
processes run for the service will run in a private network namespace
whith a private loopback network interface, and no other network
devices. Network communication between host and service can not be
initiated. This is an efficient way to take away network access for
services, thus minimizing the attack surface.

By default both switches default to &#96;+no+&#96;.

Note that &#96;+PrivateDevices=yes+&#96; should not be used for:

&#42; Services that actually require physical device access

&#42; Services which may be used to execute arbitrary user or
administrator supplied programs (such as cron, &#8230;). We shouldn't
limit what people can do with these services.

&#42; This option creates a new file system namespace where mount/umount
propagation is turned off back into the host. This means that mounts
made by the service will stay private to the service. Thus this option
should not be used by services which shall be able to establish mounts
in the host.

Note that &#96;+PrivateNetwork=yes+&#96; should not be used for:

&#42; Services that actually require network access (with the exception
of daemons only needing socket activation)

&#42; Services which may be used to execute arbitrary user or
administrator supplied programs. (see above)

&#42; Services which might need to resolve non-system user and group
names. Since on some setups resolving non-system users might require
network access to an LDAP or NIS server, enabling this option on might
break resolving of these user names. Note however that system
users/groups are always resolvable even without network access. Hence it
is safe to enable this option for daemons which just need to resolve
their own system user or group name.

&#42; This also disconnects the AF_UNIX abstract namespace from the host
(In case you wonder what this refers to: sockets listed in
&#96;+/proc/net/unix+&#96; that start with an &#96;+@\\&#96; are in the
abstract namespace, those which start in \\&#96;/\\&#96; are in the file
system namespace). This means that services which listen or connect to
AF_UNIX sockets in the abstract namespaces might break. AF_UNIX sockets
in the file system continue to work correctly even with
\\&#96;+PrivateNetwork?=yes&#96;. We strongly recommend anyway to stop
using abstract namespace AF_UNIX sockets, as they bring very little
benefit these days. If your package uses them please consider moving
them into the file system into a subdirectory in &#96;+/run+&#96;
(system services) or &#96;+\$XDG_RUNTIME_DIR+&#96; (user services).

&#42; This also disconnects the AF_NETLINK and AF_AUDIT socket families
from the host. For services requiring auditing, that need to subscribe
to network configuration changes, or want to subscribe to hardware
devices coming and going (udev) &#96;+PrivateNetwork?=yes+&#96; cannot
be used hence.

For further details see the
[systemd.exec(5)](https://www.freedesktop.org/software/systemd/man/systemd.exec.html)
man page.

\[&#35;packaging\] == Packaging

\[&#35;packaging_filesystem\] === Filesystem locations

systemd unit files &#42;must&#42; be shipped in either
&#96;+%{\_unitdir}\\&#96; or \\&#96;%{\_userunitdir}\\&#96;, for system
services and user session services, respectively. Unit drop-ins
\\&#42;must\\&#42; be shipped in appropriate sub-directories of these
two directories. Unit files and drop-ins \\&#42;must\\&#42; be
world-readable (i.e. mode \\&#96;+0644&#96;) and &#42;must not&#42; be
marked as &#96;%config&#96; or &#96;%config(noreplace)&#96;.

The &#96;+%{\_unitdir}\\&#96; and \\&#96;%{\_userunitdir}\\&#96; macros
are defined in the \\&#96;+systemd-rpm-macros&#96; package, so something
like this is required for them to be available:

&#8230;. BuildRequires: systemd-rpm-macros &#8230;.

\[&#35;packaging_unit_files_in_scriptlets\] === Unit files in spec file
scriptlets

Information on proper handling of unit files in spec file scriptlets can
be found here: [Scriptlets&#35;Systemd](Scriptlets.adoc&#35;_systemd).

\[&#35;packaging_tmpfiles_d\] === Tmpfiles.d

tmpfiles.d is a service provided systemd for managing temporary files
and directories for daemons. For more information on how to use
Tmpfiles.d in Fedora Packages, please see: [Tmpfiles.d](Tmpfiles.d.xml).

\[&#35;why_dont_we\] == Why don't we&#8230;.

&#42; Start the service after installation?

Installations can be in changeroots, in an installer context, or in
other situations where you don't want the services autostarted.

# Tmpfiles.d {#_tmpfiles_d}

## Overview {#_overview}

tmpfiles.d is a service for managing temporary files and runtime
directories for daemons. In this guideline we mainly concentrate on how
it is used to populate &#96;+/run+&#96; and &#96;+/run/lock+&#96;. Since
&#96;+/run+&#96; is a &#96;+tmpfs+&#96; filesystem, it and its contents
must be recreated on every reboot. For files intended to be created
there, this should normally not pose any problems. However, directories
will often need to be created ahead of time. This is best done using the
tmpfiles.d mechanism.

## tmpfiles.d configuration {#_tmpfiles_d_configuration}

Asking the tmpfiles.d mechanism to create directories for you just
involves dropping a file into &#96;+%{\_tmpfilesdir}+&#96;. You will
need a build dependency on systemd-rpm-macros in order to make use of
this macro.

For example, if the package needs a few directories to be created in
&#96;+/run+&#96; in order for it to run, the packager needs to create a
file named &#96;+%{name}.conf+&#96; that is installed as
&#96;+%{\_tmpfilesdir}/%{name}.conf+&#96;. The file has one or more
lines of the following format:

&#8230;. d /run/NAME PERM USER GROUP - &#8230;.

The format of the line is as follows:

&#42; &#96;+d+&#96; specifies that a directory is to be created if it
doesn't exist. You can use a different type specifier if you need it.
See &#96;+man tmpfiles.d+&#96; for possible values. &#42;
&#96;+/run/NAME+&#96; is the filesystem path to create. &#42;
&#96;+PERM+&#96; are the permissions (in the 4-digit octal format) to
apply to the directory when it is created. &#42; &#96;+USER+&#96; is the
name of the owner of the directory. &#42; &#96;+GROUP+&#96; is the name
of the group of the directory. &#42; &#96;+-+&#96; specifies that aging
should not be applied to the contents of the directory. Aging is a
mechanism for automated cleanup of files that were not used for a
specified length of time. This is mostly useful for directories such as
/tmp and is seldom used by packages. Feel free to use aging if it is
appropriate for your directory.

An example:

&#8230;. d /run/mysqld 0755 mysql mysql - &#8230;.

Information on other options is available on the [tmpfiles.d man
page](https://www.freedesktop.org/software/systemd/man/tmpfiles.d.html)
should you need to do something more advanced.

## Example spec file {#_example_spec_file}

In the spec file, the packager needs to install the tmpfiles.d conf file
into the &#96;+%{\_tmpfilesdir}+&#96; directory and also make sure the
directory is included in the rpm.

``` _rpm-spec
\&#35; For the _tmpfilesdir macro.
BuildRequires: systemd-rpm-macros

\&#35; tmpfiles.d configuration for the /run directory
Source1:  %{name}-tmpfiles.conf
[\&#8230;]

%install
mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 0644 %{SOURCE1} %{buildroot}%{_tmpfilesdir}/%{name}.conf

\&#35; This may not be needed if the upstream's install script creates the directories
\&#35; Make sure permissions are correct
install -d -m 0755 %{buildroot}/run/%{name}/

\&#35; A bit contrived as most packages will either create a subdirectory or a single file.  Not both
\&#35; Make sure permissions are correct
touch %{buildroot}/run/%{name}.pid
chmod 0644 %{buildroot}/run/%{name}.pid
[\&#8230;]

%files
\&#35; Use %attr() if needed to change ownership of these two items
%dir /run/%{name}/
%verify(not size mtime md5) /run/%{name}.pid
%{_tmpfilesdir}/%{name}.conf
```

&#96;+%{\_tmpfilesdir}\\&#96; expands to
\\&#96;%{\_prefix}/lib/tmpfiles.d+&#96; which is the location that the
package's default tmpfile creation scripts should install into.
&#96;+%{\_tmpfilesdir}/%{name}.conf+&#96; is &#42;not&#42; marked as a
&#96;+%config+&#96; file because it is not supposed to be edited by
administrators. Administrators can override the package's
&#96;+%{name}.conf+&#96; by placing an identically named file in
&#96;+/etc/tmpfiles.d/+&#96;, but this should very rarely be needed.

Files (&#42;not directories&#42;) that the program places directly into
&#96;+/run+&#96; are listed in the &#96;+%files+&#96; section as
&#96;+%verify(not size mtime md5)+&#96; so that rpm knows the file must
exist as part of this package but will not complain when the file
contents change. Files placed in the subdirectories may be listed the
same way or omitted entirely as the files will be cleaned up on every
reboot.

## Why not create the directories with XXXXXX instead? {#_why_not_create_the_directories_with_xxxxxx_instead}

There are multiple ways to try creating the directories but most suffer
some disadvantage that tmpfiles.d addresses:

### Have the daemon create the directory when it starts up {#_have_the_daemon_create_the_directory_when_it_starts_up}

Many times, daemons run as an unprivileged user who would not be allowed
to create new directories directly into &#96;+/run+&#96;. If the daemon
does not drop privileges, then you can patch it to create the files and
directories when the daemon starts and submit the patch upstream.

### Have the init script create the directory when it starts up the daemon {#_have_the_init_script_create_the_directory_when_it_starts_up_the_daemon}

Since the init script is run by root, before the daemon drops
privileges, why not create the directories there?

&#42; This code would need to be implemented in every init script
packaged. Using tmpfiles.d we can cut down on the number of places we
have to put code like this. &#42; Having to add the mkdir to the systemd
unit files when tmpfiles.d is already in place introduces the need to
run shell code for that init script. Systemd is no longer able to handle
starting the daemon by itself which slows things down. The shell code
also introduces imperative constructs into the otherwise declarative
structure which is nice to avoid. &#42; Properly labelling the created
directories is done automatically by the tmpfiles.d mechanism but would
have to be manually done by the init script.

# Unowned Directories {#_unowned_directories}

The term \'unowned directory\' (or \'orphaned directory\') refers to a
packaging mistake where these three things happen:

&#42; a package includes files within a directory it creates, but
&#42;not&#42; the directory itself &#42; none of the package's
dependencies provide the directory either &#42; the directory belongs to
your package and does not belong to any core package or base filesystem
package that is considered essential/fundamental to any Fedora System.

## Issues {#_issues}

Unowned directories can cause the following problems.

### Inaccessible Directories {#_inaccessible_directories}

A restrictive superuser umask during package installation can create
inaccessible directories when installed using the RPM Package Manager
older than 4.4.2.3. Fedora 9 and RHEL 5.3 are the first to use RPM
4.4.2.3 which sets umask 0022 always. On platforms with older versions
of RPM if the superuser does this:

&#96;+ umask 077+&#96;\
&#96;+ yum update+&#96;\
&#96;+ [\\&#96; + \\&#96;]{.or} rpm -ivh PACKAGE+&#96;

Unowned directories within the updated or installed packages will only
be readable and executable by root. This prevents other users from using
the files within those directories.

This causes run-time problems for users. For example, unreadable subdirs
below %\_libdir disable plugins. Unreadable subdirs below %\_datadir
prevent application data, help texts, and graphics from being accessed.

Several sorts of users fix such permission problems with chmod instead
of taking the time to report it as a bug. It is common belief that such
bugs are so obvious they would be found by the package maintainer or
will be reported by other users.

### Directories not Removed {#_directories_not_removed}

Upon uninstalling the package (or upgrading to another version), the old
directory is not removed from the file system because it does not belong
in the package in the RPM database.

Especially if directories contain a version number, they clutter up the
file system with every update which doesn't remove old directories.

### Directories cannot be Verified {#_directories_cannot_be_verified}

Unowned/orphaned directories cannot be checked with rpm -V and not with
rpm -qf either.

### ./configure Scripts can Fail {#_configure_scripts_can_fail}

Upstream source tarball configuration can fail, because it detects the
presence of an old but empty versioned header directories or because it
is trying to use multiple versioned directories instead of just the
latest valid one.

## Tools to Help {#_tools_to_help}

It's easy to find unowned directories with &#96;+rpmls+&#96; from
rpmdevtools or &#96;+rpm -qlv+&#96;. Just a bit of carefulness is needed
to not include core filesystem directories, such as %\_bindir, %\_libdir
(and obvious others, e.g. from the \'filesystem\' pkg) which don't
belong into your package.

## Common Mistakes {#_common_mistakes}

Here are some examples of common packaging mistakes in spec %files lists
to avoid

### Wildcarding Files inside a Created Directory {#_wildcarding_files_inside_a_created_directory}

#### Unversioned {#_unversioned}

    %{_datadir}/foo/\&#42;

This includes everything *in* \'foo\', but not \'foo\' itself. \'rpm
-qlv pkgname\' will show a missing drwxr-xr-x entry for \'foo\'. Correct
would be:

    %{_datadir}/foo/

to include the directory *and* the entire tree below it.

#### Versioned {#_versioned}

    %{_docdir}/%{name}-%{version}/\&#42;
    %{_includedir}/%{name}-%{version}/\&#42;.h

This is the same as the unversioned scenario with the addition that
every time the package is upgraded to a new version the old directory
will remain on the filesystem. Correct would be:

    %{_docdir}/%{name}-%{version}/
    %dir %{_includedir}/%{name}-%{version}
    %{_includedir}/%{name}-%{version}/\&#42;.h

### Forgetting to Include a Toplevel Directory {#_forgetting_to_include_a_toplevel_directory}

    %dir %{_libdir}/foo-2/fu
    %dir %{_libdir}/foo-2/bar
    %{_libdir}/foo-2/fu/\&#42;.so
    %{_libdir}/foo-2/bar/config\&#42;

Here it is an attempt at including the directories explicitly with the
%dir macro. However, while \'bar\' is included, \'foo-2\' is not.
Typically packagers run into that mistake if all installed files are
stored only in subdirs of the parent \'foo-2\' directory. Correct would
be:

    %dir %{_libdir}/foo-2
    %dir %{_libdir}/foo-2/fu
    %dir %{_libdir}/foo-2/bar
    %{_libdir}/foo-2/fu/\&#42;.so
    %{_libdir}/foo-2/bar/config\&#42;

#### Only Including Files {#_only_including_files}

    %{_datadir}/%{name}/db/raw/\&#42;.db
    %{_datadir}/%{name}/pixmaps/\&#42;.png

Here only specific data files are included, and all 4 directories below
%\_datadir are unowned. Correct would be:

    %dir %{_datadir}/%{name}
    %dir %{_datadir}/%{name}/db
    %dir %{_datadir}/%{name}/db/raw
    %dir %{_datadir}/%{name}/pixmaps
    %{_datadir}/%{name}/db/raw/\&#42;.db
    %{_datadir}/%{name}/pixmaps/\&#42;.png

# Users and Groups Guidelines {#_users_and_groups_guidelines}

This guideline is for packaging cases that require creation of users and
groups.

## Basic premise for users {#_basic_premise_for_users}

In designing these guidelines it was accepted that individual sites will
have a need to customize the allocation of UIDs and GIDs to their
particular systems. For instance, if they have both Debian and Fedora
installs or if they've already allocated user accounts in the range that
we use for system accounts and need to place system accounts elsewhere.
Therefore, the methods that these guidelines advocate had to be
adaptable so that local sysadmins could make our packages use the UIDs
and GIDs that they desired at their site.

The guidelines provide two options: letting each individual system
allocate UID and GID values individually or using a \'soft static\'
allocation that attempts to allocate UIDs and GIDs consistently. In
either case, if the username or groupname being created by the package
already exists on the system the package will use that instead of
creating a new one. This allows the local system administrator to
pre-allocate the UIDs and GIDs for particular usernames and groupnames
in order to set them to a particular value for their site.

### Methods of pre-allocating {#_methods_of_pre_allocating}

There are many ways to pre-allocate the UIDs and GIDs. Sites that only
want to customize the UIDs and GIDs of a few nonessential services may
write a script to create the entries with &#96;+useradd+&#96; and
&#96;+groupadd+&#96; and install our package afterwards.

Sites that want to pre-allocate accounts that are needed during an
unattended kickstart install have trickier problem. One way for them to
accomplish their goals is to create a customized version of the
&#96;+setup+&#96; package with the desired users and groups along with
their chosen UID/GID mappings in the &#96;+/etc/passwd+&#96;,
&#96;+/etc/shadow+&#96;, and &#96;+/etc/group+&#96; files. Then they
make sure the install transaction uses that package instead of the
vanilla distro one (by versioning their setup package higher than ours
(for instance, with an epoch) and putting it in a local repo they
include when installing or replacing our setup package with their own in
a local mirror of the packages that they are installing from). Since
setup is at the top of the dependency tree, it will be installed before
any package which needs to use the UIDs and GIDs that are defined in it.

:::: tip
::: title
:::

&#42;Using LDAP to preallocate&#42;: Sites with LDAP or other network
authentication systems may want to use those for pre-allocating their
system accounts sitewide. Such sites should make sure their
infrastructure is robust and includes suitable local caching of the
system accounts. Without suitable local caching, a computer that becomes
disconnected from the network may not be able to start essential
services because the computer is unable to resolve a username or
groupname to a proper UID or GID.
::::

### Known caveat of the pre-allocation strategy {#_known_caveat_of_the_pre_allocation_strategy}

The practice of using existing users and groups if their symbolic names
(usernames and groupnames) already exists on the system lets the system
administrator customize the UIDs and GIDs as they please. However, it
has one drawback that system admins should be aware of. If an unrelated
account has already been created that uses those usernames and
groupnames the package will make use of those accounts.

As an example, say that you are installing the mailman package which
wants to create the &#96;+mailman+&#96; user and group so that the
private mailing list archives can be owned by that user and group on
disk. One of your local users already has the local username
&#96;+mailman+&#96;. When the mailman package is installed, it will
detect that there is already a &#96;+mailman+&#96; user and use that
account for owning its private archives. The local user who owns the
mailman account would then be able to read those private archives.

At the moment, there is no strategy for the packagers to counteract
this. It is up to the site system administrators to keep track of and
remove conflicts for the user and group names used by their users and
those used by the packages they are using.

## Allocation Strategies {#_allocation_strategies}

We have two methods for creating users and groups: Dynamic and Soft
Static.

Any package can use dynamic allocation; it is especially appropriate for
packages that use separate identities only for privilege separation and
don't create any files owned by that group/user account. Because of the
limited number of soft static UIDs and GIDs available, it is better to
use dynamic allocation if in doubt.

Soft static allocation ensures that multiple independently installed
systems use the same UID and GID values; either UID and GID values
allocated by Fedora or values that were optionally pre-allocated by the
system administrator. Don't use soft static allocation unnecessarily as
the number of available values is limited. Soft static allocation is
only appropriate for packages where the UID or GID values are shared
between computers. For instance, if the package creates files with the
assigned UID or GID that are likely to be shared over NFS. Soft static
allocation &#42;MUST&#42; be evaluated by the FPC. See the paragraph in
the [ soft static section](&#35;_soft_static_allocation) for details the
FPC will want.

In some cases it is desirable to create only a group without a user
account. Usually this is because there are some system resources to
which we want to control access by using that group and a separate user
account would add no value. Examples of common such cases include (but
are not limited to) games whose executables are setgid for the purpose
of sharing high score files or the like, and/or software that needs
exceptional permissions to some hardware devices and it wouldn't be
appropriate to grant those to all system users nor even only those
logged in on the console. In these cases, apply only the
&#96;+groupadd+&#96; parts of the below recipes.

### Dynamic allocation {#_dynamic_allocation}

To create system users and groups in packages using dynamic allocation,
the package shall install a
&#96;sysusers.d/&lt;package-name&gt;.conf&#96; file. If it is not
provided by the upstream, the maintainer &#42;should&#42; provide one
either as a separate &#96;+Source+&#96; or otherwise create it during
the package build.

For example for the &#96;munge&#96; package, this file may contain:
&#96;&#96;&#96; &#35;Type Name ID GECOS Home directory Shell u munge -
\'Runs Uid \'N\' Gid Emporium\' /run/munge - &#96;&#96;&#96;

(The shell is not specified, so the default of &#96;nologin&#96; shall
be used.)

When a package with a sysusers.d file is built, a virtual
&#96;Provides&#96; for &#96;+user(...)\\&#96; and
\\&#96;+group(...)&#96; is automatically generated. When &#96;rpm&#96;
installs a package with such &#96;Provides&#96;, it shall create the
users and groups according to those definitions.

Use &#96;+rpm -q \--qf=\'\[%{SYSUSERS}\\n\]\' ...+&#96; to view the
definitions of users and groups decoded from the virtual
&#96;Provides&#96;.

### Creation of users and groups with scriptlets {#_creation_of_users_and_groups_with_scriptlets}

For Fedora releases before 42, manual creation of users and groups is
required.

The sysusers file must be a separate &#96;Source&#96; file.

In the specfile, add a BuildRequires for systemd-rpm-macros, install the
sysusers file, use the &#96;%sysusers_create_compat&#96; macro to
consume it in the &#96;%pre&#96; section (in this example the sysusers
config file is &#96;Source3&#96; of the specfile), and the
&#96;%sysusers_requires_compat&#96; macro to specify the runtime
dependencies for the &#96;%pre&#96; section: &#96;&#96;&#96; \[&#8230;\]
BuildRequires: systemd-rpm-macros %{?sysusers_requires_compat}

\[&#8230;\] %install install -p -D -m 0644 %{SOURCE3}
%{buildroot}%{\_sysusersdir}/munge.conf

\[&#8230;\] %pre %sysusers_create_compat %{SOURCE3}

\[&#8230;\] %files %{\_sysusersdir}/munge.conf \[&#8230;\]
&#96;&#96;&#96;

This form is compatible with Fedora 42+, and the same spec file may be
used for older and newer releases. In F42+, the
&#96;%sysusers_requires_compat&#96; and
&#96;%sysusers_create_compat&#96; macros will evaluate as empty.

### Soft static allocation {#_soft_static_allocation}

To allocate a UID and/or GID, file a ticket
[here](https://pagure.io/packaging-committee/new_issue) for the FPC to
evaluate. If the FPC finds that your package needs a soft static UID or
GID, they will approve your request and pass it on to the maintainers of
the &#96;+setup+&#96; package for implementation. Because the number of
UIDs and GIDs is limited, you need to justify your package's need for a
soft static uid in the FPC ticket. Explain how the uids and gids are
being shared between computers. If applicable, also explain why the
program can't be adapted to use symbolic names (username and groupname)
instead. If a specific UID or GID should be used, please mention it and
why (for instance, it is the one used by upstream or the one used by
other distributions). We will try to accommodate on a first-come-first
serve basis if the UID/GID is available from within the Fedora system
UID/GID range.

To create users and groups in packages with an allocated UID/GID, follow
the steps in the dynamic allocation section above, but add the UID or
GID in the &#96;ID&#96; column.

### Sharing of users or groups between packages {#_sharing_of_users_or_groups_between_packages}

The package that provides the definition of the user or group account
has automatically-generated virtual &#96;Provides&#96;. Other packages
which want to ensure that users or groups exist, &#42;may&#42; use
&#96;Requires&#96; on the user or group names.

For example, &#96;+Requires: user(mock)\\&#96; or \\&#96;+Requires:
group(man)&#96;.

&#96;rpm&#96; automatically creates weak dependencies
(&#96;Recommends&#96;) for packages which contain files owned by users
and groups. In the future, those depencencies will be changed to
&#96;Requires&#96;.

### List of statically allocated UID/GID and corresponding package {#_list_of_statically_allocated_uidgid_and_corresponding_package}

The list of statically allocated accounts is maintained in the
&#96;setup&#96; package:
[uidgid](https://src.fedoraproject.org/rpms/setup/blob/rawhide/f/uidgid).

# Versioning Guidelines {#_versioning_guidelines}

Fedora's package versioning scheme encompasses both the
&#96;+Version:+&#96; and &#96;+Release:+&#96; tags, as well as
&#96;+Epoch:+&#96;. The overriding goal is to provide sequences of
packages which are treated as updates by RPM's version comparison
algorithm while accommodating varied and often inconsistent upstream
versioning schemes.

The &#96;+Version:+&#96; field contains the upstream project version,
and the &#96;+Release:+&#96; field specifies the downstream release
number.

## Some definitions {#_some_definitions}

Note that upstreams may each have their own terminology and it is in
general impossible to define these terms with complete generality. For
some upstreams, every commit is itself considered a version. Some
upstreams never make releases, instead just letting users take whatever
is in the code repository at any given time.

release version

:   A version of the software which upstream has decided to release. The
    act of releasing the software can be as simple as adding a git tag.
    This includes so-called \'point releases\' or \'patchlevels\' which
    some upstreams make, since those are actually assigned versions and
    released.

snapshot

:   An archive taken from upstream's source code control system which is
    not associated with any release version.

prerelease version

:   Before a release happens, many upstreams will decide which version
    that will release will have, and then produce \'alphas\', \'betas\',
    \'release candidates\', or the like which carry that new version but
    indicate that the release of that version has not yet been made.
    These we call prerelease versions. Any snapshots made while upstream
    is preparing for their release are also considered prerelease
    versions.

postrelease version

:   Any version which happens after a particular release is technically
    \'post-release\', but before upstream begins making prereleases for
    the next version, any snapshot is considered a postrelease version.

non-sorting version sequence

:   A sequence of version strings which is not ordered in the same way
    that RPM's version comparison function would order it. RPM has a
    somewhat complicated version comparison function which it will use
    to determine if a package is \'newer\'. If upstream's idea of what
    constitutes a \'newer\' version differs from RPM's implementation
    then simply using upstream's versions directly will result in
    updates which don't actually update any packages.

## &#96;+Epoch+&#96; tag {#_96epoch96_tag}

The &#96;+Epoch:+&#96; tag provides the most significant input to RPM's
version comparison function. If present, it &#42;&#42;must&#42;&#42;
consist of a positive integer. It &#42;&#42;should only&#42;&#42; be
introduced or incremented when necessary to avoid ordering issues. The
&#96;+Epoch:+&#96; tag, once introduced to a package, &#42;&#42;must
never&#42;&#42; be removed or decreased.

## &#96;+Release+&#96; tag {#_96release96_tag}

The &#96;+Release:+&#96; &#42;&#42;should&#42;&#42; be managed
automatically using the &#96;+%autorelease+&#96; macro:

``` _rpm-spec
Release: %autorelease
```

As described in [%autorelease
documentation](https://fedora-infra.github.io/rpmautospec-docs/autorelease.html),
the build machinery will replace the macro with the number of builds
since the last commit that changed the &#96;+Version+&#96; field,
suffixed with the &#96;%{?dist}&#96; tag. This means that a commit that
changes &#96;+Version+&#96; automatically gets &#96;Release:
1%{?dist}&#96;, and commits after that get &#96;Release: 2%{?dist}&#96;,
&#96;Release: 3%{?dist}&#96;, and so on.

Alternatively, the &#96;+Release:+&#96; field &#42;&#42;may&#42;&#42; be
updated manually. See [Traditional versioning with part of the upstream
version information in the release
field](Versioning.adoc&#35;traditional-versioning).

## Simple versioning {#_simple_versioning}

Most upstream versioning schemes are \'simple\'; they generate versions
like &#96;+1.2.03.007p1+&#96;. They consist of one or more version
components, separated by periods. Each component is a whole number,
potentially with leading zeroes. The components can also include one or
more ASCII letters, upper or lower case. The value of a component must
&#42;never&#42; be reduced (to a value which sorts lower) without a
component somewhere to the left increasing. Note that the version
sequence (&#96;+1.4a+&#96;, &#96;+1.4b+&#96;, &#96;+1.4+&#96;) does not
meet this criterion, as &#96;+4+&#96; sorts lower than &#96;+4b+&#96;.
The sequence (&#96;+1.4+&#96;, &#96;+1.4a+&#96;, &#96;+1.4b+&#96;) is,
however, simple.

This is a very common versioning scheme, and the vast majority of
software projects use something which works like this.

To package &#42;release versions&#42; of software using this versioning
scheme:

&#42; Use the upstream project version verbatim in the
&#96;+Version:+&#96; tag. Don't trim leading zeroes.

## Complex versioning {#_complex_versioning}

There are several ways in which the simple scheme might not work in a
particular situation:

&#42; Upstream has never chosen a version; only snapshots are available
for packaging. &#42; Upstream simply doesn't use a version scheme which
orders properly under RPM's version comparison operation. &#42; You wish
to package a prerelease version (snapshot or otherwise). &#42; You wish
to package a postrelease snapshot. &#42; Upstream was thought to be
following one scheme but then changed in a way that does not sort
properly. &#42; You need to apply a small fix to a release branch of
Fedora without updating the newer branches. &#42; More than one of the
above may apply (lucky you). Follow all of the relevant recommendations
below together.

This subsection describes how to modify the upstream project version to
be suitable for the &#96;+Version+&#96; field. Use of &#96;Release:
%autorelease&#96; remains unchanged.

### Handling non-sorting versions with tilde, dot, and caret {#_handling_non_sorting_versions_with_tilde_dot_and_caret}

The tilde symbol (\'&#96;+\~+&#96;\') is used before a version component
which must sort &#42;earlier&#42; than any non-tilde component. It is
used for any pre-release versions which wouldn't otherwise sort
appropriately.

For example, with upstream releases &#96;+0.4.0+&#96;,
&#96;+0.4.1+&#96;, &#96;+0.5.0-rc1+&#96;, &#96;+0.5.0-rc2+&#96;,
&#96;+0.5.0+&#96;, the two \'release candidates\' should use
&#96;+0.5.0\~rc1+&#96; and &#96;+0.5.0\~rc2+&#96; in the
&#96;+Version:+&#96; field.

Bugfix or \'patchlevel\' releases that some upstream make should be
handled using simple versioning. The separator used by upstream may need
to be replaced by a dot or dropped.

For example, if the same upstream released &#96;+0.5.0-post1+&#96; as a
bugfix version, this \'post-release\' should use &#96;+0.5.0.post1+&#96;
in the &#96;+Version:+&#96; field. Note that &#96;+0.5.0.post1+&#96;
sorts lower than both &#96;+0.5.1+&#96; and &#96;+0.5.0.1+&#96;.

The caret symbol (\'&#96;+\^+&#96;\') is used before a version component
which must sort &#42;later&#42; than any non-caret component. It is used
for post-release snapshots, see next section.

:::: important
::: title
:::

The caret operator is not supported in RHEL7 which has rpm 4.11. If you
need to support RHEL7/EPEL7 from the same specfile, use
&lt;&lt;Traditional versioning with part of the upstream version
information in the release field&gt;&gt; instead.
::::

### Snapshots {#_snapshots}

Snapshots (a version taken from the upstream source control system not
associated with a release), &#42;&#42;must&#42;&#42; contain a snapshot
information field after a caret (&#96;+\^+&#96;). The first part of the
field ensures proper sorting. That field may either be the date in
eight-digit \'YYYYMMDD\' format, which specifies the last modification
of the source code, or a number. The packager &#42;&#42;may&#42;&#42;
include up to 17 characters of additional information after the date,
specifying the version control system and commit identifier. The
snapshot information field is appended to version field described above,
possibly including the pre-release and patchlevel information.

One of the following formats should be used for the snapshot information
field:

&#42; &#96;+&lt;date&gt;.&lt;revision&gt;+&#96; &#42;
&#96;+&lt;date&gt;&lt;scm&gt;&lt;revision&gt;+&#96; &#42;
&#96;+&lt;number&gt;.&lt;revision&gt;+&#96; &#42;
&#96;+&lt;number&gt;.&lt;scm&gt;&lt;revision&gt;+&#96; &#42;
&#96;+&lt;scm&gt;&lt;date&gt;.&lt;revision&gt;+&#96; &#42;
&#96;+&lt;scm&gt;&lt;number&gt;.&lt;revision&gt;+&#96;

Where &#96;+&lt;scm&gt;+&#96; is a short string identifying the source
code control system upstream uses (e.g. \'git\', \'svn\', \'hg\') or the
string \'snap\'. The &#96;+&lt;scm&gt;+&#96; string may be abbreviated
to a single letter. &#96;+&lt;revision&gt;+&#96; is either a short git
commit hash, a subversion revision number, or something else useful in
identifying the precise revision in upstream's source code control
system. If the version control system does not provide an identifier
(e.g. CVS), this part should be omitted. A full hash &#42;&#42;should
not&#42;&#42; be used for &#96;+&lt;revision&gt;+&#96;, to avoid overly
long version numbers; only the first 7 to 10 characters.

For example, if the last upstream release was &#96;+0.4.1+&#96;, a
snapshot could use &#96;+0.4.1\^20200601g01234ae+&#96; in the
&#96;+Version:+&#96; field. Similarly, if the upstream then makes a
pre-release with version &#96;+0.5.0-rc1+&#96;, but it is buggy, and we
need to actually package two post-pre-release snapshots, those shapshots
could use &#96;+0.5.0\~rc1\^20200701gdeadf00f+&#96; and
&#96;+0.5.0\~rc1\^20200702gdeadaeae+&#96; in the &#96;+Version:+&#96;
field.

Alternatively, those three snapshots could be versioned as
&#96;+0.4.1\^1.git01234ae+&#96;, &#96;+0.5.0\~rc1\^1.gitdeadf00f+&#96;
and &#96;+0.5.0\~rc1\^2.gitdeadaeae+&#96;.

Note that &#96;+0.4.1\^&lt;something&gt;+&#96; sorts higher than
&#96;+0.4.1+&#96;, but lower than both &#96;+0.4.2+&#96; and
&#96;+0.4.1.&lt;anything&gt;+&#96;.

### Upstream has never chosen a version {#_upstream_has_never_chosen_a_version}

When upstream has never chosen a version, you &#42;&#42;must&#42;&#42;
use &#96;+Version: 0+&#96;. \'0\' sorts lower than any other possible
value that upstream might choose. If upstream does choose to release
\'version 0\', then just set &#96;+Release:+&#96; higher than the
previous value. (When &#96;%autorelease&#96; is used, this happens
automatically.)

### Upstream uses invalid characters in the version {#_upstream_uses_invalid_characters_in_the_version}

It's possible that upstream uses characters besides ASCII letters (upper
and lower case), digits and periods in its version. They must be removed
and potentially replaced with valid characters. Any such alterations
&#42;&#42;must&#42;&#42; be documented in the specfile. It is not
possible to cover all potential situations here, so it is left to the
packager to alter the upstream versioning scheme consistently.

After altering the version to be free of invalid characters, see
&lt;&lt;Unsortable versions&gt;&gt; below if the modifications, when
applied to successive releases from upstream, will not order properly.

### Unsortable versions {#_unsortable_versions}

When upstream uses a versioning scheme that does not sort properly,
first see if simply inserting a tilde or caret is enough to make the
string sortable.

For example, if upstream uses a sequence like &#96;+1.2pre1+&#96;,
&#96;+1.2pre2+&#96;, &#96;+1.2final+&#96;, then &#96;+1.2\~pre1+&#96;,
&#96;+1.2\~pre2+&#96;, &#96;+1.2_final+&#96; could be used as
&#96;+Version+&#96;. The underscore (\'&#96;+\_+&#96;\') is a visual
separator that does not influence sort order, and is used here because
\'final\' does not form a separate version component.

If this is not possible, use something similar to the snapshot version
information field described above, with the upstream version moved to
the second part of the snapshot information field:
&#96;+&lt;date&gt;.&lt;version&gt;+&#96;.

For example, if upstream releases versions &#96;+I+&#96;,
&#96;+II+&#96;, ..., &#96;+VIII+&#96;, &#96;+IX+&#96; use
&#96;+20200101.I+&#96;, &#96;+20200201.II+&#96;, ...,
&#96;+20200801.III+&#96;, &#96;+20200901.IX+&#96; in the
&#96;+Version+&#96; field.

### Upstream breaks version scheme {#_upstream_breaks_version_scheme}

It is possible that upstream simply adopts a different versioning
scheme, fails to follow an expected pattern, or even simply resets their
version to some lower value. If none of the above operations can help
with giving a version which sorts properly, or give you a version which
sorts lower than the packages already in Fedora, then you have little
recourse but to increment the &#96;+Epoch:+&#96; tag, or to begin using
it by adding &#96;+Epoch: 1+&#96;. At the same time, try to work with
upstream to hopefully minimize the need to involve &#96;+Epoch:+&#96; in
the future.

### Examples {#_examples_3}

#### Comparing versions with &#96;rpmdev-vercmp&#96; {#_comparing_versions_with_96rpmdev_vercmp96}

When in doubt, verify the sorting with &#96;rpmdev-vercmp&#96; from the
&#96;rpmdevtools&#96; package:

&#96;&#96;&#96;console \$ rpmdev-vercmp 2\~almost\^post 2.0.1
2\~almost\^post &lt; 2.0.1 &#96;&#96;&#96;

#### Simple versioning {#_simple_versioning_2}

+----------------------+----------------------+-----------------------+
| Upstream version     | Version tag          | Explanation           |
+======================+======================+=======================+
| 1.0                  | 1.0                  | The first release.    |
+----------------------+----------------------+-----------------------+
| 1.1                  | 1.1                  | An upstream update.   |
+----------------------+----------------------+-----------------------+
| 1.2.1                | 1.2.1                | Another upstream      |
|                      |                      | update. Extra levels  |
|                      |                      | of versioning are     |
|                      |                      | OK...                 |
+----------------------+----------------------+-----------------------+
| 1.3                  | 1.3                  | ...they can come and  |
|                      |                      | go without problems.  |
+----------------------+----------------------+-----------------------+

In this case the full N-V-R could be e.g.
&#96;pkg-1.2.1-1.fc{CURRENTVER}&#96; (immediately after an update) or
&#96;pkg-1.2.1-5.fc{CURRENTVER}&#96; (after downstream rebuilds with the
same upstream version).

+----------------------+----------------------+-----------------------+
| Upstream version     | Version tag          | Explanation           |
+======================+======================+=======================+
| 5.2                  | 5.2                  | Upstream release.     |
+----------------------+----------------------+-----------------------+
| 5.2a                 | 5.2a                 | Upstream introduced a |
|                      |                      | letter to indicate a  |
|                      |                      | patch release. You    |
|                      |                      | trust upstream to use |
|                      |                      | letters in            |
|                      |                      | alphabetical order,   |
|                      |                      | so it's OK to use the |
|                      |                      | version as is.        |
+----------------------+----------------------+-----------------------+
| 5.2b                 | 5.2b                 | Another patch release |
|                      |                      | after 5.2 --- this is |
|                      |                      | not a beta.           |
+----------------------+----------------------+-----------------------+
| 5.2b.1               | 5.2b.1               | Even this is OK as    |
|                      |                      | long as the sequence  |
|                      |                      | increases.            |
+----------------------+----------------------+-----------------------+
| 5.3                  | 5.3                  | Another upstream      |
|                      |                      | release.              |
+----------------------+----------------------+-----------------------+

In this case the full N-V-R could be e.g.
&#96;pkg-5.2b.1-1.fc{CURRENTVER}&#96;.

#### Complex versioning with a reasonable upstream {#_complex_versioning_with_a_reasonable_upstream}

+----------------------+----------------------+-----------------------+
| Upstream version     | Version tag          | Notes                 |
+======================+======================+=======================+
| 1.0.0-rc1            | &#                   | first prerelease      |
|                      | 96;+1.0.0\~rc1+&#96; |                       |
+----------------------+----------------------+-----------------------+
| 1.0.0-rc2            | &#                   | second prerelease     |
|                      | 96;+1.0.0\~rc2+&#96; |                       |
+----------------------+----------------------+-----------------------+
| 1.0.0                | &#96;+1.0.0+&#96;    | release               |
+----------------------+----------------------+-----------------------+
| 1.0.1                | &#96;+1.0.1+&#96;    | bugfix release        |
+----------------------+----------------------+-----------------------+
| 1.0.1-security1      | &#96;+pkg-1          | security bufix        |
|                      | .0.1.security1+&#96; | release               |
+----------------------+----------------------+-----------------------+

In this case the full N-V-R could be e.g.
&#96;pkg-1.0.0\~rc2-42.fc{CURRENTVER}&#96; (if many rebuilds were done).

#### Complex versioning with non-sorting upstream post-release versions {#_complex_versioning_with_non_sorting_upstream_post_release_versions}

+----------------------+----------------------+-----------------------+
| Upstream version     | Version tag          | Notes                 |
+======================+======================+=======================+
| 1.1.0\~BETA          | &#9                  | this is a prerelease, |
|                      | 6;+1.1.0\~BETA+&#96; | first beta            |
+----------------------+----------------------+-----------------------+
| 1.1.0\~BETA1         | &#96                 | this is a prerelease, |
|                      | ;+1.1.0\~BETA1+&#96; | second beta           |
+----------------------+----------------------+-----------------------+
| 1.1.0\~BETA2         | &#96                 | this is a prerelease, |
|                      | ;+1.1.0\~BETA2+&#96; | third beta            |
+----------------------+----------------------+-----------------------+
| 1.1.0\~CR1           | &#                   | this is a prerelease, |
|                      | 96;+1.1.0\~CR1+&#96; | candidate release 1   |
+----------------------+----------------------+-----------------------+
| 1.1.0\~CR2           | &#                   | this is a prerelease, |
|                      | 96;+1.1.0\~CR2+&#96; | candidate release 2   |
+----------------------+----------------------+-----------------------+
| 1.1.0-1%             | &#96;+1.1.0+&#96;    | final release         |
+----------------------+----------------------+-----------------------+
| 1.1.0-GA1            | &#96;+1.1.           | post release, GA1     |
|                      | 0.20201001.GA1+&#96; |                       |
+----------------------+----------------------+-----------------------+
| 1.1.0-CP1            | &#96;+1.1.           | post release, CP1,    |
|                      | 0.20201011.CP1+&#96; | after GA1, does not   |
|                      |                      | sort properly         |
+----------------------+----------------------+-----------------------+
| 1.1.0-CP2            | &#96;+1.1.           | post release, CP2,    |
|                      | 0.20201101.CP2+&#96; | after CP1             |
+----------------------+----------------------+-----------------------+
| 1.1.0-SP1            | &#96;+1.1.           | post release, SP1,    |
|                      | 0.20210101.SP1+&#96; | after CP2             |
+----------------------+----------------------+-----------------------+
| 1.1.0-SP1-CP1        | &#96;+1.1.0.20       | post release,         |
|                      | 210105.SP1_CP1+&#96; | SP1_CP1, after SP1    |
+----------------------+----------------------+-----------------------+

In this case the full N-V-R could be e.g.
&#96;pkg-1.1.0.20210105.SP1_CP1-1.fc{CURRENTVER}&#96;.

#### Complex versioning with a pre- and post-release snapshots {#_complex_versioning_with_a_pre_and_post_release_snapshots}

+----------------------+----------------------+-----------------------+
| Upstream version     | Version              | Notes                 |
+======================+======================+=======================+
| 1.0.0-rc1            | &#                   | First prerelease      |
|                      | 96;+1.0.0\~rc1+&#96; |                       |
+----------------------+----------------------+-----------------------+
| 1.0.0-rc2            | &#                   | Second prerelease     |
|                      | 96;+1.0.0\~rc2+&#96; |                       |
+----------------------+----------------------+-----------------------+
| git commit           | &#96;+1.0.0\~rc2\^20 | Post-prerelease       |
| &#96;f00fabd&#96;    | 210101gf00fabd+&#96; | snapshot              |
+----------------------+----------------------+-----------------------+
| 1.0.0                | &#96;+1.0.0+&#96;    | A release             |
+----------------------+----------------------+-----------------------+
| 1.0.1                | &#96;+1.0.1+&#96;    | A bugfix release      |
+----------------------+----------------------+-----------------------+
| git commit           | &#96;+1.0.1\^20      | A snapshot            |
| &#96;bbbccc0&#96;    | 210203gbbbccc0+&#96; |                       |
|                      | or                   |                       |
|                      | &#96;+pkg-1.0        |                       |
|                      | .1\^1.gbbbccc0+&#96; |                       |
+----------------------+----------------------+-----------------------+
| 1.0.1-security1      | &#96;+1              | A security bufix      |
|                      | .0.1.security1+&#96; | release. From past    |
|                      |                      | history we know that  |
|                      |                      | the bugfix releases   |
|                      |                      | will have sortable    |
|                      |                      | versions. If not, we  |
|                      |                      | could use             |
|                      |                      | \'&#96;+&lt;date&     |
|                      |                      | gt;.security1+&#96;\' |
|                      |                      | instead.              |
+----------------------+----------------------+-----------------------+
| git commit           | &#96;                | Another snapshot      |
| &#96;abc0202&#96;    | +1.0.1.security1\^20 |                       |
|                      | 210301gabc0202+&#96; |                       |
|                      | or                   |                       |
|                      | &#9                  |                       |
|                      | 6;+pkg-1.0.1.securit |                       |
|                      | y1\^1.gabc0202+&#96; |                       |
+----------------------+----------------------+-----------------------+

In this case the full N-V-R could be e.g.
&#96;pkg-1.0.1.security1\^20210301gabc0202-1.fc{CURRENTVER}&#96;.

\[&#35;traditional-versioning\] == Traditional versioning with part of
the upstream version information in the Release field

The method described in this section is deprecated, but
&#42;&#42;may&#42;&#42; be used. As mentioned in the [Handling
non-sorting versions with tilde, dot, and
caret](#_handling_non_sorting_versions_with_tilde_dot_and_caret) section
above, this method is recommended for packages with complex versioning
when supporting RHEL7 and other systems with old rpm versions.

In this method, &#96;+%autorelease+&#96; is not used, and the
&#96;Release&#96; field must be managed manually.

This method for dealing with most pre- and post-release versions and
unsortable versions involves potentially removing some information from
the &#96;+Version:+&#96; tag while imposing additional structure onto
the &#96;+Release:+&#96; tag. There are potentially four fields which
comprise the structured &#96;+Release:+&#96; tag:

&#42; package release number (&#96;+&lt;pkgrel&gt;+&#96;) &#42; extra
version information (&#96;+&lt;extraver&gt;+&#96;) &#42; snapshot
information (&#96;+&lt;snapinfo&gt;+&#96;) &#42; minor release bump
(&#96;+&lt;minorbump&gt;+&#96;)

The package release number &#42;&#42;must&#42;&#42; always be present
while the others may or may not be depending on the situation.

Those items which are present are combined (with periods to separate
them) to construct the final &#96;+Release:+&#96; tag. In the usual
notation where square brackets indicate that an item is optional:

&lt;pkgrel&gt;\[.&lt;extraver&gt;\]\[.&lt;snapinfo&gt;\]%{?dist}\[.&lt;minorbump&gt;\]

The actual values to be used for those three fields are situational and
are referenced in the sections below. Note that your particular
situation might not result in the use of &#96;+&lt;extraver&gt;+&#96; or
&#96;+&lt;snapinfo&gt;+&#96;, and in most situations
&#96;+&lt;minorbump&gt;+&#96; won't be used at all. Simply do not
include those which you don't have.

Note that the dist tag is supplied by other portions of the system and
may in some circumstances contain additional structure, including
tildes. As this is not under the control of the packager, that structure
is not covered here. The packager &#42;&#42;must&#42;&#42; simply
include &#96;+%{?dist}+&#96; verbatim as indicated above.

### Unsortable versions {#_unsortable_versions_2}

When upstream uses a versioning scheme that does not sort properly,
first see if there is any portion which can be removed from the right
side of the version string such that the remainder is sortable. This is
often possible if upstream uses a sequence like (\'1.2pre1\',
\'1.2pre1\', \'1.2final\'). If so, use the removed portion as
&#96;+&lt;extraver&gt;+&#96; above, and the remainder as the package
version. If this splitting leaves a leading or trailing period in either
value, remove it.

If this is not possible, use Version: 0 and move the *entire* version
string into &#96;+&lt;extraver&gt;+&#96;.

### Snapshots {#_snapshots_2}

All snapshots &#42;&#42;must&#42;&#42; contain a snapshot information
field (&#96;+&lt;snapinfo&gt;:+&#96;) in the &#96;+Release:+&#96; tag.
That field must at minimum consist of the date in eight-digit
\'YYYYMMDD\' format. The packager &#42;&#42;may&#42;&#42; include up to
17 characters of additional information after the date. The following
formats are suggested:

&#42; &#96;+YYYYMMDD.&lt;revision&gt;+&#96; &#42;
&#96;+YYYYMMDD&lt;scm&gt;&lt;revision&gt;+&#96;

Where &#96;+&lt;scm&gt;+&#96; is a short string identifying the source
code control system upstream uses (e.g. \'git\', \'svn\', \'hg\') or the
string \'snap\'. &#96;+&lt;revision&gt;+&#96; is either a short git
commit hash, a subversion revision number, or something else useful in
identifying the precise revision in upstream's source code control
system. Obviously if CVS is used, no such revision information exists,
so it would be omitted, but otherwise it &#42;&#42;should&#42;&#42; be
included.

### Prerelease versions {#_prerelease_versions}

In the &#96;+Version:+&#96; tag, use the version that upstream has
determined the next release will be. For the field of the
&#96;+Release:+&#96; tag, use a number of the form \'0.N\' where N is an
integer beginning with 1 and increasing for each revision of the
package. Prerelease versions &#42;&#42;must&#42;&#42; use a
&#96;+Release:+&#96; tag strictly less than 1, as this is the sole
indicator that a prerelease has been packaged.

### Release and post-release versions {#_release_and_post_release_versions}

For the &#96;+&lt;pkgrel&gt;+&#96; field of the &#96;+Release:+&#96;
tag, use an integer beginning with 1 and increasing for each revision of
the package. Release and post-release versions &#42;&#42;must&#42;&#42;
use a &#96;+Release:+&#96; tag greater than or equal to 1.

### Rebuilds in older branches using &#96;&lt;minorbump&gt;&#96; {#_rebuilds_in_older_branches_using_96ltminorbumpgt96}

In the situation described in &lt;&lt;Only an old branch needs a
change&gt;&gt;, you &#42;&#42;may&#42;&#42; adjust the
&#96;+Release+&#96; by appending a number &#42;after&#42; the dist tag,
creating a E-V-R for F{CURRENTVER} that still compares lower than the
one in F{NEXTVER}. Set &#96;+&lt;minorbump&gt;+&#96; to an in integer
beginning with \'1\' and increase it by one for each minor bump you need
to do. Remove &#96;+&lt;minorbump&gt;+&#96; once you are able to
increase the package release normally without introducing ordering
issues.

### Examples {#_examples_4}

Examples of many possible versioning scenarios of traditional versioning
are available from [Package Versioning
Examples](https://fedoraproject.org/wiki/Package_Versioning_Examples).

## Rawhide is allowed to lag temporarily {#_rawhide_is_allowed_to_lag_temporarily}

A package &#42;&#42;may&#42;&#42; temporarily have a lower EVR in
Rawhide when compared to a release branch of Fedora ONLY in the case
where the package fails to build in Rawhide. This permits important
updates to be pushed to existing Fedora releases regardless of the
current state of Rawhide.

# Weak Dependencies Policy {#_weak_dependencies_policy}

## Introduction {#_introduction}

Weak dependencies are basically variants of the &#96;+Requires:+&#96;
tag and are matched against (virtual) &#96;+Provides:+&#96; and package
names using &#96;+Epoch-Version-Release+&#96; range comparisons, just
like regular &#96;+Requires:+&#96;. They come in two strengths: \'weak\'
and \'hint\' and two directions \'forward\' (analogous to
&#96;+Requires:+&#96;) and \'backwards\' (which has no analog in the
previous dependency system).

+----------------------+----------------------+-----------------------+
|                      | Forward              | Backward              |
+----------------------+----------------------+-----------------------+
| Weak                 | Recommends:          | Supplements:          |
+----------------------+----------------------+-----------------------+
| Hint                 | Suggests:            | Enhances:             |
+----------------------+----------------------+-----------------------+

Weak dependencies allow smaller minimal installations while keeping the
default installation feature rich. They also allow packages to specify
preferences for specific providers while maintaining the flexibility of
virtual provides, for example, preferring ruby vs jruby or
community-mysql vs mariadb.

## Weak dependencies {#_weak_dependencies}

Weak dependencies are by default treated similarly to regular
&#96;+Requires:+&#96;. Matching packages are added to the dnf
transaction. If adding the package would lead to an error dnf will by
default ignore the dependency. This allows users to exclude packages
that would be added by weak dependencies or remove them later. To skip
installing weak dependencies, pass
&#96;\--setopt=install_weak_deps=False&#96; to &#96;dnf&#96;.

As with regular dependencies, weak dependencies MUST be satisfiable
within the official Fedora repositories.

Weak dependencies may only be used in a package if the package still
functions without the dependency present. It is acceptable, however, to
create packages that have very limited functionality without adding any
of its weak requirements. Weak dependencies should be used where
possible to minimize the installation for reasonable use cases,
especially for building virtual machines or containers that have a
single purpose only and do not require the full feature set of the
package.

Typical use cases for weak dependencies are:

&#42; Documentation &#42;&#42; Documentation viewers if missing them is
handled gracefully &#42; Examples &#42; Plug-ins or add-ons &#42;&#42;
Support for file formats &#42;&#42; Support for protocols &#42;&#42;
&#8230;

## Hints {#_hints}

Hints are by default ignored by dnf. They may be used by GUI tools to
offer add-on packages that are not installed by default but might be
useful in combination with the installed packages. The requirements of
the main use cases of a package should not merely be referenced by hints
but included by strong or weak dependencies.

## Package Preference {#_package_preference}

dnf (or more precisely libsolv) will use weak dependencies and hints to
decide which package to use if there is a choice between multiple
equally valid packages. In these cases packages that are pointed at by
dependencies from installed or to be installed packages are preferred.
Note, that this does not alter the normal rules of dependency
resolution. For example, weak dependencies cannot enforce a older
version of a package to be chosen.

If there are multiple (typically virtual) providers for a dependency the
requiring package may add a Suggests: to provide a hint to the
dependency resolver as to which option is preferred.
&#96;+Enhances:+&#96; should only be used for the rare occasion when the
main package and other providers agree that adding the hint to the
required package is for some reason the cleaner solution.

### Real life example {#_real_life_example}

Package A: Requires: mysql

Package mariadb: Provides: mysql

Package community-mysql: Provides: mysql

If you want to prefer mariadb over community-mysql -&gt; add
&#96;+Suggests:+&#96; &#96;+mariadb+&#96; to Package A.

## Forward vs Backward Dependencies {#_forward_vs_backward_dependencies}

Forward dependencies are, as Requires, evaluated for packages that are
being installed. The best of the matching (fulfilling) packages are also
installed. For reverse dependencies the packages containing the
dependency are installed if a matching package is getting installed
also.

In general forward dependencies should be used. Add the dependency to
the package getting the other package added to the system.

Reverse dependencies are mainly designed for 3rd party vendors who can
attach their plug-ins/add-ons/extensions to distribution or other 3rd
party packages. Within Fedora the control over which packages a package
requires should stay with the package maintainer. There are, however,
cases when it is easier for the requiring package not needing to care
about all add-ons. In this cases reverse dependencies may be used with
the agreement of the package maintainer of the targeted package.

Note, that EPEL or other third party repositories may have (and are
encouraged to have) a different policy.

# What can be packaged {#_what_can_be_packaged}

Not everything can be packaged in Fedora. Most things considered to be
\'free software\' or \'open source software\' are permitted, but
definitions of these are not always consistent and Fedora has a few
specific requirements and exceptions. This is an overview of some
specific requirements and exceptions, but it is not intended to be
exhaustive. If questions arise, the [Packaging
Committee](https://fedoraproject.org/wiki/Packaging_Committee) and the
[Legal Team](https://fedoraproject.org/wiki/Legal:Main) are the primary
places to receive answers.

## Legal Issues {#_legal_issues}

Some software (or in some cases, portions of that software) cannot be
packaged for legal reasons. This includes issues related to licensing,
patents, trademark law, etc.

See the following pages for various examples.

&#42; <https://fedoraproject.org/wiki/Legal:Main> &#42;
<https://fedoraproject.org/wiki/Legal:Licenses> &#42;
<https://fedoraproject.org/wiki/Forbidden_items>

## Impermissible Content {#_impermissible_content}

It is important to make distinction between computer executable code and
content. While code is permitted (assuming, of course, that it has an
open source compatible license, is not legally questionable, etc.), only
some kinds of content are permissible.

The rule is this:

If the content enhances the OS user experience, then the content is OK
to be packaged in Fedora. This means, for example, that things like:
fonts, themes, clipart, and wallpaper are OK.

Content still has to be reviewed for inclusion. It must have an open
source compatible license, must not be legally questionable. In
addition, there are several additional restrictions for content:

&#42; Content must not be pornographic, or contain nudity, whether
animated, simulated, or photographed. There are better places on the
Internet to get porn. &#42; Content should not be offensive,
discriminatory, or derogatory. If you're not sure if a piece of content
is one of these things, it probably is. &#42; All content is subject to
review by FESCo, who has the final say on whether or not it can be
included.

Some examples of content which is permissible:

&#42; Package documentation or help files. &#42; Clipart for use in
office suites. &#42; Background images (non-offensive, discriminatory,
with permission to freely redistribute). &#42; Fonts (under an open
source license, with no ownership/legal concerns). &#42; Game levels are
not considered content, since games without levels would be non
functional. &#42; Sound or graphics included with the source tarball
that the program or theme uses (or the documentation uses) are
acceptable. &#42; Game music or audio content is permissible, as long as
the content is freely distributable without restriction, and the format
is not patent encumbered. &#42; Example files included with the source
tarball are not considered content.

Some examples of content which are not permissible:

&#42; Comic book art files &#42; Religious texts &#42; Files in
patent-encumbered media formats

If you are unsure if something is considered approved content, ask the
[Packaging
Committee](https://fedoraproject.org/wiki/Packaging_Committee) or, if
your question is of a legal nature, [Legal
Team](https://fedoraproject.org/wiki/Legal:Main).

## Packages which are not useful without external code {#_packages_which_are_not_useful_without_external_code}

Some software is not functional or useful without the presence of
external code dependencies in the runtime operating system environment.
When those external code dependencies are non-free, legally
unacceptable, or binary-only (with the exception of permissible
firmware), then the dependent software is not acceptable for inclusion
in Fedora. If the code dependencies are acceptable for Fedora, then they
should be packaged and included in Fedora as a pre-requisite for
inclusion of the dependent software. Software which downloads code
bundles from the internet in order to be functional or useful is not
acceptable for inclusion in Fedora (regardless of whether the downloaded
code would be acceptable to be packaged in Fedora as a proper
dependency).

This also means that packages which are not functional or useful without
code or packages from third-party sources are not acceptable for
inclusion in Fedora.

## Only one kernel package {#_only_one_kernel_package}

Fedora allows only a single kernel package; packages containing
alternate kernels are not allowed in the distribution. If there are
kernel features which would be generally useful, please communicate with
the [Kernel Team](https://fedoraproject.org/wiki/Kernel).

## No external kernel modules {#_no_external_kernel_modules}

Fedora does not allow kernel modules to be packaged outside of the main
kernel package. You should communicate with the [Kernel
Team](https://fedoraproject.org/wiki/Kernel) regarding enabling
additional kernel modules.

\[&#35;prebuilt-binaries-or-libraries\] == No inclusion of pre-built
binaries or libraries

All program binaries and program libraries included in Fedora packages
must be built from the source code that is included in the source
package. This is a requirement for the following reasons:

&#42; Security: Pre-packaged program binaries and program libraries not
built from the source code could contain parts that are malicious,
dangerous, or just broken. Also, these are functionally impossible to
patch. &#42; Compiler Flags: Pre-packaged program binaries and program
libraries not built from the source code were probably not compiled with
standard Fedora compiler flags for security and optimization.

Content binaries (such as .pdf, .png, .ps files) are *not* required to
be rebuilt from the source code.

If you are in doubt as to whether something is considered a program
binary or a program library, here is some helpful criteria:

&#42; Is it executable? If so, it is probably a program binary. &#42;
Does it contain a &#96;+.so+&#96;, &#96;+.so.&#35;+&#96;, or
&#96;+.so.&#35;.&#35;.&#35;+&#96; extension? If so, it is probably a
program library. &#42; If in doubt, ask your reviewer. If the reviewer
is not sure, they should ask the Fedora Packaging Committee.

Packages which require non-open source components to build are also not
permitted (e.g. proprietary compiler required).

When you encounter prebuilt binaries in a package you &#42;MUST&#42;:

&#42; Remove all pre-built program binaries and program libraries in
%prep prior to the building of the package. Examples include, but are
not limited to, &#96;+&#42;.class+&#96;, &#96;+&#42;.dll+&#96;,
&#96;+&#42;.DS_Store+&#96;, &#96;+&#42;.exe+&#96;,
&#96;+&#42;.jar+&#96;, &#96;+&#42;.o+&#96;, &#96;+&#42;.pyc+&#96;,
&#96;+&#42;.pyo+&#96;, &#96;+&#42;.egg+&#96;, &#96;+&#42;.so+&#96;,
&#96;+&#42;.swf+&#96; files. &#42; Ask upstream to remove the binaries
in their next release.

### Exceptions {#_exceptions_2}

&#42; Some software (usually related to compilers or cross-compiler
environments) cannot be built without the use of a previous toolchain or
development environment (open source). If you have a package which meets
this criteria, contact the Fedora Packaging Committee for approval.
Please note that this exception, if granted, is limited to only the
initial build of the package. You may bootstrap this build with a
\'bootstrap\' pre-built binary, but after this is complete, you must
immediately increment Release, drop the \'bootstrap\' pre-built binary,
and build completely from source. Bootstrapped packages containing
pre-built \'bootstrap\' binaries must not be pushed as release packages
or updates under any circumstances. These packages should contain the
necessary logic to be built once bootstrapping is completed and the
prebuilt programs are no longer needed. Information about how you should
break circular dependencies by bootstrapping can be found
[here](index.adoc&#35;bootstrapping). &#42; An exception is made for
binary firmware, as long as it meets the requirements documented
[here](https://fedoraproject.org/wiki/Licensing:Main&#35;Binary_Firmware).
&#42; Some pre-packaged program binaries or program libraries may be
under terms which do not permit redistribution, or be affected by legal
scenarios such as patents. In such situations, simply deleting these
files in %prep is not sufficient, the maintainer will need to make a
modified source that does not contain these files. See: [When Upstream
uses Prohibited
Code](SourceURL.adoc&#35;when-upstream-uses-prohibited-code).

\[&#35;pregenerated-code\] == Pregenerated code

Often a package will contain code which was itself generated by other
code. This often takes the form of configure files or parsing code
generated by bison/yacc or lex/flex.

It is required that the original source files from which the code was
generated be included in the source package. Generally these files are
part of the source archive supplied by upstream, but it may be necessary
to fetch those files from an upstream source repository and include them
in the source package as separate Source: entries.

It is preferred, but not required, that the tools used to generate such
code be free software and included in Fedora.

It is suggested, but not required, that such code be regenerated as part
of the build process. The means for doing this are entirely specific to
the individual package being built, but it may happen automatically if
the necessary dependencies are present at build time.

&#42; Build Systems :last-reviewed: 2020-07-18

# CMake Packaging Guidelines {#_cmake_packaging_guidelines}

This document provides best practices for the usage of [the CMake build
system](https://cmake.org/) in Fedora packages.

## Build Dependencies {#_build_dependencies_2}

You &#42;MUST&#42; add following BuildRequires:

``` _rpm-spec
BuildRequires: cmake
```

## Available Macros {#_available_macros_2}

You will generally make use of these in your specs:

&#96;+%cmake+&#96;

:   Defines CFLAGS, LDFLAGS, etc. and calls &#96;+%\_\_cmake+&#96; with
    appropriate parameters (&#96;+-DCMAKE_INSTALL_PREFIX:PATH=/usr+&#96;
    and such). You can pass &#96;+-Doption=value+&#96; to this macro in
    order to set options for the buildsystem.

&#96;+%cmake_build+&#96;

:   Builds the project (using &#96;+%\_\_cmake \--build+&#96;).

&#96;+%cmake_install+&#96;

:   Installs the built project (using &#96;+%\_\_cmake
    \--install+&#96;).

&#96;+%ctest+&#96;

:   Runs the tests that are defined with &#96;+add_test()\\&#96; in
    project (using \\&#96;%\_\_ctest+&#96;).

When packaging KDE software, you most likely would replace
&#96;+%cmake+&#96; with either &#96;+%cmake_kf5+&#96; or
&#96;+%cmake_kf6+&#96;. For more information, see [KDE Packaging
Guidelines](KDEPackaging.xml).

It is rarely necessary (but permissible) to use or alter these:

:::: note
::: title
:::

All macros starting with double underscore is meant to be private, NOT
stable and likely to be removed in the future.
::::

&#96;+%\_\_cmake+&#96;

:   The path to the cmake executable.

&#96;+%\_\_ctest+&#96;

:   The path to the ctest executable.

&#96;+%\_\_cmake_in_source_build+&#96;

:   Controls whether builds are done
    [out-of-source](https://fedoraproject.org/wiki/Changes/CMake_to_do_out-of-source_builds)
    (when undefined, the default) or in-source (when defined). Whenever
    possible, using out-of-source builds is advised, as this is the
    direction both Fedora and CMake upstream are moving.

&#96;+%\_\_cmake_builddir+&#96;

:   Holds the location of the actual directory where the build was made.
    When making out-of-source builds, this macro is the same as
    [%\_vpath_builddir](vpath.xml). When doing in-source builds, this
    macro will hold the actual location that was used for the build.

    :::: warning
    ::: title
    :::

    This macro is suitable only for rare compatibility reasons. For
    normal out-of-source builds, this macro is the same as
    &#96;+%\_vpath_builddir+&#96;. It may be removed in the future.
    ::::

## Example Usage {#_example_usage}

``` _rpm-spec
%conf
%cmake

%build
%cmake_build

%install
%cmake_install

%check
%ctest
```

&#42;NOTE:&#42; If building for &lt; EPEL 10 then &#96;%cmake&#96;
should be in &#96;%build&#96;.

## Notes {#_notes}

&#96;+-DCMAKE_SKIP_RPATH:BOOL=ON+&#96;. With recent cmake-2.4, it should
not be used. This CMake version should handle RPATHs issues correctly
(set them in build-dir, remove them during installation). Setting
&#96;+CMAKE_SKIP_RPATH+&#96; for this version would avoid RPATHs in
build-dir too. This might link binaries against system-libraries (e.g.
when a previous version of the package was installed) instead of the
libraries which were created by the build.

Nevertheless, RPATH issues might arise when CMake was used improperly.
For example, installing a target with &#96;+INSTALL(FILES &#8230; RENAME
&#8230;)\\&#96; will \\&#42;not\\&#42; strip rpaths; in this case
\\&#96;+INSTALL(TARGETS \\&#8230;)&#96; must be used in combination with
changing the &#96;+OUTPUT_NAME+&#96; property.

CMake has good documentation in two places:

&#42; <https://cmake.org/documentation/> &#42;
<https://gitlab.kitware.com/cmake/community/wikis/Home>

# Meson Packaging Guidelines {#_meson_packaging_guidelines}

This document provides best practices for the usage of [the Meson build
system](https://mesonbuild.com/) in Fedora packages. Meson is a build
system (similar to automake) which can generate code for other
lower-level build systems. For example, it can generate code for
[ninja](https://ninja-build.org/). When packaging software which builds
using Meson it's important to use the &#96;+%meson+&#96; macros instead
of &#96;+%ninja+&#96; or other lower-level build system macros directly.
The backend used by Meson could change.

## Build Dependencies {#_build_dependencies_3}

You &#42;MUST&#42; add following BuildRequires:

&#8230;. BuildRequires: meson &#8230;.

## Available Macros {#_available_macros_3}

You will generally make use of these in your specs:

&#96;+%meson+&#96;

:   Defines CFLAGS, LDFLAGS, etc. and calls &#96;+%\_\_meson+&#96; with
    appropriate parameters (&#96;+\--libdir=%{\_libdir}\\&#96; and
    such). You can pass \\&#96;-Doption=value+&#96; to this macro in
    order to set options for the buildsystem.

&#96;+%meson_build+&#96;

:   An alias for &#96;+%ninja_build -C %{\_vpath_builddir}+&#96;.

&#96;+%meson_install+&#96;

:   An alias for &#96;+%ninja_install -C %{\_vpath_builddir}+&#96;.

&#96;+%meson_test+&#96;

:   An alias for &#96;+%ninja_test -C %{\_vpath_builddir}+&#96;.

It is rarely necessary (but permissible) to use or alter these:

&#96;+%\_\_meson+&#96;

:   The path to the meson executable

Also see [Defining source and build directories](vpath.xml).

## Example RPM spec file {#_example_rpm_spec_file}

&#8230;. %global \_vpath_srcdir sdk/%{name}/projects/meson

Name: angelscript Version: 2.31.1 Release: 1%{?dist} Summary: Flexible
cross-platform scripting library

License: zlib URL: <https://www.angelcode.com/angelscript/> Source:
%{url}sdk/files/%{name}\_%{version}.zip

BuildRequires: meson BuildRequires: gcc

%package devel Summary: Development libraries and header files for
%{name} Requires: %{name}%{?\_isa} =
%{?epoch:%{epoch}:}%{version}-%{release}

%description devel %{summary}.

%prep %autosetup -c

%conf %meson

%build %meson_build

%install %meson_install

%check %meson_test

%files %{\_libdir}/lib%{name}.so.&#42;

%files devel %{\_libdir}/lib%{name}.so %{\_includedir}/%{name}.h
&#8230;.

&#42;NOTE:&#42; If building for &lt; EPEL 10 then &#96;%meson&#96;
should be in &#96;%build&#96;.

&#42; Programming Languages = Ada Packaging Guidelines

This document describes the current policies for packaging Ada programs
and libraries for Fedora. These are Ada-specific amendments to the
generic Packaging Guidelines. Ada packages must also conform to the
[Packaging Guidelines](../) and the [Review
Guidelines](../ReviewGuidelines/).

## Compilation {#_compilation}

&#42; Ada code in Fedora &#42;MUST&#42; be compiled using GNAT, the
default Ada compiler in Fedora. All packages that contain Ada code
&#42;MUST&#42; have "&#96;+BuildRequires: gcc-gnat+&#96;" to ensure that
the compiler is available. &#42; The GNAT tools are usually invoked
through the builder GPRbuild, so Ada packages typically need
"&#96;+BuildRequires: gprbuild+&#96;". &#42; There are a number of RPM
macros that contain Fedora's standard compiler and linker flags adapted
for GNAT. The appropriate macro &#42;MUST&#42; be used in the build
stage. The right macro to use depends on what build tools the package
uses. &#42;&#42; For packages that are built with GPRbuild or Gnatmake
but without Comfignat there are the macros
\\\<var\\\>GPRbuild_flags\\\</var\\\> and
\\\<var\\\>Gnatmake_flags\\\</var\\\>, which contain builder, compiler
and linker flags. &#42;&#42; In case a package's build system invokes
the underlying GNAT tools without using GPRbuild or Gnatmake, then the
appropriate macro for each tool &#42;MUST&#42; be used. If for example
Gnatlink is invoked directly, then the expansion of
\\\<var\\\>Gnatlink_flags\\\</var\\\> shall be passed to it. &#42;&#42;
For packages whose build systems use Comfignat there is the macro
\\\<var\\\>Comfignat_make\\\</var\\\>. It expands to a Make command with
appropriate values for Comfignat's configuration variables, including
builder, compiler and linker flags, directory variables and the
directories project. Use it alone to build the default target:

\+ &#8230;. %build %{Comfignat_make} &#8230;.

\+ If needed, a different target and/or additional variables may be
appended:

\+ &#8230;. %{Comfignat_make} demo_programs atomic_doodads=true &#8230;.

\+ For the installation stage of Comfignat-using packages, the macro
\\\<var\\\>make_install\\\</var\\\> (&#42;not&#42;
\\\<var\\\>makeinstall\\\</var\\\>) is recommended. &#42; The macros
\\\<var\\\>GPRbuild_arches\\\</var\\\> and
\\\<var\\\>GNAT_arches\\\</var\\\> expand to a list of architectures
where GNAT packages are available in Fedora. When there is a need to
prevent attempts to build an Ada package on secondary architectures
where GNAT has not been bootstrapped, this &#42;MUST&#42; be done with
either "&#96;+ExclusiveArch: %{GPRbuild_arches}\\&#96;" or
"\\&#96;+ExclusiveArch: %{GNAT_arches}&#96;". &#42; All packages that
contain Ada code &#42;MUST&#42; have "&#96;+BuildRequires:
fedora-gnat-project-common+&#96;" to ensure that the necessary RPM
macros are defined. &#42; If the upstream source package comes with a
build system, for example a GNAT project file or makefiles and a
configuration script, then it's probably best to use that if possible.
If not, it is recommended that the packager write a GNAT project file
and use GPRbuild to control the compilation.

### Trampolines {#_trampolines}

An executable stack has been made a linker error in Fedora. This can
affect Ada packages because [GCC uses
trampolines](https://gcc.gnu.org/onlinedocs/gccint/Trampolines.html) to
implement some language constructs. The compiler's usage of trampolines
has been greatly reduced, but [some cases
remain](https://gcc.gnu.org/onlinedocs/gnat_rm/No_005fImplicit_005fDynamic_005fCode.html).
One case that occurs is when a nested subprogram in Ada is passed as a
callback routine to a function written in C -- which means that the
executable stack is also exposed to C code that may contain buffer
overflows. In such cases the options are to explicitly allow an
executable stack by passing "&#96;+-largs
-Wl,\--no-warn-execstack+&#96;" to GPRbuild, or restructure the code to
eliminate the need for trampolines. Which option is best may depend on
how exposed the program is to potentially hostile input.

Correct usage of the RPM macros should result in a warning message from
the compiler that points out where in the code a trampoline is needed.

## Runpaths {#_runpaths}

GPRbuild adds a runpath to the built binaries by default. Fedora's
builder flags normally include an option to disable the automatic
runpath. There are however cases where it would be advantageous to allow
a runpath. Libraries can have test suites or auxiliary programs that
aren't installed but run during the build and need to link to the
library in the build directory, and they may rely on an automatic
runpath for this. In those cases the spec file may define a macro named
\\\<var\\\>GNAT_add_rpath\\\</var\\\>. The builder will then be allowed
to add a runpath in those parts of the spec file where
\\\<var\\\>GNAT_add_rpath\\\</var\\\> is defined.

:::: note
::: title
:::

\\\<var\\\>GNAT_add_rpath\\\</var\\\> does not exempt a package from the
Packaging Guidelines. [The policy on runpaths](../&#35;_beware_of_rpath)
still applies.
::::

## Devel packages {#_devel_packages}

&#42; Ada library packages &#42;MUST&#42; have a -devel subpackage
containing all the files that are necessary for compilation of code that
uses the library. This includes Ada specification files (\\&#42;.ads),
Ada body files (\\&#42;.adb), Ada library information files
(\\&#42;.ali) and GNAT project files (\\&#42;.gpr). (There is no
requirement to include all body files. Typically only some body files
are needed.)

&#42; The -devel package &#42;MUST NOT&#42; contain any makefiles or
other files that are only used for recompiling the library.

&#42; The -devel package &#42;MUST NOT&#42; contain any \\&#42;.o files.

### GNAT project files {#_gnat_project_files}

&#42; The -devel package &#42;MUST&#42; contain one or more GNAT project
files to be imported by other projects that use the library.

&#42; Project files &#42;MUST&#42; be architecture-independent. This
means that the same project file must point to libraries in /usr/lib or
/usr/lib64 depending on what target architecture the compiler is
currently compiling for. This &#42;SHOULD&#42; be done by importing the
"directories" project (that is, the project file directories.gpr) and
using the variable \\\<var\\\>Directories.Libdir\\\</var\\\> which is
defined there. The value of \\\<var\\\>Directories.Libdir\\\</var\\\> is
set to either "/usr/lib" or "/usr/lib64" depending on the hardware
platform.

&#42; Project files &#42;MUST NOT&#42; contain hard-coded directory
names, neither absolute nor relative; they should get them from some
source. The source may be an Autoconf-generated configuration script or
other build system. Project files that aren't pre-processed by such a
build system &#42;SHOULD&#42; use the variable
\\\<var\\\>Directories.Includedir\\\</var\\\> rather than a hard-coded
"/usr/include".

&#42; If the "directories" project is used, then the -devel package
&#42;MUST&#42; have an explicit "&#96;+Requires:
fedora-gnat-project-common+&#96;".

&#42; Project files &#42;MUST&#42; have an
\\\<var\\\>Externally_Built\\\</var\\\> attribute equal to "true".

Here's an example of what a project file installed with a library may
look like:

&#8230;. with \'directories\'; project Example is for Library_Name use
\'example\'; for Source_Dirs use (Directories.Includedir &amp;
\'/example\'); for Library_Dir use Directories.Libdir; for
Library_ALI_Dir use Directories.Libdir &amp; \'/example\'; for
Externally_Built use \'true\'; end Example; &#8230;.

## File placement {#_file_placement}

&#42; Ada source files in -devel packages (\\&#42;.ads and \\&#42;.adb)
&#42;MUST&#42; be placed in the &#96;+%{\_includedir}\\&#96; directory
or a subdirectory thereof. Placing them directly in
\\&#96;%{\_includedir}\\&#96; may be appropriate if there are very few
of them in the package and their names include the name of the library.
Otherwise they should usually be placed in a subdirectory, for example
\\&#96;%{\_includedir}/%{name}+&#96;.

&#42; Ada library information files (\\&#42;.ali) &#42;MUST&#42; be
placed in a subdirectory of &#96;+%{\_libdir}\\&#96;, for example
\\&#96;%{\_libdir}/%{name}+&#96;.

&#42; GNAT projects files (\\&#42;.gpr) &#42;MUST&#42; be placed in the
&#96;+%{\_GNAT_project_dir}\\&#96; directory or a subdirectory thereof.
A subdirectory, for example \\&#96;%{\_GNAT_project_dir}/%{name}\\&#96;,
may be a good idea if there are lots of project files in the same
package or if they have generic names. Otherwise they should usually be
placed directly in \\&#96;%{\_GNAT_project_dir}+&#96;. The name of the
library &#42;MUST&#42; be included either in the name of each project
file or in the name of the subdirectory where the project files are
placed.

Packages that use GPRinstall in the installation phase can use the macro
\\\<var\\\>GPRinstall_flags\\\</var\\\> to pass the correct pathnames
and other parameters to GPRinstall.

# C and C++ Packaging Guidelines {#_c_and_c_packaging_guidelines}

## Introduction {#_introduction_2}

The C and C++ languages and runtimes are one of the most common
development frameworks for packages in fedora. As such there is a wide
variety of quality, style, and convention in all of those packages. The
follow document provides best practice for certain aspects of C and C++
packaging.

## Packaging {#_packaging}

### BuildRequires and Requires {#_buildrequires_and_requires}

If your application is a C or C++ application you must list a
&#96;BuildRequires&#96; against &#96;gcc&#96;, &#96;gcc-c++&#96; or
&#96;clang&#96;. Those packages will include everything that is required
to build a standards conforming C or C++ application.

If your library includes standard C or C++ headers, you must list
&#96;BuildRequires&#96; against &#96;gcc&#96;, &#96;gcc-c++&#96;, or
&#96;clang&#96; to install the needed standards conforming headers.

If at runtime you use &#96;cpp&#96; to process C or C++ language headers
then you have no choice but to use &#96;Requires&#96; for &#96;gcc&#96;,
&#96;gcc-c\\&#96;, or \\&#96;clang\\&#96; to install the required
headers for a standard conforming C or {cpp} application. In the future
this might change if a set of standard C or {cpp} language headers are
provided by a special-purpose provides e.g. \\&#96;c-headers\\&#96; or
\\&#96;c-headers&#96;.

You need not include a &#96;BuildRequires&#96; or &#96;Requires&#96; on
&#96;glibc-headers&#96;, or any other core C or C++ implementation
package unless you have a specific and special need e.g. static
compilation requires the &#96;.&#42;-static&#96; library packages e.g.
&#96;BuildRequires: glibc-static&#96;. The default use case of a
dynamically compiled C or C++ application is taken care of by the
&#96;gcc&#96;, &#96;gcc-c++&#96;, and &#96;clang&#96; packages.

Please refer to [Compiler Guidelines](index.adoc&#35;compiler) for the
list of supported compilers for C and C++ compilers.

### Packaging Q&amp;A {#_packaging_qampa}

**Q:** Do I need a &#96;Requires: glibc&#96; to ensure I have the C
runtime installed for my application?

**A:** No. RPM will automatically determine what ELF libraries you need
based on the binaries in your package. This is sufficient to cause glibc
to be installed.

**Q:** Do I need to include a &#96;Requires: libgcc&#96;?

**A:** If you are using an API from &#96;libgcc&#96; directly, then yes,
you must have a &#96;Requires: libgcc&#96;. In general though
&#96;glibc&#96; requires &#96;libgcc&#96;, so it is always installed.

## Libraries {#_libraries}

Libraries should have unique shared object names (SONAMEs via
&#96;-Wl,-soname=libfoo.so&#96;) that do not conflict with other library
SONAMEs used in the distribution. For example there should be only one
&#96;libfoo.so&#96; in the distribution. The exception is when there are
multiple implementations of the same library &#96;libfoo.so&#96;
provided by different authors and each conflicts with the other. In this
case both &#96;libfoo.so&#96; must provide exactly the same interface,
but with a different implementation. Having two &#96;libfoo.so&#96; each
with a different API is bad practice and makes it harder to package and
distribute those packages.

## Versioned Symbols {#_versioned_symbols}

Without versioned symbols, RPM will generate a dependency expression
naming the library but without a version, effectively setting
\'\$Major.0.0\' as the minimum version. Versioned symbols provide the
information required to ensure that libraries are actually new enough to
run the software that links to them.

Examine the capabilities provided by the binary rpm: &#96;rpm -qp
\--provides &lt;package&gt;&#96;. A package with shared libraries will
list the library as &#96;libc.so.6()(64bit)&#96; and if the library
provides versioned symbols it will also list the library with versions
as &#96;libm.so.6(GLIBC_2.41)(64bit)&#96;.

Package maintainers are encouraged to work with upstream projects to add
versioned symbols to libraries that do not include them yet.

Adding symbol versions is simple for the majority of libraries,
initially requiring only a symbol map and one additional argument to the
linker during the build process.

&#96;&#96;&#96; generate_initial_map.sh: &#35;!/bin/sh echo \'&#35;
Avoid modifying a symbol set after it has been released\' echo \'&#35;
When adding features in a new release, add a new set\' echo \'&#35;
Removing features is a breaking change\' echo \'\$2 {\' echo \'
global:\' objdump -T \$1 \| \\ grep -F .text \| \\ awk \'{print \$7;}\'
\| \\ c++filt \| \\ awk \'/\[() \]/ {print \' \\\'\' \$0 \'\\\';\';} \\
!/\[() \]/ {print \' \' \$0 \';\';}\' \| \\ sort echo \'}\'
&#96;&#96;&#96;

Run &#96;generate_initial_map.sh /path/to/library.so.1
&lt;LIBRARY&gt;\_&lt;VERSION&gt;&#96; to generate a map file.

### Adding version-script to Automake {#_adding_version_script_to_automake}

The GNU Portability Library
[manual](https://www.gnu.org/software/gnulib/manual/html_node/LD-Version-Scripts.html)
includes examples of using version-script in automake. In Makefile.am:

&#96;&#96;&#96; if HAVE_LD_VERSION_SCRIPT libfoo_la_LDFLAGS +=
-Wl,\--version-script=\$(srcdir)/libfoo.map endif &#96;&#96;&#96;

### Adding version-script to CMake {#_adding_version_script_to_cmake}

The BSD-3-Clause licensed
[protobuf](https://github.com/protocolbuffers/protobuf) project includes
examples of using version-script in CMake.

In CMakeLists.txt, check the linker for support:

&#96;&#96;&#96; file(WRITE \${CMAKE_CURRENT_BINARY_DIR}/cmaketest.map
\'{ global: main; local: &#42;; };\') &#35; CheckLinkerFlag module
available in CMake &gt;=3.18. if(\${CMAKE_VERSION} VERSION_GREATER_EQUAL
3.18) include(CheckLinkerFlag) check_linker_flag(CXX
-Wl,\--version-script=\${CMAKE_CURRENT_BINARY_DIR}/cmaketest.map
project_HAVE_LD_VERSION_SCRIPT) endif() file(REMOVE
\${CMAKE_CURRENT_BINARY_DIR}/cmaketest.map) &#96;&#96;&#96;

And, where the library is defined:

&#96;&#96;&#96; if(project_HAVE_LD_VERSION_SCRIPT)
target_link_options(libfoo PRIVATE
-Wl,\--version-script=\${protobuf_source_dir}/src/libfoo.map)
set_target_properties(libfoo PROPERTIES LINK_DEPENDS
\${project_source_dir}/src/libfoo.map) endif() &#96;&#96;&#96;

### Adding version-script to Meson {#_adding_version_script_to_meson}

Meson's [test
cases](https://github.com/mesonbuild/meson/blob/master/test%20cases/linuxlike/3%20linker%20script/meson.build)
include examples of using version-script.

&#96;&#96;&#96; &#35; Solaris 11.4 ld supports \--version-script only
when you also specify &#35; -z gnu-version-script-compat if
meson.get_compiler(\'c\').get_linker_id() == \'ld.solaris\'
add_project_link_arguments(\'-Wl,-z,gnu-version-script-compat\',
language: \'C\') endif

&#35; Static map file mapfile = \'bob.map\' vflag =
\'-Wl,\--version-script,@0@/@1@\'.format(meson.current_source_dir(),
mapfile)

l = shared_library(\'bob\', \'bob.c\', link_args : vflag, link_depends :
mapfile) &#96;&#96;&#96;

## Applications {#_applications}

No additional suggestions are provided for applications at this time.

# D Packaging Guidelines {#_d_packaging_guidelines}

## ldc {#_ldc}

All D packages depend on ldc to build, so every package must have ldc as
BuildRequires. In addition, the ldc package includes some useful macros
for D packages.

### Compiler options {#_compiler_options}

&#96;+%{\_d_optflags}\\&#96; must be used with ldc (normal
\\&#96;%{optflags}+&#96; do not apply to ldc, only to gcc).

&#96;+%{\_d_optflags}+&#96; is defined as:

&#8230;. -release -w -g -O2 &#8230;.

-release *disables asserts, invariants, contracts and boundscheck*\
-w *enables warnings*\
-g *generates debug information*\
-O2 *is the optimisation level*

Some D packages use Makefiles, which usually use the \$DFLAGS variable
in the same way that C packages with Makefiles use \$CFLAGS. In this
case, &#96;+export DFLAGS=\'%{\_d_optflags}\'\\&#96; is usually
appropriate. In other cases, the build script in the D package has an
option to pass in \\&#96;%{\_d_optflags}\\&#96;. It is the
responsibility of the packager to ensure that
\\&#96;%{\_d_optflags}+&#96; are used with ldc when the package is
built.

### Header Files {#_header_files}

D packages contain header files, which end with .d or .di. These header
files must be installed into &#96;+%{\_d_includedir}/%{name}+&#96;.

&#96;+%{\_d_includedir}+&#96; is defined as:

&#8230;. /usr/include/d/ &#8230;.

## Libraries {#_libraries_2}

At this time, Linux does not support shared libraries for D code (only
OSX does). As a result, D packages are explicitly excluded from the
restrictions against packaging static libraries.

To build static libraries in D, you use the same tools that you would
for C, specifically, ar, ranlib, and strip.

If your D package contains static libraries, you must disable debuginfo
generation, by adding this line to the top of your spec file:

&#8230;. %global debug_package %{nil} &#8230;.

Otherwise, it would generate an empty debuginfo package.

All static libraries must be placed in the &#42;-devel subpackage. When
doing this, you must also have &#96;+Provides: %{name}-static =
%{version}-%{release}+&#96; in the devel package definition.

It is possible that this will leave the root package empty, if this is
the case, do not list a %files section for the root package, only for
the -devel package. This is illustrated in the example template below.

## Template {#_template}

&#8230;. %global debug_package %{nil}

Name: foo Version: 1.2.3 Release: 1%{?dist} Summary: Does foo in D
Group: Development/Libraries License: LGPL-2.1-or-later URL:
<https://anywhere.com/> Source:
[https://anywhere.com/%{name}-%{version}.tar.bz2](https://anywhere.com/%{name}-%{version}.tar.bz2)
BuildRequires: ldc Requires: tango

%description Foo and bar.

%package devel Provides: %{name}-static = %{version}-%{release} Summary:
Support for developing D application Group: Development/Libraries

%prep %setup -q

%build export DFLAGS=\'%{\_d_optflags}\' %configure make
%{?\_smp_mflags}

%install mkdir -p %{buildroot}%{\_libdir} mkdir -p
%{buildroot}%{\_d_includedir}/%{name}/

make install DESTDIR=%{buildroot}

install -m 0644 lib/&#42; %{buildroot}%{\_libdir} install -m 0644
include/&#42; %{buildroot}%{\_d_includedir}/%{name}/

%clean rm -rf %{buildroot}

%files devel %doc README.txt %license LICENSE.txt
%{\_d_includedir}/%{name}/ %{\_libdir}/&#42;.a

%changelog &#42; Wed Aug 25 2010 John Doe &lt;<jdoe@anywhere.com>&gt;
1.2.3-1 - initial package &#8230;.

# Fortran Packaging Guidelines {#_fortran_packaging_guidelines}

## Modules and include files {#_modules_and_include_files}

The fortran modules files, ending in .mod are files describing a fortran
90 (and above) module API and ABI. These are not like C header files
describing an API, they are compiler dependent and arch dependent, and
not easily readable by a human being. They are nevertheless searched for
in the includes directories by gfortran (in directories specified with
&#96;+-I+&#96;).

Due to the ABI specificity, the module directory used must be
architecture specific. In addition each gfortran release (e.g. from 4.4
to 4.5) may lead to an incompatible change in the .mod files, therefore
mass rebuilds of Fortran packages must take place when gfortran is
updated.

Fortran can also use include files, similar to C headers. Common used
filename suffixes are \'.inc\' and \'.h\', although \'.fh\' has been
used for files that are designed to function as public headers.

## Packaging of Fortran programs {#_packaging_of_fortran_programs}

Fortran programs in Fedora MUST be compiled, if possible, using the
default Fortran compiler in Fedora, \'gfortran\'. As usual, standard
Fedora optimization flags &#96;+%{optflags}+&#96; MUST be used in the
compilation.

Fortran include files MUST be placed in the standard include directory:
either directly in &#96;+%{\_includedir}\\&#96;, or if headers have
general names or upstream recommends having an own directory, in e.g.
\\&#96;%{\_includedir}/%{name}+&#96;.

As Fortran modules are architecture and GCC version specific, they MUST
be placed into &#96;+%{\_fmoddir}\\&#96; (or its package-specific
subfolder in case the modules have generic names), which is owned by
\'gcc-gfortran\'. For directory ownership any packages containing
Fortran modules MUST \\&#96;+Requires: gcc-gfortran%{\_isa}&#96;.

To use the modules in the Fortran module directory, one needs to add
&#96;+-I%{\_fmoddir}\\&#96; to the compiler flags (this is already
included in \\&#96;+FFLAGS&#96; used by &#96;+%configure+&#96;).

# Golang Packaging Guidelines {#_golang_packaging_guidelines}

This document details best practices for packaging Golang packages.

:::: note
::: title
:::

The [previous version](Golang_old.xml) of these Guidelines involved
creating separate &#96;+-devel+&#96; packages containing the Go source
code for each library dependency. As of
[Changes/GolangPackagesVendoredByDefault](https://fedoraproject.org/wiki/Changes/GolangPackagesVendoredByDefault),
new Go packages MUST be built with vendored dependencies, as outlined in
the current version of the Guidelines.
::::

## go2rpm {#_go2rpm}

[go2rpm](https://gitlab.com/fedora/sigs/go/go2rpm) is a tool that
automates many of these steps. It is advisable to try &#96;+go2rpm
\--name NAME \--profile vendor IMPORT_PATH+&#96; first before attempting
to write a SPEC by hand. go2rpm will generate a Guidelines-compliant
spec file, download the upstream sources, create a vendor archive using
&#96;+go_vendor_archive+&#96; from Go Vendor Tools and then use
&#96;+go_vendor_license+&#96; to scan the upstream sources and vendored
dependencies for license files, prompt the user for any licenses it
could not detect, and then generate a cumulative SPDX expression.

## Import Path {#_import_path}

In Golang, packages are referenced by full URLs listed in the project's
&#96;+go.mod+&#96; file.

``` rpm-spec
%global goipath     github.com/kr/pretty
```

## Naming {#_naming}

New Golang library packages are no longer allowed, so all Golang
packages are user-facing applications that MUST be named according to
the standard [Naming Guidelines](Naming.xml). In particular, vendored Go
packages MUST NOT have a &#96;+golang-+&#96; prefix, unless that is part
of the upstream name of the project.

This also applies to existing packages. When converting a package with a
&#96;+golang-\\&#96; prefix that was created under the old guidelines to
use vendored dependencies, the package MUST go through the
{rename-policy}\[package rename process\]. This guideline seeks to
create a clear separation between packages created under the old
approach and the new vendored method and to avoid cases where
\\&#96;-devel+&#96; subpackages are removed from existing
&#96;+golang-+&#96; packages and then merged back to stable branches.

## Go Language Architectures {#_go_language_architectures}

To compile on various architectures, golang and gcc-go compilers are
available. The golang compiler currently supports x86, x86_64, ppc64le,
ppc64 (partially, see upstream issue&#35;13192), s390x, armv7hl and
aarch64.

Binaries SHOULD set ExclusiveArch so that we only attempt to build
packages on those arches. This is now automatically added by the
&#96;+%gometa+&#96; macro by leveraging the
&#96;+%{golang_arches}\\&#96; macro. Packagers can exclude
\\&#96;%ix86+&#96; (see
[Changes/EncourageI686LeafRemoval](https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval))
by passing &#96;+-f+&#96; to the &#96;+%gometa+&#96; macro. The
&#96;+-f+&#96; flag tells &#96;+%gometa+&#96; to set
&#96;+ExclusiveArch: %{golang_arches_future}\\&#96; instead of
\\&#96;+ExclusiveArch: %{golang_arches}&#96;.
&#96;+%{golang_arches_future}\\&#96; includes the same architectures as
\\&#96;{golang_arches}\\&#96; sans \\&#96;%ix86+&#96;.

## Go compiler flags {#_go_compiler_flags}

### Preserve compiler flags {#_preserve_compiler_flags}

Packages MUST preserve the Fedora golang compiler flags by using the
&#96;+%gobuild+&#96; macro or by passing the appropriate
&#96;+%gobuild\_&#42;flags+&#96; macros to an upstream build script.

``` _rpm-spec
\&#35; Using %gobuild
%gobuild -o %{gobuilddir}/bin/%{name} %{goipath}

\&#35; Using a simple upstream build script
%make_build BUILD_OPTS=%{gobuild_baseflags_shescaped}

\&#35; Using an upstream build script that provides separate options for ldflags
%make_build \
BUILD_OPTS=%{gobuild_baseflags_shescaped} \
GO_LDFLAGS=%{gobuild_ldflags_shescaped}
```

See the inline comments in
[macros.go-compilers-golang](https://gitlab.com/fedora/sigs/go/go-rpm-macros/-/blob/main/rpm/macros.d/macros.go-compilers-golang?ref_type=heads)
for more information on passing the compiler flags to an upstream build
script.

:::: tip
::: title
:::

It is recommended to use the &#96;+%gobuild+&#96; macro if possible.
Some upstream build scripts may not provide a proper way to pass
additional flags to the compiler or have other issues that can be a
source of bugs. When using &#96;+%gobuild+&#96;, make sure to set the
appropriate linker flags and build tags as described below.
::::

### Passing additional flags {#_passing_additional_flags}

Go supports passing additional linker flags (for example, to enable
&#96;+\--version+&#96; functionality) and build tags for conditional
compilation. When using an upstream build script, these may be set
automatically. Otherwise, the packager should set them manually.

:::: important
::: title
:::

Make sure to consult the upstream build process and documentation to
determine what linker flags you may need to include to properly encode
the version into the binary for projects that provide a flag like
&#96;+\--version+&#96; or what build tags to select to enable additional
optional features.
::::

#### Linker flags {#_linker_flags}

In some cases, it may be necessary to pass additional flags to the Go
linker. This can be accomplished by setting the &#96;+\$GO_LDFLAGS+&#96;
environment variable which will then be read by the macros.

``` _rpm-spec
\&#35; The correct value to pass to -X differs between projects; this is an example.
export GO_LDFLAGS='-X %{goipath}/internal.Version=%{version}'
```

Packages MUST NOT set Go linker flags using the &#96;+\$LDFLAGS+&#96;
environment variable. This is supported for backwards compatibility, but
it is deprecated.

#### Build tags {#_build_tags}

Go supports build tags to conditionally include or exclude code from the
build. To pass build tags to the Go compiler, set
&#96;+\$GO_BUILDTAGS+&#96; to a space-separated list of tags.

``` _rpm-spec
\&#35; These tags are just examples. Each project has its own.
export GO_BUILDTAGS='systemd selinux'
```

Packages MUST NOT set Go tags using the &#96;+\$BUILDTAGS+&#96;
environment variable.

## Macro dependencies {#_macro_dependencies}

Packages MUST have &#96;+BuildRequires: go-rpm-macros+&#96; to pull in
the Go macros and compiler.

This is automated by the &#96;+%gometa+&#96; macro.

Packages that use the &#96;+%go_vendor_license\_&#42;+&#96; macros MUST
have &#96;+BuildRequires: go-vendor-tools+&#96;.

## Vendored dependencies {#_vendored_dependencies}

Packages MUST vendor their Go module dependencies. Packagers SHOULD use
the &#96;+go_vendor_archive+&#96; command from [Go Vendor
Tools](https://fedora.gitlab.io/sigs/go/go-vendor-tools/) to generate a
reproducible vendor archive. Packages that do not use Go Vendor Tools
must include a script or other standardized, documented procedure to
download sources with &#96;go mod vendor&#96; and reproducibly produce a
tarball. Packagers SHOULD regenerate vendor archives themselves, even if
upstreams include a vendor directory in their upstream sources. This
allows for easier [security updates using Go Vendor
Tools](https://fedora.gitlab.io/sigs/go/go-vendor-tools/scenarios/&#35;security-updates).

Conventionally, &#96;+Source0+&#96; in the specfile is the primary
archive, and &#96;+Source1+&#96; is the vendor archive, and the values
are automatically filled in using the forge macros.

``` _rpm-spec
Source0:        %{gosource}
\&#35; %%archivename is the basename as the archive provided
\&#35; by %%gosource without the extension.
Source1:        %{archivename}-vendor.tar.bz2
\&#35; go-vendor-tools configuration generated by go2rpm
Source2:        go-vendor-tools.toml
```

Then, run &#96;+go_vendor_archive create &lt;PACKAGE_NAME&gt;.spec+&#96;
to create a vendor tarball.

\[&#35;bundled-provides\] === Bundled provides

Packages MUST include &#96;+bundled(golang(IMPORT_PATH)) = VERSION+&#96;
Provides for all vendored Go modules. This is handled automatically by
[a dependency
generator](https://gitlab.com/fedora/sigs/go/go-rpm-macros/-/blob/main/rpm/fileattrs/go_mod_vendor.attr?ref_type=heads).
It runs on any &#96;+modules.txt+&#96; file in a license directory. Mark
the &#96;+vendor/modules.txt+&#96; file with &#96;+%license+&#96; in
&#96;+%files+&#96;, and then the generator will scan the file and create
the &#96;+bundled()\\&#96; Provides. \\&#96;+vendor/modules.txt&#96; is
included in &#96;+go_vendor_license_filelist+&#96; by default (see
&lt;&lt;installing-licenses&gt;&gt;) so most packages will not need to
do this manually.

``` _rpm-spec
\&#35; Only necessary to include explicitly when not using %%go_vendor_license_filelist
%license vendor/modules.txt
```

## Licensing {#_licensing}

Packages must follow the [Fedora Licensing
Guidelines](LicensingGuidelines.xml). For vendored Go packages, this
means that the license files of the main project as well as all of the
vendored Go modules MUST be included in the package and marked with
&#96;+%license+&#96;. Each vendored Go module MUST include a license
file; Go modules that are missing license files MUST NOT be included in
vendored archives until the licensing is clarified.

Additionally, the package's &#96;+License:+&#96; tag MUST include a
cumulative SPDX expression encompassing both the main package and the
vendored Go modules.

\[&#35;go-vendor-tools-licensing\] == Licensing with Go Vendor Tools

[Go Vendor Tools](https://fedora.gitlab.io/sigs/go/go-vendor-tools/)
provides the &#96;+go_vendor_license+&#96; command and macros to help
determine the correct &#96;+License:+&#96; expression and install
license files as mandated by the previous section.

Packagers MUST run &#96;+go_vendor_license report+&#96; (either
directly, through go2rpm, or using the
[%go_vendor_license_check](https://fedora.gitlab.io/sigs/go/go-vendor-tools/man/rpm_macros/&#35;go_vendor_license_check)
macro in a *local* mock build) and double check its output before
uploading sources to the lookaside cache. Any errors MUST be addressed.
If any part of the output is wrong, &#96;+go_vendor_license+&#96; \'s
behavior can be modified in [the licensing section of the Go Vendor
Tools config
file](https://fedora.gitlab.io/sigs/go/go-vendor-tools/config/&#35;licensing).

This document only outlines the standard usage of Go Vendor Tools needed
to comply with the Guidelines --- consult the [Go Vendor Tools
documentation](https://fedora.gitlab.io/sigs/go/go-vendor-tools/) for
details on advanced usage. Packagers can follow the scenarios
documentation to [generate a new specfile with
go2rpm](https://fedora.gitlab.io/sigs/go/go-vendor-tools/scenarios/&#35;generate-go2rpm)
or [update existing specfiles for new upstream
versions](https://fedora.gitlab.io/sigs/go/go-vendor-tools/scenarios/&#35;manual-update)
to run &#96;+go_vendor_license+&#96; and make sure that the License is
valid and automatically update it if necessary before running a full
build.

:::: warning
::: title
:::

While Go Vendor tools provide facilities to scan for licenses and
generate SPDX expressions, it is still the packager's responsibility to
perform a basic check of the output and ensure adherence to the Fedora
Licensing Guidelines, including ensuring that all keys in the License
tag are allowed licenses in Fedora, before uploading any sources to the
lookaside cache.

If necessary, the license expression for individual files can be
overridden in the config file, [as outlined in the scenarios
documentation](https://fedora.gitlab.io/sigs/go/go-vendor-tools/scenarios/&#35;manually-detecting-licenses).
::::

### go-vendor-tools.toml {#_go_vendor_tools_toml}

Packages MUST include a &#96;+go-vendor-tools.toml+&#96; file to specify
the license detector backend and other configuration options. See the
[configuration
reference](https://fedora.gitlab.io/sigs/go/go-vendor-tools/config/) for
more information. The recommended approach is to use &#96;+go2rpm+&#96;
that automatically creates a valid &#96;+go-vendor-tools.toml+&#96;. A
minimal configuration looks like this:

``` toml
[licensing]
detector = 'askalono'
```

This file is used by the macros and is conventionally included in the
specfile as &#96;+Source2:+&#96;, just below the upstream archive and
the &#96;+go_vendor_archive+&#96;-generated tarball. In this document,
&#96;+%{S:2}\\&#96; (expands to the path to \\&#96;+Source2&#96;) will
be used to represent the path to the Go Vendor Tools config file.

### Installing go-vendor-tools {#_installing_go_vendor_tools}

Packages that use the Go Vendor Tools macros MUST have
&#96;+BuildRequires: go-vendor-tools+&#96; and use the
[%go_vendor_license_buildrequires](https://fedora.gitlab.io/sigs/go/go-vendor-tools/man/rpm_macros/&#35;go_vendor_license_buildrequires)
macro to generate requirements needed for the selected license detector
backend.

``` rpm-spec
BuildRequires:  go-vendor-tools
```

``` rpm-spec
%generate_buildrequires
%go_vendor_license_buildrequires -c %{S:2}
```

\[&#35;installing-licenses\] === Installing licenses

Packagers SHOULD use the
[%go_vendor_license_install](https://fedora.gitlab.io/sigs/go/go-vendor-tools/man/rpm_macros/&#35;go_vendor_license_install)
macro to install license files of the main project and all vendored Go
modules. By default, this macro will install the license files into main
package's license directory. The macro also copies the
&#96;+vendor/modules.txt+&#96; file to the license directory to enable
the Golang &#96;+bundled()+&#96; generator (see
&lt;&lt;bundled-provides&gt;&gt;).

``` rpm-spec
\&#35; Install into the main package's license directory
%go_vendor_license_install -c %{S:2}
```

Then, the macro will populate
[%{go_vendor_license_filelist}](https://fedora.gitlab.io/sigs/go/go-vendor-tools/man/rpm_macros/&#35;go_vendor_license_filelist)
with a list of files that can be passed to &#96;+%files -f+&#96;.

``` rpm-spec
%files -f %{go_vendor_license_filelist}
```

### Checking licenses {#_checking_licenses}

As stated, packagers MUST check licenses using Go Vendor Tools before
uploading sources to the lookaside cache. Any errors raised by
&#96;+go_vendor_license+&#96; MUST be addressed.

As an additional measure, the [%go_vendor_license_check
macro](https://fedora.gitlab.io/sigs/go/go-vendor-tools/man/rpm_macros/&#35;go_vendor_license_check)
runs the same license scan as the &#96;+go_vendor_license report+&#96;
command. Packages SHOULD use &#96;+go_vendor_license_check+&#96; in
&#96;+%check+&#96; so the package build will fail if there are any
license errors. Go Vendor Tools scans the upstream sources and vendored
libraries for license files and generates a cumulative SPDX expression.
Also, the macro checks that the expression in the package's License tag
is equivalent (regardless of order or possible expression
simplification) to what &#96;+go_vendor_license report+&#96; expects.

``` rpm-spec
\&#35; Scan licenses and verify that the License tag is equivalent to what
\&#35; go_vendor_license calculates.
%go_vendor_license_check -c %{S:2}

\&#35; The macro can also compare a license expression stored in a macro with
\&#35; go_vendor_license's output.
%go_vendor_license_check -c %{S:2} %{go_licenses}
```

### In case of missing licenses {#_in_case_of_missing_licenses}

&#96;+go_vendor_license+&#96; checks if any Go module is missing a
license file. Again, Go modules that are missing license files MUST NOT
be included in vendored archives until the situation is fixed upstream.

In some cases, &#96;+go mod vendor+&#96; may fail to download a
project's license file, even if it exists for the equivalent version in
the upstream repository. This is usually because the license files have
non-standard names or because the licenses are installed in a
subdirectory instead of the root of the module. In the former case,
&#96;+go_vendor_archive+&#96; MAY be configured using
[post_commands](https://fedora.gitlab.io/sigs/go/go-vendor-tools/config/&#35;archive&amp;&#35;x2D;&amp;&#35;x2D;post_commands)
to download the license file from the upstream repository as a temporary
measure, but packagers MUST report this to upstream and ask it to rename
the license file to [a format supported by &#96;+go mod
vendor+&#96;](https://github.com/golang/go/blob/ac94297758f3d83fca5ffa16cd179bb098bbd914/src/cmd/go/internal/modcmd/vendor.go&#35;L398-L415).
If the license file is included in a subdirectory of a module, the file
should be copied to the root directory to satisfy the Go Vendor Tools
license checker.

## Testing {#_testing}

You SHOULD run unit tests.

Some tests may be disabled, especially the following kinds of unit tests
are incompatible with a secure build environment such as mock:

&#42; tests that call a remote server or API over the Internet, &#42;
tests that attempt to reconfigure the system, &#42; tests that rely on a
specific app running on the system, like a database or syslog server.

If a test is broken for some other reason, you can disable it the same
way. However, you SHOULD also report the problem upstream. Remember to
trace in a comment why each check was disabled, with links to eventual
upstream problem reports.

Tests can be run using [the %gocheck2
macro](https://fedora.gitlab.io/sigs/go/go-vendor-tools/man/rpm_macros/&#35;gocheck2)
which calls &#96;+go test+&#96; internally while preserving the Fedora
build flags and providing additional options to skip certain tests.

Packages MUST NOT use the deprecated legacy &#96;+%gocheck+&#96; macro.

## Go modules mode {#_go_modules_mode}

Packages SHOULD enable Go modules mode by including &#96;+%global
gomodulesmode GO111MODULE=on+&#96; in the specfile to set the
&#96;+GO111MODULE+&#96; environment variable. Customarily, this
definition is included at the beginning of &#96;+%build+&#96; before the
&#96;+%gobuild+&#96; invocation.

:::: note
::: title
:::

[Go modules](https://go.dev/ref/mod) are the system &#96;+go+&#96; uses
to manage dependencies. Go modules mode replaces &#96;+\$GOPATH+&#96;
mode (the previous dependency management system). Go can be configured
to use modules or &#96;+\$GOPATH+&#96; mode by setting the
[\$GO111MODULE environment
variable](https://go.dev/ref/mod&#35;mod-commands) to &#96;+on+&#96;,
&#96;+off+&#96;, or &#96;+auto+&#96;. &#96;+auto+&#96; is the upstream
default. By default, &#96;+%gobuild+&#96; in Fedora sets
&#96;+GO111MODULE=off+&#96; for compatibility with the legacy Golang
Packaging Guidelines but this approach is not recommended for new
packages built with vendored dependencies. Modules mode should be used
so &#96;+%gobuild+&#96; will read modules metadata and include metadata
about package dependencies in the binary and to make sure [Go
embed](https://pkg.go.dev/embed) works properly.
::::

## Macros {#_macros_2}

The RPM macros provided by &#96;+go-vendor-tools+&#96; are used to
validate and install licenses. See [Go Vendor Tools RPM Macros
docs](https://fedora.gitlab.io/sigs/go/go-vendor-tools/man/rpm_macros/)
and &lt;&lt;go-vendor-tools-licensing&gt;&gt;.

&#96;+go-rpm-macros+&#96; is primarily responsible for the
&#96;+%gobuild+&#96; macro that calls &#96;+go build+&#96; with Fedora's
build flags.

&#96;+go-rpm-macros+&#96; also provides wrappers around the [Forge
macros](SourceURL.xml) from the
[forge-srpm-macros](https://git.sr.ht/~gotmax23/forge-srpm-macros/)
package that makes it easier to specify the Source URL and unpack
sources for Go projects hosted on common software forges like Github.
These macros include &#96;%gometa&#96;, &#96;%gosource&#96;, and
&#96;%goprep&#96;. Packagers can use these macros instead of specifying
sources and calling &#96;+%autosetup+&#96; / &#96;+%setup+&#96;
manually. See [the standalone
docs](https://gitlab.com/fedora/sigs/go/go-rpm-macros/-/blob/main/doc/forge-wrappers.adoc?ref_type=heads)
and example specfile in these guidelines for more information.

## Example {#_example_3}

### go-vendor-tools configuration {#_go_vendor_tools_configuration}

These entries were generated automatically by go2rpm. All Go packages
MUST have a go-vendor-tools.toml file committed to distgit alongside the
specfile.

:::: formalpara
::: title
go-vendor-tools.toml
:::

``` toml
[archive]

[licensing]
detector = 'askalono'

[[licensing.licenses]]
path = 'vendor/github.com/google/shlex/COPYING'
sha256sum = 'cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30'
expression = 'Apache-2.0'

[[licensing.licenses]]
path = 'vendor/github.com/jwalton/gchalk/LICENSE-chalk'
sha256sum = '44e453533edb9f1c037cb260c58f66f1d9b2e7823a07407cd6d04320e3925fea'
expression = 'MIT'

[[licensing.licenses]]
path = 'vendor/github.com/jwalton/gchalk/pkg/ansistyles/LICENSE-ansi-styles'
sha256sum = '310f4b4de77142b34acc5a58de93558fde5dea75891c7822b4086f71372ec983'
expression = 'MIT'

[[licensing.licenses]]
path = 'vendor/github.com/jwalton/go-supportscolor/LICENSE'
sha256sum = '892282511d65ac08025fbabcd8af330d0aa94e459d81a818251ff5a934383816'
expression = 'MIT'

[[licensing.licenses]]
path = 'vendor/gopkg.in/yaml.v3/LICENSE'
sha256sum = 'd18f6323b71b0b768bb5e9616e36da390fbd39369a81807cca352de4e4e6aa0b'
expression = 'MIT AND (MIT AND Apache-2.0)'
```
::::

### Specfile with forge macro wrappers {#_specfile_with_forge_macro_wrappers}

This is the default method used by go2rpm and is the current convention
for Go packages.

:::: formalpara
::: title
ov.spec
:::

``` rpm-spec
\&#35; Generated by go2rpm 1.17.1 (with extra code comments added manually)
%bcond check 1

\&#35; https://github.com/noborus/ov
%global goipath         github.com/noborus/ov
Version:                0.43.0

%gometa -L -f

Name:           ov
Release:        %autorelease
Summary:        Feature-rich terminal-based text viewer

\&#35; Generated by go-vendor-tools
License:        Apache-2.0 AND BSD-3-Clause AND MIT AND MPL-2.0
URL:            %{gourl}
Source0:        %{gosource}
\&#35; Generated by go-vendor-tools
Source1:        %{archivename}-vendor.tar.bz2
\&#35; Go Vendor Tools configuration generated by go2rpm
Source2:        go-vendor-tools.toml

BuildRequires:  go-vendor-tools

%description
Feature-rich terminal-based text viewer. It is a so-called terminal pager.

%prep
\&#35; Unpack upstream sources (Source0) and apply patches if they exist.
\&#35; This also creates the %%{gobuilddir} directory used to store the binary built
\&#35; during %%build.
%goprep -p1
\&#35; Unpack the vendor archive in Source1.
tar -xf %{S:1}

%generate_buildrequires
\&#35; Install license scanner dependencies.
%go_vendor_license_buildrequires -c %{S:2}

%build
\&#35; Enable Go modules mode as required by the Guidelines.
%global gomodulesmode GO111MODULE=on
\&#35; Set version in binary. The exact value to pass to -X differs by project.
export GO_LDFLAGS='-X main.Version=%{version}'
\&#35; Build the binary
%gobuild -o %{gobuilddir}/bin/ov %{goipath}
\&#35; Generate shell completions
%{gobuilddir}/bin/%{name} --completion bash \&gt; %{name}.bash
%{gobuilddir}/bin/%{name} --completion fish \&gt; %{name}.fish
%{gobuilddir}/bin/%{name} --completion zsh  \&gt; %{name}.zsh

%install
\&#35; Install license files
%go_vendor_license_install -c %{S:2}

\&#35; Install binaries built during %%build
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/\&#42; %{buildroot}%{_bindir}/

\&#35; Install shell completions generated during %%build
install -Dpm 0644 ov.bash %{buildroot}%{bash_completions_dir}/ov
install -Dpm 0644 ov.fish %{buildroot}%{fish_completions_dir}/ov.fish
install -Dpm 0644 ov.zsh  %{buildroot}%{zsh_completions_dir}/_ov

%check
\&#35; Perform license check
%go_vendor_license_check -c %{S:2}
\&#35; Run Go unit tests
%if %{with check}
%gocheck2
%endif

%files -f %{go_vendor_license_filelist}
%doc README.md
%{_bindir}/ov
%{bash_completions_dir}/ov
%{fish_completions_dir}/ov.fish
%{zsh_completions_dir}/_ov

%changelog
%autochangelog
```
::::

### Specfile with manual defintions {#_specfile_with_manual_defintions}

This above approach is used by default in go2rpm but Go packages can
also be built without the forge macros. Be sure to include the manual
dependency on &#96;+go-rpm-macros+&#96; and the appropriate
ExclusiveArch invocation.

:::: formalpara
::: title
ov.spec
:::

``` rpm-spec
%bcond check 1

Name:           ov
Version:        0.43.0
Release:        %autorelease
Summary:        Feature-rich terminal-based text viewer
\&#35; Generated by go-vendor-tools
License:        Apache-2.0 AND BSD-3-Clause AND MIT AND MPL-2.0
URL:            https://github.com/noborus/ov
Source0:        %{url}/archive/v%{version}/ov-%{version}.tar.gz
\&#35; Generated by go-vendor-tools
Source1:        ov-%{version}-vendor.tar.bz2
Source2:        go-vendor-tools.toml

ExclusiveArch:  %{golang_arches_future}
BuildRequires:  go-rpm-macros
BuildRequires:  go-vendor-tools

%description
Feature-rich terminal-based text viewer. It is a so-called terminal pager.

%prep
\&#35; Unpack upstream sources (Source0) and apply patches if they exist.
%autosetup -p1
\&#35; Unpack the vendor archive in Source1.
tar -xf %{S:1}

%generate_buildrequires
\&#35; Install license scanner dependencies.
%go_vendor_license_buildrequires -c %{S:2}

%build
\&#35; Enable Go modules mode as required by the Guidelines.
%global gomodulesmode GO111MODULE=on
\&#35; Set version in binary. The exact value to pass to -X differs by project.
export GO_LDFLAGS='-X main.Version=%{version}'
\&#35; Build the binary
%gobuild -o ov .
\&#35; Generate shell completions
./ov --completion bash \&gt; ov.bash
./ov --completion fish \&gt; ov.fish
./ov --completion zsh  \&gt; ov.zsh

%install
\&#35; Install license files
%go_vendor_license_install -c %{S:2}

\&#35; Install binaries built during %%build
install -Dp ./ov -t %{buildroot}%{_bindir}

\&#35; Install shell completions generated during %%build
install -Dpm 0644 ov.bash %{buildroot}%{bash_completions_dir}/ov
install -Dpm 0644 ov.fish %{buildroot}%{fish_completions_dir}/ov.fish
install -Dpm 0644 ov.zsh  %{buildroot}%{zsh_completions_dir}/_ov

%check
\&#35; Perform license check
%go_vendor_license_check -c %{S:2}
\&#35; Run Go unit tests
%if %{with check}
%gocheck2
%endif

%files -f %{go_vendor_license_filelist}
%doc README.md
%{_bindir}/ov
%{bash_completions_dir}/ov
%{fish_completions_dir}/ov.fish
%{zsh_completions_dir}/_ov

%changelog
%autochangelog
```
::::

## Additional resources {#_additional_resources}

- [Go Vendor Tools
  documentation](https://fedora.gitlab.io/sigs/go/go-vendor-tools/)

- [Go RPM Macros
  documentation](https://gitlab.com/fedora/sigs/go/go-rpm-macros/-/tree/main/doc?ref_type=heads)

- [go2rpm project on Gitlab](https://gitlab.com/fedora/sigs/go/go2rpm)

# Legacy Golang Packaging Guidelines {#_legacy_golang_packaging_guidelines}

:::: important
::: title
:::

These guidelines were replaced by [a newer version](Golang.xml).

They exist as a historical reference for packages that don't follow the
new guidelines yet.
::::

This document details best practices for packaging Golang packages. Most
of it is automated by an extensive use of macros.

## go2rpm {#_go2rpm_2}

[go2rpm](https://pagure.io/GoSIG/go2rpm/) is tool that automates many of
these steps. It is advisable to try &#96;+go2rpm import_path+&#96; first
before attempting to write a SPEC by hand.

## Import Path {#_import_path_2}

In Golang, packages are referenced by full URLs. Since this URL is
referenced in several places throughout the rpmspec, set the base import
path as a global define at the top of the spec file

``` rpm-spec
%global goipath     github.com/kr/pretty
```

All macros, including package name, source URL, will be computed from
this value.

:::: note
::: title
:::

&#42;Take the time to identify it accurately.&#42; Changing it later
will be inconvenient.

&#42; it may differ from the repository URL; &#42; generally, the
correct value will be the one used by the project in its documentation,
coding examples, and build assertions; &#42; use the gopkg import path
for all code states when a project uses it.

If upstream confused itself after multiple forks and renamings, you will
need to fix references to past names in the Go source files, unit tests
included. Perform this fixing in &#96;+%prep+&#96;.
::::

## Naming {#_naming_2}

### Source packages (src.rpm) {#_source_packages_src_rpm}

&#42; Golang source packages dedicated to providing code MUST be named
after their main import path. This process is automated by the
&#96;+%{goname}+&#96; macro. This macro will remove any capitalization,
\'go\' keywords, and any duplication in the import path.

\+ For example:

\+

&#42;&#42; the import path &#96;+github.com/kr/pretty+&#96; will become
&#96;+golang-github-kr-pretty+&#96; &#42;&#42; the import path
&#96;+github.com/DATA-DOG/go-txdb+&#96; will become
&#96;+golang-github-data-dog-txdb+&#96; &#42;&#42; the import path
&#96;+github.com/gopherjs/gopherjs+&#96; will become
&#96;+golang-github-gopherjs+&#96;

\+ The filename of spec MUST match the name of the package.

\+ If you're not sure what will the name processed by the
&#96;+%{goname}+&#96; macro be, simply build the SRPM with:

fedpkg \--release f31 srpm

\+ The SRPM filename will be the one to use in your rpmspec and spec
filename.

&#42; Source packages that provide a well-known application such as
&#96;+etcd+&#96; MUST be named after the application. End users do not
care about the language their applications are written in. But do not
name packages after an obscure utility binary that happens to be built
by the package.

#### Implementation: &#96;+%{gorpmname}+&#96; {#_implementation_96gorpmname96}

&#96;+%gometa+&#96; uses the &#96;+%{gorpmname}\\&#96; macro to compute
the main \\&#96;%{goname}\\&#96; from \\&#96;%{goipath}+&#96;.

:::: note
::: title
:::

&#42;&#96;+%{gorpmname}+&#96; can produce collisions&#42;

&#96;+%{gorpmname}+&#96; tries to compute human-friendly and
rpm-compatible naming from Go import paths. It simplifies them, removing
redundancies and common qualifiers. As a result it is possible for two
different import paths to produce the same result. In that case, feel
free to adjust this result manually to avoid the collision.
::::

### Go code packages: &#96;+%{goname}-devel+&#96; {#_go_code_packages_96goname_devel96}

#### In a source package dedicated to providing Go code {#_in_a_source_package_dedicated_to_providing_go_code}

Packages that ship Go code in &#96;+%{goipath}\\&#96; should be named
\\&#96;%{goname}-devel+&#96;. If your source package is already named
&#96;+%{goname}+&#96; then:

``` rpm-spec
%package devel
[…]
%description devel
[…]
%files devel -f devel.file-list
```

This has been automated by the &#96;+%{gopkg}\\&#96; and
\\&#96;%{gopdevelkg}+&#96; macros described in the &lt;&lt;Package
metadata&gt;&gt; section below.

#### In a another kind of source package {#_in_a_another_kind_of_source_package}

If your source package is named something other than
&#96;+%{goname}+&#96;, you SHOULD use:

``` rpm-spec
%package -n %{goname}-devel
[…]
%description -n %{goname}-devel
[…]
%files -n %{goname}-devel -f devel.file-list
```

#### Separate code packages {#_separate_code_packages}

And, finally, if you wish to split the project Go code in multiple
packages, you can compute the corresponding names with:

``` rpm-spec
%global goname1 %gorpmname importpath1
[…]
%package -n %{goname1}-devel
[…]
%description -n %{goname1}-devel
[…]
%files -n %{goname1}-devel -f %{goname1}.file-list
```

See also the [Dealing with cyclic
dependencies](Golang_advanced.adoc&#35;_dealing_with_cyclic_dependencies)
chapter.

Do remember that for Go, each directory is a package. Never separate the
.go files contained in a single directory in different packages.

#### Import path compatibility packages: &#96;+%{compat-%{oldgoname}-devel}+&#96; {#_import_path_compatibility_packages_96compat_oldgoname_devel96}

When a project can be referenced under multiple import paths, due to
forks, renamings, rehostings, organizational changes, or confusing
project documentation, it is possible to generate compatibility
sub-packages to connect code that uses one of the other import paths to
the canonical one.

The canonical import path SHOULD always be the one referenced in the
project documentation. However some projects do not document import path
changes, and rely on HTTPS redirections (for example
<https://github.com/docker/docker> → <https://github.com/moby/moby>).
Such a redirection is a sufficient indicator the canonical import path
has changed (but please make sure with upstream).

The new import path SHOULD be reflected in &#96;+%{goipath}\\&#96; and
compatibility import paths MUST be declared with the
\\&#96;+goaltipaths&#96; macro:

``` rpm-spec
\&#35; A space-separated list of import paths to simulate.
%global goaltipaths
```

For example, the Go library &#96;+github.com/Sirupsen/logrus+&#96; was
renamed &#96;+github.com/sirupsen/logrus+&#96; and the documentation
reflects this new import path. The packager SHOULD thus request a
renaming of his package with a new import path and a compatibility
import path:

``` rpm-spec
%global goipath     github.com/sirupsen/logrus
%global goaltipaths github.com/Sirupsen/logrus
```

If a project has gone through multiple rename, multiple compatibility
import paths can be specified as well.

:::: note
::: title
:::

&#42;Never defer renamings&#42;

Packagers MUST NOT use import path compatibility sub-packages to alias
the canonical import path to one of the previous namings. Packagers MUST
apply upstream renaming choices to the main &#96;+%{goipath}\\&#96; spec
variable and everything that derives from it, such as
\\&#96;%{goname}+&#96;. Deferred renamings introduce friction with
upstream and other packagers.
::::

### Go binary packages {#_go_binary_packages}

The binaries produced by your rpmspec SHOULD generally be listed in the
main package. However, if you want a more appropriate name or split
binaries among different packages, you can create additional binary
subpackage. Of course these package MUST NOT be noarch.

For example we can create the package bbolt that will contain the binary
of the same name:

``` rpm-spec
%package -n bbolt
[…]
%description -n bbolt
[…]
%files -n bbolt
%license LICENSE
%{_bindir}/bbolt
```

## Versioning {#_versioning}

Many Go libraries do not use package versions or have regular releases
and are instead maintained in public version control. In this case,
follow the standard Fedora version conventions. This means that often Go
packages will have a version number of &#96;+0+&#96; and a release
number like &#96;+0.10.20190319git27435c6+&#96;.

Most of this process is automated by macros so that you don't have to
specify the release number yourself.

You first specify either a Version, tag or commit in the header.

``` rpm-spec
Version:
%global tag
%global commit
```

Then use the &#96;+%gometa+&#96; macro:

%gometa

The &#96;+%gometa+&#96; macro will automatically process the
&#96;+%{?dist}\\&#96; tag of the \\&#96;+Release&#96; field to take into
account the commit if any.

:::: note
::: title
:::

&#42;Commits vs releases&#42;

You SHOULD package releases in priority. Please reward the projects that
make an effort to identify stable code states. Only fall back to commits
when the project does not release, when the release is more than six
months old, or if you absolutely need one of the changes of a later
commit. In the later cases please inform the project politely of the
reason you needed to give up on their official releases. Promoting
releases is a way to limit incompatible commit hell.
::::

## Go Language Architectures {#_go_language_architectures_2}

To compile on various architectures, golang and gcc-go compilers are
available. The golang compiler currently supports x86, x86_64, ppc64le,
ppc64 (partially, see upstream issue&#35;13192), s390x, armv7hl and
aarch64.

Binaries SHOULD set ExclusiveArch so that we only attempt to build
packages on those arches. This is now automatically added by the
&#96;+%gometa+&#96; macro by leveraging the
&#96;+%{golang_arches}\\&#96; macro. Packagers can exclude
\\&#96;%ix86+&#96; (see
[Changes/EncourageI686LeafRemoval](https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval))
by passing &#96;+-f+&#96; to the &#96;+%gometa+&#96; macro. The
&#96;+-f+&#96; flag tells &#96;+%gometa+&#96; to set
&#96;+ExclusiveArch: %{golang_arches_future}\\&#96; instead of
\\&#96;+ExclusiveArch: %{golang_arches}&#96;.
&#96;+%{golang_arches_future}\\&#96; includes the same architectures as
\\&#96;{golang_arches}\\&#96; sans \\&#96;%ix86+&#96;.

## Dependencies {#_dependencies}

Packages MUST have &#96;+BuildRequires: go-rpm-macros+&#96;.

This is automated by the &#96;+%gometa+&#96; macro.

### Automatic Dependency Generation {#_automatic_dependency_generation}

Most of the &#96;+golang-&#42;+&#96; packages are source code only. The
&#96;+&#42;-devel+&#96; sub-package that includes the source code should
explicitly have provides for the golang imports that it includes. These
provides are automatically deduced from import paths.

Binary builds that include these imports will use them in BuildRequires,
for example:

``` rpm-spec
BuildRequires: golang(github.com/gorilla/context)
```

### Bundled or unbundled {#_bundled_or_unbundled}

At the moment golang projects packaged in Fedora SHOULD be unbundled by
default. It means projects are built from dependencies packaged in
Fedora.

For some project it can be reasonable to build from bundled
dependencies. Every bundling needs a proper justification.

### BuildRequires {#_buildrequires}

The BuildRequires of the project contains the dependencies needed by
unit tests and binaries.

You can gather them manually with &#96;golist&#96;. For
example:[]{#manual_br}

``` bash
export GOPATH=/home/user/go
export GO111MODULE=off
export goipath='github.com/sirupsen/logrus'
go get $goipath
(sort -u | xargs -I{} echo 'BuildRequires:  golang({})') \&lt;\&lt;\&lt; '$(
golist --imported --package-path $goipath --skip-self
golist --imported --package-path $goipath --skip-self --tests
)'
```

outputs:

    BuildRequires:  golang(github.com/stretchr/testify/assert)
    BuildRequires:  golang(github.com/stretchr/testify/require)
    BuildRequires:  golang(golang.org/x/crypto/ssh/terminal)

If automatic buildrequires are available on your build target, you can
use the &#96;+%go_generate_buildrequires+&#96; macro in
&#96;+%generate_buildrequires+&#96;:

``` rpm-spec
%generate_buildrequires
%go_generate_buildrequires
```

This macro leverages &#96;+golist+&#96; to gather build dependencies and
tests dependencies from the package source.

## Testing {#_testing_2}

You MUST run unit tests. Due to the nature of Go development, especially
the lack of use of semantic versioning, API breakages are frequent.These
need to be detected early and dealt with upstream.

Some tests may be disabled, especially the following kinds of unit tests
are incompatible with a secure build environment such as mock:

&#42; tests that call a remote server or API over the Internet, &#42;
tests that attempt to reconfigure the system, &#42; tests that rely on a
specific app running on the system, like a database or syslog server.

If a test is broken for some other reason, you can disable it the same
way. However, you SHOULD also report the problem upstream. Remember to
trace in a comment why each check was disabled, with links to eventual
upstream problem reports.

## Walkthrough {#_walkthrough}

This chapter will present a typical Go spec file step by step, with
comments and explanations.

### Spec preamble: &#96;+%{goipath}\\&#96;, \\&#96;%{forgeurl}\\&#96; and \\&#96;%gometa+&#96; {#_spec_preamble_96goipath96_96forgeurl96_and_96gometa96}

#### Usual case {#_usual_case}

A Go package is identified by its import path. A Go spec file will
therefore start with the &#96;+%{goipath}+&#96; declaration. Don't get
it wrong, it will control the behaviour of the rest of the spec file.

%global goipath google.golang.org/api

If your package is hosted on a forge like GitHub, GitLab, Bitbucket or
Pagure, the hosting of the Go package will be automatically deduced from
this variable (typically by prefixing it with \\https://). If that is
not the case, you need to declare explicitly the hosting URL with the
&#96;+%{forgeurl}+&#96; macro

%global forgeurl <https://github.com/google/google-api-go-client>

The &#96;+%{forgeurl}\\&#96; declaration is followed by either
\\&#96;+Version&#96;, &#96;+commit+&#96; or &#96;+tag+&#96;. Use the
combination that matches your use-case.

%global commit 2dc3ad4d67ba9a37200c5702d36687a940df1111

:::: note
::: title
:::

You can also define &#96;+date+&#96; to override the mtime of the Source
archive.
::::

Now that we have all the required variables, the &#96;+%gometa+&#96;
macro can be run

%gometa

It will compute and set the following variables if they are not already
set by the packager:

goname

:   an rpm-compatible package name derived from goipath

gosource

:   a URL that can be used as SourceX: value

gourl

:   a URL that can be used as URL: value

It will delegate processing to the &#96;+%forgemeta+&#96; macro for:

forgesource

:   a URL that can be used as SourceX: value

forgesetupargs

:   the correct arguments to pass to &#96;+%setup+&#96; for this source
    used by &#96;+%forgesetup+&#96; and &#96;+%forgeautosetup+&#96;

archivename

:   the source archive filename, without extensions

archiveext

:   the source archive filename extensions, without leading dot

archiveurl

:   the URL that can be used to download the source archive, without
    renaming

topdir

:   the source archive top directory (can be empty)

extractdir

:   the source directory created inside &#96;+%{\_builddir}\\&#96; after
    using \\&#96;%forgesetup+&#96;, &#96;+%forgeautosetup+&#96; or
    &#96;+%{forgesetupargs}+&#96;

repo

:   the repository name

owner

:   the repository owner (if used by another computed variable)

shortcommit

:   the commit hash clamping used by the forge, if any

scm

:   the scm type, when packaging code snapshots: commits or tags

distprefix

:   the prefix that needs adding to dist to trace non-release packaging

Most of the computed variables are both overridable and optional.

Now we can add the remaining elements of the preamble. First, we can
define a multiline description block shared between subpackages:

``` rpm-spec
%global common_description %{expand:
cmux is a generic Go library to multiplex connections based on their payload.
Using cmux, you can serve gRPC, SSH, HTTPS, HTTP, Go RPC, and pretty much any
other protocol on the same TCP listener.}
```

This description MUST stay within 80 characters per line.

:::: note
::: title
:::

If you need specific devel summary and description, you can also define:

- &#96;+%global godevelsummary+&#96;

- &#96;+%global godeveldescription+&#96;
::::

Then we MUST specify the license files that will be added to the devel
subpackages:

&#96;+%global golicenses+&#96;: A space-separated list of shell globs
matching the project license files.

And the possible documentation that SHOULD be included:

&#96;+%global godocs+&#96;: A space-separated list of shell globs
matching the project documentation files. The Go rpm macros will pick up
".md" files by default without this.

:::: note
::: title
:::

You can also exclude files from &#96;+%golicense+&#96; and
&#96;+%godocs+&#96; with:

- &#96;+%global golicensesex+&#96;

- &#96;+%global godocsex+&#96;

For example you might want to exclude &#96;+INSTALL&#42;+&#96; files
from &#96;+%godocs+&#96; as these should not be provided.
::::

### Source package metadata: &#96;+%{goname}\\&#96;, \\&#96;%{gourl}\\&#96; and \\&#96;%{gosource}+&#96; {#_source_package_metadata_96goname96_96gourl96_and_96gosource96}

We can declare the usual rpm headers, using the values computed by
&#96;+%gometa+&#96;:

``` rpm-spec
Name:      %{goname}
\&#35; If not set before
Version:
Release:   1%{?dist}
Summary:
License:
URL:       %{gourl}
Source:    %{gosource}
```

You can replace them with manual definitions. For example, replace
&#96;+%{gourl}\\&#96; with the project homepage if it exists separately
from the repository URL. Be careful to only replace
\\&#96;%{go&#42;}+&#96; variables when it adds value to the specfile and
you understand the consequences. Otherwise you will just add
maintenance-intensive discrepancies in the distribution.

### BuildRequires {#_buildrequires_2}

If they are not automatically generated, you can now add the
dependencies needed for package building and unit testings:

``` rpm-spec
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(golang.org/x/crypto/ssh/terminal)
```

See &lt;&lt;manual_br,this section&gt;&gt; on how to get the
BuildRequires list manually.

### Description {#_description}

Now add the main package description:

``` rpm-spec
%description
%{common_description}
```

### Package metadata {#_package_metadata}

The process of declaring Go code packages has been automated with the
&#96;+%{gopkg}\\&#96; macro. It will automatically generate a
\\&#96;%package+&#96; and &#96;+%description+&#96; for all primary
import paths and compatibility ones.

%gopkg

If you only need to generate Go devel subpackages without compat, use:

%godevelpkg

If necessary, you can then define one or multiple Go packages that will
contain the binaries being built. See the previous &lt;&lt;Go binary
packages&gt;&gt; section.

### %prep: &#96;+%goprep+&#96; , removing vendoring {#_prep_96goprep96_removing_vendoring}

&#96;+%goprep+&#96; unpacks the Go source archives and creates the
project "GOPATH" tree used in the rest of the spec file. It removes
vendored (bundled) code: use the &#96;+-k+&#96; flag if you wish to keep
this vendored code, and deal with the consequences in the rest of the
spec.

%goprep

&#96;+%goprep+&#96; only performs basic vendoring detection. It will
miss inventive ways to vendor code. Remove manually missed vendor code
after the &#96;+%goprep+&#96; line.

&#96;+%goprep+&#96; will not fix upstream sources for you. Since all the
macro calls that follow &#96;+%goprep+&#96; assume clean problem-free
sources, you need to correct them just after the &#96;+%goprep+&#96;
line:

&#42; replace calls to deprecated import paths with their correct value
&#42; patch code problems &#42; remove dead code (some upstreams
deliberately ship broken source code in the hope someone will get around
to fix it)

:::: note
::: title
:::

You SHOULD send fixes and problem reports upstream. Any patch used
SHOULD contain a link to an upstream bug report or merge request. At
minimum, a comment SHOULD be added to explain the patch rationale.
::::

When you package an import path, that participates in a dependency loop,
you need bootstrapping to manage the initial builds:
<https://docs.fedoraproject.org/en-US/packaging-guidelines/&#35;bootstrapping>
For Go code, that means your bootstrap section should:

&#42; remove unit tests that import other parts of the loop &#42; remove
code that imports other parts of the loop

Sometimes one can resolve dependency loops just by splitting specific
subdirectories in a separate -devel subpackage. See also [Dealing with
cyclic
dependencies](Golang_advanced.adoc&#35;_dealing_with_cyclic_dependencies).

### Automatic BuildRequires {#_automatic_buildrequires}

If BuildRequires generator are supported, you can now add them to your
build:

``` rpm-spec
%generate_buildrequires
%go_generate_buildrequires
```

### Packaging a binary: the %build section {#_packaging_a_binary_the_build_section}

If your package is a source package only, you can skip this
&#96;+%build+&#96; section entirely.

Otherwise, you first need to identify manually the project parts that
can be built, and how to name the result. Practically, it's any
directory containing a main() Go section. Nice projects put those in
&#96;+cmd+&#96; subdirectories named after the command that will be
built, which is what we will document here, but it is not a general
rule. Sometimes the whole &#96;+%goipath+&#96; builds as a single
binary.

``` rpm-spec
for cmd in cmd/\&#42; ; do
%gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
```

### Installing the packages {#_installing_the_packages}

#### Source package installation {#_source_package_installation}

If you package a library, &#96;+%gopkginstall+&#96; will perform
installation steps for all primary import paths and compatibility ones.

%gopkginstall

If you only need to install Go devel subpackages without compat, use:

%godevelinstall

#### Binary package installation {#_binary_package_installation}

For binaries, we simply create the &#96;+%{\_bindir}+&#96; directory in
the buildroot and install the commands as executable in it:

``` rpm-spec
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/\&#42; %{buildroot}%{_bindir}/
```

:::: note
::: title
:::

Be wary of command names which might already exist in Fedora. If you
have any doubt, you can check if the command is already provided in
Fedora:

``` shell
dnf whatprovides --disablerepo='\&#42;' --enablerepo=rawhide '/usr/bin/$cmd'
```

If this is the case, use your best judgment to rename the command.
::::

### Running the unit tests: &#96;+%gocheck+&#96; {#_running_the_unit_tests_96gocheck96}

As said before, you MUST run unit tests in &#96;+%check+&#96;:

%gocheck

However it is often necessary to disable some of them. You have 3
exclusion flags to do so:

&#42; &#96;+-d &lt;directory&gt;+&#96;: exclude the files contained in
&#96;+&lt;directory&gt;+&#96; non-recursively (subdirectories are not
excluded) &#42; &#96;+-t &lt;tree root&gt;+&#96;: exclude the files
contained in &#96;+&lt;tree root&gt;+&#96; recursively (subdirectories
are excluded) &#42; &#96;+-r &lt;regexp&gt;+&#96;: exclude files
matching &#96;+&lt;regexp&gt;+&#96;

Remember to document why a test has been disabled.

### %files declaration {#_files_declaration}

#### When shipping source code {#_when_shipping_source_code}

The &#96;+%gopkgfiles+&#96; will process the file list produced in
&#96;+%install+&#96; and add the necessary license and documentation
files:

%gopkgfiles

#### When shipping binaries {#_when_shipping_binaries}

Binaries are usually shipped in the main package. This package MUST
include legal files and documentation associated with those binaries.

``` rpm-spec
%files
%license LICENSE
%doc cmd/foo/README.md
%{_bindir}/\&#42;
```

## Examples {#_examples_5}

### Simple source package {#_simple_source_package}

:::: formalpara
::: title
golang-github-stretchr-testify.spec
:::

``` rpm-spec
```
::::

### Handling package renames {#_handling_package_renames}

:::: formalpara
::: title
golang-github-sirupsen-logrus.spec
:::

``` rpm-spec
```
::::

### Simple binary package {#_simple_binary_package}

:::: formalpara
::: title
golang-github-boltdb-bolt.spec
:::

``` rpm-spec
```
::::

## Additional resources {#_additional_resources_2}

### Advanced uses cases {#_advanced_uses_cases}

&#42;&#42; [Shipping additional
files](Golang_advanced.adoc&#35;_shipping_additional_files) &#42;&#42;
[Additional header
declarations](Golang_advanced.adoc&#35;_additional_header_declarations)
&#42;&#42; [Dealing with cyclic
dependencies](Golang_advanced.adoc&#35;_dealing_with_cyclic_dependencie)

### Additional annotated templates {#_additional_annotated_templates}

&#42;&#42; [Minimal source
package](Golang_templates.adoc&#35;_minimal_source_package) &#42;&#42;
[Full source package](Golang_templates.adoc&#35;_full_source_package)
&#42;&#42; [Minimal alternative import
path](Golang_templates.adoc&#35;_minimal_alternative_import_path)
&#42;&#42; [Full alternative import
path](Golang_templates.adoc&#35;_full_alternative_import_path)
&#42;&#42; [Minimal binary](Golang_templates.adoc&#35;_minimal_binary)
&#42;&#42; [Full binary](Golang_templates.adoc&#35;_full_binary)
&#42;&#42; [Multi package](Golang_templates.adoc&#35;_multi_package)
&#42;&#42; [Manual package
(deprecated)](Golang_templates.adoc&#35;_manual_package_deprecated)

# Advanced uses cases {#_advanced_uses_cases_2}

## Shipping additional files {#_shipping_additional_files}

If you need to ship additional files in your source code packages, you
can use the following macros in the preamble:

&#42; &#96;+%global goextensions+&#96; A space separated list of
extensions that should be included in the devel package in addition to
Go default file extensions. &#42; &#96;+%global gosupfiles+&#96;: A
space-separated list of shell globs matching other files to include in
the devel package. &#42; &#96;+%global gosupfilesex+&#96; A
space-separated list of shell globs matching other files you wish to
exclude from package lists. Only works with "gosupfiles"-specified
files.

For example, if you have glide files to ship:

``` rpm-spec
%global gosupfiles glide.yaml glide.lock
```

## Additional header declarations {#_additional_header_declarations}

Use &#96;+%godevelheader+&#96; to add specific subpackage declarations.
For example, you might want to require the main package containing the
binaries, or Obsoletes/Provides another package in case of renaming.

``` rpm-spec
%global godevelheader %{expand:
Requires:
Obsoletes:
Provides:
}
```

## Dealing with cyclic dependencies {#_dealing_with_cyclic_dependencies}

In many cases, you'll encounter packages that depend on each other, also
known as cyclic dependencies, making it difficult to build either
package.

Typically, when you have a problematic requires, it is only used in
specific project subpackages, and most project dependents do not need
those subpackages directly or indirectly. The idea is then to affect the
goipaths associated with the problematic subpackages to a separate
-devel rpm package, to simplify your dependency graph.

Let's take for example the following packages:
&#96;+cloud.google.com/go+&#96; and &#96;+golang.org/x/oauth2+&#96;.

&#96;+cloud.google.com/go+&#96; has the following dependency graph:

    github.com/golang/mock/gomock
    github.com/golang/protobuf/proto
    github.com/golang/protobuf/ptypes
    github.com/golang/protobuf/ptypes/any
    github.com/golang/protobuf/ptypes/duration
    github.com/golang/protobuf/ptypes/empty
    github.com/golang/protobuf/ptypes/struct
    github.com/golang/protobuf/ptypes/timestamp
    github.com/golang/protobuf/ptypes/wrappers
    github.com/google/btree
    github.com/google/go-cmp/cmp
    github.com/google/martian
    github.com/google/martian/fifo
    github.com/google/martian/httpspec
    github.com/google/martian/martianhttp
    github.com/google/martian/martianlog
    github.com/google/martian/mitm
    github.com/google/pprof/profile
    github.com/googleapis/gax-go/v2
    go.opencensus.io/plugin/ocgrpc
    go.opencensus.io/stats
    go.opencensus.io/stats/view
    go.opencensus.io/tag
    go.opencensus.io/trace
    golang.org/x/build/kubernetes
    golang.org/x/build/kubernetes/api
    golang.org/x/build/kubernetes/gke
    golang.org/x/oauth2
    golang.org/x/oauth2/google
    golang.org/x/oauth2/jwt
    golang.org/x/sync/errgroup
    golang.org/x/sync/semaphore
    golang.org/x/text/language
    golang.org/x/time/rate
    […]

And &#96;+golang.org/x/oauth2+&#96; has the following dependency graph:

    cloud.google.com/go/compute/metadata
    golang.org/x/net/context/ctxhttp

As you can see both packages depend on each other. If we search for
where &#96;+cloud.google.com/go+&#96; is used in
&#96;+golang.org/x/oauth2+&#96;:

``` bash
grep -nr 'cloud.google.com/go/compute/metadata' $GOPATH/src/golang.org/x/oauth2

/home/user/go/src/golang.org/x/oauth2/google/default.go:17:      'cloud.google.com/go/compute/metadata'
/home/user/go/src/golang.org/x/oauth2/google/google.go:15:       'cloud.google.com/go/compute/metadata'
```

We can see that it is used in the &#96;+golang.org/x/oauth2/google+&#96;
subpackage, which is precisely the subpackage needed by
&#96;+cloud.google.com/go+&#96;. It is thus not possible to split
&#96;+golang.org/x/oauth2/google+&#96; into separate devel subpackage to
resolve our cyclic dependency graph.

Now if we search for where &#96;+golang.org/x/oauth2+&#96; is used in
&#96;+cloud.google.com/go+&#96;:

``` bash
grep -nr 'golang.org/x/oauth2/google' $GOPATH/src/cloud.google.com/go

/home/user/go/src/cloud.google.com/go/cmd/go-cloud-debug-agent/debuglet.go:38:   'golang.org/x/oauth2/google'
/home/user/go/src/cloud.google.com/go/internal/testutil/context.go:26:   'golang.org/x/oauth2/google'
/home/user/go/src/cloud.google.com/go/profiler/integration_test.go:30:   'golang.org/x/oauth2/google'
/home/user/go/src/cloud.google.com/go/authexample_test.go:22:    'golang.org/x/oauth2/google'
```

We can see that it is not used in the
&#96;+cloud.google.com/go/compute/metadata+&#96; subpackage. As a result
we can split &#96;+cloud.google.com/go/compute/metadata+&#96; into a
separate devel subpackage to resolve our cyclic dependency graph.

To achieve this, we use multiple &#96;+goipaths+&#96; in the preamble:

``` rpm-spec
%global goipaths0       cloud.google.com/go
%global goipathsex0     cloud.google.com/go/compute

%global goipaths1       cloud.google.com/go/compute
```

&#96;+goipaths0+&#96; will be the main package from which we exclude
&#96;+compute+&#96;, and &#96;+goipaths1+&#96; will be the split package
containing it.

After building, we end up with two packages:

&#42; &#96;+golang-cloud-google-devel-0.36.0-1.fc31.x86_64.rpm+&#96;,
which provides:

\+

    golang(cloud.google.com/go) = 0.36.0-1.fc31
    golang(cloud.google.com/go/asset/apiv1beta1) = 0.36.0-1.fc31
    golang(cloud.google.com/go/asset/v1beta1) = 0.36.0-1.fc31
    golang(cloud.google.com/go/bigquery) = 0.36.0-1.fc31
    golang(cloud.google.com/go/bigquery/datatransfer/apiv1) = 0.36.0-1.fc31
    golang(cloud.google.com/go/bigquery/storage/apiv1beta1) = 0.36.0-1.fc31
    golang(cloud.google.com/go/bigtable) = 0.36.0-1.fc31
    golang(cloud.google.com/go/bigtable/bttest) = 0.36.0-1.fc31
    golang(cloud.google.com/go/bigtable/internal/cbtconfig) = 0.36.0-1.fc31
    golang(cloud.google.com/go/bigtable/internal/gax) = 0.36.0-1.fc31
    golang(cloud.google.com/go/bigtable/internal/option) = 0.36.0-1.fc31
    golang(cloud.google.com/go/bigtable/internal/stat) = 0.36.0-1.fc31
    golang(cloud.google.com/go/civil) = 0.36.0-1.fc31
    golang(cloud.google.com/go/cloudtasks/apiv2beta2) = 0.36.0-1.fc31
    golang(cloud.google.com/go/cloudtasks/apiv2beta3) = 0.36.0-1.fc31
    golang(cloud.google.com/go/cmd/go-cloud-debug-agent/internal/breakpoints) = 0.36.0-1.fc31
    golang(cloud.google.com/go/cmd/go-cloud-debug-agent/internal/controller) = 0.36.0-1.fc31
    golang(cloud.google.com/go/cmd/go-cloud-debug-agent/internal/debug) = 0.36.0-1.fc31
    golang(cloud.google.com/go/cmd/go-cloud-debug-agent/internal/debug/arch) = 0.36.0-1.fc31
    golang(cloud.google.com/go/cmd/go-cloud-debug-agent/internal/debug/dwarf) = 0.36.0-1.fc31
    golang(cloud.google.com/go/cmd/go-cloud-debug-agent/internal/debug/elf) = 0.36.0-1.fc31
    golang(cloud.google.com/go/cmd/go-cloud-debug-agent/internal/debug/gosym) = 0.36.0-1.fc31
    golang(cloud.google.com/go/cmd/go-cloud-debug-agent/internal/debug/local) = 0.36.0-1.fc31
    golang(cloud.google.com/go/cmd/go-cloud-debug-agent/internal/debug/remote) = 0.36.0-1.fc31
    golang(cloud.google.com/go/cmd/go-cloud-debug-agent/internal/debug/server) = 0.36.0-1.fc31
    golang(cloud.google.com/go/cmd/go-cloud-debug-agent/internal/debug/server/protocol) = 0.36.0-1.fc31
    golang(cloud.google.com/go/cmd/go-cloud-debug-agent/internal/debug/tests/peek) = 0.36.0-1.fc31
    golang(cloud.google.com/go/cmd/go-cloud-debug-agent/internal/valuecollector) = 0.36.0-1.fc31
    golang(cloud.google.com/go/container) = 0.36.0-1.fc31
    golang(cloud.google.com/go/container/apiv1) = 0.36.0-1.fc31
    golang(cloud.google.com/go/containeranalysis/apiv1beta1) = 0.36.0-1.fc31
    golang(cloud.google.com/go/dataproc/apiv1) = 0.36.0-1.fc31
    golang(cloud.google.com/go/dataproc/apiv1beta2) = 0.36.0-1.fc31
    golang(cloud.google.com/go/datastore) = 0.36.0-1.fc31
    golang(cloud.google.com/go/debugger/apiv2) = 0.36.0-1.fc31
    golang(cloud.google.com/go/dialogflow/apiv2) = 0.36.0-1.fc31
    golang(cloud.google.com/go/dlp/apiv2) = 0.36.0-1.fc31
    golang(cloud.google.com/go/errorreporting) = 0.36.0-1.fc31
    golang(cloud.google.com/go/errorreporting/apiv1beta1) = 0.36.0-1.fc31
    golang(cloud.google.com/go/expr/apiv1alpha1) = 0.36.0-1.fc31
    golang(cloud.google.com/go/firestore) = 0.36.0-1.fc31
    golang(cloud.google.com/go/firestore/apiv1) = 0.36.0-1.fc31
    golang(cloud.google.com/go/firestore/apiv1beta1) = 0.36.0-1.fc31
    golang(cloud.google.com/go/firestore/genproto) = 0.36.0-1.fc31
    golang(cloud.google.com/go/firestore/internal) = 0.36.0-1.fc31
    golang(cloud.google.com/go/functions/metadata) = 0.36.0-1.fc31
    golang(cloud.google.com/go/httpreplay) = 0.36.0-1.fc31
    golang(cloud.google.com/go/httpreplay/internal/proxy) = 0.36.0-1.fc31
    golang(cloud.google.com/go/iam) = 0.36.0-1.fc31
    golang(cloud.google.com/go/iam/admin/apiv1) = 0.36.0-1.fc31
    golang(cloud.google.com/go/iam/credentials/apiv1) = 0.36.0-1.fc31
    golang(cloud.google.com/go/internal) = 0.36.0-1.fc31
    golang(cloud.google.com/go/internal/btree) = 0.36.0-1.fc31
    golang(cloud.google.com/go/internal/fields) = 0.36.0-1.fc31
    golang(cloud.google.com/go/internal/leakcheck) = 0.36.0-1.fc31
    golang(cloud.google.com/go/internal/optional) = 0.36.0-1.fc31
    golang(cloud.google.com/go/internal/pretty) = 0.36.0-1.fc31
    golang(cloud.google.com/go/internal/protostruct) = 0.36.0-1.fc31
    golang(cloud.google.com/go/internal/testutil) = 0.36.0-1.fc31
    golang(cloud.google.com/go/internal/trace) = 0.36.0-1.fc31
    golang(cloud.google.com/go/internal/tracecontext) = 0.36.0-1.fc31
    golang(cloud.google.com/go/internal/uid) = 0.36.0-1.fc31
    golang(cloud.google.com/go/internal/version) = 0.36.0-1.fc31
    golang(cloud.google.com/go/irm/apiv1alpha2) = 0.36.0-1.fc31
    golang(cloud.google.com/go/kms/apiv1) = 0.36.0-1.fc31
    golang(cloud.google.com/go/language/apiv1) = 0.36.0-1.fc31
    golang(cloud.google.com/go/language/apiv1beta2) = 0.36.0-1.fc31
    golang(cloud.google.com/go/logging) = 0.36.0-1.fc31
    golang(cloud.google.com/go/logging/apiv2) = 0.36.0-1.fc31
    golang(cloud.google.com/go/logging/internal) = 0.36.0-1.fc31
    golang(cloud.google.com/go/logging/internal/testing) = 0.36.0-1.fc31
    golang(cloud.google.com/go/logging/logadmin) = 0.36.0-1.fc31
    golang(cloud.google.com/go/longrunning) = 0.36.0-1.fc31
    golang(cloud.google.com/go/longrunning/autogen) = 0.36.0-1.fc31
    golang(cloud.google.com/go/monitoring/apiv3) = 0.36.0-1.fc31
    golang(cloud.google.com/go/oslogin/apiv1) = 0.36.0-1.fc31
    golang(cloud.google.com/go/oslogin/apiv1beta) = 0.36.0-1.fc31
    golang(cloud.google.com/go/profiler) = 0.36.0-1.fc31
    golang(cloud.google.com/go/profiler/mocks) = 0.36.0-1.fc31
    golang(cloud.google.com/go/profiler/proftest) = 0.36.0-1.fc31
    golang(cloud.google.com/go/pubsub) = 0.36.0-1.fc31
    golang(cloud.google.com/go/pubsub/apiv1) = 0.36.0-1.fc31
    golang(cloud.google.com/go/pubsub/internal/distribution) = 0.36.0-1.fc31
    golang(cloud.google.com/go/pubsub/loadtest) = 0.36.0-1.fc31
    golang(cloud.google.com/go/pubsub/loadtest/pb) = 0.36.0-1.fc31
    golang(cloud.google.com/go/pubsub/pstest) = 0.36.0-1.fc31
    golang(cloud.google.com/go/redis/apiv1) = 0.36.0-1.fc31
    golang(cloud.google.com/go/redis/apiv1beta1) = 0.36.0-1.fc31
    golang(cloud.google.com/go/rpcreplay) = 0.36.0-1.fc31
    golang(cloud.google.com/go/rpcreplay/proto/intstore) = 0.36.0-1.fc31
    golang(cloud.google.com/go/rpcreplay/proto/rpcreplay) = 0.36.0-1.fc31
    golang(cloud.google.com/go/scheduler/apiv1beta1) = 0.36.0-1.fc31
    golang(cloud.google.com/go/securitycenter/apiv1beta1) = 0.36.0-1.fc31
    golang(cloud.google.com/go/spanner) = 0.36.0-1.fc31
    golang(cloud.google.com/go/spanner/admin/database/apiv1) = 0.36.0-1.fc31
    golang(cloud.google.com/go/spanner/admin/instance/apiv1) = 0.36.0-1.fc31
    golang(cloud.google.com/go/spanner/apiv1) = 0.36.0-1.fc31
    golang(cloud.google.com/go/spanner/internal/backoff) = 0.36.0-1.fc31
    golang(cloud.google.com/go/spanner/internal/testutil) = 0.36.0-1.fc31
    golang(cloud.google.com/go/speech/apiv1) = 0.36.0-1.fc31
    golang(cloud.google.com/go/speech/apiv1p1beta1) = 0.36.0-1.fc31
    golang(cloud.google.com/go/storage) = 0.36.0-1.fc31
    golang(cloud.google.com/go/talent/apiv4beta1) = 0.36.0-1.fc31
    golang(cloud.google.com/go/texttospeech/apiv1) = 0.36.0-1.fc31
    golang(cloud.google.com/go/trace) = 0.36.0-1.fc31
    golang(cloud.google.com/go/trace/apiv1) = 0.36.0-1.fc31
    golang(cloud.google.com/go/trace/apiv2) = 0.36.0-1.fc31
    golang(cloud.google.com/go/translate) = 0.36.0-1.fc31
    golang(cloud.google.com/go/translate/internal/translate/v2) = 0.36.0-1.fc31
    golang(cloud.google.com/go/videointelligence/apiv1) = 0.36.0-1.fc31
    golang(cloud.google.com/go/videointelligence/apiv1beta1) = 0.36.0-1.fc31
    golang(cloud.google.com/go/videointelligence/apiv1beta2) = 0.36.0-1.fc31
    golang(cloud.google.com/go/vision/apiv1) = 0.36.0-1.fc31
    golang(cloud.google.com/go/vision/apiv1p1beta1) = 0.36.0-1.fc31
    golang-cloud-google-devel = 0.36.0-1.fc31
    golang-cloud-google-devel(x86-64) = 0.36.0-1.fc31
    golang-ipath(cloud.google.com/go) = 0.36.0-1.fc31

&#42;
&#96;+golang-cloud-google-compute-devel-0.36.0-1.fc31.x86_64.rpm+&#96;,
which provides:

\+

    golang(cloud.google.com/go/compute/metadata) = 0.36.0-1.fc31
    golang-cloud-google-compute-devel = 0.36.0-1.fc31
    golang-cloud-google-compute-devel(x86-64) = 0.36.0-1.fc31
    golang-ipath(cloud.google.com/go/compute) = 0.36.0-1.fc31

We now have broken the cyclic dependency graph:
&#96;+golang.org/x/oauth2+&#96; can now depend separately on
&#96;+golang-cloud-google-compute-devel+&#96;.

Here is the full example:

:::: formalpara
::: title
golang-cloud-google-go.spec
:::

``` rpm-spec
```
::::

# Additional annotated templates {#_additional_annotated_templates_2}

## Minimal source package {#_minimal_source_package}

:::: formalpara
::: title
spectemplate-go-0-source-minimal.spec
:::

``` rpm-spec
```
::::

## Full source package {#_full_source_package}

:::: formalpara
::: title
spectemplate-go-1-source-full.spec
:::

``` rpm-spec
```
::::

## Minimal alternative import path {#_minimal_alternative_import_path}

:::: formalpara
::: title
spectemplate-go-2-alternative-import-path-minimal.spec
:::

``` rpm-spec
```
::::

## Full alternative import path {#_full_alternative_import_path}

:::: formalpara
::: title
spectemplate-go-3-alternative-import-path-full.spec
:::

``` rpm-spec
```
::::

## Minimal binary {#_minimal_binary}

:::: formalpara
::: title
spectemplate-go-4-binary-minimal.spec
:::

``` rpm-spec
```
::::

## Full binary {#_full_binary}

:::: formalpara
::: title
spectemplate-go-5-binary-full.spec
:::

``` rpm-spec
```
::::

## Multi package {#_multi_package}

:::: formalpara
::: title
spectemplate-go-6-multi.spec
:::

``` rpm-spec
```
::::

## Manual package (deprecated) {#_manual_package_deprecated}

:::: formalpara
::: title
spectemplate-go-7-manual.spec
:::

``` rpm-spec
```
::::

# Haskell Packaging Guidelines {#_haskell_packaging_guidelines}

This page documents the guidelines and conventions for packaging Haskell
projects in Fedora.

[GHC](https://haskell.org/ghc) (Glasgow Haskell Compiler) is the current
mainstream Haskell compiler. Most Haskell packages are released on
[Hackage](https://hackage.haskell.org) and use the
[Cabal](https://www.haskell.org/cabal/) package system. So the current
guidelines largely focus on packaging for GHC using Cabal.

## Spec file templates {#_spec_file_templates}

Spec files in line with these templates are generated automatically by
the [cabal-rpm](https://src.fedoraproject.org/rpms/cabal-rpm) packaging
tool which also adds dependencies listed in the package's
&#96;+.cabal+&#96; configuration file. Most packages should then build,
though for some packages it may be necessary to specify some additional
BuildRequires and/or Requires, and to check non-Haskell devel
dependencies.

Standardizing the packaging helps to lower the maintenance burden across
Fedora's Haskell packages.

There are three types of Haskell Cabal packages: library (Lib), binary
only (Bin), and binary with library (BinLib):

### Library Only {#_library_only}

``` RPMspec
```

### Binary Only {#_binary_only}

``` RPMspec
```

### BinLib {#_binlib}

``` RPMspec
```

## Package Naming {#_package_naming}

Haskell Bin packages should follow the usual Fedora Package Naming
Guidelines for base package naming: i.e., follow the upstream name.
Examples include projects like &#96;+alex+&#96; and
&#96;+cabal-install+&#96;.

The names of Haskell Lib packages, packaged for &#96;+ghc+&#96;, are
prefixed by \'ghc-\'. For example the Haskell aeson library package is
named &#96;+ghc-aeson+&#96;, and the Haskell X11 library package is
named &#96;+ghc-X11+&#96;, etc.

Haskell BinLib packages should be named like a Bin package if the most
important part they provide is an executable (eg &#96;+hlint+&#96;,
&#96;+ShellCheck+&#96;, and &#96;+pandoc+&#96;), otherwise they should
be named and packaged as a Lib package (eg &#96;+ghc-hakyll+&#96; (has a
setup executable), &#96;+ghc-vty+&#96; (has demo executables)) if they
are actually a library that includes an helper executable or demo or
minor utility. In this case typically the executable should live in the
devel subpackage (or maybe the library base package if it is used at
runtime).

Note that having different Haskell source packages named \'ghc-xyz\' and
\'xyz\' is not allowed since they would both correspond to the same
upstream package named \'xyz\' on Hackage.

BinLib packages should subpackage their libraries with naming following
Lib packages. For example the &#96;+pandoc+&#96; BinLib package has
library subpackages

&#42; &#96;+ghc-pandoc+&#96; for the shared library, &#42;
&#96;+ghc-pandoc-devel+&#96; for devel files and the static library,
&#42; &#96;+ghc-pandoc-prof+&#96; for the profiling static library,
&#42; &#96;+ghc-pandoc-doc+&#96; for the library's extracted development
documentation.

If a library is packaged for more than one Haskell compiler or
interpreter, the base name should instead be prefixed with
&#96;+haskell+&#96;, e.g. &#96;+haskell-X11+&#96;. Such a package would
then have subpackages for each compiler and/or interpreter it is built
for (e.g. &#96;+ghc-X11+&#96;, hugs98-X11&#96;, etc).

Package naming preserves case to follow the upstream naming conventions
as closely as possible, including package dependencies.

## Headers {#_headers}

The macro &#96;+pkg_name+&#96; is used to carry the name of the upstream
library package (i.e. without the Fedora \'ghc-\' prefix). It should be
defined at the top of Lib and BinLib packages:

&#96;+%global pkg_name+&#96;

## Cabal Flags {#_cabal_flags}

If needed Cabal flags for build options should be set by changing the
package's &#96;+.cabal+&#96; file: this can usually be done with the
&#96;+cabal-tweak-flag+&#96; script to avoid having to carry and
maintain patches for this.

For example &#96;+cabal-tweak-flag systemlib True+&#96; might enable a
flag to use a system library dependency.

&#96;+%cabal_configure_options+&#96; can be set to pass other options to
Cabal.

Modifying the &#96;+.cabal+&#96; file flags defaults allows packagers
and tools like &#96;+cabal-rpm+&#96; to track actual package
dependencies correctly.

## Dependencies {#_dependencies_2}

The &#96;+cabal-tweak-dep-ver+&#96; script can used to change version
bounds of dependencies in the package's .cabal file:
&#96;+cabal-tweak-dep-ver deppkg oldbound newbound+&#96;

eg: &#96;+cabal-tweak-dep-ver base \'&lt; 4.16\' \'&lt; 4.17\'+&#96;

Similarly &#96;+cabal-tweak-drop-dep+&#96; for dropping a redundant
dependency (eg a compatibility dummy package).

eg: &#96;+cabal-tweak-drop-dep mtl-compat+&#96;

Spec file build dependencies are generated by the &#96;+cabal-rpm+&#96;
packaging tool.

Binary RPM dependencies for Haskell libraries are automatically
generated at build-time by the &#96;+ghc-deps.sh+&#96; script.

## Shared and static library linking {#_shared_and_static_library_linking}

GHC uses static libraries for linking by default. Lib and BinLib
packages should provide static, shared, and profiling libraries:

&#42; the shared library lives in the base library package,

&#42; the static library and interface development files in the -devel
subpackage,

&#42; and the profiling library and profiling interface files in the
-prof subpackage.

Since GHC assumes static versions of libraries are installed they need
to be in the devel subpackage and it doesn't make sense to subpackage
them.

Executables in Bin and BinLib packages should be statically linked for
portability.

Due to how GHC links shared libraries using &#96;+\--no-as-needed+&#96;
they generate a lot of rpmlint &#96;+E: undefined-non-weak-symbol+&#96;
errors, this is unfortunately currently expected (see these
[upstream](https://gitlab.haskell.org/ghc/ghc/-/issues/17157)
[issues](https://gitlab.haskell.org/ghc/ghc/-/issues/23216)).

## RPM Macros {#_rpm_macros_2}

The templates all have buildrequires for ghc-rpm-macros, which provides
[macros.ghc](https://src.fedoraproject.org/rpms/ghc-rpm-macros/blob/master/f/macros.ghc)
to assist with packaging Haskell Cabal packages.

&#8230;. BuildRequires: ghc-rpm-macros &#8230;.

The main commonly used macros are:

&#42; &#96;+%ghc_bin_build+&#96; &#42; &#96;+%ghc_lib_build+&#96; &#42;
&#96;+%ghc_bin_install+&#96; &#42; &#96;+%ghc_lib_install+&#96;

They are used in the templates and explained in more detail below.

## Bin packages {#_bin_packages}

Executables are statically linked to Haskell libraries by default.

&#8230;. %build %ghc_bin_build

%install %ghc_bin_install &#8230;.

&#96;+%ghc_bin_build+&#96; is used to configure and build bin packages.
It runs:

&#42; &#96;+%cabal_configure+&#96;: configure the package for building
and dynamic linking.

&#42; &#96;+%cabal build+&#96;: builds the package.

&#96;+%ghc_bin_install+&#96; is used to install bin packages. It runs:

&#42; &#96;+%cabal_install+&#96;: to install the package.

## Lib and BinLib packages {#_lib_and_binlib_packages}

Devel subpackages need to setup some Requires:

&#8230;. %package -n ghc-%{pkg_name}-devel Summary: Haskell %{pkg_name}
library development files Requires: ghc-compiler = %{ghc_version}
Requires: ghc-%{pkg_name} = %{version}-%{release} &#8230;.

Lib packages need to use &#96;+%setup -n+&#96;:

&#8230;. %prep %setup -q -n %{pkg_name}-%{version} &#8230;.

Both Lib and BinLib have:

&#8230;. %build %ghc_lib_build

%install %ghc_lib_install &#8230;.

&#96;+%ghc_lib_build+&#96; is used to configure, build and generate
documentation for Lib and BinLib packages. It runs:

&#42; &#96;+%cabal_configure \--ghc -p+&#96;: configures the package for
building with ghc and profiling. Libraries should build profiling
versions of their static libraries.

&#42; &#96;+%cabal build+&#96;: builds the package.

&#42; &#96;+%cabal haddock+&#96;: generates HTML library documentation
from the source code.

&#42;&#42; If documentation is failing to build for some reason,
&#96;+%ghc_lib_build_without_haddock+&#96; can be used instead of
&#96;+%ghc_lib_build+&#96; to disable haddock generation.

&#96;+%ghc_lib_install+&#96; is used to install Lib and BinLib packages.
It runs:

&#42; &#96;+%cabal_install+&#96;: installs the package without
registering it in ghc-pkg.

&#42; &#96;+%cabal_pkg_conf+&#96;: creates ghc-pkg .conf metadata file
for package installation time

&#42; &#96;+%ghc_gen_filelists+&#96;: generates rpm filelists.

## Debuginfo {#_debuginfo}

Debuginfo is currently disabled for Haskell packages, because ghc's
Dwarf output is not very useful. Stack backtraces can also be generated
using profiling libraries.

## Directories {#_directories}

GHC libraries are installed under
&#96;+%ghclibdir/%{pkg_name}-%{version}+&#96;:

Library documentation lives under
&#96;+%ghclibdocdir/%{pkg_name}-%{version}+&#96;.

## File lists {#_file_lists}

Filelists for shared and devel library subpackages are generated through
&#96;+%ghc_lib_install+&#96; using the macro
&#96;+%ghc_gen_filelists+&#96;.

It generates the filelists &#96;+ghc-%{pkg_name}.files+&#96;,
&#96;+ghc-%{pkg_name}-devel.files+&#96;,
&#96;+ghc-%{pkg_name}-prof.files+&#96;, and
&#96;+ghc-%{pkg_name}-doc.files+&#96;.

## Compiling non-Cabal packages {#_compiling_non_cabal_packages}

Packages compiling Haskell code without Cabal, i.e., directly with
&#96;+ghc+&#96; or &#96;+ghc \--make+&#96;, should use &#96;+-O1+&#96;
optimization, like Cabal does by default.

## References {#_references}

&#42; <https://hackage.haskell.org/package/cabal-rpm> &#42;
<https://src.fedoraproject.org/rpms/ghc-rpm-macros> &#42; [Debian
Haskell Group](https://wiki.debian.org/Haskell) &#42; [Fedora Haskell
SIG](https://fedoraproject.org/wiki/Haskell_SIG)

# Java Packaging Guidelines {#_java_packaging_guidelines}

This page represents Fedora guidelines for packaging libraries and
applications written in Java and related languages that use the Java
Virtual Machine as a bytecode interpreter.

It does not aim to extensively describe packaging techniques and tips.
RPM macros and commands used here are documented in man pages.
Furthermore, a separate [Java Packaging
HOWTO](https://docs.fedoraproject.org/en-US/java-packaging-howto/)
describes Java packaging techniques in detail and includes examples,
templates and documentation aimed at packagers and Java developers who
are taking their first steps in Java RPM packaging.

Fedora Java packaging is originally based on the [JPackage
Project](https://web.archive.org/web/20191223234327/http://www.jpackage.org/)
standards. Over time, we have diverged in packaging tools in most areas
but we mostly keep backward compatibility with older packages that make
use of JPackage standards.

## Package naming {#_package_naming_2}

Packages MUST follow the standard Fedora [package naming
guidelines](Naming.xml).

Java API documentation MUST be placed into a sub-package called
&#96;+%{name}-javadoc+&#96;.

## Release tags {#_release_tags}

Packages MUST follow the standard Fedora [package versioning
guidelines](Versioning.xml).

## Architecture support {#_architecture_support}

The system JDK / JRE might not be available on all architectures that
are supported by any given Fedora release.

For this reason, all Java packages MUST contain an
&#96;+ExclusiveArch+&#96; tag:

&#42; Packages that build only &#96;+noarch+&#96; sub-packages MUST use
&#96;+ExclusiveArch: %{java_arches} noarch+&#96;. &#42; Packages that
include architecture-dependent build artifacts (i.e. &lt;&lt;JNI&gt;&gt;
modules) MUST use &#96;+ExclusiveArch: %{java_arches}+&#96;.

The &#96;+%{java_arches}+&#96; macro contains a list of all the
architectures where the system JRE / JDK is available and is defined on
all Fedora releases.

## Pre-built dependencies {#_pre_built_dependencies}

Packages MUST follow the standard Fedora [dependency bundling
guidelines](what-can-be-packaged.adoc&#35;prebuilt-binaries-or-libraries).

In particular, &#96;+&#42;.class+&#96; and &#96;+&#42;.jar+&#96; files
from upstream releases MUST NOT be used during build of Fedora packages
and they MUST NOT be included in binary RPM.

## JAR file installation {#_jar_file_installation}

The following applies to all JAR files except &lt;&lt;JNI,JNI-using JAR
files&gt;&gt; and application-specific JAR files (i.e., JAR files that
can only reasonably be used as part of an application and therefore
constitute application-private data).

### Split JAR files {#_split_jar_files}

If a project offers the choice of packaging it as a single monolithic
JAR or as several separate JARs, the split packaging SHOULD be
preferred.

### Installation directory {#_installation_directory}

&#42; All architecture-independent JAR files MUST go into
&#96;+%{\_javadir}+&#96; or its subdirectory. &#42; For installation of
architecture dependent JAR files, see &lt;&lt;JNI&gt;&gt;.

### Filenames {#_filenames}

&#42; If the package provides a &#42;single&#42; JAR file installed
filename SHOULD be &#96;+%{name}.jar+&#96;. &#42; If the package
provides &#42;multiple&#42; JAR files, they SHOULD be installed in a
&#96;+%{name}\\&#96; subdirectory. \\&#42; Versioned JAR files
(\\&#96;&#42;-%{version}.jar+&#96;) MUST NOT be installed unless the
package is a compatibility package. &#42; Packages MAY provide
alternative filenames, as long as they do not conflict with other
packages.

## BuildRequires and Requires {#_buildrequires_and_requires_2}

Java packages MUST BuildRequire their respective build system (or a
versioned binding thereof):

&#42; &#96;+BuildRequires: maven-local+&#96; or
&#96;+maven-local-openjdk\${N}\\&#96; for packages built with Maven
\\&#42; \\&#96;+BuildRequires: javapackages-local&#96; or
&#96;+javapackages-local-openjdk\${N}+&#96; for packages not built with
Maven

Java applications SHOULD have &#96;+Requires+&#96; on an appropriate
Java runtime package:

&#42; &#96;+java-headless+&#96; for applications not requiring graphical
interface &#42; &#96;+java+&#96; for applications requiring graphical
interface &#42; &#96;+java-devel+&#96; for applications requiring
additional content related to Java development

## Javadoc installation {#_javadoc_installation}

&#42; JavaDoc documentation MAY be generated. &#42; If javadoc
documentation is generated, it MUST be installed into a directory of
&#96;+%{\_javadocdir}/%{name}\\&#96; as part of the
\\&#96;-javadoc+&#96; subpackage. &#42; Directory or symlink
&#96;+%{\_javadocdir}/%{name}-%{version}\\&#96; SHOULD NOT exist.
\\&#42; The javadoc subpackage MUST be declared \\&#96;+noarch&#96;,
even if main package is architecture specific.

## No class-path in MANIFEST.MF {#_no_class_path_in_manifest_mf}

JAR files MUST NOT include a &#96;+class-path+&#96; entry in their
&#96;+META-INF/MANIFEST.MF+&#96; file.

## Hardcoded paths {#_hardcoded_paths}

Packages MUST NOT hardcode paths to JAR files they use. When a package
needs to reference a JAR file, the packager SHOULD use one of tools that
are designed for locating JAR files in the system.

## Maven pom.xml files {#_maven_pom_xml_files}

If upstream project is shipping Maven &#96;+pom.xml+&#96; files, these
MUST be installed. Additionally, the package MUST install a mapping
between the upstream artifact and the filesystem by using the
&#96;+%mvn_install+&#96; macro.

If upstream project does not ship Maven &#96;+pom.xml+&#96; file, the
official [maven repository](https://mvnrepository.com/) should be
consulted and if the project publishes &#96;+pom.xml+&#96; files there,
they SHOULD be included.

If modifications to Maven pom.xml files are needed, the
&#96;+%pom\_&#42;+&#96; family of macros SHOULD be used.

## Wrapper Scripts {#_wrapper_scripts}

Applications wishing to provide a convenient method of execution SHOULD
provide a wrapper script in &#96;+%{\_bindir}\\&#96;. Packages SHOULD
use \\&#96;%jpackage_script+&#96; to create these wrapper scripts.

## Compatibility packages {#_compatibility_packages}

In certain cases it might be necessary to create compatibility packages
that provide older API/ABI level of the same library. However, creating
these compatibility packages is strongly discouraged.

To standardize and simplify packaging of such compatibility packages,
the following rules apply:

&#42; Compatibility packages MUST be named in the same way as the
original package except the addition of the version to the package's
name. &#42; Any JAR and POM files MUST be versioned, as well.

\[&#35;JNI\] == Packaging JAR files that use JNI

### Applicability {#_applicability}

Java programs that wish to make calls into native libraries do so via
the Java Native Interface (JNI). A Java package uses JNI if it contains
a .so file. Note that this file can be embedded within JAR files
themselves.

### Guideline {#_guideline}

JNI packages MUST follow guidelines of ordinary Java packages, with
these exceptions:

&#42; JAR files using JNI or containing JNI shared objects themselves
MUST be placed in &#96;+%{\_jnidir}\\&#96;, but MAY be symlinked to
\\&#96;%{\_libdir}/%{name}\\&#96;. \\&#42; JNI shared objects MUST be
placed in \\&#96;%{\_libdir}/%{name}+&#96;.

# JavaScript Packaging Guidelines {#_javascript_packaging_guidelines}

## Overview {#_overview_2}

JavaScript code used for the web needs special consideration to ensure
that it meets the high standards expected of all code shipped by Fedora,
while still being useful and complying with conventions already used on
millions of websites. Additionally, certain libraries typically used on
the web can also be useful in a server-side context (by nodejs or
rubygem-execjs), so it's important to package JavaScript so it meets the
standards required of locally executed code as well.

Please note that this section really only applies to JavaScript
libraries intended for use on the web. Server-side JavaScript runtimes
like Node.js [have their own guidelines](Node.js.xml), and software like
GNOME which embeds JavaScript for extensions have their own directories
and policies as well.

Packages containing JavaScript should make the best effort to regenerate
any precompiled/minimized JS wherever possible, as this leads to more
maintainable packages. Where this would result in a significant
hardship, the bundled pregenerated JS may be shipped with a specfile
comment explaining the decision. This does not eliminate the requirement
to validate licenses of bundled code.

## Naming Guidelines {#_naming_guidelines_2}

The name of a JavaScript library package MUST start with
&#96;+js-\\&#96; then the upstream name. For example:
\\&#96;+js-jquery&#96;.

## BuildRequires {#_buildrequires_3}

To ensure the presence of the necessary RPM macros, all packages that
provide JavaScript in &#96;+%{\_jsdir}+&#96; MUST have:

BuildRequires: web-assets-devel

## Requires {#_requires}

To ensure the availability of the necessary directories, all packages
that provide JavaScript in &#96;+%{\_jsdir}+&#96; MUST have:

Requires: web-assets-filesystem

JavaScript packages MUST NOT have Requires on any HTTP daemon-specific
configuration package, such as &#96;+web-assets-httpd+&#96;, since they
could be used by any HTTP daemon.

## RPM Macros {#_rpm_macros_3}

+----------------------+----------------------+-----------------------+
| Macro                | Normal Definition    | Notes                 |
+======================+======================+=======================+
| &#                   | &#96;+%{\_datad      | The directory where   |
| 96;+%{\_jsdir}+&#96; | ir}/javascript+&#96; | JavaScript libraries  |
|                      |                      | are stored            |
+----------------------+----------------------+-----------------------+

## Install Location {#_install_location}

&#42; If a JavaScript library can be executed locally or consists purely
of JavaScript code, it MUST be installed into a subdirectory of
&#96;+%{\_jsdir}+&#96;.

&#42; If a package contains JavaScript code, but is never useful outside
the browser (e.g. if it is some sort of HTML user interface library) it
may instead install to &#96;+%{\_assetdir}+&#96;. For more information,
see [the Web Assets guidelines](Web_Assets.xml).

&#42; If a package contains JavaScript code that is only used as part of
a web application, and it is not useful to any other applications
whatsoever, it may continue to ship that code along with the
application. However, that does not absolve it from complying with the
rest of these guidelines.

&#42; If a package contains JavaScript code that is not useful on the
web, but only in locally run software (e.g. [Node.js](Node.js.xml) or
GNOME shell extensions), it should use the appropriate directory for its
runtime, not &#96;+%{\_jsdir}+&#96;.

## Server Location {#_server_location}

JavaScript code is included as part of the general [Web Assets
framework](Web_Assets.xml). Therefore, &#96;+%{\_jsdir}\\&#96; is
available on Fedora-provided web servers by default at
\\&#96;/\_sysassets/javascript/+&#96;.

For instance, jQuery may be installed in
&#96;+%{\_jsdir}/jquery/jquery-min.js+&#96;, so web applications that
need to use it can simply include this HTML tag:

    \&lt;script type='text/javascript' src='/_sysassets/javascript/jquery/jquery-min.js'\&gt;\&lt;/script\&gt;;

Regardless, web applications may want to make subdirectories of
&#96;+%{\_jsdir}+&#96; available under their own directory via aliases
or symlinks for compatibility purposes or to eliminate needless
deviation from upstream.

## Compilation/Minification {#_compilationminification}

If a JavaScript library typically is shipped as minified or compiled
code, it MUST be compiled or minified as part of the RPM build process.
Shipping pre-minified or pre-compiled code is unacceptable in Fedora.

The compiler or minifier used by upstream should be used to compile or
minify the code. If the minifier used by upstream is unable to be
included in Fedora, an alternative minifier may be used. See [this
page](https://fedoraproject.org/wiki/JavaScript/Minification_Issues) for
a list of known problem areas and suggestions for workarounds.

Additionally, the uncompiled/unminified version MUST be included
alongside the compiled/minified version.

Minified JavaScript is not useful for JavaScript run locally, as the
entire point of minification is to reduce HTTP transfer times.
Therefore, JavaScript not intended for the web (e.g. for Node.js or
GNOME Shell extensions) MUST NOT be minified.

## Bundling of other Libraries {#_bundling_of_other_libraries}

It is common for a single minified JavaScript file to contain bundled
code from other JavaScript libraries. JavaScript is treated no
differently than other libraries in this respect, so the [Bundling
Guidelines](index.adoc&#35;bundling). MUST still be followed.

## Wrappers for Other Languages or Environments {#_wrappers_for_other_languages_or_environments}

Sometimes there may exist a simple wrapper from a foreign language (like
Ruby via rubygem-execjs or Java via rhino) or server-side JavaScript
environment (like Node.js) to a pure JavaScript library. Such packages
should delete the bundled library code and instead point to and Require
the code provided by the primary Fedora package for that library.

## Node.js Modules that contain browser/pure-JS components {#_node_js_modules_that_contain_browserpure_js_components}

Some Node.js modules include parts that can be used in the browser or by
other server-side JavaScript engines. Such packages should be shipped as
one SRPM that contains two packages:

&#42; One &#96;+js-foo+&#96; package that contains the pure JavaScript
portion, following these guidelines.

&#42; One &#96;+nodejs-foo+&#96; package that contains the Node.js
module portion, following the [Node.js guidelines](Node.js.xml). This
may symlink to the necessary files or directories of the
&#96;+js-foo+&#96; package.

# Lisp Packaging Guidelines {#_lisp_packaging_guidelines}

This document seeks to document the conventions and customs surrounding
the proper packaging of Common Lisp implementations and libraries in
Fedora. This document does *not* describe conventions and customs for
application programs that are written in Common Lisp.

## Introduction {#_introduction_3}

Most Common Lisp implementations provide a compiler to generate their
own binary representation of source. These binary files typically end in
.fasl (for Fast Load). These .fasl files are not compatible across
Common Lisp implementations, or even between different versions of the
same implementation. This unique property calls for special support on
the packaging front.

The Common Lisp community currently rallies around a common packaging
and deployment technology called asdf (Another System Definition
Format). Projects deployed using asdf include a system definition file.
These files include information about project dependencies, licensing,
and the authors. Projects don't typically distribute binaries, but
rather depend on the asdf utilities to compile the Lisp source code on
demand. When you run program that depends on a library managed by asdf,
the asdf system will automatically compile the dependent Lisp code on
demand and cache the results.

The Debian Lisp community have developed tools and guidelines for
packaging and maintaining asdf managed libraries on Linux systems. Their
tool is called common-lisp-controller and, combined with asdf, it
ensures that .fasl files are managed properly on the system. For
instance, when a Common Lisp implementation is upgraded, the .fasl files
for all of the packages built using the old implementation are deleted
so that new ones may be generated on demand.

The rest of this packaging guideline aims to describe how to package
Common Lisp implementations, libraries and programs to take advantage of
asdf and the common-lisp-controller.

## Guidelines for Libraries and Programs written in Common Lisp {#_guidelines_for_libraries_and_programs_written_in_common_lisp}

### Naming {#_naming_3}

Lisp libraries should have their package names prefixed with \'cl-\',
except in the case where the library name already starts with \'cl-\'.

Rationale: There is some overlap between Lisp library names and existing
Fedora packages. Creating a special name space for Lisp libraries should
simplify life for everybody.

### -devel sub-package {#_devel_sub_package}

Pure lisp libraries do not require -devel sub-packages, as they install
source code by default.

### Use of asdf {#_use_of_asdf}

Libraries should be managed by asdf, a packaging format for Common Lisp
libraries (see the cl-asdf package for details). Most modern Lisp
libraries already ship with asdf system definition files (with names
typically ending in \'.asd\'). If none exist, then one will have to be
written. The contents of these files is not all that different from an
RPM .spec file, so this should not be too difficult for a Lisp-savvy
packager. The ASDF manual describing how to write .asd files is
available [here](https://common-lisp.net/project/asdf/asdf.html).

### Install location and hooking into the common-lisp-controller {#_install_location_and_hooking_into_the_common_lisp_controller}

Libraries should depend on the common-lisp-controller package. Lisp
source should be installed in %{\_datadir}/common-lisp/source/. The
package should own that directory. The parent directories are owned by
the common-lisp-controller package. A symlink to the asdf system
definition file should be created from
%{\_datadir}/common-lisp/systems/.asd to
%{\_datadir}/common-lisp/source//.asd (this target directory is also
owned by common-lisp-controller). The %post section should call
&#96;+register-common-lisp-source+&#96;. The %preun section should call
&#96;+unregister-common-lisp-source+&#96;. These scripts are provided by
&#96;+common-lisp-controller+&#96;.

### Spec file template {#_spec_file_template}

&#8230;. Name: &#35; see normal package guidelines Version: &#35; see
normal package guidelines Release: 1%{?dist} Summary: &#35; see normal
package guidelines (SNPG)

Group: &#35; SNPG License: &#35; SNPG URL: &#35; SNPG Source: &#35; SNPG
BuildRoot: %{\_tmppath}/%{name}-%{version}-%{release}-root-%(%{\_\_id_u}
-n)

BuildRequires: common-lisp-controller Requires: common-lisp-controller
Requires(post): common-lisp-controller Requires(preun):
common-lisp-controller

%description

%prep %setup -q

%build

%install &#35; Replace \@NAME@ below with the Common Lisp library name,
which may be different from the &#35; package name if it is not already
prefixed with \'cl-\'.

mkdir -m 755 -p %{buildroot}%{\_datadir}/common-lisp/source/@NAME@ mkdir
-m 755 -p %{buildroot}%{\_datadir}/common-lisp/systems for s in
&#42;.lisp; do install -m 644 \$s
%{buildroot}%{\_datadir}/common-lisp/source/@NAME@; done; for s in
&#42;.asd; do install -m 644 \$s
%{buildroot}%{\_datadir}/common-lisp/source/@NAME@; done; cd
%{buildroot}%{\_datadir}/common-lisp/source/@NAME@ for asd in &#42;.asd;
do ln -s %{\_datadir}/common-lisp/source/@NAME@/\$asd ../../systems;
done

%post register-common-lisp-source \@NAME@

%preun unregister-common-lisp-source \@NAME@

%files %doc %{\_datadir}/common-lisp/source/@NAME@
%{\_datadir}/common-lisp/systems/@NAME@.asd

%changelog &#8230;.

## Guidelines for Common Lisp implementations {#_guidelines_for_common_lisp_implementations}

### Naming {#_naming_4}

There are no special requirements here. Common Lisp implementations
should be packaged using their normal project name.

### -devel sub-package {#_devel_sub_package_2}

Common Lisp implementations do not require -devel sub-packages, and they
necessarily include all development tools by default.

### Use of asdf {#_use_of_asdf_2}

Common Lisp implementations should be able to load asdf by simply
entering \'(require \'asdf)\' at the Lisp Read-Eval-Print loop (REPL).
This may involve modifying search paths or related changes at build
time.

### Install location and hooking into the common-lisp-controller {#_install_location_and_hooking_into_the_common_lisp_controller_2}

Common Lisp implementations should depend on the common-lisp-controller
package.

Common Lisp implementations should install a script in
%{\_libdir}/common-lisp/bin/.sh that supports a single command on the
command line: \'install-clc\'. This should load
%{\_datadir}/common-lisp/source/common-lisp-controller/common-lisp-controller.lisp,
call (common-lisp-controller:init-common-lisp-controller-v4 ) and then
save the resulting image as default for the system.

The %post section should call
&#96;+register-common-lisp-implementation+&#96;. The %preun section
should call &#96;+unregister-common-lisp-implementation+&#96;.

These scripts, and the &#96;+%{\_libdir}/common-lisp/bin+&#96; directory
are provided and owned by the common-lisp-controller package.

All implementations should be modified to load common-lisp-controller's
&#96;+%{\_sysconfdir}/lisp-config.lisp+&#96; on startup.

## Further reading {#_further_reading}

See <https://www.cliki.net/common-lisp-controller> and
<https://common-lisp.net/project/asdf/> for more details on
common-lisp-controller and asdf.

# Lua Packaging Guidelines {#_lua_packaging_guidelines}

## What is Lua? {#_what_is_lua}

As described on the [Lua website](https://www.lua.org/), Lua is

\'Lua is a powerful, efficient, lightweight, embeddable scripting
language. It supports procedural programming, object-oriented
programming, functional programming, data-driven programming, and data
description.\'

To learn Lua, read [Programming in
Lua](https://www.lua.org/pil/contents.html).

## Spec Template for a Lua Package {#_spec_template_for_a_lua_package}

Many Lua packages use [Lua-rocks](http://luarocks.org/) for packaging.
It is helpful to examine the &#96;+.rockspec+&#96; specification as a
guide in writing your spec file. Some packages require compilation of C
programs, but others may be pure Lua. Both will have very similar
install locations.

&#8230;. Summary: Lua integration with libev Name: lua-ev License: MIT

Version: 1.5 Release: 2%{?dist}

URL: <https://github.com/brimworks/lua-ev> Source0:
%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: cmake BuildRequires: gcc BuildRequires: libev-devel
BuildRequires: lua-devel

%description Event loop programming with Lua.

%prep %autosetup -n %{name}-%{version}

%build %cmake -DINSTALL_CMOD=%{lua_libdir} %cmake_build

%install %cmake_install

%check &#35;packaged tests do not work directly &#35;Use example program
as a smoke test LUA_CPATH=%{buildroot}%{lua_libdir}/?.so \\ lua
example.lua LUA_CPATH=%{buildroot}%{lua_libdir}/?.so \\ lua -e \'ev =
require \'ev\'; print(ev.version())\'

%files %license README %doc example.lua %{lua_libdir}/ev.so

%changelog &#42; Thu Dec 08 2022 Benson Muite
&lt;<benson_muite@emailplus.org>&gt; - 1.5-1 - Use README as license

&#42; Sat Nov 19 2022 Benson Muite
&lt;<benson_muite@emailplus.org>&gt; - 1.5-2 - Fix install location
based on review - Add further smoke test

&#42; Wed Nov 16 2022 Benson Muite
&lt;<benson_muite@emailplus.org>&gt; - 1.5-1 - Initial release &#8230;.

## Naming {#_naming_5}

Lua add-on packages generally follow the naming scheme of
&#96;+lua-modulename+&#96; --- e.g. &#96;+lua-filesystem+&#96;,
&#96;+lua-lpeg+&#96;, &#96;+lua-moonscript+&#96;. If the module name
makes it clear that it is an add-on for Lua, though, the module name
itself is sufficient. e.g. &#96;+lutok+&#96;.

Use your judgement --- e.g. the second &#96;+l+&#96; in
&#96;+lua-lpeg+&#96; already stands for Lua, but it might not be seen as
unambiguous enough.

## Macros {#_macros_3}

The following macros for packaging lua extensions are provided by the
&#96;+lua-devel+&#96; package:

+-----------------------------------------------------------------------+
| Macro                                                                 |
+=======================================================================+
| Description                                                           |
+-----------------------------------------------------------------------+
| &#96;+%lua_version+&#96;                                              |
+-----------------------------------------------------------------------+
| version of system installed lua                                       |
+-----------------------------------------------------------------------+
| &#96;+%lua_libdir+&#96;                                               |
+-----------------------------------------------------------------------+
| installation directory for compiled modules                           |
+-----------------------------------------------------------------------+
| &#96;+%lua_pkgdir+&#96;                                               |
+-----------------------------------------------------------------------+
| installation directory for arch-independent modules                   |
+-----------------------------------------------------------------------+
| &#96;+%lua_requires+&#96;                                             |
+-----------------------------------------------------------------------+
| declares the needed runtime dependencies for the binary package       |
+-----------------------------------------------------------------------+

For EPEL, define the following macros at the top of your spec file:

&#8230;. %{!?lua_version: %global lua_version %{lua:
print(string.sub(\_VERSION, 5))}} &#35; for compiled modules
%{!?lua_libdir: %global lua_libdir %{\_libdir}/lua/%{lua_version}} &#35;
for arch-independent modules %{!?lua_pkgdir: %global
lua_pkgdir %{\_datadir}/lua/%{lua_version}} &#8230;.

To make the package pull the correct runtime dependencies, declare them
like this:

&#8230;. Requires: lua &gt;= %{lua_version} Requires: lua &lt; %{lua:
os.setlocale(\'C\'); print(string.sub(\_VERSION, 5) + 0.1)} &#8230;.

# Mono Packaging Guidelines {#_mono_packaging_guidelines}

## File Locations and Architectures {#_file_locations_and_architectures}

For a while, Fedora considered mono packages to be
architecture-specific, and installed assemblies to %{\_libdir}. However,
after discussions with upstream, we now consider mono packages to be
architecture (and platform) independent. This means that mono packages
should be correctly installed into the GAC in in %{\_monogacdir} or
installed into /usr/lib/PACKAGENAME.

As a notable exception, any ELF binary libraries generated in a mono
package must be correctly installed into %{\_libdir}, because these
files are architecture-specific.

Also, even though we consider mono packages to be architecture
independent, they must not be marked as \'noarch\'. Although the
assemblies are the same, the files may differ due to strings referring
to the build architecture.

In addition, because some architectures simply do not support mono,
every mono package (either a library or a mono-using application) must
include

&#8230;. ExclusiveArch: %{mono_arches} &#8230;.

The &#96;+%mono_arches+&#96; must be used instead of a list of
architectures in order to facilitate changes to the architecture list.

## gacutil in a spec file {#_gacutil_in_a_spec_file}

gacutil is used to register dlls with mono (think of it as installing a
library - which it is!).

When packaging &#42;any&#42; mono application which generates libraries
which gacutil then registers (say mysql-connector-net), you need
something like the following in the spec file

&#8230;. %install mkdir -p %{buildroot}/%{\_monogacdir} gacutil -i
bin/mono-1.0/release/MySql.Data.dll -f -package mysql-connector-net
-root %{buildroot}/usr/lib

%files %{\_monogacdir}/MySql.Data %{\_monodir}/mysql-connector-net/
&#8230;.

gacutil format

&#8230;. -i = input dll -f = check references -package = package name
-root = build root &#8230;.

## RPMS and source {#_rpms_and_source}

Don't build RPMS against built from source versions of mono. It will
work for you but probably not for other users!

While you may get away with recompiling the source for part of the
overall package (such as gnome-panel is part of gnome or
evolution-data-server is part of evolution) for other programs, you
should not attempt this with Mono.

If you're going to use the source, you &#42;MUST&#42; remove the RPMS
first.

Compiling mono is not a trivial matter and may not even work (when you
download the source, you must also *make get-monolite-latest* which
grabs a version of the corelib and mcs which are need for compiling the
main C&#35; compilers - the monolite-latest does not always work and you
end up without a working copy of Mono.

## rpmlint and mono packages {#_rpmlint_and_mono_packages}

rpmlint is a program that checks packages for common problems. For mono
packages, some of the rpmlint messages can be disregarded.

Mono installs binaries in %{\_libdir}//bin with symlinks back to
/usr/bin. rpmlint is not happy with this and generates an error (which
is the correct behaviour). It will also not recognise that mono
libraries are not ELF format and may generate errors on this as well.

rpmlint will also pick up on any .pc file installed in the rpm (see
below).

## -devel packages {#_devel_packages_2}

Mono packages &#42;must&#42; package .pc files in a -devel package, even
if that is the only file that will be included. If we were to permit .pc
files in non-devel packages, then we'll have non-devel packages that
depend on -devel packages, inflating the install needlessly.

## Empty debuginfo {#_empty_debuginfo}

Sometimes building mono packages results in an empty debuginfo sub
package, one without any files to install. See Packaging/Debuginfo

## Incorrect Behaviours {#_incorrect_behaviours}

### Distributing Prebuilt Assemblies {#_distributing_prebuilt_assemblies}

Because mono .dlls are generally architecture independent, upstream may
ship tarballs which install precompiled .dlls and .exes. All packages
&#42;must&#42; build from source so the packager needs to watch out for
these tarballs and be certain not to use them. (This can sneak in during
upgrades as well, so the packager has to make sure they're building from
source every time the tarball is changed.)

### Distributing .DLLs from other projects {#_distributing_dlls_from_other_projects}

The Mono project's website makes [this
suggestion](https://www.mono-project.com/Assemblies_and_the_GAC&#35;Libraries_with_Unstable_APIs)

&#8230;. Sometimes developers might want to distribute a library to
other developers but they might not have a library that is API stable or
has not matured enough over time to guarantee the
backwards-compatibility of their libraries or they are not willing to
maintain multiple packages of the various versions for users.
\[&#8230;\] To solve this problem, we recommend that:

&#42; The library developer ships a properly configured pkg-config file.
&#42; The library consumers include an \'update-libraries\' target on
their Makefile that will import the latest version of a library from a
system directory into their application source code distribution. &#42;
The library consumers ship this library as part of their package.
&#8230;.

This suggestion may make it easier for applications targetting unstable
library APIs but it is &#42;\_extremely poor practice\_&#42;. Using
libraries in this manner has all the same problems as linking with
static libraries, most notably that the application can suffer from
security holes in the library long after it is fixed upstream. Mono
applications in Fedora cannot include upstream DLLs (even if they are
compiled from source). This is a blocker issue and &#42;must&#42; be
fixed.

There are several techniques for detecting the presence of these
libraries, none of them fool proof. If you know of a better method,
please add it:

1.  Upstream tarball contains .dlls that were not rebuilt from source
    contained in the package.

2.  Look through the installed .dlls for any that have the same name as
    system .dlls or are suspiciously out of place (Package is myDiary
    and contains mysql.dll, sqlite.dll, and gtk-sharp.dll)

3.  Source directories look odd:

&#8230;. PKGNAME/ src/ data/ libs/ gtk-sharp/ atk-sharp/ &#8230;.

### Redefining \_libdir {#_redefining_libdir}

Packagers should avoid redefining \_libdir in their spec file.
Redefinition of this macro will cover up problems instead of helping fix
them. Packagers should:

1.  Identify which directories the files should install into according
    to the [Packaging Guidelines](index.xml) .

2.  Patch the packages build scripts to install to those locations.

3.  Identify places where the package has hardcoded the old locations
    instead of the new ones and fix those.

4.  Either report the issues to upstream or submit patches. Note that
    upstream projects are generally receptive to patches that allow
    package builders to redefine install locations at build
    time --- less receptive to patches which change upstream's hardcoded
    defaults to our hardcoded defaults.

### Defining target {#_defining_target}

Was done for a brief period when we attempted to package mono apps as
noarch. It was not necessary then (the actual fix was to stop using
AC_CANONICAL\_&#42; in the configure.ac file) and it is definitely not
needed now that we are no longer building noarch mono packages.

## Glossary {#_glossary}

&#42; &#42;AOT&#42;: Ahead Of Time. This usually refers to the ELF .so
file that is the result of ahead of time compiling an assembly. AOTs are
dependent on the assemblies they were generated from for certain data
(unlike their equivalents in python and java). AOTs are created
explicitly, not automatically. &#42; &#42;Assembly&#42;: An assembly is
the EXE or DLL file created by compiling a mono application. These are
not the same as EXE's or DLL's created by compiling a C or C program on
Windows. An assembly contains CIL code rather than machine code. \\&#42;
\\&#42;CIL\\&#42;: CIL stands for Common Intermediate Language. It is
roughly equivalent to java bytecode and is generally portable across
architectures. Some programming practices (calling out to native system
libraries) can lead to CIL code that will not run on all architectures.
\\&#42; \\&#42;GAC\\&#42;: GAC stands for Global Assembly Cache. It is a
machine-wide .NET assemblies cache. \\&#42; \\&#42;Glue
Libraries\\&#42;: Libraries which bridge a system library written in C
or C with Mono. These wrappers are separate different than AOTs.

# Node.js Packaging Guidelines {#_node_js_packaging_guidelines}

The upstream Node.js stance on [global library
packages](https://nodejs.org/en/blog/npm/npm-1-0-global-vs-local-installation/)
is that they are \'.. best avoided if not needed.\' In Fedora, we take
the same stance with our nodejs packages. You can provide a package that
uses nodejs, but you should bundle all the nodejs libraries that are
needed.

## What to Package {#_what_to_package}

&#42; The interpreter, development headers/libraries, and the assorted
tools to manage project-level installations. &#42;&#42; Examples:
nodejs, npm, yarn &#42; Packages that provide applications that users
would want to use in their shell. &#42;&#42; Examples: uglify

## Naming Guidelines {#_naming_guidelines_3}

&#42; Application packages that mainly provide tools (as opposed to
libraries) that happen to be written for Node.js must follow the general
[Naming Guidelines](Naming.xml) instead.

&#42; The name of a Node.js extension/library package must start with
*nodejs-* then the upstream name or name used in the npm registry. For
example: *nodejs-foomodule*. While it is uncommon for a package's name
to contain *node*, if it does, you should still add the nodejs prefix.
For instance, the npm registry contains a *uuid* and a *node-uuid*
module, which would need to be named *nodejs-uuid* and
*nodejs-node-uuid*, respectively.

## BuildRequires {#_buildrequires_4}

To build a package that is a nodejs module, bundles or uses nodejs
modules, or needs nodejs for building or testing, you need to have:

&#8230;. BuildRequires: nodejs-devel &#8230;.

## Macros {#_macros_4}

The following macros are defined for you:

+----------------------+----------------------+-----------------------+
| Macro                | Normal Definition    | Notes                 |
+======================+======================+=======================+
| \_\_nodejs           | %{\_bindir}/node     | The Node.js           |
|                      |                      | interpreter           |
+----------------------+----------------------+-----------------------+
| nodejs_version       | e.g. 0.9.5           | The currently         |
|                      |                      | installed version of  |
|                      |                      | Node.js.              |
+----------------------+----------------------+-----------------------+
| nodejs_sitelib       | %{\_pref             | Where Node.js modules |
|                      | ix}/lib/node_modules | written purely in     |
|                      |                      | JavaScript are        |
|                      |                      | installed             |
+----------------------+----------------------+-----------------------+
| nodejs_sitearch      | %{\_pref             | Where native C++      |
|                      | ix}/lib/node_modules | Node.js modules are   |
|                      |                      | installed             |
+----------------------+----------------------+-----------------------+
| nodejs_symlink_deps  | %{\_prefix}/lib/rpm  | See                   |
|                      | /nodejs-symlink-deps | &lt;&lt;Symlinking    |
|                      |                      | Dependencies&gt;&gt;  |
|                      |                      | below.                |
+----------------------+----------------------+-----------------------+
| nodejs_fixdep        | %{\_prefix}/l        | See                   |
|                      | ib/rpm/nodejs-fixdep | &lt;&lt;Correcting    |
|                      |                      | Dependencies&gt;&gt;  |
|                      |                      | below.                |
+----------------------+----------------------+-----------------------+
| nodejs_arches        | %{ix86} x86_64       | See                   |
|                      | %{arm}               | &#35;ExclusiveArch.   |
|                      |                      | This macro is         |
|                      |                      | provided by           |
|                      |                      | &#96;+re              |
|                      |                      | dhat-rpm-config+&#96; |
|                      |                      | in F19+ so it works   |
|                      |                      | with Koji properly.   |
+----------------------+----------------------+-----------------------+
| n                    | %global              | Filters unwanted      |
| odejs_default_filter | \_\_p                | provides from native  |
|                      | rovides_exclude_from | modules. See          |
|                      | \^%{nodejs_sitearc   | &lt;&lt;Filtering     |
|                      | h}/.&#42;\\\\.node\$ | Unwanted              |
|                      |                      | Provides&gt;&gt;      |
|                      |                      | below.                |
+----------------------+----------------------+-----------------------+

These macros are provided by the *nodejs-packaging* package.

During &#96;+%install+&#96; or when listing &#96;+%files+&#96; you can
use the &#96;+%nodejs_sitelib+&#96; or &#96;+%nodejs_sitearch+&#96;
macro to specify where the installed modules are to be found. For
instance:

&#8230;. %files &#35; A pure JavaScript node module
%{nodejs_sitelib}/foomodule/ &#35; A native node module
%{nodejs_sitearch}/barmodule/ &#8230;.

Using this macro instead of hardcoding the directory in the specfile
ensures your spec remains compatible with the installed Node.js version
even if the directory structure changes radically (for instance, if
&#96;+%nodejs_sitelib+&#96; moves into &#96;+%{\_datadir}+&#96;).

## ExclusiveArch {#_exclusivearch}

The V8 JavaScript runtime used by Node.js uses a Just-in-Time (JIT)
compiler that is specially tuned to individual architectures, and must
be manually ported to any new architectures that wish to support it.
Node.js packages must include an ExclusiveArch line that restricts them
to only these architectures.

The &#96;+%{nodejs_arches}+&#96; macro is provided to make this easy, so
pure JavaScript packages must use:

&#8230;. ExclusiveArch: %{nodejs_arches} noarch &#8230;.

Native (binary) packages must omit &#96;+noarch+&#96; and list only
&#96;+%{nodejs_arches}+&#96; or the list of architectures as
appropriate.

## Bundled Licenses {#_bundled_licenses}

The licenses of the bundled Node.js modules need to be in the spec file.
If you are using our bundling script, they will be listed in
&#96;+&lt;package&gt;-&lt;version&gt;-bundled-licenses.txt+&#96;. It is
recommended that you include
&#96;+&lt;package&gt;-&lt;version&gt;-bundled-licenses.txt+&#96; in the
rpm.

Each time you update your package, you need to verify the bundled
licenses against [Fedoras Software License
List](https://docs.fedoraproject.org/en-US/legal/allowed-licenses/).
Note that precompiled/minimized JavaScript may be packaged, but the
requirement to verify the licenses also applies to it, see the
:[JavaScript guidelines](JavaScript.xml).

List all unique licenses on the License: line of your spec file.
[Separate each license with the word
\'and\'](https://docs.fedoraproject.org/en-US/legal/license-field/&#35;_basic_rule).

&#8230;. License: &lt;license1&gt; AND &lt;license2&gt; AND
&lt;license3&gt; &#8230; Source3:
%{npm_name}-%{version}-bundled-licenses.txt &#8230; %prep &#8230; cp
%{SOURCE3} . &#8230; %files %license LICENSE
%{npm_name}-%{version}-bundled-licenses.txt &#8230;.

If you have further questions refer to the [Fedora Licensing
Guidelines](https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/).

## Using tarballs from the npm registry {#_using_tarballs_from_the_npm_registry}

The canonical method for shipping most node modules is tarballs from the
npm registry. The &#96;+Source0+&#96; for such modules should be of the
form
<https://registry.npmjs.org/>&#96;+&lt;modulename&gt;/-/&lt;modulename&gt;-&lt;version&gt;.tgz+&#96;.
For instance:

&#8230;. Source0: <https://registry.npmjs.org/npm/-/npm-1.1.70.tgz>
&#8230;.

This method should be preferred to using checkouts from git or
automatically generated tarballs from GitHub.

These tarballs store the contents of the module inside a
&#96;+package+&#96; directory, so every package using these tarballs
should use the following in &#96;+%prep+&#96;:

&#8230;. %prep %setup -q -n package &#8230;.

## Using tarballs for bundling {#_using_tarballs_for_bundling}

It is prefered to use tarballs for bundling node module dependencies.
These tarballs should be independent from the main package source. There
should be two tarballs. One for the binary, runtime package. One for
testing while the package builds. This creates a smaller installed
package.

These tarballs store the bundled modules in a directory called
node_modules_prod, and node_modules_dev.

If your packages does not need one of the tarballs, then change these
instructions accordingly. If it does not need the prod tarball, remove
&#96;+Source1+&#96; plus the &#96;+%build+&#96; and &#96;+%install+&#96;
sections. If it does not need the dev tarball, remove
&#96;+Source2+&#96; and the &#96;+%check+&#96; section.

Note1: The setup of the prod and dev tarballs will soon become a macro.
At the time of this writting, they are not.

Note2: The tarball with the dev dependencies needs to be unpacked in
%check and not in %prep to avoid accidentally bundling the unpackaged
dependencies that are only needed for testing.

&#8230;. &#8230; Source1: %{npm_name}-%{version}-nm-prod.tgz Source2:
%{npm_name}-%{version}-nm-dev.tgz &#8230; %prep &#8230; &#35; Setup
bundled runtime(prod) node modules tar xfz %{SOURCE1} mkdir -p
node_modules pushd node_modules ln -s ../node_modules_prod/&#42; . ln -s
../node_modules_prod/.bin . popd &#8230; %install &#8230; &#35; Copy
over bundled nodejs modules cp -pr node_modules node_modules_prod
%{buildroot}%{nodejs_sitelib}/%{npm_name} &#8230; %check %{\_\_nodejs}
-e \'require(\'./\')\' &#35; Setup bundled dev node_modules for testing
&#35; Note: this cannot be in %%prep or the dev node_modules &#35; can
get pulled into the regular rpm tar xfz %{SOURCE2} pushd node_modules ln
-s ../node_modules_dev/&#42; . popd pushd node_modules/.bin ln -s
../../node_modules_dev/.bin/&#42; . popd &#35; Example test run using
the binary in ./node_modules/.bin/ ./node_modules/.bin/vows \--spec
\--isolate &#8230; &#8230;.

## Installing Modules {#_installing_modules}

Most node modules do not contain their own install mechanism. Instead
they rely on &#96;+npm+&#96; to do it for them. &#96;+npm+&#96;
&#42;must not&#42; be used to install modules in Fedora packages, since
it usually requires network access.

Instead, install files in their proper place manually using
&#96;+install+&#96; or &#96;+cp+&#96;. Most files should be installed in
&#96;+%{nodejs_sitelib}/\\&#96; but documentation should be installed
via \\&#96;%doc+&#96;. In the event that the module ships arch
independent content other than JavaScript code, that content should be
installed in &#96;+%{\_datadir}+&#96; and the module should be patched
to cope with that.

### Client-side JavaScript {#_client_side_javascript}

Many node modules contain JavaScript that can be used both client-side
and server-side and it is sometimes hard to identify code intended only
for use in the browser. Since there are no current packaging guidelines
for client-side JavaScript and bundling of such code is currently
permitted in Fedora, it is currently permissible for client-side
JavaScript to be bundled with nodejs modules in
&#96;+%{nodejs_sitelib}+&#96;.

## Automatic Requires and Provides {#_automatic_requires_and_provides}

The *nodejs* package includes an automatic Requires and Provides
generator that automatically adds versioned dependencies based on the
information provided in a module's and bundled dependencies
*package.json* file. Additional Requires are added to native (binary)
modules to protect against ABI breaks in Node or the V8 JavaScript
runtime. Additional Provides: bundled() line is added for e

### Provides npm {#_provides_npm}

It also adds virtual provides in the form &#96;+npm(&lt;module
name&gt;)\\&#96; to identify modules listed in the npm registry (the
module is listed at npmjs.org) . If a module is not listed in the npm
registry, it must not provide this. Modules that aren\'t listed in the
npm registry should set \\&#96;+private&#96; to &#96;+true+&#96; in
their &#96;+package.json+&#96; file. If not, you must patch
&#96;+package.json+&#96; to include that.

### Provides bundled {#_provides_bundled}

It also automatically adds bundled provides in the form
&#96;+bundled(&lt;bundled_module_name&gt;) =
&lt;bundled_module_version&gt;+&#96; to identify bundled modules.
Bundled modules must be in either the *node_modules* or
*node_modules_prod* directories to be automatically added.

### Correcting Dependencies {#_correcting_dependencies}

For non-bundled modules only.

Occasionally the dependencies listed in package.json are inaccurate. For
instance, the module may work with a newer version of a dependency than
the one explictly listed in the *package.json* file. To correct this,
use the &#96;+%nodejs_fixdep+&#96; RPM macro. This macro should be used
in &#96;+%prep+&#96; and will patch *package.json* to contain the
correct dependency information.

To convert any dependency to not list a specific version, just call
&#96;+%nodejs_fixdep+&#96; with the npm module name of the dependency.
This changes the version in *package.json* to &#96;+&#42;+&#96;. (Or
adds one if it wasn't already listed.) For example:

&#8230;. %prep %setup -q -n package %nodejs_fixdep foomodule &#8230;.

You can also specify a version:

&#8230;. %prep %setup -q -n package %nodejs_fixdep foomodule \'&gt;2.0\'
&#8230;.

The second argument to &#96;+%nodejs_fixdep+&#96; must be a valid
*package.json* version specifier as explained in [&#96;++&#96;man npm
json\\&#96;++&#96;](https://docs.npmjs.com/files/package.json&#35;version).

You can also remove a dependency:

&#8230;. %prep %setup -q -n package %nodejs_fixdep -r foomodule &#8230;.

## Symlinking Dependencies {#_symlinking_dependencies}

For non-bundled modules only.

Node.js and npm require that dependencies explicitly be included or
linked into a *node_modules* directory inside the module directory. To
make this easier, a &#96;+%nodejs_symlink_deps+&#96; macro is provided
and will automatically create a *node_modules* tree with symlinks for
each dependency listed in *package.json*. This macro should be called in
the &#96;+%install+&#96; section of every Node.js module package.

## Building native modules with node-gyp {#_building_native_modules_with_node_gyp}

Most native modules use the &#96;+node-gyp+&#96; tool to build
themselves, which configures and uses the &#96;+gyp+&#96; build
framework to build addon modules that can interact with Node.js and the
V8 JavaScript interpreter used by it.

The WAF build framework has been abandoned by upstream and is not
supported in Fedora.

### BuildRequires {#_buildrequires_5}

To build a native module designed to be built with node-gyp, add
&#96;+BuildRequires: node-gyp+&#96;, along with &#96;+BuildRequires:
nodejs-devel+&#96; and *-devel* packages for any shared libraries needed
by the module.

### %build {#_build}

Some native modules have Makefiles or other build processes that handle
any special needs that module has, such as linking to system versions of
dependencies. If present, these should be used. Check the module's
*package.json* file for information about what command npm will run to
build these modules.

Most modules use vanilla node-gyp, and may not have build instructions
in *package.json*. To build these, simply use the following:

&#8230;. %build export CXXFLAGS=\'%{optflags}\' node-gyp rebuild
&#8230;.

Note that some modules may specify something like &#96;+node-gyp
configure &amp;&amp; node-gyp build+&#96;. This is equivalent to
&#96;+node-gyp rebuild+&#96;.

### %install {#_install}

&#96;+node-gyp+&#96; creates a shared object file with the extension
&#96;+.node+&#96; as part of its build process, which should be located
in &#96;+build/Release+&#96;. This file may be used as the main entry
point for the library, or is utilized by JavaScript wrapper code
included with the module.

If the shared object is used as the main entry point, it should be
installed at &#96;+%{nodejs_sitelib}/&lt;module
name&gt;/index.node+&#96;. The &#96;+require()\\&#96; function will
automatically load this if there is no corresponding
\\&#96;+index.js&#96; or entry point defined in *package.json* to
override it. For example:

&#8230;. %install mkdir -p %{buildroot}%{nodejs_sitelib}/foomodule cp -p
build/Release/index.node package.json
%{buildroot}%{nodejs_sitelib}/foomodule/ &#8230;.

If the shared object is called by JavaScript wrapper code, the situation
is slightly more complicated.

If the module uses the npm
[*bindings*](https://npmjs.org/package/bindings) module, the shared
object file should be installed in &#96;+%{nodejs_sitelib}/&lt;module
name&gt;/build/&lt;module name&gt;.node+&#96;, which is at the top of
[*bindings*](https://npmjs.org/package/bindings) search path and where
&#96;+node-gyp+&#96; usually creates a symlink to wherever the real
shared object file exists. For example:

&#8230;. %install mkdir -p %{buildroot}%{nodejs_sitelib}/foomodule/build
cp -p package.json wrapper.js %{buildroot}%{nodejs_sitelib}/foomodule/
cp -p build/Release/foomodule.node
%{buildroot}%{nodejs_sitelib}/foomodule/build/ &#8230;.

If the module hardcodes &#96;+build/Release/&lt;module
name&gt;.node+&#96;, the module should be patched to use
&#96;+build/&lt;module name&gt;.node+&#96; instead, and upstream should
be advised that they should use the
[*bindings*](https://npmjs.org/package/bindings) module, because their
module could break when users use debug builds of node.

If the module uses it's own Makefiles to locate the shared object
file(s) to a specific location, then those files should installed in
that location.

### Filtering Unwanted Provides {#_filtering_unwanted_provides}

RPM automatically adds some unwanted virtual provides to the shared
object files included with native modules. To remove them, add
&#96;+%{?nodejs_default_filter}+&#96; to the top of the package's spec
file. For more information, see
[Packaging:AutoProvidesAndRequiresFiltering](AutoProvidesAndRequiresFiltering.xml).

## Build testing in %check {#_build_testing_in_check}

All Node.js module spec files must include a &#96;+%check+&#96; section
that contains (at minimum) the line:

&#8230;. %{\_\_nodejs} -e \'require(\'./\')\' &#8230;.

This test ensures that the module is actually loadable, which will help
avoid situations where a new upstream release has added a new dependency
without the packager noticing.

Any other tests made available by upstream should also be run wherever
possible.

For convienence, %nodejs_symlink_deps also accepts a
&#96;+\--check+&#96; argument, which will make it operate in the current
working directory instead of the buildroot. You can use this in the
&#96;+%check+&#96; section to make dependencies available for running
tests. When this argument is used, development dependencies as listed in
the \'devDependencies\' key in *package.json* are also linked.

## Bundling Script {#_bundling_script}

It is recommended to use the nodejs-packaging-bundler script found in
the Fedora nodejs-packaging-bundler package. More documentation for it
can be found at the [Fedora nodejs-packaging
repo](https://src.fedoraproject.org/rpms/nodejs-packaging/) .

## Example Spec {#_example_spec}

&#8230;. %global npm_name tape

Name: nodejs-%{npm_name} Version: 5.1.1 Release: 1%{?dist} Summary:
Tap-producing test harness for Node.js and browsers

License: MIT AND ISC URL: <https://github.com/substack/tape> Source0:
[https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz](https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz)
Source1: %{npm_name}-%{version}-nm-prod.tgz Source2:
%{npm_name}-%{version}-nm-dev.tgz Source3:
%{npm_name}-%{version}-bundled-licenses.txt

BuildArch: noarch ExclusiveArch: %{nodejs_arches} noarch

Requires: nodejs BuildRequires: nodejs-devel

%description %{summary}.

%prep %setup -q -n package cp %{SOURCE3} . &#35; Setup bundled
runtime(prod) node modules tar xfz %{SOURCE1} mkdir -p node_modules
pushd node_modules ln -s ../node_modules_prod/&#42; . ln -s
../node_modules_prod/.bin . popd

%build &#35;nothing to do

%install mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name} cp -pr
package.json index.js lib/ \\ %{buildroot}%{nodejs_sitelib}/%{npm_name}
&#35; Copy over bundled nodejs modules cp -pr node_modules
node_modules_prod \\ %{buildroot}%{nodejs_sitelib}/%{npm_name}

mkdir -p %{buildroot}%{nodejs_sitelib}/tape/bin install -p -D -m0755
bin/tape %{buildroot}%{nodejs_sitelib}/tape/bin/tape mkdir -p
%{buildroot}%{\_bindir} ln -sr %{nodejs_sitelib}/tape/bin/tape
%{buildroot}%{\_bindir}/tape

%check %{\_\_nodejs} -e \'require(\'./\')\' &#35; Setup bundled dev
node_modules for testing &#35; Note: this cannot be in %%prep or the dev
node_modules &#35; can get pulled into the regular rpm tar xfz
%{SOURCE2} pushd node_modules ln -s ../node_modules_dev/&#42; . popd
pushd node_modules/.bin ln -s ../../node_modules_dev/.bin/&#42; . popd
&#35; Run tests ./node_modules/.bin/tap test/&#42;.js

%files %doc readme.markdown %license LICENSE
%{npm_name}-%{version}-bundled-licenses.txt %{nodejs_sitelib}/tape
%{\_bindir}/tape

%changelog &#8230;.

# OCaml Packaging Guidelines {#_ocaml_packaging_guidelines}

This document seeks to document the conventions and customs surrounding
the proper packaging of OCaml modules in Fedora. It does not intend to
cover all situations, but to codify those practices which have served
the Fedora OCaml community well.

## Naming {#_naming_6}

The base OCaml compiler is called ocaml.

OCaml modules, libraries and syntax extensions should be named
ocaml-foo. Examples include: &#96;ocaml-extlib&#96;,
&#96;ocaml-ssl&#96;.

This naming does not apply to applications written in OCaml, which can
be given their normal name. Examples include: &#96;coccinelle&#96;,
&#96;frama-c&#96;, &#96;virt-top&#96;.

Rationale: this is how they are named in other distros (Debian, PLD) and
this is consistent with Perl / PHP / Python naming.

## Packaging libraries {#_packaging_libraries}

### Main package {#_main_package}

In order to allow OCaml scripts and the toplevel to use a library, the
main package should contain only files matching:

&#42; &#96;&#42;.cma&#96; (contains the bytecode) &#42;
&#96;&#42;.cmi&#96; (contains the compiled signature) &#42;
&#96;&#42;.so&#96; (if present, contains OCaml &lt;-&gt; C stubs) &#42;
&#96;META&#96; (the findlib description) &#42; &#96;&#42;.so.owner&#96;
(if present, used by findlib) &#42; a license file (if present) marked
&#96;%license&#96;

&#42; &#96;.cmo&#96; files are not normally included. There is one
exception where &#96;&#42;.cmo&#96; files may be included: if the
&#96;.cmo&#96; file is needed to link, then it must be included to allow
the library to be linked properly.

If the package contains &#96;&#42;.so&#96; files, then they should not
have rpaths, as per Fedora packaging guidelines.

The packager should check the &#96;META&#96; file [^2]. If there is no
&#96;META&#96; file, then the packager should create one, include it in
the package, and pass it to the upstream maintainer.

Rationale: OCaml does not support dynamic linking of binaries, and even
if it did with the current module hash system for expressing strict
typing requirements almost any conceivable change to a library would
require the binary to be recompiled. OCaml scripts are the closest we
come to dynamic linking, in as much as they do not usually depend on a
specific version of a library (albeit this only works because the
scripts are recompiled each time they run).

### &#96;-devel&#96; subpackage {#_96_devel96_subpackage}

The &#96;-devel&#96; subpackage of a library should contain all other
files required to allow development with the library. Normally these
would be:

&#42; &#96;&#42;.a&#96; (contains the compiled machine code) &#42;
&#96;&#42;.cmxa&#96; (describes the compiled machine code) &#42;
&#96;&#42;.cmx&#96; (if present, allows cross-module optimizations)
&#42; &#96;&#42;.mli&#96; (contains the signature of the library) &#42;
&#96;&#42;.cmt&#96; (contains type annotations for compiled code) &#42;
&#96;&#42;.cmti&#96; (contains type annotations for interface files)

&#42; &#96;.o&#96; files are not normally included. There is one
exception --- if the file is needed to link (like &#96;std_exit.cmx&#96;
and &#96;std_exit.o&#96; in OCaml itself), then it should be included.

&#42; &#96;.ml&#96; files are not normally included. The exception is if
the file describes a module signature *and* there is no corresponding
&#96;.mli&#96; file, then the &#96;.ml&#96; file should be included.
(Note that Debian is more permissive and they often distribute
&#96;&#42;.ml&#96; files, allowing the programmer to peek at the
implementation of a module).

Documentation, examples and other articles which are useful to the
developer may be included in the &#96;-devel&#96; sub-package. The
license file (which is in the main package) does not need to be included
again in the &#96;-devel&#96; subpackage.

If the &#96;-devel&#96; subpackage would only contain documentation
files, then the packager may at their discretion place the documentation
files in the main package and not have a &#96;-devel&#96; subpackage at
all.

The &#96;-devel&#96; subpackage should require the exact
name-version-release of the main package (as per Fedora policy). It
should also require any C libraries required for development, and
sometimes this means an explicit &#96;Requires&#96; is needed. For
example, &#96;ocaml-pcre-devel&#96; needs an explicit &#96;Requires:
pcre-devel&#96; to make it usable for development.

Rationale for inclusion of all &#96;.cmx&#96; files: these files are
needed even for modules included in &#96;.cmxa&#96; libraries in order
to enable cross-module optimizations (inlining, constant propagation and
direct function calls). The &#96;.o&#96; files are not needed. \[From a
private email from Alain Frisch\]

### &#96;-doc&#96; subpackage {#_96_doc96_subpackage}

If the documentation files are very large they may be placed in a
separate &#96;-doc&#96; subpackage, as per normal Fedora guidelines.

### &#96;-data&#96; subpackage {#_96_data96_subpackage}

If the package contains excessively large data files, they may be placed
in a separate &#96;-data&#96; subpackage, as per normal Fedora
guidelines.

### &#96;Requires&#96; and &#96;Provides&#96; {#_96requires96_and_96provides96}

For each module that library &#96;A&#96; uses from another library
&#96;B&#96;, library &#96;A&#96; must have a &#96;Requires&#96; of the
form: &#96;ocaml(Modulename) = MD5hash&#96;

Similarly for each module that library &#96;A&#96; may provide to other
libraries, library &#96;A&#96; must have a &#96;Provides&#96; of the
same form.

A library must depend on the precise version of the OCaml compiler, for
example: &#96;ocaml(runtime) = 3.10.0&#96;

The correct &#96;Requires&#96; and &#96;Provides&#96; should be
generated automatically.

Rationale: OCaml does not offer binary compatibility between releases of
the compiler (even between bugfixes). Furthermore the module system uses
a hash over the interface and some internals of a module which basically
means a library or program must be linked against the identical modules
it was compiled with. The &#96;Requires&#96; and &#96;Provides&#96;
lines express the module name and hash so that RPM enforces the same
requirements as the OCaml linker itself. Please see the further reading
at the end of this page for more details.

## Packaging binaries {#_packaging_binaries}

The rules for packaging OCaml binaries are not significantly different
from packaging ordinary programs (see [Packaging
Guidelines](index.xml)).

However if the OCaml package also contains a library, then you should
follow the rules above for packaging libraries as well.

### Stripping binaries {#_stripping_binaries}

Binaries should be stripped, as per ordinary Fedora packaging
guidelines.

There is one exception where a binary should not be stripped. If the
package was compiled with &#96;ocamlc -custom&#96; then the package
contains bytecode which strip will remove, thus rendering the binary
inoperable. It is easy to test for this: if after stripping, any attempt
to run the binary results in the message &#96;No bytecode file
specified&#96; then the binary is compiled like this and should not be
stripped.

Rationale: <https://bugs.debian.org/256900>

### Providing best possible binaries {#_providing_best_possible_binaries}

The packager should attempt to ship native code compiled binaries in
preference to bytecode compiled binaries, where this is possible.

## Bytecode-only architectures {#_bytecode_only_architectures}

The OCaml native code compiler (&#96;ocamlopt&#96;) contains code
generators for popular architectures, but not for every architecture
that Fedora might support. On such architectures, the spec file should
still build bytecode libraries and binaries.

To test for presence of the native compiler, use the
&#96;+%{ocaml_native_compiler}+&#96; macro. Define conditional sections
in %build, %install and %files if necessary. For example:

&#8230;. %build make byte %ifarch %{ocaml_native_compiler} make opt
%endif &#8230;.

To test that your spec file will work on such an architecture,
temporarily remove or rename &#96;/usr/bin/ocamlopt&#96; and
&#96;/usr/bin/ocamlopt.opt&#96; while building.

Rationale: Debian packaging policy section 2.3 does the same thing.

## Unnecessary files {#_unnecessary_files}

The following files should not normally be distributed:

&#42; &#96;&#42;.cmo&#96; object files. Exception: see above. &#42;
&#96;&#42;.o&#96; for corresponding &#96;&#42;.cmx&#96;. Exception: see
above. &#42; &#96;&#42;.ml&#96; sources. Exception: see above.

## Security issues in OCaml libraries {#_security_issues_in_ocaml_libraries}

If a security issue arises in an OCaml library, then all libraries and
binaries which depend on it must be recompiled.

OCaml scripts do not need to be changed (unless resolving the security
issue requires changing the public interface to the library and the
script is broken by the change). This is because OCaml scripts are
recompiled each time they run.

## RPM Macros {#_rpm_macros_4}

The following macros are available to use in spec files:

&#42; &#96;+%{ocaml_native_compiler}\\&#96;: the architectures for which
native compilation is available \\&#42;
\\&#96;%{ocaml_natdynlink}\\&#96;: the architectures for which native
dynamic linking is available \\&#42; \\&#96;%{ocamldir}\\&#96;:
top-level installation directory for OCaml packages, currently
equivalent to \\&#96;%{\_libdir}/ocaml+&#96; &#42;
&#96;+%{ocaml_files}\\&#96;: generate a list of installed files, in
files named \\&#96;.ofiles\\&#96; (for the main package) and
.ofiles-devel (for the devel subpackage), unless \\&#96;-s\\&#96; or
\\&#96;-n\\&#96; is given. This macro requires that python3 be available
in the buildroot. Flags: \\&#42;\\&#42; \\&#96;-n\\&#96;: there is no
devel subpackage. All files are listed in \\&#96;.ofiles\\&#96;.
\\&#42;\\&#42; \\&#96;-s\\&#96;: separate installation; each
subdirectory of \\&#96;%{ocamldir}+&#96; is a separate RPM package. For
each subdirectory, &#96;.ofiles-&lt;subdir&gt;&#96; and
&#96;.ofiles-&lt;subdir&gt;-devel&#96; is generated (unless &#96;-n&#96;
is also given).

## Examples {#_examples_6}

This section contains example spec files illustrating how to build OCaml
library and binary packages with various build tools.

### Dune {#_dune}

Dune is a popular build tool for OCaml packages. RPM macros are
available to make building with dune simple.

&#42; &#96;%dune_build&#96;: Invoke dune to build all installable
artifacts in release mode. Flags: &#42;&#42; &#96;-j
&lt;number&gt;&#96;: number of jobs that can be run in parallel. This is
automatically set to &#96;%{?\_smp_mflags}&#96;, so is typically used
only to eliminate parallelism with &#96;-j 1&#96;. &#42;&#42; &#96;-p
&lt;modules&gt;&#96;: tell dune to build the comma-separated list of
modules only, rather than every installable artifact. &#42;&#42;
&#96;\--&#96;: separate flags for this macro from flags to pass to dune
&#42; &#96;%dune_install&#96;: Invoke dune to install all installable
artifacts. Flags: &#42;&#42; &#96;-n&#96;: there is no devel subpackage.
All files are associated with the main package. &#42;&#42; &#96;-s&#96;:
separate installation; each subdirectory of &#96;+%{ocamldir}+&#96; is a
separate RPM package. Otherwise, all files are associated with a single
main package. &#42;&#42; &#96;\--&#96;: separate flags for this macro
from flags to pass to dune &#42; &#96;%dune_check&#96;: Invoke dune to
run tests for all installable artifacts. Flags: &#42;&#42; &#96;-j
&lt;number&gt;&#96;: number of jobs that can be run in parallel. This is
automatically set to &#96;%{?\_smp_mflags}&#96;, so is typically used
only to eliminate parallelism with &#96;-j 1&#96;. &#42;&#42; &#96;-p
&lt;modules&gt;&#96;: tell dune to build the comma-separated list of
modules only, rather than every installable artifact. &#42;&#42;
&#96;\--&#96;: separate flags for this macro from flags to pass to dune
&#42; &#96;%odoc_package&#96;: Declare a subpackage that olds
odoc-generated documentation. Flags: &#42;&#42; &#96;-L
&lt;license_filename&gt;&#96;: give the name of a file to include in the
subpackage as a license file.

The following is an example specfile for an imaginary OCaml library
called *foolib* that is built with &#96;dune&#96;.

:::: formalpara
::: title
ocaml-dune-example.spec
:::
::::

### &#96;Topkg&#96; {#_96topkg96}

&#96;topkg&#96;, the \'transitory OCaml software packager\', generates
scripts that are executed to perform various package and build tasks.

The following is an example specfile for an imaginary OCaml library
called *foolib* that is built with &#96;topkg&#96;.

:::: formalpara
::: title
ocaml-topkg-example.spec
:::
::::

### Other build tools {#_other_build_tools}

The following is an example specfile for an imaginary OCaml library
called *foolib*.

:::: formalpara
::: title
ocaml-example.spec
:::
::::

## Further reading {#_further_reading_2}

&#42;
<https://lists.debian.org/debian-ocaml-maint/2005/01/threads.html&#35;00042> -
Thread on ABI compatibility of different versions of OCaml. &#42;
<https://www.redhat.com/archives/fedora-devel-list/2007-May/msg01234.html> -
Explains lack of dynamic linking in upstream. &#42;
<https://www.redhat.com/archives/fedora-devel-list/2007-May/msg01280.html> -
Proposal to include MD5 sums in RPM deps. &#42;
<https://bugzilla.redhat.com/show_bug.cgi?id=433783> - Common rpmlint
errors and warnings in OCaml packages.

# Octave Packaging Guidelines {#_octave_packaging_guidelines}

## What is Octave? {#_what_is_octave}

The definition from [website](https://www.octave.org/) says:

*\'GNU Octave is a high-level language, primarily intended for numerical
computations. It provides a convenient command line interface for
solving linear and nonlinear problems numerically, and for performing
other numerical experiments using a language that is mostly compatible
with Matlab. It may also be used as a batch-oriented language.\'*

If you are interested in packaging Octave packages, you should check
here for upstream sources:

&#42; [The Octave Forge website](https://octave.sourceforge.io/)

## RPM macros {#_rpm_macros_5}

The following macros are defined in /etc/rpm/macros.octave in the octave
3.4.0 (Fedora 15+) package for help in packaging:

&#8230;. &#35; Octave binary API provided %octave_api %(octave-config -p
API_VERSION \|\| echo 0)}

&#35; Octave Package Directories %octshareprefix %{\_datadir}/octave
%octprefix %{octshareprefix}/packages %octarchprefix
%{\_libdir}/octave/packages

%octpkgdir %{octshareprefix}/%{octpkg}-%{version} %octpkglibdir
%{octarchprefix}/%{octpkg}-%{version}

&#35; Run an octave command - quietly with no startup files
%octave_cmd()

&#35; Build Source into a package tar file in a temporary location
%octave_pkg_build

&#35; Install a package. We use the octave pkg install command to
install the &#35; built package into the buildroot. We also put a note
to prevent the root &#35; user from removing the package with the octave
pkg uninstall command %octave_pkg_install

&#35; preun script - we need to remove our uninstall protection and
perhaps &#35; run the package's own uninstall script. %octave_pkg_preun
&#8230;.

## Octave packaging tips {#_octave_packaging_tips}

### Naming of Octave packages {#_naming_of_octave_packages}

Packages of Octave packages have their own naming scheme. They should
take into account the upstream name of the package. This makes a package
name format of &#96;+octave-\$NAME+&#96;. When in doubt, use the name of
the module that you type to import it in octave.

\'\'\'Examples: \'\'\'

&#8230;. octave-java (Octave package named java) octave-gsl (Octave
package named gsl) &#8230;.

Limitations in the pkg function of octave (pkg.m) means that versioning
of octave packages requires that the package version must have a
MAJOR.MINOR.MICRO format. Failing to use this format results in octave
not recognising binary package components in %prefix/libexec.

### Updating the octave package database {#_updating_the_octave_package_database}

Octave maintains a list of installed packages in
/usr/share/octave/octave_packages that needs to be updated on package
install and removal. This file is in an octave plain-text format.

The contents of the /usr/share/octave/packages/ directory are scanned
for the following files when performing a pkg(\'rebuild\') from within
octave.

&#42; /usr/share/octave/packages/*NAMEOFPACKAGE*/packinfo/COPYING &#42;
/usr/share/octave/packages/*NAMEOFPACKAGE*/packinfo/DESCRIPTION

If these files are not present in any given *NAMEOFPACKAGE* directory,
then octave will silently skip the folder and fail to index it
correctly.

Octave will use the contents of octave_packages to modify its path at
startup, allowing octave to find plugins.

### Documentation files {#_documentation_files}

All package files are installed into the octave directories.

## Spec Templates for Octave packages {#_spec_templates_for_octave_packages}

There are two types of Octave packages: arch-specific and noarch.

### Arch specific Octave spec template {#_arch_specific_octave_spec_template}

&#8230;. %global octpkg image &#35; Exclude .oct files from provides
%global \_\_provides_exclude_from \^%{octpkglibdir}/.&#42;\\\\.oct\$

Name: octave-%{octpkg} Version: 1.0.13 Release: 1%{?dist} Summary: Image
processing for Octave Group: Applications/Engineering License:
GPL-2.0-or-later URL: <https://octave.sourceforge.io/image/> Source:
[https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz](https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz)

BuildRequires: octave-devel

Requires: octave(api) = %{octave_api} Requires(post): octave
Requires(postun): octave

%description The Octave-forge Image package provides functions for
processing images. The package also provides functions for feature
extraction, image statistics, spatial and geometric transformations,
morphological operations, linear filtering, and much more.

%prep %setup -q -n %{octpkg}-%{version}

%build %octave_pkg_build

%install %octave_pkg_install

%post %octave_cmd pkg rebuild

%preun %octave_pkg_preun

%postun %octave_cmd pkg rebuild

%files %{octpkglibdir} %dir %{octpkgdir} %{octpkgdir}/&#42;.m %doc
%{octpkgdir}/doc-cache %{octpkgdir}/packinfo

%changelog &#42; Sat Feb 12 2011 Orion Poplawski
&lt;<orion@cora.nwra.com>&gt; 1.0.13-1 - Initial Fedora package &#8230;.

### Noarch Octave spec template {#_noarch_octave_spec_template}

&#8230;. %global octpkg actuarial

Name: octave-%{octpkg} Version: 1.1.0 Release: 1%{?dist} Summary:
Actuarial functions for Octave Group: Applications/Engineering License:
GPLv2+ URL: <https://octave.sourceforge.io> Source:
[https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz](https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz)
BuildArch: noarch

BuildRequires: octave-devel

Requires: octave Requires(post): octave Requires(postun): octave

%description Actuarial functions for Casualty and Property lines.

%prep %setup -q -n %{octpkg}-%{version}

%build %octave_pkg_build

%install %octave_pkg_install

%post %octave_cmd pkg rebuild

%preun %octave_pkg_preun

%postun %octave_cmd pkg rebuild

%files %dir %{octpkgdir} %{octpkgdir}/&#42;.m %doc
%{octpkgdir}/doc-cache %{octpkgdir}/packinfo

%changelog &#42; Sat Feb 12 2011 Orion Poplawski
&lt;<orion@cora.nwra.com>&gt; 1.1.0-1 - Initial Fedora package &#8230;.

### Summary of differences between arch-specific and noarch octave packages {#_summary_of_differences_between_arch_specific_and_noarch_octave_packages}

&#42; Noarch packages set &#96;+BuildArch: noarch+&#96; &#42; Don't
require a specific API version &#42; Noarch packages don't install
anything into %{octpkglibdir}

### Obsoletes notes {#_obsoletes_notes}

Packages that used to be in the octave-forge package need to have the
Obsoletes line above. Packages that were not do not.

# Perl Packaging Guidelines {#_perl_packaging_guidelines}

## Module package naming {#_module_package_naming}

See [Packaging Guidelines: Naming: Perl
modules](Naming.adoc&#35;_perl_modules).

## License tag {#_license_tag}

See [Licensing guidelines specific to
Perl](https://docs.fedoraproject.org/en-US/legal/license-field/&#35;_perl_packages).

## Directory Ownership {#_directory_ownership}

As specified in the [general Packaging
Guidelines](index.adoc&#35;_file_and_directory_ownership), Perl packages
are expected to share ownership of certain directories.

In general, a noarch Perl package must own:

&#8230;. &#35; For noarch packages: vendorlib %{perl_vendorlib}/&#42;
&#8230;.

&#8230;and a arch-specific Perl package must own:

&#8230;. &#35; For arch-specific packages: vendorarch
%{perl_vendorarch}/&#42; %exclude %dir %{perl_vendorarch}/auto/ &#8230;.

## Build Dependencies {#_build_dependencies_4}

As stated in [Packaging Guidelines: Build-Time Dependencies
(BuildRequires)](index.adoc&#35;buildrequires), a package must
explicitly indicate its build dependencies (using
&#96;+BuildRequires:+&#96;) outside of the minimal set required for RPM
to build packages. This includes any dependency on Perl. While Perl may
have been in the default buildroot at one time, this is not currently
the case.

Below is a list of Perl-related build dependencies you may need.

&#42; &#96;+perl-generators+&#96; -- Automatically generates run-time
Requires and Provides for installed Perl files. Whenever you install a
Perl script or a Perl module, you must include a build dependency on
this package.

&#42; &#96;+perl-interpreter+&#96; -- The Perl interpreter must be
listed as a build dependency if it is called in any way, either
explicitly via &#96;+perl+&#96; or &#96;+%\_\_perl+&#96;, or as part of
your package's build system.

&#42; &#96;+perl-devel+&#96; - Provides Perl header files. If building
architecture-specific code which links to &#96;+libperl.so+&#96; library
(e.g. an XS Perl module), you must include &#96;+BuildRequires:
perl-devel+&#96;.

If a specific Perl module is required at build time, use
&#96;perl(*MODULE*)&#96; syntax as documented above. This applies to so
called *core* modules as well, since they may move in and out of the
base Perl package over time.

If you need to limit your package to a specific Perl version, use
&#96;+perl(:VERSION)\\&#96; dependency with desired version constraint
(e.g. \\&#96;+perl(:VERSION) \\&gt;= 5.22&#96;). Do not use a comparison
against the version of the &#96;+perl+&#96; package because it includes
an epoch number, which makes version comparisons tricky.

## Perl Requires and Provides {#_perl_requires_and_provides}

Perl packages use the virtual &#96;+perl(Foo)\\&#96; naming to indicate
a given Perl module. Packages should use this methodology, and not
require the package name directly. For example, a package requiring the
Perl module Readonly should not explicitly require
\\&#96;+perl-Readonly&#96;, but rather &#96;+perl(Readonly)\\&#96;,
which the \\&#96;+perl-Readonly&#96; package provides.

It is recommended to include explicit dependencies for core modules,
because they can move between sub-packages or disappear from core Perl.

### Versioned MODULE_COMPAT\_ Requires or &#96;+perl-libs+&#96; {#_versioned_module_compat_requires_or_96perl_libs96}

Packages with Perl modules installed in %{perl_vendorarch},
%{perl_vendorlib}, %{perl_privlib} or %{perl_archlib} will automatically
gain dependency on &#96;+perl-libs+&#96; for pure Perl modules or a
dependency on &#96;+perl(:MODULE_COMPAT\_&lt;perl_version&gt;)\\&#96;
for libraries with compiled code. The dependency is handled by
\\&#96;+perl-generators&#96;.

Packages that require the Perl interpreter or &#96;+libperl.so+&#96; but
do not install modules to the aforementioned directories or explicitly
link to &#96;+libperl.so.&lt;perl_version&gt;+&#96; need to handle the
dependency manually.

### Filtering Requires and Provides {#_filtering_requires_and_provides}

RPM's dependency generator can often throw in additional dependencies
and will often think packages provide functionality contrary to reality.
To fix this, the dependency generator needs to be overridden so that the
additional dependencies can be filtered out. Please see [Packaging
Guidelines: Automatic Filtering of Provides and Requires -
Perl](AutoProvidesAndRequiresFiltering.adoc&#35;_perl) for information.

### Manual Requires and Provides {#_manual_requires_and_provides}

Under some circumstances, RPM's automatic dependency generator can miss
dependencies that should be added. This is usually as a result of using
language constructs that the dependency script wasn't expecting. An
example of this is in the &#96;+perl-Class-Accessor-Chained+&#96;
package, where the following can be found:

&#8230;. use base \'Class::Accessor::Fast\'; &#8230; use base
\'Class::Accessor\'; &#8230;.

A tell-tale sign of this particular construct is that the package
contains a dependency on &#96;+perl(base)+&#96;, but this is not the
only situation in which dependencies can be missed. This package needed
additional dependencies as follows:

&#8230;. Requires: perl(Class::Accessor), perl(Class::Accessor::Fast)
&#8230;.

In general, it's a good idea to look at the upstream package's
documentation for details of other dependencies.

Another similar example of missing requirements can be seen in
&#96;+perl-Spreadsheet-WriteExcel+&#96;:

&#8230;. package Spreadsheet::WriteExcel::Utility; &#8230; use autouse
\'Date::Calc\' =&gt; qw(Delta_DHMS Decode_Date_EU Decode_Date_US); use
autouse \'Date::Manip\' =&gt; qw(ParseDate Date_Init); &#8230;.

Similarly, it possible to miss Provides:, as was the case in [Bug
&#35;167797](https://bugzilla.redhat.com/167797) , where the
&#96;+perl-DBD-Pg+&#96; package failed to Provide:
&#96;+perl(DBD::Pg)\\&#96; due to the following construct in
\\&#96;+DBD::Pg&#96; version 1.43:

&#8230;. { package DBD::Pg; &#8230;.

The usual way of writing this, and what's expected by RPM, is:

&#8230;. { package DBD::Pg; &#8230;.

So it's wise to examine the Provides: of your packages to check that
they are sane and complete. If something is missing, it can be fixed
either by using manual Provides: entries, or by patching the source to
use a format that RPM can parse correctly.

## URL tag {#_url_tag}

For CPAN-based packages the URL tag should use a non-versioned
metacpan.org URL. E.g., if one were packaging the module
&#96;+Net::XMPP+&#96;, the URL would be:

&#8230;. URL: <https://metacpan.org/release/Net-XMPP> &#8230;.

## Testing and Test Suites {#_testing_and_test_suites}

Perl packages typically have a large, healthy test suite. It is policy
to run as much of the test suite as possible, subject to the technical
limitations of the build system. This means, at the least:

&#42; All modules required for tests should be listed as a BuildRequires
&#42; Any \'optional\' tests should be enabled &#42; Any modules needed
for the tests but not yet in Fedora that could be included in Fedora
should also be submitted for review

### When to &#42;not&#42; test {#_when_to_42not42_test}

There are a couple caveats here:

&#42; Optional tests do not need to be enabled if they will cause
circular build deps &#42; Tests which require network or display access
should be disabled for the build system, but with a method provided for
local builds &#42; Tests which do not test package functionality should
still be invoked, but their exclusion not be considered a blocker (e.g.
&#96;+Test::Pod::Coverage+&#96;, &#96;+Test::Kwalitee+&#96; and the
like) &#42; Author, \'release candidate\', or smoke tests do not need to
be enabled e.g. tests using &#96;+Perl::Critic+&#96;.

Additionally, for \'meta\' packages that provide a common interface to a number of similar modules, it is not necessary to package all of the modules that the package supports so long as at least one module exists to allow the meta package to provide functionality. For instance, the package &#96;+perl-JSON-Any+&#96; (&#96;+JSON::Any+&#96;) provides a common interface to &#96;+JSON+&#96;, &#96;+JSON::XS+&#96;, &#96;+JSON::PC+&#96;, &#96;+JSON::Syck+&#96; and &#96;+JSON::DWIM+\\&#96

:   &#96;+JSON::PC+&#96; and &#96;+JSON::DWIM+&#96; are not currently in
    Fedora and do not need to be packaged as, e.g. &#96;+JSON::XS+&#96;
    enables &#96;+JSON::Any+&#96;.

## Conditionally enabling/disabling tests {#_conditionally_enablingdisabling_tests}

One common way to disable a test for mock but enable it locally is to
use a &#96;+\_with_foo+&#96; macro test, e.g.,

&#8230;. %check %{!?\_with_network_tests: rm t/roster.t } ./Build test
&#8230;.

With this construct, an offending test will be removed and not executed,
unless &#96;+\--with network_tests+&#96; is passed to
&#96;+rpmbuild+&#96; or %\_with_network_tests is defined somewhere, e.g.
in a user's &#96;+\$HOME/.rpmmacros+&#96;. This approach preserves the
test suite for local builds while working within the technical
limitations of the build system.

## Makefile.PL vs Build.PL {#_makefile_pl_vs_build_pl}

Perl modules typically utilize one of two different build systems:

&#42; &#96;+ExtUtils::MakeMaker+&#96; &#42; &#96;+Module::Build+&#96;

The two different styles are easily recognizable:
&#96;+ExtUtils::MakeMaker+&#96; employs the &#96;+Makefile.PL+&#96;
build file, and is the \'classical\' approach; &#96;+Module::Build+&#96;
is a newer approach, with support for things MakeMaker cannot do. While
the ultimate choice of which system to employ is clearly in the hands of
upstream, if &#96;+Build.PL+&#96; is present in a distribution the
packager should employ that build framework unless there is a good
reason to do otherwise.

See also PackagingTips/Perl&#35;Makefile.PL_vs_Build.PL .

## .h files in module packages {#_h_files_in_module_packages}

It is not uncommon for binary module packages to include .h files, see
e.g. &#96;+perl-DBI+&#96;, &#96;+perl-Glib+&#96;, &#96;+perl-Gtk2+&#96;.
For a variety of reasons these should not be split off into a -devel
package.

## Updates of packages {#_updates_of_packages}

Summary of tools used for updates and helpful comments can be found here
Perl/updates.

## Useful tips {#_useful_tips}

Some modules try to pull in modules from CPAN. Instead of patching
makefile, you can easily add PERL5_CPANPLUS_IS_RUNNING=1 to avoid CPAN
entirely.

## Perl SIG {#_perl_sig}

People around Perl, who are packaging, maintaining &amp; reviewing
packages. If you are interested in Perl, join [the mailing
list](https://lists.fedoraproject.org/admin/lists/perl-devel.lists.fedoraproject.org/),
where are discussed latest issues.

# PHP Packaging Guidelines {#_php_packaging_guidelines}

Fedora Packaging Guidelines for PHP addon modules

\[&#35;types\] == Different types of PHP packages

There are basically 4 different kinds of PHP modules, which are packaged
for Fedora:

&#42; [PECL](https://pecl.php.net) (PHP Extension Community Library)
modules, which are PHP modules usually written in C and are dynamically
loaded by the PHP interpreter on startup. This will be deprecated in
favor of PIE.

&#42; [PEAR](https://pear.php.net) (PHP Extension and Application
Repository) modules, which are reusable components written in PHP,
usually classes, which can be used in your own PHP applications and
scripts by using e.g. the &#96;+include()+&#96; directive. This is
deprecated in favor of composer and discouraged.

&#42; Composer registered libraries, which are reusable components
written in PHP, usually PSR-0 compliant classes, registered on a package
registry, most often on [Packagist](https://packagist.org/).

&#42; CHANNEL : packages which register a channel. A channel is a
repository which provides PHP extensions. This is deprecated and
discouraged.

&#42; [PIE](https://github.com/php/pie) registered extensions, which are
PHP modules usually written in C and are dynamically loaded by the PHP
interpreter on startup, registered on a package registry, most often on
[Packagist](https://packagist.org/extensions).

&#42; Other packages providing a PHP extension not handled by PEAR/PECL
mechanisms.

While upstream uses the same package and distribution format for PECL
and PEAR, creating RPMs has to take some differences into account.

3 channels are defined on installation of &#96;+php-pear+&#96;:

&#42; &#96;+pear.php.net+&#96; (alias &#96;+pear+&#96;) : the default
channel for PHP Extension and Application Repository

&#42; &#96;+pecl.php.net+&#96; (alias &#96;+pecl+&#96;) : the default
channel for PHP Extension Community Library

&#42; &#96;+\_\_uri+&#96; : Pseudo-channel for static packages

Other channels must be configured at RPM build time and at at RPM
installation time.

\[&#35;naming-scheme\] == Naming scheme

&#42; PECL packages from standard pecl channel should be named
&#96;+php-pecl-PECLPackageName-%{version}-%{release}.%{arch}.rpm+&#96;.

&#42; PEAR packages from standard pear channel should be named
&#96;+php-pear-PEARPackageName-%{version}-%{release}.noarch.rpm+&#96;.

&#42; CHANNEL packages should be named
&#96;+php-channel-ChannelAlias-%{version}-%{release}.noarch.rpm+&#96;

&#42; Packages from another channel should be named
&#96;+php-ChannelAlias-PackageName-%{version}-%{release}.noarch.rpm+&#96;

&#42; Composer enabled packages (referenced in packagist.org or another
registry) should be named
&#96;+php-vendor-library-%{version}-%{release}.noarch.rpm+&#96; (where
&#96;+vendor/library+&#96; is the known packagist name, &#96;+name+&#96;
attribute in &#96;+composer.json+&#96;). When &#96;+vendor+&#96; equals
&#96;+library+&#96;, one can be dropped (ex &#96;+symfony/symfony+&#96;
can be named &#96;+php-symfony+&#96;).

&#42; PIE enabled packages (referenced in packagist.org or another
registry) should be named
&#96;+php-vendor-extension-%{version}-%{release}.%{arch}.rpm+&#96;
(where &#96;+vendor/extension+&#96; is the known packagist name,
&#96;+name+&#96; attribute in &#96;+composer.json+&#96;). When
&#96;+vendor+&#96; equals &#96;+extension+&#96;, one can be dropped (ex
&#96;+xdebug/xdebug+&#96; can be named &#96;+php-xdebug+&#96;).

&#42; Other packages should be named
&#96;+php-PackageName-%{version}-%{release}.%{arch}.rpm+&#96;;
&#96;+%{arch}\\&#96; can be \\&#96;+noarch&#96; where appropriate.

Please make sure that a pure PHP package (PEAR, packagist&#8230;) is
correctly being built for &#96;+noarch+&#96;.

As for other packages, name should only use lowercase, underscore and
slash replaced by dash.

The &#96;+PECLPackageName+&#96; and the &#96;+PEARPackageName+&#96;
should be consistent with the upstream naming scheme. The Crack PHP
Extension would thus be named &#96;+php-pecl-crack+&#96; with the
resulting packages being &#96;+php-pecl-crack-0.4-1.i386.rpm+&#96; and
&#96;+php-pecl-crack-0.4-1.src.rpm+&#96;.

Note that applications that happen to be written in PHP do not belong
under the &#96;+php-&#42;+&#96; namespace.

\[&#35;file-placement\] == File Placement

Non-PEAR PHP software which provides shared libraries should put its PHP
source files for such shared libraries in a subfolder of
&#96;+%{*datadir}/php+&#96;, named according to the name of the
software. For example, a library called \_Whizz_Bang* (with a RPM called
&#96;+php-something-Whizz-Bang+&#96;) would put the PHP source files for
its shared libraries in &#96;+%{\_datadir}/php/Whizz_Bang+&#96;.

A PSR-0 [^3] compliant library would put its PHP files in
&#96;+%{\_datadir}/php/+&#96;

A PSR-4 [^4] compliant library would put its PHP files in
&#96;+%{\_datadir}/php/+&#96; in a PSR-0 compliant tree.

PEAR documentation provided by upstream are installed in
&#96;+%{pear_docdir}\\&#96;, should stay there, and must be marked as
\\&#96;%doc+&#96;.

PECL documentation provided by upstream is installed in
&#96;+%{pecl_docdir}\\&#96;, should stay there, and must be marked as
\\&#96;%doc+&#96;.

The &#96;+composer.json+&#96; file is not used, and should be installed
as &#96;+%doc+&#96; as it provides useful information about the package
and its dependencies.

\[&#35;requires-provides\] == Requires and Provides

\[&#35;requires-provides-pear\] === PEAR Packages from the standard
channel/repository

A PEAR package &#42;MUST&#42; have:

&#8230;. BuildRequires: php-pear(PEAR) Requires: php-pear(PEAR)
Requires(post): %{*pear} Requires(postun): %{*pear} Provides:
php-pear(foo) = %{version} &#8230;.

The virtual provide should match exactly upstream name, including case
and underscore, ex: &#96;+php-pear(Text_Wiki)+&#96;

A PEAR package must have all its dependencies available as PEAR
packages, so should only requires those using the
&#96;+php-pear(foo)+&#96; virtual provides. Known exception for
unbundled libraries (which are often bundled because not available in
any PEAR channel).

\[&#35;requires-provides-channel\] === Packages for CHANNEL (repository)
configuration

A CHANNEL package &#42;MUST&#42; have :

&#8230;. Requires: php-pear(PEAR) Requires(post): %{*pear}
Requires(postun): %{*pear} Provides: php-channel(channelname) &#8230;.

\[&#35;requires-provides-pear-nonstandard\] === PEAR Packages from a non
standard channel/repository

A PEAR package &#42;MUST&#42; have:

&#8230;. BuildRequires: php-channel(channelname) BuildRequires:
php-pear(PEAR) Requires: php-pear(PEAR) Requires(post): %{*pear}
Requires(postun): %{*pear} Requires: php-channel(channelname) Provides:
php-pear(channelname/foo) = %{version} &#8230;.

\[&#35;requires-provides-composer\] === Composer registered Packages

Each package registered on [Packagist](https://packagist.org/) (which is
the most widely used registry, so defined as the implicit one)
&#42;MUST&#42; have

&#8230;. Provides: php-composer(vendor/library) = %{version} &#8230;.

Package registered on another registry &#42;MUST&#42; have

&#8230;. Provides: php-composer(registry_url/vendor/library) =
%{version} &#8230;.

The virtual provide should match exactly upstream name, including
underscore, ex: &#96;+php-composer(pear/console_table)+&#96;

Packages moved from PEAR to Composer/Packagist should also Provide
&#96;+php-pear(foo)+&#96; when needed (used by other PEAR packages).

Packages must not Require any &#96;+php-pear(foo)\\&#96;, but should use
\\&#96;+php-composer(pear/foo)&#96;.

&#96;+composer.json+&#96; useful attributes (see [Composer schema
documentation](https://getcomposer.org/doc/04-schema.md))

&#42; &#96;+name+&#96;

&#42; &#96;+description+&#96; : 1 line, could be used as RPM summary
attribute

&#42; &#96;+homepage+&#96; : could be used as RPM URL attribute

&#42; &#96;+license+&#96;

&#42; &#96;+require+&#96; : describes mandatory dependencies PHP
version, PHP extensions or other composer libraries, those must be
required by the RPM package as &#96;+php-composer(foo)+&#96;

&#42; &#96;+require-dev+&#96; : describes development dependencies,
usually useful a build time (ex: to run unit test), so could appear as
BuidRequires

&#42; &#96;+suggest+&#96; : describes optional dependencies, so could
appear as Requires (packager choice)

&#42; &#96;+conflict+&#96; : as RPM Conflicts

&#42; &#96;+replace+&#96; : as RPM Obsoletes

&#42; &#96;+provide+&#96; : for additional virtual provides, must also
be in RPM Provides as &#96;+php-composer(foo)+&#96;

\[&#35;requires-provides-c\] === C extensions (PECL and others)

To be certain that a binary extension will run correctly with a
particular version of PHP, it is necessary to check that a particular
package has both API and ABIs matching the installed version of PHP. The
mechanism for doing this is as follows:

&#8230;. BuildRequires: php-devel Requires: php(zend-abi) =
%{php_zend_api} Requires: php(api) = %{php_core_api} &#8230;.

Each extension &#42;MUST&#42; also have (to track the move out/in of
php-src), using the &#96;+module+&#96; name as reported by \'php
\--modules\' or the .so file name in lowercase.

&#8230;. Provides: php-module = %{version} Provides: php-module%{\_isa}
= %{version} &#8230;.

\[&#35;requires-provides-pecl\] === PECL Packages

PECL extension &#42;MUST&#42; have ABI check (see [C
extensions](#requires-provides-c) above).

A PECL package &#42;MUST&#42; also have:

&#8230;. Provides: php-pecl(foo) = %{version} Provides:
php-pecl(foo)%{?\_isa} = %{version} &#8230;.

\[&#35;requires-provides-pecl-nonstandard\] === PECL Packages from a non
standard channel/repository

A PECL package from a non standard channel MUST have (instead of
previous provides)

&#8230;. Requires: php-channel(channelname) Provides:
php-pecl(channelname/foo) = %{version} Provides:
php-pecl(channelname/foo)%{?\_isa} = %{version} &#8230;.

\[&#35;requires-provides-pie\] === PIE Packages

PIE extension &#42;MUST&#42; have ABI check (see [C
extensions](#requires-provides-c) above).

Each package registered on Packagist (which is the most widely used
registry, so defined as the implicit one) &#42;MUST&#42; have:

&#8230;. Provides: php-pie(vendor/extension) = %{version} &#8230;.

\[&#35;requires-provides-other\] === Other Packages

PHP addons which are neither PEAR nor PECL should require what makes
sense (either a base PHP version or a &#96;+php-api+&#96;,
&#96;+php(zend-abi)+&#96; as necessary).

\[&#35;requires-provides-httpd\] === Apache requirement

A PHP library must not have an explicit Requires on &#96;+php+&#96; or
&#96;+httpd+&#96;, since these libraries could be used with any
webserver or any SAPI (&#96;+php-cli+&#96;, &#96;+php-cgi+&#96;,
&#96;+php-fpm+&#96;, &#8230;).

Only a PHP web application, which provides a specific Apache httpd
configuration, should have a Requires on &#96;+httpd+&#96; and
&#96;+mod_php+&#96;.

\[&#35;requires-provides-extensions\] === Extensions Requires

PHP extensions must have a Requires on all of the dependent extensions
(&#96;+php-json+&#96;, &#96;+php-gd+&#96;, &#96;+php-mbstring+&#96;,
&#8230;). These extensions are virtual Provides of the php sub-packages.

Can be ignored as always present: &#96;+core+&#96;, &#96;+date+&#96;,
&#96;+filter+&#96;, &#96;+hash+&#96;, &#96;+pcre+&#96;,
&#96;+random+&#96;, &#96;+reflection+&#96;, &#96;+session+&#96;,
&#96;+spl+&#96;, &#96;+standard+&#96;.

\[&#35;requires-provides-min-php\] === Requiring a Minimum PHP version

If you need to specify a minimum PHP version, the recommended method is
to add a Requires: &#96;+php(language) &gt;= \$VERSION+&#96; (where
&#96;+\$VERSION+&#96; is the minimum PHP version).

\[&#35;c-pecl-config-file\] == C extension and PECL package
configuration files

Each extension should drop a configuration file in
&#96;+%{php_inidir}\\&#96; and/or \\&#96;%{php_ztsinidir}+&#96; to
enable the extension. This file must contain the name of the loaded
extension. The file must use a numeric prefix to ensure correct load
order:

&#42; range 00-19 is reserved for zend_extensions (ex:
&#96;+10-opcache.ini+&#96;, &#96;+15-xdebug.ini+&#96;, &#8230;)

&#42; range 20-39 is reserved for extensions from php sources (ex:
&#96;+20-pdo.ini+&#96;, &#96;+30-pdo_pgsql.ini+&#96;, &#8230;)

&#42; range 40-99 is available for other extensions (ex:
&#96;+40-zip.ini+&#96;, &#8230;)

\[&#35;macros-scriptlets\] == Macros and scriptlets

\[&#35;macros-scriptlets-zts\] === PHP ZTS extension

When the Apache HTTPD is run in worker mode (instead of prefork mode),
the ZTS (Zend Thread Safe) version of PHP is used.

If an extension maintainer wants to provide a ZTS version of this
extension, the maintainer must ensure that:

&#42; the extension is thread safe &#42; the libraries used by the
extension are thread safe

The &#96;+php-devel+&#96; package provides the necessary files to build
ZTS modules and provides several helper macros:

For standard (NTS) extensions

&#8230;. %{\_\_php} %{\_bindir}/php %{php_extdir}
%{\_libdir}/php/modules %{php_inidir} %{\_sysconfdir}/php.d
%{php_incldir %{\_includedir}/php &#8230;.

For ZTS extensions

&#8230;. %{\_\_ztsphp} %{\_bindir}/zts-php %{php_ztsextdir}
%{\_libdir}/php-zts/modules %{php_ztsinidir} %{\_sysconfdir}/php-zts.d
%{php_ztsincldir %{\_includedir}/php-zts/php &#8230;.

&#96;+php-devel+&#96; provides the executables needed during the build
of a ZTS extension, which are:

&#42; &#96;+zts-phpize+&#96; &#42; &#96;+zts-php-config+&#96; &#42;
&#96;+zts-php+&#96; (which is only useful to run the test suite during
build)

\[&#35;macros-scriptlets-channel\] === Packages for CHANNEL (repository)
configuration

Here are some recommended scriptlets for properly registering and
unregistering the channel:

&#8230;. %post if \[ \$1 -eq 1 \] ; then %{*pear} channel-add
%{pear_xmldir}/%{name}.xml &gt; /dev/null \|\| : else %{*pear}
channel-update %{pear_xmldir}/%{name}.xml &gt; /dev/null \|\|: fi

%postun if \[ \$1 -eq 0 \] ; then %{\_\_pear} channel-delete
%{channelname} &gt; /dev/null \|\| : fi &#8230;.

\[&#35;macros-scriptlets-pear\] === PEAR Modules

The &#96;+php-pear+&#96; package provides several useful macros:

&#42; &#96;+%{pear_phpdir}\\&#96; \\&#42; \\&#96;%{pear_docdir}\\&#96;
(This evaluates to \\&#96;%{\_docdir}/pear+&#96;.) &#42;
&#96;+%{pear_testdir}\\&#96; \\&#42; \\&#96;%{pear_datadir}\\&#96;
\\&#42; \\&#96;%{pear_xmldir}\\&#96; \\&#42;
\\&#96;%{pear_metadir}\\&#96; (This evaluates to
\\&#96;/var/lib/pear+&#96;.)

These definitions for the .spec should be of interest:

&#8230;. BuildRequires: php-pear &gt;= 1:1.4.9-1.2 Provides:
php-pear(PackageName) = %{version} Requires: php-common &gt;= 4.3,
php-pear(PEAR) Requires(post): %{\_bindir}/pear Requires(postun):
%{\_bindir}/pear &#8230;.

Be sure you delete any PEAR metadata files at the end of
&#96;+%install+&#96;:

&#8230;. rm -rf %{buildroot}/%{pear_metadir}/.??&#42; &#8230;.

Here are some recommended scriptlets for properly registering the
module:

&#8230;. %post %{\_bindir}/pear install \--nodeps \--soft \--force
\--register-only %{pear_xmldir}/%{name}.xml &gt;/dev/null \|\|: &#8230;.

And here are some recommended scriptlets for properly unregistering the
module, from the standard channel:

&#8230;. %postun if \[ \'\$1\' -eq \'0\' \] ; then %{\_bindir}/pear
uninstall \--nodeps \--ignore-errors \--register-only Foo_Bar
&gt;/dev/null \|\|: fi &#8230;.

From a non standard channel (&#96;+pear+&#96; command requires the
channel):

&#8230;. %postun if \[ \'\$1\' -eq \'0\' \] ; then %{\_bindir}/pear
uninstall \--nodeps \--ignore-errors \--register-only
Foo_channel/Foo_Bar &gt;/dev/null \|\|: fi &#8230;.

\[&#35;macros-scriptlets-pecl\] === PECL Modules

The &#96;+php-pear+&#96; package provides several useful macros:

&#42; &#96;+%{pecl_phpdir}\\&#96; \\&#42; \\&#96;%{pecl_docdir}\\&#96;
\\&#42; \\&#96;%{pecl_testdir}\\&#96; \\&#42;
\\&#96;%{pecl_datadir}\\&#96; \\&#42; \\&#96;%{pecl_xmldir}+&#96;

You may need to define a few additional macros to extract some
information from PHP. It is recommended that you use the following:

&#8230;. %global php_apiver %((echo 0; php -i 2&gt;/dev/null \| sed -n
\'s/\^PHP API =&gt; //p\') \| tail -1) %{!?*pecl: %{expand: %%global*
pecl %{\_bindir}/pecl}} %{!?php_extdir: %{expand: %%global php_extdir
%(php-config \--extension-dir)}} &#8230;.

Module (un)registration is handled automatically by file triggers in the
&#96;+php-pear+&#96; package.

For older releases, here are some recommended scriptlets for properly
registering and unregistering a module:

&#8230;. BuildRequires: php-pear Requires(post): %{*pecl}
Requires(postun): %{*pecl}

%post %{pecl_install} %{pecl_xmldir}/%{name}.xml &gt;/dev/null \|\| :

%postun if \[ \$1 -eq 0 \] ; then %{pecl_uninstall} %{pecl_name}
&gt;/dev/null \|\| : fi &#8230;.

\[&#35;macros-scriptlets-other\] === Other Modules

If your module includes compiled code, you may need to define some
macros to extract some information from PHP. It is recommended that you
user the following:

&#8230;. %global php_apiver %((echo 0; php -i 2&gt;/dev/null \| sed -n
\'s/\^PHP API =&gt; //p\') \| tail -1) %global php_extdir %(php-config
\--extension-dir 2&gt;/dev/null \|\| echo \'undefined\') %global
php_version %(php-config \--version 2&gt;/dev/null \|\| echo 0) &#8230;.

\[&#35;hints\] == Additional Hints for Packagers

\[&#35;hints-pear-pecl\] === PEAR &amp; PECL Packages

The source archive contains a &#96;+package.xml+&#96; outside any
directory, so you have to use use

&#8230;. %setup -q -c &#8230;.

in your &#96;+%prep+&#96; section to avoid writing files to the build
root.

\[&#35;hints-pear\] === PEAR Packages

To create your initial specfile, you can use the default template
provided by the &#96;+rpmdevtools+&#96; package:

&#8230;. rpmdev-newspec -t php-pear php-pear-Foo &#8230;.

Or you can generate one; make sure you have the
&#96;+php-pear-PEAR-Command-Packaging+&#96; package installed:

&#8230;. pear make-rpm-spec Foo.tgz &#8230;.

# Python Packaging Guidelines {#_python_packaging_guidelines}

This version of Python Packaging Guidelines is in effect since 2021 and
represents a major rewrite and paradigm shift. Not all packages are
updated to reflect this. Older guidelines are kept as a historical
reference, but new packages &#42;MUST NOT&#42; use them. Existing
packages &#42;MUST&#42; migrate to the current Python guidelines:

&#42; ["201x-era" Python packaging guidelines](Python_201x.xml)
(Packages using these usually use the deprecated
&lt;&lt;py3_install,&#96;+%py3_install+&#96;&gt;&gt; or
&lt;&lt;py3_install_wheel,&#96;+%py3_install_wheel+&#96; macro&gt;&gt;
or call &#96;+setup.py install+&#96;.)

:::: note
::: title
:::

These guidelines only support current Fedora releases. For older
releases (such as in EPEL 8), consult the [201x-era
guidelines](Python_201x.xml).
::::

The two &lt;&lt;Distro-wide guidelines&gt;&gt; below apply to all
software in Fedora that uses Python at build- or run-time.

The rest of the Guidelines apply to packages that ship code that can be
imported with Python's &#96;+import+&#96; statement. Specifically, that
is all packages that install files under
&#96;+/usr/lib&#42;/python&#42;/+&#96;.

Except for the two "Distro-wide guidelines", these Guidelines do not
apply to simple one-file scripts or utilities, especially if these are
included with software not written in Python. However, if an application
(e.g. CLI tool, script or GUI app) needs a more complex Python library,
the library &#42;SHOULD&#42; be packaged as an importable library under
these guidelines.

A major goal for Python packaging in Fedora is to *harmonize with the
wider Python ecosystem*, that is, the [Python Packaging
Authority](https://pypa.io) (PyPA) standards and the [Python Package
Index](https://pypi.org/) (PyPI). Packagers &#42;SHOULD&#42; be prepared
to get involved with upstream projects to establish best practices as
outlined here. We wish to improve both Fedora and the wider Python
ecosystem.

:::: note
::: title
:::

Some build tools (like CMake or autotools) may not work with the latest
PyPA standards yet. (For example, they might generate
&#96;+.egg-info+&#96; directories rather than &#96;+.dist-info+&#96;.)
While this document's normative points (MUST/SHOULD) are tool-agnostic,
many of the practical tips and helper macros will not be applicable. If
this affects you, consider contacting the [Python
SIG](https://lists.fedoraproject.org/archives/list/python-devel@lists.fedoraproject.org/)
for guidance and/or following the [older guidelines](Python_201x.xml)
for the time being.
::::

:::: note
::: title
:::

Fedora's Python SIG not only develops these guidelines, but it's also
involved in PyPA standards and Python packaging best practices. Check
out [the wiki](https://fedoraproject.org/wiki/SIGs/Python) or [mailing
list](https://lists.fedoraproject.org/archives/list/python-devel@lists.fedoraproject.org/)
if you need help or wish to help out.
::::

## Distro-wide guidelines {#_distro_wide_guidelines}

### Build-time dependency on python3-devel {#_build_time_dependency_on_python3_devel}

&#42;Every&#42; package that uses Python (at run-time and/or build-time)
and/or installs Python modules &#42;MUST&#42; have a build-time
dependency on &#96;+python3-devel+&#96;, even if Python is not actually
invoked during build-time. Such a package &#42;MUST&#42; use one of the
following in its &#96;+.spec+&#96; file:

&#42;
&lt;&lt;pyproject_buildrequires,&#96;+%pyproject_buildrequires+&#96;&gt;&gt;
in the &#96;+%generate_buildrequires+&#96; section &#42;
&#96;+BuildRequires: python3-devel+&#96;

Only having a transitive build-time dependency on
&#96;+python3-devel+&#96; is not sufficient. If the package uses an
alternate Python interpreter instead of &#96;+python3+&#96;
(e.g. &#96;+pypy+&#96;, &#96;+jython+&#96;, &#96;+python2.7+&#96;), it
&#42;MAY&#42; instead require the corresponding &#96;+&#42;-devel+&#96;
package.

The &#96;+&#42;-devel+&#96; package brings in relevant RPM macros. It
may also enable automated or manual checks: for example, Python
maintainers use this requirement to list packages that use Python in
some way and might be affected by planned changes.

### Mandatory macros {#_mandatory_macros}

The following macros &#42;MUST&#42; be used where applicable.

The expansions in parentheses are provided only as reference/examples.

The macros are defined for you in all supported Fedora and EPEL
versions.

&#42; &#96;+%{python3}\\&#96; (\\&#96;/usr/bin/python3+&#96;): The
Python interpreter. For example, this macro should be used for invoking
Python from a &#96;+spec+&#96; file script, passed to
&#96;+configure+&#96; scripts to select a Python executable, or used as
&#96;+%{python3} -m pip+&#96; to run a Python-based tool.

\+ If the packaged software invokes Python at *run time* (as opposed to
running Python to build/test it), it might be necessary to pass flags to
&#96;+%{python3}+&#96; to isolate it from user-installed packages. See
&lt;&lt;Shebangs&gt;&gt; for details.

\+ &#42; &#96;+%{python3_version}\\&#96; (e.g. \\&#96;+3.9&#96;,
&#96;+3.10+&#96;): Version of the Python interpreter.

\+ &#42; &#96;+%{python3_version_nodots}\\&#96; (e.g. \\&#96;+39&#96;,
&#96;+310+&#96;): Version of the Python interpreter without the dot.
&#42; &#96;+%{python3_sitelib}\\&#96;
(e.g. \\&#96;/usr/lib/python3.9/site-packages+&#96;): Where pure-Python
modules are installed.

\+ &#42; &#96;+%{python3_sitearch}\\&#96;
(e.g. \\&#96;/usr/lib64/python3.9/site-packages+&#96;): Where Python
extension modules (native code, e.g. compiled from C) are installed.

The rest of this document uses these macros, along with
&#96;+%{\_bindir}\\&#96; (\\&#96;/usr/bin/+&#96;), instead of the raw
path names.

### Python implementation support[]{#_multiple_python_runtimes} {#_python_implementation_support}

Fedora primarily targets *CPython*, the reference implementation of the
Python language. We generally use "Python" to mean CPython.

Alternate implementations like &#96;+pypy+&#96; are available, but
currently lack comprehensive tooling and guidelines for packaging. When
targetting these, there are no hard rules (except the general Fedora
packaging guidelines). But please try to abide by the *spirit* of these
guidelines. When in doubt, consider consulting the Python SIG.

### Python version support {#_python_version_support}

Fedora packages &#42;MUST NOT&#42; depend on other versions of the
CPython interpreter than the current &#96;+python3+&#96;.

In Fedora, Python libraries are packaged for a single version of Python,
called &#96;+python3+&#96;. For example, in Fedora 32,
&#96;+python3+&#96; is Python 3.8.

In the past, there were multiple Python stacks,
e.g. &#96;+python3.7+&#96; and &#96;+python2.7+&#96;, installable
together on the same machine. That is also the case in some projects
that build *on top* of Fedora, like RHEL, EPEL and CentOS. Fedora might
re-introduce parallell-installable stacks in the future (for example if
a switch to a new Python version needs a transition period, or if enough
interested maintainers somehow appear).

Fedora does include alternate interpreter versions,
e.g. &#96;+python2.7+&#96; or &#96;+python3.5+&#96;, but these are meant
only for developers that need to test upstream code. Bug and security
fixes for these interpreters only cover this use case. Packages such as
&#96;+pip+&#96; or &#96;+tox+&#96;, which enable setting up isolated
environments and installing third-party packages into them,
&#42;MAY&#42;, as an exception to the rule above, use these interpreters
as long as this is coordinated with the maintainers of the relevant
Python interpreter.

## Naming {#_naming_7}

Python packages have several different names, which should be kept in
sync but will sometimes differ for historical or practical reasons. They
are:

&#42; the Fedora *source package name* (or *component name*,
&#96;+%{name}+&#96;), &#42; the Fedora *built RPM name*, &#42; the
*project name* used on [PyPI](https://pypi.org/) or by
[pip](https://pip.pypa.io), and &#42; the *importable module name* used
in Python (a single package may have multiple importable modules).

Some examples (both good and worse):

+-----------------+-----------------+-----------------+-----------------+
| Fedora          | Built RPM       | Project name    | Importable      |
| component       |                 |                 | module          |
+=================+=================+=================+=================+
| &#96;+python    | &#96;+python3   | &#96;           | &#96;           |
| -requests+&#96; | -requests+&#96; | +requests+&#96; | +requests+&#96; |
+-----------------+-----------------+-----------------+-----------------+
| &#96;+pyth      | &#96;+pytho     | &#9             | &#9             |
| on-django+&#96; | n3-django+&#96; | 6;+Django+&#96; | 6;+django+&#96; |
+-----------------+-----------------+-----------------+-----------------+
| &#9             | &#96;+pytho     | &#9             | &               |
| 6;+PyYAML+&#96; | n3-pyyaml+&#96; | 6;+pyyaml+&#96; | #96;+yaml+&#96; |
+-----------------+-----------------+-----------------+-----------------+
| &#96;+py        | &#96;+pyt       | &#96;+py        | &#              |
| thon-ldap+&#96; | hon3-ldap+&#96; | thon-ldap+&#96; | 96;+ldap+&#96;, |
|                 |                 |                 | &#              |
|                 |                 |                 | 96;+ldif+&#96;, |
|                 |                 |                 | etc.            |
+-----------------+-----------------+-----------------+-----------------+
| &#96;+pyth      | &#96;+pytho     | &#9             | &#96;+PIL+&#96; |
| on-pillow+&#96; | n3-pillow+&#96; | 6;+pillow+&#96; |                 |
+-----------------+-----------------+-----------------+-----------------+
| &#9             | &#96            | &#96;+jupyt     | &#96;+jupyt     |
| 6;+python-jupyt | ;+python3-jupyt | er-client+&#96; | er_client+&#96; |
| er-client+&#96; | er-client+&#96; |                 |                 |
+-----------------+-----------------+-----------------+-----------------+

Elsewhere in this text, the metavariables &#96;+SRPMNAME+&#96;,
&#96;+RPMNAME+&#96;, &#96;+PROJECTNAME+&#96;, &#96;+MODNAME+&#96; refer
to these names, respectively.

### Canonical project name {#_canonical_project_name}

Most of these names are case-sensitive machine-friendly identifiers, but
the *project name* has human-friendly semantics: it is case-insensitive
and treats some sets of characters (like &#96;+.\_-\\&#96;) specially.
For automated use, it needs to be normalized to a canonical format used
by Python tools and services such as setuptools, pip and PyPI. For
example, the canonical name of the \\&#96;+Django&#96; project is
&#96;+django+&#96; (in lowercase). This normalization is defined in [PEP
503](https://www.python.org/dev/peps/pep-0503/&#35;normalized-names),
and &lt;&lt;py_dist_name,the &#96;+%{py_dist_name}+&#96; macro&gt;&gt;
implements it for Fedora packaging. The canonical name is obtained by
switching the project name to lower case and converting all runs of
non-alphanumeric characters to single "-" characters. Example: "The
\$\$\$ Tree" becomes "the-tree".

Elsewhere in this text, the metavariable &#96;+DISTNAME+&#96; refers to
the canonical form of the project name.

Note that in some places, the original, non-normalized project name must
be used. For example, the &lt;&lt;pypi_source,&#96;+%pypi_source+&#96;
macro&gt;&gt; and the &#96;+%autosetup+&#96; macro need
&#96;+Django+&#96;, not &#96;+django+&#96;.

### Name limitations {#_name_limitations}

The character &#96;+&#96; in names of built (i.e. non-SRPM) packages
that include &#96;+.dist-info+&#96; or &#96;+.egg-info+&#96; directories
is reserved for &lt;&lt;Extras&gt;&gt; and &#42;MUST NOT&#42; be used
for any other purpose.

As an exception, &#96;+&#96; characters &#42;MAY&#42; appear at the
*end* of such names.

The &#96;+&#96; character triggers the automatic dependency generator
for extras.

Replace any &#96;+&#96; signs in the upstream name with &#96;+-+&#96;.
Omit &#96;+&#96; signs on the beginning of the name. Consider adding
&#96;Provides&#96; for the original name with &#96;+&#96; characters to
make the package easier to find for users.

### Library naming {#_library_naming}

A built (i.e. non-SRPM) package for a *Python library* &#42;MUST&#42; be
named with the prefix &#96;+python3-\\&#96;. A source package containing
primarily a \_Python library\_ \\&#42;MUST\\&#42; be named with the
prefix \\&#96;+python-&#96;.

The Fedora package's name &#42;SHOULD&#42; contain the &lt;&lt;Canonical
project name&gt;&gt;. If possible, the project name &#42;SHOULD&#42; be
the same as the name of the main importable module, in lowercase, with
underscores (&#96;+\_+&#96;) replaced by dashes (&#96;+-+&#96;).

If the importable module name and the project name do not match, users
frequently end up confused. In this case, packagers &#42;SHOULD&#42;
ensure that upstream is aware of the problem and (especially for new
packages where renaming is feasible) strive to get the package renamed.
The Python SIG is available for assistance.

A *Python library* is a package meant to be imported in Python, such as
with &#96;+import requests+&#96;. Tools like *Ansible* or *IDLE*, whose
code is importable but not primarily meant to be imported from other
software, are not considered libraries in this sense. So, this section
does not apply for them. (See the [general Libraries and Applications
guidelines](index&.xml#35;_libraries_and_applications) for general
guidance.)

The Fedora component (source package) name for a library should be
formed by taking the *canonical project name* and prepending
&#96;+python-\\&#96; if it does not already start with
\\&#96;+python-&#96;. This may leads to conflicts (e.g. between
[bugzilla](https://pypi.org/project/bugzilla/) and
[python-bugzilla](https://pypi.org/project/python-bugzilla/)). In that
case, ensure upstream is aware of the potentially confusing naming and
apply best judgment.

### Application naming {#_application_naming}

Packages that primarily provide applications, services or any kind of
executables &#42;SHOULD&#42; be named according to the general [Fedora
naming guidelines](Naming.xml) (e.g. &#96;+ansible+&#96;).

Consider adding a virtual provide according to &lt;&lt;Library
naming&gt;&gt; above (e.g. &#96;+python3-PROJECTNAME+&#96;), if it would
help users find the package.

## Files to include {#_files_to_include}

### Source files and bytecode cache[]{#_byte_compiling} {#_source_files_and_bytecode_cache}

Packages &#42;MUST&#42; include the source file (&#96;+&#42;.py+&#96;)
&#42;AND&#42; the bytecode cache (&#96;+&#42;.pyc+&#96;) for each
pure-Python importable module. The source files &#42;MUST&#42; be
included in the same package as the bytecode cache.

Scripts that are not importable (typically ones in
&#96;+%{\_bindir}\\&#96; or \\&#96;%{\_libexecdir}+&#96;) &#42;SHOULD
NOT&#42; be byte-compiled.

The cache files are found in a &#96;+*pycache*+&#96; directory and have
an interpreter-dependent suffix like &#96;+.cpython-39.pyc+&#96;.

The cache is not necessary to run the software, but if it is not found,
Python will try to create it when a module is imported. If this
succeeds, the file is not tracked by RPM and it will linger on the
system after uninstallation. If it does not succeed, users can get
spurious SELinux AVC denials in the logs.

Normally, byte compilation (generating the cache files) is done for you
by the &#96;+brp-python-bytecompile+&#96; [BRP
script](index.adoc&#35;_brp_buildroot_policy_scripts), which runs
automatically after the &#96;+%install+&#96; section of the spec file
has been processed. It byte-compiles any &#96;+.py+&#96; files that it
finds in &#96;+%{python3_sitelib}\\&#96; or
\\&#96;%{python3_sitearch}+&#96;.

You must include these files of your package (i.e. in the
&#96;+%files+&#96; section).

If the code is in a subdirectory (importable package), include the
entire directory:

``` spec
%files
%{python3_sitelib}/foo/
```

Adding the trailing slash is best practice for directories.

However, this cannot be used for top-level modules (those directly in
e.g. &#96;+%{python3_sitelib}\\&#96;), because both
\\&#96;%{python3_sitelib}\\&#96; and
\\&#96;%{python3_sitelib}/*pycache*/\\&#96; are owned by Python itself.
Here, the \\&#96;%pycached+&#96; macro can help. It expands to the given
&#96;+&#42;.py+&#96; source file and its corresponding cache file(s).
For example:

``` spec
%files
%pycached %{python3_sitelib}/foo.py
```

expands roughly to:

``` spec
%files
%{python3_sitelib}/foo.py
%{python3_sitelib}/__pycache__/foo.cpython-3X{,.opt-?}.pyc
```

#### Manual byte compilation[]{#manual-bytecompilation} {#_manual_byte_compilation}

If you need to bytecompile stuff outside of
&#96;+%{python3_sitelib}\\&#96;/\\&#96;%{python3_sitearch}\\&#96;, use
the \\&lt;\\&lt;py_byte_compile,\\&#96;%py_byte_compile+&#96;
macro&gt;&gt;.

For example, if your software adds &#96;+%{\_datadir}/mypackage+&#96; to
Python's import path and imports package &#96;+foo+&#96; from there, you
will need to compile &#96;+foo+&#96; with:

``` spec
%py_byte_compile %{python3} %{buildroot}%{_datadir}/mypackage/foo/
```

### Dist-info metadata {#_dist_info_metadata}

Each Python package &#42;MUST&#42; include *Package Distribution
Metadata* conforming to [PyPA
specifications](https://packaging.python.org/specifications/)
(specifically, [Recording installed
projects](https://packaging.python.org/specifications/recording-installed-packages/)).

The metadata &#42;SHOULD&#42; be included in the same subpackage as the
main importable module, if there is one.

This applies to libraries (e.g. &#96;+python-requests+&#96;) as well as
tools (e.g. &#96;+ansible+&#96;).

When software is split into several subpackages, it is OK to only ship
metadata in one built RPM. In this case, consider working with upstream
to also split the upstream project.

The metadata takes the form of a &#96;+.dist-info+&#96; directory
installed in &#96;+%{python3_sitelib}\\&#96; or
\\&#96;%{python3_sitearch}\\&#96;, and contains information that tools
like
https://docs.python.org/3/library/importlib.metadata.html\[\\&#96;+importlib.metadata&#96;\]
use to introspect installed libraries.

For example, a project named &#96;+MyLib+&#96; with importable package
&#96;+mylib+&#96; could be packaged with:

``` spec
%files -p python3-mylib
%{python3_sitelib}/mylib/
%{python3_sitelib}/MyLib-%{version}.dist-info/
%doc README.md
%license LICENSE.txt
```

Note that some older tools instead put metadata in an
&#96;+.egg-info+&#96; directory, or even a single file. This won't
happen if you use the &#96;+%pyproject_wheel+&#96; macro. If your
package uses a build system that generates an &#96;+.egg-info+&#96;
directory or file, please contact Python SIG.

As an exception, the Python standard library &#42;MAY&#42; ship without
this metadata.

### Explicit lists {#_explicit_lists}

Packages &#42;MUST NOT&#42; own shared directories owned by Python
itself, such as the top-level &#96;+*pycache*+&#96; directories
(&#96;+%{python3_sitelib}/*pycache*+&#96;,
&#96;+%{python3_sitearch}/*pycache*+&#96;).

Similarly to the [general rule](index&.xml#35;_explicit_lists),
packagers &#42;SHOULD NOT&#42; simply glob everything under a shared
directory.

In addition to the [general list](index&.xml#35;_explicit_lists), the
following &#42;SHOULD NOT&#42; be used in &#96;+%files+&#96;:

&#42; &#96;+%{python3_sitelib}/&#42;+&#96; &#42;
&#96;+%{python3_sitearch}/&#42;+&#96; &#42;
&#96;+%{python_sitelib}/&#42;+&#96; &#42;
&#96;+%{python_sitearch}/&#42;+&#96; &#42; &#96;+%pyproject_save_files
\'&#42;\'\\&#96; \\&#42; \\&#96;%pyproject_save_files auto&#96;

This rule serves as a check against common mistakes which are otherwise
hard to detect. It does limit some possibilities for automation.

The most common mistakes this rule prevents are:

&#42; installing a test suite system-wide as an importable module named
&#96;+test+&#96;, which would then conflict with other such packages,
and &#42; upstream adding new unexpected importable modules -- you
should always check such changes for
[conflicts](https://docs.fedoraproject.org/en-US/packaging-guidelines/Conflicts/&#35;_common_conflicting_files_cases_and_solutions),
and keep the list of such files explicit and auditable.

## PyPI parity {#_pypi_parity}

Every Python package in Fedora &#42;SHOULD&#42; also be available on
[the Python Package Index](https://pypi.org) (PyPI).

The command &#96;+pip install PROJECTNAME+&#96; &#42;MUST&#42; install
the same package (possibly in a different version), install nothing, or
fail with a reasonable error message.

If this is not the case, the packager &#42;SHOULD&#42; contact upstream
about this. The goal is to get the project name registered or blocked on
PyPI, or to otherwise ensure the rule is followed.

If your package is not or cannot be published on PyPI, you can:

&#42; Ask upstream to publish it &#42; If you wish: publish it to PyPI
yourself and maintain it &#42; Ask [Python
SIG](mailto:python-devel@lists.fedoraproject.org) to *block* the name on
PyPI for you &#42; Email [PyPI admins](mailto:admin@pypi.org) to block
the name for you, giving the project name and explaining the situation
(for example: the package cannot currently be installed via
&#96;+pip+&#96;). You can ask questions and discuss the process at the
[Python Discourse](https://discuss.python.org/t/block-names/4045).

:::: note
::: title
:::

Project names that were in Fedora but not on PyPI when these guidelines
were proposed are *blocked* from being uploaded to PyPI. This prevents
potential trolls from taking them, but it also blocks legitimate owners.
If your package is affected, contact the Python SIG or [file a PyPA
issue](https://github.com/pypa/pypi-support/issues/new?labels=PEP+541&amp;template=pep541-request.md&amp;title=PEP+541+Request%3A+PROJECT_NAME)
and mention &#96;+@encukou+&#96;.
::::

If your package's project name conflicts with a different package on
PyPI, change the project name. As painful as it is, we need to use a
single global namespace across the Python ecosystem. Software that is
not written specifically for Fedora already expects that project names
use the PyPI namespace: for example, if a third-party library identifies
a dependency by name, we don't want that dependency satisfied by an
unrelated Fedora package.

As always, [specific
exceptions](index.adoc&#35;_general_exception_policy) can be granted by
the Packaging Committee.

## Provides and requirements[]{#_provides} {#_provides_and_requirements}

### Provides for importable modules[]{#_the_py_provides_macro} {#_provides_for_importable_modules}

For any module intended to be used in Python 3 with &#96;+import
MODNAME+&#96;, the package that includes it &#42;SHOULD&#42; provide
&#96;+python3-MODNAME+&#96;, with underscores (&#96;+\_+&#96;) replaced
by dashes (&#96;+-+&#96;).

This is of course always the case if the package is named
&#96;+python3-MODNAME+&#96;. If the subpackage has some other name, then
add &#96;+%py_provides python3-MODNAME+&#96; explicitly. See the
following section to learn about &#96;+%py_provides+&#96;.

\[&#35;Automatic-unversioned-provides\] === Automatic python- and
python3.X- provides

For any &#96;+FOO+&#96;, a package that provides &#96;+python3-FOO+&#96;
&#42;SHOULD&#42; use &#96;+%py_provides+&#96; or an automatic generator
to also provide &#96;+python-FOO+&#96; and &#96;+python3.X-FOO+&#96;,
where &#96;+X+&#96; is the minor version of the interpreter.

The provide &#42;SHOULD NOT&#42; be added manually: if a generator or
macro is not used, do not add the &#96;+python-FOO+&#96; /
&#96;+python3.X-FOO+&#96; provides at all.

This is done automatically for package names by a generator. If
absolutely necessary, the generator can be disabled by undefining
&lt;&lt;*pythonname_provides,the &#96;+%*pythonname_provides+&#96;
macro&gt;&gt;.

For provides that aren't package names, or (for technical reasons) for
packages without files, the generator will not work. For these cases,
the following invocation will provide &#96;+python3-FOO+&#96;,
&#96;+python-FOO+&#96; and &#96;+python3.X-FOO+&#96;:

``` spec
%py_provides python3-FOO
```

Using the generator or macro is important, because the specific form of
the provide may change in the future.

\[&#35;Machine-readable-provides\] === Machine-readable
provides[]{#_automatic_provides_with_a_standardized_name}

Every Python package &#42;MUST&#42; provide
&#96;+python3dist(DISTNAME)\\&#96; \\&#42;and\\&#42;
\\&#96;+python3.Xdist(DISTNAME)&#96;, where &#96;+X+&#96; is the minor
version of the interpreter and &#96;+DISTNAME+&#96; is the
&lt;&lt;Canonical project name&gt;&gt; corresponding to the
&lt;&lt;Dist-info metadata&gt;&gt;. For example,
&#96;+python3-django+&#96; would provide
&#96;+python3dist(django)\\&#96; and \\&#96;+python3.9dist(django)&#96;.

This is generated automatically from the dist-info metadata. The provide
&#42;SHOULD NOT&#42; be added manually: if the generator fails to add
it, the metadata &#42;MUST&#42; be fixed.

These *Provides* are used for automatically generated *Requires*.

If absolutely necessary, the automatic generator can be disabled by
undefining the
&lt;&lt;*pythondist_provides,&#96;+%{?*pythondist_provides}+&#96;
macro&gt;&gt;. Consider discussing your use case with the Python SIG if
you need to do this.

### Dependencies {#_dependencies_3}

As mentioned above, each Python package &#42;MUST&#42; explicitly
BuildRequire &#96;+python3-devel+&#96;.

Packages &#42;MUST NOT&#42; have dependencies (either build-time or
runtime) with the unversioned prefix &#96;+python-\\&#96; if the
corresponding \\&#96;+python3-&#96; dependency can be used instead.

Packages &#42;SHOULD NOT&#42; have explicit dependencies (either
build-time or runtime) with a minor-version prefix such as
&#96;+python3.8-\\&#96; or \\&#96;+python3.8dist(&#96;. Such
dependencies &#42;SHOULD&#42; instead be automatically generated or a
macro should be used to get the version.

Packages &#42;SHOULD NOT&#42; have an explicit runtime dependency on
&#96;+python3+&#96;.

Instead of depending on &#96;+python3+&#96;, packages have an automatic
dependency on &#96;+python(abi) = 3.X+&#96; when they install files to
&#96;+%{python3_sitelib}\\&#96; or \\&#96;%{python3_sitearch}\\&#96;, or
they have an automatic dependency on \\&#96;/usr/bin/python3+&#96; if
they have executable Python scripts, or they have an automatic
dependency on &#96;+libpython3.X.so.1.0()+&#96; if they embed Python.

These rules help ensure a smooth upgrade path when &#96;+python3+&#96;
is updated in new versions of Fedora.

\[&#35;Automatically-generated-dependencies\] === Automatically
generated
dependencies[]{#_requires_and_buildrequires_with_standardized_names}

Packages &#42;MUST&#42; use the automatic Python run-time dependency
generator.

Packages &#42;SHOULD&#42; use the opt-in build-dependency generator if
possible.

The packager &#42;MUST&#42; inspect the generated requires for
correctness. All dependencies &#42;MUST&#42; be resolvable within the
targeted Fedora version.

Any necessary changes &#42;MUST&#42; be done by patches or modifying the
source (e.g. with &#96;+sed+&#96;), rather than disabling the generator.
The resulting change &#42;SHOULD&#42; be offered to upstream. As an
exception, [filtering](AutoProvidesAndRequiresFiltering.xml)
&#42;MAY&#42; be used for temporary workarounds and
[bootstrapping](index.adoc&#35;bootstrapping).

Dependencies covered by the generators &#42;SHOULD NOT&#42; be repeated
in the &#96;+.spec+&#96; file. (For example, if the generator finds a
&#96;+requests+&#96; dependency, then &#96;+Requires:
python3-requests+&#96; is redundant.)

The automatically generated requirements are in the form
&#96;+python3.Xdist(DISTNAME)\\&#96;, potentially augmented with version
requirements or combined together with
https://rpm-software-management.github.io/rpm/manual/boolean_dependencies.html\[rich
dependencies\]. Any \\&#96;.0+&#96; suffixes are removed from version
numbers to match the behavior of Python tools. ([PEP
440](https://www.python.org/dev/peps/pep-0440/) specifies that
&#96;+X.Y+&#96; and &#96;+X.Y.0+&#96; are treated as equal.)

Note that the generators only cover Python packages. Other dependencies,
often C libraries like &#96;+openssl-devel+&#96;, must be specified in
the &#96;+.spec+&#96; file manually.

Where the requirements are specified in the source depends on each
project's build system and preferences. Common locations are
&#96;+pyproject.toml+&#96;, &#96;+setup.py+&#96;, &#96;+setup.cfg+&#96;,
&#96;+config.toml+&#96;.

#### Run-time dependency generator {#_run_time_dependency_generator}

The automatic runtime dependency generator uses package metadata (as
recorded in installed &#96;+&#42;.dist-info+&#96; directories) to
determine what the package depends on.

In an emergency, you can opt-out from running the requires generator by
&lt;&lt;python_disable_dependency_generator, adding
&#96;+%{?python_disable_dependency_generator}\\&#96;\\&gt;\\&gt; to the
package (usually, just before the main package's
\\&#96;%description+&#96;).

#### Build-time dependency generator {#_build_time_dependency_generator}

The opt-in (but strongly recommended) build-time dependency generator
gathers information from [&#96;+pyproject.toml+&#96; build-system
information](https://www.python.org/dev/peps/pep-0517/&#35;source-trees)
(with fallback to &#96;+setuptools+&#96;) plus a standardized
[build-system
hook](https://www.python.org/dev/peps/pep-0517/&#35;get-requires-for-build-wheel)
to gather further requirements. See &lt;&lt;pyproject_buildrequires,the
&#96;+%pyproject_buildrequires+&#96; macro&gt;&gt; for more details.

Note that without the &#96;+-R+&#96; flag, the generator will include
run-time requirements in BuildRequires. This is useful for running tests
and for checking that the dependencies are available in Fedora.

### Test dependencies {#_test_dependencies}

See the &lt;&lt;Tests&gt;&gt; section.

\[&#35;Extras\] === Extras[]{#_python_extras}

Python extras are a way for Python projects to declare that extra
dependencies are required for additional functionality.

For example, &#96;+requests+&#96; has several standard dependencies
(e.g. &#96;+urllib3+&#96;). But it also declares an *extra* named
&#96;+requests\[security\]\\&#96;, which lists additional dependencies
(e.g. \\&#96;+cryptography&#96;). Unlike RPM subpackages, extras can
only specify additional dependencies, not additional files. The main
package will work if the optional dependency is not installed, but it
might have limited functionality.

Python tools treat extras as virtual packages. For example, if a user
runs &#96;+pip install \'requests\[security\]\'\\&#96;, or installs a
project that depends on \\&#96;+requests\[security\]&#96;, both
&#96;+requests+&#96; and &#96;+cryptography+&#96; will be installed.

In Fedora, extras are usually provided by packages with no files.
Instead of square brackets, Fedora package names conventionally use the
&#96;+&#96; character (which is valid in RPM package names, but not in
Python canonical project names nor in extras identifiers).

#### Handling extras {#_handling_extras}

Python packages &#42;SHOULD&#42; have Provides for all extras the
upstream project specifies, except:

&#42; those that are not useful for other packages (for example
build/development requirements, commonly named &#96;+dev+&#96;,
&#96;+doc+&#96; or &#96;+test+&#96;), and &#42; those that have
requirements that are not packaged in Fedora.

A package that provides a Python extra &#42;MUST&#42; provide
&#96;+python3dist(DISTNAME\[EXTRA\])\\&#96; \\&#42;and\\&#42;
\\&#96;+python3.Xdist(DISTNAME\[EXTRA\])&#96;, where &#96;+X+&#96; is
the minor version of the interpreter, &#96;+DISTNAME+&#96; is the
&lt;&lt;Canonical project name&gt;&gt;, and &#96;+EXTRA+&#96; is the
name of a single extra. For example,
&#96;+python3.9dist(requests\[security\])+&#96;. These requirements
&#42;SHOULD&#42; be generated using the automatic dependency generator.

A package that provides a Python extra &#42;MUST&#42; require the
extra's main package with exact NEVR.

A subpackage that primarily provides one Python extra &#42;SHOULD&#42;
be named by appending &#96;+&#96; and the extra name to the main package
name. For example, &#96;+python3-requests+security+&#96;.

The most straightforward way to provide an extra is with a dedicated
subpackage containing no files (a "metapackage"). This case can be
automated with the
&lt;&lt;pyproject_extras_subpkg,&#96;+%pyproject_extras_subpkg+&#96;
macro&gt;&gt; or the
&lt;&lt;python_extras_subpkg,&#96;+%python_extras_subpkg+&#96;
macro&gt;&gt;.

This is not the only way: when some extra is always useful in a distro,
it can be provided by the main package; when several extras are related,
they may be provided by a single subpackage. However, having one
dedicated subpackage per extra allows you to use the automatic
dependency generator to ensure that the extras' requirements will stay
in sync with upstream. If you create a dedicated subpackage and want it
to be always/usually installed, you can *Require*/*Recommend*/*Suggest*
it from the main package.

The dependency generator for extras activates if the following holds:

&#42; The package name must end with &#96;+EXTRA&#96; (where
&#96;+EXTRA+&#96; is the extra name). &#42; The package must contain the
&#96;+.dist-info+&#96; directory, usually as &#96;+%ghost+&#96;.

##### Example and convenience macros {#_example_and_convenience_macros}

The extra subpackage for &#96;+setuptools_scm\[toml\]\\&#96; can be
specified using the \\&#96;%pyproject_extras_subpkg+&#96; convenience
macro as follows. The macro takes the main package name and name(s) of
the extra(s):

``` spec
%pyproject_extras_subpkg -n python3-setuptools_scm toml
```

If not using &#96;+%pyproject_install+&#96;, you will instead need to
use &#96;+%python_extras_subpkg+&#96; and pass a path to the
&#96;+dist-info+&#96; directory:

``` spec
%python_extras_subpkg -n python3-setuptools_scm -i %{python3_sitelib}/\&#42;.dist-info toml
```

For this case, the extras dependency generator will read upstream
metadata from the &#96;+.dist-info+&#96; directory. If it finds that the
extra requires on &#96;+toml+&#96;, it will generate &#96;+Requires:
python3.Xdist(toml)\\&#96; and \\&#96;+Provides:
python3dist(setuptools-scm\[toml\])&#96; (and the corresponding
&#96;+python3.Xdist+&#96; provide).

If you need additional features that the
&#96;+&#42;\_extras_subpkg+&#96; macros do not cover, you will need to
write the subpackage sections manually. Such features can be, for
example:

&#42; Obsoleting/providing other names (e.g. obsoleted extras packages)
&#42; Manual strong or weak dependencies on other (possibly non-Python)
packages

As an example of what you need to write in these cases, both of the
&#96;+&#42;\_extras_subpkg+&#96; macro invocations above expand to the
following:

``` spec
%package -n python3-setuptools_scm+toml
Summary: Metapackage for python3-setuptools_scm: toml extra
Requires: python3-setuptools_scm = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n python3-setuptools_scm+toml
This is a metapackage bringing in toml extra requires for python3-setuptools_scm.
It contains no code, just makes sure the dependencies are installed.

%files -n python3-setuptools_scm+toml
%ghost %{python3_sitelib}/\&#42;.dist-info
```

Note that the dependency generator does not add a dependency on the main
package (the &#96;+Requires: python3-setuptools_scm = &#8230;+&#96;
above). If you are not using the &#96;+%python_extras_subpkg+&#96;
macro, you need to add it manually.

#### Removing extras {#_removing_extras}

If an existing extra is removed from an upstream project, the Fedora
maintainer &#42;SHOULD&#42; try to convince upstream to re-introduce it
(with an empty list of dependencies). If that fails, the extra
&#42;SHOULD&#42; be Obsoleted from either the main package or another
extras subpackage.

Note that removing extras is discouraged in [setuptools
documentation](https://setuptools.readthedocs.io/en/latest/userguide/dependency_management.html&#35;optional-dependencies)
(see the *Tip* box near the end of the *Optional dependencies* section).

#### Automatic Requires for extras {#_automatic_requires_for_extras}

The automatic &lt;&lt;Run-time dependency generator&gt;&gt; will
generate Requires on &#96;+python3.Xdist(DISTNAME\[EXTRA\])\\&#96; from
upstream \\&#96;+Requires-Dist&#96; metadata.

If the required package does not yet provide metadata for the extra,
contact the Fedora maintainer to add it.

In an emergency, you can define the
&lt;&lt;\_python_no_extras_requires,&#96;+%*python_no_extras_requires+&#96;
macro&gt;&gt; to avoid automatically generating \_all* extras
requirements.

## Interpreter invocation {#_interpreter_invocation}

### Shebangs {#_shebangs}

Shebang lines to invoke Python &#42;MUST&#42; use &#96;+%{python3}+&#96;
as the interpreter.

Shebang lines to invoke Python &#42;SHOULD&#42; be
&#96;+&#35;!%{python3} -%{py3_shebang_flags}+&#96; and they
&#42;MAY&#42; include extra flags.

If (some of) the default flags from &lt;&lt;py3_shebang_flags,the
&#96;+%{py3_shebang_flags}\\&#96; macro\\&gt;\\&gt; are not desirable,
packages \\&#42;SHOULD\\&#42; explicitly redefine the macro to remove
them by undefining the relevant \\&#96;%{*py3_shebang*&#8230;}+&#96;
macro.

Using &#96;+&#35;!%{python3}\\&#96;
(\\&#96;&#35;!/usr/bin/python3+&#96;) rather than
e.g. &#96;+&#35;!/usr/bin/env python+&#96; ensures that the system-wide
Python interpreter is used to run the code, even if the user modifies
&#96;+\$PATH+&#96; (e.g. by activating a virtual environment).

By default, &#96;+-%{py3_shebang_flags}\\&#96; expands to
\\&#96;-sP+&#96; (or just &#96;+-s+&#96; on Python version lower than
3.11 and Fedora Linux older than 37).

The &#96;+-s+&#96; flag, stored in &lt;&lt;\_py3_shebang_s,the
&#96;+%{*py3_shebang_s}\\&#96; macro\\&gt;\\&gt;, means \_don't add user
site directory to \\&#96;+sys.path&#96;.* That ensures the user's Python
packages (e.g. installed by &#96;+pip install \--user+&#96;, or just
placed in the current directory) don't interfere with the RPM installed
software. Sometimes, such content is desirable, such as with plugins.

The &#96;+-P+&#96; flag, stored in &lt;&lt;\_py3_shebang_P,the
&#96;+%{*py3_shebang_P}\\&#96; macro\\&gt;\\&gt;, means \_don't add the
script\'s directory to \\&#96;+sys.path&#96;.* Sometimes, adding the
script's directory to &#96;+sys.path+&#96; is desirable, such as with
executable Python scripts installed in a custom directory, importing
each other.

Removing the undesired flag(s) from &lt;&lt;py3_shebang_flags,the
&#96;+%{py3_shebang_flags}+&#96; macro&gt;&gt; rather than not using the
macro at all, ensures that existing or future automation won't add the
flag.

``` spec
\&#35; Remove -s from Python shebang - ensure that extensions installed with pip
\&#35; to user locations are seen and properly loaded
%undefine _py3_shebang_s
```

``` spec
\&#35; Don't add -P to Python shebangs
\&#35; The executable Python scripts in /usr/share/opt-viewer/ import each other
%undefine _py3_shebang_P
```

The &lt;&lt;pyproject_install,&#96;+%pyproject_install+&#96;
macro&gt;&gt; automatically changes all Python shebangs in
&#96;+%{buildroot}%{\_bindir}/&#42;+&#96; to use &#96;+%{python3}\\&#96;
and add contents of the
\\&lt;\\&lt;py3_shebang_flags,\\&#96;%{py3_shebang_flags}\\&#96;
macro\\&gt;\\&gt; to the existing flags. If you're not using that macro
or you need to change a shebang in a different directory, you can use
\\&lt;\\&lt;py3_shebang_fix,the \\&#96;%py3_shebang_fix+&#96;
macro&gt;&gt; as follows:

``` spec
%py3_shebang_fix SCRIPTNAME …
```

### Invokable Python modules {#_invokable_python_modules}

Every executable &#96;+TOOL+&#96; for which the current version of
Python matters &#42;SHOULD&#42; also be invokable by &#96;+python3 -m
TOOL+&#96;.

If the software doesn't provide this functionality, packagers
&#42;SHOULD&#42; ask the upstream to add it.

This applies to tools that modify the current Python environment (like
installing or querying packages), use Python for configuration, or use
Python to run plugins. It does not apply to tools like GIMP or Bash
which support plugins in multiple languages and/or have other means to
specify the interpreter.

For example, &#96;+pip+&#96; can be invoked as &#96;+python3 -m
pip+&#96;.

This allows users to accurately specify the Python version used to run
the software. This convention works across different environments that
might not always set &#96;+\$PATH+&#96; or install scripts consistently.

## Using Cython[]{#_packages_using_cython} {#_using_cython}

Tightening the [general Fedora
policy](what-can-be-packaged.adoc&#35;pregenerated-code), packages
&#42;MUST NOT&#42; use files pre-generated by Cython. These
&#42;MUST&#42; be deleted in &#96;+%prep+&#96; and regenerated during
the build.

As an exception, these sources &#42;MAY&#42; be used temporarily to
prevent build time circular dependencies by following the [bootstrapping
guidelines](index.adoc&#35;bootstrapping).

Generated files (the ones that must be deleted) have a generic
&#96;+.c+&#96; or &#96;+.cpp+&#96; extension. Cython source files (which
should stay) usually have the &#96;+.pyx+&#96; or &#96;+.pxd+&#96;
extension.

Cython is a popular tool for writing extension modules for Python. If
compiles a Python-like language to C, which is then fed to the C
compiler. Historically, Cython was hard to use upstream as a build-time
dependency. Many projects include pre-generated C files in source
distributions to avoid users from needing to install the tool.

Cython uses CPython's fast-changing internal API for performance
reasons. For a new release of Python, Cython generally needs to be
updated and the C files regenerated. In Fedora, this is frequently
needed before upstreams release re-generated sources (e.g. for Alpha
versins of Python). Since we do not have a problem with build-time
dependencies, we always want to run the Cython step.

For example, &#96;+PyYAML+&#96; removes a generated C file with:

``` spec
rm -rf ext/_yaml.c
```

For another example, in &#96;+python-lxml+&#96; all C files are
generated with Cython, which allows removing them with:

``` spec
\&#35; Remove pregenerated Cython C sources
find -type f -name '\&#42;.c' -print -delete
```

Some upstreams mix generated and hand-written C files. In such cases a
grep like this one from &#96;+scipy+&#96; helps (but might not be
entirely future proof):

``` spec
\&#35; Remove pregenerated Cython C sources
rm $(grep -rl '/\\&#42; Generated by Cython')
```

## Tests {#_tests}

### Running tests {#_running_tests}

If a test suite exists upstream, it &#42;SHOULD&#42; be run in the
&#96;+%check+&#96; section. If that is not possible with reasonable
effort, at least a basic smoke test (such as importing the packaged
module) &#42;MUST&#42; be run in &#96;+%check+&#96;.

You &#42;MAY&#42; exclude specific failing tests. You &#42;MUST NOT&#42;
disable the entire testsuite or ignore its result to solve a build
failure.

As an exception, you &#42;MAY&#42; disable tests with an appropriate
&#96;+%if+&#96; conditional (e.g.
[bcond](https://rpm-software-management.github.io/rpm/manual/conditionalbuilds.html))
when [bootstrapping](index.adoc&#35;bootstrapping).

Most errors in Python happen at run-time, so tests are extremely
important to root out issues, especially when mass rebuilds are
required.

Common reasons for skipping tests in &#96;+%check+&#96; include
requiring network access, dependencies not packaged in Fedora, and/or
specialized hardware or resources.

In these cases, you can use &lt;&lt;pyproject_check_import,the
&#96;+%pyproject_check_import+&#96;&gt;&gt; or
&lt;&lt;py3_check_import,the &#96;+%py3_check_import+&#96; macro&gt;&gt;
to test that installed modules are importable.

#### Tox {#_tox}

A popular testing tool, and one which is well integrated in Fedora, is
&#96;+tox+&#96;. Upstream, it is commonly used to test against multiple
Python versions. In a Fedora package, BuildRequire test dependencies via
&#96;+%pyproject_buildrequires -t+&#96; or &#96;+-e+&#96; (see *Test
dependencies* below) and run &#96;+tox+&#96; with:

``` spec
%tox
```

This sets up the environment (&#96;+\$PATH+&#96;,
&#96;+\$PYTHONPATH+&#96;, &#96;+\$TOX_TESTENV_PASSENV+&#96;) and
instructs &#96;+tox+&#96; to use the current environment rather than
create new ones. For more options, see &lt;&lt;Build macros&gt;&gt;.

#### pytest {#_pytest}

When upstream doesn't use &#96;+tox+&#96;, the tests need to be run
directly depending on upstream choice of a test runner. A popular runner
is &#96;+pytest+&#96;, which can be invoked using &#96;+%pytest+&#96;.

Use positional arguments to specify the test directory. See
&#96;+python3 -m pytest \--help+&#96; for how to select tests. For
example, if network-related tests are marked "network", you might use
&#96;+-m+&#96; to deselect them:

``` spec
%pytest -m 'not network'
```

The &#96;+%pytest+&#96; macro sets several environment variables
appropriate for &#96;+%check+&#96;:

&#42; Locations in the buildroot are added to &#96;+\$PATH+&#96; and
&#96;+\$PYTHONPATH+&#96;. &#42; &#96;+\$PYTHONDONTWRITEBYTECODE+&#96; is
set to avoid writing pytest-specific cache files to buildroot &#42;
&#96;+\$PYTEST_XDIST_AUTO_NUM_WORKERS+&#96; is set to
&#96;+%{\_smp_build_ncpus}\\&#96; \\&#42; If unset,
\\&#96;\$CFLAGS+&#96; and &#96;+\$LDFLAGS+&#96; are set to match the
build flags

#### Other test runners {#_other_test_runners}

If upstream doesn't use &#96;+tox+&#96; or &#96;+pytest+&#96;, other
test runners can be invoked with &lt;&lt;py3_test_envvars,the
&#96;+%{py3_test_envvars}+&#96;&gt;&gt; macro, available since Fedora
Linux 38.

This macro sets several environment variables similarly to
&#96;+%pytest+&#96;, but requires the actual test runner to be invoked
after the macro, for example:

``` spec
%{py3_test_envvars} %{python3} -m unittest
```

Or:

``` spec
%{py3_test_envvars} %{python3} tests/run_tests.py
```

### Test dependencies {#_test_dependencies_2}

One part of the Python packaging ecosystem that is still not
standardized is specifying test dependencies (and development
dependencies in general).

A good, common way for upstreams to specify test dependencies is using
an &lt;&lt;Extras,extra&gt;&gt; like &#96;+[\\&#96;,
\\&#96;]{.test}\[testing\]\\&#96; or \\&#96;\[dev\]\\&#96;. In this
case, upstream's instructions to install test dependencies might look
like \\&#96;\$ pip install -e.\[test\]+&#96;.

Another way to specify test dependencies is using a dedicated dependency
group ([PEP 735](https://www.python.org/dev/peps/pep-0735/)).

Projects using &#96;+tox+&#96; usually specify test dependencies in a
&#96;+tox+&#96;-specific format: a
[requires](https://tox.readthedocs.io/en/latest/config.html&#35;conf-requires)
key in the configuration.

These three forms are handled by the
&lt;&lt;pyproject_buildrequires,&#96;+%pyproject_buildrequires+&#96;
macro&gt;&gt;.

If upstream does not use either form, list test dependencies as manual
*BuildRequires* in the &#96;+spec+&#96; file, for example:

``` spec
\&#35; Test dependencies:
BuildRequires: python3dist(pytest)
```

If you need to do this, consider asking upstream to add a
&#96;+\[test\]+&#96; extra or a &#96;test&#96; dependency group.

### Linters {#_linters}

In &#96;+%check+&#96;, packages &#42;SHOULD NOT&#42; run "linters": code
style checkers, test coverage checkers and other tools that check code
quality rather than functionality.

Tools like &#96;+black+&#96;, &#96;+pylint+&#96;, &#96;+flake8+&#96;, or
&#96;+mypy+&#96; are often "opinionated" and their "opinions" change
frequently enough that they are nuisance in Fedora, where the linter is
not pinned to an exact version. Furthermore, some of these tools take a
long time to adapt to new Python versions, preventing early testing with
Alpha and Beta releases of Python. And they are just not needed: wrongly
formatted code is not important enough for the Fedora packager to bug
the upstream about it. Making such an issue break a package build is
entirely unreasonable.

Linters *do* make sense in upstream CI. But not in Fedora.

If a linter is used, disable it and remove the dependency on it. If that
is not easy, talk to upstream about making it easy (for example with a
configuration option or a separate &#96;+tox+&#96; environment).

For packages that contain such linters, use them at runtime or extend
them, you will usually need to run the linter in &#96;+%check+&#96;. Run
it to test functionality, not code quality of the packaged software.

## Source files from PyPI {#_source_files_from_pypi}

Packages &#42;MAY&#42; use sources from PyPI.

However, packages &#42;SHOULD NOT&#42; use an archive that omits test
suites, licenses and/or documentation present in other source archives.

For example, as of this writing &#96;+pip+&#96; provides a [source
tarball ("sdist")](https://pypi.org/project/pip/&#35;files) which omits
the relatively large &#96;+tests+&#96; and &#96;+docs+&#96; directories
present in [the source on GitHub](https://github.com/pypa/pip). In this
case, the tarball from GitHub should be used. (See the [Git
tags](SourceURL&.xml#35;_git_tags) section of Fedora SourceURL
guidelines.)

When using sources from PyPI, you can use the &lt;&lt;pypi_source,the
&#96;+%pypi_source+&#96; macro&gt;&gt; to generate the proper URL.

:::: {#_version_warning .warning}
::: title
:::

Some Python packages use metadata from &#96;git&#96; (or a similar
version control system) to construct their version string, for example
via [setuptools_scm](https://pypi.org/project/setuptools-scm/). When
publishing a package to PyPI, this version metadata is usually stored
and included in a file, so the version control history is no longer
needed to construct it. However, when using tarballs from a git forge
directly, this version information is missing and must be manually
provided by the packager. For example, the
&#96;SETUPTOOLS_SCM_PRETEND_VERSION&#96; environment variable can be set
to the desired value in the &#96;+%generate_buildrequires+&#96; and
&#96;+%build+&#96; scripts in the spec file for packages that use
&#96;setuptools_scm&#96; for this purpose.
::::

## Example spec file[]{#_example_python_spec_file} {#_example_spec_file_2}

The following is a viable spec file for a Python library called
&#96;+Pello+&#96; that follows packaging best practices.

Note that the project name &#96;+Pello+&#96; &lt;&lt;Canonical project
name,normalizes&gt;&gt; to the lowercase &#96;+pello+&#96;. The example
spec shows where each variant is typically used.

The project has an &lt;&lt;Extras,extra&gt;&gt; &#96;+color+&#96;, which
enables colorized output when installed. Since the required dependency
is quite minimal and color improves the user experience, the extra is
Recommended from the main package.

``` spec
Name:           python-pello
Version:        1.0.4
Release:        1%{?dist}
Summary:        Example Python library

License:        MIT-0
URL:            https://github.com/fedora-python/Pello
Source:         %{url}/archive/v%{version}/Pello-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
A python module which provides a convenient example.
This description provides some details.}

%description %_description

%package -n python3-pello
Summary:        %{summary}
Recommends:     python3-pello+color

%description -n python3-pello %_description


%pyproject_extras_subpkg -n python3-pello color

%prep
%autosetup -p1 -n Pello-%{version}


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install

\&#35; Here, 'pello' is the name of the importable module.
%pyproject_save_files -l pello


%check
%tox


\&#35; Note that there is no %%files section for
\&#35; the unversioned python module, python-pello.

\&#35; For python3-pello, %%{pyproject_files} handles code files and %%license,
\&#35; but executables and documentation must be listed in the spec file:

%files -n python3-pello -f %{pyproject_files}
%doc README.md
%{_bindir}/pello_greeting


%changelog
```

## Empty spec file {#_empty_spec_file}

The following is an unfinished spec file template to copy, paste and
edit.

``` spec
Name:           python-\&#8230;
Version:        \&#8230;
Release:        0%{?dist}
Summary:        \&#8230;

License:        \&#8230;
URL:            https://\&#8230;
Source:         %{url}/archive/v%{version}/\&#8230;-%{version}.tar.gz / %{pypi_source \&#8230;}

BuildArch:      noarch / BuildRequires:  gcc
BuildRequires:  python3-devel

%global _description %{expand:
\&#8230;}

%description %_description

%package -n python3-\&#8230;
Summary:        %{summary}

%description -n python3-\&#8230; %_description


%prep
%autosetup -p1 -n \&#8230;-%{version}


%generate_buildrequires
%pyproject_buildrequires -x\&#8230; / -g\&#8230; / -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files \&#8230;


%check
%tox / %pytest / %pyproject_check_import \&#8230;


%files -n python3-\&#8230; -f %{pyproject_files}
%doc README.\&#42;
%{_bindir}/\&#8230;


%changelog
```

## Macro Reference[]{#_macros} {#_macro_reference}

This section documents macros that are available to help with Python
packaging. The expansions in parentheses are provided only as
reference/examples.

See the &lt;&lt;Mandatory macros&gt;&gt; section above for:

&#42; &#96;+%{python3}\\&#96; (\\&#96;/usr/bin/python3+&#96;) &#42;
&#96;+%{python3_version}\\&#96; (e.g. \\&#96;+3.9&#96;) &#42;
&#96;+%{python3_version_nodots}\\&#96; (e.g. \\&#96;+39&#96;) &#42;
&#96;+%{python3_sitelib}\\&#96;
(e.g. \\&#96;/usr/lib/python3.9/site-packages+&#96;) &#42;
&#96;+%{python3_sitearch}\\&#96;
(e.g. \\&#96;/usr/lib64/python3.9/site-packages+&#96;)

### Shebang macros {#_shebang_macros}

\[&#35;py3_shebang_flags\] &#42; &#96;+%{py3_shebang_flags}\\&#96;
(\\&#96;+sP&#96; or &#96;+s+&#96; before Fedora Linux 37)

\+ Flags for &#96;+%{python3}\\&#96; to use in shebangs. See
\\&lt;\\&lt;Shebangs\\&gt;\\&gt; for details. Includes flags from
several \\&#96;%{*py3_shebang*&#8230;}+&#96; macros listed here.

\[&#35;\_py3_shebang_s\] &#42; &#96;+%{\_py3_shebang_s}\\&#96;
(\\&#96;+s&#96;)

\+ Undefine this macro to drop &#96;+s+&#96; from
&#96;+%{py3_shebang_flags}+&#96;.

\[&#35;\_py3_shebang_P\] &#42; &#96;+%{\_py3_shebang_P}\\&#96;
(\\&#96;+P&#96;)

\+ Undefine this macro to drop &#96;+P+&#96; from
&#96;+%{py3_shebang_flags}+&#96;. Introduced in Fedora Linux 37.

\[&#35;py3_shebang_fix\] &#42; &#96;+%py3_shebang_fix PATHS+&#96;
(&#96;+pathfix.py &#8230; PATHS+&#96;)

\+ A macro to fix shebangs in specified &#96;+PATHS+&#96;. Only shebangs
that already have &#96;+python+&#96; in them are changed. If a directory
is given, all &#96;+.py+&#96; files in it are fixed, recursively. (So,
if you need to fix shebangs in files not named &#96;+&#42;.py+&#96;, you
need to list each file separately or use a Shell glob, such as
&#96;+%{buildroot}%{\_libexecdir}/mytool/&#42;+&#96;.) Existing flags
are preserved and &#96;+%{py3_shebang_flags}+&#96; are added.

\+ For example, &#96;+&#35;! /usr/bin/env python+&#96; will be changed
to &#96;+&#35;! /usr/bin/python3 -s+&#96; and &#96;+&#35;!
/usr/bin/python -u+&#96; will be changed to &#96;+&#35;!
/usr/bin/python3 -su+&#96;.

\+ This macro is called automatically by &#96;+%pyproject_install+&#96;
on &#96;+%{buildroot}%{\_bindir}/&#42;+&#96;.

### Convenience macros {#_convenience_macros}

\[&#35;pypi_source\] &#42; &#96;+%{pypi_source PROJECTNAME \[VERSION
\[EXT\]\]}\\&#96;
(e.g. \\&#96;+https://\\&#8230;/Django-3.0.5.tar.gz&#96;)

\+ Evaluates to the appropriate URL for source archive hosted on PyPI.
Accepts the project name and up to two optional arguments:

\+

&#42;&#42; The version of the PyPI project. Defaults to
&#96;+%version+&#96; (the package version) with any &#96;+\~\\&#96;
removed. \\&#42;\\&#42; The file extension to use. Defaults to
\\&#96;+tar.gz&#96;.

\+ In most cases it is not necessary to specify those two arguments.

\+ For backward compatibility, the first argument is technically
optional as well, but omitting it is deprecated. (It defaults to
&#96;+%srcname+&#96; if defined, or to &#96;+%pypi_name+&#96; if
defined, or to &#96;+%name+&#96;.)

\[&#35;python3_platform\] &#42; &#96;+%{python3_platform}\\&#96;
(e.g. \\&#96;+linux-x86_64&#96;)

\+ The platform name. Used in some Python build systems. This
corresponds to
[&#96;+sysconfig.get_platform()+&#96;](https://docs.python.org/3/library/sysconfig.html&#35;sysconfig.get_platform).

\[&#35;python3_ext_suffix\] &#42; &#96;+%{python3_ext_suffix}\\&#96;
(e.g. \\&#96;.cpython-39-x86_64-linux-gnu.so+&#96;)

\+ Filename extension for Python extension modules. This corresponds to
the &#96;+EXT_SUFFIX+&#96;
[sysconfig](https://docs.python.org/3/library/sysconfig.html) variable.

\[&#35;python3_platform_triplet\] &#42;
&#96;+%{python3_platform_triplet}\\&#96;
(e.g. \\&#96;+x86_64-linux-gnu&#96;)

\+ A string identifying the architecture/platform. This corresponds to
the &#96;+MULTIARCH+&#96;
[sysconfig](https://docs.python.org/3/library/sysconfig.html) variable.

\[&#35;python3_cache_tag\] &#42; &#96;+%{python3_cache_tag}\\&#96;
(e.g. \\&#96;+cpython-311&#96;)

\+ Part of the bytecode cache filename that identifies the interpreter.
This corresponds to the
[&#96;+sys.implementation.cache_tag+&#96;](https://docs.python.org/3/library/sys.html&#35;sys.implementation)
value.

### Build macros {#_build_macros}

The "pyproject macros" are most useful for packaging Python projects
that use the &#96;+pyproject.toml+&#96; file defined in [PEP
518](https://www.python.org/dev/peps/pep-0518/) and [PEP
517](https://www.python.org/dev/peps/pep-0517/), which specifies the
package's build dependencies (including the build system, such as
&#96;+setuptools+&#96;, &#96;+flit+&#96; or &#96;+poetry+&#96;).

If &#96;+pyproject.toml+&#96; is not found, the macros automatically
fall backs to using &#96;+setuptools+&#96; with configuration in
&#96;+setup.cfg+&#96;/&#96;+setup.py+&#96;.

A full tutorial and discussion for the macros is available in the
macros'
[README](https://src.fedoraproject.org/rpms/pyproject-rpm-macros/).

\[&#35;pyproject_buildrequires\] &#42;
&#96;+%pyproject_buildrequires+&#96;

\+ Generate BuildRequires for the package. Used in the
&#96;+%generate_buildrequires+&#96; section of the &#96;+spec+&#96;
file. The macro has these options:

\+ &#42;&#42; &#96;+-R+&#96;: Don't include run-time requirements (e.g.
if the build backend does not support this). &#42;&#42; &#96;+-r+&#96;:
Include run-time requirements (this flag is not needed and exists for
backward-compatibility reasons only, run-time requirements are included
by default). &#42;&#42; &#96;+-x EXTRA+&#96;: Include dependencies given
by the given &lt;&lt;Extras,extra&gt;&gt;. Cannot be used with
&#96;+-R+&#96;. &#42;&#42; &#96;+-g GROUP+&#96;: Include dependencies
specified in the given dependency group ([PEP
735](https://www.python.org/dev/peps/pep-0735/)). &#42;&#42;
&#96;+-p+&#96;: Read run-time dependencies from pyproject.toml
\[project\] table. This reads also the \[optional-dependencies\] for the
given &lt;&lt;Extras,extra&gt;&gt;. Cannot be used with &#96;+-R+&#96;.
&#42;&#42; &#96;+-t+&#96;: Include dependencies for the default *tox*
environment. Cannot be used with &#96;+-R+&#96;. &#42;&#42; &#96;+-e
ENV+&#96;: Include dependencies for the given *tox* environment, and
save the &#96;+ENV+&#96; name as &#96;+%{toxenv}\\&#96;. Cannot be used
with \\&#96;-R+&#96;. Multiple comma separated values can be given, for
example:

\+

``` spec
%pyproject_buildrequires -e %{toxenv}-unit,%{toxenv}-integration
```

&#42;&#42; Additional arguments are treated as paths to
&#96;+requirements.txt+&#96; that are added on top of these dependencies

\[&#35;pyproject_wheel\] &#42; &#96;+%pyproject_wheel+&#96;

\+ Build the package. Commonly, this is the only macro needed in the
&#96;+%build+&#96; section.

\+ This macro needs BuildRequires generated by
&#96;+%pyproject_buildrequires+&#96;.

\[&#35;pyproject_install\] &#42; &#96;+%pyproject_install+&#96;

\+ Install the package built by &#96;+%pyproject_wheel+&#96;. Calls
&#96;+%py3_shebang_fix %{\_buildroot}%{\_bindir}/&#42;+&#96;.

\+ This macro needs BuildRequires generated by
&#96;+%pyproject_buildrequires+&#96;.

\[&#35;pyproject_save_files\] &#42; &#96;+%pyproject_save_files MODNAME
...+&#96;

\+ Generate a list of files corresponding to the given importable
module(s) and save it as &#96;+%{pyproject_files}+&#96;.

\+ Note that README file is not included. The LICENSE file is included
when it is specified in the metadata. Also, while the macro allows
including executable and other files (using the &#96;+auto&#96; flag),
this feature &#42;MUST NOT&#42; be used in Fedora.

\+ The &#96;+MODNAME+&#96; may be a glob pattern, which should be
specific to your package. To prevent Shell from expanding the globs, put
them in &#96;+\'\'\\&#96;, e.g. \\&#96;%pyproject_save_files
\'&#42;pytest\'\\&#96;. As mentioned in the \\&lt;\\&lt;Explicit
lists\\&gt;\\&gt; section, expressions like \\&#96;%pyproject_save_files
\'&#42;\'+&#96; are not acceptable.

\+ The macro has these options:

\+ &#42;&#42; &#96;+-l+&#96;: Declare that a missing license should
terminate the build. Packagers are encouraged to use this flag when the
&#96;%license file&#96; is not manually listed in &#96;%files&#96; to
avoid accidentally losing the file in a future version. &#42;&#42;
&#96;+-L+&#96;: Explicitly disable the check for a missing license file.
When the &#96;%license&#96; file is manually listed in &#96;%files&#96;,
packagers can use this flag to ensure future compatibility in case the
&#96;-l&#96; behavior eventually becomes a default. &#42;&#42;
&#96;+-M+&#96;: Do not list any modules. When the package has no Python
modules in it or when you need to list the modules in &#96;+%files+&#96;
manually, this option allows to save just the non-module files (such as
the &#96;+.dist-info+&#96; metadata directory). This option cannot be
combined with &#96;MODNAME&#96;s.

\[&#35;pyproject_files\] &#42; &#96;+%{pyproject_files}+&#96;

\+ Path of the file written by &#96;+%pyproject_save_files+&#96;, to be
used as:

\+

``` spec
%files -n python3-DISTNAME -f %{pyproject_files}
```

### Test macros {#_test_macros}

\[&#35;tox\] &#42; &#96;+%tox+&#96;

\+ Run tests using &#96;+tox+&#96;.

\+ This macro needs BuildRequires generated by the &#96;+-t+&#96; or
&#96;+-e+&#96; option of &lt;&lt;pyproject_buildrequires,the
&#96;+%pyproject_buildrequires+&#96; macro&gt;&gt;.

\+ Different environments may be specified with &#96;+-e+&#96;, for
example:

\+

``` spec
%check
%tox %{?with_integration_tests:-e %{toxenv},%{toxenv}-integration}
```

\+ Flags for the &#96;+tox+&#96; command can be specified after
&#96;+\--+&#96;:

\+

``` spec
%tox -- --parallel 0
```

\+ Additional arguments for the test runner may be specified after
another &#96;+\--+&#96;:

\+

``` spec
%tox -- --parallel 0 -- --verbose tests/\&#42;
```

\[&#35;toxenv\] &#42; &#96;+%{toxenv}+&#96;

\+ The *tox* environment(s) used by the &#96;+%tox+&#96; macro. Multiple
environments are separated by commas. Can be overridden manually or with
&#96;+%pyproject_buildrequires -t ENV1,ENV2+&#96;.

\[&#35;default_toxenv\] &#42; &#96;+%{default_toxenv}\\&#96;
(e.g. \\&#96;+py39&#96;)

\+ The system-wide default value of &#96;+%{toxenv}+&#96;.

\[&#35;pytest\] &#42; &#96;+%pytest+&#96;

\+ Run &#96;+%\_\_pytest+&#96; with environment variables appropriate
for tests in &#96;%check&#96;. See &lt;&lt;Running tests&gt;&gt; for
details.

\[&#35;*pytest\] &#42; &#96;+%*pytest+&#96;
(&#96;+/usr/bin/pytest+&#96;)

\+ The command that &#96;+%pytest+&#96; uses. May be redefined.

\[&#35;py3_test_envvars\] &#42; &#96;+%py3_test_envvars+&#96;
(&#96;+PATH=&#8230; PYTHONPATH=&#8230; PYTHONDONTWRITEBYTECODE=1
&#8230;+&#96;)

\+ The environment variables used by &#96;+%pytest+&#96; and
&#96;+%tox+&#96;. It may be used to invoke custom test runners in
&#96;+%check+&#96;. See &lt;&lt;Other test runners&gt;&gt; for details.
Introduced in Fedora Linux 38.

\[&#35;py3_check_import\] &#42; &#96;+%py3_check_import+&#96;

\+ Imports all provided modules. If running an upstream test suite is
not feasible, use this macro in &#96;+%check+&#96; to test that public
Python modules are importable.

\+ Takes these arguments:

\+

&#42;&#42; &#96;+-f+&#96;: path to file containing qualified module
names (separated by newlines). Optional, can be used multiple times.
&#42;&#42; &#96;+-e+&#96;: glob to exclude the matching module names.
Optional, can be used multiple times. &#42;&#42; &#96;+-t+&#96;: if set,
import only top-level module names &#42;&#42; Positional arguments
(separated by spaces or commas) specify the module name(s) to check.

\+ The macro sets various environment variables such as &#96;+PATH+&#96;
and &#96;+PYTHONPATH+&#96; to ensure the packaged versions of modules
are imported.

\[&#35;pyproject_check_import\] &#42;
&#96;+%pyproject_check_import+&#96;

\+ Imports all public modules found by &lt;&lt;pyproject_save_files,the
&#96;+%pyproject_save_files+&#96; macro&gt;&gt; whose names match any of
the provided &#96;+MODNAME+&#96; globs.

\+ This macro needs to be used with &#96;+%pyproject_save_files+&#96;
(use &#96;+%py3_check_import+&#96; in other cases).

\+ The macro takes &#96;+-e+&#96;/&#96;+-t+&#96; as well as positional
arguments for &#96;+%py3_check_import+&#96; above.

### Extras macros {#_extras_macros}

\[&#35;pyproject_extras_subpkg\] &#42;
&#96;+%pyproject_extras_subpkg+&#96;

\+ Generates a simple subpackage for a Python extra. See
&lt;&lt;Extras&gt;&gt; for more information.

\+ This macro needs to be used with &#96;+%pyproject_install+&#96; (use
&#96;+%python_extras_subpkg+&#96; in other cases).

\+ Required arguments:

\+

&#42;&#42; &#96;+-n+&#96;: name of the "base" package
(e.g. &#96;+python3-requests+&#96;) &#42;&#42; Positional arguments
(separated by spaces or commas): the extra name(s). Multiple
metapackages are generated when multiple names are provided.

\+ The macro also takes &#96;+-i+&#96;/&#96;+-f+&#96;/&#96;+-F+&#96;
arguments for &#96;+%python_extras_subpkg+&#96; below, but if they are
not given, a filelist written by &#96;+%pyproject_install+&#96; is used.

\+ Similarly, the &#96;+-a+&#96;/&#96;+-A+&#96; flags are passed to
&#96;+%python_extras_subpkg+&#96;.

\+ This macro generates all the subpackage definition sections
(&#96;+%package+&#96; including the &#96;+Summary+&#96; and
&#96;+Requires+&#96; on the base package, &#96;+%description+&#96; and,
by default, &#96;+%files+&#96;). Hence, it cannot be extended with
custom *Provides*/*Obsoletes*/*Requires*/etc. This macro is designed to
fit only the most common uses. For more complicated uses, construct the
subpackage manually as shown in the &lt;&lt;Extras&gt;&gt; section.

\+ The &#96;+%files+&#96; section is last. It can be continued to add
files that only make sense with the extra and the base package does not
fail without them. For example, the following macro will package the
extra &#96;+cli+&#96; for the project &#96;+a-cool-tool+&#96; and
include an &#96;+a-cool-tool+&#96; command:

\+

``` spec
%pyproject_extras_subpkg -n a-cool-tool cli
%{_bindir}/a-cool-tool
```

\+ Due to technical limitations, the macro never generates requirements
on the arched &#96;+BASE_PACKAGE%{?\_isa} =
%{?epoch:%{epoch}:}%{version}-%{release}\\&#96;. It only adds
\\&#96;+Requires: BASE_PACKAGE =
%{?epoch:%{epoch}:}%{version}-%{release})&#96; because a macro cannot
reliably detect if the subpackage is arched or not. So far, this has not
been a problem in practice.

\[&#35;python_extras_subpkg\] &#42; &#96;+%python_extras_subpkg+&#96;

\+ Generates a simple subpackage for a Python extra. See
&lt;&lt;Extras&gt;&gt; for more information. Takes these arguments:

\+

&#42;&#42; &#96;+-n+&#96;: name of the "base" package
(e.g. &#96;+python3-requests+&#96;) &#42;&#42; &#96;+-i+&#96;: the
&#96;+%files %ghost+&#96; path (glob) to the &#96;+.dist-info+&#96;
directory &#42;&#42; Positional arguments (separated by spaces or
commas) specify the extra name(s) --- multiple metapackages are
generated when multiple names are provided. &#42;&#42; &#96;+-f+&#96;:
Relative path to the filelist for this metapackage (which should contain
the &#96;+%files %ghost+&#96; path (glob) to the the metadata
directory). Conflicts with &#96;+-i+&#96; and &#96;+-F+&#96;. &#42;&#42;
&#96;+-F+&#96;: Skip the %files section entirely (if the packager wants
to construct it manually). Conflicts with &#96;+-i+&#96; and
&#96;+-f+&#96;. &#42;&#42; &#96;+-a+&#96;: Include &#96;+BuildArch:
noarch+&#96; in the package definition, to be used only when the package
is archful, but the "base" package passed to &#96;+-n+&#96; is not.
&#42;&#42; &#96;+-A+&#96;: Explicitly disables &#96;+-a+&#96; (does
nothing at the moment).

\+ As with &#96;+%pyproject_extras_subpkg+&#96;:

\+ &#42;&#42; This macro generates all the subpackage definition
sections, with only &#96;+%files+&#96; being customizable. For more
complicated uses, construct the subpackage manually as shown in the
&lt;&lt;Extras&gt;&gt; section. &#42;&#42; It never generates
requirements on the arched &#96;+BASE_PACKAGE%{?\_isa} =
%{?epoch:%{epoch}:}%{version}-%{release}+&#96;.

### Manual generation {#_manual_generation}

The following macros are available for cases where automatic generation
is turned off. They can also be useful for handling files in
non-standard locations where the generators don't look.

\[&#35;pycached\] &#42; &#96;+%pycached MODNAME.py+&#96;

\+ Given a Python file, lists the file and the files with its bytecode
cache. See *Source files and bytecode cache* for more information.

\[&#35;py_provides\] &#42; &#96;+%py_provides python3-MODNAME+&#96;

\+ Generates &#96;+Provides+&#96; for &#96;+python3-MODNAME+&#96;,
&#96;+python3.X-MODNAME+&#96; and &#96;+python-MODNAME+&#96;. See
&lt;&lt;Automatic-unversioned-provides&gt;&gt; for more details.

\[&#35;py_byte_compile\] &#42; &#96;+%py_byte_compile INTERPRETER
PATH+&#96;

\+ Byte-compile a Python file into a &#96;+*pycache*/&#42;.pyc+&#96;.

\+ If the &#96;+PATH+&#96; argument is a directory, the macro will
recursively byte compile all &#96;+&#42;.py+&#96; files in the
directory. (So, if you need to compile files not named
&#96;+&#42;.py+&#96;, you need to use the macro on each file
separately.)

\+ The &#96;+INTERPRETER+&#96; determines the compiled file name's
suffix and the magic number embedded in the file. These muct match the
interpreter that will import the file. Usually, the
&#96;+INTERPRETER+&#96; should be set to &#96;+%{python3}\\&#96;. If you
are compiling for a non-default interpreter, use that interpreter
instead and add a \\&#96;+BuildRequires&#96; line for it.

\[&#35;py_dist_name\] &#42; &#96;+%{py_dist_name PROJECTNAME}+&#96;

\+ Given a *project name* (e.g. &#96;+PyYAML+&#96;) it will convert it
to the canonical format (e.g. &#96;+pyyaml+&#96;). See &lt;&lt;Canonical
project name&gt;&gt; for more information.

\[&#35;py3_dist\] &#42; &#96;+%{py3_dist PROJECTNAME ...}+&#96;

\+ Given one or more *project names*, it will convert them to the
canonical format and evaluate to &#96;+python3dist(DISTNAME)+&#96;,
which is useful when listing dependencies. See
&lt;&lt;Machine-readable-provides&gt;&gt; for more information.

### System Settings {#_system_settings}

The following macros can be redefined for special use cases.

\[&#35;*python\] &#42; &#96;+%{*python}+&#96; (errors by default if not
redefined)

\+ Defining this macro sets the meaning of all "unversioned" Python
macros such as &#96;+%{python}\\&#96; or
\\&#96;%{python_sitelib}\\&#96;. Don't use these macros without
redefining \\&#96;%{\_\_python}+&#96;.

\[&#35;*python3\] &#42; &#96;+%{*python3}\\&#96;
(\\&#96;/usr/bin/python3+&#96;)

\+ The python 3 interpreter. Redefining this macro changes all the
&#96;+%{python3&#8230;}\\&#96; macros, e.g. \\&#96;%{python3}\\&#96; or
\\&#96;%{python3_sitelib}+&#96;.

\[&#35;python3_pkgversion\] &#42; &#96;+%{python3_pkgversion}\\&#96;
(\\&#96;+3&#96;)

\+ Distro-wide Python version, i.e. the &#96;+3+&#96; in
&#96;+python3+&#96;. Projects that build on top of Fedora might define
it to e.g. &#96;+3.9+&#96; to try allowing multiple Python stacks
installable in parallel. Packages in Fedora &#42;MAY&#42; use it
(e.g. in package names:
&#96;+python%{python3_pkgversion}-requests+&#96;), but &#42;MUST
NOT&#42; redefine it.

### Comparing Python versions {#_comparing_python_versions}

When comparing Python versions (e.g. to ask: is
&#96;+%{python3_version}\\&#96; greater than 3.8?), using naïve
\\&#96;%if %{python3_version} &gt; 3.8+&#96; or &#96;+%if
\'%{python3_version}\' &gt; \'3.8\'\\&#96; is not possible, because the
comparison is performed alphabetically on strings. Hence it is true that
\\&#96;\'3.10\' &lt; \'3.8\'+&#96; (which is not desired).

It is possible to explicitly compare version literals by using the
&#96;+v+&#96; prefix, similar to the Python string prefixes:

``` spec
%if v'0%{?python3_version}' \&gt; v'3.8'
\&#8230;
%endif
```

:::: note
::: title
:::

As a workaround for compatibility with RPM releases up to 4.16 (EPEL 9),
&#96;+%{python3_version_nodots}+&#96; can be compared as an integers:

``` spec
%if 0%{?python3_version_nodots} \&gt; 39
\&#8230;
%endif
```

This will work with Python 3.10 (310 &gt; 39), but eventually break with
Python 4.0 (40 &lt; 310).
::::

### Disabling automation {#_disabling_automation}

The following macros can turn off Python-specific automation.

Consider contacting the Python SIG if you need to do this.

\[&#35;python_disable_dependency_generator\] &#42;
&#96;+%{?python_disable_dependency_generator}+&#96;

\+ Disables the automatic dependency generator. See
&lt;&lt;Automatically-generated-dependencies&gt;&gt; for details.

\[&#35;*pythonname_provides\] &#42; &#96;+%undefine*
pythonname_provides+&#96;

\+ Disables automatic generation of unversioned/versioned provides for
package names, e.g. &#96;+python-FOO+&#96; and &#96;+python3.9-FOO+&#96;
for &#96;+python3-foo+&#96;. See
&lt;&lt;Automatic-unversioned-provides&gt;&gt; for more details.

\[&#35;*pythondist_provides\] &#42; &#96;+%undefine*
pythondist_provides+&#96;

\+ Disables automatic generation of machine-readable Provides,
e.g. &#96;+python3dist(foo)+&#96;. See
&lt;&lt;Machine-readable-provides&gt;&gt; for more details.

\[&#35;\_python_no_extras_requires\] &#42; &#96;+%global
\_python_no_extras_requires 1+&#96;

\+ If defined, &lt;&lt;Automatic Requires for extras&gt;&gt; will not be
generated.

\[&#35;\_python_dist_allow_version_zero\] &#42; &#96;+%global
\_python_dist_allow_version_zero 1+&#96;

\+ From Fedora Linux 38 on, it is no longer possible to build a Python
package with version 0 to prevent &lt;&lt;\_version_warning,an
accidental loss of the actual version information&gt;&gt;. If defined,
the macro will allow to build such package.

### Deprecated Macros {#_deprecated_macros}

The following macros are deprecated. See the [201x-era Python Packaging
guidelines](Python_201x.xml) for how some of them were used.

&#42; []{#py3_build} &#96;+%py3_build+&#96; &#42; []{#py3_build_wheel}
&#96;+%py3_build_wheel+&#96; &#42; []{#py3_build_egg}
&#96;+%py3_build_egg+&#96; &#42; []{#py3_install}
&#96;+%py3_install+&#96; &#42; []{#py3_install_wheel}
&#96;+%py3_install_wheel+&#96; &#42; []{#py3_install_egg}
&#96;+%py3_install_egg+&#96; &#42; []{#py3dir} &#96;+%py3dir+&#96; &#42;
[]{#py3_other_build} &#96;+%py3_other_build+&#96; &#42;
[]{#py3_other_install} &#96;+%py3_other_install+&#96; &#42;
[]{#python_provide} &#96;+%python_provide+&#96;

# Python Packaging Guidelines (201x-era) {#_python_packaging_guidelines_201x_era}

:::: important
::: title
:::

These guidelines were replaced by [a newer version](Python.xml).

They exist as a historical reference for packages that don't follow the
new guidelines yet.
::::

## Python Version Support {#_python_version_support_2}

In Fedora we have multiple Python runtimes, one for each supported major
Python release. At this point that's one for python3.x and one for
python2.7. However the Python 2 stack will be removed from Fedora and is
[deprecated](deprecating-packages.xml). Upstream support for the python2
interpreter officially ends in 2020. If a piece of software supports
python3, it MUST be packaged for python3. Software using python2 MUST
NOT be newly packaged into Fedora without FESCo exception.

For guidelines on maintaining already existing python2 packages, see the
[appendix](Python_Appendix.xml).

## Multiple Python Runtimes {#_multiple_python_runtimes}

On Fedora &#96;/usr/bin/python&#96; is, if it is installed, a symbolic
link to &#96;/usr/bin/python3&#96;. It was a symbolic link to
&#96;/usr/bin/python2&#96; on previous releases.

Packages in Fedora MUST NOT use &#96;/usr/bin/python&#96;. Instead
packages for Python 3 MUST use &#96;/usr/bin/python3&#96; (even if
upstream supports both Python 2 and 3). As a result of that
&#96;/usr/bin/python&#96; (as well as &#96;/usr/bin/env python&#96; and
similar) MUST NOT be used in shebang lines or as a dependency of a
package. All uses of unversioned python executables in shebang lines
will fail the build. These shebangs MUST be fixed (for example by using
the &#96;+%py3_shebang_fix+&#96; macro in the spec file). If it is
necessary to disable the checks, please see the information in [Shebang
lines](index&.xml#35;_shebang_lines).

All Python runtimes have a virtual provide for &#96;+python(abi) =
\$MAJOR.\$MINOR+&#96;. For example, the Python 3.7 runtime package has:

&#8230;. \$ rpm -q \--provides python3 \| grep abi python(abi) = 3.7
&#8230;.

Python modules using these runtimes should have a corresponding
\'Requires\' line on the Python runtime that they are used with. This is
done automatically for files below
&#96;+/usr/lib\[\^/\]&#42;/python\${PYVER}+&#96;

Mirroring the policy for regular packages, the Python-version-specific
subpackages of your package MUST NOT be removed in a release branch of
Fedora.

## Naming {#_naming_8}

The source package for a Python library MUST be named with the
&#96;python-&#96; prefix. A built package however must include the
Python major version in the name, using the &#96;python3-&#96; prefix.
This is accomplished by adding a subpackage. See example below.

This rule does not apply to applications.

The character &#96;+&#96; in names of built packages (i.e. non-SRPM)
that include &#96;.dist-info&#96; or &#96;.egg-info&#96; directories is
reserved for &lt;&lt;Python Extras&gt;&gt; and MUST NOT be used for any
other purpose. The &#96;+&#96; character triggers the automatic
dependency generator for extras. Replace any &#96;+&#96; signs in the
upstream name with &#96;-&#96;, or omit them when at the beginning of
the name. As an exception, &#96;+&#96; characters are permitted at the
*end* of the name.

## Dependencies {#_dependencies_4}

Packages building for Python 3 will need &#96;BuildRequires:
python3-devel&#96;. Most of them will also need &#96;BuildRequires:
python3-setuptools&#96;. When in doubt, inspect the &#96;setup.py&#96;
file for &#96;setuptools&#96; import.

Packages MUST NOT have dependencies (either build-time or runtime) on
packages named with the unversioned &#96;python-&#96; prefix.
Dependencies on Python packages instead MUST use names beginning with
&#96;python3-&#96;.

### Automatically generated dependencies {#_automatically_generated_dependencies}

Packages MAY use the automatic Python dependency generator. This
generator uses upstream egg/dist metadata (such as [setuptool's
install_requires](https://python-packaging.readthedocs.io/en/latest/dependencies.html))
to determine what the package should depend on. The generator parses the
installed metadata from
&#96;+/usr/lib(64)?/pythonX.Y/site-packages/[+]{.^/}.(egg\|dist)-info/requires.txt+&#96;,
so it will not work with software that uses plain
[distutils](https://docs.python.org/3/distutils/).

This generates run time requires in the form of
&#96;+pythonX.Ydist(foo)\\&#96;. If the generated dependencies are not
accurate, additional ones can still be added manually. To remove some, a
packager MAY modify upstream-provided metadata (usually specified in the
\\&#96;setup.py\\&#96; file) in the \\&#96;%prep+&#96; section of the
specfile or fall back to
[filtering](AutoProvidesAndRequiresFiltering.xml) those dependencies.

The packager MUST inspect the generated requires for correctness. All
dependencies MUST be resolvable within the targeted Fedora version.

As an example, the upstream notebook package has (as of version 5.6.0):

``` python
install_requires = [
'jinja2',
'tornado\&gt;=4',
'pyzmq\&gt;=17',
'ipython_genutils',
'traitlets\&gt;=4.2.1',
'jupyter_core\&gt;=4.4.0',
'jupyter_client\&gt;=5.2.0',
'nbformat',
'nbconvert',
'ipykernel',
'Send2Trash',
'terminado\&gt;=0.8.1',
'prometheus_client'
],
```

And the resulting dependencies:

&#8230;. python3.7dist(ipykernel) python3.7dist(ipython-genutils)
python3.7dist(jinja2) python3.7dist(jupyter-client) &gt;= 5.2
python3.7dist(jupyter-core) &gt;= 4.4 python3.7dist(nbconvert)
python3.7dist(nbformat) python3.7dist(prometheus-client)
python3.7dist(pyzmq) &gt;= 17 python3.7dist(send2trash)
python3.7dist(terminado) &gt;= 0.8.1 python3.7dist(tornado) &gt;= 4
python3.7dist(traitlets) &gt;= 4.2.1 &#8230;.

Note that any &#96;+.0+&#96; suffixes are removed from version numbers
to match the behavior of Python tools. ([PEP
440](https://www.python.org/dev/peps/pep-0440/&#35;final-releases)
specifies that &#96;+X.Y+&#96; and &#96;+X.Y.0+&#96; are treated as
equal.)

This generator is enabled by default in Fedora. If a packager wishes to
explicitly opt out of the generator because the upstream metadata are
not applicable, a packager SHOULD opt out explicitly by adding:

&#96;+%{?python_disable_dependency_generator}+&#96;

Although this statement can be used anywhere in the spec, we recommend
putting it just before the main package's &#96;+%description+&#96;
declaration.

### Python Extras {#_python_extras_2}

[Python extras](https://www.python.org/dev/peps/pep-0508/&#35;extras)
are a way for Python projects to declare that extra dependencies are
required for additional functionality.

For example, &#96;requests&#96; has several standard dependencies (e.g.
&#96;urllib3&#96;). But it also declares an *extra* named
&#96;+requests\[security\]+&#96;, which lists additional dependencies
(e.g. &#96;cryptography&#96;). Unlike RPM subpackages, extras can only
specify additional dependencies, not additional files. The main package
will work if the optional dependency is not installed, but it might have
limited functionality.

Python tools treat extras as virtual packages. For example, if a user
runs &#96;+pip install requests\[security\]\\&#96;, or installs a
project that depends on \\&#96;+requests\[security\]&#96;, both
&#96;requests&#96; and &#96;cryptography&#96; will be installed.

Starting with Fedora 33, extras are usually provided by packages with no
files. Instead of square brackets, Fedora package names conventionally
use the &#96;+&#96; character to separate the package name and the
*extra* name, e.g. the package would be named
&#96;python3-requests+security&#96;. The plus sign is valid in RPM
package names, but not in Python canonical project names nor in extras
identifiers.

Python packages SHOULD have &#96;Provides&#96; for all extras the
upstream project specifies, except those that are not useful for other
packages (for example build/development requirements, commonly named
&#96;dev&#96;, &#96;doc&#96; or &#96;test&#96;).

A package that provides a Python extra MUST provide
&#96;+python3dist(...\[...\])\\&#96; and
\\&#96;+python3.Xdist(...\[...\])&#96;, for example,
&#96;+python3.9dist(requests\[security\])+&#96;. These requirements
SHOULD be generated using the automatic dependency generator.

A package that provides a Python extra MUST require the extra's main
package with exact NEVR.

A subpackage that primarily provides one Python extra SHOULD be named by
appending &#96;+&#96; and the extra name to the main package name. For
example, &#96;python3-requests+security&#96;.

The most straightforward way to provide an extra is with a dedicated
subpackage containing no files (a \'metapackage\'). This case can be
automated with the &#96;+%python_extras_subpkg+&#96; macro.

Alternative approach: when some extra is always useful in a distro, it
can be provided by the main package; when several extras are related,
they may be provided by a single subpackage. However, having one
dedicated subpackage per extra allows you to use the automatic
dependency generator to ensure that the extras\' requirements will stay
in sync with upstream. If you create a dedicated subpackage and want it
to be always/usually installed, you MAY Require/Recommend/Suggest it
from the main package.

The dependency generator for extras activates if the following holds:

- The package must contain the &#96;.egg-info&#96;/&#96;.dist-info&#96;
  directory, usually as &#96;+%ghost+&#96;.

- The package name must end with &#96;+EXTRA&#96; (where &#96;EXTRA&#96;
  is the extra name).

As an example, the extra subpackage for
&#96;+requests\[security\]\\&#96; can be specified using the
\\&#96;%python_extras_subpkg+&#96; convenience macro as follows. The
macro takes the main package name and name(s) of the extra(s) as well as
path to the &#96;.egg-info&#96; or &#96;.dist-info&#96; directory:

    %{?python_extras_subpkg:%python_extras_subpkg -n python3-requests -i %{python3_sitelib}/\&#42;.egg-info security}

For this case, the extras dependency generator will read upstream
metadata from the &#96;.egg-info&#96; directory. If it finds that the
&#96;security&#96; extra has a dependency on &#96;cryptography&#96;, it
will generate &#96;+Requires: python3.Xdist(cryptography)\\&#96;,
\\&#96;+Provides: python3dist(requests\[security\])&#96; (and the
corresponding &#96;+python3.Xdist+&#96; variant).

If you need additional features that the
&#96;+%python_extras_subpkg+&#96; macro does not cover, you will need to
write the subpackage sections manually. Such features can be, for
example:

- Obsoleting/providing other names (e.g. obsoleted extras packages)

- Manual strong or weak dependencies on other (possibly non-Python)
  packages

- Including files excluded from the main package (if such files only
  make sense with the extra and the base package does not fail without
  them)

As an example of what you need to write in these cases, the
&#96;+%python_extras_subpkg+&#96; macro invocation above expands to the
following:

    %package -n python3-requests+security
    Summary: Metapackage for python3-requests: security extras
    Requires: python3-requests = %{?epoch:%{epoch}:}%{version}-%{release}
    %description -n python3-requests+security
    This is a metapackage bringing in security extras requires for python3-requests.
    It contains no code, just makes sure the dependencies are installed.

    %files -n python3-requests+security
    %ghost %{python3_sitelib}/\&#42;.egg-info

Note that the dependency generator does not add a dependency on the main
package (the &#96;+Requires: python3-setuptools_scm = &#8230;+&#96;
above). If you are not using the &#96;+%python_extras_subpkg+&#96;
macro, you need to add it manually.

:::: note
::: title
:::

The &#96;+%python_extras_subpkg+&#96; can take multiple extras names to
generate multiple packages. For more options, see the [change proposal
which introduced
this](https://fedoraproject.org/wiki/Changes/PythonExtras).
::::

## Provides {#_provides}

For any module &#96;foo&#96; intended to be used in Python 3 with
&#96;import foo&#96;, the package that includes it &#42;should&#42;
provide &#96;python3-foo&#96;. This is of course always the case if the
subpackage is named &#96;python3-foo&#96; (as in the examples below). If
the subpackage has some other name, then &#96;Provides: python3-foo&#96;
should be added explicitly (via &#96;+%py_provides python3-foo+&#96;,
see below).

### The %py_provides macro {#_the_py_provides_macro}

All packages that provide &#96;+python3-&#8230;+&#96; (for any
&#96;+&#8230;+&#96;) SHOULD also provide &#96;+python-&#8230;+&#96; and
&#96;+python3.X-&#8230;+&#96;. Starting from Fedora 33, most of the
Python packages named &#96;+python3-&#8230;+&#96; will provide such
names automatically via the dependency generator in
&#96;/usr/lib/rpm/fileattrs/pythonname.attr&#96;.

Any manually added virtual provides of &#96;+python3-&#8230;+&#96;
SHOULD be done via the &#96;+%py_provides+&#96; macro.

Instead of:

    Provides: python3-pkg_resources = %{version}-%{release}

Do:

    %py_provides python3-pkg_resources

Optionally, supply a custom &#96;epoch:version-release&#96; as a second
argument to &#96;+%py_provides+&#96;.

On releases older than Fedora 33, or (for technical limitations) for
packages without files, it is necessary to use &#96;+%py_provides+&#96;
even for package names:

    %package -n python3-%{srcname}
    Summary: %{summary}
    %py_provides python3-%{srcname}

Packagers SHOULD try to remove explicit &#96;+%py_provides+&#96; calls
for package names, but MAY preserve them if they aim for compatibility
with older releases or packages without files.

:::: note
::: title
:::

Historically, there was &#96;+%python_provide+&#96; macro with similar
but different semantics. It still works for compatibility reasons but it
is deprecated and SHOULD NOT be used and packagers SHOULD replace is
with appropriate &#96;+%py_provides+&#96; call.
::::

## Automatic Provides with a standardized name {#_automatic_provides_with_a_standardized_name_2}

When building a Python package, RPM looks for &#96;+.dist-info+&#96; and
&#96;+.egg-info+&#96; files or directories in the &#96;+%files+&#96;
sections of all packages. If one or more are found, RPM parses them to
find the &#42;standardized name&#42; (i.e. dist name, name on PyPI) of
the packaged software, and then automatically creates two
&#96;+Provides:+&#96; tags in the following format:

&#8230;. Provides: python3.Ydist(CANONICAL_STANDARDIZED_NAME) Provides:
python3dist(CANONICAL_STANDARDIZED_NAME) &#8230;.

The &#96;+3.Y+&#96; is the Python version used (usually 3.6 and higher),
and between the parentheses is the name of the software in a
&#42;canonical format&#42; used by Python tools and services such as
setuptools, pip and PyPI. The canonical name is obtained by switching
the standardized name to lower case and converting all runs of
non-alphanumeric characters to single "-" characters. Example: "The
\$\$\$ Tree" becomes "the-tree".

### Requires and BuildRequires with standardized names {#_requires_and_buildrequires_with_standardized_names_2}

These Provides tags can be used to list Requires and BuildRequires of a
package using the *standardized names* (i.e. dist name, name on PyPI) of
Python modules. To make it easier, you can use the
&#96;+%{py3_dist}\\&#96; macro that accept one or more parameters: the
\_standardized name(s)\_ of the desired Python software. It will convert
the name(s) to the \_canonical format\_ and create the proper
\\&#96;+python3dist(\\&#8230;)&#96; tag(s).

In addition, you can use the &#96;+%{py_dist_name}+&#96; macro that
simply transforms any *standardized name* to the *canonical format*.

For example:

&#8230;. BuildRequires: %{py3_dist PyMySQL} &gt;= 0.7.5 &#35; =&gt;
BuildRequires: python3dist(pymysql) &gt;= 0.7.5

Requires: %{py3_dist virtualenv pyPEG2} &#35; =&gt; Requires:
python3dist(virtualenv) python3dist(pypeg2)

%{py_dist_name 0-.*.-.*.-.*.-.*.-.*.-.*.-0} &#35; =&gt; 0-0 &#8230;.

## Source Files from PyPI {#_source_files_from_pypi_2}

When packaging software which is available from PyPI, you can make use
of the &#96;+%pypi_source+&#96; macro. This macro accepts from zero to
three arguments and evaluates to an appropriate URL for the source file
on PyPI. The arguments are:

1.  The name of the PyPI project. Defaults to &#96;+%srcname+&#96; if
    defined, or to &#96;+%pypi_name+&#96; if defined, or to
    &#96;+%name+&#96; (the package name).

2.  The version of the PyPI project. Defaults to &#96;+%version+&#96;
    (the package version) with any &#96;\~&#96; characters removed (used
    for alpha/beta/dev versions in RPM version but not in Python package
    version).

3.  The file extension to use. Defaults to &#96;tar.gz&#96;.

In most cases it is not necessary to specify any arguments.

## Macros {#_macros_5}

The following macros are defined for you in all supported Fedora and
EPEL releases:

+-----------------------------------------------------------------------+
| Macro                                                                 |
+=======================================================================+
| Expanded path                                                         |
+-----------------------------------------------------------------------+
| Notes                                                                 |
+-----------------------------------------------------------------------+
| &#96;+%{\_\_python}+&#96;                                             |
+-----------------------------------------------------------------------+
| (Error)                                                               |
+-----------------------------------------------------------------------+
| Don't use this macro without redefining it. Defining it changes the   |
| meaning of other \'unversioned\' Python macros such as                |
| &#96;+%{python}\\&#96; or \\&#96;%{python_sitelib}+&#96;.             |
+-----------------------------------------------------------------------+
| &#96;+%{\_\_python3}+&#96;                                            |
+-----------------------------------------------------------------------+
| &#96;+/usr/bin/python3+&#96;                                          |
+-----------------------------------------------------------------------+
| Python 3 interpreter. Redefining this macro changes all the           |
| &#96;+%{python3&#8230;}+&#96; macros.                                 |
+-----------------------------------------------------------------------+
| &#96;+%{python3}+&#96;                                                |
+-----------------------------------------------------------------------+
| &#96;+%{\_\_python3}+&#96;                                            |
+-----------------------------------------------------------------------+
| Python 3 interpreter. Use this macro in spec files.                   |
+-----------------------------------------------------------------------+
| &#96;+%py_provides+&#96;                                              |
+-----------------------------------------------------------------------+
| (Lua script)                                                          |
+-----------------------------------------------------------------------+
| See &lt;&lt;The %py_provides macro&gt;&gt; for detailed explanation.  |
+-----------------------------------------------------------------------+
| &#96;+%{python3_sitelib}+&#96;                                        |
+-----------------------------------------------------------------------+
| &#96;+/usr/lib/python3.X/site-packages+&#96;                          |
+-----------------------------------------------------------------------+
| Where pure python3 modules are installed.                             |
+-----------------------------------------------------------------------+
| &#96;+%{python3_sitearch}+&#96;                                       |
+-----------------------------------------------------------------------+
| &#96;+/usr/lib64/python3.X/site-packages+&#96; on 64bit architectures |
| (e.g. x86_64) and &#96;+/usr/lib/python3.X/site-packages+&#96; on     |
| 32bit.                                                                |
+-----------------------------------------------------------------------+
| Where python3 extension modules (e.g. C compiled) are installed.      |
+-----------------------------------------------------------------------+
| &#96;+%{py_byte_compile}+&#96;                                        |
+-----------------------------------------------------------------------+
| (script)                                                              |
+-----------------------------------------------------------------------+
| See [byte-compiling](Python_Appendix.adoc&#35;manual-bytecompilation) |
| section for usage.                                                    |
+-----------------------------------------------------------------------+
| &#96;+%{python3_version}+&#96;                                        |
+-----------------------------------------------------------------------+
| &#96;+3.X+&#96;                                                       |
+-----------------------------------------------------------------------+
| Python 3 version. Useful when running programs with Python version in |
| filename, such as &#96;+nosetests-%{python3_version}+&#96;.           |
+-----------------------------------------------------------------------+
| &#96;+%{python3_version_nodots}+&#96;                                 |
+-----------------------------------------------------------------------+
| &#96;+3X+&#96;                                                        |
+-----------------------------------------------------------------------+
| Python 3 version without dots. Useful when listing files explicitly   |
| in %files section, such as                                            |
| &#96;+%{python3_sit                                                   |
| earch}/foo/\_speedups.cpython-%{python3_version_nodots}&#42;.so+&#96; |
+-----------------------------------------------------------------------+
| &#96;+%{python3_platform}+&#96;                                       |
+-----------------------------------------------------------------------+
| &#96;+linux-x86_64+&#96; on x86_64                                    |
+-----------------------------------------------------------------------+
| The platform name used in Python, useful for specifying               |
| &#96;+\$PYTHONPATH+&#96;, such as                                     |
| &#                                                                    |
| 96;+PYTHONPATH=build/lib.%{python3_platform}-%{python3_version}+&#96; |
+-----------------------------------------------------------------------+
| &#96;+%{python3_ext_suffix}+&#96;                                     |
+-----------------------------------------------------------------------+
| &#96;+.cpython-3X-x86_64-linux-gnu.so+&#96; on x86_64                 |
+-----------------------------------------------------------------------+
| The usual suffix of Python extension modules, useful when listing     |
| files. Note that extension modules can alternatively have a simple    |
| &#96;+.so+&#96; suffix as well, depending on how they are built.      |
+-----------------------------------------------------------------------+
| &#96;+%py3_build+&#96;                                                |
+-----------------------------------------------------------------------+
| &#96;+%{\_\_python3} setup.py build ...+&#96;                         |
+-----------------------------------------------------------------------+
| See &#96;+%py3_install+&#96; for passing arguments to &#96;+setup.py  |
| build+&#96; or directly to &#96;+setup.py+&#96;.                      |
+-----------------------------------------------------------------------+
| &#96;+%py3_install+&#96;                                              |
+-----------------------------------------------------------------------+
| &#96;+%{\_\_python3} setup.py install \--skip-build ...+&#96;         |
+-----------------------------------------------------------------------+
| Various flags are passed to &#96;+setup.py install+&#96;, see         |
| &#96;/usr/lib/rpm/macros.d/macros.python3&#96; for details and        |
| similar macros. To add extra flags/arguments to &#96;+setup.py        |
| install+&#96;, separate them with &#96;+\--\\&#96;, for example:      |
| \\&#96;%py3_install --- \--install-scripts %{\_libexecdir}\\&#96;. To |
| pass custom command line arguments directly to \\&#96;+setup.py&#96;, |
| define &#96;+%py_setup_args+&#96;.                                    |
+-----------------------------------------------------------------------+
| &#96;+%\_\_pytest+&#96;                                               |
+-----------------------------------------------------------------------+
| &#96;+/usr/bin/pytest+&#96;                                           |
+-----------------------------------------------------------------------+
| The &#96;pytest&#96; command used in &#96;+%pytest+&#96;. Don't use   |
| this macro directly, but feel free to redefine it for usage in        |
| &#96;+%pytest+&#96; if desired.                                       |
+-----------------------------------------------------------------------+
| &#96;+%pytest+&#96;                                                   |
+-----------------------------------------------------------------------+
| &#96;+PATH=... PYTHONPATH=... ... %{\_\_pytest}+&#96;                 |
+-----------------------------------------------------------------------+
| Various environment variables are set to ensure the packaged version  |
| is tested. Use this macro instead of direct &#96;pytest&#96; calls in |
| &#96;+%check+&#96;. Pass additional argument as if passed to          |
| &#96;pytest&#96;, e.g. &#96;+%pytest -m \'not network\'+&#96; to      |
| deselect tests marked as &#96;network&#96;.                           |
+-----------------------------------------------------------------------+
| &#96;+%py3_check_import ...+&#96;                                     |
+-----------------------------------------------------------------------+
| &#96;+PATH=... PYTHONPATH=... ... %{\_\_python3} -c \'import          |
| ...\'+&#96;                                                           |
+-----------------------------------------------------------------------+
| Various environment variables are set to ensure the packaged version  |
| is tested. Use this macro in &#96;+%check+&#96; to test public Python |
| modules are importable if running upstream tests suite is not         |
| feasible. Pass module names as positional arguments separated by      |
| spaces or commas.                                                     |
+-----------------------------------------------------------------------+
| &#96;+%{py_dist_name}+&#96;                                           |
+-----------------------------------------------------------------------+
| (Lua script)                                                          |
+-----------------------------------------------------------------------+
| Given a standardized name (i.e. dist name, name on PyPI) of Python    |
| software, it will convert it to a canonical format. See               |
| &lt;&lt;Automatic Provides with a standardized name&gt;&gt; for more  |
| information.                                                          |
+-----------------------------------------------------------------------+
| &#96;+%{py3_dist}+&#96;                                               |
+-----------------------------------------------------------------------+
| (Lua script)                                                          |
+-----------------------------------------------------------------------+
| Given a standardized name (i.e. dist name, name on PyPI) of Python    |
| software, it will convert it to a canonical format, and evaluates to  |
| &#96;+python3dist(CANONICAL_NAME)+&#96;, which is useful when listing |
| dependencies. See &lt;&lt;Automatic Provides with a standardized      |
| name&gt;&gt; for more information.                                    |
+-----------------------------------------------------------------------+
| &#96;+%{pypi_source}+&#96;                                            |
+-----------------------------------------------------------------------+
| (Lua script)                                                          |
+-----------------------------------------------------------------------+
| Evaluates to the appropriate URL for the package. See above for more  |
| information.                                                          |
+-----------------------------------------------------------------------+
| &#96;+%pycached ....py+&#96;                                          |
+-----------------------------------------------------------------------+
| (Lua script)                                                          |
+-----------------------------------------------------------------------+
| Given a Python file, lists the file and the files with its bytecode   |
| cache. See &lt;&lt;Byte compiling&gt;&gt; for more information.       |
+-----------------------------------------------------------------------+
| &#96;+%{py3_shebang_flags}+&#96;                                      |
+-----------------------------------------------------------------------+
| &#96;s&#96;                                                           |
+-----------------------------------------------------------------------+
| The default set of flags for Python shebangs. Redefine this to change |
| the set. Used by &#96;+%py3_shebang_fix+&#96;.                        |
+-----------------------------------------------------------------------+
| &#96;+%py3_shebang_fix ...+&#96;                                      |
+-----------------------------------------------------------------------+
| (Python script)                                                       |
+-----------------------------------------------------------------------+
| Given paths for Python files or directories with them, it changes     |
| Python shebangs to &#96;+&#35;! %{\_\_python3}\\&#96;, preserves any  |
| existing flags (if found) and adds flags defined in                   |
| \\&#96;%{py3_shebang_flags}+&#96; (if not already present).           |
+-----------------------------------------------------------------------+

During &#96;+%install+&#96; or when listing &#96;+%files+&#96; you can
use the &#96;+%{python3_sitearch}\\&#96; and
\\&#96;%{python3_sitelib}+&#96; macros to specify where the installed
modules are to be found. For instance:

&#8230;. %files &#35; A pure python3 module
%{python3_sitelib}/foomodule/ &#35; A compiled python3 extension module
%{python3_sitearch}/barmodule/ &#8230;.

Use of the macros has several benefits:

&#42; It ensures that the packages are installed correctly on multilib
architectures. &#42; Using these macros instead of hardcoding the
directory in the specfile ensures your spec remains compatible with the
installed Python version even if the directory structure changes
radically (for instance, if &#96;+python3_sitelib+&#96; moves into
&#96;+%{\_datadir}+&#96;).

## Packages using Cython {#_packages_using_cython}

A great amount of extension modules for Python (Python modules written
in a compiled language such as C or C++) are written using the
[Cython](https://cython.org/) language and compiler.

Majority of such packages contains the generated C (or C++) sources in
the source tarball.

Tightening the [general Fedora
policy](what-can-be-packaged.adoc&#35;_pregenerated_code), packages MUST
NOT use pre-generated Cython sources. They MUST be deleted in
&#96;%prep&#96; and regenerated during the build.

Any exception to this rule should be considered a
[bootstrapping](index.adoc&#35;bootstrapping).

## Files to include {#_files_to_include_2}

When packaging Python modules, several types of files are included:

&#42; \\&#42;.py source files because they are used when generating
tracebacks. &#42; \\&#42;.pyc byte compiled files. &#42;&#42; Python
will try to create them at runtime if they don't exist which leads to
spurious SELinux AVC denials in the logs. &#42;&#42; If the system
administrator invokes Python with -OO, they will be created with no
docstrings. This can break some programs. &#42; \\&#42;.egg-info or
\\&#42;.dist-info files or directories. If these are generated by the
module's build scripts they must be included in the package because they
might be needed by other applications and modules at runtime.

The source files MUST be included in the same package as the byte
compiled versions.

Packagers SHOULD NOT simply glob everything under the sitelib or
sitearch directories. The following SHOULD NOT be used:

&#42; &#96;+%{python3_sitelib}/&#42;+&#96; &#42;
&#96;+%{python3_sitearch}/&#42;+&#96; &#42;
&#96;+%{python_sitelib}/&#42;+&#96; &#42;
&#96;+%{python_sitearch}/&#42;+&#96;

And packages MUST NOT include the top-level &#96;+*pycache*+&#96;
directory (see below).

## Byte compiling {#_byte_compiling}

Python will automatically try to byte compile files when it runs in
order to speed up startup the next time it is run. These files are saved
in files with the extension of .pyc (compiled Python). These files will
be located inside a directory named &#96;+*pycache*+&#96;.

The .pyc files contain byte code that is portable across OSes. If you do
not include them in your packages, Python will try (and generally fail)
to create them when the user runs the program. If the system
administrator runs the program, then the files will be successfully
written, causing stray .pyc files which will not be removed when the
package is removed. To prevent that the byte compiled files need to be
compiled and included in the &#96;+%files+&#96; section. Normally, byte
compilation is done for you by the &#96;+brp-python-bytecompile+&#96;
script. This script runs after the &#96;+%install+&#96; section of the
spec file has been processed and byte compiles any .py files that it
finds in &#96;+%{python3_sitelib}\\&#96; or
\\&#96;%{python3_sitearch}\\&#96; (this recompilation puts the proper
filesystem paths into the modules otherwise tracebacks would include the
\\&#96;%{buildroot}+&#96; in them).

You must include the .pyc files in your package. If the build process
creates a &#96;+*pycache*+&#96; directory in a subdirectory of
&#96;+%{python3_sitearch}\\&#96; or \\&#96;%{python3_sitelib}\\&#96;,
you must also include all items in the \\&#96;+\_\_pycache\_\_&#96;
directory. You MUST NOT include the directories
&#96;+%{python3_sitearch}/*pycache*+&#96; or
&#96;+%{python3_sitelib}/*pycache*+&#96; because they are already owned
by the python3-libs package.

All that you need to do is include the files in the &#96;+%files+&#96;
section (replacing &#96;+%{python3_sitelib}+&#96; with the appropriate
macro for your package):

&#8230;. %files %{python3_sitelib}/foo/ &#8230;.

or, if the Python code installs directly into
&#96;+%{python3_sitelib}\\&#96;, use the \\&#96;%pycached+&#96; macro to
include the bytecode cache files:

&#8230;. %files %pycached %{python3_sitelib}/foo.py &#8230;.

That evaluates roughly to

&#8230;. %files %{python3_sitelib}/foo.py
%{python3_sitelib}/*pycache*/foo.cpython-%{python3_version_nodots}{,.opt-?}.pyc
&#8230;.

:::: note
::: title
:::

The &#96;+%pycached+&#96; macro only supports Python 3.5+, so for older
Python versions (such as 3.4 in EPEL 6 or 7), you need to list the files
manually.
::::

:::: note
::: title
:::

In case you need to use other macros with the &#96;+%pycached+&#96;
macro, such as &#96;+%exclude+&#96; or &#96;+%ghost+&#96;, pass the
other macro as part of the argument to &#96;+%pycached+&#96;. For
example: &#96;+%pycached %exclude /path/to/foo.py+&#96; Using the macros
in wrong order would only apply &#96;+%exclude+&#96; to the first entry
that &#96;+%pycached+&#96; generates.
::::

### Manual byte compilation {#_manual_byte_compilation_2}

For more details on the internals of byte compilation, please see [the
appendix](Python_Appendix.adoc&#35;manual-bytecompilation).

## Example Python spec file {#_example_python_spec_file}

The following is a very simple spec file for a Python module.

:::: formalpara
::: title
python-example.spec
:::
::::

## Reviewer checklist {#_reviewer_checklist}

The following briefly summarizes the guidelines for reviewers to go
over:

&#42; &#42;Must&#42;: Python modules must be built from source. They
cannot simply drop an egg or whl from upstream into the proper
directory. (See [prebuilt binaries
Guidelines](what-can-be-packaged.adoc&#35;prebuilt-binaries-or-libraries)
for details). &#42; &#42;Must&#42;: Python modules must not download any
dependencies during the build process. &#42; &#42;Must&#42;: When
building a compat package, it must install using easy_install -m so it
won't conflict with the main package. &#42; &#42;Must&#42;: When
building multiple versions (for a compat package) one of the packages
must contain a default version that is usable via \'import MODULE\' with
no prior setup. &#42; &#42;Should&#42;: Additional
&#96;+python3-&#8230;+&#96; provides should be accomplished via a
&#96;+%py_provides+&#96; call. &#42; &#42;Should&#42;: A package which
is used by another package via an egg interface should provide egg info.

# Additional Python Guidelines {#_additional_python_guidelines}

Here are some additional Python-related guidelines, moved here in order
to keep the main page manageable.

\[&#35;manual-bytecompilation\] == Manual byte compilation

:::: note
::: title
:::

This section only applies for the 201x-era guidelines. In the new
guidelines, see the [Manual byte
compilation](Python.adoc&#35;manual-bytecompilation) section.
::::

When byte compiling a .py file, python embeds a magic number in the byte
compiled files that correspond to the runtime. Files in
&#96;+%{python?\_sitelib}\\&#96; and \\&#96;%{python?\_sitearch}\\&#96;
MUST correspond to the runtime for which they were built. For instance,
a pure Python module compiled for the 3.4 runtime MUST be below
\\&#96;%{\_usr}/lib/python3.4/site-packages+&#96;

The &#96;+brp-python-bytecompile+&#96; script tries to figure this out
for you. The script determines which interpreter to use when byte
compiling the module by checking what directory the file is installed
in. If it's &#96;+/usr/lib{,64}/pythonX.Y+&#96;, then
&#96;+pythonX.Y+&#96; is used to byte compile the module. If
&#96;+pythonX.Y+&#96; is not installed, then an error is returned and
the rpm build process will exit on an error so remember to
&#96;+BuildRequire+&#96; the proper python package.

If you have &#96;+&#42;.py+&#96; files outside of the
&#96;+/usr/lib(64)?/pythonX.Y/\\&#96; directories and you require those
files to be byte compiled (e.g. it\'s an importable Python module) you
MUST compile them explicitly using the \\&#96;%py_byte_compile+&#96;
macro. Note that not all Python files are importable Python modules;
when in doubt, grep the sources for the appropriate import statement.

An example for a package that has both Python versions:

&#8230;. &#35; Buildrequire both python2 and python3
BuildRequires: python2-devel python3-devel

%install
&#35; Installs a python2 private module into %{buildroot}%{\_datadir}/mypackage/foo
&#35; and installs a python3 private module into %{buildroot}%{\_datadir}/mypackage/bar
make install DESTDIR=%{buildroot}

&#35; Manually invoke the python byte compile macro for each path that needs byte
&#35; compilation.
%py_byte_compile %{python2} %{buildroot}%{\_datadir}/mypackage/foo
%py_byte_compile %{python3} %{buildroot}%{\_datadir}/mypackage/bar
&#8230;.

The &#96;+%py_byte_compile+&#96; macro takes two arguments. The first is
the python interpreter to use for byte compiling. The second is a file
or directory to byte compile. If the second argument is a directory, the
macro will recursively byte compile any &#42;.py file in the directory.

## Manual byte compilation for EPEL 6 and 7 {#_manual_byte_compilation_for_epel_6_and_7}

The script interpreter defined in &#96;+%{\_\_python}\\&#96; is used to
compile the modules outside of \\&#96;/usr/lib(64)?/pythonX.Y/\\&#96;
directories. This defaults to \\&#96;/usr/bin/python+&#96; (that's
Python 2.6 or on EPEL 6 and 2.7 on EPEL 7). If you need to compile the
modules for python3, set it to &#96;+/usr/bin/python3+&#96; instead:

&#8230;. %global \_\_python %{python3} &#8230;.

Doing this is useful when you have a python3 application that's
installing a private module into its own directory. For instance, if the
foobar application installs a module for use only by the command line
application in &#96;+%{\_datadir}/foobar+&#96;. Since these files are
not in one of the python3 library paths (i.e.,
&#96;+/usr/lib/python3.6+&#96;) you have to override
&#96;+%{\_\_python}\\&#96; to tell \\&#96;+brp-python-bytecompile&#96;
to use the python3 interpreter for byte compiling.

These settings are enough to properly byte compile any package that
builds Python modules in &#96;+%{python?\_sitelib}\\&#96; or
\\&#96;%{python?\_sitearch}+&#96; or builds for only a single Python
interpreter. However, if the application you're packaging needs to build
with both python2 and python3 and install into a private module
directory (perhaps because it provides one utility written in python2
and a second utility written in python3) then you need to do this
manually. Here's a sample spec file snippet that shows what to do:

&#8230;. &#35; Turn off the brp-python-bytecompile script %global
*os_install_post %(echo \'%{*os_install_post}\' \| sed -e
\'s!/usr/lib\[\^\[:space:\]\]&#42;/brp-python-bytecompile[]{#:space:}.&#42;\$!!g\')
&#35; Buildrequire both python2 and python3 BuildRequires: python2-devel
python3-devel \[&#8230;\]

%install &#35; Installs a python2 private module into
%{buildroot}%{\_datadir}/mypackage/foo &#35; and installs a python3
private module into %{buildroot}%{\_datadir}/mypackage/bar make install
DESTDIR=%{buildroot}

&#35; Manually invoke the python byte compile macro for each path that
needs byte &#35; compilation. %py_byte_compile %{python2}
%{buildroot}%{\_datadir}/mypackage/foo %py_byte_compile %{python3}
%{buildroot}%{\_datadir}/mypackage/bar &#8230;.

Note that this &#42;does disable&#42; the compilation of files in
&#96;+/usr/lib(64)?/pythonX.Y/+&#96;.

## Byte compilation reproducibility {#_byte_compilation_reproducibility}

This subsection only applies to Fedora &lt;= 40, ELN, and EPEL. In later
Fedora releases, this is implemented automatically.

For two Python files with the exact same content and metadata, byte
compilation might produce different results. The resulting
&#96;.pyc&#96; files are functionally identical but are not bit-by-bit
identical. In most cases, internal Python reference counter is here to
blame because it might have a different internal state during each byte
compilation. If you want a deeper explanation, take a look at [this
Bugzilla
comment](https://bugzilla.redhat.com/show_bug.cgi?id=1686078&#35;c2).

This inconvenience might cause a problem in Koji where noarch packages
built as a part of an arch build might be rejected because they have
different content.

To work around this issue, BuildRequire marshalparser
&#96;BuildRequires: /usr/bin/marshalparser&#96; (a tool that makes
&#96;.pyc&#96; files more reproducible) and instruct it to process the
&#96;.pyc&#96; files in certain paths by setting the
&#96;+%py_reproducible_pyc_path+&#96; macro:

&#8230;. %global py_reproducible_pyc_path
%{buildroot}%{\_datadir}/llamafarm/plugins &#8230;.

With that setting, marshalparser recursively finds all byte-compiled
Python files in &#96;+%{buildroot}%{\_datadir}/llamafarm/plugins+&#96;
and attempts to fix them. This happens at the very end of the build
process when all previous byte compilation steps are finished. If
marshalparser cannot parse some of the cache files, the build fails.

# R Packaging Guidelines {#_r_packaging_guidelines}

[R](http://www.r-project.org/) is a language and environment for
statistical computing and graphics. R is similar to the award-winning S
system, which was developed at Bell Laboratories by John Chambers et al.
It provides a wide variety of statistical and graphical techniques
(linear and nonlinear modelling, statistical tests, time series
analysis, classification, clustering, &#8230;).

R is designed as a true computer language with control-flow
constructions for iteration and alternation, and it allows users to add
additional functionality by defining new functions. For computationally
intensive tasks, C, C++ and Fortran code can be linked and called at run
time. For more info, see [An introduction to
R](http://cran.r-project.org/doc/manuals/R-intro.html).

This document covers how to handle R \'add-on packages\' for inclusion
in Fedora's repositories. For a complete example, see the
&lt;&lt;Example spec file&gt;&gt; below.

## Naming {#_naming_9}

The canonical source of R packages is
[CRAN](https://cran.r-project.org/), the \'Comprehensive R Archive
Network\'. The are additional CRAN-like repositories for specific
fields, such as [Bioconductor](https://bioconductor.org/) (Bioc for
short) for bioinformatics. But since they are designed to be
complementary, package names do not conflict with each other.

R add-ons &#42;MUST&#42; be packaged with &#96;R-\$pkg&#96; as the name
of the source package, where &#96;\$pkg&#96; is the name of the project
on the upstream CRAN-like repository, i.e. the package
[DESCRIPTION](https://cran.r-project.org/doc/manuals/r-devel/R-exts.html&#35;The-DESCRIPTION-file)\'s
&#96;Package&#96; field. This &#96;\$pkg&#96; name &#42;MUST&#42; be
exactly as written upstream, including case distinctions and dots. Also:

&#42; The spec's &#96;Summary&#96; field &#42;SHOULD&#42; match the
package DESCRIPTION's &#96;Title&#96; field. &#42; The spec's
&#96;Description&#96; field &#42;SHOULD&#42; match the package
DESCRIPTION's &#96;Description&#96; field.

## Versioning {#_versioning_2}

Since upstream versions may contain characters that are invalid in RPM
version strings, they &#42;MUST&#42; be translated to be RPM-compatible.
Particularly, it is common for R packages to specify patch versions
using the hyphen as the separator, e.g. &#96;1.2-3&#96;. Such hyphens
&#42;MUST&#42; be converted to a dot. This translation &#42;SHOULD&#42;
be done via the &#96;+%R_rpm_version+&#96; macro as follows:

    Version: %R_rpm_version 1.2-3

Apart from defining &#96;+%{version}\\&#96; as \\&#96;1.2.3\\&#96; in
this case, this macro sets \\&#96;%\_\_R_upstream_version+&#96; to keep
track of the upstream version for URL generation.

## License {#_license}

Typically, R packages do not contain license files per CRAN policy. R
allows and ships a set of open source licenses, and R packages just
declare which one they adhere to in the DESCRIPTION file. Following this
policy, and as an exception to the general Licensing Guidelines, we do
not require upstream R packages to add additional license files.

:::: note
::: title
:::

Full text licenses can be found under &#96;/usr/share/R/licenses&#96;.
These texts can also be displayed in the R console using the
&#96;RShowDoc()&#96; function.
::::

## Sources {#_sources}

Projects from standard CRAN-like repositories &#42;MUST&#42; be packaged
from the sources that are published there. Packages from the following
repositories &#42;MUST&#42; use the set macros provided for automatic
generation of the project's URL and package's source URL:

&#42; CRAN: &#96;+%{cran_url}\\&#96; and \\&#96;%{cran_source}\\&#96;
\\&#42; Bioc: \\&#96;%{bioc_url}\\&#96; and \\&#96;%{bioc_source}+&#96;

The URLs above correspond to the default *software* repositories.
Bioconductor provides additional repositories that can be specified via
an argument:

&#42; AnnotationData: &#96;+%{bioc_url data/annotation}\\&#96; and
\\&#96;%{bioc_source data/annotation}\\&#96; \\&#42; ExperimentData:
\\&#96;%{bioc_url data/experiment}\\&#96; and \\&#96;%{bioc_source
data/experiment}\\&#96; \\&#42; Workflows: \\&#96;%{bioc_url
workflows}\\&#96; and \\&#96;%{bioc_source workflows}+&#96;

## Architectures {#_architectures}

Packages that do not contain architecture-specific code (i.e. no
compiled parts), &#42;MUST&#42; set &#96;BuildArch: noarch&#96;.

:::: note
::: title
:::

This affects the installation path:

&#42; &#96;+%{\_datadir}/R/library/\$pkg+&#96; for noarch packages;
&#42; &#96;+%{\_libdir}/R/library/\$pkg+&#96; otherwise;

but this is automatically handled by RPM macros as described below.
::::

## Dependencies {#_dependencies_5}

### Automatic standardized names {#_automatic_standardized_names}

All R packages will automatically produce standardized
&#96;Requires&#96; and &#96;Provides&#96; via a generator in
&#96;R-rpm-macros&#96;:

&#42; &#96;Provides&#96; are in the form &#96;R(\$pkg) = \$version\\&#96

:   &#42; &#96;Requires&#96; are in the form &#96;R(\$pkg)&#96;, with
    optional &#96;&gt;= \$version&#96; as specified in the package's
    metadata if supplied;

where &#96;\$pkg&#96; is the upstream package name, and
&#96;\$version&#96; is the RPM-compatible version as described in
&lt;&lt;Versioning&gt;&gt;.

The packager &#42;MUST&#42; inspect the generated &#96;Requires&#96; for
correctness. All hard dependencies (R's &#96;LinkingTo&#96;,
&#96;Depends&#96;, &#96;Imports&#96;) &#42;MUST&#42; be resolvable
within the targeted Fedora version.

### BuildRequires {#_buildrequires_6}

Packages &#42;MUST&#42; declare &#96;BuildRequires: R-devel&#96;, which
in turn pulls the necessary &#96;R-rpm-macros&#96; and sets the
development environment (compilers, libraries, etc.).

:::: note
::: title
:::

Note that R packages inherit their compilation flags from the main R
package, which stores them in &#96;+%{\_libdir}/R/etc/Makeconf+&#96;.
The design of R is such that all R add-on packages use the same
optimization flags that the main R package was built with. Accordingly,
this is why R addon packages do not pass &#96;+%{optflags}+&#96;.
::::

If other libraries and utilities (e.g. cmake) are required for building,
they &#42;MUST&#42; be declared explicitly as &#96;BuildRequires&#96;.

Build-time dependencies on other R packages are automatically handled by
the &#96;+%R_buildrequires+&#96; macro, which &#42;MUST&#42; be called
in the &#96;+%generate_buildrequires+&#96; scriptlet.

:::: note
::: title
:::

&#42; All hard dependencies (R's &#96;LinkingTo&#96;, &#96;Depends&#96;,
&#96;Imports&#96;) are declared as &#96;BuildRequires&#96; using
standardized names (see &lt;&lt;Automatic standardized names&gt;&gt;).
&#42; Soft dependencies (R's &#96;Suggests&#96;, &#96;Enhances&#96;) are
skipped, except for packages used to develop the test suite (see
&lt;&lt;Dynamic BuildRequires&gt;&gt;).
::::

### Bundled dependencies {#_bundled_dependencies}

Following the general guidelines, packages &#42;SHOULD&#42; unbundle
other dependencies found in R package sources whenever possible.
Whenever bundled dependencies are used, they &#42;MUST&#42; be declared
with virtual &#96;Provides&#96;.

### Sub-packages {#_sub_packages}

Some R packages expose header files under the standard path
&#96;R/library/\$pkg/include&#96; (defined by CRAN and expected by R),
so that other packages can link to them via &#96;LinkingTo&#96;. The
[Rcpp](https://cran.r-project.org/package=Rcpp) package is a notable
example. Sometimes, these headers are required at build-time, sometimes
at build- as well as run-time and therefore they are essential for
proper functioning. For these and a variety of other reasons, these
headers &#42;MUST NOT&#42; be split off into a &#96;-devel&#96;
sub-package.

If a particular package contains a large number of examples or
documentation that do not impact the package's functionality, these
parts &#42;MAY&#42; be split off into a sub-package, but sub-packages in
general are highly discouraged.

## Walkthrough {#_walkthrough_2}

### Preparing the sources {#_preparing_the_sources}

The rest of the scriptlets expect package sources to be extracted in a
subdirectory named after the package. Therefore, in &#96;+%prep+&#96;,
the call to &#96;+%setup+&#96; or &#96;+%autosetup+&#96; &#42;MUST&#42;
set the &#96;-c&#96; option.

    %prep
    %autosetup -c

Other code for unbundling, fixes and workarounds &#42;MAY&#42; be placed
here.

### Dynamic BuildRequires {#_dynamic_buildrequires}

The &#96;+%R_buildrequires+&#96; macro &#42;MUST&#42; be called in the
&#96;+%generate_buildrequires+&#96; scriptlet to generate the dynamic
&#96;BuildRequires&#96;.

    %generate_buildrequires
    %R_buildrequires

Testing packages such as &#96;testthat&#96;, which are declared in
&#96;Suggests&#96;, are whitelisted in &#96;+%{\_\_R_whitelist}\\&#96;,
and added as \\&#96;BuildRequires\\&#96; by
\\&#96;%R_buildrequires+&#96;.

:::: important
::: title
:::

Currently, only the most common testing suites available in Fedora are
supported:

&#96;testthat\|tinytest\|RUnit\|testit&#96;
::::

Using other &#96;Suggests&#96; in the tests &#42;SHOULD&#42; be
considered a bug. However, some additional &#96;Suggests&#96;
&#42;MAY&#42; be used by overwriting &#96;+%{\_\_R_whitelist}+&#96; as
follows:

    %global __R_whitelist testthat|mockery|withr

if the packager wishes to use &#96;mockery&#96; and &#96;withr&#96; on
top of &#96;testthat&#96;.

### Building and Installing {#_building_and_installing}

R packages are built and installed in a single stage via &#96;R CMD
INSTALL&#96;. Therefore, the &#96;+%build+&#96; section &#42;MUST&#42;
be empty.

Two macros are provided and &#42;MUST&#42; be called in the
&#96;+%install+&#96; section. First, &#96;+%R_install+&#96; builds and
installs the package into &#96;+%{buildroot}%{\_R_libdir}\\&#96;, then
\\&#96;%R_save_files+&#96; generates a list of files corresponding to
the given importable module, and saves it as &#96;+%{R_files}+&#96;.

    %build

    %install
    %R_install
    %R_save_files

:::: note
::: title
:::

The &#96;+%R_install+&#96; macro ensures reprodubility by setting the
package's build timestamp as &#96;\$SOURCE_DATE_EPOCH&#96;.
::::

:::: note
::: title
:::

R package installation generates a new &#96;R.css&#96; file that
conflicts with the master &#96;R.css&#96; file included in the main R
package. The &#96;+%R_install+&#96; macro deletes this file.
::::

:::: note
::: title
:::

The &#96;+%R_install+&#96; macro calls &#96;+%\_R_libdir_check+&#96; to
ensure that a noarch package did not produce a shared library, or an
archful package actually contains a shared library; otherwise, it fails
with an informative error message. If the packager does not want this
check, &#96;+%\_R_libdir_check+&#96; &#42;MAY&#42; be set to
&#96;+%nil+&#96;.
::::

### Testing {#_testing_3}

The &#96;+%R_check+&#96; macro &#42;MUST&#42; be called in the
&#96;+%check+&#96; section to run R package checks.

    %check
    %R_check

According to CRAN's guidelines, R packages &#42;MUST&#42; work without
soft dependencies. If package checks fail because soft dependencies are
used unconditionally (e.g. in examples or tests), this is considered a
bug and &#42;SHOULD&#42; be reported upstream. Meanwhile, a workaround
&#42;MUST&#42; be put in place:

&#42; If the failure happens in an example, the
&#96;\\\--no-examples&#96; flag &#42;MAY&#42; be appended to
&#96;+%R_check+&#96;. &#42; If the failure happens in a test, a
&#96;skip()&#96; call &#42;MAY&#42; be added in the proper place to skip
a test, or a test file &#42;MAY&#42; be removed, or even the
&#96;\\\--no-tests&#96; flag &#42;MAY&#42; be appended to
&#96;+%R_check+&#96; for more complicated situations.

### Listing files {#_listing_files}

Module files &#42;MUST&#42; be added via the &#96;-f&#96; option as
follows:

    %files -f %{R_files}

If necessary, any additional files outside the package's path
&#42;SHOULD&#42; be added explicitly afterwards.

## Example spec file {#_example_spec_file_3}

This is an example spec file for a hypothetical R package called
\'foo\', with upstream version &#96;1.2-3&#96;:

    Name:           R-foo
    Version:        %R_rpm_version 1.2-3
    Release:        %autorelease
    Summary:        Adds foo functionality for R

    License:        GPL-2.0-or-later
    URL:            %{cran_url}
    Source:         %{cran_source}

    \&#35; BuildArch:      noarch
    BuildRequires:  R-devel
    \&#35; BuildRequires:  somelib-devel

    %description
    R Interface to foo, enables bar!

    %prep
    %autosetup -c

    %generate_buildrequires
    %R_buildrequires

    %build

    %install
    %R_install
    %R_save_files

    %check
    %R_check

    %files -f %{R_files}

    %changelog
    %autochangelog

# Ruby Packaging Guidelines {#_ruby_packaging_guidelines}

:::: note
::: title
:::

&#42;JRuby Gems&#42;: Although Fedora has fully functioning JRuby
integrated with system RubyGems, we have decided to not include the
JRuby specific packaging guidelines here, as they need some more work.
They will appear here as soon as we feel that we've got everything
covered properly. You can contact us on [Ruby-SIG mailing
list](https://lists.fedoraproject.org/archives/list/ruby-sig@lists.fedoraproject.org/)
in case of any questions about the prepared JRuby packaging guidelines.
::::

There are three basic categories of ruby packages:
&lt;&lt;RubyGems&gt;&gt;, &lt;&lt;Non-Gem Packages,non-gem Ruby
packages&gt;&gt;, and &lt;&lt;Applications,applications written in
Ruby&gt;&gt;. These guidelines contain sections common to all of these
as well as sections which apply to each one individually. Be sure to
read all the guidelines relevant to the type of ruby package you are
building.

## Ruby Compatibility {#_ruby_compatibility}

Each Ruby package MUST indicate it depends on a Ruby interpreter (this
does not apply to &lt;&lt;RubyGems&gt;&gt;). Use &#96;ruby(release)&#96;
virtual requirement to achieve that:

&#8230;. Requires: ruby(release) &#8230;.

If the package requires Ruby of certain version(s), make the requirement
versioned like this:

&#8230;. Requires: ruby(release) &gt;= 1.9.1 &#8230;.

:::: note
::: title
:::

&#42;Alternate interpreters&#42;: Alternate Ruby interpreters (currently
JRuby) also &#96;Provide: ruby(release)&#96;. This implies, that pure
RubyGems packages (these are shared among interpreters) SHOULD NOT have
&#96;Requires: ruby&#96; or &#96;Requires: jruby&#96; to have their
dependencies satisfied by any of these interpreters.
::::

:::: warning
::: title
:::

&#42;Over specified ruby(release) versioning&#42;: Please note that if
the &#96;ruby(release)&#96; version requirement is too specific, it
might cause an unexpected interpreter to be drawn in. E.g.
&#96;ruby(release) = 1.8&#96; will require JRuby package, since it is
the only package that provides it.
::::

### Different Interpreters Compatibility {#_different_interpreters_compatibility}

Most of the pure Ruby packages will work on all Ruby interpreters. There
are however cases when the packages use interpreter-specific functions
(like &#96;fork()&#96;) and won't run on other interpreters (JRuby). In
this case, the package SHOULD require that interpreter. For example, a
package that uses &#96;fork&#96; SHOULD explicitly specify
&#96;Requires: ruby&#96;. In case of such package, packager SHOULD file
a bug to ask upstream to provide support for other interpreter(s). This
SHOULD be documented in specfile.

### Shebang lines {#_shebang_lines}

On Fedora, &#96;/usr/bin/ruby&#96; is implemented via
[Rubypick](https://github.com/bkabrda/rubypick). Rubypick is a tool
similar to RVM or rbenv. It allows choosing interpreter to execute Ruby
script. Rubypick routes anything executed via &#96;/usr/bin/ruby&#96; to
&#96;/usr/bin/ruby-mri&#96; or &#96;/usr/bin/jruby&#96;. By default, it
runs MRI (Matz's Ruby Implementation), but user can explicitly specify
the interpreter by using &#96;+*mri*+&#96; or &#96;+*jruby*+&#96; as a
first parameter. For example:

&#8230;. ruby *jruby* jruby_script.rb gem *mri* install foo rails
*jruby* s &#8230;.

Using the &#96;RUBYPICK&#96; environment variable can achieve the same
results. The environment variable can be used to set one interpreter as
the global default:

&#8230;. export RUBYPICK=*jruby* ruby jruby_script.rb &#35; Will use
jruby gem install foo &#35; Will also use jruby &#8230;.

Ruby executables that are known to only run on one Ruby implementation
SHOULD use that specific implementation in their shebang
(&#96;+&#35;!/usr/bin/ruby-mri+&#96; or
&#96;+&#35;!/usr/bin/jruby+&#96;) to ensure that they run using that
implementation. All other code SHOULD use
&#96;+&#35;!/usr/bin/ruby+&#96;.

## Naming Guidelines {#_naming_guidelines_4}

&#42; Packages that contain Ruby Gems MUST be called
&#96;+rubygem-%{gem_name}+&#96;.

&#42; The name of a ruby extension/library package MUST start with the
interpreter it is built for (ruby, jruby, etc.) and then the
&#96;UPSTREAM&#96; name. For example: &#96;ruby-UPSTREAM&#96;. If the
upstream name &#96;UPSTREAM&#96; contains &#96;ruby&#96;, that SHOULD be
dropped from the name. For example, the SQLite database driver for ruby
is called &#96;sqlite3-ruby&#96;. The corresponding Fedora package
SHOULD be called &#96;ruby-sqlite3&#96;, and not
&#96;ruby-sqlite3-ruby&#96;.

&#42; Application packages that mainly provide user-level tools that
happen to be written in Ruby MUST follow the general [Naming
Guidelines](Naming.xml) instead.

## Macros {#_macros_6}

Non-gem ruby packages and ruby gem packages install to certain standard
locations. The &#96;ruby-devel&#96; and &#96;rubygems-devel&#96;
packages contain macros useful for the respective package types.
Alternate ruby interpreters will have equivalent locations (to be added
to this table later).

+-----------------+-----------------------------------+-----------------+
| Macro           | Expanded path                     | Usage           |
+=================+===================================+=================+
| &#42;From       |                                   |                 |
| ruby-devel;     |                                   |                 |
| intended for    |                                   |                 |
| non-gem         |                                   |                 |
| packages.&#42;  |                                   |                 |
+-----------------+-----------------------------------+-----------------+
| &#9             | &#96;+/u                          | Place for       |
| 6;+%{ruby_vendo | sr/lib{64}/ruby/vendor_ruby+&#96; | architecture    |
| rarchdir}+&#96; |                                   | specific (e.g.  |
|                 |                                   | &#42;.so)       |
|                 |                                   | files.          |
+-----------------+-----------------------------------+-----------------+
| &#              | &#96;+                            | Place for       |
| 96;+%{ruby_vend | /usr/share/ruby/vendor_ruby+&#96; | architecture    |
| orlibdir}+&#96; |                                   | independent     |
|                 |                                   | (e.g. &#42;.rb) |
|                 |                                   | files.          |
+-----------------+-----------------------------------+-----------------+
| &               | &#96;+/usr/l                      | Place for local |
| #96;+%{ruby_sit | ocal/lib{64}/ruby/site_ruby+&#96; | architecture    |
| earchdir}+&#96; |                                   | specific (e.g.  |
|                 |                                   | &#42;.so)       |
|                 |                                   | files.          |
+-----------------+-----------------------------------+-----------------+
| &#96;+%{ruby_si | &#96;+/usr                        | Place for local |
| telibdir}+&#96; | /local/share/ruby/site_ruby+&#96; | architecture    |
|                 |                                   | independent     |
|                 |                                   | (e.g. &#42;.rb) |
|                 |                                   | files.          |
+-----------------+-----------------------------------+-----------------+
| &#42;From       |                                   |                 |
| rubygems-devel; |                                   |                 |
| intended for    |                                   |                 |
| gem             |                                   |                 |
| packages.&#42;  |                                   |                 |
+-----------------+-----------------------------------+-----------------+
| &#96;+%         | &#96;+/usr/share/gems+&#96;       | Top directory   |
| {gem_dir}+&#96; |                                   | for the Gem     |
|                 |                                   | structure.      |
+-----------------+-----------------------------------+-----------------+
| &#96;+%{gem     | &#96;+%{gem_dir}/                 | Directory with  |
| _instdir}+&#96; | gems/%{gem_name}-%{version}+&#96; | the actual      |
|                 |                                   | content of the  |
|                 |                                   | Gem.            |
+-----------------+-----------------------------------+-----------------+
| &#96;+%{ge      | &#96;+%{gem_instdir}/lib+&#96;    | The             |
| m_libdir}+&#96; |                                   | &#96;lib&#96;   |
|                 |                                   | folder of the   |
|                 |                                   | Gem.            |
+-----------------+-----------------------------------+-----------------+
| &#96;+%{g       | &#96;+%{gem_dir}/cache            | The cached Gem. |
| em_cache}+&#96; | /%{gem_name}-%{version}.gem+&#96; |                 |
+-----------------+-----------------------------------+-----------------+
| &#96;+%{        | &#                                | The Gem         |
| gem_spec}+&#96; | 96;+%{gem_dir}/specifications/%{g | specification   |
|                 | em_name}-%{version}.gemspec+&#96; | file.           |
+-----------------+-----------------------------------+-----------------+
| &#96;+%{ge      | &#96;+%{gem_dir}                  | The rdoc        |
| m_docdir}+&#96; | /doc/%{gem_name}-%{version}+&#96; | documentation   |
|                 |                                   | of the Gem.     |
+-----------------+-----------------------------------+-----------------+
| &#96;+%{gem_ex  | &#96;+%{\_libdir}/gems/           | The directory   |
| tdir_mri}+&#96; | ruby/%{gem_name}-%{version}+&#96; | for MRI Ruby    |
|                 |                                   | Gem extensions. |
+-----------------+-----------------------------------+-----------------+

### Interpreter independence and directory macros {#_interpreter_independence_and_directory_macros}

You might have noticed that the table above has different directories
for non-gem libraries on different ruby interpreters but only a single
set of directories for rubygem libraries. This is because code written
for one ruby interpreter will often run on all ruby interpreters that
Fedora ships (ruby, jruby, etc.). However, some code uses methods that
are not available on all interpreters (see &lt;&lt;Different
Interpreters Compatibility&gt;&gt;). Rubygems have a facility to ship
different versions of the code in the same gem so that the gem can run
on all versions of the interpreter, so we only need to have one common
directory for rubygems that all the interpreters can use.

The standard ruby &#96;+%{vendorlib}+&#96; directories lack this
facility. For this reason, non-gem libraries need to be placed in
per-interpreter directories and MUST have a separate subpackage (or
package depending on upstream) for each interpreter that they support.

## Libraries {#_libraries_3}

These guidelines only apply to Ruby packages whose main purpose is
providing a Ruby library; packages that mainly provide user-level tools
that happen to be written in Ruby MUST follow the
&lt;&lt;Applications,Ruby applications Guidelines&gt;&gt; instead.

### RubyGems {#_rubygems}

[RubyGems](https://rubygems.org/) are Ruby's own packaging format. Gems
contain a lot of the same metadata that RPM's need, making fairly smooth
interoperation between RPM and Gems possible. This guideline ensures
that Gems are packaged as RPMs in a way that such RPMs fit cleanly with
the rest of the distribution and makes it possible for the end user to
satisfy dependencies of a Gem by installing the appropriate RPM-packaged
Gem.

Both RPM's and Gems use similar terminology; there are specfiles,
package names, dependencies, etc. for both. To keep confusion to a
minimum, terms relating to Gem concepts will be explicitly referred to
with the word \'Gem\' prefixed, e.g., \'Gem specification\' (.gemspec).
An unqualified \'package\' in the following always means an RPM.

&#42; Spec files MUST contain a definition of &#96;+%{gem_name}+&#96;
which is the name from the Gem's specification.

&#42; The &#96;Source&#96; of the package MUST be the full URL to the
released Gem archive; the version of the package MUST be the Gem's
version.

&#42; The package MUST have &#96;BuildRequires: rubygems-devel&#96; to
pull in the macros needed to build.

&#42; There SHOULD NOT be any rubygem &#96;Requires&#96; nor
&#96;Provides&#96; listed, since those are autogenerated.

&#42; There SHOULD NOT be &#96;Requires: ruby(release)&#96;, unless you
want to explicitly specify Ruby version compatibility. The automatically
generated dependency on RubyGems (&#96;Requires: ruby(rubygems)&#96;) is
enough.

#### Filtering Requires and Provides {#_filtering_requires_and_provides_2}

Runtime requires and provides are automatically generated by RPM's
dependency generator. However, it can sometimes throw in additional
dependencies contrary to reality. To fix this, the dependency generator
needs to be overridden so that the additional dependencies can be
filtered out. See
[AutoProvidesAndRequiresFiltering](AutoProvidesAndRequiresFiltering.xml)
for details.

#### Building gems {#_building_gems}

Since gems aren't just an archive format but instead encapsulate both an
archive and information used for building the Ruby library, building an
RPM from a gem looks a little different from other RPMs.

A sample spec for building gems would look like this:

&#8230;. %prep %autosetup -p1 -n %{gem_name}-%{version}

&#35; Modify the gemspec if necessary

%build &#35; Create the gem as gem install only works on a gem file gem
build ../%{gem_name}-%{version}.gemspec

&#35; %%gem_install compiles any C extensions and installs the gem into
./%%gem_dir &#35; by default, so that we can move it into the buildroot
in %%install %gem_install

%install mkdir -p %{buildroot}%{gem_dir} cp -a ./%{gem_dir}/&#42;
%{buildroot}%{gem_dir}/

&#35; If there were programs installed: mkdir -p %{buildroot}%{\_bindir}
cp -a ./%{\_bindir}/&#42; %{buildroot}%{\_bindir}

&#35; If there are C extensions, copy them to the extdir. mkdir -p
%{buildroot}%{gem_extdir_mri} cp -a
.%{gem_extdir_mri}/{gem.build_complete,&#42;.so}
%{buildroot}%{gem_extdir_mri}/ &#8230;.

##### %prep {#_prep}

RPM (as of 4.14) can directly unpack gem archives, so we can call
&#96;gem unpack&#96; to extract the source from the gem. Then we call
&#96;+%setup -n %{gem_name}-%{version}+&#96; to tell rpm what the
directory the gem has unpacked into. At the same directory level, the
%{gem_name}-%{version}.gemspec file is created automatically as well.
This &#96;.gemspec&#96; file will be used to rebuild the gem later. If
we need to modify the &#96;.gemspec&#96; (for instance, if the version
of dependencies is wrong for Fedora or the &#96;.gemspec&#96; is using
old, no longer supported fields) we would do it here. Patches to the
code itself can also be done here.

##### %build {#_build_2}

Next we build the gem. Because &#96;+%gem_install+&#96; only operates on
gem archives, we next recreate the gem with &#96;gem build&#96;. The gem
file that is created is then used by &#96;+%gem_install+&#96; to build
and install the code into the temporary directory, which is
&#96;+./%{gem_dir}\\&#96; by default. We do this because the
\\&#96;%gem_install+&#96; command both builds and installs the code in
one step so we need to have a temporary directory to place the built
sources before installing them in &#96;+%install+&#96; section.

&#96;+%gem_install+&#96; macro accepts two additional options:

-n &lt;gem_file&gt;

:   Allows to override gem used for installation. This might get useful
    for converting legacy spec, so you might specify %{SOURCE0} as a gem
    for installation.

-d &lt;install_dir&gt;

:   Might override the gem installation destination. However we do not
    suggest to use this option.

:::: note
::: title
:::

The &#96;+%gem_install+&#96; macro MUST NOT be used to install into the
&#96;+%{buildroot}+&#96;
::::

##### %install {#_install_2}

Here we actually install into the &#96;+%{buildroot}\\&#96;. We create
the directories that we need and then copy what was installed into the
temporary directories into the \\&#96;%{buildroot}\\&#96; hierarchy.
Finally, if this ruby gem creates shared objects the shared objects are
moved into the arch specific \\&#96;%{gem_extdir_mri}+&#96; path.

#### Patching required gem versions {#_patching_required_gem_versions}

One common patching need is to change overly strict version requirements
in the upstream &#96;.gemspec&#96;. This could be because upstream's
&#96;.gemspec&#96; only mentions versions that they've explicitly tested
against but we know that a different version will also work or because
we know that the packages we ship have applied fixes for problematic
behavior without bumping the version number (for instance, backported
fixes). To adjust such dependencies, you can use the
&#96;+%gemspec_add_dep+&#96; and &#96;+%gemspec_remove_dep+&#96; macros.

For example, if you wanted to use any version of Aruba instead of the
overly specific version requested by upstream, you could use in
&#96;+%prep+&#96; section following two lines:

&#8230;. %gemspec_remove_dep -g aruba \'\~&gt; 0.14.2\' %gemspec_add_dep
-g aruba &#8230;.

:::: caution
::: title
:::

&#42;Use macros only on top of generated .gemspec&#42;: The
&#96;+%gemspec_add_dep+&#96; and &#96;+%gemspec_remove_dep+&#96; macros
work reliably only on .gemspec generated using the ruby spec command.
Please don't use the macros on upstream .gemspec files.
::::

:::: important
::: title
:::

&#42;Be sure to test&#42;: Do not simply change versions without testing
that the new version works. There are times the upstream is overly
strict but there are also times when the version requirement was
specified because a specific bug was encountered or the API changed in a
minor release.
::::

### Packaging for Gem and non-Gem use {#_packaging_for_gem_and_non_gem_use}

:::: important
::: title
:::

&#42;Packaging for non-Gem use is no longer needed&#42;: Originally,
rubygem modules were not placed in ruby's library path, so we packaged
rubygems for use with both gems and non-gems. This allowed code that
used &#96;require(\'ARubyModulePackagedAsAGem\');&#96; to function. The
current &#96;rubygem&#96; module adds all gems to the ruby library path
when it is require'd. So, packagers MUST NOT create non-Gem subpackages
of rubygems for new packages. Since the majority of Ruby packages in
Fedora are now packaged as installed gems, you might need to patch the
code to use &#96;require(\'rubygem\')&#96; as early in the program as
possible to ensure that these ruby components are properly found.
Packages for ruby gems that currently create a non-gem subpackage SHOULD
be adapted to stop shipping the non-gem subpackage (with a [proper
Obsoletes and
Provides](index.adoc&#35;renaming-or-replacing-existing-packages) in the
main rubygem package).
::::

### Non-Gem Packages {#_non_gem_packages}

Non-Gem Ruby packages MUST require ruby-devel package at build time with
a &#96;BuildRequires: ruby-devel&#96;, and MAY indicate the minimal ruby
version they need for building.

#### Build Architecture and File Placement {#_build_architecture_and_file_placement}

The following only affects the files that the package installs into
&#96;+%{ruby_vendorarchdir}\\&#96; and \\&#96;%{ruby_vendorlibdir}+&#96;
(the actual Ruby library files). All other files in a Ruby package MUST
adhere to the general Fedora packaging conventions.

:::: important
::: title
:::

&#42;Site versus Vendor&#42;: Previously,
&#96;+%{ruby_sitelibdir}\\&#96; and \\&#96;%{ruby_sitearchdir}\\&#96;
were used. However, as they are meant only for local installations,
please use \\&#96;%{ruby_vendorlibdir}\\&#96; and
\\&#96;%{ruby_vendorarchdir}+&#96; instead.
::::

#### Pure Ruby packages {#_pure_ruby_packages}

Pure Ruby packages MUST be built as noarch packages.

The Ruby library files in a pure Ruby package MUST be placed into
&#96;+%{ruby_vendorlibdir}+&#96; (or its proper subdirectory). The
specfile MUST use this macro.

#### Ruby packages with binary content/shared libraries {#_ruby_packages_with_binary_contentshared_libraries}

For packages with binary content, e.g., database drivers or any other
Ruby bindings to C libraries, the package MUST be architecture specific.

The binary files in a Ruby package with binary content MUST be placed
into &#96;+%{ruby_vendorarchdir}+&#96; (or its proper subdirectory). The
Ruby files in such a package SHOULD be placed into %{ruby_vendorlibdir}.
The specfile MUST use these macros.

For packages which create C shared libraries using &#96;extconf.rb&#96;

&#8230;. export CONFIGURE_ARGS=\'\--with-cflags=\'%{optflags}\'\'
&#8230;.

SHOULD be used to pass &#96;CFLAGS&#96; to &#96;Makefile&#96; correctly.
Also, to place the files into the correct folders during build, pass
&#96;\--vendor&#96; to &#96;extconf.rb&#96; like this:

&#8230;. extconf.rb \--vendor &#8230;.

## Applications {#_applications_2}

Applications are

&#42; programs that provide user-level tools or &#42; web applications,
typically built using Rails, Sinatra or similar frameworks.

The RPM packages MUST obey FHS rules. They SHOULD be installed into
&#96;+%{\_datadir}+&#96;. The following macro can help you:

&#8230;. %global app_root %{\_datadir}/%{name} &#8230;.

These packages typically have no &#96;Provides&#96; section, since no
other libraries or applications depend on them.

Here's an abbreviated example:

&#8230;. %global app_root %{\_datadir}/%{name}

Summary: Deltacloud REST API Name: deltacloud-core Version: 0.3.0
Release: 3%{?dist} Group: Development/Languages License: Apache-2.0 AND
MIT URL: <https://incubator.apache.org/deltacloud> Source:
[https://rubygems.org/gems/%{name}-%{version}.gem](https://rubygems.org/gems/%{name}-%{version}.gem)
Requires: rubygem-haml &#35;&#8230; Requires(post): chkconfig
&#35;&#8230; BuildRequires: rubygem-haml &#35;&#8230; BuildArch: noarch

%description The Deltacloud API is built as a service-based REST API.
You do not directly link a Deltacloud library into your program to use
it. Instead, a client speaks the Deltacloud API over HTTP to a server
which implements the REST interface.

%package doc Summary: Documentation for %{name} Group: Documentation
Requires:%{name} = %{version}-%{release}

%description doc Documentation for %{name}

%prep %setup -q -n %{name}-%{version}

%build

%install mkdir -p %{buildroot}%{app_root} mkdir -p
%{buildroot}%{\_initddir} mkdir -p %{buildroot}%{\_bindir} cp -r &#42;
%{buildroot}%{app_root} mv
%{buildroot}%{app_root}/support/fedora/%{name} %{buildroot}%{\_initddir}
find %{buildroot}%{app_root}/lib -type f \| xargs chmod -x chmod 0755
%{buildroot}%{\_initddir}/%{name} chmod 0755
%{buildroot}%{app_root}/bin/deltacloudd rm -rf
%{buildroot}%{app_root}/support rdoc \--op
%{buildroot}%{\_defaultdocdir}/%{name}

%post &#35; This adds the proper /etc/rc&#42;.d links for the script
/sbin/chkconfig \--add %{name}

%files %{\_initddir}/%{name} %{\_bindir}/deltacloudd %dir %{app_root}/
%{app_root}/bin &#35;&#8230;

%files doc %{\_defaultdocdir}/%{name} %{app_root}/tests
%{app_root}/%{name}.gemspec %{app_root}/Rakefile

%changelog &#35;&#8230; &#8230;.

Note, that although the source is a RubyGem, we have to install the
files manually under %{\_datadir}/%{name}, %{\_bindir}, etc. to follow
FHS and general packaging guidelines. If additional Fedora specific
files (systemd &#96;.service&#96; files, configurations) are required,
they SHOULD be

&#42; added via another &#96;+%SOURCE+&#96; tags

&#8230;. Source1: deltacloudd-fedora &#8230;.

&#42; placed into appropriate locations during &#96;+%install+&#96;
stage

&#8230;. install -m 0755 %{SOURCE1} %{buildroot}%{\_bindir}/deltacloudd
&#8230;.

## Running test suites {#_running_test_suites}

If there is test suite available for the package (even separately, for
example not included in the gem but available in the upstream
repository), it SHOULD be run in &#96;+%check+&#96;. The test suite is
the only automated tool which can assure basic functionality of the
package. Running it is especially helpful when mass rebuilds are
required. You MAY skip test suite execution when not all build
dependencies are met but this MUST be documented in the specfile. The
missing build dependencies to enable the test suite SHOULD be packaged
for Fedora as soon as possible and the test suite re-enabled.

The tests SHOULD NOT be run using Rake, as Rake almost always draws in
some unnecessary dependencies like hoe or gemcutter. For similar
reasons, a dependency on Bundler SHOULD be avoided. Also, code coverage
frameworks such as SimpleCov and Coveralls SHOULD be avoided.

### Testing With Different Ruby Implementations {#_testing_with_different_ruby_implementations}

To run tests with different Ruby implementation such as JRuby, add
&#96;BuildRequires: jruby&#96;. Then use Rubypick's interpreter
switching:

&#8230;. ruby *jruby* -Ilib -e \'Dir.glob \'./test/test\_&#42;.rb\',
&amp;method(:require)\' &#8230;.

If your package is running unittests for ruby-mri and it is intended to
run under alternate interpreters then it needs to run the unittests
under all alternate interpreters as well. This is the only method we
have to check compatibility of the code under each interpreter. The same
rules apply that you can omit this if libraries you need are unavailable
for a specific alternate interpreter but you MUST have a comment to
explain.

### Testing frameworks usage {#_testing_frameworks_usage}

The Ruby community supports many testing frameworks. The following
sections demonstrate how several to execute test suites using the more
common of them.

#### MiniTest / Test::UNIT {#_minitest_testunit}

MiniTest as well as Test::UNIT are shipped with Ruby. To use them, you
need to use &#96;BuildRequires: rubygem-minitest&#96; or
&#96;BuildRequires: rubygem-testunit&#96; respectively. To execute the
test suite you can use something like:

&#8230;. %check ruby -Ilib -e \'Dir.glob
\'./test/&#42;&#42;/&#42;\_test.rb\', &amp;method(:require)\' &#8230;.

You might need to adjust &#96;+-Ilib+&#96; to be &#96;+-Ilib:test+&#96;,
or you could need to use a slightly different matching pattern for
&#96;+test\_&#42;.rb+&#96;, etc. Packagers are expected to use the right
pattern for each gem.

#### RSpec {#_rspec}

To run tests using RSpec &gt;= 3 you add &#96;BuildRequires:
rubygem-rspec&#96; and use something like:

&#8230;. %check rspec -Ilib spec &#8230;.

### Test suites not included in the package {#_test_suites_not_included_in_the_package}

Sometimes you have to get the tests separately from upstream's gem
package. As an example lets suppose you're packaging
&#96;rubygem-delorean&#96;, version 1.2.0, which is hosted on Github.
Tests are not included in the Gem itself, so you need to get them and
adjust the specfile accordingly:

&#8230;. &#35; git clone <https://github.com/bebanjo/delorean.git>
&amp;&amp; cd delorean &#35; git checkout v1.2.0 &#35; tar -czf
rubygem-delorean-1.2.0-specs.tgz spec/ Source1:
%{name}-%{version}-specs.tgz

&#35; &#8230; %prep %setup -q -n %{gem_name}-%{version} -b 1

&#35; &#8230;

%check pushd ./%{gem_instdir} &#35; Link the test suite into the right
place in source tree. ln -s %{\_builddir}/spec .

&#35; Run tests rspec spec popd

&#35; &#8230; &#8230;.

&#42; Make sure to include the version of the tests in the source name,
so that when updating to new version, rpmbuild will fail because it
won't find the proper &#96;+%{SOURCE1}+&#96; (and this will remind you
to update the tests, too). &#42; Add the commands you used to get the
tests into the specfile as comments. This will make it a lot easier the
next time you will need to get them. &#42; Run the tests as you normally
would.

# Rust Packaging Guidelines {#_rust_packaging_guidelines}

[Rust](https://www.rust-lang.org) is a strongly and statically typed,
compiled programming language that supports concepts from both
imperative and functional programming.

Because there is not yet a stable Rust ABI, and because conditional
compilation is a widely used feature in the Rust ecosystem, Rust
libraries (\'crates\') can not be distributed in compiled form, and are
instead distributed as source code.

This document covers how to handle Rust code in packages, specific to
the different ways in which projects can be set up:

&#42; [Rust \'crates\'](&#35;_rust_crates): packages that are
individually published on [crates.io](https://crates.io), the official
package registry for Rust (primarily libraries, but also
\'single-crate\' applications) &#42; [Non-crate Rust
projects](&#35;_non_crate_rust_projects): Rust projects that are not
published on crates.io, or larger projects that are comprised of many
crates (cargo workspace) &#42; [Python projects](&#35;_python_projects)
with a \'native\' component implemented in Rust: usually built with
[setuptools_rust](https://github.com/PyO3/setuptools-rust) or
[maturin](https://github.com/PyO3/maturin) &#42; [mixed Rust / C/C++
projects](&#35;_mixed_rust_cc_projects) where parts of the project are
implemented in Rust: either built by wrapping cargo, or by utilizing
[meson](https://mesonbuild.com/Rust.html)\'s limited support for
directly building Rust code

The [rust2rpm](https://pagure.io/fedora-rust/rust2rpm) tool can be used
to generate spec files for Rust crates from cargo / crate metadata. It
is designed to produce spec files that are in line with the (Rust)
Packaging Guidelines.

There are also guidelines for [packaging shared
libraries](&#35;_building_shared_libraries_with_cargo_c) that are
implemented in Rust (usually built and installed with
[cargo-c](https://crates.io/crates/cargo-c)).

## Generic rules {#_generic_rules}

This section covers rules that apply to *all* packages that ship Rust
code.

### Compiler flags {#_compiler_flags}

Similarly to other language ecosystems in Fedora, there is a
standardized set of compiler flags that &#42;MUST&#42; be passed to the
Rust compiler.

The defaults for Rust are defined in the &#96;%build_rustflags&#96;
macro from the &#96;rust-srpm-macros&#96; package. It is part of the
default buildroot on Fedora 39+, where the &#96;%set_build_flags&#96;
macro automatically sets the &#96;\$RUSTFLAGS&#96; environment variable
based on this macro.

For compatibility with older releases or EPEL, this environment variable
can be set manually at the start of &#96;%build&#96; and
&#96;%check&#96; in package's spec files:

``` shell
export RUSTFLAGS='%build_rustflags'
```

This is not necessary for packages that use the &#96;%cargo_prep&#96;,
&#96;%cargo_build&#96;, and &#96;%cargo_test&#96; macros, which
configure &#96;cargo&#96; to use the default &#96;%build_rustflags&#96;
directly.

### Mandatory &#96;BuildRequires&#96; {#_mandatory_96buildrequires96}

The RPM macros that provide basic functionality for building Rust code
are included in &#96;rust-rpm-macros&#96;, which is part of the default
buildroot in Fedora, as it is a dependency of
&#96;redhat-rpm-config&#96;. When building for ELN or EPEL8, this is not
the case, and packages need to use &#96;BuildRequires:
rust-toolset&#96;.

Packages that build Rust code with cargo - directly or indirectly - or
which call any of the &#96;+%cargo\_&#42;+&#96; macros, &#42;MUST&#42;
add &#96;+BuildRequires: cargo-rpm-macros+&#96;, which provides the
implementations of all &#96;+%cargo\_&#42;+&#96; macros. This package is
not part of the default buildroot, since it pulls in additional
dependencies (i.e. a Python interpreter).

### Dynamically generated &#96;BuildRequires&#96; for crate dependencies {#_dynamically_generated_96buildrequires96_for_crate_dependencies}

With Semantic Versioning (*\'SemVer\'*) being the only supported
versioning scheme for Rust crates, dependencies on Rust libraries are
almost exclusively specified as *\'this version or any newer version
that is API-compatible with it\'*, i.e. a range of supported versions.

These ranges of supported versions need to be correctly translated into
RPM dependencies, otherwise a wrong version of a dependency might get
pulled in for builds, causing unhelpful error messages about missing
dependencies.

Since dependencies of Rust projects change frequently, packages for
projects that build Rust code with cargo &#42;MUST&#42; use dynamically
generated &#96;BuildRequires&#96; by calling the
&#96;%cargo_generate_buildrequires&#96; macro in the
&#96;%generate_buildrequires&#96; scriptlet.

For example, a dependency on &#96;serde = \'1.0.100\'&#96; specified in
a project's &#96;Cargo.toml&#96; metadata (a dependency on the crate
named \'serde\', with version \'1.0.100\' or any version API-compatible
with \'1.0.100\', with default features enabled) would cause a
dependency like this to be generated for RPM:

&#8230;. BuildRequires: (crate(serde/default) &gt;= 1.0.100 with
crate(serde/default) &lt; 2.0.0\~) &#8230;.

Refer to the section about [RPM macros](&#35;_rpm_macros) for how to
pass feature flags to this macro.

### License tags {#_license_tags}

Similar to other languages that produce statically linked binaries, Rust
executables (and shared libraries) contain code that originates in other
packages (i.e. packages for other Rust crates), which in turn are
covered by different license terms.

This needs to be taken into account by maintaining a separate
&#96;License&#96; tag for the subpackage that contains these binaries.
More information about &#96;License&#96; tags is available from the
[Fedora Legal
docs](https://docs.fedoraproject.org/en-US/legal/license-field/).

The &#96;cargo-rpm-macros&#96; package provides two RPM macros that help
with filling the &#96;License&#96; tag correctly for projects that are
built with &#96;cargo&#96;:

- &#96;%cargo_license_summary&#96;

This macro determines and prints a summary of all the licenses of the
Rust crates that end up statically linked into final binaries (properly
excluding build-only or test-only dependencies). This summary can then
be copied from the build log into the spec file as a comment. The actual
contents of the &#96;License&#96; tag can then be obtained by
constructing a conjunction of these individial licenses (with SPDX
&#96;AND&#96; operators).

- &#96;%cargo_license&#96;

This macro determines and prints a complete breakdown of all Rust crates
that end up statically linked into final binaries (according to the same
logic as in the &#96;%cargo_license_summary&#96; macro), their versions,
*and* their individual license expressions. Generating this list
dynamically at build-time ensures that its contents always match the
actual dependencies.

Both macros accept the same arguments as other &#96;%cargo\_&#42;&#96;
macros (&#96;-a&#96;, &#96;-n&#96;, &#96;-f&#96;), and for their output
to match the actual binaries, the same flags &#42;MUST&#42; be passed to
them and &#96;%cargo_build&#96;.

### Vendored dependencies {#_vendored_dependencies_2}

[In
general](https://docs.fedoraproject.org/en-US/packaging-guidelines/&#35;bundling),
packages &#42;SHOULD NOT&#42; use bundled crate dependencies, whenever
possible.

Whenever vendored / bundled crate dependencies *are* used (no matter
which mechanism is used for the purpose), all bundled crate dependencies
&#42;MUST&#42; be declared with virtual &#96;Provides&#96; in the format
&#96;Provides: bundled(crate(\$crate)) = \$version&#96; in the
subpackage that contains the Rust component. For example, these virtual
&#96;Provides&#96; are used to determine the impact of security
vulnerabilities on packages that use vendored Rust dependencies.

There are also two situations in which bundling at least *some* Rust
crates is usually unavoidable:

#### Replacing git dependencies {#_replacing_git_dependencies}

One of the types of dependencies cargo supports are git snapshots, which
are usually used to reference either a specific commit, or a reference
to a downstream fork of a crate.

The project &#42;SHOULD&#42; be patched to use a version of this crate
that is available on [crates.io](https://crates.io) instead, if that is
possible. If it turns out that depending on a git snapshot is no longer
necessary, this patch &#42;SHOULD&#42; be submitted to the upstream
project.

If the dependency is not published on [crates.io](https://crates.io), or
if the versions published there are not a suitable replacement, a git
snapshot of the crate can be bundled. This can be achieved by creating
and supplying a tarball with the git snapshot as a separate source,
unpacking the tarball in &#96;%prep&#96;, and patching
&#96;Cargo.toml&#96; to replace the git-based dependency with a
path-based dependency. Adding this subproject as a workspace member
ensures that its dependencies are included during dependency resolution.

#### Replacing patched crate sources {#_replacing_patched_crate_sources}

Another way in which cargo supports specifying modified dependencies is
by \'patching\' a crate source, specifying an alternative source for
specific crates - which will likely be either git references or
path-based dependencies that are present to override a crate that is
published on [crates.io](https://crates.io) with a (modified) local
copy, or a git repository that points to a (modified) fork of the crate.

These replacements &#42;SHOULD&#42; be dropped in favor of using only
published versions of crates. If that is not possible, they must be
replaced by path-based dependencies, similar to the process described
for [git-type dependencies](&#35;_replacing_git_dependencies).

#### Using vendor tarballs {#_using_vendor_tarballs}

Support for building with vendored dependencies was added in version 25
of cargo-rpm-macros and rust2rpm.

&#42; The &#96;%cargo_prep&#96; macro accepts a &#96;-v \$VENDOR&#96;
argument, where &#96;\$VENDOR&#96; is the path to the directory that
contains the vendored crate dependencies. When this argument is passed,
the generated cargo configuration is set up for building against
dependencies in this directory instead of dependencies from the
system-wide registry. &#42; The &#96;%cargo_generate_buildrequires&#96;
macro &#42;MUST NOT&#42; be called when using vendored dependencies.
&#42; The &#96;%cargo_vendor_manifest&#96; macro generates a manifest
(&#96;cargo-vendor.txt&#96;) that lists the names and versions of all
crates in the vendor tarball. This macro &#42;MUST&#42; be called (for
example, in the &#96;%build&#96; scriptlet), and the generated file
&#42;MUST&#42; be added as a &#96;%license&#96; file in the appropriate
package's list of &#96;%files&#96;. An RPM generator parses this file
and generates appropriate virtual &#96;Provides&#96; for all bundled
crates, as is required for any bundled dependencies. &#42; Packages that
build with vendored dependencies &#42;MUST NOT&#42; provide a Rust
library interface (i.e. in &#96;-devel&#96; subpackages), because the
resulting packages would have broken dependencies.

Typically, the &#96;%prep&#96; scriptlet will look like this when using
vendored dependencies (assuming &#96;Source1&#96; is the vendor tarball,
and it contains a top-level &#96;vendor&#96; directory):

``` rpm
%prep
%autosetup -%{crate}-%{version} -p1 -a1
%cargo_prep -v vendor
```

The necessary spec file adaptations and the generation of the vendor
tarball itself happen automatically when running rust2rpm in \'vendor\'
mode.

## Rust crates {#_rust_crates}

A large part of the process of packaging Rust crates can (and *should*)
be automated by using
[rust2rpm](https://pagure.io/fedora-rust/rust2rpm). It is designed to
generate spec files that are compliant with both the general and the
Rust Packaging Guidelines.

Additionally, due to some properties of packages for Rust crates (i.e.
subpackages that correspond to crate features / optional dependencies),
[rust2rpm](https://pagure.io/fedora-rust/rust2rpm) &#42;MUST&#42; be
re-run for every new version of a crate to ensure that generated feature
subpackages stays in sync with crate metadata.

### rust2rpm {#_rust2rpm}

The recommended way to write spec files for Rust crates is to use
[rust2rpm](https://pagure.io/fedora-rust/rust2rpm), and apply any
necessary modifications on top of the generated spec file.

There are a few common situations in which automatically generated spec
files need manual changes:

&#42; invalid &#96;Summary&#96; / &#96;%description&#96;: The heuristics
for generating the &#96;Summary&#96; or &#96;%description&#96; for the
package from the crate metadata can fail to produce valid values (i.e.
&#96;Summary&#96; tag that is too long). In this case, the
&#96;Summary&#96; needs to be shortened manually. This can also be
overridden in the package-specific rust2rpm configuration file. &#42;
unwanted dependencies / subpackages: Some crates provide non-default /
optional features that are either unnecessary (i.e. only applicable to
non-Linux systems), or have additional dependencies that are not
packaged for Fedora. These features and unavailable optional
dependencies &#42;MUST&#42; be removed from crate metadata - otherwise,
the package will either fail to build, or produce subpackages with
broken dependencies. &#42; nightly-only / unstable features: Some crates
provide features that are only available on a nightly version of the
Rust compiler, or features that are unstable and require an opt-in by
passing environment variables. Features like these &#42;SHOULD&#42; be
removed from crate metadata, since they either cannot work (Fedora ships
only the stable Rust toolchain) or are not feasible to support. &#42;
unwanted / unnecessary files (\'bloat\'): Some projects include files
that are not required for the crate to function properly (files for CI
settings, development / helper scripts, etc.). Files like these
&#42;SHOULD&#42; be prevented from being installed (by adding /
modifying the &#96;package.include&#96; or &#96;package.exclude&#96;
settings in the crate metadata). It is recommended to submit changes
like this to the upstream project. &#42; incompatible compiler flags:
Some crates include custom settings for the &#96;release&#96; profile
that are incompatible with RPM packaging. These settings &#42;MUST&#42;
be removed from the &#96;release&#96; profile by patching
&#96;Cargo.toml&#96;.

Crates that provide Rust bindings for C libraries usually require some
additional changes (if possible):

&#42; linking against system libraries: This often requires making some
dependencies non-optional and / or modifying &#96;build.rs&#96; scripts
to unconditionally link against system libraries instead of building and
statically linking a bundled copy of the library. &#42; regenerating
Rust bindings (and tests for them) at build-time: This too often
requires making the &#96;bindgen&#96; dependency non-optional and / or
modifying &#96;build.rs&#96; to cause regeneration of Rust bindings at
build-time.

Note that patching &#96;Cargo.toml&#96; files (especially changing the
set of optional dependencies and features) &#42;MUST&#42; be done by
running &#96;rust2rpm -p&#96;, since changes like these affect spec file
generation (i.e. the list of generated subpackages), which is only
correctly taken into account if the patch is created *before* generation
of the spec file.

It is recommended to track non-empty &#96;+rust2rpm.toml+&#96;
configuration files in the package repository alongside the generated
&#96;+.spec+&#96; file.

### Package naming {#_package_naming_3}

Packages for Rust crates from [crates.io](https://crates.io)
&#42;MUST&#42; use &#96;rust-\$crate&#96; as the name of the source
package (where &#96;\$crate&#96; is the name of the project on
[crates.io](https://crates.io)).

This ensures that there are no name collisions between Rust crates
published on [crates.io](https://crates.io) and Rust crates packaged for
Fedora.

When generating a package for a Rust crate that contains executable
targets, the convention followed by
[rust2rpm](https://pagure.io/fedora-rust/rust2rpm) is to generate a
subpackage with a name that matches the crate name (i.e. the
&#96;rust-\$crate&#96; source package will have a &#96;\$crate&#96;
subpackage). If necessary, this subpackage can be renamed, for example,
if the name does not match expectations, or if it would conflict with
another already existing package.

### Package versioning {#_package_versioning}

Projects that are built with cargo and / or published on
[crates.io](https://crates.io) follow Semantic Versioning (with small
cargo-specific tweaks). Since SemVer strings can contain characters that
are invalid in RPM version strings, they &#42;MUST&#42; be translated to
be RPM-compatible.

For example, pre-releases are denoted by a &#96;-&lt;pre&gt;&#96; suffix
in SemVer, but the &#96;-&#96; character is invalid in RPM Versions.
This can be solved by replacing &#96;-&#96; with the &#96;\~&#96;
character, which denotes pre-releases in RPM version strings. This
translation happens automatically for the &#96;Version&#96; tag when
generating a spec file with
[rust2rpm](https://pagure.io/fedora-rust/rust2rpm), and the \'upstream\'
version is stored in a separate macro that can be used to refer to the
\'original\' version string.

Additionally, some Rust crates carry extra \'build\' metadata in their
versions (a &#96;+&lt;build&gt;&#96; suffix). This format is primarily
used to carry information about the version of a bundled C library. This
&#96;+&lt;build&gt;&#96; suffix &#42;MUST&#42; be removed from crate
metadata with a patch, since it can interfere with RPM dependency /
version resolution. This happens automatically when using rust2rpm
version 25 or newer.

### Package sources {#_package_sources}

The canonical source of Rust crates is [crates.io](https://crates.io).
Projects from [crates.io](https://crates.io) &#42;MUST&#42; be packaged
from the sources that are published there (i.e. by using the
&#96;+%{crates_source}+&#96; macro).

If the sources published on [crates.io](https://crates.io) do not
contain all files that are necessary for creating the package (for
example, missing &#96;.desktop&#96; file or man pages), the upstream
sources can be used as an *additional* source, but they &#42;MUST
NOT&#42; be used for building the crate itself. It is recommended to
file an issue with the upstream project about including these additional
files in published crates.

Alternatively, if the project in question does not provide a Rust
library interface, it can be packaged as a [Non-crate Rust
project](&#35;_non_crate_rust_projects) using the upstream sources
instead.

### Crate license {#_crate_license}

Most tooling support for determining licenses requires accurate metadata
about licenses in crate metadata, including the
&#96;%cargo_license&#42;&#96; macros, and other third-party tools like
&#96;cargo-license&#96; and &#96;cargo-deny&#96;.

For this reason, the license metadata for all Rust crates packaged for
Fedora &#42;MUST&#42; match the license tag of the Fedora package
itself. Any crates that set &#96;package.license-file&#96; in their
metadata (which is reserved for non-standard / non-SPDX licenses)
&#42;MUST&#42; be patched to set &#96;package.license&#96; in their
metadata, and an accurate SPDX expression &#42;MUST&#42; be provided
instead. Patches like this &#42;SHOULD&#42; be submitted upstream.

### Subpackages for crate features {#_subpackages_for_crate_features}

Optional features / dependencies of Rust crates are translated into RPM
subpackages to support resolving dependencies for features and optional
dependencies of crates. The list of crate \'features\' (including any
implicitly defined features for optional dependencies) &#42;MUST&#42; be
kept in sync with the list of subpackages, i.e. for every feature
&#96;\$foo&#96; of the crate &#96;\$crate&#96;, there must be a
subpackage with name &#96;rust-\$crate+\$foo-devel&#96;, and vice-versa.
This is required for RPM generators for &#96;Provides&#96; and
&#96;Requires&#96; for these optional features / dependencies to work
correctly.

If optional features that are *not* part of the default feature set are
unused and would pull in additional (possibly unavailable) dependencies,
the package &#42;MAY&#42; omit subpackages for these specific feature
names. However, care needs to be taken that the features corresponding
to the ommitted subpackages are not \'reachable\' via subpackages that
have *not* been omitted, since this would result in packages with
unsatisfiable dependencies. Disabling optional features sometimes cannot
be handled correctly simply by omitting subpackages for specific
features. In these cases, the crate metadata in &#96;Cargo.toml&#96;
needs to be patched accordinly instead.

Beware that the \'default\' feature is always implicitly defined by
cargo, even if the crate metadata does not contain a
&#96;\[features\]&#96; table or an explicitly defined \'default\'
feature, so the subpackage for the \'default\' feature will be present
in all packages for Rust crates with a library interface.

### RPM generators for &#96;Provides&#96; and &#96;Requires&#96; {#_rpm_generators_for_96provides96_and_96requires96}

The cargo-rpm-macros package includes RPM generators for automatically
generating &#96;Provides&#96; and &#96;Requires&#96; for Rust crates
that comply with the Packaging Guidelines (i.e. install their files into
the correct location, &#96;+%{crate_instdir}+&#96;).

It is recommended to verify that the generated &#96;Provides&#96; and
&#96;Requires&#96; are sane - for example, the following
&#96;Provides&#96; and &#96;Requires&#96; must be present to ensure
correct inter-subpackage dependencies:

&#42; the main &#96;rust-\$crate-devel&#96; subpackage &#42;MUST&#42;
provide &#96;+crate(\$crate) = %{version}\\&#96; \\&#42; the
\\&#96;rust-\$crate\$feature-devel&#96; subpackages &#42;MUST&#42;
provide &#96;+crate(\$crate/\$feature) = %{version}\\&#96; and require
\\&#96;+crate(\$crate) = %{version}&#96; (i.e.
&#96;rust-\$crate-devel&#96;)

Additionally, dependencies on external Rust crates must be as expected:

&#42; the main &#96;rust-\$crate-devel&#96; subpackage &#42;MUST&#42;
require the virtual &#96;Provides&#96; for all non-optional crate
dependencies &#42; the &#96;rust-\$crate+\$feature-devel&#96;
subpackages &#42;MUST&#42; require the virtual &#96;Provides&#96; for
the optional crate dependencies and features that are listed as the
feature's dependencies in crate metadata

### Packaging multiple versions {#_packaging_multiple_versions}

In most circumstances, the latest version of a crate &#42;SHOULD&#42; be
packaged, and - if possible - packagers &#42;SHOULD&#42; port crates to
use the latest available version of their dependencies, and submit these
patches to upstream to limit divergence between the upstream project and
the Fedora package.

However, there are two common scenarios in which it is often necessary
to provide packages for multiple versions of a library crate
simultaneously:

&#42; It is not feasible to port a crate to the version of a crate
dependency in Fedora due to large API changes between the required and
the packaged version. &#42; The number of packages affected by a
required SemVer-incompatible library update is very large.

In these cases, a \'compat package\' can be created for the older
version (i.e. usually the current version), and the suffix-less package
can be updated to the newer version.
[rust2rpm](https://pagure.io/fedora-rust/rust2rpm) supports
automatically creating \'compat packages\' with names that are compliant
with the [Naming Guidelines for this
case](https://docs.fedoraproject.org/en-US/packaging-guidelines/Naming/&#35;multiple)
*and* compatible with the restrictions of Semantic Versioning by using
the &#96;rust2rpm \--compat&#96; flag.

All \'compat packages\' for Rust crates &#42;MUST&#42; follow the
guidelines for Rust crates, and two additional rules apply when creating
them:

&#42; For crates that also includes an executable, only the package for
the *latest* version can include this executable, and it &#42;MUST
NOT&#42; be built and included in any older versions, to prevent both
the name of the executable under &#96;/usr/bin&#96; and the name of the
subpackage would conflict between the old and the new version of the
package. &#42; The packager &#42;SHOULD&#42; check whether running tests
in the old version of the crate would cause additional, potentially
undesirable dependencies, for example, older versions of other
dependencies that would require creating additional \'compat
packages\' - in this case, tests &#42;SHOULD&#42; be disabled (i.e. by
flipping the &#96;check&#96; bcond).

### The &#96;check&#96; bcond {#_the_96check96_bcond}

The behaviour of some RPM macros depends on the presence and value of
the &#96;\_with_check&#96; macro, i.e. if &#96;%bcond_without check&#96;
or &#96;%bcond_with check&#96; are used in the spec file - notably, the
&#96;%cargo_generate_buildrequires&#96; macro only includes
&#96;dev-dependencies&#96; (i.e. dependencies that are only used for
compiling and / or running a project's test suite with cargo) if the
&#96;check&#96; bcond is enabled.

Additionally, packages for Rust crates that are generated by
[rust2rpm](https://pagure.io/fedora-rust/rust2rpm) use the value of this
macro to determine if the &#96;%check&#96; scriptlet is run.

Packages for Rust crates &#42;MUST&#42; set this bcond to avoid
unexpected behaviour of the &#96;%cargo\_&#42;&#96; macros, by either
explicitly *enabling* or *disabling* tests.

### Running tests {#_running_tests_2}

Rust crates can have three different kinds of tests in their test
suites:

&#42; *\'unit tests\'*: These tests are included alongside library /
application source code in the &#96;src/&#96; directory, and can
reference private APIs (similar to \'glass-box\' tests). &#42;
*\'integration tests\'*: These tests are usually separate files under
the &#96;tests/&#96; directory, and they can only rely on public API of
the tested crate (similar to \'black-box\' tests). &#42; *\'doctests\'*:
These tests are automatically extracted from code blocks in Markdown
documentation, which is often used as a mechanism to ensure that code
snippets in documentation for public methods are correct and continue to
compile.

By default, running &#96;cargo test&#96; (i.e. by calling the
&#96;%cargo_test&#96; macro), all three kinds of tests are run. They can
also be invoked separately (for example, because parts of the test suite
or large data files are not included in published sources) by passing
through filtering arguments to the underlying &#96;cargo test&#96;
command:

&#42; &#96;%cargo_test --- \--lib&#96;: only run *\'unit tests\'* for
the library interface &#42; &#96;%cargo_test --- \--bin foo&#96;: only
run *\'unit tests\'* for binary \'foo\' &#42;
&#96;%cargo_test --- \--doc&#96;: only run *\'doctests\'* &#42;
&#96;%cargo_test --- \--test bar&#96;: only run *\'integration test\'*
\'bar\'

This can be combined with additional flags to skip tests with specific
names (or that contain a specific string in their name) by passing the
&#96;\--skip&#96; argument through to the test harness (can be specified
multiple times):

&#8230;. %cargo_test --- \--lib --- \--skip foo::bar::tests::test1
&#8230;.

By default, cargo uses substring matching to match &#96;\--skip&#96;
arguments and actual names of tests, which can be turned off by using
the &#96;\--exact&#96; flag.

If any tests are skipped or disabled, the package &#42;SHOULD&#42;
include comments that explain why this is the case, and include links to
upstream issues, if available.

## Non-crate Rust projects {#_non_crate_rust_projects}

This section applies to Rust projects that are not packaged from sources
on crates.io.

The most common cases are

&#42; applications that do not provide a library interface, &#42;
projects comprised of multiple crates (cargo workspaces) that may or may
not be published (or useful) separately, and &#42; Python packages
implemented in Rust ([covered below](&#35;_python_projects)).

Packages like this &#42;MUT NOT&#42; ship crate sources in
&#96;+%{cargo_registry}\\&#96;, i.e. they cannot ship
\\&#96;-devel\\&#96; subpackages that contain crate sources or have
subpackages that have virtual provides for \\&#96;+crate(\\&#8230;) =
%{version}&#96;.

### Package naming {#_package_naming_4}

Packages for non-crate Rust projects &#42;MUST&#42; be named according
to the generic [Naming
Guidelines](https://docs.fedoraproject.org/en-US/packaging-guidelines/Naming/),
i.e. they &#42;MUST NOT&#42; use a &#96;rust-&#96; prefix for the source
package name.

### Package sources {#_package_sources_2}

The generic guidelines for [referencing
sources](https://docs.fedoraproject.org/en-US/packaging-guidelines/SourceURL/)
apply.

The &#96;+%{crates_source}+&#96; macro &#42;SHOULD NOT&#42; be used for
packages like this, even when packaging a Rust crate that is also
published on crates.io.

### RPM macros {#_rpm_macros_6}

Any &#96;-a&#96; and &#96;-n&#96; flags or &#96;-f&#96; arguments that
are passed to &#96;%cargo_generate_buildrequires&#96; are applied to
*all* workspace members during dependency resolution.

The &#96;+%cargo_install+&#96; macro &#42;SHOULD NOT&#42; be used for
packages like this. Instead, use &#96;install&#96; or &#96;cp&#96; to
copy built executables or shared libraries from
&#96;+target/rpm/&#42;+&#96; into the buildroot explicltly, as needed.

## Python projects {#_python_projects}

Python packages that use
[setuptools_rust](https://github.com/PyO3/setuptools-rust) or
[maturin](https://github.com/PyO3/maturin) to build a \'native\' Python
extension also need to apply the [generic rules](&#35;_generic_rules)
for Rust packages in addition to following the [Python Packaging
Guidelines](https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/).

Both [setuptools_rust](https://github.com/PyO3/setuptools-rust) and
[maturin](https://github.com/PyO3/maturin) build the native Python
extension by calling cargo internally, so the basic setup for projects
that build with cargo is required for packages like this as well.

This includes calling &#96;%cargo_prep&#96; in &#96;%prep&#96; to set up
the build environment for cargo, and using
&#96;%cargo_generate_buildrequires&#96; to dynamically generate the
appropriate &#96;BuildRequires&#96; for Rust crate dependencies.

Additionally, &#96;%cargo_license&#96; and / or
&#96;%cargo_license_summary&#96; &#42;MUST&#42; be used to determine the
licenses that apply to the statically linked Python extension.

The packager also &#42;MUST&#42; ensure that the default [compiler
flags](&#35;_compiler_flags) are passed to rustc, and that debuginfo is
not stripped during the build process due to settings in the
&#96;setuptools-rust&#96; or &#96;maturin&#96; configuration.

## Mixed Rust / C/C++ projects {#_mixed_rust_cc_projects}

Handling of projects that include both C/C++ and Rust code depends on
how building the Rust code is integrated into the project's build
system.

Independent of the specific setup, the correct [compiler
flags](&#35;_compiler_flags) &#42;MUST&#42; be passed to rustc, and the
License tag of the package that contains the Rust component
&#42;MUST&#42; take the licenses of statically linked crates into
account.

### Building with cargo internally {#_building_with_cargo_internally}

Projects with build systems that call cargo internally to build Rust
components &#42;MUST&#42; follow the same guidelines as other projects
that build Rust code with cargo.

Packages &#42;MUST&#42; ensure that the cargo calls that are internal to
the project's build system do not pass flags or arguments that are
incompatible with either the default [compiler
flags](&#35;_compiler_flags) or cargo options that are set in the
&#96;%cargo_build&#96; macro or configured by &#96;%cargo_prep&#96;.

### Building with meson directly {#_building_with_meson_directly}

Recent versions of [meson](https://mesonbuild.com/Rust.html) have
limited support for building crate dependencies without cargo. It is
necessary to manually override crate sources with the local registry to
use packaged crate dependencies.

## Building shared libraries with cargo-c {#_building_shared_libraries_with_cargo_c}

While it is not currently possible to build Rust crates as shared
libraries, Rust projects can define a C-compatible public API so that
they can be built as standard shared libraries with a C ABI.

In most cases, libraries like this are built with
[cargo-c](https://crates.io/crates/cargo-c), which provides convenient
wrappers (&#96;cargo-cbuild&#96; and &#96;cargo-cinstall&#96;) for both
building and installing shared libraries (including support for
generating and installing header files and and pkg-config files).

The &#96;cargo-c&#96; package includes RPM macros for this functionality
(&#96;%cargo_cbuild&#96; and &#96;%cargo_cinstall&#96;), which accept
the same arguments as their cargo counterparts.

## RPM macros {#_rpm_macros_7}

The process of building and installing Rust projects is almost entirely
automated with several RPM macros:

&#42; &#96;%cargo_prep&#96;: This macro &#42;MUST&#42; be called in the
&#96;%prep&#96; scriptlet after sources have been unpacked. It sets up
the build environment for cargo and injects a cargo configuration file,
which sets the default compiler flags and configures the local crate
registry as a replacement for [crates.io](https://crates.io). &#42;
&#96;%cargo_generate_buildrequires&#96;: This macro &#42;MUST&#42; be
called in the &#96;%generate_buildrequires&#96; scriptlet, except when
building with vendored dependencies. This is the mechanism that
automatically generates depepdencies on other Rust crates based on the
metadata in &#96;Cargo.toml&#96;. &#42; &#96;%cargo_build&#96;: This
macro &#42;MUST&#42; only be called in the &#96;%build&#96; scriptlet
unless the build is handled in another way, i.e. \'cargo build\' is
called internally by build scripts. It runs &#96;cargo build&#96; with
the appropriate command line arguments. Calling this macro &#42;MAY&#42;
be skipped if the crate is not supported on the current CPU
architecture. &#42; &#96;%cargo_install&#96;: This macro &#42;MUST&#42;
only be called in the &#96;%install&#96; scriptlet for crates that
provide a library interface. It runs &#96;cargo package&#96; and
installs the resulting directory tree into
&#96;+%{buildroot}/%{crate_instdir}\\&#96; (i.e.
\\&#96;%{buildroot}/%{cargo_registry}/%{crate}-%{version}/\\&#96;). For
crates that provide \\&#96;bin\\&#96; targets, it installs all built
executables into \\&#96;%{buildroot}/%{\_bindir}\\&#96;. If any built
executables need to be installed in a different location, they can be
moved after calling \\&#96;%cargo_install\\&#96;, or
\\&#96;%cargo_install\\&#96; can be replaced with manual installation
steps (copying from \\&#96;+target/rpm/\\&#42;&#96;). To prevent
installation of executables by this macro, the
&#96;+%cargo_install_bin+&#96; macro can be defined to &#96;0&#96;. To
prevent installation of library sources by this macro, the
&#96;+%cargo_install_lib+&#96; macro can be defined to &#96;0&#96;.
&#42; &#96;%cargo_test&#96;: This macro &#42;MUST&#42; only be called in
the &#96;%check&#96; scriptlet. It runs &#96;cargo test&#96; with the
appropriate command line arguments. Calling this macro &#42;MAY&#42; be
skipped if the crate is not supported on the current CPU architecture or
if tests are disabled in general. &#42; &#96;%cargo_license&#96; /
&#96;%cargo_license_summary&#96;: These macros &#42;MUST&#42; be called
in the &#96;%build&#96; scriptlet after &#96;%cargo_build&#96; when
building crates that include binary targets. They can be used to print
the list of the licenses of the crates that are statically linked into
any built executable or shared library (see [License
tags](&#35;_license_tags)). &#42; &#96;%cargo_vendor_manifest&#96;: This
macro &#42;MUST&#42; be called in the &#96;%build&#96; scriptlet after
&#96;%cargo_build&#96; when building Rust projects with vendored
dependencies. It writes a machine-readable list of all vendored
dependencies to &#96;cargo-vendor.txt&#96;, which &#42;MUST&#42; be
included as a &#96;%license&#96; file in the package that contains the
statically linked executable(s).

All packages for Rust crates &#42;MUST&#42; set either &#96;%bcond check
1&#96; or &#96;%bcond check 0&#96;. The value of this macro affects
whether &#96;%cargo_generate_buildrequires&#96; includes dependencies
that are required for building and running tests.

Non-crate packages can either use the &#96;%bcond check&#96; *or* pass
the &#96;-t&#96; flag to the &#96;%cargo_generate_buildrequires&#96;
macro to include test-only dependencies in &#96;BuildRequires&#96;
generation.

All &#96;%cargo\_&#42;&#96; macros (except &#96;%cargo_prep&#96; and
&#96;%cargo_vendor_manifest&#96;) accept a set of optional flags /
arguments that can be used to control the feature flags that are passed
to cargo (usually to enable optional / non-default features):

&#42; &#96;-a&#96;: Causes the &#96;\--all-features&#96; flag to be
passed to cargo, and the &#96;%cargo_generate_buildrequires&#96; macro
to resolve dependencies with all optional features enabled. &#42;
&#96;-n&#96;: Causes the &#96;\--no-default-features&#96; flags to be
passed to cargo, and the &#96;%cargo_generate_buildrequires&#96; macro
to resolve dependencies with all default and optional features disabled.
&#42; &#96;-f foo,bar&#96;: Causes the &#96;\--features foo,bar&#96;
argument to be passed to cargo, and the
&#96;%cargo_generate_buildrequires&#96; macro to resolve dependencies
with the additional features &#96;foo&#96; and &#96;bar&#96; enabled.
This argument accepts a comma-separated list of feature names (or names
of optional dependencies).

The &#96;-a&#96; and &#96;-n&#96; flags are mutually exclusive and
cannot be passed together. The &#96;-a&#96; flag and &#96;-f&#96;
arguments are also incompatible, since passing &#96;-a&#96; already
enables all features. However, using the &#96;-n&#96; flag and
specifically enabling *some* features with the &#96;-f&#96; argument is
valid.

There are some common situations in which passing these flags or
arguments is necessary:

&#42; It can be necessary to enable additional features and / or
optional dependencies to build and run the test suite of a crate. In
this case, the required features &#42;MUST&#42; be enabled by passing
the corresponding flags to all &#96;%cargo\_&#42;&#96; macros, unless
the required optional dependencies are not packaged yet. &#42; Some
applications support additional / non-default features by passing
feature flags. If it is desirable to build applications with these
features enabled, the required features need to be enabled by passing
the corresponding flags to all &#96;%cargo\_&#42;&#96; macros (including
&#96;%cargo_license&#96; and &#96;%cargo_license_summary&#96;).

Note that the &#96;-n&#96; flag should only be used in exceptional
circumstances, for example when enabling a different backend than the
one enabled by default, and &#42;MUST NOT&#42; be used to avoid missing
dependencies that are part of the &#96;\'default\'&#96; feature set of a
crate.

When passing any of the &#96;-a&#96; or &#96;-n&#96; flags or an
&#96;-f&#96; argument to a &#96;%cargo_build&#96; and / or
&#96;%cargo_install&#96; macro, the same flags MUST also be passed to
&#96;%cargo_license&#96; and &#96;%cargo_license_summary&#96; (if
present). Otherwise, the list of generated licenses and the generated
license summary will not match what is used when the application or
library is compiled.

## Templates {#_templates}

### Non-crate Rust project {#_non_crate_rust_project}

``` rpm
Name:           my-awesome-project
Version:        25.11.26
Release:        %autorelease
Summary:        My Awesome Rust Project

SourceLicense:  WTFPL
\&#35; FIXME: paste output of %%cargo_license_summary here
License:        %{shrink:
WTFPL AND
\&#8230;
}
\&#35; LICENSE.dependencies contains a full license breakdown

URL:            https://forge.example/me/my-awesome-project
Source:         %{url}/archive/v%{version}.tar.gz

BuildRequires:  cargo-rpm-macros

%description
My Awesome Rust Project.

%prep
%autosetup -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires -t

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} \&gt; LICENSE.dependencies

%install
install -Dpm 0755 target/rpm/my-awesome-cli -t %{buildroot}%{_bindir}

%check
%cargo_test

%files
%license LICENSE
%license LICENSE.dependencies
%doc README.md
%{_bindir}/my-awesome-cli

%changelog
%autochangelog
```

### Python project {#_python_project}

``` rpm
Name:           python-rustypackage
Version:        25.11.26
Release:        %autorelease
Summary:        Rusty Python Package

License:        WTFPL
URL:            https://forge.example/me/python-rustypackage
Source:         %{url}/archive/v%{version}/rustypackage-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  cargo-rpm-macros

%global _description %{expand:
My Rusty Python Package.}

%description %_description

%package     -n python3-rustypackage
Summary:        %{summary}

\&#35; FIXME: paste output of %%cargo_license_summary here
License:        %{shrink:
WTFPL AND
\&#8230;
}
\&#35; LICENSE.dependencies contains a full license breakdown

%description -n python3-rustypackage %_description

%prep
%autosetup -n rustypackage-%{version} -p1
%cargo_prep

%generate_buildrequires
\&#35; maturin requires all dependencies to be available,
\&#35; even those for tests and features that are not enabled
%cargo_generate_buildrequires -a -t
%pyproject_buildrequires

%build
%pyproject_wheel
%{cargo_license_summary}
%{cargo_license} \&gt; LICENSE.dependencies

%install
%pyproject_install
%pyproject_save_files -l rustypackage

%check
%pyproject_check_import
\&#35; %%pytest
\&#35; %%cargo_test

%files -n python3-rustypackage -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
```

Verify that project license file(s) &#42;and&#42; the
&#96;LICENSE.dependencies&#96; file are included in built packages as
expected (&#96;+rpm -qL -p &lt;path to RPM&gt;+&#96;) when using
&#96;+%pyproject_save_files -l+&#96;.

# Tcl packaging guidelines {#_tcl_packaging_guidelines}

These conventions apply to Tcl packages in Fedora 9 and later. There are
some aspects of Tcl in Fedora 7 and Fedora 8 that will conflict with
these guidelines.

## Naming Conventions {#_naming_conventions}

The name for all Tcl/Tk extensions must be prefixed with
&#96;+tcl-\\&#96;. This rule applies even for Tcl/Tk packages that are
already prefixed with \\&#96;+tcl&#96; in the name (see examples below).
An optional &#96;+Provides: foo+&#96; is recommended to allow selecting
the package based on the upstream name, as long as the upstream name is
not excessively generic and does not conflict with an existing package
name. Tk extensions have the option of adding additional Provides: with
the prefix &#96;+tk-+&#96;.\
Examples:

&#8230;. Name: tcl-bwidget Provides: bwidget = %{version}-%{release},
tk-bwidget = %{version}-%{release} &#8230;.

&#8230;. Name: tcl-tclxml Provides: tclxml = %{version}-%{release}
&#8230;.

&#8230;. Name: tcl-thread &#8230;.

The exception to this naming rule are existing packages that provide
both an extension and a shell, such as &#96;+expect+&#96;. However, note
that providing a shell is strongly discouraged (see below).

## Applications {#_applications_3}

Tcl and Tk applications &#42;must&#42; use a non-versioned interpreter
name in shebang line. This is to prevent any unnecessary dependency on
the version of the interpreter being used. Most dependencies are with
specific Tcl extensions, not the command line applications.
Nevertheless, if an application does require a specific version of Tcl,
it should use the standard Tcl package system to express this, as well
as an explicit &#96;+Requires: tcl(abi) = 8.x+&#96; in the spec file.

Bad:

&#8230;. &#35;!/usr/bin/tclsh8.5 &#8230;.

Good:

&#8230;. &#35;!/usr/bin/tclsh package require -exact Tcl 8.5 &#8230;.

The same rules apply for Tk applications. The non-versioned
&#96;+wish+&#96; interpreter name &#42;must&#42; be used.

## Extensions {#_extensions}

Since Fedora 9, &#96;+%{\_libdir}\\&#96; and \\&#96;%{\_datadir}\\&#96;
have been removed from the search path to optimize package loading
times. Instead, Tcl extension packages \\&#42;must\\&#42; be installed
in \\&#96;%{\_datadir}/tcl8.x+&#96; if they are noarch packages
containing only Tcl code, or &#96;+%{\_libdir}/tcl8.x+&#96; if they are
arch-specific extensions containing shared libraries. Note that most Tcl
extensions are not configured do install in these directories out of the
box, and may need to use additional configure switches, patches, or
script code in &#96;+%install+&#96; to move the files to the correct
location.

Both arch-specific and &#96;+noarch+&#96; Tcl extensions &#42;must&#42;
use

&#8230;. Requires: tcl(abi) = 8.6 &#8230;.

to indicate which Tcl version (8.5 in F19 and F20, 8.6 in F21+) they
were built against. This is necessary because the guidelines below
require extensions to be installed into tcl-versioned directories, which
are only used by a single version of Tcl. This does impose an
inconvenience that all arch-specific and noarch extensions will need to
be rebuilt for a new minor version of Tcl, but since new Tcl minor
versions only appear once every few years, this should not be such a
problematic inconvenience.

### noarch packages {#_noarch_packages}

The following macros &#42;must&#42; be used at the top of the spec file
to determine the correct installation paths:

&#8230;. %{!?tcl_version: %global tcl_version %(echo \'puts
\$tcl_version\' \| tclsh)} %{!?tcl_sitelib: %global tcl_sitelib
%{\_datadir}/tcl%{tcl_version}} &#8230;.

In order for the macros to work, the package must also
&#96;+BuildRequires: tcl+&#96; either directly, or indirectly with
&#96;+BuildRequires: tcl-devel+&#96;

Merely adding the &#96;+%{tcl_sitearch}\\&#96; and
\\&#96;%{tcl_sitelib}\\&#96; is not enough to ensure that the packages
get installed into the correct location. Most Tcl extensions will
install into \\&#96;%{\_libdir}\\&#96; by default. There are two ways to
change this. For most \\&#96;+noarch&#96; packages, you can use the
&#96;+\--libdir+&#96; and &#96;+\--datadir+&#96; configure switches to
change the installation directory:

&#8230;. %configure \--libdir=%{tcl_sitelib} \--datadir=%{tcl_sitelib}
&#8230;.

For &#96;+noarch+&#96; packages that aren't fixed by using
&#96;+\--libdir+&#96;, you can simply move the installation directory in
the &#96;+%install+&#96; section of the spec file.

&#8230;. %install rm -rf \$RPM_BUILD_ROOT make install
DESTDIR=\$RPM_BUILD_ROOT install -d \$RPM_BUILD_ROOT%{tcl_sitelib} mv
\$RPM_BUILD_ROOT%{\_datadir}/foobar%{version}
\$RPM_BUILD_ROOT%{tcl_sitelib}/foobar%{version} &#8230;.

It may also be acceptable to patch upstream's &#96;+configure+&#96;
script and &#96;+Makefile+&#96; to add additional flexibility for the
install directory, but the packager is not required to do this.

### arch-specific packages {#_arch_specific_packages}

The following macros &#42;must&#42; be used at the top of the spec file
to determine the correct installation paths:

&#8230;. %{!?tcl_version: %global tcl_version %(echo \'puts
\$tcl_version\' \| tclsh)} %{!?tcl_sitearch: %global tcl_sitearch
%{\_libdir}/tcl%{tcl_version}} &#8230;.

In order for the macros to work, the package must also
&#96;+BuildRequires: tcl+&#96; either directly, or indirectly with
&#96;+BuildRequires: tcl-devel+&#96;

While &#96;+%{tcl_sitearch}\\&#96; is a symlink to
\\&#96;%{tcl_sitelib}+&#96; in Fedora 8 and earlier, in Fedora 9 it is
an actual directory.

The &#96;+\--libdir+&#96; flag for the configure script can often be
used to set the correct installation directory:

&#8230;. %build %configure \--libdir=%{tcl_sitearch} &#8230;.

For most arch-specific packages, the &#96;+\--libdir+&#96; flag for the
configure script is also used to locate tclConfig.sh. Some of these
arch-specific packages will break if &#96;+\--libdir+&#96; is redirected
to &#96;+%{tcl_sitearch}\\&#96;. For packages that can\'t handle
alternate values for \\&#96;\--libdir+&#96;, you can simply move the
installation directory in the &#96;+%install+&#96; section of the spec
file:

&#8230;. %install make install DESTDIR=\$RPM_BUILD_ROOT install -d
\$RPM_BUILD_ROOT%{tcl_sitearch} mv
\$RPM_BUILD_ROOT%{\_libdir}/foobar%{version}
\$RPM_BUILD_ROOT%{tcl_sitearch}/foobar%{version} &#8230;.

Arch-specific packages can be generally grouped into three categories:
those that provide a shell, those that provide a fooConfig.sh file and a
shared library for linking, and those that only provide a shared library
for dlopen().

&#42;No shells:&#42; Very few Tcl extension packages provide a shell.
Providing a shell for an extension is frowned upon. The extension's
shared library can be dynamically loaded into a Tcl interpreter through
the standard &#96;+package require &#8230;+&#96; mechanism without
providing a shell that automatically loads the shared library. The
exceptions to this rule are the shells that are commonly expected to be
present on a system, including Tk (wish) and Expect (expect, expectk).

&#42;-devel subpackage for fooConfig.sh:&#42; Some arch-specific Tcl
extensions provide a shared library and a corresponding
&#96;+fooConfig.sh+&#96; file with instructions for linking against the
library. The shared library for such packages &#42;must&#42; be
installed into %{\_libdir} so that it can be found at runtime by
applications that link against it. Unfortunately, the pkgIndex.tcl file
in the package directory often references the shared library with a
relative path. There are two ways to fix this. First, the maintainer can
choose to keep the installation directory as %{\_libdir}, and make a
symlink to %{tcl_sitearch}. Second, the maintainer can choose to patch
the pkgIndex.tcl file to contain an appropriate path to the shared
library. Either solution is acceptible.

&#96;+fooConfig.sh+&#96; files must be placed in a -devel subpackage.
This may require some sed magic to modify &#96;+fooConfig.sh+&#96; so
that the paths to the libraries and headers are still correct.

&#42;No dlopen()\'d libraries in %{\_libdir}:&#42; If the extension does
&#42;not&#42; provide a &#96;+fooConfig.sh+&#96; file, then the shared
library &#42;must not&#42; be installed directly in
&#96;+%{\_libdir}\\&#96;, but in the package-specific installation
directory in \\&#96;%{tcl_sitearch}\\&#96; instead. This may require a
patch to update the extension\'s \\&#96;+pkgIndex.tcl&#96; file to look
for the shared library in the correct location.

&#42;Stubs are ok if put in -devel subpackage:&#42; Some Tcl extensions
provide a static \'stub\' library. Stub libraries are a Tcl-ism to
provide version-independent dynamic linking on a variety of platforms.
These are not normal static libraries that provide the library's actual
functionality, but instead provide a level of indirection pointing to
the shared library. These stub libraries do not have the same static
linking issues that are generally frowned upon in Fedora, and thus are
acceptable. If a package provides such a stub library, it must be placed
in a -devel subpackage. More information on stubs can be found on the
Tcl wiki: <https://wiki.tcl-lang.org/page/Stubs>

&#42; Other Domain-specific Guidelines = Ansible Collection Packaging
Guidelines :last-reviewed: 2022-09-25

## Forward {#_forward}

Ansible collections are packaged units of Ansible content, including
modules and other types of plugins. Most Ansible Plugins are written in
Python or Powershell.

Some collections are also included in Ansible Community's
&#96;+ansible+&#96; collection bundle, which is packaged in Fedora. All
collections, whether or not they are included in the &#96;+ansible+&#96;
package, MAY be packaged in Fedora.

&#96;+ansible+&#96; depends on &#96;+ansible-core+&#96;, which contains
the core engine and CLI programs (e.g. &#96;+ansible+&#96;,
&#96;+ansible-playbook+&#96;). The &#96;+ansible+&#96; package has a
different release cycle than individual collections, and it may contain
older versions of the individual components. &#96;+ansible+&#96;
installs collections in a different namespace and is parallel
installable with individual collections. The Ansible engine searches for
collections in the standalone collections directory first.

See [Changes/Ansible5](https://fedoraproject.org/wiki/Changes/Ansible5)
for more information about the split between &#96;+ansible+&#96; and
&#96;+ansible-core+&#96;.

## Naming {#_naming_10}

Collection packages MUST be named
&#96;+ansible-collection-NAMESPACE-NAME+&#96;. For example, the
&#96;+community.general+&#96; collection package is named
&#96;+ansible-collection-community-general+&#96;.

## Collection Source {#_collection_source}

Collection source code MUST be downloaded from the collection's
respective Git forge/other SCM repository. While the tarballs published
to Ansible Galaxy contain all of the collection's Python/Powershell
source code as well as some development files, they do not include the
&#96;+galaxy.yml+&#96; build configuration and development files (e.g.
unit tests) that the author may choose to remove. Note that the Ansible
Community collection requirements mandate that collections tag releases
in a public SCM repository.

Collection packages SHOULD use &#96;+%{ansible_collection_url NAMESPACE
NAME}\\&#96; as the package\'s \\&#96;+URL:&#96;. This points to the
collection's homepage on Ansible Galaxy.

## Dependencies {#_dependencies_6}

### Buildtime {#_buildtime}

Collections MUST have &#96;+BuildRequires: ansible-packaging+&#96;.
&#96;+ansible-packaging+&#96; provides macros and a dependency generator
for packaging Ansible Collections. It also pulls in
&#96;+ansible-core+&#96;, so &#96;+BuildRequires: ansible-core+&#96;
SHOULD NOT be added manually.

### Runtime {#_runtime}

The dependency generator will generate the appropriate dependency on the
Ansible engine. This ensures compatibility with Fedora 35 which contains
the classic &#96;+ansible+&#96; 2.9 package (instead of the collections
bundle) and &#96;+ansible-core+&#96;. Both versions of the Ansible
engine support collections, but they are not parallel installable.
Packages MUST NOT manually &#96;+Require+&#96; &#96;+ansible-core+&#96;
or &#96;+ansible+&#96;, unless they are known to require a specific
version, in which case the appropriate version constraints should be
used.

The dependency generator also handles inter-collection dependencies.

#### External dependencies of plugins {#_external_dependencies_of_plugins}

Ansible collections may contain various plugins that have various
external dependencies. The Ansible dev guide
[mandates](https://docs.ansible.com/ansible/latest/dev_guide/developing_modules_best_practices.html&#35;importing-and-using-shared-code)
that plugins fail cleanly if these dependencies are not installed. Many
times, external dependencies are only needed for a small subset of the
collection which may or may not be widely used. Therefore, collection
packages SHOULD weakly depend on these external libraries, i.e. use
Recommends instead of Requires.

Module dependencies are only needed on the target node not the
controller node. Therefore, collection packages SHOULD NOT depend on
these dependencies at all, weakly or strongly. Users are responsible for
installing these dependencies on the target host. Modules that are
intended to be used with &#96;+delegate_to: localhost+&#96; are an
exception to this rule.

The situation is a bit different for controller plugins, such as filter
plugins, lookup plugins, connection plugins, or inventory plugins.
Collections MAY add &#96;+Recommends+&#96; for dependencies of
controller plugins. However, packagers should use discretion when adding
any type of dependency and only do so when it is required for the
central functionality of the collection. For instance, it makes sense
for &#96;+ansible-collection-community-docker+&#96; to Recommend
&#96;+python3-docker+&#96;, but it doesn't make sense for the larger,
more general ansible-collection-community-general collection to
Recommend &#96;+python3-redis+&#96; for the &#96;+redis+&#96; lookup
plugin. This guideline seeks to prevent ballooning collection packages.
&#96;+ansible-core+&#96; and &#96;+ansible+&#96; follow this same
principle.

## Build and Installation {#_build_and_installation}

To build the collection artifact, packages MUST use
&#96;+%ansible_collection_build+&#96; in &#96;+%build+&#96;.
&#96;+%ansible_collection_install+&#96; MUST be used in
&#96;+%install+&#96; to install the artifact.

Packagers SHOULD use &#96;+%files -f
%{ansible_collection_filelist}\\&#96; to install the collection. The
\\&#96;%{ansible_collection_filelist}\\&#96; is populated by
\\&#96;%ansible_collection_install+&#96;.

## Unit Tests {#_unit_tests}

As per [the general Fedora Packaging
Guidelines](index.adoc&#35;_test_suites), collection packages SHOULD run
upstream unit tests in &#96;+%check+&#96; if practical. Integration
tests are impossible to run in the RPM build environment. In order to
run unit tests, collections MUST &#96;+BuildRequire+&#96;
&#96;+ansible-packaging-tests+&#96;, which pulls in the necessary
dependencies. Some collections have other testing dependencies, which
are usually specified in &#96;+tests/unit/requirements.txt+&#96;. These
have to be added manually. The &#96;+%ansible_test_unit+&#96; macro MUST
be used to run tests.

:::: note
::: title
EPEL Compatibility
:::

It is currently impossible to run unit tests on EPEL 8 and 9.

ansible-core in RHEL 8 and 9 are built against alternative python stacks
for which the necessary test dependencies are not available.

The rest of these guidelines are applicable to EPEL 8 and 9, and
&#96;+ansible-packaging+&#96; itself is available there.
::::

## Unnecessary Files {#_unnecessary_files_2}

By default, collections ship with all of the files in the repository
root, unless they are manually excluded. Therefore, many collections
contain development files that are unwanted by users.

Packagers SHOULD exclude these files, which SHOULD be done by patching
the collection's &#96;+galaxy.yml+&#96; to add these files to the
&#96;+build_ignore+&#96; configuration. These files SHOULD NOT be
removed with &#96;+rm+&#96;. See the [Ansible
documentation](https://docs.ansible.com/ansible/latest/dev_guide/collections_galaxy_meta.html&#35;collection-galaxy-metadata-structure)
for more information on the &#96;+galaxy.yml+&#96; syntax.

Common development files include:

&#42; The &#96;+tests+&#96; directory containing unit and integration
tests &#42; SCM configuration such as &#96;+.gitignore+&#96; and
&#96;+.keep+&#96; files &#42; The &#96;+.azure-pipelines+&#96; and
&#96;+.github+&#96; directories that contain CI configuration

These files often have to be removed downstream, as there are some
unresolved issues with pushing these changes to upstream community
collections. These issues are irrelevant in the Fedora context.

## Shebangs {#_shebangs_2}

Ansible plugins are not executable. However, many of them have
&#96;+&#35;!/usr/bin/python+&#96; shebangs for legacy reasons. These
shebangs MUST be removed for the following reasons:

1.  Non-executable files shouldn't have shebangs

2.  Keeping the shebangs results in an unnecessary dependency on
    &#96;+python-unversioned-command+&#96;.

&#96;+%py3_shebang_fix+&#96; MUST NOT be used, as it will break
compatibility with certain Ansible target nodes. It won't fix the
non-executable file issue, either.

Shebangs can be removed with:

``` bash
find -type f ! -executable -name '\&#42;.py' -print -exec sed -i -e '1{\@^\&#35;!.\&#42;@d}' '{}' +
```

## Documentation and License Files {#_documentation_and_license_files}

License files and documentation for collections are installed to the
collection's directory in &#96;+/usr/share/ansible+&#96;, by default.
Packagers MAY choose to either mark the license and documentation files
in this directory with &#96;+%license+&#96; and &#96;+%doc+&#96; or to
add the correct paths to &#96;+build_ignore+&#96; in
&#96;+galaxy.yml+&#96; and install them into the standard directories.
Avoid duplicating these files in both places.

Note that some multi-licensed collections store licenses in a
&#96;+LICENSES+&#96; directory. This whole directory MUST be marked with
&#96;+%license+&#96;.

Refer to the [Legal docs](legal::index.xml) for the rules about allowed
licenses and determining the &#96;+License:+&#96; field.

## Example Specfile {#_example_specfile}

``` rpm-spec
\&#35; Only run tests where the dependencies are available
%if %{defined fedora}
%bcond_without tests
%else
%bcond_with tests
%endif

Name:           ansible-collection-community-rabbitmq
Version:        1.2.2
Release:        1%{?dist}
Summary:        RabbitMQ collection for Ansible

\&#35; plugins/module_utils/_version.py: Python Software Foundation License version 2
License:        GPL-3.0-or-later and PSF-2.0
URL:            %{ansible_collection_url community rabbitmq}
%global forgeurl https://github.com/ansible-collections/community.rabbitmq
Source0:        %{forgeurl}/archive/%{version}/%{name}-%{version}.tar.gz
\&#35; Patch galaxy.yml to exclude unnecessary files from the built collection.
\&#35; This is a downstream only patch.
Patch0:         build_ignore.patch

BuildRequires:  ansible-packaging
%if %{with tests}
BuildRequires:  ansible-packaging-tests
\&#35; Collection specific test dependency
BuildRequires:  glibc-all-langpacks
%endif

BuildArch:      noarch

%description
%{summary}.


%prep
%autosetup -n community.rabbitmq-%{version} -p1
find -type f ! -executable -name '\&#42;.py' -print -exec sed -i -e '1{\@^\&#35;!.\&#42;@d}' '{}' +


%build
%ansible_collection_build


%install
%ansible_collection_install


%if %{with tests}
%check
%ansible_test_unit
%endif


%files -f %{ansible_collection_filelist}
%license COPYING PSF-license.txt
%doc README.md CHANGELOG.rst

%changelog
```

build_ignore.patch:

``` _patch
diff --git a/galaxy.yml b/galaxy.yml
index 0b37162..acd029a 100644
--- a/galaxy.yml
+++ b/galaxy.yml
@@ -13,3 +13,13 @@ repository: https://github.com/ansible-collections/community.rabbitmq
documentation: https://docs.ansible.com/ansible/latest/collections/community/rabbitmq/
homepage: https://github.com/ansible-collections/community.rabbitmq
issues: https://github.com/ansible-collections/community.rabbitmq/issues
+build_ignore:
+  \&#35; Remove unnecessary development files from the built package.
+  - tests
+  - .azure-pipelines
+  - .gitignore
+  \&#35; Licenses and docs are installed with %%doc and %%license
+  - PSF-license.txt
+  - COPYING
+  - README.md
+  - CHANGELOG.rst
```

## Macro Breakdown {#_macro_breakdown}

Here is a short breakdown of exactly what each macro included in
&#96;+ansible-packaging+&#96; does.

\[&#35;ansible_collection_url\] === &#96;+%ansible_collection_url+&#96;

&#42;Usage:&#42;

``` rpm-spec
URL:            %{ansible_collection_url NAMESPACE NAME}
```

This macro points to a collection's Ansible Galaxy page. It is intended
to be used for the &#96;+URL:+&#96; tag in the specfile preamble. It
takes the collection namespace and collection name as arguments.

If no arguments are passed to this macro, it falls back to the values of
&#96;+%{collection_namespace}\\&#96; and \\&#96;%{collection_name}+&#96;
if they are set in the specfile. New packages SHOULD explicitly pass the
namespace and name as arguments. The fallback may be removed in the
future. See the [Legacy Macros](&#35;legacy_macros) section for more
information.

\[&#35;ansible_collection_build\]

### &#96;+%ansible_collection_build+&#96; {#_96ansible_collection_build96}

&#42;Usage:&#42;

``` rpm-spec
%build
%ansible_collection_build
```

This macro simply runs &#96;+ansible-galaxy collection build+&#96;.

\[&#35;ansible_collection_install\] ===
&#96;+%ansible_collection_install+&#96;

&#42;Usage:&#42;

``` rpm-spec
%install
%ansible_collection_install
```

This macro pulls out the collection namespace, name, and version from
&#96;+galaxy.yml+&#96; and then uses it to run &#96;+ansible-galaxy
collection install+&#96;. After that, it writes out
&#96;+%{ansible_collection_filelist}+&#96; based on the metadata it
previously extracted

\[&#35;ansible_test_unit\] === &#96;+%ansible_test_unit+&#96;

&#42;Usage:&#42;

``` rpm-spec
%check
%ansible_test_unit
```

This macro parses galaxy.yml to determine the collection namespace and
name that's needed to create the directory structure that ansible-test
expects. After creating a temporary build directory with the needed
structure, the script runs ansible-test units with the provided
arguments.

\[&#35;ansible_collection_filelist\] ===
&#96;+%{ansible_collection_filelist}+&#96;

&#42;Usage:&#42;

``` rpm-spec
%files -f %{ansible_collection_filelist}
%doc \&#8230;
%license \&#8230;
```

This macro points a file list that's written out by
&#96;+%ansible_collection_install+&#96;. Currently, it only contains a
single entry to own the collection's entire directory in
&#96;+%{ansible_collections_dir}+&#96;

\[&#35;ansible_collections_dir\]

This macro expands to
&#96;+%{\_datadir}/ansible/collections/ansible_collections+&#96;. It is
used internally by the other macros. Packagers are expected to use
&#96;+%ansible_collection_install+&#96; and
&#96;+%ansible_collection_filelist+&#96; instead of directly referencing
this directory.

\[&#35;legacy_macros\] === Legacy macros

\[&#35;collection_namespace\] ==== &#96;+%{collection_namepsace}+&#96;
&#42;Usage:&#42;

``` rpm-spec
%global collection_namespace NAMESPACE
```

The ansible-packaging macros previously required packagers to manually
set &#96;+%collection_namespace+&#96; in specfiles. Now, the macros
extract the collection namespace from the &#96;galaxy.yml&#96;.

\[&#35;collection_name\] ==== &#96;+%{collection_name}+&#96;

&#42;Usage:&#42;

``` rpm-spec
%global collection_name NAME
```

The ansible-packaging macros previously required packagers to manually
set &#96;+%collection_name+&#96; in specfiles. Now, the macros extract
the collection name from the &#96;galaxy.yml&#96;.

\[&#35;ansible_collection_files\] ====
&#96;+%{ansible_collection_files}+&#96;

&#42;Usage:&#42;

``` rpm-spec
%files
%doc \&#8230;
%license \&#8230;
%{ansible_collection_files}
```

New specfiles should use &#96;+%files -f
%{ansible_collection_filelist}\\&#96; instead of this macro.
\\&#96;%{ansible_collection_files}\\&#96; requires setting
\\&#96;%collection_namespace+&#96; and &#96;+%collection_name+&#96;.

# Linear Algebra Libraries {#_linear_algebra_libraries}

## Introduction {#_introduction_4}

BLAS (Basic Linear Algebra Subprograms) and LAPACK (Linear Algebra
PACKage) are routines that provide standard building blocks for
performing a wide range of linear algebra operations. There are stable
reference implementations from [Netlib](https://netlib.org/) written in
Fortran, with C interfaces available (called CBLAS and LAPACKE
respectively), as well as several optimized implementations providing
fast subsets of these APIs.

### Available implementations {#_available_implementations}

&#42; &#96;blas&#96;, &#96;lapack&#96; - Netlib's reference
implementation of the Fortran and C interfaces. &#42; &#96;atlas&#96; -
Automatically Tuned Linear Algebra Software. &#42; &#96;blis&#96; -
BLAS-like Library Instantiation Software framework. &#42;
&#96;openblas&#96; - OpenBLAS, an optimized BLAS based on GotoBLAS2.

ATLAS, BLIS and OpenBLAS provide BLAS and a subset of LAPACK. Both BLIS
and OpenBLAS provide several flavors: a sequential version, a threaded
one, and another with OpenMP support (all of them with or without
support for 64-bit integers).

Due to implementation differences, it is important that all components
of a particular software stack link to the same BLAS/LAPACK
implementation. Also, users may want to choose a particular
implementation that works best for them at run time. This guideline
gives a structure that can enforce the first while allowing the second,
as well as providing a transparent fallback mechanism to Netlib's
reference implementation for those symbols not included in the selected
backend via
[FlexiBLAS](https://www.mpi-magdeburg.mpg.de/projects/flexiblas).

### BLAS/LAPACK wrapper {#_blaslapack_wrapper}

[FlexiBLAS](https://www.mpi-magdeburg.mpg.de/projects/flexiblas) is a
framework that wraps both BLAS and LAPACK APIs in a single library.
BLAS/LAPACK consumers must link against FlexiBLAS, and this wrapper is
able to redirect calls to a selected optimized backend with negligible
overhead. It also provides transparent fallback to Netlib's reference
implementation if a certain symbol is not present in the selected
backend. These are the main features:

&#42; Provides a 100% BLAS and LAPACK compatible ABI/API, with
interfaces for both 32- and 64-bit integers. &#42; Runtime exchangeable
BLAS and LAPACK backend without recompilation via an environment
variable. &#42; Integration of user-owned BLAS libraries without
administrator privileges, even in system-wide installed programs. &#42;
Works with OpenBLAS, ATLAS and BLIS, as well as non-free alternatives
such as Intel MKL, ACML&#8230; &#42; Flexible per-system/user/host
configuration files. &#42; Basic profiling support.

:::: note
::: title
:::

Fedora ships &#96;openblas-openmp&#96; as the system-wide default
backend.
::::

## Packaging BLAS/LAPACK dependent packages {#_packaging_blaslapack_dependent_packages}

Consumers of any subset of BLAS and/or LAPACK MUST compile against
FlexiBLAS (unless not supported; see below).

:::::: note
::: title
:::

:::: formalpara
::: title
Exceptions
:::

&#42; Although support for LAPACKE is planned, the few packages using
this interface are not yet supported by FlexiBLAS as of v3.1.2. These
packages MUST link against OpenBLAS instead, or &#96;lapack&#96; if the
routines used are not supported by this backend. Current exceptions of
this type include &#96;opencv&#96;, &#96;scamp&#96; and
&#96;sextractor&#96;. &#42; On rare occasions, a package may use an
exceptional feature present in a particular backend and cannot be
adapted to FlexiBLAS by any means. In such cases, the package MUST link
against this backend. Current exceptions of this type include
&#96;julia&#96; (linked against OpenBLAS) and &#96;psfex&#96; (linked
against ATLAS).
::::
::::::

### Build requirements {#_build_requirements}

First, only FlexiBLAS's development package MUST be listed in
&#96;BuildRequires&#96;:

&#8230;. BuildRequires: flexiblas-devel &#8230;.

which brings all the necessary development files, both for the 32-bit
(the most common) and the 64-bit integer interface.

:::: important
::: title
:::

If the package &#42;only&#42; supports the interface for 64-bit
integers, then 32-bit architectures MUST be excluded (see [Arch-Specific
Runtime and Build-Time
Dependencies](index.adoc&#35;_arch_specific_runtime_and_build_time_dependencies)).
::::

### Configuration {#_configuration}

The packager MUST specify &#96;flexiblas&#96; or &#96;flexiblas64&#96;
(for the 32-bit or 64-bit interface respectively) as both the BLAS and
LAPACK library names where applicable, and packages using
&#96;pkg-config&#96; will automatically obtain the proper flags for the
headers and libraries. Similarly, CMake-based projects using
&#96;FindBLAS&#96; will automatically detect and configure the proper
flags for FlexiBLAS (since CMake v3.19), and no further action will be
required from the packager.

Unfortunately, many upstream projects present heterogeneous ways of
accessing these APIs. In a best-case scenario, the building framework
may define specific options to explicitly set the BLAS and/or LAPACK
libraries. More commonly, the packager MUST ensure that
&#96;+%{\_includedir}/flexiblas+&#96; and
&#96;+%{\_libdir}/flexiblas+&#96; (or
&#96;+%{\_includedir}/flexiblas64+&#96; and
&#96;+%{\_libdir}/flexiblas64+&#96;) are injected as header and library
locations in the proper flags and configuration files, and/or
&#96;-lflexiblas&#96; (or &#96;-lflexiblas64&#96;) is provided to the
linker. In rare occasions, hardcoded paths in source files MUST be
modified, and patches MAY be required. The packager SHOULD work with
upstream to standardize the way in which these libraries are detected
and configured.

:::: important
::: title
:::

To ensure that the program has been properly linked against FlexiBLAS,
the packager MUST check that the &#96;Requires&#96; are correct, i.e.,
&#96;libflexiblas&#96; is listed, but not &#96;libblas&#96;,
&#96;liblapack&#96; or any other backend.
::::

### Tests {#_tests_2}

Optimized BLAS/LAPACK backends are much faster than Netlib's reference
implementation, but in return results may vary a little. Consequently,
tests that are too tight (with too small tolerances) may fail. In these
cases, the packager SHOULD enable the reference implementation in the
&#96;%check&#96; section as follows:

&#8230;. export FLEXIBLAS=netlib &#8230;.

or, alternatively, via &#96;FLEXIBLAS64&#96; for builds using 64-bit
integers.

## Backend selection {#_backend_selection}

### System-level selection {#_system_level_selection}

A package compiled against FlexiBLAS pulls out the corresponding
&#96;flexiblas-netlib(64)&#96; subpackage, which in turn requires the
default optimized backend (i.e.,
&#96;flexiblas-openblas-openmp(64)&#96;). This is set via the
\'default=IMPLEMENTATION-NAME\' key (by default,
&#96;default=openblas-openmp&#96;), present in the main configuration
file shipped in the main subpackages,
&#96;+%{\_sysconfdir}/flexiblasrc+&#96; and
&#96;+%{\_sysconfdir}/flexiblas64rc+&#96;.

To allow system-level selection of other BLAS/LAPACK implementations,
more backends must be installed in the first place (e.g.,
flexiblas-atlas, flexiblas-blis-serial&#8230;), and then they can be
swapped system-wide via the &#96;flexiblas&#96; CLI tool, or just by
modifying the \'default\' key in the configuration file by hand.

### User-level selection {#_user_level_selection}

Persistent user-level selection of system-provided BLAS/LAPACK
implementations can be done via the CLI tool:

&#8230;. \$ flexiblas set IMPLEMENTATION-NAME \$ flexiblas64 set
IMPLEMENTATION-NAME &#8230;.

provided the sub-package for &#96;IMPLEMENTATION-NAME&#96; is installed.

Non-persistent user-level selection can be triggered via an environment
variable:

&#8230;. \$ FLEXIBLAS=IMPLEMENTATION-NAME ./yourapp \$
FLEXIBLAS64=IMPLEMENTATION-NAME ./yourapp64 &#8230;.

User-level selection of user-owned BLAS/LAPACK libraries can be achieved
just by changing &#96;IMPLEMENTATION-NAME&#96; with a path to any custom
BLAS/LAPACK-compatible library in the examples above.

# Fedora Cron Job Files {#_fedora_cron_job_files}

This document describes the guidelines for packaging cron job files in
Fedora.

For the purposes of these guidelines, a cron job file is defined as a
script (e.g., a shell script or a Perl script). These cron job files are
scheduled to run on regular intervals by a cron daemon.

## Cron Job Files on the filesystem {#_cron_job_files_on_the_filesystem}

Packages with cron job files must place those cron job files into one or
more of the following directories /etc/cron.hourly, /etc/cron.daily,
/etc/cron.weekly, /etc/cron.monthly depending on the intended interval
they should run.

There is an exception to this rule: If a certain cron job has to be
executed at some frequency or at a specific time interval other than the
above, then a custom crontab file should be added to /etc/cron.d (with
0640 permissions). In this case, the cron job file (the script) must be
placed in an appropriate system location (e.g. %{\_bindir},
%{\_libexecdir}), and NOT in /etc/cron.d.

Both cron job files and crontab definition files installed in any of
these directories must be treated as configuration files so that they
can easily be modified by the local system administrator.

## Cron Job file {#_cron_job_file}

A typical cron job file is just a script like

&#8230;. &#35;!/bin/sh &#35; My cron job script &#35; set -x

echo \'This is my simple cron job script\'

exit 0 &#8230;.

Example of crontab definition run at ever other hour specified in
/etc/cron.d/example

&#8230;. &#35; .\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-- minute (0 - 59) &#35; \|
.\-\-\-\-\-\-\-\-\-\-\-\-- hour (0 - 23) &#35; \| \|
.\-\-\-\-\-\-\-\-\-- day of month (1 - 31) &#35; \| \| \| .\-\-\-\-\-\--
month (1 - 12) OR jan,feb,mar,apr &#8230; &#35; \| \| \| \| .\-\-\-- day
of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat &#35; \|
\| \| \| \| &#35; &#42; &#42; &#42; &#42; &#42; user-name command to be
executed

0 &#42;/2 &#42; &#42; &#42; root /usr/bin/example &#8230;.

## Cron job file names {#_cron_job_file_names}

The file name of a cron job file should match the name of the package
from which it comes.

If a package supplies multiple cron job files files in the same
directory, the file names should all start with the name of the package
followed by a hyphen (-) and a suitable suffix.

## Cron Job Files Packaging {#_cron_job_files_packaging}

Cron job file(s) in packages must be marked as %config(noreplace), and
their filename(s) should match the name of the package.

Helper files used by cron job files should be placed in appropriate
system locations (e.g. %{\_bindir} or %{\_libexecdir}) and do not need
to be marked as %config.

Packages with cron job files must have an explicit &#96;+Requires:
crontabs+&#96;. Since &#96;+crontabs+&#96; requires
&#96;+/etc/cron.d+&#96; and all cron daemon packages create (and own)
that directory, &#96;+crontabs+&#96; serves as a virtual requires for
cron daemon functionality.

### Example of cron job packaging {#_example_of_cron_job_packaging}

``` _rpm-spec
Name:
\&#8230;
Source1: %{name}.cron
Requires: crontabs

\&#8230;

%install
\&#8230;
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/cron.monthly
%{__install} -p -D -m 0750 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/cron.monthly/%{name}

%files
%config(noreplace) %{_sysconfdir}/cron.monthly/%{name}
```

# Packaging of add-ons for GNU Emacs {#_packaging_of_add_ons_for_gnu_emacs}

## Purpose {#_purpose}

The purpose of this document is to promote good practice in packaging
add-ons for GNU Emacs, and to encourage the submission of more Emacs
add-on packages to the package collection by providing easy to use spec
file templates.

## Important notes on these Guidelines {#_important_notes_on_these_guidelines}

The guidelines in the following sections make extensive use of the
macros defined in &#96;+/usr/lib/rpm/macros.d/macros.emacs+&#96; which
is installed with the &#96;+emacs-common+&#96; package.

There are two distinct cases where consideration of these guidelines is
required:

1.  This case refers to the situation where a package's principal
    purpose is to provide extra functionality for Emacs, and the package
    serves no purpose without the presence of Emacs. An example of this
    case is the VM mail reader, as packaged in &#96;+emacs-vm+&#96;.
    Below we refer to this as &#42;Case I&#42;.

2.  This case refers to the situation where a package's principal
    functionality does not require Emacs, but the package also includes
    some auxiliary Elisp files to provide support for the package in
    Emacs. Below we refer to this as &#42;Case II&#42;.

## Package naming and sub-package organization {#_package_naming_and_sub_package_organization}

### Case I {#_case_i}

Where a package is primarily an add-on for Emacs, the main package
should be called &#96;emacs-*foo*&#96;.

### Case II {#_case_ii}

Where a package's principal functionality does not require Emacs, but
the package also includes some auxiliary Elisp files to provide support
for the package in Emacs, these should be included in the main package
which will need to Require the &#96;+emacs-filesystem+&#96; package.
More detail below.

## Package contents {#_package_contents}

### Case I {#_case_i_2}

Files specific to GNU Emacs should be placed in the main package,
&#96;emacs-*foo*&#96;. This should contain the elisp source, compiled
elisp and any other files needed to use the package or sub-package with
GNU Emacs.

### Case II {#_case_ii_2}

The compiled elisp source and the elisp source files should be packaged
as part of the main package, and not split out into separate packages.

## File locations {#_file_locations}

File locations for GNU Emacs add-on (sub-)packages:

&#42; All elisp and related files for the package should be installed in
the directory &#96;+%{*emacs_sitelispdir}/foo+&#96;. &#42; If the
package requires a startup file this should be called
&#96;\_foo*-init.el&#96; and be placed in
&#96;+%{\_emacs_sitestartdir}+&#96;.

## Package Requires {#_package_requires}

### Case I {#_case_i_3}

Package Requires for GNU Emacs add-on (sub-)packages:

&#42; Where relevant &#96;emacs-*foo*&#96; must have &#96;Requires:
emacs-common-*foo* = %{version}-%{release}&#96; &#42;
&#96;emacs-*foo*&#96; must have &#96;+Requires:
emacs(bin)%{?\_emacs_version: &gt;= %{\_emacs_version}}+&#96;

### Case II {#_case_ii_3}

If the package has auxillary files for use with GNU Emacs, the package
must have &#96;+Requires: emacs-filesystem &gt;=
%{\_emacs_version}+&#96;

## Package BuildRequires {#_package_buildrequires}

Package BuildRequires for GNU Emacs add-on packages:

&#42; In general it should suffice to have &#96;+BuildRequires:
emacs-nw+&#96;

## Manual byte compilation {#_manual_byte_compilation_3}

Usually package Elisp compilation is handled via a make file shipped
with the package, but on some occasions it may be necessary to add
commands to the &#96;+%build+&#96; section of the spec file to byte
compile files. In that case, use &#96;+%{\_emacs_bytecompile}
file.el+&#96;

It is a requirement that all Elisp files are byte compiled and packaged,
unless there is a good reason not to, in which case this should be
documented with a comment in the spec file.

## Use of BuildArch: noarch {#_use_of_buildarch_noarch}

If an add-on package requires only byte compilation of elisp then
&#96;+BuildArch: noarch+&#96; should be used. This is highly unlikely to
ever apply to Case II.

## Example spec file templates {#_example_spec_file_templates}

### Template for an add-on package for GNU Emacs (Case I) {#_template_for_an_add_on_package_for_gnu_emacs_case_i}

This is a template for a package for GNU Emacs. The main package is
called &#96;emacs-*foo*&#96; and contains all files needed to run
package foo with GNU Emacs. This includes both compiled and source elisp
files.

&#8230;. %global pkg foo %global pkgname Foo

Name: emacs-%{pkg} Version: Release: %autorelease Summary:

Group: License: URL: Source0:

BuildArch: noarch BuildRequires: emacs-nw Requires:
emacs(bin)%{?\_emacs_version: &gt;= %{\_emacs_version}}

%description %{pkgname} is an add-on package for GNU Emacs. It does
wonderful things&#8230;

%prep %autosetup -n %{pkg}-%{version}

%build

%install

%post

%preun

%files %doc %{\_emacs_sitelispdir}/%{pkg}
%{\_emacs_sitestartdir}/&#42;.el

%changelog %autochangelog &#8230;.

### Template for a package which contains auxiliary GNU Emacs files (Case II) {#_template_for_a_package_which_contains_auxiliary_gnu_emacs_files_case_ii}

This is a skeleton of a package which also includes support files for
GNU Emacs

&#8230;. Name: foo Version: Release: %autorelease Summary:

Group: License: URL: Source0:

BuildRequires: emacs-nw Requires: emacs-filesystem%{?\_emacs_version:
&gt;= %{\_emacs_version}}

%description Foo is a package which contains auxiliary Emacs support
files.

%prep %autosetup

%build

%install

%post

%preun

%files %doc %{\_emacs_sitelispdir}/foo %{\_emacs_sitestartdir}/&#42;.el

%changelog %autochangelog &#8230;.

## Principles behind the guidelines {#_principles_behind_the_guidelines}

### Location of installed files {#_location_of_installed_files}

Files for add-on package foo should be placed in
&#96;+%{*emacs_sitelispdir}/foo+&#96; which evaluates to
&#96;/usr/share/emacs/site-lisp/\_foo*&#96;.

Usually an add-on package will require a startup file, and this should
be called &#96;\_foo\_-init.el&#96; and be placed in
&#96;+%{\_emacs_sitestartdir}\\&#96; which evaluates to
\\&#96;/usr/share/emacs/site-lisp/site-start.d/+&#96;.

### Packaging of source elisp files {#_packaging_of_source_elisp_files}

Typically, an Emacs add-on package will be compiled from source elisp
files. The resulting compiled elisp files will then be included in the
relevant &#96;emacs-*foo*&#96; package. It is important to also include
the source elisp files for several reasons. For example when debugging a
problem with an Emacs package, the Elisp debugger can look up the
relevant code or symbol definition in the source lisp file if present.
Also, it's sometimes helpful to jump to a variable description string
from the Emacs help system.

### BuildArch for Emacs add-on packages {#_buildarch_for_emacs_add_on_packages}

You should set &#96;+BuildArch: noarch+&#96; for add-on packages which
only compile elisp files during building.

If the package building process also compiles programs in other
languages, you may need to not set &#96;+BuildArch+&#96;.

### Requires for GNU Emacs {#_requires_for_gnu_emacs}

Add-on packages should have appropriate Requires entries for the flavor
of Emacs they are targeted at. GNU Emacs is available in multiple
packages - some details of these packages follow.

1.  The &#96;+emacs+&#96; package is built with pure GTK support to
    allow the user to run Emacs in a windowed environment.

2.  The &#96;+emacs-gtk+x11+&#96; package is built with X11 support via
    the GTK toolkit to allow the user to run Emacs in a windowed
    environment.

3.  The &#96;+emacs-lucid+&#96; package is built with X11 support via
    the Lucid toolkit to allow the user to run Emacs in a windowed
    environment.

4.  The &#96;+emacs-nw+&#96; package is built without GUI support. It is
    suitable for running in a terminal.

Note:

&#42; The &#96;+emacs+&#96;, &#96;+emacs-gtk+x11+&#96;,
&#96;+emacs-lucid+&#96;, and &#96;+emacs-nw+&#96; packages all have
Requires: emacs-common. &#42; The emacs, &#96;+emacs-gtk+x11+&#96;,
&#96;+emacs-lucid+&#96;, and &#96;+emacs-nw+&#96; packages all have a
virtual Provides: &#96;+emacs(bin)+&#96;.

Assuming your add-on package will work in both a windowed and a console
Emacs session, it is wrong to have &#96;+Requires: emacs+&#96; as that
would pull in a dependency on GTK even if the console variant of Emacs
is installed. Rather you should use Requires: &#96;+emacs(bin)+&#96; for
GNU Emacs add-on packages.

If the package ONLY works with GTK support built into Emacs, then the
package should have &#96;+Requires: emacs+&#96;. This is very uncommon.

#### Why we need versioned Requires {#_why_we_need_versioned_requires}

Many elisp packages aim for backwards source level compatibility by
checking whether some features exist in the Emacs in use when the
package is being run or byte-compiled. If yes, they use what's
available. If no, they provide their own versions of missing functions,
macros etc. This propagates into &#96;+&#42;.elc+&#96; during byte
compilation, and quite a few functions do get added between upstream
Emacs releases.

So let's say I byte-compile a package into &#96;+&#42;.elc+&#96; with
Emacs 29.3. Elisp package &#96;\_quux\_&#96; checks if the
&#96;\_foo-bar\_&#96; function is available in the Emacs being used to
byte-compile it. Yes, it is, so the internal backwards compat version of
&#96;\_foo-bar\_&#96; included in &#96;\_quux\_&#96; does not end up in
the &#96;+&#42;.elc+&#96;. Now, let's assume &#96;\_foo-bar\_&#96; was
added in Emacs 29.3 and didn't exist in 29.2 and we're trying to run the
&#96;+&#42;.elc+&#96; with 29.2 -&gt; boom, &#96;\_foo-bar\_&#96; is not
available. Note: this wouldn't happen if only &#96;+&#42;.el+&#96; were
shipped - &#96;+&#42;.elc+&#96; are the potential and likely problem.
Requiring &gt;= version of the Emacs used to byte-compile the
&#96;+&#42;.elc+&#96; is not the only solution (nor enough for all
corner cases), but is the best one we currently have available.

The main package and subpackages will need to have appropriately
versioned Requires to ensure that a recent enough version of Emacs is
installed. Emacs byte compiled lisp is usually forward compatible with
later Emacs versions, but is frequently not compatible with earlier
versions of Emacs.

#### Determining the Required Emacs version at package build time {#_determining_the_required_emacs_version_at_package_build_time}

It is recommended to derive greater-than-or-equal-to valued versioned
dependencies from the version of Emacs used to byte-compile the package
at package build time. The &#96;+emacs-common+&#96; package includes
&#96;+/usr/lib/rpm/macros.d/macros.emacs+&#96; which defines a
&#96;+%{\_emacs_version}+&#96; macro containing the version of Emacs
installed.

### Other packages containing Emacsen add-ons (Case II) {#_other_packages_containing_emacsen_add_ons_case_ii}

It is often the case that a software package, while not being primarily
an Emacs add-on package, will contain components for Emacs. For example,
the Gnuplot program contains some elisp files for editing Gnuplot input
files in GNU Emacs and running Gnuplot from GNU Emacs. In this case, we
want to enable the Emacs support IF Emacs is installed, but we don't
want to mandate the installation of Emacs on installation of this
package since Emacs is not required for providing the core functionality
of the package. To enable this, the &#96;+emacs-filesystem+&#96;
sub-package was created which owns the
&#96;+/usr/share/emacs/site-lisp+&#96; directory. A package can then
Require the &#96;+emacs-filesystem+&#96; package in order to install its
Elisp files without pulling in Emacs and its dependency chain.

# Environment Modules {#_environment_modules}

## Introduction {#_introduction_5}

When one has multiple programs serving the same purpose (for instance
SMTP servers such as sendmail, exim and postfix; or print servers such
as lprng and cups), it is usual to wrap these using alternatives.
Alternatives provides a clean way to have many types of software serving
the same purpose installed at the same time and have the commands such
as &#96;+mail+&#96; and &#96;+lpr+&#96; point to the wanted versions.

However, when there are multiple variants that each serve the needs of
some user and thus must be available simultaneously by users, the
alternatives system simply isn't enough since it is system-wide. This
has been reality on supercomputers and clusters for eons, and multiple
implementations of a solution has been developed: [environment
modules](http://modules.sourceforge.net/) and
[Lmod](https://www.tacc.utexas.edu/tacc-projects/lmod). Fedora currently
makes use of this primarily for handling switching between different MPI
implementations.

Environment modules are also useful in situations where a package wants
to install binaries that use common names and might conflict file in or
otherwise pollute /usr/bin. Use must then load an environment module
before being able to make use of those programs.

## Using environment modules {#_using_environment_modules}

To see what modules are available, run &#96;+\$ module avail+&#96;. To
load a module run e.g. &#96;+\$ module load mpi/openmpi-x86_64+&#96;. To
unload a module, run e.g. &#96;+\$module unload
mpi/openmpi-x86_64+&#96;.

The upstream documentation for the module command is available
[here](https://modules.readthedocs.io/en/stable/module.html) or with
&#96;+man module+&#96;.

## Creating environment modules {#_creating_environment_modules}

To install an environment module, place a module file into
&#96;+%{\_modulesdir}\\&#96;, which should evaluate to
\\&#96;/usr/share/modulefiles+&#96;. This macro is available in Fedora
and EPEL 7+. The directory &#96;+/usr/share/Modules/modulefiles+&#96; is
to be used only for internal modules of environment-modules.
&#96;+/etc/modulefiles+&#96; is available to local system administrator
use.

The module files are plain text with optional tcl syntax, for instance
an environment module for 64-bit OpenMPI &#96;+mpi/openmpi-x86_64+&#96;:

&#8230;. &#35;%Module 1.0 &#35; &#35; OpenMPI module for use with
\'environment-modules\' package: &#35; conflict mpi prepend-path PATH
/usr/lib64/openmpi/bin prepend-path LD_LIBRARY_PATH
/usr/lib64/openmpi/lib prepend-path PYTHONPATH
/usr/lib64/python2.7/site-packages/openmpi prepend-path MANPATH
/usr/share/man/openmpi-x86_64 setenv MPI_BIN /usr/lib64/openmpi/bin
setenv MPI_SYSCONFIG /etc/openmpi-x86_64 setenv MPI_FORTRAN_MOD_DIR
/usr/lib64/gfortran/modules/openmpi-x86_64 setenv MPI_INCLUDE
/usr/include/openmpi-x86_64 setenv MPI_LIB /usr/lib64/openmpi/lib setenv
MPI_MAN /usr/share/man/openmpi-x86_64 setenv MPI_PYTHON_SITEARCH
/usr/lib64/python2.7/site-packages/openmpi setenv MPI_COMPILER
openmpi-x86_64 setenv MPI_SUFFIX \_openmpi setenv MPI_HOME
/usr/lib64/openmpi &#8230;.

The module file begins with the magic cookie &#96;+&#35;%Module +&#96;,
where is the version of the module file used. The current version is
1.0.

The above commands prepends the path with the bindir of the 64-bit
OpenMPI (compiled with GCC) and adds the relevant library path. Then it
sets various environment variables.

It is also possible to set &#96;+CFLAGS+&#96; and &#96;+LDFLAGS+&#96;
with the above manner, but in the case of MPI compilers it is not
necessary since the compilers are invoked with the &#96;+mpicc+&#96;,
&#96;+mpicxx+&#96;, &#96;+mpif77+&#96; and &#96;+mpif90+&#96; wrappers
that already contain the necessary include and library paths. Also, in
the case of development packages an override of &#96;+CFLAGS+&#96;
and/or &#96;+LDFLAGS+&#96; is not sane, as it may cause trouble in
building RPMs as it overrides &#96;+%{optflags}+&#96;.

The upstream documentation for module files is available
[here](https://modules.readthedocs.io/en/stable/modulefile.html) or with
&#96;+man modulefile+&#96;.

## Switching between module implementations {#_switching_between_module_implementations}

Switching between the environment-modules and Lmod implementations is
done via alternatives. The shell init scripts
/etc/profile.d/modules.\\{csh,sh} are links to
/etc/alternatives/modules.\\{csh.sh} and can be manipulated with the
alternatives command.

## Lmod {#_lmod}

[Lmod](https://www.tacc.utexas.edu/tacc-projects/lmod) is an environment
modules implementation written in Lua, and can make use of module files
written in Lua as well as Tcl. Such files have a \'.lua\' extensions.
However, such files &#42;must not&#42; be installed
/usr/share/modulefiles so as to not cause issues when the
environment-modules package is in use. Instead install into
%{\_datadir}/lmod/lmod/modulefiles/Core.

# Fonts {#_fonts}

## Foreword {#_foreword}

The bulk of Fedora software relies on OpenType compliance and was tested
against compliant fonts.

Unfortunately, most font makers feel the OpenType specification is a
document written by "software people" for "software people". They spurn
its recommendations. They can not be relied upon to release fonts in a
software-friendly state, nor to fix the resulting problems, nor to
provide useful advice.

To enable the packaging of fonts by non experts,
&lt;&lt;Checklist&gt;&gt; provides a list of sanity rules. Most are
short unambiguous one liners, easy to understand and apply. Do read this
list, even if it feels long. Unless your upstream is a model of
discipline, you WILL need it. Avoid &lt;&lt;Exceptions&gt;&gt; if you do
not feel ambitious -- here be dragons.

Once you sorted what to package using the checklist, the rpm-specific
part of fonts packaging is simple:

&#42; take our spec templates, &#42; fill in the blanks with
descriptions and the file lists resulting from the sorting.

Fedora automation will do the rest.

&lt;&lt;Tooling&gt;&gt; provides in-depth documentation of those
templates, and other operational tips. The operational tips are useful.
The spec templates documentation, not so much. The templates are
commented and will usually be self-explanatory.

Lastly, &lt;&lt;Rationale&gt;&gt; provides some help, in case a third
party attempts to confuse you. A lot of upstreams are dead set against
applying OpenType recommendations. They will provide elaborate
argumentation, on why the common rule does not apply to them.

## Checklist {#_checklist}

### Legal {#_legal}

&#42; \[x\] Font files MUST comply with our
<https://docs.fedoraproject.org/en-US/legal/license-approval/&#35;_licenses_allowed_for_fonts>.
&#42; \[x\] Trademark uses MUST be authorized by their owners,
&#42;&#42; trademarks may occur in font naming or font content
(logos...). &#42; \[x\] Registered names or trademarks MUST NOT prevent
downstream modifications, &#42;&#42; requiring a rename on significant
modification is acceptable.

### Packaging unit: an ideal font family {#_packaging_unit_an_ideal_font_family}

Because fonts upstreams are, on average, extremely messy, a large part
of packaging fonts involves sorting files and fixing font file metadata
to produce the consistent and reliable font catalog expected by
applications and users.

:::::: important
::: title
:::

:::: formalpara
::: title
Font family
:::

A &#42;&#42;font family&#42;&#42; is composed of &#42;font files, that
share a single design, and differ ONLY in&#42;:
::::

+---------+------------------------------------------------------------+
| Weight  | Bold, Black...                                             |
+---------+------------------------------------------------------------+
| Width∕  | Narrow, Condensed, Expanded...                             |
| Stretch |                                                            |
+---------+------------------------------------------------------------+
| Slop    | Italic, Oblique                                            |
| e/Slant |                                                            |
+---------+------------------------------------------------------------+
| Optical | Caption...                                                 |
| sizing  |                                                            |
+---------+------------------------------------------------------------+

Those parameters correspond to the [default
axes](https://docs.microsoft.com/en-us/typography/opentype/spec/dvaraxisreg&#35;registered-axis-tags)
of OpenType variable fonts.
::::::

&#42; \[x\] Packagers MUST apply the definition provided in this section
to determine font family boundaries, &#42;&#42; it takes precedence over
application support concerns, over upstream and packager habits and
practices.

See also the &lt;&lt;Fontconfig&gt;&gt; section.

### Font file formats {#_font_file_formats}

:::::: note
::: title
:::

:::: formalpara
::: title
OpenType: one standard, five formats
:::

[OpenType](https://en.wikipedia.org/wiki/OpenType) uses an *SFNT*
container around bitmaps (&#96;+&#42;.otb+&#96;) and outlines in *TT*
(&#96;+&#42;.ttf+&#96;) or *CFF* (&#96;+&#42;.otf+&#96;) formats.
Multiple fonts can be consolidated in a single collection
(&#96;+&#42;.ttc+&#96; or &#96;+&#42;.otc+&#96;).
::::
::::::

&#42; \[x\] Other font formats MUST be converted to OpenType, &#42;&#42;
except for fonts, intended to be used in the console (NOT a terminal
emulator): see &lt;&lt;Bitmap console fonts&gt;&gt;. &#42; \[x\] Font
packages MUST NOT contain font files in non OpenType formats.

:::::: note
::: title
:::

:::: formalpara
::: title
Font packages
:::

A &#42;font package&#42;, is an installation (RPM) package, containing
OpenType font files. It MAY be produced by a source (SRPM) package, that
also produces other (font or non-font) packages. Other kinds of font
packages are out of scope for this document.
::::
::::::

&#42; \[x\] A font family MUST NOT be packaged in multiple or mixed
OpenType formats, &#42;&#42; except for variable font data, &#42;&#42;
except when mixing is required, to achieve full symbol (glyph) coverage,
&#42;&#42; except as an application workaround; see &lt;&lt;Packaging a
font family in multiple OpenType formats; application support&gt;&gt;.
&#42; \[x\] Both variable and non-variable OpenType font files, SHOULD
be packaged, for a given font family. &#42; \[x\] OpenType format mixing
SHOULD be justified in a comment within the &#96;spec&#96; file. &#42;
\[x\] OpenType collection formats SHOULD be avoided.

### Fontconfig {#_fontconfig}

&#42; \[x\] Font packages SHOULD include the fontconfig files, that
define the selection and substitution rules applying to their font
files, &#42;&#42; written by the packager if upstream does not provide
them. &#42; \[x\] Fontconfig rules MUST rewrite &#96;family&#96; and
&#96;style&#96; when they are not compliant with [OpenType
WWS](https://docs.microsoft.com/en-us/typography/opentype/spec/name&#35;name-ids)
rules: &#42;&#42; &#96;family&#96; MUST NOT contain *Weight*, *Width* or
*Slope* attributes (ideal WWS family name, Name ID 21), &#42;&#42;
&#96;style&#96; MUST contain only *Weight*, *Width* or *Slope*
attributes (ideal WWS subfamily name, Name ID 22), &#42;&#42; Name ID 21
&amp; 22 fields may exist or not in the packaged font files, and may be
correct or not. The packager MUST set the correct value at the
fontconfig level if the value fontconfig extracts from font files is
incorrect. &#42; \[x\] Fontconfig rules MUST rewrite &#96;family&#96; to
remove format attributes when they exist, &#42;&#42; for example:
&#96;OT&#96;, &#96;TT&#96;, &#96;Variable&#96;, &#96;Graphite&#96;,
&#96;G&#96;, etc, &#42;&#42; except when &lt;&lt;Packaging a font family
in multiple OpenType formats; application support&gt;&gt;; in that case
the removal MUST only be done for the font package providing the default
format. &#42; \[x\] Fontconfig rules MUST rewrite &#96;family&#96; to
remove coverage attributes when they exist, &#42;&#42; for example:
&#96;Math&#96;, &#96;Emoji&#96;, &#96;Color Emoji&#96;,
&#96;Hebrew&#96;, &#96;Arabic&#96;, &#96;Thai&#96;, &#96;LGC&#96;, etc,
&#42;&#42; except when several font files provide the same coverage,
requiring a qualifier to distinguish between them; in that case the
removal MUST be done for the default file, and other files MUST be
treated as parts of separate font families. &#42; \[x\] Fontconfig rules
MUST rewrite &#96;fullname&#96; to &#96;&lt;family&gt;
&lt;style&gt;&#96; if it has a different value, &#42;&#42; either
natively or as a result of previous rewrites, &#42;&#42; except for the
default style, usually &#96;Regular&#96;, for which &#96;fullname&#96; =
&#96;&lt;family&gt;&#96;. &#42; \[x\] Fontconfig rules MUST rewrite
&#96;fontversion&#96; when several font files provide the same
&#96;fullname&#96; and have overlapping coverage, &#42;&#42; either
natively or as a result of previous rewrites, &#42;&#42; fontconfig will
merge the result, higher &#96;fontversion&#96; taking precedence over
lower, &#42;&#42; therefore, &#96;fontversion&#96; MUST be set by the
packager, to define the correct ordering. &#42; \[x\] Fontconfig rules
SHOULD define the generic family, a font contributes to, &#42;&#42; a
single generic family: the packager MUST choose, &#42;&#42; using the
correct priority: lower takes precedence over higher. &#42; \[x\]
Fontconfig rules SHOULD list what other font families, the provided font
family can substitute for. &#42;&#42; typically, anterior namings, known
forks, alternatives with the same font metrics... &#42;&#42; also, the
reused fonts families when &lt;&lt;Assembling different-family font
packages: partial designs&gt;&gt;. &#42; \[x\] Fontconfig rules SHOULD
define the font families, that can be used to complete the font family,
&#42;&#42; in all cases: at least the generic family and the substitutes
defined before, &#42;&#42; generic family last in completion order.
&#42; \[x\] Packagers SHOULD attempt upstreaming those fixes, &#42;&#42;
make the font naming correct in the upstream font files, &#42;&#42;
contribute the other fontconfig rules upstream, so they are distributed
with the font files. &#42; \[x\] Packagers SHOULD consult the fontconfig
[maintainer](https://src.fedoraproject.org/rpms/fontconfig/) and
[mailing
list](https://lists.freedesktop.org/mailman/listinfo/fontconfig) when in
doubt, &#42;&#42; to get guidance and identify real-world tricky cases
that call for fontconfig evolutions.

See also the &lt;&lt;Tooling&gt;&gt; section for fontconfig syntax
guidance.

### Source (SRPM) package break-up {#_source_srpm_package_break_up}

&#42; \[x\] Separate source archives MUST be packaged in separate
&#96;spec&#96; files, &#42;&#42; except when those contain parts of the
same font family and upstream coordinates their release. &#42; \[x\]
&#96;spec&#96; files SHOULD track a single font family, &#42;&#42;
except when distinct font families are only released upstream in a
common archive. &#42; \[x\] Packagers SHOULD ask upstream to split
unrelated font families in separate versioned source archives,
&#42;&#42; and package font families from their actual respective
upstreams when they are bundled with other material in a third party
project.

### Installation (RPM) package break-up: font packages {#_installation_rpm_package_break_up_font_packages}

&#42; \[x\] Packagers MUST ship each font family in a single dedicated
font package, &#42;&#42; all the files that, after fontconfig fixing,
&#42;&#42;&#42; share the same &#96;family&#96; value: &#96;family&#96;
= &#96;&lt;common family&gt;&#96; &#42;&#42;&#42; or differ only in
optical sizing: &#96;family&#96; = &#96;&lt;common family&gt;
&lt;optical sizing attribute&gt;&#96;, &#42;&#42; except when released
as un-coordinated sources, that are easier to track in separate
&#96;spec&#96; files, &#42;&#42; except for huge families, that consume
a lot of storage space; huge font families MAY be broken up in
coverage-specific font packages, &#42;&#42; see &lt;&lt;Assembling
same-family font packages&gt;&gt;. &#42; \[x\] Font packages MUST limit
themsemselves to OpenType font files and their associated
[fontconfig](https://www.fontconfig.org/),
[appstream](https://www.freedesktop.org/software/appstream/docs/sect-Metadata-Fonts.html),
legal and documentation files, &#42;&#42; for reasonable non-bulky
interpretations of documentation files.

See also the &lt;&lt;Tooling&gt;&gt; section.

:::::: important
::: title
:::

:::: formalpara
::: title
Other upstream files
:::

Support for other font systems, for specific applications, non-OpenType
font formats, bulky documentation, TEX, CSS, or JSON files... MUST be
split in separate non-font packages, that SHOULD install outside
&#96;/usr/share/fonts&#96;, and MUST NOT use
&#96;\_&lt;something&gt;\_-fonts&#96; naming.
::::

For compatibility reasons, OpenType font files MAY be exposed outside
&#96;/usr/share/fonts&#96;, with the rest of upstream files, using
symbolic links. Those symbolic links SHOULD NOT be installed by the font
package itself.
::::::

### Building {#_building}

&#42; \[x\] Packagers SHOULD build font files from sources, &#42;&#42;
whenever their prefered modification format is not the packaged OpenType
format &#42;&#42; and if the required toolchain is available as free
software under Linux

### Dependencies in font packages {#_dependencies_in_font_packages}

&#42; \[x\] Font packages MAY require or supplement other font packages,
when they contain the same font family, &#42;&#42; as defined in
&lt;&lt;Assembling same-family font packages&gt;&gt;. &#42; \[x\] Font
packages SHOULD recommend other font packages, when they contain a
reused font family, &#42;&#42; as defined in &lt;&lt;Assembling
different-family font packages: partial designs&gt;&gt;. &#42; \[x\]
Font packages SHOULD suggest other font packages, when they contain a
better version of the same font family, &#42;&#42; better: more complete
coverage, later enhanced fork, canonical version of the design... &#42;
\[x\] Font packages MAY suggest or enhance font packages, containing
other font families, &#42;&#42; this should be used sparsely, to avoid
imposing packager preferences on users. &#42; \[x\] Font packages SHOULD
depend on the basic font support package set, defined in the font
packaging templates and macros. &#42; \[x\] Except for the preceding,
font packages MUST NOT depend, in any form, on any other package.

### Dependencies to font packages in other packages {#_dependencies_to_font_packages_in_other_packages}

&#42; \[x\] Non-font packages MAY suggest or recommend font packages,
&#42;&#42; the weakest &#96;Suggests&#96; form is preferred over
&#96;Recommends&#96;, except in presence of strong pre-existing user
habits. &#42; \[x\] Non-font packages SHOULD use the &#96;font()&#96;
namespace to depend on font packages. &#42; \[x\] Non-font packages
SHOULD NOT require specific font packages, and leave font selection to
end-users, &#42;&#42; except when the packaged software actually relies
on those specific font packages, &#42;&#42; except for convenience font
metapackages, as defined in &lt;&lt;Assembling different-family font
packages: font metapackages&gt;&gt;. &#42; \[x\] Non-font packages
SHOULD require &#96;font(:lang=en)&#96; when they fail in the absence of
system fonts, &#42;&#42; hardcoding specific font families is not
future-proof. &#42; \[x\] Non-font packages MAY require font packages by
name, when relying on specific on-disk font file paths, &#42;&#42; ie
when software is not &#96;fontconfig&#96;-aware, &#42;&#42; however,
there is no obligation for font packagers to keep those paths stable
between releases. Font file formats are flexible, making any on-disk
file layout temporary. Converting applications to fontconfig use is
best.

### Assembling different-family font packages: partial designs {#_assembling_different_family_font_packages_partial_designs}

:::::: note
::: title
:::

:::: formalpara
::: title
Font reuse and font extension
:::

Because font creation is hard work, font designers will often publish
partial new designs:
::::

&#42; they will copy part of an existing design, then add to it; this is
common practice when designing a non-latin-oriented font family -- the
latin core is taken from an existing family, &#42; or they will publish
their additions as a separate font family, documenting it should be used
with the original family; this is common practice when publishing
alternate designs for part of a font.
::::::

When packaging such a partial design:

&#42; \[x\] The font package containing the new font family SHOULD
recommend the package containing the original font family, &#42;&#42;
only the core package of the original font family in case of
&lt;&lt;Assembling same-family font packages&gt;&gt;. &#42; \[x\] Re-use
recommendations SHOULD use the &#96;font()&#96; namespace.

### Assembling different-family font packages: font metapackages {#_assembling_different_family_font_packages_font_metapackages}

&#42; \[x\] Packagers MAY provide convenience font metapackages,
&#42;&#42; for example, when an upstream releases a collection of font
families, intended to be used together, &#42;&#42; a common case is
matched *serif*, *sans-serif* and *monospaced* font families. &#42;
\[x\] Font metapackages MUST NOT use the same naming conventions as
actual font packages, &#42;&#42; they MUST NOT be named
&#96;\_&lt;something&gt;\_-fonts&#96;, &#42;&#42; they MAY be named
&#96;\_&lt;something&gt;\_-fonts-all&#96;. &#42; \[x\] Font metapackages
MUST require, recommend or suggest separate font packages, that conform
to this document, &#42; \[x\] Font metapackages SHOULD use the
&#96;font()&#96; namespace to require, recommend or suggest actual font
packages, &#42;&#42; see &lt;&lt;Dependencies to font packages in other
packages&gt;&gt;. &#42; \[x\] Font metapackages SHOULD NOT contain any
other file, except for documentation.

## Exceptions {#_exceptions_3}

### Bitmap console fonts {#_bitmap_console_fonts}

&#42; \[x\] Bitmap console fonts MAY be packaged in a legacy font
format, understood by [kbd](https://kbd-project.org/). &#42; \[x\]
Bitmap console fonts MUST be installed in
&#96;/lib/kbd/consolefonts/&#96; not &#96;/usr/share/fonts&#96;. &#42;
\[x\] Bitmap console font packages SHOULD be named
&#96;\_&lt;something&gt;\_-fonts-console&#96; not
&#96;\_&lt;something&gt;\_-fonts&#96;.

:::::: note
::: title
:::

:::: formalpara
::: title
Console fonts
:::

As long as [kbd](https://kbd-project.org/) and
[systemd-vconsole](https://www.freedesktop.org/software/systemd/man/vconsole.conf.html)
can not use the same file formats as the rest of the system, bitmap
console fonts are effectively private kbd resources. They will be
ignored in the rest of this document. It does not apply to them.
::::
::::::

### Assembling same-family font packages {#_assembling_same_family_font_packages}

&#42; \[x\] A font family MUST NOT be split over several font packages,
unless one of the exceptions listed above applies.

When a font family is split over a set of several font packages:

&#42; \[x\] Involved packagers MUST choose a core font package. &#42;
\[x\] This core package SHOULD contain the font files, necessary to
provide a minimal scope of the font family. &#42; \[x\] This core
package MAY contain fontconfig rules, for all the font files composinng
the font family, &#42;&#42; fontconfig ignores rules that do not match
installed files. &#42; \[x\] This core package MUST be named as if it
contained the whole font family. &#42; \[x\] This core package MUST NOT
require any other package in the set. &#42; \[x\] The other packages of
the set MUST require, directly or indirectly, this core package. &#42;
\[x\] The other packages of the set MUST supplement, directly or
indirectly, this core package. &#42; \[x\] The other packages of the set
MUST NOT use the &#96;font()&#96; namespace to require or supplement
other parts of the set, &#42;&#42; Splitting a font family interacts
badly with &#96;font()&#96; auto-provides. &#42; \[x\] All the packages
involved in an indirect require or supplement chain MUST be part of the
set.

### Packaging a font family in multiple OpenType formats; application support {#_packaging_a_font_family_in_multiple_opentype_formats_application_support}

&#42; \[x\] Packagers MUST make a reasonable effort, to get applications
that do not support all OpenType formats, fixed upstream. &#42; \[x\] If
that fails, as a last ressort, packagers MAY request a [FESCo
exemption](https://pagure.io/fesco), to package a limited number of font
families in multiple OpenType formats. &#42; \[x\] Packagers MUST ensure
that the resulting additional font data, is separated in distinct font
packages, &#42;&#42; that the average Fedora user can install those font
families in a single format, &#42;&#42; that he is not left wondering,
which package to install.

## Tooling {#_tooling}

Creating font packages by hand can be extremely repetitive, error-prone
and labor-intensive. Therefore, fonts packaging is heavily automated. It
relies on numerous macros and variables to define what goes where.

Those macros and variables are defined in the &#96;fonts-rpm-macros&#96;
package. The &#96;fonts-rpm-templates&#96; package contains
&#96;spec&#96; and &#96;fontconfig&#96; templates, corresponding to
common fonts packaging needs.

### Fontconfig {#_fontconfig_2}

The &#96;fonts-rpm-templates&#96; package contains &#96;fontconfig&#96;
templates, corresponding to common fonts packaging needs.

Using fontconfig, you can help users and software make sense of broken
font files.

:::::: note
::: title
:::

:::: formalpara
::: title
On brokenness and interoperability
:::

Fixing may imply behaviour differences, with entities that chose another
mitigation strategy. The root cause of those differences is the upstream
release of files in a broken state. Producing daring glyph shapes is the
designer prerogative. That artistic license does not extend to flouting
technical conventions, software relies on.
::::

Upstream should always be given the chance to fix its files. If it does
not care about our needs, fixing downstream is second best. Inflicting
intact breakage on our users is always worst.
::::::

#### Some applications {#_some_applications}

- The Foo project releases &#96;Foo Narrow Oblique&#96;. Because the
  font maker remembers early font formats only allowed 4-style family
  grouping ([Name
  ID](https://docs.microsoft.com/en-us/typography/opentype/spec/name&#35;name-ids)
  1 and 2), it declares it as &#96;family: Foo Narrow&#96; and
  &#96;style: Oblique&#96;. The fontconfig rules for &#96;Foo Narrow
  Oblique&#96; MUST rewrite it to the
  [recommended](https://docs.microsoft.com/en-us/typography/opentype/spec/namesmp)
  [WWS-compliant](https://docs.microsoft.com/en-us/typography/opentype/spec/name&#35;nid21)
  &#96;family: Foo&#96; and &#96;style: Narrow Oblique&#96; (Name ID
  16/17 or 21/22).

- The Foo project releases the &#96;Universal Foo&#96; wide-coverage
  font family. To allow installing only part of this family, it splits
  it in &#96;Universal Foo&#96;, &#96;Universal Foo Hebrew&#96; and
  &#96;Universal Foo Thai&#96;. The fontconfig rules for &#96;Universal
  Foo&#96; MUST rewrite the &#96;family&#96; (and therefore
  &#96;fullname&#96;) for all &#96;Universal Foo Hebrew&#96; and
  &#96;Universal Foo Thai&#96; font files, so they declare
  &#96;Universal Foo&#96; instead. Fontconfig will present the result as
  a single wide-encoding family to applications, even if the files
  remain split on-disk, even if all of them are not installed.

- The Foo project releases &#96;Foo Sans&#96;. The fontconfig rules for
  &#96;Foo Sans&#96; SHOULD declare any missing glyph can be taken from
  the &#96;sans-serif&#96; generic font family.

- The GNOME project releases the &#96;Bitstream Vera&#96; set of font
  families; later the &#96;DejaVu&#96; project forks and extends those
  fonts. The fontconfig rules for &#96;DejaVu Sans&#96; SHOULD declare
  it can be substituted for &#96;Bitstream Vera Sans&#96;.

- Microsoft ships Windows with the &#96;Arial&#96; font family. Due to
  its long and wide availability, &#96;Arial&#96; is now used in many
  documents. However it can not be included in Free Desktop systems for
  licensing reasons. Red Hat commissions an &#96;Arial&#96; substitute,
  &#96;Liberation Sans&#96;, for use on Linux. Google commissions
  another &#96;Arial&#96; substiture, &#96;Arimo&#96;, for use on
  ChromeOS. The fontconfig rules for &#96;Liberation Sans&#96; SHOULD
  declare it can be substituted for both &#96;Arial&#96; and
  &#96;Arimo&#96;.

#### Style naming {#_style_naming}

The
[OpenType](https://docs.microsoft.com/en-us/typography/opentype/spec/os2&#35;usweightclass)
[specification](https://docs.microsoft.com/en-us/typography/opentype/spec/os2&#35;uswidthclass),
the [CSS](https://www.w3.org/TR/css-fonts-4/&#35;font-weight-prop)
[specification](https://www.w3.org/TR/css-fonts-4/&#35;font-stretch-prop)
and the [fontconfig
manual](https://www.freedesktop.org/software/fontconfig/fontconfig-user.html)
document the canonical mappings of style keywords.

Those mappings are not absolute. The addition of variable capabilities
enabled the creation of new keywords and axes values, including in non
variable font files.

Nevertheless, the OpenType specification requires correlating the new
capabilities with the traditional keyword scale:

&#42; \[x\] an axis step, with a value, close to one of the
specification keywords, SHOULD be named with this keyword, &#42;&#42; a
slight deviation from the canonical keyword value, for design reasons,
is expected and accepted. &#42; \[x\] an axis step, SHOULD NOT be named
with a keyword, when its value differs greatly from the keyword
canonical value, &#42;&#42; font files that define new intermediary
steps should also define new keywords.

Additionnally:

&#42; \[x\] axis keywords SHOULD NOT use whitespace, due to software
processing constraints, &#42;&#42; &#96;SemiCondensed&#96; is a good
keyword; &#96;Semi Condensed&#96; --- not. &#42; \[x\] keywords SHOULD
be assembled in &#96;width weight slant&#96; order in style names, for
historical reasons, &#42;&#42; with the default &#96;Regular&#96;
ommited except when alone.

#### Checking results {#_checking_results}

To verify the metadata of font files installed by a package named
&#96;\${pkg}&#96;:

:::: formalpara
::: title
Check command
:::

``` bash
fc-scan -f \
'%{family[0]};%{style[0]};%{fullname[0]};%{width};%{weight};%{slant};%{fontversion};%{file}\n' \
/usr/share/fonts/${pkg} | sort -t ';' -k1,1d -k4,4n -k5,5n -k6,6n -k2,2d -k7,7dr \
| uniq | column --separator ';' -t
```
::::

:::: formalpara
::: title
Command output, before fixes
:::

    …
::::

:::: formalpara
::: title
Command output, once fixed
:::

    …
::::

### Spec template documentation {#_spec_template_documentation}

The &#96;fonts-rpm-templates&#96; package contains &#96;spec&#96;
templates, corresponding to common fonts packaging needs.

#### Packaging a single font family {#_packaging_a_single_font_family}

This is the simplest packaging pattern, when upstream releases:

&#42; a single font family, &#42; conforming to this guideline's
definition of a font family, &#42; in a single dedicated source archive,
&#42; without any specific difficulty.

##### Macros and variables {#_macros_and_variables}

:::::: important
::: title
:::

:::: formalpara
::: title
Declaration ordering
:::

Changing the proposed line order will more often than not result in a
&#96;spec&#96; file that still works. That may be tempting, since the
suggested order is far from traditional.
::::

Be aware that this particular order was selected after reworking a large
pool of test files, to maximize commonalities, and reduce divergence
between packaging situations. Reordering may still work but the result
will be harder to review, refactor, and copy in other &#96;spec&#96;
files.
::::::

###### SRPM generic declarations {#_srpm_generic_declarations}

This pattern starts with a block of traditional &#96;spec&#96;
declarations:

:::: formalpara
::: title
SRPM generic declarations
:::

``` rpm-spec
Version:
Release:
URL:
```
::::

###### Shared font declarations {#_shared_font_declarations}

Then it declares elements, that will be shared by all the packaged font
families. Here, we only process one of those, but the block will be at
the same place in the other patterns.

+---------+------------------------------------------------------------+
| %{f     | an optional upstream identifier, when upstream publishes   |
| oundry} | multiple font families, with consistent QA rules. Font     |
|         | families released by the same upstream will usually play   |
|         | well with one another. Marking them as such helps users    |
|         | choose good font package sets. If there is no registered   |
|         | foundry, the name or brandname of the typographer can be   |
|         | used instead provided it enables distinguishing the font.  |
|         | &#42; for example, the [Open Font                          |
|         | Library](https://fontlibrary.org/) identifier is           |
|         | &#96;oflb&#96;.                                            |
+---------+------------------------------------------------------------+
| %{fontl | the identifier of the font family license, according to    |
| icense} | our licensing rules.                                       |
+---------+------------------------------------------------------------+

Those identifiers are followed by variables, containing:

&#42; lists of space-separated shell globs, &#42; matching the files
associated with the font family, &#42; as they exist in the build root
at the end of the &#96;%build&#96; stage.

+---------+------------------------------------------------------------+
| %       | the font family legal files                                |
| {fontli |                                                            |
| censes} |                                                            |
+---------+------------------------------------------------------------+
| %{fo    | the font family documentation files                        |
| ntdocs} |                                                            |
+---------+------------------------------------------------------------+
| %{font  | exclusions from the &#96;%{fontdocs}&#96; list             |
| docsex} |                                                            |
+---------+------------------------------------------------------------+

:::: formalpara
::: title
Shared font declarations
:::

``` rpm-spec
%global foundry           SIL
%global fontlicense       OFL-1.1
%global fontlicenses      OFL.txt
%global fontdocs          \&#42;.txt
%global fontdocsex        %{fontlicenses}
```
::::

###### Family-specific font declarations {#_family_specific_font_declarations}

This is followed by a family-specific declaration block.

+---------+------------------------------------------------------------+
| %{font  | the human-friendly font family name, whitespace included,  |
| family} | restricted to the &#42;Basic Latin&#42; Unicode block.     |
+---------+------------------------------------------------------------+
| %{fonts | the generated font package summary. It must be less than   |
| ummary} | 80 columns in length.                                      |
+---------+------------------------------------------------------------+

This block contains its own shell glob lists.

+---------+------------------------------------------------------------+
| %       | the font family font files                                 |
| {fonts} |                                                            |
+---------+------------------------------------------------------------+
| %{fon   | the font family fontconfig files                           |
| tconfs} |                                                            |
+---------+------------------------------------------------------------+

Followed by:

+---------+------------------------------------------------------------+
| %{fo    | a multi-line description block for the generated package.  |
| ntdescr | Each line should be less than 80 columns in length.        |
| iption} |                                                            |
+---------+------------------------------------------------------------+

:::: formalpara
::: title
Family-specific font declarations
:::

``` rpm-spec
%global fontfamily        Andika
%global fontsummary       SIL Andika, a font family for literacy and beginning readers
%global fonts             \&#42;.ttf
%global fontconfs         %{SOURCE10}
%global fontdescription   %{expand:
Andika is a sans serif, Unicode-compliant font family designed especially for
literacy use, taking into account the needs of beginning readers. The focus is
on clear, easy-to-perceive letterforms that will not be readily confused with
one another.}
```
::::

###### Source declarations {#_source_declarations}

Then package sources are declared the usual way.

:::: formalpara
::: title
Source declarations
:::

``` rpm-spec
Source:
Source10: [number]-%{fontpkgname}.conf
```
::::

Keeping fontconfig file names in sync with the package name is a good
idea. Take a look at the templates in &#96;fonts-rpm-templates&#96; for
information on how to write good fontconfig files and choose the correct
priority &#96;\[number\]&#96;.

:::::: note
::: title
:::

:::: formalpara
::: title
Font package names
:::

Font package names will be automatically computed from the previous
declarations, and put into the &#96;%{fontpkgname}&#96; variable. You
MAY override this variable at need. However, needing an override usually
indicates that either the upstream font naming is broken, or you're
trying to do something wrong.
::::
::::::

###### Remainer of the spec file {#_remainer_of_the_spec_file}

All those declarations are used and processed in the rest of the
&#96;spec&#96; file by the following macros:

+---------+------------------------------------------------------------+
| %       | generate font package headers                              |
| fontpkg |                                                            |
+---------+------------------------------------------------------------+
| %fo     | perform font-related steps, at the end of the              |
| ntbuild | &#96;%build&#96; section                                   |
+---------+------------------------------------------------------------+
| %font   | perform font-related steps, at the end of the              |
| install | &#96;%install&#96; section                                 |
+---------+------------------------------------------------------------+
| %fo     | perform font-related steps, at the end of the              |
| ntcheck | &#96;%check&#96; section                                   |
+---------+------------------------------------------------------------+
| %fo     | generate font package &#96;%file&#96; lists                |
| ntfiles |                                                            |
+---------+------------------------------------------------------------+

:::: formalpara
::: title
Remainer of the spec file
:::

``` rpm-spec
%fontpkg

%prep
%setup

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
```
::::

##### Annotated spec template {#_annotated_spec_template}

Putting it all together:

:::: formalpara
::: title
spectemplate-fonts-0-simple.spec
:::

``` rpm-spec
```
::::

#### Packaging a single font family (advanced) {#_packaging_a_single_font_family_advanced}

Sometimes, packaging a font family requires a little more work, with the
associated automation. You may need to complete the previous pattern.

##### Macros and variables {#_macros_and_variables_2}

###### Shared font declarations {#_shared_font_declarations_2}

One more shell glob list:

+---------+------------------------------------------------------------+
| %{f     | exclusions from the &#42;%{fontlicenses}&#42; list         |
| ontlice |                                                            |
| nsesex} |                                                            |
+---------+------------------------------------------------------------+

###### Family-specific font declarations {#_family_specific_font_declarations_2}

+---------+------------------------------------------------------------+
| %{      | multi-line container for package header directives         |
| fontpkg |                                                            |
| header} |                                                            |
+---------+------------------------------------------------------------+

:::: formalpara
::: title
Semi-complex family declaration
:::

``` rpm-spec
%global fontfamily        PT Sans
%global fontsummary       PT Sans, a grotesque pan-Cyrillic font family
%global fontpkgheader     %{expand:
Obsoletes: paratype-pt-sans-caption-fonts \&lt; %{version}-%{release}
}
%global fonts             PTS\&#42;.ttf PTN\&#42;.ttf PTC\&#42;.ttf
%global fontconfs         %{SOURCE10}
%global fontdescription   %{expand:
The PT Sans family was developed as part of the “Public Types of Russian
Federation” project. This project aims at enabling the peoples of Russia to
read and write their native languages, using free/libre fonts. It is
dedicated to the 300-year anniversary of the Russian civil type invented by
Peter the Great from 1708 to 1710, and was realized with financial support
from the Russian Federal Agency for Press and Mass Communications.}
```
::::

... and more shell glob lists:

+---------+------------------------------------------------------------+
| %{f     | exclusions from the &#42;%{fonts}&#42; list                |
| ontsex} |                                                            |
+---------+------------------------------------------------------------+
| %{fontc | exclusions from the &#42;%{fontconfs}&#42; list            |
| onfsex} |                                                            |
+---------+------------------------------------------------------------+
| %{f     | the font family *appstream* files, if any; those files are |
| ontapps | generated automatically if not specified                   |
| treams} |                                                            |
+---------+------------------------------------------------------------+
| %{fon   | exclusions from the &#42;%{fontappstreams}&#42; list       |
| tappstr |                                                            |
| eamsex} |                                                            |
+---------+------------------------------------------------------------+

###### Remainer of the spec file {#_remainer_of_the_spec_file_2}

Bulky documentation can be split in a separate subpackage

:::: formalpara
::: title
Documentation subpackage
:::

``` rpm-spec
%package   doc
Summary:   %{name} optional documentation files
BuildArch: noarch
%description doc
This package provides optional documentation files shipped with %{name}.

[…]

%files doc
%license OFL.txt
%doc \&#42;.pdf
```
::::

Text files published for other systems may need recoding.

+---------+------------------------------------------------------------+
| %li     | allows converting upstream files to UTF-8 and Unix end of  |
| nuxtext | lines if necessary. It takes the following optional        |
|         | arguments: &#42; &#96;-e \[encoding\]&#96; source OS       |
|         | encoding (automatically detected otherwise) &#42;          |
|         | &#96;-n&#96; do not recode files, only adjust folding and  |
|         | end of lines                                               |
+---------+------------------------------------------------------------+

##### Annotated spec template {#_annotated_spec_template_2}

Putting it all together:

:::: formalpara
::: title
spectemplate-fonts-1-full.spec
:::

``` rpm-spec
```
::::

#### Packaging multiple font families {#_packaging_multiple_font_families}

Those patterns can be extended the following way, when packaging
multiple font families, from a project named after the main packaged
family.

##### Macros and variables {#_macros_and_variables_3}

###### Shared font declarations {#_shared_font_declarations_3}

&#96;%{foundry}&#96;, &#96;%{fontlicense}&#96;,
&#96;%{fontlicensex}&#96;, &#96;%{fontdocs}&#96; and
&#96;%{fontdocsex}&#96; are applied to all font families,

&#42; unless overriden by the same variable, suffixed with a specific
block number &#42; for example &#96;%{fontdocs2}&#96;

A variable, can be used to share a description block:

:::: formalpara
::: title
Using a common description variable
:::

``` rpm-spec
%global common_description %{expand:
IBM wanted Plex to be a distinctive, yet timeless workhorse — an alternative to
its previous corporate font family, “Helvetica Neue”, for this new era. The
Grotesque style was the perfect fit. Not only do Grotesque font families
balance human and rational elements, the Grotesque style also came about during
the Industrial Age, when IBM was born.}

[…]

%global fontfamily1       Plex Sans
%global fontsummary1      IBM Plex Sans, the new grotesque IBM corporate font family
%global fontpkgheader1 %{expand:
Suggests: font(ibmplexsansmono)
}
%global fonts1            IBM-Plex-{Sans,Sans-\&#42;,Arabic}/fonts/complete/otf/\&#42;otf
%global fontsex1          IBM-Plex-Sans-Thai-Looped/fonts/complete/otf/\&#42;otf
%global fontconfs1        %{SOURCE11} 65-%{fontpkgname1}.conf
%global fontdescription1  %{expand:
%{common_description}
This package provides the grotesque sans-serif variable-width IBM Plex Sans,
the main font family of the Plex set.}

%global fontfamily2       Plex Mono
%global fontsummary2      IBM Plex Mono, the monospace grotesque coding font family of the Plex set
%global fonts2            IBM-Plex-Mono/fonts/complete/otf/\&#42;otf
%global fontconfs2        %{SOURCE12}
%global fontdescription2  %{expand:
%{common_description}
This package provides the grotesque sans-serif fixed-width IBM Plex Mono, a
little something for developers, because monospace does not need to be monotone.}
```
::::

###### Family-specific font declarations {#_family_specific_font_declarations_3}

&#42; each font family is declared in a separate family-specific block,
&#42; each block is identified by a number, suffixed to the
corresponding block variables, &#42;&#42; for example
&#96;%{fontfamily1}&#96; &#42; the zero-suffix block is used to generate
SRPM metadata, &#42; all the zero-suffix variables are aliased to
no-suffix variables of the same name, and vice versa.

###### Packaging macros {#_packaging_macros}

&#42; &#96;%fontpkg&#96;, &#96;%fontbuild&#96;, &#96;%fontinstall&#96;,
&#96;%fontcheck&#96; and &#96;%fontfiles&#96; accept the following
arguments: &#42;&#42; &#96;-a&#96; process everything &#42;&#42; &#96;-z
\[number\]&#96; process the &#96;\[number\]&#96; declaration block &#42;
if no flag is specified they will only process the zero/no-suffix block
&#42;&#42; consequently, packaging multiple font families will usually
require the &#96;-a&#96; option

+---------+------------------------------------------------------------+
| %{      | generate font package headers. Optional arguments (usually |
| \\fontm | unnecessary):                                              |
| etapkg} |                                                            |
+---------+------------------------------------------------------------+

&#42; &#96;-n \[name\]&#96; use &#96;\[name\]&#96; as metapackage name
&#42; &#96;-s \[variable\]&#96; use the content of &#96;\[text\]&#96; as
metapackage summary &#42; &#96;-d \[variable\]&#96; use the content of
&#96;\[variable\]&#96; as metapackage description &#42; &#96;-z
\[numbers\]&#96; restrict metapackaging to &#96;\[numbers\]&#96;è
space-separated list of font package suffixes

:::: formalpara
::: title
Complex metapackaging example
:::

``` rpm-spec
%fontmetapkg -z 1,2,3

%global lgcmetasummary All the font packages, generated from %{name}, Latin-Greek-Cyrillic subset
%global lgcmetadescription %{expand:
This metapackage installs all the font packages, generated from the %{name}
source package, in a version restricted to coverage of Latin, Greek and
Cyrillic.
}

%fontmetapkg -n dejavu-lgc-fonts-all -s lgcmetasummary -d lgcmetadescription -z 4,5,6
```
::::

##### Annotated spec template {#_annotated_spec_template_3}

Putting it all together:

:::: formalpara
::: title
spectemplate-fonts-2-multi.spec
:::

``` rpm-spec
```
::::

#### Packaging font families, released as part of something else {#_packaging_font_families_released_as_part_of_something_else}

The last pattern concerns the packaging one or several font families
from a source rpm which is not named after the first packaged font
family:

&#42; either because the project name differs from the main font family
name, &#42; or when the source archive and rpm are used to package more
than fonts.

It is almost identical to the previous one.

##### Macros and variables {#_macros_and_variables_4}

###### Family-specific font declarations {#_family_specific_font_declarations_4}

Do not declare a zero/no-suffix family-specific block, as it will
attempt to generate SRPM metadata, and collide with existing SRPM
declarations.

##### Annotated spec template {#_annotated_spec_template_4}

Putting it all together:

:::: formalpara
::: title
spectemplate-fonts-3-sub.spec
:::

``` rpm-spec
```
::::

## Rationale {#_rationale_2}

### Legal {#_legal_2}

Fonts are subject to specific copyright, trademark and patent laws.
Reading our [fonts legal
page](https://fedoraproject.org/wiki/Legal_considerations_for_fonts) is
recommended.

### Packaging unit: an ideal font family {#_packaging_unit_an_ideal_font_family_2}

Font upstreams will often deviate from the OpenType model in their
naming:

&#42; because mistakes happen, &#42; because font formats are complex,
with a long history, and a huge amount of legacy compability bagage,
&#42; because upstreams may focus on the artistic side of font creation,
to the detriment of its technical side, &#42; because upstreams may
attempt to workaround problems in the legacy proprietary applications
available on their platform of choice, &#42; because upstreams may be
dormant, and miss changes in the OpenType specification, or use font
creation tools that have still not implemented those changes.

Those deviations occur in upstream file names and upstream font file
metadata. Upstream choices in those elements can not be relied upon to
define useful and consistent font family boundaries.

Shared font files, are no place to workaround application-specific
problems. Fedora must apply the OpenType standard strictly, to enable
the leveraging by Free Desktop applications, of the application
capabilities this standard was designed to unlock. One can always find
bits of code not updated to take into account decades-old changes in
font standards. Waiting on this code to be fixed is being last, not
*First*.

### Font file formats {#_font_file_formats_2}

#### OpenType highlights {#_opentype_highlights}

##### Variable fonts {#_variable_fonts}

Application support for variable fonts is sparse right now. They can not
replace older OpenType formats yet.

##### TT versus CFF {#_tt_versus_cff}

&#42; OpenType TT boasts
[hinting](https://en.wikipedia.org/wiki/Font_hinting) capabilities, but
hinting is labor-intensive and does not scale to large-encoding fonts.
In practice modern TT fonts are hinted using automated processes similar
to the auto-hinter present in [freetype](https://www.freetype.org/).
&#42; OpenType CFF lacks hinting but uses the excellent rasterizer Adobe
[contributed](https://opensource.googleblog.com/2013/05/got-cff.html) to
freetype, achieving similar results. &#42; Low-resolution rendering is
increasingly irrelevant with the replacement of 96dpi screens by 4K+
HiDPI hardware.

Therefore, don't use hinting as a format selection criterium, unless
you're sure a human actually proofed the result on a modern renderer, at
the screen pixel densities exercised by Fedora users.

Choose the OpenType format best supported upstream, typically the one
produced by upstream's preferred font creation toolchain. For historical
reasons the math behind OpenType TT and OpenType CFF differs, converting
from one to the other may introduce corner cases problems.

##### Collections {#_collections}

While collection formats save some storage space, they introduce a high
level of complexity packaging and application-side, make it impossible
to install font families separately, and create a user-unfriendly
environment.

Avoid packaging &#96;+&#42;.ttc+&#96; and &#96;+&#42;.otc+&#96; files
unless left no choice by upstream.

#### Legacy deprecated formats {#_legacy_deprecated_formats}

Legacy formats are too limited to handle Unicode-level coverage, fail to
declare their encoding, do not permit the kind of style selection
expected in modern fonts, do not provide human-friendly naming layers,
etc. They're full of quirks and a source of (security) bugs in
applications.

In 2006, at the first [Text
Layout](https://www.freedesktop.org/wiki/TextLayout/) summit, all the
major Free Desktop players agreed to converge on a unified text layout
engine, built around the
[HarfBuzz](https://github.com/harfbuzz/harfbuzz) project and the
OpenType format. As a result, modern Free Desktop applications and
libraries [no](https://bugzilla.redhat.com/show_bug.cgi?id=1753295)
[longer](https://bugs.documentfoundation.org/show_bug.cgi?id=104701)
[support](https://gitlab.gnome.org/GNOME/pango/issues/368) other
formats.

Use tools like [fontforge](https://fontforge.github.io/) or
[fonttosfnt](https://fedoraproject.org/wiki/BitmapFontConversion)
(provided by xorg-x11-font-utils) to
[convert](https://gitlab.gnome.org/GNOME/pango/issues/386&#35;note_568255)
legacy fonts to an OpenType format. Get it done upstream or script it
within the &#96;%build&#96; section of your &#96;spec&#96; file.

Like any other format conversion it will need some proofing. That's why
packaging fonts in a &#42;single&#42; &#42;correct&#42; format is a
requisite for reliable text rendering.

##### Web fonts {#_web_fonts}

Due to the limitations of the browsers that existed at the time, and due
to the fear foundries had of widespread font piracy, initial support for
web fonts used a hodgepole of obscure, broken and incomplete font
formats (&#96;svg&#96;, &#96;eot&#96;, &#96;woff&#96;, etc).

All major browsers have been [fixed](https://caniuse.com/&#35;feat=ttf)
long ago to accept OpenType fonts.

Do not package web fonts except in OpenType format. If your upstream
still religiously cargo-cults other formats in its CSS files, get those
fixed.

The only remotely useful web font format is &#96;woff&#96;. Its
advantages compared to OpenType are marginal at best on a
well-configured web server. The sole remaining reason for &#96;woff&#96;
existence is to serve as a light form of DRM for proprietary fonts
(Normal applications do not read &#96;woff&#96; files). That concern
does not apply to Fedora. Fedora wants to *share*. Any so-called web
font can be useful in
[other](https://fedoramagazine.org/tuning-your-bash-or-zsh-shell-in-workstation-and-silverblue/)
parts of the distribution. That requires distributing fonts in a common
generic format.

##### Postscript fonts {#_postscript_fonts}

The OpenType CFF outline format is derived from the one used in
Postscript. It was designed by Adobe to permit lossless conversion of
legacy Postscript fonts. The SFNT container used by OpenType is vastly
more capable than the original PostScript format.

Therefore, there's no risk, and lots of advantages, in converting
Postscript fonts. If their upstream does not want to bother, do not
bother packaging the result.

##### X11 core fonts {#_x11_core_fonts}

Once upon a time every Linux GUI application used the so-called *Core
fonts* server-side X11 backend [^5]. It was riddled with problems. The
FLOSS developers finally gave up on it, declared it legacy and broken by
design, and moved to client-side font handling (fontconfig). Nowadays
almost no modern Linux GUI application uses the *Core fonts* backend.
Few (if any) people are willing to fix its remaining bugs.

Therefore, unless your font has previously been registered in *Core
fonts*, and the problems triggered by this font hopefully fixed, you
&#42;SHOULD NOT&#42; declare it there. This is especially true of fonts
in modern OpenType formats.

The users of this legacy backend won't thank you for destabilizing it
with new fonts. They value stability. Otherwise they'd have moved to
fontconfig like everyone else a long time ago.

### Fontconfig {#_fontconfig_3}

Free Desktop systems rely on multiple upstreams to provide their fonts.
They are heavily dependent on fontconfig to present a consistent
user-friendly font pool in applications. High quality fontconfig rules
are indispensable to permit easy substitution of font families, and to
mask upstream messiness.

Applying strict WWS rules helps applications identify all the parts of a
font family, and makes selectors like bolder possible.

Removing format attributes from &#96;family&#96; prevents breakage, when
the technical format shipped by the distribution changes after an
update. Because font technology continues to improve, format changes are
bound to happen sooner or later. Applications can still request font
format information via the fontconfig API if they need to.

Removing coverage attributes from &#96;family&#96; enables merging all
matching files in a single synthetic family. That is more user friendly,
and prevents breakage when upstream decides to split the font family
over different lines. Because creating a wide-coverage font family is a
hard, long-term endeavour --- Unicode is not finalized yet --- such
changes are common.

The other decisions are just choosing good defaults for the font family.
While fontconfig can take a guess at those, its guess will never be as
accurate as packager decisions. Packagers can ask upstream for
clarifications. Fontconfig can not.

Remember that a lot of upstream naming decisions are taken to accomodate
systems, that are missing an automatic font substition / font merging
layer. The format and coverage information in &#96;family&#96; names is
intended to help manual selection of font files. Our guidelines ask
packagers to convert those to information fontconfig understands. Free
Desktop systems can do a lot more, as long as the information provided
to fontconfig is correct.

### Source (SRPM) package break-up {#_source_srpm_package_break_up_2}

As noted in the [Packaging Guidelines](index.adoc&#35;bundling), Fedora
packages should make every effort to avoid having multiple, separate,
upstream projects bundled together in a single package. This applies
equally to font packages.

Multi-source packages are difficult to maintain and confusing to users.

### Installation (RPM) package break-up: font packages {#_installation_rpm_package_break_up_font_packages_2}

Once all the preceding has been done, a font package should only
contain:

&#42; OpenType font files, &#42; in a single OpenType format, &#42;&#42;
baring coverage constrains. &#42; with WWS-compliant &#96;style&#96;
values, &#42; sharing the same &#96;family&#96; value, &#42;&#42; except
for optical sizing atttibutes, which are appended to the common
&#96;family&#96; root. &#42; fontconfig files, &#42; appstream files,
&#42; legal files, &#42; documentation files.

### Building {#_building_2}

Building from source ensures it will be possible to modify the font when
problems are reported and upstream is not responsive. Sometimes that
means working with upstream to sanitize its build processes.

### Packaging a font family in multiple OpenType formats; application support {#_packaging_a_font_family_in_multiple_opentype_formats_application_support_2}

Fonts are comparatively bulky. Shipping fonts in multiple formats makes
the situation worse on user systems, mirrors and live images. Every font
family that ships in multiple formats, consumes space that could be used
by another font package, enhancing the user experience.

Because applications will make different choices in presence of multiple
formats for the same font family, because different formats use
different rasterization engines, because format conversions can
introduce artefacts, shipping multiple formats reduces the effectiveness
of Fedora QA.

Most applications in Fedora support indifferently all OpenType formats,

Most fonts in Fedora are only available in a single OpenType format,

Rendering text in all the locales supported by Fedora requires using
multiple fonts in multiple formats,

Therefore packaging a font family in multiple OpenType formats should
only be done as a limited exception.

# GAP Packaging Guidelines {#_gap_packaging_guidelines}

This document describes the conventions and customs surrounding the
proper packaging of [GAP](https://www.gap-system.org/) add-on packages
in Fedora. Throughout this document, we use the word *add-on* to
substitute for GAP upstream's use of the word *package*, to avoid
confusion with RPM packages.

## Naming {#_naming_11}

The main GAP package and its attendant libraries and help system are in
packages named gap, gap-libs, gap-core, gap-online-help, gap-rpm-macros,
gap-devel, gap-vim, and libgap. To distinguish add-on packages from
these core packages, add-ons MUST have names of the form gap-pkg-foo.
For example, the FGA add-on is named gap-pkg-fga.

## Add-on Location {#_add_on_location}

Architecture-independent (noarch) packages MUST be installed in
&#96;+%{gap_libdir}/pkg/%{pkgname}\\&#96;, and architecture-specific
packages in \\&#96;%{gap_archdir}/pkg/%{pkgname}\\&#96;, where
\\&#96;%{pkgname}+&#96; expands to the GAP name for the add-on.

GAP add-ons are written to be installed simply by unpacking them in an
existing GAP directory tree. For most add-ons, the only build action
necessary is building the documentation. However, since the add-on
authors assumed this would happen within the GAP tree, add-ons freely
use relative paths to access GAP files. For example, packages that use
TTH to build documentation (see below) commonly invoke
&#96;+../../../convert.pl+&#96;. The RPM spec file MUST account for
this, either by altering the add-on to point to paths under
&#96;+%{gap_libdir}+&#96;, or by creating symbolic links to create the
appearance that the build is taking place inside the GAP tree. If the
add-on is altered for the build, the spec file SHOULD arrange for the
original (unaltered) files to be installed, so that paths are correct
after installation.

GAP add-ons are frequently distributed in tarballs with a top-level
directory of the form &#96;addon-version&#96;. The add-on SHOULD be
installed without the version number. Documentation for one package
often crosslinks into documentation for other packages. If the
directories involved contain version numbers, then the crosslinks can be
broken by a package upgrade. Avoid this situation by omitting the
version numbers. GAP itself can retrieve the version number from the
add-on's &#96;+PackageInfo.g+&#96; file, so no information is lost.

## BuildRequires {#_buildrequires_7}

All add-ons MUST include &#96;+BuildRequires: gap-devel+&#96;, as that
package contains essential tools needed for compiling binary modules and
building documentation, as well as a set of RPM macros for use in spec
files. Each add-on also MUST contain a &#96;+BuildRequires+&#96; that is
dependent on the documentation style used by the GAP add-on.

### TTH {#_tth}

Add-ons that use a &#96;+buildman.pe+&#96; or &#96;+convert.pl+&#96;
script to build documentation also need &#96;+BuildRequires: tth+&#96;
in order to build HTML documentation pages from TeX input. Some add-ons
bundle these scripts, as well as a few auxiliary files. Add-ons
containing any of the following files should be modified to link to the
version of the file contained in the gap or gap-devel packages.

&#42; &#96;+gapmacro.tex+&#96; →
&#96;+%{gap_libdir}/doc/gapmacro.tex+&#96; &#42;
&#96;+gapmacrodoc.tex+&#96; →
&#96;+%{gap_libdir}/doc/gapmacrodoc.tex+&#96; &#42;
&#96;+manualbib.xml+&#96; → &#96;+%{gap_libdir}/doc/manualbib.xml+&#96;
&#42; &#96;+manualbib.xml.bib+&#96; →
&#96;+%{gap_libdir}/doc/manualbib.xml.bib+&#96; &#42;
&#96;+manualindex+&#96; → &#96;+%{gap_libdir}/doc/manualindex+&#96;
&#42; &#96;+buildman.pe+&#96; →
&#96;+%{gap_libdir}/etc/buildman.pe+&#96; &#42; &#96;+convert.pl+&#96; →
&#96;+%{gap_libdir}/etc/convert.pl+&#96;

### GAPDoc {#_gapdoc}

Add-ons that use GAPDoc to build documentation MUST include
&#96;+BuildRequires: GAPDoc-latex+&#96; to pull in the necessary LaTeX
packages. These packages do not need &#96;+Requires: GAPDoc+&#96;, since
&#96;+gap-core+&#96; depends on GAPDoc.

### Autodoc {#_autodoc}

Add-ons that use Autodoc to build documentation MUST include
&#96;+BuildRequires: gap-pkg-autodoc+&#96;. Such packages do not need to
include &#96;+BuildRequires: GAPDoc-latex+&#96;, as the Autodoc package
&#96;+Requires: GAPDoc-latex+&#96;.

## Requires, Recommends, and Suggests {#_requires_recommends_and_suggests}

All add-ons MUST include &#96;+Requires: gap-core+&#96;, either directly
or transitively. In addition, dependencies on other GAP packages, as
recorded in &#96;+PackageInfo.g+&#96;, MUST be specified, with the
exception of &#96;+GAPDoc+&#96;, as noted above. GAP has a 2-level
dependency system, specified with &#96;+NeededOtherPackages+&#96; and
&#96;+SuggestedOtherPackages+&#96; tags in &#96;+PackageInfo.g+&#96;.
How these dependencies map onto the 3-level RPM dependency system of
Requires, Recommends, and Suggests is left to the discretion of the
Fedora packager.

## Unnecessary Files {#_unnecessary_files_3}

GAP add-ons are intended to be unpacked in place within a GAP directory
tree. Ordinarily, the entire distribution directory is copied into
&#96;+%{gap_libdir}/pkg+&#96; or &#96;+%{gap_archdir}/pkg+&#96;. This
includes the documentation directories, which are consumed by the tools
contained in gap-online-help. However, some files are not needed in the
final install directory. Files that should not appear there include:

&#42; Textual descriptions of the add-on, such as a README &#42; License
files (COPYING, COPYRIGHT, LICENSE, etc.) &#42; Files for building
documentation, often called &#96;+make_doc+&#96; &#42; Files generated
by LaTeX and associated tools, including files with these suffixes:
&#42;&#42; .aux &#42;&#42; .bbl &#42;&#42; .blg &#42;&#42; .idx
&#42;&#42; .ilg &#42;&#42; .ind &#42;&#42; .log &#42;&#42; .toc

Note that License files MUST still be included in the package with the
%license tag, and other documentation such as README files can be
included as %doc.

The &#96;+%gap_copy_docs+&#96; macro is intended to make installation of
documentation files easier. For most packages, ensure that the
&#96;doc&#96; subdirectory exists in the buildroot, then invoke the
macro without arguments in &#96;+%install+&#96;. For special cases, two
optional arguments can be given:

&#42; &#96;+-d directory+&#96;: for cases where the documentation
directory is not named &#96;doc&#96;, or there are multiple
documentation directories

&#42; &#96;+-n package+&#96;: the installed add-on directory name is
assumed to be available from a macro &#96;+%pkgname+&#96;. If that is
not the case, use this macro to give the main add-on directory name.

## Documentation {#_documentation}

Since GAP documentation MUST be installed under
&#96;+%{gap_libdir}/pkg+&#96; or &#96;+%{gap_archdir}/pkg+&#96; for the
builtin documentation browser to find it, such documentation SHOULD NOT
be duplicated with &#96;+%doc+&#96;. However, the documentation SHOULD
still be marked as such so that documentation-free installs work as
expected. Most add-ons SHOULD include &#96;+%docdir+&#96; declarations
in the &#96;+%files+&#96; section of the spec file; e.g., &#96;+%docdir
%{gap_libdir}/pkg/%{pkgname}/doc+&#96; and &#96;+%docdir
%{gap_libdir}/pkg/%{pkgname}/htm+&#96;.

## Other RPM macros {#_other_rpm_macros}

Other RPM macros that may be useful for GAP add-on spec files include
the following:

&#42; &#96;+%gap_version+&#96;: the version of the main GAP package;
e.g., 4.12.0.

&#42; &#96;+%gap_archdir+&#96;: parent directory for arch-specific GAP
add-ons, currently &#96;+%{\_libdir}/gap+&#96;.

&#42; &#96;+%gap_libdir+&#96;: the root directory of the GAP
installation, currently &#96;+%{\_datadir}/gap+&#96;.

&#42; &#96;+%gap_arch+&#96;: the GAP name for the build architecture;
e.g., &#96;x86_64-redhat-linux-gnu&#96;.

# LibreOffice extension rpm guidelines {#_libreoffice_extension_rpm_guidelines}

1.  Extensions &#42;Must&#42; be installed unpacked under
    %{\_libdir}/libreoffice/share/extensions. These are termed bundled
    extensions. Extensions should not be installed as shared extensions
    i.e. via unopkg \--shared\

2.  An extension should normally just be able to Require: an appropriate
    LibreOffice component e.g. libreoffice-core, without a specific
    n-v-r as extensions use the stable UNO ABI which rarely changes, and
    then only to add extra APIs. So unless you require a specific
    feature of a LibreOffice release there is no need to require a
    specific n-v-r and force a rebuild on every n-v-r of libreoffice.\

3.  Extensions &#42;Must&#42; be named libreoffice-FOO.\

4.  Extensions are similar to e.g. xorg video drivers in that there
    exist proprietary or binary only extensions, but of course normal
    Fedora rules apply to what extensions can be packaged, i.e. see
    normal packaging licensing etc. rules. The license &#42;Must&#42; be
    acceptable, and the package &#42;Must&#42; be built from source.\

5.  Extensions can be written in any language that has an uno binding,
    e.g. C++, python, java or StarBasic. Consider the additional
    packaging guidelines of the language that the extension is written
    in if such guidelines exists.\

6.  Many extensions are actually architecture independent, but cannot be
    noarch packages due to libreoffice limitations. Such packages will
    generate empty debuginfo sub-packages. If this is the case, add
    \'%global debug_package %{nil}\' to the package.

    a.  \+ An example is&#8230;\

&#8230;. %global extname writer2latex Name: libreoffice-%{extname}
Requires: libreoffice-core

%install install -d -m 755
\$RPM_BUILD_ROOT%{\_libdir}/libreoffice/share/extensions/%{extname}
unzip -q target/lib/%{extname}.oxt -d
\$RPM_BUILD_ROOT%{\_libdir}/libreoffice/share/extensions/%{extname}
&#8230;.

# Packaging Guidelines for MinGW Cross Compilers {#_packaging_guidelines_for_mingw_cross_compilers}

## Introduction {#_introduction_6}

The Fedora MinGW project's mission is to provide an excellent
development environment for Fedora users who wish to cross-compile their
programs to run on Windows, minimizing the need to use Windows at all.
In the past developers have had to port and compile all of the libraries
and tools they have needed, and this huge effort has happened
independently many times over. We aim to eliminate duplication of work
for application developers by providing a range of libraries and
development tools which have already been ported to the MinGW
cross-compiler environment. This means that developers will not need to
recompile the application stack themselves, but can concentrate just on
the changes needed to their own application.

The targets Win32 and Win64 are supported with the MSVCRT runtime. The
target Win64 with the UCRT runtime is also supported, however, only for
the base toolchain. Builds for UCRT are not enabled for packages above
the toolchain at this time.

## Separate vs integrated MinGW source packages {#_separate_vs_integrated_mingw_source_packages}

There are two permitted ways to provide MinGW builds of software in
Fedora:

&#42; &#42;&#42;Separate source packages&#42;&#42;: There are distinct
RPM spec files for the native and MinGW builds, maintained as
independent components of Fedora. This is the traditional approach to
MinGW packaging in Fedora

&#42; &#42;&#42;Integrated source packages&#42;&#42;: There is a single
RPM spec file for the native and MinGW builds, as a single component of
Fedora. The MinGW builds are emitted as binary sub-RPMs. This is the
modern, preferred, approach to MinGW packaging in Fedora.

The traditional approach of completely separated source packages was
adopted initially because of concerns that instability in the MinGW
toolchain or Windows builds may prevent timely updates to the native
package. Experience in Fedora since then has shown that is not generally
a problem that impacts most packages, especially where Windows support
is an explicitly tested deliverable of the upstream project.

Using the separate packaging approach has a significantly higher
overhead:

&#42; The addition of MinGW support must go through the full Fedora
review process for new packages, largely duplicating review already
performed on the native package.

&#42; There is an ongoing burden for the maintainer to ensure the MinGW
source package tracks changes to the corresponding native source package
as it rebases to new releases.

&#42; There is additional work in handling patches/updates in response
to bug reports. Bug reports are often only reported against one of the
two components not both, but with security vulnerabilities there are
twice the number of bug reports created. There are then also multiple
koji builds and updates to handle.

With the integrated packaging approach there is a small extra overhead
on the native package maintainer to ensure MinGW builds keep working and
a small additional load of MinGW specific bug reports. This is usually
negligible compared to the overhead of maintaining separated packages.

With this in mind, the recommendation of the MinGW SIG is thus:

&#42; Where the same Fedora contributor intends to maintain both the
native and MinGW builds of a package, they &#42;&#42;MUST&#42;&#42; use
the integrated packaging approach.

&#42; Where the upstream project explicitly supports the Windows
platform as a build target and has automated CI, contributors
&#42;&#42;SHOULD&#42;&#42; prefer the integrated MinGW packaging
approach. Native package maintainers &#42;&#42;SHOULD&#42;&#42;
ordinarily accept addition of integrated MinGW support. If declining the
request the native maintainer should give a rationale for their
decision.

&#42; Where the upstream project does not have automated testing of
Windows builds, the MinGW package support &#42;&#42;MAY&#42;&#42; use
either packaging approach. The native maintainer may decline the request
for integrated packaging at their discretion.

&#42; Where the upstream project only supports Windows builds, the
separate packaging approach &#42;&#42;MUST&#42;&#42; be used. There will
be no corresponding native package in Fedora expected. This situation is
very rare.

&#42; When a contributor proposes a new native package to Fedora that
provides libraries that are known to support Windows, the reviewer
&#42;&#42;SHOULD&#42;&#42; inquire whether the contributor would like to
add MinGW builds at the same time. The contributor may decline this
request at their discretion.

## Adding MinGW support alongside a new native package {#_adding_mingw_support_alongside_a_new_native_package}

When a corresponding native package does not already exist, it will
always be required to go through the standard Fedora new package review
process. The proposed MinGW support &#42;&#42;MUST&#42;&#42; follow the
integrated packaging approach to provide both the MinGW and native
builds, where technically possible. As noted in the previous section, in
some rare situations there will be no corresponding native package, thus
requiring the separate pacakaging approach to be taken.

## Adding MinGW support to an existing native package {#_adding_mingw_support_to_an_existing_native_package}

When a corresponding native package is already present in Fedora, the
preference is to add MinGW support to the native source package.

Where the source package changes are simple, the contributor
&#42;&#42;SHOULD&#42;&#42;:

&#42; Make the required spec file additions in their fork of the package
&#42; Submit a koji scratch-build to prove the changes have the expected
effect &#42; Open a merge request against the native package with the
spec changes, adding a link to the koji scratch-build results as a
comment.

The existing native package maintainer thus gets clear view of the
impact of the MinGW additions to their package, to evaluate the
viability of following the integrated packaging approach.

Where there is doubt about the viability of following the integrated
package approach, a bug &#42;&#42;MAY&#42;&#42; be opened against the
package ahead of starting work to discuss the two packaging options with
the native package maintainer.

If the native maintainer declines the proposal to add MinGW support to
the existing package, the regular Fedora new package process MUST be
followed to introduce MinGW support following the separate packaging
approach.

## Track Fedora native package versions {#_track_fedora_native_package_versions}

In general terms, cross-compiled MinGW versions of packages which are
already natively available in Fedora, should follow the native Fedora
package as closely as possible. This means they should stay at the same
version, include all the same patches as the native Fedora package, and
be built with the same configuration options.

The preferred way to achieve this goal is for the MinGW support to use
the integrated packaging approach.

## Follow Fedora policy {#_follow_fedora_policy}

Cross compiled MinGW packages must follow Fedora policy, except where
noted in this document. Cross compiled packages go through the same
review process, GIT admin process etc. as other Fedora packages.

## Package naming {#_package_naming_5}

MinGW packages require special naming to denote the appropriate CPU
architecture the binaries have been built for. There should
&#42;never&#42; be a package prefixed with &#96;+mingw-\\&#96; output
during a build. The \\&#96;+mingw-&#96; prefix is exclusive for RPM spec
file names and the source RPM file name. The CPU architecture specific
packages are created by sections with &#96;+%files -n mingw32-foo+&#96;,
&#96;+%files -n mingw64-foo+&#96; or &#96;+%files -n ucrt64-foo+&#96;.

+-----------------------------------+-----------------------------------+
| &#96;+mingw-+&#96;                | Used for source package and RPM   |
|                                   | spec name (only where the         |
|                                   | separate packaging approach is    |
|                                   | chosen)                           |
+-----------------------------------+-----------------------------------+
| &#96;+mingw32-+&#96;              | Used for packages which are built |
|                                   | for Win32 with the MSVCRT runtime |
+-----------------------------------+-----------------------------------+
| &#96;+mingw64-+&#96;              | Used for packages which are built |
|                                   | for Win64 with the MSVCRT runtime |
+-----------------------------------+-----------------------------------+
| &#96;+ucrt64-+&#96;               | Used for packages which are built |
|                                   | for Win64 with the UCRT runtime   |
+-----------------------------------+-----------------------------------+

## Base packages {#_base_packages}

The base packages provide a root filesystem, base libraries, binutils
(basic programs like \'strip\', \'ld\' etc), the compiler (gcc) and the
Win32/Win64 API. Packages may need to depend on one or more of these. In
particular, almost all packages should BuildRequire
&#96;+mingw32-filesystem+&#96;, &#96;+mingw64-filesystem+&#96;,
&#96;+mingw32-gcc+&#96; and &#96;+mingw64-gcc+&#96;.

+-----------------------------------+-----------------------------------+
| &#96;+mingw32-filesystem+&#96; /  | Core filesystem directory layout, |
| &#96;+mingw64-filesystem+&#96; /  | and RPM macros for spec files.    |
| &#96;+ucrt64-filesystem+&#96;     | Equivalent to \'filesystem\' RPM  |
+-----------------------------------+-----------------------------------+
| &#96;+mingw32-binutils+&#96; /    | Cross-compiled binutils           |
| &#96;+mingw64-binutils+&#96; /    | (utilities like \'strip\',        |
| &#96;+ucrt64-binutils+&#96;       | \'as\', \'ld\') which understand  |
|                                   | Windows executables and DLLs.     |
|                                   | Equivalent to \'binutils\' RPM    |
+-----------------------------------+-----------------------------------+
| &#96;+mingw32-gcc+&#96; /         | GNU compiler collection.          |
| &#96;+mingw64-gcc+&#96; /         | Compilers for C and C++ which     |
| &#96;+ucrt64-gcc+&#96;            | cross-compile to a Windows        |
|                                   | target. Equivalent to gcc RPM     |
+-----------------------------------+-----------------------------------+
| &#96;+mingw32-crt+&#96; /         | Base libraries for core MinGW     |
| &#96;+mingw64-crt+&#96; /         | runtime &amp; development         |
| &#96;+ucrt64-crt+&#96;            | environment. Equivalent to        |
|                                   | \'glibc\' RPM                     |
+-----------------------------------+-----------------------------------+
| &#96;+mingw32-headers+&#96; /     | Win32 and Win64 API. A free       |
| &#96;+mingw64-headers+&#96; /     | (public domain) reimplementation  |
| &#96;+ucrt64-headers+&#96;        | of the header files required to   |
|                                   | link to the Win32 and Win64 API.  |
|                                   | No direct equivalent in base      |
|                                   | Fedora - glibc-devel is closest   |
+-----------------------------------+-----------------------------------+

## Build for multiple targets {#_build_for_multiple_targets}

The goal of the MinGW framework is to provide an easy way for package
maintainers to build their packages for multiple targets using one .spec
file. To aid developers in this several RPM macros have been developed
which are part of the mingw-filesystem package. These RPM macros will be
explained later on in these guidelines.

By default MinGW support will be built for both the Win32 and Win64
targets with the MSVCRT runtime. Building of the Win64 target with the
UCRT64 runtime is not yet enabled by default.

When a package can only be built for a subset of these targets this can
be indicated by setting one or more of these:

+-----------------------------------+-----------------------------------+
| &#96;+%global mingw_build_win32   | Don't build for the Win32 target  |
| 0+&#96;                           | with the MSVCRT runtime           |
+-----------------------------------+-----------------------------------+
| &#96;+%global mingw_build_win64   | Don't build for the Win64 target  |
| 0+&#96;                           | with the MSVCRT runtime           |
+-----------------------------------+-----------------------------------+
| &#96;+%global mingw_build_ucrt64  | Don't build for the Win64 target  |
| 0+&#96;                           | with the UCRT runtime             |
+-----------------------------------+-----------------------------------+

## One source RPM, separate binary RPMs per-target {#_one_source_rpm_separate_binary_rpms_per_target}

Each cross compiled MinGW package which builds binaries for a specific
target should put the binaries for that target in a separate subpackage.
So if a package &#96;+mingw-foo+&#96; or &#96;+foo+&#96; builds binaries
for the Win32 and Win64 targets with the MSVCRT runtime, then the source
RPM should provide two subpackages named &#96;+mingw32-foo+&#96; and
&#96;+mingw64-foo+&#96;. If a package builds for the UCRT runtime, it
will also have a &#96;+ucrt64-foo+&#96; subpackage.

This means that a spec file must contains %package and %files sections
for all the targets.

When using the separate packaging approach, packages containing
translations must use &#96;+%mingw_find_lang+&#96; instead of
&#96;+%find_lang+&#96;.

When using the integrated packaging approach, packages containing
translations must use &#96;+%find_lang&#96; followed by
&#96;+%mingw_find_lang+&#96;.

This causes all translation filelists to be split in per-target
filelists. For example: when a spec file contains something like this:

``` _rpm-spec
%install
\&lt;snip\&gt;
%mingw_find_lang foo
```

then one file per mingw target will get created named
&#96;+mingw32-foo.lang+&#96;, &#96;+mingw64-foo.lang+&#96;, and
&#96;+ucrt64-foo.lang+&#96;. These file lists can be included in the
%files section for the targets:

``` _rpm-spec
%files -n mingw32-foo -f mingw32-foo.lang
\&lt;snip\&gt;
%files -n mingw64-foo -f mingw64-foo.lang
\&lt;snip\&gt;
%files -n ucrt64-foo -f ucrt64-foo.lang
```

## Filesystem layout {#_filesystem_layout}

Integration into the main root filesystem layout is as follows:

&#8230;.

\| - etc \| \| \| +- rpm \| \| \| +- macros.mingw \| +- macros.mingw32
\| +- macros.mingw64 \| +- usr \| +- bin - Links to MinGW cross compiler
toolchain \| \| \| +- i686-w64-mingw32-cpp \| +- i686-w64-mingw32-gcc \|
+- i686-w64-mingw32-g \| +- x86_64-w64-mingw32-cpp \| +-
x86_64-w64-mingw32-gcc \| +- x86_64-w64-mingw32-g \| +-
x86_64-w64-mingw32ucrt-cpp \| +- x86_64-w64-mingw32ucrt-gcc \| +-
x86_64-w64-mingw32ucrt-g+ \| - \\&#8230; etc.. \| +- lib \| \| \| +- rpm
\| \| \| +- mingw-find-debuginfo.sh - extract debug information from
Win32 and Win64 binaries \| +- mingw-find-lang.sh - generates per-target
file lists containing translations \| +- mingw-find-provides.sh - extra
DLL names \| +- mingw-find-requires.sh - discover required DLL names \|
+- i686-w64-mingw32 - root of mingw toolchain and binaries for the Win32
target with MSVCRT runtime - see next diagram +- x86_64-w64-mingw32 -
root of mingw toolchain and binaries for the Win64 target with MSVCRT
runtime - see next diagram&#96; - x86_64-w64-mingw32urt - root of mingw
toolchain and binaries for the Win64 target with UCRT runtime - see next
diagram&#96; &#8230;.

The bulk of the packaged content is located under the respective MinGW
root, one of &#96;+/usr/i686-w64-mingw32+&#96;,
&#96;+/usr/x86_64-w64-mingw32+&#96; and
&#96;+/usr/x86_64-w64-mingw32ucrt+&#96;:

&#8230;.

\| +- bin - Binutils toolchain binaries for the target \| \| \| +- ar \|
+- as \| +- dlltool \| +- ld \| +- &#8230; etc &#8230; \| +- lib -
Binutils toolchain support libraries / files for the target \| +-
sys-root - root for cross compiled MinGW binaries \| +- mingw \| +-
bin - cross-compiled MinGW binaries &amp; runtime DLL parts +- etc -
configuration files +- include - include files for cross compiled MinGW
libs +- lib - cross-compiled static MinGW libraries &amp; linktime DLL
parts \| \| \| +- pkgconfig - pkg-config definitions for libraries \| +-
share \| +- man &#8230;.

## Filenames of the cross-compilers and binutils {#_filenames_of_the_cross_compilers_and_binutils}

The MinGW cross-compilers and binutils are Fedora binaries and are
therefore placed in &#96;+%{\_bindir}\\&#96; (i.e.,
\\&#96;/usr/bin+&#96;) according to the FHS and Fedora guidelines.

The MinGW cross-compilers and binutils which generate i686 binaries for
Windows with the MSVCRT runtime are named:

``` _rpm-spec
%{_bindir}/i686-w64-mingw32-gcc
%{_bindir}/i686-w64-mingw32-g++
%{_bindir}/i686-w64-mingw32-ld
%{_bindir}/i686-w64-mingw32-as
%{_bindir}/i686-w64-mingw32-strip
etc.
```

The same binaries are present in
&#96;+%{\_prefix}/i686-w64-mingw32/bin+&#96; without any prefix in the
name, i.e.,

``` _rpm-spec
%{_prefix}/i686-w64-mingw32/bin/gcc
%{_prefix}/i686-w64-mingw32/bin/g++
%{_prefix}/i686-w64-mingw32/bin/ld
%{_prefix}/i686-w64-mingw32/bin/as
%{_prefix}/i686-w64-mingw32/bin/strip
etc.
```

The same also applies for the x86_64 target with both MSVCRT and UCRT
runtimes. The target with MSVCRT uses \'x86_64-w64-mingw32\' as prefix
instead of \'i686-w64-mingw32\', while UCRT uses
\'x86_64-w64-mingw32ucrt\'.

## Naming of the root filesystem {#_naming_of_the_root_filesystem}

The root filesystem contains Windows executables and DLLs and any other
Windows-only files. It is necessary both because we need to store
Windows libraries in order to link further libraries which depend on
them, and also because MinGW requires a root filesystem location.

The location for Win32 target with MSVCRT runtime is provided by the
macro:

``` _rpm-spec
%{mingw32_sysroot}   %{_prefix}/i686-w64-mingw32/sys-root
```

The Win64 target with MSVCRT runtime is provided by the macro:

``` _rpm-spec
%{mingw64_sysroot}   %{_prefix}/x86_64-w64-mingw32/sys-root
```

The Win64 target with UCRT runtime is provided by the macro:

``` _rpm-spec
%{ucrt64_sysroot}   %{_prefix}/x86_64-w64-mingw32ucrt/sys-root
```

## Standard mingw RPM macros {#_standard_mingw_rpm_macros}

The &#96;+mingw-filesystem+&#96; package provides a number of
convenience macros for the cross compiled sysroot directories, and
toolchain. It is mandatory to use these macros in all MinGW cross
compiled packages submitted to Fedora.

### Toolchain macros {#_toolchain_macros}

The following macros are for the %build and %install section of the spec

Generic macros:

+----------------------+----------------------+-----------------------+
| Macro                | Available in         | Explanation           |
|                      | mingw-filesystem     |                       |
+----------------------+----------------------+-----------------------+
| mingw_cmake          | &gt;= 95             | Call the \'cmake\'    |
|                      |                      | binary for all the    |
|                      |                      | configured targets    |
+----------------------+----------------------+-----------------------+
| mingw_cmake_kde4     | &gt;= 95             | Call the \'cmake\'    |
|                      |                      | binary for all the    |
|                      |                      | configured targets    |
|                      |                      | with KDE4 specific    |
|                      |                      | parameters set        |
+----------------------+----------------------+-----------------------+
| mingw_configure      | &gt;= 95             | Call the configure    |
|                      |                      | command for all the   |
|                      |                      | configured targets    |
+----------------------+----------------------+-----------------------+
| mingw_make           | &gt;= 95             | Call the \'make\'     |
|                      |                      | command for all the   |
|                      |                      | configured targets    |
+----------------------+----------------------+-----------------------+
| mingw_make_build     | &gt;= 113            | Call \'make -O        |
|                      |                      | -j&lt;nprocs&gt; V=1  |
|                      |                      | VERBOSE=1\' command   |
|                      |                      | for all configured    |
|                      |                      | targets               |
+----------------------+----------------------+-----------------------+
| mingw_make_install   | &gt;= 113            | Call \'make install   |
|                      |                      | DES                   |
|                      |                      | TDIR=\$RPM_BUILD_ROOT |
|                      |                      | \'INS                 |
|                      |                      | TALL=/usr/bin/install |
|                      |                      | -p\' for all          |
|                      |                      | configured targets    |
+----------------------+----------------------+-----------------------+
| mingw_meson          | &gt;= 104            | Call the meson binary |
|                      |                      | for all the           |
|                      |                      | configured targets    |
+----------------------+----------------------+-----------------------+
| mingw_ninja          | &gt;= 104            | Call the ninja binary |
|                      |                      | for all the           |
|                      |                      | configured targets    |
+----------------------+----------------------+-----------------------+
| mingw_objcopy        | &gt;= 95             | cross compiler        |
|                      |                      | \'objcopy\' binary    |
|                      |                      | (which supports both  |
|                      |                      | Win32 and Win64       |
|                      |                      | binaries)             |
+----------------------+----------------------+-----------------------+
| mingw_objdump        | &gt;= 95             | cross compiler        |
|                      |                      | \'objdump\' binary    |
|                      |                      | (which supports both  |
|                      |                      | Win32 and Win64       |
|                      |                      | binaries)             |
+----------------------+----------------------+-----------------------+
| mingw_qmake_qt4      | &gt;= 95             | Call the Qt4 qmake    |
|                      |                      | binary for all        |
|                      |                      | configured targets    |
|                      |                      | (requires             |
|                      |                      | mingw32-qt-qmake      |
|                      |                      | and/or                |
|                      |                      | mingw64-qt-qmake to   |
|                      |                      | be installed)         |
+----------------------+----------------------+-----------------------+
| mingw_qmake_qt5      | &gt;= 96             | Call the Qt5 qmake    |
|                      |                      | binary for all        |
|                      |                      | configured targets    |
|                      |                      | (requires             |
|                      |                      | mingw32-qt5-qmake     |
|                      |                      | and/or                |
|                      |                      | mingw64-qt5-qmake to  |
|                      |                      | be installed)         |
+----------------------+----------------------+-----------------------+
| mingw_strip          | &gt;= 95             | cross compiler        |
|                      |                      | \'strip\' binary      |
|                      |                      | (which supports both  |
|                      |                      | Win32 and Win64       |
|                      |                      | binaries)             |
+----------------------+----------------------+-----------------------+

Win32 with MSVCRT runtime specific macros:

+-----------------+-----------------+-----------------+-----------------+
| Macro           | Available in    | Value           | Explanation     |
|                 | min             |                 |                 |
|                 | gw32-filesystem |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| mingw32_ar      | &gt;= 95        | i686            | cross compiler  |
|                 |                 | -w64-mingw32-ar | \'ar\' binary   |
+-----------------+-----------------+-----------------+-----------------+
| mingw32_cc      | &gt;= 95        | i686-           | cross compiler  |
|                 |                 | w64-mingw32-gcc | \'gcc\' binary  |
+-----------------+-----------------+-----------------+-----------------+
| mingw32_cflags  | &gt;= 95        | -O2 -g -pipe    | Default         |
|                 |                 | -Wall           | compiler flags  |
|                 |                 | -Wp,-D_F        | for C/C++       |
|                 |                 | ORTIFY_SOURCE=2 | binaries        |
|                 |                 | -fexceptions    |                 |
|                 |                 | \--param=ss     |                 |
|                 |                 | p-buffer-size=4 |                 |
+-----------------+-----------------+-----------------+-----------------+
| mingw32_cmake   | &gt;= 95        |                 | Call the        |
|                 |                 |                 | \'cmake\'       |
|                 |                 |                 | binary for the  |
|                 |                 |                 | Win32 target    |
+-----------------+-----------------+-----------------+-----------------+
| mi              | &gt;= 95        |                 | standard        |
| ngw32_configure |                 |                 | invocation for  |
|                 |                 |                 | autotools       |
|                 |                 |                 | \'configure\'   |
|                 |                 |                 | scripts         |
+-----------------+-----------------+-----------------+-----------------+
| mingw32_cpp     | &gt;= 95        | i686-           | cross compiler  |
|                 |                 | w64-mingw32-gcc | \'cpp\' binary  |
|                 |                 | -E              |                 |
+-----------------+-----------------+-----------------+-----------------+
| mingw32_env     | &gt;= 95        |                 | Set the correct |
|                 |                 |                 | environment     |
|                 |                 |                 | variables for   |
|                 |                 |                 | the Win32       |
|                 |                 |                 | target          |
+-----------------+-----------------+-----------------+-----------------+
| mingw32_host    | &gt;= 95        | i               | Host platform   |
|                 |                 | 686-w64-mingw32 | for build       |
+-----------------+-----------------+-----------------+-----------------+
| mingw32_meson   | &gt;= 104       |                 | Call the meson  |
|                 |                 |                 | binary for the  |
|                 |                 |                 | Win32 target    |
+-----------------+-----------------+-----------------+-----------------+
| mingw32_ninja   | &gt;= 104       |                 | Call the ninja  |
|                 |                 |                 | binary for the  |
|                 |                 |                 | Win32 target    |
+-----------------+-----------------+-----------------+-----------------+
| mingw32_objcopy | &gt;= 95        | i686-w64-       | cross compiler  |
|                 |                 | mingw32-objcopy | \'objcopy\'     |
|                 |                 |                 | binary          |
+-----------------+-----------------+-----------------+-----------------+
| mingw32_objdump | &gt;= 95        | i686-w64-       | cross compiler  |
|                 |                 | mingw32-objdump | \'objdump\'     |
|                 |                 |                 | binary          |
+-----------------+-----------------+-----------------+-----------------+
| min             | &gt;= 95        | i686-w64-min    | Call the        |
| gw32_pkg_config |                 | gw32-pkg-config | pkg-config      |
|                 |                 |                 | command for the |
|                 |                 |                 | Win32 target    |
+-----------------+-----------------+-----------------+-----------------+
| mi              | &gt;= 95        | mi              | Call the Qt4    |
| ngw32_qmake_qt4 |                 | ngw32-qmake-qt4 | qmake command   |
|                 |                 |                 | for the Win32   |
|                 |                 |                 | target          |
+-----------------+-----------------+-----------------+-----------------+
| mi              | &gt;= 96        | mi              | Call the Qt5    |
| ngw32_qmake_qt5 |                 | ngw32-qmake-qt5 | qmake command   |
|                 |                 |                 | for the Win32   |
|                 |                 |                 | target          |
+-----------------+-----------------+-----------------+-----------------+
| mingw32_ranlib  | &gt;= 95        | i686-w64        | cross compiler  |
|                 |                 | -mingw32-ranlib | \'ranlib\'      |
|                 |                 |                 | binary          |
+-----------------+-----------------+-----------------+-----------------+
| mingw32_strip   | &gt;= 95        | i686-w6         | cross compiler  |
|                 |                 | 4-mingw32-strip | \'strip\'       |
|                 |                 |                 | binary          |
+-----------------+-----------------+-----------------+-----------------+
| mingw32_target  | &gt;= 95        | i               | Target platform |
|                 |                 | 686-w64-mingw32 | for build       |
+-----------------+-----------------+-----------------+-----------------+

Win64 with MSVCRT runtime specific macros:

+-----------------+-----------------+-----------------+-----------------+
| Macro           | Available in    | Value           | Explanation     |
|                 | min             |                 |                 |
|                 | gw64-filesystem |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| mingw64_ar      | &gt;= 95        | x86_64          | cross compiler  |
|                 |                 | -w64-mingw32-ar | \'ar\' binary   |
+-----------------+-----------------+-----------------+-----------------+
| mingw64_cc      | &gt;= 95        | x86_64-         | cross compiler  |
|                 |                 | w64-mingw32-gcc | \'gcc\' binary  |
+-----------------+-----------------+-----------------+-----------------+
| mingw64_cflags  | &gt;= 95        | -O2 -g -pipe    | Default         |
|                 |                 | -Wall           | compiler flags  |
|                 |                 | -Wp,-D_F        | for C/C++       |
|                 |                 | ORTIFY_SOURCE=2 | binaries        |
|                 |                 | -fexceptions    |                 |
|                 |                 | \--param=ss     |                 |
|                 |                 | p-buffer-size=4 |                 |
+-----------------+-----------------+-----------------+-----------------+
| mingw64_cmake   | &gt;= 95        |                 | Call the        |
|                 |                 |                 | \'cmake\'       |
|                 |                 |                 | binary for the  |
|                 |                 |                 | Win64 target    |
+-----------------+-----------------+-----------------+-----------------+
| mi              | &gt;= 95        |                 | standard        |
| ngw64_configure |                 |                 | invocation for  |
|                 |                 |                 | autotools       |
|                 |                 |                 | \'configure\'   |
|                 |                 |                 | scripts         |
+-----------------+-----------------+-----------------+-----------------+
| mingw64_cpp     | &gt;= 95        | x86_64-         | cross compiler  |
|                 |                 | w64-mingw32-gcc | \'cpp\' binary  |
|                 |                 | -E              |                 |
+-----------------+-----------------+-----------------+-----------------+
| mingw64_env     | &gt;= 95        |                 | Set the correct |
|                 |                 |                 | environment     |
|                 |                 |                 | variables for   |
|                 |                 |                 | the Win64       |
|                 |                 |                 | target          |
+-----------------+-----------------+-----------------+-----------------+
| mingw64_host    | &gt;= 95        | x86             | Host platform   |
|                 |                 | _64-w64-mingw32 | for build       |
+-----------------+-----------------+-----------------+-----------------+
| mingw64_meson   | &gt;= 104       |                 | Call the meson  |
|                 |                 |                 | binary for the  |
|                 |                 |                 | Win64 target    |
+-----------------+-----------------+-----------------+-----------------+
| mingw64_ninja   | &gt;= 104       |                 | Call the ninja  |
|                 |                 |                 | binary for the  |
|                 |                 |                 | Win64 target    |
+-----------------+-----------------+-----------------+-----------------+
| mingw64_objcopy | &gt;= 95        | x86_64-w64-     | cross compiler  |
|                 |                 | mingw32-objcopy | \'objcopy\'     |
|                 |                 |                 | binary          |
+-----------------+-----------------+-----------------+-----------------+
| mingw64_objdump | &gt;= 95        | x86_64-w64-     | cross compiler  |
|                 |                 | mingw32-objdump | \'objdump\'     |
|                 |                 |                 | binary          |
+-----------------+-----------------+-----------------+-----------------+
| min             | &gt;= 95        | x86_64-w64-min  | Call the        |
| gw64_pkg_config |                 | gw32-pkg-config | pkg-config      |
|                 |                 |                 | command for the |
|                 |                 |                 | Win64 target    |
+-----------------+-----------------+-----------------+-----------------+
| mi              | &gt;= 95        | mi              | Call the Qt4    |
| ngw64_qmake_qt4 |                 | ngw64-qmake-qt4 | qmake command   |
|                 |                 |                 | for the Win64   |
|                 |                 |                 | target          |
+-----------------+-----------------+-----------------+-----------------+
| mi              | &gt;= 96        | mi              | Call the Qt5    |
| ngw64_qmake_qt5 |                 | ngw64-qmake-qt5 | qmake command   |
|                 |                 |                 | for the Win64   |
|                 |                 |                 | target          |
+-----------------+-----------------+-----------------+-----------------+
| mingw64_ranlib  | &gt;= 95        | x86_64-w64      | cross compiler  |
|                 |                 | -mingw32-ranlib | \'ranlib\'      |
|                 |                 |                 | binary          |
+-----------------+-----------------+-----------------+-----------------+
| mingw64_strip   | &gt;= 95        | x86_64-w6       | cross compiler  |
|                 |                 | 4-mingw32-strip | \'strip\'       |
|                 |                 |                 | binary          |
+-----------------+-----------------+-----------------+-----------------+
| mingw64_target  | &gt;= 95        | x86             | Target platform |
|                 |                 | _64-w64-mingw32 | for build       |
+-----------------+-----------------+-----------------+-----------------+

Win64 with UCRT runtime specific macros:

+-----------------+-----------------+-----------------+-----------------+
| Macro           | Available in    | Value           | Explanation     |
|                 | uc              |                 |                 |
|                 | rt64-filesystem |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
| ucrt64_ar       | &gt;= 133       | x86_64-w64      | cross compiler  |
|                 |                 | -mingw32ucrt-ar | \'ar\' binary   |
+-----------------+-----------------+-----------------+-----------------+
| ucrt64_cc       | &gt;= 133       | x86_64-w64-     | cross compiler  |
|                 |                 | mingw32ucrt-gcc | \'gcc\' binary  |
+-----------------+-----------------+-----------------+-----------------+
| ucrt64_cflags   | &gt;= 133       | -O2 -g -pipe    | Default         |
|                 |                 | -Wall           | compiler flags  |
|                 |                 | -Wp,-D_F        | for C/C++       |
|                 |                 | ORTIFY_SOURCE=2 | binaries        |
|                 |                 | -fexceptions    |                 |
|                 |                 | \--param=ss     |                 |
|                 |                 | p-buffer-size=4 |                 |
+-----------------+-----------------+-----------------+-----------------+
| ucrt64_cmake    | &gt;= 133       |                 | Call the        |
|                 |                 |                 | \'cmake\'       |
|                 |                 |                 | binary for the  |
|                 |                 |                 | Win64 target    |
+-----------------+-----------------+-----------------+-----------------+
| u               | &gt;= 133       |                 | standard        |
| crt64_configure |                 |                 | invocation for  |
|                 |                 |                 | autotools       |
|                 |                 |                 | \'configure\'   |
|                 |                 |                 | scripts         |
+-----------------+-----------------+-----------------+-----------------+
| ucrt64_cpp      | &gt;= 133       | x86_64-w64-     | cross compiler  |
|                 |                 | mingw32ucrt-gcc | \'cpp\' binary  |
|                 |                 | -E              |                 |
+-----------------+-----------------+-----------------+-----------------+
| ucrt64_env      | &gt;= 133       |                 | Set the correct |
|                 |                 |                 | environment     |
|                 |                 |                 | variables for   |
|                 |                 |                 | the Win64       |
|                 |                 |                 | target          |
+-----------------+-----------------+-----------------+-----------------+
| ucrt64_host     | &gt;= 133       | x86             | Host platform   |
|                 |                 | _64-w64-mingw32 | for build       |
+-----------------+-----------------+-----------------+-----------------+
| ucrt64_meson    | &gt;= 104       |                 | Call the meson  |
|                 |                 |                 | binary for the  |
|                 |                 |                 | Win64 target    |
+-----------------+-----------------+-----------------+-----------------+
| ucrt64_ninja    | &gt;= 104       |                 | Call the ninja  |
|                 |                 |                 | binary for the  |
|                 |                 |                 | Win64 target    |
+-----------------+-----------------+-----------------+-----------------+
| ucrt64_objcopy  | &gt;= 133       | x86_64-w64-ming | cross compiler  |
|                 |                 | w32ucrt-objcopy | \'objcopy\'     |
|                 |                 |                 | binary          |
+-----------------+-----------------+-----------------+-----------------+
| ucrt64_objdump  | &gt;= 133       | x86_64-w64-ming | cross compiler  |
|                 |                 | w32ucrt-objdump | \'objdump\'     |
|                 |                 |                 | binary          |
+-----------------+-----------------+-----------------+-----------------+
| uc              | &gt;= 133       | x86             | Call the        |
| rt64_pkg_config |                 | _64-w64-mingw32 | pkg-config      |
|                 |                 | ucrt-pkg-config | command for the |
|                 |                 |                 | Win64 target    |
+-----------------+-----------------+-----------------+-----------------+
| u               | &gt;= 133       | u               | Call the Qt4    |
| crt64_qmake_qt4 |                 | crt64-qmake-qt4 | qmake command   |
|                 |                 |                 | for the Win64   |
|                 |                 |                 | target          |
+-----------------+-----------------+-----------------+-----------------+
| u               | &gt;= 133       | u               | Call the Qt5    |
| crt64_qmake_qt5 |                 | crt64-qmake-qt5 | qmake command   |
|                 |                 |                 | for the Win64   |
|                 |                 |                 | target          |
+-----------------+-----------------+-----------------+-----------------+
| ucrt64_ranlib   | &gt;= 133       | x86_64-w64-min  | cross compiler  |
|                 |                 | gw32ucrt-ranlib | \'ranlib\'      |
|                 |                 |                 | binary          |
+-----------------+-----------------+-----------------+-----------------+
| ucrt64_strip    | &gt;= 133       | x86_64-w64-mi   | cross compiler  |
|                 |                 | ngw32ucrt-strip | \'strip\'       |
|                 |                 |                 | binary          |
+-----------------+-----------------+-----------------+-----------------+
| ucrt64_target   | &gt;= 133       | x86             | Target platform |
|                 |                 | _64-w64-mingw32 | for build       |
+-----------------+-----------------+-----------------+-----------------+

### Filesystem location macros {#_filesystem_location_macros}

The following macros are for use in %build, %install and %files sections
of the RPM spec

For the Win32 with MSVCRT runtime target:

+----------------------+----------------------+-----------------------+
| mingw32_bindir       | %                    | Location of Windows   |
|                      | {mingw32_prefix}/bin | executables.          |
+----------------------+----------------------+-----------------------+
| mingw32_datadir      | %{m                  | Shared data used      |
|                      | ingw32_prefix}/share | under Windows.        |
+----------------------+----------------------+-----------------------+
| mingw32_docdir       | %{mingw              | Documentation.        |
|                      | 32_prefix}/share/doc |                       |
+----------------------+----------------------+-----------------------+
| mingw32_infodir      | %{mingw3             | Info files (see note  |
|                      | 2_prefix}/share/info | below).               |
+----------------------+----------------------+-----------------------+
| mingw32_includedir   | %{min                | Header files used     |
|                      | gw32_prefix}/include | when cross-compiling  |
|                      |                      | for Windows.          |
+----------------------+----------------------+-----------------------+
| mingw32_libdir       | %                    | Windows libraries     |
|                      | {mingw32_prefix}/lib | (see sections below). |
+----------------------+----------------------+-----------------------+
| mingw32_libexecdir   | %{min                |                       |
|                      | gw32_prefix}/libexec |                       |
+----------------------+----------------------+-----------------------+
| mingw32_mandir       | %{mingw              | Man pages (see note   |
|                      | 32_prefix}/share/man | below).               |
+----------------------+----------------------+-----------------------+
| mingw32_prefix       | %{mi                 | Windows equivalent of |
|                      | ngw32_sysroot}/mingw | %{\_prefix}, required |
|                      |                      | by MinGW.             |
+----------------------+----------------------+-----------------------+
| mingw32_sbindir      | %{                   |                       |
|                      | mingw32_prefix}/sbin |                       |
+----------------------+----------------------+-----------------------+
| mingw32_sysconfdir   | %                    | Configuration files   |
|                      | {mingw32_prefix}/etc | used when running     |
|                      |                      | under Windows.        |
+----------------------+----------------------+-----------------------+
| mingw32_sysroot      | %{\_prefix}/i686-    | Windows system root.  |
|                      | w64-mingw32/sys-root |                       |
+----------------------+----------------------+-----------------------+

For the Win64 with MSVCRT runtime target:

+----------------------+----------------------+-----------------------+
| mingw64_bindir       | %                    | Location of Windows   |
|                      | {mingw64_prefix}/bin | executables.          |
+----------------------+----------------------+-----------------------+
| mingw64_datadir      | %{m                  | Shared data used      |
|                      | ingw64_prefix}/share | under Windows.        |
+----------------------+----------------------+-----------------------+
| mingw64_docdir       | %{mingw              | Documentation.        |
|                      | 64_prefix}/share/doc |                       |
+----------------------+----------------------+-----------------------+
| mingw64_infodir      | %{mingw6             | Info files (see note  |
|                      | 4_prefix}/share/info | below).               |
+----------------------+----------------------+-----------------------+
| mingw64_includedir   | %{min                | Header files used     |
|                      | gw64_prefix}/include | when cross-compiling  |
|                      |                      | for Windows.          |
+----------------------+----------------------+-----------------------+
| mingw64_libdir       | %                    | Windows libraries     |
|                      | {mingw64_prefix}/lib | (see sections below). |
+----------------------+----------------------+-----------------------+
| mingw64_libexecdir   | %{min                |                       |
|                      | gw64_prefix}/libexec |                       |
+----------------------+----------------------+-----------------------+
| mingw64_mandir       | %{mingw              | Man pages (see note   |
|                      | 64_prefix}/share/man | below).               |
+----------------------+----------------------+-----------------------+
| mingw64_prefix       | %{mi                 | Windows equivalent of |
|                      | ngw64_sysroot}/mingw | %{\_prefix}, required |
|                      |                      | by MinGW.             |
+----------------------+----------------------+-----------------------+
| mingw64_sbindir      | %{                   |                       |
|                      | mingw64_prefix}/sbin |                       |
+----------------------+----------------------+-----------------------+
| mingw64_sysconfdir   | %                    | Configuration files   |
|                      | {mingw64_prefix}/etc | used when running     |
|                      |                      | under Windows.        |
+----------------------+----------------------+-----------------------+
| mingw64_sysroot      | %{\_prefix}/x86_64-  | Windows system root.  |
|                      | w64-mingw32/sys-root |                       |
+----------------------+----------------------+-----------------------+

For the Win64 with UCRT runtime target:

+----------------------+----------------------+-----------------------+
| ucrt64_bindir        | %{ucrt64_prefix}/bin | Location of Windows   |
|                      |                      | executables.          |
+----------------------+----------------------+-----------------------+
| ucrt64_datadir       | %{                   | Shared data used      |
|                      | ucrt64_prefix}/share | under Windows.        |
+----------------------+----------------------+-----------------------+
| ucrt64_docdir        | %{ucrt               | Documentation.        |
|                      | 64_prefix}/share/doc |                       |
+----------------------+----------------------+-----------------------+
| ucrt64_infodir       | %{ucrt6              | Info files (see note  |
|                      | 4_prefix}/share/info | below).               |
+----------------------+----------------------+-----------------------+
| ucrt64_includedir    | %{uc                 | Header files used     |
|                      | rt64_prefix}/include | when cross-compiling  |
|                      |                      | for Windows.          |
+----------------------+----------------------+-----------------------+
| ucrt64_libdir        | %{ucrt64_prefix}/lib | Windows libraries     |
|                      |                      | (see sections below). |
+----------------------+----------------------+-----------------------+
| ucrt64_libexecdir    | %{uc                 |                       |
|                      | rt64_prefix}/libexec |                       |
+----------------------+----------------------+-----------------------+
| ucrt64_mandir        | %{ucrt               | Man pages (see note   |
|                      | 64_prefix}/share/man | below).               |
+----------------------+----------------------+-----------------------+
| ucrt64_prefix        | %{u                  | Windows equivalent of |
|                      | crt64_sysroot}/mingw | %{\_prefix}, required |
|                      |                      | by MinGW.             |
+----------------------+----------------------+-----------------------+
| ucrt64_sbindir       | %                    |                       |
|                      | {ucrt64_prefix}/sbin |                       |
+----------------------+----------------------+-----------------------+
| ucrt64_sysconfdir    | %{ucrt64_prefix}/etc | Configuration files   |
|                      |                      | used when running     |
|                      |                      | under Windows.        |
+----------------------+----------------------+-----------------------+
| ucrt64_sysroot       | %{\                  | Windows system root.  |
|                      | _prefix}/x86_64-w64- |                       |
|                      | mingw32ucrt/sys-root |                       |
+----------------------+----------------------+-----------------------+

## Compilation of binaries {#_compilation_of_binaries}

In order to build binaries for multiple targets we have to call commands
like &#96;+./configure+&#96; and &#96;+make+&#96; multiple times (once
for each target). If one has to write this all out in a spec file then
it will lead to duplicate code. To reduce the amount of duplication,
several RPM macros have been introduced to help with the compilation.
These macros are &#96;+%mingw_configure+&#96;, &#96;+%mingw_cmake+&#96;,
&#96;+%mingw_cmake_kde4+&#96;, &#96;+%mingw_qmake_qt4+&#96;,
&#96;+%mingw_qmake_qt5+&#96; and &#96;+%mingw_make+&#96;

These macros use out of source compilation to build binaries for all the
targets. Almost all packages support out of source compilation or
require slight patching. The only known exceptions to date are zlib and
openssl. Packages which don't support out of source compilation may
require a different approach like performing everything in the %install
phase. If you happen to stumble across a package which requires a
different approach feel free to contact us on the Fedora MinGW mailing
list

Some packages need to be built multiple times for each target. Examples
of this are packages which have to be built once for a static version
and once for a shared version. Such packages can add a custom suffix to
the build directory used. Say you've got something like below:

``` _rpm-spec
mkdir build_shared
pushd build_shared
%{mingw32_configure} --enable-shared
popd
mkdir build_static
pushd build_static
%{mingw32_configure} --enable-static
popd
```

This can be rewritten to something like this:

``` _rpm-spec
MINGW_BUILDDIR_SUFFIX=shared %mingw_configure --enable-shared
MINGW_BUILDDIR_SUFFIX=static %mingw_configure --enable-static
```

Most packages used the command &#96;+make %{?\_smp_mflags}\\&#96; to
build the package. In the MinGW cross compiler framework you have to use
\\&#96;%mingw_make %{?\_smp_mflags}\\&#96; to build the package for all
configured targets. As with the \\&#96;%mingw_configure+&#96; macro you
can also use the MINGW_BUILDDIR_SUFFIX environment variable to indicate
a custom suffix to the build directory used

To install the package the command &#96;+make install
DESTDIR=\$RPM_BUILD_ROOT+&#96; was used in almost all cases. This can be
rewritten to &#96;+%mingw_make install DESTDIR=\$RPM_BUILD_ROOT+&#96; to
install the package for all configured targets. The environment variable
MINGW_BUILDDIR_SUFFIX can also be used here.

Some packages require some custom instructions before the files are
ready to be packaged. Such code can remain as is. However, you may need
to duplicate these instructions multiple times (for all configured
targets).

## Dependencies {#_dependencies_7}

If a package contains binaries which depend on a DLL provided by another
package, these dependencies should be expressed in the form:

&#8230;. mingw32(foo.dll) &#8230;.

where &#96;+foo.dll+&#96; is the name of the DLL. The name must be
converted to lowercase because Windows binaries contain case insensitive
dependencies. The form \'mingw32(foo.dll)\' should be used for Win32
binaries and the form \'mingw64(foo.dll)\' for Win64 binaries.

Correct dependency generation is done automatically. Packagers should
start their spec files with this line:

``` _rpm-spec
%{?mingw_package_header}
```

All binary packages should depend on &#96;+mingw32-filesystem+&#96; or
&#96;+mingw64-filesystem+&#96; (depending on the files in the package).

All specfiles should BuildRequire at least one of these (depending on
the targets for which you want to build):

``` _rpm-spec
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw64-filesystem
```

and any other BuildRequires that they need.

Most mingw RPM macros can be assumed to exist in all non-EOL Fedora
releases. If the package does, however, rely on a newly introduced
macro, a versioned dependancy on the &#96;+mingw-XX-filesystem+&#96;
packages should be used.

## Build architecture {#_build_architecture}

All packages should have:

``` _rpm-spec
BuildArch: noarch
```

unless they contain Fedora native executables. Where using the separate
packaging approach, the &#96;+BuildArch+&#96; tag must be present in the
common spec file header. Where using the integrated packaging approach,
the &#96;+BuildArch+&#96; tag must be present under the %package header
for each MinGW sub-RPM that is present.

## Libraries (DLLs) {#_libraries_dlls}

All libraries must be built as DLLs.

Because of the peculiarity of Windows, DLLs are stored in the
&#96;+%{mingw32_bindir}\\&#96; directory, along with a control file in
the \\&#96;%{mingw32_libdir}\\&#96; directory. For example, for a
library called \\&#96;+foo&#96; there would be:

``` _rpm-spec
%{mingw32_bindir}/foo.dll
%{mingw32_libdir}/foo.dll.a
```

The &#96;+foo.dll+&#96; file is the main library, &#96;+foo.dll.a+&#96;
is a stub linked to applications so they can find the library at
runtime. All of these files are required in those locations in order to
link successfully. The &#96;+.dll+&#96; may contain a version number
although not always (e.g., &#96;+foo-0.dll+&#96;).

### Do not use %{mingw32_bindir}/&#42; or %{mingw32_libdir}/&#42; in %files section {#_do_not_use_mingw32_bindir42_or_mingw32_libdir42_in_files_section}

The &#96;+%files+&#96; section must list DLLs and import libraries
separately. Packages must NOT use &#96;+%{mingw32_bindir}/&#42;+&#96; or
&#96;+%{mingw32_libdir}/&#42;+&#96;

The reason for this is that libtool is very fragile and will give up on
building a DLL very easily. Therefore we force the name of the DLL to be
listed explicitly in the &#96;+%files+&#96; section in order to catch
this during RPM builds.

### Stripping {#_stripping}

Libraries and executables should be stripped. This is done correctly and
automatically if the spec file starts with this line:

``` _rpm-spec
%{?mingw_package_header}
```

### Debuginfo subpackage {#_debuginfo_subpackage}

Most binaries contain debugging symbols when the package gets built. To
split the debugging symbols to a separate debuginfo package (as is done
with native Fedora packages) the spec file must include these lines:

``` _rpm-spec
%{?mingw_package_header}
[\&#8230;]
%{?mingw_debug_package}
```

The &#96;+%{?mingw_debug_package}\\&#96; line must be placed after the
\\&#96;%description tag+&#96;. Otherwise spectool and other RPM tools
may fail to function.

When using the integrated packaging approach the &#96;+%install+&#96;
section must also contain a call to the
&#96;+%{mingw_debug_install_post}+&#96; macro after any binary files
have been installed to the virtual root:

``` _rpm-spec
%install
[\&#8230;]
%{?mingw_debug_install_post}
```

## File listing {#_file_listing}

The MinGW packages are intended to allow developers to compile and test
the Windows support of their applications. It is furthermore expected
that developers will build Windows installers (MSIs) for their
applications using the MinGW package content.

Thus the Fedora MinGW package file listing must include content needed
to satisfy either build/test usage or the creation of Windows
installers.

### Executables (EXEs) {#_executables_exes}

Most libraries also provide executables. These can include executables
which can be used to test or showcase the library in question (for
example gtk3-demo.exe in mingw-gtk3). Other examples are helper
executables which are used by the library itself internally (for example
gspawn-win32-helper.exe in mingw-glib2).

Executables which are required for proper functionality of the libraries
must be packaged in the matching mingw32/mingw64 subpackage. Other
optional executables targetted at end users should be packaged (for
example certtool.exe in GNUTLS). Executables targetted at developers are
discouraged, but may be packaged in optional (dependent) subpackages at
a packager's discretion.

### Files which are already part of native packages {#_files_which_are_already_part_of_native_packages}

There are various types of files which are simply duplicates of
equivalent files found in Fedora native packages. These files should not
be packaged in the MinGW package. The following files don't need to be
packaged in the MinGW package when their native counterpart already
contains them:

&#42; Man pages (&#96;+%{mingw32_mandir}\\&#96; /
\\&#96;%{mingw64_mandir}\\&#96; / \\&#96;%{ucrt64_mandir}\\&#96;)
\\&#42; Info files (\\&#96;%{mingw32_infodir}\\&#96; /
\\&#96;%{mingw64_infodir}\\&#96; / \\&#96;%{ucrt64_infodir}\\&#96;)
\\&#42; Generic documentation (\\&#96;%{mingw32_docdir}\\&#96; /
\\&#96;%{mingw64_docdir}\\&#96; / \\&#96;%{ucrt64_docdir}\\&#96;)
\\&#42; Autoconf files (\\&#96;%{mingw32_datadir}/aclocal+&#96; /
&#96;+%{mingw64_datadir}/aclocal+&#96; /
&#96;+%{ucrt64_datadir}/aclocal+&#96;) &#42; gtk-doc files
(&#96;+%{mingw32_datadir}/gtk-doc+&#96; /
&#96;+%{mingw64_datadir}/gtk-doc+&#96; /
&#96;+%{ucrt64_datadir}/gtk-doc+&#96;)

Note, generic Documentation aimed at end users, as opposed to
developers, should be included where it is likely that application
developers will want to bundle it with their Windows installers.

## Converting between separate and integrated packaging {#_converting_between_separate_and_integrated_packaging}

In general it it possible to convert in either direction between the
separate and integrated packaging approaches. Both approaches result in
the exact same binary RPMs for MinGW content, only differing in their
source RPM specfile.

To convert from separate to integrated packaging

&#42; Ensure the existing native software package has either the same
(or newer) version number as the existing MinGW package. &#42; Add MinGW
support to the existing native package spec file &#42; If both the
native and existing MinGW packages were at the same version, ensure the
release number of the native package is newer than any previous build of
the MinGW package. &#42; Build the new native package with MinGW support
&#42; Retire the separate MinGW package

To convert from integrated to separate packaging

&#42; Go through the new package review process for the separate MinGW
package, ensuring it is the same version number as the existing
integrated package &#42; Import the separate MinGW package to dist-git
but don't build it. &#42; Drop MinGW support from the existing native
package spec file &#42; Build the native package without MinGW support
&#42; Ensure the separate MinGW package has a newer release number than
any existing MinGW binary sub-RPMs built from the native package &#42;
Build the separate MinGW package

In both cases the upgrade experience should be transparent to users
installing and updating Fedora deployments.

It is recommended that such conversions only be performed in Rawhide. If
there is need to do a conversion from integrated to separate packaging
in a stable release stream, a single Bohdi update must include both the
native and mingw package builds.

## Disabling MinGW packages {#_disabling_mingw_packages}

When using the integrated packaging approach it &#42;&#42;MUST&#42;&#42;
be possible to disable the build of MinGW sub-RPMs, and the build
&#42;&#42;MUST&#42;&#42; be disabled by default except for the Fedora
distribution target. This ensures that the native package can still be
built in derivative distros, such as RHEL, where the MinGW toolchains
not included. This is achieved by including a conditional near the top
of the specfile:

``` _rpm-spec
%if 0%{?fedora}
%bcond_without mingw
%else
%bcond_with mingw
%endif
```

and then wrapping all MinGW related &#96;+%package+&#96; /
&#96;+%files&#96; definitions and relevant &#96;+%build+&#96; or
&#96;+%install+&#96; commands in a conditional check:

``` _rpm-spec
%if %{with mingw}
%package -n mingw32-example
Summary: %{summary}
BuildArch: noarch
[\&#8230;]
%endif
```

## Example Integrated Package Specfile {#_example_integrated_package_specfile}

``` _rpm-spec
%if 0%{?fedora}
%bcond_without mingw
%else
%bcond_with mingw
%endif

Name: example
Version: 1.0.0
Release: 1%{?dist}
Summary: Example library

License: LGPL-2.1-or-later
URL: https://fedoraproject.org
Source: https://fedoraproject.org/example-%{version}.tar.bz2

BuildRequires: gcc
BuildRequires: binutils
BuildRequires: gettext
BuildRequires: zlib

%if %{with mingw}
BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc
BuildRequires: mingw32-binutils
BuildRequires: mingw32-gettext
BuildRequires: mingw32-win-iconv
BuildRequires: mingw32-zlib

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc
BuildRequires: mingw64-binutils
BuildRequires: mingw64-gettext
BuildRequires: mingw64-win-iconv
BuildRequires: mingw64-zlib
%endif

%description
Example library.

%package devel
Summary: Example library development package
\&#8230;

%description devel
Example library development headers and library.

%if %{with mingw}
\&#35; If a package maintainer wishes to bundle static libraries then they
\&#35; can be placed in -static subpackages. Otherwise, the -static subpackages
\&#35; can be dropped

\&#35; Win32
%package -n mingw32-example
Summary: MinGW compiled example library for the Win32 target
BuildArch: noarch

%description -n mingw32-example
MinGW compiled example library for the Win32 target.

%package -n mingw32-example-static
Summary: Static version of the MinGW Win32 compiled example library
Requires: mingw32-example = %{version}-%{release}

%description -n mingw32-example-static
Static version of the MinGW Win32 compiled example library.

\&#35; Win64
%package -n mingw64-example
Summary: MinGW compiled example library for the Win64 target

%description -n mingw64-example
MinGW compiled example library for the Win64 target.
BuildArch: noarch

%package -n mingw64-example-static
Summary: Static version of the MinGW Win64 compiled example library
Requires: mingw64-example = %{version}-%{release}

%description -n mingw64-example-static
Static version of the MinGW Win64 compiled example library.

%{?mingw_debug_package}
%endif


%prep
%autosetup -p1 -n example-%{version}


%build

%define _configure ../../configure

mkdir -p build/native
cd build/native
%configure \&#8230;
%make_build
cd ../..

%if %{with mingw}
%mingw_configure --enable-static --enable-shared --enable-foo
%mingw_make_build
%endif

%install
cd build/native
%make_install

%find_lang example
cd ../..

%if %{with mingw}
%mingw_make_install

%mingw_find_lang example
%endif

%files
%{_libdir}/libexample.so.\&#42;

%files devel
%{_libdir}/libexample.so
%{_libdir}/pkgconfig/example.pc
%{_includedir}/example/

\&#35; Static subpackages are optional (as mentioned earlier)

%if %{with mingw}
\&#35; Win32
%files -n mingw32-example -f mingw32-example.lang
%{mingw32_bindir}/libexample-0.dll
%{mingw32_includedir}/example/
%{mingw32_libdir}/libexample.dll.a
%{mingw32_libdir}/pkgconfig/example.pc

%files -n mingw32-example-static
%{mingw32_libdir}/libexample.a

\&#35; Win64
%files -n mingw64-example -f mingw64-example.lang
%{mingw64_bindir}/libexample-0.dll
%{mingw64_includedir}/example/
%{mingw64_libdir}/libexample.dll.a
%{mingw64_libdir}/pkgconfig/example.pc

%files -n mingw64-example-static
%{mingw64_libdir}/libexample-0.a
%endif

%changelog
\&#42; Sun Apr 15 2012 Erik van Pienbroek \&lt;epienbro@fedoraproject.org\&gt; - 1.0.0-1
- Initial release
```

## Example Separate Package Specfile {#_example_separate_package_specfile}

The separate package specfile essentially extracts all the content
within the &#96;+%{with mingw}+&#96; conditionals from the previous
example, and puts it into a standalone specfile.

``` _rpm-spec
%{?mingw_package_header}

Name: mingw-example
Version: 1.0.0
Release: 1%{?dist}
Summary: MinGW compiled example library

License: LGPL-2.1-or-later
URL: https://fedoraproject.org
Source: https://fedoraproject.org/example-%{version}.tar.bz2

BuildArch: noarch

BuildRequires: mingw32-filesystem
BuildRequires: mingw32-gcc
BuildRequires: mingw32-binutils
BuildRequires: mingw32-gettext
BuildRequires: mingw32-win-iconv
BuildRequires: mingw32-zlib

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-gcc
BuildRequires: mingw64-binutils
BuildRequires: mingw64-gettext
BuildRequires: mingw64-win-iconv
BuildRequires: mingw64-zlib


%description
MinGW compiled example library.


\&#35; If a package maintainer wishes to bundle static libraries then they
\&#35; can be placed in -static subpackages. Otherwise, the -static subpackages
\&#35; can be dropped

\&#35; Win32
%package -n mingw32-example
Summary: MinGW compiled example library for the Win32 target

%description -n mingw32-example
MinGW compiled example library for the Win32 target.

%package -n mingw32-example-static
Summary: Static version of the MinGW Win32 compiled example library
Requires: mingw32-example = %{version}-%{release}

%description -n mingw32-example-static
Static version of the MinGW Win32 compiled example library.

\&#35; Win64
%package -n mingw64-example
Summary: MinGW compiled example library for the Win64 target

%description -n mingw64-example
MinGW compiled example library for the Win64 target.

%package -n mingw64-example-static
Summary: Static version of the MinGW Win64 compiled example library
Requires: mingw64-example = %{version}-%{release}

%description -n mingw64-example-static
Static version of the MinGW Win64 compiled example library.


%{?mingw_debug_package}


%prep
%autosetup -p1 -n example-%{version}


%build
%mingw_configure --enable-static --enable-shared --enable-foo
%mingw_make_build


%install
%mingw_make_install

\&#35; Libtool files don't need to be bundled
find %{buildroot} -name '\&#42;.la' -delete

%mingw_find_lang example


\&#35; Note: there should be no %%files section for the main package!

\&#35; Static subpackages are optional (as mentioned earlier)

\&#35; Win32
%files -n mingw32-example -f mingw32-example.lang
%{mingw32_bindir}/libexample-0.dll
%{mingw32_includedir}/example/
%{mingw32_libdir}/libexample.dll.a
%{mingw32_libdir}/pkgconfig/example.pc

%files -n mingw32-example-static
%{mingw32_libdir}/libexample.a

\&#35; Win64
%files -n mingw64-example -f mingw64-example.lang
%{mingw64_bindir}/libexample-0.dll
%{mingw64_includedir}/example/
%{mingw64_libdir}/libexample.dll.a
%{mingw64_libdir}/pkgconfig/example.pc

%files -n mingw64-example-static
%{mingw64_libdir}/libexample-0.a


%changelog
\&#42; Sun Apr 15 2012 Erik van Pienbroek \&lt;epienbro@fedoraproject.org\&gt; - 1.0.0-1
- Initial release
```

# Message Passing Interface {#_message_passing_interface}

## Introduction {#_introduction_7}

Message Passing Interface (MPI) is an API for parallelization of
programs across multiple nodes and has been around since 1994
[1](https://en.wikipedia.org/wiki/Message_Passing_Interface). MPI can
also be used for parallelization on SMP machines and is considered very
efficient in it too (close to 100% scaling on parallelizable code as
compared to \~80% commonly obtained with threads due to unoptimal memory
allocation on NUMA machines). Before MPI, about every manufacturer of
supercomputers had their own programming language for writing programs;
MPI made porting software easy.

There are many MPI implementations available, such as [Open
MPI](https://www.open-mpi.org/) (the default MPI compiler in Fedora and
the MPI compiler used in RHEL), [MPICH](https://www.mpich.org/) (in
Fedora and RHEL) and [MVAPICH1 and
MVAPICH2](https://mvapich.cse.ohio-state.edu/) (in RHEL but not yet in
Fedora).

As some MPI libraries work better on some hardware than others, and some
software works best with some MPI library, the selection of the library
used must be done in user level, on a session specific basis. Also,
people doing high performance computing may want to use more efficient
compilers than the default one in Fedora (gcc), so one must be able to
have many versions of the MPI compiler each compiled with a different
compiler installed at the same time. This must be taken into account
when writing spec files.

## Packaging of MPI compilers {#_packaging_of_mpi_compilers}

The files of MPI compilers MUST be installed in the following
directories:

+-----------------------------------+-----------------------------------+
| File type                         | Placement                         |
+===================================+===================================+
| Binaries                          | &#                                |
|                                   | 96;+%{\_libdir}/%{name}/bin+&#96; |
+-----------------------------------+-----------------------------------+
| Libraries                         | &#                                |
|                                   | 96;+%{\_libdir}/%{name}/lib+&#96; |
+-----------------------------------+-----------------------------------+
| \[\[PackagingDrafts/Fortran       | Fortran modules\]\]               |
+-----------------------------------+-----------------------------------+
| &#96;+%{\_fmoddir}/%{name}+&#96;  | \[\[Packaging/Python              |
+-----------------------------------+-----------------------------------+
| Python modules\]\]                | &#96;+%                           |
|                                   | {python2_sitearch}/%{name}\\&#96; |
|                                   | \\&#96;                           |
|                                   | %{python3_sitearch}/%{name}+&#96; |
+-----------------------------------+-----------------------------------+
| Config files                      | &#96;+%{\_sy                      |
|                                   | sconfdir}/%{name}-%{\_arch}+&#96; |
+-----------------------------------+-----------------------------------+

As include files and manual pages are bound to overlap between different
MPI implementations, they MUST also placed outside normal directories.
It is possible that some man pages or include files (either those of the
MPI compiler itself or of some MPI software installed in the compiler's
directory) are architecture specific (e.g. a definition on a 32-bit arch
differs from that on a 64-bit arch), the directories that MUST be used
are as follows:

+-----------------------------------+-----------------------------------+
| File type                         | Placement                         |
+===================================+===================================+
| Man pages                         | &#96;+%{                          |
|                                   | \_mandir}/%{name}-%{\_arch}+&#96; |
+-----------------------------------+-----------------------------------+
| Include files                     | &#96;+%{\_in                      |
|                                   | cludedir}/%{name}-%{\_arch}+&#96; |
+-----------------------------------+-----------------------------------+

Architecture independent parts (except headers which go into
&#96;+-devel+&#96;) MUST be placed in a &#96;+-common+&#96; subpackage
that is &#96;+BuildArch: noarch+&#96;.

The runtime of MPI compilers (mpirun, the libraries, the manuals etc)
MUST be packaged into %{name}, and the development headers and libraries
into %{name}-devel.

As the compiler is installed outside &#96;+PATH+&#96;, one needs to load
the relevant variables before being able to use the compiler or run MPI
programs. This is done using [environment
modules](EnvironmentModules.xml).

The module file MUST be installed under
&#96;+%{\_sysconfdir}/modulefiles/mpi+&#96;. This allows as user with
only one mpi implementation installed to load the module with:

&#8230;. module load mpi &#8230;.

The module file MUST have the line:

&#8230;. conflict mpi &#8230;.

to prevent concurrent loading of multiple mpi modules.

The module file MUST prepend &#96;+\$MPI_BIN+&#96; into the user's
&#96;+PATH+&#96; and prepend &#96;+\$MPI_LIB+&#96; to
&#96;+LD_LIBRARY_PATH+&#96;. The module file MUST also set some helper
variables (primarily for use in spec files):

+----------------------+----------------------+-----------------------+
| Variable             | Value                | Explanation           |
+======================+======================+=======================+
| &#96;+MPI_BIN+&#96;  | &#96;+%{\_libdi      | Binaries compiled     |
|                      | r}/%{name}/bin+&#96; | against the MPI stack |
+----------------------+----------------------+-----------------------+
| &#96;                | &#96;                | MPI stack specific    |
| +MPI_SYSCONFIG+&#96; | +%{\_sysconfdir}/%{n | configuration files   |
|                      | ame}-%{\_arch}+&#96; |                       |
+----------------------+----------------------+-----------------------+
| &#96;+MPI_F          | &#96;+%{\_fm         | MPI stack specific    |
| ORTRAN_MOD_DIR+&#96; | oddir}/%{name}+&#96; | Fortran module        |
|                      |                      | directory             |
+----------------------+----------------------+-----------------------+
| &#9                  | &#96;                | MPI stack specific    |
| 6;+MPI_INCLUDE+&#96; | +%{\_includedir}/%{n | headers               |
|                      | ame}-%{\_arch}+&#96; |                       |
+----------------------+----------------------+-----------------------+
| &#96;+MPI_LIB+&#96;  | &#96;+%{\_libdi      | Libraries compiled    |
|                      | r}/%{name}/lib+&#96; | against the MPI stack |
+----------------------+----------------------+-----------------------+
| &#96;+MPI_MAN+&#96;  | &                    | MPI stack specific    |
|                      | #96;+%{\_mandir}/%{n | man pages             |
|                      | ame}-%{\_arch}+&#96; |                       |
+----------------------+----------------------+-----------------------+
| &#96;+MPI_PY         | &#96;+%{python2_sit  | MPI stack specific    |
| THON2_SITEARCH+&#96; | earch}/%{name}+&#96; | Python 2 modules      |
+----------------------+----------------------+-----------------------+
| &#96;+MPI_PY         | &#96;+%{python3_sit  | MPI stack specific    |
| THON3_SITEARCH+&#96; | earch}/%{name}+&#96; | Python 3 modules      |
+----------------------+----------------------+-----------------------+
| &#96                 | &#96;+%{n            | Name of compiler      |
| ;+MPI_COMPILER+&#96; | ame}-%{\_arch}+&#96; | package, for use in   |
|                      |                      | e.g. spec files       |
+----------------------+----------------------+-----------------------+
| &#                   | &                    | The suffix used for   |
| 96;+MPI_SUFFIX+&#96; | #96;+\_%{name}+&#96; | programs compiled     |
|                      |                      | against the MPI stack |
+----------------------+----------------------+-----------------------+

As these directories may be used by software using the MPI stack, the
MPI runtime package MUST own all of them.

MUST: By default, NO files are placed in &#96;+/etc/ld.so.conf.d+&#96;.
If the packager wishes to provide alternatives support, it MUST be
placed in a subpackage along with the ld.so.conf.d file so that
alternatives support does not need to be installed if not wished for.

MUST: If the maintainer wishes for the environment module to load
automatically by use of a scriptlet in /etc/profile.d or by some other
mechanism, this MUST be done in a subpackage.

MUST: The MPI compiler package MUST provide an RPM macro that makes
loading and unloading the support easy in spec files, e.g. by placing
the following in &#96;+/etc/rpm/macros.openmpi+&#96;

&#8230;. %\_openmpi_load \\ . /etc/profile.d/modules.sh; \\ module load
mpi/openmpi-%{\_arch}; \\ export CFLAGS=\'\$CFLAGS %{optflags}\';
%\_openmpi_unload \\ . /etc/profile.d/modules.sh; \\ module unload
mpi/openmpi-%{\_arch}; &#8230;.

loading and unloading the compiler in spec files is as easy as
&#96;+%{\_openmpi_load}\\&#96; and \\&#96;%{\_openmpi_unload}+&#96;.

Automatic setting of the module loading path in python interpreters is
done using a &#96;+.pth+&#96; file placed in one of the directories
normally searched for modules (&#96;+%{python2_sitearch}\\&#96;,
\\&#96;%{python3_sitearch}\\&#96;). Those \\&#96;.pth+&#96; files should
append the directory specified with \$MPI_PYTHON2_SITEARCH or
\$MPI_PYTHON3_SITEARCH environment variable, depending on the
interpreter version, to &#96;+sys.path+&#96;, and do nothing if those
variables are unset. Module files MUST NOT set PYTHONPATH directly,
since it cannot be set for both Python versions at the same time.

If the environment module sets compiler flags such as &#96;+CFLAGS+&#96;
(thus overriding the ones exported in &#96;+%configure+&#96;, the RPM
macro MUST make them use the Fedora optimization flags
&#96;+%{optflags}+&#96; once again (as in the example above in which the
openmpi-%{\_arch} module sets CFLAGS).

## Packaging of MPI software {#_packaging_of_mpi_software}

Software that supports MPI MUST be packaged also in serial mode \[i.e.
no MPI\], if it is supported by upstream. (for instance:
&#96;+foo+&#96;).

If possible, the packager MUST package versions for each MPI compiler in
Fedora (e.g. if something can only be built with mpich and mvapich2,
then mvapich1 and openmpi packages do not need to be made).

MPI implementation specific files MUST be installed in the directories
used by the used MPI compiler (&#96;+\$MPI_BIN+&#96;,
&#96;+\$MPI_LIB+&#96; and so on).

The binaries MUST be suffixed with &#96;+\$MPI_SUFFIX+&#96; (e.g.
\_openmpi for Open MPI, \_mpich for MPICH and \_mvapich2 for MVAPICH2).
This is for two reasons: the serial version of the program can still be
run when an MPI module is loaded and the user is always aware of the
version s/he is running. This does not need to hurt the use of shell
scripts:

&#8230;. &#35; Which MPI implementation do we use?

&#35;module load mpi/mvapich2-i386 &#35;module load mpi/openmpi-i386
module load mpi/mpich-i386

&#35; Run preprocessor foo -preprocess &lt; foo.in &#35; Run calculation
mpirun -np 4 foo\${MPI_SUFFIX} &#35; Run some processing mpirun -np 4
bar\${MPI_SUFFIX} -process &#35; Collect results bar -collect &#8230;.

The MPI enabled bits MUST be placed in a subpackage with the suffix
denoting the MPI compiler used (for instance: &#96;+foo-openmpi+&#96;
for Open MPI \[the traditional MPI compiler in Fedora\] or
&#96;+foo-mpich+&#96; for MPICH). For directory ownership and to
guarantee the pickup of the correct MPI runtime, the MPI subpackages
MUST require the correct MPI compiler's runtime package.

Each MPI build of shared libraries SHOULD have a separate -libs
subpackage for the libraries (e.g. foo-mpich-libs). As in the case of
MPI compilers, library configuration (in &#96;+/etc/ld.so.conf.d+&#96;)
MUST NOT be made.

In case the headers are the same regardless of the compilation method
and architecture (e.g. 32-bit serial, 64-bit Open MPI, MPICH), they MUST
be split into a separate &#96;+-headers+&#96; subpackage (e.g.
\'foo-headers\'). Fortran modules are architecture specific and as such
are placed in the (MPI implementation specific) &#96;+-devel+&#96;
package (foo-devel for the serial version and foo-openmpi-devel for the
Open MPI version).

Each MPI build MUST have a separate -devel subpackage (e.g.
foo-mpich-devel) that includes the development libraries and
&#96;+Requires: %{name}-headers+&#96; if such a package exists. The goal
is to be able to install and develop using e.g. \'foo-mpich-devel\'
without needing to install e.g. openmpi or the serial version of the
package.

Files must be shared between packages as much as possible. Compiler
independent parts, such as data files in
&#96;+%{\_datadir}/%{name}\\&#96; and man files MUST be put into a
\\&#96;-common+&#96; subpackage that is required by all of the binary
packages (the serial package and all of the MPI packages).

### A sample spec file {#_a_sample_spec_file}

&#8230;. &#35; Define a macro for calling ../configure instead of
./configure %global dconfigure %(printf %%s \'%configure\' \| sed
\'s!\\./configure!../configure!g\')

Name: foo Requires: %{name}-common = %{version}-%{release}

%package common

%package openmpi BuildRequires: openmpi-devel &#35; Require explicitly
for dir ownership and to guarantee the pickup of the right runtime
Requires: openmpi Requires: %{name}-common = %{version}-%{release}

%package mpich BuildRequires: mpich-devel &#35; Require explicitly for
dir ownership and to guarantee the pickup of the right runtime Requires:
mpich Requires: %{name}-common = %{version}-%{release}

%build &#35; Have to do off-root builds to be able to build many
versions at once

&#35; To avoid replicated code define a build macro %define dobuild() \\
mkdir \$MPI_COMPILER; \\ cd \$MPI_COMPILER; \\ %dconfigure
\--program-suffix=\$MPI_SUFFIX ;\\ make %{?\_smp_mflags} ; \\ cd ..

&#35; Build serial version, dummy arguments MPI_COMPILER=serial
MPI_SUFFIX= %dobuild

&#35; Build parallel versions: set compiler variables to MPI wrappers
export CC=mpicc export CXX=mpicxx export FC=mpif90 export F77=mpif77

&#35; Build OpenMPI version %{\_openmpi_load} %dobuild
%{\_openmpi_unload}

&#35; Build mpich version %{\_mpich_load} %dobuild %{\_mpich_unload}

%install &#35; Install serial version make -C serial install
DESTDIR=%{buildroot} INSTALL=\'install -p\' CPPROG=\'cp -p\'

&#35; Install OpenMPI version %{\_openmpi_load} make -C \$MPI_COMPILER
install DESTDIR=%{buildroot} INSTALL=\'install -p\' CPPROG=\'cp -p\'
%{\_openmpi_unload}

&#35; Install MPICH version %{\_mpich_load} make -C \$MPI_COMPILER
install DESTDIR=%{buildroot} INSTALL=\'install -p\' CPPROG=\'cp -p\'
%{\_mpich_unload}

%files &#35; All the serial (normal) binaries

%files common &#35; All files shared between the serial and different
MPI versions

%files openmpi &#35; All openmpi linked files

%files mpich &#35; All mpich linked files &#8230;.

# Shell Completions {#_shell_completions}

Shell completions are command line completions for a specific shell,
such as Bash, fish or Zsh.

## RPM Macros {#_rpm_macros_8}

The following macros &#42;MUST&#42; be used instead of hardcoding paths.

+-----------------------------------+-----------------------------------+
| macro                             | definition                        |
+===================================+===================================+
| %{bash_completions_dir}           | %{\_dat                           |
|                                   | adir}/bash-completion/completions |
+-----------------------------------+-----------------------------------+
| %{fish_completions_dir}           | %{\_d                             |
|                                   | atadir}/fish/vendor_completions.d |
+-----------------------------------+-----------------------------------+
| %{zsh_completions_dir}            | %{\_datadir}/zsh/site-functions   |
+-----------------------------------+-----------------------------------+

## Shell Completions Packaging {#_shell_completions_packaging}

Shell completion files &#42;MUST&#42; use standard file permissions
(0644).

### Example of shell completions packaging {#_example_of_shell_completions_packaging}

``` _rpm-spec
Name: foo
\&#8230;

%install
\&#8230;

\&#35; Bash completion
install -Dpm 0644 foo.bash -t %{buildroot}%{bash_completions_dir}

\&#35; Fish completion
install -Dpm 0644 foo.fish -t %{buildroot}%{fish_completions_dir}

\&#35; Zsh completion
install -Dpm 0644 _foo -t     %{buildroot}%{zsh_completions_dir}
\&#8230;

%files
%{bash_completions_dir}/foo.bash
%{fish_completions_dir}/foo.fish
%{zsh_completions_dir}/_foo
```

# Sugar Activity Packaging Guidelines {#_sugar_activity_packaging_guidelines}

These guidelines are for packaging Sugar activities.
[Sugar](http://wiki.laptop.org/go/Sugar) is the core of the OLPC Human
Interface.

## Macros {#_macros_7}

Sugar looks for its activities in two fixed locations, which are defined
in sugar-toolkit with rpm macros:

Architecture Independent (noarch):

&#8230;. %global sugaractivitydir /usr/share/sugar/activities/ &#8230;.

Architecture Dependent:

&#8230;. %global sugarlibdir %{\_libdir}/sugar/activities &#8230;.

## Necessary BuildRequires {#_necessary_buildrequires}

All Sugar Activities use setup.py, which is dependant upon
sugar-toolkit. Accordingly, all activities need to:

&#8230;. BuildRequires: sugar-toolkit &#8230;.

## Naming {#_naming_12}

All activities &#42;MUST&#42; be named &#96;+sugar-+&#96;.

## Architecture-specific Activities {#_architecture_specific_activities}

All activities containing compiled code (thus, architecture-specific)
must be built in the %build section. Any architecture-specific bits must
either go in &#96;+%{\_bindir}\\&#96; \\&#96;%{\_libdir}\\&#96; or
\\&#96;%{sugarlibdir}+&#96; as appropriate.

## Runtime Dependencies {#_runtime_dependencies}

All runtime dependency information &#42;MUST&#42; be manually added.
There is no build time detection for Sugar activities.

## Sample SPEC {#_sample_spec}

&#8230;. Name: sugar-journal Version: 79 Release: 1%{?dist} Summary:
Journal for Sugar

Group: Sugar/Activities License: GPL-2.0-or-later URL:
<http://wiki.laptop.org/go/Journal> Source:
journal-activity-%{version}.tar.bz2 Source1: sugar-journal-checkout.sh
BuildRoot: %{\_tmppath}/%{name}-%{version}-%{release}-root-%(%{\_\_id_u}
-n)

BuildRequires: python sugar-toolkit Requires: sugar BuildArch: noarch

%description The Journal activity provides an intuitive interface for
viewing projects and files saved by the XO user. Activities that the
user has stopped will show in the journal view with a timer showing how
long ago they were stopped.

%prep %setup -q -n journal-activity-%{version}

%build

%install rm -rf \$RPM_BUILD_ROOT mkdir -p
\$RPM_BUILD_ROOT%{sugaractivitydir} ./setup.py install
\$RPM_BUILD_ROOT%{sugaractivitydir}

%clean rm -rf \$RPM_BUILD_ROOT

%files %doc NEWS %{sugaractivitydir}/Journal.activity/

%changelog &#42; Fri Apr 04 2008 Dennis Gilmore
&lt;<dennis@ausil.us>&gt; - 79-1 - Initial packaging &#8230;.

## Sample Checkout Script {#_sample_checkout_script}

&#8230;. &#35;!/bin/bash

VERSION=79 NAME=journal-activity

rm -rf \$NAME-\$VERSION

git clone git://dev.laptop.org/\$NAME \$NAME-\$VERSION

tar -cjvf \$NAME-\$VERSION.tar.bz2 \$NAME-\$VERSION

rm -rf \$NAME-\$VERSION &#8230;.

# Packaging of Tree-sitter parsers {#_packaging_of_tree_sitter_parsers}

## Macros {#_macros_8}

The macros in package &#96;tree-sitter-srpm-macros&#96; can do most of
the work for you.

### Specifying the build system {#_specifying_the_build_system}

Declare that this is a Tree-sitter parser with:

``` spec
BuildSystem: tree_sitter
```

The &#96;%prep&#96;, &#96;%conf&#96;, &#96;%generate_buildrequires&#96;,
&#96;%build&#96;, &#96;%install&#96; and &#96;%check&#96; sections will
all be provided for you.

This requires RPM version 4.20 (i.e., Fedora 41) or greater.

### Defining packages and their contents {#_defining_packages_and_their_contents}

Generate &#96;%package&#96; and &#96;%files&#96; sections for the
subpackages built from your package:

``` spec
%{tree_sitter -l language-name}
```

Here, *language-name* is the human-friendly name(s) of the Language
parser(s) provided by this package, to be mentioned in the package
summaries and descriptions.

## Example spec file {#_example_spec_file_4}

``` spec
Name:           tree-sitter-typescript
Version:        0.21.2
Release:        %autorelease
License:        MIT
URL:            https://github.com/tree-sitter/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    tree_sitter

%{tree_sitter -l %{quote:TypeScript and TSX}}

%changelog
%autochangelog
```

# Web Assets Packaging Guidelines {#_web_assets_packaging_guidelines}

## Scope {#_scope}

&#42;Web Assets&#42; are any static content that are shipped intact to
web browsers, usually by web applications. These might be user interface
frameworks, Flash video players, CSS frameworks, icon libraries, or lots
of other possibilities.

If your package is primarily or solely shipped to a browser and not used
locally, and is not JavaScript, it probably falls under these
guidelines. JavaScript packages must follow the [JavaScript
guidelines](JavaScript.xml) in addition to these guidelines.

## Rationale {#_rationale_3}

There are lots of little bits shipped to browsers that aren't just
JavaScript that typically have been bundled along with web applications
up to this point. [There are a lot of good reasons why we shouldn't
bundle JavaScript this
way](JavaScript.adoc&#35;_bundling_of_other_libraries), so it only
follows that we should fix it for the rest of that kind of stuff too.

## BuildRequires {#_buildrequires_8}

To ensure the presence of the necessary RPM macros, all packages that
provide web assets must have:

``` _rpm-spec
BuildRequires:  web-assets-devel
```

## Requires {#_requires_2}

To ensure the availability of the necessary directories, all packages
that provide web assets must have:

``` _rpm-spec
Requires:  web-assets-filesystem
```

Web application packages that ship configuration files for Apache HTTPd
should ensure that the httpd configuration is installed as well:

``` _rpm-spec
Requires:  web-assets-httpd
```

## RPM Macros {#_rpm_macros_9}

+----------------------+----------------------+-----------------------+
| Macro                | Normal Definition    | Notes                 |
+======================+======================+=======================+
| \_webassetdir        | %{\                  | The directory where   |
|                      | _datadir}/web-assets | all web assets are    |
|                      |                      | stored                |
+----------------------+----------------------+-----------------------+

## Install Location {#_install_location_2}

All packages that contain static content useful to different web
applications must install into a subdirectory of
&#96;+%{\_assetdir}\\&#96;. For instance, the \\&#96;+jquery-ui&#96;
package should install itself into
&#96;+%{\_webassetdir}/jquery-ui+&#96;.

All packages that contain static content that is only useful within the
package in which they are shipped should continue to ship that content
in the application's directory structure. However, they must follow the
remainder of the guidelines outlined in this document.

## Server Location {#_server_location_2}

All HTTP daemons in the distribution should make
&#96;+%{\_webassetdir}\\&#96; available in \\&#96;/.sysassets+&#96;.

Therefore, if the &#96;+fabulous-web-icons+&#96; package ships an icon
as &#96;+%{\_webassetdir}/fabulous-web-icons/important.png+&#96;, you
can include it in a web application with the following HTML:

&#8230;. &lt;img
src=\'/.sysassets/fabulous-web-icons/important.png\'&gt; &#8230;.

Regardless, web applications may want to make subdirectories of
&#96;+%{\_webassetdir}+&#96; available under their own directory via
aliases or symlinks for compatibility purposes or to eliminate needless
deviation from upstream.

## Content Guidelines {#_content_guidelines}

Web Assets must follow the general guidelines for [what can be
packaged](WhatCanBePackaged.xml), unless stated otherwise in this
document.

## CSS {#_css}

Pure CSS frameworks can be included as-is. CSS frameworks that use an
alternative language that compiles to CSS, such as
[LESS](https://lesscss.org/), must compile to CSS as part of the build
process.

Packages containing CSS should make the best effort to regenerate any
precompiled/minimized CSS wherever possible, as this leads to more
maintainable packages. Where this would result in a significant
hardship, the bundled pregenerated CSS may be shipped with a specfile
comment explaining the decision. This does not eliminate the requirement
to validate licenses of bundled content.

## Flash {#_flash}

Flash files (which typically use the &#96;+.swf+&#96; extension) must
follow the general and licensing guidelines for code, not content, and
must be built from source using a toolchain available in Fedora.

The Flash software needs to be compiled by a free software toolchain,
such as &#96;+swfc+&#96;. [Pre-built &#96;+.swf+&#96; files &#42;must
not&#42; be included in Fedora
packages.](WhatCanBePackaged.adoc&#35;prebuilt-binaries-or-libraries)
That compilation must be performed as part of the build process for the
package.

If the flash software is not compilable using the toolchains inside of
Fedora then the flash software cannot be shipped. In some cases you may
be able to patch out use of the flash software (for instance, if it's a
fallback in case the browser doesn't support HTML5) or you may have to
give up on packaging the software until the flash software toolchain is
enhanced to allow building.

## Java applets {#_java_applets}

Java applets should follow the general and licensing guidelines for
code, not content. Additionally, they should follow the [Java
guidelines](Java.xml), with the exception that the actual
&#96;+.jar+&#96; file for the Java applet should be installed into a
subdirectory of &#96;+%{\_webassetdir}+&#96;.

## Images {#_images}

Images that are part of a larger Web Asset package can be included in
that package's subdirectory. For instance, a UI library might contain
images for its UI components in its subdirectory.

Web Asset packages that consist solely of images, such as a set of
icons, may be shipped as their own package.

## Fonts {#_fonts_2}

All system fonts (available in &#96;+%{\_datadir}/fonts+&#96;) are
automatically made available in &#96;+%{\_webassetdir}/fonts/+&#96; via
a symlink. For more information on packaging system fonts, see the [font
guidelines](FontsPolicy.xml). Please note that only fonts available in
the Fedora package collection are made available on HTTP servers by
default.

Please note that those guidelines prohibit packaging fonts elsewhere.
There is no compelling reason to support other font formats, as most
browsers that support web fonts support the TTF or OTF formats used by
system fonts, therefore alternative web font formats like WOFF are
prohibited.

# WordPress plugins Packaging Guidelines {#_wordpress_plugins_packaging_guidelines}

[WordPress plugins](https://wordpress.org/plugins/) are packaged for
Fedora so that the plugin can be used for both and without requiring
both.

## Requirements for packaging {#_requirements_for_packaging}

&#42; Use the [specfile template](&#35;Specfile_template) &#42; Set
&#96;+plugin_name+&#96; and &#96;+plugin_human_name+&#96; by appending
the first two lines appropriately &#42;&#42; &#96;+plugin_name+&#96; is
the short name used in the URL for the plugin's page on wordpress.org
&#42;&#42; &#96;+plugin_human_name+&#96; is the full name of the plugin
as displayed on the plugin's page on wordpress.org &#42; Fill in the
version of the package as it is displayed in the .zip filename &#42;
Fill in a package description in both places where it says \'Your
plugin's description goes here.\'

### Example {#_example_4}

<https://wordpress.org/plugins/stats/>

&#8230;. %global plugin_name stats %global plugin_human_name
WordPress.com Stats &#8230;.

## Notes {#_notes_2}

&#42; The spec must be named
&#96;+wordpress-plugin-%{plugin_name}.spec+&#96; as per the
Packaging:NamingGuidelines\[naming guidelines\] &#42; Remember to enter
a changelog entry

## Specfile template {#_specfile_template}

&#8230;. %global plugin_name %global plugin_human_name

Name: wordpress-plugin-%{plugin_name} Version: Release: 1%{?dist}
Summary: %{plugin_human_name} plugin for WordPress

Group: Applications/Publishing &#35; According to
<https://plugins.trac.wordpress.org/> all plugins are licensed &#35;
under the GPL unless otherwise stated in the plugin source. License:
GPL-3.0-or-later URL:
[https://wordpress.org/plugins/%{plugin_name}/](https://wordpress.org/plugins/%{plugin_name}/)
Source:
[https://downloads.wordpress.org/plugin/%{plugin_name}.%{version}.zip](https://downloads.wordpress.org/plugin/%{plugin_name}.%{version}.zip)
BuildRoot: %(mktemp -ud
%{\_tmppath}/%{name}-%{version}-%{release}-XXXXXX) Requires: wordpress
BuildArch: noarch

%description Your plugin's description goes here.

This package is built for use with WordPress (wordpress), not WordPress
MU. Use wordpress-mu-plugin-%{plugin_name} for WordPress MU.

%package -n wordpress-mu-plugin-%{plugin_name} Summary:
%{plugin_human_name} plugin for WordPress MU Group:
Applications/Publishing &#35; According to
<https://plugins.trac.wordpress.org/> all plugins are licensed &#35;
under the GPL unless otherwise stated in the plugin source. License:
GPL-3.0-or-later Requires: wordpress-mu BuildArch: noarch

%description -n wordpress-mu-plugin-%{plugin_name} Your plugin's
description goes here.

This package is built for use with WordPress MU (wordpress-mu), not
regular WordPress. Use wordpress-plugin-%{plugin_name} for regular
Wordpress.

%prep %setup -q -c echo \'To enable \'%{plugin_human_name}\', go to the
administrative section of your blog, \'Plugins\', and enable the plugin
there.\' &gt; README.fedora echo \'To allow users to enable
\'%{plugin_human_name}\' for their blogs, be sure to enable this plugin
in the administrative control panel for your website.\' &gt;
README.fedora.mu

%build

%install rm -rf %{buildroot} mkdir -p
%{buildroot}%{\_datadir}/wordpress/wp-content/plugins/ cp -a
%{plugin_name} %{buildroot}%{\_datadir}/wordpress/wp-content/plugins/
mkdir -p %{buildroot}%{\_datadir}/wordpress-mu/wp-content/plugins/ cp -a
%{plugin_name} %{buildroot}%{\_datadir}/wordpress-mu/wp-content/plugins/

%clean rm -rf %{buildroot}

%files %doc README.fedora
%{\_datadir}/wordpress/wp-content/plugins/%{plugin_name}

%files -n wordpress-mu-plugin-%{plugin_name} %doc README.fedora.mu
%{\_datadir}/wordpress-mu/wp-content/plugins/%{plugin_name}

%changelog &#8230;.

[^1]: To avoid *foofont-fonts* packages.

[^2]: [findlib Reference Manual - META
    files.](http://projects.camlcity.org/projects/dl/findlib-1.9.5/doc/ref-html/r759.html)

[^3]: [PSR-0](https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-0.md)

[^4]: [PSR-4](https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-4-autoloader.md)

[^5]: Fonts accessed through the original *core* X protocol, using tools
    like *mkfontdir*, *xfs*, */etc/X11/fontpath.d/*, *XLFD* strings,
    etc. See also this
    [paper](https://keithp.com/~keithp/talks/xtc2001/paper/) written
    shortly before projects massively migrated to client-side fonts.
