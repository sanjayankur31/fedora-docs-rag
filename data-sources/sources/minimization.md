&#42; &#42;&#42;Objective&#42;&#42; = Fedora Minimization Objective

While Fedora is well suited for traditional physical/virtual
workstations and servers, it is often overlooked for use cases beyond
traditional installs.

Some modern types of deployments --- such as IoT and containers --- are
quite sensitive to size. For IoT that's usually slow data connections
(for updates/management) and for cloud and containers it's the massive
scale.

A specific example is Systemd --- while being very useful (everybody
loves Systemd) and is always present on physical systems, it is rarely
needed in containers. So it wasn't a problem for packages to require
Systemd just for *systemd-sysusers* to create users. However, in
containers, that means a significant size increase.

Besides that, basically all types of deployments benefit from a reduced
size, as there is a direct relationship between the installation
footprint and attacks surface &amp; relevant CVEs.

# Vision {#_vision}

Thousands of individual and corporate contributors collaborate in the
Fedora community to explore new problems and to build a fast-moving
modern OS with a rich ecosystem allowing them to experiment on
modernising their infrastructure.

# Mission {#_mission}

Helping open source developers, sysadmins, and Linux distribution
maintainers to focus on what's relevant for them.

# Outcomes {#_outcomes}

Fedora is a popular platform because its ecosystem is both cutting-edge
and well optimized for modern deployments such as IoT and containers.
That makes many people use Fedora rather than to build and assemble
their own artifacts directly from upstream projects. And that relieves
the pressure on open source developers caused by users who would
otherwise ask for their specific security and other issues to be fixed
quickly.

So:

&#42; Open source developers can focus on feature development &#42;
Sysadmins can easily consume pre-built bits that also get regular
updates &#42; Fedora contributors (vendors and individuals) can
collaborate within the Fedora community on exploring and developing open
source solutions to problems of the future

# Outputs {#_outputs}

Specific use cases are defined in Fedora. The community then focuses on
those use cases with development and maintenance, optimisation (like
minimisation), and testing (like CI and gating). These use cases can be
transparently prioritized for infrastructure resources based on
community interests.

Feedback Pipeline actively monitors each use case and records the size
and the dependencies required for it to run. Data history is kept and
shown to see changes over time. And to keep things small over time,
Feedback Pipeline also automatically detects size increases and
potentially automatically opens Bugzilla bugs to track/fix/justify such
increases transparently.

An active focus on minimization means that our maintainers produce
size-optimised content with the same or lower amount of effort. Tooling,
services, and data help them to make the right decision about
dependencies easily, and to keep things smaller over time.

# Actions {#_actions}

&#42;&#42;Identify relevant use cases&#42;&#42; and allow the community
(meaning not just the Minimization Team) to define their own. We think
of a use case as a set of packages installed in a specific context,
having a specific purpouse --- such as *Apache HTTP Server Container*.
Define use cases at least for:

&#42; *httpd* &#42; *nginx* &#42; *MariaDB* &#42; *PostgreSQL* &#42;
*Fedora IoT* &#42; *Python 3*

Also, consider looking at container-native use cases, such as:

&#42; *GO for container apps* &#42; *Rust for container apps* &#42;
*Quarkus*

Collect specific use cases by talking to people at tech events, internet
forums, and any other viable venues.

&#42;&#42;Extend monitoring services&#42;&#42; (Feedback Pipeline) that:

&#42; Visualize dependencies and a total size for each use case &#42;
Monitor size changes over time &#42; Auto-detect large size changes
&#42; Notifies maintainers about unexpected size increases

Other than features, we also need to:

&#42; write tests to significantly simplify contribution &#42; do
performance optimizations for the service to scale well &#42; explore
the use of CI and Rawhide Gating

Being able to see what's going on is a prerequisite of implementing any
changes. Seeing all the relevant opportunities helps us to focus on the
ones having the most impact, and a transparent tracking helps us prove
the usefulnes of our work, and to further focus on the most impactful
activities.

&#42;&#42;Minimize&#42;&#42; the installation size of the use cases by
optimizing RPM dependencies, features, software architecture, and other
factors. Specifically, look for:

&#42; Unnecessary RPM dependencies (although there probably won't be
many) &#42; Multiple implementations of the same functionality required
by various packages --- try to make them use the same one &#42;
Context-specific requirements --- such as requiring Systemd on
traditional deployments being fine vs. requiring it in containers means
significant size increases. Leverage weak dependencies in those cases
(that might require code changes). &#42; Dependnecies on large things
while only using a fraction of the functionality --- such as requiring
the whole Perl stack to run a single script --- such script can be
rewritten to Python which is everywhere mostly because of DNF

