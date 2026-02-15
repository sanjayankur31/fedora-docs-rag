To enable the EPEL repository on your system, install the appropriate
release package as described below. These packages contain the
repository configuration and public package signing key.

:::: caution
::: title
:::

Some EPEL packages depend on packages from repositories that are not
enabled by default. Take note of the additional repositories being
enabled in the instructions on this page.
::::

:::: note
::: title
:::

For convenience, some distributions include copies of EPEL release
packages in their default repositories, allowing you to install them by
name without the full URL. The EPEL project recommends using the
official permalinks on this page to ensure the best experience.
::::

# Release package permalinks {#_release_package_permalinks}

- [epel-release-latest-10](https://dl.fedoraproject.org/pub/epel/epel-release-latest-10.noarch.rpm)

- [epel-next-release-latest-9](https://dl.fedoraproject.org/pub/epel/epel-next-release-latest-9.noarch.rpm)

- [epel-release-latest-9](https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm)

- [epel-release-latest-8](https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm)

# EL10 {#_el10}

## CentOS Stream 10 {#_centos_stream_10}

``` console
$ dnf config-manager --set-enabled crb
$ dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-10.noarch.rpm
```

## RHEL 10 {#_rhel_10}

``` console
$ subscription-manager repos --enable codeready-builder-for-rhel-10-$(arch)-rpms
$ dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-10.noarch.rpm
```

# EL9 {#_el9}

:::: note
::: title
:::

EPEL 9 has two different release packages. If you are using RHEL 9, only
install the `epel-release` package. If you are using CentOS Stream 9,
install **both** the `epel-release` and `epel-next-release` packages.
::::

## CentOS Stream 9 {#_centos_stream_9}

``` console
$ dnf config-manager --set-enabled crb
$ dnf install https://dl.fedoraproject.org/pub/epel/epel{,-next}-release-latest-9.noarch.rpm
```

## RHEL 9 {#_rhel_9}

``` console
$ subscription-manager repos --enable codeready-builder-for-rhel-9-$(arch)-rpms
$ dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm
```

## Other RHEL 9 compatible distributions {#_other_rhel_9_compatible_distributions}

EPEL 9 officially targets CentOS Stream 9 and RHEL 9. EPEL 9 packages
will also likely work with other distributions that target RHEL 9
compatibility. We cannot list specific instructions for all such
distributions, but in general the steps needed should look similar to
the steps for RHEL 9. First enable the distribution's equivalent of the
CRB repository, then install the `epel-release` package.

``` console
$ dnf config-manager --set-enabled crb
$ dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm
```

# EL8 {#_el8}

## RHEL 8 {#_rhel_8}

``` console
$ subscription-manager repos --enable codeready-builder-for-rhel-8-$(arch)-rpms
$ dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
```

## Other RHEL 8 compatible distributions {#_other_rhel_8_compatible_distributions}

EPEL 8 officially targets RHEL 8. EPEL 8 packages will also likely work
with other distributions that target RHEL 8 compatibility. We cannot
list specific instructions for all such distributions, but in general
the steps needed should look similar to the steps for RHEL 8. First
enable the distribution's equivalent of the PowerTools/CRB repository,
then install the `epel-release` package.

``` console
$ dnf config-manager --set-enabled powertools
$ dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
```

# Previous versions (End-of-life releases) {#end_of_life_releases}

:::: warning
::: title
:::

**End-of-life releases are no longer supported.**
::::

:::: note
::: title
:::

Due to major security changes in SSL in the last 10 years, older
releases may not be able to directly point to these releases. As of
2021-01-22, EPEL-5 and 4 systems do not have the newer TLS 1.2
algorithms that Internet servers are required to use for security
reasons. The best method for working with these is to have a newer
system mirror the entire archive and then for your systems to point to
that mirror.
::::

- EPEL 7: <https://dl.fedoraproject.org/pub/archive/epel/7/>

- EPEL 6: <https://dl.fedoraproject.org/pub/archive/epel/6/>

- EPEL 5: <https://dl.fedoraproject.org/pub/archive/epel/5/>

- EPEL 4: <https://dl.fedoraproject.org/pub/archive/epel/4/>
  :experimental:

# Available packages in EPEL {#available_packages_and_versions_in_epel}

Since EPEL is part of the Fedora project, you can search the available
packages in the [Fedora Packages web
app](https://packages.fedoraproject.org/). This provides an overview of
available versions across various EPEL branches. If you find a package
that is not yet available in the EPEL branch you would like it to be,
please follow [this guide](epel-package-request.xml) to request it.

Alternately, you can browse the repo files directly:

- EPEL 10:
  [x86_64](https://dl.fedoraproject.org/pub/epel/10/Everything/x86_64/),
  [s390x](https://dl.fedoraproject.org/pub/epel/10/Everything/s390x/),
  [ppc64le](https://dl.fedoraproject.org/pub/epel/10/Everything/ppc64le/),
  [aarch64](https://dl.fedoraproject.org/pub/epel/10/Everything/aarch64/),
  [sources](https://dl.fedoraproject.org/pub/epel/10/Everything/source/tree/)

- EPEL 9:
  [x86_64](https://dl.fedoraproject.org/pub/epel/9/Everything/x86_64/),
  [s390x](https://dl.fedoraproject.org/pub/epel/9/Everything/s390x/),
  [ppc64le](https://dl.fedoraproject.org/pub/epel/9/Everything/ppc64le/),
  [aarch64](https://dl.fedoraproject.org/pub/epel/9/Everything/aarch64/),
  [sources](https://dl.fedoraproject.org/pub/epel/9/Everything/source/tree/)

- EPEL 8:
  [x86_64](https://dl.fedoraproject.org/pub/epel/8/Everything/x86_64/),
  [s390x](https://dl.fedoraproject.org/pub/epel/8/Everything/s390x/),
  [ppc64le](https://dl.fedoraproject.org/pub/epel/8/Everything/ppc64le/),
  [aarch64](https://dl.fedoraproject.org/pub/epel/8/Everything/aarch64/),
  [sources](https://dl.fedoraproject.org/pub/epel/8/Everything/SRPMS/)

You can also browse these same directories on any of our
[mirrors](https://admin.fedoraproject.org/mirrormanager/mirrors/EPEL).
:experimental:

# The EPEL testing repository {#_the_epel_testing_repository}

The `epel-testing` repository contains updates scheduled to be released
for the maintained releases of EPEL. User testing and feedback provided
via [Bodhi](https://bodhi.fedoraproject.org), on the
[epel-devel](https://admin.fedoraproject.org/mailman/listinfo/epel-devel)
mailing list and the relevant [Bugzilla](https://bugzilla.redhat.com) is
vital to ensure that good updates are released quickly and bad ones kept
away from release.

## Using the epel-testing repository {#using_the_epel_testing_repository}

### Enabling the repository persistently {#enabling_the_repository_persistently}

The following command will enable the `epel-testing` repository
persistently.

``` console
$ dnf config-manager --set-enabled epel-testing
```

Use `dnf repolist` to verify. If you wish to disable it again, run the
following command.

``` console
$ dnf config-manager --set-disabled epel-testing
```

:::: tip
::: title
:::

`dnf distro-sync` will sync the packages to the versions available in
the repository. This might be useful to run after you disable the
testing repository to downgrade packages back to the stable versions.
::::

:::: note
::: title
:::

The `dnf config-manager` command is available as part of the
dnf-plugins-core package. You can also edit the
`/etc/yum.repos.d/epel-testing.repo` file manually to set `enabled=1`
under the `[epel-testing]` section.
::::

### Enabling the repository temporarily {#enabling_the_repository_temporarily}

You can enable the the `epel-testing` repository on a case-by-case basis
instead of persistently.

The following command will enable the `epel-testing` repository for a
single upgrade transaction.

``` console
$ dnf --enablerepo epel-testing upgrade
```

The following command will enable the `epel-testing` repository for a
single install transaction.

``` console
$ dnf --enablerepo epel-testing install <foo>
```

## What to test, testing, and reporting results {#what_to_test_testing_and_reporting_results}

The [Bodhi](https://bodhi.fedoraproject.org) system is used to track and
collate feedback on testing updates. All testing updates will be shown
in the Bodhi system. First of all, if any test update package works
worse for you in any respect than the pre-update version did, this is a
problem that should be communicated to the developers. Secondly, when
you click on a certain update, you will see a screen with more
information on the update. The `Details` section should give you
information on what the update is intended to fix. You should, if
possible, test that the update does indeed fix the issues it claims to
fix.

You can give your feedback on a test update by using the [Bodhi web
interface](https://bodhi.fedoraproject.org). There is a `Login` link in
the left-hand sidebar. Log in using your Fedora account. If you don't
have a Fedora account, you can [create an account
here](https://admin.fedoraproject.org/accounts/user/new). Once you are
logged in, you will be able to leave a comment on the update. Underneath
the comment box are three options: `Untested`, `Works for me`, and
`Does not work`. For a guide on when to leave each type of feedback,
read the [update feedback
guidelines](https://fedoraproject.org/wiki/QA:Update_feedback_guidelines).

Each `Works for me` adds 1 to the test update's karma, while each
`Does not work` subtracts 1 from it. `Untested` leaves the karma
unchanged. Usually, test updates with karma of 3 are automatically sent
out as full official updates, while test updates with karma of -3 are
automatically withdrawn from the testing repository. As you can see,
your testing and feedback is vital to make sure that good updates are
released quickly and bad ones don't get out to the general public.

## See also {#see_also}

- [Bodhi Guide](https://fedoraproject.org/wiki/Bodhi) :experimental:
  :page-aliases: request.adoc

# Requesting a new package in EPEL {#_requesting_a_new_package_in_epel}

When requesting a Fedora package for EPEL, the steps are a little
different depending on your ability or willingness to help.

If you are already a Fedora contributor, for your own package use the
[standard
procedures](package-maintainers::Package_Maintenance_Guide.xml) for
requesting a new branch using `fedpkg request-branch`.

:::: note
::: title
:::

Before requesting a package in EPEL, it must first be in Fedora. There
are some rare exceptions where an EPEL-only package is necessary, but
those are out of scope for this guide.
::::

## Determine the component {#determine_the_component}

EPEL package requests are tracked in bugzilla. The **source package**
name is used as the bugzilla `Component` field. This may or may not be
the same as the package name you are looking for. If you are not sure
what the source package name is, search for your desired package in the
[Fedora Packages web app](https://packages.fedoraproject.org/). Once you
locate the desired package in this app, the URL will have the following
structure:

``` console
https://packages.fedoraproject.org/pkgs/<source_package>/<package>/
```

The title of the page will be \"\<package\> Subpackage of
\<source_package\>\" if the names are different, or just \"\<package\>\"
if the names are the same. Use the source package name for the component
in the rest of this guide.

## File a bug {#file_a_bug}

Before opening a new bug report, check the existing ones to see if the
package has already been requested. Use the following URL (replacing
`<component>` with your component) to view existing open bugs.

``` console
https://bugz.fedoraproject.org/<component>
```

If there are no open requests for the EPEL version you desire, then open
a new bug at <https://bugzilla.redhat.com/enter_bug.cgi>.

:::: important
::: title
:::

Please file separate bugs for different EPEL major versions. For EPEL 8
and 9 you just need to file a bug for the major versions. For EPEL10,
please note which [EPEL minor
versions](https://docs.fedoraproject.org/en-US/epel/branches) you are
requesting in the bug description.
::::

:::: note
::: title
Bugzilla fields for an EPEL request
:::

- Classification: `Fedora`

- Product: `Fedora EPEL`

- Component: `<component>` (if the component is not found, skip to the
  next note)

- Version: `epel10` (or `epel9`, `epel8`, etc.)

- Summary: Please branch and build \<package\> in epel10 (or epel9,
  epel8, etc.)
::::

If this package has never been in EPEL before, the component will not
exist in the `Fedora EPEL` Product. You can still request the package by
using the `Fedora` Product.

:::: note
::: title
Bugzilla fields for an EPEL request (alternative)
:::

- Classification: `Fedora`

- Product: `Fedora`

- Component: `<component>`

- Version: `rawhide`

- Summary: Please branch and build \<package\> in epel10 (or epel9,
  epel8, etc.)
::::

If the component isn't found in either the `Fedora EPEL` or `Fedora`
Products, then it probably doesn't exist in Fedora and needs to be added
there first.

At this point, things change depending on your ability or willingness to
help.

### Consumers/end users {#end_users}

Clear out `Description` and put in:

``` console
Please branch and build <package> in epel10.
```

If you desire the package in the current epel10 minor version please add
that to the description as noted above.

If there is no response after a week, add the following comment in the
bug:

``` console
Will you be able to branch and build <package> in epel10?
```

If there is no action on the bug after two more weeks, send an email to
[epel-devel](https://lists.fedoraproject.org/admin/lists/epel-devel@lists.fedoraproject.org/)
asking if there are any packagers who would like to package and maintain
your package in EPEL. Be sure to include the Bugzilla URL in your email.

### Fedora/EPEL packagers {#fedora_packagers}

Clear out Description and put in:

``` console
Please branch and build <package> in epel10.

If you do not wish to maintain <package> in epel10,
or do not think you will be able to do this in a timely manner,
I would be happy to be a co-maintainer of the package (FAS <your FAS Id>);
please add me through https://src.fedoraproject.org/rpms/<package>/adduser
```

If you desire the package in the current epel10 minor version please add
that to the description as noted above.

If there is no response after a week, add the following comment in the
bug:

``` console
Will you be able to branch and build <package> in epel10?
I would be happy to be a co-maintainer if you do not wish
to build it on epel10 (FAS: <your FAS Id>).
```

If there is no action on the bug after two more weeks, follow the
[stalled EPEL request
steps](epel-package-request.xml#stalled_epel_requests), and open a
ticket with [releng](https://forge.fedoraproject.org/releng/tickets):

- Ticket Title:

  ``` console
  Stalled EPEL package: <package>
  ```

- Ticket Body:

  ``` console
  <package> has a stalled EPEL branch request.

  <bugzilla URL>

  Since this has met the time requirements as outlined in the stalled EPEL request policy,
  please grant my FAS (@<FAS of requester>) commit access to the package.

  cc: @<FAS of maintainer>
  ```

After you have been given commit permissions, you can then branch,
build, and maintain the package in epel.

## Stalled EPEL requests {#stalled_epel_requests}

There are times that an EPEL / Fedora package maintainer isn't
responding to an EPEL package request. If a different packager would
like to build and maintain that package in EPEL, these are the steps
they take.

- Anybody opens a Bugzilla bug requesting a package be added to EPEL-X.
  A packager (the Bugzilla reporter or another person) expresses that
  they are willing to help maintain / co-maintain that package in
  EPEL-X.

- A week goes by with no action.

- They re-say that they are willing to maintain / co-maintain the
  package in EPEL and set a needinfo flag for the maintainer.

  - This is in case the initial message was missed.

- Two weeks go by with no response.

- They file a [releng
  ticket](https://forge.fedoraproject.org/releng/tickets) requesting
  appropriate privileges to be able to branch and build that package in
  EPEL-X. This ticket must include a link to the bugzilla request and
  mention the maintainer's FAS account.

  - This part of the policy will adjust as various features get
    implemented in pagure and dist-git.

- The privileges are given and the packager is made the Bugzilla contact
  for EPEL.

- They then request a branch, and build the package in EPEL-X following
  normal steps.

\"Action\" is considered something that progresses the bug. \"Action\"
can be positive or negative. Such as a response of \"The code has not
been updated for 10 years and has security issues\" and then they close
the ticket. \"No Action\" could be no response at all, or it could be a
response of \"I do not want to do epel\" and then they do nothing else.

A template for these steps can be found above. :experimental:

## Communicating with EPEL {#communicating_with_epel}

There are many ways to communicate with EPEL and its members:

- The
  [epel:fedoraproject.org](https://matrix.to/#/#epel:fedoraproject.org)
  channel on offers real-time support for EPEL users and developers.

- The [#epel](https://web.libera.chat/?channels=#epel) IRC channel on
  [Libera Chat](https://libera.chat) is a secondary chat location, but
  is not bridged to Matrix.

- The
  [epel-devel](https://lists.fedoraproject.org/admin/lists/epel-devel@lists.fedoraproject.org/)
  mailing list is for general EPEL discussion. [Historic
  archives](https://www.redhat.com/archives/epel-devel-list/) are
  available.

- The
  [epel-announce](https://lists.fedoraproject.org/admin/lists/epel-announce@lists.fedoraproject.org/)
  mailing list is a low volume mailing list for only important
  announcements.

- The
  [epel-package-announce](https://lists.fedoraproject.org/admin/lists/epel-package-announce@lists.fedoraproject.org/)
  mailing list is a list that gets information about package updates as
  they happen in the stable repository.

- If you find a bug in a EPEL maintained package, please report it to
  [<https://bugzilla.redhat.com/>](https://bugzilla.redhat.com/enter_bug.cgi?product=Fedora+EPEL)
  under the \"Fedora EPEL\" product.

- Infrastructure issues (mirrors, repos, etc.) should be reported to
  [Fedora releng](https://forge.fedoraproject.org/releng/tickets).

- The EPEL Steering Committee meets on Wednesday every week in the
  [Fedora Meeting
  1](https://chat.fedoraproject.org/#/room/#meeting-1:fedoraproject.org)
  Matrix channel. The time is **not** tied to U.S. daylight savings
  time, so it is at 18:00 UTC regardless of the time of year. Please
  check the time on the [epel
  calendar](https://calendar.fedoraproject.org/epel/); sometimes it can
  change or a meeting can be skipped. Feel free to join us! Logs of past
  meetings can be viewed in
  [meetbot](https://meetbot.fedoraproject.org/sresults/?group_id=epel&type=team).

- The EPEL Steering Committee has [monthly office hours for the EPEL
  project](https://discussion.fedoraproject.org/t/join-us-for-the-epel-office-hours-every-month/37235).
  :experimental: :page-aliases: help.adoc, contribute.adoc

# Joining EPEL {#_joining_epel}

There are many ways to join in and help out with EPEL. A few are listed
below. If you think of another way to help out, feel free to bring it up
on our mailing list or at our weekly meetings.

## Maintaining packages {#_maintaining_packages}

Package Maintainers update, fix bugs and improve packages in the EPEL
collection. See the [EPEL package
maintainers](epel-package-maintainers.xml) page for more information on
roles and how to join this group.

## Testing and Quality Assurance {#_testing_and_quality_assurance}

EPEL strives to ship packages that are as stable and bug free as
possible. Testing of packages is always welcome. EPEL uses the Bodhi
updates system to manage updates. Packages enter the epel-testing
repository where they MUST spend 2 weeks or until sufficient testing is
done on them. See our [EPEL QA](epel-qa.xml) page for information on
helping with testing and quality assurance.

## Release Engineering {#_release_engineering}

EPEL Release engineering is responsible for making sure packages are
built and signed and mirrored out. Currently this group is a subset of
the Fedora Release Engineering group. See the [Fedora Release
Engineering page](https://docs.pagure.org/releng/contributing.html) for
more information. :experimental:

# EPEL Quality Assurance {#_epel_quality_assurance}

EPEL strives to produce bug free and stable packages. Testing and
Quality assurance is vital to this effort.

## Testing packages {#testing_packages}

Packages entering the EPEL collection MUST spend 2 weeks or until they
reach +3 karma in the updates system before being promoted as a stable
update. During this time they are in the
[epel-testing](epel-testing.xml) repository. Everyone is encouraged to
install and test packages from this repository and provide feedback. The
[Bodhi web interface](https://admin.fedoraproject.org/updates) is one
place to provide feedback. You can also use the \'fedora-easy-karma\'
package to quickly provide feedback on all the packages you have
installed from the epel-testing repository.

## Broken dependency reports {#broken_dependency_reports}

Running periodic reports to find and note broken dependencies is another
great way to ensure quality packages. Broken dependencies should never
appear in the stable repos.

## Noting packages that appear in both EPEL and RHEL {#noting_packages_that_appear_in_both_epel_and_rhel}

EPEL strives to never ship packages that are already available in RHEL.
Noting and removing packages that this is the case for is another great
way to help out with improving EPEL. Note that over the lifecycle of a
RHEL release, new packages are sometimes added, so an EPEL package may
start off as allowed and then need to be later removed.

## Fedora QA resources {#fedora_qa_resources}

See the [Fedora QA](https://docs.fedoraproject.org/en-US/qa-docs/) page
for information about helping with Fedora Quality. :experimental:

# EPEL packaging {#_epel_packaging}

This page contains guidelines which are not relevant or are no longer
relevant to Fedora, but still apply to EPEL packages. These guidelines
are designed to avoid conflict with the larger [Fedora Packaging
Guidelines](packaging-guidelines::index.xml), but should any conflicts
occur, these guidelines should take precedence on EPEL packages.

As a reminder, these guidelines only apply to EPEL packages, not to
Fedora packages.

## Package dependencies {#package_dependencies}

All EPEL package dependencies (build-time or runtime) MUST ALWAYS be
satisfiable within the Target Base (as defined by [EPEL
policy](epel-policy.xml#_policy)) or EPEL itself. [Weak package
dependencies](packaging-guidelines::WeakDependencies.xml) are allowed on
packages from other RHEL channels that are not part of the Target Base,
such as the HighAvailability or ResilientStorage channels. This allows
for repoclosure with only the Target Base, but allows EPEL packages to
pull in other packages via weak dependencies when additional channels
are enabled.

This does not mean that EPEL packages should incorrectly identify a
dependency as weak (e.g. changing a Requires to a Recommends). On a case
by case basis, exceptions to this policy may be granted by the EPEL
Steering Committee. To request an exception [open an
issue](https://pagure.io/epel/issues) and add the \"meeting\" tag.

## ELN

[ELN](https://docs.fedoraproject.org/en-US/eln/) is a new buildroot and
compose process for Fedora that takes Fedora Rawhide dist-git sources
and emulate a Red Hat Enterprise Linux compose. The packages included
are thus based on what is planned to be included in the next major RHEL
release, and in that way it is already useful for EPEL packagers.

[ELN Extras](https://docs.fedoraproject.org/en-US/eln/extras/), however,
is an extension that is mostly driven by EPEL packagers. Given that one
of the pain points in bootstrapping a new EPEL is in processing the
dependency graph of the packages our packagers are *actually* interested
in (whether they are a library that some in-house or ISV software needs,
or a tool) and getting them branched and built, we can use ELN Extras in
this way:

- add packages to ELN Extras\' content resolver input, e.g. [KDE
  packages](https://github.com/minimization/content-resolver-input/blob/master/configs/eln_extras_kde.yaml);
  note that this has sufficient metadata to indicate who will maintain
  such packages

- check the
  [dependencies](https://tiny.distro.builders/workload-dependencies--eln_extras_kde--fedora-empty-base--repository-fedora-eln--x86_64.html)
  pulled in

The former list is what packagers actually care about, the latter is
just what needs to be brought in.

## EPEL 8 {#epel_8}

### Scriptlets {#_scriptlets}

Fedora has been moving towards the use of file triggers and away from
requiring that packagers cut and paste scriptlets into loads of
packages. At the time of this writing, we are trying to backport all of
these to EPEL8, so that fedora packages are easily able to build on
EPEL8 without any changes. When EPEL 8 becomes old enough, that these
backports are not feasible and/or wanted, we will list them here.

## RPM macros {#_rpm_macros}

Not all macros defined in (or built into) existing Fedora packages will
work when a spec is converted for use in EPEL.
[epel-rpm-macros](https://src.fedoraproject.org/rpms/epel-rpm-macros/)
backports the newer macros and is installed by default in EPEL mock
chroots.

## Scriptlets {#_scriptlets_2}

Fedora has been moving towards the use of file triggers and away from
requiring that packagers cut and paste scriptlets into loads of
packages. These scriptlets would still be needed for EPEL, and as
scriptlets are no longer needed in any Fedora release, they're moved
here.

## Python {#_python}

The [Fedora Python Packaging
Guidelines](packaging-guidelines::Python.xml) underwent a major overhaul
in 2021. The macros used in these guidelines are also available in RHEL
9. EPEL 9 Python packages **SHOULD** use these guidelines. EPEL 9 Python
packages **MAY** use the older [201x-era Fedora Python Packaging
Guidelines](packaging-guidelines::Python_201x.xml). EPEL 8 Python
packages **MUST** use the older guidelines. New Python 2 packages
**SHOULD NOT** be added to EPEL 8, because the RHEL 8 Python 2.7
Application Stream was [retired in June
2024](https://access.redhat.com/support/policy/updates/rhel-app-streams-life-cycle).

### Automatically generated dependencies {#_automatically_generated_dependencies}

The Python run-time dependency generator mentioned in the [Fedora Python
Packaging Guidelines](packaging-guidelines::Python.xml) is enabled by
default for EPEL 8 and EPEL 9 builds.

The dependency generator in RHEL 8 is significantly limited compared to
the one in Fedora and RHEL 9. Simple dependencies and minimum/maximum
versions work correctly, but more advanced specifications such as
[environment
markers](https://peps.python.org/pep-0508/#environment-markers) and
[compatible release
clauses](https://peps.python.org/pep-0440/#compatible-release) do not.
This can lead to missing dependencies, included dependencies that should
have been skipped, or other incorrect behavior. The packager **MUST**
inspect the generated requires for correctness. If the software uses an
advanced dependency specification that does not parse correctly, the
packager **MUST** ensure the dependency is included. This can be done
either by patching the source to achieve the desired result from the
generator, or by using an explicit `Requires:` statements.
:experimental:

# EPEL packaging examples {#_epel_packaging_examples}

## Missing-but-built examples {#_missing_but_built_examples}

These examples are for the [Missing RHEL sub-packages/missing built
sub-packages/short term
policy](epel-policy-missing-sub-packages.xml#short_term).

### Missing-but-built workflow {#_missing_but_built_workflow}

This is an example workflow.

1.  `fedpkg request-repo --exception <package>-epel`

    - For example: fedpkg request-repo \--exception pycairo-epel

2.  `fedpkg request-branch --repo <package>-epel epel<version>`

    - For example: `fedpkg request-branch --repo pycairo-epel epel9`

      :::: note
      ::: title
      :::

      `request-repo` and `request-branch` can be done at the same time
      as long as `request-repo` is done first.
      ::::

3.  Wait until you get an email saying the request is done

4.  `fedpkg clone <package>-epel ; cd <package>-epel`

    - For example: `fedpkg clone pycairo-epel ; cd pycairo-epel`

5.  `fedpkg retire "For epel only, not Fedora"`

6.  `fedpkg switch-branch epel<version>`

    - For example: `fedpkg switch-branch epel9`

7.  Download the source rpm corresponding to the latest released RHEL
    build

8.  `fedpkg import <full patch to source rpm>`

    - For example: `fedpkg import /tmp/pycairo-1.20.0-4.el9.src.rpm`

9.  `fedpkg commit -m "import from CentOS Stream srpm"`

10. `git mv <package>.spec <package>-epel.spec`

    - For example: `git mv pycairo.spec pycairo-epel.spec`

11. `fedpkg commit -m "rename spec file"`

12. Edit the spec file so it builds, but only produces the missing
    binaries

13. Test build and test install your rpm, which ever way you like to do
    that

14. `fedpkg commit -m "Convert RHEL<version> <package> to <package>-epel with just <package>-devel subpackage"`

    - For example:
      `fedpkg commit -m "Convert RHEL9 pycairo to pycairo-epel with just python3-cairo-devel subpackage"`

15. `fedpkg push`

16. `fedpkg build`

17. `fedpkg update`

### Missing-but-built spec examples {#_missing_but_built_spec_examples}

These examples should help you convert your RHEL spec file to a `-epel`
spec file.

#### Header/top of spec {#_headertop_of_spec}

- State where the original spec came from, and where to look to make
  sure it is in sync.

- A variable for the original name of the package. It doesn't have to be
  `rhel_name`, but keep it consistent.

  - Do a global replacement of `%{name} to %{rhel_name}` in your spec
    file.

- Turn off debugsource.

<!-- -->

    # This spec file is derived from the RHEL9 pycairo spec file.  They should be kept
    # in sync over time.
    # https://gitlab.com/redhat/centos-stream/rpms/pycairo
    %global rhel_name pycairo
    %global _debugsource_template %{nil}

#### %prep {#_prep}

Add `-n %{rhel_name}-%{version}` to your setup. So the build doesn't
think the source is in `<package>-epel-version`.

    %prep
    %autosetup -p1 -n %{rhel_name}-%{version}

#### %package %description and %files {#_package_description_and_files}

You need to add `-n %{rhel_name}-` to each of these.

    %package -n %{rhel_name}-devel
    %description -n %{rhel_name}-devel
    %files -n %{rhel_name}-devel

#### Fix Requires: {#_fix_requires}

Most `-devel` packages have a `Requires:` equal to the
Name-Version-Release (NVR)

    %package -n %{rhel_name}-devel
    Requires: %{rhel_name}%{?_isa} = %{version}-%{release}

If this were a perfect world, you could leave your `-epel` package like
that. But it's not a perfect world, and there are many times you need to
update your `-epel` package separate from the RHEL package being
updated.

The following are two options. It is up to the `-epel` package
maintainer to decide which is right for them, or perhaps do things your
own way.

##### Remove release {#_remove_release}

If your -epel package only has some unchanging headers, you usually do
not need to keep completely in step with the RHEL release, only the
version. If that is the case, simply remove the `-%{release}` section.

    %package -n %{rhel_name}-devel
    Requires: %{rhel_name}%{?_isa} = %{version}

##### Rename release {#_rename_release}

If your `-epel` package has to be updated each time the RHEL package is
updated, no matter what, one way to do this is with a `%{rhel_release}`
that goes along with your `%{rhel_name}`. If you do this, your `-epel`
release must be less than the RHEL release.

    ...
    %global rhel_name pycairo
    %global rhel_release 4
    %global epel_release 1
    ...
    Name: %{rhel_name}-epel
    Release: 0.%{rhel_release}%{?dist}.%{epel_release}
    ...
    %package -n %{rhel_name}-devel
    Requires: %{rhel_name}%{?_isa} = %{version}-%{rhel_release}
    ...

#### ExcludeArch: (if needed) {#_excludearch_if_needed}

Some sub-packages are only missing in some arches. If that is the case,
then you should use `ExcludeArch:` to have your package only built on
those arches you care about.

    # This is only for non-x86/POWER architectures
    ExcludeArch: %{ix86} x86_64 %{power64}

#### Remove files shipped in RHEL {#_remove_files_shipped_in_rhel}

At the end of the `%install` section, remove all the files you will not
be shipping.

    %install
    %py3_install

    # remove files shipped in RHEL
    rm -rf %{buildroot}%{python3_sitearch}

#### Remove un-needed sections {#_remove_un_needed_sections}

- **Need to remove**

  - `%files`

    - Remove all the `%files` sections you will not be shipping.

    - Make sure any file listed in those sections is removed in the
      `%install` section.

- **Optional remove**

  - `%package` and `%description`

  - `%prep`, `%post`, and other scripts

  - `%check`

    - This really depends on what you are doing. If `%check` takes an
      hour, and all you need is a few headers, feel free to remove it.
      If the missing package has an actual program in it, leave it in.

    - When in doubt, leave `%check` in.

## Missing un-built examples {#_missing_un_built_examples}

These examples are for the [Missing RHEL sub-packages/missing un-built
sub-packages
policy](epel-policy-missing-sub-packages.xml#missing_un-built_sub-packages).

# EPEL package maintainers {#_epel_package_maintainers}

EPEL packages are maintained by members of the community. These
maintainers respond to bug reports, update packages and add new packages
to the collection as needed. EPEL packagers are members of the Fedora
`packagers` group.

## Joining the EPEL package maintainers {#joining_the_epel_package_maintainers}

There are several ways you can join the EPEL package maintainer group:

1.  If you are an existing Fedora package maintainer, you can maintain
    EPEL packages by becoming a maintainer or co-maintainer of an
    existing EPEL package, which you can apply for in pkgdb. You can
    also [request EPEL
    branches](epel-faq.xml#how_do_i_request_a_epel_branch_for_an_existing_fedora_package)
    for your Fedora package and maintain them for EPEL with a Package
    SCM request.

2.  If you are not currently in the Fedora packager group, you could
    join that group by submitting one or more new packages for
    Fedora/EPEL, and following the normal Fedora sponsorship process.
    Then, simply [request EPEL
    branches](epel-faq.xml#how_do_i_request_a_epel_branch_for_an_existing_fedora_package)
    for your new packages once they are approved.

3.  If you are not currently in the Fedora packager group and wish to
    help co-maintain one or more packages in EPEL, you can try and find
    an existing package and maintainer of that package who wishes to
    mentor you. You can then follow the [\"Become a co-maintainer\" path
    to
    sponsorship](package-maintainers::How_to_Get_Sponsored_into_the_Packager_Group.xml#become_a_co_maintainer).

4.  If you are an existing EPEL/Fedora maintainer and wish to maintain a
    package in EPEL that someone else maintains in Fedora, file a bug
    asking them if they would like to maintain it in EPEL, if no
    response in a week or if the Fedora maintainer has no interest in
    EPEL, follow the [stalled EPEL Request
    procedure](epel-package-request.xml#stalled_epel_requests) and
    maintain it yourself.

## EPEL policies and guidelines {#epel_policies_and_guidelines}

Where possible, EPEL tries to use and follow any applicable Fedora
guidelines. There are of course some exceptions due to older packages
and EPEL seeking stability over newer packages. You can find a list of
all such guidelines at the [EPEL Packaging
Guidelines](epel-packaging.xml) page.

## EPEL updates policy {#epel_updates_policy}

EPEL strives to provide updates that are compatible and stable to
compliment the Enterprise Linux packages it's built on. You can find a
detailed list of updates policies on the [EPEL updates policy
page](epel-policy-updates.xml) as well as [a page on incompatible
updates when they absolutely can't be
avoided](epel-policy-incompatible-upgrades.xml).

## RHEL entitlements for EPEL package maintainers {#rhel_entitlements_for_epel_package_maintainers}

Please see [this page](epel-rhel-entitlements.xml) for information about
getting a free RHEL subscription for EPEL package maintenance.

## New package wish list {#new_package_wish_list}

The best way to get a new package into EPEL is to first get it added to
Fedora. You can add such packages to the [wish list for
Fedora](https://fedoraproject.org/wiki/Package_maintainers_wishlist).

It is possible to have packages only in EPEL, for example if the
functionality has already been merged in a more recent package in
Fedora, but it should be exceptional. Such packages can be submitted for
review as per the regular process. Be ready to discuss why your package
only applies to EPEL.

If the package is in Fedora but not in EPEL, see above. :experimental:

# EPEL Packagers SIG {#_epel_packagers_sig}

## About {#epel_packagers_sig}

:::: note
::: title
This SIG is deprecated
:::

The EPEL Steering Committee has decided to deprecate this SIG. New
requests for co-maintainership should no longer request adding this SIG
to packages.
::::

EPEL Packagers SIG is a dist-git group. Being a member of that group
allows you to work with packages that have added the [epel-packagers-sig
group](https://src.fedoraproject.org/group/epel-packagers-sig) as a
collaborator on their packages. You will be able to branch, build and
work on those EPEL packages.

You do not need to be a member of the EPEL Packagers SIG to build
packages on EPEL.

[EPEL Packagers SIG
Sponsors](https://accounts.fedoraproject.org/group/epel-packagers-sig/)
are SIG members that are also on the EPEL Steering Committee.

## Why {#_why}

There is often a lag between a new Enterprise Linux release being
available, and extra packages being available for it:

- That package has to be branched and built

- The existing maintainers have to decide if they want to support the
  latest EPEL or not

- Rinse and repeat for every dependency

- Then have years of maintenance and updates for that package

Adding the epel-packagers-sig group as a collaborator for a package
gives the regular package maintainer(s) more people to maintain it over
the years. It can also help get the package into the latest version of
EPEL faster.

## Workflow {#_workflow}

We aim to be somewhere in between the language-based SIGs (e.g. the
[Python SIG](https://fedoraproject.org/wiki/SIGs/Python)) and being
\"provenpackagers for EPEL\":

- like the language-based SIG, it's opt in: if a package maintainer
  would like help maintaining their packages for EPEL, they can add
  epel-packagers-sig as co-maintainers

- SIG members can request new EPEL branches for packages they
  co-maintain

- SIG members can mark packages they co-maintain to be automatically
  branched for the next EPEL release

Existing maintainers can decide whether to give the SIG commit access
(in which case SIG members can also commit to Rawhide and Fedora
branches), or only collaborator access (with epel repos allowlisted).
Collaborator access is now sufficient to both request branches and push
updates.

Automatic branching is not implemented yet.

### Packages {#_packages}

Candidate packages for onboarding --- [NEW branch requests over two
weeks
old](https://bugzilla.redhat.com/buglist.cgi?bug_status=NEW&f1=days_elapsed&list_id=11600601&o1=greaterthan&product=Fedora&product=Fedora%20EPEL&query_format=advanced&short_desc=epel&short_desc_type=allwordssubstr&v1=14).
We should consider reviewing this periodically.

Branch requests and/or bug requests that need to be brought into the
SIG's attention should block [the EPELPackagersSIG
tracker](https://bugzilla.redhat.com/show_bug.cgi?id=EPELPackagersSIG).

See [the guidelines for stalled
requests](epel-package-request.xml#stalled_epel_requests) for follow-ups
if a branch request has been stale for at least a week.

## Joining the EPEL Packagers SIG {#_joining_the_epel_packagers_sig}

Getting added to `epel-packagers-sig` grants collective access to all
packages this group has access to, so we do need to be more careful when
adding new contributors to this group.

A candidate should be a skilled package maintainer who is experienced in
a wide variety of package types and who are familiar with the [Fedora
packaging guidelines](fesco::Package_maintainer_responsibilities.xml)
and [EPEL package maintainer policies](epel-policy.xml). They should
have been packaging with Fedora and/or EPEL for at least a year.

The procedure is similar to that for
[provenpackagers](fesco::Provenpackager_policy.xml#_becoming_provenpackager).

- File a ticket in the [EPEL issue
  tracker](https://pagure.io/epel/issues) indicating why you wish to
  become a member.

- A [Packagers SIG
  Sponsor](https://accounts.fedoraproject.org/group/epel-packagers-sig/)
  will send an e-mail to the SIG members, so they are aware about the
  ticket.

- Packagers SIG Sponsors vote in the EPEL ticket.

- You must get at least 1 positive votes from SIG Sponsor with no
  negative votes, over a one week review period, to be approved.

If you haven't been approved after one week, the EPEL Steering Committee
will vote (normal EPEL voting mechanism applies).

### Get to work {#_get_to_work}

- Look through [the general EPEL issues](https://pagure.io/epel/issues)
  related to packaging and see where you can help.

- Look through [the EPEL Packagers SIG bug
  tracker](https://bugzilla.redhat.com/show_bug.cgi?id=EPELPackagersSIG),
  see if there are any you want to help with.

- Look through [old epel
  bugs](https://bugzilla.redhat.com/buglist.cgi?bug_status=NEW&f1=days_elapsed&list_id=11600601&o1=greaterthan&product=Fedora&product=Fedora%20EPEL&query_format=advanced&short_desc=epel&short_desc_type=allwordssubstr&v1=14).
  Many of them are requesting packages. See if there are any you think
  should be added to the EPEL Packagers Sig tracker.

- Look at [the EPEL Packagers SIG
  dashboard](https://packager-dashboard.fedoraproject.org/dashboard?groups=epel-packagers-sig)
  to see if there is anything there you can do.

- Look at
  [Will-It-Install](https://tdawson.fedorapeople.org/epel/willit/status-overall.html)
  and see if there are any packages that will not install that you can
  help with.

  - [EPEL 9 packages that will not
    install](https://tdawson.fedorapeople.org/epel/willit/epel9/status-wont-install.html).

  - [EPEL 8 packages that will not
    install](https://tdawson.fedorapeople.org/epel/willit/epel8/status-wont-install.html).

See [the guidelines for stalled
requests](epel-package-request.xml#stalled_epel_requests) for follow-ups
if a branch request has been stale for at least a week.

## Communicating with the EPEL Packagers SIG {#communicating_with_the_epel_packagers_sig}

We use the same communication channels as EPEL; see [Communicating with
EPEL](epel-communication.xml) for details. :experimental:

# EPEL Next {#_epel_next}

## Introduction {#epel_next}

EPEL packages are built against RHEL. EPEL Next is an additional
repository that allows package maintainers to alternatively build
against CentOS Stream. This is sometimes necessary when CentOS Stream
contains an upcoming RHEL library rebase, or if an EPEL package has a
minimum version build requirement that is already in CentOS Stream but
not yet in RHEL. EPEL Next has its own distgit branches, koji build
targets, and bodhi releases.

EPEL Next packages have `.next` appended to the disttag (e.g. a disttag
of `.el9.next` for epel9-next) to provide an upgrade path from an EPEL
package that was built from the same distgit commit. A package
maintainer can rebuild the same commit for both EPEL and EPEL Next and
get two different NVRs in koji. Within six months, the build requirement
necessitating building in EPEL Next should be in RHEL, and at that time
the package maintainer can do a normal release bump commit in the EPEL
branch and get a newer NVR than both the previous EPEL and EPEL Next
packages.

To get started with EPEL Next, request the corresponding branch for the
EPEL release you are targeting, e.g. request an epel9-next branch to
rebuild an EPEL 9 package against CentOS Stream 9. Once the branch is
created you can merge commits from other branches and submit a build
just like you would for other EPEL or Fedora branches.

## Example workflow {#example_workflow}

The workflow for building and releasing a package in EPEL Next is
intentionally very similar to EPEL itself.

In this example, the scenario is that you have an EPEL package (built
against RHEL) that installs on RHEL, but not on CentOS Stream, due to a
dependency that was rebased in the distro which is destined for the next
minor release of RHEL. You can use EPEL Next to build a compatible
package now.

- `fedpkg request-branch epel9-next` and wait for the branch to be
  created

- `git checkout epel9-next`

- `git merge epel9`

- `git push`

- `fedpkg build`

- submit bodhi update via web interface or cli

This will result in an EPEL Next package that is the same as the
existing EPEL package, except for the `.next` suffix on the disttag and
being built against CentOS Stream 9. Your `epel9-next` branches can
diverge from the corresponding epel9 branches as needed. If an update
for your EPEL package requires a minimum version of a dependency that is
only in CentOS Stream so far, you can update in the `epel9-next` branch
first, then merge from `epel9-next` to `epel9` when the dependency is
added to the next RHEL minor release.

## FAQ {#_faq}

### How do I enable EPEL Next? {#how_do_i_enable_epel_next}

`dnf install epel-next-release`

### If I build my package in EPEL do I also need to build my package in EPEL Next? {#if_i_build_my_package_in_epel_do_i_also_need_to_build_my_package_in_epel_next}

Probably not. Due to the strong compatibility guarantees of RHEL, most
EPEL packages built against RHEL install just fine on CentOS Stream. But
there are some situations where it is necessary to rebuild an EPEL
package to get it to install on CentOS Stream, and EPEL Next exists to
provide package maintainers a place to do just that.

### Are all EPEL packages also in EPEL Next? {#are_all_epel_packages_also_in_epel_next}

No. EPEL Next is designed to be a small overlay on top of EPEL. The
epel-next-release package requires epel-release.

### Why isn't this called EPEL Stream? {#why_isnt_this_called_epel_stream}

The term stream is already massively overloaded. \"Next\" correctly
describes the purpose of the repository, which is providing packages
compatible with the next minor release of RHEL. Additionally, EPEL Next
isn't exclusively useful for CentOS Stream. It's also useful for:

- RHEL Beta releases.

- RHEL itself temporarily at minor release time when an EPEL package was
  already rebuilt for a library change in EPEL Next but hasn't been
  rebuilt in EPEL yet.

### When I request an epel9 branch, will an epel9-next branch be requested automatically? {#when_i_request_an_epel9_branch_will_an_epel9_next_branch_be_requested_automatically}

No. That is something that used to happen for [EPEL
Playground](epel-about-playground.xml). Most maintainers didn't like it.
EPEL Next is opt-in.

### Can I use EPEL Next to provide a newer version of a package than what's in EPEL? {#can_i_use_epel_next_to_provide_a_newer_version_of_a_package_than_whats_in_epel}

EPEL Next is bound by the same [guidelines and
policies](epel-policy.xml) as regular EPEL. If a version upgrade is
inappropriate for EPEL, it's inappropriate for EPEL Next. If a version
upgrade is unavoidable because of upcoming changes in RHEL, then you
must follow the [incompatible upgrades
process](epel-policy-incompatible-upgrades.xml).

### Why is the package I'm looking for in EPEL but not in EPEL Next? {#why_is_the_package_im_looking_for_in_epel_but_not_in_epel_next}

EPEL Next is **not** a complete rebuild of all EPEL packages. Most EPEL
packages already install on CentOS Stream correctly. EPEL Next is an
additional repository to be used with regular EPEL (not instead of) to
resolve the occasional compatibility issue. If you install both
epel-release and epel-next-release, \`dnf install \` should pick the
correct available package from the appropriate repository. If that
doesn't work, please file a
[bug](https://bugzilla.redhat.com/enter_bug.cgi?product=Fedora%20EPEL)
to let the maintainer know.

### How do I report a package that needs to be rebuilt in EPEL Next? {#how_do_i_report_a_package_that_needs_to_be_rebuilt_in_epel_next}

File a
[bug](https://bugzilla.redhat.com/enter_bug.cgi?product=Fedora%20EPEL)
to let the maintainer know.

### Why does epel-next-release require epel-release? {#why_does_epel_next_release_require_epel_release}

If you try to install only epel-next-release without epel-release
available, you'll see an error like this.

    Error:
    Problem: conflicting requests
    - nothing provides epel-release = 9-7.el9 needed by epel-next-release-9-7.el9.noarch from @commandline

This is because epel-next-release intentionally requires epel-release.
EPEL Next is designed to be used *with* EPEL, not as a replacement. EPEL
Next packages will often require other packages in EPEL. :experimental:

# EPEL Playground {#_epel_playground}

:::: warning
::: title
:::

**EPEL Playground was shut down in January 2022**
::::

EPEL 8 Playground was a place that developers and maintainers could
\"play around\" with updated, or changed packages in epel. EPEL
Playground never really worked out and ended up being more burden than
helpful.

If developers or maintainers want something similar to EPEL Playground
we recommend [Fedora COPR](https://copr.fedorainfracloud.org/), which
has availability for EPEL builds. :experimental:

# EPEL package maintainer generic job description {#_epel_package_maintainer_generic_job_description}

This job description is designed to be inserted into an existing job
description supplied by your employer or sponsoring organization. The
purpose of this description is to help separate the individual from the
role. In this way, you can ensure the longevity of package support
without requiring that you (and only you) are capable of maintaining the
package.

You might find this useful in cases where, for example, your employer is
using an EPEL package in their infrastructure. In such a case, it is
your duty to your employer and to Fedora to make sure that your package
lives on in case you do not.

## Generic job description {#generic_job_description}

**EPEL Package Maintainer**

This role includes maintaining one or more packages through the Fedora
Project. These packages are rebuilt in the Fedora Extra Packages for
Enterprise Linux (EPEL) repository
(<https://docs.fedoraproject.org/en-US/epel/>). The list of packages is
not specified here, because it may need to fluctuate over time, but a
list should be maintained with the group manager/project lead.

This organization is under no obligation to maintain these packages
beyond the organization's desire to do so. All responsibilities
undertaken are completely voluntary. If the organization desires to no
longer support maintaining one or more packages in the future, its only
responsibility is to follow the normal procedure to orphan a package.

In this role you are responsible for interacting with the packaging
community in Fedora, following all guidelines and procedures specified
by Fedora for building and maintaining packages, and interacting with
the upstream of your package. The upstream of a package is usually the
open source project that is producing the software being packaged. In
some cases, your own organization may be or control the upstream
project. A very important role in this position is being the conduit for
patches, fixes, and updates from upstream that resolve security
problems, fix bugs, and introduce new features.

The EPEL project synchronizes packages with specific release of Red Hat
Enterprise Linux. To maintain an EPEL package, you must help maintain
the synchronization against at least the one specific version of Red Hat
Enterprise Linux.

### Job duties {#job_duties}

- Interact with upstream

- Interact with Fedora and EPEL sub-group

- Maintain package throughout the life of the associated Enterprise
  Linux

- Provide security updates

- Be active in the appropriate packaging communities

- Follow all Fedora and EPEL guidelines, procedures, and rules
  :experimental:

# RHEL entitlements for EPEL maintainers {#_rhel_entitlements_for_epel_maintainers}

EPEL maintainers can use the free [RHEL developer
subscription](https://developers.redhat.com) to develop and test their
packages. The [mock](https://rpm-software-management.github.io/mock/)
tool includes `rhel+epel-<version>-<arch>.cfg` configuration files that
[integrate with this
subscription](https://rpm-software-management.github.io/mock/Feature-rhelchroots),
even on non-RHEL distributions such as Fedora.

An EPEL maintainer may alternatively use other RHEL-like distributions
to develop and test their packages. Mock includes several other
`<distro>+epel-<version>-<arch>.cfg` configuration files to choose from.
These distributions will have some differences from RHEL. It is the
maintainer's responsibility to ensure that their EPEL packages work on
RHEL in spite of these differences. :experimental:

# Packaging guidelines and policies for EPEL {#_packaging_guidelines_and_policies_for_epel}

The packages in EPEL follow the Fedora Packaging and Maintenance
Guidelines --- that includes, but is not limited to the [packaging
guidelines](packaging-guidelines::index.xml), the [package naming
guidelines](packaging-guidelines::index.xml#_naming), and the [package
review guidelines](packaging-guidelines::ReviewGuidelines.xml) that are
designed and maintained by the [FESCo](fesco::index.xml), and [Packaging
Committee](https://fedoraproject.org/wiki/Packaging_Committee).
EPEL-specific exceptions are documented here and in the [EPEL
packaging](epel-packaging.xml) page.

Please note that the sections \"Guidelines\" and \"Policies\" use their
names on purpose. Consider the guidelines as something that should be
followed normally, but doesn't have to if there are good reasons not
to --- please ask EPEL members in case you are in doubt if your reasons
are good. The word *policies* has a stronger meaning, and what is
written in that section should be considered rules that must always be
followed.

## Package maintenance and update policy {#package_maintenance_and_update_policy}

EPEL wants to provide a common \"look and feel\" to the users of our
repository. Thus the EPEL Steering Committee wrote this policy that
describes the regulations for package maintenance and updates in EPEL,
that are a bit more strictly regulated then they are in Fedora now.

### Digest {#_digest}

The goal is to have packages in EPEL that enhances the Enterprise Linux
distributions the packages were build against without disturbing or
replacing packages from that distribution. The packages in the
repository should, if possible, be maintained in similar ways to the
Enterprise Packages they were built against. In other words: have a
mostly stable set of packages that normally do not change at all and
only changes if there are good reasons for it --- so no \"hey, there is
a new version, it builds, let's ship it\" mentality.

### Policy {#_policy}

EPEL packages should only enhance and never disturb the Enterprise Linux
distributions they were built for. Thus packages from EPEL should never
replace packages from the target base distribution. Kernel modules are
not allowed, as they can disturb the base kernel easily.

In EPEL8 or later, it is permitted to provide an alternative non-modular
package to any package found only in a non-default RHEL module.

The Target Base for each distribution has been defined in older mailing
list discussions as the version of Red Hat Enterprise Linux that the
Koji builders have access to.

- EPEL 10's leading minor version is built against CentOS Stream 10
  repos

  - `baseos`

  - `appstream`

  - `crb`

- EPEL 10's trailing minor versions are built against Red Hat Enterprise
  Linux 10 channels

  - `rhel-10-for-*-baseos-rpms`

  - `rhel-10-for-*-appstream-rpms`

  - `codeready-builder-for-rhel-10-*-rpms`

- EPEL 9 Next is built against CentOS Stream 9 repos

  - `baseos`

  - `appstream`

  - `crb`

- EPEL 9 is built against Red Hat Enterprise Linux 9 channels

  - `rhel-9-for-*-baseos-rpms`

  - `rhel-9-for-*-appstream-rpms`

  - `codeready-builder-for-rhel-9-*-rpms`

- EPEL 8 is built against Red Hat Enterprise Linux 8 channels

  - `rhel-8-for-*-baseos-rpms`

  - `rhel-8-for-*-appstream-rpms`

  - `codeready-builder-for-rhel-8-*-rpms`

EPEL packages which are known to also exist in other RHEL channels
should keep a lower `epoch:version-release` (EVR) than the RHEL package.
This is because packages have been known to move from these other
channels into the target base channels. Keeping a lower EVR helps ensure
a smooth upgrade path.

The packages in the repository should, if possible, be maintained in
similar ways to the Enterprise Packages they were built against. In
other words: have a mostly stable set of packages that normally does not
change at all and only changes if there are good reasons for changes.
This is the spirit of a stable enterprise environment.

The changes that cant be avoided get routed into different release
trees. Only updates that fix important bugs (say: data-corruption,
security problems, really annoying bugs) go to a testing branch for a
short time period and then are pushed to the stable branch; those people
that sign and push the EPEL packages to the public repo will skim over
the list of updated packages for the stable repo to make sure that sure
the goal \"only important updates for the stable branch\" is fulfilled.

Other updates get queued up in a testing repository over time. That
repository becomes the new stable branch after 2 weeks of testing. But
even these updates should be limited to fixes only as far as possible
and should be tested in Fedora beforehand if possible. Updated Packages
that change the ABI or require config file adjustments must be avoided
if at all possible. Compat- Packages that provide the old ABI need to be
provided in the repo if there is no way around a package update that
changes the ABI. Packages in the testing repo for 2 weeks are
automatically promoted to stable. Packages with sufficient karma are
also promoted to stable. Update candidates that aren't pushed to stable
after 6 months are eligible to be removed by Release Engineering.

For more information about updating EPEL packages, including minimum
testing time for packages, refer to the [EPEL updates
policy](epel-policy-updates.xml).

## Workflow examples/information {#workflow_examples_information}

- Maintainer builds the package.

- Maintainer submits an update for testing using bodhi.

- If the update gets sufficient karma it is promoted to stable.

- After 2 weeks, if the package does not have a negative karma, bodhi
  will promote the package to stable.

- Pushes for both testing and stable take place daily.

## Guidelines and backgrounds for this policy {#guidelines_and_backgrounds_for_this_policy}

### Some examples of what package updates that are fine or not {#some_examples_of_what_package_updates_that_are_fine_or_not}

Examples hopefully help to outline how to actually apply above policy in
practise.

#### Minor version updates {#minor_version_updates}

Let's assume package foo is shipped in EPEL 8 as version 1.0.1; upstream
developers now ship 1.0.2

- build as normal, but wait at least two weeks and possibly more in
  testing.

#### A little bit bigger minor version updates {#a_little_bit_bigger_minor_version_updates}

Let's assume package foo is shipped in EPEL 8 as version 1.0.1; upstream
developers now ship 1.2.0; the ABI is compatible to 1.0.1 and the
existing config files continue to work

- build as normal, but leave in testing until there is sufficient karma
  to go to stable.

#### A yet again little bit bigger minor version updates {#a_yet_again_little_bit_bigger_minor_version_updates}

Let's assume package foo is shipped in EPEL 8 as version 1.0.1; upstream
developers now ship 1.4.0; the ABI is compatible to 1.0.1, but the
config files need manual adjustments

- build for the stable branch is normally not acceptable; a backport
  should be strongly considered if there are any serious bugs that must
  be fixed

- build for the testing branch is also disliked; but it is acceptable if
  there is no other easy way out to solve serious bugs; but the update
  and the config file adjustments need to be announced to the users
  properly --- use the epel-announce list for this.

- leave in testing if at all possible.

#### A major version update {#a_major_version_update}

Let's assume package foo is shipped in EPEL 8 as version 1.0.1; upstream
developers now ship 2.0.0; the ABI changes or the config files need
manual adjustments

- This update should be avoided if possible at all. If there really is
  no other way to fix a serious bug then follow the [incompatible
  upgrades policy](epel-policy-incompatible-upgrades.xml). In the case
  of a library package changing soname, consider shipping a compat
  package that provides the current soname at the same time you ship the
  new soname.

#### Security updates {#security_updates}

Security updates should be marked as such in bodhi and will be pushed to
stable. Because of this you should always try and make as few changes as
possible on these sorts of updates. Apply only the backported fix, or if
you must, the new version that provides only the fix. Try and avoid
pushing other changes with a security update.

## Add more examples as they show up {#add_more_examples_as_they_show_up}

If too many show up, put them into a separate document.

## Still unsure if a package is fine for EPEL? {#still_unsure_if_a_package_is_fine_for_epel}

Just ask on [epel-devel mailing list or #epel IRC
channel](epel-communication.xml) for opinions from EPEL members.

## Why not a rolling release with latest packages like what was in Fedora Extras? {#why_not_a_rolling_release_with_latest_packages_like_what_was_in_fedora_extras}

Why should we? That would be what Fedora Extras did and worked and works
well for it --- but that's mainly because Fedora (Core) has lots of
updates and a nearly rolling-release scheme/quick release cycle, too.
But the Enterprise Linux we build against is much more careful with
updates and has longer life-cycle; thus we should do the same for EPEL,
as most users will properly prefer it that way, as they chose a stable
distro for some reasons --- if they want the latest packages they might
have chosen Fedora.

Sure, there are lots of areas where having a mix of a stable base and a
set of quite new packages on top of it is wanted. **Maybe** the EPEL
project will provide a solution (in parallel to the carefully updated
repository!) for those cases in the long term, but not for the start.
There are already third party repositories out there that provide
something in this direction, so users might be served by them already.

Further: A rolling release scheme like Fedora Extras did is not possible
for many EPEL packages for another reason, new packages often require
new versions of certain core libraries. This will cause problems in EPEL
because we won't be able to provide updated libs as it would replace
libraries in the core OS.

Example: This document was written round about when RHEL5 got released;
many packages that get build for RHEL5 can't be build for RHEL4 at this
point of time already, as the RHEL4-gtk2-Package is two years old and is
too old for many current applications, as they depend on a newer gtk2.
So if even if we would try to have a rolling scheme with quite new
package we'd fail, as we can't build a bunch of package due to this
dependencies on libs; in the end we would have a repo with some quite
new packages while others are still quite old. That mix wouldn't make
either of the \"latest versions\" or \"careful updates only\" sides
happy; so we try to target the \"careful updates only\" sides. Remember,
EPEL's support and updates cycle is much longer then Fedora's.

## Distribution specific guidelines {#distribution_specific_guidelines}

The [Fedora Packaging Guidelines](packaging-guidelines::index.xml) are
written for current Fedora releases. Sometimes there are changes in
Fedora that cause the packaging guidelines there to not make sense for
the older software being run in RHEL. When that occurs, we document the
differences with the Fedora Packaging Guidelines on the [EPEL
packaging](epel-packaging.xml) page.

## Policy for conflicting packages {#policy_for_conflicting_packages}

[Per RHEL release package conflict channel
exclusions](epel-faq.xml#does_epel_replace_packages_provided_within_red_hat_enterprise_linux)

- EPEL packages must not conflict with packages in the target base of
  RHEL. See above link for a complete list of channels per RHEL Release
  that EPEL does not conflict with. This includes source package names
  due to the way that koji deals with packages from external
  repositories.

- As an exception to the above rule, devel packages in EPEL that are
  alternate versions of devel packages in RHEL (i.e. compat packages)
  are allowed to conflict with each other. See the section about
  [conflicts in compat
  packages](epel-policy.xml#conflicts_in_compat_packages) for more
  details.

- EPEL packages can conflict with packages in other RHEL channels
  outside of the target base.

- EPEL maintainers should be open to communication from RHEL maintainers
  and try and accommodate them by not shipping specific packages, or by
  adjusting the package in EPEL to better handle a conflicting package
  in a channel on a case by case basis.

When a package is added to RHEL for that is already in EPEL, it usually
needs to be removed from EPEL. Please follow the [retirement
process](package-maintainers::Package_Retirement_Process.xml) to do
this. If the package is only available for a subset of all
architectures, it might still be possible to keep the package in EPEL as
described in the [EPEL packaging
guidelines](epel-packaging.xml#limited_arch_packages).

## Conflicts in compat packages {#conflicts_in_compat_packages}

Due to the EPEL policy of maintaining backwards compatibility, EPEL has
a greater need for forward compat (i.e. newer alternate version)
packages than Fedora. There may also be cases where backwards compat
(i.e. older alternate version) packages are needed. When creating a
compat package, note that it is okay to set a Conflicts between them as
noted in the [Fedora conflicts
guidelines](packaging-guidelines::Conflicts.xml#_compat_package_conflicts).
This is allowed both between EPEL packages and between EPEL and RHEL
packages. The latter is an explicit exception to the general rule for
EPEL packages to not conflict with target base RHEL packages.

## Policy for `-epel` suffixed packages {#policy_for_epel_suffixed_packages}

The `-epel` suffix on package names is reserved for EPEL-only packages
that provide [missing RHEL
subpackages](epel-policy-missing-sub-packages.xml). Any other use of the
`-epel` suffix requires an explict exception from the [EPEL Steering
Committee](epel-policy-steering-committee.xml).

## Policy for orphan and retired packages {#policy_for_orphan_and_retired_packages}

EPEL follows the [Fedora policy for orphan and retired
packages](fesco::Policy_for_orphan_and_retired_packages.xml).

Unretiring an EPEL-only package requires a re-review.

No re-review is required to unretire an EPEL branch if the package is
still in Fedora.

## Policy for end-of-life releases {#policy_for_end_of_life_releases}

When a RHEL release reaches the end of the [Maintenance Support
phase](https://access.redhat.com/support/policy/updates/errata#Life_Cycle_Dates),
the corresponding EPEL release also goes end-of-life. On the day
maintenance support ends for the RHEL release, Koji build targets are
removed, and it is no longer possible to build or distribute new EPEL
packages for that release. A short time after that, the now end-of-life
EPEL repository is archived, and MirrorManager is adjusted to serve that
repository from the archives.

For EPEL releases with minor versions (e.g. EPEL 10) the process is
similar. When a new RHEL minor version is released, the branch
associated to the previous minor release goes end-of-life. This means
that it should go through the same retirement process. The final minor
release will be active until the end of overall EPEL major release.

## Upgrade path policy {#upgrade_path_policy}

Similar to
[Fedora](fesco::Package_maintainer_responsibilities.xml#_miscellaneous_items),
EPEL packages **SHOULD** have a valid upgrade path between EPEL major
versions.

- EPEL 8 → EPEL 9 → EPEL 10.\*

This involves setting the `Version:` and `Release:` tags as appropriate
in spec files, as well as the `Epoch:` tag if necessary. More
information about these tags can be found in the [Fedora versioning
guidelines](packaging-guidelines::Versioning.xml).

For EPEL releases with minor versions (e.g. EPEL 10), EPEL packages
**MUST** have a valid upgrade path between EPEL minor versions of the
same major version.

- EPEL 10.0 → EPEL 10.1 → EPEL 10.2

A simple way to achieve this is to push changes to the leading branch
(e.g. epel10) first, and then selectively fast-forward merge or
cherry-pick commits to trailing branches (e.g. epel10.0, epel10.1) if
needed. Diverging from this pattern is allowed but discouraged, as it
can easily lead to upgrade path issues and prevent users from getting
necessary updates. :experimental:

# EPEL branches {#_epel_branches}

Fedora and EPEL package sources are maintained in [Fedora's
dist-git](https://src.fedoraproject.org). The default branch is
`rawhide`, corresponding to [Fedora Rawhide](releases::rawhide.xml).
Additional branches are used for other Fedora and EPEL releases.

The rest of this page will describe the specific branches that are used
for EPEL packages. The general mechanics of working with dist-git
branches is covered in greater detail in the [Package Maintenance
Guide](package-maintainers::Package_Maintenance_Guide.xml#working_with_branches).

## EPEL 10 {#_epel_10}

EPEL 10 has separate dnf repositories and dist-git branches for each
minor version of RHEL 10.

### epel10 {#_epel10}

The `epel10` branch is used to create builds for the leading EPEL 10
minor version repository. Prior to the CentOS Stream 10 end of life
(which corresponds to the end of the RHEL 10 [Full Support
Phase](https://access.redhat.com/support/policy/updates/errata#Life_Cycle_Dates)),
these builds are built against external repositories of the matching
major version of CentOS Stream 10.

- CentOS Stream 10 BaseOS

- CentOS Stream 10 AppStream

- CentOS Stream 10 CRB

These builds will indicate the minor version they are targeting in their
[dist tag](packaging-guidelines::DistTag.xml) using the format of
`.el10_x`, where `x` is the minor version. They are published in the
`pub/epel/10` dnf repository for consumption by CentOS Stream 10, which
is a symbolic link to the latest `pub/epel/10.x` dnf repository.

After the CentOS Stream 10 end of life (which corresponds to the
beginning of the RHEL 10 [Maintenance Support
Phase](https://access.redhat.com/support/policy/updates/errata#Life_Cycle_Dates)),
these builds are built against external repositories of the final minor
version of RHEL 10.

- RHEL 10.10 BaseOS

- RHEL 10.10 AppStream

- RHEL 10.10 CRB

### epel10.x {#_epel10_x}

The `epel10.x` branches (where `x` is the minor version, e.g.
`epel10.0`) are used to create builds for the trailing EPEL 10 minor
version repositories. These builds are built against external
repositories of the matching minor version of RHEL 10.

- RHEL 10.x BaseOS

- RHEL 10.x AppStream

- RHEL 10.x CRB

These builds will indicate the minor version they are targeting in their
[dist tag](packaging-guidelines::DistTag.xml) using the format of
`.el10_x`, where `x` is the minor version. They are published in
`pub/epel/10.x` dnf repositories for consumption by the corresponding
RHEL 10 minor version.

### minor branch lifetime {#_minor_branch_lifetime}

Each epel10.x branch lifetime depends on its corresponding RHEL 10 minor
development and release process.

Before CentOS 10 starts receiving changes corresponding to a new RHEL
minor release, a new epel10.x+1 branch is created by cloning the
packages of the current active epel10.x branch. During this period, new
builds against the epel10 branch will start landing in the new
epel10.x+1 tag to become candidates for the new epel10.x+1 Bodhi
release. New updates on the epel10.x branch are built against a CentOS
10 snapshot until its corresponding RHEL 10 minor release is available.

When a RHEL10 minor version stops being the leading release, its
corresponding epel10.x branch goes end-of-life. This means that new
package builds won't be accepted and its contents will be archived.

Exceptions to this are the first minor branch, which is made arround the
CentOS 10 release, and the one associated to the last RHEL minor
release, which follows the regular EPEL branch lifetime policies.

## EPEL 9 {#_epel_9}

EPEL 9 has two dnf repositories and dist-git branches.

### epel9 {#_epel9}

The `epel9` branch is used to create builds for the EPEL 9 repository.
These builds are built against external repositories of the matching
major version of RHEL 9.

- RHEL 9 BaseOS

- RHEL 9 AppStream

- RHEL 9 CRB

They are published in the `pub/epel/9` dnf repository for consumption by
both RHEL 9 and CentOS Stream 9. EPEL 9 has no connection to RHEL 9
minor versions, and is always built against the current RHEL 9 minor
version.

### epel9-next {#_epel9_next}

The `epel9-next` branch is used to create builds for the EPEL 9 Next
repository. These builds are built against external repositories of the
matching major version of CentOS Stream 9.

- CentOS Stream 9 BaseOS

- CentOS Stream 9 AppStream

- CentOS Stream 9 CRB

They are published in the `pub/epel/next/9` dnf repository for
consumption by CentOS Stream 9.

`epel9-next` branches are optional, and maintainers usually do not need
to create them. You can read more about EPEL 9 Next and when it is
needed [here](epel-about-next.xml).

## EPEL 8 {#_epel_8}

EPEL 8 has a single dnf repository and dist-git branch.

### epel8 {#_epel8}

The `epel8` branch is used to create builds for the EPEL 8 repository.
These builds are built against external repositories of the matching
major version of RHEL 8.

- RHEL 8 BaseOS

- RHEL 8 AppStream

- RHEL 8 CRB

They are published in the `pub/epel/8` dnf repository for consumption by
RHEL 8. EPEL 8 has no connection to RHEL 8 minor versions, and is always
built against the current RHEL 8 minor version. :experimental:

# EPEL updates policy {#_epel_updates_policy}

This document describes the policy for updates to packages in the EPEL
package collection. For general EPEL package guidelines, refer to the
[EPEL guidelines and policy](epel-policy.xml) page.

## Stable releases {#stable_releases}

- All updates MUST spend at least 1 week in the testing repository, or
  +3 karma from testers.

- All updates should strive to avoid situations that require manual
  intervention to keep the package functioning after update.

- Major updates with changes to user experience are to be avoided. If
  they cannot be avoided, the [EPEL incompatible upgrades
  policy](epel-policy-incompatible-upgrades.xml) MUST be followed. This
  includes two separate announcements to the epel-announce mailing list.

- When new packages enter the Enterprise Linux distribution that is
  already available in EPEL, that package will be marked dead.package
  and blocked in pkgdb and koji.

## Exceptions {#_exceptions}

In some rare cases, exceptions will need to be made. Bring your case
before the EPEL Steering Committee at one of the weekly meetings and/or
the mailing list. Possibly grounds for exception might include:

- Serious security issue that cannot be backported to the existing
  version, so a new major version is required.

- Serious bugs that cannot be fixed in the existing version.

In cases of major disruption, EPEL updates will looked to be done along
with Red Hat Enterprise Linux minor releases (8.1, 8.2, 8.3) so as to
allow for longer testing or differing beta testing. :experimental:

# Incompatible upgrades policy {#_incompatible_upgrades_policy}

## Background {#incompatible_upgrades_policy}

Incompatible version upgrades in EPEL are to be avoided. However, in
certain situations, they are unavoidable. An example of such a situation
would be a security update that is difficult/impossible to backport.
This policy aims to both discourage incompatible upgrades for trivial
reasons, while allowing them for security updates where the version of
the software in question is no longer maintained upstream and the
maintainer is unable to backport just the security fix.

## Process for incompatible upgrades {#process_for_incompatible_upgrades}

1.  Send e-mail to
    [epel-devel](lists.fedoraproject.org/archives/list/epel-devel@lists.fedoraproject.org/)
    with details of the proposed upgrade. Include items such as the CVE
    of the security issue to be fixed, and/or an upstream bug tracker
    reference (if applicable). Also reference a bug in
    [Bugzilla](epel-communication.xml) against the package.

2.  In the case of a critical CVE the maintainer **MAY** build the
    package and submit it to bodhi for testing. \'Auto-request stable?\'
    **MUST NOT** be checked.

3.  File an [EPEL issue](https://pagure.io/epel/issues). This can be
    done while discussion is ongoing; please link to the thread in the
    mailing list archive so the EPEL Steering Committee can monitor the
    discussion and know when it is ready to be discussed.

4.  After a week of mailing list discussion, an EPEL Steering Committee
    member will add the meeting tag and the issue will be discussed at
    the next weekly meeting.

5.  If a majority of Steering Committee members present at the EPEL
    meeting concur, the incompatible upgrade can be built, if it has not
    been already.

6.  At the same time that the update is submitted to bodhi for testing,
    the maintainer is responsible for sending e-mail to epel-announce
    announcing the incompatible upgrade and specific actions that users
    must take in order to continue using the software.

7.  Package MUST remain in testing for at least 1 week, regardless of
    received karma. In bodhi, \'Auto-request stable?\' **MUST NOT** be
    checked.

8.  When pushing the package to stable, the maintainer **MUST** send
    another e-mail to epel-announce.

## Procedure for other packages {#procedure_for_other_packages}

For other - non-security - incompatible updates, the maintainer **MUST
NOT** push those types of changes. Consider shipping an alternatively
named new package (e.g. foo2) to provide the newer version.

## Discussion points {#discussion_points}

1.  Approval process - majority of those present seems to be lax, but
    being there's no body such as FESCo in \"charge\" of EPEL (yes, I
    realize that FESCo has oversight, but oversight != make day-to-day
    decisions such as these), I'm not sure what else to put there.

2.  How to enforce the mail to epel-announce? Maybe have the chair of
    the EPEL meeting send it? :experimental:

# Retirement policy {#_retirement_policy}

## Background {#retirement_policy}

There are three reasons for retiring a package in EPEL.

- The package is now included in RHEL.

- Security reasons.

- Maintainer no longer has time and/or desire.

## Process: Package in RHEL {#process_package_in_rhel}

If a package is in RHEL, you should have received a bug telling you your
package is going to be in RHEL. It should also say which RHEL release it
will be in (e.g. RHEL 8.8).

**Do not remove your EPEL package until you have verified that it is in
RHEL.**

- If the package version in RHEL is older than the version in EPEL, send
  an e-mail to
  [epel-devel](https://lists.fedoraproject.org/archives/list/epel-devel@lists.fedoraproject.org/),
  documenting the potential loss of functionality. If the package
  version in RHEL is the same or newer, sending the e-mail is optional

- Once your package is in RHEL, you should [retire the package from
  EPEL](https://docs.fedoraproject.org/en-US/package-maintainers/Package_Retirement_Process/#_procedure).

  - fedpkg switch-branch epel8 (or whichever epel branch is correct)

  - fedpkg retire \"REASON FOR RETIREMENT\"

## Process: Security reasons {#process_security_reasons}

If a package has a severe security issue, and the fix cannot be
backported, usually this can be fixed [with an incompatible
upgrade](epel-policy-incompatible-upgrades.xml#process_for_incompatible_upgrades).
If the EPEL version is fairly old, and a newer version cannot be built,
it's possible that the only choice of action is to remove the package.

1.  Send e-mail to
    [epel-devel](https://lists.fedoraproject.org/archives/list/epel-devel@lists.fedoraproject.org/)
    with details of the proposed retirement. Include items such as the
    CVE of the security issues affecting the existing version, and/or an
    upstream bug tracker reference (if applicable). Also reference a bug
    in [Bugzilla](epel-communication.xml) against the package.

2.  Discussion takes place on epel-devel for a minimum period of 1 week,
    unless this is for a critical security update such as remote root.

3.  The maintainer is then responsible for sending an e-mail to
    epel-announce. It should announce the retirement and specific
    actions that users must take in order to continue using the software
    (e.g. install using `pip` or some other delivery mechanism).

4.  [Retire the package from
    EPEL](https://docs.fedoraproject.org/en-US/package-maintainers/Package_Retirement_Process/#_procedure).

    - `fedpkg switch-branch epel8` (or whichever epel branch is correct)

    - `fedpkg retire "REASON FOR RETIREMENT"`

## Process: No time or desire {#process_no_time_or_desire}

EPEL is run and maintained by many volunteers. A person's life, job, and
priorities change over time. It is natural that a time might come that
you no longer have the time or desire to maintain a package.

1.  Check if there are other maintainers of the package.
    [<https://src.fedoraproject.org/rpms/package>](https://src.fedoraproject.org/rpms/nedit)
    If there are, ask them if they would like to maintain the epel
    branches.

2.  If none of the other maintainers want to maintain the epel branches,
    send an e-mail to
    [epel-devel](https://lists.fedoraproject.org/archives/list/epel-devel@lists.fedoraproject.org/).
    Let us know you cannot maintain the package anymore, and none of the
    other maintainers can either. If there is anything special about the
    package, or urgent issues such as the package not being installable,
    let us know that as well.

3.  After two weeks, If nobody has volunteered to take over the package
    for you, send an e-mail to epel-announce. It should announce the
    retirement and specific actions that users must take in order to
    continue using the software (e.g. install using `pip` or some other
    delivery mechanism).

4.  [Retire the package from
    EPEL](https://docs.fedoraproject.org/en-US/package-maintainers/Package_Retirement_Process/#_procedure).

    - `fedpkg switch-branch epel8` (or whichever epel branch is correct)

    - `fedpkg retire "REASON FOR RETIREMENT"`

## Process: Not installable {#process_not_installable}

There are times that packages are not installable in EPEL. These
packages fall into two categories. Packages that once were installable,
but no longer are. Packages that were never installable.

### Process: Once installable {#process_once_installable}

If a package was once installable, but no longer is, try to fix the
problem. If you cannot, or you do not have the time or desire to fix it,
follow the [No Time or Desire
policy](https://docs.fedoraproject.org/en-US/epel/epel-policy-retirement/#process_no_time_or_desire)

### Process: Never installable {#process_never_installable}

If a package was never installable in an EPEL repo, try to fix the
problem. If you cannot fix the problem and wish to retire the package
from that EPEL branch / repo, you can.

1.  [Retire the package from
    EPEL](https://docs.fedoraproject.org/en-US/package-maintainers/Package_Retirement_Process/#_procedure).

    - `fedpkg switch-branch epel8` (or whichever epel branch is correct)

    - `fedpkg retire "REASON FOR RETIREMENT"` :experimental:

# Regarding EPEL and Software Collections {#_regarding_epel_and_software_collections}

## Background {#_background}

RHEL comes with the `scl-utils` and `scl-utils-build` packages --- which
contain tools for using and building SCLs. These packages appear to
function as expected with RHEL and CentOS Stream.

## Recommendations {#_recommendations}

EPEL will not provide SCL support, although it will not prohibit use of
the SCL tools provided with RHEL.

EPEL will not provide any SCLs.

For use cases that require the parallel installation of multiple
versions of the same component, EPEL recommends the same solution as
Fedora in the [Fedora Packaging
Guidelines](https://docs.fedoraproject.org/en-US/packaging-guidelines/Naming/#multiple).
:experimental:

# Missing RHEL sub-packages {#_missing_rhel_sub_packages}

When a RHEL source package is built, it often creates more than one
binary package. These extra packages are generally called sub-packages.

Sometimes RHEL sub-packages that are built are not published. Sometimes
packages are built for all arches, but only published on one or two
arches. We call these two types \"missing built sub-packages\".

Sometimes when a RHEL source package is built, it does not create all
the sub-packages that it potentially could. We call these types
\"missing un-built sub-packages\".

EPEL cannot have a package with the same name as a source or binary
package published in RHEL. To solve the problem of missing built and
un-built sub-packages, the following policy and procedures have been
setup.

## Shared guidelines {#shared_guidelines}

- You MUST name your source package `<package>-epel` per the [policy for
  `-epel` suffixed
  packages](epel-policy.xml#policy_for_epel_suffixed_packages)

- You MUST NOT conflict with any RHEL packages or files

## Missing built sub-packages {#missing_built_sub-packages}

### Short term {#short_term}

Create an EPEL package that only has the missing packages, or missing
arches.

- Be prepared to maintain this package as long as it is needed.

  - It is recommended that you add the epel-packagers-sig group as a
    co-maintainer.

- A package review is not required, but it is a good idea to have
  someone look at the updated spec file.

- If you need help building this, ask for help. We have [some
  examples](epel-packaging-examples.xml#_missing_but_built_examples).

- It qualifies for an exception to the package review process so you can
  request the repo with.

  - `fedpkg request-repo --exception <package>-epel`

- Once the repo is created, you must retire the rawhide branch to make
  it clear that this is an EPEL-only package and shouldn't be branched
  for future Fedora releases.

  - `fedpkg retire 'EPEL-only package'`

- When/If the missing package(s) are added to RHEL CRB, retire your
  -epel package following the [EPEL retirement
  policy](epel-policy-retirement.xml#process_package_in_rhel).

[Short term examples and
workflow](epel-packaging-examples.xml#_missing_but_built_examples)

### Long term {#long_term}

Request the package be added to the appropriate RHEL CRB repository.

- To initiate this process, please file an issue in
  link:https://issues.redhat.com and request it be added to RHEL. Report
  the bug against the RHEL project, assign it to the proper CentOS
  Stream versions, and add the source package name in the Component
  field. More details on this can be found in the [CentOS contributor
  guide](https://docs.centos.org/en-US/stream-contrib/quickstart/#_1_file_an_issue).

- Be sure to say that it is impacting an EPEL build, and which package
  it is impacting.

``` console
Please add <sub-package> to CRB in RHEL9

I am building <my package> in EPEL9.
<my package> requires <sub-package> to build in EPEL9.

(Optional)
<my package> is important because these other packages depend on it:
<other packages>

(Optional)
<my package> is important because <my company> uses it for <reason>
```

In the past, the default answer for a request like this was \"no\". But
in mid-2021 the RHEL policy changed to allow the RHEL package maintainer
to make the decision. There are still packages where the answer might be
\"no\", but many maintainers are choosing to add the sub-packages to the
RHEL CRB repo.

## Missing un-built sub-packages {#missing_un-built_sub-packages}

You can create packages that supply missing sub-packages that were not
built in RHEL but are built in Fedora.

In the past these were named \<package\>-extra, but these are now named
`<package>-epel` to avoid confusion.

[Missing but un-built
examples](epel-packaging-examples.xml#_missing_un_built_examples)
:experimental:

# EPEL Steering Committee {#_epel_steering_committee}

## Background {#Background}

The EPEL Steering Committee was formed in 2007 by FESCo as a governing
body for EPEL. The original committee consisted of 7 members who
invested the most time and work for the original EPEL idea. In late 2014
the committee was revived with just 5 members, who were doing the most
work at the time. In 2021 the committee was expanded back to 7. The new
positions going to those members who were most active in the committee
meetings. In 2023 the committee decided that members would be elected.
The first election of committee members is planned for the spring of
2024.

## Committee Members {#committee_members}

### Current Committee Members {#current_committee_members}

- Kevin Fenzi (nirik) - Start: February 2007

- Troy Dawson (tdawson) - Start: October 2020

- Carl George (carlwgeorge) - Start: October 2020

- Davide Cavalca (dcavalca) - Start: June 2021

- Neal Gompa (ngompa) - Start: June 2021

- Jonathan Wright (jonathanspw) - Start: June 2024

- Robby Callicotte (rcallicotte) - Start: June 2025

### Past Committee Members {#past_committee_members}

- Michel Lind (salimma) - Start: June 2021 End: June 2025

- Pablo Greco (pgreco) - Start: February 2019 End: June 2024

- Brian Stinson (bstinson) - Start: December 2014 End: June 2021

- Jim Perrin (jperrin) - Start: December 2014 End: October 2020

- Stephen J Smoogen (smooge) - Start: February 2008 End: October 2020

- Anssi Johansson (avij) - Start: April 2015 End: February 2019

- Dennis Gilmore (ausil) - Start: February 2007 End: February 2019

- Mike McGrath (mmcgrath) - Start: February 2007 End: December 2014

- Michael Stahnke (stahnma) - Start: February 2007 End: December 2014

- Xavier Lamien (SmootherFrOgZ) - Start: February 2007 End: December
  2014

- Andy Gospodarek (Gospo) - Start: February 2007 End: December 2014

- Jeff Sheltren (Jeff_S) - Start: February 2007 End: December 2014

- Karsten Wade (quaid) - Start: February 2007 End: December 2014

- Thorsten Leemhuis - Start: February 2007 End: February 2008

### Committee member selection {#committee_member_selection}

From EPEL's beginning (2007) until 2024, committee members were based on
the most active members when new seats needed to be filled. Starting in
2024, Steering Committee members will be elected for two year terms.
EPEL Streeing Committee elections will be part of the [Fedora elections
process](docs.fedoraproject.org/en-US/program_management/elections/).
EPEL committee elections will occur during the first Fedora election
cycle of a calendar year.

## Committee chair {#committee_members}

### Current committee members {#committee_chair_history}

- Troy Dawson (tdawson ) Start: October 2020

- Stephen J Smoogen ( smooge ) Start: February 2008 End: October 2020

- Thorsten Leemhuis - Start: February 2007 End: February 2008

### Committee chair selection {#committee_chair_selection}

From EPEL's beginning (2007) until 2024 the committee chair was a
committee volunteer who stayed as chair until they stepped down.
Starting in 2024, the committee chair will be elected each year, by the
committee, after the committee elections.

## Committee meeting {#committee_meeting}

The place and time for the EPEL Steering Committee meeting can be found
in the [Communicating with EPEL](epel-communication.xml) section of our
documentation

The meeting is public and everyone is invited.

### Committee meeting voting {#committee_meeting_voting}

The EPEL Steering Committee tracks ongoing decisions using the [EPEL
ticketing system](https://pagure.io/epel/issues). Decisions are voted on
at the weekly Steering Committee meeting. These decisions usually fall
into one of these categories:

- tickets asking for a change in EPEL policy

- tickets asking for an exception to EPEL policy

- tickets requesting approval for an [incompatible
  upgrade](https://docs.fedoraproject.org/en-US/epel/epel-policy-incompatible-upgrades/)

Eligible voters are all currently-serving members of the Steering
Committee. If a member is unable to attend a meeting, they may relay
their vote through another member.

An official vote must be one of `+1`, `0`, `-1`:

- `+1` - I am in favor of the proposal as currently written.

- `0` - I am removing myself from the list of voters required for
  majority for this proposal.

- `-1` - I am opposed to the proposal as currently written.

A vote of `0` reduces the denominator of the fraction required to
achieve the 51% majority. In effect, it says \"I am agreeing to vote
with the remaining majority, whatever they decide.\"

If a vote achieves a 51% majority of eligible voters, regardless of
their attendance at the meeting and accounting for any explicit `0`
votes, in favor of a proposal, that proposal is accepted.

If a vote fails to achieve a 51% majority of eligible voters, regardless
of their attendance at the meeting and accounting for any explicit `0`
votes, that proposal is rejected.

After the meeting where the proposal is voted on, a member of the
Steering Committee will update the ticket with the results of the vote.
If the proposal was approved, it may proceed with implementation.

If a matter is urgent, the proposer can request a vote within the ticket
before the next meeting. Steering Committee members will record their
votes as comments in the ticket.

Decisions made by the EPEL Steering Committee may be re-discussed in
FESCo meetings, if necessary. FESCo retains authority over EPEL Steering
Committee decisions and can exercise a veto on a voted-upon topic.
:experimental:

# About EPEL {#_about_epel}

EPEL was started because many Fedora contributors wanted to use the
Fedora packages they maintain on Red Hat Enterprise Linux (RHEL) and its
compatible derivatives.

## Goals of the EPEL effort {#goals_of_the_epel_effort}

Make high quality packages that have been developed, tested, and
improved in Fedora available for RHEL and compatible derivatives such as
Alma and Rocky Linux.

Work closely with the Fedora Project to achieve this goal --- use the
same guidelines, rules, policies, and infrastructure, as far as
possible.

If we hit problems, solve the problems with the other parties and groups
of Fedora, such as Packaging Committee, instead of creating EPEL-only
solutions; EPEL-only solutions introduce confusion for packagers and
users, and make porting packages between Fedora and EPEL harder.

For the rare cases where it is not possible or desired to remain
synchronized with Fedora, maintain add-on documents for EPEL that
describe the differences and the reasons for them.

## Who needs these packages {#who_needs_these_packages}

### Enterprise Linux user/administrator perspective {#enterprise_linux_useradministrator_perspective}

Every user and admin has experienced at least one desired package not
being included and supported in RHEL. This project gives you a place to
promote, support, and benefit from packages that exist in Fedora and
were not included in a RHEL version.

Whether it is a package your company needs as part of its standard
install, or software you want available so you and your users can do
your work and have your fun, Fedora enterprise packages are a good
method to build support and community around particular software needs.

### Community perspective {#community_perspective}

Many members of the Fedora community are also users/administrators of
Enterprise Linux distributions that are derived from Fedora, such as
CentOS Stream and RHEL. Everyone has their own reasons for promoting a
particular piece of software. EPEL packages are the best way to gain
users and support from Enterprise Linux users.

### ISV/IHV perspective {#isvihv_perspective}

The benefits of building upon EPEL as an ISV or IHV have great
potential. If your software package currently packages its own copies of
open source libraries or well-known tools, you can rely upon EPEL to
provide those packages. For example, Perl modules are often needed and
repackaged, yet can be available through EPEL instead. You let
dependencies be met by EPEL, and your team concentrates on what they do
best: develop, support, and provide your product(s).

Additionally, if you are on an ISV/IHV team that utilizes open source
software packages to deliver your products, you have the opportunity to
contribute to EPEL. This ensures a community of support, review, and
testing for packages that your customers depend on for your products.

For independent software and hardware vendors, this is how you get your
software into the enterprise ecosystem:

1.  Use the Fedora process to get your favorite software in to the
    repository:

    - Get an entirely new package into Fedora.

    - Become a co-maintainer for the package you want to have
      enterprise-level longevity.

    - Package a free and open source library or other shareable software
      source to build a community around your applications.

2.  Gain the additional six to twelve months of Fedora testing and
    feedback.

3.  Be ready for RHEL beta testing before the alpha snapshot is taken,
    gaining another three to six months lead time.

4.  Ship your enterprise-ready version with the RHEL GA.

5.  Ongoing support and package maintenance is a part of your free and
    open source development process, along with advancing the technology
    in parallel in Fedora.

## Academia perspective {#academia_perspective}

Aside from the usual need for software that wasn't included in RHEL,
there is a large opportunity for academia to provide students with
learning opportunities beyond piecemeal open source project experience.

Where a typical free and open source learning experience for a student
might be to dive into coding or documentation, Fedora enterprise
packaging is one way to gain cross-over experience. The real-world,
hands-on experience includes supporting a free and open source community
and user base, creating an enterprise community around the software, and
managing feature enhancements, bug fixes, and security updates across
all communities.

## Red Hat perspective {#red_hat_perspective}

This is a simple imagination exercise.

\'\'Imagine you are a company that enables a large, fully open and free
Linux based distribution for the general world communities (cf. Fedora),
while supporting a large, fully open Linux based distribution for its
customers (cf. RHEL).

Imagine that what is in your enterprise distribution is what you think
you can support for your customers, and is influenced by what those
customers are asking for. Would it be in your best interest, or the best
interest of your customers, to pull in every single software package you
possibly could? Would you be able to provide QA and support on such a
large package set?

Imagine that it is easier to pick your package set (the ones you
support), and to enable the promotion and community support of
enterprise-quality packages.

If you look around, you see that people have put in great effort to
provide these packages that did not make it into RHEL. The Fedora
enterprise packages are a way of enabling, growing, and honoring the
work that has come before.\'\' :experimental:

# History and philosophy of EPEL (Extra Packages for Enterprise Linux) {#_history_and_philosophy_of_epel_extra_packages_for_enterprise_linux}

## History {#history_and_philosophy_of_epel_extra_packages_for_enterprise_linux}

The EPEL project was born out of Fedora. There was a need for quality
3rd party packages for Enterprise Linux using the already existing
Fedora infrastructure. Early on there was a move to help consolidate
existing 3rd parties, which for various reasons ended up mostly failing.
The EPEL project was formed as a Project rather than a special interest
group. This entailed a steering committee, formal votes and regular
progress reports to FESCo. After several years, it was determined that
EPEL could function just as well as a SIG where folks just got things
done and reached consensus, so EPEL moved to that model.

## Philosophy {#_philosophy}

EPEL strives to never replace or interfere with packages shipped by
Enterprise Linux. Packages in EPEL should be supported for the full life
cycle of the Enterprise Linux they are build against. Additionally, they
should strive to never require manual update procedures or processes.
During the stable part of the EPEL cycle, packages shouldn't update in a
way that changes the user experience or otherwise adds more than
bugfixes.

# Frequently Asked Questions (FAQ) {#_frequently_asked_questions_faq}

## About {#_about}

### What is EPEL? {#what_is_epel}

Extra Packages for Enterprise Linux (EPEL) is an initiative within the
[Fedora Project](https://fedoraproject.org/) to provide high quality
additional packages for [CentOS Stream](https://centos.org/) and [Red
Hat Enterprise Linux](https://redhat.com/rhel) (RHEL). EPEL packages
will also likely work with other distributions that target RHEL
compatibility.

As part of the Fedora packaging community, EPEL packages are 100%
free/libre open source software (FLOSS).

### Why is the Fedora Project sponsoring EPEL? {#why_is_the_fedora_project_sponsoring_epel}

A large number of contributors and users of Fedora and Enterprise Linux
want to work within Fedora to provide these packages.

The Fedora Project is a user of EPEL packages within the Fedora
infrastructure itself. The Fedora Project is in a position to know the
pain of not having a desired piece of software included in the RHEL
distribution, and also a unique position to do something about it.
Although RHEL is derived from Fedora, only a commercially supported
subset of Fedora derived packages are included in the RHEL distribution.
By sponsoring the EPEL project, Fedora contributors and users gain in
many ways.

### Is EPEL commercially supported by Red Hat? {#is_epel_commercially_supported_by_red_hat}

No. EPEL is a volunteer effort from the Fedora community. Just like
Fedora itself, Red Hat hosts infrastructure for this project and Red Hat
engineers are involved as maintainers and leaders but there are no
commercial support contracts or service level agreements provided by Red
Hat for packages in EPEL.

### Which distributions and releases does EPEL provides packages for? {#which_distributions_and_releases_does_epel_provides_packages_for}

EPEL provides packages for CentOS Stream 10, CentOS Stream 9, Red Hat
Enterprise Linux 9, and Red Hat Enterprise Linux 8. EPEL packages will
also likely work with other distributions that target RHEL
compatibility. Packages for earlier versions of CentOS Stream and RHEL
are no longer provided because these versions are end of life.

### How is EPEL different from other third party repositories for RHEL? {#how_is_epel_different_from_other_third_party_repositories_for_rhel}

- EPEL packages are in most cases built or derived from the equivalent
  ones in Fedora repository and maintained by the same people. It has
  also been improved through peer reviews, testing and feedback from end
  users.

- EPEL adheres to the well documented [Fedora Packaging
  guidelines](packaging-guidelines::index.xml), which RHEL has started
  following. This ensures good integration.

- EPEL is purely a complementary add-on repository and does not replace
  packages in RHEL.

- EPEL has a large team of contributors including Red Hat engineers and
  volunteer community members working together to maintain the
  repository.

- EPEL only provides free and open source software unencumbered by
  patents or any legal issues.

### Can I rely on these packages? {#can_i_rely_on_these_packages}

The EPEL project strives to provide packages with both high quality and
stability. However, EPEL is maintained by a community of people who
generally volunteer their time and no commercial support is provided. It
is the nature of such a project that packages will come and go from the
EPEL repositories over the course of a single release. In addition, it
is possible that occasionally an incompatible update will be released
such that administrator action is required. By policy these are
announced in advance in order to give administrators time to test and
provide suggestions.

It is strongly recommended that if you make use of EPEL, and especially
if you rely upon it, that you subscribe to the
[epel-announce](https://lists.fedoraproject.org/admin/lists/epel-announce.lists.fedoraproject.org/)
list. Traffic on this list is kept to a minimum needed to notify
administrators of important updates.

### What is EPEL-Next? {#what_is_epel_next}

EPEL packages are built against RHEL. EPEL Next packages are built
against CentOS Stream.

EPEL-Next is not a complete rebuild of all the EPEL packages, but only
those packages that need to be rebuilt to install on CentOS Stream. The
EPEL-Next repo is meant to be layered on top of the regular EPEL
repository.

Learn more about EPEL-Next on the following page:

- [EPEL Next](epel-about-next.xml)

## Packages {#_packages_2}

### Does EPEL replace packages provided within Red Hat Enterprise Linux? {#does_epel_replace_packages_provided_within_red_hat_enterprise_linux}

No. EPEL is purely a complementary repository that provide add-on
packages. EPEL packages will not conflict with any of the channels that
it builds against, with limited exceptions (see [conflicts in compat
packages](epel-policy.xml#conflicts_in_compat_packages)). Those specific
channels are listed in the [EPEL policy](epel-policy.xml#_policy).

It is permitted for EPEL to provide an alternative non-modular package
to any package found only in a non-default RHEL module.

EPEL will coordinate with other channels/products to minimize any
conflicts, but may replace or cause issues with other channels.

### What is the policy on updates for packages in EPEL? {#what_is_the_policy_on_updates_for_packages_in_epel}

Refer to the [EPEL package maintenance and updates](epel-policy.xml)
policy for all the details.

### How does Fedora Project ensure the quality of the packages in EPEL? {#how_does_fedora_project_ensure_the_quality_of_the_packages_in_epel}

Packages are peer reviewed against extensive [packaging
guidelines](packaging-guidelines::index.xml) before being imported into
the repository. Only updates that fix important bugs get pushed to the
stable repository directly. Other updates hit a testing repository first
and get released as an EPEL scheduled update in parallel with the EL
scheduled updates. Packages often are tested in Fedora, too. The Fedora
Packaging Guidelines and QA team back up all these efforts, helping to
avoid errors. There are also discussions for more strict QA policies. Do
participate and help us.

### How long are EPEL packages updated? {#how_long_are_epel_packages_updated}

Ideally EPEL packages are maintained as long as the corresponding RHEL
release is supported. However, EPEL is a volunteer effort, and a package
maintainer can retire their EPEL branch at any time.

### How can we be sure that someone will maintain the packages until end of life of the distribution the packages were built for? {#how_can_we_be_sure_that_someone_will_maintain_the_packages_until_end_of_life_of_the_distribution_the_packages_were_built_for}

The only way to be sure is to do it yourself, which is coincidentally
the reason EPEL was started in the first place.

Software packages in EPEL are maintained on a voluntary basis. If you
want to ensure that the packages you want remain available, get involved
directly in the EPEL effort. More experienced maintainers help review
your packages and you learn about packaging. If you can, get your
packaging role included as part of your job description; EPEL has
written a [generic
description](epel-package-maintainer-generic-description.xml) that you
can use as the basis for adding to a job description.

We do our best to make this a healthy project with many contributors who
take care of the packages in the repository, and the repository as a
whole, for all releases until RHEL closes support for the distribution
version the packages were built for. That is ten years after release
(currently) --- a long time frame, and we know a lot can happen in ten
years. Your participation is vital for the success of this project.

### What if my ISV/IHV wants to maintain a package in EPEL? {#what_if_my_isvihv_wants_to_maintain_a_package_in_epel}

Software and hardware vendors are encouraged to get involved in EPEL.
For more information, read the [ ISV/IHV
perspective](epel-about.xml#isvihv_perspective).

### Why isn't a package in EPEL 9 when it is in EPEL 8? {#why_isnt_a_package_in_epel_9_when_it_is_in_epel_8}

Packages are not automatically branched for each EPEL version. Each
package must be branched by a packager for each particular release, and
packagers may or may not be interested in EPEL 9 while they were
interested in EPEL 8. If you are an EPEL 9 user and want to see a
particular package added, it's a good idea to ask the existing EPEL or
Fedora maintainer. This lets the current maintainer know that there are
real users who would benefit from the package (instead of simply
guessing at the size of the user base).

To request an EPEL package for a particular EPEL branch, follow the
[EPEL package request steps](epel-package-request.xml).

### Are games or similar packages not strictly meant for enterprise users allowed and wanted? {#are_games_or_similar_packages_not_strictly_meant_for_enterprise_users_allowed_and_wanted}

Yes. There are people that use EL distributions on their home desktop or
similar scenarios because Fedora's release and updates cycle is faster
than required for them. Some of those people want to play games or use
other non-enterprise oriented software. Having such packages in the
repository doesn't affect anyone that uses EL distributions for other
needs.

### Why don't you simply rebuild all Fedora packages for RHEL that are not part of it? {#why_dont_you_simply_rebuild_all_fedora_packages_for_rhel_that_are_not_part_of_it}

We require maintainers to take ownership and commit to maintaining the
packages in the long term. Merely rebuilding all the packages
automatically has higher potential for packages being broken or
orphaned.

### What if the EPEL package is added to RHEL? {#what_if_the_epel_package_is_added_to_rhel}

If the package is added to RHEL it must be retired from EPEL as it is no
longer an \"extra package for enterprise linux\". There is some
automation in place to file a ticket to give the EPEL maintainer a heads
up; see the [EPEL package retirement
process](package-maintainers::Package_Retirement_Process.xml#_epel) for
more information.

## Using EPEL {#using_epel}

### How can I install the packages from the EPEL software repository? {#how_can_i_install_the_packages_from_the_epel_software_repository}

Follow the instructions on the [getting started
page](getting-started.xml).

### Where is the software repository located? {#where_is_the_software_repository_located}

EPEL packages are located at the [main
mirror](https://dl.fedoraproject.org/pub/epel/). There are mirrors
available at the [mirror
list](https://admin.fedoraproject.org/mirrormanager/mirrors/EPEL).

The snapshots of the EPEL repository are available in an [EPEL
archive](https://archives.fedoraproject.org/pub/archive/epel/). Those
are useful when a package was removed from EPEL, e.g. because the
package was added into a later RHEL version and you have not yet
migrated to the latest RHEL version.

### Can an IPv6-only host connect to main download server? {#ipv6_download_server}

The main fedora download server is currently ipv4 only.

- <https://dl.fedoraproject.org/pub/epel/>

It is recommended that you find the closest ipv6 mirror from the mirror
list.

- <https://admin.fedoraproject.org/mirrormanager/mirrors/EPEL>

If you must connect directly to a fedora ipv6 download server, go here.

- <https://download-ib01.fedoraproject.org/pub/epel/>

### Where can I find help or report issues? {#where_can_i_find_help_or_report_issues}

You can find help or discuss issues on the
[epel-devel](https://admin.fedoraproject.org/mailman/listinfo/epel-devel)
mailing list or IRC channel #epel on libera.chat. Report issues against
EPEL via
[Bugzilla](https://bugzilla.redhat.com/enter_bug.cgi?product=Fedora%20EPEL).
More options are available to [communicate with
EPEL](epel-communication.xml).

### How do I know that a package is a EPEL package? {#how_do_i_know_that_a_package_is_a_epel_package}

All EPEL packages are signed with an official EPEL gpg-key. The public
key IDs can be found at <https://getfedora.org/security/>. The keys are
included in epel-release and dnf will ask you to import it the first
time you install an EPEL package.

### How can I find out if a package is from EPEL? {#how_can_i_find_out_if_a_package_is_from_epel}

If you want to find out if a package comes from EPEL, use a query such
as this:

``` console
$ rpm -qp foo-0.1-5.el5.i386.rpm --qf '%{NAME}-%{VERSION}-%{RELEASE} %{VENDOR}\n'
foo-0.1-5.el5 Fedora Project
$ rpm -qp foo-0.1-5.el5.i386.rpm --qf '%{NAME}-%{VERSION}-%{RELEASE} %{DISTRIBUTION}\n'
foo-0.1-5.el5 Extras Packages for Enterprise Linux
$ rpm -qp foo-0.1-5.el5.i386.rpm --qf '%{NAME}-%{VERSION}-%{RELEASE} %{SIGPGP}\n'
foo-0.1-5.el5 883f030500468e3e4e119cc036217521f611025863009f5fe424c6fe4bc81a57f45722e465e71381dda2f6009f7c08e1743794b5b9a5a4cd149081092801a5d935
```

Or you can install and run the \'keychecker\' script to list all
packages signed with a particular key as well as which repo they came
from.

### Is EPEL \"upstream\" or \"an official package repository\" (like Fedora Extras was)? {#is_epel_upstream_or_an_official_package_repository_like_fedora_extras_was}

EPEL is just one of several add-on repositories with RPM packages for
RHEL. It is not an official repository. The different repositories serve
different user bases or follow different ideas.

Just like RHEL itself, EPEL in reality is more a \"downstream\" in the
sense that Fedora is upstream and EPEL, just like Red Hat, takes
packages for its product that are constantly developed, tested and
receive feedback in Fedora. Red Hat, through their sponsorship for the
Fedora project and participation of Red Hat maintainers, continues to
back EPEL, but Red Hat has not endorsed EPEL or commercially supported
it.

The EPEL maintainers are well aware that EPEL can't serve all needs, and
that other repositories are likely needed, for types of software the
Fedora project won't provide, which currently includes packages for EPEL
with a rolling release model or non-free and patent encumbered software.

## Contributing to EPEL {#contributing_to_epel}

### Who can contribute to EPEL? {#who_can_contribute_to_epel}

Anyone may contribute to EPEL. If you are using RHEL or compatible
spin-offs, and you have the required skills for maintaining packages or
are willing to learn, you are welcome to contribute.

### How do I get my packages into EPEL? {#how_do_i_get_my_packages_into_epel}

You have to follow the same
[process](package-maintainers::Package_Maintenance_Guide.xml) as Fedora
except that you request an EPEL branch such as epel8, epel9, or epel10.

### How do I request a EPEL branch for an existing Fedora package? {#how_do_i_request_a_epel_branch_for_an_existing_fedora_package}

Look [here for the procedure used to get a Fedora package in
EPEL](epel-package-request.xml).

### I maintain a package in Fedora. Do I have to maintain it for EPEL? {#i_maintain_a_package_in_fedora._do_i_have_to_maintain_it_for_epel}

No. You can if you want, or you can ask someone else to maintain the
package in EPEL for you. In some cases, you may be approached by a
current EPEL maintainer who wants to maintain your package in EPEL.

### I maintain a package in Fedora and want to maintain packages in EPEL, too, but I don't have a RHEL subscription for testing? {#i_maintain_a_package_in_fedora_and_want_to_maintain_packages_in_epel_too_but_i_dont_have_a_rhel_subscription_for_testing}

Please see [this page](epel-rhel-entitlements.xml) for information about
getting a free RHEL subscription for EPEL package maintenance.

### I'm a Fedora contributor and want to maintain my packages in EPEL, too. What do I have to do and what do you expect from me? {#im_a_fedora_contributor_and_want_to_maintain_my_packages_in_epel_too._what_do_i_have_to_do_and_what_do_you_expect_from_me}

All Fedora packagers can request EPEL branches in Git via the normal
procedure. Please keep in mind that by building your packages in EPEL we
expect that you are aware of the [ special EPEL guidelines and
policies](epel-policy.xml) and that you will adhere to them. You should
also plan to maintain the packages for the near future --- ideally for
several years, or for the full planned lifetime of EPEL. Remember that
RHEL has a planned lifetime of 10 years.

You may want to look into formalizing your packaging role in your
company or other organization. If you can do that, this [generic job
description](epel-package-maintainer-generic-description.xml) may help.
Aside from making sure that you are recognized for the value you give
your organization, formal role recognition ensures that your
organization has someone continuing to maintain the package, even if
someone new is in the role.

It is the maintainer's responsibility to ensure that their EPEL packages
work on RHEL. Please see [this page](epel-rhel-entitlements.xml) for
information about getting a free RHEL subscription for EPEL package
maintenance.

### How do you make sure that packages in EPEL and in Fedora do not split? {#how_do_you_make_sure_that_packages_in_epel_and_in_fedora_do_not_split}

The plan is to have one primary maintainer per package who is
responsible for making certain that the package enhancements applied to
one tree find their way into the other trees (for example, Fedora
devel).

This maintainer decides what makes sense to apply for the package in
general. New EL branches for new EL releases are normally created from
the associated Fedora branch on which the EL release is based.
Therefore, the EL maintainer has a genuine interest in getting
enhancements merged into Fedora.

### Will my packages from Fedora simply build unchanged on EPEL {#will_my_packages_from_fedora_simply_build_unchanged_on_epel}

Most likely they will build unchanged. However, there are specific items
to consider. All your build requirements in the package must be part of
RHEL or EPEL.

### I need to build a package that in turn requires another one I have just added. How do I do this? {#i_need_to_build_a_package_that_in_turn_requires_another_one_i_have_just_added._how_do_i_do_this}

You will need to request a buildroot override in bodhi.

### How can I know which packages are part of RHEL? {#how_can_i_know_which_packages_are_part_of_rhel}

The easiest ways to do this are to either use the [RHEL developer
subscription](epel-rhel-entitlements.xml) or check the RHEL package
manifests.

- [RHEL 9 package
  manifest](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html-single/package_manifest/index)

- [RHEL 8 package
  manifest](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/8/html-single/package_manifest/index)

You can also check the package source repos in the [CentOS Stream GitLab
space](https://gitlab.com/redhat/centos-stream/rpms). Note that a GitLab
branch corresponds to the same major version of RHEL, e.g. the c9s
branch for RHEL 9. If a branch has a `dead.package` file, that means it
was removed during development of that RHEL version and is thus eligible
for EPEL.

### I want to build packages for EPEL but some of my packages dependencies are not available in EPEL --- or --- I'd like to see a Fedora package in EPEL that is not yet available there {#i_want_to_build_packages_for_epel_but_some_of_my_packages_dependencies_are_not_available_in_epel____or____id_like_to_see_a_fedora_package_in_epel_that_is_not_yet_available_there}

See [here how to get a Fedora package in
EPEL](epel-package-request.xml).

### RHEL 8 has binaries in the release, but is missing some corresponding -devel package. How do I build a package that needs that missing -devel package? {#rhel_8_has_binaries_in_the_release_but_is_missing_some_corresponding__devel_package._how_do_i_build_a_package_that_needs_that_missing__devel_package}

There is a short term and a long term solution. These two solutions
should be used together.

- Short Term: Create an epel package that only has the missing packages.

  - Be prepared to maintain this package as long as it is needed.

  - It is recommended that you name it `<package>-epel`

  - It is recommended that you add the epel-packagers-sig group as a
    co-maintainer

  - It qualifies for an exception to the [package review
    process](packaging-guidelines::ReviewGuidelines.xml) so you can
    request the repo with

    - `fedpkg request-repo --exception <package>-epel`

  - Once the repo is created, you must retire the rawhide branch to make
    it clear that this is an EPEL-only package and it shouldn't be
    branched for future Fedora releases

    - `fedpkg retire 'EPEL-only package'`

  - If you need help building this, ask for help. We have some examples.

  - When/If the missing package(s) are added to RHEL CRB, retire your
    `-epel` package.

- Long Term: Request the package be added to RHEL 8 and 9 CRB
  repository.

  - To initiate this process, please file an issue in
    <https://issues.redhat.com> and request it be added to RHEL 8 and 9.
    Report the bug against the RHEL project, assign it to the proper
    CentOS Stream versions and add the source package name in the
    Component field. More details on this can be found in the [CentOS
    contributor
    guide](https://docs.centos.org/en-US/stream-contrib/quickstart/#_1_file_an_issue).

  - Be sure to say that it is impacting an EPEL build, and which package
    it is impacting.

### Can I bring a modular package into EPEL? {#can_i_bring_a_modular_package_into_EPEL}

When EPEL 8 was launched, it came together with the EPEL 8 Modular repo
as an effort to bring modular packages to EPEL. After years of struggle,
[it was
decided](https://lists.fedoraproject.org/archives/list/epel-announce@lists.fedoraproject.org/thread/LNNPYQU6OLT2OMGKJM6DXLCE5RIJ57HJ/)
to disable by default the EPEL 8 Modular repository on October 31st
2022, and then to archive the repository from Febraury 14th 2023 onward.
Currently there is no plan to bring modularity back to EPEL.

If you want to bring a package that is distributed as modular in Fedora
you will need to create a [non-modular version of the
package](https://docs.fedoraproject.org/en-US/packaging-guidelines/Naming/#multiple).

## Miscellaneous {#_miscellaneous}

### I want to get a package into EPEL. What do I have to do? {#i_want_to_get_a_package_into_epel._what_do_i_have_to_do}

Get it in Fedora first. This isn't a strict rule, but all the EPEL
packages need to meet the Fedora packaging guidelines. If people want it
in EPEL, they probably want it in Fedora as well.

If it is in Fedora, and you are the maintainer, branch and build it as
you would any other Fedora release.

If it is in Fedora, and you are NOT the maintainer, follow the [EPEL
package request steps](epel-package-request.xml).

### Is it possible to get a package only into EPEL and not Fedora? {#is_it_possible_to_get_a_package_only_into_epel_and_not_fedora}

Simply go through the review process for Fedora and specify only EL
targets for the initial import. Due to technical reasons, a main branch
for Rawhide will always be created. Therefore [retire the
package](package-maintainers::Package_Retirement_Process.xml) directly
in Fedora Rawhide to avoid confusion. But note that maintaining packages
in Fedora has many advantages for you, you should consider maintaining
the package in both Fedora and EPEL if it makes for the package to be in
Fedora.

### What do I have to do to get a package removed from EPEL? {#what_do_i_have_to_do_to_get_a_package_removed_from_epel}

Please follow the [Package retirement
process](package-maintainers::Package_Retirement_Process.xml).

### What do I need to do if I need to get a updated package quickly into the EPEL proper? {#what_do_i_need_to_do_if_i_need_to_get_a_updated_package_quickly_into_the_epel_proper}

Please do not try and push your packages directly to stable unless they
are security updates or critical bug fixes. This is enforced by epel
releng/signers who will change your request to testing unless your
update meets the criteria for pushing to stable.

Normal updates spend a weeks in testing before being pushed to stable.
If enough people test those updates and give your package sufficient
karma in bodhi it can be pushed to stable before that week is up.

### Why doesn't EPEL use repotags? {#why_doesnt_epel_use_repotags}

There were a lot of long discussions in the months of EPEL about using
repotags or not. Lots of people from inside and outside of Fedora and
EPEL, as well as maintainers from other repositories, participated in
those discussions. No real agreement could be found as to whether the
benefits outweigh the disadvantages - part of the problem was that
people sometimes couldn't agree on the benefits or disadvantages
repotags have (or if there are any). The final decision in three voting
sessions (one done by FESCo before EPEL had a Steering Committee and
twice done by EPEL's first Steering Committee) was to go without
repotags in EPEL.

### Is EPEL willing to cooperate with other third party repositories? {#is_epel_willing_to_cooperate_with_other_third_party_repositories}

EPEL is always willing to discuss cooperation with other parties and
repositories and encourages maintainers to do so whenever possible.

### What about compatibility with other third party repositories? {#what_about_compatibility_with_other_third_party_repositories}

Mixing different RPM repositories that were not designed to be mixed can
lead to incompatibilities that often result in dependency resolution
problems in dnf. Sometimes it even happens that software is not working
as expected if libraries and applications come from different
repositories. EPEL is designed as an add-on repository for RHEL. The
best way to avoid problems is to avoid mixing EPEL with other third
party repositories that have conflicting packages on the same system.
Some people nevertheless do it and the dnf priorities plugin can help to
avoid the worst problems.

If you encounter a problem where packages from EPEL are incompatible
with another repository, or lead dnf to bail out during dependency
resolution, please report a bug in
[Bugzilla](https://bugzilla.redhat.com) and contact the maintainer of
the other repositories. The EPEL project encourages its maintainers to
solve such problems together with the maintainers from other
repositories in order to find a solution that is acceptable for both
sides. However, there is no guarantee such a solution can or will be
found in every case, as technical solutions to solve a repository-mixing
issue might have side-effects or drawbacks for one of the repositories
involved.

## Other questions? {#other_questions}

You can contact the [EPEL
team](#where_can_i_find_help_or_report_issues).
