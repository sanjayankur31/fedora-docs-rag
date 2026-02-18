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