&#42;&#42;Engage with upstream developers&#42;&#42; regarding bigger
changes in packaging and architecture. An example is Systemd and
splitting the *systemd-sysuser* package.

&#42;&#42;Implement process and policy changes&#42;&#42; reflecting
bigger, more general changes. Again, a good example is using Systemd in
containers, or the general issue of creating users in containers.

&#42;&#42;Provide guidance&#42;&#42; for the Fedora community in form of
blog posts, videos, and conference talks. Even though we might have
guidelines and policies in place, spreading the word is always
important.

# Resources and Inputs {#_resources_and_inputs}

Cloud resources to prototype services. We are not going to change the
existing Fedora infrastructure in any way before whatever we develop
proves useful and worth the hustle of stabilization and changing
production.

No existing Fedora Infra or Release Engineering resources are needed at
the moment. However, we might need help with setting up (or getting
access to) the cloud resources.

Active support from our maintainers, the FPC, and other community
members is definitely needed. This is obviously not something we can
\'request\', but it's still a necessary input.

# Guiding Principles {#_guiding_principles}

&#42;&#42;Usefulness over size&#42;&#42;: There is a balance between the
usefulness and size. We take that in mind and will not implement drastic
changes that would prevent our users from using Fedora. However, nothing
prevents us from producing additional very specific and mininal
artifacts.

&#42;&#42;Using RPM&#42;&#42;: We're doing this with RPM. We're not
achieving minimization by deleting files after installation. This might
be obvious, but still worth mentioning.

&#42; &#42;&#42;Community&#42;&#42; = Contributing to Minimization

Are you interested in minimizing the installation footprint various
Fedora bits and pieces? Are you interested in contributing? Or perhaps
already working on something and want to make it more visible? Then
you're at the right place!

# What to contribute {#_what_to_contribute}

The main areas of contribution include:

## Collecting use cases and problems {#_collecting_use_cases_and_problems}

Help us make sure we work on stuff that's relevant to people. Both
Fedora users and others who might become Fedora users. Talk to people at
events, online forums, or anywhere, really. Ask them on how they run
stuff, what pain points they experience, or what would they like to see.

## Optimizing Fedora packaging {#_optimizing_fedora_packaging}

Look at the use cases and problems we've collected and see if there are
ways to minimize them by optimizing the packaging. That might include
cutting off unnecessary dependencies, switching common dependencies to a
single implementation, or even proposing policy changes about packaging.

## Working with upstream communities {#_working_with_upstream_communities}

Many changes go beyond Fedora. Are there any potential code changes that
could help us? Or anything that requires coordination upstream? Reach
out to upstream communities, offer help, build connections with the
members, and help make bigger changes.

## Developing tools and services {#_developing_tools_and_services}

Ask our maintainers and developers if there's anything in their
minimization-related workflows that could use some automation or a tool,
and help develop that. That goes for both making things smaller, as well
as keeping them small over time.

## Looking at alternative approaches {#_looking_at_alternative_approaches}

Look at other Linux distributions, repositories, container images, and
other solutions, and compare them with Fedora. Anything they do
differently? Maybe even better? What could we experiment with and learn
about?

## Promoting Minimization and Fedora {#_promoting_minimization_and_fedora}

Being visible helps us get more feedback, more contributors, and to do a
better overall progress. Write blog posts about cool things that are
happening, about interesting problems we're solving, or about examples
of using Fedora in various use cases. Submit talks at events, write on
social media, make videos, etc.

# How to join {#_how_to_join}

