The Fedora Project releases a new version of Fedora Linux approximately
every six months and provides updated packages (maintenance) to these
releases for approximately 13 months. This allows users to \'skip a
release\' while still being able to always have a system that is still
receiving updates.

# Release Dates {#_release_dates}

Our [release schedule](https://fedorapeople.org/groups/schedule/)
intentionally includes some \'buffer\' weeks, with early and later
release targets. Predictable release dates benefit end users planning on
upgrades, downstream distros making their schedules based on our work,
and of course our own developers working on getting features to users.
End users (and the press!) should plan on the release being available by
the \'Target date &#35;1\' milestone.

But you know that \'trick\' where to keep yourself from being late you
set all of your clocks ahead by five minutes? For a month or two, it
works---you're on time everywhere!---but then you start to compensate
because you know that extra time is built in. We've put out Fedora Linux
releases on time for the past few years, and in order to keep doing
that, we need to keep seriously aiming for the early target. That way,
when we do need it, we can actually use the built in time. Fedora
contributors should plan on having the release done by the \'Early
target\' milestone.

# Development Schedule {#_development_schedule}

We say \'\'approximately every six months\'\' because like many things,
releases don't always go exactly as planned. The schedule is not
strictly time-based, but a hybrid of time and quality. The milestone
releases are
[tested](https://fedoraproject.org/wiki/QA:Release_validation_test_plan)
for compliance with the [Fedora Release
Criteria](https://fedoraproject.org/wiki/Fedora_Release_Criteria), and
releases will be delayed if this is not the case.

The schedule for the release currently under development is on its
[release schedule](https://fedorapeople.org/groups/schedule/) page. Beta
and General Availability (final) releases happen at approximately 14:00
UTC.

## Development Planning {#_development_planning}

Fedora development planning is handled by the [Release Planning
Process](program_management::changes_policy.xml). So-called
\'\'Changes\'\' are proposed, initially reviewed, and monitored through
the development process by the [Fedora Engineering Steering
Committee](fesco::index.xml) (FESCo) and [Fedora Program
Manager](program_management::index.adoc&#35;_fedora_program_manager).

## Development Process {#_development_process}

Fedora uses a system involving two \'development\' trees.
[Rawhide](rawhide.xml) is a constantly rolling development tree. No
releases are built directly from Rawhide. Approximately 10 weeks before
the planned date of a Fedora release, a tree for that release is
\'[branched](branched.xml)\' from the Rawhide tree. At that point the
Rawhide tree is moving towards the release \'\'after\'\' the new
Branched release, and the pending release is stabilized in the Branched
tree.

:::: tip
::: title
:::

This means that development of a Fedora release is considered to begin
at the time its \'\'predecessor\'\' branches from Rawhide. For instance,
development on Fedora Linux 31 began the day after Fedora Linux 30
branched from Rawhide and entered the stabilization process.
::::

After the [Bodhi activation
point](fesco::Updates_Policy.adoc&#35;updates-testing-activation) , the
[Bodhi](https://fedoraproject.org/wiki/Bodhi) system is permanently
active on the Branched release (all the way until it goes end of life),
and requirements for updates to be marked as \'\'stable\'\' are set out
in the [Updates Policy](fesco::Updates_Policy.xml). Packages must go
through the
[\'\'updates-testing\'\'](quick-docs::repositories.adoc&#35;the-updates-testing-repository)
repository for the release before entering its
[\'\'stable\'\'](quick-docs::repositories.adoc&#35;stable-is-not-a-repository)
repository, according to rules defined in the updates policy. These
rules tighten gradually from Beta through to post-GA (Final), but the
basic process does not change.

For some time prior to a milestone (Beta, Final) release a
[freeze](https://fedoraproject.org/wiki/Milestone_freezes) is in effect
which prevents packages moving from \'\'updates-testing\'\' to
\'\'stable\'\' except in accordance with the
[blocker](https://fedoraproject.org/wiki/QA:SOP_blocker_bug_process) and
[freeze
exception](https://fedoraproject.org/wiki/QA:SOP_freeze_exception_bug_process)
bug policies. This freeze is lifted once the milestone is finished, and
so packages begin to move from \'\'updates-testing\'\' to \'\'stable\'\'
as normal again, until the next milestone's freeze date.

## Schedule Methodology {#_schedule_methodology}

Fedora Linux release schedules repeat ad infinitum with \'early target\'
dates of the third Tuesday in April and October. Significant changes to
the release schedule must be approved by FESCo. The Fedora Program
Manager works with teams across the project to incorporate their
activities into the overall schedule and will make updates that do not
affect release milestones.

## Development Schedule Rationale {#_development_schedule_rationale}

Fedora generally develops new releases over a six month period to
provide a regular and predictable release schedule. The bi-annual
targeted release dates are the third Tuesday of April and October,
making them easy to remember and avoid significant holiday breaks.
Changes to this standard must be approved by FESCo.

A six month release schedule also follows the precedence of Red Hat
Linux (precursor to Fedora). Former Red Hat software engineer Havoc
Pennington offers a [historical
perspective](https://web.archive.org/web/20240607150548/https://listman.redhat.com/archives/fedora-advisory-board/2006-December/002039.html).
GNOME started following a time based release based on the ideas and
success of Red Hat Linux and other distributions following Fedora having
adopted a similar release cycle. Several other major components have
started following a time-based release schedule. While the exact release
schedules vary between these components and other upstream projects, the
interactions between these components and Fedora Linux makes a six
month, time-based release schedule a good balance.

## Schedule Contingency Planning {#_schedule_contingency_planning}

If \'\'Mass rebuild\'\' is not completed on time, all the subsequent
milestones starting with \'\'Branch point\'\' are pushed back for one
week until the \'\'Mass rebuild\'\' is completed.

If the Beta
[Go/No-Go_Meeting](https://fedoraproject.org/wiki/Go_No_Go_Meeting)
results in a \'No Go\' determination, rescheduling of the milestone and
subsequent milestones follows these rules:

&#42; Slip of the Beta from the Early Target to Target &#35;1 does not
affect Final Release (GA) date. The Final Release (GA) date remains on
\'\'Early Final Target\'\'. &#42; Slip of the Beta to Target &#35;1 adds
a new \'\'Beta Target &#35;2\'\' &#42; Slip of the Beta past Target
&#35;N (where N &gt;= 2) adds a new \'\'Beta Target &#35;(N+1)\'\' and
also adds a new \'\'Final Target &#35;N\'\'

If the Final
[Go/No-Go_Meeting](https://fedoraproject.org/wiki/Go_No_Go_Meeting)
results in a \'No Go\' determination, that milestone and subsequent
milestones will be pushed back by one week.

One week is added to the schedule to maintain the practice of releasing
on Tuesdays. Tuesdays are the designated release day because they are
good days for news coverage and correspond to the established day we
synchronize our content with the mirrors that carry our releases. Be
aware of holidays and of possible PR conflicts with the new proposed
final date.

Go/No-Go Meetings receive input from representatives of
[FESCo](fesco::index.xml), [Release
Engineering](https://docs.pagure.org/releng/), and [Quality
Assurance](https://fedoraproject.org/wiki/QA).

# Maintenance Schedule {#_maintenance_schedule}

We say maintained for \'\'approximately 13 months\'\' because the
supported period for releases is dependent on the date the release under
development goes final. As a result, \'\'Release N\'\' is supported
until four weeks after the release of \'\'Release N+2\'\'.

## Maintenance Schedule Rationale {#_maintenance_schedule_rationale}

Fedora Linux is focused on free and open source software innovations and
moves quickly. If you want a distribution that moves slower, but has a
longer lifecycle, CentOS Stream or Red Hat Enterprise Linux, which are
downstream of Fedora might be more suitable for you.

Historically, the Fedora Project has found that supporting two releases
plus Rawhide and the pre-release Branched code to be a manageable work
load.

# End of Life (EOL) {#_end_of_life_eol}

When a release reaches the point where it is no longer supported when no
updates are created for it, then it is considered End of Life (EOL).
Branches for new packages in the SCM are not allowed for distribution N
after the Fedora N+2 release and new builds are no longer allowed.

The tasks performed at EOL are documented in the [End of life
SOP](https://docs.fedoraproject.org/en-US/infra/release_guide/sop_release_eol/).

[Information about EOL releases](eol.xml) is available.

# Spins {#_spins}

Spins are alternate versions of Fedora Linux, tailored for various types
of users via hand-picked application sets and other customizations.

We first offered Spins with the release of Fedora Linux 7 in May 2007.
Previously, we distinguished between Spins---variants featuring
non-default desktop environments---and Labs---variants tailored for a
particular use case. While the websites still maintain this distinction,
there is no practical difference. One day, we may even get the
\'Solutions\' moniker to catch on.

## FAQ {#_faq}

### Where can I find them? {#_where_can_i_find_them}

<https://spins.fedoraproject.org> and <https://labs.fedoraproject.org>
have a full list of all the spins currently offered, and information
about each. For historical information, see the per-release information
on the sidebar.

### Who makes Spins? {#_who_makes_spins}

Teams within Fedora are responsible for curating their Spins. The
release-specific Spins listings on the sidebar have links to the
maintainers for each Spin.

Each release, the Fedora Program Manager checks with each Spin
maintainer to make sure they still want to keep their Spin active. If
they do not, or if there is no reply, the Spin is offered to the
community for adoption. Unmaintained Spins are dropped in order to make
sure our users get the intended experience.

### How do I create my own spin? {#_how_do_i_create_my_own_spin}

More information on creating spins is available in the [Creating Spins
documentation](spins/creating.xml).

### Why don't I just use plain Fedora Linux? {#_why_dont_i_just_use_plain_fedora_linux}

You can. Customized spins are merely targeted versions of Fedora Linux.
It is possible to customize plain Fedora Linux to match any official
spin. A customized spin can save you time and effort.

### Why should I choose a custom spin? {#_why_should_i_choose_a_custom_spin}

Custom spins let you experience a select set of Fedora software,
possibly in a particular way. For example, a desktop live CD could boot
directly to a GNOME desktop, with 3D desktop effects enabled and
selected backgrounds, colors and featured applications. With further
customization, a custom spin could boot directly to a movie player or
launch a Web server that is ready to publish custom data.

# Creating Spins {#_creating_spins}

This page describes the process for creating a new Spin or adopting an
abandoned Spin.

## Prerequisites {#_prerequisites}

There are a few steps you'll need to do first. Some of these may seem
obvious, but it's best to be clear.

&#42; Create a [Fedora Account](https://accounts.fedoraproject.org)
&#42; Sign the [Fedora Project Contributor
Agreement](https://fedoraproject.org/wiki/Legal:Fedora_Project_Contributor_Agreement)
in the [Accounts system](https://accounts.fedoraproject.org/) &#42; Sign
up for the
[devel-announce](https://lists.fedoraproject.org/admin/lists/devel-announce.lists.fedoraproject.org/)
and
[spins](https://lists.fedoraproject.org/admin/lists/spins.lists.fedoraproject.org/)
mailing lists. You may also want to join the higher-volume
[devel](https://lists.fedoraproject.org/admin/lists/devel.lists.fedoraproject.org/)
mailing list and any lists or
[Discussion](https://discussion.fedoraproject.org) categories that are
relevant to your Spin.

## Creating a new Spin {#_creating_a_new_spin}

To start a new Spin, you'll need to file a Self-Contained [Change
proposal](program_management::changes_policy.xml). Since Release
Engineering will need to start building the Spin, you'll need to submit
a [ticket with Release Engineering](https://pagure.io/releng). If you
want the Spin to have a non-descriptive name (for example: \'Fedora
Llamanator\' instead of \'Fedora Llama Herder Spin\'), file a trademark
issue with the [Fedora
Council](https://pagure.io/Fedora-Council/tickets/issues). But before
you do any of that&#8230;

### Before you submit a Change proposal {#_before_you_submit_a_change_proposal}

In order to be successful, there are a few things you should do as
you're starting the process.

&#42; &#42;&#42;Find helpers.&#42;&#42; Whether it's a single
co-maintainer or a full team, having help will lighten the load. It
gives you the ability to step away when you need to. And if you're
working with someone else, you can make each other's ideas better. &#42;
&#42;&#42;Set your goals.&#42;&#42; You can make a Spin for just about
any reason. But if you don't identify the reason, you'll have a hard
time building a solution for it. Who are you trying to serve? What
problem will you solve for them? How will you solve it? &#42;
&#42;&#42;Make sure a Spin is the right solution.&#42;&#42; Is a
software group in repo a better solution? &#42; &#42;&#42;Notify the
Respins SIG.&#42;&#42; The [Respins
SIG](https://fedoraproject.org/wiki/Respins-SIG) produces updated
install media post-release. Let them know you have a new Spin coming by
posting in the &#35;fedora-respins channel or emailing [Ben
Williams](https://accounts.fedoraproject.org/user/jbwillia/).

### After the change proposal is approved {#_after_the_change_proposal_is_approved}

Great! Your proposal is approved. Now it's time to make it happen.

&#42; &#42;&#42;Work with Release Engineering to build the
Spin.&#42;&#42; See the [Maintaining a Spin docs](spins/maintaining.xml)
for more about this. &#42; &#42;&#42;Open a ticket with the Websites
&amp; Apps team.&#42;&#42; You'll need to get your Spin added to the
website if you want people to be able to find it. The [Websites &amp;
Apps team](websites::index.xml) can help you get ready. &#42;
&#42;&#42;Open a ticket with the Design team.&#42;&#42; At a minimum,
you'll want a header image for the website. You may also want additional
art for the website, stickers, etc. The [Design team
repo](https://gitlab.com/fedora/design/team/requests/-/issues) is your
starting point for those requests. &#42; &#42;&#42;Open a ticket with
Fedora Media Writer.&#42;&#42; Create an issue in the [MediaWriter
repository](https://github.com/FedoraQt/MediaWriter/issues) to add your
Spin to the media creation tool.

## Adopting a Spin {#_adopting_a_spin}

If a Spin is abandoned and you want to take it over, it doesn't take
much beyond raising your hand. If the Program Manager has announced that
the Spin is abandoned, just reply to their email. For a Spin that has
been retired, first make sure there's a good use case for bringing it
back. If there is, submit a Self-Contained [Change
proposal](program_management::changes_policy.xml) as if it were a new
Spin.

# Maintaining a Spin {#_maintaining_a_spin}

## Making changes {#_making_changes}

The contents and configuration of Spins come from kickstart files in the
[fedora-kickstarts](https://pagure.io/fedora-kickstarts/) repo. To make
changes, you can submit pull requests against the appropriate file. If
you have a particularly meaningful change to make, you may want to file
a [Change proposal](program_management::changes_policy.xml) in order to
communicate it to the wider community (and get it into the release
notes).

## Monitoring status {#_monitoring_status}

You may want to start watching the [failed composes
repo](https://pagure.io/releng/failed-composes/issues) to see when your
Spin fails to compose. Currently, you can't get per-Spin notifications,
so you'll get notified for all failures. You'll probably want to set up
a mail filter for this.

If you're not sure what a failure message means or how to resolve it,
ask for help on the spins or devel mailing lists, in chat, or somewhere
else that seems appropriate.

## Release-blocking status {#_release_blocking_status}

Spins are not release-blocking by default. If you want your Spin to
block the release, [FESCo](fesco::index.xml) must approve this.

In addition, we do not re-run release candidate composes for failed
non-blocking deliverables. That means if your spin fails in the release
candidate compose, it will not be a part of the official release
artifacts. Most failures these days are systemic (in other words, they
represent an actual problem with the Spin), so it's on Spin maintainers
to watch for and resolve failures as the Go/No-Go decision approaches.

## Keepalive {#_keepalive}

Once per release cycle, the Fedora Program Manager will check with all
Spin maintainers to ensure the Spin should continue to be produced. If
you do not respond, the Program Manager will attempt to find someone to
take maintainership of the Spin.

&#42; Development Releases = Rawhide

\'Rawhide\' is the name given to the current development version of
Fedora Linux. It consists of a [package
repository](quick-docs::repositories.xml) called \'rawhide\' and
contains the latest build of all Fedora Linux packages updated on a
daily basis. Each day, the build system attempts to create a full set of
deliverables (installation images and so on), and all that compose
successfully are included in the Rawhide tree for that day.

Rawhide is sometimes called \'development\' or \'main\' (as it's the
\'main\' branch in package git repositories).

## Goals {#_goals}

Rawhide has the following Goals:

&#42; To allow package maintainers to integrate the newest *usable*
versions of their packages into Fedora. &#42; To allow advanced users
access to the newest *usable* packages in a rolling manner. &#42; To
allow incremental changes to packages that are either too minor or major
to go to stable Fedora releases. &#42; To identify and fix issues with
packages before they reach a stable release of Fedora. &#42; To allow a
place where certain low-level packages (approved by FESCo), including
(but not limited to) glibc and gcc, can gain real-world testing of
pre-release versions.

## Audience {#_audience}

Rawhide is targeted at advanced users, testers, and package maintainers.

As a Rawhide consumer, you should:

&#42; Be willing to update on an almost daily basis. Rawhide gets
hundreds of updates a day, and applying those updates on a regular basis
allows you to more easily isolate when a bug appeared and what
package(s) are responsible. &#42; Be willing and able to troubleshoot
problems. From time to time there are problems with Rawhide packages,
and you will need strong troubleshooting skills and the ability to
gather information for bug reports. You need a good understanding of dnf
and how to downgrade packages, as well as boot time troubleshooting.
&#42; Have time and desire to learn new interfaces and changes. Rawhide
packages stick closely to upstream projects, so interfaces and
command-line options are subject to frequent changes. &#42; Be willing
to reboot frequently to test new kernel versions and confirm
functionality of the boot process. If you can't reboot often, consider
using a stable release instead. &#42; Be willing and able to report bugs
to Bugzilla as you find them and help maintainers gather information to
fix them.

If the above doesn't match you, you may wish to instead follow the
[Branched](branched.xml) release (depending on the point in the [release
cycle](https://fedorapeople.org/groups/schedule/)) or use regular stable
Fedora releases.

## Using Rawhide {#_using_rawhide}

See the [wiki
template](https://fedoraproject.org/wiki/Template:Rawhide_branched_install_methods)
for instructions on installing and using Rawhide.

## Discussing Rawhide {#_discussing_rawhide}

There are a number of ways to communicate with other Rawhide users:

### IRC {#_irc}

Rawhide discussion is on topic and welcome in both the
[&#35;fedora-devel](https://web.libera.chat/?channels=&#35;fedora-devel)
and [&#35;fedora-qa](https://web.libera.chat/?channels=&#35;fedora-qa)
IRC channels.

### Mailing Lists {#_mailing_lists}

Rawhide discussion is on topic and welcome in both the
[test](https://lists.fedoraproject.org/admin/lists/test@lists.fedoraproject.org/)
and
[devel](https://lists.fedoraproject.org/admin/lists/devel@lists.fedoraproject.org/)
lists.

### Bugzilla {#_bugzilla}

Rawhide bugs should be reported against the *Fedora* product, *rawhide*
version and the affected component. Please do follow [best
practices](quick-docs::howto-file-a-bug.xml) when filing. Remember that
IRC and mailing lists are useful to help narrow down if some behavior is
a bug or where to report it, but are themselves not bug reporting
channels. Always file bugs in [Bugzilla](http://bugzilla.redhat.com).

Note that broken dependencies are mailed to maintainers for each daily
Rawhide compose where a package has such broken dependencies. Therefore,
it's usually not worth filing a bug for broken dependencies unless they
don't appear in the daily report, or you have a fix or improvement to
suggest.

## Producing Rawhide {#_producing_rawhide}

Package owners must build for Rawhide using Koji just like you would any
other build; you do not go through the Bodhi process and the build
becomes available almost immediately.

The Rawhide repository is composed every day starting at 05:15 UTC. All
rawhide builds in the buildsystem at that time are included in the
compose attempt. The compose process also attempts to build all the
standard Fedora \'deliverables\' (live and install images, ARM and Cloud
disk images, container images and so on). If any release-blocking image
fails to build as part of the compose, the compose is considered to have
failed. If the compose completes successfully, the compose will be
\'synced out\' to the mirror system. (A system where the sync only
happens if a set of automated tests run on it passes is planned, but not
yet fully implemented).

Rawhide is under &#96;development/rawhide&#96; on the mirrors. You can
find a local \'development\' mirror on the [public mirror
list](https://mirrormanager.fedoraproject.org/mirrors/Fedora/development).
Compose time varies depending on number of changes, but is typically
between 2 and 3 hours.

Composes are done in a rawhide chroot using the \'pungi\' tool called
from [a script maintained by Fedora Release
engineering](https://pagure.io/pungi-fedora/blob/main/f/nightly.sh). If
the base set of packages in Rawhide needed to compose Rawhide are
broken, the daily compose may fail.

A report for each Rawhide compose is sent to to the
[test](https://lists.fedoraproject.org/admin/lists/test@lists.fedoraproject.org/)
and
[devel](https://lists.fedoraproject.org/admin/lists/devel@lists.fedoraproject.org/)
lists. This report contains output from the repodiff tool from the
previous compose as well as a broken dependency report for packages with
broken dependencies. Additionally, private email is sent to maintainers
with packages containing broken dependencies.

Package maintainers should read and follow the [Rawhide updates
policy](fesco::Updates_Policy.adoc&#35;_rawhide) for building any
packages in Rawhide.

If needed and approved by [FESCo](fesco::index.xml), mass rebuilds are
done by Release Engineering in Rawhide a month or so before the next
release branches from it. Typically these are done for a global change
over all packages such as a new gcc release, or rpm package format.

## Questions and Answers {#_questions_and_answers}

&#42;Doesn't rawhide eat babies / kill pets / burn down houses / break
constantly?&#42;

No. Please stop telling everyone that.

&#42;So Rawhide is very stable and we can all use it?&#42;

No. See audience above. There are things that break from time to time,
but if you are able to downgrade or troubleshoot, such issues aren't too
severe. Most users should still stick to stable Fedora releases, but
Rawhide is a viable option for enthusiasts to experiment with.

&#42;I'm using a Stable Fedora release, but I want a newer package
version that's only available in Rawhide. Can I just &#96;dnf
install&#96; it?&#42;

No. Mixing releases like this is a bad idea. Better options are:

&#42; Ask the Fedora maintainer in a bug report to update the stable
version if permitted by policy. If not, there may be a [Copr
repository](http://copr.fedoraproject.org/) that provides the updated
version. See the COPR page for more details. &#42; Obtain the src.rpm
for the package you wish and try to &#96;rpmbuild \--rebuild&#96; it
(which may or may not work depending on dependencies).

&#42;I want to run the Rawhide kernel on my stable Fedora machine. Can I
do that?&#42;

Sometimes yes. The kernel is more self-contained than other Rawhide
packages and you also can easily boot your older kernel if the Rawhide
kernel goes wrong. Download and &#96;dnf install&#96; the package.
However, note that Rawhide kernels often have debugging code enabled,
which results in them performing noticeably worse than release kernels
(they will be slower and consume more memory).

&#42;Is Rawhide a \'rolling release\'?&#42;

It depends on how you define that, but yes.

&#42;How can I tell when the Rawhide compose for the day has
finished?&#42;

Check the reports sent to the
[test](https://lists.fedoraproject.org/admin/lists/test@lists.fedoraproject.org/)
and
[devel](https://lists.fedoraproject.org/admin/lists/devel@lists.fedoraproject.org/)
lists, or watch fedora-messaging for the
&#96;org.fedoraproject.prod.pungi.compose.status.change&#96; topic.

&#42;What happens during branching, does it affect my Rawhide release
somehow?&#42;

No, you're still on Rawhide and no action is required. (This was handled
differently in the past).

&#42;How do I get out of Rawhide again? I want to switch to the Branched
release or a stable release.&#42;

Note that downgrading your system to a lower release is not supported,
not tested, not a good idea, and definitely *at your own risk*. The
safest approach is to reinstall the system. If you really want to
downgrade, at least make a filesystem snapshot first (if you use the
default Btrfs filesystem).

One common use case is to switch your system to Branched right after it
is created (split from Rawhide). In this case, the sooner you do it
(after branching), the safer and easier it is---the difference between
systems is minimal at that point. Downgrading after a long time, or
downgrading to a stable release (which is completely different from
Rawhide) will be more problematic.

You can (attempt to) downgrade to Branched or a stable release using
[DNF system upgrade](quick-docs::dnf-system-upgrade.xml) (the same
approach as for upgrades). However, because Rawhide uses a different set
of system repositories, you need to explicitly disable those during the
download phase, and explicitly enable the set or repositories used on
non-Rawhide systems. So the download command would look like this (this
will disable and enable the correct repositories, and if you have some
additional (including third-party) repositories installed, it will keep
them enabled or disabled as they are currently; replace &#96;NN&#96;
with the target release number): &#96;sudo dnf system-upgrade download
\--releasever=NN \--disablerepo=\'rawhide,rawhide-modular\'
\--enablerepo=\'fedora,updates\'&#96;

Everything else should be unchanged, you can use the rest of the
aforelinked guide to proceed. There is a higher chance of encountering
broken dependencies when downgrading, because while package dependencies
must work correctly when going up in versions. They don't need to work
when going down. In that case, you can try &#96;\--skip-broken&#96; or
removing the offending packages (if possible), otherwise you're mostly
out of luck.

&#42;As a package maintainer do I have to build rawhide packages or does
the nightly compose take care of that?&#42;

You must build for Rawhide yourself (using Koji). The nightly compose
only collects packages already built and marked with the appropriate
target (rawhide) in Koji.

&#42;Are rawhide packages signed?&#42;

All of them are now signed. Make sure you have gpgcheck=1 set in your
repo file to take advantage of this.

## Hints and Tips {#_hints_and_tips}

&#42; Your package management system can be of great help in diagnosing
and working around issues you find. Do read up and understand:
&#42;&#42; &#96;dnf downgrade&#96; &#42;&#42; &#96;dnf history&#96;
&#42;&#42; &#96;dnf update \--skip-broken&#96; &#42;&#42; &#96;koji
download-build&#96; &#42; If you are using an immutable variant like
Silverblue, you should make good use of the features of OSTree like:
&#42;&#42; &#96;rpm-ostree rollback&#96; &#42;&#42; &#96;ostree admin
config-diff&#96; &#42;&#42; &#96;ostree admin pin 0&#96; &#42; You
should update frequently (preferably every day). This allows you to more
easily narrow down when a problem or issue appeared. If you apply a week
of Rawhide updates at once, you have many more packages to examine to
narrow down issues. &#42; Reboot often (preferably whenever new kernels
arrive). This allows you to test the boot up process and packages
related to it, as well as newer kernels. Read and understand the Dracut
troubleshooting steps. &#42; Follow the
[test](https://lists.fedoraproject.org/admin/lists/test@lists.fedoraproject.org/)
and
[devel](https://lists.fedoraproject.org/admin/lists/devel@lists.fedoraproject.org/)
lists for Rawhide issues. Try to at least skim them before doing your
daily Rawhide updates. Look for \'\[rawhide\]\' subjects or reports of
issues. Additionally, if you find a problem and are not sure what to
file bugs against, you can open a discussion there. &#42; Rawhide
kernels are often built with varying degrees of debugging code enabled,
which will result in worse performance and increased resource usage. See
[Kernel Debugging
Strategy](https://fedoraproject.org/wiki/KernelDebugStrategy) for
details on exactly what debugging code is enabled for which kernel
builds. You can disable SLUB debugging for those builds for which it is
enabled by passing &#96;slub_debug=-&#96; to your kernel command line in
&#96;/etc/default/grub&#96; (and re-generating your GRUB config, or just
adding it directly). Additionally, you can run kernels in the [Rawhide
Kernel Nodebug](https://fedoraproject.org/wiki/RawhideKernelNodebug)
repo that have all debugging disabled. &#42; If you are using a
graphical desktop environment in your Rawhide install, you may wish to
install several of them. This allows you to still login and troubleshoot
when your primary desktop environment is not working for some reason.
&#42; Have rescue media handy of the current stable Fedora release for
emergencies.

## History {#_history}

Red Hat Linux \'Raw Hide\'
[announcement](http://lwn.net/1998/0820/rawhide.html).

The name might come from the [song with the same
name](http://en.wikipedia.org/wiki/Rawhide_%28song%29) that starts with
\'Rolling, rolling, rolling, &#8230;\'.

At one time, Rawhide would freeze before release milestones. This was
changed with the [No Frozen Rawhide
Proposal](https://fedoraproject.org/wiki/No_Frozen_Rawhide_Proposal) and
Branched process which we now follow.

# Branched {#_branched}

Branched is the name given to a version of Fedora that has \'branched\'
from the rolling [Rawhide](rawhide.xml) tree and will become the next
stable Fedora release. It consists of a [Fedora development release
tree](http://download.fedoraproject.org/pub/fedora/linux/development/)
named after the Fedora release it will become. It contains builds of all
Fedora packages updated by maintainers with the goal of stabilizing
before release and fixing any release
[Changes](program_management::changes_policy.xml). Full nightly composes
are also produced each night when a Branched release exists, usually
containing all images and installer trees (minus any which fail to
build).

## Goals {#_goals_2}

Branched has the following goals:

&#42; To allow package maintainers to integrate their packages into
Fedora for a stable release. &#42; To allow advanced users access to the
newer packages than stable releases typically provide. &#42; To identify
and fix issues with packages before they reach a stable release of
Fedora.

## Audience {#_audience_2}

Branched is targeted at advanced users, testers and package maintainers.

As a Branched consumer, you should:

&#42; Be willing to update often. Branched doesn't get as many updates
as rawhide (and at times they are frozen), but it still gets a larger
amount than a Stable release. &#42; Be willing and able to troubleshoot
problems. From time to time there are problems with Branched packages,
and you will need strong troubleshooting skills and the ability to
gather information for bug reports. You need a good understanding of dnf
and how to downgrade packages, as well as boot-time troubleshooting.
&#42; Frequent reboots to test new kernel versions and confirm
functionality of the boot process. If you can't reboot often, consider
using a stable release instead. &#42; Be willing and able to report bugs
as you find them and help maintainers gather information to fix them.

If the above doesn't match you, you may wish to use regular stable
Fedora releases.

## Using Branched {#_using_branched}

See the [wiki
template](https://fedoraproject.org/wiki/Template:Rawhide_branched_install_methods)
for instructions on installing and using Branched.

## Communicating {#_communicating}

There are a number of ways to communicate with other Branched users:

### IRC {#_irc_2}

Branched discussion is on topic and welcome in both the
[&#35;fedora-devel](https://web.libera.chat/?channels=&#35;fedora-devel)
and [&#35;fedora-qa](https://web.libera.chat/?channels=&#35;fedora-qa)
IRC channels.

### Mailing Lists {#_mailing_lists_2}

Branched discussion is on topic and welcome in both the
[test](https://lists.fedoraproject.org/admin/lists/test@lists.fedoraproject.org/)
and
[devel](https://lists.fedoraproject.org/admin/lists/devel@lists.fedoraproject.org/)
lists.

### Bugzilla {#_bugzilla_2}

Branched bugs should be reported against the *Fedora* product, and
version that this branched will become and the affected component.
Please do follow [best practices](quick-docs::howto-file-a-bug.xml) when
filing. Remember that IRC and mailing lists are useful to help narrow
down if some behavior is a bug or where to report it, but are themselves
not bug reporting channels. Always file bugs in
[Bugzilla](https://bugzilla.redhat.com).

Note that broken dependencies are mailed to maintainers for each daily
Branched compose where a package has such broken dependencies.
Therefore, it's usually not worth filing a bug for broken dependencies
unless they don't appear in the daily report, or you have a fix or
improvement to suggest.

## Producing Branched {#_producing_branched}

The Branched compose runs every day starting at 09:15 UTC. All branched
package builds at that time that are marked as
[*stable*](quick-docs::repositories.xml) are included in the compose
attempt. If any release-blocking image fails to build as part of the
compose, the compose is considered to have failed. If the compose
completes successfully, a set of automated tests intended to check its
compliance with the [Basic Release
Criteria](https://fedoraproject.org/wiki/Basic_Release_Criteria) are
run. If these tests pass, the compose will be synced out to the mirror
system. Note that during
[freezes](https://fedoraproject.org/wiki/Milestone_freezes) there will
be many days where 0 packages are added to the compose. The Branched
tree is under &#96;development/branched&#96; on the mirrors (when it
exists). You can find a local mirror on the [public mirror
list](https://mirrormanager.fedoraproject.org/mirrors/Fedora/development).
Compose time varies depending on number of changes, but is typically
between 2 and 3 hours.

Branched is subject to various policies during its life cycle. For most
of its existence, it is subject to the [Updates
Policy](fesco::Updates_Policy.xml) and package updates for it are gated
through the [Bodhi](https://fedoraproject.org/wiki/Bodhi) package review
process. At various points of the [Fedora Release Life
Cycle](lifecycle.xml), other freezes, policies and requirements come
into effect, including the [Software String Freeze
Policy](https://fedoraproject.org/wiki/Software_String_Freeze_Policy),
the [freezes](https://fedoraproject.org/wiki/Milestone_freezes), and the
[Change
freezes](program_management::changes_policy.adoc&#35;_change_process_milestones).
See all the above links for more details on exactly what changes may
occur in the Branched tree under what conditions at what times.

Composes are done using the \'mash\' and
[Pungi](https://pagure.io/pungi) tools called from a script maintained
by Fedora Release Engineering. If the base set of packages needed to
compose are broken, the daily compose may fail.

A report for each Branched compose is sent to to the
[test](https://lists.fedoraproject.org/admin/lists/test@lists.fedoraproject.org/)
and
[devel](https://lists.fedoraproject.org/admin/lists/devel@lists.fedoraproject.org/)
lists. This report contains output from the
[compose-changelog](https://pagure.io/compose-utils) tool from the
previous compose as well as a broken dependency report for packages with
broken dependencies. Additionally, private email is sent to maintainers
with packages containing broken dependencies.

Package maintainers should read and follow the [Branched release updates
policy](fesco::Updates_Policy.xml) for building any packages in
Branched.

Until the [Bodhi enabling
point](fesco::Updates_Policy.adoc&#35;updates-testing-activation), you
cannot expect all packages in the Branched tree to be signed. To use
Branched at these times, GPG signature checking in your package
management tool must be disabled.

## Questions and Answers {#_questions_and_answers_2}

&#42;So Branched is very stable and we can all use it?&#42;

Not quite, though it has improved substantially in recent years. Still,
see audience above. There are things that break from time to time, but
if you are able to downgrade or troubleshoot, such issues aren't too
severe, however most users should stick to stable Fedora releases.

&#42;I'm using a stable Fedora release, but I want the newer package for
foo that is only available in Branched. Can I just yum\|dnf install
it?&#42;

No. Mixing releases like this is a very bad idea. Better options are:

&#42; Obtain the src.rpm for the package you wish and try to &#96;mock
\--rebuild&#96; it (which may or may not work depending on
dependencies). &#42; Ask the Fedora maintainer in a bug report to update
the stable version if permitted by policy.

&#42;How can I tell when the branched compose for the day has
finished?&#42;

You can see the reports it sends to the
[test](https://lists.fedoraproject.org/admin/lists/test@lists.fedoraproject.org/)
and
[devel](https://lists.fedoraproject.org/admin/lists/devel@lists.fedoraproject.org/)
lists. You can also watch fedora-messaging for the messages that rawhide
compose has finished.

## Hints and Tips {#_hints_and_tips_2}

&#42; Your package management system can be of great help in diagnosing
and working around issues you find. Do read up and understand: &#96;dnf
downgrade&#96;, &#96;dnf history&#96;, &#96;dnf upgrade&#96;, and
&#96;koji download-build&#96;. &#42; You should update frequently
(preferably every day). This allows you to more easily narrow down when
a problem or issue appeared. If you apply a week of Branched updates at
once, you have many more packages to examine to narrow down issues.
&#42; Reboot often (preferably whenever new kernels arrive). This allows
you to test the boot up process and packages related to it, as well as
newer kernels. Read and understand the Dracut troubleshooting steps.
&#42; Follow the
[test](https://lists.fedoraproject.org/admin/lists/test@lists.fedoraproject.org/)
and
[devel](https://lists.fedoraproject.org/admin/lists/devel@lists.fedoraproject.org/)
lists for Branched issues. Try to at least skim them before doing your
daily Branched updates. Look for \'\[branched\]\' or
\'\[F&lt;N+1&gt;\]\' subjects or reports of issues. Additionally, if you
find a problem and are not sure what to file bugs against, you can open
a discussion there. &#42; At some times, Branched kernels are made with
a large amount of debugging enabled. You can often gain a good deal of
performance by passing &#96;slub_debug=-&#96; to your kernel boot line
in &#96;/etc/grub2.cfg&#96;. Additionally, you can run kernels in the
[Rawhide Kernel
Nodebug](https://fedoraproject.org/wiki/RawhideKernelNodebug) repo that
have all debugging disabled. &#42; If you are using a graphical desktop
environment in your Branched install, you may wish to install several of
them. This allows you to still login and troubleshoot when your primary
desktop environment is not working for some reason. &#42; Have rescue
media handy of the current stable Fedora release for emergencies.

## History {#_history_2}

Branched was created as part of the \'No frozen Rawhide\' proposals:

&#42; [No Frozen Rawhide
Proposal](https://fedoraproject.org/wiki/No_Frozen_Rawhide_Proposal)
&#42; [No Frozen Rawhide
Implementation](https://fedoraproject.org/wiki/No_Frozen_Rawhide_Implementation)

&#42; Upcoming Releases = Fedora Linux {release-version}
:release-version: 43

This is a development landing page for Fedora Linux {release-version}.
User documentation, when available, will be at
[https://docs.fedoraproject.org/en-US/fedora/f{release-version}/](https://docs.fedoraproject.org/en-US/fedora/f{release-version}/)

## Quick links {#_quick_links}

&#42;
[Beta](https://qa.fedoraproject.org/blockerbugs/milestone/{release-version}/beta/buglist)
and
[Final](https://qa.fedoraproject.org/blockerbugs/milestone/{release-version}/final/buglist)
blockers &#42; [Change
Set](https://fedoraproject.org/wiki/Releases/{release-version}/ChangeSet)
&#42; [Release-Blocking Deliverables](f{release-version}/blocking.xml)
&#42;
[Schedule](https://fedorapeople.org/groups/schedule/f-{release-version}/f-{release-version}-key-tasks.html)
&#42; [Spins and Labs](f{release-version}/spins.xml)

## Assorted tracking bugs {#_assorted_tracking_bugs}

&#42; [Failed to
Build](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__&amp;f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F{release-version}FTBFS)
&#42; [Failed to
Install](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__&amp;f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F{release-version}FailsToInstall)
&#42; [Beta
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F{release-version}BetaBlocker)
&#42; [Beta Freeze
Exceptions](https://bugzilla.redhat.com/show_bug.cgi?id=F{release-version}BetaFreezeException)
&#42; [Final
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F{release-version}FinalBlocker)
&#42; [Final Freeze
Exceptions](https://bugzilla.redhat.com/show_bug.cgi?id=F{release-version}FinalFreezeException)
&#42;
[Changes](https://bugzilla.redhat.com/show_bug.cgi?id=F{release-version}Changes)

&#42;&#42;&#42; [Change
Set](https://fedoraproject.org/wiki/Releases/43/ChangeSet) = Fedora
Linux {release-version} release-blocking deliverables :release-version:
43

This is the list of release-blocking deliverables. The goal is to
provide single point of information for Fedora QA, Release Engineering
and other teams.

&#42; QA knows what's release blocking and they know where testing
priority is &#42; Release Engineering knows what's going to be produced
for upcoming release ahead of time &#42; We can avoid last minute
juggling with release at Go/No-Go meeting

This list is static and will be updated when a Change proposal that
includes changing the blocking status is approved by FESCo.

:::: note
::: title
:::

This is not an exhaustive list of Fedora deliverables This page only
lists the blocking deliverables. Teams are encouraged to maintain a list
of non-blocking deliverables for which they are responsible.
::::

:::: note
::: title
:::

Fedora CoreOS deliverables are not included here because they use a
different compose process.
::::

:::: note
::: title
:::

Images starting \'IoT/\' below are found in the separate Fedora-IoT
composes, not the main Fedora composes.
::::

:::: note
::: title
:::

Maximum sizes for compressed raw disk images apply to the uncompressed
size.
::::

+--------------------------------------------------------------+--------+
| Image                                                        | m      |
|                                                              | aximum |
|                                                              | size   |
+==============================================================+========+
| Cloud/aarch64/images                                         |        |
| /Fedora-Cloud-Base-Generic-*RELEASE_MILESTONE*.aarch64.qcow2 |        |
+--------------------------------------------------------------+--------+
| Cloud/x86_64/image                                           |        |
| s/Fedora-Cloud-Base-Generic-*RELEASE_MILESTONE*.x86_64.qcow2 |        |
+--------------------------------------------------------------+--------+
| Cloud/x86_64/images/F                                        |        |
| edora-Cloud-Base-AmazonEC2-*RELEASE_MILESTONE*.x86_64.raw.xz |        |
+--------------------------------------------------------------+--------+
| Container/x86_64/images/Fe                                   | 400 MB |
| dora-Container-Toolbox-*RELEASE_MILESTONE*.x86_64.oci.tar.xz |        |
+--------------------------------------------------------------+--------+
| Container/aarch64/images/Fed                                 | 400 MB |
| ora-Container-Toolbox-*RELEASE_MILESTONE*.aarch64.oci.tar.xz |        |
+--------------------------------------------------------------+--------+
| Everything/x86_64/                                           | 1.2 GB |
| iso/Fedora-Everything-netinst-x86_64-*RELEASE_MILESTONE*.iso |        |
+--------------------------------------------------------------+--------+
| IoT/                                                         |        |
| aarch64/images/Fedora-IoT-*RELEASE_MILESTONE*.aarch64.raw.xz |        |
+--------------------------------------------------------------+--------+
| IoT/aarch                                                    |        |
| 64/iso/Fedora-IoT-IoT-ostree-aarch64-*RELEASE_MILESTONE*.iso |        |
+--------------------------------------------------------------+--------+
| Io                                                           |        |
| T/x86_64/images/Fedora-IoT-*RELEASE_MILESTONE*.x86_64.raw.xz |        |
+--------------------------------------------------------------+--------+
| IoT/x86                                                      |        |
| _64/iso/Fedora-IoT-IoT-ostree-x86_64-*RELEASE_MILESTONE*.iso |        |
+--------------------------------------------------------------+--------+
| Server/a                                                     | 4.7 GB |
| arch64/iso/Fedora-Server-dvd-aarch64-*RELEASE_MILESTONE*.iso |        |
+--------------------------------------------------------------+--------+
| Server/aarch                                                 | 1.2 GB |
| 64/iso/Fedora-Server-netinst-aarch64-*RELEASE_MILESTONE*.iso |        |
+--------------------------------------------------------------+--------+
| Server                                                       | 4.7 GB |
| /x86_64/iso/Fedora-Server-dvd-x86_64-*RELEASE_MILESTONE*.iso |        |
+--------------------------------------------------------------+--------+
| Server/x86                                                   | 1.2 GB |
| _64/iso/Fedora-Server-netinst-x86_64-*RELEASE_MILESTONE*.iso |        |
+--------------------------------------------------------------+--------+
| Spins/aarc                                                   | 8 GB   |
| h64/images/Fedora-Minimal-RELEASE_MILESTONE\_.aarch64.raw.xz |        |
+--------------------------------------------------------------+--------+
| Workstation/aarch64/image                                    | 16 GB  |
| s/Fedora-Workstation-Disk-*RELEASE_MILESTONE*-aarch64.raw.xz |        |
+--------------------------------------------------------------+--------+
| Workstation/x86_6                                            | 3.0 GB |
| 4/iso/Fedora-Workstation-Live-x86_64-*RELEASE_MILESTONE*.iso |        |
+--------------------------------------------------------------+--------+
| KDE/aarch64/image                                            | 16 GB  |
| s/Fedora-KDE-Desktop-Disk-*RELEASE_MILESTONE*.aarch64.raw.xz |        |
+--------------------------------------------------------------+--------+
| KDE/x86_6                                                    | 4.7 GB |
| 4/iso/Fedora-KDE-Desktop-Live-*RELEASE_MILESTONE*.x86_64.iso |        |
+--------------------------------------------------------------+--------+

: F{release-version} Release-Blocking Deliverables

&#42;&#42;&#42;
[Schedule](https://fedorapeople.org/groups/schedule/f-43/f-43-key-tasks.html)
= Fedora Linux {release-version} Spins :release-version: 42

This page lists Spins (and Labs) that will be produced for Fedora Linux
{release-version}.

:::: note
::: title
:::

If the maximum size for a spin needs to be updated, file an issue
against [relval](https://pagure.io/fedora-qa/relval/issues).
::::

+--------------+--------------------------------------+---------------+
| Name         | Description                          | Maximum size  |
+==============+======================================+===============+
| [Astronomy   | The Astronomy Spin is a powerful     | 4 GB          |
| Spin         | completely open-source and free tool |               |
| ](https://fe | for astronomy amateurs and           |               |
| doraproject. | professionals.                       |               |
| org/wiki/Ast |                                      |               |
| ronomy_Spin) |                                      |               |
+--------------+--------------------------------------+---------------+
| [Budgie      | Budgie Desktop's goal is to be a     |               |
| Spin](http   | feature-rich and modern desktop that |               |
| s://fedorapr | provides unique ways of interacting  |               |
| oject.org/wi | with the system while being          |               |
| ki/Changes/F | approachable to many users with its  |               |
| edoraBudgie) | default more traditional look and    |               |
|              | feel.                                |               |
+--------------+--------------------------------------+---------------+
| [Cinnamon    | The Fedora Cinnamon spin provides    | 2.6 GB        |
| Spin](https  | advanced innovative features and a   |               |
| ://fedorapro | traditional user experience.         |               |
| ject.org/wik |                                      |               |
| i/Changes/Ci |                                      |               |
| nnamon_Spin) |                                      |               |
+--------------+--------------------------------------+---------------+
| [Design      | The Fedora Design Suite includes     | 4 GB          |
| Sui          | well-selected applications, fitting  |               |
| te](https:// | a variety of use cases. Whether you  |               |
| fedoraprojec | decide to work on publishing         |               |
| t.org/wiki/D | documents, creating images and       |               |
| esign_Suite) | pictures or even 3D content, the     |               |
|              | Design Suite has a fitting tool.     |               |
+--------------+--------------------------------------+---------------+
| [Fedora      | Fedora Jam is a full-featured audio  | 4 GB          |
| Jam](https:  | creation spin. It includes all the   |               |
| //fedoraproj | tools needed to help create the      |               |
| ect.org/wiki | music you want, anything from        |               |
| /Fedora_jam) | classical to jazz to Heavy metal.    |               |
|              | Included in Fedora jam is full       |               |
|              | support for JACK and JACK to         |               |
|              | PulseAudio bridging.                 |               |
+--------------+--------------------------------------+---------------+
| [Games       | The Fedora Games spin offers a       | 16 GB         |
| Spin](https: | perfect show-case of the best games  |               |
| //fedoraproj | available in Fedora. The included    |               |
| ect.org/wiki | games span several genres, from      |               |
| /Games_Spin) | first person shooters to real-time   |               |
|              | and turn based strategy games to     |               |
|              | puzzle games. Not all the games      |               |
|              | available in Fedora are included on  |               |
|              | this spin, but trying out this spin  |               |
|              | will give you a fair impression of   |               |
|              | Fedora's abilities to run great      |               |
|              | games.                               |               |
+--------------+--------------------------------------+---------------+
| [i3          | An Fedora Spin shipping the popular  |               |
| Spin](https  | i3 window manager. This Spin is the  |               |
| ://docs.fedo | first Fedora Spin to feature a       |               |
| raproject.or | tiling/window manager instead of a   |               |
| g/en-US/i3/) | traditional desktop environment.     |               |
+--------------+--------------------------------------+---------------+
| [Kinoite]    | An rpm-ostree-based KDE Plasma       |               |
| (https://kin | desktop                              |               |
| oite.fedorap |                                      |               |
| roject.org/) |                                      |               |
+--------------+--------------------------------------+---------------+
| [LXDE        | The Fedora LXDE spin is meant to be  | 2 GB          |
| Spin](https  | a lightweight, but yet complete      |               |
| ://fedorapro | desktop based on LXDE, the           |               |
| ject.org/wik | Lightweight X11 Desktop Environment. |               |
| i/LXDE_Spin) |                                      |               |
+--------------+--------------------------------------+---------------+
| [MATE-Compiz | The Fedora MATE spin is meant to     | 3 GB          |
| Spin](       | provide users with a classic,        |               |
| https://fedo | lightweight and traditional looking  |               |
| raproject.or | desktop.                             |               |
| g/wiki/MATE- |                                      |               |
| Compiz_Spin) |                                      |               |
+--------------+--------------------------------------+---------------+
| [Mobility    | A Wayland shell for mobile devices   |               |
| Phosh        | based on Gnome                       |               |
| Image        |                                      |               |
| ](https://fe |                                      |               |
| doraproject. |                                      |               |
| org/wiki/Cha |                                      |               |
| nges/Mobilit |                                      |               |
| yPhoshImage) |                                      |               |
+--------------+--------------------------------------+---------------+
| [Python      | The Fedora Python Classroom Lab      | 2 GB          |
| Classroom    | makes it even easier for teachers    |               |
| Lab          | and instructors to use Fedora in     |               |
| ](https://fe | their classrooms or workshops. Ready |               |
| doraproject. | to use operating system with         |               |
| org/wiki/Cha | important stuff pre-installed -      |               |
| nges/PythonC | either with GNOME or as a headless   |               |
| lassroomLab) | environment for Docker or Vagrant.   |               |
+--------------+--------------------------------------+---------------+
| [QA Test Day | The purpose of this spin is to       |               |
| Spin](       | provide a model kickstart file to    |               |
| https://fedo | people organizing Test Days that can |               |
| raproject.or | easily be tweaked for specific Test  |               |
| g/wiki/QA_Te | Days.                                |               |
| st_Day_Spin) |                                      |               |
+--------------+--------------------------------------+---------------+
| [Robotics    | Create a spin that provides as many  | 4 GB          |
| Spi          | robotics related packages to the     |               |
| n](https://f | spin to maximize out-of-the-box      |               |
| edoraproject | usable hardware and software.        |               |
| .org/wiki/Ro | Eventually provide out-of-the-box    |               |
| botics_Spin) | simulation environment for one or    |               |
|              | more scenarios.                      |               |
+--------------+--------------------------------------+---------------+
| [Fedora      | Fedora Scientific spin aims to       | 5 GB          |
| Scientific]  | create a Fedora desktop based spin   |               |
| (https://fed | which will have a generic toolset    |               |
| oraproject.o | for Linux users whose                |               |
| rg/wiki/Scie | profession/studies involve           |               |
| ntific_Spin) | scientific research. To learn more,  |               |
|              | see the documentation.               |               |
+--------------+--------------------------------------+---------------+
| [Security    | The Fedora Security Spin provides a  | 2 GB          |
| Spi          | safe test environment to work on     |               |
| n](https://f | security auditing, forensics, system |               |
| edoraproject | rescue and teaching security testing |               |
| .org/wiki/Se | methodologies in universities and    |               |
| curity_Spin) | other organizations. The spin is     |               |
|              | maintained by a community of         |               |
|              | security testers and developers. It  |               |
|              | comes with the clean and fast LXDE   |               |
|              | Desktop Environment and a customized |               |
|              | menu that provides all the           |               |
|              | instruments needed to follow a       |               |
|              | proper test path for security        |               |
|              | testing or to rescue a broken        |               |
|              | system. The Live image has been      |               |
|              | crafted to make it possible to       |               |
|              | install software while running, and  |               |
|              | if you are running it from a USB     |               |
|              | stick created with the Live Media    |               |
|              | Writer's overlay feature, you can    |               |
|              | install and update software and save |               |
|              | your test results permanently.       |               |
|              | Additional information is available  |               |
|              | at the Security Spin home page and   |               |
|              | its wiki page.                       |               |
+--------------+--------------------------------------+---------------+
| [Sugar on a  | Sugar on a Stick (SoaS) enables      | 2 GB          |
| Stick        | children to reclaim computers. SoaS  |               |
| Spin](       | aims to make it easy for children,   |               |
| https://fedo | parents, or local deployers to       |               |
| raproject.or | provide each student with a small    |               |
| g/wiki/Sugar | device (USB stick or thumbdrive)     |               |
| _on_a_Stick) | that can start any computer with the |               |
|              | student's personalized Sugar         |               |
|              | environment. We would like to see    |               |
|              | Sugar's presence, journal, and       |               |
|              | clarity principles usable on any     |               |
|              | machine --- at school, at home, and  |               |
|              | anywhere there is a suitable         |               |
|              | computing device.                    |               |
+--------------+--------------------------------------+---------------+
| [Sway        | Sway is a tiling Wayland compositor  |               |
| Spin](https  | similar to the i3 window manager.    |               |
| ://fedorapro |                                      |               |
| ject.org/wik |                                      |               |
| i/SIGs/Sway) |                                      |               |
+--------------+--------------------------------------+---------------+
| [Xfce        | The Fedora Xfce spin showcases the   | 2 GB          |
| Spin](https  | Xfce desktop, which aims to be fast  |               |
| ://fedorapro | and lightweight, while still being   |               |
| ject.org/wik | visually appealing and user          |               |
| i/Xfce_Spin) | friendly. Xfce is a full fledged     |               |
|              | desktop using the freedesktop.org    |               |
|              | standard.                            |               |
+--------------+--------------------------------------+---------------+
| [LXQt        | The Fedora LXQt spin is meant to be  | 2 GB          |
| Spin](h      | a lightweight, but yet complete      |               |
| ttps://fedor | desktop based on LXQt. LXQt is a     |               |
| aproject.org | fast and stable desktop environment  |               |
| /wiki/Change | already usable on production         |               |
| s/LXQt_Spin) | desktops. It will not get in the     |               |
|              | user's way. It is focused on being a |               |
|              | Classic Desktop with a modern Look   |               |
|              | &amp; Feel.                          |               |
+--------------+--------------------------------------+---------------+

: F{release-version} Spins and Labs

&#42; Supported Releases = Fedora Linux {release-version}
:release-version: 42

This is a development landing page for Fedora Linux {release-version}.
User documentation, when available, will be at
[https://docs.fedoraproject.org/en-US/fedora/f{release-version}/](https://docs.fedoraproject.org/en-US/fedora/f{release-version}/)

## Quick links {#_quick_links_2}

&#42;
[Beta](https://qa.fedoraproject.org/blockerbugs/milestone/{release-version}/beta/buglist)
and
[Final](https://qa.fedoraproject.org/blockerbugs/milestone/{release-version}/final/buglist)
blockers &#42; [Change
Set](https://fedoraproject.org/wiki/Releases/{release-version}/ChangeSet)
&#42; [Release-Blocking Deliverables](f{release-version}/blocking.xml)
&#42;
[Schedule](https://fedorapeople.org/groups/schedule/f-{release-version}/f-{release-version}-key-tasks.html)
&#42; [Spins and Labs](f{release-version}/spins.xml)

## Assorted tracking bugs {#_assorted_tracking_bugs_2}

&#42; [Failed to
Build](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__&amp;f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F{release-version}FTBFS)
&#42; [Failed to
Install](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__&amp;f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F{release-version}FailsToInstall)
&#42; [Beta
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F{release-version}BetaBlocker)
&#42; [Beta Freeze
Exceptions](https://bugzilla.redhat.com/show_bug.cgi?id=F{release-version}BetaFreezeException)
&#42; [Final
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F{release-version}FinalBlocker)
&#42; [Final Freeze
Exceptions](https://bugzilla.redhat.com/show_bug.cgi?id=F{release-version}FinalFreezeException)
&#42;
[Changes](https://bugzilla.redhat.com/show_bug.cgi?id=F{release-version}Changes)

# Fedora Linux {release-version} {#_fedora_linux_release_version}

This is a development landing page for Fedora Linux 41. User
documentation, when available, will be at
<https://docs.fedoraproject.org/en-US/fedora/f41/>

## Quick links {#_quick_links_3}

&#42;
[Beta](https://qa.fedoraproject.org/blockerbugs/milestone/41/beta/buglist)
and
[Final](https://qa.fedoraproject.org/blockerbugs/milestone/41/final/buglist)
blockers &#42; [Change
Set](https://fedoraproject.org/wiki/Releases/41/ChangeSet) &#42;
[Release-Blocking Deliverables](f41/blocking.xml) &#42;
[Schedule](https://fedorapeople.org/groups/schedule/f-41/f-41-key-tasks.html)
&#42; [Spins and Labs](f41/spins.xml)

## Assorted tracking bugs {#_assorted_tracking_bugs_3}

&#42; [Failed to
Build](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__&amp;f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F41FTBFS)
&#42; [Failed to
Install](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__&amp;f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F41FailsToInstall)
&#42; [Beta
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F41BetaBlocker)
&#42; [Beta Freeze
Exceptions](https://bugzilla.redhat.com/show_bug.cgi?id=F41BetaFreezeException)
&#42; [Final
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F41FinalBlocker)
&#42; [Final Freeze
Exceptions](https://bugzilla.redhat.com/show_bug.cgi?id=F41FinalFreezeException)
&#42; [Changes](https://bugzilla.redhat.com/show_bug.cgi?id=F41Changes)

# End of Life Releases {#_end_of_life_releases}

The Fedora Project maintains each release of Fedora Linux according to
the [Release Life Cycle](../lifecycle.xml). The following releases have
reached End of Life. They are no longer maintained and do not receive
any updates. To get the latest release, visit [Get
Fedora](https://getfedora.org). If you want to upgrade your old system,
please check [Upgrading to a new release of Fedora
Linux](quick-docs::upgrading.xml) page for details.

## Unsupported Fedora Linux releases {#_unsupported_fedora_linux_releases}

+----------------------+----------------------+-----------------------+
| Release              | EOL since            | Maintained for        |
+======================+======================+=======================+
| Fedora Linux 41      | 2025-12-15           | 412 days              |
+----------------------+----------------------+-----------------------+
| Fedora Linux 40      | 2025-05-13           | 385 days              |
+----------------------+----------------------+-----------------------+
| Fedora Linux 39      | 2024-11-26           | 385 days              |
+----------------------+----------------------+-----------------------+
| Fedora Linux 38      | 2024-05-21           | 399 days              |
+----------------------+----------------------+-----------------------+
| Fedora Linux 37      | 2023-12-05           | 385 days              |
+----------------------+----------------------+-----------------------+
| Fedora Linux 36      | 2023-05-16           | 371 days              |
+----------------------+----------------------+-----------------------+
| Fedora Linux 35      | 2022-12-13           | 406 days              |
+----------------------+----------------------+-----------------------+
| Fedora Linux 34      | 2022-06-07           | 406 days              |
+----------------------+----------------------+-----------------------+
| Fedora Linux 33      | 2021-11-30           | 399 days              |
+----------------------+----------------------+-----------------------+
| Fedora Linux 32      | 2021-05-25           | 392 days              |
+----------------------+----------------------+-----------------------+
| Fedora Linux 31      | 2020-11-24           | 392 days              |
+----------------------+----------------------+-----------------------+
| Fedora Linux 30      | 2020-05-26           | 392 days              |
+----------------------+----------------------+-----------------------+
| Fedora Linux 29      | 2019-11-26           | 392 days              |
+----------------------+----------------------+-----------------------+
| Fedora Linux 28      | 2019-05-28           | 392 days              |
+----------------------+----------------------+-----------------------+
| Fedora Linux 27      | 2018-11-30           | 381 days              |
+----------------------+----------------------+-----------------------+
| Fedora Linux 26      | 2018-05-29           | 322 days              |
+----------------------+----------------------+-----------------------+
| Fedora Linux 25      | 2017-12-12           | 385 days              |
+----------------------+----------------------+-----------------------+
| Fedora Linux 24      | 2017-08-08           | 413 days              |
+----------------------+----------------------+-----------------------+
| Fedora Linux 23      | 2016-12-20           | 413 days              |
+----------------------+----------------------+-----------------------+
| Fedora Linux 22      | 2016-07-19           | 420 days              |
+----------------------+----------------------+-----------------------+
| Fedora Linux 21      | 2015-12-01           | 357 days              |
+----------------------+----------------------+-----------------------+
| Fedora Linux 20      | 2015-06-23           | 553 days              |
+----------------------+----------------------+-----------------------+
| Fedora Linux 19      | 2015-01-06           | 553 days              |
+----------------------+----------------------+-----------------------+
| Fedora Linux 18      | 2014-01-14           | 364 days              |
+----------------------+----------------------+-----------------------+
| Fedora Linux 17      | 2013-07-30           | 427 days              |
+----------------------+----------------------+-----------------------+
| Fedora Linux 16      | 2013-02-12           | 462 days              |
+----------------------+----------------------+-----------------------+
| Fedora Linux 15      | 2012-06-26           | 399 days              |
+----------------------+----------------------+-----------------------+
| Fedora Linux 14      | 2011-12-09           | 402 days              |
+----------------------+----------------------+-----------------------+
| Fedora Linux 13      | 2011-06-24           | 395 days              |
+----------------------+----------------------+-----------------------+
| Fedora Linux 12      | 2010-12-02           | 380 days              |
+----------------------+----------------------+-----------------------+
| Fedora Linux 11      | 2010-06-25           | 381 days              |
+----------------------+----------------------+-----------------------+
| Fedora Linux 10      | 2009-12-17           | 387 days              |
+----------------------+----------------------+-----------------------+
| Fedora Linux 9       | 2009-07-10           | 423 days              |
+----------------------+----------------------+-----------------------+
| Fedora Linux 8       | 2009-01-07           | 426 days              |
+----------------------+----------------------+-----------------------+
| Fedora Linux 7       | 2008-06-13           | 379 days              |
+----------------------+----------------------+-----------------------+
| Fedora Core 6        | 2007-12-07           | 409 days              |
+----------------------+----------------------+-----------------------+
| Fedora Core 5        | 2007-07-02           | 469 days              |
+----------------------+----------------------+-----------------------+
| Fedora Core 4        | 2006-08-07           | 420 days              |
+----------------------+----------------------+-----------------------+
| Fedora Core 3        | 2006-01-16           | 434 days              |
+----------------------+----------------------+-----------------------+
| Fedora Core 2        | 2005-04-11           | 328 days              |
+----------------------+----------------------+-----------------------+
| Fedora Core 1        | 2004-09-20           | 320 days              |
+----------------------+----------------------+-----------------------+

: EOL Releases

## More information {#_more_information}

For more information on how the End of Life process is managed, see the
[Release Engineering
SOP](https://docs.pagure.org/releng/sop_end_of_life.html) and [PgM
Guide](program_management::pgm_guide/release_process.adoc&#35;_eol_day).

# Fedora Linux 41 {#_fedora_linux_41}

This is a development landing page for Fedora Linux 40. User
documentation, when available, will be at
<https://docs.fedoraproject.org/en-US/fedora/f40/>

## Quick links {#_quick_links_4}

&#42;
[Beta](https://qa.fedoraproject.org/blockerbugs/milestone/40/beta/buglist)
and
[Final](https://qa.fedoraproject.org/blockerbugs/milestone/40/final/buglist)
blockers &#42; [Change
Set](https://fedoraproject.org/wiki/Releases/40/ChangeSet) &#42;
[Release-Blocking Deliverables](f40/blocking.xml) &#42;
[Schedule](https://fedorapeople.org/groups/schedule/f-40/f-40-key-tasks.html)
&#42; [Spins and Labs](f40/spins.xml)

## Assorted tracking bugs {#_assorted_tracking_bugs_4}

&#42; [Failed to
Build](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__&amp;f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F40FTBFS)
&#42; [Failed to
Install](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__&amp;f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F40FailsToInstall)
&#42; [Beta
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F40BetaBlocker)
&#42; [Beta Freeze
Exceptions](https://bugzilla.redhat.com/show_bug.cgi?id=F40BetaFreezeException)
&#42; [Final
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F40FinalBlocker)
&#42; [Final Freeze
Exceptions](https://bugzilla.redhat.com/show_bug.cgi?id=F40FinalFreezeException)
&#42; [Changes](https://bugzilla.redhat.com/show_bug.cgi?id=F40Changes)

# Fedora Linux 40 {#_fedora_linux_40}

This is a development landing page for Fedora Linux 39. User
documentation, when available, will be at
<https://docs.fedoraproject.org/en-US/fedora/f39/>

## Quick links {#_quick_links_5}

&#42;
[Beta](https://qa.fedoraproject.org/blockerbugs/milestone/39/beta/buglist)
and
[Final](https://qa.fedoraproject.org/blockerbugs/milestone/39/final/buglist)
blockers &#42; [Change
Set](https://fedoraproject.org/wiki/Releases/39/ChangeSet) &#42;
[Release-Blocking Deliverables](f39/blocking.xml) &#42;
[Schedule](https://fedorapeople.org/groups/schedule/f-39/f-39-key-tasks.html)
&#42; [Spins and Labs](f39/spins.xml)

## Assorted tracking bugs {#_assorted_tracking_bugs_5}

&#42; [Failed to
Build](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__&amp;f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F39FTBFS)
&#42; [Failed to
Install](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__&amp;f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F39FailsToInstall)
&#42; [Beta
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F39BetaBlocker)
&#42; [Beta Freeze
Exceptions](https://bugzilla.redhat.com/show_bug.cgi?id=F39BetaFreezeException)
&#42; [Final
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F39FinalBlocker)
&#42; [Final Freeze
Exceptions](https://bugzilla.redhat.com/show_bug.cgi?id=F39FinalFreezeException)
&#42; [Changes](https://bugzilla.redhat.com/show_bug.cgi?id=F39Changes)

# Fedora Linux 39 {#_fedora_linux_39}

This is a development landing page for Fedora Linux 38. User
documentation, when available, will be at
<https://docs.fedoraproject.org/en-US/fedora/f38/>

## Quick links {#_quick_links_6}

&#42;
[Beta](https://qa.fedoraproject.org/blockerbugs/milestone/38/beta/buglist)
and
[Final](https://qa.fedoraproject.org/blockerbugs/milestone/38/final/buglist)
blockers &#42; [Change
Set](https://fedoraproject.org/wiki/Releases/38/ChangeSet) &#42;
[Release-Blocking Deliverables](f38/blocking.xml) &#42;
[Schedule](https://fedorapeople.org/groups/schedule/f-38/f-38-key-tasks.html)
&#42; [Spins and Labs](f38/spins.xml)

## Assorted tracking bugs {#_assorted_tracking_bugs_6}

&#42; [Failed to
Build](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__&amp;f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F38FTBFS)
&#42; [Failed to
Install](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__&amp;f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F38FailsToInstall)
&#42; [Beta
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F38BetaBlocker)
&#42; [Beta Freeze
Exceptions](https://bugzilla.redhat.com/show_bug.cgi?id=F38BetaFreezeException)
&#42; [Final
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F38FinalBlocker)
&#42; [Final Freeze
Exceptions](https://bugzilla.redhat.com/show_bug.cgi?id=F38FinalFreezeException)
&#42; [Changes](https://bugzilla.redhat.com/show_bug.cgi?id=F38Changes)

# Fedora Linux 38 {#_fedora_linux_38}

This is a development landing page for Fedora Linux 37. User
documentation, when available, will be at
<https://docs.fedoraproject.org/en-US/fedora/f37/>

## Quick links {#_quick_links_7}

&#42;
[Beta](https://qa.fedoraproject.org/blockerbugs/milestone/37/beta/buglist)
and
[Final](https://qa.fedoraproject.org/blockerbugs/milestone/37/final/buglist)
blockers &#42; [Change
Set](https://fedoraproject.org/wiki/Releases/37/ChangeSet) &#42;
[Release-Blocking Deliverables](f37/blocking.xml) &#42;
[Schedule](https://fedorapeople.org/groups/schedule/f-37/f-37-key-tasks.html)
&#42; [Spins and Labs](f37/spins.xml)

## Assorted tracking bugs {#_assorted_tracking_bugs_7}

&#42; [Failed to
Build](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__&amp;f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F37FTBFS)
&#42; [Failed to
Install](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__&amp;f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F37FailsToInstall)
&#42; [Beta
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F37BetaBlocker)
&#42; [Beta Freeze
Exceptions](https://bugzilla.redhat.com/show_bug.cgi?id=F37BetaFreezeException)
&#42; [Final
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F37FinalBlocker)
&#42; [Final Freeze
Exceptions](https://bugzilla.redhat.com/show_bug.cgi?id=F37FinalFreezeException)
&#42; [Changes](https://bugzilla.redhat.com/show_bug.cgi?id=F37Changes)

# Fedora Linux 37 {#_fedora_linux_37}

This is a development landing page for Fedora Linux 36. User
documentation, when available, will be at
<https://docs.fedoraproject.org/en-US/fedora/f36/>

## Quick links {#_quick_links_8}

&#42;
[Beta](https://qa.fedoraproject.org/blockerbugs/milestone/36/beta/buglist)
and
[Final](https://qa.fedoraproject.org/blockerbugs/milestone/36/final/buglist)
blockers &#42; [Change
Set](https://fedoraproject.org/wiki/Releases/36/ChangeSet) &#42;
[Release-Blocking Deliverables](f36/blocking.xml) &#42;
[Schedule](https://fedorapeople.org/groups/schedule/f-36/f-36-key-tasks.html)
&#42; [Spins and Labs](f36/spins.xml)

## Assorted tracking bugs {#_assorted_tracking_bugs_8}

&#42; [Failed to
Build](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__&amp;f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F36FTBFS)
&#42; [Failed to
Install](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__&amp;f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F36FailsToInstall)
&#42; [Beta
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F36BetaBlocker)
&#42; [Beta Freeze
Exceptions](https://bugzilla.redhat.com/show_bug.cgi?id=F36BetaFreezeException)
&#42; [Final
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F36FinalBlocker)
&#42; [Final Freeze
Exceptions](https://bugzilla.redhat.com/show_bug.cgi?id=F36FinalFreezeException)
&#42; [Changes](https://bugzilla.redhat.com/show_bug.cgi?id=F36Changes)

# Fedora Linux 36 {#_fedora_linux_36}

This is a development landing page for Fedora Linux 35. User
documentation, when available, will be at
<https://docs.fedoraproject.org/en-US/fedora/f35/>

## Quick links {#_quick_links_9}

&#42;
[Beta](https://qa.fedoraproject.org/blockerbugs/milestone/35/beta/buglist)
and
[Final](https://qa.fedoraproject.org/blockerbugs/milestone/35/final/buglist)
blockers &#42; [Change
Set](https://fedoraproject.org/wiki/Releases/35/ChangeSet) &#42;
[Release-Blocking Deliverables](f35/blocking.xml) &#42;
[Schedule](https://fedorapeople.org/groups/schedule/f-35/f-35-key-tasks.html)
&#42; [Spins and Labs](f35/spins.xml)

## Assorted tracking bugs {#_assorted_tracking_bugs_9}

&#42; [Failed to
Build](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__&amp;f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F35FTBFS)
&#42; [Failed to
Install](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__&amp;f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F35FailsToInstall)
&#42; [Beta
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F35BetaBlocker)
&#42; [Beta Freeze
Exceptions](https://bugzilla.redhat.com/show_bug.cgi?id=F35BetaFreezeException)
&#42; [Final
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F35FinalBlocker)
&#42; [Final Freeze
Exceptions](https://bugzilla.redhat.com/show_bug.cgi?id=F35FinalFreezeException)
&#42; [Changes](https://bugzilla.redhat.com/show_bug.cgi?id=F35Changes)

# Fedora Linux 35 {#_fedora_linux_35}

This is a development landing page for Fedora Linux 34. User
documentation, when available, will be at
<https://docs.fedoraproject.org/en-US/fedora/f34/>

## Quick links {#_quick_links_10}

&#42;
[Beta](https://qa.fedoraproject.org/blockerbugs/milestone/34/beta/buglist)
and
[Final](https://qa.fedoraproject.org/blockerbugs/milestone/34/final/buglist)
blockers &#42; [Change
Set](https://fedoraproject.org/wiki/Releases/34/ChangeSet) &#42;
[Release-Blocking Deliverables](f34/blocking.xml) &#42;
[Schedule](https://fedorapeople.org/groups/schedule/f-34/f-34-key-tasks.html)
&#42; [Spins and Labs](f34/spins.xml)

## Assorted tracking bugs {#_assorted_tracking_bugs_10}

&#42; [Failed to
Build](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__&amp;f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F34FTBFS)
&#42; [Failed to
Install](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__&amp;f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F34FailsToInstall)
&#42; [Beta
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F34BetaBlocker)
&#42; [Beta Freeze
Exceptions](https://bugzilla.redhat.com/show_bug.cgi?id=F34BetaFreezeException)
&#42; [Final
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F34FinalBlocker)
&#42; [Final Freeze
Exceptions](https://bugzilla.redhat.com/show_bug.cgi?id=F34FinalFreezeException)
&#42; [Changes](https://bugzilla.redhat.com/show_bug.cgi?id=F34Changes)

# Fedora Linux 34 {#_fedora_linux_34}

This is a development landing page for Fedora Linux 33. User
documentation, when available, will be at
<https://docs.fedoraproject.org/en-US/fedora/f33/>

## Quick links {#_quick_links_11}

&#42;
[Beta](https://qa.fedoraproject.org/blockerbugs/milestone/33/beta/buglist)
and
[Final](https://qa.fedoraproject.org/blockerbugs/milestone/33/final/buglist)
blockers &#42; [Change
Set](https://fedoraproject.org/wiki/Releases/33/ChangeSet) &#42;
[Release-Blocking
Deliverables](https://fedoraproject.org/wiki/Releases/33/ReleaseBlocking)
&#42;
[Schedule](https://fedorapeople.org/groups/schedule/f-33/f-33-key-tasks.html)
&#42; [Spins and Labs](https://fedoraproject.org/wiki/Releases/33/Spins)

## Assorted tracking bugs {#_assorted_tracking_bugs_11}

&#42; [Failed to
Build](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__&amp;f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F33FTBFS)
&#42; [Failed to
Install](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__&amp;f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F33FailsToInstall)
&#42; [Beta
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F33BetaBlocker)
&#42; [Beta Freeze
Exceptions](https://bugzilla.redhat.com/show_bug.cgi?id=F33BetaFreezeException)
&#42; [Final
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F33FinalBlocker)
&#42; [Final Freeze
Exceptions](https://bugzilla.redhat.com/show_bug.cgi?id=F33FinalFreezeException)
&#42; [Changes](https://bugzilla.redhat.com/show_bug.cgi?id=F33Changes)

# Fedora Linux 33 {#_fedora_linux_33}

This is a development landing page for Fedora Linux 32. User
documentation, when available, will be at
<https://docs.fedoraproject.org/en-US/fedora/f32/>

## Quick links {#_quick_links_12}

&#42;
[Beta](https://qa.fedoraproject.org/blockerbugs/milestone/32/beta/buglist)
and
[Final](https://qa.fedoraproject.org/blockerbugs/milestone/32/final/buglist)
blockers &#42; [Change
Set](https://fedoraproject.org/wiki/Releases/32/ChangeSet) &#42;
[Release-Blocking
Deliverables](https://fedoraproject.org/wiki/Releases/32/ReleaseBlocking)
&#42;
[Schedule](https://fedorapeople.org/groups/schedule/f-32/f-32-key-tasks.html)
&#42; [Spins and Labs](https://fedoraproject.org/wiki/Releases/32/Spins)

## Assorted tracking bugs {#_assorted_tracking_bugs_12}

&#42; [Failed to
Build](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__&amp;f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F32FTBFS)
&#42; [Failed to
Install](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__&amp;f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F32FailsToInstall)
&#42; [Beta
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F32BetaBlocker)
&#42; [Beta Freeze
Exceptions](https://bugzilla.redhat.com/show_bug.cgi?id=F32BetaFreezeException)
&#42; [Final
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F32FinalBlocker)
&#42; [Final Freeze
Exceptions](https://bugzilla.redhat.com/show_bug.cgi?id=F32FinalFreezeException)

# Fedora Linux 32 {#_fedora_linux_32}

This is a development landing page for Fedora Linux 31. User
documentation, when available, will be at
<https://docs.fedoraproject.org/en-US/fedora/f31/>

## Quick links {#_quick_links_13}

&#42;
[Beta](https://qa.fedoraproject.org/blockerbugs/milestone/31/beta/buglist)
and
[Final](https://qa.fedoraproject.org/blockerbugs/milestone/31/final/buglist)
blockers &#42; [Change
Set](https://fedoraproject.org/wiki/Releases/31/ChangeSet) &#42;
[Release-Blocking
Deliverables](https://fedoraproject.org/wiki/Releases/31/ReleaseBlocking)
&#42;
[Schedule](https://fedorapeople.org/groups/schedule/f-31/f-31-key-tasks.html)
&#42; [Spins and Labs](https://fedoraproject.org/wiki/Releases/31/Spins)

## Assorted tracking bugs {#_assorted_tracking_bugs_13}

&#42; [Failed to
Build](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__&amp;f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F31FTBFS)
&#42; [Failed to
Install](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__&amp;f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F31FailsToInstall)
&#42; [Beta
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F31BetaBlocker)
&#42; [Beta Freeze
Exceptions](https://bugzilla.redhat.com/show_bug.cgi?id=F31BetaFreezeException)
&#42; [Final
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F31FinalBlocker)
&#42; [Final Freeze
Exceptions](https://bugzilla.redhat.com/show_bug.cgi?id=F31FinalFreezeException)

# Fedora Linux 31 {#_fedora_linux_31}

This is a development landing page for Fedora Linux 30. User
documentation, when available, will be at
<https://docs.fedoraproject.org/en-US/fedora/f30/>

## Quick links {#_quick_links_14}

&#42;
[Beta](https://qa.fedoraproject.org/blockerbugs/milestone/30/beta/buglist)
and
[Final](https://qa.fedoraproject.org/blockerbugs/milestone/30/final/buglist)
blockers &#42; [Change
Set](https://fedoraproject.org/wiki/Releases/30/ChangeSet) &#42;
[Release-Blocking
Deliverables](https://fedoraproject.org/wiki/Releases/30/ReleaseBlocking)
&#42;
[Schedule](https://fedorapeople.org/groups/schedule/f-30/f-30-key-tasks.html)
&#42; [Spins and Labs](https://fedoraproject.org/wiki/Releases/30/Spins)

## Assorted tracking bugs {#_assorted_tracking_bugs_14}

&#42; [Failed to
Build](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__&amp;f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F30FTBFS)
&#42; [Failed to
Install](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__&amp;f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F30FailsToInstall)
&#42; [Beta
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F30BetaBlocker)
&#42; [Beta Freeze
Exceptions](https://bugzilla.redhat.com/show_bug.cgi?id=F30BetaFreezeException)
&#42; [Final
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F30FinalBlocker)
&#42; [Final Freeze
Exceptions](https://bugzilla.redhat.com/show_bug.cgi?id=F30FinalFreezeException)

# Fedora Linux 30 {#_fedora_linux_30}

This is a development landing page for Fedora Linux 29. User
documentation, when available, will be at
<https://docs.fedoraproject.org/en-US/fedora/f29/>

## Quick links {#_quick_links_15}

&#42;
[Beta](https://qa.fedoraproject.org/blockerbugs/milestone/29/beta/buglist)
and
[Final](https://qa.fedoraproject.org/blockerbugs/milestone/29/final/buglist)
blockers &#42; [Change
Set](https://fedoraproject.org/wiki/Releases/29/ChangeSet) &#42;
[Release-Blocking
Deliverables](https://fedoraproject.org/wiki/Releases/29/ReleaseBlocking)
&#42;
[Schedule](https://fedorapeople.org/groups/schedule/f-29/f-29-key-tasks.html)
&#42; [Spins and Labs](https://fedoraproject.org/wiki/Releases/29/Spins)

## Assorted tracking bugs {#_assorted_tracking_bugs_15}

&#42; [Failed to
Build](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__&amp;f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F29FTBFS)
&#42; [Failed to
Install](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__&amp;f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F29FailsToInstall)
&#42; [Beta
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F29BetaBlocker)
&#42; [Beta Freeze
Exceptions](https://bugzilla.redhat.com/show_bug.cgi?id=F29BetaFreezeException)
&#42; [Final
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F29FinalBlocker)
&#42; [Final Freeze
Exceptions](https://bugzilla.redhat.com/show_bug.cgi?id=F29FinalFreezeException)

# Fedora Linux 29 {#_fedora_linux_29}

This is a development landing page for Fedora Linux 28. User
documentation, when available, will be at
<https://docs.fedoraproject.org/en-US/fedora/f28/>

## Quick links {#_quick_links_16}

&#42;
[Beta](https://qa.fedoraproject.org/blockerbugs/milestone/28/beta/buglist)
and
[Final](https://qa.fedoraproject.org/blockerbugs/milestone/28/final/buglist)
blockers &#42; [Change
Set](https://fedoraproject.org/wiki/Releases/28/ChangeSet) &#42;
[Release-Blocking
Deliverables](https://fedoraproject.org/wiki/Releases/28/ReleaseBlocking)
&#42;
[Schedule](https://fedorapeople.org/groups/schedule/f-28/f-28-key-tasks.html)
&#42; [Spins and Labs](https://fedoraproject.org/wiki/Releases/28/Spins)

## Assorted tracking bugs {#_assorted_tracking_bugs_16}

&#42; [Failed to
Build](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__&amp;f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F28FTBFS)
&#42; [Failed to
Install](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__&amp;f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F28FailsToInstall)
&#42; [Beta
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F28BetaBlocker)
&#42; [Beta Freeze
Exceptions](https://bugzilla.redhat.com/show_bug.cgi?id=F28BetaFreezeException)
&#42; [Final
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F28FinalBlocker)
&#42; [Final Freeze
Exceptions](https://bugzilla.redhat.com/show_bug.cgi?id=F28FinalFreezeException)

# Fedora Linux 28 {#_fedora_linux_28}

This is a development landing page for Fedora Linux 27. User
documentation, when available, will be at
<https://docs.fedoraproject.org/en-US/fedora/f27/>

## Quick links {#_quick_links_17}

&#42;
[Beta](https://qa.fedoraproject.org/blockerbugs/milestone/27/beta/buglist)
and
[Final](https://qa.fedoraproject.org/blockerbugs/milestone/27/final/buglist)
blockers &#42; [Change
Set](https://fedoraproject.org/wiki/Releases/27/ChangeSet) &#42;
[Release-Blocking
Deliverables](https://fedoraproject.org/wiki/Releases/27/ReleaseBlocking)
&#42;
[Schedule](https://fedorapeople.org/groups/schedule/f-27/f-27-key-tasks.html)
&#42; [Spins and Labs](https://fedoraproject.org/wiki/Releases/27/Spins)

## Assorted tracking bugs {#_assorted_tracking_bugs_17}

&#42; [Failed to
Build](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__&amp;f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F27FTBFS)
&#42; [Beta
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F27BetaBlocker)
&#42; [Beta Freeze
Exceptions](https://bugzilla.redhat.com/show_bug.cgi?id=F27BetaFreezeException)
&#42; [Final
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F27FinalBlocker)
&#42; [Final Freeze
Exceptions](https://bugzilla.redhat.com/show_bug.cgi?id=F27FinalFreezeException)

# Fedora Linux 27 {#_fedora_linux_27}

This is a development landing page for Fedora Linux 26. User
documentation, when available, will be at
<https://docs.fedoraproject.org/en-US/fedora/f26/>

## Quick links {#_quick_links_18}

&#42;
[Beta](https://qa.fedoraproject.org/blockerbugs/milestone/26/beta/buglist)
and
[Final](https://qa.fedoraproject.org/blockerbugs/milestone/26/final/buglist)
blockers &#42; [Change
Set](https://fedoraproject.org/wiki/Releases/26/ChangeSet) &#42;
[Release-Blocking
Deliverables](https://fedoraproject.org/wiki/Releases/26/ReleaseBlocking)
&#42;
[Schedule](https://fedorapeople.org/groups/schedule/f-26/f-26-key-tasks.html)
&#42; [Spins and Labs](https://fedoraproject.org/wiki/Releases/26/Spins)

## Assorted tracking bugs {#_assorted_tracking_bugs_18}

&#42; [Failed to
Build](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__&amp;f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F26FTBFS)
&#42; [Beta
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F26BetaBlocker)
&#42; [Beta Freeze
Exceptions](https://bugzilla.redhat.com/show_bug.cgi?id=F26BetaFreezeException)
&#42; [Final
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F26FinalBlocker)
&#42; [Final Freeze
Exceptions](https://bugzilla.redhat.com/show_bug.cgi?id=F26FinalFreezeException)

# Fedora Linux 26 {#_fedora_linux_26}

This is a development landing page for Fedora Linux 25. User
documentation, when available, will be at
<https://docs.fedoraproject.org/en-US/fedora/f25/>

## Quick links {#_quick_links_19}

&#42;
[Beta](https://qa.fedoraproject.org/blockerbugs/milestone/25/beta/buglist)
and
[Final](https://qa.fedoraproject.org/blockerbugs/milestone/25/final/buglist)
blockers &#42; [Change
Set](https://fedoraproject.org/wiki/Releases/25/ChangeSet) &#42;
[Release-Blocking
Deliverables](https://fedoraproject.org/wiki/Releases/25/ReleaseBlocking)
&#42;
[Schedule](https://fedorapeople.org/groups/schedule/f-25/f-25-key-tasks.html)
&#42; [Spins and Labs](https://fedoraproject.org/wiki/Releases/25/Spins)

## Assorted tracking bugs {#_assorted_tracking_bugs_19}

&#42; [Failed to
Build](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__&amp;f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F25FTBFS)
&#42; [Beta
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F25BetaBlocker)
&#42; [Beta Freeze
Exceptions](https://bugzilla.redhat.com/show_bug.cgi?id=F25BetaFreezeException)
&#42; [Final
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F25FinalBlocker)
&#42; [Final Freeze
Exceptions](https://bugzilla.redhat.com/show_bug.cgi?id=F25FinalFreezeException)

# Fedora Linux 25 {#_fedora_linux_25}

This is a development landing page for Fedora Linux 24. User
documentation, when available, will be at
<https://docs.fedoraproject.org/en-US/fedora/f24/>

## Quick links {#_quick_links_20}

&#42;
[Beta](https://qa.fedoraproject.org/blockerbugs/milestone/24/beta/buglist)
and
[Final](https://qa.fedoraproject.org/blockerbugs/milestone/24/final/buglist)
blockers &#42; [Change
Set](https://fedoraproject.org/wiki/Releases/24/ChangeSet) &#42;
[Release-Blocking
Deliverables](https://fedoraproject.org/wiki/Releases/24/ReleaseBlocking)
&#42;
[Schedule](https://fedorapeople.org/groups/schedule/f-24/f-24-key-tasks.html)
&#42; [Spins and Labs](https://fedoraproject.org/wiki/Releases/24/Spins)

## Assorted tracking bugs {#_assorted_tracking_bugs_20}

&#42; [Failed to
Build](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__&amp;f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F24FTBFS)
&#42; [Beta
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F24BetaBlocker)
&#42; [Beta Freeze
Exceptions](https://bugzilla.redhat.com/show_bug.cgi?id=F24BetaFreezeException)
&#42; [Final
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F24FinalBlocker)
&#42; [Final Freeze
Exceptions](https://bugzilla.redhat.com/show_bug.cgi?id=F24FinalFreezeException)

# Fedora Linux 24 {#_fedora_linux_24}

This is a development landing page for Fedora Linux 23. User
documentation, when available, will be at
<https://docs.fedoraproject.org/en-US/fedora/f23/>

## Quick links {#_quick_links_21}

&#42;
[Beta](https://qa.fedoraproject.org/blockerbugs/milestone/23/beta/buglist)
and
[Final](https://qa.fedoraproject.org/blockerbugs/milestone/23/final/buglist)
blockers &#42; [Change
Set](https://fedoraproject.org/wiki/Releases/23/ChangeSet) &#42;
[Release-Blocking
Deliverables](https://fedoraproject.org/wiki/Releases/23/ReleaseBlocking)
&#42;
[Schedule](https://fedorapeople.org/groups/schedule/f-23/f-23-key-tasks.html)
&#42; [Spins and Labs](https://fedoraproject.org/wiki/Releases/23/Spins)

## Assorted tracking bugs {#_assorted_tracking_bugs_21}

&#42; [Failed to
Build](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__&amp;f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F23FTBFS)
&#42; [Beta
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F23BetaBlocker)
&#42; [Beta Freeze
Exceptions](https://bugzilla.redhat.com/show_bug.cgi?id=F23BetaFreezeException)
&#42; [Final
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F23FinalBlocker)
&#42; [Final Freeze
Exceptions](https://bugzilla.redhat.com/show_bug.cgi?id=F23FinalFreezeException)

# Fedora Linux 23 {#_fedora_linux_23}

This is a development landing page for Fedora Linux 22. User
documentation, when available, will be at
<https://docs.fedoraproject.org/en-US/fedora/f22/>

## Quick links {#_quick_links_22}

&#42;
[Beta](https://qa.fedoraproject.org/blockerbugs/milestone/22/beta/buglist)
and
[Final](https://qa.fedoraproject.org/blockerbugs/milestone/22/final/buglist)
blockers &#42; [Change
Set](https://fedoraproject.org/wiki/Releases/22/ChangeSet) &#42;
[Schedule](https://fedorapeople.org/groups/schedule/f-22/f-22-key-tasks.html)
&#42; [Spins and Labs](https://fedoraproject.org/wiki/Releases/22/Spins)

## Assorted tracking bugs {#_assorted_tracking_bugs_22}

&#42; [Failed to
Build](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__&amp;f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F22FTBFS)
&#42; [Beta
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F22BetaBlocker)
&#42; [Beta Freeze
Exceptions](https://bugzilla.redhat.com/show_bug.cgi?id=F22BetaFreezeException)
&#42; [Final
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F22FinalBlocker)
&#42; [Final Freeze
Exceptions](https://bugzilla.redhat.com/show_bug.cgi?id=F22FinalFreezeException)

# Fedora Linux 22 {#_fedora_linux_22}

This is a development landing page for Fedora Linux 21. User
documentation, when available, will be at
<https://docs.fedoraproject.org/en-US/fedora/f21/>

## Quick links {#_quick_links_23}

&#42;
[Beta](https://qa.fedoraproject.org/blockerbugs/milestone/21/beta/buglist)
and
[Final](https://qa.fedoraproject.org/blockerbugs/milestone/21/final/buglist)
blockers &#42; [Feature
List](https://fedoraproject.org/wiki/Releases/21/FeatureList) &#42;
[Schedule](https://fedorapeople.org/groups/schedule/f-21/f-21-key-tasks.html)
&#42; [Spins and Labs](https://fedoraproject.org/wiki/Releases/21/Spins)

## Assorted tracking bugs {#_assorted_tracking_bugs_23}

&#42; [Failed to
Build](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__&amp;f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F21FTBFS)
&#42; [Beta
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F21BetaBlocker)
&#42; [Beta Freeze
Exceptions](https://bugzilla.redhat.com/show_bug.cgi?id=F21BetaFreezeException)
&#42; [Final
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F21FinalBlocker)
&#42; [Final Freeze
Exceptions](https://bugzilla.redhat.com/show_bug.cgi?id=F21FinalFreezeException)

# Fedora Linux 21 {#_fedora_linux_21}

This is a development landing page for Fedora Linux 20. User
documentation, when available, will be at
<https://docs.fedoraproject.org/en-US/fedora/f20/>

## Quick links {#_quick_links_24}

&#42;
[Beta](https://qa.fedoraproject.org/blockerbugs/milestone/20/beta/buglist)
and
[Final](https://qa.fedoraproject.org/blockerbugs/milestone/20/final/buglist)
blockers &#42; [Feature
List](https://fedoraproject.org/wiki/Releases/20/FeatureList) &#42;
[Schedule](https://fedorapeople.org/groups/schedule/f-20/f-20-key-tasks.html)
&#42; [Spins and Labs](https://fedoraproject.org/wiki/Releases/20/Spins)

## Assorted tracking bugs {#_assorted_tracking_bugs_24}

&#42; [Failed to
Build](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__&amp;f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F20FTBFS)
&#42; [Beta
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F20BetaBlocker)
&#42; [Beta Freeze
Exceptions](https://bugzilla.redhat.com/show_bug.cgi?id=F20BetaFreezeException)
&#42; [Final
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F20FinalBlocker)
&#42; [Final Freeze
Exceptions](https://bugzilla.redhat.com/show_bug.cgi?id=F20FinalFreezeException)

# Fedora Linux 20 {#_fedora_linux_20}

This is a development landing page for Fedora Linux 19. User
documentation, when available, will be at
<https://docs.fedoraproject.org/en-US/fedora/f19/>

## Quick links {#_quick_links_25}

&#42;
[Beta](https://qa.fedoraproject.org/blockerbugs/milestone/19/beta/buglist)
and
[Final](https://qa.fedoraproject.org/blockerbugs/milestone/19/final/buglist)
blockers &#42; [Feature
List](https://fedoraproject.org/wiki/Releases/19/FeatureList) &#42;
[Schedule](https://fedorapeople.org/groups/schedule/f-19/f-19-key-tasks.html)
&#42; [Spins and Labs](https://fedoraproject.org/wiki/Releases/19/Spins)

## Assorted tracking bugs {#_assorted_tracking_bugs_25}

&#42; [Failed to
Build](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__&amp;f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F19FTBFS)
&#42; [Beta
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F19BetaBlocker)
&#42; [Beta Freeze
Exceptions](https://bugzilla.redhat.com/show_bug.cgi?id=F19BetaFreezeException)
&#42; [Final
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F19FinalBlocker)
&#42; [Final Freeze
Exceptions](https://bugzilla.redhat.com/show_bug.cgi?id=F19FinalFreezeException)

# Fedora Linux 19 {#_fedora_linux_19}

This is a development landing page for Fedora Linux 18. User
documentation, when available, will be at
<https://docs.fedoraproject.org/en-US/fedora/f18/>

## Quick links {#_quick_links_26}

&#42;
[Beta](https://qa.fedoraproject.org/blockerbugs/milestone/18/beta/buglist)
and
[Final](https://qa.fedoraproject.org/blockerbugs/milestone/18/final/buglist)
blockers &#42; [Feature
List](https://fedoraproject.org/wiki/Releases/18/FeatureList) &#42;
[Schedule](https://fedorapeople.org/groups/schedule/f-18/f-18-key-tasks.html)
&#42; [Spins and Labs](https://fedoraproject.org/wiki/Releases/18/Spins)

## Assorted tracking bugs {#_assorted_tracking_bugs_26}

&#42; [Failed to
Build](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__&amp;f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F18FTBFS)
&#42; [Beta
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F18BetaBlocker)
&#42; [Final
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F18FinalBlocker)

# Fedora Linux 18 {#_fedora_linux_18}

This is a development landing page for Fedora Linux 17. User
documentation, when available, will be at
<https://docs.fedoraproject.org/en-US/fedora/f17/>

## Quick links {#_quick_links_27}

&#42;
[Beta](https://qa.fedoraproject.org/blockerbugs/milestone/17/beta/buglist)
and
[Final](https://qa.fedoraproject.org/blockerbugs/milestone/17/final/buglist)
blockers &#42; [Feature
List](https://fedoraproject.org/wiki/Releases/17/FeatureList) &#42;
[Schedule](https://fedorapeople.org/groups/schedule/f-17/f-17-key-tasks.html)
&#42; [Spins and Labs](https://fedoraproject.org/wiki/Releases/17/Spins)

## Assorted tracking bugs {#_assorted_tracking_bugs_27}

&#42; [Failed to
Build](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__&amp;f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F17FTBFS)
&#42; [Beta
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F17BetaBlocker)
&#42; [Final
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F17FinalBlocker)

# Fedora Linux 17 {#_fedora_linux_17}

This is a development landing page for Fedora Linux 16. User
documentation, when available, will be at
<https://docs.fedoraproject.org/en-US/fedora/f16/>

## Quick links {#_quick_links_28}

&#42;
[Beta](https://qa.fedoraproject.org/blockerbugs/milestone/16/beta/buglist)
and
[Final](https://qa.fedoraproject.org/blockerbugs/milestone/16/final/buglist)
blockers &#42; [Feature
List](https://fedoraproject.org/wiki/Releases/16/FeatureList) &#42;
[Schedule](https://fedorapeople.org/groups/schedule/f-16/f-16-key-tasks.html)
&#42; [Spins and Labs](https://fedoraproject.org/wiki/Releases/16/Spins)

## Assorted tracking bugs {#_assorted_tracking_bugs_28}

&#42; [Failed to
Build](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__&amp;f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F16FTBFS)
&#42; [Beta
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F16BetaBlocker)
&#42; [Final
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F16FinalBlocker)

# Fedora Linux 16 {#_fedora_linux_16}

This is a development landing page for Fedora Linux 15. User
documentation, when available, will be at
<https://docs.fedoraproject.org/en-US/fedora/f15/>

## Quick links {#_quick_links_29}

&#42;
[Beta](https://qa.fedoraproject.org/blockerbugs/milestone/15/beta/buglist)
and
[Final](https://qa.fedoraproject.org/blockerbugs/milestone/15/final/buglist)
blockers &#42; [Feature
List](https://fedoraproject.org/wiki/Releases/15/FeatureList) &#42;
[Schedule](https://fedorapeople.org/groups/schedule/f-15/f-15-key-tasks.html)
&#42; [Spins and Labs](https://fedoraproject.org/wiki/Releases/15/Spins)

## Assorted tracking bugs {#_assorted_tracking_bugs_29}

&#42; [Failed to
Build](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__&amp;f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F15FTBFS)
&#42; [Beta
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F15BetaBlocker)
&#42; [Final
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F15FinalBlocker)

# Fedora Linux 15 {#_fedora_linux_15}

This is a development landing page for Fedora Linux 14. User
documentation, when available, will be at
<https://docs.fedoraproject.org/en-US/fedora/f14/>

## Quick links {#_quick_links_30}

&#42;
[Beta](https://qa.fedoraproject.org/blockerbugs/milestone/14/beta/buglist)
and
[Final](https://qa.fedoraproject.org/blockerbugs/milestone/14/final/buglist)
blockers &#42; [Feature
List](https://fedoraproject.org/wiki/Releases/14/FeatureList) &#42;
[Schedule](https://fedorapeople.org/groups/schedule/f-14/f-14-key-tasks.html)
&#42; [Spins and Labs](https://fedoraproject.org/wiki/Releases/14/Spins)

## Assorted tracking bugs {#_assorted_tracking_bugs_30}

&#42; [Failed to
Build](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__&amp;f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F14FTBFS)
&#42; [Beta
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F14BetaBlocker)
&#42; [Final
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F14FinalBlocker)

# Fedora Linux 14 {#_fedora_linux_14}

This is a development landing page for Fedora Linux 13. User
documentation, when available, will be at
<https://docs.fedoraproject.org/en-US/fedora/f13/>

## Quick links {#_quick_links_31}

&#42;
[Beta](https://qa.fedoraproject.org/blockerbugs/milestone/13/beta/buglist)
and
[Final](https://qa.fedoraproject.org/blockerbugs/milestone/13/final/buglist)
blockers &#42; [Feature
List](https://fedoraproject.org/wiki/Releases/13/FeatureList) &#42;
[Schedule](https://fedorapeople.org/groups/schedule/f-13/f-13-key-tasks.html)
&#42; [Spins and Labs](https://fedoraproject.org/wiki/Releases/13/Spins)

## Assorted tracking bugs {#_assorted_tracking_bugs_31}

&#42; [Failed to
Build](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__&amp;f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F13FTBFS)
&#42; [Beta
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F13BetaBlocker)
&#42; [Final
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F13FinalBlocker)

# Fedora Linux 13 {#_fedora_linux_13}

This is a development landing page for Fedora Linux 12. User
documentation, when available, will be at
<https://docs.fedoraproject.org/en-US/fedora/f12/>

## Quick links {#_quick_links_32}

&#42;
[Beta](https://qa.fedoraproject.org/blockerbugs/milestone/12/beta/buglist)
and
[Final](https://qa.fedoraproject.org/blockerbugs/milestone/12/final/buglist)
blockers &#42; [Feature
List](https://fedoraproject.org/wiki/Releases/12/FeatureList) &#42;
[Schedule](https://fedorapeople.org/groups/schedule/f-12/f-12-key-tasks.html)
&#42; [Spins and Labs](https://fedoraproject.org/wiki/Releases/12/Spins)

## Assorted tracking bugs {#_assorted_tracking_bugs_32}

&#42; [Failed to
Build](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__&amp;f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F12FTBFS)
&#42; [Beta
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F12BetaBlocker)
&#42; [Final
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F12FinalBlocker)

# Fedora Linux 12 {#_fedora_linux_12}

This is a development landing page for Fedora Linux 11. User
documentation, when available, will be at
<https://docs.fedoraproject.org/en-US/fedora/f11/>

## Quick links {#_quick_links_33}

&#42;
[Beta](https://qa.fedoraproject.org/blockerbugs/milestone/11/beta/buglist)
and
[Final](https://qa.fedoraproject.org/blockerbugs/milestone/11/final/buglist)
blockers &#42; [Feature
List](https://fedoraproject.org/wiki/Releases/11/FeatureList) &#42;
[Schedule](https://fedorapeople.org/groups/schedule/f-11/f-11-key-tasks.html)
&#42; [Spins and Labs](https://fedoraproject.org/wiki/Releases/11/Spins)

## Assorted tracking bugs {#_assorted_tracking_bugs_33}

&#42; [Failed to
Build](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__&amp;f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F11FTBFS)
&#42; [Beta
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F11BetaBlocker)
&#42; [Final
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F11FinalBlocker)

# Fedora Linux 11 {#_fedora_linux_11}

This is a development landing page for Fedora Linux 10. User
documentation, when available, will be at
<https://docs.fedoraproject.org/en-US/fedora/f10/>

## Quick links {#_quick_links_34}

&#42;
[Beta](https://qa.fedoraproject.org/blockerbugs/milestone/10/beta/buglist)
and
[Final](https://qa.fedoraproject.org/blockerbugs/milestone/10/final/buglist)
blockers &#42; [Feature
List](https://fedoraproject.org/wiki/Releases/10/FeatureList) &#42;
[Schedule](https://fedorapeople.org/groups/schedule/f-10/f-10-key-tasks.html)
&#42; [Spins and Labs](https://fedoraproject.org/wiki/Releases/10/Spins)

## Assorted tracking bugs {#_assorted_tracking_bugs_34}

&#42; [Failed to
Build](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__&amp;f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F10FTBFS)
&#42; [Beta
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F10BetaBlocker)
&#42; [Final
Blockers](https://bugzilla.redhat.com/show_bug.cgi?id=F10FinalBlocker)

# Fedora Linux 10 {#_fedora_linux_10}

This is a development landing page for Fedora Linux 9. User
documentation, when available, will be at
<https://docs.fedoraproject.org/en-US/fedora/f9/>

## Quick links {#_quick_links_35}

&#42; [Feature
List](https://fedoraproject.org/wiki/Releases/9/FeatureList) &#42;
[Schedule](https://fedorapeople.org/groups/schedule/f-9/f-9-key-tasks.html)

# Fedora Linux 9 {#_fedora_linux_9}

This is a development landing page for Fedora Linux 8. User
documentation, when available, will be at
<https://docs.fedoraproject.org/en-US/fedora/f8/>

## Quick links {#_quick_links_36}

&#42; [Feature
List](https://fedoraproject.org/wiki/Releases/8/FeatureList) &#42;
[Schedule](https://fedorapeople.org/groups/schedule/f-8/f-8-key-tasks.html)

# Fedora Linux 8 {#_fedora_linux_8}

This is a development landing page for Fedora Linux 7. User
documentation, when available, will be at
<https://docs.fedoraproject.org/en-US/Fedora/7/html/Release_Notes/>

# Fedora Linux 7 {#_fedora_linux_7}

This is a development landing page for Fedora Linux 6. User
documentation, when available, will be at
<https://docs.fedoraproject.org/en-US/Fedora/6/html/Release_Notes/>

# Fedora Linux 6 {#_fedora_linux_6}

This is a development landing page for Fedora Linux 5. User
documentation, when available, will be at
<https://docs.fedoraproject.org/en-US/Fedora/5/html/Release_Notes/>

# Fedora Linux 5 {#_fedora_linux_5}

This is a development landing page for Fedora Linux 4. User
documentation, when available, will be at
<https://docs.fedoraproject.org/en-US/Fedora/4/html/Release_Notes/>

# Fedora Linux 4 {#_fedora_linux_4}

This is a development landing page for Fedora Linux 3. User
documentation, when available, will be at
<https://docs.fedoraproject.org/en-US/Fedora/3/html/Release_Notes/>

# Fedora Linux 3 {#_fedora_linux_3}

This is a development landing page for Fedora Linux 2. User
documentation, when available, will be at
<https://docs.fedoraproject.org/en-US/Fedora/2/html/Release_Notes/>

# Fedora Linux 2 {#_fedora_linux_2}

This is a development landing page for Fedora Linux 1. User
documentation, when available, will be at
<https://docs.fedoraproject.org/en-US/Fedora/1/html/Release_Notes/>

# Release Name History {#_release_name_history}

Prior to Fedora Linux 21, releases had code names. This page documents
the history of release names.

## Release name relationships {#_release_name_relationships}

Name n and n+1 must share an \'is-a\' (not a \'has-a\') relationship,
but n and n+2 must not share the same is-a relationship as n and n+1.
The release names we put up for vote tend to have multiple meanings so
as to allow us to select a new name with a different relationship for
the next release. It is part of the fun!

## Release name history {#_release_name_history_2}

### Fedora Linux 21 (Twenty One) {#_fedora_linux_21_twenty_one}

&#42; Releases are no longer named starting with this release. &#42;
<https://lists.fedoraproject.org/pipermail/advisory-board/2013-October/012209.html>

### Fedora Linux 20 (Heisenbug) {#_fedora_linux_20_heisenbug}

&#42; Heisenbug is a term for a software bug that seems to disappear or
alter its behaviour when one attempts to study it. &#42;
<http://en.wikipedia.org/wiki/Heisenbug>

### Fedora Linux 19 (Schrödinger's Cat) {#_fedora_linux_19_schrödingers_cat}

&#42; Schrödinger's cat corresponds to a theoretical thought experiment.
&#42; <http://en.wikipedia.org/wiki/Schr%C3%B6dinger%27s_cat>

### Fedora Linux 18 (Spherical Cow) {#_fedora_linux_18_spherical_cow}

&#42; Spherical Cow is something that has never been observed, and may
also therefore be considered as a theoretical thought experiment. &#42;
<http://en.wikipedia.org/wiki/Spherical_cow>

### Fedora Linux 17 (Beefy Miracle) {#_fedora_linux_17_beefy_miracle}

&#42; Beefy Miracle is a name that was suggested for Fedora 16 (like
Verne), and is also something that has never been observed. &#42;
<http://beefymiracle.org/history.html>

### Fedora Linux 16 (Verne) {#_fedora_linux_16_verne}

&#42; James Lovelock is a futurologist, and so was Jules Verne &#42;
<http://en.wikipedia.org/wiki/Jules_Verne>

### Fedora Linux 15 (Lovelock) {#_fedora_linux_15_lovelock}

&#42; Laughlin is a city in the state of Nevada (United States), and so
is Lovelock. &#42; <http://en.wikipedia.org/wiki/Lovelock,_Nevada>

### Fedora Linux 14 (Laughlin) {#_fedora_linux_14_laughlin}

&#42; Robert H. Goddard was a professor of physics, and so was Robert
Laughlin. &#42; <http://en.wikipedia.org/wiki/Robert_B._Laughlin>

### Fedora Linux 13 (Goddard) {#_fedora_linux_13_goddard}

&#42; Константи́н Эдуа́рдович Циолко́вский (Konstantin/Constantine
Tsiolkovsky) was a rocket scientist, and so was Robert Goddard. &#42;
<http://en.wikipedia.org/wiki/Konstantin_Tsiolkovsky> &#42;
<https://en.wikipedia.org/wiki/Robert_H._Goddard>

### Fedora Linux 12 (Constantine) {#_fedora_linux_12_constantine}

&#42; Constantine is the name of Township in St. Joseph County, Michigan
in the United States, as well as a name of a bay in the United Kingdom.
&#42; <http://en.wikipedia.org/wiki/Constantine,_Michigan> &#42; There
are several other connections listed at
<http://en.wikipedia.org/wiki/Constantine>

### Fedora Linux 11 (Leonidas) {#_fedora_linux_11_leonidas}

&#42; Leonidas was a ship in the United States Navy. &#42;
<https://web.archive.org/web/20040310113223/http://www.history.navy.mil/photos/sh-usn/usnsh-l/ad7.htm>
&#42;
<https://www.history.navy.mil/content/history/nhhc/research/histories/ship-histories/danfs/l/leonidas-ii.html>
&#42; Leonidas is also the name of a king. &#42;
<http://en.wikipedia.org/wiki/Leonidas_I>

### Fedora Linux 10 (Cambridge) {#_fedora_linux_10_cambridge}

&#42; Cambridge is a city in the United States, as well as being
original code name of Red Hat Linux 10 (before it became Fedora Core 1),
and was the name of a ship in the United States Navy. &#42;
<https://web.archive.org/web/20031006204348/http://www.history.navy.mil/photos/sh-usn/usnsh-c/cambridg.htm>
&#42;
<https://www.history.navy.mil/content/history/nhhc/research/histories/ship-histories/danfs/c/cambridge-i.html>
&#42; <http://en.wikipedia.org/wiki/Cambridge%2C_Massachusetts> &#42;
Voting results:
<https://web.archive.org/web/20080809205521/http://jwboyer.fedorapeople.org/fedora10relname.txt.asc>

### Fedora Linux 9 (Sulphur) {#_fedora_linux_9_sulphur}

&#42; Sulphur is an element that causes an adverse reaction (tarnishing)
when it contacts silver. In mythology, it is an element used to drive
away werewolves. Sulphur is also a city in the United States. &#42;
<http://en.wikipedia.org/wiki/Silver&#35;Silver_compounds> &#42;
<https://www.redhat.com/archives/fedora-devel-list/2007-December/msg01194.html>
&#42; <http://en.wikipedia.org/wiki/Sulphur,_Louisiana>

### Fedora Linux 8 (Werewolf) {#_fedora_linux_8_werewolf}

&#42; Werewolf is the name of a movie about a dude who turns into a
werewolf. A werewolf also has an adverse reaction (death) when it comes
into contact with silver. &#42; <http://www.imdb.com/title/tt0118137/>
&#42; <http://en.wikipedia.org/wiki/Werewolf>

### Fedora Linux 7 (Moonshine) {#_fedora_linux_7_moonshine}

&#42; Moonshine is an independent record label, and also the name of a
movie. &#42; <http://en.wikipedia.org/wiki/Moonshine_Music> &#42;
<http://www.imdb.com/title/tt0009389/>

### Fedora Core 6 (Zod) {#_fedora_core_6_zod}

&#42; General Zod is a character in the DC Comics universe, as well as
an independent record label. &#42;
<http://en.wikipedia.org/wiki/General_Zod> &#42;
<http://www.zodrecords.com/>

### Fedora Core 5 (Bordeaux) {#_fedora_core_5_bordeaux}

&#42; Bordeaux is a wine-producing region in France, as well as a comic
book character. &#42; <http://en.wikipedia.org/wiki/Bordeaux> &#42;
<http://en.wikipedia.org/wiki/Sasha_Bordeaux>

### Fedora Core 4 (Stentz) {#_fedora_core_4_stentz}

&#42; Andre Stentz is a French winery. As such, both Heidelberg and
Stentz are distributors of alcoholic beverages. &#42;
<http://www.andre-stentz.fr/>

### Fedora Core 3 (Heidelberg) {#_fedora_core_3_heidelberg}

&#42; Heidelberg is a city in Germany, and also a brand/distributor of
beer. &#42; <http://en.wikipedia.org/wiki/Heidelberg> &#42;
<http://www.heidelbergdistributing.com>

### Fedora Core 2 (Tettnang) {#_fedora_core_2_tettnang}

&#42; Tettnang is a city in Germany that is a producer of hops. &#42;
<http://en.wikipedia.org/wiki/Tettnang>

### Fedora Core 1 (Yarrow) {#_fedora_core_1_yarrow}

&#42; Yarrow is a plant with many uses. Prior to the use of hops in the
flavoring of beer, yarrow was used for this purpose. &#42;
<http://en.wikipedia.org/wiki/Yarrow>

# Changes policy {#_changes_policy}

:::: tip
::: title
:::

If you know the process already, you can jump immediately to [an empty
Change Proposal
form](https://fedoraproject.org/wiki/Changes/EmptyTemplate). For help
with understanding the fields, see the [change submission
guidance](changes_guide.xml) page. Watch the [Fedora Changes policy
video](https://www.youtube.com/watch?v=oERoxg-VYPo) for a quick
introduction to the process.
::::

To report an issue with the proposal template, file an issue in the
[pgm_docs repo](https://pagure.io/fedora-pgm/pgm_docs).

&#42; [Motivation](#_motivation) &#42; [Change
Categories](#_change_categories) &#42; [Change Proposal
Sections](#_change_proposal_sections) &#42; [Essential
Communication](#_essential_communication) &#42; [Change
Process](#_change_process) &#42;&#42; [Change Process
Milestones](#_change_process_milestones) &#42;&#42; [Bugzilla
Trackers](#_bugzilla_trackers)

## Motivation {#_motivation}

The motivation for the Changes process is to raise the visibility of
planned changes and make coordination and planning effort easier. It is
nearly impossible to follow all changes happening in a big project such
as Fedora. By providing a mechanism for sharing changes, it is easier
for contributors to know what is coming and to ensure that we can
address impacts of changes well before the release date. Change
proposals should be shared as early as possible, before the change is
implemented and even in the very early state of the idea, to gather
community feedback and review.

The list of accepted changes, or *change set*, is used by different
teams across the project. For example, the change set may be used to
prepare external facing materials like release notes and release
announcements.

Change owners are trusted *and depended upon* to highlight all relevant
changes. Not noting important changes (whether due to oversight,
different opinion of importance, or intentionally) breaks the Change
process.

The Change process is an internal planning and tracking tool, and the
final release is not required to reflect all proposed changes.

## Change Categories {#_change_categories}

Fedora Engineering and Steering Committee (FESCo) has defined two Change
categories:

1.  Self-contained changes

2.  System-wide changes

### Self-Contained Changes {#_self_contained_changes}

A self-contained change is a change to isolated package(s), or a general
change with limited scope and impact on the rest of the
distribution/project. Examples include addition of a group of leaf
packages, or a coordinated effort within a Special Interest Group (SIG)
with limited impact outside the SIG's functional area. Self-contained
changes could be used for early idea state proposals for wider and
complex changes. [Creating a new Solution](releases::spins/creating.xml)
(e.g. a Spin/Lab) is a Self-Contained Change.

Public announcement of a new self-contained change promotes cooperation
on the change, and extends its visibility. Change owners may find help
from the community or useful comments. Based on the community review,
the self-contained change can be updated to the system-wide change
category, and the owner may be asked to provide more details and extend
the change proposal page.

### System-Wide Changes {#_system_wide_changes}

System-wide changes involve system-wide defaults, critical path
components, or other changes that are not eligible as self-contained
changes. Promoting a deliverable to Edition status is a System-Wide
Change by [Council
policy](council::policy/edition-promotion-policy.xml).

## Change Proposal Sections {#_change_proposal_sections}

+----------------------+----------------------+-----------------------+
| Element              | Self-Contained       | System-Wide           |
+======================+======================+=======================+
| Summary              | required             | required              |
+----------------------+----------------------+-----------------------+
| Owner                | required             | required              |
+----------------------+----------------------+-----------------------+
| Current status       | required             | required              |
+----------------------+----------------------+-----------------------+
| Detailed description | required             | required              |
+----------------------+----------------------+-----------------------+
| Feedback             | optional             | optional              |
+----------------------+----------------------+-----------------------+
| Benefit to Fedora    | required             | required              |
+----------------------+----------------------+-----------------------+
| Scope/Proposal       | required             | required              |
| owners               |                      |                       |
+----------------------+----------------------+-----------------------+
| Scope/Other          | as applicable        | required              |
| developers           |                      |                       |
+----------------------+----------------------+-----------------------+
| Scope/Release        | as applicable        | required              |
| Engineering          |                      |                       |
+----------------------+----------------------+-----------------------+
| Scope/Policies and   | as applicable        | as applicable         |
| guidelines           |                      |                       |
+----------------------+----------------------+-----------------------+
| Scope/Trademark      | as applicable        | as applicable         |
| approval             |                      |                       |
+----------------------+----------------------+-----------------------+
| Scope/Objective      | as applicable        | as applicable         |
| alignment            |                      |                       |
+----------------------+----------------------+-----------------------+
| Upgrade &amp;        | optional             | required              |
| Compatibility impact |                      |                       |
+----------------------+----------------------+-----------------------+
| How to test          | optional             | required              |
+----------------------+----------------------+-----------------------+
| User experience      | optional             | optional              |
+----------------------+----------------------+-----------------------+
| Dependencies         | optional             | required              |
+----------------------+----------------------+-----------------------+
| Contingency plan     | optional             | required              |
+----------------------+----------------------+-----------------------+
| Documentation        | optional             | required              |
+----------------------+----------------------+-----------------------+
| Release notes        | optional             | required              |
+----------------------+----------------------+-----------------------+

: Change proposal sections

## Essential Communication {#_essential_communication}

### Fedora Packaging Committee {#_fedora_packaging_committee}

For changes that require modifications to the [Fedora Packaging
Guidelines](packaging-guidelines::index.xml):

&#42; The person or group proposing the Change is responsible for
providing a first draft of packaging guideline changes to the FPC. &#42;
Ideally, this draft will be available as a pull request *before
submitting the Change proposal* so that the community and FESCo can
evaluate the specific changes.

### Release Engineering {#_release_engineering}

For all system-wide changes you must file an issue in [releng
pagure](https://pagure.io/releng/issues) to check if your change
requires Release Engineering involvement.

:::: note
::: title
:::

Release Engineering tickets are not required by default for
self-contained changes, but may be necessary if the change involves, for
example, adding a new output artifact.
::::

### Trademark Approval {#_trademark_approval}

If your Change may require trademark approval (for example, if it is a
new Spin), [file a
ticket](https://pagure.io/Fedora-Council/tickets/issues) requesting
trademark approval from the Fedora Council.

## Change process {#_change_process}

This is the general flow for change proposals:

&#42; The owner creates their proposal by making a copy of the changes
template <https://fedoraproject.org/wiki/Changes/EmptyTemplate>.
&#42;&#42; It is a good idea to keep the name of the wiki page as
similar as possible to the name in the proposal to avoid confusion.
&#42; The owner submits the change proposal by setting the wiki page to
the &#42;ChangeReadyForWrangler&#42; category. &#42; The Change Wrangler
(FOA) checks the proposed change page for formal correctness. This
includes Release Engineering, Fedora Packaging Committee, and trademark
approval tickets where necessary. &#42; Once the change proposal is
correct, the Change Wrangler (FOA) announces it on the devel-announce
and creates a post on discussion.fedoraproject.org. &#42; The change
owner must have a username on discussion.fedoraproject.org so their
change may be assigned to them. This is easly done by signing in once to
discourse using your FAS login credentials. &#42; Any team can share
their views on the discussion post (preferred) and devel mailing list
and escalate a proposed change to FESCo. The change owner may be asked
to provide more details or address proposed concerns. &#42; FESCo
members are encouraged to ask questions on the discussion post ahead of
the change ticket being openend. &#42; The Change Wrangler (FOA) files a
FESCo ticket no sooner than one week after the announcement on the
mailing list and discussion post. &#42; Change owners are subscribed to
the FESCo ticket once it has been created by the Program Manager.
&#42;&#42; Occasionally, more information is needed on some proposals,
and FESCo members may use the ticket filed for clarificiation instead of
waiting for the meeting. &#42; FESCo will then vote to approve or deny a
change proposal in accordance with the [FESCo ticket
policy](fesco:ROOT:index.adoc&#35;_ticket_policy). Do not implement your
proposal until the FESCo vote has ended. When a FESCo member has marked
the change ticket as &#42;APPROVED&#42;, you may then proceed with the
implementation. &#42;&#42; Occasionally, FESCo assigns the change to one
of the FESCo members or a trusted community member within the functional
area (a *change shepherd*), who follows the detailed status of the
change with FESCo and helps with processes within Fedora. For example,
the change shepherd may communicate high-impact aspects of the change,
or point out that a buildroot will be necessary. The shepherd follows
the status of the change until final release. &#42; The Change Wrangler
(FOA) will create Bugzilla trackers in the *Changes Tracking* component
and issues in the Release Notes repository for approved changes. &#42;
FESCo will re-review the status of changes one week before the beta
freeze following an Incomplete Changes report from the Change Wrangler
(FOA). At this time, FESCo typically decides whether to activate the
contingency plan. Any change for which FESCo can't make this decision
one week before beta must include a note on its Change wiki page and
tracking bug. Changes that cannot be completed will automatically be
deferred to the next release and do not require re-submission unless
substantial revisions are made.

:::: note
::: title
:::

In most cases, you should not submit code changes to Rawhide until after
FESCo has voted to approve the proposal.
::::

### Change process milestones {#_change_process_milestones}

#### Proposal submission deadline {#_proposal_submission_deadline}

New change proposals may be submitted using the guidelines described
elsewhere and until the appropriate change proposal submission deadline.
For a given release, this date is available in the [release
schedule](https://fedorapeople.org/groups/schedule/) and will be
announced well in advance.

:::: note
::: title
:::

Changes do not have to be accepted by this deadline, but they must have
been submitted to the Change Wrangler (FOA) by then.
::::

#### Code complete (testable) deadline {#_code_complete_testable_deadline}

&#42; By this date, a new change must be feature complete or close
enough to completion that a majority of its functionality can be tested
prior the Beta release. &#42; If a change proposal page specifies a
change will be enabled by default, it must be so by this milestone.
&#42; Changes that are testable should have their tracking bug set to
the &#42;MODIFIED&#42; status.

:::: note
::: title
:::

At this point, Rawhide and the immediately-upcoming \'N+1\' release are
already separate branches. If development, testing, integration --- and
integration testing! --- are not really all lined up by this point,
there is no shame in re-targeting for the next (N+2) release. Now is the
time for you to bring that to FESCo. Or, if this change is
time-sensitive, but needs more resources or attention from across the
community, bring that to FESCo, to the Fedora Council, and to the Fedora
community at large.
::::

#### Code complete (100%) deadline {#_code_complete_100_deadline}

&#42; Changes must be code complete, meaning all the code required to
enable the new change is finished. &#42; The level of code completeness
is reflected as tracker bug state &#42;ON_QA&#42;. The change does not
have to be fully tested by this deadline.

:::: note
::: title
:::

Code complete (100%) deadline coincides with the Beta Freeze date
because that is the last date on which it can be ensured that a build
will appear in a milestone release. The idea is really that these
requirements be met in the Beta release, but due to the nature of the
milestone freezes, in order to ensure this is the case, the requirements
must be met by the freeze date.
::::

### Bugzilla trackers {#_bugzilla_trackers}

Approved change proposals will have Bugzilla issues created by the
Change Wrangler (FOA). The following status fields should be used to
reflect the status of the change:

+-----------------------------------+-----------------------------------+
| BZ Status                         | Meaning                           |
+===================================+===================================+
| ASSIGNED                          | Change approved by FESCo          |
+-----------------------------------+-----------------------------------+
| MODIFIED                          | Change is code complete enough to |
|                                   | be testable                       |
+-----------------------------------+-----------------------------------+
| ON_QA                             | Change is 100% code complete      |
+-----------------------------------+-----------------------------------+

: Bugzilla tracker statuses

:::: note
::: title
:::

Do not close tracking bugs when a change is complete. Instead, please
comment on your tracking bug that this change is complete. The Change
Wrangler (FOA) will auto-close tracking bugs as part of release
housekeeping.
::::

# Changes policy {#_changes_policy_2}

:::: tip
::: title
:::

If you know the process already, you can jump immediately to [an empty
Change Proposal
form](https://fedoraproject.org/wiki/Changes/EmptyTemplate). For help
with understanding the fields, see the [change submission
guidance](changes_guide.xml) page. Watch the [Fedora Changes policy
video](https://www.youtube.com/watch?v=oERoxg-VYPo) for a quick
introduction to the process.
::::

To report an issue with the proposal template, file an issue in the
[pgm_docs repo](https://pagure.io/fedora-pgm/pgm_docs).

&#42; [Motivation](#_motivation) &#42; [Change
Categories](#_change_categories) &#42; [Change Proposal
Sections](#_change_proposal_sections) &#42; [Essential
Communication](#_essential_communication) &#42; [Change
Process](#_change_process) &#42;&#42; [Change Process
Milestones](#_change_process_milestones) &#42;&#42; [Bugzilla
Trackers](#_bugzilla_trackers)

## Motivation {#_motivation_2}

The motivation for the Changes process is to raise the visibility of
planned changes and make coordination and planning effort easier. It is
nearly impossible to follow all changes happening in a big project such
as Fedora. By providing a mechanism for sharing changes, it is easier
for contributors to know what is coming and to ensure that we can
address impacts of changes well before the release date. Change
proposals should be shared as early as possible, before the change is
implemented and even in the very early state of the idea, to gather
community feedback and review.

The list of accepted changes, or *change set*, is used by different
teams across the project. For example, the change set may be used to
prepare external facing materials like release notes and release
announcements.

Change owners are trusted *and depended upon* to highlight all relevant
changes. Not noting important changes (whether due to oversight,
different opinion of importance, or intentionally) breaks the Change
process.

The Change process is an internal planning and tracking tool, and the
final release is not required to reflect all proposed changes.

## Change Categories {#_change_categories_2}

Fedora Engineering and Steering Committee (FESCo) has defined two Change
categories:

1.  Self-contained changes

2.  System-wide changes

### Self-Contained Changes {#_self_contained_changes_2}

A self-contained change is a change to isolated package(s), or a general
change with limited scope and impact on the rest of the
distribution/project. Examples include addition of a group of leaf
packages, or a coordinated effort within a Special Interest Group (SIG)
with limited impact outside the SIG's functional area. Self-contained
changes could be used for early idea state proposals for wider and
complex changes. [Creating a new Solution](releases::spins/creating.xml)
(e.g. a Spin/Lab) is a Self-Contained Change.

Public announcement of a new self-contained change promotes cooperation
on the change, and extends its visibility. Change owners may find help
from the community or useful comments. Based on the community review,
the self-contained change can be updated to the system-wide change
category, and the owner may be asked to provide more details and extend
the change proposal page.

### System-Wide Changes {#_system_wide_changes_2}

System-wide changes involve system-wide defaults, critical path
components, or other changes that are not eligible as self-contained
changes. Promoting a deliverable to Edition status is a System-Wide
Change by [Council
policy](council::policy/edition-promotion-policy.xml).

## Change Proposal Sections {#_change_proposal_sections_2}

+----------------------+----------------------+-----------------------+
| Element              | Self-Contained       | System-Wide           |
+======================+======================+=======================+
| Summary              | required             | required              |
+----------------------+----------------------+-----------------------+
| Owner                | required             | required              |
+----------------------+----------------------+-----------------------+
| Current status       | required             | required              |
+----------------------+----------------------+-----------------------+
| Detailed description | required             | required              |
+----------------------+----------------------+-----------------------+
| Feedback             | optional             | optional              |
+----------------------+----------------------+-----------------------+
| Benefit to Fedora    | required             | required              |
+----------------------+----------------------+-----------------------+
| Scope/Proposal       | required             | required              |
| owners               |                      |                       |
+----------------------+----------------------+-----------------------+
| Scope/Other          | as applicable        | required              |
| developers           |                      |                       |
+----------------------+----------------------+-----------------------+
| Scope/Release        | as applicable        | required              |
| Engineering          |                      |                       |
+----------------------+----------------------+-----------------------+
| Scope/Policies and   | as applicable        | as applicable         |
| guidelines           |                      |                       |
+----------------------+----------------------+-----------------------+
| Scope/Trademark      | as applicable        | as applicable         |
| approval             |                      |                       |
+----------------------+----------------------+-----------------------+
| Scope/Objective      | as applicable        | as applicable         |
| alignment            |                      |                       |
+----------------------+----------------------+-----------------------+
| Upgrade &amp;        | optional             | required              |
| Compatibility impact |                      |                       |
+----------------------+----------------------+-----------------------+
| How to test          | optional             | required              |
+----------------------+----------------------+-----------------------+
| User experience      | optional             | optional              |
+----------------------+----------------------+-----------------------+
| Dependencies         | optional             | required              |
+----------------------+----------------------+-----------------------+
| Contingency plan     | optional             | required              |
+----------------------+----------------------+-----------------------+
| Documentation        | optional             | required              |
+----------------------+----------------------+-----------------------+
| Release notes        | optional             | required              |
+----------------------+----------------------+-----------------------+

: Change proposal sections

## Essential Communication {#_essential_communication_2}

### Fedora Packaging Committee {#_fedora_packaging_committee_2}

For changes that require modifications to the [Fedora Packaging
Guidelines](packaging-guidelines::index.xml):

&#42; The person or group proposing the Change is responsible for
providing a first draft of packaging guideline changes to the FPC. &#42;
Ideally, this draft will be available as a pull request *before
submitting the Change proposal* so that the community and FESCo can
evaluate the specific changes.

### Release Engineering {#_release_engineering_2}

For all system-wide changes you must file an issue in [releng
pagure](https://pagure.io/releng/issues) to check if your change
requires Release Engineering involvement.

:::: note
::: title
:::

Release Engineering tickets are not required by default for
self-contained changes, but may be necessary if the change involves, for
example, adding a new output artifact.
::::

### Trademark Approval {#_trademark_approval_2}

If your Change may require trademark approval (for example, if it is a
new Spin), [file a
ticket](https://pagure.io/Fedora-Council/tickets/issues) requesting
trademark approval from the Fedora Council.

## Change process {#_change_process_2}

This is the general flow for change proposals:

&#42; The owner creates their proposal by making a copy of the changes
template <https://fedoraproject.org/wiki/Changes/EmptyTemplate>.
&#42;&#42; It is a good idea to keep the name of the wiki page as
similar as possible to the name in the proposal to avoid confusion.
&#42; The owner submits the change proposal by setting the wiki page to
the &#42;ChangeReadyForWrangler&#42; category. &#42; The Change Wrangler
(FOA) checks the proposed change page for formal correctness. This
includes Release Engineering, Fedora Packaging Committee, and trademark
approval tickets where necessary. &#42; Once the change proposal is
correct, the Change Wrangler (FOA) announces it on the devel-announce
and creates a post on discussion.fedoraproject.org. &#42; The change
owner must have a username on discussion.fedoraproject.org so their
change may be assigned to them. This is easly done by signing in once to
discourse using your FAS login credentials. &#42; Any team can share
their views on the discussion post (preferred) and devel mailing list
and escalate a proposed change to FESCo. The change owner may be asked
to provide more details or address proposed concerns. &#42; FESCo
members are encouraged to ask questions on the discussion post ahead of
the change ticket being openend. &#42; The Change Wrangler (FOA) files a
FESCo ticket no sooner than one week after the announcement on the
mailing list and discussion post. &#42; Change owners are subscribed to
the FESCo ticket once it has been created by the Program Manager.
&#42;&#42; Occasionally, more information is needed on some proposals,
and FESCo members may use the ticket filed for clarificiation instead of
waiting for the meeting. &#42; FESCo will then vote to approve or deny a
change proposal in accordance with the [FESCo ticket
policy](fesco:ROOT:index.adoc&#35;_ticket_policy). Do not implement your
proposal until the FESCo vote has ended. When a FESCo member has marked
the change ticket as &#42;APPROVED&#42;, you may then proceed with the
implementation. &#42;&#42; Occasionally, FESCo assigns the change to one
of the FESCo members or a trusted community member within the functional
area (a *change shepherd*), who follows the detailed status of the
change with FESCo and helps with processes within Fedora. For example,
the change shepherd may communicate high-impact aspects of the change,
or point out that a buildroot will be necessary. The shepherd follows
the status of the change until final release. &#42; The Change Wrangler
(FOA) will create Bugzilla trackers in the *Changes Tracking* component
and issues in the Release Notes repository for approved changes. &#42;
FESCo will re-review the status of changes one week before the beta
freeze following an Incomplete Changes report from the Change Wrangler
(FOA). At this time, FESCo typically decides whether to activate the
contingency plan. Any change for which FESCo can't make this decision
one week before beta must include a note on its Change wiki page and
tracking bug. Changes that cannot be completed will automatically be
deferred to the next release and do not require re-submission unless
substantial revisions are made.

:::: note
::: title
:::

In most cases, you should not submit code changes to Rawhide until after
FESCo has voted to approve the proposal.
::::

### Change process milestones {#_change_process_milestones_2}

#### Proposal submission deadline {#_proposal_submission_deadline_2}

New change proposals may be submitted using the guidelines described
elsewhere and until the appropriate change proposal submission deadline.
For a given release, this date is available in the [release
schedule](https://fedorapeople.org/groups/schedule/) and will be
announced well in advance.

:::: note
::: title
:::

Changes do not have to be accepted by this deadline, but they must have
been submitted to the Change Wrangler (FOA) by then.
::::

#### Code complete (testable) deadline {#_code_complete_testable_deadline_2}

&#42; By this date, a new change must be feature complete or close
enough to completion that a majority of its functionality can be tested
prior the Beta release. &#42; If a change proposal page specifies a
change will be enabled by default, it must be so by this milestone.
&#42; Changes that are testable should have their tracking bug set to
the &#42;MODIFIED&#42; status.

:::: note
::: title
:::

At this point, Rawhide and the immediately-upcoming \'N+1\' release are
already separate branches. If development, testing, integration --- and
integration testing! --- are not really all lined up by this point,
there is no shame in re-targeting for the next (N+2) release. Now is the
time for you to bring that to FESCo. Or, if this change is
time-sensitive, but needs more resources or attention from across the
community, bring that to FESCo, to the Fedora Council, and to the Fedora
community at large.
::::

#### Code complete (100%) deadline {#_code_complete_100_deadline_2}

&#42; Changes must be code complete, meaning all the code required to
enable the new change is finished. &#42; The level of code completeness
is reflected as tracker bug state &#42;ON_QA&#42;. The change does not
have to be fully tested by this deadline.

:::: note
::: title
:::

Code complete (100%) deadline coincides with the Beta Freeze date
because that is the last date on which it can be ensured that a build
will appear in a milestone release. The idea is really that these
requirements be met in the Beta release, but due to the nature of the
milestone freezes, in order to ensure this is the case, the requirements
must be met by the freeze date.
::::

### Bugzilla trackers {#_bugzilla_trackers_2}

Approved change proposals will have Bugzilla issues created by the
Change Wrangler (FOA). The following status fields should be used to
reflect the status of the change:

+-----------------------------------+-----------------------------------+
| BZ Status                         | Meaning                           |
+===================================+===================================+
| ASSIGNED                          | Change approved by FESCo          |
+-----------------------------------+-----------------------------------+
| MODIFIED                          | Change is code complete enough to |
|                                   | be testable                       |
+-----------------------------------+-----------------------------------+
| ON_QA                             | Change is 100% code complete      |
+-----------------------------------+-----------------------------------+

: Bugzilla tracker statuses

:::: note
::: title
:::

Do not close tracking bugs when a change is complete. Instead, please
comment on your tracking bug that this change is complete. The Change
Wrangler (FOA) will auto-close tracking bugs as part of release
housekeeping.
::::

# Changes policy {#_changes_policy_3}

:::: tip
::: title
:::

If you know the process already, you can jump immediately to [an empty
Change Proposal
form](https://fedoraproject.org/wiki/Changes/EmptyTemplate). For help
with understanding the fields, see the [change submission
guidance](changes_guide.xml) page. Watch the [Fedora Changes policy
video](https://www.youtube.com/watch?v=oERoxg-VYPo) for a quick
introduction to the process.
::::

To report an issue with the proposal template, file an issue in the
[pgm_docs repo](https://pagure.io/fedora-pgm/pgm_docs).

&#42; [Motivation](#_motivation) &#42; [Change
Categories](#_change_categories) &#42; [Change Proposal
Sections](#_change_proposal_sections) &#42; [Essential
Communication](#_essential_communication) &#42; [Change
Process](#_change_process) &#42;&#42; [Change Process
Milestones](#_change_process_milestones) &#42;&#42; [Bugzilla
Trackers](#_bugzilla_trackers)

## Motivation {#_motivation_3}

The motivation for the Changes process is to raise the visibility of
planned changes and make coordination and planning effort easier. It is
nearly impossible to follow all changes happening in a big project such
as Fedora. By providing a mechanism for sharing changes, it is easier
for contributors to know what is coming and to ensure that we can
address impacts of changes well before the release date. Change
proposals should be shared as early as possible, before the change is
implemented and even in the very early state of the idea, to gather
community feedback and review.

The list of accepted changes, or *change set*, is used by different
teams across the project. For example, the change set may be used to
prepare external facing materials like release notes and release
announcements.

Change owners are trusted *and depended upon* to highlight all relevant
changes. Not noting important changes (whether due to oversight,
different opinion of importance, or intentionally) breaks the Change
process.

The Change process is an internal planning and tracking tool, and the
final release is not required to reflect all proposed changes.

## Change Categories {#_change_categories_3}

Fedora Engineering and Steering Committee (FESCo) has defined two Change
categories:

1.  Self-contained changes

2.  System-wide changes

### Self-Contained Changes {#_self_contained_changes_3}

A self-contained change is a change to isolated package(s), or a general
change with limited scope and impact on the rest of the
distribution/project. Examples include addition of a group of leaf
packages, or a coordinated effort within a Special Interest Group (SIG)
with limited impact outside the SIG's functional area. Self-contained
changes could be used for early idea state proposals for wider and
complex changes. [Creating a new Solution](releases::spins/creating.xml)
(e.g. a Spin/Lab) is a Self-Contained Change.

Public announcement of a new self-contained change promotes cooperation
on the change, and extends its visibility. Change owners may find help
from the community or useful comments. Based on the community review,
the self-contained change can be updated to the system-wide change
category, and the owner may be asked to provide more details and extend
the change proposal page.

### System-Wide Changes {#_system_wide_changes_3}

System-wide changes involve system-wide defaults, critical path
components, or other changes that are not eligible as self-contained
changes. Promoting a deliverable to Edition status is a System-Wide
Change by [Council
policy](council::policy/edition-promotion-policy.xml).

## Change Proposal Sections {#_change_proposal_sections_3}

+----------------------+----------------------+-----------------------+
| Element              | Self-Contained       | System-Wide           |
+======================+======================+=======================+
| Summary              | required             | required              |
+----------------------+----------------------+-----------------------+
| Owner                | required             | required              |
+----------------------+----------------------+-----------------------+
| Current status       | required             | required              |
+----------------------+----------------------+-----------------------+
| Detailed description | required             | required              |
+----------------------+----------------------+-----------------------+
| Feedback             | optional             | optional              |
+----------------------+----------------------+-----------------------+
| Benefit to Fedora    | required             | required              |
+----------------------+----------------------+-----------------------+
| Scope/Proposal       | required             | required              |
| owners               |                      |                       |
+----------------------+----------------------+-----------------------+
| Scope/Other          | as applicable        | required              |
| developers           |                      |                       |
+----------------------+----------------------+-----------------------+
| Scope/Release        | as applicable        | required              |
| Engineering          |                      |                       |
+----------------------+----------------------+-----------------------+
| Scope/Policies and   | as applicable        | as applicable         |
| guidelines           |                      |                       |
+----------------------+----------------------+-----------------------+
| Scope/Trademark      | as applicable        | as applicable         |
| approval             |                      |                       |
+----------------------+----------------------+-----------------------+
| Scope/Objective      | as applicable        | as applicable         |
| alignment            |                      |                       |
+----------------------+----------------------+-----------------------+
| Upgrade &amp;        | optional             | required              |
| Compatibility impact |                      |                       |
+----------------------+----------------------+-----------------------+
| How to test          | optional             | required              |
+----------------------+----------------------+-----------------------+
| User experience      | optional             | optional              |
+----------------------+----------------------+-----------------------+
| Dependencies         | optional             | required              |
+----------------------+----------------------+-----------------------+
| Contingency plan     | optional             | required              |
+----------------------+----------------------+-----------------------+
| Documentation        | optional             | required              |
+----------------------+----------------------+-----------------------+
| Release notes        | optional             | required              |
+----------------------+----------------------+-----------------------+

: Change proposal sections

## Essential Communication {#_essential_communication_3}

### Fedora Packaging Committee {#_fedora_packaging_committee_3}

For changes that require modifications to the [Fedora Packaging
Guidelines](packaging-guidelines::index.xml):

&#42; The person or group proposing the Change is responsible for
providing a first draft of packaging guideline changes to the FPC. &#42;
Ideally, this draft will be available as a pull request *before
submitting the Change proposal* so that the community and FESCo can
evaluate the specific changes.

### Release Engineering {#_release_engineering_3}

For all system-wide changes you must file an issue in [releng
pagure](https://pagure.io/releng/issues) to check if your change
requires Release Engineering involvement.

:::: note
::: title
:::

Release Engineering tickets are not required by default for
self-contained changes, but may be necessary if the change involves, for
example, adding a new output artifact.
::::

### Trademark Approval {#_trademark_approval_3}

If your Change may require trademark approval (for example, if it is a
new Spin), [file a
ticket](https://pagure.io/Fedora-Council/tickets/issues) requesting
trademark approval from the Fedora Council.

## Change process {#_change_process_3}

This is the general flow for change proposals:

&#42; The owner creates their proposal by making a copy of the changes
template <https://fedoraproject.org/wiki/Changes/EmptyTemplate>.
&#42;&#42; It is a good idea to keep the name of the wiki page as
similar as possible to the name in the proposal to avoid confusion.
&#42; The owner submits the change proposal by setting the wiki page to
the &#42;ChangeReadyForWrangler&#42; category. &#42; The Change Wrangler
(FOA) checks the proposed change page for formal correctness. This
includes Release Engineering, Fedora Packaging Committee, and trademark
approval tickets where necessary. &#42; Once the change proposal is
correct, the Change Wrangler (FOA) announces it on the devel-announce
and creates a post on discussion.fedoraproject.org. &#42; The change
owner must have a username on discussion.fedoraproject.org so their
change may be assigned to them. This is easly done by signing in once to
discourse using your FAS login credentials. &#42; Any team can share
their views on the discussion post (preferred) and devel mailing list
and escalate a proposed change to FESCo. The change owner may be asked
to provide more details or address proposed concerns. &#42; FESCo
members are encouraged to ask questions on the discussion post ahead of
the change ticket being openend. &#42; The Change Wrangler (FOA) files a
FESCo ticket no sooner than one week after the announcement on the
mailing list and discussion post. &#42; Change owners are subscribed to
the FESCo ticket once it has been created by the Program Manager.
&#42;&#42; Occasionally, more information is needed on some proposals,
and FESCo members may use the ticket filed for clarificiation instead of
waiting for the meeting. &#42; FESCo will then vote to approve or deny a
change proposal in accordance with the [FESCo ticket
policy](fesco:ROOT:index.adoc&#35;_ticket_policy). Do not implement your
proposal until the FESCo vote has ended. When a FESCo member has marked
the change ticket as &#42;APPROVED&#42;, you may then proceed with the
implementation. &#42;&#42; Occasionally, FESCo assigns the change to one
of the FESCo members or a trusted community member within the functional
area (a *change shepherd*), who follows the detailed status of the
change with FESCo and helps with processes within Fedora. For example,
the change shepherd may communicate high-impact aspects of the change,
or point out that a buildroot will be necessary. The shepherd follows
the status of the change until final release. &#42; The Change Wrangler
(FOA) will create Bugzilla trackers in the *Changes Tracking* component
and issues in the Release Notes repository for approved changes. &#42;
FESCo will re-review the status of changes one week before the beta
freeze following an Incomplete Changes report from the Change Wrangler
(FOA). At this time, FESCo typically decides whether to activate the
contingency plan. Any change for which FESCo can't make this decision
one week before beta must include a note on its Change wiki page and
tracking bug. Changes that cannot be completed will automatically be
deferred to the next release and do not require re-submission unless
substantial revisions are made.

:::: note
::: title
:::

In most cases, you should not submit code changes to Rawhide until after
FESCo has voted to approve the proposal.
::::

### Change process milestones {#_change_process_milestones_3}

#### Proposal submission deadline {#_proposal_submission_deadline_3}

New change proposals may be submitted using the guidelines described
elsewhere and until the appropriate change proposal submission deadline.
For a given release, this date is available in the [release
schedule](https://fedorapeople.org/groups/schedule/) and will be
announced well in advance.

:::: note
::: title
:::

Changes do not have to be accepted by this deadline, but they must have
been submitted to the Change Wrangler (FOA) by then.
::::

#### Code complete (testable) deadline {#_code_complete_testable_deadline_3}

&#42; By this date, a new change must be feature complete or close
enough to completion that a majority of its functionality can be tested
prior the Beta release. &#42; If a change proposal page specifies a
change will be enabled by default, it must be so by this milestone.
&#42; Changes that are testable should have their tracking bug set to
the &#42;MODIFIED&#42; status.

:::: note
::: title
:::

At this point, Rawhide and the immediately-upcoming \'N+1\' release are
already separate branches. If development, testing, integration --- and
integration testing! --- are not really all lined up by this point,
there is no shame in re-targeting for the next (N+2) release. Now is the
time for you to bring that to FESCo. Or, if this change is
time-sensitive, but needs more resources or attention from across the
community, bring that to FESCo, to the Fedora Council, and to the Fedora
community at large.
::::

#### Code complete (100%) deadline {#_code_complete_100_deadline_3}

&#42; Changes must be code complete, meaning all the code required to
enable the new change is finished. &#42; The level of code completeness
is reflected as tracker bug state &#42;ON_QA&#42;. The change does not
have to be fully tested by this deadline.

:::: note
::: title
:::

Code complete (100%) deadline coincides with the Beta Freeze date
because that is the last date on which it can be ensured that a build
will appear in a milestone release. The idea is really that these
requirements be met in the Beta release, but due to the nature of the
milestone freezes, in order to ensure this is the case, the requirements
must be met by the freeze date.
::::

### Bugzilla trackers {#_bugzilla_trackers_3}

Approved change proposals will have Bugzilla issues created by the
Change Wrangler (FOA). The following status fields should be used to
reflect the status of the change:

+-----------------------------------+-----------------------------------+
| BZ Status                         | Meaning                           |
+===================================+===================================+
| ASSIGNED                          | Change approved by FESCo          |
+-----------------------------------+-----------------------------------+
| MODIFIED                          | Change is code complete enough to |
|                                   | be testable                       |
+-----------------------------------+-----------------------------------+
| ON_QA                             | Change is 100% code complete      |
+-----------------------------------+-----------------------------------+

: Bugzilla tracker statuses

:::: note
::: title
:::

Do not close tracking bugs when a change is complete. Instead, please
comment on your tracking bug that this change is complete. The Change
Wrangler (FOA) will auto-close tracking bugs as part of release
housekeeping.
::::

# Change submission guidance {#_change_submission_guidance}

In general, Changes are for coordination of development effort and for
communication (both internally and externally). They aren't mandates
that someone else implement an idea (no matter how good that idea). If
you have improvement in mind, work to get implementers committed to the
effort *before* filing a Change proposal, rather than expecting them to
show up for work once the Change is accepted.

:::: tip
::: title
:::

Watch the [Fedora Changes policy
video](https://www.youtube.com/watch?v=oERoxg-VYPo) for a quick
introduction to the process.
::::

## How do I propose a new change? {#_how_do_i_propose_a_new_change}

In order to be considered an official change proposal accepted for the
next Fedora Linux release, the change proposal must be formally
documented on a separate wiki page.

:::: tip
::: title
:::

Read the [policies](changes_policy.xml) for self-contained changes and
system-wide changes.
::::

:::: tip
::: title
:::

Pick the right category. Remember, the category can be changed to
another one based on community or FESCo review!
::::

1.  Create a new wiki page

    a.  When logged in, click the &#42;View Source&#42; button on the
        [empty change proposal
        form](https://fedoraproject.org/wiki/Changes/EmptyTemplate).

    b.  Copy the contents

    c.  Change the URL to
        https://fedoraproject.org/wiki/Changes/\\&lt;YourTitle\\&gt;
        (changing \'&lt;YourTitle&gt;\' to a slug for your page, e.g.
        \'ExampleChangeProposal\')

    d.  Click \'Create\'

    e.  Paste the contents

2.  Fill in the required details for the selected category (see inline
    comments and guidance below).

3.  Once you're satisfied with the change proposal page, set the wiki
    page category to &#96;ChangeReadyForWrangler&#96;, *and* set the
    appropriate change category (&#96;SelfContainedChange&#96; or
    &#96;SystemWideChange&#96;. Both categories must be set.

4.  Click the &#42;Save Changes&#42; button

:::: tip
::: title
:::

You can remove the HTML comments in the template if you choose.
::::

:::: warning
::: title
:::

Make sure to finish your change proposal by the change proposal
submission deadline! If you do not meet this deadline, you must seek an
exception from FESCo.
::::

The Program Manager is responsible for the actual announcement of the
change proposal, creating the FESCo ticket and tracking bug in Bugzilla.

## How do I show the status of a change I own? {#_how_do_i_show_the_status_of_a_change_i_own}

The progress of development is shown in Bugzilla with defined bug states
as explained in the change proposal template. Use this tracking bug to
show blockers, using the Blocks/Depends on fields (for example package
reviews), update the bug description with an actual status, and modify
the bug status to reflect current state. You may be asked by the Program
Manager or FESCo members to provide more detailed status (especially for
system-wide changes).

A Change is considered *code complete* when the bug state is moved to
ON_QA and when there are no blocking bugs open.

:::: note
::: title
:::

See the [Bugzilla trackers](changes_policy.adoc&#35;_bugzilla_trackers)
section of the Changes policy for more information on Bugzilla statuses.
::::

:::: note
::: title
:::

In most cases, you should not submit code changes to Rawhide until after
FESCo has voted to approve the proposal.
::::

## What are the change process deadline dates (Checkpoints)? {#_what_are_the_change_process_deadline_dates_checkpoints}

See the [Change Process
Milestones](changes_policy.adoc&#35;_change_process_milestones) section
of the Changes policy for information on the process milestones.

## What if I don't complete a change? {#_what_if_i_dont_complete_a_change}

Changes which cannot be completed for the release are automatically
deferred to the next release. You do not need to re-propose the Change
unless you are making substantial revisions to it. If you need to defer
a change, let the Program Manager know and they will update the wiki
page and the Bugzilla tracker appropriately.

## What if I have to modify my Change? {#_what_if_i_have_to_modify_my_change}

Minor modifications can be made at any time. If you have significant
modifications to make after a Change is approved, seek FESCo's approval.

## Section-by-section guidance {#_section_by_section_guidance}

### Change Proposal Name {#_change_proposal_name}

This should be descriptive, but unique. For example \'glibc 2.29\' is
preferable to \'glibc upgrade\'.

:::: tip
::: title
:::

Make sure your page is in the &#96;Changes&#96; namespace (e.g. call it
&#96;Changes/glibc_2.29&#96;)
::::

### Summary {#_summary}

A sentence or two summarizing what this change is and what it will do.
This information is used for the overall changeset summary page for each
release. Note that motivation for the change should be in the Motivation
section below, and this part should answer the question \'What?\' rather
than \'Why?\'.

:::: tip
::: title
:::

Assume that not everyone who sees this will know what you're talking
about. Give a brief description of packages or services where it makes
sense.
::::

### Owner {#_owner}

For change proposals to qualify as self-contained, owners of all
affected packages need to be included here. Alternatively, a SIG can be
listed as an owner if it owns all affected packages.

:::: tip
::: title
:::

Use your Bugzilla email in the &#96;email&#96; field to make your
Program Manager happy.
::::

### Current status {#_current_status}

Do not edit this section except to set the target release version and
update the &#96;\[\[Category:&#42;\]\]&#96; tags.

### Detailed Description {#_detailed_description}

Expand on the summary, if appropriate. A couple sentences suffices to
explain the goal, but the more details you can provide the better. If
there are multiple reasonable approaches, you should indicate why you
declined to use the others.

### Feedback {#_feedback}

Summarize the feedback from the community and address why you chose not
to accept proposed alternatives. This section is optional for all change
proposals, but is strongly suggested. Incorporating feedback here as it
is raised gives FESCo a clearer view of your proposal and leaves a good
record for the future. If you get no feedback, that is useful to note in
this section as well. This section is inspired in part by the \'Rejected
Ideas\' section described by
[PEP-0001](https://www.python.org/dev/peps/pep-0001/&#35;id46).

For innovative or possibly controversial ideas, consider collecting
feedback before you file the change proposal. This could be done via a
post to the devel mailing list for full community feedback, or sharing
with some additional people who you trust to give you candid feedback.
In the future, there will be more specific guidance about how to post
pre-proposal feedback. Either way, when you receive feedback, you should
summarize it in this section.

:::: tip
::: title
:::

You should fill in this section as feedback is received. As this is
optional the Program Manager does not need to wait for you to complete
this section before submitting to FESCo. If the discussion gets heated,
consider asking a neutral party to summarize the discussions for you.
This helps avoid bias and emotional response.
::::

### Benefit to Fedora {#_benefit_to_fedora}

What is the benefit to the distribution? Will the software we generate
be improved? How will the process of creating Fedora Linux releases be
improved?

Be sure to include the following areas if relevant:

&#42; If this is a major capability update, what has changed? For
example: This change introduces Python 5 that runs without the Global
Interpreter Lock and is fully multithreaded. &#42; If this is a new
functionality, what capabilities does it bring? For example: This change
allows package upgrades to be performed automatically and rolled-back at
will. &#42; Does this improve some specific package or set of packages?
For example: This change modifies a package to use a different language
stack that reduces install size by removing dependencies. &#42; Does
this improve specific Spins or Editions? For example: This change
modifies the default install of Fedora Workstation to be more in line
with the base install of Fedora Server. &#42; Does this make the
distribution more efficient? For example: This change replaces thousands
of individual %post scriptlets in packages with one script that runs at
the end. &#42; Is this an improvement to maintainer processes? For
example: Gating Fedora packages on automatic QA tests will make rawhide
more stable and allow changes to be implemented more smoothly. &#42; Is
this an improvement targeted at specific contributors? For example:
Ensuring that a minimal set of tools required for contribution to Fedora
are installed by default eases the onboarding of new contributors.

:::: tip
::: title
:::

When a Change has multiple benefits, it's better to list them all.
::::

### Scope {#_scope}

&#42; Proposal owners: What work do the feature owners have to
accomplish to complete the feature in time for release? Is it a large
change affecting many parts of the distribution or is it a very isolated
change? What are those changes? &#42; Other developers: &#42;REQUIRED
FOR SYSTEM-WIDE CHANGES&#42; What work do other developers have to
accomplish to complete the feature in time for release? Is it a large
change affecting many parts of the distribution or is it a very isolated
change? What are those changes? &#42; Release engineering: &#42;REQUIRED
FOR SYSTEM-WIDE CHANGES&#42; Does this feature require coordination with
release engineering (e.g. changes to installer image generation or
update package delivery)? Is a mass rebuild required? Include a link to
the releng issue. The issue is required to be filed prior to feature
submission, to ensure that someone is on board to do any process
development work and testing, and that all changes make it into the
pipeline; a bullet point in a change is not sufficient communication.
&#42; Policies and guidelines: Do the packaging guidelines or other
documents need to be updated for this feature? If so, does it need to
happen before or after the implementation is done? If a FPC ticket
exists, add a link here. Where possible, file a pull request against the
appropriate policy documents *before submitting the change proposal*.
That way, the community and FESCo can evaluate the specific changes
required. &#42; Trademark approval: If your Change may require trademark
approval (for example, if it is a new Spin), file a [Fedora Council
ticket](https://pagure.io/Fedora-Council/tickets/issues) requesting
trademark approval. &#42; Alignment with Objectives: Does your proposal
align with the [current Fedora Objectives](project::objectives.xml)?
This will not apply to many Changes, but it's important to consider when
proposing a Change. Being out of alignment isn't an automatic rejection,
it's just one more aspect to consider.

### Upgrade/compatibility impact {#_upgradecompatibility_impact}

&#42;REQUIRED FOR SYSTEM-WIDE CHANGES&#42; What happens to systems that
have had a previous versions of Fedora Linux installed and are updated
to the version containing this change? Will anything require manual
configuration or data migration? Will any existing functionality be no
longer supported?

### How To Test {#_how_to_test}

&#42;REQUIRED FOR SYSTEM-WIDE CHANGES&#42; This does not need to be a
full-fledged document. Describe the dimensions of tests that this change
implementation is expected to pass when it is done. If it needs to be
tested with different hardware or software configurations, indicate
them. The more specific you can be, the better the community testing can
be.

Remember that you are writing this how to for interested testers to use
to check out your change implementation - documenting what you do for
testing is OK, but it's much better to document what &#42;I&#42; can do
to test your change.

A good \'how to test\' should answer these four questions:

1.  What special hardware / data / etc. is needed (if any)?

2.  How do I prepare my system to test this change? What packages need
    to be installed, config files edited, etc.?

3.  What specific actions do I perform to check that the change is
    working like it's supposed to?

4.  What are the expected results of those actions?

### User Experience {#_user_experience}

If this change proposal is noticeable by users, how will their
experiences change as a result?

This section partially overlaps with the Benefit to Fedora section
above. This section should be primarily about the User Experience,
written in a way that does not assume deep technical knowledge. More
detailed technical description should be left for the Benefit to Fedora
section.

Describe what Users will see or notice, for example:

&#42; Packages are compressed more efficiently, making downloads and
upgrades faster by 10%. &#42; Kerberos tickets can be renewed
automatically. Users will now have to authenticate less and become more
productive. Credential management improvements mean a user can start
their work day with a single sign on and not have to pause for
reauthentication during their entire day. &#42; LibreOffice is one of
the most commonly installed applications on Fedora Linux and it is now
available by default to help users \'hit the ground running\'. &#42;
Green has been scientifically proven to be the most relaxing color. The
move to a default background color of green with green text will result
in Fedora Linux users being the most relaxed users of any operating
system.

### Dependencies {#_dependencies}

&#42;REQUIRED FOR SYSTEM-WIDE CHANGES&#42; What other packages (RPMs)
depend on this package? Are there changes outside the developers\'
control on which completion of this change depends? In other words,
completion of another change owned by someone else and might cause you
to not be able to finish on time or that you would need to coordinate?
Other upstream projects like the kernel (if this is not a kernel
change)?

### Contingency Plan {#_contingency_plan}

&#42;REQUIRED FOR SYSTEM-WIDE CHANGES&#42; If you cannot complete your
feature by the final development freeze, what is the backup plan? This
might be as simple as \'Revert the shipped configuration\'. Or it might
not (e.g. rebuilding a number of dependent packages). If your feature is
not completed in time, we want to assure others that other parts of
Fedora will not be in jeopardy.

A contingency plan should include:

&#42; Contingency mechanism: (What to do? Who will do it?) &#42;
Contingency deadline: When is the last time the contingency mechanism
can be put in place?

:::: tip
::: title
:::

The contingency deadline will most likely be the beta freeze. In some
cases, it may be more appropriate to set it to the start of the mass
rebuild or branch day. Rarely, you can use final freeze, but this should
only be used for Changes that are trivially-revertable.
::::

### Documentation {#_documentation}

&#42;REQUIRED FOR SYSTEM-WIDE CHANGES&#42; Is there upstream
documentation on this change, or notes you have written yourself? Link
to that material here so other interested developers can get involved.

### Release Notes {#_release_notes}

The Fedora Linux Release Notes inform end-users about what is new in the
release. Examples of [past release notes](release-notes::index.xml) are
on Fedora Docs. The release notes also help users know how to deal with
platform changes such as ABIs/APIs, configuration or data file formats,
or upgrade concerns. If there are any such changes involved in this
change, indicate them here. A link to upstream documentation will often
satisfy this need. This information forms the basis of the release notes
edited by the documentation team and shipped with the release.

# Change submission guidance {#_change_submission_guidance_2}

In general, Changes are for coordination of development effort and for
communication (both internally and externally). They aren't mandates
that someone else implement an idea (no matter how good that idea). If
you have improvement in mind, work to get implementers committed to the
effort *before* filing a Change proposal, rather than expecting them to
show up for work once the Change is accepted.

:::: tip
::: title
:::

Watch the [Fedora Changes policy
video](https://www.youtube.com/watch?v=oERoxg-VYPo) for a quick
introduction to the process.
::::

## How do I propose a new change? {#_how_do_i_propose_a_new_change_2}

In order to be considered an official change proposal accepted for the
next Fedora Linux release, the change proposal must be formally
documented on a separate wiki page.

:::: tip
::: title
:::

Read the [policies](changes_policy.xml) for self-contained changes and
system-wide changes.
::::

:::: tip
::: title
:::

Pick the right category. Remember, the category can be changed to
another one based on community or FESCo review!
::::

1.  Create a new wiki page

    a.  When logged in, click the &#42;View Source&#42; button on the
        [empty change proposal
        form](https://fedoraproject.org/wiki/Changes/EmptyTemplate).

    b.  Copy the contents

    c.  Change the URL to
        https://fedoraproject.org/wiki/Changes/\\&lt;YourTitle\\&gt;
        (changing \'&lt;YourTitle&gt;\' to a slug for your page, e.g.
        \'ExampleChangeProposal\')

    d.  Click \'Create\'

    e.  Paste the contents

2.  Fill in the required details for the selected category (see inline
    comments and guidance below).

3.  Once you're satisfied with the change proposal page, set the wiki
    page category to &#96;ChangeReadyForWrangler&#96;, *and* set the
    appropriate change category (&#96;SelfContainedChange&#96; or
    &#96;SystemWideChange&#96;. Both categories must be set.

4.  Click the &#42;Save Changes&#42; button

:::: tip
::: title
:::

You can remove the HTML comments in the template if you choose.
::::

:::: warning
::: title
:::

Make sure to finish your change proposal by the change proposal
submission deadline! If you do not meet this deadline, you must seek an
exception from FESCo.
::::

The Program Manager is responsible for the actual announcement of the
change proposal, creating the FESCo ticket and tracking bug in Bugzilla.

## How do I show the status of a change I own? {#_how_do_i_show_the_status_of_a_change_i_own_2}

The progress of development is shown in Bugzilla with defined bug states
as explained in the change proposal template. Use this tracking bug to
show blockers, using the Blocks/Depends on fields (for example package
reviews), update the bug description with an actual status, and modify
the bug status to reflect current state. You may be asked by the Program
Manager or FESCo members to provide more detailed status (especially for
system-wide changes).

A Change is considered *code complete* when the bug state is moved to
ON_QA and when there are no blocking bugs open.

:::: note
::: title
:::

See the [Bugzilla trackers](changes_policy.adoc&#35;_bugzilla_trackers)
section of the Changes policy for more information on Bugzilla statuses.
::::

:::: note
::: title
:::

In most cases, you should not submit code changes to Rawhide until after
FESCo has voted to approve the proposal.
::::

## What are the change process deadline dates (Checkpoints)? {#_what_are_the_change_process_deadline_dates_checkpoints_2}

See the [Change Process
Milestones](changes_policy.adoc&#35;_change_process_milestones) section
of the Changes policy for information on the process milestones.

## What if I don't complete a change? {#_what_if_i_dont_complete_a_change_2}

Changes which cannot be completed for the release are automatically
deferred to the next release. You do not need to re-propose the Change
unless you are making substantial revisions to it. If you need to defer
a change, let the Program Manager know and they will update the wiki
page and the Bugzilla tracker appropriately.

## What if I have to modify my Change? {#_what_if_i_have_to_modify_my_change_2}

Minor modifications can be made at any time. If you have significant
modifications to make after a Change is approved, seek FESCo's approval.

## Section-by-section guidance {#_section_by_section_guidance_2}

### Change Proposal Name {#_change_proposal_name_2}

This should be descriptive, but unique. For example \'glibc 2.29\' is
preferable to \'glibc upgrade\'.

:::: tip
::: title
:::

Make sure your page is in the &#96;Changes&#96; namespace (e.g. call it
&#96;Changes/glibc_2.29&#96;)
::::

### Summary {#_summary_2}

A sentence or two summarizing what this change is and what it will do.
This information is used for the overall changeset summary page for each
release. Note that motivation for the change should be in the Motivation
section below, and this part should answer the question \'What?\' rather
than \'Why?\'.

:::: tip
::: title
:::

Assume that not everyone who sees this will know what you're talking
about. Give a brief description of packages or services where it makes
sense.
::::

### Owner {#_owner_2}

For change proposals to qualify as self-contained, owners of all
affected packages need to be included here. Alternatively, a SIG can be
listed as an owner if it owns all affected packages.

:::: tip
::: title
:::

Use your Bugzilla email in the &#96;email&#96; field to make your
Program Manager happy.
::::

### Current status {#_current_status_2}

Do not edit this section except to set the target release version and
update the &#96;\[\[Category:&#42;\]\]&#96; tags.

### Detailed Description {#_detailed_description_2}

Expand on the summary, if appropriate. A couple sentences suffices to
explain the goal, but the more details you can provide the better. If
there are multiple reasonable approaches, you should indicate why you
declined to use the others.

### Feedback {#_feedback_2}

Summarize the feedback from the community and address why you chose not
to accept proposed alternatives. This section is optional for all change
proposals, but is strongly suggested. Incorporating feedback here as it
is raised gives FESCo a clearer view of your proposal and leaves a good
record for the future. If you get no feedback, that is useful to note in
this section as well. This section is inspired in part by the \'Rejected
Ideas\' section described by
[PEP-0001](https://www.python.org/dev/peps/pep-0001/&#35;id46).

For innovative or possibly controversial ideas, consider collecting
feedback before you file the change proposal. This could be done via a
post to the devel mailing list for full community feedback, or sharing
with some additional people who you trust to give you candid feedback.
In the future, there will be more specific guidance about how to post
pre-proposal feedback. Either way, when you receive feedback, you should
summarize it in this section.

:::: tip
::: title
:::

You should fill in this section as feedback is received. As this is
optional the Program Manager does not need to wait for you to complete
this section before submitting to FESCo. If the discussion gets heated,
consider asking a neutral party to summarize the discussions for you.
This helps avoid bias and emotional response.
::::

### Benefit to Fedora {#_benefit_to_fedora_2}

What is the benefit to the distribution? Will the software we generate
be improved? How will the process of creating Fedora Linux releases be
improved?

Be sure to include the following areas if relevant:

&#42; If this is a major capability update, what has changed? For
example: This change introduces Python 5 that runs without the Global
Interpreter Lock and is fully multithreaded. &#42; If this is a new
functionality, what capabilities does it bring? For example: This change
allows package upgrades to be performed automatically and rolled-back at
will. &#42; Does this improve some specific package or set of packages?
For example: This change modifies a package to use a different language
stack that reduces install size by removing dependencies. &#42; Does
this improve specific Spins or Editions? For example: This change
modifies the default install of Fedora Workstation to be more in line
with the base install of Fedora Server. &#42; Does this make the
distribution more efficient? For example: This change replaces thousands
of individual %post scriptlets in packages with one script that runs at
the end. &#42; Is this an improvement to maintainer processes? For
example: Gating Fedora packages on automatic QA tests will make rawhide
more stable and allow changes to be implemented more smoothly. &#42; Is
this an improvement targeted at specific contributors? For example:
Ensuring that a minimal set of tools required for contribution to Fedora
are installed by default eases the onboarding of new contributors.

:::: tip
::: title
:::

When a Change has multiple benefits, it's better to list them all.
::::

### Scope {#_scope_2}

&#42; Proposal owners: What work do the feature owners have to
accomplish to complete the feature in time for release? Is it a large
change affecting many parts of the distribution or is it a very isolated
change? What are those changes? &#42; Other developers: &#42;REQUIRED
FOR SYSTEM-WIDE CHANGES&#42; What work do other developers have to
accomplish to complete the feature in time for release? Is it a large
change affecting many parts of the distribution or is it a very isolated
change? What are those changes? &#42; Release engineering: &#42;REQUIRED
FOR SYSTEM-WIDE CHANGES&#42; Does this feature require coordination with
release engineering (e.g. changes to installer image generation or
update package delivery)? Is a mass rebuild required? Include a link to
the releng issue. The issue is required to be filed prior to feature
submission, to ensure that someone is on board to do any process
development work and testing, and that all changes make it into the
pipeline; a bullet point in a change is not sufficient communication.
&#42; Policies and guidelines: Do the packaging guidelines or other
documents need to be updated for this feature? If so, does it need to
happen before or after the implementation is done? If a FPC ticket
exists, add a link here. Where possible, file a pull request against the
appropriate policy documents *before submitting the change proposal*.
That way, the community and FESCo can evaluate the specific changes
required. &#42; Trademark approval: If your Change may require trademark
approval (for example, if it is a new Spin), file a [Fedora Council
ticket](https://pagure.io/Fedora-Council/tickets/issues) requesting
trademark approval. &#42; Alignment with Objectives: Does your proposal
align with the [current Fedora Objectives](project::objectives.xml)?
This will not apply to many Changes, but it's important to consider when
proposing a Change. Being out of alignment isn't an automatic rejection,
it's just one more aspect to consider.

### Upgrade/compatibility impact {#_upgradecompatibility_impact_2}

&#42;REQUIRED FOR SYSTEM-WIDE CHANGES&#42; What happens to systems that
have had a previous versions of Fedora Linux installed and are updated
to the version containing this change? Will anything require manual
configuration or data migration? Will any existing functionality be no
longer supported?

### How To Test {#_how_to_test_2}

&#42;REQUIRED FOR SYSTEM-WIDE CHANGES&#42; This does not need to be a
full-fledged document. Describe the dimensions of tests that this change
implementation is expected to pass when it is done. If it needs to be
tested with different hardware or software configurations, indicate
them. The more specific you can be, the better the community testing can
be.

Remember that you are writing this how to for interested testers to use
to check out your change implementation - documenting what you do for
testing is OK, but it's much better to document what &#42;I&#42; can do
to test your change.

A good \'how to test\' should answer these four questions:

1.  What special hardware / data / etc. is needed (if any)?

2.  How do I prepare my system to test this change? What packages need
    to be installed, config files edited, etc.?

3.  What specific actions do I perform to check that the change is
    working like it's supposed to?

4.  What are the expected results of those actions?

### User Experience {#_user_experience_2}

If this change proposal is noticeable by users, how will their
experiences change as a result?

This section partially overlaps with the Benefit to Fedora section
above. This section should be primarily about the User Experience,
written in a way that does not assume deep technical knowledge. More
detailed technical description should be left for the Benefit to Fedora
section.

Describe what Users will see or notice, for example:

&#42; Packages are compressed more efficiently, making downloads and
upgrades faster by 10%. &#42; Kerberos tickets can be renewed
automatically. Users will now have to authenticate less and become more
productive. Credential management improvements mean a user can start
their work day with a single sign on and not have to pause for
reauthentication during their entire day. &#42; LibreOffice is one of
the most commonly installed applications on Fedora Linux and it is now
available by default to help users \'hit the ground running\'. &#42;
Green has been scientifically proven to be the most relaxing color. The
move to a default background color of green with green text will result
in Fedora Linux users being the most relaxed users of any operating
system.

### Dependencies {#_dependencies_2}

&#42;REQUIRED FOR SYSTEM-WIDE CHANGES&#42; What other packages (RPMs)
depend on this package? Are there changes outside the developers\'
control on which completion of this change depends? In other words,
completion of another change owned by someone else and might cause you
to not be able to finish on time or that you would need to coordinate?
Other upstream projects like the kernel (if this is not a kernel
change)?

### Contingency Plan {#_contingency_plan_2}

&#42;REQUIRED FOR SYSTEM-WIDE CHANGES&#42; If you cannot complete your
feature by the final development freeze, what is the backup plan? This
might be as simple as \'Revert the shipped configuration\'. Or it might
not (e.g. rebuilding a number of dependent packages). If your feature is
not completed in time, we want to assure others that other parts of
Fedora will not be in jeopardy.

A contingency plan should include:

&#42; Contingency mechanism: (What to do? Who will do it?) &#42;
Contingency deadline: When is the last time the contingency mechanism
can be put in place?

:::: tip
::: title
:::

The contingency deadline will most likely be the beta freeze. In some
cases, it may be more appropriate to set it to the start of the mass
rebuild or branch day. Rarely, you can use final freeze, but this should
only be used for Changes that are trivially-revertable.
::::

### Documentation {#_documentation_2}

&#42;REQUIRED FOR SYSTEM-WIDE CHANGES&#42; Is there upstream
documentation on this change, or notes you have written yourself? Link
to that material here so other interested developers can get involved.

### Release Notes {#_release_notes_2}

The Fedora Linux Release Notes inform end-users about what is new in the
release. Examples of [past release notes](release-notes::index.xml) are
on Fedora Docs. The release notes also help users know how to deal with
platform changes such as ABIs/APIs, configuration or data file formats,
or upgrade concerns. If there are any such changes involved in this
change, indicate them here. A link to upstream documentation will often
satisfy this need. This information forms the basis of the release notes
edited by the documentation team and shipped with the release.

# Changes process rationale and history {#_changes_process_rationale_and_history}

The reason we have a Changes process is to coordinate work across the
project. We want to make sure everyone is aware of what's going on in
order to get community feedback and ensure we're working in the same
direction. The Changes process is ultimately about *communication*, not
*gatekeeping*.

For an opinionated view on the Changes process, see Ben Cotton's
[Opensource.com
article](https://opensource.com/article/19/3/managing-changes-open-source-projects)
or [DevConf.CZ 2019 talk](https://www.youtube.com/watch?v=cVV1K3Junkc).

## History {#_history_3}

Prior to Fedora 20, Fedora used a process called the "Features" process.
This involved determining if a change was a "feature" or an
"enhancement". Enhancements were considered not worth tracking, but
features were highly user-visible or marketing-worthy and got extra
attention. This was done in the form of manually specifying completion
percentage in the wiki and other fun tasks.

FESCo identified several key problems with this process:

&#42; The definition of a "feature" was ambiguous which led to people
submitting features unnecessarily, leading to extra administrative
overhead. &#42; The wiki page had duplicated data input &#42; The
process didn't account for different types or scopes of features &#42;
Features weren't visible to the community until after the feature
proposals were approved

For Fedora 20, we introduced a new process called the "Changes" process.
In some ways, it looks very similar to the previous Features process,
but it had a few key differences. First, Changes are broken out into
"System-Wide" and "Self-Contained" changes. System-Wide changes involve
system-wide defaults, critical path components, or other changes that
have a broad impact. Self-Contained changes have limited scope and
impact on the rest of the project. They may be the changes to leaf
packages or changes that occur within the responsibility of a single
team. Notably, Changes aren't necessarily things that get shipped in the
distribution---they may also include changes in how packages are built
or other sorts of meta-work.

Both System-Wide and Self-Contained Changes go through the same process.
The main differences are the standard of scrutiny and the required
input. System-Wide Changes must list the impact on other developers, a
listing of policy changes required, upgrade impact, a test plan, a
contingency plan, and documentation.

# Fedora Elections {#_fedora_elections}

Fedora has several elected bodies that regularly conduct elections every
release cycle. In addition, Fedora teams can request one-off elections
from the Fedora Program Manager when trying to select new leadership or
otherwise reach a decision through a formal voting process.

## Upcoming elections {#_upcoming_elections}

The following elections will take place after each release:

&#42; [FESCo
(Engineering)](https://fedoraproject.org/wiki/Development/SteeringCommittee/Nominations)
&#42; [Fedora
Council](https://fedoraproject.org/wiki/Council/Nominations) &#42;
[Mindshare](https://fedoraproject.org/wiki/Mindshare/Nominations) &#42;
[EPEL Steering
Committee](https://fedoraproject.org/wiki/EPEL/Nominations)

### Schedule {#_schedule}

See the [election
schedule](https://fedorapeople.org/groups/schedule/f-43/f-43-elections-tasks.html)
for authoritative dates. Dates may change based on the final release
date.

## Elections process {#_elections_process}

### Selection of questions from Questionnaire {#_selection_of_questions_from_questionnaire}

From the set of collected questions for nominees to FESCo (Engineering),
Fedora Council, and Mindshare\|Mindshare teams, top 3 questions are
selected, based on [Council
decision](https://pagure.io/Fedora-Council/tickets/issue/156). The
selected questions will be given to each candidate to answer before the
voting period begins as part of campaign.

The top selected questions for each body are put in templates in a
non-public part of the elections-interviews repo
(&#96;ssh://git@pagure.io/tickets/fedora-pgm/elections-interviews.git&#96;).

### Nominations for Elected Positions {#_nominations_for_elected_positions}

During this period people may self-nominate to open seats. If they wish
to nominate someone else, please consult with that person ahead of time.

### Interviews {#_interviews}

Nominees are requested to answer the selected questions using a [private
issue in
Pagure](https://pagure.io/fedora-pgm/elections-interviews/issues). In
this way, only the Program Manager and Fedora Action and Impact
Coordinator (as election wrangler substitute) are allowed to see these
answers.

### Voting Setup &amp; Validation &amp; Publishing of interviews {#_voting_setup_amp_validation_amp_publishing_of_interviews}

It is the responsibility of the Program Manager to validate the
eligibility of nominees for elections. In compliance with [Fedora
Council decision
&#35;135](https://pagure.io/Fedora-Council/tickets/issue/135), nominees
not having completed their interviews (as a private issue in Pagure) are
excluded from the list of nominees.

The Program Manager is responsible for publishing these interviews on
the [Fedora Community Blog](https://communityblog.fedoraproject.org/) as
well as setup of the [voting
machine](https://elections.fedoraproject.org/) for the elections.

### Voting Information {#_voting_information}

The [Fedora Elections Guide](elections_guide.xml) has information on the
voting method used in the Fedora elections and detailed instructions on
how to cast your vote.

If you are familiar with the voting process, you may go straight to the
[elections application](https://elections.fedoraproject.org/) to cast
your votes.

:::: note
::: title
:::

&#42;Eligible Voters&#42; Voting eligibility is determined by a
community member's Fedora Account System (FAS) memberships.

&#42; To vote for the Fedora Council you must have cla_done in FAS.
&#42; To vote for FESCo you must have cla_done + one other \'non-cla\'
group in FAS. &#42; To vote for Mindshare you must have a cla_done in
FAS. &#42; To vote for EPEL Steering Committee you must have cla_done +
one other \'non-cla\' group in FAS.
::::

## Historical elections {#_historical_elections}

&#42; See the [Elections
archive](https://elections.fedoraproject.org/archives) for historical
results.

# Elections Guide {#_elections_guide}

Fedora Elections are run using the Elections App and Range Voting.

## Voting Eligibility {#_voting_eligibility}

Eligible voters are determined by their Fedora Account System (FAS)
membership.

&#42; To vote for the Fedora Council you must have &#96;cla_done&#96; in
FAS. &#42; To vote for FESCo you must have &#96;cla_done&#96; + one
other \'non-cla\' group in FAS. &#42; To vote for Mindshare you must
have a &#96;cla_done&#96; in FAS. &#42; To vote for EPEL Steering
Committee you must have &#96;cla_done&#96; + one other \'non-cla\' group
in FAS.

## How to Vote {#_how_to_vote}

Visit the [Elections App](https://elections.fedoraproject.org/) and
select the election box you would like to vote in. You may vote in all
of the elections if you wish, but you may only vote in each election box
once, i.e. you may vote in Council, FESCo and EPEL but you may only vote
in each group once and not multiple times. Click on the 'vote now'
button on the elections box page and select the range you wish to place
against each candidate running. It is advisable to allocate a number to
each candidate based on your preference.

You will be asked to preview your score, and once you are happy, press
the 'Submit your vote' button. Then you are done, and don't forget to
claim your 'I Voted!' Fedora badge too!

## Information on Range Voting {#_information_on_range_voting}

Fedora Project has implemented &#42;Range Voting&#42; for our elections,
in particular the \'Range (score-summing, blanks treated as zero score,
no quorum rule)\' range voting system.

To cast your vote in this election simply select a value between 0 and 3
with 0 as \'least or no preference\' and 3 as \'highest preference\'.

At the end of the election, the highest ranking candidate(s) are marked
as the winners.

For more information about Range Voting, visit the Center for [Range
Voting](https://rangevoting.org/).

# Fedora Elections {#_fedora_elections_2}

Fedora has several elected bodies that regularly conduct elections every
release cycle. In addition, Fedora teams can request one-off elections
from the Fedora Program Manager when trying to select new leadership or
otherwise reach a decision through a formal voting process.

## Upcoming elections {#_upcoming_elections_2}

The following elections will take place after each release:

&#42; [FESCo
(Engineering)](https://fedoraproject.org/wiki/Development/SteeringCommittee/Nominations)
&#42; [Fedora
Council](https://fedoraproject.org/wiki/Council/Nominations) &#42;
[Mindshare](https://fedoraproject.org/wiki/Mindshare/Nominations) &#42;
[EPEL Steering
Committee](https://fedoraproject.org/wiki/EPEL/Nominations)

### Schedule {#_schedule_2}

See the [election
schedule](https://fedorapeople.org/groups/schedule/f-43/f-43-elections-tasks.html)
for authoritative dates. Dates may change based on the final release
date.

## Elections process {#_elections_process_2}

### Selection of questions from Questionnaire {#_selection_of_questions_from_questionnaire_2}

From the set of collected questions for nominees to FESCo (Engineering),
Fedora Council, and Mindshare\|Mindshare teams, top 3 questions are
selected, based on [Council
decision](https://pagure.io/Fedora-Council/tickets/issue/156). The
selected questions will be given to each candidate to answer before the
voting period begins as part of campaign.

The top selected questions for each body are put in templates in a
non-public part of the elections-interviews repo
(&#96;ssh://git@pagure.io/tickets/fedora-pgm/elections-interviews.git&#96;).

### Nominations for Elected Positions {#_nominations_for_elected_positions_2}

During this period people may self-nominate to open seats. If they wish
to nominate someone else, please consult with that person ahead of time.

### Interviews {#_interviews_2}

Nominees are requested to answer the selected questions using a [private
issue in
Pagure](https://pagure.io/fedora-pgm/elections-interviews/issues). In
this way, only the Program Manager and Fedora Action and Impact
Coordinator (as election wrangler substitute) are allowed to see these
answers.

### Voting Setup &amp; Validation &amp; Publishing of interviews {#_voting_setup_amp_validation_amp_publishing_of_interviews_2}

It is the responsibility of the Program Manager to validate the
eligibility of nominees for elections. In compliance with [Fedora
Council decision
&#35;135](https://pagure.io/Fedora-Council/tickets/issue/135), nominees
not having completed their interviews (as a private issue in Pagure) are
excluded from the list of nominees.

The Program Manager is responsible for publishing these interviews on
the [Fedora Community Blog](https://communityblog.fedoraproject.org/) as
well as setup of the [voting
machine](https://elections.fedoraproject.org/) for the elections.

### Voting Information {#_voting_information_2}

The [Fedora Elections Guide](elections_guide.xml) has information on the
voting method used in the Fedora elections and detailed instructions on
how to cast your vote.

If you are familiar with the voting process, you may go straight to the
[elections application](https://elections.fedoraproject.org/) to cast
your votes.

:::: note
::: title
:::

&#42;Eligible Voters&#42; Voting eligibility is determined by a
community member's Fedora Account System (FAS) memberships.

&#42; To vote for the Fedora Council you must have cla_done in FAS.
&#42; To vote for FESCo you must have cla_done + one other \'non-cla\'
group in FAS. &#42; To vote for Mindshare you must have a cla_done in
FAS. &#42; To vote for EPEL Steering Committee you must have cla_done +
one other \'non-cla\' group in FAS.
::::

## Historical elections {#_historical_elections_2}

&#42; See the [Elections
archive](https://elections.fedoraproject.org/archives) for historical
results.

# Fedora Elections {#_fedora_elections_3}

Fedora has several elected bodies that regularly conduct elections every
release cycle. In addition, Fedora teams can request one-off elections
from the Fedora Program Manager when trying to select new leadership or
otherwise reach a decision through a formal voting process.

## Upcoming elections {#_upcoming_elections_3}

The following elections will take place after each release:

&#42; [FESCo
(Engineering)](https://fedoraproject.org/wiki/Development/SteeringCommittee/Nominations)
&#42; [Fedora
Council](https://fedoraproject.org/wiki/Council/Nominations) &#42;
[Mindshare](https://fedoraproject.org/wiki/Mindshare/Nominations) &#42;
[EPEL Steering
Committee](https://fedoraproject.org/wiki/EPEL/Nominations)

### Schedule {#_schedule_3}

See the [election
schedule](https://fedorapeople.org/groups/schedule/f-43/f-43-elections-tasks.html)
for authoritative dates. Dates may change based on the final release
date.

## Elections process {#_elections_process_3}

### Selection of questions from Questionnaire {#_selection_of_questions_from_questionnaire_3}

From the set of collected questions for nominees to FESCo (Engineering),
Fedora Council, and Mindshare\|Mindshare teams, top 3 questions are
selected, based on [Council
decision](https://pagure.io/Fedora-Council/tickets/issue/156). The
selected questions will be given to each candidate to answer before the
voting period begins as part of campaign.

The top selected questions for each body are put in templates in a
non-public part of the elections-interviews repo
(&#96;ssh://git@pagure.io/tickets/fedora-pgm/elections-interviews.git&#96;).

### Nominations for Elected Positions {#_nominations_for_elected_positions_3}

During this period people may self-nominate to open seats. If they wish
to nominate someone else, please consult with that person ahead of time.

### Interviews {#_interviews_3}

Nominees are requested to answer the selected questions using a [private
issue in
Pagure](https://pagure.io/fedora-pgm/elections-interviews/issues). In
this way, only the Program Manager and Fedora Action and Impact
Coordinator (as election wrangler substitute) are allowed to see these
answers.

### Voting Setup &amp; Validation &amp; Publishing of interviews {#_voting_setup_amp_validation_amp_publishing_of_interviews_3}

It is the responsibility of the Program Manager to validate the
eligibility of nominees for elections. In compliance with [Fedora
Council decision
&#35;135](https://pagure.io/Fedora-Council/tickets/issue/135), nominees
not having completed their interviews (as a private issue in Pagure) are
excluded from the list of nominees.

The Program Manager is responsible for publishing these interviews on
the [Fedora Community Blog](https://communityblog.fedoraproject.org/) as
well as setup of the [voting
machine](https://elections.fedoraproject.org/) for the elections.

### Voting Information {#_voting_information_3}

The [Fedora Elections Guide](elections_guide.xml) has information on the
voting method used in the Fedora elections and detailed instructions on
how to cast your vote.

If you are familiar with the voting process, you may go straight to the
[elections application](https://elections.fedoraproject.org/) to cast
your votes.

:::: note
::: title
:::

&#42;Eligible Voters&#42; Voting eligibility is determined by a
community member's Fedora Account System (FAS) memberships.

&#42; To vote for the Fedora Council you must have cla_done in FAS.
&#42; To vote for FESCo you must have cla_done + one other \'non-cla\'
group in FAS. &#42; To vote for Mindshare you must have a cla_done in
FAS. &#42; To vote for EPEL Steering Committee you must have cla_done +
one other \'non-cla\' group in FAS.
::::

## Historical elections {#_historical_elections_3}

&#42; See the [Elections
archive](https://elections.fedoraproject.org/archives) for historical
results.

# Fedora Elections {#_fedora_elections_4}

Fedora has several elected bodies that regularly conduct elections every
release cycle. In addition, Fedora teams can request one-off elections
from the Fedora Program Manager when trying to select new leadership or
otherwise reach a decision through a formal voting process.

## Upcoming elections {#_upcoming_elections_4}

The following elections will take place after each release:

&#42; [FESCo
(Engineering)](https://fedoraproject.org/wiki/Development/SteeringCommittee/Nominations)
&#42; [Fedora
Council](https://fedoraproject.org/wiki/Council/Nominations) &#42;
[Mindshare](https://fedoraproject.org/wiki/Mindshare/Nominations) &#42;
[EPEL Steering
Committee](https://fedoraproject.org/wiki/EPEL/Nominations)

### Schedule {#_schedule_4}

See the [election
schedule](https://fedorapeople.org/groups/schedule/f-43/f-43-elections-tasks.html)
for authoritative dates. Dates may change based on the final release
date.

## Elections process {#_elections_process_4}

### Selection of questions from Questionnaire {#_selection_of_questions_from_questionnaire_4}

From the set of collected questions for nominees to FESCo (Engineering),
Fedora Council, and Mindshare\|Mindshare teams, top 3 questions are
selected, based on [Council
decision](https://pagure.io/Fedora-Council/tickets/issue/156). The
selected questions will be given to each candidate to answer before the
voting period begins as part of campaign.

The top selected questions for each body are put in templates in a
non-public part of the elections-interviews repo
(&#96;ssh://git@pagure.io/tickets/fedora-pgm/elections-interviews.git&#96;).

### Nominations for Elected Positions {#_nominations_for_elected_positions_4}

During this period people may self-nominate to open seats. If they wish
to nominate someone else, please consult with that person ahead of time.

### Interviews {#_interviews_4}

Nominees are requested to answer the selected questions using a [private
issue in
Pagure](https://pagure.io/fedora-pgm/elections-interviews/issues). In
this way, only the Program Manager and Fedora Action and Impact
Coordinator (as election wrangler substitute) are allowed to see these
answers.

### Voting Setup &amp; Validation &amp; Publishing of interviews {#_voting_setup_amp_validation_amp_publishing_of_interviews_4}

It is the responsibility of the Program Manager to validate the
eligibility of nominees for elections. In compliance with [Fedora
Council decision
&#35;135](https://pagure.io/Fedora-Council/tickets/issue/135), nominees
not having completed their interviews (as a private issue in Pagure) are
excluded from the list of nominees.

The Program Manager is responsible for publishing these interviews on
the [Fedora Community Blog](https://communityblog.fedoraproject.org/) as
well as setup of the [voting
machine](https://elections.fedoraproject.org/) for the elections.

### Voting Information {#_voting_information_4}

The [Fedora Elections Guide](elections_guide.xml) has information on the
voting method used in the Fedora elections and detailed instructions on
how to cast your vote.

If you are familiar with the voting process, you may go straight to the
[elections application](https://elections.fedoraproject.org/) to cast
your votes.

:::: note
::: title
:::

&#42;Eligible Voters&#42; Voting eligibility is determined by a
community member's Fedora Account System (FAS) memberships.

&#42; To vote for the Fedora Council you must have cla_done in FAS.
&#42; To vote for FESCo you must have cla_done + one other \'non-cla\'
group in FAS. &#42; To vote for Mindshare you must have a cla_done in
FAS. &#42; To vote for EPEL Steering Committee you must have cla_done +
one other \'non-cla\' group in FAS.
::::

## Historical elections {#_historical_elections_4}

&#42; See the [Elections
archive](https://elections.fedoraproject.org/archives) for historical
results.

# Prioritized Bugs {#_prioritized_bugs}

&#42; [Nominated
bugs](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__\&amp;f1=flagtypes.name\&amp;f2=OP\&amp;list_id=10626345\&amp;o1=substring\&amp;query_format=advanced\&amp;v1=fedora_prioritized_bug%3F)
&#42; [Accepted
bugs](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__\&amp;f1=flagtypes.name\&amp;f2=OP\&amp;list_id=10626381\&amp;o1=substring\&amp;query_format=advanced\&amp;v1=fedora_prioritized_bug%2B)

The purpose of this process is to help with processing backlog of bugs
and issues found during the development, verification, and use of Fedora
distribution. The main goal is to raise visibility of bugs and issues to
help contributors focus on the most important issues. The general
criterion for such bugs is \'failure to resolve this bug will result in
unpleasantness for a subjectively large subset of users\'.

Bugs that are evaluated as part of the [blocker bug
process](https://fedoraproject.org/wiki/QA:SOP_blocker_bug_process) are
considered prioritized by virtue of their blocker status. The
prioritized bugs process intentionally excludes include blocker bugs for
that reason.

All Fedora community members are welcome to participate by joining the
[Triage mailing
list](https://lists.fedoraproject.org/archives/list/triage%40lists.fedoraproject.org/)
and attending the [evaluation meetings](#_evaluation).

## Process description {#_process_description}

All the bugs and issues in the Fedora distribution are tracked in
[Bugzilla](https://bugzilla.redhat.com/). As such, every item on the
\'Prioritized bugs and issues\' list has assigned a bug ID and can be
tracked using standard Bugzilla tools.

The process consists of three main parts:

&#42; Nomination &#42; Evaluation &#42; Ageing

:::: note
::: title
:::

Prior to November 2019, bugs were tracked using the *Keywords* and
*Whiteboard* fields in Bugzilla. This occasionally lead to collisions
with how development teams used those fields, so we switched to using a
specific flag.
::::

### Nomination {#_nomination}

Issues eligible for this status are those which do not necessarily fail
a release criterion, but which have critical impact on a Fedora Edition
or on a council-approved Fedora Objective. Issues may also be nominated
from the Common Bugs list when they are deemed by QA to have critical
impact.

Anyone from the Fedora community can nominate a bug to be evaluated for
inclusion to the \'Prioritized bugs and issues\' list. The nomination is
done by setting the &#96;fedora_prioritized_bug&#96; flag to
&#96;?&#96;.

:::: tip
::: title
:::

You may need to click the *set flags* link on the bug in order for the
available flags to appear.
::::

The list of currently nominated bugs waiting for evaluation can be seen
using the [Bugzilla search
tool](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__\&amp;f1=flagtypes.name\&amp;f2=OP\&amp;list_id=10626345\&amp;o1=substring\&amp;query_format=advanced\&amp;v1=fedora_prioritized_bug%3F).

### Evaluation {#_evaluation}

Evaluation of nominated bugs is done by the Evaluation team. This team
is comprised of the [Fedora Project Leader](council::fpl.xml) (FPL),
[Fedora Program Manager](council::fpgm.xml) (FPgM), and people
representing Fedora Working Groups and Special Interest Groups, as well
as interested community members. The team does not have fixed group of
members. Instead members of the Evaluation team are formed at the
beginning of the meeting during Roll Call.

The team of evaluators meets on regular bi-weekly meetings on Wednesdays
at 10:00 AM US/Eastern in the
[&#35;fedora-meeting-1](https://web.libera.chat/?channels=&#35;fedora-meeting-1)
channel. See [Base Fedocal](https://calendar.fedoraproject.org/base/)
for the authoritative meeting schedule. The purpose of the regular
meeting is to review bugs nominated to the \'Prioritized bugs and
issues\' list and follow up on previously-approved bugs.

All the bugs accepted during the Evaluation meeting are marked by
setting the &#96;fedora_prioritized_bug&#96; flag to &#96;+&#96;. Bugs
that are rejected during the Evaluation meeting are marked by setting
the &#96;fedora_prioritized_bug&#96; flag to &#96;-&#96;. After the
evaluation meeting, the chair exports the list of all Prioritized bugs
to the \'Prioritized bugs and issues\' list and sends a report to the
[Triage mailing
list](https://lists.fedoraproject.org/archives/list/triage%40lists.fedoraproject.org/).
Accepted bugs are reviewed in subsequent meetings, time permitting, and
if there is no movement, they will be escalated.

The list of currently approved bugs can be seen using the [Bugzilla
search
tool](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__\&amp;f1=flagtypes.name\&amp;f2=OP\&amp;list_id=10626381\&amp;o1=substring\&amp;query_format=advanced\&amp;v1=fedora_prioritized_bug%2B).

#### Process for accepted bugs {#_process_for_accepted_bugs}

The hope is that most maintainers will see that a bug is flagged as a
Prioritized Bug and move it to the top of the pile. After all, we
prioritize relatively few bugs. However that doesn't always pan out for
a variety of reasons. This is a rough idea of what happens after a bug
is accepted as a Prioritized Bug:

&#42; The FPgM marks the bug as prioritized in Bugzilla after the
meeting &#42; After \~1 weeks with no visible progress or
acknowledgement, the FPgM marks the assignee as NEEDINFO in Bugzilla
&#42; After another \~1 week with no visible progress or
acknowledgement, the FPgM contacts the assignee outside of Bugzilla
&#42; After another \~2 weeks with no visible progress or
acknowledgement, the FPL or FPgM will escalate the bug to the assignee's
manager (if they are a Red Hat employee acting in their work role) or to
a provenpackager

:::: note
::: title
:::

The escalation is not intended to be \'this person isn't doing their
job\' in character. It is a \'hey, can you make sure your team has
resources to look at this problem that Fedora has identified as a
priority?\'
::::

:::: note
::: title
:::

When need dictates (e.g. a coming release milestone), the timeline above
may be compressed.
::::

If the evaluation team determines after working with the maintainers
that a resolution is not possible, the team may decide to remove
Prioritized Bug status.

# Program Management resources {#_program_management_resources}

This page collects training and reference resources. You may find this
useful if you're doing program or project management in Fedora.

## General program/project management {#_general_programproject_management}

&#42; [Herding cats: program management in
communities](https://www.youtube.com/watch?v=u3xBk8boiy8) (video) ---
Presented by Ben Cotton at DevConf.US 2020 &#42; [Meeting
training](https://youtu.be/3hG4Y09reZg) (video) &#42; [Duck Alignment
Academy](https://duckalignment.academy), Ben Cotton's program management
website

## Fedora policies and procedures {#_fedora_policies_and_procedures}

&#42; [Fedora Changes
process](https://www.youtube.com/watch?v=oERoxg-VYPo) (video) &#42;
[Change wrangling training](https://www.youtube.com/watch?v=Y3nVlwn4MC0)
(video) &#42; [Managing changes in open source
projects](https://www.youtube.com/watch?v=cVV1K3Junkc) (video) ---
Presented by Ben Cotton at DevConf.CZ 2019

## Tools {#_tools}

&#42; [Pagure training](https://youtu.be/ZLAkqJ-V-kw) (video) &#42;
[Schedule training](https://www.youtube.com/watch?v=llLbkynSV5c) (video)
&#42; [Taiga training](https://youtu.be/ISlI-Qxwe6E) (video)

# Fedora Program Manager Guide {#_fedora_program_manager_guide}

This guide provides information on how to do the work of the Fedora
Program Manager. If you are not the Fedora Program Manager, you are
welcome to keep reading --- this document may be informative for you ---
but if you don't understand something, that's probably okay.

# Changes Process {#_changes_process}

Fedora's Change Process is important to coordinate the development of
the next Fedora release. We need to know about disrupting changes coming
to the next release to set the scope of release, but it also helps as
marketing tool even for leaf changes. For more details on Change
Process, see the [Changes
Policy](program_management::changes_policy.xml).

## Responsibilities {#_responsibilities}

The Program Manager's key responsibility is to maintain the Changes
Process --- [announcements](pgm_guide/sop/changes-announce.xml),
[submission](pgm_guide/sop/changes-submit.xml),
[processing](pgm_guide/sop/changes-process.xml),
[tracking](pgm_guide/sop/changes-contingency.xml),
[deferring](pgm_guide/sop/changes-defer.xml),
[dropping](pgm_guide/sop/changes-drop.xml). Completed Changes are closed
as part of the [Release Day SOP](pgm_guide/sop/release_day.xml). One of
the main responsibilities is helping Change owners through the
submission process. The Program Manager works on the [Changes
Policy](program_management::changes_policy.xml) with the [Fedora
Engineering Steering Committee](fesco::index.xml) (FESCo), Working
Groups and other Fedora teams and bodies (documentation, marketing,
etc.).

# Release Process {#_release_process}

This section covers program management information related to the
process of getting a release out the door. The document is in
chronological order, referencing various SOPs, with small steps directly
in-line, and notes below.

:::: tip
::: title
:::

You may choose to create a [wiki
page](https://fedoraproject.org/wiki/Releases/31/HouseKeeping) to track
the status of housekeeping tasks, as has been done historically.
::::

## Workflow {#_workflow}

&#42; New release (\~1 year before target date) &#42;&#42; [New release
SOP](pgm_guide/sop/release-new.xml) &#42; Spin keepalive deadline (\~3
weeks before Branch point) &#42;&#42; [Spins keepalive
SOP](pgm_guide/sop/spins-keepalive.xml) &#42; Rawhide rebase warning
(1-3 weeks before Branch point) &#42;&#42; Send the [rebase warning
mail](#_rebase_warning_mail) to
<devel-announce@lists.fedoraproject.org>, replacing instances of
\'TKTK\' appropriately &#42; Branch day &#42;&#42; [Branching
SOP](pgm_guide/sop/branch.xml) &#42;&#42; See [notes on the bug rebase
process](#_bug_rebase_notes) &#42; One week before each Go/No-Go meeting
date &#42;&#42; Schedule and announce the meeting, or cancel it if the
decision is clearly No-Go: [Go/No-Go Meeting
SOP](pgm_guide/sop/go-nogo.xml) &#42; Go/No-Go meeting dates &#42;&#42;
Run the meeting, following the [Go/No-Go Meeting
SOP](pgm_guide/sop/go-nogo.xml). See [Go/No-Go Meeting
notes](#gonogo_notes). Follow up with the
[Go](pgm_guide/sop/release-go.xml) or
[No-Go](pgm_guide/sop/release-no_go.xml) SOP. &#42; Release day
&#42;&#42; [Release day SOP](pgm_guide/sop/release_day.xml) &#42; 2-14
days after release day &#42;&#42; Follow [EOL warning
SOP](pgm_guide/sop/eol-warning.xml) for the N-2 release &#42; Four weeks
after release day &#42;&#42; Follow [EOL day
SOP](pgm_guide/sop/eol-day.xml) for the N-2 release

## Rebase warning mail {#_rebase_warning_mail}

This is the email that should be sent out 1-3 weeks before the Branch
point. The actual rebase is covered in the [Branching
SOP](pgm_guide/sop/branch.xml). &#8230;. Greetings,

This e-mail is intended to inform you about the upcoming Bugzilla
changes happening on TKTK (Rawhide bug rebase) and what you need to do,
if anything.

We will be automatically changing the version for most rawhide bugs to
Fedora TKTK. This will result in regular bugs reported against rawhide
during the Fedora TKTK development cycle being changed to version
\'TKTK\' instead of their current assignment, 'rawhide'. This is to
align with the branching of Fedora TKTK from rawhide and to more
accurately tell where in the lineage of releases the bug was last
reported.

Note that this procedure does not apply to bugs that are open for the
'Package Review' or \'kernel\' components or bugs that have the
\'\'FutureFeature\'\' or \'\'Tracking\'\' keywords set. These will stay
open as rawhide bugs indefinitely.

If you do not want your bugs changed to version 'TKTK', add the
\'\'FutureFeature\'\' keyword. If you need help changing a large amount
of bugs manually, we'd be glad to help.

The process was re-approved by FESCo
<https://pagure.io/fesco/issue/1096> . &#8230;.

## Bug rebase notes {#_bug_rebase_notes}

Bugs that meet all of the following conditions are branched from Rawhide
to the newly-created version:

&#42; product == \'Fedora\' or \'Fedora Container Images\' &#42; version
== rawhide &#42; component != \'Package Review\' &#42; component !=
\'Container Review\' &#42; component != \'kernel\' &#42; component !=
\'Changes Tracking\' &#42; keyword \'\'FutureFeature\'\' is
\'\'\'not\'\'\' present &#42; keyword \'\'Tracking\'\' is
\'\'\'not\'\'\' present &#42; the string \'\'RFE\'\' is \'\'\'not\'\'\'
present in the summary &#42; status != CLOSED

According to jforbes, the reason we exclude kernel bugs is two-fold: 1.
A number of reported kernel bugs are longer-term issues that need to be
solved over time, or bugs which upstream has to eventually get to. It
has become the place to file these bugs, even if not against the rawhide
kernel in specific so that they do not get auto closed in a year. 2.
Rawhide kernels are most typically built as debug kernels only, and many
bugs filed against them are not reproducible on branched non-debug
kernels.

## []{#gonogo_notes}Go/No-Go Meeting notes {#_gono_go_meeting_notes}

The [meeting
script](https://pagure.io/fedora-pgm/pgm_communication/blob/main/f/go_nogo.txt)
in the [Go/No-Go SOP](pgm_guide/sop/go-nogo.xml) provides a general
framework for running the Go/No-Go meeting. The general flow is to
verify that a compose is available, review blocker bugs, check that the
test matrices are completed, and that CoreOS and IoT are ready.

The compose section is generally very quick. Release Engineering or QA
will confirm that a candidate compose exists. If there is no candidate
compose, skip straight to a \'no-go\' decision.

If there are proposed or accepted blocker bugs, the meeting becomes a
blocker review meeting to evaluate them. This portion of the meeting can
be led by a member of the QA team or by the Program Manager. It is not
uncommon to defer some bugs until later in the meeting so that
last-minute testing can be performed.

In the test matrices section, QA will review the results of tests. Some
optional tests may not be complete.

Finally, the Program Manager polls each of the constituent teams. If
they all vote \'go\', then the release is \'go\' and will be released on
the coming Tuesday. The Program Manager's work is done (at least as far
as this goes). If the release is \'no-go\', then a follow-up meeting
must happen.

# Prioritized Bugs {#_prioritized_bugs_2}

The [Prioritized Bugs](../../prioritized_bugs) process is designed to
get attention for issues that are not blockers, but are still
high-impact or high-visibility. The criteria are intentionally
subjective and we will drop bugs from the list if we can't convince
developers to make progress.

On Fridays (or whatever day you prefer), it's good to review the
accepted Prioritized Bugs and make sure they're not getting stale. See
the [process
documentation](../../prioritized_bugs&#35;_process_for_accepted_bugs)
for guidance on how to give nudges.

# Elections {#_elections}

The Fedora Program Manager is responsible for conducting elections for
various bodies within Fedora. After each release, the Fedora Engineering
Steering Committee run an election. The Fedora Council, Mindshare
Committee and EPEL Steering Committee run an election on a once per year
basis. Other teams may request elections at any time if they have a
need.

The Fedora Community Architect (FCA) is the backup elections wrangler.
The FCA &amp; FPgM cannot be candidates for elected positions.

:::: note
::: title
:::

FESCo has a [separate election policy](fesco::FESCo_election_policy.xml)
that requires more candidates than open seats.
::::

Fedora's election process is important to our community governance
model. Therefore, transparency and trust are vital. This is one area
where strictly adhering to the published process is important. Avoid
giving the appearance of special treatment to candidates.

:::: note
::: title
:::

At one time, we were hoping to have the Fedora Podcast conduct
interviews with candidates as well, but that has fizzled.
::::

:::: note
::: title
:::

A long time ago, we conducted IRC town halls with candidates. We stopped
doing that.
::::

# Schedule {#_schedule_5}

Developing and maintaining the [Fedora Project's
schedule](https://fedorapeople.org/groups/schedule/) may be the most
important part of the Fedora Program Manager's job. The good news is
that it is not very hard. [FESCo
approved](https://pagure.io/fesco/issue/2211&#35;comment-590831) reusing
the same general structure for every release, with target release dates
of the third Tuesday in April and October. Now it will only change if
there are major requirements that necessitate a deviation. This helps
with planning for Fedora as well as for our downstreams (read: RHEL).

Of course, you can---and should---make small changes to the schedule as
processes evolve. This may mean adding, removing, or moving some tasks.
Or it might mean changing which teams are reflecting in the [web
view](https://fedorapeople.org/groups/schedule/) of the schedule.

:::: note
::: title
:::

FESCo [authorized](https://pagure.io/fesco/issue/2329) Release
Engineering to start the mass rebuild up to five days after the
scheduled start date. This allows RelEng to accommodate travel for Flock
and DevConf.CZ, which often fall near the start of the mass rebuild.
::::

## Smartsheet {#_smartsheet}

The schedule lives in [Smartsheet](https://app.smartsheet.com) (only
available to Red Hat employees). Every so often, go in and copy a few
releases forward.

In your new schedule:

&#42; Update the "Fedora XX Release" &#42; Find and replace N-1 with N
(have to do it manually so as to not get dates) &#42; Find and replace
N-2 with N-1 (same)

Tasks are assigned to teams with flags. The &#96;pp&#96; flag has no
meaning for the community, but is used to keep in sync with other Red
Hat products. Some fields (e.g. requirements gathering) are not
relevant, but required for [Product Pages](#_product_pages). Product
Pages only cares about the &#42;key&#42; flag.

:::: tip
::: title
:::

If you want links in the schedule, add the URL in the "links" column for
that task (the &#96;Link:&#96; keyword is optional now). It will be
shown in the rendered schedule.
::::

The Early Final target date is the "master milestone" against which
everything else is anchored.

:::: tip
::: title
:::

Before publishing the schedule, check to be sure that it doesn't
conflict too horribly with major holidays, etc.
::::

To publish the schedule, &#42;Export to Microsoft Project (XML)&#42; and
save the file to the &#96;f-N&#96; directory in the [schedule
repository](https://pagure.io/fedora-pgm/schedule) as
&#96;Fedora.Schedule.xml&#96;.

:::: tip
::: title
:::

If &#42;Export to Microsoft Project (XML)&#42; is not an option, you
might need to switch to Gantt view. Smartsheet isn't very smart in that
regard.
::::

When schedules slip:

1.  Add a new target date (e.g. Beta target date &#35;2)

2.  Update the "Current X target date" when you know it's really going
    to happen

## Git repo {#_git_repo}

The files used to publish the scripts live in a [git
repository](https://pagure.io/fedora-pgm/schedule).

To create a schedule for a new version (f-30 in this example):

1.  &#96;mkdir f-30&#96;

2.  &#96;cp ../f-29/Makefile . &amp;&amp; vi Makefile&#96; &#35; copy
    forward from previous and change the version

3.  Export the XML file (see previous section)

4.  &#96;git add Fedora.Schedule.xml Makefile&#96;

5.  &#96;git commit -m 'Your commit message here'&#96;

6.  to see the changes locally: &#96;make&#96; &#35; &#96;make
    clean&#96; cleans up your mess

7.  &#96;make publish&#96; &#35; publish html and friends to
    fedorapeople

:::: note
::: title
:::

The rsync invocations in the Makefile assume you have your user name set
in &#96;\~/.ssh/config&#96; if your local name does not match your
Fedora account.
::::

To update the index page of the website, or the CSS file used to style
it, start from the schedule repo above:

1.  &#96;cd html&#96;

2.  Edit the appropriate file

3.  &#96;make publish&#96; to rsync to fedorapeople

4.  Commit and push your edits

## Product Pages {#_product_pages}

[Product Pages](https://pp.engineering.redhat.com/) is the central
resource for Red Hat internal product schedule and status information.

To register a new version in product pages:

1.  Go to admin page (&#42;Platforms&#42; &gt; &#42;Fedora Project&#42;
    &gt; &#42;Overview&#42;)

2.  Click &#42;Add new release&#42; button

3.  Short name: 30

4.  Select all the sections to copy

5.  Click &#42;OK&#42;

6.  Click &#42;Schedules&#42; tab

7.  Click &#42;Add schedules&#42; button

8.  Handle: &lt;get the Smartsheet file URL or ID&gt;

9.  Switch draft to approved

10. Set phase to planning

:::: tip
::: title
:::

Prior to May 2021, we used a Red Hat CVS server for the schedule files.
They now are pulled directly into Product Pages from Smartsheet.
::::

Key fields:

&#42; &#42;Platforms&#42;: if you want to update it, add the list of
platforms Fedora supports (used by RH releng, but Fedora releng doesn't
use it. so it's entirely optional) &#42; &#42;Documents&#42;: just make
a link to the wiki &#42; &#42;People&#42;: update this as appropriate
&#42; &#42;Communication&#42;: list of important IRC channels and
mailing lists

### Status updates {#_status_updates}

Update the phases when there's a significant change (e.g. Beta release
-&gt; change to testing).

Update the status on a weekly basis (due Thursday afternoon US East
coast time). Green means no risks and no slippage; you don't need to say
much. Yellow means there are risks, but we have it under control.
Describe what went wrong and how we're going to address it. Red means
\'oh noes!\'; explain a lot more.

## Historical notes {#_historical_notes}

This section is a collection of loosely-organized facts that give some
of the history of schedule wrangling.

&#42; Schedules used to be done with TaskJuggler (version 2,
specifically). If you ever need to do anything with the old schedule
files, you will need to get a copy of that. (By the time you read this,
it will likely be retired from Fedora.) &#42; We used to copy key
milestones to a wiki page. Ben Cotton stopped doing that because it was
annoying and he's error-prone.

# Operations Architect Communication {#_operations_architect_communication}

Communicating is the most important part of the Fedora Operations
Architect's job. There are few *required* communications for the Fedora
ops architect, but your success will depend in part on communicating
information out to the community.

This section describes what Ben Cotton did. Feel free to modify and
adapt it to fit your style.

Unless otherwise indicated, the communications in this section are
stored in the
[pgm_communication](https://pagure.io/fedora-pgm/pgm_communication/)
repository.

## Friday's Fedora Facts {#_fridays_fedora_facts}

This is a [weekly
report](https://communityblog.fedoraproject.org/tag/fridays-fedora-facts/)
in the Fedora Community Blog. It is published on Friday afternoons and
contains a summary of the previous week's activities and upcoming
events. The readership numbers, as reported by WordPress, are not
overwhelming, but everyone I talk to about it expresses appreciation.
When you're doing your job right as a program manager, you don't get
much feedback.

I keep the content up-to-date during the week by editing the
&#96;fridays_fedora_facts.md&#96; file in the
&#96;pgm_communication&#96; repository. You can use &#96;pandoc&#96; to
convert this to HTML to paste directly into the WordPress console.

The sections to include are:

&#42; &#42;Announcements&#42; --- Important announcements, including
package retirements, conference calls for papers (see below), policy
proposals and changes, etc. For items with a defined deadline, I
generally leave the announcement in there until the deadline has passed.
For items without a defined deadline, I leave them for 1--4 weeks,
depending on the relevance and impact. &#42; &#42;Help wanted&#42; ---
Requests for help from teams within Fedora. These generally come from
observing the meeting minutes and mailing lists of teams within Fedora.
I generally leave them for a few weeks. &#42; &#42;Upcoming meetings
&amp; test days&#42; --- Project-level meetings that will occur within
the next week. I generally include Council meetings, blocker review
meetings, prioritized bugs meetings, and the [FPgM office
hours](#_fpgm_office_hours) as regular entries. I also include the
[Go/No-Go](release_process.adoc&#35;_gono_go_meeting) meetings when
appropriate. If the QA team has organized test days, I will include
those as well. &#42; &#42;Fedora N&#42; --- Information about the
current in-progress Fedora release (you may have N+1 as well).
&#42;&#42; &#42;Schedule&#42; --- Upcoming schedule milestones,
generally within the next month &#42;&#42; &#42;Changes&#42; --- Changes
announced, submitted to FESCo, and approved/rejected by FESCo. These are
normally removed the week following approval or rejection. I link to the
wiki page and --- while the proposal is pending with FESCo --- a link to
the FESCo ticket. If changes are withdrawn after being approved, I will
keep the withdrawal in the report a length of time that seems reasonable
to me at the time. &#42;&#42; &#42;Blocker bugs&#42; --- A table
including the bug ID (with a link to Bugzilla), blocker status (proposed
or accepted), component, and bug status. I include this once I begin
producing the [blocker bug report](#_blocker_report).

### CfP sources {#_cfp_sources}

There's no one, unified place to get relevant CfPs. Pay attention to
social media (particularly upstream accounts), etc. You can also use:

&#42; <https://confs.tech/cfp> &#42;
<http://www.wikicfp.com/cfp/call?conference=open%20source> &#42;
<https://www.cfpland.com/>

## FPgM office hours {#_fpgm_office_hours}

This is no longer active, but if a need for it resurfaces, content can
be found in the file &#96;office_hours.md&#96; in the
&#96;pgm_communication&#96; repository.

## Blocker report {#_blocker_report}

The [blocker bug
process](https://fedoraproject.org/wiki/QA:SOP_blocker_bug_process)
belongs to the QA team, but Ben Cotton adopted the weekly blocker review
email to give Adam Williamson more time to test and diagnose bugs. The
content of the email is in the &#96;blocker_email.txt&#96; file in the
&#96;pgm_communication&#96; repository.

Begin sending the emails on the first Friday of the Beta freeze and
continue until the final release is declared \'Go\'. I generally ignore
the final blockers until Beta is released.

To produce the report:

1.  Go through each of the bugs in the [Blocker
    Bugs](https://qa.fedoraproject.org/blockerbugs) list

2.  Review the content of the bug and summarize the current state,
    including upstream bug URLs, package updates that require testing,
    etc.

3.  Note the action required for each bug. This may be QA verifying a
    fix, upstream fixing the bug, the package maintainer producing a new
    release, etc. If the bug has the *needinfo* flag set, include that.

4.  Add the bug owner to the bcc list if they have an action item. Also
    include anyone marked as needinfo.

5.  Include an action summary at the top.

6.  Send the email to the devel and test mailing lists, and bcc the
    people you identified above.

# Council meetings and processes {#_council_meetings_and_processes}

The Fedora Program Manager sits on the Fedora Council as an auxiliary
member. The FPgM generally leads the regular Council meetings and keeps
an eye on the [ticket
queue](https://pagure.io/Fedora-Council/tickets/issues). There is not
much to say here, just help bring some structure to the Council and make
sure tickets are appropriately categorized and don't languish.

# Inactive provenpackagers {#_inactive_provenpackagers}

The &#96;provenpackagers&#96; group grants members write privileges
across all Fedora packages. Thus, we want to make sure the privilege
doesn't linger on inactive accounts. In early 2021, [FESCo
adopted](https://pagure.io/fesco/issue/2549) a policy for [maintaining
provenpackager
status](fesco::Provenpackager_policy.adoc&#35;_maintaining_provenpackager_status).

The Fedora Program Manager is charged with performing an audit of these
accounts. This should take place at about the branch point of each
development cycle.

The
[inactive_provenpackagers.py](https://pagure.io/fedora-pgm/pgm_scripts/blob/main/f/provenpackager/inactive_provenpackagers.py)
script will check for provenpackagers that have not submitted a Koji
build in the last six months. It produces a list of accounts that fail
this test, as well as accounts that do not exist in Koji.

After running this script, send the output to the named accounts as well
as devel-announce. You will get some replies from people who would like
to retain the status. By policy, all they have to do is ask to keep it
and they may.

After two weeks, submit an infrastructure ticket to remove
provenpackager status from anyone who did not request keeping the group
membership. You do not need to submit it to FESCo for a vote.

:::: tip
::: title
:::

Some packagers may choose to submit a build without telling you. Before
you submit the removal request, you probably want to re-run the
inactive_provenpackagers script to see if anyone dropped off the list.
::::

# Bugzilla administration {#_bugzilla_administration}

This page contains information about administering the Fedora aspects of
Red Hat Bugzilla. Information on [branching](pgm_guide/sop/branch.xml),
[EOL warning](pgm_guide/sop/eol-warning.xml), and [EOL
closure](pgm_guide/sop/eol-day.xml) are in this guide's SOPs.

## Groups {#_groups}

The following groups are used for Fedora:

+-----------------------------------+-----------------------------------+
| Name                              | Purpose                           |
+===================================+===================================+
| fedora_contrib                    | Grants additional permissions.    |
|                                   | Populated automatically from      |
|                                   | several groups in Fedora          |
|                                   | Accounts.                         |
+-----------------------------------+-----------------------------------+
| fedora_pm                         | Can edit components in various    |
|                                   | products in the Fedora            |
|                                   | classification                    |
+-----------------------------------+-----------------------------------+
| fedora_pm_approves                | Users who can approve membership  |
|                                   | of fedora_pm                      |
+-----------------------------------+-----------------------------------+
| fedora_rules_admin                | Can administer rules engine for   |
|                                   | Fedora                            |
+-----------------------------------+-----------------------------------+

:::: note
::: title
:::

Membership in the *fedora_pm* group only grants permissions to edit
components the like. *fedora_contrib* is what lets people do the usual
stuff.
::::

# Getting started {#_getting_started}

Congratulations! You're the new Fedora Program Manager. Whether you're
new to Red Hat, to the Fedora Community, or both, there's a lot to
learn. Here's a list of things you'll need to get started:

## Fedora Account System (FAS) {#_fedora_account_system_fas}

You can't do much of anything in Fedora without this. Visit the [account
signup page](https://accounts.fedoraproject.org) to create an account.
If you already have one from your previous work with Fedora, then you're
all set.

### Groups {#_groups_2}

&#42;
&#42;[elections](https://accounts.fedoraproject.org/group/elections/)&#42;
--- Used to manage the [elections](elections.xml). &#42;
&#42;[council](https://accounts.fedoraproject.org/group/council/)&#42;
--- Grants access to Council-related things &#42;
&#42;[program-management](https://accounts.fedoraproject.org/group/program-management/)&#42;
--- Grants access to the [schedule](pgm_guide/schedule.xml) project on
fedorapeople.org

## Mailing lists {#_mailing_lists_3}

### Community mailing lists {#_community_mailing_lists}

Some you can self-subscribe to, others you will need to be added to. You
can join as many lists as you'd like, but at a minimum you should have
these.

&#42;
&#42;[council-private](https://lists.fedoraproject.org/archives/list/council-private@lists.fedoraproject.org/)&#42;
--- Private Council discussions &#42;
&#42;[devel](https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/)&#42;
--- development discussions &#42;
&#42;[devel-announce](https://lists.fedoraproject.org/archives/list/devel-announce@lists.fedoraproject.org/)&#42;
--- announcements for development &#42;
&#42;[test](https://lists.fedoraproject.org/archives/list/logistics@lists.fedoraproject.org/)&#42;
--- Release coordination logistics &#42;
&#42;[meetingminutes](https://lists.fedoraproject.org/archives/list/meetingminutes@lists.fedoraproject.org/)&#42;
--- Minutes from all logged IRC meetings &#42;
&#42;[rel-eng](https://lists.fedoraproject.org/archives/list/rel-eng@lists.fedoraproject.org/)&#42;
--- Release engineering &#42;
&#42;[test](https://lists.fedoraproject.org/archives/list/test@lists.fedoraproject.org/)&#42;
--- QA team &#42;
&#42;[test-announce](https://lists.fedoraproject.org/archives/list/test-announce@lists.fedoraproject.org/)&#42;
--- QA team announcements &#42;
&#42;[triage](https://lists.fedoraproject.org/archives/list/triage@lists.fedoraproject.org/)&#42;
--- Discussion for [prioritized bugs](prioritized_bugs.xml)

### Red Hat mailing lists {#_red_hat_mailing_lists}

&#42; &#42;[Fedora
infrastructure](https://listman.redhat.com/mailman/listinfo/fedora-infrastructure-list/)&#42;
&#42; &#42;[Fedora-Red
Hat](https://listman.redhat.com/mailman/listinfo/fedora-list/)&#42;

## Pagure groups {#_pagure_groups}

&#42; &#42;[Fedora-Council](https://pagure.io/group/Fedora-Council)&#42;
&#42; &#42;[fedora-pgm](https://pagure.io/group/fedora-pgm)&#42;

## Other tools {#_other_tools}

&#42; &#42;[Smartsheet](https://smartsheet.com)&#42; --- This is where
the [scheduling](pgm_guide/schedule.xml) magic happens &#42;
&#42;[Product Pages](https://pp.engineering.redhat.com/pp/) admin
access&#42; --- This is the Red Hat internal tracking tool for products.
To request access, fill out the [PLM+ACI Google
Form](https://docs.google.com/forms/d/e/1FAIpQLSdX2lc4n3AT7rHyth_lNpZAJ-7JMsCHiyfDnQJC92jS2eYQOA/viewform)
(Red Hat only) &#42; &#42;[Bugzilla](https://bugzilla.redhat.com)&#42;
--- You will also need to request membership in the
&#42;editcomponents&#42; group so that you can modify the Fedora
component as needed.

More Red Hat internal setup information is in the [Engineering Program
Management
Guide](https://docs.google.com/document/d/1giFWzeOp-_WVH-CZgYKFYlOF9Zre5aDGymOwmVhdm7U/edit).

&#42;&#42; SOPs &#42;&#42;&#42; Release steps = New release SOP

This document outlines procedures for new releases. Note that schedules
are often generated up to three years in advance, so they are covered
separately.

## Timing/trigger {#_timingtrigger}

On or about a year before the target release date.

If a Change proposal is submitted for the release, that's a good time to
start this process.

## Procedures {#_procedures}

1.  Create a tracking bug in Bugzilla

    a.  [Create a bug in the \'Changes Tracking\'
        component](https://bugzilla.redhat.com/enter_bug.cgi?component=Changes%20Tracking&amp;product=Fedora&amp;version=rawhide)

    b.  Set the summary to \'Fedora Linux NN Change proposal tracker\'

    c.  Set the description to \'This is a tracking bug for FNN
        Changes.\'

    d.  Click \'Submit Bug\' so you can add additional information

    e.  Add \'Tracking\' to the Keywords field

    f.  Click \'Show advanced fields\' if they're not already visible

    g.  Click \'Edit\' on the Alias and set it to \'FNNChanges\'

    h.  Click \'Save Changes\'

2.  Add docs to the [Releases](releases::index.xml) module

    a.  Make an &#96;fNN&#96; directory

    b.  Copy the contents from the previous release to this directory

    c.  Update the &#96;:release-version:&#96; macro in each adoc file

    d.  Add listings to &#96;nav.adoc&#96; under the \'Upcoming
        Releases\' header. Copy the previous release's entries and
        update version numbers as appropriate.

3.  Update the schedule

    a.  Create a schedule for the new release, following the
        ../schedule\[Schedule SOP\]

    b.  Add the new release to the index.html page on the [web
        view](https://fedorapeople.org/groups/schedule/) of the
        schedule.

4.  Update the wiki Change pages for the new release

    a.  Create the &#96;Releases/NN/ChangeSet&#96; page on the wiki. Use
        the template below for guidance

:::: formalpara
::: title
Wiki template for ChangeSet page
:::

&#8230;. {{autolang\|base=yes}}
::::

{{admon/warning\|DO NOT EDIT this page manually as it's generated
automatically and all changes will be overwritten! If you want to change
anything, change the original Changes page and it will be picked up in
the next refresh. If not, ping \[\[User:bcotton\|bcotton\]\].}}

*TOC*

{{Anchor\|accepted_system_wide}} == Fedora Linux NN Accepted System-Wide
Changes ==

{{Anchor\|accepted_self_contained}} == Fedora Linux NN Accepted
Self-Contained Changes == &#8230;. .. Add the new release to the
[Changes wiki page](https://fedoraproject.org/wiki/Changes)

# Branching SOP {#_branching_sop}

This document outlines the procedures for activities that occur on
\'branch day\': when the next Fedora Linux release branches from
Rawhide.

Many of the branching activities are handled by Release Engineering, but
several are in the scope of the Fedora Program Manager.

## Timing/trigger {#_timingtrigger_2}

This process occurs once per release. The branch day happens between the
mass rebuild and the Beta freeze.

## Procedures {#_procedures_2}

All of the following procedures should be run in the order listed.

### Update Bugzilla product description {#_update_bugzilla_product_description}

1.  Adjust wording of the [Fedora
    product](https://bugzilla.redhat.com/editproducts.cgi?action=edit&amp;product=Fedora)
    in Bugzilla to reflect the branch.

&#8230;. Bugs related to the components of the Fedora distribution. If
you are reporting a bug against a stable release or a branched
pre-release version, please select that version number. The currently
maintained released versions are: Fedora Linux N-1, Fedora Linux N. The
branched pre-released version is Fedora Linux N+1. If you have a bug to
report against the daily development tree (rawhide), please choose
\'rawhide\' as the version.

For more information about filing a bug against Fedora packages, see
<https://docs.fedoraproject.org/en-US/quick-docs/howto-file-a-bug/>
&#8230;.

### Create N+1 version {#_create_n1_version}

1.  Create N+1 in Bugzilla's
    [Fedora](https://bugzilla.redhat.com/editversions.cgi?product=Fedora)
    product versions.

2.  Create N+1 in Bugzilla's [Fedora Container
    Images](https://bugzilla.redhat.com/editversions.cgi?product=Fedora%20Container%20Images)
    product versions.

### Branch Rawhide bugs {#_branch_rawhide_bugs}

:::: warning
::: title
:::

If you run this after Branch Day, you will need to add constraint on the
bug open date. See below.
::::

1.  Change the F&lt;N+1&gt;Changes bug and bugs that block it to the
    branched version.

2.  Run the [&#96;fedora_bz.py&#96;
    script](https://pagure.io/fedora-pgm/pgm_scripts/blob/main/f/closebugs/fedora_bz.py)
    to change the version on rawhide bugs to the new release. For
    example: &#96;./fedora_bz.py branch 40&#96; (if the new release is
    40).

3.  If you are running the script late, use the &#96;\--date&#96; option
    to specify the branch date: &#96;./fedora_bz.py branch
    \--date=2024-02-06 40&#96;. This will make the script only change
    the version on bugs filed before the branch date.

:::: warning
::: title
:::

This script will take a while to run. Execute it from a machine with
stable power and networking.
::::

[This Bugzilla
query](https://bugzilla.redhat.com/buglist.cgi?classification=Fedora&amp;f1=component&amp;f3=component&amp;f4=bug_status&amp;f5=component&amp;f6=component&amp;keywords=FutureFeature%2C%20Tracking%2C%20&amp;keywords_type=nowords&amp;list_id=10832664&amp;o1=notequals&amp;o3=notequals&amp;o4=notequals&amp;o5=notequals&amp;o6=notequals&amp;product=Fedora&amp;product=Fedora%20Container%20Images&amp;query_format=advanced&amp;short_desc=RFE&amp;short_desc_type=notregexp&amp;v1=Package%20Review&amp;v3=kernel&amp;v4=CLOSED&amp;v5=Changes%20Tracking&amp;v6=Container%20Review&amp;version=rawhide)
is similar to the one the script uses to select bugs that meet the
[criteria](pgm_guide/release_process.adoc&#35;_branch_day). You can use
it to check the list before running the script if you like.

### Update Product Pages {#_update_product_pages}

1.  Set F&lt;N&gt; to the \'Development/Testing\' phase.

2.  Set F&lt;N+1&gt; to the \'Development\' phase.

# Go/No-Go Meeting SOP {#_gono_go_meeting_sop}

This document outlines procedures for scheduling and running the
[Go/No-Go meeting](pgm_guide/release_process.adoc&#35;_gono_go_meeting).

## Timing/trigger {#_timingtrigger_3}

The first go/no-go meeting occurs on the Thursday before the early
target date for a release. Meetings recur weekly until the release is
GO.

## Procedures {#_procedures_3}

### Schedule meeting {#_schedule_meeting}

1.  Schedule the meeting in Fedocal's [Fedora
    release](https://calendar.fedoraproject.org/Fedora%20release/)
    calendar. The Go/No-Go meeting is traditionally held on the Thursday
    prior to the release date from 17:00--19:00 UTC.

2.  Select an available meeting channel. It is best to set the meeting
    to recur weekly for 3 weeks in case of multiple slips.

3.  Send an email 5--7 calendar days before the meeting to the
    devel-announce, logistics, and test-announce mailing lists.

### Run the meeting {#_run_the_meeting}

The [script for the Go/No-Go
meeting](https://pagure.io/fedora-pgm/pgm_communication/blob/main/f/go_nogo.txt)
is in the [pgm_communication
repo](https://pagure.io/fedora-pgm/pgm_communication/).

Follow this script and then follow the
[Go](pgm_guide/sop/release-go.xml) or
[No-Go](pgm_guide/sop/release-no_go.xml) SOP as appropriate.

# Release Delay SOP {#_release_delay_sop}

The document outlines the procedure for delaying the release. Refer to
the [schedule contingency
planning](releases::lifecycle.adoc&#35;_schedule_contingency_planning)
docs for when to delay future milestones.

1.  In [Smartsheet](pgm_guide/schedule.adoc&#35;_smartsheet), add a new
    milestone (if needed) and update the Current (Beta\|Final) Target
    date milestone to have the new target date as a predecessor.

2.  Save the updated schedule to the [git
    repository](pgm_guide/schedule.adoc&#35;_git_repo) and publish to
    the web.

3.  Update [Product Pages](pgm_guide/schedule.adoc&#35;_product_pages).
    If the new target date is beyond target date &#35;1 or you have
    reason to believe the release will slip further, set the status to
    yellow. If the new target date is beyond target date &#35;2 or you
    have reason to believe the release will slip further, set the status
    to red.

4.  Send an announcement email similar to the below to
    <logistics@lists.fedoraproject.org>,
    <devel-announce@lists.fedoraproject.org>,
    <test-announce@lists.fedoraproject.org>, and
    <rel-eng@lists.fedoraproject.org>.

5.  Update the dates in the
    [report](pgm_guide/pgm_communication.adoc&#35;_fpgm_report) and
    [office
    hours](pgm_guide/pgm_communication.adoc&#35;_fpgm_office_hours)
    files.

## Delay announcement emails {#_delay_announcement_emails}

:::: tip
::: title
:::

These are suggestions. You can and should customize them to meet
specific releases and your own \'voice\'.
::::

### Delayed due to no RC {#_delayed_due_to_no_rc}

    Due to outstanding blocker bugs[1], we do not have an F\&lt;VERSION\&gt; \&lt;MILESTONE\&gt; RC. As
    a result, F\&lt;VERSION\&gt; \&lt;MILESTONE\&gt; is NO-GO by default and tomorrow's Go/No-Go meeting is
    cancelled.

    The next Fedora Linux \&lt;VERSION\&gt; \&lt;MILESTONE\&gt; Go/No-Go meeting[2] will be held at 1700
    UTC on Thursday \&lt;DATE\&gt; in \&lt;LOCATION\&gt;. We will aim for the
    'target date \&#35;\&lt;TARGET\&gt;' milestone of \&lt;DATE\&gt;. The release schedule[3] has
    been updated accordingly.

    [1] https://qa.fedoraproject.org/blockerbugs/milestone/\&lt;VERSION\&gt;/\&lt;MILESTONE\&gt;/buglist
    [2] https://calendar.fedoraproject.org/meeting/\&lt;MEETING ID\&gt;/
    [3] https://fedorapeople.org/groups/schedule/f-\&lt;VERSION\&gt;/f-\&lt;VERSION\&gt;-key-tasks.html

### Delayed due to No-Go decision {#_delayed_due_to_no_go_decision}

    Due to outstanding blocker bugs[1], F\&lt;VERSION\&gt; \&lt;MILESTONE\&gt; RC\&lt;CANDIDATE\&gt; was declared NO-GO in
    today's Go/No-GO meeting.

    The next Fedora Linux \&lt;VERSION\&gt; \&lt;MILESTONE\&gt; Go/No-Go meeting[3] will be held at 1700
    UTC on Thursday \&lt;DATE\&gt; in \&lt;LOCATION\&gt;. We will aim for the
    'target date \&#35;\&lt;TARGET\&gt;' milestone of \&lt;DATE\&gt;. The release schedule[4] has
    been updated accordingly.

    [1] https://qa.fedoraproject.org/blockerbugs/milestone/\&lt;VERSION\&gt;/\&lt;MILESTONE\&gt;/buglist
    [2] https://meetbot.fedoraproject.org/\&lt;MEETING MINUTES URL\&gt;
    [2] https://calendar.fedoraproject.org/meeting/\&lt;MEETING ID\&gt;/
    [3] https://fedorapeople.org/groups/schedule/f-\&lt;VERSION\&gt;/f-\&lt;VERSION\&gt;-key-tasks.html

# Release Go SOP {#_release_go_sop}

This document outlines the procedure for when a release is declared
\'go\'.

1.  Update the [Product
    Pages](pgm_guide/schedule.adoc&#35;_product_pages) status

2.  For Final releases only, update [Product
    Pages](pgm_guide/schedule.adoc&#35;_product_pages) to set the phase
    to \'Launch\' (Set this to \'Maintenance\' on release day)

3.  Send an announcement email similar to the below to
    <logistics@lists.fedoraproject.org>,
    <devel-announce@lists.fedoraproject.org>,
    <test-announce@lists.fedoraproject.org>,
    <rel-eng@lists.fedoraproject.org>.

4.  Update the dates in the
    [report](pgm_guide/pgm_communication.adoc&#35;_fpgm_report) and
    [office
    hours](pgm_guide/pgm_communication.adoc&#35;_fpgm_office_hours)
    files.

5.  Notify the Websites &amp; Apps team to ensure they're ready for
    websites changes.

## Release announcement email {#_release_announcement_email}

    The Fedora Linux \&lt;VERSION\&gt; \&lt;MILESTONE\&gt; RC\&lt;CANDIDATE\&gt; compose is GO and will be shipped live on Tuesday,\&lt;DATE\&gt;.

    For more information please check the Go/No-Go meeting minutes[1] or log[2].

    [1] https://meetbot.fedoraproject.org/\&lt;MEETING MINUTES URL\&gt;
    [2] https://meetbot.fedoraproject.org/\&lt;MEETING LOG URL\&gt;

:::: tip
::: title
:::

For the Beta release announcement, include the date that the Final
freeze starts.
::::

# Release No-Go SOP {#_release_no_go_sop}

## Trigger/timing {#_triggertiming}

This document outlines the procedure for when a release is declared
\'no-go\'.

## Procedure {#_procedure}

1.  Follow the [Release delay SOP](pgm_guide/sop/release-delay.xml).

2.  Cancel the go/no-go meeting if the \'no-go\' determination is made
    preemptively.

For the Final milestone:

1.  Submit a pull request to the &lt;VERSION-2&gt; release's
    [fedora-release
    package](https://src.fedoraproject.org/rpms/fedora-release) to
    update the eol_date variable in the &#96;fedora-release.spec&#96;
    file. You may need to request a new package build from the Release
    Engineering team.

2.  Update the &lt;VERSION-2&gt; release schedule's EOL date entry.

3.  File a [releng issue](https://pagure.io/releng/new_issue) requesting
    update of the &lt;VERSION-2&gt; release's EOL date in Bodhi.

# Release Day SOP {#_release_day_sop}

This document outlines the procedure for release day activities. Unless
otherwise specified, it applies to both Beta and Final releases.

## Release Day chat {#_release_day_chat}

Ensure the following people are in the [Release Day chat
channel](https://matrix.to/&#35;/&#35;release-day:fedora.im):

&#42; You, as the Program Manager &#42; A representative from the
Infrastructure team with access to force a re-sync of web proxies &#42;
A representative from the Websites team &#42; A representative from the
Magazine team &#42; A representative from the Docs team &#42; The Fedora
Project Leader

This channel is used to coordinate the last-minute checks before
publishing the release announcements:

&#42; Websites are updated with the new release information: &#42;&#42;
fedoraproject.org &#42;&#42; spins.fedoraproject.org &#42;&#42;
labs.fedoraproject.org &#42; (Final milestone only) Docs are updated
with the new release information: &#42;&#42; Release Notes &#42;&#42;
Quick Docs &#42; Fedora Magazine posts &#42;&#42; Release announcement
&#42;&#42; (Final milestone only) What's new in FXX Workstation.

:::: note
::: title
:::

The \'What's new in FXX Workstation\' needs to go out with the release
announcement because GNOME Software expects the target link to exist.
::::

:::: warning
::: title
:::

The release announcement and \'what's new in workstation\' articles need
to have URLs that match the patterns that GNOME Software expects. Beta
announcement is &#96;announcing-fedora-XX-beta&#96;. Final announcement
is &#96;announcing-fedora-XX&#96;. \'What's new\' is
&#96;whats-new-fedora-XX-workstation&#96;. The Magazine team is
ultimately responsible for this, but it's good to verify.
::::

## Bugzilla {#_bugzilla_3}

This section applies to the Final milestone only.

### Update product description {#_update_product_description}

Adjust wording of the [Fedora
product](https://bugzilla.redhat.com/editproducts.cgi?action=edit&amp;product=Fedora)
in Bugzilla to reflect the new release.

&#8230;. Bugs related to the components of the Fedora Linux
distribution. If you are reporting a bug against a stable release or a
branched pre-release version please select that version number. The
currently maintained released versions are: Fedora Linux N-2, Fedora
Linux N-1, and Fedora Linux N. If you have a bug to report against the
daily development tree (rawhide), please choose \'rawhide\' as the
version.

For more information about filing a bug against Fedora Linux packages,
see <https://docs.fedoraproject.org/en-US/quick-docs/howto-file-a-bug/>
&#8230;.

### Close Changes Tracking bugs {#_close_changes_tracking_bugs}

Close all of the Changes Tracking bugs still open for the version with:

&#42; Status: *CLOSED* &#42; Resolution: *CURRENTRELEASE* &#42; Comment:
Something to the effect of \'F&lt;VERSION&gt; was released today, so I
am closing this tracker. If this Change was not completed, please notify
me ASAP.\'

Then close the FNNTracking bug.

:::: tip
::: title
:::

You can use [this Bugzilla
query](https://bugzilla.redhat.com/buglist.cgi?f1=blocked&amp;list_id=11983255&amp;o1=substring&amp;query_format=advanced&amp;v1=F39Changes)
with the version number changed.
::::

## Wiki {#_wiki}

This section applies to the Final milestone only.

&#42; Edit the ChangeSet page in the wiki to include a link to the
release notes and take the table of contents off the top. &#42; Update
the [Changes wiki page](https://fedoraproject.org/wiki/Changes) to move
the release to the \'Previous Releases\' section.

## Schedule {#_schedule_6}

This section applies to the Final milestone only.

Update the index.html page on the [web
view](https://fedorapeople.org/groups/schedule/) of the schedule to
change the class of the release from \'current\' to \'supported\'.
Publish the changes using the [instructions for the schedule git
repo](pgm_guide/schedule.adoc&#35;_git_repo).

## Docs {#_docs}

This section applies to the Final milestone only.

Update the [Releases page](releases::index.xml) (or really, the
&#96;nav.adoc&#96; sidebar).

&#42; Move the link to the release's index page from Upcoming to
Supported. &#42; Remove the additional pages nested under the release.

## Product Pages {#_product_pages_2}

For the Beta milestone, set the release to &#42;Testing&#42; status.

For the Final milestone, set the release to &#42;Maintenance&#42;
status. Then add a status for version N-2 to indicate that EOL is in
four weeks.

# EOL warning SOP {#_eol_warning_sop}

This document outlines the procedure for doing the end-of-life (EOL)
warning.

## Timing/trigger {#_timingtrigger_4}

This process is triggered by the release of Fedora Linux N+2. The
schedule calls for it to occur two days after the release, but any time
within two weeks of release day is sufficient.

## Process {#_process}

Add a warning comment on open bugs for the release that will soon go EOL
using the [&#96;fedora_bz.py&#96;
script](https://pagure.io/fedora-pgm/pgm_scripts/blob/main/f/closebugs/fedora_bz.py).

For example, to post the warning on Fedora Linux 37 bugs:
&#96;./fedora_bz.py eolwarn 37&#96;

The script will read the EOL date from Bodhi, or you can override it,
e.g. &#96;./fedora_bz.py eolwarn \--date=2023-12-05 37&#96;

:::: warning
::: title
:::

This script will take a while to run. Execute it from a machine with
stable power and networking. If the script does die, you can re-run it
like &#96;./fedora_bz.py \--start-bug 123456 eolwarn 37&#96; to start
after bug &#35;123456. Use the number of the last bug that was
successfully edited. As a safety check, the script will exit if the
first bug in the list already has the comment.
::::

The script comments on all \'Fedora\' and \'Fedora Container Images\'
bugs for the release which are still open, unless they have the
&#42;&#42;Tracking&#42;&#42; keyword. This
{bugzilla_eol_query}\[Bugzilla query\] is similar to the one it uses (if
you want to examine the list before running the script).

# EOL day SOP {#_eol_day_sop}

This document outlines the procedure for performing end-of-life (EOL)
activities.

## Timing/trigger {#_timingtrigger_5}

This process occurs four weeks after the release of Fedora Linux N+2.

## Process {#_process_2}

### Bug closure {#_bug_closure}

Close open bugs using the [&#96;fedora_bz.py&#96;
script](https://pagure.io/fedora-pgm/pgm_scripts/blob/main/f/closebugs/fedora_bz.py).

For example, to close Fedora Linux 37 bugs: &#96;./fedora_bz.py eolclose
37&#96;

The script will read the EOL date from Bodhi, or you can override it,
e.g. &#96;./fedora_bz.py eolclose \--date=2023-12-05 37&#96;.

You can re-run the script to verify that all bugs are closed (it should
change 0 bugs).

:::: warning
::: title
:::

This script will take a while to run. Execute it from a machine with
stable power and networking. If it dies, you can re-run it and it should
pick up where it left off.
::::

The script closes all \'Fedora\' and \'Fedora Container Images\' bugs
for the EOL release which are still open, unless they have the
&#42;&#42;Tracking&#42;&#42; keyword. This
{bugzilla_eol_query}\[Bugzilla query\] is similar to the one it uses (if
you want to examine the list before running the script).

#### Reopening bugs {#_reopening_bugs}

If you get a request to re-open a bug, do that as a service to the
users.

### Update product description {#_update_product_description_2}

Adjust the wording of the [Fedora
product](https://bugzilla.redhat.com/editproducts.cgi?action=edit&amp;product=Fedora)
in Bugzilla to reflect the EOL.

&#8230;. Bugs related to the components of the Fedora distribution. If
you are reporting a bug against a stable release or a branched
pre-release version, please select that version number. The currently
maintained released versions are: Fedora N-1, Fedora N. If you have a
bug to report against the daily development tree (rawhide), please
choose \'rawhide\' as the version.

For more information about filing a bug against Fedora packages, see
<https://docs.fedoraproject.org/en-US/quick-docs/howto-file-a-bug/>
&#8230;.

### Disable EOL version {#_disable_eol_version}

1.  Disable the EOL release in the

    a.  [Fedora](https://bugzilla.redhat.com/editversions.cgi?product=Fedora)
        product

    b.  [Fedora Container
        Images](https://bugzilla.redhat.com/editversions.cgi?product=Fedora%20Container%20Images)
        product

### Wiki and website edits {#_wiki_and_website_edits}

1.  Update the index.html page on the [web
    view](https://fedorapeople.org/groups/schedule/) of the schedule.
    Publish the changes using the [instructions for the schedule git
    repo](pgm_guide/schedule.adoc&#35;_git_repo).

2.  Update the releases docs

    a.  Update the [Releases page](releases::index.xml) (or really, the
        &#96;nav.adoc&#96; sidebar).

    b.  Add the EOL version and date to the [End of Life
        page](releases::eol.xml).

### Product Pages {#_product_pages_3}

Set the release to \'Unsupported\' in Product Pages. Do
&#42;&#42;not&#42;&#42; unpublish the release.

# Changes SOP {#_changes_sop}

This document describes the process of handling
[Changes](changes_policy.xml). Most activities are split to individual
files for easier reading.

## Timing/trigger {#_timingtrigger_6}

Timing varies by specific procedure.

## Process {#_process_3}

### Announce proposals {#_announce_proposals}

See the [Changes (Announce) SOP](pgm_guide/sop/changes-announce.xml).

### Submit proposals to FESCo {#_submit_proposals_to_fesco}

See the [Changes (Submitting) SOP](pgm_guide/sop/changes-submit.xml).

### Process proposals {#_process_proposals}

See the [Changes (Process) SOP](pgm_guide/sop/changes-process.xml).

### Evaluate contingency plans {#_evaluate_contingency_plans}

See the [Changes (Contingency)
SOP](pgm_guide/sop/changes-contingency.xml).

### Defer Changes {#_defer_changes}

See the [Changes (Deferring) SOP](pgm_guide/sop/changes-defer:w.xml).

### Drop Changes {#_drop_changes}

See the [Changes (Dropping) SOP](pgm_guide/sop/changes-drop:w.xml).

### Completing Changes {#_completing_changes}

See the [Release Day SOP](pgm_guide/sop/release_day.xml).

### Update ChangeSet page {#_update_changeset_page}

\[&#35;update_changeset\]

After processing approved or deferred Changes, and regularly throughout
the late part of the release cycle, update the wiki page listing that
release's approved Changes.

1.  Process the status with the
    [scripts](https://pagure.io/fedora-pgm/pgm_scripts/blob/main/f/changes)

    a.  Run &#96;make version=&lt;NN&gt;
        type=&lt;SystemWide\|SelfContained&gt; build&#96; to download
        and parse the wiki pages. This includes a check of the current
        status of the tracker bugs in Bugzilla

2.  Copy the content of the &#96;ChangesList&#96; file

3.  Paste it into the appropriate section of the
    &#96;Release/F&lt;NN&gt;/ChangeSet&#96; page in the wiki

# Changes (Announcing) SoP {#_changes_announcing_sop}

This document describes the process of announcing
[Changes](changes_policy.xml).

## Timing/trigger {#_timingtrigger_7}

This process is constant.

## Process {#_process_4}

Proposals are sent to the development community for public comment.

1.  Verify that the proposal is complete and correct

    a.  You can choose to announce proposals that are missing some
        required fields (e.g. Releng ticket), on the condition that
        those are complete before it is sent to FESCo

    b.  Ensure the page has the &#96;{{Change_Proposal_Banner}}&#96;
        macro at the top

    c.  Put the *Owner* and *Email* fields are one line instead of
        multiple. This will make the BZ creation easier later.

2.  Compose an email as follows.

    a.  Set the &#96;to:&#96; field to
        &#96;<devel-announce@lists.fedoraproject.org>&#96; and the
        &#96;reply-to:&#96; field to
        &#96;<devel@lists.fedoraproject.org>&#96;

    b.  Set the subject to *F&lt;NN&gt; proposal: &lt;title&gt;
        (&lt;System-Wide\|Self-Contained&gt; Change proposal)*. This is
        to make it clear to external readers that this is a *proposal*
        and not a final decision.

    c.  In the body of the email, add the URL to the wiki page

    d.  Copy the \'this is a proposal\' content from the wiki page into
        the body. Again, this is so that it's unambigiously clear.

    e.  Copy the wiki source into the body, removing comments and
        performing other readability cleanup as you deem necessary.

3.  Send the email

4.  Create a post in the [Discourse Change Proposals
    category](https://discussion.fedoraproject.org/c/project/changes/89).

    a.  Set the topic to *F&lt;NN&gt; Change Proposal: &lt;title&gt;
        (&lt;System-Wide\|Self-Contained&gt;)*.

    b.  Place a link to the wiki page and a link to the devel-announce
        post at the top of the post.

    c.  Then copy the \'this is a proposal\' content from the wiki page
        into the post.

    d.  Copy the contents of the wiki page into the post, applying
        Markdown formatting as appropriate. You can try converting the
        wiki text to markdown by saving it as &#96;change.txt&#96; and
        running &#96;pandoc -f mediawiki -w markdown /change.txt -o
        /change.md&#96;, but it will not work perfectly and will still
        require manual adjustment.

5.  Reply to your original announcement email, again with
    &#96;reply-to&#96; set to &#96;<devel@lists.fedoraproject.org>&#96;,
    with the content: &#96;The discussion thread to provide feedback for
    this change proposal can be found here:
    <https://(link_to_discourse_post)&#96>;

6.  Update the wiki page

    a.  Replace the &#96;ChangeReadyForWrangler&#96; category with
        &#96;ChangeAnnounced&#96;

    b.  Add a link to the [devel-announce
        thread](https://lists.fedoraproject.org/archives/list/devel-announce%40lists.fedoraproject.org/)
        in the *Current status* section, with the title \'Announced\'

    c.  Add a link to the Discourse thread in the same section, with the
        title \'Discussion Thread\'

7.  Add an entry to the *Changes* table for the release in [Friday's
    Fedora Facts](pgm_guide/sop/fridays_fedora_facts.xml)

Once you have sent the email, you do not need to further participate in
the discussion. However, you should at least monitor the tone in case it
gets heated.

:::: tip
::: title
:::

You can use the [pending_changes.py
script](https://pagure.io/fedora-pgm/pgm_scripts/blob/main/f/changes/pending_changes.py)
to list proposals that are awaiting announcement. This is particularly
helpful if you set it up in a cron job or systemd timer.
::::

# Changes (Submitting) SoP {#_changes_submitting_sop}

This document describes the process of submitting
[Changes](changes_policy.xml) to FESCo.

## Timing/trigger {#_timingtrigger_8}

Submit Changes one week after the proposal is
[announced](pgm_guide/sop/changes-announce.xml).

## Process {#_process_5}

After a week of discussion (or longer if the discussion is still
productively active), submit it to FESCo for approval.

1.  Open an issue with the [Change proposal
    template](https://pagure.io/fesco/new_issue?template=change_proposal)

    a.  Use &#96;Change: &lt;title&gt;&#96; as the issue title

    b.  Replace the angle bracketed fields as appropriate

    c.  Set the *Assignee* of the issue to be the first person listed on
        the proposal

    d.  Set the *system-wide change* or *self-contained change* tag as
        appropriate

    e.  Set the *Milestone* as appropriate

2.  In the proposal wiki page

    a.  Replace the &#96;ChangeAnnounced&#96; category with
        &#96;ChangeReadyForFesco&#96;

    b.  Add the FESCo ticket URL in the *Current status* section

3.  Update the [Friday's Fedora
    Facts](pgm_guide/sop/fridays_fedora_facts.xml) entry

# Changes (Processing) SoP {#_changes_processing_sop}

This document describes the process of processing
[Changes](changes_policy.xml) after FESCo's vote.

## Timing/trigger {#_timingtrigger_9}

Process Changes after the vote is final per [FESCo's ticket
policy](fesco::index.adoc&#35;_ticket_policy).

## Process {#_process_6}

### Approved proposals {#_approved_proposals}

1.  Note the vote (e.g. \'APPROVED (+6,0,-0)\') in the comment, if not
    already recorded

2.  Apply the *pending announcement* label if the issue is still open.
    This lets the next meeting chair know to include an announcement of
    the decision in the agenda

3.  Edit the proposal's wiki page

    a.  Remove the &#96;{{Change_Proposal_Banner}}&#96; macro

    b.  Replace the &#96;ChangeReadyForFesco&#96; category with
        &#96;ChangeAcceptedF&lt;NN&gt;&#96;

4.  Create new bugs with the
    [scripts](https://pagure.io/fedora-pgm/pgm_scripts/blob/main/f/changes)

    a.  Run &#96;make version=&lt;NN&gt;
        type=&lt;SystemWide\|SelfContained&gt; build&#96; to download
        and parse the wiki pages

    b.  Run &#96;make bz&#96; to create tracking bugs in Bugzilla.

5.  Edit the created bug

    a.  Add yourself to the *cc* field

    b.  Set the bug to block the &#96;F&lt;NN&gt;Changes&#96; tracking
        bug

    c.  Set the bug status to &#96;ASSIGNED&#96;

6.  When appropriate (see below), create a Release Notes issue with the
    [Change
    template](https://gitlab.com/fedora/docs/fedora-linux-documentation/release-notes/-/issues/new?issuable_template=Change).

    a.  Use &#96;Change: &lt;title&gt;&#96; as the issue title

    b.  Replace &#96;URL HERE&#96; with the wiki URL

    c.  Set the *Milestone* appropriately

7.  Add the Bugzilla and Release Notes links to the wiki page

8.  Update the [Friday's Fedora
    Facts](pgm_guide/sop/fridays_fedora_facts.xml) entry

9.  Update the ChangeSet page

    a.  In the scripts directory, run: &#8230; &#96;make clean&#96;
        &#8230; &#96;make version=&lt;NN&gt;
        type=&lt;SystemWide\|SelfContained&gt; build&#96; to regenerate
        the content &#8230; Copy the contents of *ChangesList* and paste
        into the appropriate section of the ChangeSet page

10. If the Change involves a new Spin, add it to the [Releases
    docs](releases::index.xml).

:::: warning
::: title
:::

Bugzilla requires an email address to exist in the system in order to
add it to a bug. If an email address listed on a wiki page does not
exist in Bugzilla, that address will not be CCed on the bug. If no
address listed exists in Bugzilla, the bug will remain assigned to the
Change Wrangler. In that case you should try and find an address for a
Change owner that does exist in Bugzilla and re-assign it, or ask the
Change owner(s) to register in Bugzilla.
::::

:::: tip
::: title
:::

If the Change involves creating a new Spin, send the owners the
[Creating a Spin docs](releases::spins/creating.xml). Otherwise, the
coordination with Websites et al will probably be overlooked.
::::

RELEASE NOTES: most Changes should be considered for release notes, but
sometimes this does not make sense. When a Change will not result in any
notable impact on end users that can comprehensibly be explained to
them, a release note is not necessary. An example of such a Change is
<https://fedoraproject.org/wiki/Changes/PortingToModernC> : this is a
highly technical Change that is only of consequence and interest to
Fedora maintainers, not end users. When it does not make sense for a
Change to have release notes, put \'Release Notes tracker: N/A\' in the
\'Current status\' section of the Change page.

### Rejected proposals {#_rejected_proposals}

If a Change proposal is rejected by FESCo:

1.  Add &#96;{{Change_Rejected_Banner}}&#96; to the proposal's wiki page
    below the title

2.  Update the wiki page category to
    &#96;Category:ChangePageIncomplete&#96;

3.  If a tracking bug was pre-created, close it with Status *CLOSED
    -&gt; DEFERRED*.

# Changes (Contigency) SoP {#_changes_contigency_sop}

This document describes the process of evaluating the contingency plans
of [Changes](changes_policy.xml).

## Timing/trigger {#_timingtrigger_10}

Evaluate contigency plans at the following points in the release
schedule:

&#42; Start of the mass rebuild &#42; Completion Checkpoint (Testable)
deadline / Branch day (currently the same day) &#42; Completion
Checkpoint (100% complete) deadline / Start of Beta freeze (currently
the same day) &#42; Start of Final freeze

In addition, if a Change has a different contingency deadline for
whatever reason, evaluate plans then.

## Process {#_process_7}

In general, the process is to check with the owner and ask if the Change
is on track. If not, work with them to [defer
it](pgm_guide/sop/changes-defer.xml).

On the mass rebuild day, check for Changes that do not appear to be
progressing, and informally remind the owner of the upcoming deadlines.
The two \'change completion checkpoint\' milestones on the schedule have
specific actions below. At the Final freeze, do a final check for
still-unresolved incomplete Changes and ask FESCo to address them.

### Report incomplete Changes {#_report_incomplete_changes}

This part of the process runs at the \'Completion deadline (testable)\'
and \'Completion deadline (100% complete)\' milestones of the release
schedule.

1.  On the deadline day, use the [&#96;fedora_bz.py&#96;
    script](https://pagure.io/fedora-pgm/pgm_scripts/blob/main/f/closebugs/fedora_bz.py)
    to comment on bugs that block the Changes tracking bug that do are
    not at least as far as MODIFIED (testable deadline) or ON_QA (100%
    complete deadline).

    a.  For the testable deadline, run e.g. &#96;./fedora_bz.py
        deadline-testable 2024-02-20 40&#96;, where 40 is the release
        number and 2024-02-20 is the &#42;&#42;100% complete&#42;&#42;
        deadline date (&#42;&#42;NOT&#42;&#42; the testable deadline
        date - this date is needed because the comment mentions it).

    b.  For the 100% complete deadline, run e.g. &#96;./fedora_bz.py
        deadline-complete 40&#96;, where 40 is the release number. No
        date is needed here.

2.  The next day, create a FESCo issue using one of the
    xref:&#35;fesco-issue-templates\[FESCo issue templates\] below. You
    may choose to try to figure out if a change is complete yourself,
    but you are not obligated to.

3.  Continue to update the FESCo issue as bugs are updated.

4.  Update or defer Changes as voted by FESCo.

[]{#fesco-issue-templates}

#### Completion deadline (testable) FESCo issue template {#_completion_deadline_testable_fesco_issue_template}

&#8230;. On Tuesday, &lt;DATE&gt; we reached the Change Checkpoint:
Completion deadline (testable). At this milestone all the
F&lt;VERSION&gt; Changes should be testable, which is indicated by
\'MODIFIED\' status of a tracking bug. A \[Bugzilla
query\](https://bugzilla.redhat.com/buglist.cgi?bug_status=NEW\\&bug_status=ASSIGNED\\&bug_status=POST\\&f1=blocked\\&list_id=12817824\\&o1=substring\\&v1=F\\\<VERSION\\\>Changes)
shows all the tracking bugs which are not in \'MODIFIED\' state and are
not considered testable. System-Wide Changes with the contingency date
in bold are past the stated contingency date.

These changes are presented for FESCo review to determine what action,
if any, should be taken. The next deadline is &lt;DATE&gt; when all
changes should be 100% code complete.

&#35;&#35; System-Wide Changes

&#42; \[&lt;Change title&gt;\](&lt;Wiki URL&gt;) &#42; Owner:
@&lt;ID&gt; &#42; Contingency mechanism: &lt;mechanism&gt; &#42;
Contingency deadline: &lt;deadline&gt; &#42; &lt;repeat as necessary&gt;

&#35;&#35; Self-Contained Changes

&#42; \[&lt;Change title&gt;\](&lt;Wiki URL&gt;) &#42; Owner:
@&lt;ID&gt; &#42; &lt;repeat as necessary&gt; &#8230;.

#### Completion deadline (100% complete) FESCo issue template {#_completion_deadline_100_complete_fesco_issue_template}

&#8230;. On Tuesday, &lt;DATE&gt; we reached the Change Checkpoint:
Completion deadline (100% complete). At this milestone all the
F&lt;VERSION&gt; Changes should be fully complete, which is indicated by
\'ON_QA\' status of a tracking bug. A \[Bugzilla
query\](https://bugzilla.redhat.com/buglist.cgi?bug_status=NEW\\&bug_status=ASSIGNED\\&bug_status=POST\\&bug_status=MODIFIED\\&f1=blocked\\&list_id=12817824\\&o1=substring\\&v1=F\\\<VERSION\\\>Changes)
shows all the tracking bugs which are not in \'ON_QA\' state and are not
considered complete. System-Wide Changes with the contingency date in
bold are past the stated contingency date.

These changes are presented for FESCo review to determine what action,
if any, should be taken.

&#35;&#35; System-Wide Changes

&#42; \[&lt;Change title&gt;\](&lt;Wiki URL&gt;) &#42; Owner:
@&lt;ID&gt; &#42; Contingency mechanism: &lt;mechanism&gt; &#42;
Contingency deadline: &lt;deadline&gt; &#42; &lt;repeat as necessary&gt;

&#35;&#35; Self-Contained Changes

&#42; \[&lt;Change title&gt;\](&lt;Wiki URL&gt;) &#42; Owner:
@&lt;ID&gt; &#42; &lt;repeat as necessary&gt; &#8230;.

# Changes (Deferring) SOP {#_changes_deferring_sop}

This document describes the process of deferring
[Changes](changes_policy.xml) to the next release.

## Timing/trigger {#_timingtrigger_11}

This process is triggered by FESCo or the owner deciding to defer a
change. Often, this is the result of missing a [contingency deadline or
completion milestone](pgm_guide/sop/changes-contingency.xml). Unless the
Change changes significantly, it does not need to go through the process
again. Chnages can be deferred indefinitely.

## Process {#_process_8}

1.  &#42;&#42;Reply to the mailing list thread&#42;&#42;, only if the
    proposal has not yet been submitted to FESCo.

2.  &#42;&#42;Update the *Milestone* in the FESCo ticket&#42;&#42;, only
    if the ticket is still open (in other words, if FESCo has not yet
    reached a decision).

3.  &#42;&#42;Update the Change's wiki page.&#42;&#42; Change the
    \'Targeted Release\' to the new release. Change the category to
    \'ChangeAcceptedF&lt;N&gt;\'.

4.  &#42;&#42;Update the tracking bug.&#42;&#42; Update the *Blocks*
    field with the new release's Change tracking bug. If the Change is
    deferred after bugs have been branched, reset the version to
    \'rawhide\'.

5.  &#42;&#42;Update the Release Notes issue.&#42;&#42; Set the
    *Milestone* field to the new target release.

6.  &#42;&#42;Re-run the Change processing scripts for the old and new
    target release.&#42;&#42; See the
    [instructions](pgm_guide/sop/changes.adoc&#35;update_changeset).

:::: note
::: title
:::

If the Change was previously approved, do not award the badge for the
re-targeted release.
::::

# Changes (Dropping) SOP {#_changes_dropping_sop}

This document describes the process of dropping
[Changes](changes_policy.xml).

## Timing/trigger {#_timingtrigger_12}

This process is triggered by FESCo or the owner deciding to drop a
change. Often, this is the result of a Change having significant issues,
or a maintainer losing interest. For the Change to be revived it must go
through the full process again, starting by being updated and moved back
to ChangeReadyForWrangler.

## Process {#_process_9}

1.  &#42;&#42;Reply to the mailing list thread&#42;&#42;, only if the
    proposal has not yet been submitted to FESCo.

2.  &#42;&#42;Close the FESCo ticket&#42;&#42;, if one has been opened
    and is still open.

3.  &#42;&#42;Update the Change's wiki page.&#42;&#42; Clear the
    \'Targeted Release\'. Change the category to
    \'ChangePageIncomplete\'. Add a header at the top:
    &#96;{{admon/important\|Change dropped\|This Change is dropped. It
    can be re-proposed if interest in it revives.}}&#96; It is a good
    idea to also include an appropriate reference - a link to a FESCo
    ticket or meeting log, or a message from the Change owner.

4.  &#42;&#42;Update the tracking bug, if it exists.&#42;&#42; Clear the
    *Blocks* field. Reset the version to \'rawhide\'. Close the bug as
    DEFERRED.

5.  &#42;&#42;Close the Release Notes issue, if it exists.&#42;&#42;

6.  &#42;&#42;Re-run the Change processing scripts for the old and new
    target release.&#42;&#42; See the
    [instructions](pgm_guide/sop/changes.adoc&#35;update_changeset).

# Prioritized Bugs SOP {#_prioritized_bugs_sop}

This document outlines the process for managing [prioritized
bugs](prioritized_bugs.xml).

## Timing/trigger {#_timingtrigger_13}

Meetings occur every two weeks. Follow-up occurs weekly when priortized
bugs exist.

## Procedure {#_procedure_2}

### Meeting prep {#_meeting_prep}

The day before the meeting:

1.  Update the [IRC
    script](https://pagure.io/fedora-pgm/pgm_communication/blob/main/f/prioritized_bugs.txt)

    a.  Add the [nominated
        bugs](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__\&amp;f1=flagtypes.name\&amp;f2=OP\&amp;list_id=10626345\&amp;o1=substring\&amp;query_format=advanced\&amp;v1=fedora_prioritized_bug%3F)

    b.  Check the status of [accepted
        bugs](https://bugzilla.redhat.com/buglist.cgi?bug_status=__open__\&amp;f1=flagtypes.name\&amp;f2=OP\&amp;list_id=10626381\&amp;o1=substring\&amp;query_format=advanced\&amp;v1=fedora_prioritized_bug%2B)
        &#8230; Note any changes since the previous meeting

    c.  Note any acepted bugs closed since the last meeting in the
        \'Bugs fixed since last meeting\' section

    d.  Update the next meeting date

2.  Send an email with the agenda to <triage@lists.fedoraproject.org>
    and cc <devel@lists.fedoraproject.org>,
    <test@lists.fedoraproject.org> . bcc the assignee of nominated and
    accepted bugs. bcc the nominator of nominated bugs.

:::: tip
::: title
:::

If there are no nominated bugs and the accepted bugs (if any) are not
stuck, cancel the meeting.
::::

### Meeting process {#_meeting_process}

1.  Follow the the [IRC
    script](https://pagure.io/fedora-pgm/pgm_communication/blob/main/f/prioritized_bugs.txt)

2.  Try to achieve consensus on each decision

3.  Note decisions with the &#96;&#35;agreed&#96; command

### Post-meeting process {#_post_meeting_process}

1.  For each nominated bug

    a.  Note the decision in a comment

    b.  For accepted bugs, set the &#96;fedora_prioritized_bug&#96; flag
        to &#96;+&#96;

    c.  For rejected bugs, set the &#96;fedora_prioritized_bug&#96; flag
        to &#96;-&#96;

2.  Update the table in [Friday's Fedora
    Facts](pgm_guide/sop/fridays_fedora_facts.md)

### Check-in process {#_check_in_process}

Once a week, check that status of accepted bugs. If no progress has been
recorded in 1--2 weeks, nudge the assignee. If bugs are stuck, send a
summary email to the devel mailing list soliciting help.

Update the [Friday's Fedora
Facts](pgm_guide/sop/fridays_fedora_facts.md) table as appropriate.

# Blocker status email SOP {#_blocker_status_email_sop}

This document describes the procedure for sending blocker status emails.
The email is intended to provide a high-level overview of
release-blocking bugs.

## Timing/trigger {#_timingtrigger_14}

Send weekly beginning after the upcoming release branches from Rawhide.
It is typically sent on Fridays, however this is not a hard requirement.

## Procedures {#_procedures_4}

For each accepted and proposed blocker in the [BlockerBugs
application](https://qa.fedoraproject.org/blockerbugs) for the relevant
milestone,

1.  Add a line to the table in [Friday's Fedora
    Facts](pgm_guide/sop/fridays_fedora_facts.xml). See that SOP for
    formatting instructions.

2.  In the
    [blocker_email.txt](https://pagure.io/fedora-pgm/pgm_communication/blob/main/f/blocker_email.txt)
    file,

    a.  Add information in the bug-by-bug detail section &#8230; First
        line: &lt;&#35;&gt;. &lt;component name&gt; --- &lt;bug link&gt;
        --- &lt;bug state&gt; &#8230; Second line: &lt;bug
        title/summary&gt; &#8230; Third line: (blank) &#8230; Subsequent
        lines: Include a brief summary of the behavior and key
        constraints. Include the following, if appropriate: &#8230;.
        Link to upstream bug or pull request &#8230;. Updates that
        contain a candidate or verified fix

    b.  Add information in the action summary section &#8230; First
        line: &lt;&#35;&gt;. &lt;component name&gt; --- &lt;bug
        title/summary&gt; --- &lt;bug state&gt; &#8230; Section line:
        ACTION: &lt;action statement (see below)&gt; &#8230; Third line
        (if applicable): NEEDINFO: &lt;person marked NEEDINFO in the
        bug&gt;

When the information is fully collected, create the email message

1.  To: <test@lists.fedoraproject.org>, <devel@lists.fedoraproject.org>

2.  cc: (appropriate team mailing lists, if applicable)

3.  bcc: action-ed and needinfo-ed people (excluding upstream trackers)

4.  Open the body with a quick summary of schedule status. For example,
    indicate the current target date.

5.  Include the contents of the blocker_email.txt afterward

### Action statements {#_action_statements}

Action statements generally take the form of \'&lt;person/group&gt; to
&lt;action&gt;.\' You can write them however you want, but most will
look like one of the following:

&#42; When there's an upstream bug: \'Upstream to diagnose issue\' &#42;
When there's an upstream PR: \'Upstream to merge &lt;PR ID&gt;\' &#42;
When there's no upstream report and no diagnosis: \'Maintainers to
diagnose issue\' &#42; When there's a patch/PR or new upstream release:
\'Maintainers to create an update with &lt;patch/PR or upstream
release&gt;\' &#42; When there's an update with a candidate fix: \'QA to
verify &lt;update ID&gt;\' &#42; When the bug is in VERIFIED state:
\'(none)\' &#42; When there's informating missing: \' \'&lt;person&gt;
to provide &lt;missing info&gt;\'

### Tips {#_tips}

The following is general advice.

&#42; Don't worry about getting too deep into the technical aspects.
You're not there to diagnose issues. &#42; Update bugs if the state is
inconsistent with reality. (e.g. if an upstream PR exists, set it to
POST) &#42; If you're short on time, skip the bugs that seem likely to
be rejected. &#42; Remove the emails from the cc and bcc lines in the
text file *before* committing changes.

# Spins keepalive SOP {#_spins_keepalive_sop}

This document outlines procedures for the Spins keepalive process. This
process was [approved by the Fedora Engineering Steering
Committee](https://pagure.io/fesco/issue/1972) to ensure that [Spins and
Labs](releases::spins.xml) are actively maintained.

## Timing/trigger {#_timingtrigger_15}

The process begins &#42;&#42;two weeks&#42;&#42; before the
Self-Contained Change proposal deadline.

## Process {#_process_10}

1.  Click the &#42;New issue&#42; button in the [schedule
    repo](https://pagure.io/fedora-pgm/schedule/).

2.  Select \'&lt;spins_labs_keepalive&gt;\' as the issue template

3.  Set &#96;&lt;Spin/Lab name&gt; keepalive&#96; as the issue title

4.  Update the body of the ticket with the maintainer name, deadline
    date and Fedora Release &#35;

5.  Apply the &#42;spins keepalive&#42; tag, target release as the
    milestone and assign the ticket to the maintainer

6.  Click &#42;Create Issue&#42;

7.  Once all spins and labs keepalive requests are filed, send an email
    to the
    [devel-announce](https://lists.fedoraproject.org/archives/list/devel-announce%40lists.fedoraproject.org/)
    and
    [spins](https://lists.fedoraproject.org/archives/list/spins%40lists.fedoraproject.org/)
    mailing lists (update the date and release):

8.  After one week, send a reminder email

9.  At the deadline, send a final email

10. After one week post the deadline, send a notification email that the
    spin or lab will be dropped for this release and follow removal
    process.

11. File the respective tickets for dropped spins/labs (see removal
    process below)

:::: note
::: title
:::

Ignore the Test Days spin. It's useful to QA, but we don't release it
publicly.
::::

### Notfication of Keepalive Requests {#_notfication_of_keepalive_requests}

To notify maintainers that the keepalive deadline is coming up, the
first step is to create keepalive tickets for each Spin/Lab as listed
above. The ticket is templated so you need to just update the fields and
tag the ticket correctly. The email template to then send announcing the
spins and labs keepalive requests is as follows:

&#8230;. FESco previously approved a requirement that Spin/Labs owners
send a keepalive request in order to keep building the spin or lab. I
have opened Pagure issues\[1\] for all Spins and Labs for this
release\[2\].

If you are the owner of one of those spins and labs, please reply in the
appropriate ticket by &lt;DATE&gt;&gt; to indicate the spin should
continue to be produced. If there is a spin or lab that does not have an
open ticket, please create one\[3\].

The reasoning for this is to not ship spins that are not actively
maintained. Future improvements to the release process that will allow
for teams to self-publish solutions will eventually remove the need for
these keepalives.

\[1\]
<https://pagure.io/fedora-pgm/schedule/issues?status=Open&amp;tags=spins+keepalive>
\[2\]
<https://docs.fedoraproject.org/en-US/releases/f&lt;RELEASE&gt;/spins/>
\[3\] <https://pagure.io/fedora-pgm/schedule/new_issue> &#8230;.

### Deadline {#_deadline}

At the deadline, send this email to the
[devel-announce](https://lists.fedoraproject.org/archives/list/devel-announce%40lists.fedoraproject.org/)
and
[spins](https://lists.fedoraproject.org/archives/list/spins%40lists.fedoraproject.org/)
mailing lists with a list of spins that have not been kept alive.

&#8230;. The following Spins/Labs maintainers have not indicated they
wish to continue producing the deliverables for the upcoming release.
Any that have not been adopted in one week will be dropped.

&#42; &lt;list of Spins/Labs&gt; &#8230;.

### Process for Removal {#_process_for_removal}

One week after deadline, if=f there are still Spins/Labs that have not
been adopted or had the current maintainer send a keepalive,

1.  Open a [Release Engineering issue](https://pagure.io/releng/issues)
    to have those deliverables removed.

2.  Open a [Websites issue](https://pagure.io/fedora-websites/issues) to
    remove the deliverables from the website for the release.

:::: important
::: title
:::

Submit the removal ticket before branch day so that the images are never
produced for that release.
::::

:::: note
::: title
:::

Spins and Labs maintainers who engage in the keepalive ticket should
file their own removal request or change of ownership PR, but it is
always good practice to confirm with them that these steps are completed
in the ticekt.
::::

# Inactive packagers SOP {#_inactive_packagers_sop}

This document outlines procedures for processing inactive package
maintainers. FESCo [approved](https://pagure.io/fesco/issue/2759) a
[policy for removing inactive
packagers](fesco::Policy_for_inactive_packagers.xml). In concert with
the [Provenpackager
policy](fesco::Provenpackager_policy.adoc&#35;_maintaining_provenpackager_status),
this policy is intended to reduce the risk of account compromise for
inactive packagers.

## Timing/trigger {#_timingtrigger_16}

This process occurs once per release. The initial list of inactive
packagers is created a week before Beta freeze. Removal of inactive
packagers happens a week after the final release.

We wait until after the final release to prevent orphaning packages
near/during a freeze, which could be very unpleasant.

## Procedures {#_procedures_5}

Both parts of the process require the [find-inactive-packagers
script](https://pagure.io/find-inactive-packagers). By default, it will
open issues in the [find-inactive-packagers
repo](https://pagure.io/find-inactive-packagers/issues).

### Build list of inactive packagers {#_build_list_of_inactive_packagers}

1.  Generate a kerberos ticket with &#96;fkinit -u &lt;YOUR FEDORA
    ACCOUNT ID&gt;&#96;

2.  Set your [Pagure API
    key](https://pagure.io/settings&#35;nav-api-tab) with &#96;export
    PAGURE_API_KEY=&lt;YOUR_API_KEY&gt;&#96;

3.  Run &#96;python3 find_inactive_packagers.py \--privacy step-one
    \--open-tickets&#96; . This opens Pagure tickets for each packager.
    It also produces a &#96;inactive_packagers.csv&#96; file listing the
    inactive packagers it found.

4.  Send a list of inactive packagers to
    [devel-announce](https://lists.fedoraproject.org/archives/list/devel-announce%40lists.fedoraproject.org/).
    See the template below.

5.  (optional) Run &#96;python3 find-inactive-pacakgers.py
    check-impact&#96;. This will generate a list of pacakges that will
    be orphaned. This uses open tickets. It does not perform an
    additional check. You can re-run it several times between steps 1
    and 2 in order to keep an updated list.

&#8230;. In accordance with FESCo's Inactive Packager Policy\[1\],
packagers that have been identified as inactive have a ticket in the
find-inactive-packagers repo\[2\]. One week after the final release,
packagers who remain inactive will be removed from the packager group.
(Note that pagure.io is one of the systems checked for activity, so
commenting on your ticket that you're still around will prevent you from
showing up in the second round.)

If you have suggestions for improvement, look for the open feature
issues\[3\] and file an issue in the find-inactive-packagers repo\[4\]
if it's not there already.

For the curious, here are the stats from today's run:

&lt;INSERT STATS FROM SCRIPT&gt;

\[1\]
<https://docs.fedoraproject.org/en-US/fesco/Policy_for_inactive_packagers/>
\[2\]
<https://pagure.io/find-inactive-packagers/issues?tags=inactive_packager&amp;status=Open>
\[3\] <https://pagure.io/find-inactive-packagers/issues?tags=feature>
\[4\] <https://pagure.io/find-inactive-packagers/new_issue> &#8230;.

### Managing responses {#_managing_responses}

If the packager replies that they would like to keep packager status,
close the ticket *Keep pacakger status*.

If the packager replies that they are okay with dropping their packager
status, add the *asked_removal* tag, but &#42;do not close the
ticket.&#42;

### Request removal of inactive packagers {#_request_removal_of_inactive_packagers}

1.  Run &#96;python3 find-inactive-packagers.py step-two
    \--close-tickets&#96;. This generates a &#96;still_inactive.csv&#96;
    file and closes active tickets appropriately.

2.  Open a [Fedora Infrastructure
    ticket](https://pagure.io/fedora-infrastructure/issues) to remove
    inactive packagers.

# Inactive Provenpackagers SOP {#_inactive_provenpackagers_sop}

This document describes the process for identifying and removing
inactive provenpackagers in accordance with [FESCo
policy](fesco::Provenpackager_policy.adoc&#35;_maintaing_provenpackager_status).

## Trigger/timing {#_triggertiming_2}

This process occurs once per release cycle, starting at or near the
branch day. It occurs in two parts.

## Process {#_process_11}

### Identify and notify inactive provenpackagers {#_identify_and_notify_inactive_provenpackagers}

1.  Generate a kerberos ticket with &#96;fkinit -u &lt;YOUR FEDORA
    ACCOUNT ID&gt;&#96;

2.  Run the [inactive_provenpackagers.py
    script](https://pagure.io/fedora-pgm/pgm_scripts/blob/main/f/provenpackager/inactive_provenpackagers.py)
    from the pgm_scripts repo. This script iterates over all members of
    the *provenpackagers* group, so it may take a while. Since it's a
    read-only operation, it's safe to re-run if it gets interrupted.

3.  Send an announcement of accounts identified as inactive using the
    template below. Use the [devel-announce mailing
    list](https://lists.fedoraproject.org/archives/list/devel-announce%40lists.fedoraproject.org/)
    in the *to:* field and bcc the *\@fedoraproject.org* addresses of
    listed as inactive.

&#8230;. In accordance with FESCo policy\[1\], the following
provenpackagers will be submitted for removal in two weeks based on a
lack of Koji builds submitted in the last six months. If you received
this directly, you can reply off-list to indicate you should still be in
the provenpackager group.

Note that removal from this group is not a \'punishment\' or a lack of
appreciation for the work you have done. The intent of the process is to
ensure contributors with distro-wide package privileges are still active
and responsive. This process is done regularly at the branch point in
each release.

\[1\]
<https://docs.fedoraproject.org/en-US/fesco/Provenpackager_policy/&#35;_maintaining_provenpackager_status>

&lt;OUTPUT of inactive_provenpackagers.py script&gt; &#8230;.

### Request removal of inactive provenpackagers {#_request_removal_of_inactive_provenpackagers}

1.  Wait two weeks from the initial notification.

2.  File an [issue with the Infrastructure
    team](https://pagure.io/fedora-infrastructure/issues) listing the
    accounts to remove from the *provenpackagers* group.

# Friday's Fedora Facts SOP {#_fridays_fedora_facts_sop}

This document describes the procedures for publishing the [Friday's
Fedora
Facts](https://communityblog.fedoraproject.org/tag/fridays-fedora-facts/)
posts on the Fedora Community Blog.

## Trigger/timing {#_triggertiming_3}

Publish the post weekly on Friday (hence the name). For ease of
maintenance, update the [source
file](https://pagure.io/fedora-pgm/pgm_communication/blob/main/f/fridays_fedora_facts.md)
throughout the week.

## Procedures {#_procedures_6}

### Write the update {#_write_the_update}

1.  &#42;&#42;Collect announcements.&#42;&#42; This is an h2 level.
    Sources include: &#42;&#42; [announce mailing
    list](https://lists.fedoraproject.org/archives/list/announce%40lists.fedoraproject.org/)
    &#42;&#42; [devel-announce mailing
    list](https://lists.fedoraproject.org/archives/list/devel-announce%40lists.fedoraproject.org/)
    &#42;&#42; [CommBlog](https://communityblog.fedoraproject.org)
    &#42;&#42; Upcoming
    [schedule](https://fedorapeople.org/groups/schedule/) milestones

2.  &#42;&#42;Collect calls for participation (CfPs).&#42;&#42; This is
    an h3 level. Sources are listed in the markdown file. Use your best
    judgment in determining what might be of broad interest to the
    Fedora community. CfPs should be a table sorted by the CfP close
    date, ordered from soonest to latest. The table has the following
    columns: &#42;&#42; Conference. Includes the name and a link to the
    event website. &#42;&#42; Location. Includes the city and country
    (use the 2-letter code). Add the state if it takes places in the
    United States. For online conferences, use \'virtual\' as the
    location. For hybrid conferences, use the city and \'and virtual\'.
    &#42;&#42; Date. List day(s) of month followed by the three-letter
    month abbreviation. Do not include the year. &#42;&#42; CfP. Use
    \'closes &lt;date&gt;\' for CfPs with a defined close date. Use
    \'open\' for CfPs with an ambiguous or unstated close date. In that
    case, sort it based on a reasonable interpolation from event dates.
    In all cases, link directly to the CfP portal or a page specifically
    describing the conference's CfP process.

3.  &#42;&#42;Add help wanted calls.&#42;&#42; This is an h2 level.
    Include the following: &#42;&#42; A link to [open package review
    requests](https://fedoraproject.org/PackageReviewStatus/), and
    specificially call out the count awaiting a reviewer and the count
    needing a sponsor. &#42;&#42; A link to orphaned package or package
    retirement announcements from the [devel-announce mailing
    list](https://lists.fedoraproject.org/archives/list/devel-announce%40lists.fedoraproject.org/).
    &#42;&#42; Community surveys if any are open. &#42;&#42; Other calls
    for help that you notice on mailing lists, Discussion, or in chat.

4.  &#42;&#42;Add upcoming test days.&#42;&#42; This is an h3 level.
    Comment it out if there are no active test days. Add upcoming test
    days as an unordered list with the form \'&lt;date&gt; ---
    &lt;subject&gt;\'. Include a link to a CommBlog announcement or wiki
    page, if available. Sources include the [QA
    calendar](https://calendar.fedoraproject.org/list/QA/) and the
    [\'test days\' label in the fedora-qa
    repo](https://pagure.io/fedora-qa/issues?tags=test+days&amp;status=Open).

5.  &#42;&#42;Add meetings and events.&#42;&#42; This is an h2 level.
    Include entries in the form \'&lt;meeting&gt; --- &lt;time (UTC)&gt;
    &lt;day&gt; in &lt;location&gt;\'. Link the date to a calendar event
    when practical. Link the location the venue when not in one of the
    regular &#35;fedora-meeting-&#42; channels. Keep the meetings at
    project-level interest. For example: blocker reviews, Council,
    Mindshare, FESCo, prioritized bugs, Flock.

6.  &#42;&#42;Add releases.&#42;&#42; This is an h2 level. Generally,
    the only thing in this level should be a table of open bugs. The
    open bugs table should list all supported and in-development
    releases (including Rawhide) with a count of open bugs.

7.  &#42;&#42;Add prioritized bugs.&#42;&#42; This is an h3 level.
    Include a link to the [Prioritized Bugs process
    documentation](prioritized_bugs.xml). List the bugs in a table with
    the following columns: &#42;&#42; Bug number (with a link to the bug
    in Bugzilla) &#42;&#42; Component &#42;&#42; Status

8.  &#42;&#42;Add release-specific information.&#42;&#42; For each
    release where one of the following has content, include an h3 of
    \'Fedora Linux &lt;N&gt;\'. &#42;&#42; Count open of Fails To Build
    From Source and Fails To Install bugs as an unordered list.
    &#42;&#42; Upcoming schedule milestones. Only include important
    deadlines within the next 6--8 weeks. List them as an unordered list
    in the form \'&#42;&#42;&lt;date&gt;&#42;&#42; ---
    &lt;Milestone/deadline&gt;\' under an h4 of \'Schedule\'. &#42;&#42;
    Changes. List active change proposals in a table. Remove proposals
    after publishing the FFF where they have reached a terminal state
    (approved, rejected, or withdrawn). Link to the change set page and
    the tracking bug so readers can find approved proposals. The table
    should have the following columns: &#42;&#42;&#42; Proposal. This is
    the title of the proposal with a link to the wiki page.
    &#42;&#42;&#42; Type. (System-Wide or Self-Contained)
    &#42;&#42;&#42; Status. One of \'announced\' (include a link to the
    [devel mailing
    list](https://lists.fedoraproject.org/archives/list/devel%40lists.fedoraproject.org/)
    thread), \'FESCo &#35;&lt;ticket number&gt;\' (include a link to the
    FESCo ticket), approved, rejected, or withdrawn. &#42;&#42; Changes
    status. After the branch point, begin including a table of Change
    statuses. This is a table with the following columns:
    &#42;&#42;&#42; Status. The Bugzilla status. &#42;&#42;&#42; Count.
    The number of tracking bugs in that status. &#42;&#42; Blockers.
    List all active blockers for the next release milestone, starting
    after branch day. (You can choose to include final blockers prior to
    the beta release, if you feel like doing the work.) List blockers in
    a table with the following columns: &#42;&#42;&#42; Bug ID. The
    Bugzilla number with a link to the Bugzilla bug. &#42;&#42;&#42;
    Component. The current component that the bug is filed against.
    &#42;&#42;&#42; Bug status. The status from Bugzilla.
    &#42;&#42;&#42; Blocker status. One of
    \'Proposed(&lt;milestone&gt;)\' or \'Accepted(&lt;milestone&gt;)\'.

### Publish the update {#_publish_the_update}

1.  Run &#96;make&#96; in the directory where the
    &#96;fridays_fedora_facts.md&#96; file lives. This will generate
    HTML that you can copy and paste into WordPress.

2.  Title the post \'Friday's Fedora Facts: &lt;YYYY&gt;-&lt;WW&gt;\',
    where &lt;YYYY&gt; is the year and &lt;WW&gt; is the week of the
    year. The command &#96;date +%Y-%V&#96; will give you the correct
    date stamp.

3.  Copy the HTML and convert to blocks.

4.  Add a \'More\' element below the table of contents.

5.  Set the category to \'Program Management\'.

6.  Add the following tags: \'releases\', \'Fedora release changeset\',
    \'Friday's Fedora Facts\'. In addition, use \'Call for Papers
    (CfP)\', \'Help wanted\', \'Test Days\', \'elections\', and any
    other tags that might apply to the contents of this week's report.

7.  Set the featured image to be \'fpgm\' (a photo of a clipboard with
    the text \'From the Fedora Program Manager\') in the WordPress media
    library.

8.  After publishing the update, remove outdated content from the
    &#96;fridays_fedora_facts.md&#96; file.

Refer to the Community Blog [contribution
documentation](https://communityblog.fedoraproject.org/writing-community-blog-article/)
and [article
guidelines](https://communityblog.fedoraproject.org/editor-guidelines/)
for more details.

&#42;&#42;&#42; Elections = Election opening SOP

This document outlines the procedure for opening the post-release
election cycle. This covers two parallel activities: . Collection of
questions to use in interviews . Opening the nomination period

## Timing/trigger {#_timingtrigger_17}

This process occurs on the day following the final release.

## Procedure {#_procedure_3}

&#42; Make sure an \'I Voted\' badge has been created for this election
cycle. If it has not, open an issue with the Badges team. &#42; Edit the
[election banner
template](https://fedoraproject.org/wiki/Template:Election_Banner) in
the wiki to update the dates and current status &#42; Edit the
[Elections docs page](../../elections) to point to the current release's
schedule &#42; Add a milestone for the release in the
[elections-interviews repo
roadmap](https://pagure.io/fedora-pgm/elections-interviews/settings&#35;roadmap-tab)
&#42; Create tracking issues for each of the elections in the
[elections-interviews
repo](https://pagure.io/fedora-pgm/elections-interviews/issues). These
issues can be used to tie interview tickets to the specific election.

### Interview questionnaires {#_interview_questionnaires}

Open a ticket with each of Council, FESCo, EPEL and Mindshare Committee
to see if they want to change the questions. Include:

&#42; The deadline for finalizing questions. If they have not provided
updated questions by the deadline, use the previous cycle's questions.
&#42; The questions used in the previous cycle.

### Nomination pages {#_nomination_pages}

&#42; Update wiki pages for each election
([Council](https://fedoraproject.org/wiki/Council/Nominations),
[FESCo](https://fedoraproject.org/wiki/Development/SteeringCommittee/Nominations),
[Mindshare](https://fedoraproject.org/wiki/Mindshare/Nominations))
[EPEL](https://fedoraproject.org/wiki/Mindshare/Nominations)):
&#42;&#42; Update any references to the version &#42;&#42; Update the
list of ending terms &#42;&#42; Clear the candidates table &#42;&#42;
Remove edit protection

### Announce beginning of nomination period {#_announce_beginning_of_nomination_period}

&#42; Publish a Community Blog post with: &#42;&#42; Links to the wiki
pages &#42;&#42; Nomination deadline &#42;&#42; General information
&#42;&#42; The \'sticky\' bit set

:::: tip
::: title
:::

Copy the previous election's post with dates and versions updated. The
[F38
post](https://communityblog.fedoraproject.org/f38-election-nominations-now-open/)
is a good example.
::::

&#42; Send an email with a link to the Community Blog post and a link to
the wiki page(s) to: &#42;&#42; announce list (all elections) &#42;&#42;
devel-announce list (FESCo election) &#42; Post to Fedora Discussion
with a link to the Community Blog post and a link to the wiki page in
the: &#42;&#42; &#96;&#35;council&#96; tag (Council election) &#42;&#42;
&#96;&#35;mindshare&#96; tag (Mindshare election)

:::: tip
::: title
:::

Halfway through the nomination period, nudge the emails (only devel) and
Discussion threads to remind people of the nomination deadline.
::::

# Nomination closing SOP {#_nomination_closing_sop}

This document outlines the procedure for closing the post-release
election cycle. This covers two parallel activities: . Finalizing
questions to use in interviews . Closing the nomination period

## Timing/trigger {#_timingtrigger_18}

This process happens two weeks after the elections are
[opened](pgm_guide/sop/elections-open.xml).

## Procedure {#_procedure_4}

&#42; If the number of candidates is greater than or equal to the number
of open seats, set the nomination wiki pages to protected. Otherwise,
extend the nomination deadline *for that election only* by one week.
Repeat until the number of candidates is greater than or equal to the
number of open seats. &#42; Edit the [election banner
template](https://fedoraproject.org/wiki/Template:Election_Banner) in
the wiki to update the dates and current status &#42; Comment on the
Council, FESCo, and Mindshare Committee tickets with the final questions
that will be used. &#42; Update the &#96;templates/&#42;&#96; files in
the repo
(ssh://git@pagure.io/tickets/fedora-pgm/elections-interviews.git) with
the questions &#42; Email all candidates to inform them to submit their
interviews &#42;&#42; Interviews are submitted to the
[elections-interviews
repo](https://pagure.io/fedora-pgm/elections-interviews/issues)
&#42;&#42; Candidates who do not submit an interview by the deadline
will not be on the ballot &#42; If the Community Blog post announcing
nominations is set to \'sticky\', un-sticky it.

:::: tip
::: title
:::

As a service to candidates, send regular reminders to anyone who has not
yet submitted their interviews.
::::

# Election interview processing SOP {#_election_interview_processing_sop}

This document outlines the process for handing election interviews.

## Timing/trigger {#_timingtrigger_19}

This process occurs when a candidate submits and interview.

## Procedure {#_procedure_5}

&#42; Ensure the \'private\' box is checked on the issue. &#42;
Acknowledge the submission in the ticket. You can use the canned
response. &#42;&#42; Check if the candidate has an account in the
Community Blog. If they do not, add the &#96;login needed&#96; tag and
include the log in request in the acknowledgement. &#42; Add the
&#96;interview&#96; tag and set the milestone on the ticket. &#42; Add
the appropriate election to the \'Blocking\' field. &#42; Add the issue
link in the \'ticket\' column of the nomination wiki page.

When you are ready to add the interview to the Community Blog,

&#42; Move the issue to the Processing column on the [Interviews
board](https://pagure.io/fedora-pgm/elections-interviews/boards/Interviews).
&#42; Create the Community Blog post &#42;&#42; Include FAS account,
IRC/Matrix information, wiki page (see previous examples) &#42;&#42; Set
the candidate as the author. If the candidate has not yet logged in, use
the \'Fedora Project Community\' account. &#42;&#42; Select the public
preview option. &#42;&#42; Schedule the interview to post.
&#42;&#42;&#42; 15 minutes before the start of the voting period
(Council candidate interviews) &#42;&#42;&#42; 10 minutes before the
start of the voting period (FESCo candidate interviews) &#42;&#42;&#42;
5 minutes before the start of the voting period (Mindshare candidate
interviews) &#42; Comment on the ticket to let the candidate know the
post is available for review. Provide the public preview URL. &#42; Add
the URL in the \'interview\' column of the nomination wiki page. &#42;
Move the issue to the Ready for Review column on the [Interviews
board](https://pagure.io/fedora-pgm/elections-interviews/boards/Interviews).

# Election setup SOP {#_election_setup_sop}

This document outlines the procedures for setting up the elections.

## Timing/trigger {#_timingtrigger_20}

This process occurs the day before voting starts.

## Procedure {#_procedure_6}

In the nomination pages on the wiki, strike through any candidates that
did not submit an interview question. If the number of candidates is
less than the number of open seats, extend the deadline *for just that
election* by one week. Repeat until the number of candidates is at least
equal to the number of open seats.

### Voting setup {#_voting_setup}

The elections app runs on
[elections.fedoraproject.org](https://elections.fedoraproject.org).

&#42; maximum range: &#35; of candidates &#42; URL: link to wiki page
with nominations &#42; Admin groups: automatically includes the
elections group &#42; When adding users, add link to the interview on
Community Blog &#42; Edit the [election banner
template](https://fedoraproject.org/wiki/Template:Election_Banner) in
the wiki to update the dates and current status

:::: note
::: title
:::

FESCo elections require that the &#96;FPCA + 1&#96; box be checked in
the election setup.
::::

:::: warning
::: title
:::

Do not put any groups in the \'Legal voters groups\' unless you intend
to restrict voting to a specific group. This field is not necessary for
the regular elections.
::::

### Community Blog post {#_community_blog_post}

&#42; Create a Community Blog post that includes &#42;&#42; A link to
the Elections app &#42;&#42; Links to all candidate interviews &#42; Set
it to be sticky &#42; Schedule it to publish at the beginning of the
voting period.

### Additional announcements {#_additional_announcements}

After the Community Blog post publishes, send announcements to:

&#42; announce list (all elections) &#42; devel-announce list (FESCo
election) &#42; &#96;&#35;council&#96; tag on Discussion (Council
election) &#42; &#96;&#35;mindshare&#96; tag on Discussion (Mindshare
election)

:::: tip
::: title
:::

Halfway through the voting period, nudge the emails (only devel) and
Discussion threads to remind people of the voting deadline.
::::

# Election results SOP {#_election_results_sop}

This document outlines the process for handling election results.

## Timing/trigger {#_timingtrigger_21}

This process occurs after the voting period ends.

## Process {#_process_12}

1.  Post the results to the Community Blog

2.  Remove the embargo from the elections in the app

3.  Send results with a link to the Community Blog to the announce
    mailing list

4.  Update Pagure groups, wiki pages, mailing lists as described below

5.  Edit the [election banner
    template](https://fedoraproject.org/wiki/Template:Election_Banner)
    in the wiki to update the dates and current status

### Council {#_council}

&#42; An issue template exists for [new
members](https://pagure.io/Fedora-Council/tickets/new_issue?template=new_council_member)
and [outgoing
members](https://pagure.io/Fedora-Council/tickets/new_issue?template=outgoing_council_member).

### FESCo (Engineering) {#_fesco_engineering}

&#42; An issue template exists for [new
members](https://pagure.io/fesco/new_issue?template=new-fesco-member)
and [outgoing
members](https://pagure.io/fesco/new_issue?template=outgoing-fesco-member).

### Mindshare {#_mindshare}

&#42; Update permissions on [Mindshare GitLab
project](https://gitlab.com/groups/fedora/mindshare/-/group_members).
&#42; Update the [Mindshare members
section](https://pagure.io/mindshare/blob/master/f/website/modules/ROOT/pages/index.adoc).

:::: tip
::: title
:::

Convincing teams to give you admin access to things will make life
easier.
::::