If you want to be a listed member of this group, please [open an
issue](https://pagure.io/minimization/new_issue), introduce yourself,
and tell us how you want to help.

But you don't need to be a formal team member to contribute. We also
welcome ocasional contributions from the whole Fedora community. Just
reach out through one of the [communication
channels](communication.xml).

# Current members {#_current_members}

Adam Samalik (asamalik) --- objective lead

Peter Robinson (pbrobinson)

Zbigniew Jędrzejewski-Szmek (zbyszek)

Felipe Borges (feborges)

Neal Gompa (ngompa)

Christian Glombek (lorbus)

Michel Alexandre Salim (salimma)

Troy Dawson (tdawson)

Igor Gnatenko (ignatenkobrain)

Jun Aruga (jaruga)

# Discussing &amp; Tracking Minimization {#_discussing_amp_tracking_minimization}

&#42;&#42;Instant messaging&#42;&#42;

:   IRC &#35;fedora-devel at FreeNode is the default channel to discuss
    things live.

&#42;&#42;Mailing list&#42;&#42;

:   [Fedora Devel mailing
    list](https://lists.fedoraproject.org/admin/lists/devel.lists.fedoraproject.org/).
    This list is used to discuss many other technical topic in Fedora,
    and therefore has a large audience. That's why we use it to discuss
    larger topics that require broader attention.

&#42;&#42;Issue tracker&#42;&#42;

:   [Minimization issue tracker](https://pagure.io/minimization/issues)
    on Pagure. The idea behind this tracker is to keep track of things
    we're looking at or want to look at.

&#42;&#42;Fedora package changes&#42;&#42;

:   [Tracker bug
    1734342](https://bugzilla.redhat.com/show_bug.cgi?id=1734342) in
    Bugzilla. We block this bug with other bugs that are relevant to the
    effort. That way we can see what's going on.

Minimization is not completely centralized effort --- work is happening
(and is discussed and tracked) at many different places such as upstream
issue trackers, mailing lists, forums, meetings, etc. Many of those
referenced in in our Minimization issue tracker.

&#42; &#42;&#42;Progress&#42;&#42; = Action Plan for Minimization

This is a short-term action plan for the Minimization effort. The
objective is in an early stage and doesn't have a proper tracker, yet.
At this time, everything is tracked at and reported back to this space
in Fedora Docs.

There are four main focus areas at this moment:

1.  &#42;&#42;Prototyping tools&#42;&#42; &#42;&#42; Developing (or
    documenting existing) tools that help with exploration and analysis.

2.  &#42;&#42;Ecosystems exploration&#42;&#42; &#42;&#42; Identifying
    specific use cases (specific package installations) to optimize.
    Comparing Fedora with other ecosystems for reference.

3.  &#42;&#42;Use case analysis&#42;&#42; &#42;&#42; Digging into
    dependency trees of specific use cases (specific package
    installations), and finding ways for potential minimization.

4.  &#42;&#42;Content strategy&#42;&#42; &#42;&#42; Defining an
    effective way to let the world know about the cool things we do!

## Prototyping tools {#_prototyping_tools}

[&#42;&#42;Issue tracker: Prototyping
Tools&#42;&#42;](https://pagure.io/minimization/issues?status=Open&amp;tags=Focus+Area%3A+Prototyping+Tools&amp;close_status=)

Developing (or documenting existing) tools that help with exploration
and analysis.

Two main classes:

&#42; &#42;&#42;Use case analysis&#42;&#42; --- Tools that help with
looking at specific use cases installed in various context such as an
empty root, the Fedora base container image, or the \'Fedora Minimal\'
installation, and finding ways how to optimize the size. Visualising the
dependency tree, showing sizes of various parts, offering alternative
packages as dependencies from the Fedora repos and showing the impact of
choosing an alternative, potentially even showing dependencies on the
file level and suggesting package splits in cases a tiny portion of an
otherwise large package is used as a dependency, etc. &#42;
&#42;&#42;Monitoring and feedback&#42;&#42; --- Monitoring the sizes of
relevant use cases over time as new versions of packages are built,
reporting potential size increases. Also monitoring for specific
dependencies that have been removed in the past but could come back, and
reporting those.

## Ecosystems exploration {#_ecosystems_exploration}

[&#42;&#42;Issue Tracker: Ecosystems
Exploration&#42;&#42;](https://pagure.io/minimization/issues?status=Open&amp;tags=Focus+Area%3A+Ecosystems+Exploration&amp;close_status=)

Identifying specific use cases (specific package installations) to
optimize. Comparing Fedora with other ecosystems for reference.

Talking to other groups in Fedora such as
[IoT](https://docs.fedoraproject.org/en-US/iot/) and finding what use
cases are relevant for them to minimize, what their goals are, and
helping them with minimization.

There are also many different ecosystems other than Fedora --- other
linux distributions, various container images, etc. We'll look at those
to compare what sizes and features are available in the universe. This
will help us get a better idea about where we stand, and what our goal
should be.

## Use case analysis {#_use_case_analysis}

[&#42;&#42;Issue Tracker: Use Case
Analysis&#42;&#42;](https://pagure.io/minimization/issues?status=Open&amp;tags=Focus+Area%3A+Use+Case+Analysis&amp;close_status=)

Digging into dependency trees of specific use cases (specific package
installations), and finding ways for potential minimization.

Important part of this will be working closely together with the
maintainers as they are the subject matter experts.

## Content strategy {#_content_strategy}

[&#42;&#42;Issue Tracker: Content
Strategy&#42;&#42;](https://pagure.io/minimization/issues?status=Open&amp;tags=Focus+Area%3A+Content+Strategy&amp;close_status=)

Keeping the world up-to-date about our efforts is an essential part of
this objective. We need to have a simple content strategy to make sure
that there is information flowing consistently.

We need to consider readers with various amouts of time and levels of
interest.

# Tools &amp; Services for Minimization {#_tools_amp_services_for_minimization}

## Feedback Pipeline service {#_feedback_pipeline_service}

Reporting and notifications regarding dependencies and sizes of defined
RPM installations.

[&#42;&#42;minimization.github.io/reports&#42;&#42;](https://minimization.github.io/reports/)

## rpm-showme tool {#_rpm_showme_tool}

Dependency visualisation of an RPM-based installation (a system, an
image, etc.)

Source: <https://pagure.io/minimization/rpm-showme>

The script takes a file path or a container image name as an input, and
generates a graph of packages and their relations including sizes of all
individual packages and some basic clustering. Clicking on a package
highlights its relations to other packages.

# Discoveries {#_discoveries}

This page contains random discoveries that we make. We'll bring some
structure to this page as we go.

## Techniques {#_techniques}

### dnf {#_dnf}

&#42; \--nodocs or \--setopt=tsflags=nodocs &#42;&#42; Average shrink is
5 to 10M &#42; \--setopt=install_weak_deps=false &#42;&#42; Depending on
the package could shrink alot, could shrink nothing &#42;&#42; Can
remove some functionality &#42; install glibc-minimal-langpack
&lt;package(s)&gt; &#42;&#42; Average shrink is 200M &#42;&#42; Can
remove some language based functionality

## Packages {#_packages}

These headings can/should be changed. They are what they currently are
just for placeholders.

### Investigating Minimization {#_investigating_minimization}

&#42; httpd &#42;&#42; Remove systemd from main package &#42;&#42;
<https://src.fedoraproject.org/rpms/httpd/pull-request/7>
&#42;&#42;&#42; /usr/sbin/apachectl requires /usr/bin/systemctl so this
will require some package/subpackage shuffling. &#42; nginx &#42;&#42;
Remove systemd from main package &#42;&#42;
<https://src.fedoraproject.org/rpms/httpd/pull-request/5> &#42; mariadb
&#42;&#42; Drop perl ? &#42;&#42;&#42; The two perl scripts in mariadb
(mysqlaccess and mysql_find_rows) and might be considered being moved to
a sub-package -client-utils, similiar to the perl scripts in
-server-utils. &#42;&#42; Drop systemd ? &#42;&#42;&#42; The mariadb
containers start with run-mysqld. systemd is not involved at all.
&#42;&#42; <https://bugzilla.redhat.com/show_bug.cgi?id=1753696> &#42;
postgresql &#42;&#42; Drop systemd ? &#42; systemd &#42;&#42; Can we
pull it out of more package dependencies &#42;&#42;
<https://pagure.io/minimization/issue/2> &#42;&#42; Systemd is in all
Fedora containers due to a bug in anaconda. Although the bug has been
fixed, updating the koji image builders still hasn't happened. &#42;
polkit &#42;&#42; Currently depends on mozjs60 &#42;&#42;&#42; It's
rather large, (25M - 30M) can it be removed from some package
dependencies ? &#42;&#42;&#42; Possibly use duktape instead of mozjs
&#42;&#42;&#42; Request for information has been sent out, no replies
yet. &#42; perl &#42;&#42; It's rather large, can it be removed from
some package dependencies ?

### Finished Investigation {#_finished_investigation}

&#42; dnf \[changed\] &#42;&#42; removed systemd as a dependency.
Dropped container size by 30M. &#42; anaconda-core \[not-changed\]
&#42;&#42; Can we shift flatpack-libs dependency to anaconda-gui ?
&#42;&#42; <https://src.fedoraproject.org/rpms/anaconda/pull-request/5>
&#42;&#42;&#42; No, it needs to be where it is.

## External Articles {#_external_articles}

&#42; Building tiny container images:
<https://opensource.com/article/18/7/building-container-images> &#42;
Creating small containers with Buildah:
<https://opensource.com/article/18/5/containers-buildah> &#42; Buildah
images not so small?: <https://github.com/containers/buildah/issues/532>

# Minimization Objective Status {#_minimization_objective_status}

## Updates on the Devel list {#_updates_on_the_devel_list}

Regular updates are posted to the [Fedora Devel mailing
list](https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/):

&#42; [Friday, 15 November
2019](https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/N6LGANSTRGWU5I7NDDRFAEBDTDEL32A3/)
&#42; [Wednesday, 30 October
2019](https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/SRNQMG2XCXXPEYGZ3QUDS6UF67T2ZLJU/)
&#42; [Thursday, 3 October
2019](https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/DBLD5XO52YVEYRLZR6NQJHTMCNO5GGN2/)
&#42; [Wednesday, 25 September
2019](https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/DNGGW7QCWXQACVTJDMLHTQRR53LXRROX/)
&#42; [Wednesday, 18 September
2019](https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/74RI2KYXCPS7GU52GPZDSNRQ535QLFNC/)
&#42; [Wednesday, 11 September
2019](https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/ANW4DMWWDH3XKBQYAAQ34GVH6IKACZQZ/)
&#42; [Wednesday, 4 September
2019](https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/N34HGDSMQWNTXOJVDT7CPNCNKONQNZ74/)
&#42; [Wednesday, 28 August
2019](https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/WSIWZOAOY5QM23G4AP5ITIIA7I7I3Q5M/)
&#42; [Wednesday, 21 August
2019](https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/2QB42MDK354LWI44BRCQHRXUB6B6QCNX/)
&#42; [Friday, 2 August
2019](https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/QIX5LJJF4X6HKZXOQMKEIORRTK7ZIAN7/)

## First Phase Accomplishments {#_first_phase_accomplishments}

See the [status
page](https://docs.fedoraproject.org/en-US/minimization/status/) for
detailed info and historic weekly updates. Summary below.

&#42;&#42;Better understanding&#42;&#42; --- Yes, we now have much
better understanding of the problem and a better, more specific idea
about the next steps.

[&#42;&#42;Feedback
Pipeline&#42;&#42;](https://minimization.github.io/reports/) --- A
service that monitors use cases for size and dependencies. Includes
various views in tables and interactive dependency graphs.

&#42;&#42;Systemd and containers&#42;&#42; --- We dag into the issue of
Systemd vs. containers, especially for packages requiring it just to
create users in containers using *systemd-sysuser*. Working with
upstream on splitting the package out. Thought about, but not yet
proposed, a wider policy around this.

&#42; Mailing list discussion:
<https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/6YX6CEFBPU3XVZZEHTN6CBH2F7JDF35N/&#35;EJD4BNBE52JTEOPKAT6HFOO4HVUPBTCH>
&#42; Ticket: <https://pagure.io/minimization/issue/13>

Policy thinking:

&#42; A - If systemd is only needed to start services, a package should
only \'Recommend\' systemd. This will allow containers to install the
package without systemd. &#42; B - If a program is just using a library
of systemd, only require systemd-libs. Example: libusb &#42; C - If a
package wants to use systemd-sysusers to create users/groups, only
require systemd-sysusers. (NOTE: This subpackage isn't implemented yet)

&#42;&#42;initial-setup&#42;&#42; --- If an image is built without
users, there needs to be some way to add a user at startup.
initial-setup does a good job of that, but at the expense of size. It
pulls in anaconda-tui and anaconda-core. Those two packages then
commence to pull in alot of other, rather large, packages. This is for
the IoT images, as well as others. We currently do not have a
recommendation, but it is being worked on.

&#42;&#42;Use pcre2 instead of pcre&#42;&#42; --- The minimization
effort is trying to trim things down to just one pcre, and that is
pcre2.

&#42;&#42;Polkit and mozjs60&#42;&#42; --- Let's expain this one with a
terrible analogy! Polkit is this lovely person (.5M) that rings your
doorbell and says they will wash the windows of your house. After you
agree, they bring out their elephant (mozjs60 30M) and use it to spray
your windows with water. Polkit pulls in mozjs60, which is a rather
large package. So, we're trying to sort this one out, too.
