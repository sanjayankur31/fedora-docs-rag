# Steps {#_steps}

1.  Pick a document to update. You can find documents needing updates in
    the \[filename\]&#96;modules/ROOT/nav.adoc&#96; file. They are on
    the commented-out lines (those that start with a &#96;//FIXME&#96;).

2.  Fork the <https://pagure.io/fedora-docs/quick-docs> repo.

3.  Make your changes to the &#96;.adoc&#96; file you want to improve.

4.  Uncomment the file in \[filename\]&#96;nav.adoc&#96; remove the
    &#96;FIXME&#96; from the xref..

5.  [Build a local
    preview](fedora-docs:ROOT:contributing-docs/tools-localenv-preview.xml)
    to ensure your changes look the way you intended: Make sure you
    either have &#42;Podman&#42; or &#42;Docker&#42; installed, On a
    Linux desktop run &#96;./docsbuilder.sh&#96;. On macOS run either
    &#96;./docsbuilder.sh -p&#96; or &#96;./preview.sh&#96;. Follow
    instructions printed on the command line.

6.  When you are satisfied with your updates, submit a pull request with
    your improvements.

7.  If migrating a wiki page, create a redirect on the old page --- see
    below.

# Possible Source Material {#_possible_source_material}

Perhaps you just want to improve an existing document, in which case the
above is all you need. Or maybe you already have something in mind. But
if you are interested in helping but don't know where to start, here are
some places to look for ideas:

&#42; The old [How To
category](https://fedoraproject.org/wiki/Category:How_to) on the Fedora
wiki. Many of those documents are ripe for conversion. (Many are also
very out of date!) &#42; [Common
Issues](https://discussion.fedoraproject.org/c/ask/common-issues/82/none?solved=yes)
questions on Ask Fedora. &#42; Frequent [Fedora questions on Stack
Exchange](https://unix.stackexchange.com/questions/tagged/fedora?sort=frequent&amp;pageSize=50).
&#42; [Fedora Magazine](https://fedoramagazine.org) articles. The
magazine format is conversational, and understood to represent a moment
in time. Quick Docs versions should be more to-the-point, and kept
updated if commands or best practices change.

# Wiki Redirects {#_wiki_redirects}

Usually, wikis do not allow redirects to external sites, because the
potential for abuse is very high. We've developed a plugin for the
Fedora Wiki which allows redirects to *only* pages on this site,
<https://docs.fedoraproject.org/>. To create such a link, use the
&#96;&#35;fedoradocs&#96; macro by putting something like this at the
top of the wiki page you are replacing:

``` mediawiki
{{\&#35;fedoradocs: https://docs.fedoraproject.org/en-US/council/fpl/}}
```

Of course, you should to replace that example URL with the one for your
new target page. Again, the URL can't be something arbitrary it *must*
begin with &#96;<https://docs.fedoraproject.org/&#96>;.

Once the redirect is in place, visitors to that wiki page will be
instantly whisked (well, redirected, with the code &#96;301 Moved
Permanently&#96;) to the docs site.

Note that there is no validation that the target exists or is correct
--- please double-check that any redirects you create work properly
before moving on.

If you need to edit such a page to correct the URL, or to remove the
redirect for some reason, construct a wiki site URL with
&#96;&amp;action=edit&#96;, like:

    https://fedoraproject.org/w/index.php?title=Project_Leader\&amp;action=edit

# Getting started with Fedora {#_getting_started_with_fedora}

Petr Bokoc ; Ooyama Yosiyuki; Liam Coogan :experimental:

> The Fedora Project is a community of people working together to build
> a free and open source software platform and to collaborate on and
> share user-focused solutions built on that platform. Or, in plain
> English, we make an operating system, and we make it easy for you to
> do useful stuff with it.

Actually, we produce several operating systems, or editions anyway. The
one that you're most likely interested in, and the one that we'll be
focusing on, is &#42;&#42;Fedora Workstation&#42;&#42;. Fedora
Workstation has a wide range of software that's suitable for almost
anyone. You can use it for home use like browsing the Web, watching
streaming video, editing photos, and playing games. You can use it for
work creating documents, crunching numbers in spreadsheets, or
programming.

All of the software provided with Fedora is open source and free to
download and use. You can even modify it and distribute it yourself, if
you want---but that's beyond the scope of this guide. We're just going
to focus on the new user experience and some \'day two\' stuff so you
can acclimate to Fedora and start being productive right away.

## Who this document is for {#_who_this_document_is_for}

This document is for folks new to Fedora Workstation, or who've been
using it a while and would like to get a little more background and tips
on how to make the most of Fedora Workstation. We're focusing on desktop
use and common tasks like web browsing, streaming media, editing photos
or audio, and all kinds of productivity tasks that you may want to
tackle with your desktop or laptop computer. Typical daily computer
usage, you might say.

## What's a Linux distribution? {#_whats_a_linux_distribution}

Fedora Workstation is a Linux distribution, an operating system with the
Linux kernel at its core plus the software you need to install it,
manage it, and the applications that you want to use for daily work.

Fedora is one of many Linux distributions, and includes a lot of
software you'll find in many Linux distributions. For example, the
&#42;GNOME&#42; desktop environment, and the
\[application\]&#42;Firefox&#42; web browser,
\[application\]&#42;LibreOffice&#42; office suite, and a lot of
&#42;&#42;GNU utilities&#42;&#42; and so much more.

## Understanding Linux {#_understanding_linux}

Linux is very different from other operating systems, such as Microsoft
Windows, the leading desktop OS. This section explains concepts about
Linux and how it works, which help make it clear, for example, why Linux
asks for various passwords.

### Root {#_root}

By default Linux creates the &#96;root&#96; user account. It is the
highest level account on the system and is used for administration. It
gives the user full permission to modify files, and start and stop
critical programs (called processes) on the system. It is a security
feature in Linux that limits normal user privileges only to those
required for normal tasks.

For security reasons, the root account is disabled by default on Fedora
Workstation. Instead, the default user will be added to the group
\'wheel\'. Members of this group are able to acquire root permissions
using the \'sudo\' command. Whenever this user wants to make a
system-wide change, such as stopping a fundamental program like the web
server (httpd), the corresponding command is preceded by a sudo, e.g.
&#96;sudo systemctl stop httpd&#96;. The sudo then asks for the password
of the user, not of root.

### The command line/terminal {#_the_command_lineterminal}

Use the \[application\]&#42;Terminal&#42; program to perform command
line tasks. Benefits to using the command line include the ability to
give multiple commands on one line, but it requires greater knowledge of
Linux commands. Documentation published on this site, as well as various
tutorials and guides on the internet and elsewhere, often makes use of
these terminal commands.

## First impressions {#_first_impressions}

### GNOME {#_gnome}

\[application\]&#42;GNOME&#42;, Fedora's default *window manager*, is
the underlying graphical user environment. It provides a visual
front-end using a desktop analogy. When you log into Fedora, GNOME is
started with a predefined set of icons and menus on the desktop.

### The internet {#_the_internet}

Mozilla \[application\]&#42;Firefox&#42; is the default web browsing
application. It is accessed through menu:Activities\[Firefox\]. Firefox
is also available on other platforms such as Microsoft Windows and Mac
OS X.

### E-mail {#_e_mail}

There is no longer a default email client bundled with Fedora, but you
can install one by searching in menu:Software\[\].

You can choose \[application\]&#42;Evolution&#42;. Use it to access
e-mail, organize contacts, manage tasks, and schedule calendars.
Evolution is similar in functionality to Microsoft Outlook.

Another choice for an email client is
\[application\]&#42;Thunderbird&#42;, developed by the Mozilla
Foundation. It is a popular email client on multiple operating systems.
It is used for handling email and newsgroups without the calendaring
functions that Evolution provides.

### Instant messaging {#_instant_messaging}

The \[application\]&#42;Pidgin&#42; application is popularly used for
instant messaging. The instant messaging protocols that Pidgin supports
include MSN, AIM, IRC, and Yahoo. You can install Pidgin using
menu:Software\[\].

### Music &amp; audio {#_music_amp_audio}

Fedora provides built-in support for sound cards and playing music CDs.
Applications to import audio from CDs and manage music files are
available. Extracting audio from CDs and storing it in compressed format
on the hard drive is one way to manage a music collection.

To extract, or *rip*, the music from a CD, use the
\[application\]&#42;Sound Juicer&#42; program. You can install it by
searching for \'Sound Juicer\' in menu:Software\[\]. By default, Sound
Juicer encodes music files to the free and open OGG Vorbis format. Once
music files are generated, use \[application\]&#42;Rhythmbox&#42; to
manage and play tracks. In addition to playing audio file formats,
Rhythmbox is also used for streaming media from Internet radio stations.

### Productivity tools {#_productivity_tools}

The office suite included by default in Fedora is
\[application\]&#42;LibreOffice&#42;, a well-known and mature collection
of software. LibreOffice, includes a word processor
(\[application\]&#42;Write&#42;), a spreadsheet program
(\[application\]&#42;Calc&#42;), and presentation software
(\[application\]&#42;Impress&#42;). A simple image editing package
(\[application\]&#42;Draw&#42;) and a relational database
(\[application\]&#42;Base&#42;) are also available for optional
installation.

## Moving further {#_moving_further}

&#42; Configuring an internet connection the battery icon in the top
right corner of the screen, then selecting menu:Settings\[Network\]
&#42; Configuring graphics cards / video drivers

## Cool things to do with Fedora {#_cool_things_to_do_with_fedora}

&#42; \[application\]&#42;Linphone&#42; - demonstrates installing from
Extras, and free phone calls. Requires: headset. &#42;
\[application\]&#42;GnuCash&#42; - installs from &#96;Core&#96;, home
finance software isn't cool, but is important.

# How to file a bug {#_how_to_file_a_bug}

Ankur Sinha; Joe Walker :page-aliases: howto-file-a-bug.adoc

> The purpose of this document is to give step by step instructions on
> filing bugs in Fedora. For more information about using Bugzilla, see
> the [Bugs section](bugzilla/index.xml) of the Quick Docs.

A software bug does not necessarily need to be a software crash. Any
undesired behaviour in software can be filed as a bug. The package
maintainer can then look at the bug report and decide the best course of
action.

:::: tip
::: title
:::

&#42;Anyone can file bugs&#42;: All users are encouraged to file any
bugs they run into. Bug filing is not limited to only software
developers.
::::

## Terminology {#_terminology}

There are a few terms that are commonly used in this document:

&#42; &#42;Bug&#42;: A bug is any behaviour in a software that appears
unexpected/undesired. &#42; &#42;Bug tracker&#42;: The Fedora bug
tracking system at <https://bugzilla.redhat.com>. &#42;
&#42;Package&#42;: Each software that is available in Fedora has a
formal package name that is used by the bug tracker and other
infrastructure tools. Packages can be searched using the [Fedora
dist-git](https://src.fedoraproject.org/). &#42; &#42;Maintainer&#42;: A
body of volunteers that takes care of the software packages provided in
Fedora. These are referred to as \'package maintainers\'. They keep
track of bugs, help with issues, and generally act as middlemen between
the developers of the software and Fedora users. &#42; &#42;QA&#42;:
Quality assurance is the process of ensuring that the software works as
intended. &#42; &#42;Bodhi&#42;: The [Fedora QA Web
Application](https://bodhi.fedoraproject.org).

## Before filing a bug {#_before_filing_a_bug}

[Ask Fedora](https://ask.fedoraproject.org) --- the community support
forum --- is a good place to start if you're not sure if you've
encountered a bug. Sometimes what is perceived as a bug is a
misunderstanding or a question. The Ask Fedora community can help you
figure out if you've encountered a bug --- and if it's specific to
Fedora or is in the upstream package.

### Step 0: Check the Common Issues page {#_step_0_check_the_common_issues_page}

We maintain a list of common issues. Check this site first to see if
your issue has been reported --- and if a solution exists.

&#42; [Fedora Linux 43](https://fedoraproject.org/wiki/Common_F43_bugs)
&#42; [Fedora Linux 42](https://fedoraproject.org/wiki/Common_F42_bugs)
&#42; [Ask Fedora
listing](https://discussion.fedoraproject.org/c/ask/common-issues/82/all)

### Step 1: Check for the latest version {#_step_1_check_for_the_latest_version}

As bugs are reported and fixed, developers collect a set of fixes and
periodically release improved versions of their software. So, before
reporting an issue, it is useful to check if you are using the latest
version of a software. The simplest way to get the latest version of
software in Fedora is to regularly update your system. Users of
Gnome/KDE and other desktop environments can use their default
applications to do so. These periodically check for updates and notify
users. You can also use the default package manager &#96;dnf&#96; to
check and update your system. Only users with administrator privileges
can do so:

\$ sudo dnf upgrade \--refresh

### Step 2: Check for already filed bugs {#_step_2_check_for_already_filed_bugs}

If you are using the latest version of the software available in Fedora,
then it is likely that the bug has either not been reported, or has been
reported but a fix has not yet been released. So, it is useful to search
the list of already reported bugs before filing a new report. The
[Fedora Packages Web application](https://packages.fedoraproject.org/)
provides a link the open bugs for a package. There is also a convenient
shortcut that can be used.

<https://bugz.fedoraproject.org/&lt;package> name&gt;

Here, the &#96;package name&#96; must be the formal name of the package.

:::: tip
::: title
:::

&#42;Finding the name of the package&#42;: If you do not know the formal
package name of the software, you can use the [Fedora Packages Web
Application](https://packages.fedoraproject.org/) to search for it and
view the list of bugs there.
::::

<figure>
<img src="20180825-how-to-file-a-bug-gs.png"
alt="20180825 how to file a bug gs" />
<figcaption>Searching the Fedora Packages Web Application for Gnome
Software.</figcaption>
</figure>

:::: note
::: title
:::

&#42;Advanced searching&#42;: You can also use the [advanced search
features of the bug tracker](https://bugzilla.redhat.com/query.cgi) to
narrow down your search. However, this is not necessary.
::::

If a bug report has already been filed describing the issue, you should
provide any extra information you may have. If there is nothing more to
add to the report, you should \'CC\' (carbon-copy) yourself to the
report to receive any updates. This can be done by clicking on the
\'Save changes\' button when the \'Add me to CC list\' option is checked
as shown below:

<figure>
<img src="20180825-how-to-file-a-bug-cc-list.png"
alt="20180825 how to file a bug cc list" />
<figcaption>The CC list contains all users that should be notified when
any updates are made to the report.</figcaption>
</figure>

## Filing a bug report {#_filing_a_bug_report}

### Step 0: Create a Bugzilla account {#_step_0_create_a_bugzilla_account}

Bugs are filed on [Bugzilla](https://bugzilla.redhat.com) and you must
have a [Bugzilla account](https://bugzilla.redhat.com/createaccount.cgi)
to file bugs and interact with them. Once you have created an account on
Bugzilla, you can also login using your [Fedora
account](https://accounts.fedoraproject.org). To use your FAS account to
login to Bugzilla, you need to either use the same e-mail address on FAS
and on Bugzilla, or if they differ, you can set the Bugzilla e-mail
address in your FAS profile explicitly.

The bug tracker will only send e-mail notifications about bugs that a
user is involved in. No other e-mails will be sent.

### Step 1: Filing a new bug {#_step_1_filing_a_new_bug}

If a bug report for the particular issue has not already been filed, you
should file a new one. The easiest way to file a new report is to look
up the package in the [Fedora Packages Web
application](https://packages.fedoraproject.org/), and use the \'File a
new bug report\' link provided on the page.

<figure>
<img src="20240118-how-to-file-a-bug-new-bug-shortcut.png"
alt="20240118 how to file a bug new bug shortcut" />
<figcaption>The Fedora Packages Web Application provides a convenient
shortcut to file new bugs.</figcaption>
</figure>

This redirects to a new bug report template on the bug tracker. The
image below shows a new bug template:

<figure>
<img src="20180825-how-to-file-a-bug-new-bug.png"
alt="20180825 how to file a bug new bug" />
<figcaption>A new bug report template.</figcaption>
</figure>

The following fields need to be set:

&#42; &#42;Component&#42;: This will be set to the name of the package.
&#42; &#42;Version&#42;: You should set this to the version of Fedora
that you observed the bug on. &#42; &#42;Summary&#42;: You should
provide a useful short summary of the issue here. &#42;
&#42;Description&#42;: More detailed information about the issue should
be provided here. It already contains a template, which is explained
below. &#42; &#42;Attachment&#42;: Files that provide more information
of the issue can be uploaded with the bug report using the button here.
E.g,, screen-shots, log files, screen recordings. &#42; &#42;Severity,
Hardware, OS&#42;: These fields are optional and need not be set.

&#42;Description of problem:&#42;

Explain the issue in more detail here.

&#42;Version-Release number of selected component (if applicable):&#42;

The version of the package should be specified here. Once the package
name is known, the version can be obtained by using the &#96;rpm&#96;
command:

\$ rpm -q &lt;packagename&gt;

For example:

\$ rpm -q gnome-software gnome-software-3.28.2-1.fc28.x86_64

&#42;How reproducible:&#42;

How often is the issue observed? Usually, a good answer to this field is
one of:

&#42; Always: the issue is observed each time. &#42; Sometimes: the
issue occurs, but not each time. &#42; Only once: the issue was only
observed once.

Issues that occur always are easiest for developers to diagnose, since
they may also be able to replicate it on their machines to collect more
information. If an issue only happens sometimes, developers must spend
more time and effort to understand what causes the problem. If an issue
was only observed once, it is even harder to debug.

:::: tip
::: title
:::

&#42;Detailed bug reports make bugs easier to fix&#42;: If possible, you
should try to investigate what steps cause the issue to happen and
provide these steps in the next section:
::::

:::: tip
::: title
:::

&#42;Submit a report even if unsure&#42;: If you aren't sure of what to
fill in, you should still submit the bug report. Maintainers can follow
up with questions to gather more information.
::::

&#42;Steps to Reproduce:&#42;

These enable other users to verify the bug, and they also inform the
developers of what specific steps cause the issue. It makes it much
easier for them to look at the source code and pick out the bits that
may be faulty.

&#42;Actual results:&#42;

What is observed when the issue occurs?

&#42;Expected results:&#42;

What does the user expect that should happen if the software behaved
correctly?

&#42;Additional info:&#42;

Any additional information that may be useful to the maintainer should
be added here.

### Step 2: Follow up on filed reports {#_step_2_follow_up_on_filed_reports}

After a bug has been filed, you should keep an eye out for any updates.
The [bug status workflow](package-maintainers::bug_status.xml)
documentation describes the different statuses a bug may have. An e-mail
notification of any new comments to the report will be sent to everyone
involved in the bug report\-\--the reporter, other users, and the
maintainer. Often, maintainers will comment with queries to gather more
information on the issue. Sometimes other users that experience the same
issue may also add more information.

:::: tip
::: title
:::

&#42;Ask for instructions&#42;: If the maintainers ask for more
information but it is unclear how it should be gathered, it is perfectly
OK to ask the maintainers for explicit instructions.
::::

:::: tip
::: title
:::

&#42;E-mail notifications&#42;: The notifications are sent from
<bugzilla@redhat.com>. You should keep an eye out for e-mails from this
address, and add it to your \'no-spam\' lists.
::::

### Step 3: Test updates {#_step_3_test_updates}

A well reported bug will often be fixed, and the maintainer will make an
improved version of the software available to Fedora users. Bodhi will
add a comment to the report when this happens. You can help the
maintainer by confirming if the improved version works better in the
Bodhi.

<figure>
<img src="20180825-how-to-file-a-bug-qa.png"
alt="20180825 how to file a bug qa" />
<figcaption>Bodhi Application adds comments informing users of an update
that should fix the bug.</figcaption>
</figure>

:::: tip
::: title
:::

&#42;Help test updates&#42;: All users can help by testing new versions
of software. More information on this can be found
[here](https://fedoraproject.org/wiki/QA:Updates_Testing). Note that
this requires a [Fedora
account](https://admin.fedoraproject.org/accounts/).
::::

Once the improved version of the software has passed the QA process, the
bug will automatically be closed. Congratulations!

## Advice for specific bug types {#_advice_for_specific_bug_types}

### Crashes {#_crashes}

If you have experienced a program crash, it will almost certainly be
necessary to include a stack trace with your bug report. Crashes are
often difficult to reproduce and even more difficult to fix, so the more
information you can provide, the better. You will probably need to
install -debuginfo RPMs so your stack trace will have useful debugging
symbols. See the following pages for more information:

&#42; [Stack traces](https://fedoraproject.org/wiki/StackTraces) &#42;
[Java stack traces](https://fedoraproject.org/wiki/Java/StackTraces)

### Enhancement Requests {#_enhancement_requests}

:::: tip
::: title
:::

&#42;Most enhancement requests should be filed upstream.&#42; If the
software is missing a feature you think it should have, you generally
want to file that in the upstream project's bug tracker. Feature
requests in Fedora Linux are generally changing defaults, enabling
disabled-by-default features, etc.
::::

&#42; When filing an enhancement request in Bugzilla, add the keyword
&#96;Future Feature&#96; to the report. The Keyword should be added
right after submitting the bug. You will see the Keyword input box then.
Make sure you supply enough information and rationale for your
enhancement requests to be considered. &#42; The Fedora Project has the
objective to be a platform built exclusively from free and open-source
software. Suggestions to include support for proprietary or other
legally encumbered software is not constructive. See the list of
[forbidden items](https://fedoraproject.org/wiki/Forbidden_items) page
for details about this. &#42; If you want to make a new feature happen
on your own create a wiki page for your feature and get it accepted. See
more on the [Changes Process](program_management::changes_policy.xml).
&#42; Requests for new packages to be added to Fedora should not be
filed in Bugzilla.

### Graphical User Interfaces {#_graphical_user_interfaces}

If you are having trouble with a graphical user interface (GUI), it
often helps to include a screenshot or a screencast showing the bug in
action. This helps developers find the exact place in the code which is
causing the bug, and helps communicate what is going wrong when it is
difficult to reproduce (for example, machine-specific layout problems).

### Hardware-Specific Bugs {#_hardware_specific_bugs}

A strong indication of a hardware-specific bug is that other people with
different hardware should be able to reproduce the bug, but can't. They
also usually involve code that specifically interacts with a peripheral,
such a webcam, video card, printer, or sound card (so for instance, it
is uncommon for bugs affecting the user interface of a word processor or
desktop calculator to be hardware-specific).

If you suspect your bug has something to do with the specific hardware
you have, it will be necessary to identify the hardware so targeted
action can be taken.

PCI and PCI-E devices found by the kernel can be listed with
&#96;lspci&#96;.

USB devices found by the kernel can be listed with &#96;lsusb&#96;.

You may also find mention of specific devices or drivers in your system
logs (run &#96;journalctl&#96;).

### Security-Sensitive {#_security_sensitive}

We pay special attention to security-sensitive bugs. Read the [Reporting
a Security
Vulnerability](https://fedoraproject.org/wiki/Security_Bugs&#35;Reporting_a_Security_Vulnerability)
page to understand the special process of opening a security bug.

## Information required for bugs in specific components {#_information_required_for_bugs_in_specific_components}

&#42; [Anaconda
(installer)](https://fedoraproject.org/wiki/How_to_debug_installation_problems)
&#42;
[Dracut](https://fedoraproject.org/wiki/How_to_debug_Dracut_problems)
&#42;
[Firefox](https://fedoraproject.org/wiki/How_to_debug_Firefox_problems)
&#42; [Fonts](https://fedoraproject.org/wiki/Category:Fonts_and_text_QA)
&#42; [Kernel](https://fedoraproject.org/wiki/KernelBugTriage)
&#42;&#42;
[Sound](https://fedoraproject.org/wiki/How_to_debug_sound_problems)
&#42;
[Printing](https://fedoraproject.org/wiki/How_to_debug_printing_problems)
&#42; [SELinux](https://fedoraproject.org/wiki/SELinux/Troubleshooting)
&#42;
[Systemd](https://fedoraproject.org/wiki/How_to_debug_Systemd_problems)
&#42;
[Virtualization](https://fedoraproject.org/wiki/How_to_debug_Virtualization_problems)
&#42;&#42; [QEMU](https://fedoraproject.org/wiki/How_to_use_qemu) &#42;
[Wayland](https://fedoraproject.org/wiki/How_to_debug_Wayland_problems)
&#42; [X.org](https://fedoraproject.org/wiki/How_to_debug_Xorg_problems)

## More reading {#_more_reading}

These are some more resources for those looking to report better bugs by
providing more information:

&#42; [Bugzilla etiquette: how to be polite in bug related conversations
on the bug
tracker](https://bugzilla.mozilla.org/page.cgi?id=etiquette.html). &#42;
[A general introduction on how to file good bugs (available in multiple
languages)](https://www.chiark.greenend.org.uk/~sgtatham/bugs.html).
&#42; [An introduction to Stacktraces\-\--information software provides
about where the fault may
lie](https://fedoraproject.org/wiki/StackTraces). &#42; [Using
&#96;coredumpctl&#96; to gather more information for bug
reports](https://fedoramagazine.org/file-better-bugs-coredumpctl/).

# Bugzilla queries {#_bugzilla_queries}

Ben Cotton :page-aliases: bugzilla/query.adoc

Bugzilla lets you search for bug reports that match specified
conditions. This page covers common options. The [Red Hat Bugzilla User
Guide](https://bugzilla.redhat.com/docs/en/html/using/index.html) has
more information.

## Simple queries {#_simple_queries}

The [simple Bugzilla query
form](https://bugzilla.redhat.com/query.cgi?format=specific) does a
relatively simple keyword search.

Enter a word or short phrase that identifies the problem you saw as
uniquely as possible in the Summary field. Examples: \'view source\',
\'auto proxy\', \'drag drop\', \'png image\'.

## Advanced queries {#_advanced_queries}

The [advanced Bugzilla query
form](https://bugzilla.redhat.com/query.cgi?format=advanced) looks
dauntingly complex. While it is complex and powerful, you can safely
ignore most of the form. Any part of the form that is left blank does
not limit the search. Each part that is filled in cuts the list of bugs
down to only those that match the criteria you set.

The Status field is set by default to find NEW, ASSIGNED, NEEDINFO, and
MODIFIED bugs---the unfixed bugs (or in the case of MODIFIED the
recently fixed bugs).

In the product field, you should always use \'Fedora\', \'Fedora EPEL\',
or \'Fedora Container Images\'. In the component field, select the
source package that contains the defect. See the [finding the correct
component](bugzilla/correct-component.xml) for help.

Enter a word or short phrase that identifies the problem you saw as
uniquely as possible in the Summary field. Examples: \'view source\',
\'auto proxy\', \'drag drop\', \'png image\'. If you enter more than one
word and they are not a phrase, change the type of matching for the
Summary field from &#42;contains the string&#42; to &#42;contains all of
the words/strings&#42; or &#42;contains any of the words/strings&#42;,
as appropriate.

Fedora generally doesn't make use of keywords in Bugzilla, so you won't
usually need to use this. Keywords are specific tags, not arbitrary
words. If you try to search for keywords that are not on the list, it
won't work.

# Finding duplicates in Bugzilla {#_finding_duplicates_in_bugzilla}

Ben Cotton :page-aliases: bugzilla/find-duplicates.adoc

Fedora developers want to hear about specific and reproducible bugs that
happen when you use Fedora Linux, but it does not help to have the same
bug reported many times. You can help to get more bugs fixed faster by
checking duplicate reports before filing a new bug.

Commonly encountered bugs can be found:

&#42; On the [most frequently reported
bugs](https://bugzilla.redhat.com/duplicates.cgi?sortby=count&amp;reverse=1&amp;product=Fedora&amp;maxrows=100&amp;changedsince=7)
list &#42; On the [Common
Bugs](https://fedoraproject.org/wiki/Bugs/Common) page for Rawhide bugs,
linked from a [Blocker or Target
Tracker](https://fedoraproject.org/wiki/BugZappers/HouseKeeping/Trackers)

If your bug isn't in the lists above, you can use [Bugzilla's search
tool](bugzilla-query.xml) to find matching bugs.

## What to do with duplicates once found {#_what_to_do_with_duplicates_once_found}

If you are a triager or package maintainer, set the bug that has less
information to the CLOSED status with a resolution of DUPLICATE, and add
the bug number of the bug with the best information. This may very well
mean closing a lower-numbered bug and keeping a higher-numbered one
open---that's fine.

If you do not have permissions to change bugs you have not reported, add
a comment to both bugs pointing out the duplication and someone else
will mark them appropriately.

# Bugzilla -- Finding the Correct Component {#_bugzilla_finding_the_correct_component}

Ben Cotton :page-aliases: bugzilla/correct-component.adoc

When filing a bug, it helps if you can identify the component at fault.
This is not always obvious, so here are some tips.

## Which program is it? {#_which_program_is_it}

If you started the program from the GNOME menu, you can usually find the
name of the program by going to \'Help -&gt; About\' in the program's
internal menus. You can also go to \'System -&gt; Preferences -&gt;
Personal -&gt; Sessions\' on the GNOME menu. Click on the \'Current
Session\' tab to see a list of programs running on your desktop.

If you started the program from the command line, the name of the
program is the first \'word\' of the command (everything before the
first space, which might include dashes or underscores).

If you want to find out exactly what command a specific menu item will
run, in GNOME you can do the following:

1.  Right-click on the menu item and select \'Add this launcher to
    panel\'

2.  Right-click on the icon that appears on your panel and select
    \'Properties\'

3.  Record the \'Command\' field, then close the Properties window.

4.  Right-click on the panel icon again and select \'Remove from panel\'
    to put things back the way they were when you started.

## Which file is it? {#_which_file_is_it}

If you know which command was run, but don't know the exact file name
this corresponds to, try this on the command line:

which &lt;command-name&gt;

The first line in the results is the one you want.

For example:

\$ which ssh /usr/bin/ssh

## Which package is it? {#_which_package_is_it}

Once you have the name of a file or directory, you can determine which
package owns it using \'rpm -qf\'. For example:

\$ rpm -qf /usr/bin/nautilus-file-management-properties
nautilus-2.25.91-2.fc11.x86_64

You should include the full name and version number of this package in
your bug report.

## Which component is it? {#_which_component_is_it}

In Fedora Linux, a given \'source\' RPM can produce multiple RPMs in the
distribution. Bugzilla groups bugs according to the \'source\' RPMs.
Once you have the RPM name, you can get the \'source\' RPM name (which
might be different) using \'rpm -qi\'.

For example, run &#96;rpm -qi glibc-common&#96; and then look for the
line that says \'Source RPM:\' In this case, it's
\'glibc-2.9.90-7.src.rpm\', which means the component name to use in
Bugzilla is \'glibc\' (everything before the dash before the version
number).

\$ rpm -qi glibc-common &#8230; Group : System Environment/Base Source
RPM: glibc-2.11-2.src.rpm

:::: note
::: title
:::

If the \'Vendor:\' line does not say \'Fedora Project\', you may need to
report the bug to a different project's bug tracker.
::::

## If you don't have package installed {#_if_you_dont_have_package_installed}

For packages which you have NOT installed you can use dnf's repoquery
command:

repoquery -f /usr/bin/kdm

will find you which binary package contains the kdm executable. To find
the component that provides the binary package you found above, run:

repoquery -q \--qf=\'%{sourcerpm}\\n\' kdm

## Embedded components {#_embedded_components}

Sometimes it can be unclear whether a bug is in the main application or
a plugin or library. In these cases, just make your best guess. A
triager or developer will reassign the bug if necessary.

# Reporting Bugzilla spam {#_reporting_bugzilla_spam}

Ben Cotton :page-aliases: bugzilla/spam.adoc

Like any website that allows user contribution, Red Hat Bugzilla
sometimes gets spam comments. There are two ways to report spam.

:::: tip
::: title
:::

If you have the necessary privileges, you can mark a spam comment as
private until the admins have had a chance to remove it.
::::

## Tag comment {#_tag_comment}

The preferred way is to tag the comment as spam.

1.  On the spam comment, click the tag icon. (The alt text says \'tag
    comment\'.)

2.  In the text box that opens, type \'spam\' and hit the Enter key.

This will flag the comment to the Bugzilla admins.

## Report by email {#_report_by_email}

You can submit reports via email to <bugzilla-owner@redhat.com>. Please
include a direct link to the comment(s) you are reporting for spam.

# Managing Bugzilla email notifications {#_managing_bugzilla_email_notifications}

Ben Cotton :page-aliases: bugzilla/email-notifications.adoc

Bugzilla allows you to set granular email notification preferences.

## Email preferences {#_email_preferences}

To set your email preferences, go to the [*Email Preferences*
tab](https://bugzilla.redhat.com/userprefs.cgi?tab=email) of your user
preferences. You will see a grid that allows you to select to receive
notifications based on the bug activity (rows) and your relationship to
the bug (columns).

In addition, you can exclude notifications when you are the one making
the change or when the change is marked as a \'minor update\'.

The *Email preferences* tab also allows you to ignore specific bugs.

## Watch components {#_watch_components}

If you want to get notifications for all bugs in a specific component,
go to the [*Watch Components*
tab](https://bugzilla.redhat.com/userprefs.cgi?tab=component_watch) of
your user preferences. You can select the components you want to watch.

Watching a component will still follow the email preferences you set.

:::: note
::: title
:::

If you are a package maintainer, you do not need to add notifications
for the packages you maintain. The release engineering automation will
add you automatically.
::::

## Watch specific bugs {#_watch_specific_bugs}

If you want to track a specific but, you can add yourself to the *CC*
list.

1.  On the bug you want to watch, click the *Add me to CC list* box.

2.  Check the *This is a minor update (do not send email)* box. (This
    step is optional, but is a polite choice to reduce email
    notifications. If you take other actions beyond adding yourself to
    the CC list, use your best judgement.)

3.  Click the *Save Changes* button.

# Providing a Stack Trace {#_providing_a_stack_trace}

Michael Schwendt; Rahul Sundaram; Ankur Sinha

:::: important
::: title
:::

This page was taken from the previous Fedora Wiki documentation.

It has been cleaned up for publishing here on the Fedora Docs Portal,
but it has not yet been reviewed for technical accuracy.

It is probably

&#42; Containing formatting issues &#42; Out-of-date &#42; In need of
other love

Reviews for technical accuracy are greatly appreciated. If you want to
help, see the [README
file](https://pagure.io/fedora-docs/quick-docs/blob/master/f/README.md)
in the source repository for instructions.

Pull requests accepted at <https://pagure.io/fedora-docs/quick-docs>

Once you've fixed this page, remove this notice.
::::

> A stack trace is one of the most important pieces of information you
> can provide to help others debug an application crash. This page
> details the importance of stack traces and outlines several methods
> for obtaining stack traces.

If you are experiencing a crash, the basic steps to generating a useful
stack trace for common Gnome desktop applications are:

&#42; Install the appropriate -debuginfo RPM(s) before the crash (see
section \'&lt;&lt;debuginfo&gt;&gt;\' below). &#42; Wait for the crash
to happen or perform whatever steps reproduce it. &#42; ABRT (Automatic
Bug Reporting Tool) in Fedora will automatically detect the crash and
obtain a stack trace. &#42; Include the stack trace in your bug report
(see document [\'How To File a Bug\'](bugzilla-file-a-bug.xml) for full
instructions).

If ABRT does not start automatically, you will need to start the program
in a special way, using a debugger (such as gdb). See section
&lt;&lt;gdb&gt;&gt; below.

Special instructions apply for &lt;&lt;JavaStackTraces,Java
programs&gt;&gt; and &lt;&lt;firefox&gt;&gt;.

## What is a stack trace (backtrace)? {#_what_is_a_stack_trace_backtrace}

A stack trace (sometimes also called a backtrace) is a list of function
calls that leads to some point in the program. Debugging tools like gdb
or bug-buddy can get stack traces from crashed applications so that
developers can figure out what went wrong.

## What does a stack trace look like? {#_what_does_a_stack_trace_look_like}

A typical stack trace looks similar to the following:

    [New_Thread_8192_(LWP_15167)]

    0x420ae169 in wait4 () from /lib/i686/libc.so.6
    .
    .
    .

A better backtrace, with debuginfo symbols (see below) looks like that:

    0x000000350a6c577f in \&#42;__GI___poll (fds=0xe27460, nfds=9, timeout=-1) at ../sysdeps/unix/sysv/linux/poll.c:83
    83          return INLINE_SYSCALL (poll, 3, CHECK_N (fds, nfds), nfds, timeout);

    .
    .
    .

Notice the filenames and line numbers of where the functions are called
appearing.

## What are debugging symbols, and why are they important? {#_what_are_debugging_symbols_and_why_are_they_important}

When a program is compiled with special switches to generate debugging
symbols (the -g compiler switch) extra information is stored in the
program file. This information can be used to generate a stack trace
that contains much more information, such as the exact line number of
the source file where things went wrong. Without this information it is
very hard to figure out what went wrong by looking at the stack trace.

## What are debuginfo RPMs, and how do I get them? {#debuginfo}

Fedora includes a special type of RPMs called debuginfo RPMs. These
automatically created RPMs contain the debugging information from the
program files, but moved into an external file. All the tools that
handle debugging information know how to automatically look in these
files. This lets you easily install debugging information when you need
it. You must install the exact matching version and architecture of
debuginfo as the application you are trying to debug.

Example: Verifying Matching Version and Arch

    [warren@computer ~] $ rpm -q --qf '%{name}-%{version}-%{release}.%{arch}\n' gaim gaim-debuginfo
    gaim-2.0.0-0.26.beta5.i386
    gaim-debuginfo-2.0.0-0.26.beta5.i386

Each package with binaries in the distribution has a corresponding
debuginfo package.

### Installing debuginfo RPMs using DNF {#_installing_debuginfo_rpms_using_dnf}

debuginfo-install is a handy plugin, part of &#96;dnf-plugins-core&#96;
package, that automatically enable the debuginfo repositories and
download all the debuginfo packages needed. You can do:

    $ dnf debuginfo-install \&lt;pkg-spec\&gt;

to install all the debuginfo packages needed for package
&#96;&lt;pkg-spec&gt;&#96;.

To install only the minimal set of debuginfo packages use the package
listing of the command (without actually installing anything) to get the
names of debuginfo packages and their respective repositories. Then
construct the install command according to the following example:

    $ dnf --enablerepo=fedora-debuginfo --enablerepo=updates-debuginfo install \&lt;pkg-spec\&gt;-debuginfo

This is useful when you don't want to install debuginfo for all the
dependencies of the debugged package as their debuginfo is often not
required.

### Installing debuginfo RPMs using yum {#_installing_debuginfo_rpms_using_yum}

The &#96;debuginfo-install&#96; is a handy utility, part of
&#96;yum-utils&#96; package, that automatically enable the debuginfo
repositories and download all the debuginfo packages needed. You can do:

    $ debuginfo-install foo

to install all the debuginfo packages needed for package &#96;foo&#96;.

To install only the minimal set of debuginfo packages use the output of
&#96;debuginfo-install&#96; (without actually installing anything) to
get the names of debuginfo packages and their respective repositories.
Then construct the install command according to the following example:

    $ yum --enablerepo fedora-debuginfo,updates-debuginfo install foo-debuginfo

This is useful when you don't want to install debuginfo for all the
dependencies of the debugged package as their debuginfo is often not
required.

### Installing debuginfo RPMs manually {#_installing_debuginfo_rpms_manually}

These packages can be downloaded from the normal fedora mirrors in the
\'debug\' subdirectory of the architecture directory. For example, the
debuginfo packages for the latest development version is available from
[
http://mirrors.fedoraproject.org/publiclist/Fedora/development/](https://mirrors.fedoraproject.org/publiclist/Fedora/development/)
. Please use the mirror closest to you when downloading.

### Packagers {#_packagers}

If you are a packager looking for information about debuginfo RPMs, see
document [Debuginfo packages](packaging-guidelines:Debuginfo.xml).

## How do I generate a backtrace? {#_how_do_i_generate_a_backtrace}

First make sure that you have installed the debuginfo packages for the
application you are debugging and all related libraries. A developer
often tells you to install specific debuginfo packages because he can
tell from a stack trace which libraries are involved in the crash. See
below for recommended packages for some common type of applications.

There are several ways to get a stack trace:

&#42; Obtaining a stack trace using &lt;&lt;gdb&gt;&gt;. &#42; Obtaining
a stack trace from a &lt;&lt;coredump,core dump with GDB&gt;&gt;. &#42;
Obtaining a stack trace from an application using &lt;&lt;abrt,Automatic
Bug Reporting Tool&gt;&gt;.

## What debuginfo packages should I install? {#_what_debuginfo_packages_should_i_install}

At the very least you will need to install the debuginfo package for the
application that is crashing. You can find out what package this
application is in by typing &#96;rpm -qf path-of-program&#96;.

For certain types of programs it is also very useful to install a couple
of default packages that are useful for almost all stack traces:

&#42; Gnome applications and applications using Gtk+:
&#96;glib2-debuginfo, pango-debuginfo, gtk2-debuginfo&#96; &#42; KDE
applications: &#96;qt-debuginfo, kdelibs-debuginfo&#96;

## Obtaining a stack trace using just GDB {#gdb}

:::: note
::: title
:::

If you are running a Java program such as Eclipse or Tomcat, the
situation is a bit more complicated - see
&lt;&lt;JavaStackTraces&gt;&gt; for details.
::::

First, run the following command to start gdb:

    gdb name-of-program

Where name-of-program is the name of the program that crashed (for
example: &#96;/usr/bin/gnome-panel&#96;).

Then, at the gdb prompt, type:

    run

If you need to give any arguments to the program, give them after the
run command, like:

    run --argument

Once the program is running, reproduce the crash and go back to the
terminal where you ran gdb. The gdb prompt should be shown - if not, hit
Control+C to break into the debugger. At the gdb debugger prompt, type:

    thread apply all bt full

If that does not work (meaning that you don't get any output---​this may
be the case in programs which are not multi-threaded), type
&lt;code&gt;bt&lt;/code&gt; instead. If you still do not have any
output, read \[\[&#35;special\| this note\]\] about obtaining a stack
trace under special circumstances. The output is the stack trace. Cut
and paste all of it into a text file.

You can quit gdb by typing &#96;quit&#96;.

Sometimes, the trace can be quite large and it is difficult to copy and
paste it. In such situations, storing the trace to a file is convenient:

    gdb
    \&gt; run
    \&#35; program crashes
    \&gt; set logging file backtrace.log
    \&gt; set logging on
    \&gt; thread apply all bt full
    \&gt; set logging off
    \&gt; quit

## Obtaining a stack trace from a core dump {#coredump}

If the program that crashes leaves a core dump, you can use GDB to
obtain a stack trace. Core dumps are saved in a file on your hard disk
and are usually named something along the lines of \'core\' or
\'core.3124\'. To obtain a stack trace from one of these files, run the
following command:

    gdb name-of-program core-file-name

Where &#96;name-of-program&#96; is the name of the program that crashed
(for example: /usr/bin/gnome-panel), and &#96;core-file-name&#96; is the
name of the core file that contains the core dump (for example:
core.7812).

Then, at the gdb prompt, type:

    thread apply all bt full

If that does not work (meaning that you don't get any output---​this may
be the case in programs which are not multi-threaded), type &#96;bt&#96;
instead. If you still do not have any output, read &lt;&lt;special,this
note&gt;&gt; about obtaining a stack trace under special circumstances.
The output is the stack trace. Cut and paste all of it into a text file.

You can quit gdb by typing &#96;quit&#96;.

Note that creation of core files is disabled in Fedora by default (in
/etc/profile). To enable them for a shell session, type at the shell
prompt:

    ulimit -c unlimited

## How to install ABRT {#abrt}

If you installed Fedora via a LiveCD image, ABRT should already be
installed. You should be able to start it in &#96;Applications -&gt;
System Tools -&gt; Automatic Bug Reporting Tool&#96;. If ABRT is not
installed, for whatever reason, you can install it manually by doing the
following on a command line:

    $ su -c 'dnf install abrt'

or go to &#96;System&#96; -&gt; &#96;Administration&#96; -&gt;
&#96;Add/Remove Software&#96; in Gnome, and type&#96;abrt&#96; in the
search box and select &#96;Find&#96;. Select the abrt package and apply
the changes.

## Configuring ABRT for Bugzilla {#_configuring_abrt_for_bugzilla}

Go to &#96;Application&#96; -&gt; &#96;System Tools&#96; -&gt;
&#96;Automated Bug Reporting Tool&#96; and select it to start it
manually. Once the GUI window appears, choose &#96;Edit&#96; -&gt;
&#96;Plugins&#96; and from the Settings window, scroll down, highlight
Bugzilla and choose &#96;Configure Plugin&#96;. The Bugzilla URL should
be <https://bugzilla.redhat.com> and enter your own Bugzilla login and
password in the proper boxes.

:::: note
::: title
:::

If you do not yet have a Bugzilla account, now is the time to get one,
just go to the URL as displayed on that page and [create a new
account](https://bugzilla.redhat.com/createaccount.cgi).
::::

Next time you have a program crash, and ABRT triggers, when you hit
Report, ABRT will be able to automatically log in to Bugzilla and submit
a Bug Report for you.

## Using ABRT {#_using_abrt}

(The following assumes Gnome as the desktop &#8230; someone else will
have to update for KDE/Others)

If ABRT detects a crashed program, you will get an ABRT alert. This will
be visually indicated by a flashing red light in the system tray. Left
click on the alert light, and the Automatic Bug Reporting Tool should
start, displaying all of the crashes it has registered. To report the
bug, right click on it and choose report. ABRT will gather the logs it
needs to submit with the bug and will then let you know it is going to
submit a bug on your behalf. If you have configured ABRT as in the
previous section, it will then ask you to verify whether or not to
include the various logs, then will automatically go out to Bugzilla and
open a bug, attaching the logs into the bug. It will then show you the
bug number so that you can track the bug as it is worked on.

## Configuring ABRT when missing Debuginfos {#_configuring_abrt_when_missing_debuginfos}

When you right click on a bug in ABRT and choose Report, ABRT will
attempt to go out and retrieve the logs it will need to send as part of
the bug report. The developers have added code to detect whether or not
symbolic traces are included within the backtrace, and if it detects
that there are none, ABRT will alert you of this, and will show you the
command to run. This is the same as what is shown in the
&lt;&lt;debuginfo,debuginfo&gt;&gt; section.

## Special cases {#special}

## Programs running as another user {#_programs_running_as_another_user}

If you do not get any output from gdb after typing &#96;thread apply all
bt&#96; or &#96;bt&#96;, it may be because the program is run as root or
as another user. In GNOME for example, this is the case when running
gnome-games. In such cases, you will need to be root in order to capture
a trace. So, quit gdb, login as root, and then repeat the steps to
obtain a stack trace.

### Firefox

&#42; Install Firefox and Xulrunner debug info packages - run
&#96;ebuginfo-install firefox xulrunner&#96; as root on the command
line. &#42; Run &#96;firefox -g&#96; on the command line. That will
start firefox running inside of gdb debugger. &#42; In gdb, you should
see gdb prompt &#96;(gdb)&#96;. Issue the command &#96;run
-safe-mode&#96;. A dialog window will pop up, disable all add-ons here
and continue in safe mode. &#42; Do whatever is necessary to make
firefox crash and follow the instructions above for gdb usage. &#42;
When Firefox crashes, &lt;&lt;gdb,obtain the backtrace&gt;&gt; and
attach it to bugzilla.

For additional info see [Debugging guidelines for Mozilla
products](troubleshooting-mozilla-products.xml).

### Thunderbird {#_thunderbird}

It's almost the same as for Firefox, just the debug info packages are
different. Install them by \'debuginfo-install thunderbird\' command as
root on the console.

For additional info see [Debugging guidelines for Mozilla
products](troubleshooting-mozilla-products.xml).

### Java programs {#JavaStackTraces}

See document [Troubleshooting Java
Programs](#troubleshooting-java-programs) for info on getting stack
traces from programs running in Java.

### Daemons and their spawn {#_daemons_and_their_spawn}

You will need to gather the backtrace from the core file.

Make sure your daemon's initscript isn't forbidding dumping core files
to the disk. Add the line &#96;DAEMON_COREFILE_LIMIT=unlimited&#96; to
its configuration file in &#96;/etc/sysconfig&#96;. For example, the
Bluetooth daemon (hcid) uses &#96;/etc/sysconfig/bluetooth&#96;.

Then setup the kernel so that the core dump is written to a known
location such as &#96;/tmp&#96;. As root, run:

    echo /tmp/core \&gt; /proc/sys/kernel/core_pattern

To make this change permanent, add that line to /etc/sysctl.conf:

    kernel.core_pattern = /tmp/core

And run &#96;sysctl -p&#96; to apply it straight away.

A full list of possible patterns for the core file are available at in
the [sysctl/kernel.txt kernel
Documentation](https://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=blob;f=Documentation/sysctl/kernel.txt;hb=HEAD)
.

Finally, after reproducing your problem, you can double-check which
binary created the core file with &#96;file /tmp/core.1234&#96;. Then
run gdb on the file to create a post-mortem stack trace:

    gdb /path/to/binary/file /tmp/core.1234

and follow the instructions above for gdb usage.

:::: note
::: title
:::

you can test whether dumping a core file would work by running &#96;kill
-SEGV 1234&#96; where 1234 is the PID of the program you're testing.
::::

## Other tools {#_other_tools}

### Valgrind {#_valgrind}

The brilliant tool [valgrind](https://valgrind.org/) is often able to
say more about what is going wrong; it can give a stack trace to the
point where things start to go wrong, which might be long time before
the program actually crashes. Programs run through valgrind will run an
order of magnitude slower and use more memory, but it will be
buddyamazingly usable.

With valgrind installed (&#96;dnf install valgrind) you can use it on a
program:

    valgrind name-of-program program-arguments

With debuginfo installed stacktraces will use symbolic names. See
\[<http://valgrind.org/> valgrind.org\] for more info and tips and
tricks.

### strace {#_strace}

strace can track all system calls made by a program, which can also be
helpful in debugging, though it cannot produce stack traces. Install
with &#96;dnf install strace&#96;, and see &#96;man strace&#96; for
details.

The situation is a bit improved. Now stack trace feature is implemented
(&#96;strace -k&#96;). Though it is disabled when building because the
implementation is not stable on i386.

## References {#_references}

&#42; Much of the text from this page comes from the excellent [GNOME
bugsquad on getting stack traces](https://live.gnome.org/GettingTraces).
&#42; <https://linux.bytesex.org/gdb.html>

&#42; Installation = Creating and using a live installation image Chase
Lau ; ctrngk; The Fedora Docs Team

## Downloading Fedora {#_downloading_fedora}

You can download Fedora from <https://fedoraproject.org/>.

There are multiple desktops available for use with Fedora. Each has a
slightly different look and feel and offers varying levels of
customization. You can use the [Fedora
Workstation](https://fedoraproject.org/workstation/) image, which comes
with the GNOME desktop by default, and then change your environment
afterwards by installing additional packages, or you can download a spin
image which will give you a different environment out of the box. Visit
[Fedora Spins](https://spins.fedoraproject.org/) for more information.

You can also take advantage of Fedora Labs. Fedora Labs is a selection
of curated bundles of purpose-driven software and content as curated and
maintained by members of the Fedora Community. These may be installed as
standalone full versions of Fedora or as add-ons to existing Fedora
installations. Visit [Fedora Labs](https://labs.fedoraproject.org/) for
details. @

:::: note
::: title
:::

Please refer to [Fedora Getting Started](getting-started.xml) Guide for
getting help on the process of installing Fedora.
::::

## Creating and using live USB {#_creating_and_using_live_usb}

You can write all Fedora ISO images to a USB stick, making this a
convenient way on any USB-bootable computer to either install Fedora or
try a &#42;live&#42; Fedora environment without writing to the
computer's hard disk. You will need a USB stick at least as large as the
image you wish to write.

### Using Fedora Media Writer

The official and supported tool to create a Fedora USB stick is the
&#42;Fedora Media Writer&#42; utility, which was formerly known as
&#42;LiveUSB Creator&#42;. See [Fedora Media
Writer](preparing-boot-media.adoc&#35;_fedora_media_writer) guide in
Fedora User Documentation overview.

:::: important
::: title
:::

&#42;Fedora Media Writer&#42; destroys all data on the USB stick. If you
need a non-destructive write method (to preserve existing data on your
USB stick) or support for \'data persistence\', you can use the
[livecd-iso-to-disk](creating-and-using-a-live-installation-image.adoc&#35;using-the-livecd-iso-to-disk-tool)
utility on Fedora.
::::

### Using GNOME Disks {#gnome-disk-utility}

:::: important
::: title
:::

This method will destroy all data on the USB stick. If you need a
non-destructive write method (to preserve existing data on your USB
stick) and/or support for \'data persistence\', you can use the
&#96;livecd-iso-to-disk&#96; utility on Fedora.
::::

:::: warning
::: title
:::

This method is considered unsupported. You can use it on your own risk.
::::

This method is for people running Linux, or another unix with GNOME,
Nautilus, and GNOME Disks installed. Particularly, if you are using a
distribution other than Fedora which does not support Flatpak, this may
be the easiest available method. A standard installation of Fedora, or a
standard GNOME installation of many other distributions, should be able
to use this method. On Fedora, ensure the packages *nautilus* and
*gnome-disk-utility* are installed. Similar graphical direct-write tools
may be available for other desktops, or you may use the command-line
*direct write* method.

1.  Download a Fedora image, choose a USB stick that does not contain
    any data you need, and connect it.

2.  Run Nautilus (Files), open the &#42;Overview&#42; by pressing the
    &#42;Start/Super&#42; key, type Files, and hit kbd:\[Enter\].

3.  Find the downloaded image, right-click on it, go to &#42;Open
    With&#42;, and click &#42;Disk Image Writer&#42;.

4.  Select your USB stick as the &#42;Destination&#42;, and click
    &#42;Start Restoring&#42;.

### Command line methods {#command-line-method}

:::: warning
::: title
:::

These methods are considered unsupported. You can use them on your own
risk.
::::

#### Using the livecd-iso-to-disk tool

:::: important
::: title
:::

This method will destroy all data on the USB stick *if the
&#96;\--format&#96; parameter is passed*.
::::

The &#96;livecd-iso-to-disk&#96; method is slightly less reliable than
Fedora Media Writer and can be used reliably only from within Fedora: it
does not work in Windows or macOS, and is not supported (and will
usually fail) in non-Fedora distributions. However, it supports three
advanced features which FMW does not include:

1.  You may use a *non-destructive* method to create the stick, meaning
    existing files on the stick will not be destroyed. This is less
    reliable than the *destructive* write methods, and should be used
    only if you have no stick you can afford to wipe.

2.  On live images, you can include a feature called a *persistent
    overlay*, which allows changes made to persist across reboots. You
    can perform updates just like a regular installation to your hard
    disk, except that kernel updates require manual intervention and
    overlay space may be insufficient. Without a *persistent overlay*,
    the stick will return to a fresh state each time it is booted.

3.  On live images, you can also have a separate area to store user
    account information and data such as documents and downloaded files,
    with optional encryption for security and peace of mind.

By combining these features, you can carry your computer with you in
your pocket, booting it on nearly any system you find yourself using.

It is not a good idea to try and write a new Fedora release using the
version of &#96;livecd-iso-to-disk&#96; in a much older Fedora release:
it is best to only use a release a maximum of two versions older than
the release you are trying to write.

Ensure the
[livecd-tools](https://packages.fedoraproject.org/pkgs/livecd-tools/livecd-tools/)
package is installed: &#96;dnf install livecd-tools&#96;.

:::: note
::: title
:::

Remember to identify your USB stick's device name first. In all cases,
you can add the parameter &#96;\--efi&#96; to render the stick bootable
in native UEFI mode. Detailed usage information is available by running:
&#96;livecd-iso-to-disk \--help&#96; or &#96;man
livecd-iso-to-disk&#96;.

To make an existing USB stick bootable as a Fedora image, without
deleting any of the data on it, make sure that the USB drive is not
mounted before executing the following, and give the root password when
prompted:

``` shell
\# livecd-iso-to-disk Fedora-Workstation-Live-x86_64-43-1.1.iso /dev/sdX
```

In case it is not possible to boot from a disk created with the method
shown above, before re-partitioning and re-formatting, often resetting
the master boot record will enable booting:

``` shell
\# livecd-iso-to-disk --reset-mbr Fedora-Workstation-Live-x86_64-43-1.1.iso /dev/sdX
```
::::

:::: important
::: title
:::

Using the &#96;\--format&#96; option in the following command will erase
all data on the USB drive.
::::

If necessary, you can have &#96;livecd-iso-to-disk&#96; re-partition and
re-format the target stick:

``` shell
\# livecd-iso-to-disk --format --reset-mbr Fedora-Workstation-Live-x86_64-43-1.1.iso /dev/sdX
```

To include a persistent filesystem for &#96;/home&#96;, use the
&#96;\--home-size-mb&#96; parameter. For example:

``` shell
\# livecd-iso-to-disk --home-size-mb 2048 Fedora-Workstation-Live-x86_64-43-1.1.iso /dev/sdX
```

This will create a 2 GiB filesystem that will be mounted as
&#96;/home&#96; each time the stick is booted, allowing you to preserve
data in &#96;/home&#96; across boots.

To enable \'data persistence\' support - so changes you make to the
entire live environment will persist across boots - add the
&#96;\--overlay-size-mb&#96; parameter to add a persistent data storage
area to the target stick. For example:

``` shell
\# livecd-iso-to-disk --overlay-size-mb 2048 Fedora-Workstation-Live-x86_64-43-1.1.iso /dev/sdX
```

Here, &#96;\_2048\_&#96; is the desired size (in megabytes) of the
overlay. The &#96;livecd-iso-to-disk&#96; tool will not accept an
overlay size value greater than *4095* for VFAT, but for ext\[234\]
filesystems it is only limited by the available space.

:::: note
::: title
:::

Due to the way it's currently implemented, every single change to this
form of overlay, writes AND deletes, subtracts from its free space so it
will eventually be \'used up\' and your USB stick will no longer boot.
You can use &#96;dmsetup&#96; status &#96;live-rw&#96; to see how much
space remains in the overlay.

The output will contain something like snapshot &#96;42296/204800&#96;,
indicating that 4229 of 204800 512-byte sectors are allocated. Because
of these limitations, it is advisable to use the &#96;system-level&#96;
persistence sparingly, for configuration changes and important security
updates only. Or, if you have sufficient disk space available, changes
to the &#96;LiveOS&#96; root filesystem snapshot can be merged into a
new copy of the root filesystem.
::::

You can combine &#96;\--home-size-mb&#96; and
&#96;\--overlay-size-mb&#96;, in which case data written to
&#96;/home&#96; will not exhaust the persistent overlay.

#### Using a direct write method {#_using_a_direct_write_method}

:::: important
::: title
:::

This method will destroy all data on the USB stick. If you need a
non-destructive write method, to preserve existing data on your USB
stick, and/or support for &#96;data persistence&#96;, you can use the
&#96;livecd-iso-to-disk&#96; utility on Fedora.
::::

This method directly writes the image to the USB stick much like [Fedora
Media
Writer](creating-and-using-a-live-installation-image.adoc&#35;using-fedora-media-writer)
or GNOME Disk Utility, but uses a command line utility named
&#96;dd&#96;. Like the other *direct write* methods, it will destroy all
data on the stick and does not support any of the advanced features like
data persistence, but it is a very reliable method. The &#96;dd&#96;
tool is available on most Unix-like operating systems, including Linux
distributions and macOS, and a Windows port is available. This may be
your best method if you cannot use [Fedora Media
Writer](creating-and-using-a-live-installation-image.adoc&#35;using-fedora-media-writer)
or GNOME Disk Utility, or just if you prefer command line utilities and
want a simple, quick way to write a stick.

1.  Identify the name of the USB drive partition. If using this method
    on Windows, with the port linked above, the &#96;dd \--list&#96;
    command should provide you with the correct name.

2.  &#42;Unmount all mounted partition from that device&#42;. This is
    very important, otherwise the written image might get corrupted. You
    can umount all mounted partitions from the device with &#96;umount
    /dev/sdX&#42;&#96;, where &#96;\_X\_&#96; is the appropriate letter,
    e.g. &#96;umount /dev/sdc&#42;&#96;.

3.  Write the ISO file to the device:

    ``` shell
    \# dd if=/path/to/image.iso of=/dev/sdX bs=8M status=progress oflag=direct
    ```

4.  Wait until the command completes.

    :::: note
    ::: title
    :::

    If you see &#96;dd: invalid status flag: \'progress\'&#96;, your dd
    version doesn't support the &#96;status=progress&#96; option and
    you'll need to remove it. In this case, you won't see writing
    progress.
    ::::

### Using UNetbootin for Windows, macOS, and Linux {#unetbootin}

:::: warning
::: title
:::

This method is considered unsupported. You can use it on your own risk.
::::

:::: note
::: title
:::

UNetbootin may work in some cases but not others - for instance, it will
likely create a stick that is bootable in BIOS mode, but not UEFI mode.
Fedora cannot guarantee support for UNetbootin-written images.

While your results may vary, it is usually the case that the Fedora
Media Writer, &#96;livecd-iso-to-disk&#96;, GNOME, and &#96;dd&#96;
methods give better results than UNetbootin. If you encounter problems
with UNetbootin, please contact the UNetbootin developers, not the
Fedora developers.
::::

[UNetbootin](https://unetbootin.github.io/) is a graphical, bootable USB
image creator. Using it will allow you to preserve any data you have in
the USB drive. If you have trouble booting, however, you may wish to try
with a blank, cleanly FAT32-formatted drive.

:::: note
::: title
:::

If you are running a 64-bit Linux distribution, UNetbootin may fail to
run until you install the 32-bit versions of quite a lot of system
libraries.
::::

1.  Download the latest UNetbootin version from the [official
    site](https://unetbootin.github.io/) and install it. On Linux, the
    download is an executable file: save it somewhere, change it to be
    executable using &#96;chmod ugo+x&#96; filename or a file manager,
    and then run it.

2.  Launch UNetbootin. On Linux, you might have to type the root
    password.

3.  Click on &#96;Diskimage&#96; and search for the ISO file you
    downloaded.

4.  Select Type: USB drive and choose the correct device for your stick.

5.  Click OK.

:::: note
::: title
:::

If you do not see *sdX* listed, you might have to reformat the drive.
You can do this from most file manager or disk utility tools, e.g. the
GNOME disk utility (\'Disks\') on Fedora. The FAT32 format is most
likely to result in a bootable stick. This will cause you to lose all
data on the drive.
::::

### Creating a USB stick from a running live environment {#creating_usb_stick_from_a_running_live_environment}

If you are already running a live CD, DVD, or USB and want to convert
that into a bootable USB stick, run the following command:

``` shell
\# livecd-iso-to-disk /run/initramfs/livedev /dev/sdX'
```

:::: note
::: title
:::

This method will no longer be effective for Fedora 37 and later
versions. As of Fedora 37, the syslinux (isolinux) booting method has
been entirely removed.
::::

## Booting from USB sticks {#booting_from_USB_sticks}

Almost all modern PCs can boot from USB sticks. However, how you tell
the system to boot from a USB stick varies substantially from system to
system. Initially, you can try this:

1.  Power off the computer.

2.  Plug the USB drive into a USB port.

3.  Remove all other portable media, such as CDs, DVDs, floppy disks or
    other USB sticks.

4.  Power on the computer.

5.  If the computer is configured to automatically boot from the USB
    drive, you will see a screen that says \'Automatic boot in 10
    seconds&#8230;\' with a countdown.

    If you do a native UEFI boot, where you will see a rather more
    minimal boot menu.

If the computer starts to boot off the hard drive as normal, you'll need
to manually configure it to boot off the USB drive. Usually, that should
work like this:

1.  Wait for a safe point to reboot.

2.  As the machine starts to reboot, watch carefully for instructions on
    which key to press. Usually a function key, &#96;Escape&#96;,
    &#96;Tab&#96;, &#96;F11&#96;, &#96;F12&#96; or &#96;Delete&#96; is
    to be pressed to enter the boot device selection menu, &#96;BIOS
    setup&#96;, &#96;firmware&#96;, or &#96;UEFI&#96;. Press and hold
    that key. If you miss the window of opportunity, often only a few
    seconds, then reboot and try again. (If this does not work, consult
    the manual of your computer)

3.  Use the firmware, &#96;BIOS&#96;, interface or the boot device menu
    to put your USB drive first in the boot sequence. It might be listed
    as a hard drive rather than a removable drive. Each hardware
    manufacturer has a slightly different method for doing so.

    :::: important
    ::: title
    :::

    Your computer could become unbootable or lose functionality if you
    change any other settings. Though these settings can be reverted,
    you'll need to remember what you changed in order to do so.
    ::::

4.  Save the changes, exit, and the computer should boot from the USB
    drive.

If your system has a UEFI firmware, it will usually allow you to boot
the stick in UEFI native mode or BIOS compatibility mode. If you boot in
UEFI native mode and perform a Fedora installation, you will get a UEFI
native Fedora installation. If you boot in BIOS compatibility mode and
perform a Fedora installation, you will get a BIOS compatibility mode
Fedora installation.

For more information on all this, see the [UEFI
page](https://fedoraproject.org/wiki/Unified_Extensible_Firmware_Interface).
USB sticks written from x86_64 images with [Fedora Media
Writer](creating-and-using-a-live-installation-image.adoc&#35;using-fedora-media-writer),
[GNOME Disk
Utility](creating-and-using-a-live-installation-image.adoc&#35;gnome-disk-utility),
&#96;dd&#96;, other dd-style utilities should be UEFI native bootable.
Sticks written with other utilities may not be UEFI native bootable, and
sticks written from i686 images will never be UEFI bootable.

### Identifying a stick on Linux {#identifying_stick}

Most of the writing methods will require you to know the &#96;/dev&#96;
name for your USB stick, e.g. &#96;/dev/sdc&#96;, when using them on
Linux. You do not need to know this in order to use Fedora Media Writer.
To find this out:

1.  Insert the USB stick into a USB port.

2.  Open a terminal and run &#96;dmesg&#96;.

3.  Near the end of the output, you will see something like:

        [32656.573467] sd 8:0:0:0: [sdX] Attached SCSI removable disk

    &#96;sdX&#96; will be &#96;sdb&#96;, &#96;sdc&#96;, &#96;sdd&#96;,
    etc.

:::: note
::: title
:::

This is the name of the disk you will use. We'll call it &#96;sdX&#96;
from now on. If you have connected more than one USB stick to the
system, be careful that you identify the correct one, often you will see
a manufacturer name or capacity in the output which you can use to make
sure you identified the correct stick.
::::

## Troubleshooting a live USB {#troubleshooting_live_USB}

### livecd-iso-to-disk problems {#_livecd_iso_to_disk_problems}

Partition isn't marked bootable

:   If you get the message &#96;Partition isn't marked bootable!&#96;,
    you need to mark the partition bootable. To do this, run &#96;parted
    /dev/sdX&#96;, and use the &#96;toggle N&#96; boot command, where
    &#96;\_X\_&#96; is the appropriate letter, and &#96;\_N\_&#96; is
    the partition number. For example:

    ``` shell
    $ parted /dev/sdb
    GNU Parted 1.8.6
    Using /dev/sdb
    Welcome to GNU Parted! Type 'help' to view a list of commands.
    (parted) print
    Model: Imation Flash Drive (scsi)
    Disk /dev/sdX: 1062MB
    Sector size (logical/physical): 512B/512B
    Partition Table: msdos

    Number  Start   End     Size    Type     File system  Flags
    1      32.3kB  1062MB  1062MB  primary  fat16

    (parted) toggle 1 boot
    (parted) print
    Model: Imation Flash Drive (scsi)
    Disk /dev/sdX: 1062MB
    Sector size (logical/physical): 512B/512B
    Partition Table: msdos

    Number  Start   End     Size    Type     File system  Flags
    1      32.3kB  1062MB  1062MB  primary  fat16        boot

    (parted) quit
    Information: Don't forget to update /etc/fstab, if necessary.
    ```

Partitions need a filesystem label

:   If you get the message &#96;Need to have a filesystem label&#96; or
    &#96;UUID&#96; for your USB device, you need to label the partition:
    &#96;dosfslabel /dev/sdX LIVE&#96;.

Partition has different physical/logical endings

:   If you get this message from fdisk, you may need to reformat the
    flash drive when writing the image, by passing &#96;\--format&#96;
    when writing the stick.

MBR appears to be blank

:   If your test boot reports a corrupted boot sector, or you get the
    message &#96;MBR appears to be blank.&#96;, you need to install or
    reset the master boot record (MBR), by passing
    &#96;\--reset-mbr&#96; when writing the stick.

livecd-iso-to-disk on other Linux distributions

:   &#96;livecd-iso-to-disk&#96; is not meant to be run from a
    non-Fedora system. Even if it happens to run and write a stick
    apparently successfully from some other distribution, the stick may
    well fail to boot. Use of &#96;livecd-iso-to-disk&#96; on any
    distribution other than Fedora is unsupported and not expected to
    work: please use an alternative method, such as [Fedora Media
    Writer](&#35;using-fedora-media-writer).

### Testing a USB stick using qemu {#_testing_a_usb_stick_using_qemu}

You can test your stick using QEMU.

    \&#35; umount /dev/sdX1
    $ qemu -hda /dev/sdX -m 1024 -vga std

### Mounting a Live USB filesystem {#_mounting_a_live_usb_filesystem}

You can use the
[liveimage-mount](https://github.com/livecd-tools/livecd-tools/blob/master/tools/liveimage-mount)
script in the
[livecd-tools](https://packages.fedoraproject.org/pkgs/livecd-tools/livecd-tools/)
package to mount an attached Live USB device or other LiveOS image, such
as an ISO or Live CD. This is convenient when you want to copy in or out
some file from the LiveOS filesystem on a Live USB, or just examine the
files in a Live ISO or Live CD.

## Creating and using live CD {#proc_creating-and-using-live-cd}

We will use Fedora release 42 exemplary in all command examples. If you
need to do it for a different release, just change the number
accordingly.

### Getting started

To create a live image, the &#96;livecd-creator&#96; and &#96;mock&#96;
packages are used. For this, super user privileges are needed.

The &#96;livecd-creator&#96; tool is part of the \_livecd-tools_package.
If it is not installed on your system, add it and all other tools like
mock, lorax, git, pykickstart and a text editor with DNF:

    \&#35; dnf install livecd-tools mock

Hint: We are creating a livecd like the fedora-live-workstation image,
which is totally localized, but has english as default. There is no need
to install any localization support on your own. You can change it in
the created kickstart.cfg if necessary.

### Configuring your system

We need to add you current user to the mock group, or you need to do
anything as root user.

    \&#35; sudo usermod -aG mock $(whoami)

The \$(whoami) adds your current user, as we do not know what username
you are currently using ;)

A relogin to make the change effective, would be wise, or you switch to
root now.

Let's create the mock group:

    \&#35; newgrp mock

If you now enter:

    \&#35; groups

it shall output your username together with the old groups and the new
group \'mock\'. If this is not the case, you did something wrong.

### Creating your build environment

Now we can init the build environment. In this example we use the most
likely x86_64, but if you build it for ARM or PowerPC, you can just use
a different config by changing the ARCH-Type to the desired platform!

    \&#35; mock -r /etc/mock/fedora-42_x86_64.cfg --init

Mock creates us an empty toolbox for this, so we need to fill it with
packages, which we will need to create the image later in the process.
If you now think \'Why so complicated?\' you are only partly right, as a
toolbox is a simple container, which we need to separate the work for
different releases of Fedora, otherwise you have to overwrite and mixing
different builds on your own.

Make sure you have enough free disk space for all these files and the
ones, the livemedia-creator will download later. We suggest at least 10
GB free diskspace for this.

    \&#35; mock -r /etc/mock/fedora-42_x86_64.cfg --install lorax anaconda git pykickstart vim lorax anaconda git pykickstart vim libblockdev-lvm libblockdev-btrfs libblockdev-swap libblockdev-loop libblockdev-crypto libblockdev-dm libblockdev-mdraid libblockdev-part libblockdev-fs libblockdev-nvme libblockdev-mpath

If you wanne use a different texteditor then \'vim\', you need to
install it now, otherwise you are stuck to a not so well integrated
basic \'vim\' installation, which will be a bit unpleasant to use. Don't
panic, we don't do much editing inside the toolbox, vim will do :)

Now we enter the toolbox for the first time &#8230;

    \&#35; mock -r /etc/mock/fedora-42_x86_64.cfg --shell --isolation=simple --enable-network

This gives us a shell and networksupport, so the scripts inside the
toolbox can access the internet and install packages from the repo.

You will see something like this output:

    INFO: mock.py version 6.3 starting (python version = 3.13.7, NVR = mock-6.3-1.fc42), args: /usr/libexec/mock/mock -r fedora-42-x86_64 --shell --isolation=simple --enable-network
    Start(bootstrap): init plugins
    INFO: selinux enabled
    Finish(bootstrap): init plugins
    Start: init plugins
    INFO: selinux enabled
    Finish: init plugins
    INFO: Signal handler active
    Start: run
    Start(bootstrap): chroot init
    INFO: calling preinit hooks
    INFO: enabled root cache
    INFO: enabled package manager cache
    Start(bootstrap): cleaning package manager metadata
    Finish(bootstrap): cleaning package manager metadata
    INFO: Package manager dnf5 detected and used (fallback)
    Finish(bootstrap): chroot init
    Start: chroot init
    INFO: calling preinit hooks
    INFO: enabled root cache
    INFO: enabled package manager cache
    Start: cleaning package manager metadata
    Finish: cleaning package manager metadata
    INFO: enabled HW Info plugin
    INFO: Package manager dnf5 detected and used (direct choice)
    Finish: chroot init
    Start: shell
    \&lt;mock-chroot\&gt; sh-5.2\&#35;

Now we need to download the kickstart files, which previous Fedora
releases had as a package, from the Fedora Servers:

    \&#35; git clone https://pagure.io/fedora-kickstarts -b f42

You can access the page with a normal browser, to see which tags aka
\'branches\' like \'f42\' are available, in case you wanne do another
version. What happens now is a git checkout into the current directory
of your toolbox. Big advantage: no danger of overwriting files on your
os.

ATTENTION: before you continue, make sure you have at least 10 GB of
free storage on your systems partition as we will download a lot of rpms
and create an image that is at least 2,3 GB in size. If you don't have
enough space, all future steps can fail with the wildest error messages
and your will waste A LOT of time with it!

What we now need is a kickstart file. Never heard of it, don't panic :D

A kickstart file contains information about the size of the tmp drive in
the later started live image, it mounts, its packages and so on. You
will not need to reinvent the wheel, relax. Here is an example:

    %include fedora-live-workstation.ks
    %packages
    \&#35; Packages we want to have
    thunderbird
    \&#35; Package groups excluded from @workstation-product-environment
    -@guest-desktop-agents
    -@libreoffice
    -@multimedia
    \&#35; Packages excluded from @workstation-product
    -rhythmbox
    -unoconv
    \&#35; Packages excluded from @gnome-desktop
    -gnome-boxes
    -gnome-connections
    -gnome-text-editor
    -baobab
    -cheese
    -gnome-clocks
    -gnome-logs
    -gnome-maps
    -gnome-photos
    -gnome-remote-desktop
    -gnome-weather
    -orca
    -rygel
    -totem
    %end

What you see is a subsection of all possible options, because that git
checkout before, downloaded a full set of already working kickstart
files, which we will join up to one new kickstart.cfg file.

The above file will remove packages and groups of packages from the
later created image, compared to the normal Fedora-Live-Workstation
image. We call this a DELTA-file, because we just define the differences
between our image and the original Fedora Live Workstation image.

You see this:

    %include fedora-live-workstation.ks

This includes the original kickstart (ks) config for the original
Fedora-Live-Workstation Image as a base file. The rest of the lines
\'overwrite\' the sections in the original file. So you just tell
kickstart what you want and not want compared to the
Fedora-Live-Workstation image.

### Building the kickstart files

In this example, we removed some gnome-apps and end up what you know as
\'Fedora-Minimal-Workstation\' Image.

Take that example and save it to a file you can name i.E.
\'example-START.ks\'. Make sure you can distinguish your file later as
the starting point of your work. Because now, we will \'join\' aka.
\'flatten\' the included files to one big kickstart.cfg file, that we
will need for livemedia-creator later.

    $ ksflatten -c as-you-like-START.ks -o kickstart.cfg

The problem you are now facing is, it doesn't work out-of-box, because
ksflatten does not find all the includes it needs. You can solve this in
two ways:

a\) you move your ks file to the directory named \'fedora-kickstarts\'
and switch to it with cd, or

b\) you execute the above command and copy all files it names in the
errormessage from \'fedora-kickstarts\' to \'.\' until it stops
complaining.

From now on, you should only edit the created kickstart.cfg file for
changes, otherwise you have to repeat the next step over and over again.

### Fixing the \'Mount\'-bug

Either way, you end up with a defective cfg file, because the used
include files define the mountpoint \'/\' two times, which lead to an
error. That's easily fixed:

    \&#35; vim kickstart.cfg

search for \'&#35; Disk partitioning information\' and change the two
lines, that start with \'part /\' to this ONE line:

    part / --fstype='ext4' --size=8576

We will try to fix this, but it could take until Fedora 45.

### Creating the ISO {#create-the-iso}

Now the part you are waiting for: Let's create the iso image.

    livemedia-creator --ks kickstart.cfg --no-virt --resultdir /var/lmc --project MYPROJECTNAME --make-iso --volid MY_ID --iso-only --iso-name \&lt;FILENAME\&gt;.iso --releasever 42 --macboot

Please replace the following terms:

\'MYPROJECTNAME\' That is your internal project name, that ends up in
/etc/os-release \'MY_ID\' that is the name of the mounted ISO file AND
VERY IMPORTANT if you wanne refer to that iso in GRUB
\'&lt;FILENAME&gt;\' thats the name of the created iso file under
/var/lmc

In approximitly 15 minutes, if everything works, you have a created
&lt;filename&gt;.iso image IN YOUR TOOLBOX.

To get it out there, you enter &#8230;

    \&#35; exit

and copy it to the desired place. In example:

    \&#35; cp /var/lib/mock/fedora-42-x86_64/root/var/lmc/\&lt;filename\&gt;.iso /home/themasteruser/Downloads/Images/

Now you can test your image in different ways:

a\) you can use Gnome-Boxen to just run it in your desktop environment,
which is way easier.

or

b\) use the QEMU line in the next section.

Congratulations: You are done creating our own live-image. Some tips on
the way:

- If you need services running, check kickstart.cfg for syslive.service

- If you want to drop-in config files for the services, you have to
  build your own rpm.

- If you want to have your own packages inside the image, you need to
  add a custom repo. See \'repo\' in kickstart.cfg .

### Testing your live CD using KVM or qemu

![QEMU running Fedora 17](qemu_gtk3.png)

As root:

    \&#35; qemu-kvm -m 2048 -vga qxl -cdrom filename.iso

:::: note
::: title
:::

If you do not have
[KVM](https://en.wikipedia.org/wiki/Kernel-based_Virtual_Machine)
support, you have to use qemu instead.

    \&#35; qemu-system-x86_64 -m 2048 -vga qxl -cdrom filename.iso
::::

Replace &#96;\_filename.iso\_&#96; with the name of your created Live CD
image and &#96;\_qemu-system-x86_64\_&#96; with an appropriate qemu
binary for the target system, e.g. &#96;qemu-system-i386&#96;.

### Live image media verification

The live image can incorporate functionality to verify itself. To do so,
you need to have *isomd5sum* installed both on the system used for
creating the image and installed into the image. This is so that the
&#96;implantisomd5&#96; and &#96;checkisomd5&#96; utilities can be used.
These utilities take advantage of embedding an *md5sum* into the
application area of the iso9660 image. This then gets verified before
mounting the real root filesystem.

# Fedora on Raspberry Pi {#_fedora_on_raspberry_pi}

Flo H; jtagcat; The Fedora Docs Team

> The [Raspberry Pi](https://www.raspberrypi.org) is a credit card-sized
> ARM based single board computer (SBC). This documentation describes
> how to get started

The Raspberry Pi 3 series, 4 series, and Zero 2W are officially
supported, with support for the 3 being introduced in [Fedora
27](https://fedoraproject.org/wiki/Changes/aarch64SBCImages) and support
for the 4 and Zero 2W being introduced in [Fedora
37](https://fedoraproject.org/wiki/Changes/RaspberryPi4). This includes
hardware accelerated graphics, for which OSS support was previously
lacking.

However, Fedora decided to cut off support for (32 bit) armv7 / armhfp
as of [Fedora 37](https://fedoraproject.org/wiki/Changes/RetireARMv7),
so the Raspberry Pi 1 series, 2B, and Zero are no longer supported.

The Raspberry Pi 5 is not yet officially supported.

At the end of the document you find a Frequently Asked Questions (FAQ)
section about what is supported, and what is not.

:::: formalpara
::: title
Prerequisites
:::

&#42; A supported Raspberry Pi ([supported
boards](https://pagure.io/arm-image-installer/blob/main/f/boards.d)).
&#42; A power supply ([details on
raspberrypi.org](https://www.raspberrypi.org/documentation/computers/raspberry-pi.html&#35;power-supply)).
&#42;&#42; Zero 2 W: 2 Amps &#42;&#42; 3B and 3B+: 2.5 Amps &#42;&#42;
4B: 3.0 Amps &#42; HDMI-compatible Monitor or TV. &#42;&#42; A
Micro-HDMI to HDMI adapter/cable for the Raspberry Pi 4B. &#42;&#42; A
Mini-HDMI to HDMI adapter/cable for the Raspberry Pi Zero 2W. &#42; A
USB keyboard and USB mouse. &#42;&#42; A Micro USB to USB-A adapter,
possibly with a USB hub, for the Raspberry Pi Zero 2W, as it has only a
single Micro USB port for data. &#42; If using an SD card: &#42;&#42; A
microSD card reader. &#42;&#42; A microSD Card (16 GB or larger). &#42;
If using a USB flash drive, with USB boot: &#42;&#42; A USB flash drive,
preferably USB 3.0 or newer (16GB or larger) &#42; A computer running
Microsoft Windows, macOS, or Linux. &#42; A Fedora ARM aarch64 image,
such as Workstation or Server, from: <https://fedoraproject.org/>.
::::

The procedure for installing Fedora ARM on a microSD in preparation for
using Fedora on a Raspberry Pi depends on your computers\' operating
system (Microsoft Windows, macOS, or Linux).

&#42; For Fedora users, see: [Installing Fedora on a Raspberry Pi using
the Fedora ARM
installer](raspberry-pi.adoc&#35;_installing_fedora_on_a_raspberry_pi_using_the_fedora_arm_installer).
&#42; For users of other Linux distributions, see: [Installing Fedora on
a Raspberry Pi for Linux
users](raspberry-pi.adoc&#35;_installing_fedora_on_a_raspberry_pi_for_linux_users).
&#42; For Microsoft Windows users, see: [Installing Fedora on a
Raspberry Pi for Microsoft Windows
users](raspberry-pi.adoc&#35;_installing_fedora_on_a_raspberry_pi_for_microsoft_windows_users).
&#42; For macOS users, see: [Installing Fedora on a Raspberry Pi for
macOS
users](raspberry-pi.adoc&#35;_installing_fedora_on_a_raspberry_pi_for_macos_users).

:::: note
::: title
:::

For installation on &#42;&#42;Fedora Server Edition&#42;&#42; see [ARM
Single Board Computer (SBC)
Installation](fedora-server::installation/on-sbc.xml) and [Special:
Single Board Computers](fedora-server::server-on-sbc/index.xml).

For &#42;&#42;IoT Edition&#42;&#42; see [Reference
Platforms](iot::reference-platforms.xml)
::::

## Installing Fedora on a Raspberry Pi using the Fedora ARM installer {#_installing_fedora_on_a_raspberry_pi_using_the_fedora_arm_installer}

This procedure shows Fedora users how to add Fedora ARM to a microSD for
use with a Raspberry Pi using the Fedora ARM installer.

:::: formalpara
::: title
*Prerequisites*
:::

&#42; A supported Raspberry Pi &#42; A microSD Card (16 GB or larger).
&#42; A computer running Fedora 28 or newer. &#42; SD card reader. &#42;
A Fedora ARM aarch64 image, such as Workstation or Server, from:
<https://fedoraproject.org/>
::::

<div>

::: title
*Procedure*
:::

1.  Download a Fedora ARM image from the [Fedora
    website](https://fedoraproject.org/)

2.  Check the integrity of the download, following the instructions
    here: <https://fedoraproject.org/security>

3.  Install the &#96;arm-image-installer&#96;:

    ``` shell
    $ sudo dnf install -y arm-image-installer
    ```

4.  As the root user, write the Fedora ARM image to the microSD card:

    ``` shell
    $ sudo arm-image-installer \
    --image=\&\#60;/path/to/fedora_image\&\#62 \
    --target=\&\#60;RPi_Version\&\#62 \
    --media=/dev/__\&\#60;sd_card_device\&\#62 \
    --resizefs
    ```

    Where:

    &#42; The
    &#96;*&amp;&#35;60;/path/to/fedora_image&amp;&#35;62;*&#96; has the
    format
    &#96;Fedora-*&amp;&#35;60;spin&amp;&#35;62;*&amp;&#35;60;fedora_version*&amp;&#35;62;*.aarch64.raw.xz&#96;.
    &#42;&#42; For example:
    &#96;/home/user/Downloads/Fedora-Server-38-1.6.raw.xz&#96;. &#42;
    &#96;*&amp;&#35;60;RPi_Version&amp;&#35;62;*&#96; is: &#42;&#42;
    &#96;rpi2&#96; for a Raspberry Pi 2. &#42;&#42; &#96;rpi3&#96; for a
    Raspberry Pi 3. &#42;
    &#96;/dev/*&amp;&#35;60;sd_card_device&amp;&#35;62;*&#96; is the
    microSD card \'device\' on your system, such as &#96;/dev/sdX&#96;
    or &#96;/dev/mmcblkX&#96;. The &#96;lsblk&#96; command may help you
    identify your micro-SD card. &#42; \--resizefs: Resize the
    filesystem to occupy the entire SD card

    :::: note
    ::: title
    :::

    &#42; To see usage options for the &#96;arm-image-installer&#96;,
    run:

    \+

    ``` shell
    $ arm-image-installer --help
    ```

    &#42; For list of supported boards please check SUPPORTED-BOARDS
    file.

    \+

    ``` shell
    $ cat /usr/share/doc/arm-image-installer/SUPPORTED-BOARDS
    ```
    ::::

</div>

Your microSD card is ready to be used with your Raspberry Pi.

:::: formalpara
::: title
*Next Steps*
:::

For information on starting and configuring Fedora on Raspberry Pi, see:
[Booting Fedora on a Raspberry Pi for the first
time](raspberry-pi.adoc&#35;_booting_fedora_on_a_raspberry_pi_for_the_first_time).
::::

:::: formalpara
::: title
*Additional Resources*
:::

&#42; For information on using the Fedora ARM Installer, see: [Fedora
Wiki: Installing Fedora on your ARM
device](https://fedoraproject.org/wiki/Architectures/ARM/Installation).
&#42; For assistance or support, see: &#42;&#42; [Ask
Fedora](https://ask.fedoraproject.org/) &#42;&#42; [Fedora ARM mailing
list](https://lists.fedoraproject.org/admin/lists/arm%40lists.fedoraproject.org/)
&#42;&#42; [IRC via the &#35;fedora-arm channel on
Libera.Chat](https://web.libera.chat/?channels=&#35;fedora-arm)
::::

## Installing Fedora on a Raspberry Pi for Linux users {#_installing_fedora_on_a_raspberry_pi_for_linux_users}

This procedure shows Linux users how to add Fedora ARM to a microSD for
use with a Raspberry Pi.

:::: formalpara
::: title
*Prerequisites*
:::

&#42; A supported Raspberry Pi &#42; A microSD Card (16 GB or larger).
&#42; A computer running Linux. &#42; Root user access (via &#96;su&#96;
or &#96;sudo&#96;). &#42; SD card reader. &#42; A Fedora ARM aarch64
image, such as Workstation or Server, from:
<https://fedoraproject.org/>.
::::

<div>

::: title
*Procedure*
:::

1.  Download a Fedora ARM image from the [Fedora
    website](https://fedoraproject.org/).

2.  Run the following command to extract the &#96;.raw&#96; image and
    write the image to your microSD card:

    :::: note
    ::: title
    :::

    The location of your microSD card will be /dev/sdX or /dev/mmcblkX
    depending on your computer hardware.
    ::::

        $ xzcat \*Fedora-IMAGE-NAME.aarch64.raw.xz\* | sudo dd status=progress bs=4M of=\*/dev/XXX\*

3.  To resize the main partition, run &#96;parted&#96; and select the
    device.

        (parted) select /dev/sdX

4.  Inspect the amount of unallocated space at the end and resize the
    root partition.

        (parted) print free
        (parted) resizepart \&lt;partition_number\&gt; \&lt;target_size\&gt;

5.  Resize the LVM physical volume so it takes up all the available
    space. For this to work you must deactivate any logical volumes
    within.

        \&#35; pvresize /dev/sdaX

6.  Then extend the logical volume that corresponds to the root
    directory (&#96;/dev/fedora_fedora/root&#96; in this example).

        \&#35; lvextend -l +100%FREE /dev/fedora_fedora/root

7.  Finally, resize the XFS filesystem in the logical volume
    (&#96;/dev/mapper/fedora_fedora-root&#96; in this example).

        \&#35; xfs_growfs -d /dev/mapper/fedora_fedora-root

8.  Alternatively, you can use gparted to resize the Root Partition on
    the microSD:

        $ gparted /dev/XXX

    For information on using gparted resize a partition, see: [GNOME
    Partition Editor: GParted Manual - Resizing a
    Partition](https://gparted.org/display-doc.php?name=help-manual&#35;gparted-resize-partition).

    :::: note
    ::: title
    :::

    The root partition is shrunk to the smallest size possible to ensure
    a small download. You currently need to resize it manually. Ideally
    we would like this to happen automatically (great community project
    idea!).
    ::::

</div>

Your microSD card is ready to be used with your Raspberry Pi.

:::: formalpara
::: title
Next steps
:::

For information on starting and configuring Fedora on Raspberry Pi, see:
[Booting Fedora on a Raspberry Pi for the first
time](raspberry-pi.adoc&#35;_booting_fedora_on_a_raspberry_pi_for_the_first_time).
::::

:::: formalpara
::: title
Additional Resources
:::

&#42; For information on using &#96;gparted&#96;, see: [GNOME Partition
Editor: GParted
Manual](https://gparted.org/display-doc.php?name=help-manual). &#42; For
assistance or support, see: &#42;&#42; [Ask
Fedora](https://ask.fedoraproject.org/) &#42;&#42; [Fedora ARM mailing
list](https://lists.fedoraproject.org/admin/lists/arm%40lists.fedoraproject.org/)
&#42;&#42; [IRC via the &#35;fedora-arm channel on
Libera.Chat](https://web.libera.chat/?channels=&#35;fedora-arm)
::::

## Installing Fedora on a Raspberry Pi for Microsoft Windows users {#_installing_fedora_on_a_raspberry_pi_for_microsoft_windows_users}

This procedure shows Microsoft Windows users how to add Fedora ARM to a
microSD for use with a Raspberry Pi.

:::: formalpara
::: title
*Prerequisites*
:::

&#42; A supported Raspberry Pi &#42; A microSD Card (16 GB or larger).
&#42; A computer running Microsoft Windows. &#42; SD card reader. &#42;
A Fedora ARM aarch64 image, such as Workstation or Server, from:
<https://fedoraproject.org/>. &#42; File-decompression software (such as
[7zip](https://www.7-zip.org/)).
::::

<div>

::: title
*Procedure*
:::

1.  Download a Fedora ARM image from the [Fedora
    website](https://fedoraproject.org/).

2.  Extract the &#96;.raw&#96; file from the Fedora ARM image using
    file-decompression software (such as
    [7zip](https://www.7-zip.org/)).

    For example:

    ``` shell
    \> 'C:\Program Files\7-Zip\7z.exe' x -y 'C:\Users\admin\Downloads\Fedora-Server-38-1.6.aarch64.raw.xz'
    ```

3.  Follow the instructions provided by the Raspberry Pi foundation for
    writing an image to a microSD card from Microsoft Windows:
    [Raspberry Pi Foundation: Installing operating system images using
    Windows](https://www.raspberrypi.org/documentation/installation/installing-images/windows.md).

    :::: note
    ::: title
    :::

    The &#96;.img&#96; and &#96;.raw&#96; extensions are used
    interchangeably for RAW file. Where the instructions indicate an
    input file with the &#96;.img&#96; extension, use the Fedora ARM
    image \'.raw\'.
    ::::

</div>

Your microSD card is ready to be used with your Raspberry Pi.

:::: formalpara
::: title
*Next Steps*
:::

For information on starting and configuring Fedora on Raspberry Pi, see:
[Booting Fedora on a Raspberry Pi for the first
time](raspberry-pi.adoc&#35;_booting_fedora_on_a_raspberry_pi_for_the_first_time).
::::

:::: formalpara
::: title
*Additional Resources*
:::

&#42; For assistance or support, see: &#42;&#42; [Ask
Fedora](https://ask.fedoraproject.org/) &#42;&#42; [Fedora ARM mailing
list](https://lists.fedoraproject.org/admin/lists/arm%40lists.fedoraproject.org/)
&#42;&#42; [IRC via the &#35;fedora-arm channel on
Libera.Chat](https://web.libera.chat/?channels=&#35;fedora-arm)
::::

## Installing Fedora on a Raspberry Pi for macOS users {#_installing_fedora_on_a_raspberry_pi_for_macos_users}

This procedure shows macOS users how to add Fedora ARM to a microSD for
use with a Raspberry Pi.

:::: formalpara
::: title
*Prerequisites*
:::

&#42; A supported Raspberry Pi &#42; A microSD Card (16 GB or larger).
&#42; A computer running macOS. &#42; SD card reader. &#42; A Fedora ARM
aarch64 image, such as Workstation or Server, from:
<https://fedoraproject.org/>. &#42; File-decompression software (such as
[The Unarchiver desktop application](https://theunarchiver.com/) or [The
Unarchiver command-line tools](https://theunarchiver.com/command-line)).
::::

<div>

::: title
*Procedure*
:::

1.  Download a Fedora ARM image from the [Fedora
    website](https://arm.fedoraproject.org/).

2.  Extract the &#96;.raw&#96; file from the Fedora ARM image using
    file-decompression software (such as [The
    Unarchiver](https://theunarchiver.com/))

    For example:

    ``` shell
    $ unrar Fedora-Server-38-1.6.aarch64.raw.xz
    ```

3.  Follow the instructions provided by the Raspberry Pi foundation for
    writing an image to a microSD card from macOS: [Raspberry Pi
    Foundation: Installing operating system images on Mac
    OS](https://www.raspberrypi.org/documentation/installation/installing-images/mac.md).

    :::: note
    ::: title
    :::

    The &#96;.img&#96; and &#96;.raw&#96; extensions are used
    interchangeably for RAW file. Where the instructions indicate an
    input file with the &#96;.img&#96; extension, use the Fedora ARM
    image \'.raw\'.
    ::::

</div>

Your microSD card is ready to be used with your Raspberry Pi.

:::: formalpara
::: title
*Next Steps*
:::

For information on starting and configuring Fedora on Raspberry Pi, see:
[Booting Fedora on a Raspberry Pi for the first
time](raspberry-pi.adoc&#35;_booting_fedora_on_a_raspberry_pi_for_the_first_time)..
::::

:::: formalpara
::: title
*Additional Resources*
:::

&#42; For assistance or support, see: &#42;&#42; [Ask
Fedora](https://ask.fedoraproject.org/) &#42;&#42; [Fedora ARM mailing
list](https://lists.fedoraproject.org/admin/lists/arm%40lists.fedoraproject.org/)
&#42;&#42; [IRC via the &#35;fedora-arm channel on
Libera.Chat](https://web.libera.chat/?channels=&#35;fedora-arm)
::::

## Booting Fedora on a Raspberry Pi for the first time {#_booting_fedora_on_a_raspberry_pi_for_the_first_time}

Follow these steps to boot Fedora ARM on your Raspberry Pi. If your
MicroSD card does not have enough room, you need to resize the main
partition after the initial setup. See
&lt;&lt;resizing-the-main-partition-of-the-microsd-card-after-setup&gt;&gt;.

:::: formalpara
::: title
*Prerequisites*
:::

&#42; Raspberry Pi 3-series, 4-series, or Zero 2W. &#42; A power supply
([details
here](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html&#35;power-supply)).
&#42;&#42; Recommended 2.5 Amps, Micro USB, for Raspberry Pi 3 Model B
and B+. &#42;&#42; Recommended 3 Amps, USB-C, for the Raspberry Pi 4
Model B. &#42;&#42; Recommended 2 Amps, Micro USB, for the Raspberry Pi
Zero 2W. &#42; HDMI-compatible Monitor or TV. &#42;&#42; A Micro-HDMI to
HDMI adapter/cable for the Raspberry Pi 4B. &#42;&#42; A Mini-HDMI to
HDMI adapter/cable for the Raspberry Pi Zero 2W. &#42; A USB keyboard
and USB mouse. &#42;&#42; A Micro USB to USB-A adapter, possibly with a
USB hub, for the Raspberry Pi Zero 2W, as it has only a single Micro USB
port for data. &#42; The MicroSD card with Fedora imaged to it.
::::

<div>

::: title
*Procedure*
:::

1.  Insert the SD card into the Raspberry Pi.

2.  Connect a keyboard, mouse, monitor, and optionally network cable.

3.  Plug the Raspberry Pi into the power source. The \'Initial setup
    wizard\' should appear after Fedora loads.

4.  Follow the wizard to set your language, timezone and to create
    users.

</div>

The system displays a login prompt or getting started guide (depending
on your Desktop/SPIN).

:::: {#resizing-the-main-partition-of-the-microsd-card-after-setup .formalpara}
::: title
*Resizing the main partition of the microSD card after setup (if
required)*
:::

Follow these steps to resize the partitions for Fedora ARM on Raspberry
Pi:
::::

1.  Enlarge the 4th partition (this example uses mmcblk0).

        $ growpart /dev/mmcblk0p4

2.  &#96;growpart&#96; may not be sufficient in the case of server image
    which uses LVM. Use &#96;vgs&#96; to determine the volume group
    name.

        $ vgs

3.  Use &#96;lvextend&#96; to extend the logical volume. Assuming
    &#96;vgs&#96; lists *systemVG-LVRoot* as the volume group name, it
    looks like:

        $ lvextend -r -l +100%FREE /dev/mapper/systemVG-LVRoot

4.  Resize root partition for the server image (which uses xfs).

        $ xfs_growfs -d /

:::: formalpara
::: title
*Additional Resources*
:::

&#42; For assistance or support, see: &#42;&#42; [Ask
Fedora](https://ask.fedoraproject.org/) &#42;&#42; [Fedora ARM mailing
list](https://lists.fedoraproject.org/admin/lists/arm%40lists.fedoraproject.org/)
&#42;&#42; [IRC via the &#35;fedora-arm channel on
Freenode](irc://irc.freenode.net/&#35;fedora-arm)
::::

## Fedora on Raspberry Pi: Frequently Asked Questions {#sect-frequently-asked-questions}

Frequently asked questions regarding what is supported.

### Why do I get a rainbow display when I try and power on my Raspberry Pi? {#_why_do_i_get_a_rainbow_display_when_i_try_and_power_on_my_raspberry_pi}

The rainbow display will appear for a second at the start of the boot
process when the GPU firmware loads. However, if it persists, there is
likely a problem preventing the Pi from booting.

Common causes of the rainbow display include:

&#42; Insufficient power supply. See the
[Prerequisites](#raspberry-pi-prerequisites) section at the beginning of
this document.

&#42; There's no operating system installed. Check that an operating
system was installed and the microSD card was properly inserted into the
Raspberry Pi. For instructions about Fedora ARM on Raspberry Pi:
&#42;&#42; For Fedora users, see:
&lt;&lt;installing-fedora-on-a-raspberry-pi-using-the-fedora-arm-installer&gt;&gt;.
&#42;&#42; For users of other Linux distributions, see:
&lt;&lt;installing-fedora-on-a-raspberry-pi-for-linux-users&gt;&gt;.
&#42;&#42; For Microsoft Windows users, see:
&lt;&lt;installing-fedora-on-a-raspberry-pi-for-microsoft-windows-users&gt;&gt;.
&#42;&#42; For macOS users, see:
&lt;&lt;installing-fedora-on-a-raspberry-pi-for-macos-users&gt;&gt;.

&#42; If you try to use Fedora on a Raspberry Pi 1, Raspberry Pi 2,
Raspberry Pi Zero, or a Raspberry Pi model A, you will receive the
rainbow display. This occurs because your Raspberry Pi is not supported
(ARMv6 and ARMv7 SoCs architectures are not supported).

### What desktop environments are supported? {#_what_desktop_environments_are_supported}

All desktops as shipped in Fedora should work and both 2D and 3D
graphics work out of the box. There is an open source fully accelerated
driver for the Video Core IV GPU.

### Will there be more enhancements to the hardware support? {#_will_there_be_more_enhancements_to_the_hardware_support}

Yes. New enhancements will be delivered by the standard Fedora updates
mechanism. New, significant features will be announced by the [Fedora
Magazine](https://fedoramagazine.org/) or the [Fedora
Planet](http://fedoraplanet.org/).

### What about support for the Raspberry Pi Models A/A+, B/B+ (generation 1), 2, Zero/ZeroW, and Compute Module (generation 1)? {#_what_about_support_for_the_raspberry_pi_models_aa_bb_generation_1_2_zerozerow_and_compute_module_generation_1}

These Raspberry Pi models are not supported.

Fedora is not supported on ARMv6 or ARMv7 processors. There's been a
number of attempts to support these over the years. The current best
effort for ARMv6 is Pignus based on Fedora 23. More information can be
found at [the Pignus site](https://pignus.computer). As ARMv7 support
was retired with Fedora 37, the best option for the Raspberry Pi 2 is
likely to use Fedora 36.

:::: note
::: title
:::

Fedora DOES support the Compute Module 3 based on the same SoC as the
Raspberry Pi 3, but &#42;as the previous generation Compute Modules are
based on ARMv6 architecture, they are \[&#35;.underline\]&#35;not
supported&#35;&#42;.
::::

### What USB devices are supported on the Raspberry Pi? {#_what_usb_devices_are_supported_on_the_raspberry_pi}

Most USB2 and USB3 compatible devices that are supported in Fedora on
other devices. There are some limitations to the USB bus of the
Raspberry Pi hardware prior to the Raspberry Pi 4 as [documented
here](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html&#35;universal-serial-bus-usb).

### Is the onboard Wi-Fi supported on the Raspberry Pi 3, 4, and Zero 2W? {#_is_the_onboard_wi_fi_supported_on_the_raspberry_pi_3_4_and_zero_2w}

Wifi on the Raspberry Pi 3-series, 4-series, and Zero 2W devices works
out of the box with all supported versions of Fedora.

&#42;Using Wi-Fi on CLI&#42;

To use Wi-Fi on minimal and server images you can configure the device
using command line:

&#42; To list available networks:

\+

    $ nmcli device wifi list

&#42; To connect to a network:

\+

    nmcli device wifi connect $SSID --ask

\+ Where: &#96;\_\$SSID\_&#96; is the network identifier (or name).

### Is the onboard Bluetooth supported on the Raspberry Pi 3, 4, and Zero 2W? {#_is_the_onboard_bluetooth_supported_on_the_raspberry_pi_3_4_and_zero_2w}

Bluetooth works and is stable. The device sometimes has a generic
bluetooth address but should work without any configuration.

### Does sound work? {#_does_sound_work}

HDMI audio output is included with Fedora, however, the analog port is
not yet supported. Audio output using a USB audio interface should work.

### Does the add-on camera work? {#_does_the_add_on_camera_work}

Not at this time. There is still ongoing work to support this upstream
and to add the appropriated media acceleration support.

### Does accelerated media decode work? {#_does_accelerated_media_decode_work}

No. The upstream kernel does not support the kernel subsystems required
for accelerated media decoding.

### Does HDMI-CEC work? {#_does_hdmi_cec_work}

Yes. Yes. It's supported using the new upstream CEC support. There's a
&#96;/dev/cec0&#96; character device, it can be accessed using any
application that supports the IR remote using the &#96;rc-cec&#96;
keymap in the &#96;v4l-utils&#96; package, there's also a
&#96;cec-ctl&#96; utility for use on the command line.

### Is the Raspberry Pi Touch Display supported? {#_is_the_raspberry_pi_touch_display_supported}

Work on the official Raspberry Pi Touch Display is ongoing upstream and
initial support is provided in the 4.10 kernel, see: [GitHub:
raspberrypi/linux issues - 7\' LCD touchscreen not
supported](https://github.com/anholt/linux/issues/8). Fedora will review
any missing pieces for support soon. The touchscreen driver isn't yet
released upstream. Support for other displays is not currently planned.

### Is the composite TV out supported? {#_is_the_composite_tv_out_supported}

The composite TV out is not currently supported in a stable Fedora
release but the core support is in the 4.10 kernel. There is some
missing enabling patches which will be added to the Fedora kernel soon.

### Are the expansion HATs supported? {#_are_the_expansion_hats_supported}

The expansion HATs are not currently supported.

The long answer is a lot more complex. Most of the hardware interfaces
that are exposed by the 40 pin HAT connector are supported with drivers
shipped with Fedora.

Drivers for the hardware contained on a lot of the common HATs are also
enabled and supported in Fedora. The core means of supporting the HAT
add-on boards require the use of device tree overlays. The kernel and
the u-boot 2016.09 boot-loader supports the loading over overlays
manually. Currently there is no upstream consensus on the means of
autoloading these overlays by means of an \'overlay manager\' (also
known as Cape Manager and by numerous other names) by reading the EEPROM
ID and loading the appropriate overlay automatically.

There's also no consensus on the extensions to the dtc (Device Tree
Compiler) to build the binary blob overlays, and no consensus of the
exact format of the overlay file. There is now a group of people working
to resolve this issue which enable Fedora to better support HATs
(Raspberry Pi), Capes (BeagleBone), DIPs (C.H.I.P) and Mezzanine
(96boards) before long.

The first focus HAT to support will be the official Raspberry Pi Sense
HAT. This will be documented using the manual process to build and load
the overlay to provide access to the onboard devices as a means of
demonstrating how this process works for those wishing to use this
manual method in the interim. The link to this documentation will be
added here once that is complete.

### The use of config.txt {#_the_use_of_config_txt}

The &#96;config.txt&#96; is only used for basic configuration at the
moment. Because of the use of the opensource vc4 GPU driver, most of the
video configuration is done by Linux.

The configuration of HATs using &#96;config.txt&#96; is unsupported but
is being actively developed.

### Are Device Tree Overlays supported? {#_are_device_tree_overlays_supported}

There's basic support for overlays in u-boot and the Linux kernel but an
overlay manager is not supported upstream.

### Is GPIO supported? {#_is_gpio_supported}

GPIO is supported with the use of libgpiod and associated bindings and
utilities.

RPI.GPIO is not currently supported.

### Is SPI supported? {#_is_spi_supported}

Yes, basic SPI is supported.

### Is I2C supported? {#_is_i2c_supported}

Yes, basic I2C is supported.

### Is there Raspberry Pi 3 aarch64 support? {#_is_there_raspberry_pi_3_aarch64_support}

Yes! You can download the aarch64 disk images for the Raspberry Pi 3
[here.](https://archive.fedoraproject.org/pub/fedora-secondary/releases/)

### How do I use a serial console? {#_how_do_i_use_a_serial_console}

The serial console is disabled by default on the Raspberry Pi 2 and 3
because it requires the device to run at significantly slower speeds.

To wire up the USB to TTL adapter follow [this guide from
Adafruit](https://learn.adafruit.com/adafruits-raspberry-pi-lesson-5-using-a-console-cable/connect-the-lead).
You'll need a 3.3 volt USB to TTL Serial Cable like [this one from
Adafruit](https://www.adafruit.com/product/954).

To enable the serial console follow the specific steps for the Raspberry
Pi 2 or 3 as they both differ slightly:

&#42;Raspberry Pi 2:&#42;

1.  Insert the microSD card into a PC

2.  On the VFAT partition edit the &#96;config.txt&#96; file and
    uncomment the &#96;enable_uart&#96; line:

        $ enable_uart=1

3.  On the boot partition edit the &#96;extlinux/extlinux.conf&#96; file
    adding &#96;console=tty0 console=ttyAMA0,115200&#96; to the end of
    the append line so it looks similar to:

        $ append ro root=UUID='LARGE UUID STRING OF TEXT' console=tty0 console=ttyAMA0,115200

4.  Safely unmount the microSD card

5.  Insert microSD into Raspberry Pi, connect serial console, power on

&#42;Raspberry Pi 3:&#42;

1.  Insert the microSD card into a PC

2.  On the VFAT partition edit the &#96;config.txt&#96; file and
    uncomment the &#96;enable_uart&#96; line:

        $ enable_uart=1

3.  On the boot partition edit the &#96;extlinux/extlinux.conf&#96; file
    adding: &#96;console=tty0 console=ttyS0,115200&#96; to the end of
    the append line so it looks similar to:

        $ append ro root=UUID='LARGE UUID STRING OF TEXT' console=tty0 console=ttyS0,115200

4.  Safely unmount the microSD card

5.  Insert microSD into Raspberry Pi, connect serial console, power on

## Additional Resources {#_additional_resources}

&#42; The most up-to-date information can be found on the [Raspberry Pi
page](https://fedoraproject.org/wiki/Architectures/ARM/Raspberry_Pi?rd=Raspberry_Pi)
of the Fedora Wiki. &#42; For Raspberry Pi hardware specifications and
project ideas, see: [The Raspberry Pi Foundation
Website](https://www.raspberrypi.org/). &#42; For assistance or support,
see: &#42;&#42; [Ask Fedora](https://ask.fedoraproject.org/) &#42;&#42;
[Fedora ARM mailing
list](https://lists.fedoraproject.org/admin/lists/arm%40lists.fedoraproject.org/)
&#42;&#42; [IRC via the &#35;fedora-arm channel on
Libera.Chat](https://web.libera.chat/?channels=&#35;fedora-arm)

# Anaconda:The Fedora Installer {#_anacondathe_fedora_installer}

Ankur Sinha ; Frank Sträter ; Timothée Ravier :page-aliases:
anaconda/anaconda.adoc

![Anaconda](DSC_3217.JPG)

> Anaconda is the installation program used by Fedora, Red Hat
> Enterprise Linux and some other distributions.

During installation, a target computer's hardware is identified and
configured, and the appropriate file systems for the system's
architecture are created. Finally, Anaconda allows the user to install
the operating system software on the target computer. Anaconda can also
upgrade existing installations of earlier versions of the same
distribution. After the installation is complete, you can reboot into
your installed system and continue doing customization using [initial
setup](https://fedoraproject.org/wiki/InitialSetup).

Anaconda is a fairly sophisticated installer. It supports installation
from local and remote sources such as CDs and DVDs, images stored on a
hard drive, NFS, HTTP, and FTP. Installation can be scripted with
[kickstart](https://pykickstart.readthedocs.io/en/latest/) to provide a
fully unattended installation that can be duplicated on scores of
machines. It can also be run over VNC on headless machines. A variety of
advanced storage devices including LVM, RAID, iSCSI, and multipath are
supported from the partitioning program. Anaconda provides advanced
debugging features such as remote logging, access to the python
interactive debugger, and remote saving of exception dumps.

If you are an advanced user of Anaconda, you should check out [our
reference to Anaconda command line
options](https://anaconda-installer.readthedocs.io/en/latest/boot-options.html),
[our kickstart file format
documentation](https://anaconda-installer.readthedocs.io/en/latest/kickstart.html)
and [our reference to logging capabilities of
Anaconda](anaconda/anaconda_logging.xml).

# Anaconda Logging {#_anaconda_logging}

Yohaan Vakil; Frank Sträter ; Ben Cotton :page-aliases:
anaconda/anaconda_logging.adoc

## Introduction {#_introduction}

Anaconda tracks all of its activities in logs. This includes:

&#42; changing installation steps (that roughly correspond to different
screens in the graphical installer) &#42; storage devices detection and
manipulation &#42; installation media detection &#42; network
initialization &#42; kernel messages &#42; calls to critical methods
within anaconda &#42; calls to external programs

## Logging on the installed system {#_logging_on_the_installed_system}

During the installation the logs are stored in the &#96;/tmp&#96;
directory:

### Log files {#_log_files}

&#96;/tmp/anaconda.log&#96;

:   the general installation information, particularly the step changes.

&#96;/tmp/storage.log&#96;

:   storage devices scan and manipulation (hard drives, partitions, LVM,
    RAID), partitioning

&#96;/tmp/program.log&#96;

:   calls to external programs, their output

&#96;/tmp/packaging.log&#96;

:   [DNF](dnf.xml) package installation messages

&#96;/tmp/syslog&#96;

:   hardware-related system messages

Certain log messages are also written to the terminals:

### TTY devices {#_tty_devices}

&#96;/dev/tty3&#96;

:   messages from &#96;anaconda.log&#96;, &#96;storage.log&#96; and
    &#96;packaging.log&#96;.

&#96;/dev/tty4&#96;

:   same as &#96;syslog&#96;

&#96;/dev/tty5&#96;

:   stdout and stderr from external programs\

&#96;tty3&#96; and &#96;tty4&#96; reflect certain log files. Log files
always contain messages from all the loglevels, including debug, but the
minimal loglevel on the terminals can be controlled with the
&#96;loglevel&#96; [command line
option](https://anaconda-installer.readthedocs.io/en/latest/boot-options.html&#35;inst-loglevel).

There are two other log files created on the target filesystem, in the
&#96;/root&#96; directory, also accessible at
&#96;/mnt/sysimage/root&#96; during the installation:

&#96;/mnt/sysimage/root/install.log&#96;

:   log of the package installation process.

&#96;/mnt/sysimage/root/install.log.syslog&#96;

:   messages from installation chroot logged through the system's
    syslog.

Mostly information about users and groups created during dnf's package
installation.

### Log format {#_log_format}

In files the format of the log messages is as follows:

    H:M:S,ms LOGLEVEL facility:message

where:

&#42; &#96;H:M:S&#96; is the message timestamp &#42; &#96;ms&#96; is the
millisecond part of timestamp. Note that this will usually become zero
on a remote syslog. &#42; &#96;LOGLEVEL&#96; is the message loglevel. In
theory, because kernel messages are part of anaconda logs, all loglevels
that are defined in rsyslog can appear in the logfiles. Anaconda itself
will however log only at the following loglevels: &#42;&#42;
&#96;DEBUG&#96; &#42;&#42; &#96;INFO&#96; &#42;&#42; &#96;WARN&#96;
&#42;&#42; &#96;ERR&#96; &#42;&#42; &#96;CRIT&#96; &#42;
&#96;facility&#96; is the program or component that created the message.
Could be for instance &#96;kernel&#96;, &#96;anaconda&#96;,
&#96;storage&#96; or similar. &#42; &#96;message&#96; is the log message
itself.

For the logs running in terminals, the format simply is:

    LOGLEVEL facility:message

## Remote logging via TCP {#_remote_logging_via_tcp}

Anaconda supports remote logging handled through the rsyslog daemon
running on the installed system. It can be configured to forward its
logs through TCP to an arbitrary machine in network that is also running
a syslog daemon. This is controlled with the &#96;syslog&#96; [command
line
option](https://anaconda-installer.readthedocs.io/en/latest/boot-options.html&#35;inst-syslog).

:::: warning
::: title
:::

Do not forget to enable the port you are running your local syslog
daemon on in your firewall.
::::

### What is logged remotely {#_what_is_logged_remotely}

Everything that is logged directly by anaconda should also appear in the
remote logs. This includes messages emitted by the loader and the
storage subsystem. All anaconda tracebacks (/tmp/anaconda-tb-xyz) are
concatenated into a single file /tmp/anaconda-tb-all.log and then
transferred. Also, /tmp/x.log is transferred.

The remote logging only works when the installer initializes network.
Once network is up, it takes a couple of minutes for rsyslogd to realize
this. Rsyslog has a queue for messages that couldn't be forwarded
because of inaccessible network and it eventually forwards all of them,
in the correct order.

### Configuration {#_configuration}

It's up to you how the remote logging daemon is configured, you can for
instance log all incoming messages into one file or sort them into
directories according to the IP address of the remote system.

The anaconda RPM provides the &#96;analog&#96; script, which generates a
suitable rsyslogd configuration file based on a couple of install
parameters. It is also able to generate a bash command to launch
rsyslogd with the generated configuration. Thus you can do from a shell:
&#96;\$ eval scripts/analog -p 6080 -s -o ./someconf
/home/akozumpl/remote_inst&#96; This starts an rsyslog daemon that will
listen on port 6080. The logs from the remote machine with IP
10.34.33.221 will be stored under
&#96;/home/akozumpl/remote_inst/10.34.33.221/&#96;, e.g.
&#96;/home/akozumpl/remote_inst/10.34.33.221/anaconda.log&#96;.

The remote syslog configuration exploits several log message
characteristics to be able to sort them into the correct files: &#42;
the IP of the message sender to know which machine generated the message
and thud what directory does the message belong to. &#42;
&#96;anaconda.log, storage.log&#96; and &#96;program.log&#96; have the
name embedded in them as &#96;programname&#96;. &#42; &#96;syslog&#96;
messages are coming in from kernel and daemon facilities, just like they
do on the installed system &#42; &#96;install.log.syslog&#96; made
during package installation is logged as a special &#96;sysimage&#96;
hostname.

Run &#96;analog&#96; without the &#96;-o&#96; option to see how exactly
does a fitting configuration file look like. Also notice that it uses
the same message format for remote logging as anaconda does, but you can
of course modify this to specify any format you want.

### See also {#_see_also}

&#42; [Rsyslog
documentation](https://www.rsyslog.com/doc/master/index.html) &#42;
&#96;man tailf&#96;

## Remote logging via virtio {#_remote_logging_via_virtio}

QEMU/KVM in Fedora 13 and onwards allows one to create virtual machines
with [multiple virtio char
devices](https://fedoraproject.org/wiki/Features/VirtioSerial) exposed
to the guest machine. One such device can be used to forward anaconda
logs to the host machine. In that way we can get logs forwarded in real
time, as soon the anaconda logging subsystem is initialized (early) and
not need to wait for the network to come up. Also, it's the only way to
forward the logs in a no-network setup.

### Remote Logging Configuration {#_remote_logging_configuration}

Anaconda will be forwarding logs over virtio automatically if it is able
to find the port
&#96;/dev/virtio-ports/org.fedoraproject.anaconda.log.0\'&#96;. This is
port is created using a libvirt XML directive that wires it to a TCP
socket on the host's side. It's then possible to read the logs from
there directly, or make an rsyslog instance to parse them and file them
into respective files. See the ascii chart below for the whole ensemble:

    Anaconda---\&gt;rsyslog(guest)---\&gt;virtio(guest char device)---\&gt;kvm hypervisor---\&gt;virtio(TCP socket)
    |
    v
    forwarded log files\&lt;---rsyslog(host)

Step by step instructions to set everything up follow:

1.  Create a testing virtual machine, e.g. using Virtual Manager
    &lt;/li&gt;

2.  Add the virtio-serial port to your virtual machine, direct it to the
    TCP port 6080 on the host. Start by editing the guest
    configuration:&#96;virsh edit &lt;machine name&gt;&#96;

3.  In the guest editor, add following information into the
    &#96;&lt;devices&gt;&#96; section:

<!-- -->

    \&lt;channel type='tcp'\&gt;
    \&lt;source mode='connect' host='127.0.0.1' service='6080'/\&gt;
    \&lt;target type='virtio' name='org.fedoraproject.anaconda.log.0'/\&gt;
    \&lt;/channel\&gt;

1.  Start the listening rsyslogd process on the host, using the
    &#96;analog&#96; script described
    \[\[&#35;Remote_logging_via_TCP\|above\]\]:

<!-- -->

    eval \&#96;analog -p 6080 -o rsyslogd.conf -s /home/akozumpl/remote_inst\&#96;

1.  Start the virtual machine.

2.  Continue with the installation. Immediately after the Anaconda
    greeting is displayed the log messages will appear in the directory
    given to &#96;analog&#96; script, in the &#96;127.0.0.1&#96;
    subdirectory.

#### virt-install {#_virt_install}

If you are using virt-install you can configure it with the \--channel
option:

    --channel tcp,host=127.0.0.1:6080,mode=connect,target_type=virtio,name=org.fedoraproject.anaconda.log.0

### Known issues and troubleshooting {#_known_issues_and_troubleshooting}

&#42; works in libvirt&gt;=0.8.2 &#42; chroot syslog messages from
&#96;/mnt/sysimage/root/install.log.syslog&#96; are not forwarded. &#42;
it is not possible to start the machine unless something is listening on
the TCP port where virtio-serial is connected. &#42; if you want to test
that the virtio connection is working, instead of using analog and
rsyslog just let a netcat utility listen on the given port, e.g. &#96;nc
-l 0.0.0.0 6080&#96;. You should start seeing raw logs in the terminal
once the guest machine starts booting. &#42; if both remote TCP logging
via &#96;syslog=&#96; and remote virtio logging via &#96;virtiolog=&#96;
are specified on the command line, one has to setup two rsyslogd
instances on the server/host to listen to both the connections otherwise
the sending rsyslog's queues get full and the forwarding stops.

### See also {#_see_also_2}

&#42;
[VirtioSerial](https://fedoraproject.org/wiki/Features/VirtioSerial)
&#42; [Virtio at the libvirt wiki](https://wiki.libvirt.org/page/Virtio)
&#42; [libvirt domain XML
format](https://libvirt.org/formatdomain.html&#35;elementsConsole)

## Anaconda logs on the running system {#_anaconda_logs_on_the_running_system}

After every successful installation, anaconda logs are copied into
&#96;/var/log&#96; on the system you just installed. To avoid name
clashes with other log files there, the anaconda logs are renamed:

+-----------------------------------------------------------------------+
| Name during installation                                              |
+=======================================================================+
| Name on the target system                                             |
+-----------------------------------------------------------------------+
| &#96;/tmp/anaconda.log&#96;                                           |
+-----------------------------------------------------------------------+
| &#96;/var/log/anaconda/anaconda.log&#96;                              |
+-----------------------------------------------------------------------+
| &#96;/tmp/program.log&#96;                                            |
+-----------------------------------------------------------------------+
| &#96;/var/log/anaconda/program.log&#96;                               |
+-----------------------------------------------------------------------+
| &#96;/tmp/storage.log&#96;                                            |
+-----------------------------------------------------------------------+
| &#96;/var/log/anaconda/storage.log&#96;                               |
+-----------------------------------------------------------------------+
| &#96;/tmp/packaging.log&#96;                                          |
+-----------------------------------------------------------------------+
| &#96;/var/log/anaconda/packaging.log&#96;                             |
+-----------------------------------------------------------------------+

## Logging tips {#_logging_tips}

If you are asked to provide logs for a bugzilla, your best option is
switching from the anaconda GUI to tty2 and then use scp to copy the
files to your computer, e.g.:

``` bash
$ cd /tmp
$ scp anaconda.log aklap:/home/akozumpl/
```

It is also possible to make a complete dump of a state of running
anaconda process (the same dump that is compiled automatically if an
unhandled exception occurs). To do this send the main anaconda process
SIGUSR2:

``` bash
$ kill -USR2 \&#96;cat /var/run/anaconda.pid\&#96;\&#96;
```

This builds a file &#96;/tmp/anaconda-tb-?????&#96; that also contains
&#96;anaconda.log&#96;, &#96;storage.log&#96; and &#96;syslog&#96;.

If you are on a KVM virtual machine and there's no scp available
(stage1), you can (after setting up the network if not up already)
redirect to a special tcp file, on host:

``` bash
$ nc -l 4444 \&gt; syslog.log
```

on guest:

``` bash
$ ifconfig eth0 10.0.2.10/24 up
$ grep '' /tmp/syslog \&gt; /dev/tcp/10.0.2.2/4444
```

&#42; Accessibility

&#42; AI = Getting Started with Ollama Sumantro Mukherjee;

Ollama is a command-line tool that makes it easy to run and manage large
language models (LLMs) locally. It supports running models such as
LLaMA, Mistral, and others directly on your machine with minimal setup.
Fedora 42 introduces native support for Ollama, making it easier than
ever for developers and enthusiasts to get started with local LLMs.

:::: warning
::: title
:::

Ollama is officially available only on Fedora 42 and above. Attempting
to install on earlier versions may result in errors or broken
dependencies.
::::

## Installation {#_installation}

Installing Ollama is straightforward using Fedora's native package
manager. Open a terminal and run:

``` _bash
sudo dnf install ollama
```

This command installs the Ollama CLI and its supporting components.

## Basic Usage {#_basic_usage}

Once installed, you can start using Ollama immediately. Below are a few
basic commands to get you started:

### Run a Model {#_run_a_model}

To download and run a supported LLM (e.g., &#96;llama2&#96;):

``` _bash
ollama run llama2
```

This command pulls the model if it's not already downloaded, and starts
a local session.

### Pull a Model Without Running {#_pull_a_model_without_running}

``` _bash
ollama pull mistral
```

This will download the &#96;mistral&#96; model without starting it.

### List Installed Models {#_list_installed_models}

``` _bash
ollama list
```

Shows all models currently available on your system.

### Remove a Model {#_remove_a_model}

``` _bash
ollama rm llama2
```

Cleans up disk space by removing a previously downloaded model.

## Learn More {#_learn_more}

To explore supported models and advanced configurations, visit the
upstream project:

<https://ollama.com/>

# Getting Started with PyTorch on Fedora 42 {#_getting_started_with_pytorch_on_fedora_42}

Sumantro Mukherjee;

PyTorch is an open-source machine learning framework developed by Meta
AI. It provides dynamic computational graphs and automatic
differentiation, making it highly flexible and popular in both academia
and industry. At its core, the &#96;torch&#96; module in PyTorch offers
powerful tensor computation, similar to NumPy, but with GPU
acceleration.

With Fedora 42, PyTorch is now available directly through the system
package manager, making installation and updates seamless for users.

## Installation {#_installation_2}

You can install PyTorch using the Fedora package manager:

``` _bash
sudo dnf install python3-torch
```

This installs the core &#96;torch&#96; package and dependencies required
to start developing with PyTorch.

You can also use pip to install Pytorch:

``` _bash
pip install torch
```

Setting up local development with CUDA is very well documented here
<https://pytorch.org/get-started/locally/>

## Basic Usage {#_basic_usage_2}

After installation, you can verify the install and start working with
tensors immediately.

### Import and Version Check {#_import_and_version_check}

``` _python
import torch

print('PyTorch version:', torch.__version__)
print('CUDA available:', torch.cuda.is_available())
```

### Tensor Creation {#_tensor_creation}

``` _python
import torch

\&#35; Create a 1D tensor
a = torch.tensor([1.0, 2.0, 3.0])
print('Tensor a:', a)

\&#35; Random tensor
b = torch.rand(3)
print('Tensor b:', b)

\&#35; Add two tensors
c = a + b
print('Sum a + b:', c)
```

## Learn More {#_learn_more_2}

For tutorials, model zoo, and full documentation, visit:

- <https://pytorch.org/>

- <https://docs.fedoraproject.org/>

## Feedback {#_feedback}

If you encounter issues or have suggestions for the Fedora package, file
a bug at <https://bugzilla.redhat.com> or join the Fedora AI SIG.

&#42; Adding and managing software = Automatic Updates Ben Cotton; Petr
Bokoc; Jean-Baptiste Holcroft

You must decide whether to use automatic [DNF](dnf.xml) updates on each
of your machines. There are a number of arguments both for and against
automatic updates to consider. However, there is no single answer to
this question: it is up to the system administrator or owner of each
machine to decide whether automatic updates are desirable or not for
that machine. One of the things which makes one a good system
administrator is the ability to evaluate the facts and other people's
suggestions, and then decide for oneself what one should do.

A general rule that applies in most cases is as follows:

*If the machine is a critical server, for which unplanned downtime of a
service on the machine can not be tolerated, then you should not use
automatic updates. Otherwise, you &#42;may&#42; choose to use them.*

Even the general rule above has exceptions, or can be worked around.
Some issues might be resolved through a special setup on your part. For
example, you could create your own DNF repository on a local server, and
only put in tested or trusted updates. Then use the automatic updates
from only your own repository. Such setups, while perhaps more difficult
to set up and maintain, can remove a large amount of risk otherwise
inherent in automatic updates.

## How are automatic updates done?

You can use a service to automatically download and install any new
updates (for example security updates).

The
[dnf-automatic](https://dnf5.readthedocs.io/en/latest/dnf5_plugins/automatic.8.html)
RPM package as a [DNF](dnf) component provides a service which is
started automatically.

### Install and settings of dnf-automatic

On a fresh install of Fedora with default options, the dnf-automatic RPM
is not installed. The first command below installs this RPM:

``` bash
sudo dnf install dnf-automatic
```

By default, dnf-automatic runs from the configurations in the
&#96;/etc/dnf/automatic.conf&#96; file. These configurations only
download, but do not apply any of the packages. In order to change or
add any configurations, open the &#96;.conf&#96; file as the root user
(or using &#96;sudo&#96;) from a terminal window.

``` bash
sudo nano /etc/dnf/automatic.conf
```

A modification to automatic.conf to download all updates, apply them,
and reboot could be:

    [commands]
    apply_updates=True
    reboot=when-needed

Omit reboot=when-needed to manually reboot. A full and detailed
description of dnf-automatic settings is provided on the
[dnf-automatic](https://dnf5.readthedocs.io/en/latest/dnf5_plugins/automatic.8.html)
page.

### Run dnf-automatic

Once you are finished with the configuration, execute:

``` bash
systemctl enable --now dnf-automatic.timer
```

to enable and start the &#96;systemd&#96; timer.

Check status of &#96;dnf-automatic&#96;:

``` bash
systemctl status dnf-automatic.timer
```

Note: pre-configured timers like &#96;automatic-download.timer&#96;,
&#96;automatic-install.timer&#96; and
&#96;automatic-notifyonly.timer&#96; were merged into
&#96;dnf-automatic.timer&#96; for versions above Fedora 40 with the
switch to dnf5. For the replacement commands, please see the [options
section](https://dnf5.readthedocs.io/en/latest/dnf5_plugins/automatic.8.html&#35;options)
in the upstream dnf documentation.

## Can we trust DNF updates?

Dnf in Fedora has the GPG key checking enabled by default. Assuming that
you have imported the correct GPG keys, and still have
&#96;gpgcheck=1&#96; in your &#96;/etc/dnf/dnf.conf&#96;, then we can at
least assume that any automatically installed updates were not corrupted
or modified from their original state. Using the GPG key checks, there
is no way for an attacker to generate packages that your system will
accept as valid (unless they have a copy of the &#42;private&#42; key
corresponding to one you installed) and any data corruption during
download would be caught.

However, the question would also apply to the question of update
quality. Will the installation of the package cause problems on your
system? This we can not answer. Each package goes through a QA process,
and is assumed to be problem free. But, problems happen, and QA can not
test all possible cases. It is always possible that any update may cause
problems during or after installation.

## Why use automatic updates?

The main advantage of automating the updates is that machines are likely
to get updated more quickly, more often, and more uniformly than if the
updates are done manually. We see too many compromised machines on the
internet which would have been safe if the latest updates where
installed in a timely way.

So while you should still be cautious with any automated update
solution, in particular on production systems, it is definitely worth
considering, at least in some situations.

### Reasons FOR using automatic updates

While no one can determine for you if your machine is a good candidate
for automatic updates, there are several things which tend to make a
machine a better candidate for automatic updates.

Some things which might make your machine a good candidate for automatic
updates are:

&#42; You are unlikely to apply updates manually for whatever reason(s).
&#42; The machine is not critical and occasional unplanned downtime is
acceptable. &#42; You can live without remote access to the machine
until you can get to its physical location to resolve problems. &#42;
You do not have any irreplaceable data on the machine, or have proper
backups of such data.

If all the above apply to your machine(s), then automatic updates may be
your best option to help secure your machine. If not all the above
apply, then you will need to weigh the risks and decide for yourself if
automatic updates are the best way to proceed.

### Reasons AGAINST using automatic updates

While no one can determine for you if your machine is a bad candidate
for automatic updates, there are several things which tend to make a
machine a worse candidate for automatic updates.

Some things which might make your machine be a bad candidate for
automatic updates are:

&#42; It provides a critical service that you don't want to risk having
unscheduled downtime. &#42; You installed custom software, compiled
software from source, or use third party software that has strict
package version requirements. &#42; You installed a custom kernel,
custom kernel modules, third party kernel modules, or have a third party
application that depends on kernel versions (this may not be a problem
if you exclude kernel updates, which is the default in Fedora
&#96;dnf.conf&#96; files). (See also [bug
&#35;870790](https://bugzilla.redhat.com/show_bug.cgi?id=870790) - you
may need to modify the base section to add
&#96;exclude=kernel&#42;&#96;.) &#42; Your environment requires
meticulous change-control procedures. &#42; You update from other third
party DNF repositories besides Fedora repositories which may conflict in
versioning schemes for the same packages.

There are also some other reasons why installing automatic updates
without testing may be a bad idea. A few such reasons are:

&#42; The need to back up your configuration files before an update.
Even the best package spec files can have mistakes. If you have modified
a file which is not flagged as a configuration file, then you might lose
your configuration changes. Or an update may have a different format of
configuration file, requiring a manual reconfiguration. It is often best
to back up your configuration files before doing updates on critical
packages such as mail, web, or database server packages. &#42; Unwanted
side effects. Some packages can create annoying side effects,
particularly ones which have cron jobs. Updates to base packages like
openssl, openldap, sql servers, etc. can have an effect on many other
seemingly unrelated packages. &#42; Bugs. Many packages contain buggy
software or installation scripts. The update may create problems during
or after installation. Even cosmetic bugs, like those found in previous
Mozilla updates causing the user's icons to be removed or break, can be
annoying or problematic. &#42; Automatic updates may not complete the
entire process needed to make the system secure. For example, DNF can
install a kernel update, but until the machine is rebooted (which DNF
will not do automatically) the new changes won't take effect. The same
may apply to restarting daemons. This can leave the user feeling that he
is secure when he is not.

## Best practices when using automatic updates

If you decide to use automatic updates, you should at least do a few
things to make sure you are up-to-date.

Check for package updates which have been automatically performed, and
note if they need further (manual) intervention. You can monitor what
DNF has updated via its log file (usually &#96;/var/log/dnf.log&#96;).

You can monitor updates availability automatically by email after
modifying the dnf-automatic configuration file (usually
&#96;/etc/dnf/automatic.conf&#96;).

``` bash
[emitters]
emit_via = email

[email]
\&#35; The address to send email messages from.
email_from = root@localhost.com

\&#35; List of addresses to send messages to.
email_to = root

\&#35; Name of the host to connect to to send email messages.
email_host = localhost
```

You would replace root with an actual email address to which you want
the report sent, and localhost with an actual address of a SMTP server.
This change will mean that after dnf-automatic runs, it will email you
information about available updates, a log about downloaded packages, or
installed updates according to settings in &#96;automatic.conf&#96;.

## Alternative methods

As an alternative to dnf-automatic,
[auter](https://github.com/rackerlabs/auter) can be used. This operates
in a similar way to dnf-automatic, but provides more flexibility in
scheduling, and some additional options including running custom scripts
before or after updates, and automatic reboots. This comes at the
expense of more complexity to configure.

``` bash
sudo dnf install auter
```

You should then edit the configuration. Descriptions of the options are
contained in the conf file &#96;/etc/auter/auter.conf&#96;.

Auter is not scheduled by default. Add a schedule for &#96;\--prep&#96;
(if you want to pre-download updates) and &#96;\--apply&#96; (install
updates). The installed cron job which you can see in
&#96;/etc/cron.d/auter&#96; contains lots of examples.

To make auter run immediately without waiting for the cron job to run,
for example for testing or debugging, you can simply run it from the
command line:

``` bash
auter --apply
```

If you want to disable auter from running, including from any cron job:

``` bash
auter --disable
```

## Alternatives to automatic updates

### Notifications

Instead of automatic updates, dnf-automatic can only download new
updates and can alert you via email of available updates which you could
then install manually. This can be set by editing of
&#96;/etc/dnf/automatic.conf&#96; file.

### Scheduling updates

Another common problem is having automatic updates run when it isn't
desired (holidays, weekends, vacations, etc). If there are times that no
one will be around to fix any problem arising from the updates, it may
be best to avoid doing updates on those days.

This problem can be fixed by modification of the timer of dnf-automatic
using the description on the [Understanding and administering
systemd](understanding-and-administering-systemd.xml) page.

### Other methods of protection

Yet another thing to consider if not using automatic updates is to
provide your machine with some other forms of protection to help defend
it of any attacks that might occur before updates are in place. This
might include an external firewall, a host-based firewall (like
iptables, ipchains, and/or tcp wrappers), not performing dangerous tasks
on the computer (like browsing the web, reading e-mail, etc.), and
monitoring the system for intrusions (with system log checkers, IDS
systems, authentication or login monitoring, etc).

# Adding or removing software repositories in Fedora {#_adding_or_removing_software_repositories_in_fedora}

Anthony McGlone

> This section describes how to add, enable, or disable a software
> repository with the DNF application.

## Adding repositories {#_adding_repositories}

This section describes how to add software repositories with the
&#96;dnf config-manager&#96; command.

### For Fedora 40 or earlier (DNF 4) {#_for_fedora_40_or_earlier_dnf_4}

&#42; To add a new repository, do the following as
&#96;&#42;root&#42;&#96;.

1.  Define a new repository by adding a new file with the
    &#96;.repo&#96; suffix to the
    \[filename\]&#96;/etc/yum.repos.d/&#96; directory. For details about
    various options to use in the &#96;.repo&#96; file, see the [Setting
    \[repository\]
    Options](f40@fedora:system-administrators-guide:package-management/DNF.adoc&#35;sec-Setting_repository_Options)
    section in the System Administrator's Guide

2.  Add the repository with &#96;\--add-repo&#96;, where
    &#42;\_repository\_&#42; is the file path:

        dnf config-manager --add-repo \&#96;\&#42;_repository_\&#42;\&#96;

    For example:

        dnf config-manager --add-repo /tmp/fedora_extras.repo

### For Fedora 41 or later (DNF 5) {#_for_fedora_41_or_later_dnf_5}

&#42; To add a new repository, do the following as
&#96;&#42;root&#42;&#96;.

1.  Define a new repository by adding a new file with the
    &#96;.repo&#96; suffix to the
    \[filename\]&#96;/etc/yum.repos.d/&#96; directory. For details about
    various options to use in the &#96;.repo&#96; file, see the [Setting
    \[repository\]
    Options](f41@fedora:system-administrators-guide:package-management/DNF.adoc&#35;sec-Setting_repository_Options)
    section in the System Administrator's Guide

2.  Add the repository with &#96;addrepo&#96;, where
    &#42;\_repository\_&#42; is the file path:

        dnf config-manager addrepo --from-repofile=\&#96;\&#42;_repository_\&#42;\&#96;

    For example:

        dnf config-manager addrepo --from-repofile=/tmp/fedora_extras.repo

## Enabling repositories {#_enabling_repositories}

This section shows how to enable a particular software repository by
using the &#96;dnf config-manager&#96; command.

&#42; To enable a particular repository, run the following command as
&#96;&#42;root&#42;&#96;.

\+

    dnf config-manager setopt \&#42;_repository_\&#42;.enabled=1

\+ Where &#42;\_repository\_&#42; is the unique repository ID, for
example:

\+

    dnf config-manager setopt fedora-extras.enabled=1

## Disabling repositories {#_disabling_repositories}

This section shows how to disable a particular software repository by
using the &#96;dnf config-manager&#96; command.

&#42; To disable a particular repository, run the following command as
&#96;&#42;root&#42;&#96;.

\+

    dnf config-manager setopt \&#42;_repository_\&#42;.enabled=0

\+ Where &#42;\_repository\_&#42; is the unique repository ID, for
example:

\+

    dnf config-manager setopt fedora-extras.enabled=0

## Removing repositories {#_removing_repositories}

This section shows how to remove a Yum repository (or &#96;.repo&#96;
file).

:::: note
::: title
:::

If you know the ID of a repository, but you're not sure what
&#96;.repo&#96; it belongs to, you can run the following command
\[red\]&#35;&#96;grep -E \'\^\\\[.\\\*\]\'
/etc/yum.repos.d/\\\*&#96;&#35;. This will print a list of the
repository IDs that are associated with each Yum repository.
::::

&#42; To remove a Yum repository, run the following command as
&#96;&#42;root&#42;&#96;.

\+

    rm /etc/yum.repos.d/\&#42;_file_name_\&#42;.repo

\+ Where &#42;\_file_name\_&#42; is the name of the &#96;.repo&#96;
file.

# Adding New Fonts in Fedora {#_adding_new_fonts_in_fedora}

The Fedora Docs Team; Peter Boy

Fedora pre-installs several basic fonts by default. This page explains
how to add new fonts to a Fedora installation.

## Packaged fonts {#packaged}

Did you know Fedora packages several freely-licensed fonts? There are
several supplementary fonts to preview and try out that are not
installed by default. Like all fonts on Fedora, these fonts are not
encumbered with licenses or restrictions.

An added benefit of packaged fonts is they give you control over the
font package in the future. You will receive future updates and can
easily uninstall it later if you decide it is not the font for you.

### GNOME Software

:::: note
::: title
:::

This section uses a Graphical User Interface (G.U.I.) for managing
fonts.
::::

The easiest way to preview and install new fonts is to use
\[application\]&#96;GNOME Software&#96;. Search for a specific font or
search \'fonts\' in \[application\]&#96;GNOME Software&#96; to see what
other freely-licensed fonts are available.

### DNF package manager {#dnf}

:::: note
::: title
:::

This section uses a Command Line Interface (C.L.I.) for managing fonts.
::::

If you prefer working in a C.L.I., you can also install fonts with
\[application\]&#96;dnf&#96;.

Add or enable third-party repositories with font packages

:   Many fonts are available from the RPM Fusion repository. To enable
    the repository on your system, follow [these
    instructions](rpmfusion-setup.xml).

List all available font packages from enabled repositories

:   

<!-- -->

    […]$ dnf search fonts

Install the font package you need

:   

<!-- -->

    […]$ sudo dnf install libreoffice-opensymbol-fonts

## Unpackaged fonts {#unpackaged}

In many cases, you may want to use a specific font that is not available
in Fedora or is not made available under [Free
Culture](https://freedomdefined.org/Definition) licenses.

:::: important
::: title
:::

Unpackaged fonts are not managed by a package manager. You will not
automatically receive updates or optimizations. If a font is provided by
a distribution package, you should always use a packaged version of a
font.
::::

### System fonts

System fonts are installed for all users. Anyone with an account on the
machine will be able to use these fonts.

Create a new directory in the system fonts directory (&#96;/usr/local/share/fonts/&#96;) to accommodate the new font family, and copy the downloaded fonts (e.g. robofont.ttf files)

:   

<!-- -->

    […]$ sudo mkdir -p /usr/local/share/fonts/robofont
    […]$ sudo cp ~/Downloads/robofont.ttf /usr/local/share/fonts/robofont/

Set permissions and update SELinux labels

:   

<!-- -->

    […]$ sudo chown -R root: /usr/local/share/fonts/robofont
    […]$ sudo chmod 644 /usr/local/share/fonts/robofont/\&#42;
    […]$ sudo restorecon -vFr /usr/local/share/fonts/robofont

Update the font cache

:   

<!-- -->

    […]$ sudo fc-cache -v

### User fonts

User fonts are installed for an individual user. Only the user who
installs the fonts on the machine will be able to use these fonts. This
is also convenient if you do not have superuser (i.e. &#96;root&#96;)
access on the machine.

There are three ways to install user fonts.

#### GNOME Font Viewer {#user-fonts--gnome-font-viewer}

:::: note
::: title
:::

This section uses a Graphical User Interface (G.U.I.) for managing
fonts.
::::

The \[application\]&#96;GNOME Font Viewer&#96; is an application to
display the fonts installed on the system. It also allows you to locally
install fonts. Follow these steps to add new user fonts with
\[application\]&#96;GNOME Font Viewer&#96;:

1.  Install \[application\]&#96;GNOME Font Viewer&#96;. &#42;&#42; Use
    GNOME Software or use the command line (&#96;sudo dnf install
    gnome-font-viewer&#96;)

2.  Open a file browser.

3.  Double-click on a font file to open it in \[application\]&#96;GNOME
    Font Viewer&#96;.

4.  Click on the blue btn:\[Install\] button on the top bar.

:::: note
::: title
:::

Currently, there is a bug in the application. When you click on the
btn:\[Install\] button, it does not inform whether the installation
succeeded.
::::

\[application\]&#96;GNOME Font Viewer&#96; does two things to install
fonts:

1.  Copy font files to a font directory in the user's home directory
    &#96;.local/share/fonts&#96;.

2.  Update the font cache.

#### KDE Font Management {#user-fonts--KDE}

1.  Go to Settings and enter font in Quick Settings.

2.  On Font Management window, press the Install from&#8230;button, and
    select the downloaded fonts from within the dialog.

3.  On pop-up window (see UI text below), select a font group that will
    control where the fonts will be installed.

<!-- -->

    Do you wish to install the font(s) for personal use (only available to you), or system-wide (available to all users)?

#### Command line {#user-fonts--command-line}

:::: note
::: title
:::

This section uses a Command Line Interface (C.L.I.) for managing fonts.
::::

If you prefer a command line interface, you can install user fonts
manually. Follow these steps in a terminal window to install a font
locally:

Create a new directory &#96;\~/.local/share/fonts/&lt;font-family-name&gt;/&#96; for the new font family

:   

<!-- -->

    […]$ mkdir -p ~/.local/share/fonts/robofont

Copy font files (e.g. &#96;.ttf&#96; files) to the new directory

:   

<!-- -->

    […]$ cp ~/Downloads/robofont.ttf ~/.local/share/fonts/robofont

Update the font cache

:   

<!-- -->

    […]$ fc-cache -v

# DNF and its APT command equivalents on Fedora {#_dnf_and_its_apt_command_equivalents_on_fedora}

Michal Ambroz; Christopher Engelhard ; The Fedora Docs team

APT is the package manager/dependency solver for the Debian ecosystem,
i.e. it manages &#96;.deb&#96; packages installed by the DPKG program.
Fedora software is based on &#96;.rpm&#96; packages, and thus uses DNF,
the package manager/dependency solver for the RPM program, instead. This
document gives a brief overview of the most common APT commands one
might find in tutorials and their DNF equivalents.

## APT vs. DNF commands {#_apt_vs_dnf_commands}

+----------------------+----------------------+-----------------------+
| APT command          | DNF command          | notes                 |
+======================+======================+=======================+
| &#96;apt             | &#96;dnf             | Of course, actual     |
| install&#96;         | install&#96;         | package names may     |
|                      |                      | vary. For example,    |
| &#96;apt-get         |                      | &#96;libc6-dev&#96;   |
| install&#96;         |                      | on Debian maps to     |
|                      |                      | &#96;glibc-devel&#96; |
|                      |                      | in the Fedora         |
|                      |                      | universe.             |
+----------------------+----------------------+-----------------------+
| &#96;apt install     | &#96;dnf update      | Updates only already  |
| \--only-upgrade      | package&#96;         | installed package and |
| package&#96;         |                      | its dependencies. The |
|                      |                      | &#96;apt install&#96; |
|                      |                      | works for both        |
|                      |                      | install and upgrade   |
|                      |                      | single package if     |
|                      |                      | already installed.    |
+----------------------+----------------------+-----------------------+
| &#96;apt update&#96; | &#96;dnf             | This command is       |
|                      | check-update&#96;    | rarely needed, as dnf |
| &#96;apt-get         |                      | updates its package   |
| update&#96;          |                      | cache automatically   |
|                      |                      | when it is stale. A   |
|                      |                      | cache update can be   |
|                      |                      | forced by appending   |
|                      |                      | &#96;\--refresh&#96;  |
|                      |                      | to other commands,    |
|                      |                      | e.g. &#96;dnf upgrade |
|                      |                      | \--refresh&#96;.      |
+----------------------+----------------------+-----------------------+
| &#96;apt             | &#96;dnf             | Note that while       |
| upgrade&#96;         | upgrade&#96;         | &#96;apt update&#96;  |
|                      |                      | does something        |
| &#96;apt-get         |                      | different, &#96;dnf   |
| upgrade&#96;         |                      | update&#96; and       |
|                      |                      | &#96;dnf upgrade&#96; |
|                      |                      | are synonyms. You can |
|                      |                      | also use the shorter  |
|                      |                      | &#96;dnf up&#96;.     |
+----------------------+----------------------+-----------------------+
| &#96;apt             | &#96;dnf             | While                 |
| full-upgrade&#96;    | distro-sync&#96; or  | &#96;distro-sync&#96; |
|                      |                      | is the most direct    |
| &#96;apt-get         | &#96;dnf             | functional            |
| dist-upgrade&#96;    | system-upgrade&#96;  | equivalent, &#96;dnf  |
|                      | (see note)           | system-upgrade&#96;   |
|                      |                      | should be used to     |
|                      |                      | upgrade from one      |
|                      |                      | release to another,   |
|                      |                      | e.g. from Fedora      |
|                      |                      | Linux 34 to 35. This  |
|                      |                      | is a multi-step       |
|                      |                      | process as described  |
|                      |                      | [here](dnf            |
|                      |                      | -system-upgrade.xml). |
+----------------------+----------------------+-----------------------+
| &#96;apt remove&#96; | &#96;dnf remove&#96; |                       |
|                      |                      |                       |
| &#96;apt-get         |                      |                       |
| remove&#96;          |                      |                       |
+----------------------+----------------------+-----------------------+
| &#96;apt purge&#96;  | \-\--                | Fedora packages don't |
|                      |                      | treat configuration   |
| &#96;apt-get         |                      | files in the same way |
| purge&#96;           |                      | as Debian packages,   |
|                      |                      | so there is no direct |
|                      |                      | equivalent.           |
+----------------------+----------------------+-----------------------+
| &#96;apt             | &#96;dnf             | Note that this can    |
| autoremove&#96;      | autoremove&#96;      | occasionally remove   |
|                      |                      | packages that you     |
| &#96;apt-get         |                      | might actually want.  |
| autoremove&#96;      |                      | Use &#96;dnf          |
|                      |                      | mark&#96; to flag     |
|                      |                      | packages to keep.     |
+----------------------+----------------------+-----------------------+
| &#96;apt search&#96; | &#96;dnf search&#96; | &#96;dnf              |
|                      |                      | repoquery&#96; is     |
| &#96;apt-cache       |                      | useful for advanced   |
| search&#96;          |                      | searches.             |
+----------------------+----------------------+-----------------------+

: Apt vs DNF commands

With the exceptions of the distribution upgrade working differently, and
DNF updating the cache automatically, the commands are very similar.
More info on DNF can be found [here](dnf.xml).

## Why is APT in the Fedora repositories? {#_why_is_apt_in_the_fedora_repositories}

:::: warning
::: title
:::

APT &#42;can not&#42; be used to install packages on Fedora, you
&#42;have to use DNF&#42; instead.
::::

The &#96;apt&#96; command on Fedora used to --- until [Fedora
32](https://fedoraproject.org/wiki/Changes/Move_apt_package_from_RPM_to_DPKG_backend) --- actually
be APT-RPM, which basically mapped normal apt commands so that they
worked with Fedora's RPM package management system.

However, APT-RPM is unmaintained, broken, and insecure, and so was
dropped in favour of shipping the actual Debian APT software. Since APT
exclusively deals with &#96;.deb&#96; packages, the &#96;apt&#96;
command can no longer be used to manage Fedora packages. Its purpose is
now purely as a tool for people building packages for Debian-based
distributions on a Fedora system.

# Enabling the RPM Fusion repositories {#_enabling_the_rpm_fusion_repositories}

Micah Abbott :page-aliases: setup-rpmfusion.adoc

## Third party repositories {#_third_party_repositories}

There are a number of third-party software repositories for Fedora. They
have more liberal licensing policies and provide software packages that
Fedora excludes for various reasons. These software repositories are not
officially affiliated or endorsed by the Fedora Project. Use them at
your own discretion. For complete list, see
[FedoraThirdPartyRepos](https://rpmfusion.org/FedoraThirdPartyRepos) The
following repositories are commonly used by end users and do not
conflict with each other:

&#42; <https://rpmfusion.org>

&#42; rpm.livna.org (Obsoleted! Replaced by RPM Fusion free tainted)

### Mixing third party software repositories {#_mixing_third_party_software_repositories}

Mixing a lot of third party repositories is not recommended since they
might conflict with each other causing instability and hard to debug
issues. If you are not a technical user, one way is to not enable the
third-party repo by default and instead use the &#42;\--enablerepo&#42;
switch for dnf, or a similar method configurable in the graphical
package manager.

## The purpose of RPM Fusion {#_the_purpose_of_rpm_fusion}

The RPM Fusion project is a community-maintained software repository
providing additional packages that are not distributed by Fedora.

**Additional resources**

&#42; RPM Fusion home page: <https://rpmfusion.org/> &#42; For more
information on what packages are allowed to be distributed with Fedora,
see the following wiki page:
<https://fedoraproject.org/wiki/Forbidden_items> &#42; You can buy
multimedia codecs from Fluendo. This is a legal solution for users from
countries where software patents apply. For more information, see:
<https://fluendo.com/en/products/enterprise/fluendo-codec-pack/>.

## Enabling the RPM Fusion repositories using command-line utilities {#_enabling_the_rpm_fusion_repositories_using_command_line_utilities}

This procedure describes how to enable the RPM Fusion software
repositories without using any graphical applications.

**Prerequisites**

&#42; You have internet access.

**Procedure**

1.  To enable the *Free* repository, use:

        $ sudo dnf install \
        https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm

2.  Optionally, enable the *Nonfree* repository:

        $ sudo dnf install \
        https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm

3.  The first time you attempt to install packages from these
    repositories, the &#96;dnf&#96; utility prompts you to confirm the
    signature of the repositories. Confirm it.

## Enabling the RPM Fusion repositories using graphical applications {#_enabling_the_rpm_fusion_repositories_using_graphical_applications}

This procedure describes how to enable the RPM Fusion software
repositories without using any command-line utilities.

**Prerequisites**

&#42; You have internet access. &#42; You are using the Gnome desktop
environment.

**Procedure**

1.  In your web browser, open the following page:
    <https://rpmfusion.org/Configuration>.

2.  To enable the *Free* repository, click the &#42;RPM Fusion free for
    Fedora *version*&#42; link on the page, where *version* is the
    Fedora release you are using. This prompts you to save or open the
    repo file.

3.  Open the file using the &#42;Software Install&#42; application.

4.  The &#42;Software&#42; application opens. Click the blue
    &#42;Install&#42; button.

5.  Optionally, enable the *Nonfree* repository: click the &#42;RPM
    Fusion nonfree for Fedora *version*&#42; link on the page, where
    *version* is the Fedora release you are using.

6.  Save and install the file with the &#42;Software&#42; application
    again.

## Enabling Appstream data from the RPM Fusion repositories {#_enabling_appstream_data_from_the_rpm_fusion_repositories}

This procedure describes how to install the Appstream data provided by
the RPM Fusion software repositories.

**Prerequisites**

&#42; You have internet access. &#42; You are using the Gnome desktop
environment. &#42; You have the RPMFusion repositories installed

**Procedure**

    $ sudo dnf group upgrade core

## Enabling the RPM Fusion repositories for ostree-based systems {#_enabling_the_rpm_fusion_repositories_for_ostree_based_systems}

This procedure describes how to enable the RPM Fusion software
repositories for systems based on ostree (i.e. Silverblue, Kinoite,
Fedora IoT).

This is a two-stage process where you have to install versioned RPM
Fusion repos and then you are able to replace them with unversioned RPM
Fusion repos.

:::: note
::: title
:::

For more information about this process and the problem it solves,
please refer to the relevant [thread on the Fedora Discourse
site](https://discussion.fedoraproject.org/t/simplifying-updates-for-rpm-fusion-packages-and-other-packages-shipping-their-own-rpm-repos/30364).
::::

**Prerequisites**

&#42; You are using an ostree-based system such as Silverblue, Kinoite,
or Fedora IoT. &#42; You have internet access.

**Procedure**

1.  To install the versioned *Free* and *Nonfree* RPM Fusion repos:

        $ rpm-ostree install \
        https://mirrors.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm \
        https://mirrors.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
        $ systemctl reboot

2.  To replace the versioned RPM Fusion repos that were previously
    installed with the unversioned repos:

        $ rpm-ostree update \
        --uninstall rpmfusion-free-release \
        --uninstall rpmfusion-nonfree-release \
        --install rpmfusion-free-release \
        --install rpmfusion-nonfree-release
        $ systemctl reboot

## References {#_references_2}

&#42; <https://rpmfusion.org/Configuration> &#42;
<https://rpmfusion.org/Howto/OSTree>

# Fedora Repositories {#_fedora_repositories}

yohaan vakil; Otto Urpelainen; Chetan Giradkar; Adam Williamson
:page-aliases: repositories.adoc

> This page explains the various Fedora repositories that exist for
> different Fedora Releases, the relationship between them, and what
> packages they contain.

## The fedora repository {#_the_fedora_repository}

The *fedora* repository exists for all Fedora releases after they have
[Branched](https://fedoraproject.org/wiki/Releases/Branched) from
[Rawhide](https://fedoraproject.org/wiki/Releases/Rawhide). It is
represented for [DNF](dnf.xml) in the &#96;fedora.repo&#96; file in the
repository path. For any Fedora installation, this repository will be
enabled by default, and should usually remain so.

### The *fedora* repository in stable releases

For stable releases, *fedora* represents the frozen release state. It is
a part of the frozen tree that is created by [Release
Engineering](https://fedoraproject.org/wiki/ReleaseEngineering) when a
release is approved at a [Go/No-Go
Meeting](https://fedoraproject.org/wiki/Go_No_Go_Meeting). The package
set it contains never changes after that time. It represents the
*stable* state of a stable release in conjunction with *updates*
repository.

The stable release *fedora* repositories for the various primary
architectures can be found in the
&#96;/fedora/linux/releases/XX/Everything&#96; directory on the mirrors
(where XX is the release), and can also be queried from MirrorManager.
For instance,
<https://mirrors.fedoraproject.org/mirrorlist?repo=fedora-43&amp;arch=x86_64>
will return mirrors for the x86_64 *fedora* repository for release 43.

### The *fedora* repository in Branched releases

In Branched releases - the state a release is in between branching from
Rawhide and stable release, see
[Branched](https://fedoraproject.org/wiki/Releases/Branched) for more
details - the fedora repository alone represents the release's stable
state. The *updates* repository for Branched releases is not used until
they become stable. Before the [updates-testing
activation](https://docs.fedoraproject.org/en-US/fesco/Updates_Policy/&#35;updates-testing-activation),
package builds for the Branched release are sent directly to this
repository. After the *Bodhi enabling point*, package builds that pass
the [Updates Policy](https://fedoraproject.org/wiki/Updates_Policy) move
from *updates-testing* repository to this repository.

The Branched *fedora* repositories for the various primary
[architectures](https://fedoraproject.org/wiki/Architectures) can be
found in the &#96;/fedora/linux/development/XX&#96; directory on the
mirrors (where XX is the release), and can also be queried from
MirrorManager. For instance,
<https://mirrors.fedoraproject.org/mirrorlist?repo=fedora-44&amp;arch=x86_64>
will return mirrors for the x86_64 *fedora* repository for release 44.

## The *updates* repository

The *updates* repository exists for Branched and stable releases, but is
only populated and used for stable releases. It is represented for
[DNF](dnf.xml) in the &#96;fedora-updates.repo&#96; file in the
repository path. It exists in Branched releases solely to prevent
various tools that expect its existence from breaking. For any Fedora
installation, this repository will be enabled by default, and should
usually remain so.

For stable releases, *updates* together with *fedora* represents the
current *stable* state of the release. Package builds that pass the
[Updates Policy](https://fedoraproject.org/wiki/Updates_Policy) move
from the *updates-testing* repository to this repository. This
difference from Branched is a result of the need to maintain a precise
representation of the initial, \'frozen\' state of a stable release.

The stable release *updates* repositories for the various primary
architectures can be found in the &#96;/fedora/linux/updates/XX&#96;
directory on the mirrors (where XX is the release), and can also be
queried from
[MirrorManager](https://fedoraproject.org/wiki/MirrorManager). For
instance,
<https://mirrors.fedoraproject.org/mirrorlist?repo=updates-released-f43&amp;arch=x86_64>
will return mirrors for the x86_64 *updates* repository for release 43.

### The *updates-testing* repository

The *updates-testing* repository exists for Branched releases after the
[Bodhi enabling
point](https://fedoraproject.org/wiki/Updates_Policy&#35;Bodhi_enabling),
and for stable releases. It is represented for [DNF](dnf.xml) in the
&#96;fedora-updates-testing.repo&#96; file in the repository path. For
both, it is a \'staging\' location where new package builds are tested
before being marked as \'stable\' (and hence moving to the *fedora*
repository or the *updates* repository, respectively).

These builds are sometimes referred to as *update candidates*, and are
reviewed with the [Bodhi](https://fedoraproject.org/wiki/Bodhi) update
feedback tool, according to the [update feedback
guidelines](https://fedoraproject.org/wiki/QA:Update_feedback_guidelines).

The [Updates Policy](https://fedoraproject.org/wiki/Updates_Policy)
defines the rules for marking update candidates as *stable*. The [QA
updates-testing page](https://fedoraproject.org/wiki/QA:Updates_Testing)
provides some information for testers on using this repository. The
[Package Update
Guide](https://docs.fedoraproject.org/en-US/package-maintainers/Package_Update_Guide/)
provides information for packagers on submitting builds to
*updates-testing* and to *stable*.

The *updates-testing* repository is enabled by default for Branched
releases, but disabled by default for stable releases. The switchover is
made around the time of the [Final
Freeze](https://fedoraproject.org/wiki/Milestone_freezes) for each
release. Testers moving from Branched to stable may encounter errors
running updates around this time, caused by dependency mismatches
between packages already installed from the now-disabled
*updates-testing* repository. Running &#96;dnf distro-sync&#96; or
re-enabling the *updates-testing* repository will both usually alleviate
the issue; it is up to the individual user whether they wish to continue
using the *updates-testing* repository after the stable release or not.

The *updates-testing* repositories for both Branched and stable releases
can be found in the &#96;/fedora/linux/updates/testing/XX&#96; directory
on the mirrors (where XX is the release), and can also be queried from
[MirrorManager](https://fedoraproject.org/wiki/MirrorManager). For
instance,
<https://mirrors.fedoraproject.org/mirrorlist?repo=updates-testing-f43&amp;arch=x86_64>
will return mirrors for the x86_64 *updates-testing* repository for
release 43.

### The *rawhide* repository

In Rawhide - Fedora's rolling release repository, from which release are
Branched before finally going stable - *rawhide* is the only repository.
All package builds are sent there. It is represented for [DNF](dnf.xml)
in the &#96;fedora-rawhide.repo&#96; file in the repository path. For
any system running Rawhide, it should be enabled. For any other system,
it should not.

The *rawhide* repositories for the various primary
[architectures](https://fedoraproject.org/wiki/Architectures) can be
found in the directory on the mirrors, and can also be queried from
[MirrorManager](https://fedoraproject.org/wiki/MirrorManager). For
instance,
<https://mirrors.fedoraproject.org/mirrorlist?repo=fedora-rawhide&amp;arch=x86_64>
will return mirrors for the x86_64 *fedora* repository for Rawhide.

### *stable* is not a repository

It is not unusual to see references to the \'stable repository\', but
this is something of a misnomer. *stable* is more of a state that can be
considered to exist for both Branched releases post [Bodhi
enabling](https://fedoraproject.org/wiki/Updates_Policy&#35;Bodhi_enabling)
and for stable releases. It consists of package builds that were part of
Rawhide at the time they Branched, package builds sent directly to the
Branched *fedora* repository between the branch point and the *Bodhi
enabling point*, and package builds that passed the [Updates
Policy](https://fedoraproject.org/wiki/Updates_Policy) and moved from
*updates-testing* after the *Bodhi enabling point*.

For Branched releases, the *stable* state is represented solely by the
current contents of the *fedora* repository (and, arguably, the *bleed*
repository, but that is a small case).

For stable releases, the *stable* state is represented by the contents
of the *fedora* repository combined with the contents of the *updates*
repository.

*stable* is also a state a package can be considered to be in (or an
attribute it can be considered to have) when it has been *pushed stable*
or *tagged stable* and exists in, or will soon exist in, a *stable*
repository for a release - whichever literal repository that is (see
above).

## Installation and Product repositories / trees

The repositories referred to above are neither associated with a
specific [Fedora.next](https://fedoraproject.org/wiki/Fedora.next)
*Product*, nor part of an installable tree (a tree containing the
necessary files to be used as a base repository by
[Anaconda](https://fedoraproject.org/wiki/Anaconda), the Fedora
installer). Specialized repositories exist for these purposes.

For Fedora.next releases - and later - there is (as of September 2014)
no installable tree not associated with a specific Product. The
installable trees for various Products can be found under
&#96;/fedora/linux/releases/XX/&#96; on the mirrors for stable releases,
and under &#96;/fedora/linux/releases/test/&#96; for Branched
pre-release milestones. They can also be queried from MirrorManager. For
instance,
<https://mirrors.fedoraproject.org/mirrorlist?repo=fedora-server-44&amp;arch=x86_64>
will return mirrors for the x86_64 current installation repository for
Server.

These repositories are frozen (new packages are not pushed to them) and
are created at various points in the [Fedora Release Life
Cycle](https://fedoraproject.org/wiki/Fedora_Release_Life_Cycle). A new
installation tree (containing a repository) is built for several
Products for [each test compose or release candidate
build](https://fedoraproject.org/wiki/QA:SOP_compose_request), and the
trees for the Alpha and Beta releases are made available on the mirrors
in the directory (see above). They contain a subset of the full package
set that is considered to define each Product.

The Product trees for the GA (Final) release are made available in the
&#96;/releases&#96; tree on the mirrors.

At any given point in the release cycle, the MirrorManager request for a
Product repository may redirect to a test compose / release candidate
tree, a pre-release milestone tree, or the Final release tree.

These repositories are usually not used or enabled by default on
installed systems, as for that purpose they are redundant with one of
the three primary repositories described above. However, one could use a
Product repository in place of the *fedora* repository to keep a system
limited to the Product package set. They are represented for
[DNF](dnf.xml) in the &#96;fedora-(product).repo&#96; file in the
repository path, which may well not be installed on many systems.

## Other repositories

There are other repositories that fulfil various niche purposes, which
are documented here for the sake of providing a comprehensive reference.
They should not usually be significant to the vast majority of Fedora
users. None of these repositories is represented in a packaged
repository file, enabled by default, or should usually be used in a
Fedora installation.

### The *bleed* repository

The *bleed* repository exists for a single purpose: during [Milestone
freezes](https://fedoraproject.org/wiki/Milestone_freezes), it contains
packages that have been granted \'freeze exceptions\' via the [Blocker
Bug Process](https://fedoraproject.org/wiki/QA:SOP_blocker_bug_process)
or [Freeze Exception bug
process](https://fedoraproject.org/wiki/QA:SOP_freeze_exception_bug_process),
and which are desired to be included in the next test compose or release
candidate build, but have not yet reached *stable* state and hence been
moved to the *fedora* repository. In other words, it contains packages
explicitly required in TC/RC [compose
requests](https://fedoraproject.org/wiki/QA:SOP_compose_request).

The *bleed* repository can be found
[here](http://kojipkgs.fedoraproject.org/mash/bleed/), but again, is not
usually of interest to the vast majority of Fedora users. The packages
it contains are always also available from the build system, Koji, and
usually from the *updates-testing* repository.

### The *latest* repositories

The *latest* [repositories](http://kojipkgs.fedoraproject.org/repos/)
contain packages for various build \'tags\' as they arrive in the Koji
build system. They are not
[mashed](https://git.fedorahosted.org/cgit/mash/), a process which
principally handles multilib, and using them can cause various problems,
in addition to overloading Fedora's development servers. It is almost
always a better idea to cherry-pick new builds from
[Koji](https://fedoraproject.org/wiki/Koji) or
[Bodhi](https://fedoraproject.org/wiki/Bodhi) via their web interfaces
or command line tools.

## Repositories FAQ

### Why is *updates* only used after the stable release?

As described above, updates for both Branched pre-releases and final,
*stable* releases go through the *updates-testing* process before being
moved to a *stable* repository. Before the final release, they are
placed in the *fedora* repository. After release, they are placed in
*updates*.

The reason for the difference is that we want to have a record of the
exact \'state\' of a given Fedora stable release. That is, at the time a
Fedora release is declared to be done at a [Go/No-Go
Meeting](https://fedoraproject.org/wiki/Go_No_Go_Meeting), we consider
the state of the release at that time to be the canonical definition of
that release, and we wish to preserve a record of that state. For a
stable release, the tree containing the *fedora* repository &#42;is&#42;
that record, and the *fedora* repository it contains is the canonical
record of the precise *frozen* package set that formed the main part of
that stable release.

Since we wish to maintain this *frozen* state for the *fedora*
repository, we cannot place updates directly into it. The necessity for
the *updates* repository therefore becomes obvious - we need a place to
put updates to stable releases that is outside the *frozen* state of the
release.

Before a stable release occurs, this mechanism is not necessary. Before
the release is declared to be done, there is no *frozen* state of the
release: effectively, the whole Branched development process is *working
towards* what will become the *frozen* state of the release, so of
course package builds for the Branched release land directly in the
*fedora* repository.

### Why is *updates-testing* enabled by default in pre-releases?

While Branched development releases and stable releases both use an
*updates-testing* repository together with the Bodhi update feedback
system to stage packages before they reach the release's *stable* state,
it is enabled by default in Branched, but not in stable releases.

The reason is that the purpose of the *updates-testing* system is
somewhat different in each case. For stable releases, the system's goal
is to prevent broken updates reaching the general Fedora user
population. In most cases, Fedora systems are expected to have the
*updates-testing* repository disabled. Some QA testers then enable the
repository on testing systems to try out the updates and provide
feedback. The testers perform the job of making sure the updates are OK
before they reach the general user population.

When it comes to a Branched pre-release, the expectation is that anyone
who installs it wants to help test it: we effectively consider anyone
running a Branched release to be a tester. The function of
*updates-testing* is different in this case. There is not a \'general
user population\' of Branched users who run with *updates-testing*
disabled, and are protected from problematic updates by the group of
update testers. Instead, *updates-testing* in Branched serves other
important functions.

The main purpose is to insulate *image builds* from potentially
problematic changes. Branched images - nightly images, and the Alpha,
Beta and GA (Final) *milestone* builds and their [test compose and
release candidate
builds](https://fedoraproject.org/wiki/Go_No_Go_Meeting) - are built
from the *stable* packages, that is, only those in the *fedora*
repository, not those in *updates-testing*. In this sense,
*updates-testing* protects not a set of users, but a set of *builds*,
from potentially destabilizing changes. Especially when we are building
an Alpha, Beta or GA release, we need to be able to reduce the amount of
change in the package set between composes in order to produce an image
of high quality. The *updates-testing* mechanism allows for that: during
[Milestone freezes](https://fedoraproject.org/wiki/Milestone_freezes),
new builds can be sent to *updates-testing*, but cannot move from there
to *stable* (*fedora*) without special circumstances. In this way, we
can work on release images while not preventing packagers from sending
out builds.

For this and other less important functions, we need as much feedback as
possible, so it makes sense to have all pre-release testers have
*updates-testing* enabled by default, and encourage them to provide
feedback through Bodhi.

See a typo, something missing or out of date, or anything else which can
be improved? Edit this document at
<https://pagure.io/fedora-docs/quick-docs>.

# Finding and installing Linux applications {#_finding_and_installing_linux_applications}

Hanku Lee, Peter Boy; Fedora Documentation Team

> If you are looking for software to run on Fedora Linux, you will
> discover Fedora-packaged software, EPEL (Extra Packages for Enterprise
> Linux) and Flatpak apps. Here is an overview of software repositories
> and installation.

## Sources of software packages {#_sources_of_software_packages}

### Fedora Repository {#_fedora_repository}

The Fedora repository is available for all Fedora releases and backed by
the following characteristics.

- Free and Open Source software packaged in Fedora Linux meets license
  approval criteria. (Link to:
  <https://docs.fedoraproject.org/en-US/legal/license-approval/>)

- Fedora Quality Assurance continually improves the quality of Fedora
  releases and updates. (Link to:
  <https://docs.fedoraproject.org/en-US/qa-docs/>)

### What comes with default? {#_what_comes_with_default}

- Fedora-packaged software: registry.fedoraproject.org

- Updates repo

### Optional repos {#_optional_repos}

- Fedora Flatpaks

- EPEL

- Test repo

- Flathub

## Installation Procedures {#_installation_procedures}

The Fedora Linux ships with a graphical software manager to browse,
test, install apps and update the installation. This article caters for
users who prefer the use of graphical interface to command line
interface. The process diverges depending on desktop environment.

### GNOME {#_gnome_2}

In GNOME desktop environment, GNOME Software helps you explore, install
and update applications and system extensions.

#### How to use Software {#_how_to_use_software}

To launch Software, press the Super key (next to left Alt key), type
software, and press Enter key.

Step through the numbered list and the number annotated on the image of
GNOME Software.

#### 1. Explore applications by categories {#_1_explore_applications_by_categories}

All the featured apps will be shown on banner in the middle.

![GNOME Software](finding-installing-linux-apps/gnome1-featured.png)

Browse apps as categorized below and click a category that is of your
interest.

- Use case: Create, Work, Play, Socialize, Learn, Develop

- Editor's choice

#### 2. Search applications by name {#_2_search_applications_by_name}

If you know the name of apps to install, click the magnifying glass on
the top left corner and type in the name of apps and press Enter key.
GNOME Software will suggest a set of applications that match your
search.

#### 3. Check the software metadata {#_3_check_the_software_metadata}

Once you click an app icon, Software presents screenshot of apps and
overview.

Scroll down to examine version history, reviews and license details.

![App overview](finding-installing-linux-apps/GNOME_SW3_metadata.png)

If an app has optional add-ons to install together with the app, they
will be displayed as &#42;Add-ons&#42; before the software metadata
section.

#### 4. Installation {#_4_installation}

If you have checked the software metadata, scroll up to find and click
the blue &#42;Install&#42; button on top right corner of software you
selected.

Source (repository) is labelled as Fedora Linux (RPM) or Fedora Flatpak
under the blue \'Install\' or \'Open\' button.

![App Installation](finding-installing-linux-apps/GNOME_SW2_Install.png)

#### 5. Updates {#_5_updates}

To check system and app updates, go to updates tab and load updates. If
there are updates available, the blue download button will appear.

Click download and wait for the blue Restart &amp; Update button. System
updates require restart.

If you prefer automatic notification when there are updates available,
enable automatic Updates in the hamburger menu on the top right corner.

#### 6. Manage repositories {#_6_manage_repositories}

To enable or disable repositories, go to the hamburger menu on the top
right corner and select Software Repositories. From there, you can
toggle Fedora Flatpaks to explore more apps.

![Optional Repos](finding-installing-linux-apps/GNOME_SW6_repo.png)

### KDE {#_kde}

In KDE Plasma desktop, Discover helps you explore, install and update
applications and system extensions.

#### How to use Discover {#_how_to_use_discover}

Before launching Discover, Kickoff Application Launcher (Kickoff in
short) assists you to use the integrated search function.

Step through the numbered list and the number annotated on the image of
KDE Plasma desktop and Discover.

#### 1. Explore applications with Kickoff {#_1_explore_applications_with_kickoff}

To launch Kickoff, in the default configuration, press the Super key
(next to left Alt key). Hover your mouse over installed apps as
categorized on the left pane. All the available apps will be shown on
the right pane.

<figure>
<img src="finding-installing-linux-apps/KDE1_KickoffCategory.png"
alt="KDE Plasma Kickoff" />
<figcaption>Kickoff application launcher</figcaption>
</figure>

If you look for an application that has not been installed yet, Kickoff
will suggest a set of applications that match your search.

Get &lt;application name&gt;. Click the app to navigate to Discover,
enabling you to installation.

![Get application with
Kickoff](finding-installing-linux-apps/KDE1_KickoffGetApp.png)

#### 2. Explore applications by categories {#_2_explore_applications_by_categories}

To launch Discover directly, press the Super key (next to left Alt key),
type discover, and press Enter key.

Hover your mouse over available apps as categorized on the left pane.
Click a category that is of your interest. All the featured apps will be
shown on the right pane.

![Application by
categories](finding-installing-linux-apps/KDE2_Discover_category.png)

#### 3. Search applications by name {#_3_search_applications_by_name}

If you know the name of apps to install, type in the name of apps in the
search window on the top left corner and press Enter key. Discover will
suggest a set of applications that match your search.

#### 4. Check the software metadata {#_4_check_the_software_metadata}

Once you click an app icon, Discover presents screenshot of apps and
overview, software metadata such as software version, reviews and
license details.

![Check
metadata](finding-installing-linux-apps/KDE2_Discover_metadata.png)

#### 5. Installation {#_5_installation}

If you have checked the software metadata, click the &#42;Install&#42;
button on top right corner of software you selected.

#### 6. Updates {#_6_updates}

Update notification will appear on status bar when updates become
available. Click the notification to open Discover. Press "Update All"
button on the top right corner. System updates require restart.

![Application updates](finding-installing-linux-apps/KDE6_Updates.png)

#### 7. Manage repositories {#_7_manage_repositories}

To enable repositories, go to Settings in Discover. In case Flathub is
required to explore more apps, click the Add Flathub button.

## More information {#_more_information}

For latest improvements on functionality and look of graphical software
manager, please check the upstream documentation on the link below.

GNOME Software: <https://wiki.gnome.org/Apps/Software>

KDE Discover: <https://userbase.kde.org/Discover>

To explore and install command-line apps, refer to the DNF Command
Reference: <https://dnf.readthedocs.io/en/latest/command_ref.html>

To explore and install language libraries, packages, and development
toolchain, refer to the Fedora Developer Portal:
<https://developer.fedoraproject.org/tech.html>

# Installing Java {#_installing_java}

Héctor Louzao; Ankur Sinha ; alciregi; Nico Shetty; chris-r

Java is a popular programming language that allows you run programs on
many platforms, including Fedora. If you want to create Java programs,
you need to install a JDK (Java Development Kit). If you want to run a
Java program, you can do that on a JVM (Java Virtual Machine), which is
provided with the JRE (Java Runtime Environment). If in doubt, install
the JDK because this is sometimes required even if the intention is not
to write Java programs.

Many flavors of Java exist and also many versions of each flavor. If you
want to just run a specific application, check the documentation of that
software to see what versions of Java are supported or have been tested.
Most Java applications run on one of the following:

&#42; OpenJDK --- an open-source implementation of the Java Platform,
Standard Edition. This version is preferred, and included in Fedora.
&#42; Oracle Java SE --- The former Oracle SE is no longer distributed
by Fedora.

You can find the following Versions:

&#42; The Long Term Support &#96;LTS&#96; Versions, currently 21, 25

&#42; Latest, currently 24

## Installing OpenJDK {#_installing_openjdk}

To install OpenJDK from the Fedora repository:

&#42; Run the following command to list available versions:

    dnf search openjdk

&#42; Copy the version of OpenJDK you want to install.

:::: note
::: title
:::

Various flavors of OpenJDK are available. For information about these
options, search the [OpenJDK web site](https://openjdk.java.net/).
::::

&#42; Run the following command to install OpenJDK:

    sudo dnf install \&lt;openjdk-package-name\&gt;

Examples:

    sudo dnf install java-21-openjdk.x86_64

    sudo dnf install java-25-openjdk.x86_64

    sudo dnf install java-latest-openjdk.x86_64

### Installing OpenJDK for development {#_installing_openjdk_for_development}

In order to install the Java Development Kit, runtime environment and
associated development tools.

    sudo dnf install \&lt;openjdk-package-name\&gt;-devel

Examples:

    sudo dnf install java-21-openjdk-devel.x86_64

    sudo dnf install java-25-openjdk-devel.x86_64

    sudo dnf install java-latest-openjdk-devel.x86_64

## Installing an older Java version {#_installing_an_older_java_version}

To install an older version of Java:

&#42; Install the Adoptium Temurin Java Repository:

    sudo dnf install adoptium-temurin-java-repository

Then, enable the third party repos:

    sudo fedora-third-party enable

&#42; Run the following command to list available versions:

    dnf search temurin

&#42; Copy the version of Temurin you want to install.

&#42; Run the following command to install Temurin JDK:

    sudo dnf install \&lt;temurin-package-name\&gt;

Examples:

    sudo dnf install temurin-8-jdk.x86_64

    sudo dnf install temurin-17-jdk.x86_64

## Installing Oracle Java SE {#_installing_oracle_java_se}

To install Oracle Java SE:

1.  Navigate to [Oracle Java SE downloads
    page](https://www.oracle.com/java/technologies/javase-downloads.html),
    and choose the version of Java you wish to use.

2.  Accept the license agreement and download the appropriate tar.gz
    file for your systems architecture.

3.  Unpack the tar.gz file somewhere. For example, to extract it to the
    */opt* directory: &#96;sudo tar xf
    Downloads/jdk-25_linux-x64_bin.tar.gz -C /opt&#96;

4.  Set the *JAVA_HOME* environment variable to that directory. For
    example: &#96;export JAVA_HOME=/opt/jdk-25.0.1.1&#96;

Note: Always make sure to download latest version available.

## Switching between Java Versions {#_switching_between_java_versions}

You might have installed several versions of Java on your system, you
can switch from one.

After running this command, you will see a list of all installed Java
versions, select:

    sudo alternatives --config java

Simply enter a selection number to choose which java executable should
be used by default.

&#42; verify:

    java -version

## JDK reference {#_jdk_reference}

See the following list of Java-related acronyms for reference:

JRE

:   Java Runtime Environment; required to run Java code and applications

JVM

:   Java Virtual Machine; main component of the JRE

JDK

:   Java Development Kit; required only for development, coding

SDK

:   Software Development Kit; see JDK

JavaWS

:   [Java Web Start](https://en.wikipedia.org/wiki/Java_Web_Start) is a
    framework to start application from the Internet

JavaFX

:   [JavaFX](https://en.wikipedia.org/wiki/JavaFX) is a platform to
    create and deliver desktop and Rich Internet Apps

OpenJFX

:   is the JavaFX Open Source implementation

OpenJDK

:   Open Source project behind the Java Platform
    [openjdk.java.net](https://openjdk.java.net/).

IcedTea

:   is a support project for OpenJDK (concern only developers)
    [icedtea.classpath.org](http://icedtea.classpath.org/)

IcedTea-Web

:   is the Java Web Start package (contains only JavaWS, no applets
    anymore); install to run &#42;JNPL&#42; files

applets

:   are obsolete technology; Not implemented in any recent package

JSE, J2SE, JEE, &#8230;

:   obsolete acronyms for Java Standard &amp; Enterprise Edition; JavaSE
    is like JRE

**JDK components**

The JDK has as its primary components a collection of programming tools,
including:

&#96;appletviewer&#96;

:   this tool can be used to run and debug Java applets without a web
    browser

&#96;apt&#96;

:   the annotation-processing tool

&#96;extcheck&#96;

:   a utility which can detect JAR-file conflicts

&#96;idlj&#96;

:   the IDL-to-Java compiler. This utility generates Java bindings from
    a given Java IDL file.

&#96;jabswitch&#96;

:   the Java Access Bridge. Exposes assistive technologies on Microsoft
    Windows systems.

&#96;java&#96;

:   the loader for Java applications. This tool is an interpreter and
    can interpret the class files generated by the javac compiler. Now a
    single launcher is used for both development and deployment. The old
    deployment launcher, jre, no longer comes with Sun JDK, and instead
    it has been replaced by this new java loader.

&#96;javac&#96;

:   the Java compiler, which converts source code into Java bytecode

&#96;javadoc&#96;

:   the documentation generator, which automatically generates
    documentation from source code comments

&#96;jar&#96;

:   the archiver, which packages related class libraries into a single
    JAR file. This tool also helps manage JAR files.

&#96;javafxpackager&#96;

:   tool to package and sign JavaFX applications

&#96;jarsigner&#96;

:   the jar signing and verification tool

&#96;javah&#96;

:   the C header and stub generator, used to write native methods

&#96;javap&#96;

:   the class file disassembler

&#96;javaws&#96;

:   the Java Web Start launcher for JNLP applications

&#96;JConsole&#96;

:   Java Monitoring and Management Console

&#96;jdb&#96;

:   the debugger

&#96;jhat&#96;

:   Java Heap Analysis Tool (experimental)

&#96;jinfo&#96;

:   This utility gets configuration information from a running Java
    process or crash dump. (experimental)

&#96;jmap&#96;

:   This utility outputs the memory map for Java and can print shared
    object memory maps or heap memory details of a given process or core
    dump. (experimental)

&#96;jmc&#96;

:   Java Mission Control

&#96;jps&#96;

:   Java Virtual Machine Process Status Tool lists the instrumented
    HotSpot Java Virtual Machines (JVMs) on the target system.
    (experimental)

&#96;jrunscript&#96;

:   Java command-line script shell.

&#96;jstack&#96;

:   utility which prints Java stack traces of Java threads
    (experimental)

&#96;jstat&#96;

:   Java Virtual Machine statistics monitoring tool (experimental)

&#96;jstatd&#96;

:   jstat daemon (experimental)

&#96;keytool&#96;

:   tool for manipulating the keystore

&#96;pack200&#96;

:   JAR compression tool

&#96;policytool&#96;

:   the policy creation and management tool, which can determine policy
    for a Java runtime, specifying which permissions are available for
    code from various sources

&#96;VisualVM&#96;

:   visual tool integrating several command-line JDK tools and
    lightweight clarification needed\] performance and memory profiling
    capabilities

&#96;wsimport&#96;

:   generates portable JAX-WS artifacts for invoking a web service.

&#96;xjc&#96;

:   Part of the Java API for XML Binding (JAXB) API. It accepts an XML
    schema and generates Java classes.

The JDK also comes with a complete Java Runtime Environment, usually
called a private runtime, due to the fact that it is separated from the
\'regular\' JRE and has extra contents. It consists of a Java Virtual
Machine and all of the class libraries present in the production
environment, as well as additional libraries only useful to developers,
such as the internationalization libraries and the IDL libraries.

## Additional resources {#_additional_resources_3}

For Java in Fedora, see:

&#42; [java-devel mailing
list](https://admin.fedoraproject.org/mailman/listinfo/java-devel) &#42;
Freenode IRC channel
[&#35;fedora-java](irc://irc.freenode.net/fedora-java) &#42; [Ask Fedora
about Java](https://ask.fedoraproject.org/tags/java)

For more information about Java in general, see:

&#42; [Wikipedia page for
Java](https://en.wikipedia.org/wiki/Java_(programming_language)) &#42;
[OpenJDK homepage](https://openjdk.java.net/) &#42; [Oracle homepage for
Java](https://oracle.com/java/)

To develop Java applications, consider the following open-source IDEs:

&#42; [NetBeans](https://netbeans.org/) &#42;
[Eclipse](https://eclipse.org/) &#42; [IntelliJ
IDEA](https://www.jetbrains.com/idea/)

# Installing plugins for playing movies and music {#_installing_plugins_for_playing_movies_and_music}

Ankur Sinha ; Héctor Louzao ; Neil Gompa (ngompa) ; Dominik Mierzejewski
(rathann) :page-aliases:
assembly_installing-plugins-for-playing-movies-and-music.adoc

> As a Fedora user and system administrator, you can use these steps to
> install additional multimedia plugins that enable you to play various
> video and audio types.

## Procedure {#_procedure_5}

&#42; Use the &#96;dnf&#96; utility to install packages that provide
multimedia libraries:

\+

    sudo dnf group install Multimedia

&#42; For f41 and newer:

\+

    sudo dnf group install multimedia

# Installing Chromium or Google Chrome browsers {#_installing_chromium_or_google_chrome_browsers}

Peter Lilley;

## Chromium and Google Chrome web browsers {#_chromium_and_google_chrome_web_browsers}

Fedora Workstation, in its out of the box configuration, only includes
free and open source software. &#42;&#42;Mozilla Firefox&#42;&#42; is
the browser included in Fedora Workstation by default. However, it easy
to install either &#42;&#42;Google Chrome&#42;&#42; or
&#42;&#42;Chromium&#42;&#42;, if preferred.

### Chromium {#_chromium}

Chromium is the upstream project for Google Chrome. Chromium is included
in the Fedora Repositories. Fedora's Chromium package only contains free
and open source software, so does not include several features of Google
Chrome that rely on proprietary software.

### Google Chrome {#_google_chrome}

Google Chrome is a popular web browser developed by Google. Chrome is
built on top of the open-source browser project, Chromium. Chrome
includes additional features such as support for proprietary media files
(such as H.264 or AAC) and playback of rights-protected media (Netflix,
etc.) Chrome also includes support for other Google services such as
browser sync and location services, which are not supported by Chromium.

Google Chrome is available in Fedora Workstation via a curated
third-party repository. Once this repository is enabled, Chrome can be
installed via Software or the command line.

## Installing the browsers {#_installing_the_browsers}

Both Chromium and Google Chrome can be installed on Fedora.

### Installing Chromium {#_installing_chromium}

Chromium can be installed using the Software application and via command
line.

#### Installing Chromium using Software (GUI) {#_installing_chromium_using_software_gui}

1.  Click on Software tool in Fedora.

2.  Search for Chromium Web Browser.

3.  Click on Install.

#### Installing Chromium using Terminal {#_installing_chromium_using_terminal}

1.  To install Chromium Web Browser, use the command:

        \&#35; dnf install chromium

2.  To upgrade Chromium, use the command:

        \&#35; dnf upgrade chromium

### Installing Chrome {#_installing_chrome}

Chrome can be installed using Software or a terminal, once the
repository is enabled.

#### Installing Chrome using Software (GUI) {#_installing_chrome_using_software_gui}

1.  Open the &#42;Software&#42; application.

2.  Click on the menu at the top right and select &#42;Software
    Repositories&#42;.

3.  Make sure Third Party Repositories is enabled. If the button label
    is &#42;Install&#42;, then click that button to install the third
    party repositories. If the button reads &#42;Remove All&#42; then
    the third party repositories are already installed.

    ![installing chromium or google chrome browsers
    0](installing-chromium-or-google-chrome-browsers-0.png)

4.  Scroll down to find the repository called &#42;google-chrome&#42;.
    Click on it and choose &#42;Enable&#42;.

    ![installing chromium or google chrome browsers
    1](installing-chromium-or-google-chrome-browsers-1.png)

You can now search for &#42;Google Chrome&#42; in Software, and install
it.

#### Installing Chrome using Terminal {#_installing_chrome_using_terminal}

The additional repositories can also be managed using a terminal and
DNF.

1.  Install Third Party Repositories

        $ sudo dnf install fedora-workstation-repositories

2.  Enable the Google Chrome repo:

        $ sudo dnf config-manager setopt google-chrome.enabled=1

For Fedora 40 and older:

    $ sudo dnf config-manager --set-enabled google-chrome

\+ . Finally, install Chrome:

\+

    $ sudo dnf install google-chrome-stable

:::: note
::: title
:::

If you want to install the Chrome Dev Channel version, use the following
command:

    $ sudo dnf install google-chrome-unstable

If you want to install Chrome Beta use the following:

    $ sudo dnf install google-chrome-beta
::::

# Installing software from source on Fedora {#_installing_software_from_source_on_fedora}

ramin; Alan Bowman

Most of the software you will install on your Fedora system will either
come from a desktop application manager tool such as the [GNOME Software
tool](https://wiki.gnome.org/Apps/Software) or from a command line
package manager such as
[dnf](https://docs.fedoraproject.org/en-US/quick-docs/dnf/). These tools
make it easy to install, update, and if needed remove applications on
your system.

However, there might be times where you will need to install an
application from source, meaning to take the application source code and
compile it into a working application.

This can be because of the fact that:

&#42; No pre-compiled binary or application package is available. &#42;
You have specific dependency requirements that are not available in the
pre-compiled package. &#42; The available pre-compiled application is
out of date and you need a specific version.

In these cases you will need to install the software from the command
line, using the source files provided by the application developers or
maintainers.

## Before you start {#_before_you_start}

To install an application from source, you will need to have:

&#42; A way to extract the source file archive. This is usually an
application such as &#96;tar&#96; or &#96;gzip&#96;. &#42; A build tool
and a compiler, such as &#96;make&#96;.

These tools are generally installed by default on a modern Fedora
system. You can verify that they are available by typing in
&#96;make&#96;, &#96;tar&#96;, and &#96;gzip&#96; from the command line.
You will see instructions on how to use the application if it is
available. If the application is not available you will get an error
along with instructions on how to install.

## How to install from source {#_how_to_install_from_source}

To install from source, you will need to do the following:

1.  Download the application archive file to your computer. The default
    location is the Downloads folder, but you might be able to choose a
    location during the download process.

2.  Extract the files from the downloaded archive. The command you use
    will depend on the application package.

3.  Carefully read any instructions that came with your download. These
    instructions might also be available on the website you downloaded
    the file from. These instructions will tell you what you need to do
    to install the application.

4.  Follow the commands given in the README (or other installation
    instructions) to configure, build, compile, and install the
    application.

### Download the application archive to your computer {#_download_the_application_archive_to_your_computer}

The default download location is your Downloads folder. From the command
line the location is &#96;/home/username/Downloads&#96; (note the
capital D in Downloads).

### Extract the files from the archive {#_extract_the_files_from_the_archive}

Most applications require many files or even directories, packaged
together into an archive. The most common archives are \'tarballs,\'
with the files packaged by using the &#96;tar&#96; (tape archive)
command. These will have a &#96;.tar&#96; file extension.

In some cases the files will use a variation of the Zip archive format,
such as &#96;.zip&#96; or &#96;.gz&#96;. Depending on the size of the
download the application developer might use both &#96;tar&#96; and
&#96;gzip&#96; together, so that the file will have a &#96;.tar.gz&#96;
extension.

To extract files from a &#96;.tar&#96; archive:

``` _bash
$ tar -xf archive.tar
```

&#96;-xf&#96; means to e&#42;&#42;x&#42;&#42;tract the
&#42;&#42;f&#42;&#42;iles from the &#96;tar&#96; archive.

To extract files from a &#96;tar.gz&#96; archive:

``` _bash
$ tar -zxf archive.tar.gz
```

&#96;-zxf&#96; means to un&#42;&#42;z&#42;&#42;ip the archive, and
e&#42;&#42;x&#42;&#42;tract the &#42;&#42;f&#42;&#42;iles from the
&#96;tar&#96; archive.

To extract files from a &#96;.gz&#96; archive:

``` _bash
$ gzip -d archive.gz
```

&#96;-d&#96; means to &#42;&#42;d&#42;&#42;ecompress the archive, which
extracts the files.

You can also use &#96;gunzip&#96;, which is an alias for &#96;gzip
-d&#96;.

``` _bash
$ gunzip archive.gz
```

To extract files from a &#96;.zip&#96; archive:

``` _bash
$ unzip archive.zip
```

Use the &#96;man&#96; command to learn more about &#96;tar&#96;,
&#96;gzip&#96;, and &#96;unzip&#96;: &#96;man tar&#96;, &#96;man
gzip&#96;, or &#96;man unzip&#96;. You can also find their &#96;man&#96;
pages online: [Linux man pages](https://linux.die.net/man/). Search for
the command you want to look up.

The &lt;&lt;See also&gt;&gt; section has links to the official
documentation for these commands.

### Carefully read any instructions that came with your download {#_carefully_read_any_instructions_that_came_with_your_download}

When you extract the archive it will leave you with a directory with the
same or similar name. You can now change into that directory to find the
installation instructions that tell you how to configure and build the
application.

The extracted folder for the application will have a README or some
other file that gives instructions on how to install, configure, and
manage the application. The README file will have detailed directions on
things such as:

&#42; Choosing an alternate directory for installation. &#42; Setting
configuration options for the build. &#42; What compile time options to
use for different configurations.

:::: note
::: title
:::

If no instructions exist on how to configure or build the application,
you will need to reach out to the application developers for help. You
might also find instructions online from someone else who had a similar
issue.
::::

### Follow the instructions to configure, build, compile, and install the application {#_follow_the_instructions_to_configure_build_compile_and_install_the_application}

After you understand what options are available, you can install the
application. In general you will need to:

1.  Configure the application by using the &#96;configure&#96; command.

2.  Build and compile the application by using &#96;make&#96;.

3.  Install the application by using &#96;make install&#96;. The
    &#96;make install&#96; command will need to run using &#96;sudo&#96;
    so it can write to system directories and local directories.

Here is an example of the entire process, from extracting the files from
a &#96;.tar.gz&#96; archive to building the application:

``` bash
$ tar -zxf archive.tar.gz
$ cd archive/
$ ./configure
$ make
$ sudo make install
```

Your application is now installed. The README file or the application
website will have more information about how to use the application.

:::: note
::: title
:::

If you get any errors during the configure and build process, carefully
read the error messages and follow the instructions on how to resolve
them. There can be dependency issues for some applications, meaning that
to install application C, you need to have applications A and B
installed. Resolving dependency issues can be challenging and you might
need to look for help online to help solve the problem.
::::

**See also**

&#42; [GNU Make (build and compile tool)
documentation](https://www.gnu.org/software/make/) &#42; [GNU Tar
documentation](https://www.gnu.org/software/tar/) &#42; [GNU Gzip
documentation](https://www.gnu.org/software/gzip/)

# Installing Spotify on Fedora {#_installing_spotify_on_fedora}

Ankur Sinha; Weverton do Couto Timoteo; Mohammadreza Hendiani

:::: caution
::: title
:::

This page discusses third-party software sources not officially
affiliated with or endorsed by the Fedora Project. Use them at your own
discretion. Fedora recommends the use of free and open source software
and avoidance of software encumbered by patents.
::::

[Spotify](https://www.spotify.com/) is a cross-platform proprietary
music streaming service. Spotify is a freemium service, with
advertisements which can be removed by purchasing a subscription.
Although Spotify is not officially supported on Fedora, it can be
installed on Fedora in a number of ways:

1.  Using a Flatpak hosted by [Flathub](https://flathub.org).

2.  Using Snap hosted by [snapcraft](https://snapcraft.io/spotify).

3.  Using the third-party [RPM Fusion](https://rpmfusion.org/)
    repositories.

To install Spotify using [Flatpak](https://flatpak.org/index.html):

1.  Install Flatpak using DNF:

        sudo dnf install -y flatpak

2.  Enable the Flathub remote:

        flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo

3.  Install Spotify:

    a.  Using Gnome Software: &#8230; Head to the [Spotify page on
        Flathub](https://flathub.org/apps/details/com.spotify.Client).
        &#8230; Click \'install\', and choose to open the file using
        Gnome Software. &#8230; Click \'install\' in Gnome Software.
        &#8230; Click \'launch\' to run Spotify once installed.

    b.  Using the command line:

            flatpak install flathub com.spotify.Client

4.  Run Spotify:

    a.  Click on the Spotify icon in the applications list,

    b.  or use the following command in the terminal:

            flatpak run com.spotify.Client

To install Spotify using [Snap](https://snapcraft.io/spotify):

1.  Install Snap using DNF:

        sudo dnf install snapd

2.  Either log out and back in again, or restart your system, to ensure
    snap's paths are updated correctly.

3.  To enable classic snap support, enter the following to create a
    symbolic link between &#96;/var/lib/snapd/snap&#96; and
    &#96;/snap&#96;:

        sudo ln -s /var/lib/snapd/snap /snap

4.  Install spotify, simply use the following command:

        snap install spotify

5.  Click on the Spotify icon in the applications list.

For this method, please refer to the [&#96;lpf GitHub
Page&#96;](https://github.com/leamas/lpf) requirements.

1.  [Enable the RPMFusion repositories](rpmfusion-setup.xml).

2.  Install the &#96;lpf-spotify-client&#96; package:

        sudo dnf install lpf-spotify-client

3.  Install Spotify:

    a.  Click the \'lpf-spotify-client\' icon in the application list.

    b.  or use the following command in a terminal:

            lpf update

## References {#_references_3}

1.  <https://flathub.org/apps/details/com.spotify.Client>

2.  <https://snapcraft.io/install/spotify/fedora>

3.  <https://github.com/rpmfusion/lpf-spotify-client>

4.  <https://github.com/leamas/lpf>

5.  <https://www.spotify.com/us/download/linux/>

# Installing Zoom on Fedora {#_installing_zoom_on_fedora}

Akshata Khedekar

:::: caution
::: title
:::

This page discusses third-party software sources not officially
affiliated with or endorsed by the Fedora Project. Use them at your own
discretion. Fedora recommends the use of free and open source software
and avoidance of software encumbered by patents.
::::

## Description {#_description}

[Zoom Video Communications](https://www.zoom.us). Inc. is an American
communications technology company headquartered in San Jose, California.
It provides videotelephony and online chat services through a
cloud-based peer-to-peer software platform and is used for
teleconferencing, telecommuting, distance education, and social
relations.

## How to Setup {#_how_to_setup}

In Fedora one can setup zoom using either of the following options

### Download the RPM {#_download_the_rpm}

If you're using Fedora Workstation Edition, you can install Zoom using
the GNOME application center. Note that this option doesn't
automatically update Zoom when a new version is released.

&#42; Download the RPM installer file at our [Download
Center](https://zoom.us/download?os=linux). &#42; Open the download
location using a file manager. &#42; Double click the RPM installer file
to open it in the GNOME application center. &#42; Click Install. &#42;
Enter your admin password and continue the installation when prompted.

### Install the Zoom DNF repo {#_install_the_zoom_dnf_repo}

Download and import the Zoom DNF repo, and import the GPG key. Enter
your admin password when prompted by sudo: &#8230;. sudo curl
\--location <https://repo.zoom.us/repo/rpm/zoom_release.repo> \--output
/etc/yum.repos.d/zoom_release.repo sudo rpmkeys \--import
<https://zoom.us/linux/download/pubkey?version=6-3-10> &#8230;.

Then install Zoom itself: &#8230;. sudo dnf install zoom &#8230;.

# OpenH264 {#_openh264}

Caleb McKee

> This page contains information on the Cisco
> [OpenH264](https://www.openh264.org/) codec.

## Background {#_background}

Cisco provides an OpenH264 codec (as a source and a binary), which is
their implementation of the H.264 codec, and they cover all licensing
fees for all parties using their binary. This codec allows you to use
H.264 in WebRTC with gstreamer and Firefox. It does &#42;not&#42; enable
generic H.264 playback, only WebRTC (see [Mozilla bug
1057646](https://bugzilla.mozilla.org/show_bug.cgi?id=1057646)).

The code source is available at <https://github.com/cisco/openh264>
under a BSD license. The binary is released under this agreement from
Cisco: <https://www.openh264.org/BINARY_LICENSE.txt>

Upstream Firefox versions download and install the OpenH264 plugin by
default automatically. Due to its binary nature, Fedora disables this
automatic download.

## Installation from fedora-cisco-openh264 repository {#_installation_from_fedora_cisco_openh264_repository}

A &#96;fedora-cisco-openh264&#96; repository is distributed since Fedora
24 by default (if you have at least &#96;fedora-repos-24-0.5&#96;
package or newer). It contains the OpenH264 binary [built inside the
Fedora infrastructure](Non-distributable-rpms), but distributed by
Cisco, so that the all licensing fees are still covered by them. This
repository also contains OpenH264 plugins for gstreamer and Firefox. It
is enabled by default since Fedora 33 (if you have at least
&#96;fedora-repos-33-0.3&#96; package or newer). In order to install
OpenH264, just install the plugins:

&#8230;. \$ sudo dnf install gstreamer1-plugin-openh264 mozilla-openh264
&#8230;.

Afterward, you need to open Firefox, go to menu -&gt; Add-ons -&gt;
Plugins and enable OpenH264 plugin.

You can do a simple test whether your H.264 works in RTC on [this
page](https://mozilla.github.io/webrtc-landing/pc_test.html) (check
*Require H.264 video*).

## Manual installation of binary {#_manual_installation_of_binary}

&#42; View and agree to the
<https://www.openh264.org/BINARY_LICENSE.txt> &#42; Download the
appropriate binary for your system here:
<https://github.com/cisco/openh264/releases>

Example installation for version 1.1:

&#8230;.
wget <http://ciscobinary.openh264.org/openh264-linux64-v1.1-Firefox33.zip>\
mkdir -p \~/.mozilla/firefox/&lt;yourprofile&gt;/gmp-gmpopenh264/1.1/\
cd \~/.mozilla/firefox/&lt;yourprofile&gt;/gmp-gmpopenh264/1.1/\
unzip \~/openh264-linux64-v1.1-Firefox33.zip &#8230;.

## Firefox config changes {#_firefox_config_changes}

Type about:config into the Firefox address/URL field and accept the
warning.

&#42; From the Search field, type in 264 and a handful of options will
appear. Give the following Preference Names a value of true by
double-clicking on false:

&#8230;. media.gmp-gmpopenh264.autoupdate media.gmp-gmpopenh264.enabled
media.gmp-gmpopenh264.provider.enabled
media.peerconnection.video.h264_enabled &#8230;.

&#42; Restart Firefox &#42; After restarting, the following string in
about:config will change to the current version that has been installed
from the web:

&#8230;. media.gmp-gmpopenh264.version &#8230;.

See a typo, something missing or out of date, or anything else which can
be improved? Edit this document at
<https://pagure.io/fedora-docs/quick-docs>.

# Package management system {#_package_management_system}

Caleb McKee ; Otto Urpelainen; Ben Cotton

## Package Management System {#package-management-system}

### Introduction {#introduction}

Fedora is a distribution that uses a package management system. This
system is based on [rpm](https://rpm.org) , the RPM Package Manager,
with several higher level tools built on top of it, most notably
[PackageKit](https://www.freedesktop.org/software/PackageKit/) (default
gui) and [DNF](dnf.xml). GNOME Software is another GUI package manager.

### Advantages of package management systems

Package management systems have many advantages:

&#42; It's easy to query what version of a package is installed or
available.

&#42; It's easy to remove a package entirely, making sure all its files
are gone.

&#42; It's easy to verify the integrity of the packages files, so you
can see if it's been corrupted or tampered with.

&#42; It's easy to upgrade a package by installing the new version and
removing all the old versions files. This will make sure not to leave
any lingering files from the old package around to confuse or break
things.

&#42; It's easy to see what packages require or provide things that
other packages provide or require, so you can be sure to have the needed
items for the package to function correctly.

&#42; It's easy to install or remove groups of packages.

&#42; In many cases it's possible to downgrade back to a previous
version of a package, for example when a new version has a bug.

### Disadvantages of package management systems

&#42; You are restricted to either using the versions of the package
that are available or having to make your own package if you need a
different version.

### Why mixing source installs and packages is a bad idea

Package management systems have no way to query or note when you bypass
them and install something from source. You should avoid mixing source
installs and packaged installs for (at least) the following reasons:

&#42; You lose all the advantages above from a package managed system.

&#42; Installing from source may overwrite, delete, or change existing
files that are in a package, making that package not function correctly.

&#42; The source install may override a package install causing
undefined behavior in the package or source installed item.

&#42; Installing from source makes it impossible or very difficult for
anyone to help you debug issues, since versions can't be easily queried
and integrity checked.

&#42; Fedora packages may include patches or configuration to work with
other packages, but upstream source does not, leading to loss of
functionality.

&#42; Software installed from source will not upgrade with package
managed packages, leading to breakage in the source install package on
upgrades or os updates.

Strongly consider making your own package if you need a different
version or a version of some package with changes. See: [Packaging
Tutorial: GNU
Hello](package-maintainers::Packaging_Tutorial_GNU_Hello.xml)

### Preferred search order for a software

If some software is missing in your installation then you should try the
following steps to get the packaged version:

1.  Search in Fedora ( \'dnf search foo\' or search for \'foo\' in the
    PackageKit gui )

2.  Try one of the available [third-party
    repositories](finding-and-installing-linux-applications.adoc&#35;_enabling_third_party_repositories)

3.  [Build your own
    package](package-maintainers::Packaging_Tutorial_GNU_Hello.xml)

### Package Management tools

Here are some tools for managing packages:

&#42; [dnf](dnf.xml) - Dandified Yum &#42;
[PackageKit](https://www.freedesktop.org/software/PackageKit/) -
PackageKit gui tool (\'add/remove software\' in your menu) &#42; [GNOME
Software](https://wiki.gnome.org/Apps/Software) - ­Graphical package
manager for GNOME &#42; [KDE Discover](https://apps.kde.org/discover/) -
Graphical package manager for KDE Plasma &#42; [rpm](https://rpm.org) -
RPM package manager. &#42;
[yumex](https://github.com/timlau/yumex-dnf) - Yum Extender

See a typo, something missing or out of date, or anything else which can
be improved? Edit this document at
<https://pagure.io/fedora-docs/quick-docs>.

# PackageKit Items Not Found {#_packagekit_items_not_found}

Caleb McKee; Frank Sträter

## Missing Package

Unfortunately, the package you were searching for is not available in
Fedora. There are a few common reasons why a package might not be in
Fedora's repositories:

&#42; Fedora does not include software that is [encumbered by software
patents](Package_Not_Found&#35;Patents). &#42; Fedora does not include
proprietary software, only software with an [acceptable
license](Licensing). &#42; It is possible that no one has packaged it
yet. You might consider adding it to the [Package
WishList](PackageMaintainers/WishList), or even [packaging it
yourself](PackageMaintainers/Join)!

## Missing Codec

Unfortunately, the codec you were searching for is not available in
Fedora. A codec is a program that enables encoding and/or decoding of a
data stream, in a specific format such as MP3, MOV, or WMV.

There are a few common reasons why a codec might not be in Fedora's
repositories:

&#42; Many codecs are proprietary or [patent
encumbered](Package_Not_Found&#35;Patents). &#42; Some codecs may not be
encumbered, but may be under an [unacceptable license](Licensing).

The Fedora Project FAQ and community sites provide answers to commonly
asked questions. [Third party repositories](Third_party_repositories)
contain a wide variety of software that has not been included in the
official Fedora software repositories for various reasons. You can find
additional software using a search engine like
[Google](https://google.com). We would love to give you more specific
instructions on enabling additional codecs but our hands are tied up due
to software patents and legal restrictions around them. We apologize for
the inconvenience caused by software patents and our legal team is
working on getting these restrictions removed when it is possible to do
so. Scroll down more for details on what we are doing and how you can
help.

## Missing Driver

Unfortunately, the driver you were searching for is not available in
Fedora. There are a few common reasons why a driver might not be in
Fedora's repositories:

&#42; Some drivers are proprietary or [patent
encumbered](Package_Not_Found&#35;Patents). &#42; Some hardware may not
be supported under Linux yet, or is not yet in the upstream Linux
kernel.

Fedora strongly encourages new drivers to be included in upstream, and
does not package individual, out-of-tree, kernel drivers.

The Fedora Project FAQ and the more informal, unofficial
[1](http://fedorafaq.org) provide useful answers on commonly asked
questions. However, the unofficial site is not associated with or
supported by the Fedora Project. You can find many interesting things
using a search engine like [Google](https://google.com). [Third party
repositories](Third_party_repositories) might contain software that has
been not been included in the official Fedora software repository.

## Missing Font

Unfortunately, the font you were searching for is not available in
Fedora. There are a few common reasons why a font might not be in
Fedora's repositories:

&#42; Fedora does not include proprietary fonts, it only uses fonts with
an [acceptable font license](Licensing/Fonts). &#42; It is possible that
no one has packaged that font yet. You might consider adding it to the
:Category:Font_wishlist\[Font WishList\], or even [packaging it
yourself](PackageMaintainers/Join)!

## Missing MIME Support

Unfortunately, there is nothing in Fedora that claims to support the
MIME type you were searching for. There are a few common reasons why
Fedora may not have support for a MIME type:

&#42; Many MIME types are Windows-only. You may be able to use
[Wine](https://en.wikipedia.org/wiki/Wine_(software)) to run a Windows
program under Linux that supports your MIME type. &#42; Some MIME types
are only supported by proprietary or [patent
encumbered](Package_Not_Found&#35;Patents) software. &#42; It is
possible that acceptable software to support your MIME type exists, but
that no one has packaged it yet. You might consider adding it to the
[Package WishList](PackageMaintainers/WishList), or even [packaging it
yourself](PackageMaintainers/Join)!

## Fedora Position on Software Patents

:::: warning
::: title
:::

This information is provided only for answering common questions from
Fedora users and should not be read as legal advice. What applies to Red
Hat and the Fedora Project may not necessarily apply to you. If you need
legal assistance, consult your own lawyer. This material does not
represent the official views of Red Hat or the Fedora Project.
::::

### What is a software patent?

A patent is a set of exclusionary rights granted by a government to a
patent holder for a limited period of time, usually 20 years from the
earliest effective filing date of the patent application. These monopoly
rights are granted to patent applicants in exchange for their disclosure
of the invention claimed by the patent. Once a patent is granted in a
given country, the patent holder may exclude someone from making, using,
selling or importing embodiments of the claimed invention in that
country. Software patents are different from copyright or trademarks
despite being lumped together with them under the collective term
[Intellectual Property](https://www.gnu.org/philosophy/not-ipr.html).

### Who is responsible for taking care of any legal issues in Fedora?

The Fedora Project is not a separate and distinct legal entity. Red Hat,
the primary sponsor of the Fedora Project, is actively involved in legal
matters relating to Fedora, along with other Fedora participants. For
example, Red Hat lawyers assist Fedora Project contributors in issues
pertaining to free and open source software licensing, trademarks and
patents. Refer to the
[Legal](https://fedoraproject.org/wiki/Legal:Main?rd=Legal) page for
more information.

### If Software patents are not recognized in all regions, why can't you distribute Fedora with such software in other regions? {#if-software-patents-are-not-recognized-in-all-regions-why-not}

Contrary to common belief, software patents are granted in some form or
other in most countries, including most of the countries in which most
Fedora participants reside.

### Can't you pay the patent license fees for patent encumbered codecs?

A codec is a set of methods to encode and decode video or audio
information into a data stream. In the case of codecs like MP3 or WMV,
the company or companies associated with developing the format are also
involved in asserting (or restrictively licensing) patents that
purportedly cover the format; we refer to such codecs as \'patent
encumbered\'. Other codecs, such as WebM, Ogg Theora or Ogg Vorbis,
Dirac, and FLAC, are made available by their developers without
asserting patents on their implementations; we refer to such codecs as
\'patent unencumbered\'. Fedora includes comprehensive support for open,
patent-unencumbered codecs but is unable to include support for the
patent encumbered ones.

Patent licenses usually require the licensee to pay royalties based on
the number of users. Since Fedora is free and open source software, the
effective number of users is essentially unrestricted. Patent holders
are generally unwilling to give a blanket patent license for unlimited
use; moreover, the royalty payments would be too high for it to be
practical for the Fedora Project, or its sponsors, to pay them.
Proprietary operating systems like Microsoft Windows [include the costs
of third-party patent licenses paid by Microsoft in the pricing of the
product](https://www.softwarefreedom.org/resources/2007/patent-tax.html)
as sold to end users. Fedora is not sold commercially, so there is no
way to recoup these substantial expenses.

Even if funds were available to do so, such royalty-bearing patent
licenses would have to be compatible with the free/open source software
licenses governing the software covered by the patent license. In
practice this is usually challenging. For example, the most widely-used
FOSS licenses (GPL and LGPL) place constraints on the ability of
distributors to distribute software under benefit of third-party patent
licenses. Even if the software in question is placed under some other
license, distributing such software under benefit of a patent license
may make the software effectively non-free and thus incompatible with
Fedora legal policies.

Note that Fluendo offers an [MP3
plugin](https://fedoraproject.org/wiki/Installing_the_Fluendo_MP3_plugin)
for the Gstreamer multimedia framework (used by Totem, Rhythmbox and
other multimedia applications) for free and other codecs and DVD player
for a price that includes patent licenses. Fedora does not include or
endorse these options but you can choose to use them with Fedora if you
want to.

### There are free and open software implementations of the codecs. Why don't you include them? {#there-are-free-and-open-software-implementations-of-the-codecs}

When we speak of an implementation being FOSS, usually we are thinking
only in terms of copyright licensing. An independent FOSS implementation
of a patent-encumbered codec, however, is subject to at least as much
patent risk as, say, some proprietary reference implementation of the
same codec. Note that while copyright covers only a particular
implementation of software, patents are broader because they are more
abstract, covering ideas that might be implemented in software in any
number of ways.

### Can't you link to third party repositories and guide users to find such software? {#cant-you-link-to-third-party-repositories-and-guide-users-to-find}

In general, no, because of the risk of liability for [contributory
patent infringement](https://en.wikipedia.org/wiki/Patent_infringement).
Refer
[here](https://www.redhat.com/archives/fedora-advisory-board/2007-November/msg00050.html)
for more details.

### How is it that some other Linux distributions include such software?

There are different reasons:

&#42; Some of them include proprietary software, in some cases charging
users for their product, where the charge incorporates the cost of
licensing third-party patents. Fedora is not a commercial product and
has a policy of not distributing proprietary software. &#42; They are
willing to deal with the risk somehow. In some cases, it is because they
are not backed by a large and profitable company like Red Hat. Red Hat,
the legal entity and primary sponsor of the Fedora Project determines
its own risks which can be different from other organizations.

### What is bad about patented formats?

Even if you are willing to pay for patent licenses, there are other
things to consider:

&#42; No guarantee that your consumers actually will be able to read the
data you're trying to produce. If you've reached this page, you've
already experienced this - by producing media in a patented format, you
automatically limit your audience to whatever platforms the patent
holder has licensed their software to. &#42; No guarantee of being able
to access your data forever. If you're using some software to view a
patented media format, what happens if that software vendor goes out of
business, or refuses to port their software to newer systems? You no
longer have access to your data.

Note that this isn't even restricted to patented media formats - the
same applies to popular proprietary formats used for word processing,
spreadsheets, presentations, etc.

For more information about how software patents are bad, refer to the
[Foundation for a Free Information Infrastructure](https://ffii.org/).

### Can't you convert a patent encumbered codec to an open codec? {#cant-you-convert-a-patent-encumbered-code-to-an-open-codec}

Fedora cannot include the decoders necessary to do this since those are
patent encumbered as well. Although users might be able to do this,
converting from one format to another typically results in a visible
loss of quality. The only long term viable method is to encourage the
creation of content in open formats and Fedora and Red Hat actively
encourage and participate in such activities.

## How Fedora works against software patents

&#42; *Fedora sponsors development of free, non-patent-encumbered open
formats*

In support of free culture and the open web, and to reduce the hold of
proprietary and patent encumbered codecs, Red Hat has been sponsoring
improvements on the open Ogg Theora video codec. For example Red Hat has
funded work on the newest implementation, codenamed Thusnelda, via
Christopher Montgomery (xiphmont), who created the format. That work has
resulted in dramatic improvements to the codec.

&#42; *Fedora uses free, non-patented, open formats by default that
anyone can implement, use, and view without having to obtain patent
licenses*

Instead of MP3, use Ogg Vorbis. Instead of Windows Media, use WebM or
Ogg Theora. Instead of Microsoft Office Open XML, use [Open Document
format](https://en.wikipedia.org/wiki/OpenDocument) documents, or even
PDF. Vote with your currency by purchasing hardware and solutions that
support these free and open formats.

## The problem with proprietary and patent encumbered media formats {#the-problem-with-prorietary-and-patent-encumbered-media-formats}

Imagine sitting down to your email. Your sister has sent you some
pictures of your niece. However, when you go to look at them, all you
see is:

*I'm sorry, you need Frobozz Viewer 3.0 to view this file. It's only
\$19.99, please have your credit card ready.*

Later, you go to view your mail on a public computer at the local
library. And you get the same dialog box on their computer.

That is the reality for any sound, image, or document format that is
encumbered by software patents that require licensing - any application
that wishes to view, play, or create them requires paying the patent
holders a fee. Normally, software and hardware vendors include this
support, but they pass the costs directly onto the consumers in the cost
of their software or hardware. For every copy of Microsoft Windows that
you buy, or every DVD player that is sold, a portion of that cost goes
directly to pay patent licenses; in fact, for DVD players, it can be
over a quarter of the final cost.

And, since that patent license applies to every copy in use, it's one of
the reasons why you are not allowed to freely copy and redistribute
software such as Microsoft Windows (although, to be sure, even if
software patents did not exist, Microsoft would be unlikely to make
Windows free software).

Fedora, however, has a [public
promise](https://docs.fedoraproject.org/en-US/project/objectives/) to
always be freely redistributable by anyone. That is why Fedora cannot
include support for patented media formats - it would break this
redistribution promise. This means that, out of the box, you can't
directly play media files such as Windows Media, MPEG-4 video, or MP3
audio. Fedora supports open media formats such as WebM or Ogg
[Vorbis](https://xiph.org/vorbis/) and
[Theora](https://www.theora.org/), which are &#42;&#42;freely
implementable and usable by anyone without a patent license&#42;&#42;.

Red Hat has consistently taken the position that software patents
generally impede innovation in software development and that software
patents are inconsistent with open source/free software. Red Hat holds a
number of software patents for defensive purposes and has a patent
policy under which it agrees to refrain from enforcing its patents
against any party for exercising rights under certain free and open
source software licenses, including GPLv2, GPLv3, LGPLv2.1, and LGPLv3.

&#42; <https://www.redhat.com/en/about/patent-promise>

Red Hat explained why software patents are problematic to the European
Patent Office.

&#42;
<http://press.redhat.com/2009/04/30/old-world-and-new-world-software-patent-problems/>

Red Hat filed a friend of court briefing to the U.S. Federal Court
asking it to limit software patents.

&#42;
<http://press.redhat.com/2008/04/07/red-hat-asks-federal-court-to-limit-patents-on-software/>

The court's ruling has been applied by lower courts and the U.S. Patent
and Trademark Office to invalidate some software patents.

&#42;
<http://press.redhat.com/2008/11/03/bilski-and-software-patents-%E2%80%93-good-news-for-foss/>

Red Hat again filed a friend of court briefing to the U.S. Supreme Court
as a follow-up on the same case.

&#42;
<http://press.redhat.com/2009/10/01/asking-the-supreme-court-to-address-the-problem-of-software-patents/>

Red Hat also filed a response to U.S. patent and trademark office.

&#42;
<http://press.redhat.com/2010/09/28/red-hat-responds-to-u-s-patent-and-trademark-office-request-for-guidance-on-bilski/>

December 2010, Red Hat filed brief with U.S. Supreme Court opposing
expansion of standard for inducing patent infringement.

&#42; <http://www.redhat.com/about/news/prarchive/2010/amicus.html>

## References {#references}

&#42; <https://fedoraproject.org/wiki/Forbidden_items> &#42;
<https://docs.fedoraproject.org/en-US/project/> &#42;
<https://www.fsf.org/campaigns/playogg/en/> &#42;
<https://www.gnu.org/philosophy/why-audio-format-matters.html> &#42;
<https://dwheeler.com/essays/software-patents.html>

See a typo, something missing or out of date, or anything else which can
be improved? Edit this document at
<https://pagure.io/fedora-docs/quick-docs>.

# Securing the system by keeping it up-to-date {#_securing_the_system_by_keeping_it_up_to_date}

Petr Bokoc; Mirek Jahoda; Gregory Lee Bartholomew

This section explains:

&#42; [Why it is important to update your system
regularly](securing-the-system-by-keeping-it-up-to-date.adoc&#35;_why_it_is_important_to_keep_your_system_up_to_date)
&#42; How to apply updates manually by using the
[GUI](securing-the-system-by-keeping-it-up-to-date.adoc&#35;_manual_updating_using_gui)
or
[CLI](securing-the-system-by-keeping-it-up-to-date.adoc&#35;_manual_updating_using_cli)
&#42; How to [enable automatic
updates](securing-the-system-by-keeping-it-up-to-date.adoc&#35;_setting_automatic_updates)

## Why it is important to keep your system up-to-date {#_why_it_is_important_to_keep_your_system_up_to_date}

This section briefly explains the importance of updating your system on
a regular basis.

All software contains bugs. Often, these bugs can result in a
vulnerability that can expose your system to malicious users. Packages
that have not been updated are a common cause of computer intrusions.
Implement a plan for installing security patches in a timely manner to
quickly eliminate discovered vulnerabilities, so they cannot be
exploited.

## Manual updating using GUI {#_manual_updating_using_gui}

This section describes how to manually download and install new updates
by using GUI.

**Procedure**

1.  Hover the cursor over the upper-left corner of the screen and type
    \'Software\' and select the Software application to open it.

2.  Click the Updates button to view the available updates.

3.  Click the Download button to download new updates.

4.  After the updates are downloaded click the Restart &amp; Update
    button. Your system will restart to perform the upgrade.

![Updating by using the Software application](software-updates.png)

## Manual updating using CLI {#_manual_updating_using_cli}

This section describes how to manually download and install new updates
by using the DNF package manager.

**Procedure**

1.  Upgrade the system:

        sudo dnf upgrade

    Confirm to download the available packages.

2.  Ideally (but it is usually not required), use the &#96;rpmconf&#96;
    command to merge any config file changes you may have made with any
    new settings that might have been introduced by the package updates.
    You should do this before you reboot your system:

        sudo rpmconf -a

    To use the advanced merge option, you will need to set the
    &#96;MERGE&#96; environment variable to an editor that is capable of
    performing that function (e.g., &#96;export MERGE=\'vimdiff\'&#96;).
    See the man page for details.

    :::: tip
    ::: title
    :::

    If you install the rpmconf DNF plugin, &#96;rpmconf&#96; will run
    automatically at the end of each upgrade. Install it using the
    command:

        sudo dnf install python3-dnf-plugin-rpmconf
    ::::

**Additional Resources**

&#42; The &#96;dnf(8)&#96; manual page &#42; The &#96;rpmconf(8)&#96;
manual page

## Setting automatic updates {#_setting_automatic_updates}

This section describes how to use the DNF Automatic application to
automatically:

&#42; Download and install any new updates &#42; Only download the
updates &#42; Get notified about the updates

**Procedure**

1.  Install the *[dnf-automatic]{.package}* package:

        sudo dnf install dnf-automatic

2.  Edit the \[filename\]&#96;/etc/dnf/automatic.conf&#96; configuration
    file as needed. See the [DNF
    Automatic](https://dnf.readthedocs.io/en/latest/automatic.html)
    documentation for details.

3.  Enable and start the &#96;systemd&#96; timer:

        sudo systemctl enable --now timer

    Replace &#96;\_timer\_&#96; with one of following ones depending on
    what action you want to do:

    &#42; &#96;dnf-automatic-install.timer&#96; to download and install
    packages &#42; &#96;dnf-automatic-download.timer&#96; to only
    download packages &#42; &#96;dnf-automatic-notifyonly.timer&#96; to
    only get a notification using configured emitters in the
    \[filename\]&#96;/etc/dnf/automatic.conf&#96; file.

    For example:

        sudo systemctl enable --now dnf-automatic-install.timer
        Created symlink /etc/systemd/system/timers.target.wants/dnf-automatic-install.timer → /usr/lib/systemd/system/dnf-automatic-install.timer.

4.  Ensure that the timer has been successfully enabled and started:

        sudo systemctl status timer

    Replace &#96;\_timer\_&#96; with the timer from the previous step,
    for example:

        sudo systemctl status dnf-automatic-install.timer
        ● dnf-automatic-install.timer - dnf-automatic-install timer
        Loaded: loaded (/usr/lib/systemd/system/dnf-automatic-install.timer; enabled; vendor preset: disabled)
        Active: active (waiting) since Fri 2021-01-29 14:50:22 +08; 1s ago
        Trigger: Sat 2021-01-30 06:05:57 +08; 15h left
        Triggers: ● dnf-automatic-install.service

        Jan 29 14:50:22 localhost.localdomain systemd[1]: Started dnf-automatic-install timer.

**Additional Resources**

&#42; The [DNF
Automatic](https://dnf.readthedocs.io/en/latest/automatic.html)
documentation

**Additional Resources**

&#42; The
[DNF](f43@fedora:system-administrators-guide:package-management/DNF.xml)
chapter in the Fedora System Administrator's Guide

# Switching desktop environments {#_switching_desktop_environments}

Fedora Documentation Team

> Different Fedora Linux variants (Spins/Labs) have different default
> environments. For example, the Fedora workstation uses GNOME as its
> default desktop environment, while the KDE spin will use KDE.
> Irrespective of what installation media you used to install Fedora
> Linux, you can easily try and switch to any of the many other desktop
> environments that are available without affecting your current desktop
> environment.

## Installing additional desktop environments {#installing-desktop-environments}

You can list available desktop environments using the default package
manager, &#96;dnf&#96;.

Since Fedora 41, in a terminal use the &#96;dnf environment list&#96;
command to list all available desktop environments:

``` bash
dnf environment list --available | grep desktop
```

For older Fedoras, use the &#96;dnf group list&#96; command to list all
available desktop environments:

``` bash
dnf group list -v --available | grep desktop
```

Install the required desktop environment using the &#96;dnf install&#96;
command. Ensure to prefix with the &#96;@&#96; sign, for example:

``` bash
dnf install @kde-desktop-environment
```

## Switching desktop environments using a graphical user interface (GUI) {#switching-desktop-environments-using-gui}

First, install the desired desktop environment as described in
[Installing additional desktop
environments](&#35;installing-desktop-environments).

You can login to a different desktop for a single session using the
login manager. For example, for the Gnome Display Manager (GDM) that is
used by default on the Fedora Linux Workstation:

1.  On the login screen, select a user from the list.

2.  Click on the Preferences icon right below the password field. A
    window appears with a list of several different desktop
    environments.

3.  Choose one, and enter password as usual.

![Login Screen](switching-desktop-environments-login.png)

### Using switchdesk {#_using_switchdesk}

You also change your desktop environment using the &#96;switchdesk&#96;
tool. It also allows you to change default desktop environment for
individual users, and for all users.

1.  Install the &#96;switchdesk&#96; and &#96;switchdesk-gui&#96;
    packages:

    ``` bash
    dnf install switchdesk switchdesk-gui
    ```

2.  Run the Desktop Switching Tool application.

3.  Select the default desktop from the list of available desktop
    environments, and confirm.

![Desktop Switching Tool](switching-desktop-environments-switchdesk.png)

## Switching desktop environments using the command line interface (CLI) {#switching-desktop-environments-using-cli}

First, install the desired desktop environment as described in
[Installing additional desktop
environments](&#35;installing-desktop-environments).

Install the &#96;switchdesk&#96; package:

``` bash
dnf install switchdesk
```

Pass the selected desktop environment as the only argument to the
&#96;switchdesk&#96; command, for example:

``` bash
switchdesk kde
```

See the &#96;switchdesk(1)&#96; man page for more information.

## Manually changing the default desktop {#_manually_changing_the_default_desktop}

You can also change your default desktop environment using the
&#96;/etc/sysconfig/desktop&#96; system configuration file. If this file
does not exists, please create it. This file specifies the desktop for
new users and the display manager to run when entering runlevel 5.

Please create/edit it using your preferred text editor. Note that you
will need administrator (root) privileges to create or edit this file.

Correct values are:

&#96;DESKTOP=\'*&lt;value&gt;*\'&#96;, where &#96;\_&lt;value&gt;\_&#96;
is one of the following:

1.  &#96;GNOME&#96; - Selects the GNOME desktop environment.

2.  &#96;KDE&#96; - Selects the KDE desktop environment.

&#96;DISPLAYMANAGER=\'*&lt;value&gt;*\'&#96;, where
&#96;\_&lt;value&gt;\_&#96; is one of the following:

1.  &#96;GNOME&#96; - Selects the GNOME Display Manager.

2.  &#96;KDE&#96; - Selects the KDE Display Manager.

3.  &#96;XDM&#96; - Selects the X Display Manager.

# Using the DNF software package manager {#_using_the_dnf_software_package_manager}

Weverton do Couto Timoteo; JetStream ; The Fedora Docs team

> DNF is a software package manager that installs, updates, and removes
> packages on Fedora and is the successor to YUM (Yellow-Dog Updater
> Modified).

DNF makes it easy to maintain packages by automatically checking for
dependencies and determines the actions required to install packages.
This method eliminates the need to manually install or update the
package, and its dependencies, using the &#96;rpm&#96; command. DNF is
now the default software package management tool in Fedora.

## Usage {#sect-usage}

&#96;dnf&#96; can be used exactly as &#96;yum&#96; to search, install or
remove packages.

To search the repositories for a package type:

    \&#35; dnf search packagename

To install the package:

    \&#35; dnf install packagename

To remove a package:

    \&#35; dnf remove packagename

Other common DNF commands include:

&#42; &#96;autoremove&#96; - removes packages installed as dependencies
that are no longer required by currently installed programs.

&#42; &#96;check-update&#96; - checks for updates, but does not download
or install the packages.

&#42; &#96;downgrade&#96; - reverts to the previous version of a
package.

&#42; &#96;info&#96; - provides basic information about the package
including name, version, release, and description.

&#42; &#96;reinstall&#96; - reinstalls the currently installed package.

&#42; &#96;upgrade&#96; - checks the repositories for newer packages and
updates them.

&#42; &#96;exclude&#96; - exclude a package from the transaction.

For more DNF commands refer to the man pages by typing &#96;man dnf&#96;
at the command-line, or [DNF Read The
Docs](https://dnf.readthedocs.io/en/latest/command_ref.html)

## Automatic Updates {#sect-automatic-updates}

The &#96;dnf-automatic&#96; package is a component that allows automatic
download and installation of updates. It can automatically monitor and
report, via e-mail, the availability of updates or send a log about
downloaded packages and installed updates.

For more information, refer to the [Read the Docs:
DNF-Automatic](https://dnf.readthedocs.org/en/latest/automatic.html)
page.

## System Upgrades {#sect-system-upgrades}

The Fedora system can be upgraded directly with DNF, or with the DNF
system upgrade plugin. Refer to the [DNF System
Upgrade](dnf-system-upgrade.xml) document for more details.

## Language Support Using DNF {#sect-language-support-using-dnf}

DNF can be used to install or remove Language Support. A detailed
description with a list of available languages can be found on [Language
Support Using
Dnf](https://fedoraproject.org/wiki/I18N/Language_Support_Using_Dnf)
page.

## Plugins {#sect-plugins}

The core DNF functionality can be extended with plugins. There are
officially supported [Core DNF
plugins](https://dnf-plugins-core.readthedocs.io) and also third-party
[Extras DNF Plugins](https://dnf-plugins-extras.readthedocs.io). To
install them, run

    \&#35; dnf install dnf-plugins-core-PLUGIN_NAME

or

    \&#35; dnf install dnf-plugins-extras-PLUGIN_NAME

## Excluding Packages From Transactions {#exclude-package}

Sometimes it is useful to ignore specific packages from transactions,
such as updates. One such case, for example, could be when an update
includes a regression or a bug. DNF allows you to exclude a package from
the transaction:

&#42; using the command line

    sudo dnf upgrade --exclude=packagename

&#42; using its configuration files

You can add a line to &#96;/etc/dnf/dnf.conf&#96; to exclude packages:

    excludepkgs=packagename

This can also be added to the specific repository configuration files in
&#96;/etc/yum.repos.d/&#96;.
[Globs](https://en.wikipedia.org/wiki/Glob_(programming)) may be used
here to list multiple packages, and each specification must be separated
by a comma. If you have used this configuration, you can disable it in
individual DNF commands using using the &#96;\--disableexcludes&#96;
command line switch.

If you use a GUI update application which does not allow you to specify
packages to exclude when they run, this method can be used.

### Using the DNF Versionlock plugin {#sect-using-dnf-plugin}

You can also use the DNF &#96;versionlock&#96; plugin to limit the
packages that are included in a transaction. It allows you to list what
versions of particular packages should be considered in a transaction.
All other versions of the specified packages will be ignored. The plugin
is part of &#96;dnf-plugins-core&#96; package and can be installed using
the command below:

    sudo dnf install 'dnf-command(versionlock)'

To lock the currently installed version of a package, use:

    sudo dnf versionlock add package

To remove the version lock, use:

    sudo dnf versionlock delete package

The &#96;list&#96; command can be used to list all locked packages,
while the &#96;clear&#96; command will delete all locked entries.

## References {#sect-references}

1.  [DNF Command
    Reference](https://dnf.readthedocs.io/en/latest/command_ref.html)

2.  [DNF wiki](https://github.com/rpm-software-management/dnf/wiki)

3.  [DNF
    VersionLock](https://dnf-plugins-core.readthedocs.io/en/latest/versionlock.html)

&#42; Usage and customisation = Adding a user to sudoers Mirek Jahoda;
Ankur Sinha ; The Fedora Docs Team

One of the most common operations that administrators want to accomplish
when managing &#96;sudo&#96; permissions is to grant a new user general
&#96;sudo&#96; access. This is helpful if you want to give an account
full administrative access to the system.

**Giving a user &#96;sudo&#96; privileges**

On Fedora, it is the &#96;wheel&#96; group the user has to be added to,
as this group has full admin privileges. Add a user to the group using
the following command:

    $ sudo usermod -aG wheel username

If adding the user to the group does not work immediately, you may have
to edit the &#96;/etc/sudoers&#96; file to uncomment the line with the
group name:

    $ sudo visudo
    \&#8230;
    %wheel ALL=(ALL) ALL
    \&#8230;

You will need to logout and back in for changes to take effect.

# Changing Hostname {#_changing_hostname}

Peter Lilley; Peter Boy (pboy)

> A new installation of Fedora will assign a default hostname. You may
> wish to set a different name for easier identification of your host(s)
> on a network.

There are three variations of a hostname in a Fedora system:

1.  A &#42;&#42;static&#42;&#42; name is used by default at system
    bootup. This name will typically be short and contain only letters,
    numbers and dashes.

2.  An optional &#42;&#42;pretty&#42;&#42; name can be longer and more
    descriptive, like \'Emily's 2nd dev laptop\'.

3.  A &#42;&#42;transient&#42;&#42; name is assigned by the network. It
    is probably going to be the same as the static name, unless there
    are multiple hosts with the same static name on the local network.
    For example, if there are two hosts both with static name
    \'localhost\', one machine may be assigned a transient name of
    \'localhost-1\'.

## Displaying your current hostname {#_displaying_your_current_hostname}

For Fedora Workstation, using the default GNOME desktop, open the
Settings application and choose About.

![GNOME Settings - About](displaying-current-hostname-1.png)

To see the hostname from the command line, use the command
&#96;hostnamectl&#96; with no options. The example output below shows
the static and transient hostnames. Your output may be slightly
different depending on which hostname types have been set.

&#8230;. Static hostname: localhost.localdomain Transient hostname:
fedora Icon name: computer-laptop Chassis: laptop Machine ID:
15fc9e69d007013025f31bc5272c4ed1 Boot ID:
41ac938872bae052294bcb277241ac93 Operating System: Fedora 33
(Workstation Edition) CPE OS Name: cpe:/o:fedoraproject:fedora:33
Kernel: Linux 5.10.10-200.fc33.x86_64 Architecture: x86-64 &#8230;.

To see the current static, transient or pretty hostname, you can use the
&#96;hostnamectl&#96; command with options, such as:

&#8230;. hostnamectl \--static hostnamectl \--transient hostnamectl
\--pretty &#8230;.

## Changing the hostname {#_changing_the_hostname}

For Fedora Workstation, using the default GNOME desktop, open the
Settings application and choose About.

![GNOME Settings - About](changing-hostname-1.png)

You can replace the value in the Device name field with the name of your
choosing. The effect of this field is as follows:

&#42; If you use a name that is shorter, contains only lowercase
letters, numbers and/or dashes (\'-\'), this will set the host's static
name, and the pretty name will be left blank. &#42; If you enter a name
that is more descriptive, contains mixed-case and other types of
characters, this will set the pretty name, and a static name will be
derived from that automatically.

You can see the effect of the change by using the &#96;hostnamectl&#96;
command again:

&#8230;. Static hostname: emilys-2nd-dev-laptop Pretty hostname: Emily's
2nd dev laptop Icon name: computer-laptop Chassis: laptop Machine ID:
15fc9e69d007013025f31bc5272c4ed1 Boot ID:
41ac938872bae052294bcb277241ac93 Operating System: Fedora 33
(Workstation Edition) CPE OS Name: cpe:/o:fedoraproject:fedora:33
Kernel: Linux 5.10.10-200.fc33.x86_64 Architecture: x86-64 &#8230;.

In the previous example, \'Emily's 2nd dev laptop\' was entered via the
Settings app, and the static hostname \'emilys-2nd-dev-laptop\' was set
automatically.

Hostnames can also be set at the command line with the &#96;hostnamectl
set-hostname&#96; command. For example:

&#8230;. sudo hostnamectl set-hostname \--pretty \'Emily's 2nd dev
laptop\' sudo hostnamectl set-hostname \--static emily-dev-2 &#8230;.

# Checking Integrity With &#42;AIDE&#42; {#_checking_integrity_with_42aide42}

Héctor Louzao; The Fedora Documentation Team :page-aliases:
using-aide.adoc

> Advanced Intrusion Detection Environment (AIDE) is a utility that
> creates a database of files on the system, and then uses that database
> to ensure file integrity and detect system intrusions.

## Installing &#42;AIDE&#42; {#_installing_42aide42}

1.  To install the *aide* package:

    ``` shell
    $ sudo dnf install aide
    ```

2.  To generate an initial database:

    ``` shell
    $ sudo aide --init
    Start timestamp: 2018-07-11 12:35:47 +0200 (AIDE 0.16)
    AIDE initialized database at /var/lib/aide/aide.db.new.gz

    Number of entries:  150666

    ---------------------------------------------------
    The attributes of the (uncompressed) database(s):
    ---------------------------------------------------

    /var/lib/aide/aide.db.new.gz
    MD5      : 0isjEPsCORFk7laoGGz8tQ==
    SHA1     : j0aPLakWChM+TAuxfVIpy9nqBOE=
    RMD160   : nYyyx0AGZj4e5rwcz77afasXFrw=
    TIGER    : IBVo5A2A4En1kM6zDjD/MnlkN4QWeSOw
    SHA256   : YveypaI9c5PJNvPSZf8YFfjCMWfGUA8q
    vyqLpLJWY0E=
    SHA512   : TiUYmHYflS3A+j17qw5mW78Fn2yXLpCF
    1LE1/RhiqqtMn1MjkKDrr+3TE+/vWfa4
    7253cDhNmC6hoFndkS67Xw==


    End timestamp: 2018-07-11 12:37:35 +0200 (run time: 1m 48s)
    ```

:::: note
::: title
:::

In the default configuration, the &#42;aide \--init&#42; command checks
just a set of directories and files defined in the
&#96;/etc/aide.conf&#96; file. To include additional directories or
files in the AIDE database, and to change their watched parameters, edit
&#96;/etc/aide.conf&#96; accordingly.
::::

1.  To start using the database, remove the &#96;.new&#96; substring
    from the initial database file name:

    ``` shell
    $ sudo mv /var/lib/aide/aide.db.new.gz /var/lib/aide/aide.db.gz
    ```

2.  To change the location of the &#42;AIDE&#42; database, edit the
    &#96;/etc/aide.conf&#96; file and modify the &#96;DBDIR&#96; value.
    For additional security, store the database, configuration, and the
    &#96;/usr/sbin/aide&#96; binary file in a secure location such as a
    read-only media.

    :::: important
    ::: title
    :::

    To avoid SELinux denials after the AIDE database location change,
    update your SELinux policy accordingly. See the [Changing SELinux
    states and modes](changing-selinux-states-and-modes.xml) guide for
    more information.
    ::::

## Performing Integrity Checks {#_performing_integrity_checks}

To initiate a manual check:

``` shell
$ sudo aide --check
Start timestamp: 2018-07-11 12:41:20 +0200 (AIDE 0.16)
AIDE found differences between database and filesystem!!

Summary:
Total number of entries:    150667
Added entries:      1
Removed entries:        0
Changed entries:        2

---------------------------------------------------
Added entries:
---------------------------------------------------

f++++++++++++++++: /etc/cups/subscriptions.conf.O
\…
[output_truncated]
```

At a minimum, &#42;AIDE&#42; should be configured to run a weekly scan.
At most, &#42;AIDE&#42; should be run daily. For example, to schedule a
daily execution of AIDE at *04:05* a.m. use the &#42;cron&#42; command.

Add the following line to the &#96;/etc/crontab&#96; file:

``` shell
05 4 \* \* \* root /usr/sbin/aide --check
```

## Updating an &#42;AIDE&#42; Database {#_updating_an_42aide42_database}

After verifying the changes of your system such as, package updates or
configuration files adjustments, update your baseline &#42;AIDE&#42;
database:

``` shell
$ sudo aide --update
```

The &#42;aide \--update&#42; command creates the
&#96;/var/lib/aide/aide.db.new.gz&#96; database file. To start using it
for integrity checks, remove the &#96;.new&#96; substring from the file
name.

## Additional Resources {#_additional_resources_7}

For additional information on &#42;AIDE&#42;, see the following
documentation:

- [Guide to the Secure Configuration of Fedora (OpenSCAP Security
  Guide)](https://static.open-scap.org/ssg-guides/ssg-fedora-guide-index.html)

- [The AIDE manual](https://aide.github.io/doc/)

# Configuring IP networking with nmcli {#_configuring_ip_networking_with_nmcli}

Richard Gregory; Peter Boy (pboy)

> How to configure networking using the \[application\]&#42;nmcli&#42;
> (NetworkManager Command Line Interface) command-line utility.

## Getting started with nmcli {#_getting_started_with_nmcli}

The \[application\]&#42;nmcli&#42; (NetworkManager Command Line
Interface) command-line utility is used for controlling NetworkManager
and reporting network status. It can be utilized as a replacement for
\[application\]&#42;nm-applet&#42; or other graphical clients.
\[application\]&#42;nmcli&#42; is used to create, display, edit, delete,
activate, and deactivate network connections, as well as control and
display network device status.

The \[application\]&#42;nmcli&#42; utility can be used by both users and
scripts for controlling \[application\]&#42;NetworkManager&#42;:

&#42; For servers, headless machines, and terminals,
\[application\]&#42;nmcli&#42; can be used to control
\[application\]&#42;NetworkManager&#42; directly, without GUI, including
creating, editing, starting and stopping network connections and viewing
network status.

&#42; For scripts, \[application\]&#42;nmcli&#42; supports a terse
output format which is better suited for script processing. It is a way
to integrate network configuration instead of managing network
connections manually.

The basic format of a \[application\]&#42;nmcli&#42; command is as
follows:

    \&#8230;.
    nmcli [OPTIONS] OBJECT { COMMAND | help }
    \&#8230;.

where OBJECT can be one of the following options: &#96;general&#96;,
&#96;networking&#96;, &#96;radio&#96;, &#96;connection&#96;,
&#96;device&#96;, &#96;agent&#96;, and &#96;monitor&#96;. You can use
any prefix of these options in your commands. For example,
\[command\]&#96;nmcli con help&#96;, \[command\]&#96;nmcli c help&#96;,
\[command\]&#96;nmcli connection help&#96; generate the same output.

Some of useful optional OPTIONS to get started are:

-t, terse

:   This mode can be used for computer script processing as you can see
    a terse output displaying only the values.

    :::: {#ex-Viewing_a_terse_output_for_scripts .example}
    ::: title
    Viewing a terse output
    :::

        \&#8230;.
        ~]$ [command]\&#96;nmcli -t device\&#96;
        ens3:ethernet:connected:Profile 1
        lo:loopback:unmanaged:
        \&#8230;.
    ::::

-f, field

:   This option specifies what fields can be displayed in output. For
    example, NAME,UUID,TYPE,AUTOCONNECT,ACTIVE,DEVICE,STATE. You can use
    one or more fields. If you want to use more, do not use space after
    comma to separate the fields.

    :::: {#ex-Specifying_Fields_in_the_output .example}
    ::: title
    Specifying Fields in the output
    :::

        \&#8230;.
        ~]$ [command]\&#96;nmcli -f DEVICE,TYPE device\&#96;
        DEVICE  TYPE
        ens3    ethernet
        lo      loopback
        \&#8230;.

    or even better for scripting:

        \&#8230;.
        ~]$ [command]\&#96;nmcli -t -f DEVICE,TYPE device\&#96;
        ens3:ethernet
        lo:loopback

    &#8230;.
    ::::

-p, pretty

:   This option causes \[application\]&#42;nmcli&#42; to produce
    human-readable output. For example, values are aligned and headers
    are printed.

    :::: {#ex-Viewing_an_output_in_pretty_Mode .example}
    ::: title
    Viewing an output in pretty mode
    :::

        \&#8230;.
        ~]$ [command]\&#96;nmcli -p device\&#96;
        =====================
        Status of devices
        =====================
        DEVICE  TYPE      STATE      CONNECTION
        --------------------------------------------------------------
        ens3    ethernet  connected  Profile 1
        lo      loopback  unmanaged  --

    &#8230;.
    ::::

-h, help

:   Prints help information.

The \[application\]&#42;nmcli&#42; tool has some built-in
context-sensitive help. To list the available options and object names:

    \&#8230;.
    ~]$ [command]\&#96;nmcli help\&#96;
    \&#8230;.

To list available actions related to a specified object:

    \&#8230;.
    ~]$ [command]\&#96;nmcli object help\&#96;
    \&#8230;.

For example,

    \&#8230;.
    ~]$ [command]\&#96;nmcli c help\&#96;
    \&#8230;.

**Additional resources**

&#42; [Getting Started With
NetworkManager](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/networking_guide/getting_started_with_networkmanager)

## Brief Selection of nmcli Examples {#_brief_selection_of_nmcli_examples}

This section provides a brief selection of
\[application\]&#42;nmcli&#42; examples.

**Prerequisites**

&lt;&lt;Getting-started-with-nmcli&gt;&gt;

:::: example
::: title
Checking the overall status of NetworkManager
:::

    \&#8230;.
    ~]$ [command]\&#96;nmcli general status\&#96;
    STATE      CONNECTIVITY  WIFI-HW  WIFI     WWAN-HW  WWAN
    connected  full          enabled  enabled  enabled  enabled
    \&#8230;.

In terse mode:

    \&#8230;.
    ~]$ [command]\&#96;nmcli -t -f STATE general\&#96;
    connected
    \&#8230;.
::::

:::: example
::: title
Viewing NetworkManager logging status
:::

    \&#8230;.
    ~]$ [command]\&#96;nmcli general logging\&#96;
    LEVEL  DOMAINS
    INFO   PLATFORM,RFKILL,ETHER,WIFI,BT,MB,DHCP4,DHCP6,PPP,WIFI_SCAN,IP4,IP6,A
    UTOIP4,DNS,VPN,SHARING,SUPPLICANT,AGENTS,SETTINGS,SUSPEND,CORE,DEVICE,OLPC,
    WIMAX,INFINIBAND,FIREWALL,ADSL,BOND,VLAN,BRIDGE,DBUS_PROPS,TEAM,CONCHECK,DC
    B,DISPATCH
    \&#8230;.
::::

:::: example
::: title
Viewing all connections
:::

    \&#8230;.
    ~]$ [command]\&#96;nmcli connection show\&#96;
    NAME       UUID                                  TYPE      DEVICE
    Profile 1  db1060e9-c164-476f-b2b5-caec62dc1b05  ethernet    ens3
    ens3       aaf6eb56-73e5-4746-9037-eed42caa8a65  ethernet    --
    \&#8230;.
::::

:::: example
::: title
Viewing only currently active connections
:::

    \&#8230;.
    ~]$ [command]\&#96;nmcli connection show --active\&#96;
    NAME       UUID                                  TYPE      DEVICE
    Profile 1  db1060e9-c164-476f-b2b5-caec62dc1b05  ethernet     ens3
    \&#8230;.
::::

:::: example
::: title
Viewing only devices recognized by
\[application\]&#42;NetworkManager&#42; and their state
:::

    \&#8230;.
    ~]$ [command]\&#96;nmcli device status\&#96;
    DEVICE  TYPE      STATE      CONNECTION
    ens3    ethernet  connected  Profile 1
    lo      loopback  unmanaged  --
    \&#8230;.
::::

You can also use the following abbreviations of the
\[application\]&#42;nmcli&#42; commands:

+-----------------------------------+-----------------------------------+
| nmcli command                     | abbreviation                      |
+===================================+===================================+
| nmcli general status              | nmcli g                           |
+-----------------------------------+-----------------------------------+
| nmcli general logging             | nmcli g log                       |
+-----------------------------------+-----------------------------------+
| nmcli connection show             | nmcli con show                    |
+-----------------------------------+-----------------------------------+
| nmcli connection show \--active   | nmcli con show -a                 |
+-----------------------------------+-----------------------------------+
| nmcli device status               | nmcli dev                         |
+-----------------------------------+-----------------------------------+

: Abbreviations of some nmcli commands {#table-nmcli_examples}

**Additional resources**

&#42; For more examples, see the
*[&#42;nmcli-examples&#42;(5)]{.citetitle}* man page.

## The nmcli options {#_the_nmcli_options}

Following are some of the important \[application\]&#42;nmcli&#42;
property options:

\[option\]&#96;connection.type&#96;

:   A connection type. Allowed values are: adsl, bond, bond-slave,
    bridge, bridge-slave, bluetooth, cdma, ethernet, gsm, infiniband,
    olpc-mesh, team, team-slave, vlan, wifi, wimax. Each connection type
    has type-specific command options. For example:

    &#42;&#42; A &#96;gsm&#96; connection requires the access point name
    specified in an \[option\]&#96;apn&#96;.

        \&#8230;.
        nmcli c add connection.type gsm apn access_point_name
        \&#8230;.

    &#42;&#42; A &#96;wifi&#96; device requires the service set
    identifier specified in a \[option\]&#96;ssid&#96;.

        \&#8230;.
        nmcli c add connection.type wifi ssid
        My identifier
        \&#8230;.

You can see the &#96;TYPE_SPECIFIC_OPTIONS&#96; list in the
*[&#42;nmcli&#42;(1)]{.citetitle}* man page.

\[option\]&#96;connection.interface-name&#96;

:   A device name relevant for the connection.

        \&#8230;.
        nmcli con add connection.interface-name eth0 type ethernet
        \&#8230;.

\[option\]&#96;connection.id&#96;

:   A name used for the connection profile. If you do not specify a
    connection name, one will be generated as follows:

        \&#8230;.
        connection.type -connection.interface-name
        \&#8230;.

    The \[option\]&#96;connection.id&#96; is the name of a *connection
    profile* and should not be confused with the interface name which
    denotes a device (&#96;wlan0&#96;, &#96;ens3&#96;, &#96;em1&#96;).
    However, users can name the connections after interfaces, but they
    are not the same thing. There can be multiple connection profiles
    available for a device. This is particularly useful for mobile
    devices or when switching a network cable back and forth between
    different devices. Rather than edit the configuration, create
    different profiles and apply them to the interface as needed. The
    \[option\]&#96;id&#96; option also refers to the connection profile
    name.

The most important options for \[application\]&#42;nmcli&#42; commands
such as &#96;show&#96;, &#96;up&#96;, &#96;down&#96; are:

\[option\]&#96;id&#96;

:   An identification string assigned by the user to a connection
    profile. Id can be used in nmcli connection commands to identify a
    connection. The NAME field in the command output always denotes the
    connection id. It refers to the same connection profile name that
    the con-name does.

\[option\]&#96;uuid&#96;

:   A unique identification string assigned by the system to a
    connection profile. The &#96;uuid&#96; can be used in
    \[command\]&#96;nmcli connection&#96; commands to identify a
    connection.

**Additional resources**

&#42; See the comprehensive list in the
*[&#42;nmcli&#42;(1)]{.citetitle}* man page.

# Configuring X Window System using the xorg.conf file {#_configuring_x_window_system_using_the_xorg_conf_file}

Peter Lilley

## About xorg.conf {#_about_xorg_conf}

Traditionally, the xorg.conf file is used to configure an Xorg display
server. In Fedora (where an Xorg display server is configured instead of
the default Wayland) the X configuration is determined automatically
each time X is started. As a result, no xorg.conf file is created. In
most cases, this works well and there is no need to manually specify X
configuration.

If you need to make manual changes to your X configuration for any
reason, you will first need to create an &#96;xorg.conf&#96; file.

## Creating an xorg.conf file {#creating-an-xorg-conf-file}

You can create a basic file using the &#96;X&#96; executable. It will
contain sections and entries that you can edit to suit your needs. To
create the file, enter this command as &#42;root&#42;:

    \&#35; Xorg :1 -configure

Next, copy the file to the correct location:

    \&#35; cp /root/xorg.conf.new /etc/X11/xorg.conf

Now you may edit the file according to your needs.

See the &#96;xorg.conf(5)&#96; man page for more information.

**Additional Resources**

1.  [Configuring Xorg as the default GNOME
    session](configuring-xorg-as-default-gnome-session.xml)

# Configuring Xorg as the default GNOME session {#_configuring_xorg_as_the_default_gnome_session}

Peter Lilley

> Wayland is the default GNOME display server, and has been the default
> in Fedora since Fedora 25. However, users may still need to use the
> older Xorg display server for compatibility reasons.

To confirm the current windowing system in use, go to &#42;Settings&#42;
and select &#42;About&#42;.

![Settings - About](configuring-xorg-as-default-gnome-session_1.png)

## Configuring GNOME to use Xorg {#proc-configuring-xorg-as-default-gnome-session}

At the login screen, select the \'gear\' icon and select &#42;GNOME on
Xorg&#42;.

![Login screen - select GNOME on
Xorg](configuring-xorg-as-default-gnome-session_2.png)

Once login is completed the X11 windowing system will be in use, as can
be seen by returning to &#42;Settings&#42; &gt; &#42;About&#42;. This
change will persist unless changed back at the login screen.

![Settings - About](configuring-xorg-as-default-gnome-session_3.png)

**Changing the default GNOME session via configuration file**

As an alternative, this change can be made by editing a configuration
file &#96;/etc/gdm/custom.conf&#96;.

1.  Open &#96;/etc/gdm/custom.conf&#96; and uncomment the line:

WaylandEnable=false

1.  Add the following line to the &#96;\[daemon\]&#96; section:

DefaultSession=gnome-xorg.desktop

1.  Save the &#96;custom.conf&#96; file.

2.  Logout or reboot to enter the new session.

:::: note
::: title
:::

With the above changes applied, the option to set the GNOME session to
use Wayland will actually be removed from the \'gear icon\' menu on the
login screen.
::::

**Additional Resources**

1.  [Wayland Display Server in the System Administrator's
    Guide](f43@fedora:system-administrators-guide:Wayland.xml)

2.  [Wayland @ freedesktop.org](https://wayland.freedesktop.org/)

# Control of System Accessibility by firewalld {#_control_of_system_accessibility_by_firewalld}

Richard Gregory; Petr Bokoc (pbokoc); Peter Boy (pboy) :experimental:

> A *firewall* is a way to protect machines from any unwanted access
> from outside. In Fedora, it is installed by default during the
> installation of the operating system, enabled and configured to
> provide secure operation even without any additional action by the
> administrator. It blocks any access other than ssh by default.

## How it works {#_how_it_works}

A firewall enables users to control incoming network traffic on host
machines by defining a set of *firewall rules*. These rules are used to
sort the incoming traffic and either block it or allow through.

&#96;firewalld&#96; is a firewall service daemon that provides a dynamic
customizable host-based firewall with a &#96;D-Bus&#96; interface. Being
dynamic, it enables creating, changing, and deleting the rules without
the necessity to restart the firewall daemon each time the rules are
changed.

&#96;firewalld&#96; uses the concepts of *zones* and *services*, that
simplify the traffic management.

&#96;\_Zones\_&#96; are predefined sets of rules. Network interfaces and
sources can be assigned to a zone. The traffic allowed depends on the
network your computer is connected to and the security level this
network is assigned. Firewall services are predefined rules that cover
all necessary settings to allow incoming traffic for a specific service
and they apply within a zone.

&#96;\_Services\_&#96; use one or more ports or addresses for network
communication. Firewalls filter communication based on ports. To allow
network traffic for a service, its ports must be open.
&#96;firewalld&#96; blocks all traffic on ports that are not explicitly
set as open. Some zones, such as trusted, allow all traffic by default.

:::: formalpara
::: title
Additional resources
:::

For more information about using firewalld and configuring zones and
services, see [firewalld
documentation](https://firewalld.org/documentation/) or [Fedora
wiki:firewalld](https://fedoraproject.org/wiki/Firewalld)
::::

## Setting up firewalld {#_setting_up_firewalld}

All Fedora Editions install, configure and activate the firewall by
default. No further action is required. The only exception is *Cloud
Edition*, which relies on the higher level cloud system.

Some third party variations and redistributions may differ. In this
case, it is up to the administrator to install and activate the firewall
afterwards.

You check if firewalld is set up in a terminal by issuing

``` bash
systemctl status firewalld
```

You should get soemething like

    ● firewalld.service - firewalld - dynamic firewall daemon
    Loaded: loaded (/usr/lib/systemd/system/firewalld.service; enabled; preset\&gt;
    Drop-In: /usr/lib/systemd/system/service.d
    └─10-timeout-abort.conf
    Active: active (running) since Sat 2023-08-19 19:05:18 CEST; 3 days ago
    \&#8230;

### Installing and activating firewalld {#_installing_and_activating_firewalld}

In case you get by the command above something like

    Unit firewalld.service could not be found.

you have to install it. Run on the command line:

``` bash
$ sudo dnf install firewalld
$ sudo systemctl unmask firewalld
$ sudo systemctl start firewalld
$ sudo systemctl enable firewalld
```

This sequence installs, starts and ensures an automatic restart after a
system boot.

### Adjusting firewalld operations during system maintenance {#_adjusting_firewalld_operations_during_system_maintenance}

Sometimes a system administrator has to stop or restart firewalld during
system maintenance tasks.

:::: formalpara
::: title
Stop firewalld
:::

``` bash
$ sudo systemctl stop firewalld
```
::::

:::: formalpara
::: title
Prevent autostart at system boot
:::

``` bash
$ sudo systemctl disable firewalld
```
::::

:::: formalpara
::: title
Start firewalld
:::

``` bash
$ sudo systemctl start firewalld
```
::::

:::: formalpara
::: title
Activate autostart at system boot
:::

``` bash
$ sudo systemctl enable firewalld
```
::::

:::: formalpara
::: title
Disconnecting the firewall from the d-bus controller
:::

    $ sudo systemctl mask firewalld
::::

:::: formalpara
::: title
(Re.)Connect the firewall to the d-bus controller
:::

    $ sudo systemctl unmask firewalld
::::

### Installing the \[application\]&#42;firewall-config&#42; GUI configuration tool {#_installing_the_application42firewall_config42_gui_configuration_tool}

To use the \[application\]&#42;firewall-config&#42; GUI configuration
tool, install the \[package\]&#42;firewall-config&#42; package as
&#96;root&#96;:

``` bash
$ sudo dnf install firewall-config
```

Alternatively, in \[application\]&#42;GNOME&#42;, use the Super key and
type &#96;Software&#96; to launch the \[application\]&#42;Software
Sources&#42; application. Type &#96;firewall&#96; to the search box,
which appears after selecting the search button in the top-right corner.
Select the &#96;Firewall&#96; item from the search results, and click on
the Install button.

To run \[application\]&#42;firewall-config&#42;, use either the
\[command\]&#96;firewall-config&#96; command or press the Super key to
enter the &#96;Activities Overview&#96;, type &#96;firewall&#96;, and
press Enter.

## Managing firewalld {#_managing_firewalld}

### Viewing the current status of &#96;firewalld&#96; {#_viewing_the_current_status_of_96firewalld96}

The firewall service, &#96;firewalld&#96;, is installed on the system by
default. Use the &#96;firewalld&#96; CLI interface to check that the
service is running.

``` bash
$ sudo firewall-cmd --state
```

For more information about the service status, use the
\[command\]&#96;systemctl&#96; command

``` bash
$ sudo systemctl status firewalld
firewalld.service - firewalld - dynamic firewall daemon
Loaded: loaded (/usr/lib/systemd/system/firewalld.service; enabled; vendor pr
Active: active (running) since Mon 2017-12-18 16:05:15 CET; 50min ago
Docs: man:firewalld(1)
Main PID: 705 (firewalld)
Tasks: 2 (limit: 4915)
CGroup: /system.slice/firewalld.service
└─705 /usr/bin/python3 -Es /usr/sbin/firewalld --nofork --nopid
```

Furthermore, it is important to know how &#96;firewalld&#96; is set up
and which rules are in force before you try to edit the settings. To
display the firewall settings, see
&lt;&lt;sec-Viewing_Current_firewalld_Settings&gt;&gt;

### Viewing current firewalld settings {#sec-Viewing_Current_firewalld_Settings}

#### Viewing allowed services using GUI {#sec-Viewing_Allowed_Services_Using_GUI}

To view the list of services using the graphical
\[application\]&#42;firewall-config&#42; tool, press the Super key to
enter the Activities Overview, type \[command\]&#96;firewall&#96;, and
press Enter. The \[application\]&#42;firewall-config&#42; tool appears.
You can now view the list of services under the &#96;Services&#96; tab.

Alternatively, to start the graphical firewall configuration tool using
the command-line, enter the following command:

    $ firewall-config

The &#96;Firewall Configuration&#96; window opens. Note that this
command can be run as a normal user, but you are prompted for an
administrator password occasionally.

#### Viewing firewalld settings using CLI {#sec-Viewing_firewalld_Settings_Using_CLI}

With the CLI client, it is possible to get different views of the
current firewall settings. The \[option\]&#96;\--list-all&#96; option
shows a complete overview of the &#96;firewalld&#96; settings.

&#96;firewalld&#96; uses zones to manage the traffic. If a zone is not
specified by the \[option\]&#96;\--zone&#96; option, the command is
effective in the default zone assigned to the active network interface
and connection.

To list all the relevant information for the default zone:

    $ firewall-cmd --list-all
    public
    target: default
    icmp-block-inversion: no
    interfaces:
    sources:
    services: ssh dhcpv6-client
    ports:
    protocols:
    masquerade: no
    forward-ports:
    source-ports:
    icmp-blocks:
    rich rules:

:::: note
::: title
:::

To specify the zone for which to display the settings, add the
\[option\]&#96;\--zone=*zone-name*&#96; argument to the
\[command\]&#96;firewall-cmd \--list-all&#96; command, for example:

    ~]\&#35; firewall-cmd --list-all --zone=home
    home
    target: default
    icmp-block-inversion: no
    interfaces:
    sources:
    services: ssh mdns samba-client dhcpv6-client
    \&#8230; [output truncated]
::::

To see the settings for particular information, such as services or
ports, use a specific option. See the &#96;firewalld&#96; manual pages
or get a list of the options using the command help:

    $ firewall-cmd --help

    Usage: firewall-cmd [OPTIONS\&#8230;]

    General Options
    -h, --help           Prints a short help text and exists
    -V, --version        Print the version string of firewalld
    -q, --quiet          Do not print status messages

    Status Options
    --state              Return and print firewalld state
    --reload             Reload firewall and keep state information
    \&#8230; [output truncated]

For example, to see which services are allowed in the current zone:

    $ firewall-cmd --list-services
    samba-client ssh dhcpv6-client

Listing the settings for a certain subpart using the CLI tool can
sometimes be difficult to interpret. For example, you allow the
&#96;SSH&#96; service and &#96;firewalld&#96; opens the necessary port
(22) for the service. Later, if you list the allowed services, the list
shows the &#96;SSH&#96; service, but if you list open ports, it does not
show any. Therefore, it is recommended to use the
\[option\]&#96;\--list-all&#96; option to make sure you receive a
complete information.

### Runtime and permanent settings {#_runtime_and_permanent_settings}

Any changes made while firewalld is running will be lost when firewalld
is restarted. When firewalld is restarted, the settings revert to their
permanent values.

These changes are said to be made in *runtime mode*.

To make the changes persistent across reboots, apply them again using
the &#96;\--permanent&#96; option. Alternatively, to make changes
persistent while firewalld is running, use the
&#96;\--runtime-to-permanent *firewall-cmd*&#96; option.

If you make changes while firewalld is running using only the
&#96;\--permanent&#96; option, they do not become effective until
firewalld is restarted. However, restarting firewalld briefly stops the
networking traffic, causing disruption to your system.

#### Changing settings in runtime and permanent configuration using CLI {#_changing_settings_in_runtime_and_permanent_configuration_using_cli}

Using the CLI, you can only modify either runtime or permanent mode. To
modify the firewall settings in permanent mode, use the
&#96;\--permanent&#96; option with the &#96;firewall-cmd&#96; command.

    $ sudo firewall-cmd --permanent \&lt;other options\&gt;

Without this option, the command modifies runtime mode. To change
settings in both modes, you can use two methods:

&#42; Change runtime settings and then make them permanent as follows:

1.  Change the runtime settings:

    &#96;firewall-cmd &lt;other options&gt;&#96;

2.  Use &#96;\--runtime-to-permanent&#96; to make the changes permanent.

    &#96;firewall-cmd \--runtime-to-permanent&#96;

&#42; Set permanent settings and reload the settings into runtime mode:

1.  Make the changes in permanent mode:

    &#96;firewall-cmd \--permanent &lt;other options&gt;&#96;

2.  Reload the settings:

    &#96;firewall-cmd \--reload&#96;

The first method allows you to test the settings before you apply them
to permanent mode.

:::: note
::: title
:::

It is possible that an incorrect setting will result in a user locking
themselves out of a machine. To prevent this, use the
&#96;\--timeout&#96; option. Using this option means that after a
specified amount of time, any change reverts to its previous state. You
can not use the &#96;\--permanent&#96; option with the
&#96;\--timeout&#96; option.

For example, to add the SSH service for 15 minutes use this command:

    $ sudo firewall-cmd --add-service=ssh --timeout 15m

The SSH service will be available until access is removed after 15
minutes.
::::

### Controlling ports using firewalld {#_controlling_ports_using_firewalld}

#### What are ports? {#_what_are_ports}

Ports are logical devices that enable an operating system to receive and
distinguish network traffic and forward it accordingly to system
services. These are usually represented by a daemon that listens on the
port, that is it waits for any traffic coming to this port.

Normally, system services listen on standard ports that are reserved for
them. The httpd daemon, for example, listens on port 80. However, system
administrators may configure daemons to listen on different ports to
enhance security.

#### Opening a port {#_opening_a_port}

Through open ports, the system is accessible from the outside, which
represents a security risk. Generally, keep ports closed and only open
them if they are required for certain services.

<div>

::: title
Opening a port using the command line
:::

1.  Get a list of allowed ports in the current zone:

        $ firewall-cmd --list-ports

2.  Add a port to the allowed ports to open it for incoming traffic:

        $ sudo firewall-cmd --add-port=port-number/port-type

3.  Make the new settings persistent:

        $ sudo firewall-cmd --runtime-to-permanent

</div>

The port types are either tcp, udp, sctp, or dccp. The type must match
the type of network communication.

#### Closing a port {#_closing_a_port}

When an open port is no longer needed, close that port in firewalld. It
is highly recommended to close all unnecessary ports as soon as they are
not used because leaving a port open represents a security risk.

:::: formalpara
::: title
Closing a port using the command line
:::

To close a port, remove it from the list of allowed ports:
::::

1.  List all allowed ports:

        $ firewall-cmd --list-ports

    :::: warning
    ::: title
    :::

    This command will only give you a list of ports that have been
    opened as ports. You will not be able to see any open ports that
    have been opened as a service. Therefore, you should consider using
    the \--list-all option instead of \--list-ports.
    ::::

2.  Remove the port from the allowed ports to close it for the incoming
    traffic:

        $ sudo firewall-cmd --remove-port=port-number/port-type

3.  Make the new settings persistent:

        $ sudo firewall-cmd --runtime-to-permanent

# Creating a Disk Partition in Linux {#_creating_a_disk_partition_in_linux}

Connor Lim ;

Creating and deleting partitions in Linux is a regular practice because
storage devices (such as hard drives and USB drives) must be structured
in some way before they can be used. In most cases, large storage
devices are divided into separate sections called partitions.
Partitioning also allows you to divide your hard drive into isolated
sections, where each section behaves as its own hard drive. Partitioning
is particularly useful if you run multiple operating systems.

## Creating a Disk Partition in Linux {#_creating_a_disk_partition_in_linux_2}

This procedure describes how to partition a storage disk in Linux using
the &#96;parted&#96; command.

### Procedure {#_procedure_9}

1.  List the partitions using the &#96;parted -l&#96; command to
    identify the storage device you want to partition. Typically, the
    first hard disk (&#96;/dev/sda&#96; or &#96;/dev/vda&#96;) will
    contain the operating system, so look for another disk to find the
    one you want. For example:

        sudo parted -l
        Model: ATA RevuAhn_850X1TU5 (scsi)
        Disk /dev/vdc: 512GB
        Sector size (logical/physical): 512B/512B
        Partition Table: msdos
        Disk Flags:

        Number  Start   End    Size   Type     File system  Flags
        1      1049kB  525MB  524MB  primary  ext4         boot
        2      525MB   512GB  512GB  primary               lvm

2.  Open the storage device. Use the &#96;parted&#96; command to begin
    working with the selected storage device. For example:

        sudo parted /dev/vdc
        GNU Parted 3.3
        Using /dev/vdc
        Welcome to GNU Parted! Type 'help' to view a list of commands.
        (parted)

    :::: important
    ::: title
    :::

    Be sure to indicate the specific device you want to partition. If
    you just enter &#96;parted&#96; without a device name, it will
    randomly select a storage device to modify.
    ::::

3.  Set the partition table type to &#96;gpt&#96;, then enter
    &#96;Yes&#96; to accept it.

        (parted) mklabel gpt
        Warning: the existing disk label on /dev/vdc will be destroyed
        and all data on this disk will be lost. Do you want to continue?
        Yes/No? Yes

    :::: note
    ::: title
    :::

    The &#96;mklabel&#96; and &#96;mktable&#96; commands are both used
    for making a partition table on a storage device. At the time of
    writing, the supported partition tables are: &#96;aix&#96;,
    &#96;amiga&#96;, &#96;bsd&#96;, &#96;dvh&#96;, &#96;gpt&#96;,
    &#96;mac&#96;, &#96;ms-dos&#96;, &#96;pc98&#96;, &#96;sun&#96;,
    &#96;atari&#96;, and &#96;loop&#96;. Use &#96;help mklabel&#96; to
    get a list of supported partition tables. Remember &#96;mklabel&#96;
    will not make a partition, rather it will make a partition table.
    ::::

4.  Review the partition table of the storage device.

        (parted) print
        Model: Virtio Block Device (virtblk)
        Disk /dev/vdc: 1396MB
        Sector size (logical/physical): 512B/512B
        Partition Table: gpt
        Disk Flags:
        Number Start End Size File system Name Flags

5.  Create a new partition using the following command. For example,
    1396 MB on partition 0:

        (parted) mkpart primary 0 1396MB

        Warning: The resulting partition is not properly aligned for best performance
        Ignore/Cancel? I

        (parted) print
        Model: Virtio Block Device (virtblk)
        Disk /dev/vdc: 1396MB
        Sector size (logical/physical): 512B/512B
        Partition Table: gpt
        Disk Flags:
        Number  Start   End     Size    File system  Name     Flags
        1      17.4kB  1396MB  1396MB               primary

    :::: note
    ::: title
    :::

    Providing a partition name under GPT is a must; in the above
    example, primary is the name, not the partition type. In a GPT
    partition table, the partition type is used as partition name.
    ::::

6.  Quit using the &#96;quit&#96; command. Changes are automatically
    saved when you quit &#96;parted&#96;.

        (parted) quit
        Information: You may need to update /etc/fstab.

### Help command for creating a new partition {#_help_command_for_creating_a_new_partition}

To get help on how to make a new partition, type: &#96;help mkpart&#96;.

    (parted) help mkpart
    mkpart PART-TYPE [FS-TYPE] START END     make a partition

    PART-TYPE is one of: primary, logical, extended
    FS-TYPE is one of: udf, btrfs, nilfs2, ext4, ext3, ext2, fat32, fat16, hfsx, hfs+, hfs, jfs, swsusp,
    linux-swap(v1), linux-swap(v0), ntfs, reiserfs, hp-ufs, sun-ufs, xfs, apfs2, apfs1, asfs, amufs5,
    amufs4, amufs3, amufs2, amufs1, amufs0, amufs, affs7, affs6, affs5, affs4, affs3, affs2, affs1,
    affs0, linux-swap, linux-swap(new), linux-swap(old)
    START and END are disk locations, such as 4GB or 10%.  Negative values count from the end of the
    disk.  For example, -1s specifies exactly the last sector.

    'mkpart' makes a partition without creating a new file system on the partition.  FS-TYPE may be
    specified to set an appropriate partition ID.

:::: note
::: title
:::

&#42; Setting filesystem type (&#96;FS-TYPE&#96;) will not create an
ext4 filesystem on /dev/vdc1. You still have to create the ext4
filesystem with &#96;mkfs.ext4&#96;. &#42; A DOS partition table's
partition types are primary, logical, and extended. &#42; Providing a
partition name under GPT is a must. In a GPT partition table, the
partition type is used as the partition name.
::::

# GPG Keys Management {#_gpg_keys_management}

Connor Lim ; :experimental:

> This document explains in detail how to obtain a GPG key using common
> Fedora utilities. It also provides information on managing your key as
> a Fedora contributor.

## Creating GPG Keys {#_creating_gpg_keys}

### Creating GPG keys using the GNOME desktop {#_creating_gpg_keys_using_the_gnome_desktop}

Install the Seahorse utility, which makes GPG key management easier.

1.  Select [Activities \> Software]{.menuchoice}.

2.  Click the *Search* button and enter the name \'Seahorse\'.

3.  Click the Seahorse package and click Install to add the software.
    You can also install Seahorse using the command line with the
    command &#96;sudo dnf install seahorse&#96;.

To create a key:

1.  Select [Activities \> Passwords and Encryption Keys]{.menuchoice},
    which starts the application Seahorse.

2.  At the top left hand corner, click the [Plus Button \> GPG
    Key]{.menuchoice}.

3.  Type your full name, email address, and an optional comment
    describing who you are (e.g.: John C. Smith, <jsmith@example.com>,
    The Man).

4.  Click Create.

5.  Choose a passphrase that is strong but also easy to remember in the
    dialog that is displayed.

6.  Click OK and the key is created.

Now see &lt;&lt;backup-gpg-keys-gnome&gt;&gt;.

### Creating GPG Keys Using the KDE Desktop {#_creating_gpg_keys_using_the_kde_desktop}

1.  Start the KGpg program from the main menu by selecting [Applications
    \> Utilities &gt; KGpg]{.menuchoice}. If you have never used KGpg
    before, the program walks you through the process of creating your
    own GPG keypair.

2.  Enter your name, email address, and an optional comment in the
    dialog box that appears prompting you to create a new key pair. You
    can also choose an expiration time for your key, as well as the key
    strength (number of bits) and algorithms.

3.  Enter your passphrase in the next dialog box. At this point, your
    key appears in the main KGpg window.

To find your GPG key ID, look in the *ID* column next to the newly
created key. In most cases, if you are asked for the key ID, you should
prepend &#96;0x&#96; to the last 8 characters of the key ID, as in
&#96;0x6789ABCD&#96;.

Now see &lt;&lt;backup-gpg-keys-kde&gt;&gt;.

### Creating GPG Keys Using the Command Line {#_creating_gpg_keys_using_the_command_line}

1.  Use the following shell command:

        gpg --full-generate-key

    This command generates a key pair that consists of a public and a
    private key. Other people use your public key to authenticate and/or
    decrypt your communications. Distribute your &#42;public&#42; key as
    widely as possible, especially to people who you know will want to
    receive authentic communications from you, such as a mailing list.

2.  Press the Enter key to assign a default value if desired. The first
    prompt asks you to select what kind of key you prefer:

        Please select what kind of key you want:
        (1) RSA and RSA (default)
        (2) DSA and Elgamal
        (3) DSA (sign only)
        (4) RSA (sign only)
        (14) Existing key from card
        Your selection?

    In almost all cases, the default is the correct choice. A RSA/RSA
    key allows you not only to sign communications, but also to encrypt
    files.

3.  Choose the key size:

        RSA keys may be between 1024 and 4096 bits long.
        What keysize do you want? (3072)

    Again, the default is sufficient for almost all users, and
    represents an *extremely* strong level of security.

4.  Choose when the key will expire. It is a good idea to choose an
    expiration date instead of using the default, which is *none.* If,
    for example, the email address on the key becomes invalid, an
    expiration date will remind others to stop using that public key.

        Please specify how long the key should be valid.
        0 = key does not expire
        \&lt;n\&gt;  = key expires in n days
        \&lt;n\&gt;w = key expires in n weeks
        \&lt;n\&gt;m = key expires in n months
        \&lt;n\&gt;y = key expires in n years
        Key is valid for? (0)

    Entering a value of &#96;1y&#96;, for example, makes the key valid
    for one year. (You may change this expiration date after the key is
    generated, if you change your mind.) Before the &#96;gpg&#96;
    program asks for signature information, the following prompt
    appears:

        Is this correct (y/N)?

5.  Enter &#96;y&#96; to finish the process.

6.  Enter your name and email address. *Remember this process is about
    authenticating you as a real individual.* For this reason, include
    your *real name*. Do not use aliases or handles, since these
    disguise or obfuscate your identity.

7.  Enter your real email address for your GPG key. If you choose a
    bogus email address, it will be more difficult for others to find
    your public key. This makes authenticating your communications
    difficult. If you are using this GPG key for
    [self-introduction](https://fedoraproject.org/wiki/Introduce_yourself_to_the_Docs_Project)
    on a mailing list, for example, enter the email address you use on
    that list.

8.  Use the comment field to include aliases or other information. (Some
    people use different keys for different purposes and identify each
    key with a comment, such as \'Office\' or \'Open Source Projects.\')

9.  Enter the letter &#96;O&#96; at the confirmation prompt to continue
    if all entries are correct, or use the other options to fix any
    problems.

10. Enter a passphrase for your secret key. The &#96;gpg&#96; program
    asks you to enter your passphrase twice to ensure you made no typing
    errors.

Finally, &#96;gpg&#96; generates random data to make your key as unique
as possible. Move your mouse, type random keys, or perform other tasks
on the system during this step to speed up the process. Once this step
is finished, your keys are complete and ready to use:

    pub   rsa3072 2021-02-09 [SC] [expires: 2022-02-09]
    3782CBB60147010B330523DD26FBCC7836BF353A
    uid                      John Doe (Fedora Docs) \&lt;johndoe@example.com\&gt;
    sub   rsa3072 2021-02-09 [E] [expires: 2022-02-09]

The key fingerprint is a shorthand signature for your key. It allows you
to confirm to others that they have received your actual public key
without any tampering. You do not need to write this fingerprint down.
To display the fingerprint at any time, use this command, substituting
your email address:

    gpg --fingerprint johndoe@example.com

Your key fingerprint is actually a 160 bit SHA-1 hash of the key,
represented as a 40 character string of hexadecimal digits. Though
shorter than the public key itself, it's still a bit unwieldy, so people
tend to use a shorter *GPG key ID* to refer to a key when, for example,
looking up a key in a keyserver. The GPG key ID is a small number of hex
digits drawn from the characters representing the lower-order bits of
the fingerprint. The \'short\' GPG key ID consists of the final 8
characters of the hexadecimal fingerprint, that is, the last 32 bits of
the fingerprint. Short keys are unsafe and no longer recommended because
it's possible to create collisions so that an attacker's forged key has
the same short ID as your key. Thus if you give someone the short GPG
key ID of your key, they may retrieve the attacker's key from a
keyserver instead.

For this reason, it's preferred to use the \'long\' GPG key ID, which
consists of the final 16 characters of your key's hexadecimal
fingerprint. This represents the 64 lower-order bits of your
fingerprint, which is sufficient to be collision-resistant. The
&#96;gpg&#96; program makes it easy for you to find your key's long GPG
key ID:

    gpg --list-keys --fingerprint --keyid-format 0xlong johndoe@example.com

The &#96;0xlong&#96; format prepends \'0x\' to the key ID to make it
clear that this is a series of hexadecimal digits; it is considered good
practice to do this. The output from the above command looks like this:

    pub   rsa3072/0x26FBCC7836BF353A 2021-02-09 [SC] [expires: 2022-02-09]
    Key fingerprint = 3782 CBB6 0147 010B 3305  23DD 26FB CC78 36BF 353A
    uid                      John Doe (Fedora Docs) \&lt;johndoe@example.com\&gt;
    sub   rsa3072/0xF834D62672E88A6F 2021-02-09 [E] [expires: 2022-02-09]

The first line (beginning with \'pub\') tells you what kind the key is
(that is, 3072 bit RSA) and what the long key ID is (that is,
&#96;0x26FBCC7836BF353A&#96;). You can see that this corresponds to the
last 16 characters of the Key fingerprint in the output.

Now see &lt;&lt;backup-gpg-keys-cli&gt;&gt;. Make sure to back up your
revocation keys for all active keys as this allows to revoke keys in the
event of lost passphrase of key compromise.

## Making a Backup

### Making a Key Backup Using the GNOME Desktop {#_making_a_key_backup_using_the_gnome_desktop}

1.  Right-click your key and select *Properties*.

2.  Select the *Details* tab, and select [Export to file \> Export
    secret key]{.menuchoice}.

3.  Select a destination filename and click Export.

Store the copy in a secure place, such as a locked container.

Now see &lt;&lt;exporting-gpg-keys-gnome&gt;&gt;.

### Making a Key Backup Using the KDE Desktop {#backup-gpg-keys-kde}

1.  Right-click your key and select *Export Secret Key*.

2.  Click Continue to continue at the confirmation dialog.

3.  Select a destination filename.

4.  Click Save.

Store the copy in a secure place, such as a locked container.

Now see &lt;&lt;exporting-gpg-keys-kde&gt;&gt;.

### Making a Key Backup Using the Command Line {#backup-gpg-keys-cli}

Use the following command to make the backup, which you can then copy to
a destination of your choice:

    gpg --export-secret-keys --armor johndoe@example.com \&gt; johndoe-privkey.asc

Store the copy in a secure place, such as a locked container.

Now see &lt;&lt;exporting-gpg-keys-cli&gt;&gt;.

## Making Your Public Key Available

When you make your public key available to others, they can verify
communications you sign, or send you encrypted communications if
necessary. This procedure is also known as *exporting*.

See &lt;&lt;copying-public-gpg-keys-manually&gt;&gt; to a file if you
wish to email it to individuals or groups.

### Exporting a GPG Key Using the GNOME Desktop {#exporting-gpg-keys-gnome}

1.  Click the [Menu Button \> Sync and Publish Keys&#8230;]{.menuchoice}

2.  Click Key Servers.

3.  Select *ldap://keyserver.pgp.com* in the *Publish Keys To* combobox.

4.  Click Close.

5.  Click Sync.

Now see &lt;&lt;safeguarding-your-secret-key&gt;&gt;.

### Exporting a GPG Key Using the KDE Desktop {#exporting-gpg-keys-kde}

After your key has been generated, you can export the key to a public
keyserver

1.  Right-click on the key in the main window.

2.  Select *Export Public Keys.*

3.  From there you can export your public key to the clipboard, an ASCII
    file, to an email, or directly to a key server.

4.  Export your public key to the default key server.

Now see &lt;&lt;safeguarding-your-secret-key&gt;&gt;.

### Exporting a GPG Key Using the Command Line {#exporting-gpg-keys-cli}

Use the following command to send your key to a public keyserver:

    gpg --send-key KEYNAME

For &#96;KEYNAME&#96;, substitute the key ID or fingerprint of your
primary keypair. This will send your key to the gnupg default key
server. If you prefer another one use:

    gpg --keyserver hkp://pgp.mit.edu --send-key KEYNAME

Replacing &#96;pgp.mit.edu&#96; with your server of choice.

Now see &lt;&lt;safeguarding-your-secret-key&gt;&gt;.

### Copying a Public Key Manually {#copying-public-gpg-keys-manually}

If you want to give or send a file copy of your key to someone, use this
command to write it to an ASCII text file:

    gpg --export --armor johndoe@example.com \&gt; johndoe-pubkey.asc

Now see &lt;&lt;safeguarding-your-secret-key&gt;&gt;.

## Safeguarding Your Secret Key

Treat your secret key as you would any very important document or
physical key. (Some people always keep their secret key on their person,
either on magnetic or flash media.) If you lose your secret key, you
will be unable to sign communications, or to open encrypted
communications that were sent to you.

## Hardware Token options

If you followed the above, you have a secret key which is just a regular
file. A more secure model than keeping the key on disk is to use a
hardware token.

There are several options available on the market, for example the
[YubiKey](https://www.yubico.com/products/yubikey-5-overview/). Look for
a token which advertises OpenPGP support. See [this blog
entry](https://blog.josefsson.org/2014/06/23/offline-gnupg-master-key-and-subkeys-on-yubikey-neo-smartcard/)
for how to create a key with offline backups, and use the token for
online access.

## GPG Key Revocation {#revoking-gpg-keys}

When you revoke a key, you withdraw it from public use. *You should only
have to do this if it is compromised or lost, or you forget the
passphrase.*

### Generating a Revocation Certificate

When you create the key pair you should also create a key revocation
certificate. If you later issue the revocation certificate, it notifies
others that the public key is not to be used. Users may still use a
revoked public key to verify old signatures, but not encrypt messages.
As long as you still have access to the private key, messages received
previously may still be decrypted. If you forget the passphrase, you
will not be able to decrypt messages encrypted to that key.

    gpg --output revoke.asc --gen-revoke KEYNAME

If you do not use the &#96;\--output&#96; flag, the certificate will
print to standard output.

For &#96;KEYNAME&#96;, substitute either the key ID of your primary
keypair or any part of a user ID that identifies your keypair. Once you
create the certificate (the &#96;revoke.asc&#96; file), you should
protect it. If it is published by accident or through the malicious
actions of others, the public key will become unusable. It is a good
idea to write the revocation certificate to secure removable media or
print out a hard copy for secure storage to maintain secrecy.

### Revoking a key

1.  Revoke the key locally:

        gpg --import revoke.asc

    Once you locally revoke the key, you must send the revoked
    certificate to a keyserver, regardless of whether the key was
    originally issued in this way. Distribution through a server helps
    other users to quickly become aware the key has been compromised.

2.  Export to a keyserver with the following command:

        gpg --keyserver hkp://pgp.mit.edu --send-keys KEYNAME

    For &#96;KEYNAME&#96;, substitute either the key ID of your primary
    keypair or any part of a user ID that identifies your keypair.

## Additional resources {#_additional_resources_13}

&#42; [GPG home page](https://www.gnupg.org/) &#42; [Official GPG
documentation](https://www.gnupg.org/documentation/) &#42; [Wikipedia -
Public Key
Cryptography](https://en.wikipedia.org/wiki/Public-key_cryptography)

See a typo, something missing or out of date, or anything else which can
be improved? Edit this document at [quick-docs's git
repository](https://pagure.io/fedora-docs/quick-docs).

# Disabling the GNOME automatic screen locking {#_disabling_the_gnome_automatic_screen_locking}

Oğuz Ersen

In the interest of safety and privacy, the GNOME automatic screen lock
is enabled by default.

When the screen locks after a period of inactivity, you must enter your
password to unlock the screen.

You can disable this feature at any time.

To disable the GNOME automatic screen lock, complete the following
steps.

For Fedora 31 (GNOME 3.34):

1.  On the desktop, navigate to the upper-right corner of the screen,
    click the arrow icon to expand the desktop options and then click
    the &#42;Settings&#42; icon.

2.  From the the &#42;Settings&#42; menu, select &#42;Privacy&#42;.

3.  On the &#42;Privacy&#42; page, select &#42;Screen Lock&#42;, and
    toggle the &#42;Automatic Screen Lock&#42; switch from &#42;On&#42;
    to &#42;Off&#42;.

4.  Close the window and verify that in the &#42;Privacy&#42; page, the
    &#42;Screen Lock&#42; is &#42;Off&#42;.

For Fedora 32 (GNOME 3.36):

1.  On the desktop, navigate to the upper-right corner of the screen,
    click the arrow icon to expand the desktop options and then click
    &#42;Settings&#42;.

2.  From the &#42;Settings&#42; menu, select &#42;Privacy&#42;, and then
    select &#42;Screen Lock&#42;.

3.  On the &#42;Screen Lock&#42; page, toggle the &#42;Automatic Screen
    Lock&#42; switch from &#42;On&#42; to &#42;Off&#42;

To enable the automatic screen lock, repeat this process and toggle the
switch from &#42;Off&#42; to &#42;On&#42;.

# Displaying a User Prompt on the GNOME Login Screen {#_displaying_a_user_prompt_on_the_gnome_login_screen}

Harsh Jain

To show a user prompt instead of a list of users on the GNOME login
screen, open a terminal and perform the following steps:

1.  Create a file for the GNOME Display Manager (GDM) configuration.

        $ sudo mkdir /etc/dconf/db/gdm.d

        $ sudo vim /etc/dconf/db/gdm.d/01-hide-users

2.  In a text editor of your choice, &#96;vim&#96; in this example,
    insert the following content to the
    &#96;/etc/dconf/db/gdm.d/01-hide-users&#96; file:

        [org/gnome/login-screen]
        banner-message-enable=true
        banner-message-text='ENTER ANY MESSAGE YOU WANT HERE. FOR A NEW LINE USE \n.'
        disable-restart-buttons=true
        disable-user-list=true

    :::: note
    ::: title
    :::

    To not display the banner message, do not include the first and
    second line. To enable the &#96;Restart&#96; button, do not include
    the fourth line.
    ::::

    Save the file and return to the terminal.

3.  Create another file for GDM configuration.

        $ sudo vim /etc/dconf/profile/gdm

    Insert the following content in the &#96;/etc/dconf/profile/gdm&#96;
    file:

        user-db:user
        system-db:gdm

    Save the file.

4.  Enter the following command:

        $ sudo dconf update

5.  Check if the command was executed correctly:

        $ ls /etc/dconf/db

    The output should contain the following:

        gdm gdm.d \&#8230; [output truncated]

6.  Restart GDM for the changes to take effect.

        $ sudo systemctl restart gdm

# Disk Encryption User Guide {#_disk_encryption_user_guide}

Mat McCabe ; Mauricio Tavares; The Fedora Docs team

## What is block device encryption? {#_what_is_block_device_encryption}

Block device encryption encrypts/decrypts the data transparently as it
is written/read from block devices, the underlying block device sees
only encrypted data.

To mount encrypted block devices the sysadmin (or user, depending on
context) must provide a passphrase to activate the decryption key.

Encryption provides additional security beyond existing OS security
mechanisms in that it protects the device's contents even if it has been
physically removed from the system. Some systems require the encryption
key to be the same as for decryption, and other systems require a
specific key for encryption and specific second key for enabling
decryption.

## Encrypting block devices using dm-crypt/LUKS {#_encrypting_block_devices_using_dm_cryptluks}

[LUKS](https://gitlab.com/cryptsetup/cryptsetup/) (Linux Unified Key
Setup) is a specification for block device encryption. It establishes an
on-disk format for the data, as well as a passphrase/key management
policy.

LUKS uses the kernel device mapper subsystem via the &#96;dm-crypt&#96;
module. This arrangement provides a low-level mapping that handles
encryption and decryption of the device's data. User-level operations,
such as creating and accessing encrypted devices, are accomplished
through the use of the &#96;cryptsetup&#96; utility.

### Overview of LUKS {#_overview_of_luks}

&#42; What LUKS does: &#42;&#42; LUKS encrypts entire block devices
&#42;&#42;&#42; LUKS is thereby well-suited for protecting the contents
of mobile devices such as: &#42;&#42;&#42;&#42; Removable storage media
&#42;&#42;&#42;&#42; Laptop disk drives &#42;&#42; The underlying
contents of the encrypted block device are arbitrary. &#42;&#42;&#42;
This makes it useful for encrypting swap devices. &#42;&#42;&#42; This
can also be useful with certain databases that use specially formatted
block devices for data storage. &#42;&#42; LUKS uses the existing device
mapper kernel subsystem. &#42;&#42;&#42; This is the same subsystem used
by LVM, so it is well tested. &#42;&#42; LUKS provides passphrase
strengthening. &#42;&#42;&#42; This protects against dictionary attacks.
&#42;&#42; LUKS devices contain multiple key slots. &#42;&#42;&#42; This
allows users to add backup keys/passphrases. &#42; What LUKS does not
do: &#42;&#42; LUKS is not well-suited for applications requiring many
(more than eight) users to have distinct access keys to the same device.
&#42;&#42; LUKS is not well-suited for applications requiring file-level
encryption.

### How will I access the encrypted devices after installation? (System Startup) {#_how_will_i_access_the_encrypted_devices_after_installation_system_startup}

During system startup you will be presented with a passphrase prompt.
After the correct passphrase has been provided the system will continue
to boot normally. If you used different passphrases for multiple
encrypted devices you may need to enter more than one passphrase during
the startup.

:::: tip
::: title
:::

Consider using the same passphrase for all encrypted block devices
within a given system. This will simplify system startup and you will
have fewer passphrases to remember. Just make sure you choose a good
passphrase!
::::

### Choosing a Good Passphrase {#_choosing_a_good_passphrase}

While dm-crypt/LUKS supports both keys and passphrases, the anaconda
installer only supports the use of passphrases for creating and
accessing encrypted block devices during installation.

LUKS does provide passphrase strengthening but it is still a good idea
to choose a good (meaning \'difficult to guess\') passphrase. Note the
use of the term \'passphrase\', as opposed to the term \'password\'.
This is intentional. Providing a phrase containing multiple words to
increase the security of your data is important.

## Creating Encrypted Block Devices in Anaconda {#_creating_encrypted_block_devices_in_anaconda}

You can create encrypted devices during system installation. This allows
you to easily configure a system with encrypted partitions.

To enable block device encryption, check the \'Encrypt System\' checkbox
when selecting automatic partitioning or the \'Encrypt\' checkbox when
creating an individual partition, software RAID array, or logical
volume. After you finish partitioning, you will be prompted for an
encryption passphrase. This passphrase will be required to access the
encrypted devices. If you have pre-existing LUKS devices and provided
correct passphrases for them earlier in the install process the
passphrase entry dialog will also contain a checkbox. Checking this
checkbox indicates that you would like the new passphrase to be added to
an available slot in each of the pre-existing encrypted block devices.

:::: tip
::: title
:::

Checking the \'Encrypt System\' checkbox on the \'Automatic
Partitioning\' screen and then choosing \'Create custom layout\' does
not cause any block devices to be encrypted automatically.
::::

:::: tip
::: title
:::

You can use &#96;kickstart&#96; to set a separate passphrase for each
new encrypted block device.
::::

### What Kinds of Block Devices Can Be Encrypted? {#_what_kinds_of_block_devices_can_be_encrypted}

Most types of block devices can be encrypted using LUKS. From anaconda
you can encrypt partitions, LVM physical volumes, LVM logical volumes,
and software RAID arrays.

### Limitations of Anaconda's Block Device Encryption Support {#_limitations_of_anacondas_block_device_encryption_support}

&#42; &#42;&#42;Filling the Device with Random Data Before
Encrypting&#42;&#42;

\+ Filling a device with random data prior to encrypting improves the
strength of the encryption. However, it can take a very long time to
fill the device with random data. It is because of those time
requirements that anaconda does not offer this option. This step can be
performed manually, using a &#96;kickstart %pre&#96; script.
Instructions can be found
[here](https://fedoraproject.org/wiki/Disk_Encryption_User_Guide&#35;randomize_device).

&#42; &#42;&#42;Using a Key Comprised of Randomly Generated Data to
Access Encrypted Devices&#42;&#42;

\+ In addition to passphrases, LUKS devices can be accessed with a key
comprised of randomly generated data. Setting up one or more keys to
access the encrypted devices can be done on the installed system or
through the use of a &#96;kickstart %post&#96; script. Instructions can
be found
[here](https://fedoraproject.org/wiki/Disk_Encryption_User_Guide&#35;new_key).

## Creating Encrypted Block Devices on the Installed System After Installation {#_creating_encrypted_block_devices_on_the_installed_system_after_installation}

Encrypted block devices can be created and configured after
installation.

### Create the block devices {#_create_the_block_devices}

Create the block devices you want to encrypt by using &#96;parted&#96;,
&#96;pvcreate&#96;, &#96;lvcreate&#96; and &#96;mdadm&#96;.

### Optional: Fill the device with random data {#_optional_fill_the_device_with_random_data}

Filling &lt;device&gt; (eg: &#96;/dev/sda3&#96;) with random data before
encrypting it greatly increases the strength of the encryption. The
downside is that it can take a very long time.

:::: warning
::: title
:::

The commands below will destroy any existing data on the device.
::::

&#42; The best way, which provides high quality random data but takes a
long time (several minutes per gigabyte on most systems)

\+

    dd if=/dev/urandom of=\&lt;device\&gt;

&#42; The Fastest way, which provides lower quality random data

\+

    badblocks -c 10240 -s -w -t random -v \&lt;device\&gt;

### Format the device as a dm-crypt/LUKS encrypted device {#_format_the_device_as_a_dm_cryptluks_encrypted_device}

:::: warning
::: title
:::

The commands below will destroy any existing data on the device.
::::

    cryptsetup luksFormat \&lt;device\&gt;

:::: tip
::: title
:::

For more information, read the &#96;cryptsetup(8)&#96; man page.
::::

After supplying the passphrase twice the device will be formatted for
use. To verify, use the following command:

    cryptsetup isLuks \&lt;device\&gt; \&amp;\&amp; echo Success

To see a summary of the encryption information for the device, use the
following command:

    cryptsetup luksDump \&lt;device\&gt;

### Create a mapping to allow access to the device's decrypted contents {#_create_a_mapping_to_allow_access_to_the_devices_decrypted_contents}

To access the device's decrypted contents, a mapping must be established
using the kernel &#96;device-mapper&#96;.

It is useful to choose a meaningful name for this mapping. LUKS provides
a UUID (Universally Unique Identifier) for each device. This, unlike the
device name (eg: &#96;/dev/sda3&#96;), is guaranteed to remain constant
as long as the LUKS header remains intact. To find a LUKS device's UUID,
run the following command:

    cryptsetup luksUUID \&lt;device\&gt;

An example of a reliable, informative and unique mapping name would be
&#96;luks-&lt;uuid&gt;&#96;, where &lt;uuid&gt; is replaced with the
device's LUKS UUID (eg:
&#96;luks-50ec957a-5b5a-47ee-85e6-f8085bbc97a8&#96;). This naming
convention might seem unwieldy but is it not necessary to type it often.

    cryptsetup luksOpen \&lt;device\&gt; \&lt;name\&gt;

There should now be a device node, &#96;/dev/mapper/&lt;name&gt;&#96;,
which represents the decrypted device. This block device can be read
from and written to like any other unencrypted block device.

To see some information about the mapped device, use the following
command:

    dmsetup info \&lt;name\&gt;

:::: tip
::: title
:::

For more information, read the &#96;dmsetup(8)&#96; man page.
::::

### Create filesystems on the mapped device, or continue to build complex storage structures using the mapped device {#_create_filesystems_on_the_mapped_device_or_continue_to_build_complex_storage_structures_using_the_mapped_device}

Use the mapped device node (&#96;/dev/mapper/&lt;name&gt;&#96;) as any
other block device. To create an &#96;ext2&#96; filesystem on the mapped
device, use the following command:

    mke2fs /dev/mapper/\&lt;name\&gt;

To mount this filesystem on &#96;/mnt/test&#96;, use the following
command:

:::: important
::: title
:::

The directory &#96;/mnt/test&#96; must exist before executing this
command.
::::

    mount /dev/mapper/\&lt;name\&gt; /mnt/test

### Add the mapping information to /etc/crypttab {#_add_the_mapping_information_to_etccrypttab}

In order for the system to set up a mapping for the device, an entry
must be present in the &#96;/etc/crypttab&#96; file. If the file doesn't
exist, create it and change the owner and group to root
(&#96;root:root&#96;) and change the mode to &#96;0744&#96;. Add a line
to the file with the following format:

    \&lt;name\&gt;  \&lt;device\&gt;  none

The &lt;device&gt; field should be given in the form
\'UUID=&lt;luks_uuid&gt;\', where &lt;luks_uuid&gt; is the LUKS uuid as
given by the command &#96;cryptsetup luksUUID &lt;device&gt;&#96;. This
ensures the correct device will be identified and used even if the
device node (eg: &#96;/dev/sda5&#96;) changes.

:::: tip
::: title
:::

For details on the format of the &#96;/etc/crypttab&#96; file, read the
&#96;crypttab(5)&#96; man page.
::::

### Add an entry to &#96;/etc/fstab&#96; {#_add_an_entry_to_96etcfstab96}

Add an entry to &#96;/etc/fstab&#96; file. This is only necessary if you
want to establish a persistent association between the device and a
mountpoint. Use the decrypted device, &#96;/dev/mapper/&lt;name&gt;&#96;
in the &#96;/etc/fstab&#96; file.

In many cases it is desirable to list devices in &#96;/etc/fstab&#96; by
UUID or by a filesystem label. The main purpose of this is to provide a
constant identifier in the event that the device name (eg:
&#96;/dev/sda4&#96;) changes. LUKS device names in the form of
&#96;/dev/mapper/luks-&lt;luks_uuid&gt;&#96; are based only on the
device's LUKS UUID, and are therefore guaranteed to remain constant.
This fact makes them suitable for use in &#96;/etc/fstab&#96;.

:::: tip
::: title
:::

For details on the format of the /etc/fstab file, read the fstab(5) man
page.
::::

## Common Post-Installation Tasks {#_common_post_installation_tasks}

### Backup LUKS headers {#_backup_luks_headers}

If the sectors containing the LUKS headers are damaged - by user error
or HW failure - all data in the encrypted block device is lost. Backing
up the headers can help recovering data in such cases.

To backup the LUKS headers, use the following command:

    cryptsetup luksHeaderBackup --header-backup-file \&lt;file\&gt; \&lt;device\&gt;

To restore the LUKS headers, use the following command:

:::: warning
::: title
:::

The command below can destroy data, if wrong headers are applied or
wrong device is selected! Be sure to backup headers from recovering
device first.
::::

    cryptsetup luksHeaderRestore --header-backup-file \&lt;file\&gt; \&lt;device\&gt;

See also
<https://gitlab.com/cryptsetup/cryptsetup/wikis/FrequentlyAskedQuestions&#35;6-backup-and-data-recovery>

### Set a randomly generated key as an additional way to access an encrypted block device {#_set_a_randomly_generated_key_as_an_additional_way_to_access_an_encrypted_block_device}

a.  Generate a key

    This will generate a 256-bit key in the file
    &#96;\$HOME/keyfile&#96;.

        dd if=/dev/urandom of=$HOME/keyfile bs=32 count=1
        chmod 600 $HOME/keyfile

b.  Add the key to an available keyslot on the encrypted device

        cryptsetup luksAddKey \&lt;device\&gt; ~/keyfile

c.  Add a new passphrase to an existing device

        cryptsetup luksAddKey \&lt;device\&gt;

    After being prompted for any one of the existing passprases for
    authentication, you will be prompted to enter the new passphrase.

### Remove a passphrase or key from a device {#_remove_a_passphrase_or_key_from_a_device}

    cryptsetup luksRemoveKey \&lt;device\&gt;

You will be prompted for the passphrase you wish to remove and then for
any one of the remaining passphrases for authentication.

# Getting started with Apache HTTP Server {#_getting_started_with_apache_http_server}

Jan Kuparinen

> The Apache HTTP Server is one of the most commonly-used web servers.
> This section acts as a quick-start guide to deploying and configuring
> Apache on Fedora.

## Installing HTTPD {#_installing_httpd}

This procedure describes the steps to install Apache &#42;HTTPD&#42; on
Fedora.

1.  Install &#42;HTTPD&#42; packages.

        sudo dnf install httpd -y

2.  Start the &#42;HTTPD&#42; service.

        sudo systemctl start httpd.service

:::: note
::: title
:::

To enable auto start of &#42;HTTPD&#42; service at boot, execute the
following command:

    sudo systemctl enable httpd.service
::::

Navigate to <http://localhost> to access the Apache test page. You may
not be able to access the server from any other host. To access the
server from other hosts, see [Opening firewall
ports](&#35;opening-firewall-ports).

## Securing Apache HTTPD {#_securing_apache_httpd}

To enable TLS/SSL support, download and install one of the following
packages:

&#42; [mod_ssl](https://packages.fedoraproject.org/pkgs/httpd/mod_ssl/),
based on [OpenSSL](https://www.openssl.org) &#42;
[mod_gnutls](https://packages.fedoraproject.org/pkgs/mod_gnutls/mod_gnutls/),
based on [GnuTLS](https://www.gnutls.org/) &#42;
[mod_nss](https://packages.fedoraproject.org/pkgs/mod_nss/mod_nss/),
based on
[NSS](https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS)

### Using mod_ssl {#using-mod-ssl}

#### Installing mod_ssl {#installing-mod-ssl}

The [mod_ssl](https://packages.fedoraproject.org/pkgs/httpd/mod_ssl/)
package will be automatically enabled post installation. Install the
[mod_ssl](https://packages.fedoraproject.org/pkgs/httpd/mod_ssl/)
package using the following command:

    sudo dnf install mod_ssl -y

#### Generating a new certificate {#generating-new-certificate}

To generate a new certificate, refer to [Create a certificate using
OpenSSL](https://fedoraproject.org/wiki/Https&#35;openssl).

#### Installing an existing certificate {#installing-existing-certificate}

If you already have a certificate generated on another computer, do the
following:

1.  Move the certificate and the key file to the correct folder

        sudo mv key_file.key /etc/pki/tls/private/myhost.com.key
        sudo mv certificate.crt /etc/pki/tls/certs/myhost.com.crt

2.  Ensure that the following parameters are correct:

    a.  SELinux contexts

            restorecon /etc/pki/tls/private/myhost.com.key
            restorecon /etc/pki/tls/certs/myhost.com.crt

    b.  Ownership

            sudo chown root:root /etc/pki/tls/private/myhost.com.key
            sudo chown root:root /etc/pki/tls/certs/myhost.com.crt

    c.  Permissions

            sudo chmod 0600 /etc/pki/tls/private/myhost.com.key
            sudo chmod 0600 /etc/pki/tls/certs/myhost.com.crt

After installing the existing certificate, set up the certificate using
&lt;&lt;mod_ssl configuration&gt;&gt;.

#### mod_ssl configuration {#mod-ssl-configuration}

The default TLS/SSL configuration is contained in the file
&#96;/etc/httpd/conf.d/ssl.conf&#96;. In the &#96;ssl.conf&#96; file,
following are the directives that specify where the TLS/SSL certificate
and key are located:

    SSLCertificateFile /etc/pki/tls/certs/localhost.crt
    SSLCertificateKeyFile /etc/pki/tls/private/localhost.key

These directives are enclosed in a block defining a [virtual
host](https://httpd.apache.org/docs/current/vhosts/):

    \&lt;VirtualHost _default_:443\&gt;
    \&#8230;
    SSLCertificateFile /etc/pki/tls/certs/localhost.crt
    \&#8230;
    SSLCertificateKeyFile /etc/pki/tls/private/localhost.key
    \&#8230;
    \&lt;/VirtualHost\&gt;

To define a different location for these files, do the following:

1.  Create a copy of the &#96;/etc/httpd/conf.d/ssl.conf&#96; file and
    renew the file to &#96;z-ssl-local.conf&#96;.

2.  Edit the following lines in the &#96;z-ssl-local.conf&#96; file:

<!-- -->

    \&lt;VirtualHost _default_:443\&gt;
    SSLCertificateFile /etc/pki/tls/certs/www.myhost.org.crt
    SSLCertificateKeyFile /etc/pki/tls/private/www.myhost.org.key
    \&lt;/VirtualHost\&gt;

This file will override the two settings for the
&#96;\_default\_:443&#96; virtual host; all other settings from
&#96;ssl.conf&#96; will be retained.

#### Settings for individual virtual hosts {#settings-individual-virtual-hosts}

To use SSL/TLS for a specific virtual host with a different certificate
as default, do the following:

1.  Open that virtual host's configuration file
    &#96;/etc/httpd/conf.d/hostname.conf&#96;.

2.  Insert these lines between &#96;&lt;VirtualHost
    hostname:port&gt;&#96; and &#96;&lt;/VirtualHost&gt;&#96;:

        SSLEngine on
        SSLCertificateFile /etc/pki/tls/certs/hostname.crt
        SSLCertificateKeyFile /etc/pki/tls/private/hostname.key

## Installing webapps {#_installing_webapps}

You probably want to run something on your web server. Many of the most
popular web applications are packaged for Fedora. Using the packaged
versions of web applications is recommended. These packages will be
configured following the distribution's best practices which help to
ensure the security of the installation.

For instance, by installing static files to locations the web server
does not have the ability to write to, and doing access control with
configuration files rather than &#96;.htaccess&#96; files, which are
slightly more vulnerable to attack.

Packaged web applications will also be configured to work with SELinux,
which provides significant security benefits.

You will also receive updates through the usual Fedora update process,
making it easier to keep your installation up to date.

They will also often have the default configuration tweaked according to
Fedora's conventions, meaning you have to do less work to get the
application up and running.

Most web applications are simply packaged according to their name. For
instance, you can install Wordpress by executing the following command:

    sudo dnf install wordpress

Packaged web applications will usually provide Fedora-specific
instructions in a documentation file. For instance, Wordpress provides
the files &#96;/usr/share/doc/wordpress/README.fedora&#96; and
&#96;/usr/share/doc/wordpress/README.fedora-multiuser&#96;.

Packaged web applications usually restrict access by default so you can
access them only from the server host itself, to ensure you can run all
initial configuration safely and things like administration interfaces
are not left accessible to the public. For information on how to broaden
access, see [Enabling access to web
applications](getting-started-with-apache-http-server.adoc&#35;enabling-access-to-web-applications).

Web applications commonly require the use of a database server. This
Quick Docs article provides information on installing and configuring
[PostgreSQL](postgresql.xml) and this wiki page about
[MariaDB](https://fedoraproject.org/wiki/MariaDB) on Fedora.

## Configuring Apache HTTPD {#_configuring_apache_httpd}

&#96;/etc/httpd/conf/httpd.conf&#96; is the main Apache configuration
file. Custom configuration files are specified under
&#96;/etc/httpd/conf.d/&#42;.conf&#96;. If the same settings are
specified in both &#96;/etc/httpd/conf/httpd.conf&#96; and a
&#96;.conf&#96; file in &#96;/etc/httpd/conf.d/&#96;, the setting from
the &#96;/etc/httpd/conf.d/&#96; file will be used.

Files in &#96;/etc/httpd/conf.d/&#96; are read in alphabetical order: a
setting from &#96;/etc/httpd/conf.d/z-foo.conf&#96; will be used over a
setting from &#96;/etc/httpd/conf.d/foo.conf&#96;. Similarly, a setting
from &#96;/etc/httpd/conf.d/99-foo.conf&#96;, will be used over a
setting from &#96;/etc/httpd/conf.d/00-foo.conf&#96;.

As a best practice, do not modify &#96;/etc/httpd/conf/httpd.conf&#96;
or any of the &#96;/etc/httpd/conf.d&#96; files shipped by Fedora
packages directly. If you make any local changes to these files, then
any changes to them in newer package versions will not be directly
applied. Instead, a &#96;.rpmnew&#96; file will be created, and you will
have to merge the changes manually.

It is recommended to create a new file in &#96;/etc/httpd/conf.d/&#96;
which will take precedence over the file you wish to modify, and edit
the required settings. For instance, to change a setting specified in
&#96;/etc/httpd/conf.d/foo.conf&#96; you could create the file
&#96;/etc/httpd/conf.d/z-foo-local.conf&#96;, and place your setting in
that file.

:::: note
::: title
:::

After making any changes to your server configuration, execute the
following command:

    sudo systemctl reload httpd.service

Certain changes may require Apache to be fully restarted. To fully
restart Apache, execute the following command:

    sudo systemctl restart httpd.service
::::

### Enabling access to web applications

By default Fedora-packaged web applications are usually configured such
that, access is allowed only from the localhost. This is defined by the
file &#96;/etc/httpd/conf.d/webapp.conf&#96; which contains the
following settings:

    \&lt;Directory /usr/share/webapp\&gt;
    \&lt;IfModule mod_authz_core.c\&gt;
    \&#35; Apache 2.4
    Require local
    \&lt;/IfModule\&gt;
    \&lt;IfModule !mod_authz_core.c\&gt;
    \&#35; Apache 2.2
    Order Deny,Allow
    Deny from all
    Allow from 127.0.0.1
    Allow from ::1
    \&lt;/IfModule\&gt;
    \&lt;/Directory\&gt;

Before allowing general access to the webapp, ensure to do the
following:

&#42; \[&#42;\] Webapp has been configured correctly &#42; \[&#42;\]
Administration interface and other sensitive areas are not accessible
without appropriate authentication &#42; \[&#42;\] Database
configuration is secure, if the application uses a database

To broaden access to the application, create a file
&#96;/etc/httpd/conf.d/z-webapp-allow.conf&#96;. To allow access to all
systems on a typical local network, add the following lines into the
file:

    \&lt;Directory /usr/share/webapp\&gt;
    \&lt;IfModule mod_authz_core.c\&gt;
    \&#35; Apache 2.4
    Require local
    Require ip 192.168.1
    \&lt;/IfModule\&gt;
    \&lt;IfModule !mod_authz_core.c\&gt;
    \&#35; Apache 2.2
    Order Deny,Allow
    Deny from all
    Allow from 127.0.0.1
    Allow from ::1
    Allow from 192.168.1
    \&lt;/IfModule\&gt;
    \&lt;/Directory\&gt;

Once the application is correctly configured, add the following
configuration to allow access from any host:

    \&lt;Directory /usr/share/webapp\&gt;
    \&lt;IfModule mod_authz_core.c\&gt;
    \&#35; Apache 2.4
    Require all granted
    \&lt;/IfModule\&gt;
    \&lt;IfModule !mod_authz_core.c\&gt;
    \&#35; Apache 2.2
    Order Deny,Allow
    Allow from all
    \&lt;/IfModule\&gt;
    \&lt;/Directory\&gt;

### Opening firewall ports

:::: important
::: title
:::

This exposes your computer to the Internet and potential attackers.
Secure your system and your Apache installation properly before exposing
your server to the Internet.
::::

Apache uses port 80 for plain http connections and port 443 for TLS/SSL
connections by default. To make this service available from other
computers or the Internet, allow Apache through the firewall using any
one the following commands:

To allow Apache through the firewall at each boot:

&#42; For plain HTTP connections:

\+

    sudo firewall-cmd --permanent --add-service=http

&#42; For TLS/SSL connections:

\+

    sudo firewall-cmd --permanent --add-service=https

To allow Apache through the firewall instantly:

&#42; For plain HTTP connections:

\+

    sudo firewall-cmd --add-service=http

&#42; For TLS/SSL connections:

\+

    sudo firewall-cmd --add-service=https

:::: note
::: title
:::

If your server is running in a network with a NAT router, you will also
need to configure your router to forward the HTTP and HTTPS ports to
your server, if you wish to allow access from outside your local
network.
::::

### Disabling Test Page

To disable the test page, comment out all the lines in the file
&#96;/etc/httpd/conf.d/welcome.conf&#96; using &#96;\\#&#96; as follows:

    \&#35; \&lt;LocationMatch '^/+$'\&gt;
    \&#35;    Options -Indexes
    \&#35;    ErrorDocument 403 /.noindex.html
    \&#35; \&lt;/LocationMatch\&gt;

    \&#35; \&lt;Directory /usr/share/httpd/noindex\&gt;
    \&#35;    AllowOverride None
    \&#35;    Require all granted
    \&#35; \&lt;/Directory\&gt;

    \&#35; Alias /.noindex.html /usr/share/httpd/noindex/index.html

**Additional resources**

&#42; [Apache Documentation](https://httpd.apache.org/docs/current/)
&#42; [Apache \'Getting
Started\'](https://httpd.apache.org/docs/current/getting-started.html)
&#42; [Apache TLS/SSL
documentation](https://httpd.apache.org/docs/current/ssl/) &#42; [Apache
security
tips](https://httpd.apache.org/docs/current/misc/security_tips.html)
&#42; [OwnCloud](https://fedoraproject.org/wiki/OwnCloud)

# The GRUB2 Bootloader -- Installation and Configuration {#_the_grub2_bootloader_installation_and_configuration}

Michael Wu; The Fedora Documentation Team :page-aliases:
installing-grub2.adoc

&#42;GRUB2&#42; is the latest version of &#42;GNU GRUB&#42;, the *GRand
Unified Bootloader*. A bootloader is the first software program that
runs when a computer starts. It is responsible for loading and
transferring control to the operating system kernel. In Fedora, the
kernel is Linux. The kernel then initializes the rest of the operating
system.

&#42;GRUB2&#42; is the follower of the previous version &#42;GRUB&#42;
(version 0.9x). The original version is available under the name
&#42;GRUB Legacy&#42;.

Since Fedora 16, &#42;GRUB2&#42; has been the default bootloader on x86
BIOS systems. For upgrades of BIOS systems, the default is also to
install &#42;GRUB2&#42;, but you can opt to skip bootloader
configuration entirely.

## Discovering the firmware type {#_discovering_the_firmware_type}

To discover what firmware your machine uses, run the following command:

``` bash
[ -d /sys/firmware/efi ] \&amp;\&amp; echo UEFI || echo BIOS
```

The output returns only UEFI or BIOS, depending on the firmware your
machine runs.

## Installing GRUB2 on a BIOS system {#_installing_grub2_on_a_bios_system}

Normally, &#42;GRUB2&#42; will be installed and set up by the installer,
&#42;Anaconda&#42;, during the installation process. You will probably
never have to deal with manual installation of &#42;GRUB2&#42;. However,
in certain situations , you will want to install &#42;GRUB2&#42;
manually, especially if you need to repair the existing &#42;GRUB2&#42;
installation or you want to change its configuration.

This procedure shows the steps to install &#42;GRUB2&#42; on your
*Master Boot Record* (MBR) of your primary hard disk.

:::: formalpara
::: title
Before you start
:::

&#42; Make sure you have the the &#42;GRUB2&#42; packages and the
*os-prober* package installed in your system.
::::

\+

``` bash
dnf list installed | grep grub
```

&#42; To automatically collect information about your disks and
operating systems installed on them, the &#96;os-prober&#96; package
needs to be installed on your system.

<div>

::: title
Procedure
:::

1.  List block devices available on the system.

    ``` _bash
    lsblk
    ```

2.  Identify the primary hard disk. Usually, it is the &#96;sda&#96;
    device.

3.  Install &#42;GRUB2&#42; in the MBR of the primary hard disk.

    ``` _bash
    grub2-install /dev/sda
    ```

4.  Create a configuration file for &#42;GRUB2&#42;.

    ``` _bash
    grub2-mkconfig -o /boot/grub2/grub.cfg
    ```

5.  Reboot your computer to boot with the newly installed bootloader.

</div>

:::: formalpara
::: title
More information
:::

&#42; The &#96;grub2-mkconfig&#96; command creates a new configuration
based on the currently running system. It collects information from the
&#96;/boot&#96; partition (or directory), from the
&#96;/etc/default/grub&#96; file, and the customizable scripts in
&#96;/etc/grub.d&#96;.
::::

&#42; The configuration format is changing with time, and a new
configuration file can become slightly incompatible with the older
versions of the bootloader. Always run &#96;grub2-install&#96; before
you create the configuration file with &#96;grub2-mkconfig&#96;.

&#42; In Fedora, it is generally safe to edit
&#96;/boot/grub2/grub.cfg&#96; manually. &#42;Grubby&#42; in Fedora
patches the configuration when a kernel update is performed and will try
to not make any other changes than what is necessary. Manual changes can
be overwritten with &#96;grub2-mkconfig&#96; when the system gets
upgraded with &#42;Anaconda&#42;. Customizations placed in
&#96;/etc/grub.d/40_custom&#96; or &#96;/boot/grub2/custom.cfg&#96;
files will survive running the &#96;grub2-mkconfig&#96; command.

## Installing GRUB2 on a UEFI system {#_installing_grub2_on_a_uefi_system}

Normally, &#42;GRUB2&#42; will be installed and set up by the installer,
&#42;Anaconda&#42;, during the installation process. You will probably
never have to deal with manual installation of &#42;GRUB2&#42;. However,
in certain situations , you will want to install &#42;GRUB2&#42;
manually, especially if you need to repair the existing &#42;GRUB2&#42;
installation or you want to change its configuration.

This procedure shows the steps to install &#42;GRUB2&#42; on a UEFI
system on Fedora 18 or newer. The procedure consists of four parts.

### Creating an EFI System Partition {#create-an-esp}

The UEFI firmware requires to boot from an *EFI System Partition* on a
disk with a GPT label. To create such a partition:

1.  List available block devices to find a place to create your ESP.

    ``` _bash
    lsblk -f -p
    ```

2.  Create at least a 128 MiB disk partition using a GPT label on the
    primary hard disk.

    ``` _bash
    gdisk /dev/sda
    ```

    For the sake of this procedure, we assume that the created partition
    is recognized as &#96;/dev/sda1&#96;.

3.  Format the partition with the *FAT32* file system.

    ``` _bash
    mkfs.vfat /dev/sda1
    ```

4.  Create the &#96;/boot/efi&#96; directory as a mount point for the
    new partition.

    ``` _bash
    mkdir /boot/efi
    ```

5.  Mount the partition to the &#96;/boot/efi&#96; mount point.

    ``` _bash
    mount /dev/sda1 /boot/efi
    ```

6.  Proceed to the next part.

### Install the bootloader files

In order to use &#42;GRUB2&#42; with on UEFI systems, you need to
install necessary packages:

1.  Re-install the necessary packages.

    ``` _bash
    dnf reinstall grub2-efi grub2-efi-modules shim-\\&#42;
    ```

2.  If the above command ends with an error, install the packages.

    ``` _bash
    dnf install grub2-efi grub2-efi-modules shim-\\&#42;
    ```

:::: formalpara
::: title
More information
:::

&#42; This installs the signed &#42;shim&#42; and the &#42;GRUB2&#42;
binary.
::::

### Create a GRUB2 configuration {#create-a-grub-2-configuration}

If you already have a working &#42;GRUB2&#42; EFI configuration file,
you do not need to do anything else.

Otherwise, create the configuration file using the
&#96;grub2-mkconfig&#96; command.

``` _bash
grub2-mkconfig -o /boot/grub2/grub.cfg
```

:::: formalpara
::: title
More information
:::

&#42; Under EFI, &#42;GRUB2&#42; looks for its configuration in
&#96;/boot/efi/EFI/fedora/grub.cfg&#96;, however the postinstall script
of &#96;grub2-common&#96; installs a small shim which chains to the
standard configuration at &#96;/boot/grub2/grub.cfg&#96; which is
generated above. To reset this shim to defaults, delete the existing
&#96;/boot/efi/EFI/fedora/grub.cfg&#96; and then reinstall
&#96;grub2-common&#96;.
::::

\+

``` _bash
rm -f /boot/efi/EFI/fedora/grub.cfg
dnf reinstall grub2-common
```

\+ &#42; For newly installed kernels to work, &#96;grubby&#96; expects
&#96;/etc/grub2-efi.cfg&#96; to be a symlink to the real
&#96;grub.cfg&#96; (for example &#96;/boot/grub2/grub.cfg&#96;).

### Solving problems with UEFI bootloader

When you power on your system, your firmware will look for EFI variables
that tell it how to boot. On running systems, which have booted into the
EFI mode and their EFI runtime services are working correctly, you can
configure your boot menu with &#96;efibootmgr&#96;.

If not, &#96;shim&#96; can help you bootstrap. The EFI program
&#96;/boot/efi/EFI/BOOT/fallback.efi&#96; will look for files called
&#96;BOOT.CSV&#96; in your ESP and will add boot entries corresponding
to them. The &#96;shim&#96; command provides its own &#96;BOOT.CSV&#96;
file that will add an entry for &#96;grub2-efi&#96;.

During the boot process, you can use the &#42;EFI Shell&#42; to invoke
the &#96;fallback.efi&#96; profile to boot the system:

1.  Enter the boot partition.

        \&gt; fs0:

2.  Navigate into the &#96;EFI\\BOOT&#96; directory.

        \&gt; cd EFI\BOOT

3.  Invoke the &#96;fallback.efi&#96; profile.

        \&gt; fallback.efi

:::: formalpara
::: title
More information
:::

&#42; If you have no boot entries at all, then just booting off your
disk in UEFI mode should automatically invoke
&#96;/boot/efi/EFI/BOOT/BOOTX64.EFI&#96;, which will, in turn, invoke
&#96;fallback.efi&#96;.
::::

&#42; If you already have incorrect boot entries, you'll either need to
delete them or to modify &#96;BOOT.CSV&#96; to create new entries with
different names.

## Adding other operating systems to the GRUB2 menu {#_adding_other_operating_systems_to_the_grub2_menu}

Normally, &#42;GRUB2&#42; is preset to boot multiple operating systems
during the Fedora installation process. If you can, it is advisable to
install non-Linux operating systems first. Then, during the installation
process, all those operating systems and their locations will be
discovered and properly set.

Adding other records into the &#42;GRUB2&#42; menu only means to run
&#96;grub2-mkconfig&#96; command to regenerate the configuration files.
During this process, all operating systems known to the system will be
added into the configuration. By reinstalling &#42;GRUB2&#42;, this
configuration will be used for further boots.

:::: formalpara
::: title
Before you start
:::

&#42; Make sure that the operating systems are on disks, connected to
the system. &#42; You have the &#96;os-prober&#96; package installed.
::::

<div>

::: title
Procedure
:::

1.  Recreate the &#42;GRUB2&#42; configuration file.

    ``` _bash
    grub2-mkconfig -o /boot/grub2/grub.cfg
    ```

2.  Install &#42;GRUB2&#42;. &#42; On UEFI systems.

    ``` _bash
    dnf reinstall shim-\\&#42; grub2-efi-\\&#42; grub2-common
    ```

    &#42; On BIOS systems, specify the disk where the bootloader should
    be installed.

    ``` _bash
    grub2-install /dev/sda
    ```

</div>

:::: formalpara
::: title
More information
:::

&#42; The &#96;grub2-mkconfig&#96; command will add entries for all
operating systems it can find. &#42; When problems appear, see the [GRUB
manual](https://www.gnu.org/software/grub/manual/grub/grub.html&#35;Multi_002dboot-manual-config)
to solve issues with booting secondary operating systems.
::::

## Setting default entry for GRUB2 {#_setting_default_entry_for_grub2}

Since &#96;grub2-mkconfig&#96; (and &#42;os-prober&#42;) cannot estimate
which operating system, of those it finds, is to be marked as default,
we usually are unable to predict the order of the entries in
&#96;/boot/grub2/grub.cfg&#96;. To change the default layout, we need to
set the default based on the &#96;name&#96; or &#96;title&#96;.

<div>

::: title
Before you start
:::

1.  Open &#96;/etc/default/grub&#96; and make sure these lines exist in
    the file.

    ``` _bash
    GRUB_DEFAULT=saved
    GRUB_SAVEDEFAULT=false
    ```

2.  If you needed to change the content of the
    &#96;/etc/default/grub&#96;, apply the changes to
    &#96;grub.cfg&#96;.

    ``` _bash
    grub2-mkconfig -o /boot/grub2/grub.cfg
    ```

</div>

<div>

::: title
Procedure
:::

1.  List all possible menu entries.

    ``` _bash
    grep -P '^menuentry' /boot/grub2/grub.cfg | cut -d ''' -f2
    ```

2.  Select one of the displayed options and use it as an argument to set
    the default menu entry.

    ``` _bash
    grub2-set-default \&lt;menuentry\&gt;
    ```

3.  Verify the default menu entry

    ``` _bash
    grub2-editenv - list
    ```

4.  Regenerate the &#42;GRUB2&#42; configuration file and reinstall the
    bootloader into the MBR, as described in [Adding other operating
    systems to the &#42;GRUB2&#42;
    menu](&#35;adding-other-operating-systems-grub2).

</div>

:::: formalpara
::: title
More information
:::

If you understand the risks involved, you can manually modify the
&#96;/boot/grub2/grub.cfg&#96; file. In that case, set the number of the
default operating system using the &#96;set default&#96; variable.
::::

For example:

``` _bash
set default='5'
```

:::: note
::: title
:::

If you edit the configuration file manually, the settings will be
overwritten each time the &#96;grub2-mkconfig&#96; command runs.
::::

## Restoring the bootloader using the Live disk {#_restoring_the_bootloader_using_the_live_disk}

Sometimes, especially after a secondary operating systems has been
installed, the master boot record gets damaged which then prevents the
original Linux system from booting.

If this happens, it is necessary to reinstall &#42;GRUB2&#42; to
recreate the original settings. The process not only discovers all
installed operating systems, but usually adds them to the
&#42;GRUB2&#42; configuration files, so they will all become bootable by
&#42;GRUB2&#42;.

:::: formalpara
::: title
Before you start
:::

&#42; Get the Fedora Live ISO from
[fedoraproject.org](https://fedoraproject.org).
::::

&#42; Prepare a bootable device using the downloaded ISO, either a CD or
a USB.

<div>

::: title
Procedure
:::

1.  Boot the Fedora live system from the bootable device you have
    created.

2.  Open the terminal.

3.  Examine the partition layout and identify the &#96;/boot&#96; and
    the &#96;/root&#96; partition.

    ``` _bash
    lsblk -f -p
    ```

4.  If your &#96;/root&#96; partition is encrypted by LUKS, it must be
    decrypted.

    a.  Make sure the crypt module is in use.

        ``` _bash
        modprobe dm-crypt
        ```

    b.  Decrypt the &#96;/root&#96; partition (e.g.
        &#96;/dev/sda3&#96;).

        ``` _bash
        cryptsetup luksOpen /dev/sda3 myvolume
        ```

        The decrypted device (i.e. &#96;myvolume&#96;) will be
        accessible under &#96;/dev/mapper&#96;.

5.  Follow the BTRFS steps (used by default in Fedora 33 or newer).

    a.  Mount the &#96;/root&#96; partition.

        &#42; For LUKS.

        ``` _bash
        mount /dev/mapper/myvolume /mnt -o subvol=root
        ```

        &#42; For non-LUKS.

        ``` _bash
        mount /dev/sda3 /mnt -o subvol=root
        ```

6.  Follow the LVM steps (used by default before Fedora 33).

    a.  Scan the LVM volumes for the volume group corresponding to the
        &#96;/root&#96; partition.

        ``` _bash
        vgscan
        ```

    b.  Activate the volume group (e.g. &#96;fedora&#96;).

        ``` _bash
        vgchange -ay fedora
        ```

    c.  Find the logical volume corresponding to &#96;/root&#96;.

        ``` _bash
        lvs
        ```

        The logical volume will be accessible under
        &#96;/dev/mapper&#96;.

    d.  Mount the logical volume (e.g.
        &#96;/dev/mapper/fedora-root&#96;) corresponding to the
        &#96;/root&#96; partition.

        ``` _bash
        mount /dev/mapper/fedora-root /mnt
        ```

7.  Mount the &#96;/boot&#96; partition (e.g. &#96;/dev/sda2&#96;).

    ``` _bash
    mount /dev/sda2 /mnt/boot
    ```

8.  Mount system processes and devices into the &#96;/root&#96;
    filesystem.

    ``` _bash
    mount -o bind /dev /mnt/dev
    mount -o bind /proc /mnt/proc
    mount -o bind /sys /mnt/sys
    mount -o bind /run /mnt/run
    ```

9.  On UEFI systems, bind the &#96;efivars&#96; directory and mount the
    EFI system partition (e.g. &#96;/dev/sda1&#96;).

    ``` _bash
    mount -o bind /sys/firmware/efi/efivars /mnt/sys/firmware/efi/efivars
    mount /dev/sda1 /mnt/boot/efi
    ```

10. Change your filesystem to the one mounted under &#96;/mnt&#96;.

    ``` _bash
    chroot /mnt
    ```

11. Re-install &#42;GRUB2&#42;.

</div>

&#42; On UEFI systems, several packages are required.

\+

``` _bash
dnf reinstall shim-\\&#42; grub2-efi-\\&#42; grub2-common
```

&#42; On BIOS systems, specify the disk (e.g. &#96;/dev/sda&#96;) where
&#42;GRUB2&#42; should be installed.

\+

``` _bash
grub2-install /dev/sda
```

\+ . Re-generate the &#42;GRUB2&#42; configuration file.

\+

``` _bash
grub2-mkconfig -o /boot/grub2/grub.cfg
```

\+ . Sync and exit the chroot.

\+

``` _bash
sync \&amp;\&amp; exit
```

\+ . Reboot the system.

## Using the GRUB2 boot prompt {#_using_the_grub2_boot_prompt}

If improperly configured, &#42;GRUB2&#42; may fail to load and
subsequently drop to a boot prompt. To boot into the system, follow the
steps below.

<div>

::: title
Procedure
:::

1.  Load the necessary modules to read your system's partitions (you
    will also need to load &#96;part_msdos&#96; or &#96;part_gpt&#96;,
    depending on your partition table).

    &#42; For BTRFS filesystems (Fedora 33 or newer).

        grub\&gt; insmod btrfs

    &#42; For LVM filesystems (older than Fedora 33).

        grub\&gt; insmod xfs
        grub\&gt; insmod lvm

2.  List the drives which &#42;GRUB2&#42; sees.

        grub\&gt; ls

3.  Examine the output to understand the partition table of the
    &#96;/dev/sda&#96; device. The following example shows a DOS
    partition table with three partitions.

        (hd0) (hd0,msdos3) (hd0,msdos2) (hd0,msdos1)

    A GPT partition table of the &#96;/dev/sda&#96; device with four
    partitions could look like this.

        (hd0) (hd0,gpt4) (hd0,gpt3)  (hd0,gpt2) (hd0,gpt1)

4.  Probe each partition of the drive and locate your &#96;vmlinuz&#96;
    and &#96;initramfs&#96; files.

        grub\&gt; ls (hd0,1)/

    The outcome of the previous command will list the files on
    &#96;/dev/sda1&#96;. The partition that contains the &#96;/boot&#96;
    directory is the correct one. There you will search for the full
    names of the &#96;vmlinuz&#96; and &#96;initramfs&#96; files.

5.  Follow the &lt;&lt;btrfs-boot-setup, Pre-boot setup for
    BTRFS&gt;&gt; or the &lt;&lt;lvm-boot-setup, Pre-boot setup for
    LVM&gt;&gt; to recover your system.

6.  After the pre-boot setup, boot the system.

        grub\&gt; boot

7.  To restore the bootloader's functionality, regenerate the
    &#42;GRUB2&#42; configuration file and reinstall the bootloader, as
    described in [Adding other operating systems to the &#42;GRUB2&#42;
    menu](#adding-other-operating-systems-grub2).

</div>

### Pre-boot setup for BTRFS filesystems {#_pre_boot_setup_for_btrfs_filesystems}

&#42; On BIOS systems.

1.  Set &#42;GRUB2&#42; root to your &#96;/boot&#96; partition. If your
    &#96;/boot&#96; partition is &#96;(hd0,msdos1)&#96;, the command
    will be.

        grub\&gt; set root=(hd0,msdos1)

2.  Next, select the desired kernel. Set the &#96;/root&#96; partition
    (e.g. &#96;/dev/sda2&#96;).

        grub\&gt; linux /vmlinuz-5.14.10-300.fc35.x86_64 root=/dev/sda2 ro rootflags=subvol=root

    &#42; On UEFI systems.

3.  Set &#42;GRUB2&#42; root to your EFI system partition. If your EFI
    system partition is &#96;(hd0,gpt1)&#96;, use this command.

        grub\&gt; set root=(hd0,gpt1)

4.  Next, select the desired kernel. Find the path to &#96;vmlinuz&#96;
    and set the &#96;/root&#96; partition (e.g. &#96;/dev/sda3&#96;).

        grub\&gt; linux (hd0,gpt2)/vmlinuz-5.14.10-300.fc35.x86_64 root=/dev/sda3 ro rootflags=subvol=root

5.  Select the RAM filesystem that will be loaded.

        grub\&gt; initrd (hd0,gpt2)/initramfs-5.14.10-300.fc35.x86_64.img

### Pre-boot setup for LVM filesystems {#_pre_boot_setup_for_lvm_filesystems}

&#42; On BIOS systems.

1.  Set &#42;GRUB2&#42; root to your &#96;/boot&#96; partition. If your
    &#96;/boot&#96; partition is &#96;(hd0,msdos1)&#96;, use this
    command.

        grub\&gt; set root=(hd0,msdos1)

2.  Next, select the desired kernel. Set &#96;root&#96; to the logical
    volume that corresponds to the &#96;/root&#96; directory.

        grub\&gt; linux /vmlinuz-3.0.0-1.fc16.i686 root=/dev/mapper/fedora-root

3.  Select the RAM filesystem that will be loaded.

        grub\&gt; initrd /initramfs-3.0.0-1.fc16.i686.img

    &#42; On UEFI systems.

4.  Set &#42;GRUB2&#42; root to your EFI system partition. If your EFI
    system partition is &#96;(hd0,gpt1)&#96;, use this command.

        set root=(hd0,gpt1)

5.  Next, select the desired kernel. Find the path to &#96;vmlinuz&#96;
    and set &#96;root&#96; to the logical volume that corresponds to the
    &#96;/root&#96; directory.

        linux (hd0,gpt2)/vmlinuz-3.0.0-1.fc16.i686 root=/dev/mapper/fedora-root

6.  Select the RAM filesystem that will be loaded.

        initrd (hd0,gpt2)/initramfs-3.0.0-1.fc16.i686.img

## Booting the system using a configuration file on a different partition {#_booting_the_system_using_a_configuration_file_on_a_different_partition}

If you end up in &#42;GRUB2&#42; boot prompt, it is also possible to
boot using a *configfile* that's located on another partition, as is
often the case with multi-boot systems containing Ubuntu and Fedora.
Follow the below procedure if you need to boot from a configuration file
on a different partition.

<div>

::: title
Procedure
:::

1.  Load the necessary modules to read your system's partitions (you
    will also need to load &#96;part_msdos&#96; or &#96;part_gpt&#96;,
    depending on your partition table).

    &#42; For BTRFS filesystems.

        grub\&gt; insmod btrfs

    &#42; For LVM filesystems.

        grub\&gt; insmod xfs
        grub\&gt; insmod lvm

2.  Set &#42;GRUB2&#42; root to your &#96;/boot&#96; partition. On UEFI
    systems, you should set &#42;GRUB2&#42; root to the EFI system
    partition.

        grub\&gt; set root=(hd0,msdos1)

3.  Set the path to the configuration file.

        grub\&gt; configfile /grub2/grub.cfg

</div>

:::: formalpara
::: title
More information
:::

&#42; The &#42;hd0,msdos1&#42; line shows the pertinent &#96;/boot&#96;
partition, which holds the &#96;grub.cfg&#96; file. The setting may be
different on your system. See also [Using the GRUB2 boot
prompt](#_using_the_grub2_boot_prompt) for more information.
::::

## Setting a password for interactive edit mode {#_setting_a_password_for_interactive_edit_mode}

If you wish to protect the &#42;GRUB2&#42; interactive edit mode with a
password, but allow ordinary users to boot the computer, use the
&#96;grub2-set-password&#96; command. You will be prompted for the
password, and then will have to confirm it. The encrypted password will
be stored in /boot/grub2/user.cfg.

To remove password protection, simply delete the user.cfg file.

Alternately, you can set this up manually:

<div>

::: title
Procedure
:::

1.  Create the &#96;/etc/grub.d/01_users&#96; file and write the
    following lines into the file.

    ``` _bash
    cat \&lt;\&lt; EOF
    set superusers='root'
    export superusers
    password root \&lt;password\&gt;
    EOF
    ```

2.  Regenerate the &#42;GRUB2&#42; configuration file, as described in
    [Adding other operating systems to the &#42;GRUB2&#42;
    menu](#adding-other-operating-systems-grub2).

</div>

:::: formalpara
::: title
More information
:::

You can encrypt the password by using &#42;pbkdf2&#42;. Use
&#96;grub2-mkpasswd-pbkdf2&#96; to encrypt the password, then replace
the password line with:
::::

    password_pbkdf2 root grub.pbkdf2.sha512.10000.1B4BD9B60DE889A4C50AA9458C4044CBE129C9607B6231783F7E4E7191D8254C0732F4255178E2677BBE27D03186E44815EEFBAD82737D81C87F5D24313DDDE7.E9AEB53A46A16F30735E2558100D8340049A719474AEEE7E3F44C9C5201E2CA82221DCF2A12C39112A701292BF4AA071EB13E5EC8C8C84CC4B1A83304EA10F74

To remove password protection, simple remove the changes you made to the
&#96;/etc/grub.d/01_users&#96; file and regenerate the &#42;GRUB2&#42;
configuration file, as before.

More details can be found at [Ubuntu Help: GRUB2
Passwords](https://help.ubuntu.com/community/Grub2/Passwords).

:::: note
::: title
:::

Starting from Fedora 15, the
&#96;\--password=&lt;encrypted_grub_passwd&gt; \--iscrypted&#96;
kickstart option must be used if setting an encrypted &#42;GRUB2&#42;
password in the kickstart file.
::::

## Dealing with the \'Absent Floppy Disk\' Error {#_dealing_with_the_absent_floppy_disk_error}

It has been reported by some users that &#42;GRUB2&#42; may fail to
install on a partition's boot sector if the computer's floppy controller
is activated in BIOS without an actual floppy disk drive being present.
Such situations resulted in an *Absent Floppy Disk* error.

To workaround this issue, go into the rescue mode and follow the
procedure in [Installing GRUB2 on a BIOS
system](&#35;installing-grub-2-on-a-bios-system) &#42;GRUB2&#42;, but
use the &#96;\--no-floppy&#96; option with the &#96;grub2-install&#96;
command.

    \&#35; grub2-install \&lt;target device\&gt; --no-floppy

## Using old graphics modes in bootloader {#_using_old_graphics_modes_in_bootloader}

The terminal device is chosen with GRUB_TERMINAL. For more information,
see the [Grub
manual](https://www.gnu.org/software/grub/manual/grub/grub.html&#35;Simple-configuration).

Valid terminal output names depend on the platform, but may include
&#96;console&#96; (PC BIOS and EFI consoles), &#96;serial&#96; (serial
terminal), &#96;gfxterm&#96; (graphics-mode output), &#96;ofconsole&#96;
(Open Firmware console), or &#96;vga_text&#96; (VGA text output, mainly
useful with Coreboot).

The default is to use the platform's native terminal output.

In Fedora, &#96;gfxterm&#96; is the default options. To get the legacy
graphics modes:

<div>

::: title
Procedure
:::

1.  Edit the &#96;/etc/default/grub&#96; file.

2.  Set the &#96;GRUB_TERMINAL&#96; variable to one of the above
    mentioned options.

3.  Regenerate the &#42;GRUB2&#42; configuration file and reinstall the
    bootloader into the MBR, as described in [Adding other operating
    systems to the &#42;GRUB2&#42;
    menu](&#35;adding-other-operating-systems-grub2).

</div>

## Enabling Serial Console in GRUB2 {#_enabling_serial_console_in_grub2}

To enable Serial console in grub:

<div>

::: title
Procedure
:::

1.  Edit the &#96;/etc/default/grub&#96; file.

2.  Adjust &#96;baudrate&#96;, &#96;parity&#96;, &#96;bits&#96;, and
    &#96;flow&#96; controls to fit your environment and cables, see the
    example.

        GRUB_CMDLINE_LINUX='console=tty0 console=ttyS0,115200n8'
        GRUB_TERMINAL=serial
        GRUB_SERIAL_COMMAND='serial --speed=115200 --unit=0 --word=8 --parity=no --stop=1'

3.  Regenerate the &#42;GRUB2&#42; configuration file and reinstall the
    bootloader into the MBR, as described in [Adding other operating
    systems to the &#42;GRUB2&#42;
    menu](#adding-other-operating-systems-grub2).

</div>

**Additional resources**

&#42; <https://www.gnu.org/software/grub/manual/grub.html>

# How to create a Samba share {#_how_to_create_a_samba_share}

Alessio, Peter Lilley, Petr Bokoc

Samba allows for Windows and other clients to connect to file share
directories on Linux hosts. It implements the server message block (SMB)
protocol. This guide covers creating a shared file location on a Fedora
machine that can be accessed by other computers on the local network.

## Install and enable Samba {#install_and_enable_samba}

The following commands install Samba and set it to run via
&#96;systemctl&#96;. This also sets the firewall to allow access to
Samba from other computers.

&#8230;. sudo dnf install samba sudo systemctl enable smb \--now
firewall-cmd \--get-active-zones sudo firewall-cmd \--permanent
\--zone=FedoraWorkstation \--add-service=samba sudo firewall-cmd
\--reload &#8230;.

## Sharing a directory inside /home {#sharing_a_directory_inside_home}

In this example you will share a directory inside your home directory,
accessible only by your user.

Samba does not use the operating system users for authentication, so
your user account must be duplicated in Samba. So if your account is
&#96;jane&#96; on the host, the user &#96;jane&#96; must also be added
to Samba. While the usernames must match, the passwords can be
different.

Create a user called &#96;jane&#96; in Samba: &#8230;. sudo smbpasswd -a
jane &#8230;.

Create a directory to be the share for jane, and set the correct SELinux
context: &#8230;. mkdir /home/jane/share sudo semanage fcontext \--add
\--type \'samba_share_t\' \'/home/jane/share(/.&#42;)?\' sudo restorecon
-R \~/share &#8230;.

Samba configuration lives in the &#96;/etc/samba/smb.conf&#96; file.
Adding the following section at the end of the file will instruct Samba
to set up a share for jane called \'share\' at the
&#96;/home/jane/share&#96; directory just created. &#8230;.

comment = My Share path = /home/jane/share writeable = yes browseable =
yes public = yes create mask = 0644 directory mask = 0755 write list =
user &#8230;.

Restart Samba for the changes to take effect:

&#8230;. sudo systemctl restart smb &#8230;.

## Sharing a directory for many users {#sharing_a_directory_for_many_users}

In this example, you will share a directory (outside your home
directory) and create a group of users with the ability to read and
write to the share.

Remember that a Samba user must also be a system user, in order to
respect filesystem permissions. This example creates a system group
&#96;myfamily&#96; for two new users &#96;jack&#96; and &#96;maria&#96;.
&#8230;. sudo groupadd myfamily sudo useradd -G myfamily jack sudo
useradd -G myfamily maria &#8230;.

:::: tip
::: title
:::

You could create these users without a system password. This would
prevent access to the system via SSH or local login.
::::

Add &#96;jack&#96; and &#96;maria&#96; to Samba and create their
passwords:

&#8230;. sudo smbpasswd -a jack sudo smbpasswd -a maria &#8230;.

Setting up the shared folder: &#8230;. sudo mkdir /home/share sudo chgrp
myfamily /home/share sudo chmod 770 /home/share sudo semanage fcontext
\--add \--type \'samba_share_t\' \'/home/share(/.&#42;)?\' sudo
restorecon -R /home/share &#8230;.

Each share is described by its own section in the
&#96;/etc/samba/smb.conf&#96; file. Add this section to the bottom of
the file: &#8230;.

comment = Family Share path = /home/share writeable = yes browseable =
yes public = yes valid users = \@myfamily create mask = 0660 directory
mask = 0770 force group = +myfamily &#8230;.

Explanation of the above:

&#42; &#96;valid users&#96;: only users of the group &#96;family&#96;
have access rights. The @ denotes a group name. &#42; &#96;force group =
+myfamily&#96;: files and directories are created with this group,
instead of the user group. &#42; &#96;create mask = 0660&#96;: files in
the share are created with permissions to allow all group users to read
and write files created by other users. &#42; &#96;directory mask =
0770&#96;: as before, but for directories.

Restart Samba for the changes to take effect:

&#8230;. sudo systemctl restart smb &#8230;.

## Managing Samba Users {#managing_samba_users}

### Change a samba user password {#change_a_samba_user_password}

:::: tip
::: title
:::

Remember: the system user and Samba user passwords can be different. The
system user is needed in order to handle filesystem permissions.
::::

&#8230;. sudo smbpasswd maria &#8230;.

### Remove a samba user {#remove_a_samba_user}

&#8230;. sudo smbpasswd -x maria &#8230;.

If you don't need the system user, remove it as well:

&#8230;. sudo userdel -r maria &#8230;.

## Troubleshooting and logs {#troubleshooting_and_logs}

Samba log files are located in &#96;/var/log/samba/&#96;

&#8230;. tail -f /var/log/samba/log.smbd &#8230;.

You can increase the verbosity by adding this to the
&#96;\[global\]&#96; section of &#96;/etc/samba/smb.conf&#96;:

&#8230;.

loglevel = 5 &#8230;.

To validate the syntax of the configuration file
&#96;/etc/samba/smb.conf&#96; use the command &#96;testparm&#96;.
Example output:

&#8230;. Load smb config files from /etc/samba/smb.conf Loaded services
file OK. Server role: ROLE_STANDALONE &#8230;.

To display current samba connections, use the &#96;smbstatus&#96;
command. Example output:

&#8230;. Samba version 4.12.3 PID Username Group Machine Protocol
Version Encryption Signing

    7259    jack         jack         192.168.122.1 (ipv4:192.168.122.1:40148)  SMB3_11           -                    partial(AES-128-CMAC)

    Service      pid     Machine       Connected at                     Encryption   Signing
    ---------------------------------------------------------------------------------------------
    family       7259    192.168.122.1 Fri May 29 14:03:26 2020 AEST    -            -

    No locked files
    \&#8230;.

    [[trouble_with_accessing_the_share]]
    === Trouble with accessing the share

    Some things to check if you cannot access the share.

    . Be sure that the user exists as a system user as well as a Samba user
    +
    Find \&#96;maria\&#96; in the Samba database:
    +
    \&#8230;.
    sudo pdbedit -L | grep maria

    maria:1002:
    \&#8230;.
    +
    Confirm that \&#96;maria\&#96; also exists as a system user.
    +
    \&#8230;.
    cat /etc/passwd | grep maria

    maria:x:1002:1002::/home/maria:/bin/bash
    \&#8230;.
    +
    . Check if the shared directory and sub-directories have the correct SELinux context.
    +
    \&#8230;.
    ls -dZ /home/share

    unconfined_u:object_r:samba_share_t:s0 /home/share
    \&#8230;.
    +
    . Check if the system user has access permission to the shared directory.
    +
    \&#8230;.
    ls -ld /home/share

    drwxrwx---. 2 root myfamily 4096 May 29 14:03 /home/share
    \&#8230;.
    +
    In this case, the user should be in the \&#96;myfamily\&#96; group.

    . Check in the configuration file \&#96;/etc/samba/smb.conf\&#96; that the user and group have access permission.
    +
    \&#8230;.
    [family]
    comment = Family Share
    path = /home/share
    writeable = yes
    browseable = yes
    public = yes
    valid users = @myfamily
    create mask = 0660
    directory mask = 0770
    force group = +myfamily
    \&#8230;.
    +
    In this case, the user should be in the \&#96;myfamily\&#96; group.

    [[trouble_with_writing_in_the_share]]
    === Trouble with writing in the share

    . Check in the samba configuration file if the user/group has write permissions.
    +
    \&#8230;.
    [family]
    comment = Family Share
    path = /home/share
    writeable = yes
    browseable = yes
    public = yes
    valid users = @myfamily
    create mask = 0660
    directory mask = 0770
    force group = +myfamily
    \&#8230;.
    +
    In this example, the user should be in the \&#96;myfamily\&#96; group.

    . Check the share directory permissions.
    +
    \&#8230;.
    ls -ld /home/share

    drwxrwx---. 2 root myfamily 4096 May 29 14:03 /home/share
    \&#8230;.
    +
    This example assumes the user is part of the \&#96;myfamily\&#96; group which has read, write, and execute permissions for the folder.


    = Joining an Active Directory or FreeIPA domain
    Oliver Gutierrez

    // Optional  free form useful additional information as comment


    Fedora can join Active Directory and FreeIPA domains using the \&#96;realm\&#96; command.

    If you want your Fedora machine to be part of an Active directory or FreeIPA domain just follow this steps

    . Gather needed information

    \&#42; If your network is not configured to automatically setup the DNS to the domain DNS, you will need the domain DNS IP address.
    \&#42; You will need to provide the credentials of a domain user with permissions to join new machines to the domain.


    . Configure the DNS to use the Active Directory or FreeIPA domain DNS servers (if your network uses DHCP to set this DNS to the correct server, skip this step)
    You can do this editing the network settings using the GNOME configuration panel or you can edit directly the file \&#96;/etc/systemd/resolved.conf\&#96; and add your DNS manually.
    +
    \&#8230;.
    [Resolve]
    DNS=192.168.122.143 172.17.0.2 1.0.0.1
    \&#8230;.

    . After saving the file, restart \&#96;systemd-resolved\&#96; service.
    +
    \&#8230;.
    $ sudo systemctl restart systemd-resolved
    \&#8230;.

    . Change the machine name to the machine name you want + the domain name.
    +
    \&#8230;.
    $ sudo hostnamectl set-hostname my_machine.example.domain
    \&#8230;.

    . Use the \&#96;realm\&#96; command to join the machine to the domain.
    +
    \&#8230;.
    $ sudo realm join example.domain -v
    \&#8230;.

    . After the command finished the machine should be part of the Active Directory or FreeIPA domain


    = How to Set Nvidia as Primary GPU on Optimus-based Laptops
    Akashdeep Dhar ; Jun Aruga ; Ankur Sinha;
    :page-aliases: how-to-set-nvidia-as-primary-gpu-on-optimus-based-laptops.adoc

    //:imagesdir: ./images




    == Introduction
    The goal is to have an active NVIDIA GPU on an Optimus-based laptop and use it for all activities on Desktops Environments with Xorg-X11.
    Avoid using this guide if you prefer to render your desktop with the integrated GPU and selectively choose applications to utilize the NVIDIA GPU.

    [NOTE]
    ====
    The instructions in this document have been verified to work on releases of Fedora 32 Workstation and later versions that use Xorg-X11.

    Some guides on the internet recommend a different approach to installing Nvidia drivers on Fedora, such as directly using the binaries provided by Nvidia. However, the Fedora Project cannot guarantee that these will always function with every Fedora release. Therefore, we recommend following the steps outlined in this document instead.

    As of Fedora 34, Wayland has become the default display server on Fedora Workstation for GNOME desktop environments. To follow the steps provided in this guide, you must be logged in to a session that runs on Xorg-X11.


    ====

    [WARNING]
    ====
    This guide requires the secure boot to be \&#42;\&#42;turned off\&#42;\&#42; to load up the unsigned NVIDIA kernel modules.
    ====

    To make all rendering default to the NVIDIA GPU, you need to follow these steps very carefully.

    First, consider the following points:

    \&#42; Why would you want to do this?

    Using the NVIDIA GPU all the time allows for smoother transitions and richer animation effects. Premium desktop environments like GNOME benefit greatly from this.
    Enabling the NVIDIA GPU all the time leads to lower CPU load and memory consumption, which would otherwise be high due to the added in-memory video buffer.

    \&#42; Why might this not be ideal?

    Using the NVIDIA GPU all the time can cause a slight increase in battery consumption. This shouldn't be a concern if your device is plugged in while in use.
    The increased heat generation from the constantly enabled NVIDIA GPU might be a concern. You wouldn't want to play demanding games (AAA titles) on Proton while using your laptop on your lap.

    == Step \&#35;1: Update from the existing repositories
    Execute
    ----
    sudo dnf upgrade
    ----
    Once to update all your packages first.

    image:how-to-set-nvidia-as-primary-gpu-on-optimus-based-laptops-0.png[]

    == Step \&#35;2: Add the RPMFusion repository for NVIDIA drivers
    Then you need to add the \&#42;RPM Fusion repository for NVIDIA drivers\&#42;. To do that, open up \&#42;GNOME Software\&#42; and click on the \&#42;hamburger menu\&#42; (three horizontal lines) on the top-right corner. Then click on \&#42;Software Repositories\&#42; from the dropdown menu. There you will see this.

    image:how-to-set-nvidia-as-primary-gpu-on-optimus-based-laptops-1.png[]

    Select \&#42;RPM Fusion for Fedora 32 - Nonfree - NVIDIA Driver\&#42; and \&#42;ENABLE\&#42; it. It requires elevated privileges so enter your password and it will be done.

    == Step \&#35;3: Update from the newly added repositories
    Execute
    ----
    sudo dnf upgrade --refresh
    ----
    to fetch all available updates from the newly added repository.

    image:how-to-set-nvidia-as-primary-gpu-on-optimus-based-laptops-2.png[]

    == Step \&#35;4: Install the driver and its dependencies
    Execute
    ----
    sudo dnf install gcc kernel-headers kernel-devel akmod-nvidia xorg-x11-drv-nvidia xorg-x11-drv-nvidia-libs xorg-x11-drv-nvidia-libs.i686
    ----
    to get the driver and all necessary dependencies.

    image:how-to-set-nvidia-as-primary-gpu-on-optimus-based-laptops-3.png[]

    == Step \&#35;5: Wait for the kernel modules to load up
    You \&#42;\&#42;must\&#42;\&#42; wait 5-10 minutes for the kernel modules to load. Please do not proceed to the next steps immediately.

    == Step \&#35;6: Read from the updated kernel modules
    Execute
    ----
    sudo akmods --force
    sudo dracut --force
    ----
    This would force the configuration to be read from the updated kernel modules which now have the NVIDIA drivers in them.

    == Step \&#35;7: Reboot your system
    Wait for 3-5 minutes for the changes to take effect and then reboot your system.

    Log in to a session with Xorg-X11.

    From the desktop, go to the \&#42;About\&#42; page in the \&#42;Settings\&#42; application. You are likely to see the following output.

    image:how-to-set-nvidia-as-primary-gpu-on-optimus-based-laptops-4.png[]

    This means that the driver installation was successful leading to the detection of two distinct video accelerators - internal and dedicated.

    == Step \&#35;8: Edit the X11 configuration
    Please ensure that the [application]\&#96;xrandr\&#96; package is installed before proceeding with this step:

    ----
    sudo dnf install xrandr
    ----

    Execute the following command to copy the display render details for the X11.

    ----
    sudo cp -p /usr/share/X11/xorg.conf.d/nvidia.conf /etc/X11/xorg.conf.d/nvidia.conf
    ----

    Once done, open up the \&#96;nvidia.conf\&#96; from the copy destination and edit it to add
    ----
    Option 'PrimaryGPU' 'yes'
    ----
    to the \&#96;OutputClass\&#96; section of it.

    For example, use \&#96;nano\&#96;
    ----
    sudo nano /etc/X11/xorg.conf.d/nvidia.conf
    ----
    and make changes.

    The file should look like this. Your file should look similar to this.

    image:how-to-set-nvidia-as-primary-gpu-on-optimus-based-laptops-5.png[]

    You can see the additions in both sections.

    Save it using \&#96;[Ctrl]+[S]\&#96; and exit out using \&#96;[Ctrl]+[X]\&#96;.

    NOTE: If you are using a display manager other than GDM (the default of Fedora Workstation), you will need to configure it appropriately. Please refer https://wiki.archlinux.org/index.php/NVIDIA_Optimus\&#35;Display_managers[to the Arch wiki for instructions]. For SDDM (the KDE spin default) on Fedora32, the Arch wiki is _wrong_, and you need to edit the \&#96;/etc/sddm/Xsetup\&#96; file, _not_ \&#96;/usr/share/sddm/scripts/Xsetup\&#96;.

    == Step \&#35;9: Reboot your system
    Reboot your system and proceed to the next steps to verify the change in configuration.

    == Step \&#35;10: Verify the configuration
    Open a terminal and type in
    ----
    glxinfo | egrep 'OpenGL vendor|OpenGL renderer'
    ----
    It should show your NVIDIA GPU.

    image:how-to-set-nvidia-as-primary-gpu-on-optimus-based-laptops-6.png[]

    Check on \&#96;screenfetch\&#96;.
    ----
    screenfetch
    ----
    It should show your NVIDIA GPU under the GPU name.

    image:how-to-set-nvidia-as-primary-gpu-on-optimus-based-laptops-7.png[]

    Check in your \&#42;Settings\&#42; application.
    You would see something like this in the \&#42;About\&#42; page.

    image:how-to-set-nvidia-as-primary-gpu-on-optimus-based-laptops-8.png[]

    You can make other configuration changes using \&#42;NVIDIA X Server Settings\&#42; application.
    Also the GPU would show activity in its utilization percentage to signify that it is actually working.

    image:how-to-set-nvidia-as-primary-gpu-on-optimus-based-laptops-9.png[]

    == References
    Should you face issues while following these steps or if these do not match your use case,
    feel free to convey your queries on https://ask.fedoraproject.org[Fedora Forums].

    Here are the links you can refer to for obtaining more information.

    \&#42; https://rpmfusion.org/Howto/Optimus[RPMFusion's Optimus How-to guide]
    \&#42; https://rpmfusion.org/Howto/NVIDIA[RPMFusion's NVIDIA How-to guide]
    \&#42; https://unix.stackexchange.com/questions/16407/how-to-check-which-gpu-is-active-in-linux[GPU Activity on UNIX StackExchange]
    \&#42; https://www.reddit.com/r/Fedora/comments/bw4b0p/how_to_fedora_nvidia_prime/[Fedora Subreddit (zvitaly’s response only)]


    = How to debug systemd problems
    Caleb McKee; Petr Bokoc; Peter Boy

    If you are experiencing a problem with system boot-up due to xref:understanding-and-administering-systemd.adoc[systemd], please see the link:Bugs/Common[commonbugs] document before filing a bug. Some easy configuration tweaks that fix a wide range of issues may be listed there. If the problem you are seeing is not listed there or none of the workarounds seem to help, please consider filing a bug to help us make Fedora run better on your hardware.

    [TIP]
    ====
    Have a look at the upstream project's  link:http://freedesktop.org/wiki/Software/systemd/Debugging[helpful documentation] on the topic.
    ====



    [[various-useful-systemd-related-commands]]
    == Various useful systemd related commands

    \&#42; List all jobs that are 'running' or 'waiting'. This command can be used to identify causes of a slow boot. The boot process waits for 'running' jobs to complete. Jobs listed as 'waiting' will only be executed after 'running' jobs have completed.
    +
    [source,bash]
    ----
    […]\&#35; systemctl list-jobs
    ----

    \&#42; List all available services and their current status
    +
    [source,bash]
    ----
    […]\&#35; systemctl list-units -t service --all
    ----


    \&#42; Show all active services
    +
    [source,bash]
    ----
    […]\&#35; systemctl list-units -t service
    ----


    \&#42; Examine the current runtime status of a service. (In this example the ssh service)
    +
    [source,bash]
    ----
    […]\&#35; systemctl status sshd.service
    ----


    \&#42; Show all available targets.
    +
    [source,bash]
    ----
    […]\&#35; systemctl list-units -t target --all
    ----


    \&#42; Show all active targets.
    +
    [source,bash]
    ----
    […]\&#35; systemctl list-units -t target
    ----


    \&#42; Display which services a target pulls in. ( In this example the
    multi-user.target )
    +
    [source,bash]
    ----
    […]\&#35; systemctl show -p 'Wants' multi-user.target
    ----


    \&#42; Examine what gets started when booted into a specific target. (in this example the multi-user.target)
    +
    [source,bash]
    ----
    […]\&#35; /usr/lib/systemd/systemd --test --system --unit=multi-user.target
    ----


    [[systemd-boot-parameters]]
    == Various useful systemd boot parameters

    The following boot parameters are also available to further assist with
    debugging boot issues.

    systemd.unit=:: Overrides the unit to activate on boot. This may be used to temporarily boot into a different boot unit, for example \&#96;rescue.target\&#96; or \&#96;emergency.target\&#96;. Defaults to \&#96;default.target\&#96;.

    systemd.dump_core=:: Takes a boolean argument. If true, systemd dumps the core when it crashes. Otherwise no core dump is created. Defaults to true.

    systemd.crash_shell=:: Takes a boolean argument. If true, systemd spawns a shell when it crashes. Otherwise no core dump is created. Defaults to false, for security reasons, as the shell is not protected by any password authentication.

    systemd.crash_chvt=:: Takes an integer argument. If positive, systemd activates the specified virtual terminal when it crashes. Defaults to -1.

    systemd.confirm_spawn=:: Takes a boolean argument. If true, asks for confirmation when spawning processes. Defaults to false.

    systemd.show_status=:: Takes a boolean argument. If true, shows terse service status updates on the console during bootup. Defaults to true.

    systemd.sysv_console=::  Takes a boolean argument. If true, output of SysV init scripts will be directed to the console. Defaults to true, unless quiet is passed as kernel command line option in which case it defaults to false.

    systemd.log_target=:: Sets the log target. Argument must be console, syslog, kmsg, yslog-or-kmsg, or null.

    systemd.log_level=::  Sets the log level. This command accepts a numerical log level or the well-known syslog symbolic names (lowercase): emerg, alert, crit, err, warning, notice, info, debug as an argument.

    systemd.log_color=:: Highlights important log messages. Argument is a boolean value. If the argument is omitted, it defaults to true.

    systemd.log_location=:: Includes code location in log messages. This is mostly relevant for debugging purposes. Argument is a boolean value. If the argument is omitted it defaults to true.


    See a typo, something missing or out of date, or anything else which can be improved? Edit this document or provide a comment using the buttons above on the right side below the blue header banner.


    = How to enable touchpad click
    Ankur Sinha; Caleb McKee; Petr Bokoc


    [[scope]]
    == Scope

    Fedora tries to make various desktop environments available to its users. Since Fedora tries to link:https://docs.fedoraproject.org/en-US/package-maintainers/Staying_Close_to_Upstream_Projects/[stay as close to upstream as possible], we follow the various defaults selected by the desktop environment upstreams. Generally, this entails a disabled touchpad click by default. This wiki page tries to compile the different methods that can be used to enable 'tapping' on various desktop environments.

    [NOTE]
    ====
    Please note that this is only a resource to aid our users. For discussions on this setting, please talk to the relevant DE upstream. Fedora does not intend to make any changes to upstream defaults.
    ====


    [[desktop-configurations]]
    == Desktop configurations

    This wiki page has more information about link:https://fedoraproject.org/wiki/Input_device_configuration[Input Device configuration]. An example \&#96;xorg.conf.d\&#96; snippet to enable tapping is given link:https://fedoraproject.org/wiki/Input_device_configuration\&#35;Example:_Tap-to-click[here].

    [[gnome]]
    === GNOME

    The '_mouse and touchpad_' utility can be used to enable tapping and set scrolling options in GNOME. See the link:http://library.gnome.org/users/gnome-help/stable/mouse-touchpad-click.html.en[Official GNOME documentation]


    [[kde-plasma-workspaces]]
    === KDE Plasma Workspaces

    1. Enter KDE System Settings
    2. Choose Hardware \&gt; Input Devices \&gt; Touchpad (If the 'Touchpad' setting is not there, install kcm_touchpad first, then restart System Settings. It is installed by default.)
    3. Select the Tapping tab
    4. Check the 'Tap to click' checkbox
    5. Set some tapping actions under 'Buttons' below, the default is to do
    nothing

    Alternatively, the systemwide method described under link:https://fedoraproject.org/wiki/How_to_enable_touchpad_click\&#35;Other_window_managers[Other window managers] can also be used.

    // link:\&#35;Other_window_managers[Other window managers] can also be used.

    [[xfce]]
    === Xfce

    1.  Enter Xfce Settings
    2.  Select the Mouse and Touchpad settings
    3.  If necessary, select your Touchpad device
    4.  In the General section, enable 'Tap touchpad to click'

    [[other-window-managers]]
    === Other window managers

    Create a new file named \&#96;/etc/X11/xorg.conf.d/99-synaptics-overrides.conf\&#96;.

    Then, in your favourite text editor, modify this file as such:

    \&#8230;.
    Section  'InputClass'
    Identifier  'touchpad overrides'
    \&#35; This makes this snippet apply to any device with the 'synaptics' driver
    \&#35; assigned
    MatchDriver  'synaptics'

    \&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;
    \&#35;\&#35; The lines that you need to add \&#35;\&#35;
    \&#35; Enable left mouse button by tapping
    Option  'TapButton1'  '1'
    \&#35; Enable vertical scrolling
    Option  'VertEdgeScroll'  '1'
    \&#35; Enable right mouse button by tapping lower right corner
    Option 'RBCornerButton' '3'
    \&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;\&#35;

    EndSection
    \&#8230;.

    For more information on tweaking \&#96;xorg.conf.d\&#96; files, please read the man page:
    [source,bash]
    […]$ man xorg.conf




    = Installing and Running VLC
    Lyle Corman ; Ankur Sinha
    //:page-aliases:
    :experimental:
    //:imagesdir: ./images


    == Installing VLC


    \&#42; Install VLC:
    +
    [source,]
    ----
    $ sudo dnf install vlc
    ----



    == Running VLC

    \&#42; To run the VLC media player using GUI:
    +
    --
    . Open the launcher by pressing the _Super_ key.
    . Type _vlc_.
    . Press _Enter_.
    --


    \&#42; To run VLC from the command line:
    +
    [subs='quotes']
    ----
    $ vlc _source_
    ----
    +
    Replace _source_ with path to the file to be played, URL, or other data source. For more details, see link:https://wiki.videolan.org/Documentation:Command_line/\&#35;Opening_streams[Opening streams] on VideoLAN wiki.



    = Installing Docker and Docker-Compose
    Bradley G Smith,

    // Optional  free form useful additional information as comment

    //include::{partialsdir}/3rdparty-message.adoc[]
    ////

    This message needs to be included on any document referencing third party software
    repositories. Add the following line verbatim to the top of any such document:


    Please do not change this message without consultation. Thanks!

    ////

    [CAUTION]
    ====
    This page discusses third-party software sources not officially affiliated with or endorsed by the Fedora Project.
    Use them at your own discretion.
    Fedora recommends the use of free and open source software and avoidance of software encumbered by patents.
    ====



    [[sect-overview]]
    == Overview

    This guide provides useful information about installing link:https://www.docker.com/[Docker] and Docker-Compose using rpms available from Fedora.
    The role of Podman and related packages is also discussed.

    The Docker community also provides rpms for Fedora. For instructions on how to install these rpms please see link:https://docs.docker.com/engine/install/fedora/[Install Docker Engine on Fedora].

    [[sect-what-is-docker]]
    === What is Docker?

    link:https:/docker.io[Docker] accelerates 'how you build, share, and run applications' by providing an easy to use and configure mechanism to develop and run containers.

    This guide is primarily  focused on the Docker rpms available from Fedora and using \&#96;dnf\&#96; and the command line to install these rpms on Fedora.

    [[sect-what-is-docker-compose]]
    === What is Docker-Compose?

    link:https://docs.docker.com/compose/[Docker-Compose] (referred to as Compose below) is software that enables users to easily manage multi-container applications or multiple applications on a single instance of Docker.

    Version 1 of Compose was deployed as a stand-alone application called \&#96;docker-compose\&#96;.
    Version 2 (the current version) is available as a plug-in to the \&#96;docker\&#96; command and launched as \&#96;docker compose [options]\&#96;.

    [[sect-fedora-41]]
    == Docker on Fedora 41 (and newer)

    The Docker related rpms in Fedora 41 and newer are listed in the table below.
    The corresponding rpm names from the Docker community are also listed for comparison.
    Mixing rpms from Docker with Fedora provided rpms is not recommended and may be blocked by \&#96;dnf\&#96;.

    .Docker rpms in Fedora 41 (and newer) compared to rpms from Docker community.
    [cols='1,1,1',_options='header']
    |===
    |Fedora RPM Name|Docker RPM Name|Notes

    |containerd
    |containerd
    |Container runtime

    |docker-buildx
    |docker-buildx-plugin
    |Docker buildx plug-in

    |docker-cli
    |docker-ce-cli
    |Docker command line client, i.e. \&#96;docker\&#96;

    |docker-compose
    |docker-compose-plugin
    |Compose v2 implemented as a plug-in

    |docker-compose-switch
    |n/a - See link:https://github.com/docker/compose-switch[compose-switch] for installation instructions
    |Provides command line \&#96;docker-compose\&#96; that works with Compose v2

    |moby-engine
    |docker-ce
    |Server component for Docker
    |===

    === Installation

    In order to get \&#96;docker\&#96; on the command line, use the command below.
    This will also install appropriate dependencies.

    [source,bash]
    ----
    sudo dnf install docker-cli containerd
    ----

    In order to get Compose as a plug-in use the command below.
    This will also install appropriate dependencies.
    This provides Compose v2 features and capabilities.

    [source,bash]
    ----
    sudo dnf install docker-compose
    ----

    In order to get \&#96;docker-compose\&#96; on the command line, use the command below.
    This will also install appropriate dependencies.
    This provides Compose v2 features and capabilities.

    [source,bash]
    ----
    sudo dnf install docker-compose-switch
    ----

    === Podman Alternatives

    link:https://podman.io/[Podman] is a powerful and feature complete application that can be used instead of Docker.
    The instructions below are limited to only those that provide the \&#96;docker\&#96; and/or \&#96;docker-compose\&#96; commands.
    Please visit link:https://podman.io/[Podman] to learn more about Podman capabilities and benefits.

    In order to get \&#96;docker\&#96; on the command line, use the command below.
    This will also install appropriate dependencies.
    This will conflict with \&#96;docker-cli\&#96;.

    [source,bash]
    ----
    sudo dnf install podman-docker
    ----

    In order to get Compose as a plug-in use the command below.
    This will also install appropriate dependencies.
    This provides Compose v2 features and capabilities.

    [source,bash]
    ----
    sudo dnf install podman docker-compose
    ----

    In order to get \&#96;docker-compose\&#96; on the command line, use the command below.
    This will also install appropriate dependencies.
    This provides Compose v2 features and capabilities.

    [source,bash]
    ----
    sudo dnf install podman docker-switch
    ----

    [[sect-fedora-40]]
    == Docker on Fedora 40

    The Docker related rpms in Fedora 40 are listed in the table below.
    The corresponding rpm names from the Docker community are also listed for comparison.
    Mixing rpms from Docker with Fedora provided rpms is not recommended and may be blocked by \&#96;dnf\&#96;.

    .Docker rpms in Fedora 40 compared to rpms from Docker community.
    [cols='1,1,1',_options='header']
    |===
    |Fedora RPM Name|Docker RPM Name|Notes

    |containerd
    |containerd
    |Container runtime

    |n/a
    |docker-buildx-plugin
    |Docker buildx plug-in

    |moby-engine
    |docker-ce-cli
    |Docker command line client, i.e. \&#96;docker\&#96;

    |docker-compose
    |docker-compose
    |Compose v1

    |moby-engine
    |docker-ce
    |Server component for Docker
    |===

    === Installation

    In order to get \&#96;docker\&#96; on the command line, use the command below.
    This will also install appropriate dependencies.

    [source,bash]
    ----
    sudo dnf install moby-engine containerd
    ----

    In order to get \&#96;docker-compose\&#96; on the command line, use the command below.
    This will also install appropriate dependencies.
    This provides Compose v1 features and capabilities.

    [source,bash]
    ----
    sudo dnf install docker-compose
    ----

    === Podman Alternatives

    link:https://podman.io/[Podman] is a powerful and feature complete application that can be used instead of Docker.
    The instructions below are limited to only those that provide the \&#96;docker\&#96; and/or \&#96;docker-compose\&#96; commands.
    Please visit link:https://podman.io/[Podman] to learn more about Podman capabilities and benefits.

    In order to get \&#96;docker\&#96; on the command line, use the command below.
    This will also install appropriate dependencies.
    This will conflict with \&#96;docker-cli\&#96;.

    [source,bash]
    ----
    sudo dnf install podman-docker
    ----

    In order to get \&#96;docker-compose\&#96; on the command line, use the command below.
    This will also install appropriate dependencies.
    This provides Compose v1 features and capabilities.

    [source,bash]
    ----
    sudo dnf install podman docker-compose
    ----


    = Jitsi Meet Self-Hosting Guide
    quiet
    // :page-aliases:
    // :experimental:


    [WARNING]
    ====
    This documentation hasn't been updated in a while. Some information might no longer be valid. You can find the latest version of the upstream documentation at https://jitsi.github.io/handbook/docs/devops-guide/
    ====


    Jitsi video conferencing stack enables users to create virtual meetings, conferences, and collaboration sessions among other notable use-cases. Jitsi video conferencing stack provides:

    \&#42; Jitsi Meet (\&#96;jitsi-meet\&#96;): a web-based client application used by conference participants

    \&#42; Jitsi Videobridge (\&#96;jitsi-videobridge\&#96;): a server-side component of the Jitsi stack. Acts as a central hub for video conferences, where participants can join by accessing a uniquely generated conference URL from the server. Jitsi Videobridge conducts negotiation of audio and video streams between conference participants and also provides the necessary infrastructure for seamless experience.

    \&#42; Webserver configurations (\&#96;jitsi-meet-nginx\&#96;) and (\&#96;jitsi-meet-apache\&#96;): components that help serve the Jitsi Meet web client to handle incoming HTTPS requests.

    \&#42; Configuration for Prosody (\&#96;jitsi-meet-prosody\&#96;): a server-side component providing user authentication and management, conference room management. Ensures secure communication within Jitsi video conferencing stack.

    \&#42; Jicofo (\&#96;jicofo\&#96;): a server-side component for conference management, participant control and media routing.


    == Installing Jitsi


    The installation instructions are similar to the official Debian/Ubuntu instructions. Notable differences are:

    \&#42; Slightly different file locations
    \&#42; The \&#96;Jicofo\&#96; and \&#96;Jitsi Videobridge\&#96; components log to \&#96;syslog\&#96; instead of to their own logfiles.
    \&#42; The \&#96;Jicofo\&#96; component runs from a service, not from an \&#96;init\&#96; script.

    .Prerequisites

    \&#42; Small server, which is accessible from the Internet
    \&#42; Domain name and an SSL certificate for that domain


    .Procedure

    . Enable the \&#96;jitsi\&#96; repository:
    +
    ----
    $ sudo dnf copr enable lcts/jitsi
    ----


    . Install the \&#96;jitsi\&#96; meta package to be able to configure a Jitsi server:
    +
    ----
    $ sudo dnf install jitsi
    ----
    +
    Alternatively, you can install other packages from the \&#96;jitsi\&#96; repository:
    +
    \&#42; \&#96;jitsi-meet\&#96; - the Jitsi Meet web app
    \&#42; \&#96;jitsi-meet-nginx\&#96; - Jitsi configuration for NGinx
    \&#42; \&#96;jitsi-meet-apache\&#96; -Jitsi configuration for Apache
    \&#42; \&#96;jitsi-meet-prosody\&#96; - Jitsi configuration for Prosody
    \&#42; \&#96;jitsi-videobridge\&#96; - the Jitsi Videobridge component
    \&#42; \&#96;jicofo\&#96; - the Jitsi Conference Focus component


    .Additional resources

    \&#42; After installation, you need to configure all packages before you use them. For more information, see the \&#96;/usr/share/doc/\&lt;package\&gt;/README-fedora.md\&#96; file.

    \&#42; You can report issues with packages at link:https://pagure.io/jitsi-rpm/issues[jitsi-rpm queue].
    +
    [IMPORTANT]
    ====
    If you encounter problems with software, contact the respective upstream developers.
    ====

    == Configuring Jitsi

    After installation, you need to perform a few additional configuration steps. The steps consist of replacing various placeholder variables with your values to ensure that Jitsi is correctly configured to work in your specific deployment. The placeholders are identified by underscores for example \&#96;\___variableName___\&#96;.

    In all files, replace \&#96;\___jitsiFQDN___\&#96; with the fully-qualified domain name of your instance and \&#96;\____\&lt;component\&gt;Secret__\&#96; with a strong random password. You need three secrets:

    \&#42; \&#96;\___focusSecret___\&#96;
    \&#42; \&#96;\___focusUserSecret___\&#96;
    \&#42; \&#96;\___jvbUserSecret___\&#96;

    You do not need to memorize the secrets. They are only used by different Jitsi components to communicate to each other.


    === Configuring Jitsi Prosody

    You can find Prosody configuration for Jitsi in the \&#96;/etc/prosody/conf.d/jitsi-meet.cfg.lua\&#96; file.


    .Procedure

    . Generate the SSL/TLS certificate for the Jitsi domain:
    +
    ----
    $ prosodyctl cert generate __jitsiFQDN__
    ----
    +
    You need to replace \&#96;\___jitsiFQDN___\&#96; with the actual domain name of your Jitsi installation. The generated certificate secures the Jitsi Meet web interface and enables encrypted communication.


    . Generate the SSL/TLS certificate for the auth subdomain:
    +
    ----
    $ prosodyctl cert generate auth.__jitsiFQDN__
    ----
    +
    The \&#96;auth\&#96; subdomain is typically used for authentication purposes in Jitsi Meet. Replace \&#96;\___jitsiFQDN___\&#96; with your Jitsi domain name to generate the certificate for the auth subdomain.


    . Add the Jitsi domain certificate as a trusted anchor to ensure that it is recognized as a valid certificate by the system:
    +
    ----
    $ trust anchor /var/lib/prosody/__jitsiFQDN__
    ----
    +
    The certificate file is typically located at \&#96;/var/lib/prosody/\___jitsiFQDN___\&#96;. Therefore you need to replace \&#96;\___jitsiFQDN___\&#96; with the actual domain name to specify the correct file path.


    . Add the auth subdomain certificate as a trusted anchor:
    +
    ----
    $ trust anchor /var/lib/prosody/auth.__jitsiFQDN__
    ----
    +
    The certificate file is expected to be located at \&#96;/var/lib/prosody/auth.\___jitsiFQDN___\&#96;. Replace \&#96;\___jitsiFQDN___\&#96; with your Jitsi domain name to provide the accurate file path.


    . Register a user with the username \&#96;focus\&#96; in the Prosody XMPP server:
    +
    ----
    $ prosodyctl register focus auth.__jitsiFQDN__ __focusUserSecret__
    ----
    +
    The \&#96;focus\&#96; user is a special user for Jitsi Meet conference management and coordination. It is responsible for example for creating and controlling conferences. The \&#96;auth.\___jitsiFQDN___\&#96; portion specifies the domain where the user is registered.
    +
    Replace \&#96;\___jitsiFQDN___\&#96; with your Jitsi domain name. The \&#96;\___focusUserSecret___\&#96; is the password or secret associated with the \&#96;focus\&#96; user. Replace \&#96;\___focusUserSecret___\&#96; with a strong and secure password.


    . Register a user with the username \&#96;jvb\&#96; in the Prosody XMPP server:
    +
    ----
    $ prosodyctl register jvb auth.__jitsiFQDN__ __jvbUserSecret__
    ----
    +
    The \&#96;jvb\&#96; user is used by Jitsi Videobridge component to handle video streams in Jitsi Meet. The \&#96;auth.\___jitsiFQDN___\&#96; portion specifies the domain where the user is registered.
    +
    Replace \&#96;\___jitsiFQDN___\&#96; with your Jitsi domain name. The \&#96;\___jvbUserSecret___\&#96; is the password or secret associated with the \&#96;jvb\&#96; user. Replace \&#96;\___jvbUserSecret___\&#96; with a strong and secure password.


    . Enable and start the prosody service:
    +
    ----
    $ sudo systemctl enable --now prosody
    ----


    === Configuring Jitsi Meet

    .Procedure

    . Locate the \&#96;/etc/jitsi-meet/config.js\&#96; configuration file.

    . Replace the placeholder variables in \&#96;config.js\&#96;.


    === Configuring Jitsi webserver

    .Prerequisites

    \&#42; Configure an HTTPS server for \&#96;\___jitsiFQDN___\&#96;.

    .Procedure

    \&#42; For Apache:
    \&#42;\&#42; Replace the placeholders in the \&#96;/etc/httpd/conf.d/jitsi-meet.conf\&#96; file.

    \&#42;\&#42; Restart the \&#96;httpd\&#96; service:
    +
    ----
    $ sudo systemctl restart httpd
    ----


    \&#42; For Nginx:
    \&#42;\&#42; Replace the placeholders in the \&#96;/etc/nginx/conf.d/jitsi-meet.conf\&#96; file.

    \&#42;\&#42; Restart the \&#96;nginx\&#96; service:
    +
    ----
    $ sudo systemctl restart nginx
    ----



    === Configuring Jicofo

    .Procedure


    . Replace the  \&#96;\___jitsiFQDN___\&#96; and \&#96;\___focusSecret___\&#96; placeholder variables in \&#96;/etc/jicofo/config\&#96; and \&#96;/etc/jicofo/sip-communicator.properties\&#96; files.

    . Enable and start \&#96;jicofo.service\&#96;:
    +
    ----
    $ sudo systemctl enable --now jicofo.service
    ----


    === Configuring Jitsi Videobridge

    .Prerequisites

    \&#42; Open the port \&#96;10000/udp\&#96; if you use Network Address Translation (NAT):

    . Install the \&#96;jitsi-videobridge-firewalld\&#96; package to obtain service definition for \&#96;jitsi-videobridge.service\&#96;
    . Use the service definition to configure \&#96;firewalld\&#96; to open \&#96;10000/udp\&#96; for Jitsi Videobridge.


    .Procedure

    . Replace the \&#96;\___jitsiFQDN___\&#96; and \&#96;\___jvbUserSecret___\&#96; placeholders in the \&#96;/etc/jitsi-videobridge/jvb.conf\&#96; file.

    . Enable and start \&#96;jitsi-videobridge.service\&#96;:
    +
    ----
    $ sudo systemctl enable --now jitsi-videobridge.service
    ----



    .Additional resources

    \&#42; \&#96;/etc/sysconfig/jitsi-videobridge\&#96;


    For more information see link:https://jitsi.org/[jitsi]


    = Machine Owner Key Enrollment
    Jiri Eischmann

    [abstract]
    This page documents how to enroll a machine owner key that is created during the Nvidia driver installation (typically in GNOME Software).

    == Prerequisite

    The Nvidia driver has been installed and a machine owner key to self-sign the driver has been created in GNOME Software (or in a similar tool that supports it).

    == Enrolling Self-signing Key after Reboot

    In order to successfully reboot to Fedora Workstation after the Nvidia driver installation, you have to enroll the machine owner key you created during installation in GNOME Software. During rebooting you'll be presented with the mokutil tool, follow the below steps to enroll the key:

    1. Press any key to continue.
    image:mok-util-01.png[mok-util-01.png,title='Shim UEFI key management']

    2. Select \&#42;Enroll MOK\&#42;.
    image:mok-util-02.png[mok-util-02.png,title='Perform MOK management']

    3. Select \&#42;Continue\&#42; to proceed to the enrollment.
    image:mok-util-03.png[mok-util-03.png,title='Enroll MOK']

    4. Select \&#42;Yes\&#42; to enroll the key.
    image:mok-util-04.png[mok-util-05.png,title='Enroll the key(s)?']

    5. Type the password you created for the key during installation.
    image:mok-util-05.png[mok-util-06.png,title='mokutil start screen']

    6. Select \&#42;Reboot\&#42; to reboot into the OS with the Nvidia drivers enabled.
    image:mok-util-06.png[mok-util-07.png,title='Enroll the key(s) - Password']

    == Security Implications

    Note that the enrolled machine owner key will be used to sign any future updates to the module or any other module you will decide to install and they will be implicitly trusted. All future updates will happen transparently with no interaction and/or authorization. Therefore, it's recommended to delete the machine owner key when it's no longer needed.

    == Deleting Machine Owner Key

    To delete the machine owner key, perform the following command in the terminal:
    +
    [subs='quotes']
    ----
    $ \&#42;sudo mokutil --delete /etc/pki/akmods/certs/public_key.der\&#42;
    ----



    = Managing keyboard shortcuts for running an application in GNOME
    Rekha K Raj
    // :page-aliases:
    // :experimental:

    ////
    info sources:

    http://ask.fedoraproject.org/en/question/9623/how-can-i-set-a-key-shortcut-to-launch-terminal-under-gnome/
    https://help.gnome.org/users/gnome-help/stable/keyboard-shortcuts-set.html.en

    https://unix.stackexchange.com/questions/119432/save-custom-keyboard-shortcuts-in-gnome
    https://askubuntu.com/questions/26056/where-are-gnome-keyboard-shortcuts-stored

    tested on F28 live CD in VM
    ////

    == Adding keyboard shortcuts for custom applications in GNOME

    This section describes how to add a keyboard shortcut for starting a custom application in GNOME.

    [discrete]
    === Procedure

    . Open \&#42;Settings\&#42; and choose the \&#42;Devices\&#42; entry from the list:
    +
    image::shortcuts-settings-devices.png[]
    +
    NOTE: Earlier Fedora versions might not need this step.

    . Choose the \&#42;Keyboard Shortcuts\&#42; entry from the list and scroll down to the bottom of the list of keyboard shortcuts:
    +
    image::shortcuts-keyboard-scroll.png[]

    . Click the \&#42;+\&#42; button at the bottom of the list.
    +
    A window for entering the details appears:
    +
    image::shortcuts-add-empty.png[]

    . Fill in details for the application.
    +
    image::shortcuts-add-filled.png[]
    +
    Replace _My Application_ with the name of the application and _myapp --special options_ with the command to run this application, including any options.

    . Click the \&#42;Set shortcut\&#8230;\&#42; button.
    +
    A window for entering the keyboard shortcut appears:
    +
    image::shortcuts-add-enter.png[]

    . Press the key combination that should become the shortcut for starting the application.
    +
    As soon as you release the key combination, the window for entering the shortcut closes. The window for application name and command now displays the entered shortcut:
    +
    image::shortcuts-add-shortcut.png[]

    . Click the \&#42;Add\&#42; button.
    +
    Your application shortcut now appears in the list under _Custom Shortcuts_:
    +
    image::shortcuts-added.png[]

    // optional - close settings?

    ////
    info sources:

    http://ask.fedoraproject.org/en/question/9623/how-can-i-set-a-key-shortcut-to-launch-terminal-under-gnome/
    https://help.gnome.org/users/gnome-help/stable/keyboard-shortcuts-set.html.en
    ////




    == Disabling keyboard shortcuts for custom applications in GNOME

    This section describes how to disable a keyboard shortcut for starting a custom application in GNOME.

    [discrete]
    === Procedure

    . Open \&#42;Settings\&#42; and choose the \&#42;Devices\&#42; entry from the list:
    +
    image::shortcuts-settings-devices.png[]
    +
    NOTE: Earlier Fedora versions might not need this step.

    . Choose the \&#42;Keyboard Shortcuts\&#42; entry from the list and scroll down to the bottom of the list of keyboard shortcuts:
    +
    image::shortcuts-keyboard-scroll.png[]

    . Scroll down in the list of shortcuts and applications until you locate the application that you want to disable:
    +
    image::shortcuts-added.png[]

    . Click on the entry.
    +
    A window for editing the shortcut appears:
    +
    image::shortcuts-edit.png[]

    . Click the small \&#42;x\&#42; button to the right of the displayed shortcut.
    +
    The keyboard shortcut is removed from this shortcut and the shortcut list now displays _Disabled_ instead of the key combination:
    +
    image::shortcuts-disabled.png[]

    . Close the shortcut editing window.



    == Enabling keyboard shortcuts for custom applications in GNOME

    This section describes how to enable a keyboard shortcut for starting a custom application in GNOME.

    . Open \&#42;Settings\&#42; and choose the \&#42;Devices\&#42; entry from the list:
    +
    image::shortcuts-settings-devices.png[]
    +
    NOTE: Earlier Fedora versions might not need this step.

    . Choose the \&#42;Keyboard\&#42; entry from the list and scroll down to the bottom of the list of keyboard shortcuts:
    +
    image::shortcuts-keyboard-scroll.png[]

    . Scroll down in the list of shortcuts and applications until you locate the application that you want to enable:
    +
    image::shortcuts-list-disabled.png[]

    . Click on the entry.
    +
    A window for editing the shortcut appears:
    +
    image::shortcuts-disabled.png[]

    . Click the \&#42;Set shortcut\&#8230;\&#42; button.
    +
    A window for entering the keyboard shortcut appears:
    +
    image::shortcuts-enabling-entering.png[]

    . Press the key combination that should become the shortcut for starting the application.
    +
    As soon as you release the key combination, the window for entering the shortcut closes. The window for application name and command now displays the entered shortctut:
    +
    image::shortcuts-enabling-entered.png[]

    . Close the shortcut editing window.



    == Removing keyboard shortcuts for custom applications in GNOME

    This section describes how to remove a keyboard shortcut for starting a custom application in GNOME.

    [discrete]
    === Procedure

    . Open \&#42;Settings\&#42; and choose the \&#42;Devices\&#42; entry from the list:
    +
    image::shortcuts-settings-devices.png[]
    +
    NOTE: Earlier Fedora versions might not need this step.

    . Choose the \&#42;Keyboard\&#42; entry from the list and scroll down to the bottom of the list of keyboard shortcuts:
    +
    image::shortcuts-keyboard-scroll.png[]

    . Scroll down in the list of shortcuts and applications until you locate the application that you want to remove:
    +
    image::shortcuts-added.png[]

    . Click on the entry.
    +
    A window for editing the shortcut appears:
    +
    image::shortcuts-edit.png[]

    . Click the red \&#42;Remove\&#42; button.
    +
    The shortcut is removed.



    = Performing administration tasks using sudo
    Harsh Jain; Peter Boy
    //:page-aliases:

    //include::partial$attributes.adoc[]


    [abstract]
    How to perform tasks requiring \&#42;root\&#42; privileges without logging in as \&#42;root\&#42;.

    == What is sudo?

    The [command]\&#96;sudo\&#96; command allows users to gain administrative or root access. When trusted users precede an administrative command with [command]\&#96;sudo\&#96;, they are prompted for their own password. Then, when they have been authenticated and assuming that the command is permitted, the administrative command is executed as if they were the root user.

    Only users listed in the [filename]\&#96;/etc/sudoers\&#96; configuration file are allowed to use the [command]\&#96;sudo\&#96; command. The command is executed in the user's shell, not a root shell.

    The syntax for the sudo command is as follows:

    [subs=quotes]
    ----
    sudo _COMMAND_
    ----

    Replace \&#96;_COMMAND_\&#96; with the command to run as the root user.




    [id='how-to-use-sudo']
    == How to use sudo

    === Using sudo to assign administrator privileges

    Add users to the [directory]\&#96;/etc/sudoers\&#96; configuration file to allow them to use the [command]\&#96;sudo\&#96; command. For these users, the [command]\&#96;sudo\&#96; command is run in the user’s shell instead of in a root shell. As a result, the root shell can be disabled for increased security.

    The administrator can also allow different users access to specific commands using the sudo configuration. Administrators must use the [command]\&#96;visudo\&#96; command to edit the [directory]\&#96;/etc/sudoers\&#96; configuration file.

    To assign full administrative privileges to a user, type [command]\&#96;visudo\&#96; and add the following line to the user privilege section after replacing \&#96;_USERNAME_\&#96; with the target user name:

    [subs=quotes]
    ----
    _USERNAME_ ALL=(ALL) ALL
    ----

    This line allows the specified user to use [command]\&#96;sudo\&#96; from any host and execute any command.

    To allow a user access to specific commands, use the following example after replacing \&#96;_USERS_\&#96; with a target system group:

    [subs=quotes]
    ----
    _%USERS_ localhost=/usr/sbin/shutdown -h now
    ----

    This command allows all members of the \&#96;_USERS_\&#96; system group to issue the [command]\&#96;/sbin/shutdown -h\&#96; as long as the command is issued from the console.

    The man page for [command]\&#96;sudoers\&#96; has a detailed listing of options for this file.


    === Using the same password for root as the user account

    If you use a single user desktop, you might find it convenient to configure [command]\&#96;sudo\&#96;, so you can use the same password to access \&#42;root\&#42; as you use for your regular account. To do this, select to be added to the Administration group during installation. To do it at later stage, or to add a different user, use the following procedure:

    . Become the \&#42;root\&#42; user:
    +
    ----
    $ su -
    ----
    +
    . Enter the password for the root account when prompted.

    . To use your regular password for the root access, run:
    +
    [subs=quotes]
    ----
    \&#35; usermod _USERNAME_ -a -G groupname
    ----
    +
    Replace \&#96;_USERNAME_\&#96; with your account name

    . Log off and back on in order to have access to the group.

    NOTE: When [command]\&#96;sudo\&#96; prompts you for a password, it expects your user password, not the \&#96;root\&#96; password.


    === Logging sudo commands

    Each successful authentication using the [command]\&#96;sudo\&#96; command is logged to the [filename]\&#96;/var/log/messages\&#96; file. For each authentication, the [filename]\&#96;/var/log/secure\&#96; file lists the user name and the command that was executed.

    For additional logging, use the \&#96;pam_tty_audit\&#96; module to enable TTY auditing for specific users. TTY auditing prints the file name of the terminal connected to the standard I/O. To enable TTY auditing, add the following line to your [filename]\&#96;/etc/pam.d/system-auth\&#96; file:

    [subs=quotes]
    ----
    session required pam_tty_audit.so disable=pattern enable=_PATTERN_
    ----

    Replace \&#96;_PATTERN_\&#96; with a comma-separated list of users (and globs, if needed).

    For example, the following command enables TTY auditing for the root user and disables it for all other users:

    ----
    session required pam_tty_audit.so disable=\&#42; enable=root
    ----

    Using the \&#96;pam_tty_audit\&#96; PAM module for auditing only records TTY input. As a result, when the audited user logs in, \&#96;pam_tty_audit\&#96; records the user’s exact keystrokes and saves them in [filename]\&#96;/var/log/audit/audit.log\&#96;. For more information, see the \&#42;pam_tty_audit(8)\&#42; manual page.


    [[warning-and-caveats]]
    == Warnings and caveats

    You must use the user account you created following the installation process, at first boot, for daily use and the \&#42;root\&#42; account only for system administration. Avoid using \&#42;root\&#42; for any non-administration usage, since the account makes it easy to create security or data risks.

    There are several potential risks to keep in mind when using the [command]\&#96;sudo\&#96; command. You can avoid them by editing the [filename]\&#96;/etc/sudoers\&#96; configuration file using [command]\&#96;visudo\&#96; command.


    === sudo timeout

    By default, [command]\&#96;sudo\&#96; stores the password for a five minute timeout period. Any subsequent uses of the command during this period will not prompt you for a password. This could be exploited by an attacker if you leave your workstation unattended and unlocked while still being logged in. You can change this behavior by adding the following line to the \&#96;/etc/sudoers\&#96; configuration file:

    [subs=quotes]
    ------------
    Defaults    timestamp_timeout=_VALUE_
    ------------

    Here, \&#96;_VALUE_\&#96; is the desired timeout length in minutes. Setting the value to 0 causes [command]\&#96;sudo\&#96; to require a password every time.

    If an account is compromised, an attacker can use [command]\&#96;sudo\&#96; to open a new shell with administrative privileges.

    Opening a new shell as a root user in this way allows an attacker administrative access for a theoretically unlimited period of time and bypasses the timeout period specified in the \&#96;/etc/sudoers\&#96; file. Using this method, the attacker \&#42;does not\&#42; need to provide a password for [command]\&#96;sudo\&#96; again until the session ends.


    === Using sudo to access Docker

    Docker has the ability to change the group ownership of the Docker socket to allow users added to the Docker group to be able to run Docker containers without having to execute the [command]\&#96;sudo\&#96; or [command]\&#96;su\&#96; command to become root.

    Enabling access to the Docker daemon from non-root users is a problem from a security perspective. It is a security issue for Fedora, because if a user can talk to the Docker socket they can execute a command which gives them full root access to the host system. Docker has no auditing or logging built in, while [command]\&#96;sudo\&#96; does.

    It is recommended that sudo rules are implemented to permit access to the Docker daemon. This allows [command]\&#96;sudo\&#96; to provide logging and audit functionality.


    === Run Docker using sudo

    . Set up [command]\&#96;sudo\&#96; as shown in xref:performing-administration-tasks-using-sudo.adoc\&#35;_using_sudo_assign_admin_privileges[Using sudo to assign administrator privileges].
    . Create an alias for running the docker command by adding the following line to your \&#96;~/.bashrc\&#96; file:
    +
    ----
    alias docker='sudo /usr/bin/docker'
    ----
    +
    When the user executes the docker command as non-root, sudo will be used to manage access and provide logging.


    === Using sudo without a password

    You can enable \&#96;root\&#96; access without a password specified, allowing any process on your system to become \&#96;root\&#96;. Add the following line to your \&#96;/etc/sudoers\&#96; file:

    [subs=quotes]
    ------------
    _user_        ALL=(ALL)       NOPASSWD: /usr/bin/docker
    ------------

    This will allow \&#96;_user_\&#96; to access docker without a password.

    IMPORTANT: For security reasons, it is recommended that you always use [command]\&#96;sudo\&#96; with a password.


    :experimental:

    = How to Reset the root Password
    The Fedora docs team

    [abstract]
    A root password may be set up while installing Fedora Linux, although it is now suggested to leave the root account locked and use \&#96;sudo\&#96;. This article describes how to proceed if you have used a root password, but for some reason you can no longer access it.


    There are two common methods to reset the root password if it is forgotten or lost.

    \&#42; In Rescue Mode

    \&#42; Using a Fedora Live Media (USB/DVD/CD)


    == How to reset the root password in Rescue Mode

    [NOTE]
    ====
    Changing passwords as root will not prompt for the old password.
    ====

    While booting the system, the xref:grub2-bootloader.adoc[GRUB2] menu will be displayed. To boot the system into rescue mode using \&#96;bash\&#96; follow these steps:

    . Select the boot entry you wish to edit with the arrow keys.

    . Select the entry you wish to edit by pressing kbd:[e].

    . Use the arrow keys to go to select the line beginning with \&#96;linux\&#96;, \&#96;linux16\&#96;, or \&#96;linuxefi\&#96;.

    . Go the the end of that line and include a space and the following \&#96;rw init=/bin/bash\&#96;.
    +
    [NOTE]
    ====
    If your disk is encrypted, you may need to add \&#96;plymouth.enable=0\&#96;
    ====

    . Press kbd:[Ctrl+X] or kbd:[F10] to boot the entry

    . Run the command:
    +
    [source,bash]
    ----
    passwd
    ----
    +
    You will be prompted to enter the new root password twice.
    +
    [NOTE]
    ====
    You can also reset a non-root user password using the same command if you specify \&#96;passwd \&lt;username\&gt;\&#96;.
    ====


    . Reboot the machine with:
    +
    [source,bash]
    ----
    /sbin/reboot -f
    ----

    . As the boot (GRUB) menu appears (same as the first step), again select the boot entry you want to use, press kbd:[e], and add the \&#96;autorelabel=1\&#96; option to the end of the command line. This will temporarily set SELinux in _permissive_ mode (instead of the standard enforcing mode), which will allow the relabeling process to proceed, as well as trigger the relabeling process.
    +
    Then, boot the modified entry with kbd:[Ctrl+X] or kbd:[F10].

    The system may take a moment to boot while SELinux relabels its permissions on the filesystem.
    If you see the Plymouth boot screen you can press the \&#96;ESC\&#96; key on your keyboard to view the SELinux progress.

    Once it is complete, your system is ready and your password has been successfully changed.

    For more information about SELinux states and modes, see xref:selinux-changing-states-and-modes.adoc[Changing SELinux States and Modes].

    [[sect-reset-password-using-the-fedora-live-media]]
    == How to reset the root password with a Fedora Live Media

    [NOTE]
    ====
    To _download_ and create a live USB of Fedora Workstation, follow the instructions on the xref:creating-and-using-a-live-installation-image.adoc[Fedora USB Live Media Quick Doc].

    __For additional information__, specifically about live media using BTRFS, see also
    xref:grub2-bootloader.adoc\&#35;_restoring_the_bootloader_using_the_live_disk[Restoring the bootloader using the Live disk]
    ====

    . Boot the Live installation media and choose \&#96;Try Fedora\&#96;.

    . From the desktop, open a terminal and switch to root using \&#96;su\&#96; (the system will not ask for a password).

    . To view your hard drive device nodes, enter \&#96;df -H\&#96; into the terminal.
    For this example we will use \&#96;/dev/sda1\&#96; for the \&#96;/boot\&#96; partition and \&#96;/dev/sda2\&#96; for the root \&#96;/\&#96; partition.
    +
    If you are using LVM partitions, type: \&#96;sudo lvscan\&#96; and note the \&#96;/dev\&#96; path of your root partition.
    For this example we will use \&#96;/dev/fedora/root\&#96;.

    . Create a directory for the mount point (use the \&#96;-p\&#96; option to create subdirectories):
    +
    [source,bash]

    ----

    mkdir -p /mnt/sysimage/boot

    ----

    . Mount the \&#96;/\&#96; (root) partition (be sure to use the actual device node or LVM path of your root \&#96;/\&#96; partition):
    +
    To mount root on a \&#42;standard partition\&#42; scheme enter:
    +
    [source,bash]

    ----

    mount /dev/sda2 /mnt/sysimage

    ----
    +
    To mount root on an \&#42;LVM partition\&#42; scheme enter:
    +
    [source,bash]

    ----

    mount /dev/fedora/root /mnt/sysimage

    ----

    . Continue the process by mounting \&#96;/boot\&#96;, \&#96;proc\&#96;, \&#96;/dev\&#96;, and \&#96;/run\&#96; with:
    +
    [source,bash]

    ----

    mount /dev/sda1 /mnt/sysimage/boot

    mount -t proc none /mnt/sysimage/proc

    mount -o bind /dev /mnt/sysimage/dev

    mount -o bind /run /mnt/sysimage/run

    ----

    . \&#96;chroot\&#96; to the mounted root partition with:
    +
    [source,bash]

    ----

    chroot /mnt/sysimage /bin/bash

    ----

    . Change the root password:
    +
    [source,bash]

    ----

    passwd

    ----

    . Exit out of chroot with:
    +
    [source,bash]

    ----

    exit

    ----
    +
    and exit out of the terminal.

    . Reboot your system and boot from the hard drive.

    Congratulations, your root password has been successfully changed.

    [[sect-additional-troubleshooting]]
    == Additional Troubleshooting

    . If you cannot enter rescue mode because you forgot the Firmware/BIOS password here are some options:

    .. Refer to your computer's documentation for instructions on resetting the Firmware/BIOS password in CMOS memory.

    .. Temporarily move the system hard disk to another machine, and follow the procedures above to reset the root password.

    . If you have set a password for your boot loader, refer to xref:creating-and-using-a-live-installation-image.adoc[Creating and Using a Live Installation Image].

    . If you want to reset the boot loader password, refer to the instructions on how to link:++https://fedoraproject.org/wiki/Reset_Bootloader_Password++[Reset the Bootloader Password].


    = Root Account Locked
    Héctor H. Louzao P
    //:page-aliases:


    == Phenomenon

    Cannot open access to console, the root account is locked in emergency mode (dracut emergency shell)

    == Reason

    This is a known problem. It happens Fedora releases 28 and newer, which don’t require password for root account during
    installation https://fedoraproject.org/wiki/Changes/ReduceInitialSetupRedundancy\&#35;Root_Account[Root Account] and use
    first user added as \&#96;administrator/superuser\&#96;. In this case root account is locked, and if \&#96;/home\&#96; is inaccessible – then
    the system can’t use superuser/administrator account either.

    == What to Do?

    If you find yourself in this situation and you can’t resolve problem with \&#96;/home\&#96; mounting from Live disk/USB,
    and you need access to emergency mode, the solution is simple.

    . Boot into Live disk/usb and chroot into your Fedora installations as documented in this xref:grub2-bootloader.adoc\&#35;_restoring_bootloader_using_live_disk[Fedora Quick-docs Article]
    - following steps depends of your File System \&#96;LVM/BTRF/LUKS\&#96;.

    . Unlock root account by supplying password for it:
    +
    ----
    passwd root
    ----

    . Exit chroot environment with [Ctrl-d] or
    +
    ----
    exit
    ----

    . Reboot your computer with GUI or with
    +
    ----
    systemctl reboot
    ----


    = Wine – Running Windows applications in the Fedora GUI
    Héctor H. Louzao Pozueco;  Ankur Sinha; Akshata Khedekar
    //:page-aliases:

    [abstract]
    http://winehq.org/[Wine] is an open source implementation of the Windows API on top of X and OpenGL.

    Wine emulates the Windows runtime environment by translating Windows  system calls into POSIX-compliant system calls, recreating the directory structure of Windows systems, and providing alternative implementations of Windows system libraries, system services through https://wiki.winehq.org/Wineserver[wineserver].

    == Packages

    Fedora's Wine packages are split up to allow for smaller installations. The \&#96;wine\&#96; meta package will bring with it the most important components
    of Wine. Expert users may want to pick specific components from the list
    https://packages.fedoraproject.org/pkgs/wine/[here].
    The current versions of the Wine packages can also be seen on the https://packages.fedoraproject.org/pkgs/wine/wine/[Fedora packages application].

    [[configuration-files]]
    == Configurations files

    The default wine configuration files is stored in your \&#96;$HOME\&#96; directory:

    \&#96;\&#96;\&#96;
    $HOME/.wine
    \&#96;\&#96;\&#96;

    TIP: Different prefixes can be used as described in the
    xref:\&#35;working-with-prefix[wine prefix] section lower in this document.

    [[wine-desktop-files]]
    == Wine desktop files

    https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html\&#35;variables[Wine respects the XDG Base Directory Specification].
    \&#96;$XDG_DATA_HOME\&#96; defines the base directory relative to which
    user-specific data files should be stored. If \&#96;$XDG_DATA_HOME\&#96; is either
    not set or empty, it defaults to \&#96;$HOME/.local/share\&#96;.

    Wine stores its desktop files in \&#96;$XDG_DATA_HOME/applications/wine\&#96;.

    [[gui-configuration-register]]
    == GUI for configuring the Wine registry (winecfg)

    https://wiki.winehq.org/Winecfg[\&#96;winecfg\&#96;] is a GUI configuration tool for Wine, designed to make life
    a little easier than editing the registry.

    This utility is provide by the https://packages.fedoraproject.org/pkgs/wine/wine-common/[\&#96;wine-common\&#96; package].
    It allows you to:

    - set the Windows version
    - change the default libraries (DLLs) Wine loads
    - modify graphics settings
    - modify desktop integration related settings
    - modify drive mappings
    - change sound/audio settings

    WARNING: Some applications do not work with the default
    Windows version which Wine offers. E.g.: Amazon Kindle
    Desktop Edition.

    [[wine-script]]
    == Gui Wine script (winetricks)

    https://wiki.winehq.org/Winetricks[Winetricks] is a helper script to download and install various
    redistributable runtime libraries needed to run some programs in Wine.
    These may include replacements for components of Wine using closed
    source libraries.

    It is provided by the https://packages.fedoraproject.org/pkgs/winetricks/winetricks/[\&#96;winetricks\&#96; package]:

    \&#96;\&#96;\&#96;
    sudo dnf install winetricks
    \&#96;\&#96;\&#96;

    It can download and install applications and libraries
    needed to run some programs in Wine, e.g., Adobe Digital Edition.

    [[working-with-prefix]]
    == Wine prefix

    A https://wiki.winehq.org/FAQ\&#35;Wineprefixes[Wine prefix] is a folder that contains all of the Wine configurations
    as well as all of the Windows pieces that Wine uses for compatibility,
    including libraries and a registry.

    Some applications need a 32 or 64 wine prefix, this can be done in the
    following way:

    - Create a clean wine32/64 prefix:


    \&#96;\&#96;\&#96;
    WINEPREFIX='$HOME/\&lt;directory\&gt;' WINEARCH=winxx wine wineboot
    \&#96;\&#96;\&#96;

    \&#42; Where \&#96;xx\&#96; is 32 or 64 bits
    \&#42; \&#96;\&lt;directory\&gt;\&#96; is the directory which you can store the wine environment

    To use a wine prefix created before:

    \&#96;\&#96;\&#96;
    export WINEPREFIX=$HOME/\&lt;directory\&gt;
    \&#96;\&#96;\&#96;

    [[install-basic-applications]]
    == Install some basics/utils applications

    How to install the follow applications under wine?

    1. Adobe Digital Edition 4.5

    \&#42; use \&#96;winetricks\&#96; as described before and select \&#42;\&#42;install application\&#42;\&#42; in
    the menu 'What you do you want to do?'
    \&#42; in 'Which package(s) would you like to install?' select \&#96;adobe_diged4\&#96;

    2. Kindle Desktop Edition

    \&#42; download from -\&gt; https://www.amazon.com/Amazon-Digital-Services-LLC-Download/dp/B00UB76290[Amazon Kindle]
    \&#42; install it
    \&#42; use winecfg to change the default windows version so is 7 to a higher
    version

    [[bugs-and-problems]]
    == Bugs and problems

    Before reporting bugs against Wine please make sure your system is fully
    up to date.

    \&#8230;.
    dnf upgrade
    \&#8230;.

    Also check if a newer version is available in the https://fedoraproject.org/wiki/QA:Updates_Testing[updates-testing] repository.

    \&#8230;.
    dnf --enablerepo=updates-testing update wine
    \&#8230;.

    If you are using the proprietary graphics drivers please remove them
    from your system and try again, as they are known to cause problems.

    When debugging Wine, your goal is to determine if the issue is one of
    _code functionality_ or _packaging in Fedora_.

    Check the http://appdb.winehq.org[Wine Application Database] to see if
    your application is supported, or if there are known issues that match
    yours. Anything that falls into this category is a bug in upstream code
    functionality.

    The next step is to see if the problem persists with a clean ~/.wine
    folder. To try this without losing your old configuration:

    \&#8230;.
    mv ~/.wine ~/.wine-save
    \&#8230;.

    Afterwards try to trigger the bug again. Your original wine folder can
    be restored with:

    \&#8230;.
    rm -fr ~/.wine; mv ~/.wine-save ~/.wine
    \&#8230;.

    If your application still does not work but has been working in a
    previous version of wine it is probably a regression. Consider filling a
    bug in the upstream https://bugs.wine-staging.com/[Wine-staging bug
    tracking system].

    IMPORTANT: Do not file bugs in the Winehq.org bugzilla unless told to do so.

    If you really think that your bug is Fedora-related, file a bug against
    the Wine component in https://bugzilla.redhat.com[Fedora's bug tracking
    system].


    = Setting a key shortcut to run an application in GNOME
    Adam Samalik; Anthony McGlone
    :page-authors: {author},{author_2}
    :page-aliases: proc_setting-key-shortcut

    If you frequently use a certain application, you can set a keyboard shortcut to quickly launch that application on GNOME.

    This example shows how to set a key shortcut to launch the terminal.

    To set a key shortcut to run an application:

    . Open the \&#42;Settings\&#42; menu and select \&#42;Keyboard\&#42; from the list.
    . Scroll down to the \&#42;Keyboard Shortcuts\&#42; section and click \&#42;View and Customize Shortcuts\&#42;.
    . Click on the \&#42;Custom Shortcuts\&#42; menu item. Then click \&#42;Add Shortcut\&#42;.
    . Enter the following details in the \&#42;Add Custom Shortcut\&#42; window:
    \&#42; Add a \&#96;Name\&#96; for your shortcut, for example, \&#96;Terminal\&#96;.
    \&#42; Enter the command that launches the application. For example, \&#96;gnome-terminal\&#96;.
    . Click \&#42;Set Shortcut\&#42; to open the \&#42;Enter the new shortcut\&#42; dialog.
    . Type a keyboard shortcut, for example \&#96;Ctrl-Alt-T\&#96;.
    . Click \&#42;Add\&#42;.

    Your shortcut appears under \&#42;Custom Shortcuts\&#42; and is ready to use. If you need to edit or remove
    a shortcut, follow the steps below.

    To edit a shortcut:

    . Open the \&#42;Custom Shortcuts\&#42; menu.
    . Click on the shortcut that you wish to edit.
    . Modify \&#42;Name\&#42;, \&#42;Command\&#42; as needed.
    . To change \&#42;Shortcut\&#42;, click on the x icon beside the keys.
    . Click \&#42;Set Shortcut\&#42; and enter the new shortcut keys.

    To remove a shortcut:

    . Open the \&#42;Custom Shortcuts\&#42; menu.
    . Click on the shortcut that you wish to remove.
    . Click the \&#42;Remove\&#42; button.




    = Screen Recorder – Comparison of Applications and How to Use Them
    Ankursinha; Brunovernay; Hhlp
    :experimental:
    :page-aliases: screencast-apps-comparison.adoc


    == Using Gnome's native screencast tool

    Gnome3 has already a screen recording functionality. Pressing Alt+Ctrl+Shift+R recording will start. There should be a red icon on the message tray in the right-bottom corner of your screen. If the message tray is hidden, Super+M will activate it. Pressing the red icon will stop the recording. The video is saved in the Video directory on your home directory on link:https://en.wikipedia.org/wiki/Webm[webm] format.

    === Increase the duration of screencast videos

    At just 30 seconds long the default length of screencast using this method isn’t ideal, particularly if you plan on making a lengthy video or need to demo a particular workflow or feature. It is possible to increase the duration of screencasts manually, by modifying the following gsettings string using the Terminal application:
    [,console]
    ----
    gsettings set org.gnome.settings-daemon.plugins.media-keys max-screencast-length 60
    ----
    Replace the ’60’ value with the length you want in seconds, e.g., 300 for 5 minutes, 600 for 10 minutes, and so on. If you set the value to ‘0’ there will be no time limit.

    Remember: you can stop recording at any time regardless of the duration you set. Just press the keyboard shortcut you use to start recording to stop recording.

    == KDE Spectacle

    KDE Spectacle supports screen recording for a KDE Plasma Wayland session since the 23.04 release. To launch Spectacle, press kbd:[PrtSc].

    On the middle right side of Spectacle, click the tab 'Recording', select one of three options - Workspace, Selected Screen and Selected Window.

    Press 'Finish recording' to stop the recording. Recorded footage will be saved as WebM file format as a default.

    == Byzanz

    Byzanz is a desktop recorder striving for ease of use. It can record to GIF images, Ogg Theora video - optionally with sound – and other formats. It is available in Fedora. To install execute
    [,console]
    ----
    % sudo dnf install byzanz
    ----

    It is similar to former Istanbul, but can also produce:

    \&#42; animated GIF files (video only)
    \&#42; Ogg Theora files (with or without audio)
    \&#42; FLV Flash screen files (lossless, can be postprocessed)
    \&#42; Byzanz format for conversion later to multiple formats

    == Simple Screen Recorder

    SimpleScreenRecorder is a Linux program that is created to record programs and games.

    Features

    \&#42; Graphical user interface (Qt-based).
    \&#42; Faster than VLC and ffmpeg/avconv.
    \&#42; Records the entire screen or part of it, or records OpenGL applications directly (similar to Fraps on Windows).
    \&#42; Synchronizes audio and video properly (a common issue with VLC and ffmpeg/avconv).
    \&#42; Reduces the video frame rate if your computer is too slow (rather than using up all your RAM like VLC does).
    \&#42; Fully multithreaded: small delays in any of the components will never block the other components, resulting is smoother video and better performance on computers with multiple processors.
    \&#42; Pause and resume recording at any time (either by clicking a button or by pressing a hotkey).
    \&#42; Shows statistics during recording (file size, bit rate, total recording time, actual frame rate, \&#8230;).
    \&#42; Can show a preview during recording, so you don't waste time recording something only to figure out afterwards that some setting was wrong.
    \&#42; Uses libav/ffmpeg libraries for encoding, so it supports many different codecs and file formats (adding more is trivial).
    \&#42; Can also do live streaming (experimental).
    \&#42; Sensible default settings: no need to change anything if you don't want to.
    \&#42; Tooltips for almost everything: no need to read the documentation to find out what something does.

    SimpleScreenRecorder is available in the RPM Fusion repository. RPM Fusion can be activated with this command:
    [source,]
    ----
    rpm -Uvh http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-stable.noarch.rpm
    ----

    After that, SimpleScreenRecorder can be installed with this command:
    [source,]
    ----
    sudo dnf install simplescreenrecorder
    ----


    == OBS Studio

    OBS Studio provides feature-rich professional tools for your video recordings and live streaming. You can find the latest version of the upstream documentation at https://obsproject.com/kb/quick-start-guide


    == Recording Web apps or Web pages

    This is a special case, and tools designed for this task can achieve a better result. Chrome has plugins to do the job.

    == Advanced Topics: Adding Audio

    \&#42; You must have audacity (or other audio recorder) installed
    \&#42; Record your audio track, taking care to synchronize it with events in your recording (I believe this may be easier to record the audio track first, then go back and play the audio while recording video)
    \&#42; Export your audio to a wave or ogg-vorbis file, I use /tmp/stream.wav
    \&#42; Grab the script xref:attachment$screencast/fedora-av-splice.sh[fedora-av-splice.sh]. This script uses the gstreamer framework to add the audio and re-encode the theora video file
    \&#42; Run fedora-av-splice.sh /tmp/stream.wav /path/to/theora.ogg /path/to/result.ogg
    \&#42; Get a cup of coffee while things encode, this will be cpu intensive.
    \&#42; You should be able to play the resulting file in mplayer, vlc, totem, or xine


    == Advanced Topics: Alternative Audio Tracks

    Goal: Create alternative audio tracks for pre-existing screencast named desktop-recording.ogg

    Additional Software Needed: libannodex in Fedora

    \&#42; Create a 10 second timestamp test pattern video with gstreamer
    +
    [source,]
    ----
    gst-launch-0.8 videotestsrc num-buffers=250 ! video/x-raw-yuv,framerate=25.0 ! timeoverlay ! theoraenc ! oggmux ! filesink location=test.ogg
    ----
    // This file could not be found on the WIKI
    //+
    //Or use the provided https://fedoraproject.org/w/index.php?title=Special:Upload\&amp;wpDestFile=ScreenCasting_test.ogg[File:ScreenCasting test.ogg]

    \&#42; chain the two videos together to produce a video with 10 second lead-in
    [source,]
    ----
    cat test.ogg desktop-recording.ogg \&gt; edit-video.ogg
    ----
    \&#42; begin playing video with totem edit-video.ogg
    \&#42; begin recording new audio track at the end of the 10 second lead in.
    \&#42; make small edits as needed at the beginning and end of the audio to have audio file make time length of the original video
    \&#42; use shell script xref:attachment$screencast/fedora-av-splice.sh[fedora-av-splice.sh] as above to replace the original audio track

    // This one worked
    //\&#42; use https://fedoraproject.org/wiki/File:ScreenCasting_fedora-av-splice.sh[File:ScreenCasting fedora-av-splice.sh] as above to replace the original audio track

    == Advanced Topics: Adding a video timestamp

    For further editing needs, one can overlay the time over the original video. This may help in the production of additional audio tracks.

    // Here is a small script to produce a video with video timestamp visible: File:ScreenCasting_fedora-video-timestamp.sh
    // Not working
    // https://fedoraproject.org/w/index.php?title=Special:Upload\&amp;wpDestFile=ScreenCasting_fedora-video-timestamp.sh

    // Not working:
    // https://fedoraproject.org/wiki/File:ScreenCasting_fedora-video-timestamp.sh

    == References

    \&#42; https://extensions.gnome.org/extension/690/easyscreencast/
    \&#42; https://lwn.net/Articles/478370/
    \&#42; http://commons.wikimedia.org/wiki/Help:Converting_video
    \&#42; http://screencast-o-matic.com/
    \&#42; http://www.theora.org/theorafaq.html\&#35;41
    // \&#42; Byzanz - http://www.advogato.org/person/company/diary.html?start=18
    \&#42; http://www.debugmode.com/wink/
    \&#42; http://www.misterhowto.com/index.php?category=Computers\&amp;subcategory=Video\&amp;article=make_a_screencast_with_linux
    \&#42; http://www.misterhowto.com/index.php?category=Computers\&amp;subcategory=Video\&amp;article=avi_to_dv_with_ffmpeg
    \&#42; http://www.misterhowto.com/index.php?category=Computers\&amp;subcategory=Video\&amp;article=change_or_remove_audio_track_with_mencoder
    \&#42; http://blogcritics.org/archives/2007/02/05/194332.php
    \&#42; https://github.com/foss-project/green-recorder
    \&#42; https://www.maartenbaert.be/simplescreenrecorder/




    = GNOME Shell extensions
    Ankur Sinha; Fedora Documentation Team

    From the https://extensions.gnome.org/about/[website]:

    'GNOME Shell extensions are small pieces of code written by third party developers that modify the way GNOME works.
    (If you are familiar with Chrome Extensions or Firefox Addons, GNOME Shell extensions are similar to them.)

    Since extensions are created outside of the normal GNOME design and development process, they are supported by their authors, rather than by the GNOME community.
    Some features first implemented as extensions might find their way into future versions of GNOME.'

    So, please report bugs in these extensions directly to their developers.

    Extensions can either be local or system-wide.
    Local extensions are ones installed by each user in their home directories (\&#96;~/.local/share/gnome-shell/extensions\&#96;), whereas system-wide extensions are installed by administrators in system directories (\&#96;/usr/share/gnome-shell/extensions/\&#96;).
    System extensions, therefore, cannot be installed, updated or removed by non-administrator users.
    They can, however, be enabled or disabled by each user.

    NOTE: In the event of crashes with GNOME shell, the first recommended step to diagnosing the issue is to disable all extensions. In cases where GNOME Shell crashes directly on login, you can use a different desktop environment if it is installed, or use the command line tools listed below using a virtual terminal (\&#96;ctrl + alt + f2\&#96;) to disable them.

    == Installing and removing system-wide GNOME Shell extensions

    These are generally provided in the Fedora repositories and can be installed, removed, and updated using the default package management tools like \&#96;dnf\&#96;.
    You can find a list https://packages.fedoraproject.org/search?query=gnome-shell-extension[here by searching the packages application] for \&#96;gnome-shell-extension\&#96;.

    Run dconf to update the system dconf databases, making the newly installed system-wide extensions available to all users.
    \&#96;\&#35; dconf update\&#96;

    == Installing and removing local GNOME Shell extensions

    Local GNOME Shell extensions can be installed in multiple ways.

    - Directly from the https://extensions.gnome.org/about/[website] using Firefox.
    This requires the installation of a browser extension.
    If it is not installed, the website displays a notification with a link that installs it.

    - Manual installation.
    This is not recommended.
    Advanced users that would like to do so should follow the instructions provided by the developers.

    These can all be used to update installed local extensions also.

    == Enabling, disabling and changing settings for GNOME Shell extensions

    All extensions can be enabled, disabled, and their preferences modified by each user using:

    - https://extensions.gnome.org/local/[Gnome's Extensions website] using Firefox.

    - \&#96;gnome-shell-extension-tool\&#96;.
    While this tool allows you to enable and disable extensions, it does not allow you to modify their settings.
    It does allow you to reload an extension without logging out and back in and it also creates the default skeleton if you would like to write a new extension.
    Please use \&#96;gnome-shell-extension-tool -h\&#96; to learn more.

    - the https://packages.fedoraproject.org/pkgs/gnome-extensions-app/gnome-extensions-app/[GNOME Extensions] app.
    Apart from other customisations, GNOME Extensions also allows enabling, disabling, and modifying preferences for GNOME shell extensions.



    = Using Kubernetes on Fedora
    Bradley G Smith,

    // Optional  free form useful additional information as comment

    //include::{partialsdir}/3rdparty-message.adoc[]
    ////

    This message needs to be included on any document referencing third party software
    repositories. Add the following line verbatim to the top of any such document:


    Please do not change this message without consultation. Thanks!

    ////

    [CAUTION]
    ====
    This page discusses third-party software sources not officially affiliated with or endorsed by the Fedora Project.
    Use them at your own discretion.
    Fedora recommends the use of free and open source software and avoidance of software encumbered by patents.
    ====



    [[sect-overview]]
    == Overview

    This guide provides information about link:https://kubernetes.io[Kubernetes] and the Kubernetes rpms available from Fedora.

    All currently supported versions of Kubernetes are available in each Fedora release (subject to a possible link:https://go.dev[Golang] language constraint).

    A short guide on creating a Kubernetes cluster using \&#96;\&#96;\&#96;kubeadm\&#96;\&#96;\&#96; is included, as a short introduction to Kubernetes for those new to this technology stack.

    The guide also touches on an alternative source for Kubernetes rpms available in link:https://copr.fedorainfracloud.org[COPR] and potential uses.

    [[sect-what-is-kubernetes]]
    === What is Kubernetes?

    link:https:/kubernetes.io[Kubernetes] is an 'open-source system for automating deployment, scaling, and management of containerized applications' on one or more machines.
    Kubernetes automates many of the tasks necessary to deploy, manage, and scale applications that are running as a container.
    This automation is vital when managing applications in data center or cloud environment where there are 100's or 1000's of machines and a corresponding complexity in numbers of applications.Fedora provides several technologies, in addition to Kubernetes, that run containers such as link:https://docker.com[Docker] or link:https://podman.io[Podman].

    Kubernetes is now at the center of a vast ecosystem of products and services (link:https://cncf.io/[Cloud Native Computing Foundation]) that help organizations create, install, run, manage and secure container-based applications and services at any possible scale.

    Kubernetes can be used in a home lab on a single machine, a small cluster for home or business automation, edge-based services and applications in remote offices or enterprise scale production workloads in the cloud.

    This guide is focused on the Kubernetes rpms available from Fedora and using \&#96;dnf\&#96; and the command line to install these rpms on Fedora and create a basic cluster using \&#96;kubeadm\&#96;.
    A short section on versioned rpms for link:https://cri-o.io[CRI-O] and link:https://github.com/kuberb    etes/cri-tools[CRI-Tools] is included.

    Please visit the xref:virtualization-an-overview.adoc[Fedora Quick Docs Virtualization Guide] to learn more about containers and other virtualization technologies and their availability in Fedora.

    [[sect-content-guide]]
    == Content guide

    [cols='1,1']
    |===
    |xref:using-kubernetes-basics.adoc[Basics]
    |A brief overview of Kubernetes for those new to the technology along with a terminology table.

    |xref:using-kubernetes-versioned.adoc[Versioned rpms - Fedora 41 and newer]
    |The guide to the versioned rpm format for Kubernetes in Fedora 41 and newer.

    |xref:using-kubernetes-kubelet.adoc[Resilient \&#96;\&#96;\&#96;kubelet\&#96;\&#96;\&#96; configuration]
    | A brief guide to \&#96;\&#96;\&#96;kubelet\&#96;\&#96;\&#96; configuration methods.

    |xref:using-kubernetes-kubeadm.adoc[Create a cluster]
    |A guide to using \&#96;\&#96;\&#96;kubeadm\&#96;\&#96;\&#96; to instantiate a Kubernetes cluster on a single Fedora machine for exploration, testing, and development.

    |xref:using-kubernetes-cri-o.adoc[CRI-O and CRI-Tools]
    |A guide to the versions of link:https://cri-o.io[CRI-O] and link:https://github.com/kuberbetes/cri-tools[CRI-Tools] available in Fedora 41 and newer.

    |===



    = Kubernetes Basics
    Bradley G Smith,
    :page-aliases: kubernetes/basics

    // Optional  free form useful additional information as comment

    //include::{partialsdir}/3rdparty-message.adoc[]
    ////

    This message needs to be included on any document referencing third party software
    repositories. Add the following line verbatim to the top of any such document:


    Please do not change this message without consultation. Thanks!

    ////

    [CAUTION]
    ====
    This page discusses third-party software sources not officially affiliated with or endorsed by the Fedora Project.
    Use them at your own discretion.
    Fedora recommends the use of free and open source software and avoidance of software encumbered by patents.
    ====



    [[sect-kubernetes-defined]]
    == Kubernetes Defined

    link:https:/kubernetes.io[Kubernetes] is an 'open-source system for automating the deployment, scaling, and management of containerized applications' on one or more machines.
    Kubernetes automates many of the tasks necessary to deploy, manage, and scale applications that are running as a container.
    This automation is vital when managing applications in data center or cloud environment where there are 100's or 1000's of machines and a corresponding complexity in numbers of applications. Fedora provides several technologies, in addition to Kubernetes, that run containers such as link:https://docker.com[Docker] or link:https://podman.io[Podman].

    Kubernetes had its genesis in the concepts and principles used at Google to run container-base workloads at scale and with resilience.
    Kubernetes is now at the center of a vast ecosystem of products and services (link:https://cncf.io/[Cloud Native Computing Foundation]) that help organizations create, install, run, manage and secure container-based applications and services at any possible scale.

    There are numerous ways to install and configure Kubernetes depending on purpose and target environment.
    Is this for a home lab on a single machine, a small cluster for home or business automation, edge-based services and applications in remote offices or enterprise scale production workloads in the cloud?

    There is an enormous amount of Kubernetes information available online and in books. A good place to start is the link:https://kubernetes.io/docs/home/[Kubernetes Documentation] web site. Become familiar with what is available here, then use your favorite search engine to find additional material tailored to your requirements.

    [[sect-versions]]
    == Versions

    The Kubernetes team uses link:https://semver.org[semantic versioning] for Kubernetes where a given version has 3 primary components separated by periods: _major.minor.patch_. An example is 1.30.1 where the major version is _1_, the minor version is _30_, and the patch level is _1_. \&#42;A Kubernetes release is a new minor version such as 1.30 or 1.31.\&#42; The versioned rpms in Fedora are, therefore, at the minor version level.

    Using \&#96;\&#96;\&#96;dnf update\&#96;\&#96;\&#96; on an existing versioned kubernetes rpm will update patch releases only. See the xref:using-kubernetes-versioned.adoc\&#35;sect-fedora-40-version-update[update process recommendations] for versioned rpms.

    [[sect-terminology]]
    == Terminology

    Kubernetes is complex and like many complex systems has its own terminology.
    The terminology used in this guide are defined here.
    The Kubernetes teams maintains a comprehensive link:https://kubernetes.io/docs/reference/glossary/[glossary] which is used in the subset below.

    [horizontal]
    cluster:: a set of one or more nodes managed as an entity.
    A cluster has at least one node and one control plane (these can be on the same or separate machines).
    control plane:: the node or nodes in the cluster hosting the management services for the cluster.
    At least one node in a cluster has a control plane.
    A control plane machine can also function as a worker node.
    node:: a worker machine (either a virtual machine or physical machine) in a Kubernetes cluster that has the services required to run pods.
    These services include the \&#96;kubelet\&#96; container runtime and \&#96;kube-proxy\&#96;.
    pods:: containerized applications are deployed and managed in Kubernetes as pods.
    A pod is the base object managed by Kubernetes in a cluster.
    A pod typically has a single primary container but may include more capabilities including multiple containers.


    [[sect-additional-information]]
    == Additional Information

    Kubernetes and the ecosystem of related components found under the link:https://www.cncf.io[Cloud Native Computing Foundation] umbrella is vast as is the plethora of internet accessible information about Kubernetes. Kubernetes and this ecosystem is also evolving rapidly such that online information may be out-dated or incomplete (_likely including information in this Quick Doc -ed_).



    = Versioned Kubernetes RPMS on Fedora
    Bradley G Smith,
    :page-aliases: kubernetes/versioned

    // Optional  free form useful additional information as comment

    //include::{partialsdir}/3rdparty-message.adoc[]
    ////

    This message needs to be included on any document referencing third party software
    repositories. Add the following line verbatim to the top of any such document:


    Please do not change this message without consultation. Thanks!

    ////

    [CAUTION]
    ====
    This page discusses third-party software sources not officially affiliated with or endorsed by the Fedora Project.
    Use them at your own discretion.
    Fedora recommends the use of free and open source software and avoidance of software encumbered by patents.
    ====



    [[sect-overview]]
    == Overview

    Versioned Kubernetes rpms (e.g. kubernetes1.34.rpm, kubernetes1.33.rpm) were introduced in Fedora 41 and is the standard used for Kubernetes in all Fedora releases.

    As versioned rpms are distinct packages which contain the same set of files, they are treated as conflicting by rpm.
    The necessary changes to the package update process to deal with this conflict are documented below.

    [[golang-constraint]]
    === Go language constraint

    Each Kubernetes version (at the _minor_ level, _e.g._ Kubernetes v1.31) is built with a specific version of the go language. Each Fedora release is paired with a specific go version
    For example, Go 1.22 is available on Fedora 40 and go 1.23 is available on Fedora 41.

    A new Kubernetes version may be built with a version of Go not available on older Fedora releases thereby blocking the packaging of that Kubernetes version for that specific Fedora release.
    If the Go version is updated, the blocked Kubernetes version will be made available as long as the Kubernetes version is still supported.

    [[sect-kubernetes-rpms]]
    == Kubernetes rpms in Fedora

    The table below lists the Kubernetes rpms available for each Kubernetes release, what the rpm contains, and notes on purpose and any cautions or restrictions.

    .Versioned Kubernetes rpms in Fedora 41 (and newer)
    [cols='1,1,1',_options='header']
    |===
    |RPM Name|Contents|Notes
    |kubernetes
    |kubelet
    |Kubelet is the Kubernetes runtime on a node.

    |kubernetes-kubeadm
    |kubeadm
    |Kubeadm initializes a cluster and joins new nodes to a cluster.
    This rpm is optional but recommended by the Kubernetes team.
    Install on every node if used.

    |kubernetes-client
    |kubectl
    |Kubernetes command line client.
    Recommended on any node configured as a control plane as it allows the cluster administrator control over the cluster from an ssh session on the control plane.
    Install on a machine that can connect to the cluster over the network.

    |kubernetes-systemd
    |kube-apiserver, kube-controller-manager, kube-proxy, kube-scheduler
    |Systemd services for a kubernetes control-plane and/or node.
    Not needed for most installations as kubeadm will install these components as static pods.
    If used, then install on all nodes.
    Use systemctl to enable kube-proxy on all nodes. Enable kube-apiserver, kube-controller-manager, and kube-scheduler on control plane nodes.

    |===

    [[sect-installation]]
    == Versioned rpm installation recommendations

    For most modern kubernetes clusters install kubernetes, kubernetes-kubeadm, and kubernetes-client on each machine in the cluster.
    If disk space is a constraint only install kubernetes-client on control-plane machines.

    [source,bash]
    ----
    \&#35; using kubernetes 1.34 as an example
    sudo dnf install kubernetes1.34 kubernetes1.34-kubeadm kubernetes1.34-client
    ----

    If conducting a manual installation of Kubernetes (see link:https://github.com/kelseyhightower/kubernetes-the-hard-way[Kubernetes The Hard Way]) then install all kubernetes rpms except kubernetes-kubeadm.

    [source,bash]
    ----
    \&#35; using kubernetes 1.34 as an example
    sudo dnf install kubernetes1.34 kubernetes1.34-client kubernetes1.34-systemd
    ----

    [[sect-update]]
    == Versioned rpm update recommendations

    Since rpm treats kubernetes1.34 as a different application from kubernetes1.31, yet both rpms install the same files in the same locations. These rpms therefore conflict and the normal \&#96;\&#96;\&#96;dnf update\&#96;\&#96;\&#96; will not succeed in replacing v1.34 with v1.31.
    There are two options available when using dnf: remove/install or swap.

    The remove and install sequence using normal \&#96;\&#96;\&#96;dnf\&#96;\&#96;\&#96; commands to first remove one version of Kubernetes and then replace it with the next version. Both \&#96;\&#96;\&#96;dnf\&#96;\&#96;\&#96; commands will also remove/install any dependencies.

    \&#42;Important Note\&#42; - this is only needed when changing minor versions, that is replacing v1.34 with v1.31. Updates at the patch level such as v1.34.2 to v1.34.3 use the normal \&#96;\&#96;\&#96;dnf update\&#96;\&#96;\&#96; command.

    [source,bash]
    ----
    \&#35; Remove and replace with kubernetes 1.34 and 1.31 as an example
    sudo dnf remove kubernetes1.34 kubernetes1.34-kubeadm kubernetes1.34-client
    sudo dnf install kubernetes1.31 kubernetes1.31-kubeadm kubernetes1.31-client
    ----

    The \&#96;\&#96;\&#96;dnf swap\&#96;\&#96;\&#96; command can also be used to change from one Kubernetes release to the next.
    Using swap avoids re-installation of dependencies but the \&#96;\&#96;\&#96;kubernetes1.31\&#42;\&#96;\&#96;\&#96; dnf package specification will install all matching rpms from the repository and not just the rpms removed by the initial \&#96;\&#96;\&#96;kubernetes1.34\&#42;\&#96;\&#96;\&#96; package specification.:w


    [source,bash]
    ----
    \&#35; Remove and replace with kubernetes 1.34 and 1.31 as an example
    sudo dnf swap kubernetes1.34\&#42; kubernetes1.31\&#42;
    ----

    [[sect-retirement]]
    == Versioned rpm retirement policy

    The link:https://kubernetes.io[Kubernetes Project] releases a new (minor) version every 4 months which is then supported for one (1) year.

    Patches for each minor version are released monthly.

    Two months after a Kubernetes version reaches end-of-life, the corresponding rpm is retired in Rawhide following the link:https://docs.fedoraproject.org/en-US/package-maintainers/Package_Retirement_Process/[Package Retirement Process].
    Packages for the corresponding version of CRI-O and CRI-Tools are also retired.


    = Resilient kubelet configuration
    Bradley G Smith,
    :page-aliases: kubernetes/kubelet

    // Optional  free form useful additional information as comment

    //include::{partialsdir}/3rdparty-message.adoc[]
    ////

    This message needs to be included on any document referencing third party software
    repositories. Add the following line verbatim to the top of any such document:


    Please do not change this message without consultation. Thanks!

    ////

    [CAUTION]
    ====
    This page discusses third-party software sources not officially affiliated with or endorsed by the Fedora Project.
    Use them at your own discretion.
    Fedora recommends the use of free and open source software and avoidance of software encumbered by patents.
    ====



    [[overview]]
    == kubelet overview

    The \&#96;\&#96;\&#96;kubelet\&#96;\&#96;\&#96; is the Kubernetes agent that runs on every node in a cluster. \&#96;\&#96;\&#96;kubelet\&#96;\&#96;\&#96; is installed using the kubernetes rpm (_e.g._ \&#96;\&#96;\&#96;kubernetes1.30\&#96;\&#96;\&#96; is a versioned rpm for Kubernetes v1.30). The \&#96;\&#96;\&#96;kubelet\&#96;\&#96;\&#96; runs as a systemd service on Fedora. In early implementations, the \&#96;\&#96;\&#96;kubelet\&#96;\&#96;\&#96; was configured via link:https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/[flags] that were set in a systemd unit file and passed to the \&#96;\&#96;\&#96;kubelet\&#96;\&#96;\&#96; as command line parameters.

    In more recent versions of the \&#96;\&#96;\&#96;kubelet\&#96;\&#96;\&#96; these flags are deprecated in favor of a link:https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/[configuration file] that uses either JSON or YAML for the configuration syntax.

    The legacy non-versioned rpms use, by default, flags to configure the \&#96;\&#96;\&#96;kubelet\&#96;\&#96;\&#96;. Versioned rpms use the configuration file method.

    With both versioned and non-versioned rpms, all files, including systemd related files, can be erased during version updates (_e.g._ kubernetes1.29 to kubernetes1.30 - minor version updates). If these files are modified by the user then there is risk that useful or important changes can be lost. Systemd provides options that help safeguard against loss of node-specific configurations.

    [[systemd]]
    == Systemd configuration recommendations

    Flags for the \&#96;\&#96;\&#96;kubelet\&#96;\&#96;\&#96; running on a node are set in a systemd unit file with the relevant file dependent on which rpms are installed.

    The kubernetes rpm (_e.g_ kubernetes1.30 for version 1.30) installs the default \&#96;\&#96;\&#96;kubelet\&#96;\&#96;\&#96; systemd file at:

    [source,bash]
    ----
    /usr/lib/systemd/system/kubelet.service
    ----

    The kubernetes-kubeadm rpm installs an overriding \&#96;\&#96;\&#96;kubelet\&#96;\&#96;\&#96; unit file at:

    [source,bash]
    ----
    /usr/lib/systemd/system/kubelet.service.d/10-kubeadm.conf
    ----

    We strongly recommend to \&#42;not\&#42; modify either file as any changes could be lost during an update.

    As documented by the Kubernetes team (link:https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/kubelet-integration/\&#35;the-kubelet-drop-in-file-for-systemd)[https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/kubelet-integration/\&#35;the-kubelet-drop-in-file-for-systemd]), create the following directory for user managed, system-level systemd \&#96;\&#96;\&#96;kubelet\&#96;\&#96;\&#96; overrides:

    [source,bash]
    ----
    $ sudo mkdir -p /etc/systemd/system/kubelet.service.d/
    ----

    Then create a unit file (\&#96;\&#96;\&#96;.conf\&#96;\&#96;\&#96; extension required) and copy the file to the directory listed above. Settings in this file will override settings from either or both of the default systemd files.

    This file is not managed by the system package manager and will be unchanged by kubernetes version updates. Be sure to have software version control and/or a backup plan in place to avoid loss during a Fedora system upgrade or crash.

    [[configfile]]
    == Configuration file recommendations

    All versioned kubernetes rpms use a \&#96;\&#96;\&#96;kubelet\&#96;\&#96;\&#96; configuration file by default. If this file does not exist it will be created during the cluster instantiation process. The default configuration file location is:

    [source,bash]
    ----
    \&#35; default configuration file
    $ /var/lib/kubelet/config.yaml
    ----

    This file is \&#42;not\&#42; managed by rpm so will persist across kubernetes upgrades.

    [[configfile-dropin]]
    === Drop-in configuration file

    Kubernetes 1.30 and newer have a drop-in configuration file option that is \&#42;not\&#42; enabled by default.
    In a systemd file define a path using the \&#96;\&#96;\&#96;--config-dir\&#96;\&#96;\&#96; option:

    [source,bash]
    ----
    \&#35; define configdir
    --config-dir=/etc/kubernetes/kubelet.conf.d
    ----

    See link:https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/\&#35;kubelet-conf-d[the online documentation] for current information including an option to enable this feature for v1.28 or v1.29.

    [[configfile-merge-order]]
    === Configuration file merge order

    As the \&#96;\&#96;\&#96;kubelet\&#96;\&#96;\&#96; starts, configuration settings are merged in the following order (link:https://kubernetes.io/docs/tasks/administer-cluster/kubelet-config-file/\&#35;kubelet-configuration-merging-order[merge order documentation]):

    . Feature gates specified over the command line (lowest precedence).
    . The kubelet configuration.
    . Drop-in configuration files, according to sort order.
    . Command line arguments excluding feature gates (highest precedence).



    = Creating a Kubernetes cluster on Fedora
    Bradley G Smith,
    :page-aliases: kubernetes/kubeadm

    // Optional  free form useful additional information as comment

    //include::{partialsdir}/3rdparty-message.adoc[]
    ////

    This message needs to be included on any document referencing third party software
    repositories. Add the following line verbatim to the top of any such document:


    Please do not change this message without consultation. Thanks!

    ////

    [CAUTION]
    ====
    This page discusses third-party software sources not officially affiliated with or endorsed by the Fedora Project.
    Use them at your own discretion.
    Fedora recommends the use of free and open source software and avoidance of software encumbered by patents.
    ====



    [cluster-creation]
    == Creating a Kubernetes cluster with \&#96;\&#96;\&#96;kubeadm\&#96;\&#96;\&#96; using Fedora rpms

    Below is a guide to creating a functional Kubernetes cluster on a single Fedora machine that is suitable as a learning and exploring environment.
    This guide is not intended to create a production environment.

    The guide below generally follows and substantially borrows from the link:https://kubernetes.io/docs/setup/production-environment/tools/kubeadm/create-cluster-kubeadm/[Creating a cluster with kubeadm] guide created by the Kubernetes team.

    Fedora 41 has both versioned and unversioned (v1.29) Kubernetes rpms.
    Kubernetes 1.29 is no longer supported by the Kubernetes community.

    . Update system with DNF.
    Reboot if necessary, although a reboot can be deferred until after the next step.
    +
    [source,bash]
    ----
    sudo dnf update
    ----

    . Disable swap.
    The kubeadm installation process will generate a warning if swap is detected (see link:https://github.com/kubernetes/kubernetes/issues/53533[this ticket for details]).
    For a learning and lab environment it may be easiest to disable swap.
    Swap can be left enabled if desired and the kubeadm is configured to not stop if swap is detected.
    Modern Fedora systems use zram by default.
    Reboot after disabling swap.
    +
    [source,bash]
    ----
    sudo systemctl stop swap-create@zram0
    sudo dnf remove zram-generator-defaults
    sudo reboot now
    ----

    . SELinux.
    Most guides to installing Kubernetes on Fedora recommend that xref:getting-started-with-selinux.adoc[SELinux] be disabled.
    Kubernetes will work well with SELinux enabled and many containers will work as intended.
    If problems are encountered then disabling SELinux might be one option to try.
    See xref:selinux-changing-states-and-modes.adoc[the Quick Doc SELinux guide to changing SELinux states] for more information.

    . Disable the firewall.
    Kubeadm will generate an installation warning if the firewall is running.
    Disabling the firewall removes one source of complexity in a learning environment.
    Modern Fedora systems use firewalld.
    +
    [source,bash]
    ----
    sudo systemctl disable --now firewalld
    ----
    +
    See the Firewall Rules section in Roman Gherta's article link:https://fedoramagazine.org/kubernetes-with-cri-o-on-fedora-linux-39/[Kubernetes with CRI-O on Fedora 39] for the proper way to configure the Fedora firewall to work with Kubernetes,
    +
    The current list of ports and protocols used by a Kubernetes cluster can be found at link:https://kubernetes.io/docs/reference/networking/ports-and-protocols/[https://kubernetes.io/docs/reference/networking/ports-and-protocols/].

    . Install \&#96;iptables\&#96; and \&#96;iproute-tc.\&#96;
    Newer Kubernetes rpms include these packages by default.
    +
    [source,bash]
    ----
    sudo dnf install iptables iproute-tc
    ----

    . Configure IPv4 forwarding and bridge filters.
    Below copied from link:https://kubernetes.io/docs/setup/production-environment/container-runtimes/[https://kubernetes.io/docs/setup/production-environment/container-runtimes/]
    +
    [source,bash]
    ----
    sudo cat \&lt;\&lt;EOF | sudo tee /etc/modules-load.d/k8s.conf
    overlay
    br_netfilter
    EOF
    ----

    . Load the overlay and bridge filter modules.
    +
    [source,bash]
    ----
    sudo modprobe overlay
    sudo modprobe br_netfilter
    ----

    . Add required \&#96;sysctl\&#96; parameters and persist.
    +
    [source,bash]
    ----
    \&#35; sysctl params required by setup, params persist across reboots
    sudo cat \&lt;\&lt;EOF | sudo tee /etc/sysctl.d/k8s.conf
    net.bridge.bridge-nf-call-iptables  = 1
    net.bridge.bridge-nf-call-ip6tables = 1
    net.ipv4.ip_forward                 = 1
    EOF
    ----

    . Apply \&#96;sysctl\&#96; parameters without a reboot.
    +
    [source,bash]
    ----
    sudo sysctl --system
    ----

    . Verify \&#96;br_filter\&#96; and overlay modules are loaded.
    +
    [source,bash]
    ----
    lsmod | grep br_netfilter
    lsmod | grep overlay
    ----

    . Verify that the \&#96;net.bridge.bridge-nf-call-iptables\&#96;, \&#96;net.bridge.bridge-nf-call-ip6tables\&#96;, and \&#96;net.ipv4.ip_forward\&#96; system variables are set to \&#96;1\&#96; in your sysctl configuration by running the following command:
    +
    [source,bash]
    ----
    sysctl net.bridge.bridge-nf-call-iptables net.bridge.bridge-nf-call-ip6tables net.ipv4.ip_forward
    ----

    . Install a link:https://kubernetes.io/docs/setup/production-environment/container-runtimes/[container runtime].
    CRI-O is installed in this example.
    Containerd is also an option.
    Note: If using CRI-O, verify that the major:minor version of cri-o is the same as the version of Kubernetes (installed below).
    CRI-O rpms are versioned like Kubernetes rpms.
    Install the CRI-O version that matches the target Kubernetes version.
    +
    [source,bash]
    ----
    sudo dnf install cri-o1.31 containernetworking-plugins
    ----

    . Check for available Kubernetes versions.
    If uncertain about what versions of Kubernetes are currently available in Fedora 41 or newer the following command may be useful.
    In the example below, Kubernetes 1.29, 1.30, 1.31, and 1.32 versioned rpms are available in Fedora 41.
    Current information on supported releases and end-of-life dates can be found on the link:https://kubernetes.io/releases/[Release History] page maintained by the Kubernetes team.
    +
    [source,bash]
    ----
    sudo dnf list kubernetes1.??
    ----
    +
    Output will look like:
    +
    [source]
    ----
    \&gt; sudo dnf list kubernetes1.??
    Updating and loading repositories:
    Repositories loaded.
    Available packages
    kubernetes1.29.x86_64 1.29.11-2.fc41 updates
    kubernetes1.30.x86_64 1.30.7-1.fc41  updates
    kubernetes1.31.x86_64 1.31.3-1.fc41  updates
    kubernetes1.32.x86_64 1.32.0-1.fc41  updates
    ----

    . Install Kubernetes.
    In this example, all three Kubernetes applications (\&#96;kubectl\&#96;, \&#96;kubelet\&#96;, and \&#96;kubeadm\&#96;) are installed on this single node machine.
    Please see the notes above on recommended packages for control plane or worker nodes if the cluster will have both types of machines.
    +
    [source,bash]
    ----
    sudo dnf install kubernetes1.31 kubernetes1.31-kubeadm kubernetes1.31-client
    ----

    . Start and enable cri-o.
    +
    [source,bash]
    ----
    sudo systemctl enable --now crio
    ----

    . Pull needed system container images for Kubernetes.
    This is strictly optional.
    The \&#96;\&#96;\&#96;kubeadm init\&#96;\&#96;\&#96; command below will pull images, if needed.
    +
    [source,bash]
    ----
    sudo kubeadm config images pull
    ----

    . Start and enable \&#96;kubelet\&#96;.
    Kubelet will be in a crash loop until the cluster is initialized in the next step.
    +
    [source,bash]
    ----
    sudo systemctl enable --now kubelet
    ----

    . Initialize the cluster.
    +
    [source,bash]
    ----
    sudo kubeadm init --pod-network-cidr=10.244.0.0/16
    ----

    . kubeadm will generate output to the terminal tracking initialization steps.
    If successful, the output below is displayed.
    At this point there is a cluster running on this single machine.
    After kubeadm finishes you should see:
    +
    ----
    Your Kubernetes control-plane has initialized successfully!

    To start using your cluster, you need to run the following as a regular user:

    mkdir -p $HOME/.kube
    sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
    sudo chown $(id -u):$(id -g) $HOME/.kube/config

    Alternatively, if you are the root user, you can run:

    export KUBECONFIG=/etc/kubernetes/admin.conf
    ----

    . The steps listed above allow a non-root user to use \&#96;kubectl\&#96;, the Kubernetes command line tool.
    Run these commands now.
    +
    [source,bash]
    ----
    mkdir -p $HOME/.kube
    sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
    sudo chown $(id -u):$(id -g) $HOME/.kube/config
    ----

    . Allow the control plane machine to also run pods for applications.
    Otherwise more than one machine is needed in the cluster.
    +
    [source,bash]
    ----
    kubectl taint nodes --all node-role.kubernetes.io/control-plane-
    ----

    . Install flannel into the cluster to provide cluster networking.
    There are many other networking solutions besides flannel.
    Flannel is straightforward and suitable for this guide.
    +
    [source,bash]
    ----
    kubectl apply -f https://github.com/coreos/flannel/raw/master/Documentation/kube-flannel.yml
    ----

    . Display list of running pods in the cluster.
    All pods should display a status of Running.
    A status of CrashLoopBackOff may show up for the coredns pod.
    This happens commonly when installing Kubernetes on a virtual machine and the DNS service in the cluster may not select the proper network.
    Use your favorite internet search engine to find possible solutions. See also the troubleshooting section below for two possible solutions.
    +
    [source,bash]
    ----
    kubectl get pods --all-namespaces
    ----

    At this point there is a single machine in the cluster running the control plane and available for work as a node.

    Upgrades to Kubernetes clusters requires care and planning.
    See link:https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/[Upgrading kubeadm clusters] for more information.

    The xref:dnf.adoc\&#35;sect-using-dnf-plugin[DNF Versionlock plugin] is useful in blocking unplanned updates to Kubernetes rpms.
    Occasionally, the Kubernetes version in a Fedora release reaches end-of-life and a new version of Kubernetes is added to the repositories.
    Or, an upgrade to Fedora on a cluster machine will also result in a different version of Kubernetes.
    Once DNF Versionlock is installed, the following command will hold kubernetes rpms and the cri-o rpm at the 1.31 major:minor version but still allow patch updates to occur:
    [source,bash]
    ----
    sudo dnf versionlock add kubernetes\&#42;-1.31.\&#42; cri-o-1.31.\&#42;
    ----

    [cluster-creation-troubleshooting]
    == Troubleshooting CrashLoopBackOff

    The CoreDNS team provides a guide to link:https://coredns.io/plugins/loop/\&#35;troubleshooting-loops-in-kubernetes-clusters[troubleshooting loops in Kubernetes clusters] with several options to help resolve the problem.

    A 'quick and dirty' option, as described by the CoreDNS team, is to edit the CoreDNS configmap using \&#96;kubectl\&#96;. In the configmap, replace \&#96;forward . /etc/resolv.conf\&#96; with the IP address of the DNS server for your network. If the DNS server has an IP address of \&#96;192.168.110.201\&#96; then the result would look like \&#96;forward . 192.168.110.201\&#96;. To edit the CoreDNS configmap use:

    [source,bash]
    ----
    kubectl edit configmap coredns -n kube-system
    ----

    \&#96;kubectl\&#96; will launch the editor for your instance of Fedora. The Fedora default is \&#96;nano\&#96; which can be easily changed.

    Another option is to disable the systemd-resolved stub resolving on the machine hosting the cluster using the code below. Many thanks for @jasonbrooks (https://pagure.io/user/jasonbrooks) for his review and recommendations.

    [source,bash]
    ----
    sudo mkdir -p /etc/systemd/resolved.conf.d/
    sudo cat \&lt;\&lt;EOF | sudo tee /etc/systemd/resolved.conf.d/stub-listener.conf
    [Resolve]
    DNSStubListener=no
    EOF
    ----




    = Versioned CRI-O and CRI-Tools RPMs
    Bradley G Smith,

    // Optional  free form useful additional information as comment

    //include::{partialsdir}/3rdparty-message.adoc[]
    ////

    This message needs to be included on any document referencing third party software
    repositories. Add the following line verbatim to the top of any such document:


    Please do not change this message without consultation. Thanks!

    ////

    [CAUTION]
    ====
    This page discusses third-party software sources not officially affiliated with or endorsed by the Fedora Project.
    Use them at your own discretion.
    Fedora recommends the use of free and open source software and avoidance of software encumbered by patents.
    ====



    [[sect-overview]]
    == Overview

    link:https://cri-o.io[CRI-O] and link:https://github.com/kubernetes-sigs/cri-tools[CRI-Tools] are independent software packages available in Fedora repositories that are version matched to Kubernetes. If Kubernetes 1.34 is installed, then, when installed, CRI-O and CRI-Tools should also have the same minor version, _i.e_ 1.34.

    [[sect-cri-o]]
    == CRI-O

    The \&#42;\&#42;C\&#42;\&#42;ontainer \&#42;\&#42;R\&#42;\&#42;untime \&#42;\&#42;I\&#42;\&#42;nterface(link:https://kubernetes.io/docs/concepts/architecture/cri/[CRI]) is the plugin interface used by the \&#96;\&#96;\&#96;kubelet\&#96;\&#96;\&#96; to communicate with the container runtime on each node that launches pods and their containers. There are several implementations of CRI including link:https://cri-o.io[CRI-O] and link://https://containerd.io/[containerd].

    CRI-O is available in Fedora repositories as versioned rpms in parallel with Kubernetes. If kubernetes1.34 is installed and CRI-O is the designated CRI implementation, then cri-o1.34 needs to be installed.

    === Configuration

    CRI-O configuration options are set in \&#96;/etc/crio/crio.conf\&#96;. This file is managed by rpm and therefore replaced when a versioned CRI-O package is replaced by another package (not counting patch level updates) such as when the cri-o1.34 rpm is replaced by the cri-o1.31 rpm. One method to create and manage custom CRI-O configuration settings that persist across updates is to take advantage of CRI-O support for a drop-in configuration. The default drop-in subdirectory is \&#96;/etc/crio/crio.conf.d/\&#96;. Settings in configuration files placed in the drop-in directory take precedence over the same setting in the default configuration file \&#96;/etc/crio/crio.conf\&#96;. If multiple drop-in configuration files have the same setting, the file that is sorted last in lexical order will have precedence. See link:https://github.com/cri-o/cri-o/blob/main/docs/crio.conf.d.5.md[crio.conf.d] man file for additional information.

    See xref:using-kubernetes-kubelet.adoc[Resilient kubelet configuration] for related \&#96;kublet\&#96; configuration options.

    [[sect-cri-tools]]
    == CRI-Tools

    link:https://github.com/kubernetes-sigs/cri-tools/[CRI-Tools] is a command line interface to any implementation of the CLI. CRI-Tools is available from the Kubernetes team. It is required when using \&#96;\&#96;\&#96;kubeadm\&#96;\&#96;\&#96; to initialize a cluster.

    CRI-Tools is available in Fedora repositories as versioned rpms in parallel with Kubernetes. If kubernetes1.34 and kubernetes1.34-kubeadm are installed then cri-tools1.34 needs to be installed.

    [[sect-retirement]]
    == Retirement

    Versioned packages for CRI-O and CRI-Tools are retired from Fedora repositories when the corresponding Kubernetes version is retired. See xref:using-kubernetes-versioned.adoc\&#35;sect-retirement[Versioned rpm retirement policy] for additional information.


    = Using Shared System Certificates
    NITISH SHARMA ; Mirek Jahoda ; Petr Bokoc
    //:imagesdir: ./images


    The Shared System Certificates storage enables NSS, GnuTLS, OpenSSL, and Java to share a default source for retrieving system certificate anchors and black list information. By default, the trust store contains the Mozilla CA list, including positive and negative trust. The system allows updating of the core Mozilla CA list or choosing another certificate list.


    == Using the System-wide Trust Store

    In Fedora, the consolidated system-wide trust store is located in the \&#96;/etc/pki/ca-trust/\&#96; and \&#96;/usr/share/pki/ca-trust-source/\&#96; directories. The trust settings in \&#96;/usr/share/pki/ca-trust-source/\&#96; are processed with lower priority than settings in \&#96;/etc/pki/ca-trust/\&#96;.

    Certificate files are treated depending on the subdirectory they are installed to the following directories:

    \&#42; for trust anchors
    \&#42;\&#42; \&#96;/usr/share/pki/ca-trust-source/anchors/\&#96; or
    \&#42;\&#42; \&#96;/etc/pki/ca-trust/source/anchors/\&#96;
    \&#42; for distrusted certificates
    \&#42;\&#42; \&#96;/usr/share/pki/ca-trust-source/blocklist/\&#96; or
    \&#42;\&#42; \&#96;/etc/pki/ca-trust/source/blocklist/\&#96;
    \&#42; for certificates in the extended BEGIN TRUSTED file format
    \&#42;\&#42; \&#96;/usr/share/pki/ca-trust-source/\&#96; or
    \&#42;\&#42; \&#96;/etc/pki/ca-trust/source/\&#96;

    NOTE: In a hierarchical cryptographic system, a trust anchor is an authoritative entity which is assumed to be trustworthy. For example, in X.509 architecture, a root certificate is a trust anchor from which a chain of trust is derived. The trust anchor must be put in the possession of the trusting party beforehand to make path validation possible.



    == Adding New Certificates

    Often, system administrators want to install a certificate into the trust store. This can be done with the [command]\&#96;trust anchor\&#96; sub-command of the [command]\&#96;trust\&#96; command, as described in xref:managing-trusted-system-certificates[Managing Trusted System Certificates].

    Alternatively, you can simply copy the certificate file in the PEM or DER file format to the \&#96;/etc/pki/ca-trust/source/anchors/\&#96; directory, followed by running the [command]\&#96;update-ca-trust\&#96; command, for example:

    [subs='+quotes,macros']
    ----
    \&#35; cp _~/certificate-trust-examples/Cert-trust-test-ca.pem_ _/etc/pki/ca-trust/source/anchors/_
    ----

    ----
    \&#35; update-ca-trust
    ----

    The [command]\&#96;update-ca-trust\&#96; command ensures that the certificate bundles in application-specific formats, such as Java keystore, are regenerated.

    [NOTE]
    ====
    The certificates installed in the above steps cannot be removed with the [command]\&#96;trust anchor --remove\&#96;.
    ====

    [NOTE]
    ====
    While the Firefox browser is able to use an added certificate without executing [command]\&#96;update-ca-trust\&#96;, it is recommended to run [command]\&#96;update-ca-trust\&#96; after a CA change. Also note that browsers, such as Firefox, Epiphany, or Chromium, cache files, and you might need to clear the browser's cache or restart your browser to load the current system certificates configuration.
    ====



    == Managing Trusted System Certificates

    To list, extract, add, remove, or change trust anchors, use the [command]\&#96;trust\&#96; command. To see the built-in help for this command, enter it without any arguments or with the [option]\&#96;--help\&#96; directive:

    [subs='quotes,_macros']
    ----
    $ [command]\&#96;trust\&#96;
    usage: trust command \&amp;lt;args\&amp;gt;\&#8230;

    Common trust commands are:
    list             List trust or certificates
    extract          Extract certificates and trust
    extract-compat   Extract trust compatibility bundles
    anchor           Add, remove, change trust anchors
    dump             Dump trust objects in internal format

    See 'trust \&amp;lt;command\&amp;gt; --help' for more information
    ----

    To list all system trust anchors and certificates, use the [command]\&#96;trust list\&#96; command:

    [subs='quotes,_macros']
    ----
    $ [command]\&#96;trust list\&#96;
    pkcs11:id=%d2%87%b4%e3%df%37%27%93%55%f6%56%ea%81%e5%36%cc%8c%1e%3f%bd;type=cert
    type: certificate
    label: ACCVRAIZ1
    trust: anchor
    category: authority

    pkcs11:id=%a6%b3%e1%2b%2b%49%b6%d7%73%a1%aa%94%f5%01%e7%73%65%4c%ac%50;type=cert
    type: certificate
    label: ACEDICOM Root
    trust: anchor
    category: authority
    \&#8230;
    [output_has_been_truncated]
    ----



    To store a trust anchor into the system-wide trust store, use the [command]\&#96;trust anchor\&#96; sub-command and specify a _path.to_ a certificate, for example:

    [subs='macros']
    ----
    \&#35; trust anchor pass:quotes[_path.to/certificate.crt_]
    ----

    To remove a certificate, use either a _path.to_ a certificate or an ID of a certificate:

    [subs='macros']
    ----
    \&#35; trust anchor --remove pass:quotes[_path.to/certificate.crt_]
    \&#35; trust anchor --remove pass:quotes[_'pkcs11:id=%AA%BB%CC%DD%EE;type=cert'_]
    ----

    .More information

    All sub-commands of the [command]\&#96;trust\&#96; commands offer a detailed built-in help, for example:

    ----
    $ trust list --help
    usage: trust list --filter=\&lt;what\&gt;

    --filter=\&lt;what\&gt;     filter of what to export
    ca-anchors        certificate anchors
    blacklist         blacklisted certificates
    trust-policy      anchors and blacklist (default)
    certificates      all certificates
    pkcs11:object=xx  a PKCS\&#35;11 URI
    --purpose=\&lt;usage\&gt;   limit to certificates usable for the purpose
    server-auth       for authenticating servers
    client-auth       for authenticating clients
    email             for email protection
    code-signing      for authenticating signed code
    1.2.3.4.5\&#8230;      an arbitrary object id
    -v, --verbose       show verbose debug output
    -q, --quiet         suppress command output
    ----





    == Additional Resources

    For more information, see the following man pages:

    \&#42; \&#96;update-ca-trust(8)\&#96;
    \&#42; \&#96;trust(1)\&#96;




    = Using YubiKeys with Fedora
    The Fedora Documentation Team; Alexander Wellbrock


    == What is a YubiKey?

    A YubiKey is a small USB and NFC based device, a so called https://developers.yubico.com/Developer_Program/Guides/YubiKey_Hardware.html[hardware security token], with modules for many security related use-cases. It generates one time passwords (OTPs), stores private keys and in general implements different authentication protocols. They are created and sold via a company called http://yubico.com/[Yubico].

    For more information about YubiKey features, see their https://yubico.com/products/[product page].

    == How do I get a YubiKey?

    You can purchase a YubiKey from http://store.yubico.com/[Yubico's website].

    == Consider a backup YubiKey

    As soon as you start working with security tokens you have to account for the potential to lock yourself out of accounts tied to these tokens. As hardware security tokens are unique and designed to be extremely hard to copy you can't just make a backup of it like you can with software vaults like Keepass or AndOTP. Because of this all registrations you do with your primary key you should immediately do with a second backup key that you store in a secure location like a safe or at least always leave at home.

    In practice this means to register both hardware tokens with your linux and web accounts, generate private keys twice and configure both public keys at e.g. github.

    == Storage limitations

    For some features private keys and other secrets are stored on the YubiKey. Each feature has it's own storage space and hence https://support.yubico.com/hc/en-us/articles/360013790319-How-many-accounts-can-I-register-my-YubiKey-with-[maximum number of credential slots]:

    - OTP - Unlimited, as only one secret per key is required
    - FIDO U2F - Unlimited, as only one secret per key is required
    - FIDO2 - 25 credentials
    - OATH - 32 credentials
    - PIV - 24 x509 certificates and their respective private keys
    - OpenPGP - 3 keys; one for encryption, signing and authentication each

    == Using a YubiKey to authenticate to a machine running Fedora

    Local system authentication uses https://www.redhat.com/sysadmin/pluggable-authentication-modules-pam[Pluggable Authentication Modules (PAM)]. You have two options here: pam_yubico and pam_u2f. The former is required for YubiKeys without FIDO2/U2F. If your key supports the FIDO2 standard depends on firmware and hardware model.

    The setup is as follows: install the PAM module, register a YubiKey with your user account, create base configuration for either of the two authentication options and then choose the PAM configuration you want to use the YubiKey with.

    === Dependencies

    The packages required for both PAM modules are available in the official repositories.

    [NOTE]
    ===
    Note that one difference of both PAM modules is, with pam_yubico you don't need to touch your yubikey, it's enough if the key is inserted in your device. With pam_u2f you have to touch your key every time authentication is required.
    ===

    ==== For pam_yubico

    Install the PAM yubico module from the official repositories:

    [source,_bash]
    […]$ sudo dnf install pam_yubico

    ==== For pam_u2f

    Install the PAM u2f module and the CLI tool from the official repositories:

    [source,_bash]
    […]$ sudo dnf install pam-u2f pamu2fcfg

    === Base configuration files

    ==== For pam_yubico

    There are two ways to configure the YubiKey PAM module to authenticate users. Either via the YubiCloud or using challenge-response. The YubiCloud is the standard method but depends on Yubico's cloud to validate your OTPs and hence requires constant internet access.

    Create two base configuration files in /etc/pam.d/yubikey-required and yubikey-sufficient.

    For YubiCloud use the following:

    [source]
    \&#35;%PAM-1.0
    auth       required     pam_yubico.so id=[Your API Client ID] key=[Your API Client Key]

    [source]
    \&#35;%PAM-1.0
    auth       sufficient     pam_yubico.so id=[Your API Client ID] key=[Your API Client Key]

    [CAUTION]
    ====
    Note that the key is optional but without it there is no TLS verification which makes this susceptible to MitM attacks by default. Obtain a key at https://upgrade.yubico.com/getapikey[Yubico].
    ====

    [CAUTION]
    ====
    Note that the online auth method won't work if the device is offline and can't reach the YubiCloud.
    ====

    [NOTE]
    ====
    If you have SELinux on the enforcing mode (the default mode), you should flip on the allow_ypbind boolean first, because pam_yubico needs to be able to connect to Yubico's online authentication. servers.

    [source,_bash]
    […]$ sudo setsebool -P allow_ypbind=1
    ====

    For challenge-response use the following:

    [source]
    \&#35;%PAM-1.0
    auth       required     pam_yubico.so mode=challenge-response

    [source]
    \&#35;%PAM-1.0
    auth       sufficient     pam_yubico.so mode=challenge-response

    [NOTE]
    ====
    You may add the debug option at the end of these lines right after the mode option to get troubleshooting information in journald.
    ====

    If you want to use both methods for different use-cases just create the respective configuration files and use them as includes as described in the next section accordingly.

    ==== For pam_u2f

    Create two base configuration files in /etc/pam.d/u2f-required and u2f-sufficient.

    [source]
    \&#35;%PAM-1.0
    auth       required     pam_u2f.so

    [source]
    \&#35;%PAM-1.0
    auth       sufficient     pam_u2f.so

    [NOTE]
    ====
    You may add the debug option at the end of these lines right after the mode option to get troubleshooting information in journald.
    ====

    === Register YubiKey(s) with your local account(s)

    ==== For pam_yubico

    If you use the online YubiCloud method you need the ID of your YubiKey. For this just enter the key and retrieve an OTP code with a short press on the button and extract the first 12 characters - this is your key ID.

    [source]
    cccccbcgebif | bclbtjihhbfbduejkuhgvhkehnicrfdj

    Create a configuration file ~/.yubico/authorized_keys with your user account followed by key IDs separated by colons.

    [source]
    fedora-user:cccccbcgebif[:\&lt;another-key-id\&gt;]

    Alternatively, activate challenge-response in slot 2 and register with your user account.
    The first command (ykman) can be skipped if you already have a challenge-response credential stored in slot 2 on your YubiKey. (Verify with 'ykman otp info')
    Repeat both or only the last step if you have a backup key (strongly recommended).

    [source,_bash]
    […]$ ykman otp chalresp --generate --touch 2
    […]$ ykpamcfg -2

    [source]
    Stored initial challenge and expected response in '/home/\&lt;username\&gt;/.yubico/challenge-1\&#8230;5'.

    Or for any other system user using sudo.

    [source,_bash]
    […]$ sudo -u someuser ykpamcfg -2

    ==== For pam_u2f

    Use the tool pamu2fcfg to retrieve a configuration line that goes into ~/.config/Yubico/u2f_keys. This configuration line consists of a username and a part tied to a key separated by colon.

    [source]
    fedora-user:owBYtPIH2yzjlSQaRrVcxB\&#8230;Pg==,es256,+presence

    If the key is PIN protected you'll be asked to enter the PIN for this operation.

    [source,_bash]
    […]$ mkdir -p ~/.config/Yubico
    […]$ pamu2fcfg \&gt; ~/.config/Yubico/u2f_keys

    If you have a backup key add it with the --nouser option and append it to the existing key (line). (All output should end up in the same line.)

    [source,_bash]
    […]$ pamu2fcfg -n \&gt;\&gt; ~/.config/Yubico/u2f_keys


    === Configure desired PAM modules

    Next configure PAM to accept a YubiKey as a means of authentication. There are many options in /etc/pam.d to modify and add a YubiKey, but the most common use-cases are:

    - /etc/pam.d/login
    - /etc/pam.d/gdm
    - /etc/pam.d/sudo
    - /etc/pam.d/sshd

    In a PAM configuration file if using {yubikey,u2f}-sufficient add an include line before or if using {yubikey,u2f}-required add it after a line that reads 'auth substack system-auth' or 'auth include system-auth'. An include of yubikey-sufficient looks like this:

    [source]
    auth include yubikey-sufficient

    The following example sets a YubiKey OTP as 'sufficient' factor for terminal login. This means that a YubiKey alone is enough to authenticate a user when logging in on a terminal.

    Open /etc/pam.d/login with your editor of choice. Find the line that reads 'auth substack system-auth'. Above that, insert the following:

    [source]
    auth include yubikey-sufficient

    The result looks similar to this:

    [source]
    \&#35;%PAM-1.0
    auth       include      yubikey-sufficient
    auth       substack     system-auth
    auth       include      postlogin
    account    required     pam_nologin.so
    account    include      system-auth
    password   include      system-auth
    \&#35; pam_selinux.so close should be the first session rule
    session    required     pam_selinux.so close
    session    required     pam_loginuid.so
    \&#35; pam_selinux.so open should only be followed by sessions to be executed in the user context
    session    required     pam_selinux.so open
    session    required     pam_namespace.so
    session    optional     pam_keyinit.so force revoke
    session    include      system-auth
    session    include      postlogin
    -session   optional     pam_ck_connector.so

    Next time you open a console (local, not ssh session) and attempt to login you should be prompted \&#96;YubiKey for '\&lt;user\&gt;':\&#96;. Tap your YubiKey to input an OTP and you will be logged without entering a password.

    [CAUTION]
    ====
    When using the yubikey-required option make sure to test this thoroughly in another session without closing your current one to mitigate locking yourself out of the system.
    ====

    To add a YubiKey to more than terminal login, like local sshd servers, sudo or GDM login, add the respective auth include to one of the other configuration files in /etc/pam.d.

    == Customizing a YubiKey with Fedora

    A YubiKey comes pre-configured for Yubico OTP, but apart from that it uses default PINs for every other feature which you'll most likely want to change before use. There is software for customizing the YubiKey in the official repositories.

    There are essentially two tools to use together with their respective GUI variants. 'yubikey-manager' and 'ykpersonalize'. The former is newer but supports less options than the latter. For all available options install both.

    [source,_bash]
    […]$ sudo dnf install ykpers

    There is a gui for this command:

    [source,_bash]
    […]$ sudo dnf install yubikey-personalization-gui

    There is a more recent, simpler tool, ykman:

    [source,_bash]
    […]$ sudo dnf install yubikey-manager

    YubiKey manager also has a gui:

    [source,_bash]
    […]$ sudo dnf install yubikey-manager-qt

    === Writing a new static password to the second slot of the key

    Newer YubiKeys (YubiKey 2+) have the ability to store two separate configurations. The first is generally used for OTPs, the second for a strong, static password. If the button is pressed shortly, something up to 1.5 seconds, the first configuration is triggered. If the button is pressed longer, in the range of 2.5 to 5 seconds, the second configuration is triggered.

    Write a static key using ykman otp static.

    [source,_bash]
    […]$ ykman otp static 2 cbdefghijklnrtuv

    A more elaborate example: write a new static key to the second configuration slot using a specific AES key.

    [source,_bash]
    […]$ ykpersonalize -2 -o append-cr -a 123456deadcafebeef65432112345678 -o -man-update

    This writes a static key to the YubiKey based on the 32-byte AES key specified with the -a option. The -2 option sets the second slot as target. The other two options are a matter of personal taste. The append-cr option sends a carriage return as the last character of the key. That way I do not have to press \&lt;ENTER\&gt; myself. The -man-update option disables easy updating of the static key in the YubiKey. Enabling this will allow for altering the static password without the use of ykpersonalize.

    === Writing a new AES key to the first slot of the key

    [CAUTION]
    ====
    Slot 1 is special as it contains a factory credential already uploaded to YubiCloud. Deleting and recreating a Yubico OTP secret and uploading it to YubiCloud yourself will put a special mark on it which has consequences: service providers might not trust such a key and Yubico might delete those secrets at anytime for practically any reason.
    ====

    If we want to write a new configuration to the first slot of the key, we need to specify some more options. If you want to be able to upload you key to Yubico, in order to authenticate against their servers, remember what the values are that you use below. You will need them later on.

    [source,_bash]
    […]$ ykpersonalize -1 -o fixed=vvhhhrhkhgidic -o uid=deadbeefcafe -a 123456deadcfaebeef65432112345678 -o append-cr

    The -1 option tells ykpersonalize to use the first configuration. The fixed option specifies the public ID of the YubiKey. This is referred to as the 'prefix' later on, when we go uploading it. The value you use here has to start with 'ff' in hex or 'vv' in modhex (xref:\&#35;_what_is_modhex[see below]). Yubico enforces this when you try to upload your key to their servers. The value for the fixed option can be up to 16 characters in length.

    As part of the OTP, you can specify an internal identifier for your key. This is what the uid option does. The value is in plain hex, not modhex and ''exactly'' 12 character long.

    The -a option, again, is the 32-byte AES key and append-cr appends a carriage return to my key as the last character.

    When you hit the \&lt;ENTER\&gt; key, the ykpersonalize program will present you with my options and ask for
    confirmation before continuing:

    ====
    Firmware version 2.1.1 Touch level 1795 Program sequence 3
    Configuration data to be written to key configuration 1:

    fixed: m:vvhhhrhkhgidic
    uid: h:deadbeefcafe
    key: h:123456deadcfaebeef65432112345678
    acc_code: h:000000000000
    ticket_flags: APPEND_CR
    config_flags:

    Commit? (y/n) [n]:
    ====

    After pressing 'y', I am able to generate OTPs with my new key!

    ==== What is modhex?

    When plugged in, the operating system treats the YubiKey as a USB keyboard. USB keyboards send scancodes to the operating system, which the operating system then interprets as keystrokes. The YubiKey has to make sure no ambiguity arises: there are many different kinds of keyboard layouts and the scancodes have to be interpreted as the same character on machines using every random keyboard layout out there. To fix this, the people of Yubico have created 'modhex', which is a modified representation of hexadecimal characters that uses only 'safe' characters. 'Safe' characters are basically characters which have the same scancode on all keyboard layouts.

    ==== Uploading the generated AES key to Yubico

    If you want to customize your YubiKey's AES key but still want to use it to authenticate through Yubico's servers, you can upload the key through https://upgrade.yubico.com/getapikey/. You will need to enter your email address and YubiKey's OTP.

    === Update the PINs of the PIV module

    The https://www.yubico.com/authentication-standards/smart-card/[Personal Identity Verification (PIV)] module stores private keys and corresponding certificate files for purposes such as encryption, authentication and signatures. If your YubiKey supports this you want to change the PIN and PUK as well as the Management Key.

    Set the PIN.

    [source,_bash]
    […]$ ykman piv access change-pin
    Enter the current PIN: 123456
    Enter the new PIN: \&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;
    Repeat for confirmation: \&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;
    New PIN set.

    Set the PUK.

    [source,_bash]
    […]$ ykman piv access change-puk
    Enter the current PUK: 12345678
    Enter the new PUK: \&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;
    Repeat for confirmation: \&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;
    New PUK set.

    Update the Management Key.

    [source,_bash]
    […]$ ykman piv access change-management-key --generate --protect
    Enter the current management key [blank to use default key]:
    Enter PIN: \&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;

    You can now safely use the PIV module to generate private keys and store certificates.

    === Change the PIN of the FIDO2 module

    https://www.yubico.com/authentication-standards/fido2/[FIDO2] is an open authentication standard and encompasses sub-standards and protocols to either provide two-factor or even passwordless authentication methods.

    One interesting use case of the FIDO module to note is storing OpenSSH public-key identities, which modern OpenSSH agents can pick up right away and use. This makes ssh keys quite portable.

    If your key supports FIDO change its pin with ykman fido access like this:

    [source,_bash]
    […]$ ykman piv access change-pin
    Enter the current PIN: 123456
    Enter the new PIN: \&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;
    Repeat for confirmation: \&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;
    New PIN set.

    === Configure a password for OATH

    The OATH feature provides TOTP and HOTP authentication protocols. It can be protected with a passphrase to access and generate OTP codes. This is different from the Yubico OTP feature, which uses a single stored secret on the YubiKey for challenge-response.

    Change the OATH password with:

    [source,_bash]
    […]$ ykman oath access change
    Enter the new password:
    Repeat for confirmation:

    Configure your device to remember this password so you don't have to re-enter it anymore.

    [source,_bash]
    […]$ ykman oath access remember

    == Using the YubiKey to authenticate against OpenSSH servers

    Using FIDO2 and OpenSSH 8.2+ you can generate OpenSSH keys that are only usable if the YubiKey is connected. It's possible to protect the key usage by either presence or presence + pin-entry.

    Generate a public key on every host you intend to use the private key, so an OpenSSH agent may discover it:

    [source,_bash]
    […]$ ssh-keygen -t ed25519-sk

    Generate the public key and store its identity in the FIDO2 module to make the private-public key-pair portable:

    [source,_bash]
    […]$ ssh-keygen -t ed25519-sk -O resident -O application=ssh:fedora -O verify-required

    [NOTE]
    So called resident keys require that the private key is protected by a PIN.

    === Alternative for keys without FIDO2 support

    If the key does not support FIDO2 you have to use an alternative method via the PIV module and PKCS\&#35;11.

    Create an ED25519 private key inside the PIV module, requiring pin entry upon use and always require a touch of the YubiKey button:

    [source,_bash]
    […]$ ykman piv keys generate --algorithm ED25519 --pin-policy ONCE --touch-policy ALWAYS 9a public.pem
    Enter PIN: \&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;

    The slot 9a on the key is dedicated to authentication. There are https://docs.yubico.com/yesdk/users-manual/application-piv/slots.html[more slots] for features like encryption or signing.

    Create a certificate in this same slot for the PIV/PKCS\&#35;11 library:

    [source,_bash]
    […]$ ykman piv certificates generate --subject 'CN=OpenSSH' --hash-algorithm SHA384 9a pubkey.pem
    Enter PIN: \&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;
    Touch your YubiKey…

    Now generate a public key from the X.509 certificate stored on the YubiKey. Other features like resident keys work the same as with the FIDO2 approach, but you have to add the additional option as shown below.

    [source,_bash]
    […]$ ssh-keygen -D /usr/lib/libykcs11.so -e

    Login to systems with this public key:

    [source,_bash]
    […]$ ssh -I /usr/lib/libykcs11.so user@remote.example.org

    The ssh-agent may also load keys from the YubiKey with:

    [source,_bash]
    […]$ ssh -s /usr/lib/libykcs11.so

    == Using the YubiKey to authenticate to websites

    As of 2019, there is work in place to attempt to standardize using a YubiKey on the web. The new standard is called WebAuthn, and you can learn more about it here: https://www.yubico.com/solutions/webauthn/. For now, the easiest way to see which platforms support the YubiKey is by browsing https://www.yubico.com/works-with-yubikey/catalog/[yubico's catalog].

    As an alternative to Yubico OTP or WebAuthn, neither of which require storage of credentials on the YubiKey by default, you may also use plain old TOTP like employed in most websites today. There are desktop and at least android apps to work with this conveniently. You may store up to 32 TOTP credentials on a YubiKey 5.

    Install the desktop application from the official repositories:

    [source,_bash]
    […]$ sudo dnf install -y yubioath-desktop

    Add an TOTP account with ykman like this:

    [source,_bash]
    […]$ ykman oath accounts add google \&lt;TOTP secret\&gt;

    Retrieve a TOTP code like this:

    [source,_bash]
    […]$ ykman oath accounts code google


    = Viewing logs in Fedora
    JJ Asghar; hector louzao ; Mirek Jahoda
    //:imagesdir: ./images

    Log files contain messages about the system, including the kernel, services, and applications running on it.
    These contain information that helps troubleshoot issues, or simply monitor system functions.
    Fedora uses the https://freedesktop.org/wiki/Software/systemd/[systemd] system and service manager.
    With systemd, messages for most services are now stored in the systemd journal which is a binary file that must be accessed using the \&#96;journalctl\&#96; command.

    System tools that do not use systemd for their logs continue to place them as plain text files in the \&#96;/var/log/\&#96; directory.
    In Fedora, there are two ways of accessing system logs:

    \&#42; The command line
    \&#42; A GUI applications


    == Using the command line to view log files

    The \&#96;journalctl\&#96; command can be used to view messages in the system journal on the command line.
    For plain text log files, generic tools may be used:

    \&#42; \&#96;cat\&#96;, \&#96;more\&#96;, \&#96;less\&#96;, \&#96;tail\&#96;, or \&#96;head\&#96;.
    \&#42; the \&#96;grep\&#96; command to search for specific information.
    \&#42; any text editor of your choosing (nano/pico/vim/emacs)

    Please note that you may require \&#96;sudo\&#96; access to view these files.

    === Using journalctl to view system information

    \&#42; To view all collected journal entries, simply use:

    [source,bash]
    ----
    journalctl
    ----

    \&#42; To view a logs related to a specific file, you can provide the \&#96;journalctl\&#96; command with a filepath.
    The example shown below shows all logs of the kernel device node \&#96;/dev/sda\&#96;:
    ----
    $ journalctl /dev/sda
    ----

    \&#42; To view log for the current boot use the \&#96;-b\&#96; option :
    ----
    $ journalctl -b
    ----

    \&#42; To view kernel logs for the previous boot, you can add the \&#96;-k\&#96; option:
    ----
    $ journalctl -k -b -1
    ----


    === Using journalctl to view log information for a specific service

    \&#42; To filter logs to only see ones matching the 'foo' systemd service:
    ----
    $ journalctl -b _SYSTEMD_UNIT=foo
    ----

    \&#42; Matches can be combined.
    For example, to view logs for systemd-units that match \&#96;foo\&#96;, and the PID \&#96;number\&#96;:
    ----
    $ journalctl -b _SYSTEMD_UNIT=foo _PID=number
    ----

    \&#42; If the separator '+' is used, two expressions may be combined in a logical OR.
    For example, to view all messages from the \&#96;foo\&#96; service process with the \&#96;PID\&#96; plus all messages from the \&#96;foo1\&#96; service (from any of its processes):
    ----
    $ journalctl -b _SYSTEMD_UNIT=foo _PID=number + _SYSTEMD_UNIT=foo1
    ----

    \&#42; If two matches refer to the same field, all entries matching either expression are shown.
    For example, this command will show logs matching a systemd-unit \&#96;foo\&#96; or a systemd-unit \&#96;foo1\&#96;:
    ----
    $ journalctl -b _SYSTEMD_UNIT=foo _SYSTEMD_UNIT=foo1
    ----


    NOTE: The files for service modification are stored in a directory within \&#96;\&#42;/etc/systemd/system\&#42;\&#96;, to know more about systemd, please refer to \&lt;\&lt;understanding-and-administering-systemd.adoc\&#35;Understanding Systemd Services\&gt;\&gt;


    === Using journalctl to view older logs

    \&#42; To view older logs use the \&#96;--list-boots\&#96; option :

    This will show a tabular list of boot numbers, their IDs, and the timestamps of the first and last message pertaining to the boot:

    ----
    $ journalctl --list-boots
    -8 42cdeac65d494e938b9cb92f315b08a4 Mon 2018-11-12 10:36:42 CET—Mon 2018-11-12 20:08:24 CET
    -7 c110d2b8705345b786fe310de628bfc7 Tue 2018-11-13 10:29:27 CET—Tue 2018-11-13 10:04:00 CET
    ----

    with this ID you can use \&#96;journalctl\&#96; as usual :

    ----
    $ journalctl --boot=ID _SYSTEMD_UNIT=foo
    ----

    \&#42; To know more about \&#96;journalctl\&#96;, read the man page:
    ----
    $ man journalctl
    ----



    == Using Gnome Logs to view log files

    The \&#96;GNOME Logs\&#96; application provides a convenient GUI tool to view the systemd journal.
    \&#96;GNOME Logs\&#96; is not currently installed by default on Fedora systems.

    \&#42; You can install \&#96;Gnome Logs\&#96; using the default software installation application on your system.
    On a Fedora Workstation install running the GNOME desktop:

    \&#42;\&#42; Press the \&#96;Super\&#96; key
    \&#42;\&#42; Type \&#96;Software\&#96;
    \&#42;\&#42; In the \&#96;Search\&#96; field type \&#96;Logs\&#96; and choose the \&#96;GNOME Logs\&#96; item from the list of results
    \&#42;\&#42; Install the application

    \&#42; You can also install \&#96;GNOME Logs\&#96; using the command line with \&#96;dnf\&#96;:

    ----
    $ sudo dnf install gnome-logs
    ----

    In \&#96;GNOME Logs\&#96;, you can filter for time periods, search within logs, and display categories.

    \&#42; To select a log file type, from the side bar of GNOME Logs, select the type to view.
    \&#42; To select a time period, from the menu bar, click \&#96;Log\&#96;, and select a time period.
    \&#42; To search within logs, select a log file from the results pane.
    . Click the search icon.
    . Enter one or more search criterion in the search field.



    = Getting started with SELinux
    The Fedora Docs Team; Peter Boy (pboy)
    :page-aliases: getting-started-with-selinux.adoc
    //:imagesdir: ./images

    == Introduction to SELinux

    Security Enhanced Linux (SELinux) provides an additional layer of system security. SELinux fundamentally answers the question: _May \&lt;subject\&gt; do \&lt;action\&gt; to \&lt;object\&gt;?_, for example: _May a web server access files in users' home directories?_

    The standard access policy based on the user, group, and other permissions, known as Discretionary Access Control (DAC), does not enable system administrators to create comprehensive and fine-grained security policies, such as restricting specific applications to only viewing log files, while allowing other applications to append new data to the log files.

    SELinux implements Mandatory Access Control (MAC). Every process and system resource has a special security label called a _SELinux context_. A SELinux context, sometimes referred to as a _SELinux label_, is an identifier which abstracts away the system-level details and focuses on the security properties of the entity. Not only does this provide a consistent way of referencing objects in the SELinux policy, but it also removes any ambiguity that can be found in other identification methods; for example, a file can have multiple valid path names on a system that makes use of bind mounts.

    The SELinux policy uses these contexts in a series of rules which define how processes can interact with each other and the various system resources. By default, the policy does not allow any interaction unless a rule explicitly grants access.

    [NOTE]
    ====
    It is important to remember that SELinux policy rules are checked after DAC rules. SELinux policy rules are not used if DAC rules deny access first, which means that no SELinux denial is logged if the traditional DAC rules prevent the access.
    ====

    SELinux contexts have several fields: user, role, type, and security level. The SELinux type information is perhaps the most important when it comes to the SELinux policy, as the most common policy rule which defines the allowed interactions between processes and system resources uses SELinux types and not the full SELinux context. SELinux types usually end with \&#96;_t\&#96;. For example, the type name for the web server is \&#96;httpd_t\&#96;. The type context for files and directories normally found in \&#96;/var/www/html/\&#96; is \&#96;httpd_sys_content_t\&#96;. The type contexts for files and directories normally found in \&#96;/tmp\&#96; and \&#96;/var/tmp/\&#96; is \&#96;tmp_t\&#96;. The type context for web server ports is \&#96;http_port_t\&#96;.

    For example, there is a policy rule that permits Apache (the web server process running as \&#96;httpd_t\&#96;) to access files and directories with a context normally found in \&#96;/var/www/html/\&#96; and other web server directories (\&#96;httpd_sys_content_t\&#96;). There is no allow rule in the policy for files normally found in \&#96;/tmp\&#96; and \&#96;/var/tmp/\&#96;, so access is not permitted. With SELinux, even if Apache is compromised, and a malicious script gains access, it is still not able to access the \&#96;/tmp\&#96; directory.

    [\&#35;fig-intro-httpd-mysqld]
    .SELinux allows the Apache process running as httpd_t to access the /var/www/html/ directory and it denies the same process to access the /data/mysql/ directory because there is no allow rule for the httpd_t and mysqld_db_t type contexts). On the other hand, the MariaDB process running as mysqld_t is able to access the /data/mysql/ directory and SELinux also correctly denies the process with the mysqld_t type to access the /var/www/html/ directory labeled as httpd_sys_content_t.
    image::selinux-intro-apache-mariadb.png[SELinux_Apache_MariaDB_example]

    [discrete]
    === Additional resources
    To better understand SELinux basic concepts, see the following documentation:

    \&#42; link:++https://people.redhat.com/duffy/selinux/selinux-coloring-book_A4-Stapled.pdf++[The SELinux Coloring Book]

    \&#42; link:++https://videos.cdn.redhat.com/summit2015/presentations/13893_security-enhanced-linux-for-mere-mortals.pdf++[SELinux for Mere Mortals]

    \&#42; link:++http://selinuxproject.org/page/FAQ++[SELinux Wiki FAQ]

    \&#42; link:++https://github.com/SELinuxProject/selinux-notebook/releases/++[The SELinux Notebook]


    == Benefits of running SELinux

    SELinux provides the following benefits:

    \&#42; All processes and files are labeled. SELinux policy rules define how processes interact with files, as well as how processes interact with each other. Access is only allowed if an SELinux policy rule exists that specifically allows it.

    \&#42; Fine-grained access control. Stepping beyond traditional UNIX permissions that are controlled at user discretion and based on Linux user and group IDs, SELinux access decisions are based on all available information, such as an SELinux user, role, type, and, optionally, a security level.

    \&#42; SELinux policy is administratively-defined and enforced system-wide.

    \&#42; Improved mitigation for privilege escalation attacks. Processes run in domains, and are therefore separated from each other. SELinux policy rules define how processes access files and other processes. If a process is compromised, the attacker only has access to the normal functions of that process, and to files the process has been configured to have access to. For example, if the Apache HTTP Server is compromised, an attacker cannot use that process to read files in user home directories, unless a specific SELinux policy rule was added or configured to allow such access.

    \&#42; SELinux can be used to enforce data confidentiality and integrity, as well as protecting processes from untrusted inputs.

    However, SELinux is not:

    \&#42; antivirus software,

    \&#42; replacement for passwords, firewalls, and other security systems,

    \&#42; all-in-one security solution.

    SELinux is designed to enhance existing security solutions, not replace them. Even when running SELinux, it is important to continue to follow good security practices, such as keeping software up-to-date, using hard-to-guess passwords, or firewalls.


    == SELinux examples

    The following examples demonstrate how SELinux increases security:

    \&#42; The default action is deny. If an SELinux policy rule does not exist to allow access, such as for a process opening a file, access is denied.

    \&#42; SELinux can confine Linux users. A number of confined SELinux users exist in SELinux policy. Linux users can be mapped to confined SELinux users to take advantage of the security rules and mechanisms applied to them. For example, mapping a Linux user to the SELinux \&#96;user_u\&#96; user, results in a Linux user that is not able to run (unless configured otherwise) set user ID (setuid) applications, such as [command]\&#96;sudo\&#96; and [command]\&#96;su\&#96;, as well as preventing them from executing files and applications in their home directory. If configured, this prevents users from executing malicious files from their home directories.

    \&#42; Increased process and data separation. Processes run in their own domains, preventing processes from accessing files used by other processes, as well as preventing processes from accessing other processes. For example, when running SELinux, unless otherwise configured, an attacker cannot compromise a Samba server, and then use that Samba server as an attack vector to read and write to files used by other processes, such as MariaDB databases.

    \&#42; SELinux helps mitigate the damage made by configuration mistakes. Domain Name System (DNS) servers often replicate information between each other in what is known as a zone transfer. Attackers can use zone transfers to update DNS servers with false information. When running the Berkeley Internet Name Domain (BIND) as a DNS server in Fedora, even if an administrator forgets to limit which servers can perform a zone transfer, the default SELinux policy prevents zone files footnote:[Text files that include information, such as host name to IP address mappings, that are used by DNS servers.] from being updated using zone transfers, by the BIND \&#96;named\&#96; daemon itself, and by other processes.

    \&#42; See the link:++https://www.networkworld.com++[NetworkWorld.com] article, link:++https://www.networkworld.com/article/2283723/lan-wan/a-seatbelt-for-server-software--selinux-blocks-real-world-exploits.html++[A seatbelt for server software: SELinux blocks real-world exploits]footnote:[Marti, Don. 'A seatbelt for server software: SELinux blocks real-world exploits'. Published 24 February 2008. Accessed 27 August 2009: link:++https://www.networkworld.com/article/2283723/lan-wan/a-seatbelt-for-server-software--selinux-blocks-real-world-exploits.html++[].], for background information about SELinux, and information about various exploits that SELinux has prevented.


    == SELinux architecture

    SELinux is a Linux Security Module (LSM) that is built into the Linux kernel. The SELinux subsystem in the kernel is driven by a security policy which is controlled by the administrator and loaded at boot. All security-relevant, kernel-level access operations on the system are intercepted by SELinux and examined in the context of the loaded security policy. If the loaded policy allows the operation, it continues. Otherwise, the operation is blocked and the process receives an error.

    SELinux decisions, such as allowing or disallowing access, are cached. This cache is known as the Access Vector Cache (AVC). When using these cached decisions, SELinux policy rules need to be checked less, which increases performance. Remember that SELinux policy rules have no effect if DAC rules deny access first.


    == SELinux states and modes

    SELinux can run in one of three modes: disabled, permissive, or enforcing.

    Disabled mode is strongly discouraged; not only does the system avoid enforcing the SELinux policy, it also avoids labeling any persistent objects such as files, making it difficult to enable SELinux in the future.

    In permissive mode, the system acts as if SELinux is enforcing the loaded security policy, including labeling objects and emitting access denial entries in the logs, but it does not actually deny any operations. While not recommended for production systems, permissive mode can be helpful for SELinux policy development.

    Enforcing mode is the default, and recommended, mode of operation; in enforcing mode SELinux operates normally, enforcing the loaded security policy on the entire system.

    Use the [command]\&#96;setenforce\&#96; utility to change between enforcing and permissive mode. Changes made with [command]\&#96;setenforce\&#96; do not persist across reboots. To change to enforcing mode, enter the [command]\&#96;setenforce 1\&#96; command as the Linux root user. To change to permissive mode, enter the [command]\&#96;setenforce 0\&#96; command. Use the [command]\&#96;getenforce\&#96; utility to view the current SELinux mode:

    ----
    [~]\&#35; getenforce
    Enforcing
    ----

    ----
    [~]\&#35; setenforce 0
    [~]\&#35; getenforce
    Permissive
    ----

    ----
    [~]\&#35; setenforce 1
    [~]\&#35; getenforce
    Enforcing
    ----

    In Fedora, you can set individual domains to permissive mode while the system runs in enforcing mode. For example, to make the \&#96;httpd_t\&#96; domain permissive:

    ----
    [~]\&#35; semanage permissive -a httpd_t
    ----







    = Changing SELinux States and Modes
    The Fedora Docs Team; Peter Boy (pboy)
    :page-aliases: changing-selinux-states-and-modes.adoc
    //:imagesdir: ./images


    // NOTE (TODO): several links (URLs) could be replaced with URLs when the appropriate docs become available on fp.org


    == Permanent changes in SELinux states and modes

    As discussed in xref:selinux-getting-started.adoc\&#35;_SELinux_states_and_modes[Getting started with SELinux] SELinux can be enabled or disabled. When enabled, SELinux has two modes: enforcing and permissive.

    Use the [command]\&#96;getenforce\&#96; or [command]\&#96;sestatus\&#96; commands to check in which mode SELinux is running. The [command]\&#96;getenforce\&#96; command returns \&#96;Enforcing\&#96;, \&#96;Permissive\&#96;, or \&#96;Disabled\&#96;.

    The [command]\&#96;sestatus\&#96; command returns the SELinux status and the SELinux policy being used:

    [source,bash]
    ----
    [~]$ sestatus
    SELinux status:                 enabled
    SELinuxfs mount:                /sys/fs/selinux
    SELinux root directory:         /etc/selinux
    Loaded policy name:             targeted
    Current mode:                   enforcing
    Mode from config file:          enforcing
    Policy MLS status:              enabled
    Policy deny_unknown status:     allowed
    Memory protection checking:     actual (secure)
    Max kernel policy version:      31
    ----

    [NOTE]
    ====
    When systems run SELinux in permissive mode, users and processes can label various file-system objects incorrectly. File-system objects created while SELinux is disabled are not labeled at all. This behavior causes problems when changing to enforcing mode because SELinux relies on correct labels of file-system objects.

    To prevent incorrectly labeled and unlabeled files from causing problems, file systems are automatically relabeled when changing from the disabled state to permissive or enforcing mode. In permissive mode, use the [command]\&#96;fixfiles -F onboot\&#96; command as root to create \&#96;/.autorelabel\&#96; file containing the \&#96;-F\&#96; option to ensure that files are relabeled upon next reboot.
    ====


    == Enabling SELinux

    When enabled, SELinux can run in one of two modes: enforcing or permissive. The following sections show how to permanently change into these modes.

    While enabling SELinux on systems that previously had it disabled, to avoid problems, such as systems unable to boot or process failures, follow this procedure.

    .Prerequisites

    \&#42; The [package]\&#96;selinux-policy-targeted\&#96;, [package]\&#96;selinux-policy\&#96;, [package]\&#96;libselinux-utils\&#96;, and [package]\&#96;grubby\&#96; packages are installed. To check that a particular package is installed:
    +
    [subs='quotes']
    ----
    $ \&#42;rpm -q _package_name_\&#42;
    ----

    .Procedure

    . If your system has SELinux disabled at the kernel level (this is the recommended way, see xref:changing-selinux-states-and-modes.adoc\&#35;_disabling_selinux[]), change this first. Check if you have the \&#96;selinux=0\&#96; option in your kernel command line:
    +
    [subs='quotes']
    ----
    $ \&#42;cat /proc/cmdline\&#42;
    BOOT_IMAGE=\&#8230; \&#8230; selinux=0
    ----

    .. Remove the \&#96;selinux=0\&#96; option from the bootloader configuration using [command]\&#96;grubby\&#96;:
    +
    [subs='quotes']
    ----
    $ \&#42;sudo grubby --update-kernel ALL --remove-args selinux\&#42;
    ----

    .. The change applies after you restart the system in one of the following steps.

    . Ensure the file system is relabeled on the next boot:
    +
    [subs='quotes']
    ----
    $ \&#42;sudo fixfiles onboot\&#42;
    ----

    . Enable SELinux in permissive mode. For more information, see xref:changing-selinux-states-and-modes.adoc\&#35;_changing_to_permissive_mode[].

    . Restart your system:
    +
    [subs='quotes']
    ----
    $ \&#42;reboot\&#42;
    ----

    . Check for SELinux denial messages.
    +
    [subs='quotes']
    ----
    $ \&#42;sudo ausearch -m AVC,USER_AVC,SELINUX_ERR,USER_SELINUX_ERR -ts recent\&#42;
    ----

    . If there are no denials, switch to enforcing mode. For more information, see xref:changing-selinux-states-and-modes.adoc\&#35;_changing_to_enforcing_mode[].

    To run custom applications with SELinux in enforcing mode, choose one of the following scenarios:

    \&#42; Run your application in the \&#96;unconfined_service_t\&#96; domain.
    // See \&lt;\&lt;Targeted_Policy-Unconfined_Processes\&gt;\&gt; for more information.

    \&#42; Write a new policy for your application. See the link:https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/using_selinux/writing-a-custom-selinux-policy_using-selinux[Writing a custom SELinux policy] chapter in the link:https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/using_selinux/index[RHEL 8 Using SELinux] document for more information.


    === Changing to permissive mode

    Use the following procedure to permanently change SELinux mode to permissive. When SELinux is running in permissive mode, SELinux policy is not enforced. The system remains operational and SELinux does not deny any operations but only logs AVC messages, which can be then used for troubleshooting, debugging, and SELinux policy improvements. Each AVC is logged only once in this case.

    .Prerequisites

    \&#42; The \&#96;selinux-policy-targeted\&#96;, \&#96;libselinux-utils\&#96;, and \&#96;policycoreutils\&#96; packages are installed on your system.
    \&#42; The \&#96;selinux=0\&#96; or \&#96;enforcing=0\&#96; kernel parameters are not used.

    .Procedure

    . Open the \&#96;/etc/selinux/config\&#96; file in a text editor of your choice, for example:

    ----
    \&#35; vi /etc/selinux/config
    ----

    . Configure the \&#96;SELINUX=permissive\&#96; option:
    [subs='quotes']
    ----
    \&#35; This file controls the state of SELinux on the system.
    \&#35; SELINUX= can take one of these three values:
    \&#35;       enforcing - SELinux security policy is enforced.
    \&#35;       permissive - SELinux prints warnings instead of enforcing.
    \&#35;       disabled - No SELinux policy is loaded.
    SELINUX=\&#42;permissive\&#42;
    \&#35; SELINUXTYPE= can take one of these two values:
    \&#35;       targeted - Targeted processes are protected,
    \&#35;       mls - Multi Level Security protection.
    SELINUXTYPE=targeted
    ----

    . Restart the system:
    +
    [subs='quotes']
    ----
    \&#35; \&#42;reboot\&#42;
    ----


    === Changing to enforcing mode

    Use the following procedure to switch SELinux to enforcing mode. When SELinux is running in enforcing mode, it enforces the SELinux policy and denies access based on SELinux policy rules. In Fedora, enforcing mode is enabled by default when the system was initially installed with SELinux.

    .Prerequisites

    \&#42; The \&#96;selinux-policy-targeted\&#96;, \&#96;libselinux-utils\&#96;, and \&#96;policycoreutils\&#96; packages are installed on your system.

    \&#42; The \&#96;selinux=0\&#96; or \&#96;enforcing=0\&#96; kernel parameters are not used.

    .Procedure

    . Open the \&#96;/etc/selinux/config\&#96; file in a text editor of your choice, for example:
    +
    ----
    \&#35; vi /etc/selinux/config
    ----

    . Configure the \&#96;SELINUX=enforcing\&#96; option:
    +
    [subs='quotes']
    ----
    \&#35; This file controls the state of SELinux on the system.
    \&#35; SELINUX= can take one of these three values:
    \&#35;       enforcing - SELinux security policy is enforced.
    \&#35;       permissive - SELinux prints warnings instead of enforcing.
    \&#35;       disabled - No SELinux policy is loaded.
    SELINUX=\&#42;enforcing\&#42;
    \&#35; SELINUXTYPE= can take one of these two values:
    \&#35;       targeted - Targeted processes are protected,
    \&#35;       mls - Multi Level Security protection.
    SELINUXTYPE=targeted
    ----

    . Save the change, and restart the system:
    +
    [subs='quotes']
    ----
    \&#35; reboot
    ----
    +
    On the next boot, SELinux relabels all the files and directories within the system and adds SELinux context for files and directories that were created when SELinux was disabled.

    .Verification

    . After the system restarts, confirm that the \&#96;getenforce\&#96; command returns \&#96;Enforcing\&#96;:
    +
    ----
    $ getenforce
    Enforcing
    ----

    [NOTE]
    ====
    After changing to enforcing mode, SELinux may deny some actions because of incorrect or missing SELinux policy rules. To view what actions SELinux denies, enter the following command as root:
    [subs='quotes']
    ----
    \&#35; ausearch -m AVC,USER_AVC,SELINUX_ERR,USER_SELINUX_ERR -ts today
    ----
    Alternatively, with the [package]\&#96;setroubleshoot-server\&#96; package installed, enter:
    [subs='quotes']
    ----
    \&#35; grep 'SELinux is preventing' /var/log/messages
    ----

    Standard users can use the GUI \&#96;setroubleshoot\&#96; to file bugs directly to Bugzilla.

    If SELinux is active and the Audit daemon (auditd) is not running on your system, then search for certain SELinux messages in the output of the dmesg command:
    ----
    \&#35; dmesg | grep -i -e type=1300 -e type=1400
    ----

    If SELinux denies some actions, see the link:https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/using_selinux/troubleshooting-problems-related-to-selinux_using-selinux[Troubleshooting problems related to SELinux] chapter in the link:https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/using_selinux/index[RHEL 8 Using SELinux] document for information about troubleshooting.
    ====


    == Disabling SELinux

    Use the following procedure to permanently disable SELinux.

    [IMPORTANT]
    ====
    When SELinux is disabled, SELinux policy is not loaded at all; it is not enforced and AVC messages are not logged. Therefore, all benefits of running SELinux listed in xref:changing-selinux-states-and-modes.adoc\&#35;_benefits_of_selinux[Benefits of SELinux] are lost.

    It is recommended to use permissive mode instead of permanently disabling SELinux. See xref:changing-selinux-states-and-modes.adoc\&#35;_changing_to_permissive_mode[] for more information about permissive mode.
    ====

    [WARNING]
    ====
    Disabling SELinux using the SELINUX=disabled option in the /etc/selinux/config results in a process in which the kernel boots with SELinux enabled and switches to disabled mode later in the boot process. Because memory leaks and race conditions causing kernel panics can occur, prefer disabling SELinux by adding the selinux=0 parameter to the kernel command line as described in Changing SELinux modes at boot time if your scenario really requires to completely disable SELinux.
    ====

    .Prerequisites

    \&#42; The [package]\&#96;grubby\&#96; package is installed:
    +
    [subs='quotes']
    ----
    $ \&#42;rpm -q grubby\&#42;
    grubby-_version_
    ----

    .Procedure

    . Open the \&#96;/etc/selinux/config\&#96; file in a text editor of your choice, for example:
    +
    [subs='quotes']
    ----
    \&#35; vi /etc/selinux/config
    ----

    . Configure the SELINUX=disabled option:
    +
    [subs='quotes']
    ----
    \&#35; This file controls the state of SELinux on the system.
    \&#35; SELINUX= can take one of these three values:
    \&#35;       enforcing - SELinux security policy is enforced.
    \&#35;       permissive - SELinux prints warnings instead of enforcing.
    \&#35;       disabled - No SELinux policy is loaded.
    SELINUX=disabled
    \&#35; SELINUXTYPE= can take one of these two values:
    \&#35;       targeted - Targeted processes are protected,
    \&#35;       mls - Multi Level Security protection.
    SELINUXTYPE=targeted
    ----

    . Save the change, and restart your system:
    ----
    \&#35; reboot
    ----

    .Verification

    \&#42; After reboot, confirm that the [command]\&#96;getenforce\&#96; command returns \&#96;Disabled\&#96;:
    +
    [subs='quotes']
    ----
    $ \&#42;getenforce\&#42;
    Disabled
    ----


    == Changing SELinux Modes at Boot Time

    On boot, you can set several kernel parameters to change the way SELinux runs:

    enforcing=0::  Setting this parameter causes the system to start in permissive mode, which is useful when troubleshooting issues. Using permissive mode might be the only option to detect a problem if your file system is too corrupted. Moreover, in permissive mode, the system continues to create the labels correctly. The AVC messages that are created in this mode can be different than in enforcing mode.
    +
    In permissive mode, only the first denial from a series of the same denials is reported. However, in enforcing mode, you might get a denial related to reading a directory, and an application stops. In permissive mode, you get the same AVC message, but the application continues reading files in the directory and you get an AVC for each denial in addition.

    selinux=0::  This parameter causes the kernel to not load any part of the SELinux infrastructure. The init scripts notice that the system booted with the [option]\&#96;selinux=0\&#96; parameter and touch the \&#96;/.autorelabel\&#96; file. This causes the system to automatically relabel the next time you boot with SELinux enabled.
    +
    [IMPORTANT]
    ====
    Using the [option]\&#96;selinux=0\&#96; parameter is not recommended. To debug your system, prefer using permissive mode.
    ====

    autorelabel=1::  This parameter forces the system to relabel similarly to the following commands:
    +
    ----
    \&#35; touch /.autorelabel
    \&#35; reboot
    ----
    +
    If a file system contains a large amount of mislabeled objects, start the system in permissive mode to make the autorelabel process successful.

    For additional SELinux-related kernel boot parameters, such as [option]\&#96;checkreqprot\&#96;, see the \&#96;kernel-parameters.txt\&#96; file. This file is available in the source package of your Linux kernel (.src.rpm). To download the source package containing the currently used kernel:
    ----
    [~]\&#35; dnf download --source kernel
    ----


    = Troubleshooting Problems Related to SELinux
    Mat McCabe; Joe Walker; Peter Boy (pboy)
    :page-aliases: troubleshooting_selinux.adoc
    //:imagesdir: ./images

    If you plan to enable SELinux on systems where it has been previously disabled or if you run a service in a non-standard configuration, you might need to troubleshoot situations potentially blocked by SELinux. Note that in most cases, SELinux denials are signs of misconfiguration.

    == Identifying SELinux denials

    Follow only the necessary steps from this procedure; in most cases, you need to perform just step 1.

    \&#42;Procedure\&#42;

    . When your scenario is blocked by SELinux, the [command]\&#96;/var/log/audit/audit.log\&#96; file is the first place to check for more information about a denial. To query Audit logs, use the \&#96;ausearch\&#96; tool. Because the SELinux decisions, such as allowing or disallowing access, are cached and this cache is known as the Access Vector Cache (AVC), use the \&#96;AVC\&#96; and \&#96;USER_AVC\&#96; values for the message type parameter, for example:
    +
    ----
    \&#35; ausearch -m AVC,USER_AVC,SELINUX_ERR,USER_SELINUX_ERR -ts recent
    ----
    +
    If there are no matches, check if the Audit daemon is running. If it does not, repeat the denied scenario after you start auditd and check the Audit log again.

    . In case auditd is running, but there are no matches in the output of ausearch, check messages provided by the systemd Journal:
    +
    ----
    \&#35; journalctl -t setroubleshoot
    ----

    . If SELinux is active and the Audit daemon is not running on your system, then search for certain SELinux messages in the output of the dmesg command:
    +
    ----
    \&#35; dmesg | grep -i -e type=1300 -e type=1400
    ----

    . Even after the previous three checks, it is still possible that you have not found anything. In this case, AVC denials can be silenced because of \&#96;dontaudit\&#96; rules.
    +
    To temporarily disable \&#96;dontaudit\&#96; rules, allowing all denials to be logged:
    +
    ----
    \&#35; semodule -DB
    ----
    +
    After re-running your denied scenario and finding denial messages using the previous steps, the following command enables \&#96;dontaudit\&#96; rules in the policy again:
    +
    ----
    \&#35; semodule -B
    ----

    . If you apply all four previous steps, and the problem still remains unidentified, consider if SELinux really blocks your scenario:
    \&#42; Switch to permissive mode:
    +
    ----
    \&#35; setenforce 0
    $ getenforce
    Permissive
    ----
    \&#42; Repeat your scenario.

    If the problem still occurs, something different than SELinux is blocking your scenario.

    == Analyzing SELinux denial messages

    After identifying that SELinux is blocking your scenario, you might need to analyze the root cause before you choose a fix.

    \&#42;Prerequisites\&#42;

    \&#42;\&#42; The \&#96;policycoreutils-python-utils\&#96; and \&#96;setroubleshoot-server\&#96; packages are installed on your system.

    \&#42;Procedure\&#42;

    . List more details about a logged denial using the \&#96;sealert\&#96; command, for example:
    +
    ----
    $ sealert -l '\&#42;'
    SELinux is preventing /usr/bin/passwd from write access on the file
    /root/test.

    \&#42;\&#42;\&#42;\&#42;\&#42;  Plugin leaks (86.2 confidence) suggests \&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;

    If you want to ignore passwd trying to write access the test file,
    because you believe it should not need this access.
    Then you should report this as a bug.
    You can generate a local policy module to dontaudit this access.
    Do
    \&#35; ausearch -x /usr/bin/passwd --raw | audit2allow -D -M my-passwd
    \&#35; semodule -X 300 -i my-passwd.pp

    \&#42;\&#42;\&#42;\&#42;\&#42;  Plugin catchall (14.7 confidence) suggests \&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;\&#42;

    \&#8230;

    Raw Audit Messages
    type=AVC msg=audit(1553609555.619:127): avc:  denied  { write } for
    pid=4097 comm='passwd' path='/root/test' dev='dm-0' ino=17142697
    scontext=unconfined_u:unconfined_r:passwd_t:s0-s0:c0.c1023
    tcontext=unconfined_u:object_r:admin_home_t:s0 tclass=file permissive=0

    ..

    Hash: passwd,passwd_t,admin_home_t,file,write
    ----

    . If the output obtained in the previous step does not contain clear suggestions:

    \&#42; Enable full-path auditing to see full paths to accessed objects and to make additional Linux Audit event fields visible:
    +
    ----
    \&#35; auditctl -w /etc/shadow -p w -k shadow-write
    ----

    \&#42; Clear the \&#96;setroubleshoot\&#96; cache:
    +
    ----
    \&#35; rm -f /var/lib/setroubleshoot/setroubleshoot.xml
    ----

    \&#42; Reproduce the problem.
    \&#42; Repeat step 1.
    +
    After you finish the process, disable full-path auditing:
    +
    ----
    \&#35; auditctl -W /etc/shadow -p w -k shadow-write
    ----

    . If \&#96;sealert\&#96; returns only \&#96;catchall\&#96; suggestions or suggests adding a new rule using the \&#96;audit2allow\&#96; tool, match your problem with examples listed and explained in SELinux denials in the Audit log.

    \&#42;Additional resources\&#42;

    \&#42; \&#96;sealert(8)\&#96; man page

    == Fixing analyzed SELinux denials

    In most cases, suggestions provided by the \&#96;sealert\&#96; tool give you the right guidance about how to fix problems related to the SELinux policy. See Analyzing SELinux denial messages for information how to use \&#96;sealert\&#96; to analyze SELinux denials.

    Be careful when the tool suggests using the \&#96;audit2allow\&#96; tool for configuration changes. You should not use \&#96;audit2allow\&#96; to generate a local policy module as your first option when you see an SELinux denial. Troubleshooting should start with a check if there is a labeling problem. The second most often case is that you have changed a process configuration, and you forgot to tell SELinux about it.

    \&#42;\&#42;Labeling problems\&#42;\&#42;

    A common cause of labeling problems is when a non-standard directory is used for a service. For example, instead of using \&#96;/var/www/html/\&#96; for a website, an administrator might want to use \&#96;/srv/myweb/\&#96;. On Red Hat Enterprise Linux, the \&#96;/srv\&#96; directory is labeled with the \&#96;var_t\&#96; type. Files and directories created in /srv inherit this type. Also, newly-created objects in top-level directories, such as \&#96;/myserver\&#96;, can be labeled with the \&#96;default_t\&#96; type. SELinux prevents the Apache HTTP Server (\&#96;httpd\&#96;) from accessing both of these types. To allow access, SELinux must know that the files in \&#96;/srv/myweb/\&#96; are to be accessible by \&#96;httpd\&#96;:

    ----
    \&#35; semanage fcontext -a -t httpd_sys_content_t '/srv/myweb(/.\&#42;)?'
    ----

    This \&#96;semanage\&#96; command adds the context for the \&#96;/srv/myweb/\&#96; directory and all files and directories under it to the SELinux file-context configuration. The \&#96;semanage\&#96; utility does not change the context. As root, use the \&#96;restorecon\&#96; utility to apply the changes:

    ----
    \&#35; restorecon -R -v /srv/myweb
    ----

    \&#42;\&#42;Incorrect Context\&#42;\&#42;
    The \&#96;matchpathcon\&#96; utility checks the context of a file path and compares it to the default label for that path. The following example demonstrates the use of \&#96;matchpathcon\&#96; on a directory that contains incorrectly labeled files:

    ----
    $ matchpathcon -V /var/www/html/\&#42;
    /var/www/html/index.html has context unconfined_u:object_r:user_home_t:s0, should be system_u:object_r:httpd_sys_content_t:s0
    /var/www/html/page1.html has context unconfined_u:object_r:user_home_t:s0, should be system_u:object_r:httpd_sys_content_t:s0
    ----

    In this example, the \&#96;index.html\&#96; and \&#96;page1.html\&#96; files are labeled with the \&#96;user_home_t\&#96; type. This type is used for files in user home directories. Using the \&#96;mv\&#96; command to move files from your home directory may result in files being labeled with the \&#96;user_home_t\&#96; type. This type should not exist outside of home directories. Use the \&#96;restorecon\&#96; utility to restore such files to their correct type:

    ----
    \&#35; restorecon -v /var/www/html/index.html
    restorecon reset /var/www/html/index.html context unconfined_u:object_r:user_home_t:s0-\&gt;system_u:object_r:httpd_sys_content_t:s0
    ----

    To restore the context for all files under a directory, use the \&#96;-R\&#96; option:

    ----
    \&#35; restorecon -R -v /var/www/html/
    restorecon reset /var/www/html/page1.html context unconfined_u:object_r:samba_share_t:s0-\&gt;system_u:object_r:httpd_sys_content_t:s0
    restorecon reset /var/www/html/index.html context unconfined_u:object_r:samba_share_t:s0-\&gt;system_u:object_r:httpd_sys_content_t:s0
    ----

    \&#42;\&#42;Confined applications configured in non-standard ways\&#42;\&#42;

    Services can be run in a variety of ways. To account for that, you need to specify how you run your services. You can achieve this through SELinux booleans that allow parts of SELinux policy to be changed at runtime. This enables changes, such as allowing services access to NFS volumes, without reloading or recompiling SELinux policy. Also, running services on non-default port numbers requires policy configuration to be updated using the \&#96;semanage\&#96; command.

    For example, to allow the Apache HTTP Server to communicate with MariaDB, enable the \&#96;httpd_can_network_connect_db\&#96; boolean:

    ----
    \&#35; setsebool -P httpd_can_network_connect_db on
    ----

    Note that the \&#96;-P\&#96; option makes the setting persistent across reboots of the system.

    If access is denied for a particular service, use the \&#96;getsebool\&#96; and \&#96;grep\&#96; utilities to see if any booleans are available to allow access. For example, use the \&#96;getsebool -a | grep ftp\&#96; command to search for FTP related booleans:

    ----
    $ getsebool -a | grep ftp
    ftpd_anon_write --\&gt; off
    ftpd_full_access --\&gt; off
    ftpd_use_cifs --\&gt; off
    ftpd_use_nfs --\&gt; off

    ftpd_connect_db --\&gt; off
    httpd_enable_ftp_server --\&gt; off
    tftp_anon_write --\&gt; off
    ----

    To get a list of booleans and to find out if they are enabled or disabled, use the \&#96;getsebool -a\&#96; command. To get a list of booleans including their meaning, and to find out if they are enabled or disabled, install the \&#96;selinux-policy-devel\&#96; package and use the \&#96;semanage boolean -l\&#96; command as root.

    \&#42;\&#42;Port numbers\&#42;

    Depending on policy configuration, services can only be allowed to run on certain port numbers. Attempting to change the port a service runs on without changing policy may result in the service failing to start. For example, run the \&#96;semanage port -l | grep http\&#96; command as root to list \&#96;http\&#96; related ports:

    ----
    \&#35; semanage port -l | grep http
    http_cache_port_t              tcp      3128, 8080, 8118
    http_cache_port_t              udp      3130
    http_port_t                    tcp      80, 443, 488, 8008, 8009, 8443
    pegasus_http_port_t            tcp      5988
    pegasus_https_port_t           tcp      5989
    ----

    The \&#96;http_port_t\&#96; port type defines the ports Apache HTTP Server can listen on, which in this case, are TCP ports 80, 443, 488, 8008, 8009, and 8443. If an administrator configures \&#96;httpd.conf\&#96; so that httpd listens on port 9876 (\&#96;Listen 9876\&#96;), but policy is not updated to reflect this, the following command fails:

    ----
    \&#35; systemctl start httpd.service
    Job for httpd.service failed. See 'systemctl status httpd.service' and 'journalctl -xn' for details.

    \&#35; systemctl status httpd.service
    httpd.service - The Apache HTTP Server
    Loaded: loaded (/usr/lib/systemd/system/httpd.service; disabled)
    Active: failed (Result: exit-code) since Thu 2013-08-15 09:57:05 CEST; 59s ago
    Process: 16874 ExecStop=/usr/sbin/httpd $OPTIONS -k graceful-stop (code=exited, status=0/SUCCESS)
    Process: 16870 ExecStart=/usr/sbin/httpd $OPTIONS -DFOREGROUND (code=exited, status=1/FAILURE)
    ----

    An SELinux denial message similar to the following is logged to \&#96;/var/log/audit/audit.log\&#96;:

    ----
    type=AVC msg=audit(1225948455.061:294): avc:  denied  { name_bind } for  pid=4997 comm='httpd' src=9876 scontext=unconfined_u:system_r:httpd_t:s0 tcontext=system_u:object_r:port_t:s0 tclass=tcp_socket
    ----

    To allow \&#96;httpd\&#96; to listen on a port that is not listed for the \&#96;http_port_t\&#96; port type, use the \&#96;semanage port\&#96; command to assign a different label to the port:

    ----
    \&#35; semanage port -a -t http_port_t -p tcp 9876
    ----

    The \&#96;-a \&#96;option adds a new record; the \&#96;-t\&#96; option defines a type; and the -p option defines a protocol. The last argument is the port number to add.

    \&#42;\&#42;Corner cases, evolving or broken applications, and compromised systems\&#42;\&#42;

    Applications may contain bugs, causing SELinux to deny access. Also, SELinux rules are evolving – SELinux may not have seen an application running in a certain way, possibly causing it to deny access, even though the application is working as expected. For example, if a new version of PostgreSQL is released, it may perform actions the current policy does not account for, causing access to be denied, even though access should be allowed.

    For these situations, after access is denied, use the \&#96;audit2allow\&#96; utility to create a custom policy module to allow access. You can report missing rules in the SELinux policy in Red Hat Bugzilla. For \&#96;Red Hat Enterprise Linux 8\&#96;, create bugs against the Red Hat Enterprise Linux 8 product, and select the \&#96;selinux-policy\&#96; component. Include the output of the \&#96;audit2allow -w -a\&#96; and \&#96;audit2allow -a\&#96; commands in such bug reports.

    If an application asks for major security privileges, it could be a signal that the application is compromised. Use intrusion detection tools to inspect such suspicious behavior.

    The Solution Engine on the Red Hat Customer Portal can also provide guidance in the form of an article containing a possible solution for the same or very similar problem you have. Select the relevant product and version and use SELinux-related keywords, such as selinux or avc, together with the name of your blocked service or application, for example: \&#96;selinux samba\&#96;.

    == SELinux denials in the audit log

    The Linux Audit system stores log entries in the \&#96;/var/log/audit/audit.log\&#96; file by default.

    To list only SELinux-related records, use the \&#96;ausearch\&#96; command with the message type parameter set to \&#96;AVC\&#96; and \&#96;AVC_USER\&#96; at a minimum, for example:

    ----
    \&#35; ausearch -m AVC,USER_AVC,SELINUX_ERR,USER_SELINUX_ERR
    ----

    An SELinux denial entry in the Audit log file can look as follows:

    ----
    type=AVC msg=audit(1395177286.929:1638): avc:  denied  { read } for  pid=6591 comm='httpd' name='webpages' dev='0:37' ino=2112 scontext=system_u:system_r:httpd_t:s0 tcontext=system_u:object_r:nfs_t:s0 tclass=dir
    ----

    The most important parts of this entry are:

    \&#42; \&#96;avc: denied\&#96; - the action performed by SELinux and recorded in Access Vector Cache (AVC)
    \&#42; \&#96;{ read }\&#96; - the denied action
    \&#42; \&#96;pid=6591\&#96; - the process identifier of the subject that tried to perform the denied action
    \&#42; \&#96;comm='httpd'\&#96; - the name of the command that was used to invoke the analyzed process
    \&#42; \&#96;httpd_t\&#96; - the SELinux type of the process
    \&#42; \&#96;nfs_t\&#96; - the SELinux type of the object affected by the process action
    \&#42; \&#96;tclass=dir\&#96; - the target object class

    The previous log entry can be translated to:

    __SELinux__ denied the \&#96;__httpd__\&#96; process with PID 6591 and the \&#96;__httpd_t__\&#96; type to read from a directory with the \&#96;__nfs_t__\&#96; type.

    The following SELinux denial message occurs when the Apache HTTP Server attempts to access a directory labeled with a type for the Samba suite:

    ----
    type=AVC msg=audit(1226874073.147:96): avc:  denied  { getattr } for  pid=2465 comm='httpd' path='/var/www/html/file1' dev=dm-0 ino=284133 scontext=unconfined_u:system_r:httpd_t:s0 tcontext=unconfined_u:object_r:samba_share_t:s0 tclass=file
    ----

    \&#42; \&#96;{ getattr }\&#96; - the \&#96;getattr\&#96; entry indicates the source process was trying to read the target file’s status information. This occurs before reading files. SELinux denies this action because the process accesses the file and it does not have an appropriate label. Commonly seen permissions include \&#96;getattr\&#96;, \&#96;read\&#96;, and \&#96;write\&#96;.
    \&#42; \&#96;path='/var/www/html/file1'\&#96; - the path to the object (target) the process attempted to access.
    \&#42; \&#96;scontext='unconfined_u:system_r:httpd_t:s0'\&#96; - the SELinux context of the process (source) that attempted the denied action. In this case, it is the SELinux context of the Apache HTTP Server, which is running with the \&#96;httpd_t\&#96; type.
    \&#42; \&#96;tcontext='unconfined_u:object_r:samba_share_t:s0'\&#96; - the SELinux context of the object (target) the process attempted to access. In this case, it is the SELinux context of \&#96;file1\&#96;.

    This SELinux denial can be translated to:

    SELinux denied the \&#96;__httpd__\&#96; process with PID 2465 to access the \&#96;__/var/www/html/file1__\&#96; file with the \&#96;__samba_share_t__\&#96; type, which is not accessible to processes running in the httpd_t domain unless configured otherwise.

    \&#42;\&#42;Additional resources\&#42;\&#42;

    \&#42; \&#96;auditd(8)\&#96; and \&#96;ausearch(8)\&#96; man pages

    == Additional resources

    \&#42; link:https://access.redhat.com/articles/2191331[Basic SELinux Troubleshooting in CLI]
    \&#42; RHEL 9: link:https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/using_selinux/index[Using SELinux]
    \&#42; link:https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/selinux_users_and_administrators_guide/index[RHEL 7, SELinux User's and Administrator's Guide]
    \&#42; link:https://fedorapeople.org/~dwalsh/SELinux/Presentations/selinux_four_things.pdf[Four Key Causes of SELinux Errors]
    \&#42; link:https://wiki.centos.org/HowTos/SELinux[CentOS Wiki How Tos: SELinux]







    = Upgrading Fedora Linux Online Using Package Manager
    Ben Cotton; Kamil Páral;  Caleb McKee
    //:page-aliases:

    [abstract]
    This page contains information explaining how to upgrade Fedora Linux online using \&#96;dnf\&#96; (without the xref:dnf-system-upgrade.adoc[DNF system upgrade plugin]).


    [WARNING]
    ====
    This is not a supported upgrade method. Read xref:upgrading.adoc[Upgrading to a new release of Fedora Linux] to see a list of supported and tested upgrade methods. The steps included in the guide are \&#42;at your own risk\&#42;.
    ====

    == Upgrading Fedora Linux using dnf directly

    == Participate

    If you are upgrading using link:https://fedoraproject.org/wiki/DNF[DNF] and it shows any general dependency issues, please file them in http://bugzilla.redhat.com[Bugzilla]. But please read this page, all references pages and search the mailing list archives before filing bugs. And of course, please help keep this page updated.

    If you want to help make live upgrades work smoothly, join the
    link:SIGs/LiveUpgrade[Live Upgrade Special Interest Group].

    == Upgrading across multiple releases

    If you need to upgrade across several releases, it is generally recommended to go one release at a time: for example, rather than going directly from Fedora Linux 37 to Fedora Linux 39, first go to Fedora Linux 38 and then to Fedora Linux 39. This tends to reduce the number of package dependency issues you may encounter. If you are upgrading from an link:End_of_life[End of life] release, please also see link:\&#35;eol[the end-of-life section].

    == Instructions to upgrade using dnf

    === 1. Backup your system

    Backup any personal data to an external hard drive or to another machine. If there is some unrecoverable error that requires a fresh install, you don't want to lose any data.

    === 2. Read about common problems

    Further down in this page there is a list of common problems specific to dnf upgrades for specific versions. Some of them require attention before the upgrade.

    General advice on upgrading Fedora Linux can be found on the link:https://docs.fedoraproject.org/en-US/quick-docs/upgrading/[Upgrading] page. You should also read the http://docs.fedoraproject.org/install-guide/[Installation Guide] and http://docs.fedoraproject.org/release-notes/[Release Notes] for the version you plan to upgrade to - they contain important information regarding upgrading issues. Finally, check the list of link:Common_bugs[Common bugs].

    === 3. Clean Stuff

    Review and remove all .rpmsave and .rpmnew files before and after upgrading. (And if you have selinux enabled then remember to check security context if you move config files around.)

    TIP: \&#42;Find unused config files\&#42; + Merge and resolve the changes found by the following script: \&#96;dnf install rpmconf; rpmconf -a\&#96;. Now find and remove old config which nobody owns: \&#96;rpmconf -c\&#96;.

    Now is a good time to remove packages you don't use - especially non-standard packages.

    TIP: \&#42;Find and review 'unused' packages\&#42; + You can find packages not required by other packages with the tool \&#96;package-cleanup\&#96; from the \&#96;dnf-utils\&#96; package: \&#96;dnf install dnf-utils; package-cleanup --leaves\&#96;. These packages could be candidates for removal, but check to see whether you use them directly or if they are used by applications not backed by rpm packages. Remove them with \&#96;dnf remove package-name-and-version\&#96;. Another useful tool for cleaning up unused packages is \&#96;rpmreaper\&#96;. It's an ncurses application that lets you view rpm dependency graph and mark packages for deletion. Marking one package can make other packages leaf, which you can see immediately, so you don't have to run the tool several times to get rid of a whole sub-tree unused packages. Install with \&#96;dnf install rpmreaper\&#96;.

    TIP: \&#42;Find and review 'lost' packages\&#42; + You can find orphaned packages (i.e. packages not in the repositories anymore) with \&#96;package-cleanup --orphans\&#96;. This will also show packages which have been partially uninstalled but where the '%postun' script failed.

    === 4. Do the upgrade

    If you have 3rd party repositories configured, you may need to adjust
    them for the new Fedora Linux version. If you switch from one Fedora Linux release
    to another there is often nothing that needs to be done. If you switch
    to Rawhide from a standard Fedora Linux release (or vice versa) then most of
    the time you will need to install the Rawhide release RPMs from the 3rd
    party repository as well (or the standard ones, if switching back).

    Note that the upgrade is likely to fail if there are outdated
    dependencies from packages not backed by a dnf repository or backed by a
    repository which isn't ready for the new version.

    It is a good idea to do the upgrade outside the graphical environment.
    Log out of your graphical desktop and then

    [[fedora-upgrade]]
    ==== fedora-upgrade

    A small script named fedora-upgrade is available which aims to automate
    the process outlined below. To run it, do the following

    \&#8230;.
    $ sudo dnf install fedora-upgrade
    $ sudo fedora-upgrade
    \&#8230;.

    When performing upgrade via remote shell, it is a good idea to use screen
    or tmux utility to be able to get back to running transaction in case
    your connection drops.

    Alternatively, follow the manual steps:

    [[go-to-a-text-console]]
    ==== Go to a text console

    \&#8230;.
    ctrl + alt + F2
    \&#8230;.

    (or)

    log in as root, and go into multi-user.target

    \&#8230;.
    systemctl isolate multi-user.target
    \&#8230;.

    [[fully-update-your-current-fedora-install]]
    ==== Fully update your current Fedora Linux install

    \&#8230;.
    \&#35; dnf upgrade
    \&#8230;.

    [[install-the-package-signing-key-for-the-release-you-are-upgrading-to]]
    ==== Install the package signing key for the release you are upgrading to

    If you are upgrading across two releases or fewer from Fedora Linux 20 or
    later, this step should be unnecessary. If you are upgrading from an
    older Fedora Linux or upgrading across three or more releases, you may need to
    import the signing key for the target release.

    If it turns out not to be, you should be able to import keys like so:

    \&#8230;.
    \&#35; rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-fedora-23-x86_64
    \&#8230;.

    , replacing '23' and 'x86_64' with the new Fedora Linux version and your
    architecture, respectively.

    You can also find package signing keys for currently-supported releases
    https://getfedora.org/keys/[here]. Keys for EOL releases can be found
    https://getfedora.org/keys/obsolete.html[here]. Click _Primary_ (or
    _Secondary_, if you are using a secondary architecture), and you will
    see _Get it from: Fedora Project_, where _Fedora Project_ is a link.
    Copy that URL, and run:

    \&#8230;.
    \&#35; rpm --import (url)
    \&#8230;.

    to install the key. On old releases, \&#96;rpm\&#96; may have trouble doing this; if
    that happens, download the file with \&#96;curl -o\&#96; or \&#96;wget\&#96; and import the downloaded file.

    [[clean-the-cache]]
    ==== Clean the cache

    Then remove all traces of the version you are leaving from the dnf cache
    in \&#96;/var/cache/dnf\&#96;.

    \&#8230;.
    \&#35; dnf clean all
    \&#8230;.

    ==== Upgrade all packages

    CAUTION: \&#42;Never upgrade on battery power\&#42; + Never run the upgrade operation on battery power! Always connect to the mains, if using a laptop. However, if your system does have a battery, it's a good idea to ensure it's charged and connected in case of a power outage during the upgrade.

    CAUTION: \&#42;Do not interrupt an upgrade for any reason\&#42; + Once a live upgrade is started, do not stop the upgrade by rebooting, killing the process, or by any other method until it is complete. Interrupting an upgrade will cause the affected system to be in a mixed state -- partially the old release and partially the new release. In this state, the system will not be reliable and will not operate as expected. You can try running \&#96;dnf distro-sync\&#96; and \&#96;package-cleanup --problems\&#96; to try and fix the problems.

    Run the upgrade command:

    \&#8230;.
    \&#35; dnf --releasever=\&lt;target_release_number\&gt; --setopt=deltarpm=false distro-sync
    \&#8230;.

    NOTE: \&#42;Dependency issues\&#42; + If you experience any dependency problems, you have to solve them manually. These are often caused by packages being retired in the newer release, but not properly obsoleted. Often it is enough to remove several problematic package(s).
    You may find that a package you care about depends on a package that must be removed for the upgrade to proceed. Usually you will be able to reinstall the important package once the upgrade is complete.

    If it seems like you must remove a package with many dependencies, especially ones that look important, please be careful. If you are attempting to upgrade across multiple releases, try a smaller jump to see if that avoids the problem.

    If you are at all unsure in any way, ask for help on a mailing list, forum or IRC before removing packages.

    === 5. Make sure Fedora Linux is upgraded

    Distro-sync will usually take care of upgrades for the third party
    repositories you have enabled as well. Confirm with \&#96;dnf repolist\&#96; after the upgrade
    process is over. \&#96;dnf\&#96; might complain about conflicts or requirements.
    That is probably because you have used non-standard repositories or
    installed non-standard packages manually. Try to guess which packages
    cause the problem (or at least is a part of the dependency chain) -
    uninstall them and try again. Remember to install the packages again if
    they are essential.

    Ensure that all (new) essential packages from the new version are
    installed with

    \&#8230;.
    \&#35; dnf group upgrade 'Minimal Install'
    \&#8230;.

    You might want to update other groups too, see

    \&#8230;.
    \&#35; dnf group list -v
    \&#8230;.

    For example

    \&#8230;.
    \&#35; dnf group upgrade 'GNOME Desktop' \
    'Development Tools' 'Sound and Video' \
    'Games and Entertainment' 'Administration Tools' \
    'Office/Productivity' 'System Tools'
    \&#8230;.

    === 6. Preparing for reboot

    Before booting you should usually install the bootloader from your new
    grub by running

    \&#8230;.
    /usr/sbin/grub2-install BOOTDEVICE
    \&#8230;.

    - where BOOTDEVICE is often \&#96;/dev/sda\&#96; or \&#96;/dev/vda\&#96; for some virtual machine installs. If
    you have more than one hard disk, make sure you use the correct device!

    If you get an error (e.g. \&#96;/dev/sda does not have any corresponding BIOS drive\&#96;) from that, then try \&#96;/usr/sbin/grub2-install --recheck BOOTDEVICE\&#96;.

    It might also be necessary to update the grub config file:

    \&#8230;.
    cp --backup=numbered -a /boot/grub2/grub.cfg{,.bak} \&#35; create backup copy
    /usr/sbin/grub2-mkconfig -o /boot/grub2/grub.cfg \&#35; update config file
    \&#8230;.

    === 7. Cleanup your system

    Again, cleanup your system as described in section 2. Also you might
    want to remove some cache files that are no longer used, for example
    files from older Fedora Linux releases in the following directories:

    \&#42; /var/cache/dnf
    \&#42; /var/cache/mock
    \&#42; /var/lib/mock

    == Release specific notes

    Note: the release-specific notes for link:End_of_life[End of life] releases are on the
    link:Upgrading_from_EOL_Fedora_using_package_manager[EOL packager manager upgrade page].

    === From pre-release

    If you are upgrading to a final release from an Alpha, Beta, or release candidate, please see link:Upgrading_from_pre-release_to_final[Upgrading from pre-release to final].

    === To Rawhide

    See the link:Releases/Rawhide[Rawhide] release page for more information on Rawhide.

    \&#8230;.
    \&#35; dnf upgrade
    \&#35; dnf install dnf-plugins-core fedora-repos-rawhide
    \&#35; dnf config-manager --set-disabled fedora updates updates-testing
    \&#35; dnf config-manager --set-enabled rawhide
    \&#35; dnf clean -q dbcache packages metadata
    \&#35; dnf --releasever=rawhide --setopt=deltarpm=false distro-sync --nogpgcheck

    \&#35;\&#35; Optional: it is generally advised to do a selinux autorelabel and reboot
    \&#35; touch /.autorelabel
    \&#8230;.

    === Fedora Linux 31
    Before running

    \&#8230;.
    dnf distro-sync
    \&#8230;.

    you must run

    \&#8230;.
    dnf module reset libgit2 exa bat
    \&#8230;.

    See link:https://bugzilla.redhat.com/show_bug.cgi?id=1747408[Bug 1747408].

    === Fedora Linux 30

    No special instructions. Follow the above instructions.

    === Fedora Linux 29

    No special instructions. Follow the above instructions.

    [[upgrading-from-legacy-end-of-life-eol-fedora-releases]]
    === Upgrading from legacy end of life (EOL) Fedora Linux releases

    Note that Fedora strongly recommends against ever running an end-of-life release on any production system, or any system connected to the public internet, in any circumstances. You should never allow a production Fedora Linux deployment to reach end-of-life in the first place.

    With that in mind, if you do have an end-of-life release installed on a system you cannot just discard or re-deploy, you can attempt to upgrade it, though this is a less-tested and less-supported operation.

    For detailed instructions on upgrades from EOL releases, please read link:Upgrading_from_EOL_Fedora_using_package_manager[Upgrading from EOL Fedora Linux using package manager].

    See a typo, something missing or out of date, or anything else which can be improved? Edit this document at https://pagure.io/fedora-docs/quick-docs.













    = How to debug Dracut problems
    Caleb McKee; Héctor Louzao; Frank Sträter
    //:imagesdir: ./images

    // include::partial$attributes.adoc[]

    \&#42;Foreword\&#42;

    If you are experiencing a problem with system initialization due to
    Dracut, please see the link:https://discussion.fedoraproject.org/c/ask/common-issues/82/none[common bugs] document before
    filing a bug. Some easy configuration tweaks that fix a wide range of
    issues may be listed there. If the problem you are seeing is not listed
    there or none of the workarounds seem to help, please consider filing a
    bug to help us make Fedora run better on your hardware.

    Be prepared to include some information (logs) about your system as
    well. These should be complete (no snippets please), not in an archive,
    uncompressed, with MIME type set as text/plain.

    [[identifying-your-problem-area]]
    == Identifying your problem area

    .  Remove \&#96;rhgb\&#96; and \&#96;quiet\&#96; from the kernel command line
    .  Add \&#96;rd.shell\&#96; to the kernel command line. This will present a shell
    in case dracut is unable to locate your root device
    .  Add \&#96;rd.shell rd.debug log_buf_len=1M\&#96; to the kernel command line so
    that dracut shell commands are printed as they are executed
    .  Inspect the system logs:
    \&#8230;.
    \&#35; less /run/initramfs/rdsosreport.txt
    \&#35; journalctl -a
    \&#35; dmesg
    \&#35; less /run/initramfs/init.log
    \&#8230;.

    [[information-to-include-in-your-report]]
    == Information to include in your report

    [[all-bug-reports]]
    === All bug reports

    In all cases, the following should be mentioned and attached to your bug
    report:

    \&#42; The exact kernel command-line used. Typically from the bootloader
    configuration file (e.g. \&#96;/etc/grub.conf\&#96;) or from \&#96;/proc/cmdline\&#96;
    \&#42; A copy of your disk partition information from \&#96;/etc/fstab\&#96;
    \&#42; A device listing from device-mapper. This can be obtained by running
    the command \&#96;dmsetup ls -- tree\&#96;
    \&#42; A list of block device attributes including vol_id compatible mode.
    This can be obtained by running the commands \&#96;blkid\&#96; and \&#96;blkid -o udev\&#96;
    \&#42; Turn on dracut debugging (see   link:\&#35;debugging-dracut[the 'debugging dracut'
    section]), and attach all relevant information from the boot log. This
    can be obtained by running the command \&#96;dmesg|grep dracut\&#96;
    \&#42; If you use a dracut configuration file, please include \&#96;/etc/dracut.conf\&#96;

    [[logical-volume-management-related-problems]]
    === Logical Volume Management related problems

    As well as the information from
    link:\&#35;all-bug-reports[the 'all bug reports'
    section], include the following information:

    \&#42; Include physical volume information by running the command: \&#96;lvm pvdisplay\&#96;
    \&#42; Include volume group information by running the command: \&#96;lvm vgdisplay\&#96;
    \&#42; Include logical volume information by running the command: \&#96;lvm lvdisplay\&#96;

    [[software-raid-related-problems]]
    === Software RAID related problems

    As well as the information from
    link:\&#35;all-bug-reports[the 'all bug reports'
    section], include the following information:

    \&#42; If using software RAID disk partitions, please include the output of \&#96;/proc/mdstat\&#96;

    [[network-root-device-related-problems]]
    Network root device related problems
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This section details information to include when experiencing problems
    on a system whose root device is located on a network attached volume
    (e.g. iSCSI, NFS or NBD). As well as the information from
    link:\&#35;all-bug-reports[the 'all bug reports'
    section], include the following information:

    \&#42; Please include the output of

    [[debugging-dracut]]
    == Debugging dracut

    [[configure-a-serial-console]]
    === Configure a serial console

    Successfully debugging dracut will require some form of console logging
    during the system boot. This section documents configuring a serial
    console connection to record boot messages. To enable serial console
    output for both the kernel and the bootloader, follow the procedure
    below.

    .  Open the file \&#96;/etc/grub.conf\&#96; for editing. Below the line _timeout=5_, add the following:
    +
    \&#8230;.
    serial --unit=0 --speed=9600
    terminal --timeout=5 serial console
    \&#8230;.

    .  Also in \&#96;/etc/grub.conf\&#96;, add the following boot arguments to the _kernel_ line:
    +
    \&#8230;.
    console=tty0 console=ttyS0,9600
    \&#8230;.

    .  When finished, \&#96;/etc/grub.conf\&#96; should look similar to the example below:

    \&#8230;.
    default=0
    timeout=5
    serial --unit=0 --speed=9600
    terminal --timeout=5 serial console
    title Fedora (2.6.29.5-191.fc11.x86_64)
    root (hd0,0)
    kernel /vmlinuz-2.6.29.5-191.fc11.x86_64 ro root=/dev/mapper/vg_uc1-lv_root console=tty0 console=ttyS0,9600
    initrd /dracut-2.6.29.5-191.fc11.x86_64.img
    \&#8230;.

    More detailed information on how to configure the kernel for console
    output can be found at
    http://www.faqs.org/docs/Linux-HOWTO/Remote-Serial-Console-HOWTO.html\&#35;CONFIGURE-KERNEL[1].

    [[using-the-dracut-shell]]
    === Using the dracut shell

    Dracut offers a shell for interactive debugging in the event dracut
    fails to locate your root filesystem. To enable the shell:

    .  Add the boot parameter \&#96;rd.shell\&#96; to your bootloader configuration
    file (e.g. \&#96;/etc/grub/conf\&#96;)
    .  Remove the boot arguments \&#96;rhgb\&#96; and \&#96;quiet\&#96;

    A sample \&#96;/etc/grub.conf\&#96; bootloader configuration file is listed below:

    \&#8230;.
    default=0
    timeout=5
    serial --unit=0 --speed=9600
    terminal --timeout=5 serial console
    title Fedora (2.6.29.5-191.fc11.x86_64)
    root (hd0,0)
    kernel /vmlinuz-2.6.29.5-191.fc11.x86_64 ro root=/dev/mapper/vg_uc1-lv_root console=tty0 rd.shell
    initrd /dracut-2.6.29.5-191.fc11.x86_64.img
    \&#8230;.

    If system boot fails, you will be dropped into a shell as seen in the
    example below:

    \&#8230;.
    No root device found
    Dropping to debug shell.

    sh: can't access tty; job control turned off
    \&#35;
    \&#8230;.

    Use this shell prompt to gather the information requested above (see
    link:\&#35;all-bug-reports[the 'all bug reports'
    section]).

    [[accessing-the-root-volume-from-the-dracut-shell]]
    === Accessing the root volume from the dracut shell

    From the dracut debug shell, you can manually perform the task of
    locating and preparing your root volume for boot. The required steps
    will depend on how your root volume is configured. Common scenarios
    include:

    \&#42; A block device (e.g. \&#96;/dev/sda7\&#96;)
    \&#42; A LVM logical volume (e.g. \&#96;/dev/VolGroup00/LogVol00\&#96;)
    \&#42; An encrypted device (e.g. \&#96;/dev/mapper/luks-4d5972ea-901c-4584-bd75-1da802417d83\&#96;)
    \&#42; A network attached device (e.g. \&#96;netroot=iscsi:@192.168.0.4::3260::iqn.2009-02.org.fedoraproject:for.all\&#96;)

    The exact method for locating and preparing will vary. However, to
    continue with a successful boot, the objective is to locate your root
    volume and create a symlink \&#96;/dev/root\&#96; which points to the file system. For example, the following example demonstrates accessing and booting a root volume that is an encrypted LVM Logical volume.

    .  Inspect your partitions using \&#96;parted\&#96;:
    +
    \&#8230;.
    \&#35; parted /dev/sda -s p
    Model: ATA HTS541060G9AT00 (scsi)
    Disk /dev/sda: 60.0GB
    Sector size (logical/physical): 512B/512B
    Partition Table: msdos

    Number  Start   End     Size    Type      File system  Flags
    1      32.3kB  10.8GB  107MB   primary   ext4         boot
    2      10.8GB  55.6GB  44.7GB  logical                lvm
    \&#8230;.

    .  You recall that your root volume was a LVM logical volume. Scan and
    activate any logical volumes:
    +
    \&#8230;.
    \&#35; lvm vgscan
    \&#35; lvm vgchange -ay
    \&#8230;.

    .  You should see any logical volumes now using the command \&#96;blkid\&#96;:
    +
    \&#8230;.
    \&#35; blkid
    /dev/sda1: UUID='3de247f3-5de4-4a44-afc5-1fe179750cf7' TYPE='ext4'
    /dev/sda2: UUID='Ek4dQw-cOtq-5MJu-OGRF-xz5k-O2l8-wdDj0I' TYPE='LVM2_member'
    /dev/mapper/linux-root: UUID='def0269e-424b-4752-acf3-1077bf96ad2c' TYPE='crypto_LUKS'
    /dev/mapper/linux-home: UUID='c69127c1-f153-4ea2-b58e-4cbfa9257c5e' TYPE='ext3'
    /dev/mapper/linux-swap: UUID='47b4d329-975c-4c08-b218-f9c9bf3635f1' TYPE='swap'
    \&#8230;.

    .  From the output above, you recall that your root volume exists on an
    encrypted block device. Unlock your encrypted root volume.
    +
    \&#8230;.
    UUID=$(cryptsetup luksUUID /dev/mapper/linux-root)
    cryptsetup luksOpen /dev/mapper/linux-root luks-$UUID
    Enter passphrase for /dev/mapper/linux-root:
    Key slot 0 unlocked.
    \&#8230;.

    .  Next, make a symbolic link to the unlocked root volume
    +
    \&#8230;.
    ln -s /dev/mapper/luks-$UUID /dev/root
    \&#8230;.

    .  With the root volume available, you may continue booting the system
    by exiting the dracut shell
    +
    \&#8230;.
    exit
    \&#8230;.

    [[summary-of-dracut-kernel-command-line-options]]
    === Summary of dracut kernel command line options

    A selection of the most common debugging related dracut options:

    \&#96;\&#42;rd.shell\&#42;\&#96;::
    Drop to a shell, if the initramfs fails.

    \&#96;\&#42;rd.debug\&#42;\&#96;::
    Set -x for the dracut shell.

    \&#96;\&#42;rd.break=[cmdline|pre-udev|pre-trigger|initqueue|pre-mount|mount|pre-pivot|cleanup]\&#42;\&#96;::
    Drop the shell on defined breakpoint (use
    \&#96;egrep 'rd.?break' /usr/lib/dracut/modules.d/99base/init.sh\&#96; to find the
    breakpoints supported by your dracut version)

    \&#96;\&#42;rd.udev.info\&#42;\&#96;::
    Set udev to loglevel info (this is the default level)

    \&#96;\&#42;rd.udev.debug\&#42;\&#96;::
    Set udev to loglevel debug

    See the \&#96;dracut.cmdline(7)\&#96;
    https://man7.org/linux/man-pages/man7/dracut.cmdline.7.html[man page] for
    the complete reference.







    = Virtualization – an Overview
    Markmc ; Denisarnaud ; Lhirlimann

    //:page-aliases:
    // :experimental:
    //include::{partialsdir}/attributes.adoc[]

    // migrated from
    // https://fedoraproject.org/wiki/Virtualization

    [abstract]
    This page covers the efforts to integrate various virtualization technologies into Fedora.


    == Introduction

    Virtualization allows one to run many guest virtual machines on top of a host operating system such as Fedora. What this means is that using one computer, you can mimic several individual computers and even run different operating systems in each of these virtual machines. There are many different virtualization technologies, including both free and open source software and proprietary offerings. A link:https://web.archive.org/web/20080327111126/http://www-128.ibm.com/developerworks/linux/library/l-linuxvirt/?ca=dgr-lnxw01Virtual-Linux[good article on IBM DeveloperWorks (M Tim Jones, Dec 2006, archived)] Web site illustrates the four main different virtualization families, namely

    \&#42; hardware emulation
    \&#42; hardware-assisted full virtualization
    \&#42; para-virtualization (PV)
    \&#42; operating system-level virtualization (containers/zones)

    == Hardware Emulation

    image::virtualization/virtualization-hardware-emulation.png[]

    //[[File:Virtualization_Hardware_Emulation.png|200px|thumb|Hardware Emulation Virtualization]]

    Hardware emulation uses a VM to simulate the required hardware. A few implementations:

    \&#42; link:https://bochs.sourceforge.io[Bochs]
    \&#42; link:https://wiki.qemu.org[QEMU]

    == Hardware-assisted full virtualization

    //[[File:Virtualization_Full.png|200px|thumb|Full Virtualization]]

    image::virtualization/virtualization-hardware-assisted-full.png[]


    Full virtualization uses a hypervisor (a.k.a. VMM, standing for Virtual Machine Monitor) to share the underlying hardware. A few implementations:

    \&#42; link:https://www.linux-kvm.org[ KVM] / link:https://wiki.qemu.org[QEMU] is a full virtualization solution for Linux on x86 hardware containing virtualization extensions (Intel VT or AMD-V). Using KVM, one can run multiple virtual machines running unmodified Linux or Windows images.

    //KVM is part of [http://et.redhat.com RedHat Emerging Technologies (ET)].

    \&#42; link:https://xenproject.org[Xen] is a virtual-machine monitor providing services that allow multiple computer operating systems to execute on the same computer hardware concurrently. Xen has been the solution of choice for RedHat EL distributions since 2005. The kernel-2.6.18 dropped support for Xen, but the necessary modules/modifications have been added to the upstream kernel again, from 2.6.37 for DomU (guests) and from 3.0 for Dom0 (base domain, part of the host). Therefore, Xen Dom0 host support, that was dropped after Fedora 8, it has now been re-introduced, from Fedora 16.

    \&#42; link:https://www.virtualbox.org[VirtualBox] is a full virtualization solution for x86 and AMD64/Intel64 hardware. Sun Microsystems started that project, which is now fully supported by Oracle. There is a dual licencing scheme, among which GPLv2. Allegedly VirtualBox is one of the fastest full virtualization solutions.

    == Para-Virtualization (PV)

    [[File:Virtualization_Para.png|200px|thumb|Para-Virtualization]]

    image::virtualization/virtualization-para.png[]

    Paravirtualization shares the process with the guest operating system. A few implementations:

    \&#42; link:https://www.linux-kvm.org[KVM] (see above).
    \&#42; link:https://xen.org[Xen] (see above).

    //Doesn't exist anymore
    //\&#42; link:https://kraxel.fedorapeople.org/xenner[xenner] is a utility allowing paravirtualized Xen guests to be run using KVM.

    == Operating system-level virtualization

    //[[File:Virtualization_Containers.png|200px|thumb|Containers-based Virtualization]]

    image::virtualization/virtualization-system-level.png[ ]

    Operating system-level virtualization partitions a host into insulated guests, which are therefore as kinds of chroot, but with much stronger resource isolation.

    Originally, this family of virtualization was referred to as _zones_ and evolved into highly sophisticated  _containers_ today.

    A few implementations:

    \&#42; link:https://fedoraproject.org/wiki/Docker[Docker] isolate a single process in its own environment

    // obviously gon?
    // \&#42; link:https://fedoraproject.org/wiki/Sandboxing[sandboxing]

    \&#42; link:https://wiki.openvz.org[OpenVZ] and the Debian-based ProxMox for the off-the-shelf server

    \&#42; link:https://linuxcontainers.org/lxc[LXC] (Linux Containers), an operating system–level virtualization method for running multiple isolated Linux systems (containers) on a single control host

    // Wiki page about it on fedora: https://fedoraproject.org/wiki/LXC
    // to migrate to docs?

    \&#42; link:https://en.wikipedia.org/wiki/Linux-VServer/[Linux-VServer], which does not seem to be no longer active (the last news is dated back in 2009)


    == Fedora Support

    At time of writing, Fedora includes full support for link:https://www.linux-kvm.org/[KVM]/link:https://wiki.qemu.org/[QEMU], link:https://xen.org/[Xen] and link:https://linuxcontainers.org[LXC].

    A number of third parties (e.g., link:https://rpmfusion.org[RPMFusion]) provide add-on packages for other virtualization technologies: link:https://openvz.org/[OpenVZ], link:http://linux-vserver.org/[Linux-VServer], link:https://www.virtualbox.org[VirtualBox].

    Anticipating this diversification of technology, since the days of Fedora Core 5, all core management applications have been built on top of the link:https://libvirt.org[libvirt] toolkit, which offers a technology independent API for managing virtual systems.

    === Clouds
    As Cloud-based infrastructures rely, by nature, on virtualization technologies, both subjects are therefore heavily inter-related. The link:https://fedoraproject.org/cloud/[_Fedora Cloud Edition_] is dedicated to the subject, worth to follow as well.

    === History
    Fedora Core 5 was the first release to include Xen as a core integrated technology. The new Linux native virtualization, KVM, was introduced to Fedora 7. For a more detailed account of virtualization progress in Fedora, consult the link:https://fedoraproject.org/wiki/Virtualization/History[Virtualization History] page.


    === News
    There is semi-regular coverage of Virtualization news in various Fedora communication media, specifically in link:https://fedoramagazine.org[Fedora Magazine], link:https://communityblog.fedoraproject.org/[Fedora Community Blog], and link:https://discussion.fedoraproject.org/tag/libvirt[Fedora Discussion, \&#35;libvirt]

    //Fedora Weekly News, and more detailed status updates posted to the  fedora-virt Mailing List. For ease of reference, there is an [[Virtualization/News |archive of virtualization news]]


    == Getting started

    The Quick Docs article xref:getting-started-with-virtualization.adoc[Virtualization – Getting Started] provides an excellent overview to using the virtualization capabilities in Fedora.

    Specifically for _Fedora Server Edition_ there is xref:fedora-server::virtualisation/index.adoc[extensive and step-by-step guidance] available.

    Various link:https://fedoramagazine.org/?s=virtualization[magazine articles on virtualization] have introductory material as well.

    // to be redirected
    // https://fedoraproject.org/wiki/Magazine_articles_on_virtualization

    == Bugs

    See xref:virtualization-howto-debug-issues.adoc[Virtualization – How to Debug Issues] for some tips on reporting virtualization bugs to link:https://bugzilla.redhat.com[bugzilla].

    // If you wish to help triaging and fixing virtualization bugs, [[virtualization bugs]] is a good starting point. On the page [[Virtualization Preview Repository]], you shall find information if you can be a ''potential virtualization tester''.


    == Mailing list and IRC

    //To get in touch with Fedora virtualization users and developers try [irc://irc.oftc.net/\&#35;virt \&#35;virt on irc.oftc.net].
    There isn't any designated virt mailing list, so try the standard Fedora lists like link:https://lists.fedoraproject.org/mailman/listinfo/users[users] or link:https://lists.fedoraproject.org/mailman/listinfo/devel[devel] lists.

    // completely outdated
    // == Relevant Packages ==
    //We have a page containing [[Virtualization packages|a catalogue of all the virtualization related packages]] in Fedora.


    == oVirt

    link:https://ovirt.org/[oVirt] is a Fedora based project which provides small host images and a web-based virtual machine management console. See link:https://ovirt.org/[their website] to learn more and get involved.


    // Completely outdated
    //== Other virtualization information ==
    //You can find more virtualization information at the category 'Virtualization' on this wiki.


    = Virtualization – Getting Started
    Jan Kuparinen
    :page-aliases: getting-started-with-virtualization.adoc
    :experimental:

    Fedora uses the libvirt family of tools as its virtualization solution.

    == Enabling hardware virtualization support

    This section covers setting up \&#96;libvirt\&#96; on your system. After setting up \&#96;libvirt\&#96;, you can create virtualized guest operating systems, also known as virtual machines.


    === System requirements

    To run virtualization on Fedora, you need:

    \&#42; At least 600MB of hard disk storage per guest. A minimal command-line Fedora system requires 600MB of storage. Standard Fedora desktop guests require at least 3GB of space.

    \&#42; At least 256MB of RAM per guest, plus 256MB for the base operating system. At least 756MB is recommended for each guest of a modern operating system. A good way to estimate this is to think about how much memory is required for the operating system normally, and allocate that amount to the virtualized guest.

    KVM requires a CPU with virtualization extensions, found on most consumer CPUs. These extensions are called Intel VT or AMD-V. To check whether you have CPU support, run the following command:

    ----
    $ grep -E '^flags.\&#42;(vmx|svm)' /proc/cpuinfo
    ----

    If this command results in nothing printed, your system does not support the relevant virtualization extensions. You can still use QEMU/KVM, but the emulator will fall back to software virtualization, which is much slower.



    == Installing virtualization software

    When installing Fedora, you can install the virtualization packages by
    selecting \&#42;Virtualization\&#42; in the \&#42;Base Group\&#42; in the installer.

    //See xref:f43@fedora:install-guide:install/Installing_Using_Anaconda.adoc[Installing Using Anaconda].

    For existing Fedora installations, you can install the virtualization tools via the command line using the Virtualization Package Group. To view the packages, run:

    [source,shell,subs='attributes']
    ----
    $ dnf group info virtualization

    Group: Virtualization
    Description: These packages provide a graphical virtualization environment.
    Mandatory Packages:
    virt-install
    Default Packages:
    libvirt-daemon-config-network
    libvirt-daemon-kvm
    qemu-kvm
    virt-manager
    virt-viewer
    Optional Packages:
    libguestfs-tools
    python3-libguestfs
    virt-top
    ----

    . Run the following command to install the mandatory and default packages in the virtualization group:
    +
    [source,shell,subs='attributes']
    ----
    $ sudo dnf install @virtualization
    ----
    +
    Alternatively, to install the mandatory, default, and optional packages, run:
    +
    [source,shell,subs='attributes']
    ----
    $ sudo dnf group install --with-optional virtualization
    ----
    +
    . After the packages install, start the \&#96;libvirtd\&#96; service:
    +
    [source,shell,subs='attributes']
    ----
    $ sudo systemctl start libvirtd
    ----
    +
    To start the service on boot, run:
    +
    [source,shell,subs='attributes']
    ----
    $ sudo systemctl enable libvirtd
    ----
    +
    . To verify that the KVM kernel modules are properly loaded:
    +
    [source,shell,subs='attributes']
    ----
    $ lsmod | grep kvm
    kvm_amd               114688  0
    kvm                   831488  1 kvm_amd
    ----
    +
    If this command lists \&#96;kvm_intel\&#96; or \&#96;kvm_amd\&#96;, KVM is properly configured.

    === Networking Support

    By default, libvirt will create a private network for your guests on the host machine. This private network will use a 192.168.x.x subnet and not be reachable directly from the network the host machine is on. However, virtual guests can use the host machine as a gateway and can connect out via it. If you need to provide services on your guests that are reachable via other machines on your host network you can use iptables DNAT rules to forward in specific ports, or you can set up a bridged environment.

    See the https://wiki.libvirt.org/page/Networking[libvirt networking setup page] for more information on how to setup a bridged network.



    == Creating virtual machines

    The installation of Fedora guests using Anaconda is supported. The installation can be started on the command-line using the \&#96;virt-install\&#96; program or in the user interface program \&#96;virt-manager\&#96;.

    === Creating a guest with virt-install

    \&#96;virt-install\&#96; is a command-line based tool for creating virtualized guests. Execute \&#96;virt-install --help\&#96; for command line help, or you can find the manual page at \&#96;man 1 virt-install\&#96;.

    To use the virt-install command, you should first download an ISO of the Fedora version you wish to install.  You can find the latest Fedora images at https://fedoraproject.org.  This ISO is only needed during Fedora installation, and can be deleted to free up storage space afterwards if desired.

    //More information about Fedora installation can be found in the xref:f43@fedora:install-guide:index.adoc[Installation Guide].

    In this example we'll use Fedora Workstation.

    ==== Planning VM Resources
    Adjust the ram, vcpus, and disk size parameters according to the resources you have available.

    \&#42; Storage: An easy way to check your disk size from a bash shell is using the \&#96;df(1)\&#96;\&#96; utility from the shell:
    +
    [source,shell,subs='attributes']
    ----
    $ df -h
    ----
    \&#42; Memory: You can check your available memory from the shell using free(1):
    +
    [source,shell,subs='attributes']
    ----
    $ free -m
    ----
    \&#42; VCPU: You can check your processor information using \&#96;lscpu(1)\&#96;:
    +
    [source,shell,subs='attributes']
    ----
    $ lscpu
    ----

    When allocating resources to your VM, keep in mind the minimum system requirements for the version of Fedora you are installing as well as your use case requirements. For Fedora 43, you can find this in the xref:f43@fedora:release-notes:welcome/Hardware_Overview.adoc[Release Notes].

    ===== Create Storage for the VM

    The libvirt default storage pool is located at \&#96;\&#96;/var/lib/libvirt/images\&#96; - which is the parent file path we use in this example.  For individuals who are lacking enough storage in that path, you can simply mount a new disk or partition to that directory path (from the BASH shell, type \&#96;man 1 mount\&#96;) or select a new path. In the example \&#96;virt-install\&#96; command below, the disk did not exist prior to running virt-install.  When the specified disk is not pre-existing, you must specify the size so virt-install can create a disk for you.  If your disk already exists, you can safely remove the \&#96;,size=20\&#96; parameter from the disk argument.

    You have several disk storage options for your VM.  While it's outside the scope of this article to discuss these in detail, the following are a few common options.  These examples use 20G as the upper limit for disk size, but you can adjust this size to fit your needs.

    [NOTE]
    ====
    Again, you do not need to manually allocate storage using the example options shown below if you specify the size parameter in the virt-install example shown below.
    ====

    ====== Raw File (Non-Sparse)

    To create a fully allocated (non-sparse) raw file:

    [source,shell,subs='attributes']
    ----
    $ sudo dd if=/dev/zero of=/var/lib/libvirt/images/guest.img bs=1M count=20480
    ----

    you can also use fallocate(1):

    [source,shell,subs='attributes']
    ----
    $ sudo fallocate -l 20480M /var/lib/libvirt/images/guest.img
    ----

    ====== Raw File (Sparse)

    To create a dynamically allocated (sparse) raw file:

    [source,shell,subs='attributes']
    ----
    $ sudo rm -f /var/lib/libvirt/images/guest.img
    $ sudo truncate --size=20480M /var/lib/libvirt/images/guest.img
    ----


    ====== QCOW2
    To create a new qcow2-formatted disk separately, you can use qemu-img (the example below specifies a disk size of 20G):

    [source,shell,subs='attributes']
    ----
    \&#35; sudo qemu-img create -f qcow2 /var/lib/libvirt/images/guest.qcow2 20480
    ----

    More information about libvirt storage options can be found at https://libvirt.org/storage.html.

    Finally, run the virt-install command using the following format (adjusting parameters as needed):

    [source,shell,subs='attributes']
    ----
    $ sudo virt-install --name Fedora43 \
    --description 'Fedora 43 Workstation' \
    --ram 4096 \
    --vcpus 2 \
    --disk path=/var/lib/libvirt/images/Fedora-Workstation-43/Fedora-Workstation-43-20180518.0.x86_64.qcow2,size=20 \
    --os-variant fedora43 \
    --network bridge=virbr0 \
    --graphics vnc,listen=127.0.0.1,port=5901 \
    --cdrom /var/lib/libvirt/images/Fedora-Workstation-43/Fedora-Workstation-Live-x86-64-43-1.1.iso \
    --noautoconsole
    ----

    [NOTE]
    ====
    Note:  For the graphics parameter, we're setting the vnc listener to localhost because it's more secure to tunnel your VNC connection through SSH so that you don't expose VNC to everyone with access to the network.
    ====

    \&#96;virt-install\&#96; can use kickstart files, for example, \&#96;virt-install -x ks=kickstart-file-name.ks\&#96;.

    If graphics were enabled, a VNC window will open and present the graphical installer. If graphics were not enabled, a text installer will appear. Proceed with the Fedora installation.

    === Creating a guest with virt-manager

    . Start Virtual Machine Manager by navigating to menu:Applications[System Tools], or by running the following command:
    +
    [source,shell,subs='attributes']
    ----
    $ sudo virt-manager
    ----
    +
    . Open a connection to a hypervisor by navigating to menu:File[Add connection].
    . Choose \&#42;qemu\&#42; for KVM, or \&#42;Xen\&#42; for Xen.
    . Choose \&#42;local\&#42; or select a method to connect to a remote hypervisor.
    . After a connection is opened, click the new icon next to the hypervisor, or right-click on the active hypervisor and select \&#42;New\&#42;.
    . Configure the virtual machine following the steps in the \&#42;New VM\&#42; wizard.
    . Click \&#42;Finish\&#42; at the end of the wizard to provision the guest operating system. After a few moments a VNC window will appear. Proceed with the Fedora installation.



    == Managing virtual machines

    When the installation of the guest operating system is complete, it can be managed using the \&#96;virt-manager\&#96; program or via command line using \&#96;virsh\&#96;.

    === Managing guests with virt-manager

    . Start the Virtual Machine Manager by navigating to menu:[Applications]System Tools, or run:
    +
    ----
    $ virt-manager
    ----
    +
    If you are not root, you will be prompted to enter the root password.
    . Choose the host you wish to manage and click \&#42;Connect\&#42; in the \&#42;Open Connection\&#42; dialog window.
    . The list of virtual machines is displayed in the main window. Guests that are running will display a '\&gt;' icon. Guests that are not running will be greyed out.
    . To manage a particular guest, double click on it, or right click and select \&#42;Open\&#42;.
    . A new window for the guest will open that will allow you to use its console, see information about its virtual hardware and start, stop, and pause it.

    For further information about \&#96;virt-manager\&#96;, see https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/virtualization_deployment_and_administration_guide/sect-creating_guests_with_virt_manager[RedHat virt-manager guide].

    Bugs in the \&#96;virt-manager\&#96; tool should be reported in https://bugzilla.redhat.com[Bugzilla] against the \&#96;virt-manager\&#96;
    component.

    === Managing guests with virsh

    The \&#96;virsh\&#96; command-line utility allows you to manage virtual machines on the command line. The \&#96;virsh\&#96; utility is built around the libvirt management API:

    \&#42; \&#96;virsh\&#96; has a stable set of commands whose syntax and semantics are preserved across updates to the underlying virtualization platform.
    \&#42; \&#96;virsh\&#96; can be used as an unprivileged user for read-only operations (e.g. listing domains, listing domain statistics).
    \&#42; \&#96;virsh\&#96; can manage domains running under Xen, QEMU/KVM, ESX, or other back-ends with no perceptible difference to the user.

    To start a virtual machine:

    ----
    $ virsh create \&lt;name of virtual machine\&gt;
    ----

    To list the virtual machines currently running:

    ----
    $ virsh list
    ----

    To list all virtual machines, running or not:

    ----
    $ virsh list --all
    ----

    To gracefully power off a guest:

    ----
    $ virsh shutdown \&lt;virtual machine (name | id | uuid)\&gt;
    ----

    To non gracefully power off a guest:

    ----
    $ virsh destroy \&lt;virtual machine (name | id | uuid)\&gt;
    ----

    To save a snapshot of the machine to a file:

    ----
    $ virsh save \&lt;virtual machine (name | id | uuid)\&gt; \&lt;filename\&gt;
    ----

    To restore a previously saved snapshot:

    ----
    $ virsh restore \&lt;filename\&gt;
    ----

    To export the configuration file of a virtual machine:

    ----
    $ virsh dumpxml \&lt;virtual machine (name | id | uuid)
    ----

    For a complete list of commands available for use with \&#96;virsh\&#96;:

    ----
    $ virsh help
    ----

    Or consult the manual page: \&#96;man virsh\&#96;.

    Bugs in the \&#96;virsh\&#96; tool should be reported in https://bugzilla.redhat.com[Bugzilla] against the \&#42;libvirt\&#42; component.


    === Remote management

    The following remote management options are available:

    \&#42; If using non-root users via SSH, see the setup instructions in https://wiki.libvirt.org/page/SSHSetup
    \&#42; If using root for access via SSH, then create SSH keys for root, and use \&#96;ssh-agent\&#96; and \&#96;ssh-add\&#96; before launching \&#96;virt-manager\&#96;.
    \&#42; To use TLS, set up a local certificate authority and issue x509 certs to all servers and clients. For information on configuring this option, see https://wiki.libvirt.org/page/TLSSetup.



    == Other virtualization options

    === QEMU/KVM without libvirt

    QEMU/KVM can be invoked directly without libvirt, however you cannot to use tools such as \&#96;virt-manager\&#96;, \&#96;virt-install\&#96;, or \&#96;virsh\&#96;. Plain QEMU (without KVM) can also virtualize other processor architectures like ARM or PowerPC.

    === Xen

    Fedora can run as a Xen guest operating system and also be used as a Xen host (with the latter being true from Fedora 16; for using an earlier version of Fedora as a Xen host, check out the experimental repo available at https://myoung.fedorapeople.org/dom0). For a guide on how to install and setup a Fedora Xen host, see https://wiki.xen.org/wiki/Fedora_Host_Installation[Fedora Host Installation] page on the Xen Project wiki.

    === OpenStack

    OpenStack consists of a number of services for running infrastructure as a service (IaaS) clouds. They are the Object Store (Swift), Compute (Nova), and Image (Glance) services.

    === OpenNebula

    OpenNebula is an open source toolkit for data center virtualization.

    === oVirt

    The https://www.ovirt.org/[oVirt project] is an open virtualization
    project providing a end-to-end, server virtualization
    management system with advanced capabilities for hosts and guests,
    including high availability, live migration, storage management, system
    scheduler, and more.

    == Troubleshooting and known issues

    First take a look at the well-known  link:https://discussion.fedoraproject.org/tags/c/ask/common-issues/82/none/f38[common issues]. Replace the version number by the version you are actually using.

    For troubleshooting tips, see xref:virtualization-howto-debug-issues.adoc[Virtualization – How to Debug Issues]



    = Installing virtual operating systems with GNOME Boxes
    Ankursinha; Brunovernay; Hhlp
    :experimental:
    //:page-aliases:


    [abstract]
    GNOME Boxes is an application in GNOME Desktop Environment, which enables you to virtually access various operating systems.

    == Installing a virtual operating system from the list of predefined systems

    To install a virtual operating system:

    . Run \&#42;GNOME Boxes\&#42; using the \&#42;Super\&#42; key and type \&#96;Boxes\&#96;. In GNOME Boxes, click the \&#42;+\&#42; button and then \&#42;Create a Virtual Machine\&#42;.
    +
    image::Boxes_new_machine.png[New machine]

    . Download an operating system.
    +
    image::Download_os.png[Download your system]

    +
    Choose one of the predefined systems from the list.
    +
    image::Select_virtual_machine.png[Select machine]
    Alternatively, download an ISO image from the relevant website and select the file as shown in the screen below:
    +
    image::Select_from_file.png[Select from file]
    +
    . Review your installation.
    +
    image::Installation_review.png[Installation review]
    +
    To modify resources of the installed virtual operating system, such as RAM or disk size, click the \&#42;Customize\&#42; button.
    +
    image::Customize_resources.png[Customize resources]
    +
    . To start the installation of the virtual operating system, click the \&#42;Create\&#42; button.
    +
    The actual installation process may differ based on the selected operating system.
    +
    Installed systems are available to run in the main menu of \&#42;GNOME Boxes\&#42;.
    +
    image::Select_from_boxes_menu.png[Select operating system]



    = How to use QEMU
    Richard Gregory
    // :page-aliases:



    [abstract]
    QEMU is a very flexible virtualization technology however it is quite slow and it is recommended that you understand and evaluate alternative solutions before picking this one.
    Refer to xref:getting-started-with-virtualization.adoc[Getting started with virtualization]

    [[qemu]]
    == QEMU

    QEMU is a generic and open source processor emulator which achieves a good emulation speed by using dynamic translation.

    QEMU has two operating modes:

    \&#42; Full system emulation.
    In this mode, QEMU emulates a full system (for example a PC), including a processor and various peripherals.
    It can be used to launch different Operating Systems without rebooting the PC or to debug system code.
    \&#42; User mode emulation (Linux host only). In this mode, QEMU can launch Linux processes compiled for one CPU on another CPU.

    [[download]]
    == Download

    QEMU is available on Fedora repository. It can be installed by using xref:dnf.adoc[DNF]:

    \&#8230;.
    $ su -c 'dnf install qemu'
    \&#8230;.


    [[qemu-commands]]
    == QEMU commands

    To discover the qemu commands that are installed perform the following:

    \&#8230;.
    $ ls /usr/bin/qemu-\&#42;
    \&#8230;.

    In the following examples where 'qemu' is, substitute your command for executing qemu. E.g.

    \&#8230;.
    qemu-system-i386
    \&#8230;.

    or

    \&#8230;.
    qemu-i386
    \&#8230;.

    Of course, this does not apply to 'qemu-img'.

    [[qemu-virtual-machine-installation]]
    == QEMU virtual machine installation

    Create the virtual image for the system:

    \&#8230;.
    $ qemu-img create fedora.qcow 5G
    \&#8230;.

    Of course you are not obliged to take 5GB.

    Note: Even if you take 10GB this does NOT mean that the image does really HAVE the size of 10GB. It just means that your new system is limited up to 10GB - if the new system takes only 1,2 GB also the image will only be at 1,2GB.

    Now let's install the OS. Put in the install CD and type into your konsole (all in one line without break):

    \&#8230;.
    $ qemu -cdrom /dev/cdrom -hda fedora.qcow -boot d -net nic -net user -m 196 -rtc base=localtime
    \&#8230;.

    '-user -net' is important to have internet access within your new system.
    '-m 196' is the Set virtual RAM size (megabytes), default is 128 MB, I chose 196.

    The install may take some time. After the install, qemu will try to boot the new OS itself.
    Maybe this may fail (was the case for me) - but don't worry.
    If that happens: just close the qemu window and type the following command into your konsole to launch your new OS:

    \&#8230;.
    $qemu fedora.qcow -boot c -net nic -net user -m 196 -rtc base=localtime
    \&#8230;.

    [[testing-iso-images]]
    == Testing ISO Images

    Type, in the proper directory

    \&#8230;.
    $ qemu -m 512M -cdrom \&lt;isoname\&gt;.iso
    \&#8230;.

    [[debugging]]
    == Debugging

    To get kernel output dumped to a file outside the virtual system, add e.g. '-serial file:/tmp/qemu-output.log' to the qemu command line.
    When booting the virtual system, add 'console=ttyS0' to the kernel boot parameters.

    This output is particularly helpful if you are having trouble booting the system, in which case you may also wish to remove 'rhgb' and 'quiet' from the kernel boot parameters.


    = How to enable nested virtualization in KVM
    Fedora Documentation Team

    // Optional  free form useful additional information as comment


    [abstract]
    //------
    Nested virtualization allows you to run a virtual machine (VM) inside another VM while still using hardware acceleration from the host.
    //------


    // ===========================================
    // include::{partialsdir}/proc_enabling-nested-virtualization-in-kvm.adoc[leveloffset=+1]
    // ===========================================


    == Checking if nested virtualization is supported

    For Intel processors, check the \&#96;/sys/module/kvm_intel/parameters/nested\&#96; file. For AMD processors, check the \&#96;/sys/module/kvm_amd/parameters/nested\&#96; file. If you see \&#96;1\&#96; or \&#96;Y\&#96;, nested virtualization is supported; if you see \&#96;0\&#96; or \&#96;N\&#96;, nested virtualization is not supported.

    For example:

    ----
    cat /sys/module/kvm_intel/parameters/nested
    Y
    ----


    == Enabling nested virtualization

    To enable nested virtualization for Intel processors:

    . Shut down all running VMs and unload the \&#96;kvm_probe\&#96; module:
    +
    ----
    sudo modprobe -r kvm_intel
    ----
    . Activate the nesting feature:
    +
    ----
    sudo modprobe kvm_intel nested=1
    ----
    +
    . Nested virtualization is enabled until the host is rebooted. To enable it permanently, add the following line to the \&#96;/etc/modprobe.d/kvm.conf\&#96; file:
    +
    ----
    options kvm_intel nested=1
    ----

    To enable nested virtualization for AMD processors:

    . Shut down all running VMs and unload the \&#96;kvm_amd\&#96; module:
    +
    ----
    sudo modprobe -r kvm_amd
    ----
    . Activate the nesting feature:
    +
    ----
    sudo modprobe kvm_amd nested=1
    ----
    . Nested virtualization is enabled until the host is rebooted. To enable it permanently, add the following line to the \&#96;/etc/modprobe.d/kvm.conf\&#96; file:
    +
    ----
    options kvm_amd nested=1
    ----


    // ===========================================
    // include::{partialsdir}/proc_configuring-nested-virtualization-in-virt-manager.adoc[leveloffset=+1]
    // ===========================================
    // [[proc_configuring-nested-virtualization-in-virt-manager]]
    == Configuring nested virtualization in virt-manager

    Configure your VM to use nested virtualization:

    . Open virt-manager, double-click the VM in which you wish to enable nested virtualization, and click the \&#42;Show virtual hardware details\&#42; icon.

    . Click \&#42;CPUs\&#42; in the side menu. In the \&#42;Configuration\&#42; section, there are two options - either type \&#96;host-passthrough\&#96; in the \&#42;Model:\&#42; field, or select the \&#42;Copy host CPU configuration\&#42; check box (that fills the \&#96;host-model\&#96; value in the \&#42;Model\&#42; field).
    +
    NOTE: Using host-passthrough is not recommended for general usage. It should only be used for nested virtualization purposes.
    +
    . Click \&#42;Apply\&#42;.


    // ===========================================
    // include::{partialsdir}/proc_testing-nested-virtualization.adoc[leveloffset=+1]
    // ===========================================
    // [[proc_testing-nested-virtualization]]
    == Testing nested virtualization

    . Start the virtual machine.
    . On the virtual machine, run:
    +
    ----
    sudo dnf group install virtualization
    ----
    +
    . Verify that the virtual machine has virtualization correctly set up:
    +
    ----
    sudo virt-host-validate
    QEMU: Checking for hardware virtualization                                 : PASS
    QEMU: Checking if device /dev/kvm exists                                   : PASS
    QEMU: Checking if device /dev/kvm is accessible                            : PASS
    QEMU: Checking if device /dev/vhost-net exists                             : PASS
    QEMU: Checking if device /dev/net/tun exists                               : PASS
    \&#8230;
    ----


    == Additional resources

    \&#42; https://bugzilla.redhat.com/show_bug.cgi?id=1055002
    \&#42; https://kashyapc.wordpress.com/2012/01/14/nested-virtualization-with-kvm-intel/
    \&#42; https://kashyapc.wordpress.com/2012/01/18/nested-virtualization-with-kvm-and-amd/




    = Creating Windows virtual machines using virtIO drivers
    Cole Robinson
    //:page-aliases:


    Fedora infrastructure hosts virtIO drivers and additional software agents for Windows virtual machines running on kernel-based virtual machines (KVM). https://www.linux-kvm.org/page/Virtio[virtIO] is a virtualization standard for network and disk device drivers.

    Fedora cannot ship Windows virtIO drivers because they cannot be built automatically as part of Fedora’s build system: the only way to build Windows virtIO drivers is on a machine running Windows.  In addition, shipping pre-compiled sources is generally against Fedora policies.  Microsoft does not provide virtIO drivers, you must download them yourself in order to make virtIO drivers available for Windows VMs running on Fedora hosts.

    For details on downloading the drivers, please see: https://github.com/virtio-win/virtio-win-pkg-scripts/blob/master/README.md



    = \&#42;VMware\&#42; – What is it and How use it?
    Héctor Louzao; The Fedora Docs team
    :page-aliases: how-to-use-vmware.adoc


    VMware provides cloud computing and virtualization software and services, their most important products are:

    \&#42;\&#42; VMware Workstation Player, is a virtualization software package and can run existing virtual appliances and create its own virtual machines (which require an operating system to be installed to be functional). VMware Player is available for personal non-commercial use.

    \&#42;\&#42; VMware Workstation Pro, it enables users to set up virtual machines (VMs) on a single physical machine, and use them simultaneously along with the actual machine. Each virtual machine can execute its own operating system, including versions of Microsoft Windows, Linux, BSD, and MS-DOS.

    \&#42;\&#42; https://www.vmware.com/products/desktop-hypervisor/workstation-and-fusion[VMware Player/Workstation]

    [IMPORTANT]

    Wmware is now free for commercial, educational, and personal use!, the free version includes all the features from the former paid versions.

    == How to Download VMware

    To download any Product::

    \&#42; Navigate to Broadcom Support: https://support.broadcom.com/[Broadcom Support] and create an account.
    \&#42; From the Software menu section, select VMware Cloud Foundation then My Downloads.
    \&#42; Click on VMware Workstation Player/VMware Workstation Pro.
    \&#42; Click on your release.
    \&#42; Click Download.

    == How to Resolve Issues for WORKSTATION and PLAYER (ANY KERNEL + ANY VERSION)

    === Installation

    ==== Player

    ----
    $ sudo chmod +x ./VMware-Player-x.y.z-nn.x86_64.bundle
    $ sudo ./VMware-Player-x.y.z-nn.x86_64.bundle
    ----

    ==== Workstation

    ----
    $ sudo chmod +x ./VMware-Workstation-Full-x.y.z-nn.x86_64.bundle
    $ sudo ./VMware-Workstation-Full-x.y.z-nn.x86_64.bundle
    ----

    === Resolving Conflict with Kernel

    The problem here is always the same \&#96;vmnet\&#96; and \&#96;vmmon\&#96; doesn’t start well or doesn’t start at all, You should find a PATCH deal with changes in vmmon.c and vmnet.c because something breaks or add some parameters to these files, you can found the following:

    \&#42;\&#42; know what is your kernel version?: \&#96;uname -r\&#96;.
    \&#42;\&#42; know your Vmware version or install the latest. \&#96;/usr/bin/vmware -v\&#96;
    \&#42;\&#42; Try to find the PATCH for a specific KERNEL version and Vmware.
    \&#42;\&#42; You have to deal with sources ( \&#42;\&#42;vmnet\&#42;\&#42; and \&#42;\&#42;vmmon\&#42;\&#42; ) and apply fixed in both of them.
    \&#42;\&#42; Try to find the fix for the specific product Vmware and Kernel version.

    NOTE: This guide try to help with all this boring stuff.

    === Prerequisite

    ----
    $ sudo dnf install kernel-devel kernel-headers gcc gcc-c++ make git
    ----

    === Installation

    This repository tracks patches needed to build VMware (Player and Workstation) host modules against recent kernels.

    For Example, I would like to Patch Workstation:

    ----
    wget https://github.com/mkubecek/vmware-host-modules/archive/workstation-x.y.z.tar.gz
    tar -xzf workstation-x.y.z.tar.gz
    cd vmware-host-modules-workstation-x.y.z
    make
    sudo make install
    ----

    [IMPORTANT]

    Based on your VMware product, replace “x.y.z” with your installed version and/or “workstation” with “player”.

    === Dealing with Secure Boot and VMware modules

    Options are available but for the moment __Disable Secure Boot__ is the best option.

    === Deal with Kernel Updates

    You can create a script to take of this after a kernel update. Save it as \&#96;/etc/kernel/install.d/99-vmmodules.install\&#96;:

    ----
    \&#35;!/usr/bin/bash

    export LANG=C

    COMMAND='$1'
    KERNEL_VERSION='$2'
    BOOT_DIR_ABS='$3'
    KERNEL_IMAGE='$4'

    ret=0

    case '$COMMAND' in
    add)
    VMWARE_VERSION=$(cat /etc/vmware/config | grep player.product.version | sed '/.\&#42;\'\(.\&#42;\)\'.\&#42;/ s//\1/g')

    [ -z VMWARE_VERSION ] \&amp;\&amp; exit 0

    mkdir -p /tmp/git; cd /tmp/git
    git clone -b workstation-${VMWARE_VERSION} https://github.com/mkubecek/vmware-host-modules.git
    cd vmware-host-modules
    make VM_UNAME=${KERNEL_VERSION}
    make install VM_UNAME=${KERNEL_VERSION}

    ((ret+=$?))
    ;;
    remove)
    exit 0
    ;;
    \&#42;)
    usage
    ret=1;;
    esac

    exit $ret
    ----

    === Additional Resources

    - link:https://github.com/mkubecek/vmware-host-modules[VMware Git Repo]


    = Using UEFI with QEMU
    Cole Robinson; Caleb McKee; Petr Bokoc


    [[firmware-installation]]
    == Firmware installation

    UEFI for x86 QEMU/KVM VMs is called OVMF (Open Virtual Machine Firmware). It comes from EDK2 (EFI Development Kit), which is the UEFI reference implementation.

    [[installing-uefi-for-qemu-from-fedora-repos]]
    == Installing 'UEFI for QEMU' from Fedora repos

    Since June 2016, OVMF is available in Fedora repositories. All you need to have installed is \&#96;edk2-ovmf\&#96; RPM. Furthermore, it should be now a dependency of the package, so you probably have it installed already. This includes firmware for secureboot (\&#96;OVMF_CODE.secboot.fd\&#96;)

    [[installing-uefi-for-qemu-nightly-builds]]
    == Installing 'UEFI for QEMU' nightly builds

    Gerd Hoffmann, Red Hatter and QEMU developer, has a dnf repo on his personal site that provides nightly builds of a whole bunch of QEMU/KVM firmware, including EDK2/OVMF.

    Here's how to pull down the nightly builds for x86:

    [source,bash]
    ----
    […]\&#35; sudo dnf install dnf-plugins-core
    […]\&#35; sudo dnf config-manager addrepo --from-repofile=http://www.kraxel.org/repos/firmware.repo
    […]\&#35; sudo dnf install edk2.git-ovmf-x64
    ----

    Note, these are nightly builds, and may occasionally be broken.

    [[optionally-configure-libvirtd-to-advertise-uefi-support]]
    == Optionally Configure libvirtd to advertise UEFI support

    Libvirt needs to know about UEFI-\&gt;NVRAM config file mapping, so it can advertise it to tools like virt-manager/virt-install. On Fedora 22 and later, libvirt packages are configured to look for the nightly build paths, so this will work out of the box.

    However, if you want to use custom binaries, you will need to edit the \&#96;nvram\&#96; variable in \&#96;/etc/libvirt/qemu.conf\&#96; and restart libvirtd.

    [[creating-a-vm]]
    == Creating a VM

    [[virt-manager]]
    === virt-manager

    Create a new VM in virt-manager. When you get to the final page of the
    'New VM' wizard, do the following:

    \&#42; Click 'Customize before install', then select 'Finish'
    \&#42; On the 'Overview' screen, change the 'Firmware' field to select the 'UEFI x86_64' option.
    \&#42; Click 'Begin Installation'
    \&#42; The boot screen you'll see should use \&#96;linuxefi\&#96; commands to boot the
    installer, and you should be able to run \&#96;efibootmgr\&#96; inside that
    system, to verify that you're running an UEFI OS.

    [[virt-install]]
    === virt-install

    Add \&#96;--boot uefi\&#96; to your \&#96;virt-install\&#96; command. Example:

    [source,bash]
    ----
    sudo virt-install --name f20-uefi \
    +   --ram 2048 --disk size=20 \
    +   --boot uefi \
    +   --location https://dl.fedoraproject.org/pub/fedora/linux/releases/22/Workstation/x86_64/os/
    +
    ----

    [[testing-secureboot-in-a-vm]]
    == Testing Secureboot in a VM

    These steps describe how to test Fedora Secureboot support inside a KVM VM. The audience here is QA folks that want to test secureboot, and any other curious parties. This requires configuring the VM to use UEFI, so it builds upon the previous UEFI steps.

    [[run-enrolldefaultkeys.efi]]
    === Run EnrollDefaultKeys.efi

    (Formerly this article recommended the independent utility 'LockDown_ms.efi'.)

    Since OVMF doesn't ship with any SecureBoot keys installed, we need to
    install some to mimic what an MS certified UEFI machine will ship with.
    OVMF now ships with the binaries required to set up a default set of
    keys. The easiest way is to use UefiShell.iso which is available at
    \&#96;/usr/share/edk2/ovmf/UefiShell.iso\&#96;. Boot your VM with this as the
    CD-ROM image and it should boot into the UEFI shell. At the prompt

    \&#42; Shell\&gt; fs0:
    \&#42; FS0:\\&gt; EnrollDefaultKeys.efi
    \&#42; FS0:\\&gt; reset
    \&#42; The VM will restart. Let it boot into Fedora as normal. Log in
    \&#42; You should see the string 'Secure boot enabled' in dmesg. Secureboot
    is now enabled for every subsequent boot.

    [[testing-fedora-cddvd-secure-boot-in-a-vm]]
    === Testing Fedora CD/DVD Secure Boot in a VM

    Once you have a secureboot configured VM as described above, it's easy
    to use this to test ISO media secureboot support.

    \&#42; Use virt-manager to attach the ISO media to your VM
    \&#42; Use virt-manager to change the VM boot settings to boot off the CDROM
    \&#42; Start the VM
    \&#42; Switch to a terminal inside the VM, verify Secureboot is enabled by
    checking dmesg

    [[notes]]
    == Notes

    [[using-uefi-with-aarch64-vms]]
    === Using UEFI with AArch64 VMs

    Fedora's AArch64 releases will only run on UEFI, so require UEFI inside the VM. However the steps are slightly different. See this page for complete documentation:
    https://fedoraproject.org/wiki/Architectures/AArch64/Install_with_QEMU

    [[extra-links]]
    == Extra links

    \&#42; http://www.linux-kvm.org/page/OVMF[KVM wiki OVMF page]
    \&#42; https://wiki.ubuntu.com/SecurityTeam/SecureBoot[Ubuntu secureboot
    page]
    \&#42; http://en.opensuse.org/openSUSE:UEFI_Secure_boot_using_qemu-kvm[OpenSUSE
    secureboot page]
    \&#42; http://www.labbott.name/blog/2016/09/15/secure-ish-boot-with-qemu/[Using
    SecureBoot with QEMU]


    = Virtualization – How to Debug Issues
    Markmc ; Crobinso ; Voxadam
    //:page-aliases:
    // :experimental:

    //include::{partialsdir}/attributes.adoc[]

    [IMPORTANT]
    ====
    .\&#42;Work in progress!\&#42;
    This page was taken from the previous Fedora Wiki documentation.

    It has been cleaned up for publishing here on the Fedora Docs Portal, but it has not yet been reviewed for technical accuracy.

    Don't use it for now. It is probably

    \&#42; Containing formatting issues
    \&#42; Out-of-date
    \&#42; In need of other love

    Reviews for technical accuracy are greatly appreciated. If you want to help, see the https://pagure.io/fedora-docs/quick-docs/blob/master/f/README.md[README file] in the source repository for instructions.

    Pull requests accepted at https://pagure.io/fedora-docs/quick-docs

    Once you've fixed this page, remove this notice.
    ====
    // Migrated from
    // https://fedoraproject.org/wiki/How_to_debug_Virtualization_problems



    == Effective bug reporting

    Reporting bugs effectively is an important skill for any Fedora user or developer.

    Narrowing down the possible causes of the bug and providing the right information in the bug report allows a bug to be resolved quickly. Filing a bug report with little useful information can mean that your bug lays unresolved, possibly until it is closed automatically when the distribution version reaches 'end of life'.

    See xref:bugzilla-file-a-bug.adoc[how to file a bug report] for generic information on filing bugs. This page contains information specific to virtualization bugs.

    // Note: if you're filing a virtualization related bug against a package which isn't on [[Virtualization\&#35;Relevant_Packages|this list]], then please cc the [mailto:fedora-virt-maint@redhat.com fedora-virt-maint@redhat.com] alias in bugzilla to ensure virt developers see the bug.

    == Version Information

    Once you've ensured you have the latest updates installed
    //for the [[Virtualization\&#35;Relevant_Packages|relevant packages]]
    , gather details of the version numbers of those packages e.g.
    [source,]
    ----
    […]$ rpm -q qemu-kvm qemu-common python-virtinst virt-viewer virt-manager
    ----

    To find out what kernel version you are currently running, and what machine architecture you're using:

    [source,]
    ----
    […]$ uname -a
    ----

    Of course, you should also make sure to file the bug using the appropriate version of Fedora. Rawhide users should file bugs using the 'rawhide' version.

    == Hardware Information

    Fedora's virtualization capabilities rely heavily on hardware capabilities, so when filing bugs please include copious information on your hardware platform including:

    [source,]
    ----
    […]$ cat /proc/cpuinfo
    […]$ lspci -vvv
    […]$ virt-host-validate
    ----

    You can also check what virtualization capabilities are available on your machine by running:

    [source,]
    ----
    […]$ virsh capabilities
    ----

    == Guest Configuration

    When filing a bug related to problems seen in the guest, include full details on the guest configuration including CPU architecture, RAM size, devices etc. This is most easily done by including the output of \&#96;virsh dumpxml MyGuest\&#96; or, in the case of qemu, the full qemu command line.

    == Virt Manager

    Virt Manager stores a logfile in \&#96;~/.cache/virt-manager/virt-manager.log\&#96;.

    Examine the log file and include any pieces that look like they might be useful in the bug report. If in doubt, attach the whole file to the bug.

    You can also run virt-manager from the command line using \&#96;virt-manager --no-fork\&#96; and check whether any relevant messages were printed there.

    == virt-install

    virt-install stores a log file in ' ~/.cache/virtinst/virt-install.log\&#96;.

    Run \&#96;virt-install\&#96; using the \&#96;--debug\&#96; option to get detailed debug spew.

    In order to gain access to a serial console during the install, you can use \&#96;-x 'console=ttyS0'\&#96;. Using a serial console combined with a VNC install can be very useful for debugging e.g. \&#96;--nographics -x 'console=ttyS0 vnc'\&#96;

    == libvirt

    Any program using libvirt can be debugged using the \&#96;LIBVIRT_DEBUG=1\&#96; environment variable e.g.
    [source,]
    ----
    […]$ LIBVIRT_DEBUG=1 virt-manager --no-fork
    […]$ LIBVIRT_DEBUG=1 virsh list --all
    ----

    If your issue looks like it might be related to \&#96;libvirtd\&#96; try looking in \&#96;/var/log/messages\&#96; for any error messages.

    You can also use  link:http://libvirt.org/logging.html[/etc/libvirt/libvirtd.conf logging configuration] to e.g. log debug spew to a file:

    [source,]
    ----
    log_level = 1
    log_outputs = 0:file:/tmp/libvirtd.log
    ----

    Alternatively, you could try running \&#96;libvirtd\&#96; from the command line with debugging options enabled:

    [source,]
    ----
    […]\&#35; systemctl stop libvirtd
    […]\&#35; LIBVIRT_DEBUG=1 libvirtd --verbose
    ----

    == libguestfs

    If link:https://libguestfs.org/[libguestfs], link:https://libguestfs.org/guestfish.1.html[guestfish], link:https://libguestfs.org/virt-df.1.html[virt-df] etc. are causing problems, run:

    [source,]
    ----
    […]\&#35; libguestfs-test-tool
    ----

    If everything is working, near the end of the output you will see

    \&#96;===== TEST FINISHED OK =====\&#96;.

    If things are not working, post the __complete, unedited__ output of that command into a bug report.

    == Networking

    If you are having trouble with guests connected to a libvirt link:https://libvirt.org/formatnetwork.html[virtual network], link:https://wiki.libvirt.org/page/Networking[shared physical interface] or bridge, try these commands:

    [source,]
    ----
    […]\&#35; virsh net-list --all
    […]\&#35; brctl show
    […]\&#35; sysctl net.bridge.bridge-nf-call-iptables
    […]\&#35; iptables -L -v -n
    […]\&#35; ps -ef | grep dnsmasq
    […]\&#35; ifconfig -a
    […]\&#35; cat /proc/sys/net/ipv4/ip_forward
    […]\&#35; service libvirtd reload
    ----

    If you find that \&#96;/proc/sys/net/ipv4/ip_forward\&#96; is not being set to \&#96;1\&#96; at boot time, try looking at the ordering of the libvirtd and NetworkManager services:

    [source,]
    ----
    […]\&#35; find /etc/rc.d -regex '.\&#42;rc[35].d/S.\&#42;\(libvirtd\|NetworkManager\)'
    […]\&#35; rm -f /etc/chkconfig.d/libvirtd /etc/chkconfig.d/NetworkManager
    […]\&#35; chkconfig libvirtd resetpriorities
    […]\&#35; chkconfig NetworkManager resetpriorities
    […]\&#35; find /etc/rc.d -regex '.\&#42;rc[35].d/S.\&#42;\(libvirtd\|NetworkManager\)'
    ----


    //  CONTINUE MIGRATION HERE

    == kvm

    See also the [http://www.linux-kvm.org/page/Bugs KVM wiki page on reporting bugs].

    The output of any \&lt;code\&gt;qemu-kvm\&lt;/code\&gt; command run by \&lt;code\&gt;libvirtd\&lt;/code\&gt; is stored in \&lt;code\&gt;/var/log/libvirt/qemu/GuestName.log\&lt;/code\&gt;.

    [[Testing_KVM_with_kvm_autotest|kvm-autotest]] is an excellent way of testing basic KVM functionality.

    == Xen ==

    Some useful information on how to debug Xen issues can be found in the [http://wiki.xen.org/wiki/Debugging_Xen Debugging Xen] Wiki page. If you think you found an actual bug, you may want to follow the steps outlined either on the [http://wiki.xen.org/wiki/Reporting_Bugs_against_Xen Reporting Bugs against Xen] Wiki page, or on [http://blog.xen.org/index.php/2013/06/04/reporting-a-bug-against-the-xen-hypervisor/ this] blog post.

    The bugs that have been reported and are currently being tracked by the Xen developers are collected in the [http://bugs.xenproject.org/xen/ Xen Hypervisor Bug Tracker], so you may want to have a look there, to see if the bug you found is already being taken care of.

    Some more useful information:

    \&#42; log files are available at \&lt;code\&gt;/var/log/xen/\&lt;/code\&gt;, for both HVM and PV guests (look for your guest name and domain ID)
    \&#42; if your guest is crashing, we suggest you do the following:
    \&#42;\&#42; Set 'on_crash=preserve' in your domain config file
    \&#42;\&#42; Copy the guest kernel's System.map to the host
    \&#42;\&#42; Once the guest has crashed, run \&lt;code\&gt;/usr/lib/xen/bin/xenctx -s System.map \&amp;lt;domid\&amp;gt;\&lt;/code\&gt;

    == General Tips ==

    === System Log Files ===

    Always look in \&lt;code\&gt;dmesg\&lt;/code\&gt;, \&lt;code\&gt;/var/log/messages\&lt;/code\&gt; etc. for any useful information.

    === strace ===

    \&lt;code\&gt;strace\&lt;/code\&gt; can often shed light on a bug - e.g. if you run \&lt;code\&gt;virt-manager\&lt;/code\&gt;, or \&lt;code\&gt;libvirtd\&lt;/code\&gt; or \&lt;code\&gt;qemu-kvm\&lt;/code\&gt; under strace you can see what files they accessed, what commands they executed, what system calls they invoked etc.:

    \&lt;pre\&gt;
    $\&gt; strace -ttt -f libvirtd
    \&lt;/pre\&gt;

    If the program in question is already running, you can attach to it using \&lt;code\&gt;strace -p\&lt;/code\&gt;.

    === gdb ===

    \&lt;code\&gt;gdb\&lt;/code\&gt; can often be useful to trace the execution of a program. However, in order to get useable information, you will need to install 'debuginfo' packages. See the [[StackTraces]] page for more information.

    === SELinux ===

    If you see 'AVC denied' or 'setroubleshoot' messages in \&lt;code\&gt;/var/log/messages\&lt;/code\&gt;, your bug might be caused by an SELinux policy issue. Try temporarily putting SELinux into 'permissive' mode with:

    \&lt;pre\&gt;
    $\&gt; setenforce 0
    \&lt;/pre\&gt;

    If this makes your bug go away that doesn't mean your bug is fixed, it just narrows down the cause! You should include the AVC details from \&lt;code\&gt;ausearch -m AVC -ts recent\&lt;/code\&gt; in the bug report, or if the message includes a \&lt;code\&gt;sealert -l\&lt;/code\&gt; command then include the details printed by the command.

    One common cause of SELinux problems is mislabeled files. Try:

    \&lt;pre\&gt;
    $\&gt; restorecon /path/to/file/in/selinux/message
    \&lt;/pre\&gt;

    If you are installing using an ISO on an NFS mount, you need to ensure that it is mounted using the \&lt;code\&gt;virt_content_t\&lt;/code\&gt; label:

    \&lt;pre\&gt;
    $\&gt; mount -o context='system_u:object_r:virt_content_t:s0' \&#8230;
    \&lt;/pre\&gt;

    If you are using libvirt storage pools, like nfs, or USB pass-through, you might want to check, or toggle one of the following SELinux booleans: virt_use_comm, virt_use_fusefs, virt_use_nfs, virt_use_samba, virt_use_usb.

    \&lt;pre\&gt;
    $\&gt; getsebool virt_use_nfs
    virt_use_nfs --\&gt; off
    $\&gt; setsebool -P virt_use_nfs on
    \&lt;/pre\&gt;

    == Troubleshooting =

    === Permission issues ==

    Prior to Fedora 11/libvirt 0.6.1, all virtual machines run through libvirt were run as root, giving full administrator capabilities. While this simplified VM management, it was not very security conscious: a compromised virtual machine could possibly have administrator privileges on the host machine.

    In Fedora 11/libvirt-0.6.1, security started to improve with the addition of [[Features/SVirt_Mandatory_Access_Control|svirt]]. In a nutshell, libvirt attempts to automatically apply selinux labels to every file a VM needs to use, like disk images. If a VM tries to open a file that libvirt didn't label, permission will be denied.

    Fedora 12 saw things improve even more. As of libvirt-0.6.5, VMs were now launched with reduced process capabilities. This prevented the VM from doing things like altering host network configuration (something it shouldn't typically need to do). And as of libvirt-0.7.0, the VM emulator process was no longer run as 'root' by default, instead being run as an unprivleged 'qemu' user.

    While all these changes are great for security, they broke previously working setups which depended on the relaxed VM permissions. Most issues have work arounds that come at the expense of security. Over time, many of these issues should be made to 'just work', but we aren't there yet.

    === Changing the QEMU/KVM process user ===

    {{admon/warning|Changing the QEMU/KVM process user has security implications.}}

    To change the user that libvirt will run the QEMU/KVM process as, edit /etc/libvirt/qemu.conf and uncomment and change the user= and group= fields. For example, if wanting to run KVM as the user 'foobar', you would set the fields to \&lt;pre\&gt;\&#8230;
    user='foobar'
    group='foobar'
    \&#8230;\&lt;/pre\&gt; Then restart libvirtd with \&lt;pre\&gt;service libvirtd restart\&lt;/pre\&gt;

    === Changing SVirt/Selinux configuration ===

    {{admon/warning|Changing the SVirt/SELinux settings may have security implications.}}

    SVirt can be disabled for the libvirt QEMU driver by editing /etc/libvirt/qemu.conf, uncommenting and setting \&lt;pre\&gt;security_driver='none'\&lt;/pre\&gt; Then restart libvirtd with \&lt;pre\&gt;service libvirtd restart\&lt;/pre\&gt;

    === Changing QEMU/KVM process capabilities ===

    {{admon/warning|Changing the this setting has security implications.}}

    Libvirt by default launches QEMU/KVM guests with reduced process capabilities. To disable this feature, edit /etc/libvirt/qemu.conf, uncomment and set \&lt;pre\&gt;clear_emulator_capabilities=0\&lt;/pre\&gt; Then restart libvirtd with \&lt;pre\&gt;service libvirtd restart\&lt;/pre\&gt;

    == KVM performance issues ==

    Often times, VM slowness is caused because the VM is using plain QEMU and not KVM.

    === Ensuring system is KVM capable ===

    Verify that the KVM kernel modules are properly loaded:

    \&lt;pre\&gt;
    $ lsmod | grep kvm
    kvm
    kvm_intel
    \&lt;/pre\&gt;

    If that command did not list kvm_intel or kvm_amd, KVM is not properly configured. See [http://www.linux-kvm.org/page/FAQ\&#35;How_can_I_tell_if_I_have_Intel_VT_or_AMD-V.3F| this KVM wiki page] to ensure your hardware supports virtualization extensions. If it doesn't, you cannot use KVM acceleration, only plain QEMU is an option.

    If your hardware does support virtualization extensions, try to reload the kernel modules with:

    \&lt;pre\&gt;
    su -c 'bash /etc/sysconfig/modules/kvm.modules'
    \&lt;/pre\&gt;

    Retry the above lsmod command and see if you get the desired output. If not, or if the kvm.modules command produces an error, check the output of:

    \&lt;pre\&gt;
    dmesg | grep -i kvm
    \&lt;/pre\&gt;

    If you see 'KVM: disabled by BIOS', please see the [http://www.linux-kvm.org/page/FAQ\&#35;.22KVM:_disabled_by_BIOS.22_error| relevant KVM wiki page]
    Any other error message is probably a bug, and should be reported.

    If all that works out fine, you want to make your that your VMs are actually using KVM

    === Is My Guest Using KVM? ===

    Often people are unsure whether their qemu guest is actually using hardware virtualization via KVM.

    Firstly, check that libvirt thinks KVM is available:

    \&lt;pre\&gt;
    $\&gt; virsh capabilities  | grep kvm
    \&lt;domain type='kvm'\&gt;
    \&lt;emulator\&gt;/usr/bin/qemu-kvm\&lt;/emulator\&gt;
    \&lt;/pre\&gt;

    If that does not return anything, try this command to further identify what might need fixing to enable KVM support:

    \&lt;pre\&gt;
    $\&gt; virt-host-validate
    \&lt;/pre\&gt;

    Next, check that the guest is configured to use KVM:

    \&lt;pre\&gt;
    $\&gt; virsh dumpxml ${guest} | grep kvm
    \&lt;domain type='kvm' id='18'\&gt;
    \&lt;emulator\&gt;/usr/bin/qemu-kvm\&lt;/emulator\&gt;
    \&lt;/pre\&gt;

    If that does not return anything, you want to make \&lt;domain type='kvm'\&gt; and \&lt;emulator\&gt;/usr/bin/qemu-kvm\&lt;/emulator\&gt;, using the command:

    \&lt;pre\&gt;
    virsh edit ${guest}
    \&lt;/pre\&gt;

    Next, look in \&lt;code\&gt;/var/log/libvirt/qemu/${guest}.log\&lt;/code\&gt; to check that \&lt;code\&gt;/usr/bin/qemu-kvm\&lt;/code\&gt; is the emulator that was executed by libvirt and that there are no error messages about \&lt;code\&gt;/dev/kvm\&lt;/code\&gt;.

    If you want to get really funky, you can check whether \&lt;code\&gt;qemu-kvm\&lt;/code\&gt; has \&lt;code\&gt;/dev/kvm\&lt;/code\&gt; open:

    \&lt;pre\&gt;
    $\&gt; for iii in /proc/$(ps h -o tid -C qemu-kvm)/fd/\&#42;; do readlink $iii; done | grep kvm
    anon_inode:kvm-vcpu
    /dev/kvm
    anon_inode:kvm-vm
    \&lt;/pre\&gt;

    == Serial console access for troubleshooting and management ==

    Serial console access is useful for debugging kernel crashes and remote management can be very helpful.

    Fully-virtualized guest OS will automatically have a serial console configured, but the guest kernel will not be configured to use this out of the box. To enable the guest console in a Linux fully-virt guest, edit the /etc/grub.conf in the guest and add 'console=tty0 console=ttyS0'. This ensures that all kernel messages get sent to the serial console, and the regular graphical console. The serial console can then be access in same way as paravirt guests:

    \&lt;pre\&gt;
    su -c 'virsh console \&amp;lt;domain name\&amp;gt;'
    \&lt;/pre\&gt;

    Alternatively, the graphical \&lt;code\&gt;virt-manager\&lt;/code\&gt; program can display the serial console. Simply display the 'console' or 'details' window for the guest \&amp; select 'View -\&gt; Serial console' from the menu bar. \&lt;code\&gt;virt-manager\&lt;/code\&gt; may need to be run as root to have sufficient privileges to access the serial console.

    == Graphical console access ==

    In order to get a graphical console on your guest you can either use 'virt-manager' and select the console icon for the guest, or you can use the 'virt-viewer' tool to just directly connect to the console:

    \&lt;pre\&gt;
    virt-viewer guestname
    \&lt;/pre\&gt;

    == Accessing data on guest disk images ==

    {{Admon/caution | If the guest image might be live, you must only use read-only access, otherwise you risk corrupting the disk image.\&lt;br\&gt;\&lt;br\&gt;It is always safe to use \&lt;code\&gt;guestfish --ro\&lt;/code\&gt;}}

    The [http://libguestfs.org/guestfish.1.html guestfish] program lets you manipulate guest disk images without needing to run the guest:

    \&lt;pre\&gt;
    su -c 'yum install guestfish'
    guestfish -d NameOfGuest -i --ro
    \&amp;gt;\&amp;lt;fs\&amp;gt; ll /
    \&amp;gt;\&amp;lt;fs\&amp;gt; cat /boot/grub/grub.conf
    \&lt;/pre\&gt;

    See \&lt;code\&gt;man guestfish\&lt;/code\&gt; and [http://libguestfs.org/ the libguestfs website] for information and examples.   guestfish can also be scripted.

    [http://libguestfs.org/virt-rescue.1.html virt-rescue] is an alternative libguestfs tool which you can use to make ad hoc changes.  [http://libguestfs.org/virt-edit.1.html virt-edit] can be used to edit single files in guests, eg:

    \&lt;pre\&gt;
    virt-edit NameOfGuest /boot/grub/grub.conf
    \&lt;/pre\&gt;

    == Known issues

    [discrete]
    === Audio output

    Audio has always been difficult to get working with libvirt, but the recent security changes have actually provided the mechanisms to make it work. The primary problem is that the VM is not sending sound output to your user's pulseaudio session. There may be a pulseaudio option to work around this issue, but I've managed to make it work with:

    \&#42; [[SELinux/FAQ\&#35;How_do_I_enable_or_disable_SELinux_.3F|Set selinux to permissive]].
    \&#42; Configure libvirt to [[\&#35;Changing_the_QEMU.2FKVM_process_user|run guests as your regular user]]
    \&#42; Set \&lt;pre\&gt;vnc_allow_host_audio = 1\&lt;/pre\&gt; in /etc/libvirt/qemu.conf, and restart libvirtd with \&lt;pre\&gt;service libvirtd restart\&lt;/pre\&gt;

    This will eventually be solved out of the box by having the VNC graphical client receive audio from the VM and play it as the current user. Some code exists to handle this for virt-viewer/virt-manager, but it isn't 100% complete yet. For more info, see [https://bugzilla.redhat.com/show_bug.cgi?id=595880 gtk-vnc bug 595880], [https://bugzilla.redhat.com/show_bug.cgi?id=536692 libvirt SDL audio bug 536692], [https://bugzilla.redhat.com/show_bug.cgi?id=508317 libvirt VNC audio bug 508317]

    [discrete]
    === SDL Graphics

    QEMU needs access to your $XAUTHORITY file in order to use SDL graphics.

    \&#42; Configure SDL graphics for your VM. Easiest way to do this:

    \&lt;pre\&gt;$\&gt; echo \&lt;graphics type='sdl display='$DISPLAY' xauth='$XAUTHORITY'/\&gt;
    \&lt;graphics type='sdl display=':0.0' xauth='/home/cole/.Xauthority'/\&gt;
    (copy that string)
    $\&gt; su -c 'virsh edit $vmname'
    (stick that string somewhere in the \&lt;devices\&gt; block, remove any other \&lt;graphics\&gt; devices)
    \&lt;/pre\&gt;

    \&#42; [[SELinux/FAQ\&#35;How_do_I_enable_or_disable_SELinux_.3F|Set selinux to permissive]]. For more info, see [https://bugzilla.redhat.com/show_bug.cgi?id=609279 bug 609276]

    \&#42; Give VM user access to your $XAUTHORITY file. The default VM user in Fedora 12+ is 'qemu', so you can provide read access with \&lt;pre\&gt;setfacl -m u:qemu:r $XAUTHORITY\&lt;/pre\&gt; If you get an 'operation not supported' error, you can optionally provide less discerning read access with \&lt;pre\&gt;chmod +r $XAUTHORITY\&lt;/pre\&gt; Beware, this probably has security implications. If that does not work, you can optionally change the VM user to either root (behavior of older Fedora versions), or [[\&#35;Changing_the_QEMU.2FKVM_process_user|to your own regular user]]

    [discrete]
    === Errors using \&lt;interface type='ethernet'/\&gt;

    Libvirt's default behavior of dropping QEMU/KVM process capabilities prevents \&lt;interface type='ethernet'/\&gt; from working correctly. You can try:

    \&#42; Have libvirt [[\&#35;Changing_QEMU.2FKVM_process_capabilities|not drop QEMU/KVM process capabilities]]

    If that isn't sufficient, you may want to try the following:

    \&#42; [[SELinux/FAQ\&#35;How_do_I_enable_or_disable_SELinux_.3F|Set selinux to permissive]]
    \&#42; Have libvirt [[\&#35;Changing_the_QEMU.2FKVM_process_user|run QEMU/KVM as root]]

    [discrete]
    === PCI device assignment

    Libvirt's default behavior of dropping QEMU/KVM process capabilities prevents PCI device assignment from working correctly. See [https://bugzilla.redhat.com/show_bug.cgi?id=573850 bug 573850] for more info. I only managed to get this working with the following steps:

    \&#42; Have libvirt [[\&#35;Changing_QEMU.2FKVM_process_capabilities|not drop QEMU/KVM process capabilities]]
    \&#42; [[SELinux/FAQ\&#35;How_do_I_enable_or_disable_SELinux_.3F|Set selinux to permissive]]
    \&#42; Have libvirt [[\&#35;Changing_the_QEMU.2FKVM_process_user|run QEMU/KVM as root]]



    = How to Publish your Software on Copr, Fedora's User Repository
    Christopher Engelhard; Jean-Baptiste Holcroft; Otto Urpelainen
    // :page-aliases:



    [abstract]
    This is a short tutorial on how to create and maintain a Copr repository for your software in an automated fashion. It assumes some basic familiarity with Git \&amp; how to create a RPM package.

    In this guide, we'll

    - create an RPM package for a program

    - create a Copr repository and publish the program to it

    - set up automatic management of program version, package release and package changelog

    - set up automatic building of new package versions

    The aim is to let you keep your software up-to-date in Copr without ever having to interact with anything other than your software's git repository.

    TIP: You can set up similar automation when packaging someone else's program, i.e. building from a downloaded source tarball. The needed modifications are described xref:\&#35;_packaging_from_source_tarballs[at the end of the tutorial].

    == Prerequisites
    The following is needed:

    . Our program's source in a _publicly available git repository_ somewhere. This tutorial uses a simple example program - hellocopr - to demonstrate the process. The program and all files referenced in this guide can be found in the link:https://pagure.io/copr-tito-quickdoc[project's git repository]. It's a very simple (\&amp; pointless) python program with a setuptools installer:
    +
    [source,]
    ----
    user@host ~/copr-tito-quickdoc % ls
    doc  LICENSE  README.md  requirements.txt  setup.py  src

    user@host ~/copr-tito-quickdoc % ls src/hellocopr
    colors.py  hellocopr.py  __init__.py
    ----

    . A _Fedora (FAS) account_ in order to be able to create repositories on Copr. This tutorial's demo repository can be found link:https://copr.fedorainfracloud.org/coprs/lcts/hellocopr/[here].

    . The utility _\&#96;tito\&#96;_ installed on your system. link:https://github.com/rpm-software-management/tito[Tito] is capable of a lot of advanced automation for package creation, most of which we won't need here. Check out its documentation to learn more.

    . A _specfile_ for our program. For more information on how to create one,
    refer to xref:package-maintainers::Packaging_Tutorial_GNU_Hello.adoc[Packaging Tutorial: GNU Hello]
    or adapt this tutorial's link:https://pagure.io/copr-tito-quickdoc/blob/master/f/doc/hellocopr.spec.annotated[annotated example specfile].

    TIP: You can follow along with this tutorial by cloning or forking the repository and checking out the \&#96;initial\&#96; tag. This will put the repository in the state just before the next step. The repo's commit history matches the steps followed in this tutorial.

    == Step 1: Creating the package using tito

    Copy link:https://pagure.io/copr-tito-quickdoc/c/00963ac9339a13eefd2ab1ca42b1f72af12d3cac?branch=master[the spec file] into the project's base directory. A few changes should be made before proceeding:

    . The values of \&#96;Version:\&#96; and \&#96;Release:\&#96; do not matter, since these will be managed by tito. It makes sense to set them to \&#96;Version: 0.0.0\&#96; and \&#96;Release: 0%\{?dist}\&#96; to mark that this package hasn't been built yet.

    . tito will also handle the creation of the source tarball from the git repository, so change the _\&#96;Source0:\&#96; URL_ to the filename \&#96;%\{name}-%\{version}.tar.gz\&#96; \&amp; add a comment to tell users how to get the tarball

    . The changelog can be left empty.
    +
    \&#96;\&#96;\&#96;
    user@host ~/copr-tito-quickdoc % cat hellocopr.spec
    \&#8230;
    Version: 0.0.0
    Release: 0%\{?dist}
    \&#8230;
    \&#35; Sources can be obtained by
    \&#35; git clone https://pagure.io/copr-tito-quickdoc
    \&#35; cd copr-tito-quickdoc
    \&#35; tito build --tgz
    Source0: %\{name}-%\{version}.tar.gz
    \&#8230;
    %changelog
    \&#96;\&#96;\&#96;

    Commit the changes.

    Next, we initialize the project for use with tito.

    \&#96;\&#96;\&#96;
    user@host ~/copr-tito-quickdoc % tito init
    Creating tito metadata in: ~/copr-tito-quickdoc/.tito
    - created ~/copr-tito-quickdoc/.tito
    - wrote tito.props
    - created ~/copr-tito-quickdoc/.tito/packages
    - wrote ~/copr-tito-quickdoc/.tito/packages/.readme
    - committed to git
    Done!
    \&#96;\&#96;\&#96;

    This creates link:https://pagure.io/copr-tito-quickdoc/c/7a6919d3dd56943bb988a755f8233157965aa9bb?branch=master[a subdirectory \&#96;.tito\&#96; with some default configuration], which can be left unchanged for now.

    We can now do a test build of the package using _\&#96;tito build\&#96;_. Usually, tito will build from a tag, which we haven't created yet. However, using the \&#96;--test\&#96; flag, we can build from the most recent commit instead, which will be written to \&#96;/tmp/tito\&#96;:

    [source,]
    ----
    user@host ~/copr-tito-quickdoc % tito build --rpm --test
    Creating output directory: /tmp/tito
    WARNING: unable to lookup latest package tag, building untagged test project
    WARNING: .tito/packages/hellocopr doesn't exist in git, using current directory
    Building package [hellocopr-0.0.0-0]
    Wrote: /tmp/tito/hellocopr-git-11.7a6919d.tar.gz
    \&#8230;

    Successfully built: /tmp/tito/hellocopr-0.0.0-0.git.11.7a6919d.fc32.src.rpm
    - /tmp/tito/noarch/hellocopr-0.0.0-0.git.11.7a6919d.fc32.noarch.rpm
    ----

    Once we've fixed any issues with the package that might crop up, we can let _tito_ create a package release using \&#96;tito tag\&#96;. Since we haven't set a proper version yet, we need to pass it to tito for the first tag:

    [source,]
    ----
    user@host ~/copr-tito-quickdoc % tito tag --use-version 1.0.0
    ----

    This will open the editor \&amp; display a pre-formatted changelog entry build up from all commits since the last release, which we can edit as needed. Since there have been none so far, the entry will just contain '- new package built with tito'. Save the file, link:https://pagure.io/copr-tito-quickdoc/c/f44e81d695df669bcdb7237612baf41b80da98e0?branch=master[and tito will]

    . set the Version in the specfile to 1.0.0

    . set the Release in the specfile to 1

    . append the changelog entry to the specfile's \&#96;%changelog\&#96; section

    . commit the result and tag it with \&#96;\&lt;name\&gt;-\&lt;version\&gt;-\&lt;release\&gt;\&#96;, i.e. \&#96;hellocopr-1.0.0-1\&#96;
    +
    [source,]
    ----
    user@host ~/copr-tito-quickdoc % tito tag --use-version 1.0.0
    Creating output directory: /tmp/tito
    Tagging new version of hellocopr: untagged -\&gt; 1.0.0-1
    Created tag: hellocopr-1.0.0-1
    View: git show HEAD
    Undo: tito tag -u
    Push: git push --follow-tags origin
    ----

    Push to the commits \&amp; tags to the remote using \&#96;git push --follow-tags\&#96;, and we're ready to release the package on Copr.


    == Step 2: Publishing the package in a Copr repository

    . Go to https://copr.fedorainfracloud.org/ and log in. Once done, click on _New Project_ to start creating a repository for our program. On the following input mask,

    .. Under _1. Project information_ -\&gt; _Project name_ set the name to what you want your repo to be called - since this will only contain a single package, it makes sense to use projectname = packagename, i.e. _hellocopr_. This is the only settings that cannot be changed later.

    .. Under _2. Build options_ tick all distributions you want to create repositories for - usually all Fedora versions \&amp; maybe EPEL versions as well

    .. Under _4. Other Options_ make sure that _Follow Fedora branching_ is ticked, this will ensure that your repository will automatically update for new Fedora release.

    . Go to _Packages_ -\&gt; _New Package_

    .. Under _1. Provide the source_, set the package name \&amp; the URL of your git repository

    .. Under _2. How to build SRPM from the source_ select _tito_

    .. Under _3. Generic package setup_ tick the box for _Auto-rebuild_

    . Your package will appear in the list of packages. Hit _Rebuild_ to trigger a build. The following page lets you change any build options if necessary, we'll just use the defaults, i.e. the options we set in the previous step. Hit _Submit_ and Copr will build the package from the tito tag we created in Step 1.

    Once the build has finished, you can test installing the package from Copr by activating your repository.
    [source,]
    ----
    user@host ~/copr-tito-quickdoc % sudo dnf copr enable \&lt;username\&gt;/hellocopr

    user@host ~/copr-tito-quickdoc % sudo dnf install hellocopr
    ----

    == Step 3: Automate package (re)-builds

    Next, we want to set up Copr to automatically build a new package version whenever we create one, so that we no longer need to log in and trigger one manually. To achieve this, we simply need to trigger a build whenever we push a new tag to the repository.

    This requires some configuration both of your Git repository and of the Copr project.

    Configuration can be found under _Settings_ -\&gt; _Integrations_, the page also explains the steps to configure your git repository for all common Git forges (Pagure, Github, Gitlab \&amp; Bitbucket).

    Now, to test this, let's make some changes to our program that will come in handy for the final layer of automation and create a new release for our software.

    Currently, the example program has its version hardcoded at multiple places. link:https://pagure.io/copr-tito-quickdoc/c/61abf1cdf622d8c9fb4f03eb6b06c4ddc1677362?branch=master[Let's change this] so that the version string is sourced from a single file. Which file this is doesn't matter, but ideally the version variable should be the only thing in it that is likely to change. In this case, we use the previously empty \&#96;src/hellocopr/pass:[__]initpass:[__].py\&#96;. We name this new version '1.0.1'.

    Commit the changes, and create a new release with tito

    [source,]
    ----
    user@host ~/copr-tito-quickdoc % tito tag
    Creating output directory: /tmp/tito
    Tagging new version of hellocopr: 1.0.0-1 -\&gt; 1.0.1-1
    Created tag: hellocopr-1.0.1-1
    View: git show HEAD
    Undo: tito tag -u
    Push: git push --follow-tags origin
    ----

    Note that by omitting the \&#96;--use-version\&#96; option, tito now updates the version automatically. It does so by

    . Increasing the Version's final digit by 1 - \&#96;1.0.0\&#96; -\&gt; \&#96;1.0.1\&#96;
    . Resetting the Release to 1 if it isn't already.

    If you want to bump to a different version, say \&#96;1.1.0\&#96;, you can do so again by passing \&#96;--use-version\&#96;.

    Push the resulting commit \&amp; tag, and if you now check your projects page on Copr, you'll see that a new build of \&#96;hellocopr-1.0.1-1\&#96; has been triggered by our pushing a tag.

    == Step 4: Let tito manage the program version

    If you check the git log, you'll find that I actually forgot to update hellocopr's version variable to 1.0.1. We don't want that to happen again. Luckily, since we single-source our version, we can let tito automatically generate this file from a template.

    First, copy the version source file \&#96;src/hellocopr/pass:[__]initpass:[__].py\&#96; to \&#96;.tito/templates/pass:[__]initpass:[__].py.template\&#96;. Then, open the template file and replace the version string with \&#96;$version\&#96;. It also makes sense to add a note that the file is managed by tito and should not be edited manually.
    [source,]
    ----
    user@host ~/copr-tito-quickdoc % cat .tito/templates/__init__.py.template
    \&#8230;
    \&#35; This file is automatically created from a template by tito. Do not edit it manually.

    __version__ = '$version'
    ----

    Next, add the following to \&#96;.tito/tito.props\&#96;
    [source,]
    ----
    [version_template]
    destination_file = src/hellocopr/__init__.py
    template_file = .tito/templates/__init__.py.template
    ----

    https://pagure.io/copr-tito-quickdoc/c/28600f6e41d5a4b60f2e47cf077f2fe2d9224e1d?branch=master[Commit the changes]. Now, when we tag a new release, tito will take the template, replace \&#96;$version\&#96; with whatever version was tagged, and copy the resulting file to \&#96;src/hellocopr/pass:[__]initpass:[__].py\&#96; before updating the spec file and committing the changes.

    We can test this by tagging a new release:
    [source,]
    ----
    user@host ~/copr-tito-quickdoc % % tito tag
    Creating output directory: /tmp/tito
    Tagging new version of hellocopr: 1.0.1-1 -\&gt; 1.0.2-1
    Created tag: hellocopr-1.0.2-1
    View: git show HEAD
    Undo: tito tag -u
    Push: git push --follow-tags origin

    user@host ~/copr-tito-quickdoc % cat src/hellocopr/__init__.py
    \&#8230;
    \&#35; This file is automatically created from a template by tito. Do not edit it manually.

    __version__ = '1.0.2'
    ----

    If you again push the tag to the remote repo, Copr will again automatically trigger a rebuild.

    == Release procedure in brief
    From now on, updating your software in the Copr repository is as simple as

    . Commit all changes for your new version.
    . Perform a test build using \&#96;tito build --test\&#96;
    . Tag the release with \&#96;tito tag\&#96; (add \&#96;--use-version\&#96; if necessary)
    . Push the tag to your git repo using \&#96;git push --follow-tags\&#96;

    and Copr will take care of the rest.

    == Packaging from source tarballs

    You can use a similar process to manage someone elses software on Copr, i.e. build from a tarball downloaded from upstream.

    To do so, the following changes need to be made to the procedure described above:

    . Instead of the unpacked sources, download \&amp; commit the source tarball you want to package to your repository
    . Instead of modifying the source directly, add any changes you need to make in the form of patch files. List these as \&#96;PatchX:\&#96; in the spec file
    . Also in the spec file, set the \&#96;Version:\&#96; back to whatever version the program is at and \&#96;Source0:\&#96; back to the tarball URL. You can use macros like \&#96;%\{version}\&#96; for the latter to automatically follow version changes.
    . Modify tito's \&#96;.tito/tito.props\&#96; to, one, not try to build a source tarball and two, bump the \&#96;Release:\&#96; instead of the \&#96;Version:\&#96; when tagging
    +
    [source,]
    ----
    [buildconfig]
    builder = tito.builder.NoTgzBuilder
    tagger = tito.tagger.ReleaseTagger
    ----

    . Don't do any tito templating

    The rest of the procedure stays the same. If you make changes to the package without changing the source, you can just tag a new release with tito. If you do update the source tarball, you need to update the \&#96;Version:\&#96; field and reset \&#96;Release:\&#96; to \&#96;0%\{?dist}\&#96; before tagging.

    TIP: The tarball-adapted version of the project can be found in the \&#96;https://pagure.io/copr-tito-quickdoc/tree/foreign-sources[foreign-sources]\&#96; branch of the git repo.



    \&#42; Databases
    = PostgreSQL
    Jiyoung Joung; niko d; Héctor H. Louzao P
    //:imagesdir: ./images

    [NOTE]
    ====
    Users of Fedora Server Edition find additional information in xref:fedora-server::services/postgresql-setup.adoc[Setting up PostgreSQL Database Server]
    ====
    [[installation]]
    == Installation

    The installation and initialization of the postgresql server is a little
    bit different in comparison to other packages and other Linux distros.
    This document aims to summarize basic installation steps relevant to
    recent Fedora Linux releases.

    \&#8230;.
    sudo dnf install postgresql-server postgresql-contrib
    \&#8230;.

    The postgresql server is not running and disabled by default. To set it to start at boot, run:

    \&#8230;.
    sudo systemctl enable postgresql
    \&#8230;.

    The database needs to be populated with initial data after installation. The database initialization could be done using following command. It
    creates the configuration files postgresql.conf and pg_hba.conf

    \&#8230;.
    sudo postgresql-setup --initdb --unit postgresql
    \&#8230;.

    To start the postgresql server manually, run

    \&#8230;.
    sudo systemctl start postgresql
    \&#8230;.


    [[user-creation-and-database-creation]]
    == User Creation and Database Creation

    Now you need to create a user and database for the user. This needs to be run from a \&#96;postgres\&#96; user account on your system.

    \&#8230;.
    sudo -u postgres psql
    \&#8230;.

    From here you can create a postgres user and database. Here, we will assume your computer's user account is called \&#96;lenny\&#96;. Note: you can also run this from the shell as well with \&#96;createuser lenny\&#96; and \&#96;createdb --owner=lenny carl\&#96;.

    \&#8230;.
    postgres=\&#35; CREATE USER lenny WITH PASSWORD 'leonard';
    postgres=\&#35; CREATE DATABASE my_project OWNER lenny;
    \&#8230;.

    It might be good idea to add password for the \&#96;postgres\&#96; user while you're at it:

    \&#8230;.
    postgres=\&#35; \password postgres
    \&#8230;.

    Press Ctrl + D or \&#96;\q\&#96; to leave the psql session running as user \&#96;postgres\&#96;. Now you can access your new database from your user account (\&#96;lenny\&#96;) and start using it.

    \&#8230;.
    psql my_project
    \&#8230;.


    [[initial-configuration]]
    == Initial Configuration

    The postgresql server is using two main configuration files

    \&#42; /var/lib/pgsql/data/postgresql.conf
    \&#42; /var/lib/pgsql/data/pg_hba.conf


    If you’re getting ident errors from your app you’ll probably need to perform the accepted solution described at https://serverfault.com/questions/406606/postgres-error-message-fatal-ident-authentication-failed-for-user?newreg=a4fdc3e21349449985cc65b82399c5b4
    \&#8230;.
    sudo gedit /var/lib/pgsql/data/pg_hba.conf
    \&#8230;.

    and edit \&#96;host all all 127.0.0.1/32 ident\&#96; to \&#96;host all all 127.0.0.1/32 md5\&#96; and \&#96;host all all ::1/128 ident\&#96; to \&#96;host all all ::1/128 md5\&#96;. Once you've made this change, be sure to restart the postgresql service for the changes to take affect.

    \&#8230;.
    sudo systemctl restart postgresql
    \&#8230;.

    These changes should allow most applications to connect with username/password.


    [[upgrade]]
    == Upgrade

    As you can see from the error message in my example, it is not a fresh
    installation, but an upgrade.

    \&#8230;.
    Nov 14 11:45:56 mlich-lenovo.usersys.redhat.com postgresql-check-db-dir[2108]: An old version of the database format was found.
    Nov 14 11:45:56 mlich-lenovo.usersys.redhat.com postgresql-check-db-dir[2108]: Use 'postgresql-setup upgrade' to upgrade to version 9.3.
    \&#8230;.

    With version 9 you can use the upgrade tool. It is packaged as \&#96;postgresql-upgrade\&#96;:

    \&#8230;.
    postgresql-setup upgrade

    Redirecting to /bin/systemctl stop  postgresql.service
    Upgrading database: OK

    The configuration files was replaced by default configuration.
    The previous configuration and data are stored in folder /var/lib/pgsql/data-old.

    See /var/lib/pgsql/pgupgrade.log for details.
    \&#8230;.

    The data are located at

    \&#42; /var/lib/pgsql/data
    \&#42; /var/lib/pgsql/data-old

    The upgrade itself will backup your existing data and migrate your
    database. Don't forget to migrate your configuration (with meld, for
    example: \&#96;meld /var/lib/pgsql/data{,-old}/postgresql.conf\&#96;).

    You may need to switch postgresql to trust mode before updating. This should be fixed already.

    You can also upgrade by dumping your database and loading it again. For
    more information, see the link:\&#35;link-upgrade[official documentation].

    [[skipped-release]]
    === Skipped major release

    In Fedora 43 the Postgres packages went from 16 to 18. Database upgrades cannot skip a major release and the above procedure will not work.
    Unless you have already upgraded to Postgres 17 on Fedora 42, you will have to do the upgrade from 16 to 18 in 2 steps on Fedora 43.

    First you have to uninstall Postgres 18 and install Postgres 17. You can verify which packages are installed with \&#96;rpm -qa |grep ^postgres\&#96;
    Before you install Postgres 17, please backup your data directory. Even though a backup is part of the upgrade procedure, it is better to be safe than sorry.
    After installing the Postgres 17 packages, you can use the above upgrade procedure to do the actual upgrade from 16 to 17.
    Then you have to uninstall Postgres 17 and install Postgres 18 again.
    Please run above upgrade procedure one more time and you are good to go.

    During this 2 step procedure you might encounter a few obstacles, which are explained here:

    In case you see the error \&#96;old cluster does not use data checksums but the new one does\&#96; you can either choose to create the checksums or upgrade with checksums disabled.
    To create the checksums, drop into the shell of the \&#96;postgres\&#96; user and run the following command: \&#96;pg_checksums -e -D \&lt;data-dir\&gt;\&#96;.
    However, when you see this error, you have already updated the packages to a newer release while the database is still on the previous one.
    Thus it might be easier to upgrade with \&#96;PGSETUP_INITDB_OPTIONS='–no-data-checksums' postgresql-upgrade \&lt;data-dir\&gt;\&#96; and create the checksums afterwards.
    Unless you changed the Postgres data directory, \&#96;\&lt;data-dir\&gt;\&#96; is \&#96;/var/lib/pgsql/data\&#96;.

    Don't forget to adjust and consolidate your config files (\&#96;\&#42;.conf\&#96;) from the old and new data directories as well as to update the collation for all databases.

    Update the collation (as postgres user): \&#96;ALTER DATABASE \&lt;dbname\&gt; REFRESH COLLATION VERSION; \c \&lt;dbname\&gt;; REINDEX DATABASE;\&#96;

    [[firewall]]
    == Firewall

    PostgreSQL operates on port 5432 (or whatever else you set in your
    \&#96;postgresql.conf\&#96;). In firewalld you can open it like this:

    \&#8230;.
    \&#35; make it last after reboot
    firewall-cmd --permanent --add-port=5432/tcp
    \&#35; change runtime configuration
    firewall-cmd --add-port=5432/tcp
    \&#8230;.

    In the case of iptables:

    \&#8230;.
    iptables -A INPUT -p tcp --dport 5432 -m state --state NEW,ESTABLISHED -j ACCEPT
    \&#8230;.

    Bear in mind that you probably don't want to open your database server
    to the whole world.

    [[selinux]]
    == SELinux

    If you have SELinux enforced, you may run into trouble when trying to do
    some non-standard configuration. For example, if you would like to change
    a location of your database, you have to add new context mapping for the
    new location:

    \&#8230;.
    semanage fcontext -a -t postgresql_db_t '/my/new/location(/.\&#42;)?'
    \&#8230;.

    If the default port doesn't work for you, you may need to map postgre's port type to your desired port:

    \&#8230;.
    semanage port -a -t postgresql_port_t -p tcp 5433
    \&#8230;.

    If you install a webapp that wants to communicate with PostgreSQL via
    TCP/IP, you will have to tell SELinux to allow this on the webserver
    host:

    \&#8230;.
    setsebool -P httpd_can_network_connect_db on
    \&#8230;.

    [[configuration]]
    == Configuration

    As mentioned above, the postgresql server is using two main configuration files

    \&#42; /var/lib/pgsql/data/postgresql.conf
    \&#42; /var/lib/pgsql/data/pg_hba.conf


    [[systemd]]
    === systemd

    Some configuration parameters are passed to daemon via command line
    options. This behaviour may override settings in \&#96;postgresql.conf\&#96;. For
    example, if you want to change the server's port number to 5433, create
    a file named \&#96;/etc/systemd/system/postgresql.service\&#96; containing:

    \&#8230;.
    .include /lib/systemd/system/postgresql.service
    [Service]
    Environment=PGPORT=5433
    \&#8230;.

    Note: changing PGPORT or PGDATA will typically require adjusting SELinux
    configuration as well; see section selinux.

    Please follow the systemd documentation
    http://fedoraproject.org/wiki/systemd\&#35;How_do_I_customize_a_unit_file.2F_add_a_custom_unit_file.3F[2]
    for more details.

    [[postgresql.conf]]
    === postgresql.conf

    If you want postgres to accept network connections, you should change

    \&#8230;.
    listen_addresses = 'localhost'
    \&#8230;.

    to

    \&#8230;.
    listen_addresses = '\&#42;'
    \&#8230;.

    [[pg_hba.conf]]
    === pg_hba.conf

    Once your database is set up, you need to configure access to your
    database server. This may be done by editing file
    \&#96;/var/lib/pgsql/data/pg_hba.conf\&#96;. There are rules like this in the
    file:

    \&#8230;.
    \&#35; TYPE    DATABASE        USER            ADDRESS                 METHOD
    host    all             all             127.0.0.1/32            md5
    host    all             all             ::1/128                 md5
    local   all             postgres                                peer
    \&#8230;.

    First field stands for connection type. It can have these values:

    \&#42; \&#42;local\&#42; — Unix-domain socket
    \&#42; \&#42;host\&#42; — plain or SSL-encrypted TCP/IP socket
    \&#42; \&#42;hostssl\&#42; — an SSL-encrypted TCP/IP socket
    \&#42; \&#42;hostnossl\&#42; — plain TCP/IP socket

    Last column specifies which authentication method will be used.

    \&#42; \&#42;md5\&#42; — client has to supply password processed with MD5 algorithm
    \&#42; \&#42;ident\&#42; — obtain user name of connecting client from operating system
    and consult it with specified map
    \&#42; \&#42;trust\&#42; — anyone who is able to connect to PostgreSQL server may act
    as any user without supplying password
    \&#42; \&#42;peer\&#42; — obtains user's name from operating system and checks if it
    matches database user name

    When the database server is authenticating the client, it seeks for a record with a matching connection type, client address, requested database, and user name. As soon as it finds these credentials, it performs the authentication. If the authentication fails, no more subsequent records are taken into account. If no record matches, the client's access is denied.

    The default settings are usually restricted to localhost.

    When you install your database server and at first you try to 'make it
    work', you should turn off firewall, SELinux and make the \&#96;postgres\&#96;
    authentication permissive. _Bear in mind this will greatly expose your
    server, so do it [.underline]\&#35;only\&#35; on a trusted network — preferably with no network at all_:

    \&#8230;.
    host    all             all             127.0.0.1/32            trust
    \&#8230;.

    As soon as you are able to connect, turn on the security systems one by
    one while verifying the connection can be established.

    For more information see official documentation for
    https://www.postgresql.org/docs/current/auth-pg-hba-conf.html[pg_hba.conf file].

    [[optimization]]
    == Optimization

    The default configuration of postgres is severely undertuned. It can handle simple applications without consistent database access, but if you require higher performance, you should re-configure your instance. All the magic is happening in \&#96;/var/lib/pgsql/data/postgresql.conf\\&#96;\&#96;. Also, the logging mechanism is not configured very intuitively.

    [[performance]]
    === Performance

    The number of clients which may be connected to PostgreSQL at the same time:

    \&#8230;.
    max_connections = \&lt;number\&gt;
    \&#8230;.

    \&#96;shared_buffers\&#96; is the entry point. This is telling PostgreSQL how much
    memory is dedicated for caching. Setting this to 25% of total memory of
    your system is a good start. If it doesn't work for you, try to go for
    something between 15% - 40% of total memory.

    \&#8230;.
    shared_buffers = \&lt;memory unit\&gt;
    \&#8230;.

    This value is used by the query planner to know how much memory is available in the system. The query planner uses this information to figure out whether the plan fits into memory or not. Setting this to 50% of total memory is a common practice.

    \&#8230;.
    effective_cache_size = \&lt;memory unit\&gt;
    \&#8230;.

    When PostgreSQL performs sorting operations, it plans its strategy
    whether to sort the query on disk or in memory. Bear in mind that this
    memory is available for every sorting instance. In case of multiple
    users submitting queries to your database server, this can ramp up
    pretty high. Therefore this is tightly bound to \&#96;max_connections\&#96;.

    \&#8230;.
    work_mem = \&lt;memory unit\&gt;
    \&#8230;.

    For more information about this topic I advise you to read the
    link:\&#35;link-tuning[official documentation] about tuning PostgreSQL.

    [[logging]]
    === Logging

    By default, logs are rotated every week and you might not find much
    information in there. One could miss a log level, date, time, etc. Also,
    for simple web applications, some prefer to increase verbosity.

    \&#8230;.
    log_destination = 'stderr'
    \&#8230;.

    This is just fine. If you would like syslog to take care of your logs,
    change \&#96;'stderr'\&#96; to \&#96;'syslog'\&#96;, or even \&#96;'syslog,stderr'\&#96;. If you go for
    syslog, don't forget to configure syslog itself too; for more info, see
    link:\&#35;link-logging[official documentation].

    \&#8230;.
    logging_collector = on
    \&#8230;.

    In case of logging to \&#96;stderr\&#96;, \&#96;postgres\&#96; will grab all the logs if you
    enable the \&#96;logging_collector\&#96; option.

    This is default option:

    \&#8230;.
    log_filename = 'postgresql-%a.log'
    \&#8230;.

    A preferred method could be to name log files by date when they were
    created:

    \&#8230;.
    log_filename = 'postgresql-%G-%m.log
    \&#8230;.

    Rotation. This really depends on the app itself. In the case of a simple app with little data in the database, all the logs may be kept persistently on disk without rotation.

    \&#8230;.
    log_truncate_on_rotation = off
    log_rotation_age = 31d
    \&#8230;.

    Increase number of entries in log:

    \&#8230;.
    client_min_messages = notice      \&#35; default notice
    log_min_messages = info           \&#35; default warning
    log_min_error_statement = notice  \&#35; default error
    \&#8230;.

    If you would like to log slow queries, feel free to use this option:

    \&#8230;.
    log_min_duration_statement = 1000  \&#35; in ms
    \&#8230;.

    The default log entry doesn't contain much info:

    \&#8230;.
    FATAL:  Ident authentication failed for user 'test'
    DETAIL:  Connection matched pg_hba.conf line 84: 'host    all             all             ::1/128                 ident'
    \&#8230;.

    Let's improve it to:

    \&#8230;.
    2013-12-30 17:51:36 CET testx@::1(50867):postgres [11213] FATAL:  password authentication failed for user 'testx'
    2013-12-30 17:51:36 CET testx@::1(50867):postgres [11213] DETAIL:  Connection matched pg_hba.conf line 84: 'host   all             all             ::1/128                 md5 '
    \&#8230;.

    You just have to alter the option \&#96;log_line_prefix\&#96;.

    \&#8230;.
    \&#35; %t -- timestamp
    \&#35; %u -- user
    \&#35; %r -- client's host
    \&#35; %d -- database
    \&#35; %p -- PID
    log_line_prefix = '%t %u@%r:%d [%p] '
    \&#8230;.

    If you are running only a single database with a single user connecting, it makes more sense to simplify the prefix to

    \&#8230;.
    log_line_prefix = '%t [%p] '
    \&#8230;.

    [[final-recipe]]
    ==== Final recipe

    \&#8230;.
    log_destination = 'stderr'
    logging_collector = on
    log_filename = 'postgresql-%G-%m.log'
    log_truncate_on_rotation = off
    log_rotation_age = 31d
    client_min_messages = notice
    log_min_messages = info
    log_min_error_statement = notice
    log_line_prefix = '%t %u@%r:%d [%p] '
    \&#8230;.

    [[reference]]
    == Reference

    link:PostgreSQL/README.rpm-dist[Full RPM packaging documentation]

    https://wiki.postgresql.org/wiki/Tuning_Your_PostgreSQL_Server[Tuning
    performance]

    https://www.postgresql.org/docs/18/runtime-config-logging.html[Logging
    configuration]

    https://www.postgresql.org/docs/18/upgrading.html[Upgrading
    PostgreSQL]

    https://www.postgresql.org/docs/18/auth-pg-hba-conf.html[pg_hba.conf
    file]

    See a typo, something missing or out of date, or anything else which can be
    improved? Edit this document at https://pagure.io/fedora-docs/quick-docs.


    = Installing MySQL/MariaDB
    Alessio ; Héctor Louzao ; Ankur Sinha
    //:page-aliases:


    [abstract]
    MySQL is a popular RDBMS (Relational Database Management System). MariaDB was born as a fork of MySQL.
    Nowadays the two products are a little bit different. Migrating data from one system to the other could not be a trivial task.


    MariaDB is fully GPLv2 licensed while MySQL has two licensing options, GPLv2 (for the Community edition) and Enterprise.

    In the Fedora repositories you can find:

    \&#42; MariaDB 10.3 (as a regular package or as a module)
    \&#42; MariaDB 10.4 (as a module)
    \&#42; MySQL 8.0 community edition (as a regular package or as a module)

    NOTE: MariaDB and MySQL packages conflict because they provide similar files. So, you can only install one of them, either MariaDB or MySQL, but not both.

    In addition you can also install MySQL community edition (8.0 or 5.7) from the repository maintained by Oracle/MySQL itself.



    //include::{partialsdir}/proc_installing-mysql-from-oracle.adoc[leveloffset=+1]
    //[id='install-from-oracle-mysql']
    == Install from Oracle MySQL


    === Adding the MySQL repository to Fedora

    Please download the release package provided by Oracle from: https://dev.mysql.com/downloads/repo/yum/
    Once downloaded, please install it using dnf:

    ----
    sudo dnf install \&lt;path to downloaded rpm\&gt;
    ----

    Please note that this repository is provided by Oracle
    so any issues/bugs encountered will need to be reported to them
    via their communication channels: https://www.mysql.com/about/faq/

    === Installing MySQL on Fedora

    ----
    sudo dnf install mysql-server
    ----

    === Start MySQL Service and Enable at login:

    ----
    sudo systemctl start mysqld
    sudo systemctl enable mysqld
    ----

    find Default Password,  For security reasons, MySQL generates a temporary root key. Please note that MySQL has even stricter security policies than MariaDB.

    ----
    sudo grep 'temporary password' /var/log/mysqld.log
    ----

    === Configuring MySQL before the first use

    ----
    sudo mysql_secure_installation
    ----

    Then, answer the security questions as you prefer. or just say \&#42;\&#42;yes\&#42;\&#42; to all of them.

    === Using MySQL

    ----
    sudo mysql -u root -p
    ----

    === Removing MySQL

    I suggest to remove in the following way, the most appropriate and safe way without removing many dependencies is:

    ----
    sudo rpm -e --nodeps mysql-community-libs mysql-community-common mysql-community-server
    ----



    //include::{partialsdir}/proc_installing-mysql-from-fedora-repo.adoc[leveloffset=+1]
    //[id='install-from-fedora-main-repo']
    == Install from Fedora Main Repo

    The community provide a MySQL package in the main repo.

    ----
    sudo dnf install {community-mysql-server|mariadb-server}
    ----

    === Configuring MySQL/MariaDB

    Enable the service at boot and start:

    ----
    sudo systemctl enable {mysqld|mariadb}
    sudo systemctl start  {mysqld|mariadb}
    ----

    === Configuring SQL before the first use

    ----
    sudo mysql_secure_installation
    ----

    Some questions will be asked: answer to them as you prefer; answering _yes_ to all of them is perfectly fine.

    === Using SQL

    ----
    sudo mysql -u root -p
    ----

    === Removing SQL

    I suggest to remove in the following way:

    ----
    sudo dnf remove {community-mysql-server|mariadb-server}
    ----




    //include::{partialsdir}/proc_installing-mysql-from-container.adoc[leveloffset=+1]
    //[id='install-from-container']
    == Install from Podman

    === Downloading a SQL Server Docker Image

    ----
    podman pull {mysql/mysql-server|mariadb/server}
    ----

    === See Logs

    ----
    podman logs {mysql|mariadb}
    ----

    === Starting a MySQL Server Instance

    The command's below contain the random password generated for the root user;

    ----
    podman logs mysql 2\&gt;\&amp;1 | grep GENERATED
    ----

    ----
    podman run -d --name=mysql -e MYSQL_ROOT_PASSWORD=mypassword mysql/mysql-server
    ----

    === Starting a MariaDB Server Instance

    ----
    podman run -d --name=mariadb -ed MYSQL_ROOT_PASSWORD=mypassword mariadb/server
    ----

    WARNING: Password blank default for MariaDB

    NOTE: The -d option used for _BOTH_ in the podman run command above makes the container run in the background. Use this command to monitor the output from the container:

    === Connecting to MySQL Server from within the Container

    ----
    podman exec -it mysql mysql -uroot -p
    ----

    you must reset the server root password by issuing this statement:

    ----
    mysql\&gt; ALTER USER 'root'@'localhost' IDENTIFIED BY 'password';
    ----

    === Connecting to MariaDB Server from within the Container

    ----
    podman exec -it mariadb bash
    ----

    === Resetting SQL_ROOT_PASSWORD

    you must reset the server root password by issuing this statement:

    ----
    mysql\&gt; ALTER USER 'root'@'localhost' IDENTIFIED BY 'password';
    ----

    === Stopping and Deleting a SQL Container

    ----
    podman {start|stop|restart} {mysql|mariadb}
    ----

    === Deleting a SQL Container

    ----
    podman rm {mysql|mariadb}
    ----

    WARNING: you can do the same with _docker_ just change _podman_ with _docker_.



    //include::{partialsdir}/proc_using-mysql-mariadb.adoc[leveloffset=+1]
    == Using the RDBMS

    Connect to the MySQL/MariaDB shell using the \&#96;mysql\&#96; command.

    For both of them, the command is \&#96;mysql\&#96;. The syntax an the options are generally the same.

    ----
    $ mysql -u root -p
    ----

    Once gained access to the shell you can get the running version of the software:

    ----
    mysql\&gt; SELECT version();
    ----

    You can create a database:

    ----
    mysql\&gt; create schema test;
    ----

    Create a user:

    ----
    mysql\&gt; GRANT ALL PRIVILEGES ON test.\&#42; TO 'my_user'@'localhost' IDENTIFIED BY 'PaSsWoRd';
    ----

    List the available databases:

    ----
    mysql\&gt; show schemas;
    ----

    === Files location

    The database disk storage is located in \&#96;/var/lib/mysql\&#96;.


    == How To Allow Remote Access MySQL/MariaDB/MYSQL Community

    === Add New Rule to Firewalld

    Open SQL port (3306) on FireWalld:

    ----
    sudo firewall-cmd --permanent --zone=public --add-service=mysql
    ----

    \&#35;\&#35;\&#35; OR \&#35;\&#35;\&#35;

    ----
    sudo firewall-cmd --permanent --zone=public --add-port=3306/tcp
    ----

    === Restart firewalld.service

    ----
    systemctl restart firewalld.service
    ----

    === Editing Conf. Files:

    Configuration files:

    \&#42; MySQL           -\&gt; \&#96;/etc/my.cnf/\&#96;
    \&#42; MySQL Community -\&gt; \&#96;/etc/my.cnf.d/community-mysql-server.cnf\&#96;
    \&#42; MariaDB         -\&gt; \&#96;/etc/my.conf\&#96;

    NOTE: you can ensure that with the following command \&#96;rpm -qc [package]\&#96;.

    Navigate to the line that begins with the bind-address directive. It will look like this:
    you could set this directive to a wildcard IP address, either \&#42;, ::, or 0.0.0.0:

    ----
    bind-address            = 0.0.0.0
    ----

    After changing this line, save and close the file and then restart the MySQL service:

    ----
    sudo systemctl restart {mysqld|mariadb}
    ----

    === Creating a USER

    ----
    CREATE USER 'your_username'@'host_ip_addr' IDENTIFIED BY 'your_password';
    ----

    NOTE: Replace your_username and your_password depending on what you want the username and password to be. Here, host_ip_addr is the hostname or IP address of the computer from where you want to connect to the MySQL/MariaDB server. You can also use % as host_ip_addr if you want to connect from any computer. It can also be something like 192.168.2.% if you want to connect from computers from the IP range 192.168.2.1 – 192.168.2.254.

    === Allow Access

    ----
    GRANT ALL PRIVILEGES ON \&#42;.\&#42; TO 'your_username'@'%';
    IDENTIFIED BY 'my-new-password' WITH GRANT OPTION;
    ----

    \&#35;\&#35;\&#35;\&#35; OR \&#35;\&#35;\&#35;\&#35;

    It is common for people to want to create a 'root' user that can connect from anywhere, so as an example, we'll do just that, but to improve on it we'll create
    a root user that can connect from anywhere on the local area network (LAN)

    ----
    GRANT ALL PRIVILEGES ON \&#42;.\&#42; TO 'root'@'192.168.100.%'
    IDENTIFIED BY 'my-new-password' WITH GRANT OPTION;
    ----

    ----
    FLUSH PRIVILEGES;
    ----

    === Connecting

    ----
    mysql -u [USER] -h [IP] -p
    ----



    //include::{partialsdir}/proc_troubleshooting-mysql.adoc[leveloffset=+1]
    //[id='how-to-troubleshoot-issues-in-sql']
    == How To Troubleshoot Issues in SQL

    Version:

    ----
    dnf list installed | grep -i -e maria -e mysql -e galera
    ----

    Check parameters in configuration file:

    \&#42; MySQL:

    ----
    mysqld --print-defaults
    ----

    \&#42; MariaDB/MySQL Community:

    ----
    /usr/libexec/mysqld --print-defaults
    ----

    WARNING: Compatibility between different version are not allowed Just install one of them.

    === How to Access SQL Error Logs

    Oftentimes, the root cause of slowdowns, crashes, or other unexpected behavior in SQL can
    In many cases, the error logs are most easily read with the less program, a command line u

    if SQL isn’t behaving as expected, you can obtain more information about the source of the

    \&#42; \&#42;\&#42;systemctl status mysqld.service\&#42;\&#42; doesn't start well, This information doesn’t explain
    well what is happening?, after this command you should type \&#96;journalctl -xe -u mariadb -u mysqld\&#96;.
    \&#42; Look at Log files, can be located in \&#96;/var/log/mysql/mysqld.log\&#96; for MySQL, and \&#96;/var/log/mariabd\&#96; for MariaDB.

    === How To Troubleshoot Socket Errors in SQL

    SQL manages connections to the database server through the use of a socket file, a special kind of file that facilitates communications between different processes. The MySQL server’s socket file is named mysqld.sock and on Ubuntu systems it’s usually stored in the /var/run/mysqld/ directory. This file is created by the MySQL service automatically.

    Sometimes, changes to your system or your SQL configuration can result in SQL being unable to read the socket file, preventing you from gaining access to your databases. The most common socket error looks like this:

    ----
    ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/var/run/mysqld/mysqld.sock' (2)
    ----

    There are a few reasons why this error may occur, and a few potential ways to resolve it.
    One common cause of this error is that the SQL service is stopped or did not start to begin with, meaning that it was unable to create the socket file in the first place. To find out if this is the reason you’re seeing this error, try starting the service with _systemctl_:

    ----
    sudo systemctl start {mysqld|mariadb}
    ----

    Then try accessing the MySQL prompt again. If you still receive the socket error, double check the location where your MySQL installation is looking for the socket file. This information can be found in the \&#96;mysqld.cnf\&#96; file:

    look for the socket parameter in the [mysqld] section of this file. It will look like this:

    ----
    [mysqld]
    user            = mysql
    pid-file        = /var/run/mysqld/mysqld.pid
    socket          = /var/run/mysqld/mysqld.sock
    port            = 3306
    ----

    Close this file, then ensure that the mysqld.sock file exists by running an ls command on the directory where SQL expects to find it:

    ----
    ls -a /var/run/mysqld/
    ----

    If the socket file exists, you will see it in this command’s output:

    ----
    mysqld.pid  mysqld.sock  mysqld.sock.lock
    ----

    if the file does not exist, the reason may be that MySQL is trying to create it, but does not have adequate permissions to do so. You can ensure that the correct permissions are in place by changing the directory’s ownership to the mysql user and group:

    ----
    sudo chown mysql:mysql /var/run/mysqld/
    ----

    Then ensure that the mysql user has the appropriate permissions over the directory. Setting these to 775 will work in most cases:

    ----
    sudo chmod -R 755 /var/run/mysqld/
    ----

    Finally, restart the MySQL service so it can attempt to create the socket file again:

    ----
    sudo systemctl restart {mysqld|mariadb}
    ----

    Then try accessing the MySQL prompt once again. If you still encounter the socket error, there’s likely a deeper issue with your MySQL instance, in which case you should review the error log to see if it can provide any clues.


    = How to Manage Various Database Server from GUI
    Héctor Louzao; Rafael Fontenelle

    // Optional  free form useful additional information as comment


    For database management, it is more user-friendly to use graphical tools:

    - MySQL/MariaDB:

    \&#42;\&#42; phpMyAdmin.noarch : A web interface for MySQL and MariaDB

    ----
    sudo dnf install phpMyAdmin
    ----

    - MySQL Specific:

    \&#42;\&#42; MySQL Workbench is a unified visual tool for database architects, developers, and DBAs.

    - Mixed:

    \&#42;\&#42; DBeaver Community   Universal Database Manager.

    ----
    flatpak install io.dbeaver.DBeaverCommunity
    ----

    \&#42;\&#42; PostgreSQL client for DBeaver Community

    ----
    flatpak install io.dbeaver.DBeaverCommunity.Client.pgsql
    ----

    \&#42;\&#42; MariaDB client for DBeaver Community

    ----
    flatpak install io.dbeaver.DBeaverCommunity.Client.mariadb
    ----

    - PostgreSQL:

    \&#42;\&#42; pgadmin3 Graphical client for PostgreSQL

    ----
    sudo dnf install pgadmin3
    ----

    \&#42;\&#42; phpPgAdmin - A web interface for PostgreSQL

    for Fedora \&lt;= 32

    ----
    sudo dnf install phpPgAdmin
    ----

    for Fedora \&gt;= 33


    == Installation

    The installation of the postgresql GUI web-server is a little bit different
    in comparison to older Fedora because the package is out of the repo.

    1. We assume you have php installed on your server and Working.

    2. Download the latest from GitHub repo:

    https://github.com/phppgadmin/phppgadmin/releases

    ----
    sudo tar xf phpPgAdmin-x.y.z.tar.bz2 -C /var/www/phpPgadmin
    ----

    In order to make phpPgAdmin navigable, we create a configuration file for the web service (Apache in this case):

    ----
    sudo nano /etc/httpd/conf.d/phpPgAdmin.conf
    ----

    The content will be an alias that will point to the installation path of
    the application:

    ----
    Alias /phppgadmin /var/www/phpPgAdmin
    ----

    Save the file and Reload the Web Service:

    ----
    sudo systemctl reload httpd
    ----

    phpPgAdmin requires the presence in Fedora 31 of certain PHP extensions,
    mainly the one that allows the connection with the database service, which
    we will install from the system repositories:

    ----
    sudo dnf install -y php-pgsql
    ----

    To access the web installer of phpPgAdmin in Fedora from a browser we will
    indicate the IP address or DNS name of the server followed by the alias we
    have defined and follow the steps requested.

    See a typo, something missing or out of date, or anything else which can be
    improved? Edit this document at https://pagure.io/fedora-docs/quick-docs.



    \&#42; Printing and scanning




    = CUPS – Useful Tricks
    Brandon Nielsen; Zdenek Dohnal


    == How to install a print queue

    The fact whether you have to install a printer or not depends on several things:

    \&#42; what is the device you want to install - a printer from remote CUPS server (called remote print queue) or a printer,
    \&#42; where is the device you want to install - connected by USB to your PC, in your local network, in a different network or installed on a remote server,
    \&#42; how old is the device you want to install:
    \&#42;\&#42; standalone printers - most SOHO (Small Office, Home Office) and office printers made after 2010 have at least one way of supporting driverless printing, older devices depend on drivers - classic or printer applications,
    \&#42;\&#42; remote print queues on a server - any OS with CUPS 2.2.8 and newer or OS where IPP Everywhere support was backported (f.e. RHEL 8) are capable of supporting IPP Everywhere, otherwise a combination of driver and raw queue is needed in client-server communication,
    \&#42; what is the purpose of the device where you install the printer - endpoint device, which is used by user as a desktop, or a server, which shares the installed printers further,
    \&#42; what are your personal preferences - using or not using IPP protocol, using or not using mDNS for autoinstallation if possible from network layout.

    So there are several user stories based on those dependencies, which are described further down.

    === Common user stories

    ==== I have a printer made after 2015, I'm at home and want to print from my PC

    \&#42; the most common setup on desktop
    \&#42; the printer is new enough to support driverless standards via USB and network, so driverless support doesn't depend on your connection
    \&#42; the PC is an endpoint device, I don't want to share the printer
    \&#42; I don't mind using mDNS and IPP, mDNS is enabled in my firewall, IPP and mDNS (or similar settings) are enabled on the printer, and mDNS resolution works (checked by pinging .local hostname)

    CUPS temporary queues for xref:_how_to_setup_cups_temporary_queues_with_usb_printer[USB] or xref:_how_to_setup_cups_temporary_queues_with_network_printer[network] are ideal for this use case.

    ==== I have an older printer, I'm at home and want to print from my PC

    \&#42; the printer doesn't have a driverless support - check via xref:_how_to_find_out_whether_my_printer_is_capable_of_driverless_printing?[ipptool] for network printers (if the printer has IPP support and you enable the port) and via xref:_how_to_find_out_if_my_usb_device_supports_ipp_over_usb[lsusb] for USB printers,
    \&#42; my PC is an endpoint device

    Currently there are two options - install the printer in xref:_how_to_install_a_printer_via_printer_application_in_snap_and_making_it_available_for_cups[printer application] and CUPS will automatically see it, or install it with classic driver xref:_how_to_install_a_permanent_print_queue[permanently]. Installation with classic driver is deprecated and will be removed in CUPS 3.0.

    ==== I'm in a company which has a print server where office printers are installed, I want to print to the print server - no mDNS, but with driverless

    \&#42; the print server supports IPP Everywhere and is in a different network or doesn't register on mDNS, or I don't want to use mDNS
    \&#42; remote print queue has the URI ipp://\&lt;server_hostname\&gt;:631/printers/\&lt;queue_name\&gt;, where \&lt;server_hostname\&gt; is the hostname of print server and \&lt;queue_name\&gt; is a name of a print queue I want to connect to
    \&#42; xref:_how_to_find_out_whether_my_printer_is_capable_of_driverless_printing?[ipptool] command passes if the URI is used

    Such printers has to be installed xref:_how_to_install_a_permanent_print_queue[permanently] with IPP Everywhere driver.

    ==== I'm in a company which has a printer server where office printers are installed, I want to print to the print server - with working mDNS in local network

    Such remote printers are discovered automatically via mDNS and used as xref:_how_to_setup_cups_temporary_queues_with_network_printer[CUPS temporary queues] on network - they are seen on mDNS and automatically picked up by dialogs.

    ==== I want to print, but I don't want to or can't use mDNS, regardless whether my printer supports driverless printing

    Every printer which can't be discovered by mDNS has to be installed xref:_how_to_install_a_permanent_print_queue[permanently] in CUPS or, in CUPS 3.0, by printer profile.

    . Driverless printers:
    \&#42; all of them supported by \&#42;IPP Everywhere\&#42; model under Manufacturer entry in CUPS Web UI and as \&#42;everywhere\&#42; in CLI
    \&#42; types based on origin:
    \&#42;\&#42; Network:
    \&#42;\&#42;\&#42; URI: ipp://\&lt;hostname_or_ip\&gt;:631/ipp/print , where \&lt;hostname_or_ip\&gt; is hostname or IP address of the printer
    \&#42;\&#42; IPP-over-USB printers via ipp-usb:
    \&#42;\&#42;\&#42; URI: ipp://localhost:60000/ipp/print
    \&#42;\&#42; Printers installed via printer application:
    \&#42;\&#42;\&#42; URI: ipp://localhost:8000/ipp/print/\&lt;printer_name\&gt; , where \&lt;printer_name\&gt; is the printer name chosen in printer application

    . Remote print queues on a print server:
    \&#42; URI: ipp://\&lt;server_ip_or_server_hostname\&gt;:631/printers/\&lt;remote_print_queue\&gt; , where \&lt;server_ip_or_server_hostname\&gt; is server's IP address or hostname and \&lt;remote_print_queue\&gt; is a name of the print queue installed on the server
    \&#42; it depends on CUPS on the server whether a local printer which points to a printer on the server can be installed as IPP Everywhere model - usually CUPS 2.2.8 and newer support driverless and some distributions such as CentOS 8 backported the functionality as well
    \&#42; otherwise it depends on printer's driver on the old server - the key is to prevent applying the options multiple times (so one of the connections has to be raw and loses some of the functionality)

    . Legacy or specialized printers
    \&#42; (deprecated, to be removed in CUPS 3.0) can be discovered by CUPS and installed with classic drivers
    \&#42; can be installed in printer application and then installed in CUPS as a permanent queue (see driverless printers - printers installed via printer application above)

    ==== Driverless options don't do the trick for me on my driverless printer, I want to use features from the driver

    The current recommended action is to install the printer via xref:_how_to_install_a_printer_via_printer_application_in_snap_and_making_it_available_for_cups[printer application], which contains the classic driver, because installation the printer permanently in CUPS with classic driver is deprecated and it will be removed in CUPS 3.0. Then mDNS can be used to catch it by CUPS or the printer from printer application has to be installed permanently in CUPS as a IPP Everywhere printer.

    In case of IPP-over-USB printers, a reject rule has to be added as described in xref:cups-known-issues.adoc\&#35;_usb_printerscanner_doesnt_work_due_a_conflict_on_usb_port[known issues].

    ==== I install the printer on a server, which will share the printer further

    Printers on the server have to be installed xref:_how_to_install_a_permanent_print_queue[permanently] to be shared. IPP Everywhere model (directly to the printer or via printer application) is the ideal, but a classic driver with standardized PPD options on a server capable of using driverless is fine as well - clients can use IPP Everywhere model when pointing to the server and options are translated properly. Otherwise there is a possibility that some options aren't applied or applied twice. Don't forget about enabling IPP in firewall, setting ACLs to the server via [filename]\&#96;/etc/cups/cupsd.conf\&#96; and attaching the daemon to port 631 instead of localhost.

    ==== I'm in a company with old print server incapable of driverless, I want to print

    The important thing is to prevent applying options multiple times in this scenario. There are several ways how to do it:

    \&#42; ask your IT support for the driver (print queue on the server has to be raw)
    \&#42; use \&#42;ServerName\&#42; directive in [filename]\&#96;/etc/cups/client.conf\&#96; or \&#42;CUPS_SERVER\&#42; environment variable to connect to the server directly - you won't be able to do admin tasks, but capable of printing.

    === How to find out whether my printer is capable of driverless printing?

    Network printers have the prerequisites - enablement of IPP port on the printer is the minimum, mDNS is required for automatic printer discovery by \&#96;libcups\&#96;. If needed, enable AirPrint, IPP Everywhere or any other driverless standards related options in the printer settings, either via the printer panel or the printer web interface.

    \&#42; [command]\&#96;ipptool\&#96; command which sends IPP Get-Printer-Attributes request to the network printer passes:

    ----
    $ ipptool -tv ipp://printer.example.com:631/ipp/print get-printer-attributes.test
    '/usr/share/cups/ipptool/get-printer-attributes.test':
    Get-Printer-Attributes:
    attributes-charset (charset) = utf-8
    attributes-natural-language (naturalLanguage) = en
    printer-uri (uri) = ipp://printer.example.com:631/ipp/print
    requested-attributes (1setOf keyword) = all,media-col-database
    Get printer attributes using get-printer-attributes                  [PASS]
    \&#8230;
    ----

    , where \&#96;printer.example.com\&#96; is the hostname or IP of your network printer,

    \&#42; look for AirPrint among device specification,
    \&#42; https://www.pwg.org/printers/[Officially certified printers for IPP Everywhere],
    \&#42; check xref:_how_to_setup_cups_temporary_queues_with_network_printer[manual] for enabling CUPS temporary queues - if your printer is seen in the end in CUPS commands that way, your printer is capable of driverless printing,
    \&#42; [USB devices only] check for IPP over USB (xref:_how_to_find_out_if_my_usb_device_supports_ipp_over_usb[manual] here).

    === How to find out if my USB device supports IPP over USB

    Check whether your USB device has a following text in [command]\&#96;lsusb -v\&#96; output:

    ----
    \&#8230;
    bInterfaceClass         7 Printer
    bInterfaceSubClass      1 Printer
    bInterfaceProtocol      4
    iInterface              0
    \&#8230;
    ----

    If the device has the _bInterfaceClass 7_, _bInterfaceSubClass 1_ and _bInterfaceProtocol 4_ in the sequence, it supports IPP over USB which is critical for USB device driverless printing and scanning.

    Note: Some manufacturers bind IPP over USB support with network driverless standards, which is not correct. If the printer has network and USB connectivity and IPP over USB is not shown in \&#96;lsusb\&#96; output, try to look into printer settings, enable AirPrint and check the \&#96;lsusb -v\&#96; output again.

    === How to setup CUPS temporary queues

    To setup the temporary queues correctly, there are several prerequisites:

    \&#42; printer/remote print queue has a driverless support and has it enabled,
    \&#42; your PC has avahi-daemon service or avahi-daemon socket running,
    \&#42; your PC has cups socket or service running,
    \&#42; mDNS hostnames are resolvable - test by pinging a .local hostname

    ==== How to setup CUPS temporary queues with network printer

    \&#42; additional requirement:
    \&#42;\&#42; enable MDNS in your firewall settings

    After this the temporary queue will appear in the print dialog and you don't need to install a specific print queue unless you have a reason for it.

    You can check if your printer is seen in mDNS messages by (\&#42;avahi-tools\&#42; must be installed):

    ----
    $ avahi-browse -avrt
    \&#8230;
    = enp0s25 IPv4 HP LaserJet M1536dnf MFP (42307C)             _ipp._tcp            local
    hostname = [NPI42307C.local]
    address = [192.168.1.10]
    port = [631]
    txt = ['UUID=434e4239-4243-4a42-5859-3c4a9242307c' 'Scan=T' 'Duplex=T' 'Color=F' 'note=' 'adminurl=http://NPI42307C.local.' 'priority=10' 'product=(HP LaserJet M1536dnf MFP)' 'ty=HP LaserJet M1536dnf MFP' 'URF=CP99,W8,OB10,PQ3-4-5,DM1,IS1-4,MT1-2-3-5,MT1-2-3-5,RS600' 'rp=ipp/printer' 'pdl=application/postscript,application/vnd.hp-PCL,application/vnd.hp-PCLXL,application/pdf,image/urf' 'qtotal=1' 'txtvers=1']
    \&#8230;
    ----

    and if CUPS or its backends see the printer by commands:

    (lists all existing print queues - permanent or temporary - temporary ones contain \&#42;network\&#42; as the second string on a line)

    ----
    $ lpstat -l -e
    HP_LaserJet_M1536dnf_MFP_42307C network none ipp://HP%20LaserJet%20M1536dnf%20MFP%20(42307C)._ipp._tcp.local/
    myprinter permanent ipp://localhost/printers/myprinter beh:/1/3/5/socket://printer:9100
    ----

    or

    (lists all devices, which CUPS sees in the local network or USB)

    ----
    $ lpinfo -l -v
    \&#8230;
    Device: uri = ipp://HP%20LaserJet%20M1536dnf%20MFP%20(42307C)._ipp._tcp.local/
    class = network
    info = HP LaserJet M1536dnf MFP (driverless)
    make-and-model = HP LaserJet M1536dnf MFP
    device-id = MFG:HP;MDL:LaserJet M1536dnf MFP;CMD:PDF,PS,PCL,AppleRaster,URF;
    location =
    \&#8230;
    ----

    ==== How to setup CUPS temporary queues with USB printer

    \&#42; additional requirements:
    \&#42;\&#42; install \&#42;ipp-usb\&#42;,  which will transform IPP over USB devices to network printer on localhost:

    ----
    $ sudo dnf -y install ipp-usb
    ----

    Then you can follow the steps in xref:_how_to_setup_cups_temporary_queues_with_network_printer[manual] for network printers.

    === How to install a permanent print queue

    Prerequisites for permanent driverless printers: enable IPP in your firewall, enable IPP on your printer if possible.

    ==== Installation via CUPS web UI ====

    \&#42; start cups.service

    ----
    $ sudo systemctl start cups
    ----

    \&#42; go to \&#42;http://localhost:631\&#42; in your browser
    \&#42; go to \&#42;Administration\&#42; tab
    \&#42; click on \&#42;Add printer\&#42;
    \&#42; enter your credentials
    \&#42; choose the found device or the connection you prefer - for driverless permanent queue choose \&#42;Internet Printing Protocol (ipp)\&#42;
    \&#42; in case you didn't choose a found device, enter the device uri at the next page - for driverless printers they usually are:

    ----
    Network printers:
    ipp://\&lt;printer_IP_or_printer_hostname\&gt;:631/ipp/print

    USB printers via ipp-usb:
    ipp://localhost:60000/ipp/print

    Non-driverless printers via printer application:
    ipp://localhost:8000/ipp/print/\&lt;printer_name\&gt;

    Printers pointing to a remote CUPS server:
    ipp://\&lt;server_ip_or_server_hostname\&gt;:631/printers/\&lt;remote_print_queue\&gt;
    ----

    \&#42; choose device manufacturer and model (\&#42;IPP Everywhere\&#42; for driverless printers)
    \&#42; set a different default options if needed and finish

    \&#42;Notes:\&#42;

    Adding a permanent queue for driverless USB printers or non-driverless printers installed in a printer application is usually unnecessary, because they are shared by mDNS on localhost, so any application using CUPS 2.0+ API functions (cupsGetDests(), cupsGetNamedDest(), cupsCopyDestInfo()) should be able to pick them automatically (for network printer it depends whether the device is in the same subnet as your machine). Installing them permanently should be necessary only if an application doesn't use the recent API or to work around a bug which happens when using them as temporary queues.

    If there are more devices via \&#42;ipp-usb\&#42; or printer applications, they listen on different ports - devices via ipp-usb start on port 60000, separate printer applications start on port 8000.


    ==== Installation via CLI commands ====

    \&#42; you will need a device uri - \&#96;\&lt;device_uri\&gt;\&#96;, which you can find by \&#96;lpinfo -v\&#96;:

    ----
    $ lpinfo -v
    direct usb://HP/Officejet%20Pro%208500%20A909a?serial=NNNNNNNNN\&amp;interface=1
    ====================================================================
    network dnssd://Officejet%20Pro%208500%20A909a%20%5B43FD8E%5D._pdl-datastream._tcp.local/
    =================================================================================
    ----

    or construct it manually - f.e. for IPP printers:

    ----
    ipp://\&lt;IP/hostname\&gt;:631/ipp/print
    ----

    and a driver name - \&#96;\&lt;driver\&gt;\&#96;, f.e.:

    ----
    $ lpinfo -m
    \&#8230;.
    everywhere IPP Everywhere
    ==========
    \&#8230;
    ----

    ----
    $ lpadmin -p \&lt;name\&gt; -v \&lt;device_uri\&gt; -m \&lt;driver\&gt; -E
    ----

    where \&#96;\&lt;device_uri\&gt;\&#96; and \&#96;\&lt;driver\&gt;\&#96; are underscored strings from previous commands and \&#96;\&lt;name\&gt;\&#96; is a print queue name, which is chosen by you.

    == How to install a printer via printer application in SNAP and making it available for CUPS

    Currently printer applications are available in SNAPs on Fedora. I'm planning to release them as RPMs, but the code base will be the same, so its testing can happen even with SNAPs.

    \&#42; install snapd,

    First we have to install snapd for testing purposes:

    ----
    $ sudo dnf -y install snapd
    $ sudo ln -s /var/lib/snapd/snap /snap
    $ snap version
    ----

    If the installation had been successful, the last command will show snapd's version.

    \&#42; install and run printer application,

    First the SNAP with printer application has to be installed and started by the commands below. All printer applications are available in SNAP Store under the same names as they are at https://github.com/orgs/OpenPrinting/repositories[OpenPrinting repositories]. We will use [filename]\&#96;ps-printer-app\&#96; printer application in the next steps.

    ----
    $ sudo snapd install --edge ps-printer-app
    $ sudo snapd run ps-printer-app
    ----

    \&#42; go to http://localhost:8000,

    After starting the printer application its web interface becomes available at http://localhost:8000 - if user installs and runs another printer application, it will become available at localhost on the next port (8001). The printer application can contain several printers (as [filename]\&#96;cupsd\&#96; does).

    \&#42; click on \&#96;Add Printer\&#96; on the main page,
    \&#42; choose the printer's name,
    \&#42; select the found device or choose \&#96;Network printer\&#96; from \&#96;Device\&#96; scroll menu and provide hostname or IP of the device,
    \&#42; choose to auto-detect driver or select the driver by yourself,
    \&#42; click on \&#96;Add Printer\&#96;,
    \&#42; now the printer should be available at least on localhost via mDNS (if [filename]\&#96;avahi-daemon\&#96; is running and \&#96;nss-mdns\&#96; is installed)- check it by [filename]\&#96;avahi-browse\&#96;(\&#96;avahi-tools\&#96; has to be installed):

    ----
    $ avahi-browse -avrt
    \&#8230;
    =     lo IPv4 HP Laserjet M1536                             _ipp._tcp            local
    hostname = [fedora-2.local]
    address = [127.0.0.1]
    port = [8000]
    txt = ['Scan=F' 'PaperMax=legal-A4' 'Fax=F' 'product=(HP LaserJet M1536dnf MFP Postscript (recommended))' 'mopria-certified=1.3' 'priority=0' 'qtotal=1' 'txtvers=1' 'Duplex=T' 'Color=F' 'TLS=1.2' 'URF=V1.5,W8,PQ3-4-5,DM1,FN3,IS0-20,MT1-5-6-3,OB10,RS300-600' 'UUID=24837a30-5f87-3ac9-6d85-086d486092dd' 'pdl=image/pwg-raster,image/urf,application/vnd.printer-specific,application/pdf,application/postscript,image/jpeg,image/png' 'note=' 'adminurl=http://fedora-2.local:8000/HP_Laserjet_M1536/' 'ty=HP LaserJet M1536dnf MFP Postscript (recommended)' 'rp=ipp/print/HP_Laserjet_M1536']
    \&#8230;
    ----

    \&#42; and by \&#96;lpstat -e\&#96;:

    ----
    $ lpstat -e
    \&#8230;
    HP_Laserjet_M1536
    \&#8230;
    ----

    The available printing options for the printer installed via printer application can be checked with [filename]\&#96;lpoptions\&#96; command:

    ----
    $ lpoptions -p HP_Laserjet_M1536 -l
    PageSize/Media Size: 184.15x260mm 195.09x269.88mm A4 A5 B5 DoublePostcardRotated Env10 EnvC5 EnvDL EnvMonarch Executive FanFoldGermanLegal ISOB5 Legal \&#42;Letter Postcard roc16k Custom.WIDTHxHEIGHT
    InputSlot/Media Source: \&#42;Auto Tray1 Auto
    MediaType/Media Type: \&#42;Unspecified Stationery Light6074 MidWeight96110 Heavy111130 ExtraHeavy131175 MonochromeLaserTransparency Labels StationeryLetterhead Envelope StationeryPreprinted Prepunched Colored Bond StationeryRecycled Rough Vellum
    cupsPrintQuality/cupsPrintQuality: Draft \&#42;Normal High
    ColorModel/Output Mode: \&#42;Gray
    Duplex/Duplex: \&#42;None DuplexNoTumble DuplexTumble
    OutputBin/OutputBin: \&#42;FaceDown
    ----

    == How to install a scanner

    Scanners in Linux don't have to be installed the same way as printers are if they are in the same network or connected via USB - you just need \&#42;sane-backends\&#42; to be installed and any scanning application will communicate with scanner/multifunction device via the backend which supports the scanner.

    However, the older HP scanners and multifunction devices require an additional package - \&#42;hplip\&#42; - and its binary plugins downloaded via [command]\&#96;hp-plugin -i\&#96; if they aren't supported by sane-backends already.

    === How to find out my multifunction device or standalone scanner is capable of driverless scanning?

    \&#42; check the device specification and look for eSCL/AirScan/WSD - if any of these are mentioned, the device is capable of driverless scanning
    \&#42; most devices which advertise they can do AirPrint are capable of AirScan too
    \&#42; [USB devices only] check for IPP over USB (xref:_how_to_find_out_if_my_usb_device_supports_ipp_over_usb[manual] here).

    === How to make driverless scanning work

    For LAN located and USB devices:

    \&#42; have \&#42;avahi-daemon\&#42; enabled and running

    ----
    $ sudo systemctl enable avahi-daemon
    $ sudo systemctl start avahi-daemon
    ----

    \&#42; enable MDNS in firewall
    \&#42; [USB devices only] install \&#42;ipp-usb\&#42;

    For network scanners in a different network:

    \&#42; set the scanner device uri in [filename]\&#96;/etc/sane.d/airscan.conf\&#96; - see:

    ----
    man sane-airscan
    ----

    == How to setup mDNS with systemd-resolved

    systemd-resolved is enabled and running by default since F33 and can be setup to work with Avahi on mDNS support which CUPS needs - Avahi does the advertising, registering and sharing devices, and resolved will handle '.local' address resolution. It will work with following steps:

    \&#42; put [option]\&#96;MulticastDNS=resolve\&#96; into [filename]\&#96;/etc/systemd/resolved.conf\&#96;

    ----
    $ sudo systemctl restart systemd-resolved
    $ sudo nmcli connection modify \&lt;connection_name\&gt; connection.mdns yes connection.llmnr yes
    $ sudo systemctl restart NetworkManager
    ----

    == How to compress files

    Example:

    ----
    $ tar -czvf cups-information.tar.gz /etc/cups cups.logs troubleshoot.txt lpinfo.log
    ----

    == Restarting cups service

    You restart cups service with:

    ----
    su -c 'systemctl restart cups.service'
    ----


    = CUPS – Printing and Scanning Terminology
    Brandon Nielsen; Zdenek Dohnal


    == Printing

    === Print queue

    Abstraction unit in CUPS for a printer - it has a device uri, which represents connection to the device, and can exist with classic driver (PPD file from different package) or without (driverless printing). The entries you see in print dialogs and settings are those _print queues_. They can be _permanent or temporary_.

    === Permanent print queues

    The queues with classic driver or driverless print queue which need to be shared further down the network.

    === Temporary print queues

    The queue which don't need to be installed at all - they show up during print dialog and they disappear once the printing is done successfully. They rely on _driverless printing_.

    === Remote CUPS queue

    The queue on the different machine, where other cupsd process is running, than on the local machine. They are usually found in enterprise solutions, where printers aren't in the same network as users or if admin wants a centralized monitoring above all printers. In such solutions, users set up _cups-browsed_ to install remote CUPS queue as local queues via _BrowsePoll_ directive, or install a specific queue via GNOME. There can be a solution how to redirect mDNS messages which CUPS server advertises to the networks with users, but I haven't been to setup this correctly yet.

    === Classic drivers

    Those are the binaries and PPD files, which need to be installed for the device to work. This is older way of supporting devices, which will go away in the future.

    === Driverless printing (wireless/ethernet)

    Most of modern devices (2010+) complies to AirPrint, Mopria or IPP Everywhere standard, which means they don't need a classic driver for being able to print. Those devices have IPP (Internet Printing Protocol) 2.0+ implemented within, are capable to 'advertise' themselves via mDNS and they support document formats like PDF, PCLm, JPEG, Apple Raster or PWG Raster.

    There are several prerequitises which need to fulfill in OS to have an access to the driverless feature:

    \&#42; avahi-daemon must run
    \&#42; there needs to be a '.local' address resolver active - systemd-resolved or nss-mdns
    \&#42; the device itself must have IPP port (631) and Bonjour/MDNS enabled
    \&#42; IPP and MDNS need to be enabled in firewall

    How does the driverless printing work under the roof (put it simply):

    \&#42; CUPS sees the printer in mDNS messages via Avahi
    \&#42; CUPS will find out the printer capabilities via IPP
    \&#42; if there is a print job, CUPS will set up the filter chain to convert the incoming file into document format which printer understands (Apple Raster, PDF, PWG Raster, PCLm, JPEG)

    In case it is needed, PPD file is generated by PPD generator in CUPS or by _driverless_ binary.

    One of the features which use driverless printing is _CUPS temporary queues_.

    See xref:cups-useful-tricks.adoc\&#35;_how_to_find_out_whether_my_printer_is_capable_of_driverless_printing[manual] how to check if your printer is capable of driverless printing.

    === Printing using a driver

    This printing is similar to driverless printing in matter of setting up a filter chain, but:

    \&#42; it can use limited mDNS and IPP functionality or it doesn't use them at all
    \&#42; all information about device capabilities is taken from PPD (Postscript Printer Description) file
    \&#42; can use a specialized filters and specialized communication with the device (depends on driver)

    The downsides of this approach is to rely on 3rd party drivers, you need to always install a permanent queue for it and it will go away in the future.

    === Raw queue

    No filters are started by CUPS if you print to such a queue, the data are sent as they are to the target, no options are applied by CUPS - all regardless of incoming document format. It is required the application you use for printing sends a printer-ready data (in the correct format, with all chosen options applied) or the destination is set to the desired settings (f.e. printer/print server is set to do two-sided-long-edge duplex with grayscale settings, so every document printed will have this settings and user won't  be able to change it in an application).

    This approach is usually set for printing to older label printers via a specific application, or, in the past, for printing to remote CUPS queue. Because CUPS has no way how to provide common user experience (finding out printer properties, converting various document formats into a document format the printer accepts, setting printing options) for such queues, their usage is deprecated and it will be removed in the future (in CUPS 3.X).

    === Raw printing

    Raw printing happens if CUPS receives a file in document format which printer accepts directly and CUPS recognizes the format based on rules from its MIME database. CUPS daemon doesn't start any filters for such a job (it might encapsulate options into IPP packet, if the connection with the printer is over IPP) with exception for PDFs, where the _pdftopdf_ filter is started to apply generic settings like scaling, rotation etc. Raw printing itself happens on print queues with classic driver and driverless print queues. This functionality stays with CUPS 3.X.

    The difference between raw printing and raw queue is the raw printing is a situation which happens if CUPS daemon gets a file in format which printer accepts, so the daemon does not spawn additional filters for such job (with PDF being an exception), and spawns filters for document formats, which are not acceptable by the printer directly, whereas the raw queue is a queue, which CUPS daemon does not spawn any filters in any circumstances, and behaves like a Unix pipeline.

    === Printer applications

    The binaries which provide support for older devices which aren't capable of complying to driverless standards. The core idea is they will be capable of accepting the old driver and then advertise itself as a device capable of driverless printing. Then the new CUPS will be able to see them and user will be able to print via them as if they were temporary queues. The currently available printer applications in Fedora are _ippeveprinter_ (a part of CUPS - see cups-printerapp package) and _lprint_ (provides support for devices which requires raw printing - mostly label printers). Other printer applications like https://github.com/OpenPrinting/ps-printer-app[ps-printer-app], https://github.com/OpenPrinting/ghostscript-printer-app[ghostscript-printer-app], https://github.com/OpenPrinting/hplip-printer-app[hplip-printer-app] and https://github.com/OpenPrinting/gutenprint-printer-app[gutenprint-printer-app] are currently available as SNAPs until cups-filters 2.0 is released and packaged. Printer applications are, except for _ippeveprinter_, written using _PAPPL_ library, so such printer application provides CLI interface and Web Interface for users to interact with.

    === Driverless printing (USB)

    Driverless printing has its variant for devices which are connected via USB - it is covered by 'IPP over USB' standard. For make it work, you need 'ipp-usb' package, which will register the device with Avahi on localhost - then USB device will look as a wireless/ethernet device. The discovery/printing looks the same as with a wireless/ethernet device with driverless support.

    See xref:cups-useful-tricks.adoc\&#35;_how_to_find_out_whether_my_printer_is_capable_of_driverless_printing[manual] how to check for IPP-over-USB.

    == Scanning

    === Classic scanning (via hplip and sane-backends)

    The classic scanning works via backends, which are binaries for communication with device. There are several backends, usually created by reverse engineering communication between scanner and MS Windows driver. None of classic backends implements a protocol, which is compatible with most devices available.

    === Driverless scanning

    The driverless scanning uses sane-escl (not built in Fedora) and sane-airscan backends for communicating with newer devices. Those newer devices usually support eSCL (based on AirScan protocol by Apple) or WSD (Web Services for Devices by Microsoft), which _sane-airscan_ is able to use.

    Regarding USB scanning, it has the same requirement as printing. The device must support IPP over USB driverless standard and _ipp-usb_ package must be installed to get driverless scanning via USB - the package is required because it creates a driverless interface over USB interface which _sane-airscan_ uses for driverless communication with device.





    = CUPS – Known Issues
    Brandon Nielsen; Zdenek Dohnal


    Here are several known issues, which arise with certain circumstances, and there isn't general solution or upstream didn't want to add the solution to its project:

    == cups-browsed

    === Cannot print due 'No destination hostname provided by cups-browsed, is it running?'


    cups-browsed sometimes loses connection to print server (usually with old ones, like cups-1.4.2) when laptop changes network connection (change of WiFi network or after hibernate/suspend). You can make printing working again with cancelling your jobs and restarting cups-browsed by

    ----
    $ cancel -a
    $ sudo systemctl restart cups-browsed
    ----

    === cups-browsed consumes large amount of CPU

    Creating local printer queues takes long time for some printers with larger PPD file, so timeout of http connection will time out and it creates infinite loop of creating local printer queues. To solve this issue, please add

    ----
    HttpLocalTimeout N
    HttpRemoteTimeout N
    ----

    into [filename]\&#96;/etc/cups/cups-browsed.conf\&#96;, where \&#96;N\&#96; is number of seconds after which connection is timed out. Then restart cups-browsed service. This option is currently in Fedora 27 and above.

    === [SINCE FEDORA 27] cups-browsed creates different printer queue names than before

    This issue is connected to remote cups queues, which are advertised by older CUPS version (usually below cups-1.5, e.g. RHEL 6). Cups-browsed creates local print queues named by printer's DNS-SD ID by default and naming by remote cups queue is enabled again by adding:

    ----
    LocalQueueNamingRemoteCUPS RemoteName
    ----

    into [filename]\&#96;/etc/cups/cups-browsed.conf\&#96; and restart cups-browsed service.

    == cups-filters

    === Printing takes a long time or doesn't print at all

    When your printer needs a lot of time to do printing (from your POV) or doesn't print at all (some Xerox printers have such problems with gs renderer, so they are working again only with pdftops renderer), you can try to change the default postscript renderer. The default renderer in Fedora for most printers is gs filter from Ghostscript, but we have pdftops filter from Poppler for Brother, Minolta and Konica Minolta printers - this setup is called hybrid.

    Other available renderer setups are gs (from Ghostscript), pdftops and pdftocairo (from Poppler), mupdf (from mupdf) and acroread (from adobe reader, not in Fedora official repositories), then you can set different default renderer for your print queue like this:

    ----
    \&#35; lpadmin -p \&lt;printer-name\&gt; -o pdftops-renderer-default=gs/pdftops/pdftocairo/mudpf/acroread/hybrid
    ----

    \&#42;BEWARE:\&#42; Most 'slow' printing issues are caused by PDF creating applications, which generates bad PDF file - and that bad generated PDF file is mostly the core of problem. To sum it up, slow printing issue can rise again with different PDF file, then it is on user's decision: if he wants to print fast and probably sometimes change the default renderer, or slow printing is not such critical issue.

    == CUPS

    === [Fixed in F33 and later] Firefox, Evince (PDF viewer), GVim, Gedit, Gnome Control Center show a 'dummy'/duplicate print queue, which doesn't work

    This bug is connected to every application which uses GTK print dialog. GTK dialog decided to take information about available from two sources - mDNS messages from Avahi and CUPS - this dummy/duplicate print queue is a print queue GTK created in its dialog based on Avahi messages, but it doesn't exist in CUPS, because no one created it, and later GTK behaves like it exists in CUPS. So every time an user wants to print, GTK sends a request to CUPS for this queue, but it gets dropped by CUPS because the queue doesn't exist.

    The feature which GTK is trying to do here is called CUPS temporary queues - GTK developers is currently working on a immediate fix in this https://bugzilla.redhat.com/show_bug.cgi?id=1784449[bugzilla]. The future plan is to use https://github.com/OpenPrinting/cpdb-backend-cups[cpdb-backend-cups] backend in GTK, but right now we are focusing on the intermediate fix.

    ===  CUPS doesn't take nicely some kinds of FQDN

    CUPS sometimes has problems with some kinds of FQDN - that means when you use FQDN in [option]\&#96;BrowsePoll\&#96; directive in [filename]\&#96;/etc/cups/cups-browsed.conf\&#96;, CUPS doesn't recognize it as valid hostname - it is solved by adding:

    ----
    ServerAlias your.own.fully.qualified.hostname.com
    ----

    into [filename]\&#96;/etc/cups/client.conf\&#96; and restarting cups service.

    === There are less options available if the device is used as driverless than with a classic driver

    The similar situation can happen with \&#42;sane-airscan\&#42; supported scanners. Some devices declare less options via protocols - f.e. IPP 2.0+, WSD, eSCL - which support driverless solutions than via classic drivers. Usually it is an issue with device's firmware, which can be verify by checking the output of the following command:

    ----
    $ ipptool -tv \&lt;ipp_device_uri\&gt; get-printer-attributes.test
    ----

    The commands does the same IPP request which is done when a temporary queue appears in the print dialog or when you install the queue permanently. The printer options are set from the IPP response for this request, so if the option is missing in the response, CUPS cannot generate such a printer option. The solution is to try to update the device firmware, report the issue to the device manufacturer and at https://bugzilla.redhat.com[bugzilla] with logs.

    === [F33+] Printing via IPPS doesn't work

    Fedora 33 came up with a raised bar regarding crypto-policies, so SSL and older TLS protocols are disabled on system level. The change breaks printing via IPPS to devices which don't support newer protocols. You can set back legacy crypto support in crypto-policies via:

    ----
    $ sudo update-crypto-policies --set DEFAULT:FEDORA32
    ----

    The policy change transitionally has an impact on devices found by cups-browsed, because the daemon prefers IPPS uris if they are reported as available by printer/server.

    === Printed PDF has incorrectly printed characters

    Sometimes, PDF support does not work correctly with certain printers, which can result in garbled output (e.g. diacritics such as š or ž are printed as small rectangles).

    If the printer driver supports rasterization as well, one could reinstall the printer with IPP Everywhere driver (the default driverless driver doesn't work with print as raster option):

    ----
    $ lpadmin -p \&lt;printer\&gt; -m everywhere -E
    ----

    One can now force rasterization for a new print job with:

    ----
    $ lp -d \&lt;printer\&gt; -o print-as-raster \&lt;file\&gt;
    ----

    or set the rasterization for this printer by default with:

    ----
    $ lpadmin -p \&lt;printer\&gt; -o print-as-raster-default=true
    ----

    However, be aware that some of the IPP functionality will not work with rasterization, e.g. finishings, so the best way of solving such issues is to contact your printer's manufacturer and ask them to update the printer's PDF support in its firmware.

    == HPLIP

    First I would like to mention that we are not responsible for support HPLIP, which is downloaded and installed from HP website. Please install hplip rpms from official Fedora repositories at most cases.

    === Hp-plugin: file does not match its checksum. File may have been corrupted or altered

    This common error is mostly caused by external causes (server outage, network outage), when wget tries to download plugin, but it returns only error message. It is connected with message:

    ----
    Plugin download failed with error code = N
    ----

    where \&#96;N\&#96; is return value of [command]\&#96;wget\&#96; ([command]\&#96;man wget\&#96;), which is used for downloading proprietary plugin. Solutions for this issue may vary - you can wait until servers go up again or try to install plugin, which you download manually from http://www.openprinting.org/download/printdriver/auxfiles/HP/plugins/ (select 'Select and install an existing local copy of the plug-in file' during [command]\&#96;hp-setup\&#96; or [command]\&#96;hp-plugin\&#96;).

    === Unable to load cupsext

    This error can occur when hplip is installed from HP website, or its dependencies are mixed python2 and python3 packages or installed by pip. This is solved by removing all hplip packages (hplip, hplip-gui, hplip-libs, hplip-common, libsane-hpiao) and installing them again all from repositories.

    === Missing hplip-gui

    GUI tools and GUI parts of HP commands are moved to hplip-gui subpackage, because the main package can work without GUI, so the main package is smaller. The outcome of this decision is HP commands need to be run with \&#96;-i\&#96; option for interactive mode, or hplip-gui subpackage needs to be installed.

    Tools, which need to be run with \&#96;-i\&#96; option for CLI or need to have hplip-gui installed for GUI:

    ----
    hp-align
    hp-clean
    hp-colorcal
    hp-diagnose_queues
    hp-fab
    hp-firmware
    hp-info
    hp-plugin
    hp-sendfax
    hp-setup
    hp-testpage
    hp-unload
    ----

    Tools, which are in hplip-gui:

    ----
    hp-check
    hp-print
    hp-systray
    hp-toolbox
    hp-devicesettings
    hp-faxsetup
    hp-linefeedcal
    hp-makecopies
    hp-printsettings
    hp-wificonfig
    ----

    === HP printer isn't discovered, doesn't print or doesn't print well

    Some HP printers don't work well with URIs provided by CUPS (dnssd, usb, ipp) or they need proprietary plugin from HP, which cannot be in Fedora because of licensing issues. For such printers please try to run:

    ----
    hp-setup -i -g
    ----

    for interactive mode, or:

    ----
    hp-setup -g
    ----

    for graphic mode. This command installs HP printers and HP scanners. If you have issue about HP printer/HP scanner, which isn't discovered, doesn't print or doesn't print well, please try to install it by [command]\&#96;hp-setup\&#96;, if it helps. If it doesn't help, please file a bugzilla, attach output of hp-setup and mention that you tried [command]\&#96;hp-setup\&#96;.

    === Device which needs plugin does not work after HPLIP update

    Devices which need plugin can stop to work after update to newer HPLIP version - it is due the check for plugin version in the code. The check is necessary to prevent inconsistencies when new features in open sourced HPLIP need new proprietary libraries from plugin. To make your printer work again, just download and install plugin again with:

    ----
    $ hp-plugin -i
    ----

    === Devices which require a binary plugin stopped to work on Fedora Silverblue/CoreOS

    Devices which require a HP close source binary plugin need to have plugin installed every time you start/restart your PC by default. HP closed source script installs the plugins into a readonly directories, so the plugins are removed once you start/restart Fedora. The workaround is to try if your device supports driverless printing and scanning, try hplip-plugin package from RPMFusion or keep installing the plugin everytime you want to print.

    == golang-github-openprinting-ipp-usb

    === USB printer/scanner doesn't work due a conflict on USB port

    \&#42;ipp-usb\&#42; daemon keeps the USB port of IPP-over-USB device opened for any possible IPP communication in the future, which blocks the port for other drivers (f.e. HPLIP, gutenprint, sane-backends\&#8230;).

    For printers the solution is to _uninstall the queue with the driver_ by:

    ----
    $ lpadmin -x \&lt;queue_name\&gt;
    ----

    and start using the one from \&#42;ipp-usb\&#42; (as a xref:cups-terminology.adoc\&#35;_temporary_print_queues[CUPS temporary queue] or install a permanent one - the default device uri is \&#96;ipp://localhost:60000/ipp/print\&#96;).

    In case of scanners \&#42;sane-airscan\&#42; automatically picks up the virtual device from \&#42;ipp-usb\&#42; if the device is capable of using WSD or eSCL protocols. However, if the scanner had been supported by classic scanner driver such as hplip or sane-backends and is now claimed by \&#42;ipp-usb\&#42; because it supports \&#42;IPP-over-USB\&#42; driverless standard, the old scanner is still shown, but it won't work for scanning due USB conflict. It happens because classic backends just list any device which they can find on USB interfaces and matches the description the backend supports, but backends don't check whether they actually can communicate with the device until they try to open the USB port for scanning process itself. This becomes a problem for scanning applications, which automatically choose the previous scanner as a default choice for scanning (such as _Simple Scan_) - users have to pick a driverless scanner from the list of available scanners before they scan.

    The scanner device discovered by classic SANE backends can be disabled from showing it among available scanners by commenting out its entry in backend's configuration file located in [filename]\&#96;/etc/sane.d\&#96; or the whole backend name in [filename]\&#96;/etc/sane.d/dll.conf\&#96;/[filename]\&#96;/etc/sane.d/dll.d\&#96;, f.e. Canon MF440 Series is reported by \&#96;pixma\&#96; and \&#96;airscan\&#96; backends, but only \&#96;airscan\&#96; works because it is a backend based on network protocol and USB interface is claimed by \&#96;ipp-usb\&#96;, so we will disable the \&#96;pixma\&#96; backend by commenting its line in [filename]\&#96;/etc/sane.d/dll.conf\&#96;:

    ----
    $ cat /etc/sane.d/dll.conf
    \&#8230;
    pint
    \&#35;pixma
    plustek
    \&#8230;
    ----

    If \&#42;ipp-usb\&#42; created device doesn't match your use case (the options you use are missing, the device doesn't work even if it is IPP-over-USB supported), please report the issue together with logs from [filename]\&#96;/var/log/ipp-usb/\&#96; directory at https://bugzilla.redhat.com[bugzilla]. \&#42;ipp-usb\&#42; itself supports quirks, which allows you to set the daemon to ignore your device and you can switch back to a classic driver. The steps are following:

    - get the device model name f.e. Canon MF440 Series:

    ----
    $ sudo ipp-usb check
    Configuration files: OK
    IPP over USB devices:
    Num  Device              Vndr:Prod  Model
    1. Bus 001 Device 005  04a9:2823  'Canon MF440 Series'
    ----

    - create a quirk file in [filename]\&#96;/etc/ipp-usb/quirks\&#96; directory in the format below:

    ----
    $ cat /etc/ipp-usb/quirks/canon.conf
    [Canon_MF440_Series]
    blacklist = true
    ----

    - restart the \&#96;ipp-usb\&#96; service:

    ----
    $ sudo systemctl restart ipp-usb
    ----


    == sane-airscan

    === There are less options available if the device is discovered by sane-airscan than with a classic driver

    The similar situation can happen with \&#96;everywhere\&#96; or \&#96;driverless\&#96; printer models. Some devices declare less options via protocols - f.e. IPP 2.0+, WSD, eSCL - which support driverless solutions than via classic drivers. Usually it is an issue with device's firmware, which can be verify in sane-airscan debug logs and network traffic. The solution is to try to update the device firmware, report the issue to the device manufacturer and at https://bugzilla.redhat.com[bugzilla] with logs.


    = CUPS – Filing a Bug Report
    Brandon Nielsen; Zdenek Dohnal


    // include::partial$attributes.adoc[]


    == Deciding which component

    Problems involving printing may relate to several components.

    The configuration GUI (See above) is either https://bugzilla.redhat.com/enter_bug.cgi?product=Fedora\&amp;component=control-center[GNOME 3 System Settings application] or https://bugzilla.redhat.com/enter_bug.cgi?product=Fedora\&amp;component=system-config-printer[system-config-printer]. These packages also provide the printer applet, handle automatic queue creation, and disable/enable queues when USB printers are disconnected and reconnected.

    Most GTK+ applications use the GTK+ print dialog. If the problem occurs when using GTK+ applications but not when printing from the command line or from another non-GTK+ application, the problem should probably be reported against the GTK+ version which the application uses. You can find out the version by the following query (\&#42;thunderbird\&#42; is used as an example of RPM package):

    ----
    $ rpm -q thunderbird | grep gtk
    libgtk-3.so.0
    ----

    From the output you can see \&#42;thunderbird\&#42; uses GTK+ version 3.

    If the problem occurs with only one GTK+ application, and other GTK+ applications print fine, the bug should be filed against that particular application.

    If the problem only happens with PDF files, the bug may well be in https://bugzilla.redhat.com/enter_bug.cgi?product=Fedora\&amp;component=poppler[poppler] (the CUPS \&#42;pdftops\&#42; filter is a wrapper around one of the poppler utility programs).

    Report bugs only seen using the \&#42;smb\&#42; backend against https://bugzilla.redhat.com/enter_bug.cgi?product=Fedora\&amp;component=samba[samba].

    For bugs only seen when using the \&#42;hp\&#42; backend, or the hpijs or hpcups drivers, select https://bugzilla.redhat.com/enter_bug.cgi?product=Fedora\&amp;component=hplip[hplip] for the component.

    For bugs for cups-browsed daemon and its printer discovery, please select https://bugzilla.redhat.com/enter_bug.cgi?product=Fedora\&amp;component=cups-filters[cups-filters]

    Other possibilities, depending on the problem, include:

    \&#42; https://bugzilla.redhat.com/enter_bug.cgi?product=Fedora\&amp;component=foomatic[foomatic] (the Foomatic CUPS filter and driver)
    \&#42; https://bugzilla.redhat.com/enter_bug.cgi?product=Fedora\&amp;component=foomatic-db[foomatic-db] (the actual printer database used by Foomatic)
    \&#42; https://bugzilla.redhat.com/enter_bug.cgi?product=Fedora\&amp;component=ghostscript[ghostscript] (which converts PostScript to other formats)
    \&#42; https://bugzilla.redhat.com/enter_bug.cgi?product=Fedora\&amp;component=gutenprint[gutenprint] (a driver that supports very many printers)

    For anything else, or if you are not sure, choose https://bugzilla.redhat.com/enter_bug.cgi?product=Fedora\&amp;component=cups[cups] or use your best guess.

    == Other information to include

    Be prepared to include some information about your system as well.

    === Before gathering of information

    \&#42; Please change your OS locale to English.
    \&#42; Please attach gathered information as archive (example is xref:cups-useful-tricks.adoc\&#35;_how_to_compress_files[here], you may need root permissions) to the bugzilla issue.
    \&#42; Please do not forget to trigger your issue after debug enabling and restarting cups and before information gathering.

    ===  Information to gather

    \&#42; the PPD file for the print queue (from the \&#96;/etc/cups/ppd\&#96; directory)
    \&#42; the document you are attempting to print -- if the document is large, please try to see if the problem also occurs with a smaller document
    \&#42; cupsd journal logs when debug level 2 is turned on. See the xref:how-to-debug-printing-problems.adoc\&#35;_enable_cups_debug_logging[how-to for turning debug2 on and for getting logs from systemd-journald].
    \&#42; if the issue is connected to a print job, attach journal logs for this specific job too. How-to get logs xref:how-to-debug-printing-problems.adoc\&#35;_get_a_job_log_for_a_specific_job_id[here], example with JID. You can find out JID value by command:

    ----
    $ lpstat -W all
    ----

    Find your job there and JID is a number after '-'.

    \&#42; If the issue is about f.e. 'printing from evince prints garbage, but printing from libreoffice works', then attach two separate files - first will contain logs when you print from evince, latter logs when you print from libreoffice.
    \&#42; [filename]\&#96;troubleshoot.txt\&#96; from system-config-printer (BEWARE: it doesn't contain journal logs - don't forget to attach them too).
    \&#42; xref:how-to-debug-printing-problems.adoc\&#35;_what_make_and_model_is_my_printer[make and model] of printer
    \&#42; config files - [filename]\&#96;/etc/cups/client.conf\&#96; (if it contains any changes from default), [filename]\&#96;/etc/cups/cupsd.conf\&#96;
    \&#42; if the issue is with cups-browsed and printer's discovery, attach [filename]\&#96;/etc/cups/cups-browsed.conf\&#96; and cups-browsed logs gained by xref:how-to-debug-printing-problems.adoc\&#35;_cups_browsed_logging[this how-to].

    Some example documents can be found in the https://fedoraproject.org/wiki/Category:Printing_Test_Cases[Printing Test Cases category].

    ==  Further reading

    The https://fedoraproject.org/wiki/Printing[main printing page] and the xref:cups-terminology.adoc\&#35;_printing[printing terminology page] have more information about how printing works in Fedora.





    \&#42; Troubleshooting
    = Troubleshooting Bluetooth problems
    Dzickus; Hhlp; Devurandom

    //:page-aliases:


    Bluetooth is a short range wireless protocol that is used to connect to various low bandwidth I/O devices (like keyboards, mice, headsets).  Newer versions have a low-energy mode with a slightly higher bandwidth and range.

    The Bluetooth solution is composed of a userspace daemon, bluetoothd, that communicates through a management port in the kernel to the hardware drivers.  Applications that want to communicate with the bluetoothd daemon do so over a d-bus api.  This includes the various GNOME bluetooth applets.


    == Identifying Bluetooth Problems

    === Was the bluetooth hardware found?

    \&#42; make sure bluetooth was found and enabled (note hci0: and 'UP RUNNING'):
    +
    [source,_console]
    ----
    $ hciconfig
    hci0:   Type: Primary  Bus: USB
    BD Address: xx:xx:xx:xx:xx:xx  ACL MTU: 1021:4  SCO MTU: 96:6
    UP RUNNING PSCAN
    RX bytes:15047 acl:0 sco:0 events:2433 errors:0
    TX bytes:599323 acl:0 sco:0 commands:2431 errors:0
    ----

    \&#42; If the command returns nothing (no hci: info), then there is a hardware issue
    +
    [source,_console]
    ----
    $ lsusb -v | grep Bluetooth | grep DeviceProtocol
    bDeviceProtocol         1 Bluetooth
    ----

    \&#42; If the lsusb command returns nothing, there is no hardware, a dmesg output would be needed

    \&#42; If the lsusb commands returns Bluetooth, then check for attached driver
    +
    [source,_console]
    ----
    $ lsusb -t | grep Wireless
    |__ Port 4: Dev 4, If 1, Class=Wireless, Driver=btusb, 12M
    |__ Port 4: Dev 4, If 0, Class=Wireless, Driver=btusb, 12M
    ----

    \&#42; If Driver is empty, \&#96;lsusb -v\&#96; output would be needed to add ids

    \&#42; If hciconfig shows output but not UP
    +
    [source,_console]
    ----
    $ hciconfig up
    ----

    \&#42; List of paired devices:
    +
    [source,_console]
    ----
    $ bluetoothctl
    [bluetooth]\&#35; show
    [bluetooth]\&#35; devices
    [bluetooth]\&#35; info \&lt;mac addr of any device you have problems with\&gt;
    ----

    === Is the bluetoothd daemon running?

    \&#42; Verify under systemd bluetooth is 'Active' and 'enabled'
    +
    [source,_console]
    ----
    $ systemctl status bluetooth
    ● bluetooth.service - Bluetooth service
    Loaded: loaded (/usr/lib/systemd/system/bluetooth.service; enabled; vendor preset: enabled)
    Active: active (running) since Wed 2017-10-04 16:07:40 EDT; 1 day 22h ago
    Docs: man:bluetoothd(8)
    Main PID: 27427 (bluetoothd)
    Status: 'Running'
    Tasks: 1 (limit: 4915)
    CGroup: /system.slice/bluetooth.service
    └─27427 /usr/libexec/bluetooth/bluetoothd
    ----

    \&#42; Verify obex is configured to run (to transfer files from phone)

    [source,_console]
    ----
    $ systemctl --global --user is-enabled obex
    enabled
    ----

    == Simple debugging

    Most bluetooth problems happen in the bluez package (bluetoothd), ie the userspace daemon.

    .Enabling bluetoothd debugging
    \&#42; edit \&#96;/usr/lib/systemd/system/bluetooth.service\&#96;
    \&#42; add \&#96;-d\&#96; to ExecStart line as option to bluetoothd
    \&#42; save and quit

    [source,_console]
    ----
    $ systemctl daemon-reload
    $ systemctl restart bluetooth
    ----

    Debugging is enabled and can help pinpoint where some of the bluetooth problems are

    .Capture the logs to put in bugzilla report

    [source,_console]
    ----
    $ journalctl -r -u bluetooth \&gt; /tmp/bluetoothd.out
    ----

    == Resolving firmware problems

    It happens that the firmware of bluetooth adapters enters a state where it is unable to pair with a certain (or all) bluetooth devices.  You might be able to resolve such problems by resetting your adapter.

    In the case of a laptop with a built-in bluetooth adapter this might be achieved by:


    1. Enter the laptop's firmware settings (BIOS) and disable the built-in adapter
    2. Save settings and restart the laptop
    3. Enter the firmware settings a second time and enable the bluetooth adapter again
    4. Save and restart
    5. Now try to pair the device again





    = Troubleshooting Java Programs
    Ravidiip; Tuju


    [abstract]
    Java provides a range of information to resolve problems with application programs or the runtime environment, in particular stack traces.  These should be attached to a bug report.


    [IMPORTANT]
    ====
    This page was taken from the previous Fedora Wiki documentation.

    It has been cleaned up for publishing here on the Fedora Docs Portal, but it has not yet been reviewed for technical accuracy.

    It is probably

    \&#42; Containing formatting issues
    \&#42; Out-of-date
    \&#42; In need of other love

    Reviews for technical accuracy are greatly appreciated. If you want to help, see the https://pagure.io/fedora-docs/quick-docs/blob/master/f/README.md[README file] in the source repository for instructions.

    Pull requests accepted at https://pagure.io/fedora-docs/quick-docs

    Once you've fixed this page, remove this notice.
    ====


    This page is an appendix to the bugs xref:bugzilla-providing-a-stacktrace.adoc[Providing a Stack Trace] page. The situation for getting stack traces from Java software is slightly more complicated than with most other Fedora Project software, because of the two kinds of stack traces (Java and native).

    == The Two Kinds of Java Stack Traces

    Stack traces produced by libgcj (i.e. produced by the virtual machine as it runs) cover all parts of the program and libraries written in Java, and all JNI and CNI methods as well - but _not_ non-Java code called _from_ JNI or CNI methods. Also, unfortunately, they do not typically provide source code line numbers - even if full debugging information is available. However, the good news is, libgcj stack traces will provide more information in gcc 4.1 - which it is hoped will go into Rawhide in time for inclusion in Fedora Core 5.

    Stack traces produced by gdb - which, by convention, are called 'backtraces' - cover all native code (whether that is C code, or Java code compiled to machine code). However, for interpreted code, they only show calls to the interpreter, but not _what_ is being interpreted.

    Thus, neither Java stack traces nor gdb backtraces are suitable for all situations. Sometimes it will be necessary to examine Java stack traces, sometimes gdb backtraces, and sometimes both.

    == Obtaining a Java stack trace from a Java program

    Sometimes, Java programs will print out Java stack traces when they crash or fail in some way, either to the terminal window from which they are run, or to a log file.

    If you get a stack trace, and if you get one or more 'Caused by:' clauses, please remember that the \&#42;last\&#42; 'Caused By' clause is the most important. \&#42;\&#42;Please always post _at least_ the last 'Caused By' clause (if any) when reporting a problem\&#42;\&#42;.

    === Application-specific details:

    ==== Eclipse

    If you can get into Eclipse, you can view the error log by going to the \&#96;Window\&#96; menu and then \&#96;Show View -\&gt; Other -\&gt; PDE Runtime -\&gt; Error Log\&#96;. Double-click on an error to get a popup dialog with a stack trace, which can be copied-and-pasted directly into a bug report.

    If Eclipse fails to start, run it with \&#96;eclipse -consolelog\&#96; to output the log to the console. If that doesn't produce anything useful, try \&#96;eclipse -consolelog -debug\&#96; .

    ==== Tomcat

    Examine all the files in \&#96;/var/log/tomcat5\&lt;/\&#96; and any webapp-specific log files that you have configured.

    === When you cannot obtain a Java stack trace

    If a Java program simply fails without printing a stack trace - not on the terminal window or even in a log file anywhere - then: If it is natively-compiled, or if it says \&#96;Aborted\&#96; or \&#96;Segmentation fault\&#96; or \&#96;Illegal instruction\&#96; immediately before it quits, try to obtain a gdb backtrace as described in the next section. Otherwise, a gdb backtrace will probably not be helpful, so just file a bug report without a stack trace.

    Future work: In the upcoming gcc 4.1, a \&#96;SIGQUIT\&#96; handler is planned which will enable the generation of Java stack traces on demand by the user. (This cannot be used for crashes which terminate the program, however - it can only be used for certain failures which leave the program running.)

    == Obtaining a gdb backtrace from a Java program

    First you will need to read the StackTraces page, up to the point of starting gdb.

    Because libgcj uses several signals internally, you need to tell gdb first of all to ignore some of them, by typing or pasting the following commands into gdb:

    [source,]
    ----
    handle SIGHUP nostop print
    handle SIGPWR nostop noprint
    handle SIGXCPU nostop noprint
    handle SIG32 nostop noprint
    handle SIG33 nostop noprint
    ----

    gdb can also be quite slow at loading the debugging information for various libraries (which can drastically affect the startup time of programs), so, to get nice friendly progress indications, you might want to also specify:

    [source,]
    set verbose on

    Now type \&#96;run\&#96; or \&#96;r\&#96; for short and continue reading the instructions on the StackTraces page.

    === Ignoring 'Null Pointer Exceptions' of the harmless variety in gdb

    Sometimes code generates one or more \&#96;Null Pointer Exceptions\&#96; which are in fact harmless - or at least, irrelevant to the bug you are trying to trace. (Not all \&#96;Null Pointer Exceptions\&#96; are harmless or irrelevant, but some are.) Because gcj uses SIGSEGV to detect \&#96;Null Pointer Exceptions\&#96;, you can also specify

    [source,]
    handle SIGSEGV nostop noprint

    to tell gdb to ignore SIGSEGVs, or

    [source,]
    handle SIGSEGV nostop print

    to tell gdb to inform you of SIGSEGVs, but otherwise ignore them.



    = Troubleshooting Mozilla Products
    Xhorak; Stransky; Coremodule


    [abstract]
    This article helps affected users in reporting of Firefox and Thunderbird bugs and ease package maintainers fixing them.


    [IMPORTANT]
    ====
    This page was taken from the previous Fedora Wiki documentation.

    It has been cleaned up for publishing here on the Fedora Docs Portal, but it has not yet been reviewed for technical accuracy.

    It is probably

    \&#42; Containing formatting issues
    \&#42; Out-of-date
    \&#42; In need of other love

    Reviews for technical accuracy are greatly appreciated. If you want to help, see the https://pagure.io/fedora-docs/quick-docs/blob/master/f/README.md[README file] in the source repository for instructions.

    Pull requests accepted at https://pagure.io/fedora-docs/quick-docs

    Once you've fixed this page, remove this notice.
    ====


    == Using Mozilla crash reporter

    Application crash can occur during runtime. Application window simply disappear and bug report dialog will show up. By accepting this dialog crash will be reported to Mozilla crashstat servers. To view and submit the crash info please do:

    \&#42; Open https://support.mozilla.org/en-US/kb/mozillacrashreporter[Mozilla Crash Reporter]page
    \&#42; If there is any crash report, submit them (the 'Submit All' button).
    \&#42; Paste all crash ID to bugreport.

    == Using local debugging

    === Installing debug info packages

    Debug info packages which contains source files are required to create meaningful bug report (unless you use Mozilla crash reporter). To install them you need to execute following command as root:

    [source,]
    dnf debuginfo-install firefox

    for Firefox,
    [source,]
    dnf debuginfo-install thunderbird

    for Thunderbird.

    === Using coredumpctl to get backtrace
    You can use coredumpctl to get backtrace. Run on terminal:

    [source,]
    coredumpctl list

    and find Firefox crash there and get crash ID. Then launch gdb on it by

    [source,]
    coredumpctl debug ID

    you should get a gdb session and you should be able to get backtrace by

    [source,]
    thread apply all bt full

    gdb command.

    === Running application in debugger

    To run application in gnu debugger you need to run command:
    [source,]
    firefox -g -d gdb

    for Firefox,
    [source,]
    thunderbird -g -d gdb

    After debugger is started which is indicated by line:
    [source,]
    (gdb)

    To run program use command:
    [source,]
    run

    [id=optaincrashstacktrace]
    === Obtain crash stack trace
    Then bring application to crash. This should be indicated by (gdb) prompt. Type:
    [source,]
    ----
    set logging on crash_bt.log
    thread apply all bt full
    print DumpJSStack()
    set logging off
    ----
    to store stack and Javascript trace into _crash_bt.log_ file. Don't forget to attach this file to bug report.

    == Application freeze

    If you are able to reproduce freeze you can follow _[[Application crash,(no link provided)]]_ steps. There is only one difference in \&lt;\&lt;obtaincrashstacktrace,Obtain crash stack trace\&gt;\&gt; section where \&#96;(gdb)\&#96; prompt is missing. To get prompt you have to press Ctrl-C.

    === Getting Mozilla crash report from running application
    You can kill running application by kill signal and then obtain and submit Mozilla crash stats.

    To terminate all firefox instances run on terminal:

    [source,]
    kill -s 11 ${pid_of_firefox}

    This should terminate all Firefox instances and produce Mozilla crash report dialog. In next Firefox run you should see crash ID at \&#96;about:crashes\&#96; page. Please submit the crash to Mozilla and paste crash ID to bugreport.

    === Attach debugger to running application
    Before you can attach to running application you need to have [[\&#35;Installing debug info packages|debug symbols installed]].

    When the freeze occurs randomly and/or difficult to predict you can attach to running application when it freezes by:
    [source,bash]
    gdb firefox \&#96;ps ax|grep firefox/firefox|grep -v grep|grep -v 'contentproc'|cut -d ' ' -f3\&#96;

    for Firefox.

    [source,bash]
    gdb thunderbird \&#96;ps ax|grep thunderbird/thunderbird|grep -v grep|grep -v 'contentproc'|cut -d ' ' -f3\&#96;

    for Thunderbird.

    Then you can continue by \&lt;\&lt;obtaincrashstacktrace,Obtain crash stack trace\&gt;\&gt;.

    == Figuring out what is responsible for crash
    Some crashes and problems come from installed addons or 3rd party plugins. To determine if that's the case run application with ''-safe-mode'' parameter:
    [source,bash]
    firefox -safe-mode

    or
    [source,bash]
    thunderbird -safe-mode


    Then \&#96;Disable all add-ons\&#96; needs to be checked and \&#96;Make Changes and Restart\&#96; pressed.
    [NOTE]
    ====
    This setting disables all your add-ons and plugins until you manually re-enable them.
    ====
    // {{admon/note|Note|This setting disables all your add-ons and plugins until you manually re-enable them.}}

    If problem still persist it isn't most likely related to addons or plugins and you can just simply follow instructions in [[\&#35;Application crash]]. Otherwise continue to next section.

    == Reporting addons and plugins issues

    [IMPORTANT]
    ====
    Reenable plugins and addons|At first don't forget to _reenable all plugins and addons_ in  \&#96;Tools/Add-ons/Extensions\&#96; and \&#96;Plugins\&#96; menu and _restart application_.
    ====
    // {{admon/important|Reenable plugins and addons|At first don't forget to '''reenable all plugins and addons''' in ''Tools/Add-ons/Extensions'' and ''Plugins'' menu and '''restart application.'''}}

    For _Firefox_ set your location to \&#96;about:plugins\&#96; page. This page contains information about all installed plugins and it may help us in resolving your issue. Save it by _File/Save Page As\&#8230;_ to file and attach saved file to bug report.

    For _Thunderbird_ make screenshot of \&#96;Tools/Addons/Extensions\&#96; and \&#96;Tools/Addons/Plugins\&#96; dialogs and attach images to bugzilla.

    Attach also output of following commands:
    [source,bash]
    ----
    $ rpm -q firefox xulrunner thunderbird flash-plugin gnash google-talkplugin nspluginwrapper thunderbird-lightning thunderbird-enigmail flash-plugin
    ls -l /usr/lib64/mozilla/plugins/
    ls -l /usr/lib/mozilla/plugins/
    ls -l /usr/share/mozilla/extensions
    ----

    You may also run Firefox or Thunderbird by \&#96;strace\&#96;. This help us to track which dynamic libraries are loaded during startup. Strace usage:
    [source,bash]
    strace firefox \&amp;\&gt; strace_output

    or in case of Thunderbird:
    [source,bash]
    strace thunderbird \&amp;\&gt; strace_output

    and don't forget to attach created _strace_output_ file to bug report. If application crash or freeze stack trace is also very useful, for instructions see [[\&#35;Application crash]] section.

    == Bug report attachment in a nutshell
    To make long story short, execute following commands and attach _~/bug-report_ file to bugzilla:

    [source,bash]
    ----
    rpm -q firefox xulrunner thunderbird flash-plugin gnash google-talkplugin nspluginwrapper thunderbird-lightning thunderbird-enigmail flash-plugin \&gt; ~/bug-report
    ls -l /usr/lib64/mozilla/plugins/   \&gt;\&gt; ~/bug-report
    ls -l /usr/lib/mozilla/plugins/     \&gt;\&gt; ~/bug-report
    ls -l /usr/share/mozilla/extensions \&gt;\&gt; ~/bug-report
    ----

    For _Firefox_ go to \&#96;about:support\&#96; and \&#96;about:plugins\&#96; pages, save them and attach to bug report.

    For _Thunderbird_ make screenshot of
    \&#96;Tools/Addons/Extensions\&#96; and \&#96;Tools/Addons/Plugins\&#96;, dialogs and attach images to bugzilla.

    Continue in [[\&#35;Application crash]] if required.

    == Advanced debugging
    _TODO_

    Thanks for your time you spare to reporting bugs!


    = Troubleshooting Wayland Problems
    Kparal
    :page-aliases: debug-wayland-problems.adoc
    //:imagesdir: ./images


    [IMPORTANT]
    ====
    This page was automatically converted from Wiki.

    It has been cleaned up for publishing here on the Fedora Docs Portal, but it has not yet been reviewed for technical accuracy.

    https://fedoraproject.org/wiki/How_to_debug_Wayland_problems

    It is probably

    \&#42; Badly formatted
    \&#42; Missing graphics and tables that do not convert well from mediawiki
    \&#42; Out-of-date
    \&#42; In need of other love

    Reviews for technical accuracy are greatly appreciated. If you want to help, see the https://pagure.io/fedora-docs/quick-docs/blob/master/f/README.md[README file] in the source repository for instructions.

    Pull requests accepted at https://pagure.io/fedora-docs/quick-docs

    Once you've fixed this page, remove this notice.
    ====


    https://en.wikipedia.org/wiki/Wayland_%28display_server_protocol%29[Wayland] is intended as a simpler replacement for https://en.wikipedia.org/wiki/X_Window_System[X11]. Wayland changes the design of a Linux desktop architecture considerably. Unlike X11, there is no dedicated standalone server in Wayland. What was previously done between the app, its toolkit, the Xserver and the window manager is now shared between the app, its toolkit and the Wayland compositor which manages the compositing, input, windows management, etc. The apps and toolkits are now in charge of their own rendering and decorations (client side decorations), so any issues usually sit between the toolkit (e.g. GTK+) and the Wayland compositor (e.g. mutter).

    You can read more about Wayland on the GNOME https://wiki.gnome.org/Initiatives/Wayland[Wayland initiative] wiki page. You can read more about the current state of Wayland features on https://fedoraproject.org/wiki/Wayland_features[Wayland features] page.

    [id='identifying-wayland-problems']
    == Identifying Wayland problems

    [id='are-you-running-a-wayland-session']
    === Are you running a Wayland session?

    In \&#42;GNOME\&#42;, there's a gear button at the login screen which can be used
    to either log into a Wayland session (simply called _GNOME_, it's the
    default option), or a legacy X11 session (called _GNOME on Xorg_). If
    you have a password-less user account, you won't see the gear icon, it
    is displayed only when the password prompt appears. Use the gear button
    to determine type of session you're logging into. If you want to start
    your session in a different way, read
    https://wiki.gnome.org/Initiatives/Wayland/TryingIt[the advanced
    techniques for trying Wayland].

    image:gdm-pick-wayland.png[gdm-pick-wayland.png,title='gdm-pick-wayland.png',width=400]

    In \&#42;KDE\&#42;, there is support for running a nested Wayland session inside
    your X11 session. You'll need to install \&#96;kwin-wayland\&#96; package and then
    follow up with https://community.kde.org/KWin/Wayland[this howto]. There
    doesn't seem to be out-of-the-box support for running a full Wayland
    session at the moment.

    Other desktop environments are not currently capable of running a
    Wayland session.

    [id='identifying-the-session-type-in-runtime']
    ==== Identifying the session type in runtime



    If you want to figure out which type of session you're running right
    now, without logging out and in again, you can use several ways to
    figure it out:

    \&#42; Wayland session should have \&#96;WAYLAND_DISPLAY\&#96; variable set, X11
    session should not have it:
    +
    \&#8230;.
    $ echo $WAYLAND_DISPLAY
    wayland-0
    \&#8230;.
    \&#42; \&#96;loginctl\&#96; can give you this information. First run \&#96;loginctl\&#96; and
    find your session number (if should be an integer number, with your
    username and seat assigned). Then look at the session type (\&#96;x11\&#96; or
    \&#96;wayland\&#96;):
    +
    \&#8230;.
    $ loginctl show-session \&lt;YOUR_NUMBER\&gt; -p Type
    Type=x11
    \&#8230;.

    If you're running an X11 session, not a Wayland session, your problems
    are not related to Wayland. It's a bug either in that particular
    application, or X11 itself, see https://fedoraproject.org/wiki/How_to_debug_Xorg_problems[How to
    debug Xorg problems].

    [id='does-your-application-run-on-wayland-natively-or-uses-xwayland-x11-compatibility-layer']
    === Does your application run on Wayland natively, or uses XWayland (X11 compatibility layer)?

    It is important to know whether the problematic application is a native
    Wayland application, or runs through XWayland, which allows legacy
    applications to still run on top of Xorg server, but display in a
    Wayland session.

    There are several ways how to identify whether an application is using
    Wayland or XWayland:

    \&#42; Select the window using \&#96;xwininfo\&#96; or \&#96;xprop\&#96;. Run:
    +
    \&#8230;.
    $ xwininfo
    \&#8230;.
    +
    Your mouse pointer should change to a cross under X11, it doesn't seem
    to change under Wayland. Now click anywhere inside the app window you
    want to test. If the \&#96;xwininfo\&#96; command finishes (it should print window
    properties into the terminal), the app under test is running under
    XWayland. If nothing happens (the \&#96;xwininfo\&#96; command is still waiting
    until you select a window), the app under test is running under Wayland
    (you can close the command with \&#96;Ctrl+C\&#96;). +
    You can also use \&#96;xprop\&#96; command using the same instructions.
    \&#42; XWayland applications are listed in \&#96;xlsclients\&#96; output. Run:
    +
    \&#8230;.
    $ xlsclients
    \&#8230;.
    +
    However, this list of not always entirely reliable, some apps might be
    missing.
    \&#42; You can try to run the app while unsetting \&#96;DISPLAY\&#96; environment
    variable:
    +
    \&#8230;.
    $ DISPLAY='' command
    \&#8230;.
    +
    If the application runs OK, it should be using Wayland natively.
    \&#42; You can run the app with \&#96;WAYLAND_DEBUG=1\&#96; environment variable:
    +
    \&#8230;.
    $ WAYLAND_DEBUG=1 command
    \&#8230;.
    +
    If you see loads of output (when compared to a standard run), the app is
    using Wayland natively.
    \&#42; Under GNOME, you can determine this using
    http://blog.bodhizazen.net/linux/how-to-determine-if-an-application-is-using-wayland-or-xwayland/[integrated
    Looking Glass tool]. Hit \&#96;Alt+F2\&#96;, run:
    +
    \&#8230;.
    lg
    \&#8230;.
    +
    click on _Windows_ in the upper right corner of the tool and select
    desired window by clicking on its name. If you see \&#96;MetaWindowWayland\&#96;
    in the first line, this app is running under Wayland. If you see
    \&#96;MetaWindowX11\&#96; in the first line, this app is running under X11.

    If you have identified the problem to be in a XWayland application, try
    to reproduce the issue in a standard X11 session. If it happens as well,
    it is not related to Wayland, it's a bug either in that particular
    application, or Xorg server, see https://fedoraproject.org/wiki/How_to_debug_Xorg_problems[How to
    debug Xorg problems]. If the problem happens only under XWayland but not
    in an X11 session, it should still be reported against Xorg server (
    package), because XWayland is included in it (as
    \&#96;xorg-x11-server-Xwayland\&#96; subpackage).

    [id='identifying-problem-component]
    == Identifying problem component

    Wayland itself is a protocol and the problem is rarely in the protocol
    itself. Rather, the problem is likely to be in the app or its toolkit,
    or in the compositor.

    The most notable Wayland-ready toolkits are:

    \&#42; https://en.wikipedia.org/wiki/GTK%2B[GTK+ 3] - default apps in GNOME
    environment use almost exclusively this toolkit. Please note that apps
    using older GTK+ 2 are not Wayland-ready.
    \&#42; https://en.wikipedia.org/wiki/Qt_%28software%29[QT 5] - many apps in
    KDE environment use this toolkit. Please note that apps using older QT 4
    are not Wayland-ready.

    The most notable Wayland compositors are:

    \&#42; https://en.wikipedia.org/wiki/Wayland_%28display_server_protocol%29\&#35;Weston[Weston]
    - the reference implementation of a Wayland compositor, maintained
    directly by the Wayland project
    \&#42; https://en.wikipedia.org/wiki/Mutter_%28software%29[Mutter] -
    compositor in GNOME. If you run GNOME, it is using this compositor.
    \&#42; https://community.kde.org/KWin/Wayland[Kwin] - compositor in KDE. If
    you run KDE, it is using this compositor.


    [id='testing-under-different-compositors']
    === Testing under different compositors

    If you experience a problem with a Wayland app, it is very useful to
    know whether the problem is present under just a single compositor (in
    that case it's likely a compositor bug) or under multiple compositors
    (in that case it's likely an app/toolkit bug).

    Please run your session with the reference Weston compositor and try to
    reproduce the issue. You can either run Weston as a nested window, or as
    a full session. First, install package (you can read many useful
    information in its man page):

    \&#96;$ sudo dnf install weston\&#96;

    Then create a config file which will specify that you want to have
    XWayland support enabled in your weston sessions. Create
    \&#96;~/.config/weston.ini\&#96; with this contents:

    \&#96;[core]\&#96; +
    \&#96;xwayland=true\&#96;

    Now you can start weston either as nested window or as a full session.

    \&#42; To start a nested Weston window, run this from a terminal:
    +
    \&#8230;.
    $ weston
    \&#8230;.
    +
    A Weston window should open and you should see and a terminal icon in
    its top left corner. Use that icon to launch a terminal and from that
    you can run apps and other commands using Weston. Exit the compositor by
    simply closing the window or killing the \&#96;weston\&#96; process.
    \&#42; To start a full Weston session (not nested inside another X11 or
    Wayland session), switch to a free VT (Ctrl+Alt+Fx) and run:
    +
    \&#8230;.
    $ weston-launch
    \&#8230;.
    +
    You can exit the session by pressing Control+Alt+Backspace shortcut.

    If you can reproduce the issue with Weston, file an issue against the
    app or its toolkit (gtk+, qt, etc). Otherwise file the issue against the
    compositor your environment uses (mutter, kwin, etc). If the problem
    occurs only with XWayland apps but not native Wayland apps, report a bug
    against Xorg server.

    [id='reporting-the-issue']
    == Reporting the issue

    [id='using-up-to-date-software]
    === Using up-to-date software

    Before reporting the bug, please make sure you use the latest available
    software.
    Make sure there are no system updates waiting:

    \&#96;$ sudo dnf update\&#96;

    If there are (and the available updates look plausibly related to the
    components you're seeing issues with), please update the system and
    verify whether the issue is still present or has been fixed.

    [id='looking-for-similar-reports']
    === Looking for similar reports

    In order to avoid duplicate reports and also wasting your time debugging
    something someone has maybe already debugged, please search through the
    existing reports first. The most visible issues or concerns are listed
    in xref:troubleshooting-wayland-problems\&#35;known-issues-frequent-complaints-fundamental-changes[Known
    issues, frequent complaints, fundamental changes]. If you don't see it
    there, you need to search deeper. You can find Wayland related issues
    most likely in here:

    \&#42; [https://bugzilla.gnome.org/buglist.cgi?bug_status=UNCONFIRMED\&amp;bug_status=NEW\&amp;bug_status=ASSIGNED\&amp;bug_status=REOPENED\&amp;bug_status=NEEDINFO\&amp;component=Backend%3A%20Wayland\&amp;component=wayland\&amp;list_id=74680\&amp;order=changeddate%20DESC%2Cbug_status%2Cpriority%2Cassigned_to%2Cbug_id\&amp;product=gtk%2B\&amp;product=mutter\&amp;query_based_on=\&amp;query_format=advanced
    mutter/wayland and GTK+/wayland in GNOME Bugzilla]
    \&#42; https://bugzilla.gnome.org/showdependencytree.cgi?id=757579\&amp;hide_resolved=1[Wayland-related
    issues tracker across GNOME Bugzilla]
    \&#42; https://bugzilla.redhat.com/showdependencytree.cgi?id=WaylandRelated\&amp;hide_resolved=1[Wayland-related
    issues tracker across Red Hat Bugzilla]
    (https://bugzilla.redhat.com/showdependencytree.cgi?id=KDEWaylandRelated\&amp;hide_resolved=1[KDE
    tracker])
    \&#42; [https://bugzilla.redhat.com/buglist.cgi?classification=Fedora\&amp;component=wayland\&amp;list_id=4118943\&amp;order=changeddate%20DESC%2Cbug_status%2Cpriority%2Cassigned_to%2Cbug_id\&amp;product=Fedora\&amp;query_based_on=\&amp;query_format=advanced\&amp;resolution=---
    Wayland in Red Hat Bugzilla]
    \&#42; [https://bugs.freedesktop.org/buglist.cgi?list_id=561109\&amp;order=changeddate%20DESC%2Cbug_status%2Cpriority%2Cassigned_to%2Cbug_id\&amp;product=Wayland\&amp;query_based_on=\&amp;query_format=advanced\&amp;resolution=---
    Wayland in Freedesktop Bugzilla]
    \&#42; Google search

    [id='filing-a-bug']
    === Filing a bug

    After you've identified against which component to (most probably)
    report the issue and found no existing report of it, there are several
    places where to report it:

    \&#42; https://bugzilla.redhat.com/[Red Hat Bugzilla] - recommended for
    issues related to wayland itself, weston compositor, non-GNOME apps, KDE
    project, QT toolkit
    \&#42; https://bugzilla.gnome.org/[GNOME Bugzilla] - recommended for issues
    related to mutter compositor, GTK+ toolkit, applications under the GNOME
    project (most of default apps in Fedora Workstation)

    When reporting the issue, please make your report block our tracker, so
    that we have a good overall picture of what is broken across many
    different components. In your bug report, set \&#42;Blocks: WaylandRelated\&#42;
    or \&#42;Blocks: KDEWaylandRelated\&#42; (you might need to toggle showing
    advanced fields to see the _Blocks:_ field). That will make it block one
    of these trackers, depending where you reported the bug:

    \&#42; https://bugzilla.redhat.com/show_bug.cgi?id=1277927[Wayland Tracker in
    Red Hat Bugzilla]
    (https://bugzilla.redhat.com/show_bug.cgi?id=1298494[KDE tracker])
    \&#42; https://bugzilla.gnome.org/show_bug.cgi?id=757579[Wayland Tracker in
    GNOME Bugzilla]

    [id='information-to-include-in-your-bug-report']
    === Information to include in your bug report

    1.  System journal. Since there is no unique server like the X11 server,
    most of the important information will come from the the Wayland
    compositor and the apps. All of that should be in system journal
    nowadays. You can save a full journal since last boot like this:
    +
    \&#8230;.
    $ journalctl -ab \&gt; journal.log
    \&#8230;.
    +
    You can also edit the file and according to the timestamps remove
    everything long prior to when the issue occurred, in order to make the
    log more succinct.
    \&#42; If your system crashed or became unresponsive so that you had to
    reboot it, you can see the journal from the previous boot using
    \&#96;journalctl -a -b -1\&#96; instead.
    2.  Wayland debug output. If you can reproduce the issue, please run the
    problematic app like this:
    +
    \&#8230;.
    $ WAYLAND_DEBUG=1 command |\&amp; tee debug.out
    \&#8230;.
    +
    You should see loads of output being printed out. It will involve all
    communication between the app and the compositor.
    3.  Information whether the same problem occurs when you run the app
    using XWayland instead of Wayland. For GTK+ 3 apps, you can force a
    native Wayland app to run using XWayland like this:
    +
    \&#8230;.
    $ GDK_BACKEND=x11 command
    \&#8230;.
    +
    Vice versa, you can also force a XWayland app to run using Wayland (in
    case it has just experimental support):
    +
    \&#8230;.
    $ GDK_BACKEND=wayland command
    \&#8230;.
    +
    QT 5 apps run with XWayland by default. You can force Wayland backend:
    +
    \&#8230;.
    $ QT_QPA_PLATFORM=wayland-egl command
    \&#8230;.
    +
    All of this applies to just GTK+ 3 and QT 5 apps.
    4.  Hardware description is useful for some hardware-related bugs:
    +
    \&#8230;.
    $ lspci -nn \&gt; lspci.out
    \&#8230;.
    5.  Package versions. You can collect the list and versions of all your
    packages installed using:
    +
    \&#8230;.
    $ rpm -qa | sort \&gt; packages.out
    \&#8230;.
    6.  The
    link:Bugs_and_feature_requests\&#35;Things_Every_Bug_Should_Have[usual
    information] that every bug report should have.

    [id='debugging-gnome-shell']
    === Debugging gnome-shell

    If gnome-shell gets stuck and unresponsive, it's very helpful to obtain
    a backtrace from its process and attach it to the report. If this
    happens, switch to a different VT if possible (\&#96;Ctrl+Alt+F3\&#96; through
    \&#96;F7\&#96;), or log in using ssh. First install debug symbols:

    \&#8230;.
    $ sudo dnf debuginfo-install \&#96;rpm -q gnome-shell\&#96;
    \&#8230;.

    Then attach gdb debugger to your gnome-shell process:

    \&#8230;.
    $ gdb -p \&#96;pgrep -U $(id -un) -x gnome-shell\&#96;
    \&#8230;
    (gdb) set logging on
    (gdb) thread apply all backtrace full
    \&#8230; press Enter until the whole backtrace is displayed \&#8230;
    (gdb) quit
    \&#8230;.

    You should have the backtrace saved in \&#96;gdb.txt\&#96; file.

    [id='debugging-mutter']
    === Debugging mutter

    You can debug mutter (used in gnome-shell) by setting its
    https://developer.gnome.org/meta/stable/running-mutter.html[environment
    variables]. These need to be set prior to run gnome-shell, so if you
    want to log into GNOME from GDM, you need to create a wrapper script
    called from a desktop file in \&#96;/usr/share/wayland-sessions\&#96;.

    \&#42;FIXME: Putting the wrapper script and desktop file here would be
    helpful.\&#42;

    [id='known-issues-frequent-complaints-fundamental-changes']
    == Known issues, frequent complaints, fundamental changes

    Here we will list high-profile issues which are known to be broken, not
    yet implemented, or intentionally behaving differently from regular X11
    apps. Also please look at https://fedoraproject.org/wiki/Wayland_features[Wayland features] which
    lists all current missing or in-progress features and their details.

    To see all known issues, look at Bugzilla reports as mentioned in xref:troubleshooting-wayland-problems/\&#35;looking-for-similar-reports[Looking for similar reports].

    [id='graphical-applications-cant-be-run-as-root-from-terminal']
    === Graphical applications can't be run as root from terminal

    It is not possible to start graphical apps under the root account from
    terminal when using \&#96;su\&#96; or \&#96;sudo\&#96;. Apps which use polkit to request
    administrator permissions for just certain operations and only when
    needed are not affected (they are not started as root right away). The
    discussion is ongoing about the best approach to take, see
    https://bugzilla.redhat.com/show_bug.cgi?id=1274451[bug 1274451] and
    https://lists.fedoraproject.org/archives/list/devel%40lists.fedoraproject.org/thread/A6VXI4WAGSIIWGOTAVNDBVS4VFYXITHA/\&#35;2YU2RBYCXQSCGHGP772W5LRXUMTSINHA['On
    running gui applications as root' thread in fedora-devel mailing list].

    [id='many-well-known-x11-utilities-dont-work']
    === Many well-known X11 utilities don't work

    Power users are familiar with a large range of X11-related utilities,
    like \&#96;xkill\&#96;, \&#96;xrandr\&#96;, \&#96;xdotool\&#96;, \&#96;xsel\&#96;. These tools won't work under
    Wayland session, or will only work with XWayland applications but not
    Wayland applications. Some tools might have a replacement which allows
    to perform similar tasks.

    \&#42;FIXME: add some Wayland-ready replacements for popular X11 tools\&#42;

    [id='games-and-other-apps-cant-change-monitor-resolution']
    === Games and other apps can't change monitor resolution

    It is no longer possible for an app to change monitor resolution.
    Usually this was done by games to increase performance. Wayland-based
    games will use a different approach - scaling its output. But for X11
    games (running through XWayland) this solution is not available. This
    results in a number of different types of behavior, based on how the
    game is written - the game might be fixed in the desktop resolution, or
    rendered as a small centered image with black bars around it, or crash
    on startup, or something different. See
    https://bugzilla.redhat.com/show_bug.cgi?id=1289714[bug 1289714].

    For some games, a possible workaround is to manually set custom monitor
    resolution before running the game, if you really need it. It will not
    help always, though.

    [id='screen-capture-is-not-available-with-usual-apps']
    === Screen capture is not available with usual apps

    One of the features of Wayland is its security design, which helps to
    guard the user against malicious apps. Apps can no longer see everything
    on the screen and spy on you. But that also means you cannot run a
    common application (like https://src.fedoraproject.org/rpms/shutter[shutter]
    or https://src.fedoraproject.org/rpms/gtk-recordmydesktop[gtk-recordmydesktop])
    and use it to make a screenshot or a screencast of your desktop - it will
    see only its own window, but nothing else (or it might crash right away).
    System (trusted) apps need to be used to perform these actions.

    In GNOME, you can use Screenshot tool (available in overview or as
    \&#96;Printscreen\&#96; hotkey or as \&#96;gnome-screenshot\&#96; command) to capture a
    screenshot of the full desktop or a particular window. You can press
    \&#96;Ctrl+Alt+Shift+R\&#96; keyboard shortcut to start video recording of the
    whole desktop (stop it by pressing the same shortcut again, there's an
    indicator in the upper right corner, or it stops automatically after 30
    seconds by default) and find the screencast in \&#96;~/Videos\&#96;. For
    screencast, you can also use
    https://extensions.gnome.org/extension/690/easyscreencast/[EasyScreenCast]
    gnome-shell extension.

    [id='mouse-pointer-is-laggingstuttering-under-load']
    === Mouse pointer is lagging/stuttering under load

    If your computer is under load, your mouse pointer movement might stop
    being fluent, but start lagging (get stuck in a place for a short time,
    then jump to a different place instantly). This is probably more
    noticeable on slow systems/systems with fewer CPU cores. See
    https://bugzilla.gnome.org/show_bug.cgi?id=745032[bug 745032].

    [id='keyboard-events-are-sometimes-quickly-repeated']
    === Keyboard events are sometimes quickly repeated

    There is a rare issue when you press a key to type a letter and you'll
    see multiple copies of the letter typed in. See
    https://bugzilla.gnome.org/show_bug.cgi?id=757942[bug 757942] and
    https://bugzilla.gnome.org/show_bug.cgi?id=777693[bug 777693].

    [id='not-all-keys-can-be-sent-to-a-remote-desktop-or-a-virtual-machine']
    === Not all keys can be sent to a remote desktop or a virtual machine

    Some applications forward all input, including system-specific keys/shortcuts like or , to a remote system. This is mostly remote desktop viewers like _vncviewer_ or virtual machine managers like _virt-manager_ or _boxes_. Under Wayland, some of these shortcuts can't be intercepted, and therefore are used in the host system, not the
    remote/guest system. See https://bugzilla.redhat.com/show_bug.cgi?id=1285770[bug 1285770].



    = How to troubleshoot sound problems
    Hank Lee ; The Music and Audio SIG

    [abstract]
    This page covers some basic troubleshooting techniques to help narrow down the root cause of an issue. It also explains information that should be included when filing bugs related to sound.

    == Introduction

    Sound problems in Fedora Linux can stem from various factors, including audio profiles, pairing procedures, device compatibility, or user misconfiguration. Typical issues users may encounter:

    \&#42; No sound output or input
    \&#42; Only “Dummy Output” is available
    \&#42; Microphones not being detected
    \&#42; Audio devices missing after updates
    \&#42; Broken Bluetooth audio connections

    This guide provides a step-by-step approach to diagnosing and resolving these sound issues. It covers both general troubleshooting and specific fixes for input-related problems, such as missing microphones or inactive input devices.

    == Diagnosing the Problem

    \&#42; Determining if the issue is with the kernel, PipeWire, or specific applications.
    \&#42; Collecting logs and system information.

    === Check which Kernel driver is in use by PCI devices

    To display kernel drivers handling each device, use the lspci (List PCI) command with the option -k. Searching for known issues specific to driver’s name and your hardware model before reporting issues to Ask Fedora.

    [source,_console]
    ----
    $ sudo lspci -k
    ----

    New hardware drivers are updated continuously. If you see a device listed as unknown, query your PCI device ID database.

    [source,_console]
    ----
    $ sudo lspci -Q
    ----

    And update your local PCI ID database by running the command update-pciids.

    [source,_console]
    ----
    $ sudo update-pciids
    ----

    === ALSA Firmware

    The ALSA Firmware package contains firmware for various third-party sound cards.

    See which firmware is in use by running the following command.

    [source,_console]
    ----
    $ sudo dnf list alsa-firmware
    ----

    The regular ALSA Firmware will appear \&lt;alsa-firmware.noarch\&gt;.

    If the regular firmware is not on the output, install the alsa-firmware.

    [source,_console]
    ----
    $ sudo dnf install alsa-firmware
    ----

    If any other firmware is installed, put them on blocklist on configuration directory for modprobe.

    [source,_console]
    ----
    /etc/modprobe.d/\&#42;.conf
    ----

    Add the line on configuration file.

    [source,_console]
    ----
    blacklist \&lt;the module to blocklist\&gt;
    ----

    The dracut tool creates an initial image used by the kernel for preloading the block device modules. The option -f overwrite existing initramfs file.

    [source,_console]
    ----
    $ sudo dracut -f
    ----

    Reboot your computer for the change to take effect.

    [source,_console]
    ----
    $ sudo reboot
    ----

    === Hardware information

    It is always useful to include detailed information on your sound hardware when filing a sound-related bug. To produce this information, run this command:

    [source,_console]
    ----
    $ alsa-info.sh --no-upload
    ----

    It will generate a file containing detailed information about your sound hardware with the name /tmp/alsa-info.txt. Attach this file to your bug report.

    === Is it PipeWire?

    PipeWire is a media sharing server, low-level multimedia framework that aims to;

    \&#42; improve handling of audio and video under Linux

    \&#42; work for all users at all levels

    \&#42; offer support for PulseAudio, JACK (JACK Audio Connection Kit), ALSA and GStreamer-based applications

    === Visual checks on ports

    Qpwgraph is a graph manager dedicated to PipeWire.

    Visual checks on ports using Qpwgraph will help discover all the routing between applications and devices and change the routing as you need. For example, if multiple applications and devices are connected and disconnected like below,

    \&#42; Firefox: video conference application using WebRTC protocol

    \&#42; VLC: media playback

    \&#42; OBS Studio: live stream and recording

    \&#42; USB soundcards or mixers: devices

    it will be useful to learn how ports are connected to applications and devices graphically.

    Ports are directional, they can be either:

    \&#42; Source ports (output). Located at the right-most edge of a node, they generate an audio/video/midi stream.

    \&#42; Sink ports (input). Located at the left-most edge of a node, they consume an audio/video/midi stream.

    Ports also have different types:

    \&#42; Audio (default color: green)

    \&#42; Video (default color: blue)

    \&#42; PipeWire/JACK MIDI (default color: red)

    \&#42; ALSA MIDI (default color: purple)

    Ports of the same type and opposite directions can be connected.

    Check the upstream documentation for user guide link:https://gitlab.freedesktop.org/rncbc/qpwgraph/-/blob/main/docs/qpwgraph-user_manual.md[Qpwgraph User Guide].

    == Resolving Audio Input Issues

    Follow these steps to resolve most audio input issues.

    Solution steps:

    === Step 1: Reinstall PipeWire and Related Packages

    Make sure the necessary PipeWire components are installed and working correctly.

    [source,_console]
    ----
    $ sudo dnf reinstall pipewire pipewire-pulseaudio pipewire-alsa wireplumber
    ----

    Then reboot your system.

    === Step 2: Check Audio Service Status

    Ensure that the PipeWire and WirePlumber services are active.

    [source,_console]
    ----
    $ systemctl --user status pipewire
    $ systemctl --user status pipewire-pulse
    $ systemctl --user status wireplumber
    ----

    If they are not running, start and enable them:

    [source,_console]
    ----
    $ systemctl --user enable --now pipewire.socket
    $ systemctl --user enable --now pipewire-pulse.socket
    $ systemctl --user start  pipewire
    $ systemctl --user start  pipewire-pulse
    $ systemctl --user enable --now wireplumber
    ----

    === Step 3: Verify User Permissions

    Check that your user belongs to the correct groups:

    [source,_console]
    ----
    $ groups
    ----

    If \&#96;audio\&#96; is missing, add it:

    [source,_console]
    ----
    $ sudo usermod -aG audio $USER
    ----

    === Step 4: Reset configuration files

    If the audio configuration is corrupted, you can reset it by moving the old config folders:

    [source,_console]
    ----
    $ mv ~/.config/pulse ~/.config/pulse_backup
    $ mv ~/.config/pipewire ~/.config/pipewire_backup
    ----

    Then reboot your system.

    === Step 5: Check hardware

    If you're using an external microphone, try reconnecting it or testing with a different device to rule out hardware issues.

    == Diagnosing and Fixing Bluetooth Audio Problems

    Bluetooth audio issues can often be categorized into one of three categories: device detection, pairing, or missing audio profile. This section provides a structured guide to determine which of these stages the problem belongs to and how to resolve it.

    === Category 1: Device Not Detected

    \&#42;Symptoms\&#42;

    \&#42; Bluetooth audio device does not appear in \&#96;bluetoothctl\&#96; or GNOME Settings.
    \&#42; No MAC address shown even while device is in pairing mode.

    This usually means the Linux Bluetooth stack never received an advertisement packet from the device. Common causes include:

    \&#42; The Bluetooth adapter (HCI device) is not fully initialized or supported.
    \&#42; The device uses a newer Bluetooth version or chipset that requires kernel or firmware support not yet available.

    \&#42;Check\&#42;

    Use \&#96;btmon\&#96; to monitor Bluetooth traffic and look for \&#42;LE Advertising Report\&#42; event. When a Bluetooth device is detected properly, you will see lines like:

    [source,_console]
    ----
    $ sudo btmon
    Bluetooth monitor ver 5.81
    LE Advertising Report (0x02)
    Num reports: 1
    Event type: Connectable undirected - ADV_IND (0x00)
    Address type: Random (0x01)
    Address: C4:9D:61:BC:E7:09 (Static)
    Data length: 25
    16-bit Service UUIDs (partial): 1 entry
    Unknown (0xfd2a)
    Company: Sony Corporation (301)
    Data[17]: 13000130ed000000004001fffd1c91351c
    RSSI: -40 dBm (0xd8)
    ----

    \&#42; LE Advertising Report indicates the device is actively broadcasting (advertising).

    \&#42; Address is the MAC address of the detected device.

    \&#42; RSSI: Signal strength; a negative value of -40 dBm, means the device is nearby.

    As a next step, run the \&#96;bluetoothctl show\&#96; command to display the current status and configuration of the Bluetooth adapter. It provides information such as adapter name, power status (on/off), discoverability (whether other devices can see it), and pairability.

    [source,_console]
    ----
    $ bluetoothctl show
    Controller A0:C5:89:3B:26:52 (public)
    Manufacturer: 0x0002 (2)
    Version: 0x08 (8)
    Name: hanku
    Alias: hanku
    Class: 0x007c010c (8126732)
    Powered: yes
    PowerState: on
    Discoverable: yes
    DiscoverableTimeout: 0x000000b4 (180)
    Pairable: yes
    ----

    This is useful for checking if your Bluetooth adapter is properly initialized and ready for scanning, pairing, or connecting to devices.

    NOTE: If there is a problem, the output of \&#96;bluetoothctl show\&#96; or \&#96;btmon\&#96; may reveal signs like the adapter being powered off, not discoverable, or missing from the index entirely. For example, in btmon, if no LE Advertising Report appears, it may indicate the Bluetooth device is not broadcasting or not being detected.

    To continue, start the Bluetooth control tool to list Bluetooth devices and their statuses.

    [source,_bash]
    ----
    $ bluetoothctl
    Agent registered
    [CHG] Device 40:19:20:19:69:9F RSSI: 0xffffffb9 (-71)
    [CHG] Device 28:6B:B4:40:2F:87 RSSI: 0xffffffbd (-67)
    [CHG] Device 28:6B:B4:4C:82:E5 RSSI: 0xffffffb9 (-71)
    [WF-C710N]\&gt; scan on
    SetDiscoveryFilter success
    Discovery started
    [DEL] Device C4:9D:61:BC:E7:09 LE_WF-C710N
    [NEW] Device C4:9D:61:BC:E7:09 LE_WF-C710N
    [WF-C710N]\&gt;
    ----

    Here's a summary of what's happening in your bluetoothctl session:

    \&#42; Agent registered: A Bluetooth agent (for pairing/authentication) has been successfully registered.

    \&#42; [CHG] Device \&#8230; RSSI: 0xffffffb9 (-71): RSSI (signal strength) for a known device has changed. The value 0xffffffb9 is just a signed hex representation of -71 dBm — a moderate signal.

    \&#42; [WF-C710N]\&gt; scan on
    → You've started device discovery (scanning). WF-C710N is the device name, typically set by the manufacturer.

    \&#42; SetDiscoveryFilter success
    → Any filters for discovery (For example, only LE devices) were successfully applied. LE means Low Energy, which is common for Bluetooth audio devices.

    \&#42; Discovery started
    → The adapter began scanning for nearby devices.

    \&#42; [DEL] Device C4:9D:61:BC:E7:09 LE_WF-C710N
    → The device was removed from the internal cache/list temporarily — possibly due to reappearance or profile update.

    \&#42; [NEW] Device C4:9D:61:BC:E7:09 LE_WF-C710N
    → The device reappeared during scanning and is now listed as newly discovered.

    NOTE: If the device never appears in scans (no MAC shown), this is often \&#42;\&#42;not solvable by user-level configuration or re-pairing\&#42;\&#42;, and may indicate hardware or firmware-level incompatibility.

    \&#42;Recommendation\&#42;

    \&#42; Test the device on other operating systems (Ubuntu LTS, Windows, macOS) to confirm functionality.
    \&#42; Search bug trackers (For example, kernel.org, Fedora Bugzilla, bluez mailing list) for known issues related to the specific device or chipset.
    \&#42; If no workaround exists, consider using another headset known to work well with Linux.

    \&#42;Comment\&#42;

    \&#42; In community forums, it's helpful to distinguish device detection issues from pairing or profile switching problems. Many Bluetooth devices work well under Linux. However, some may exhibit issues—such as failing to pair or not switching audio profiles—because of unsupported codecs. Understanding the differences between these issue types helps users know what to expect and makes it easier for contributors to improve guidance and support.

    === Category 2: Pairing Fails or Is Incomplete

    \&#42;Symptoms\&#42;

    \&#42; Device is visible but cannot be paired or consistently fails to connect
    \&#42; Authorization timeouts or connection errors

    \&#42;Check\&#42;

    \&#42; Use \&#96;bluetoothctl\&#96; for manual steps.

    [source,_console]
    ----
    $ bluetoothctl
    ----

    Example \&#96;bluetoothctl\&#96; prompt commands:
    [source,_console]
    ----
    power on
    agent on
    default-agent
    scan on
    pair \&lt;MAC\&gt;
    trust \&lt;MAC\&gt;
    connect \&lt;MAC\&gt;
    ----

    \&#42;Fix\&#42;

    \&#42; Remove device and retry pairing.

    [source,_console]
    ----
    $ bluetoothctl remove \&lt;MAC\&gt;
    ----

    \&#42; Restart Bluetooth service.

    [source,_console]
    ----
    $ sudo systemctl restart bluetooth
    ----

    For some devices, make sure to hold the pairing button until rapid blinking starts.

    === Category 3: Missing or Failing Audio Profiles

    \&#42;Symptoms\&#42;

    \&#42; The device is paired but no usable audio profile (for example, A2DP, HSP) is shown or active.
    \&#42; Only HSP/HFP is available, A2DP (Advanced Audio Distribution Profile) is missing.

    \&#42;Check\&#42;

    \&#42; Confirm PipeWire is used.

    [source,_console]
    ----
    $ pactl info | grep Server
    ----

    Example Output:

    [source,_console]
    ----
    Server String: /run/user/1000/pulse/native
    Server Protocol Version: 35
    Server Name: PulseAudio (on PipeWire 1.4.2)
    Server Version: 15.0.0
    ----

    This output shows that the system is using the PulseAudio compatibility layer on top of PipeWire. To further inspect the audio setup, the command \&#96;pactl list cards short\&#96; provides a concise summary of all audio cards recognized by PulseAudio. It’s useful for quickly identifying available audio devices without diving into detailed properties.

    [source,_console]
    ----
    $ pactl list cards short
    ----

    Example Output:

    [source,_console]
    ----
    42 alsa_card.pci-0000_00_1f.3 alsa
    1092 bluez_card.14_06_A7_04_73_78 module-bluez5-device.c
    ----

    The absence of Bluetooth-related cards (in the format bluez_card.XX_XX_XX_XX_XX_XX) in the output of the \&#96;pactl list cards short\&#96; command indicates that one or more issues may be present.

    Next, the command below filters the output of \&#96;pactl list cards\&#96; to only show lines containing either profile or name, ignoring case;

    [source,_console]
    ----
    $ pactl list cards | grep -i 'profile\|name:'
    ----

    Example Output:

    [source,_console]
    ----
    Name: alsa_card.pci-0000_00_1f.3
    api.acp.auto-profile = 'false'
    Name: bluez_card.14_06_A7_04_73_78
    bluez5.profile = 'off'
    Active Profile: a2dp-sink
    Part of profile(s): headset-head-unit-cvsd, headset-head-unit
    Part of profile(s): a2dp-sink-sbc, a2dp-sink-sbc_xq, a2dp-sink
    Part of profile(s): headset-head-unit-cvsd, headset-head-unit
    ----

    Line-by-Line Explanation:

    \&#42; Name: alsa_card.pci-0000_00_1f.3
    → This is a built-in or PCI-based audio card managed by ALSA.

    \&#42; api.acp.auto-profile = 'false'
    → ACP (Advanced Configuration Profile) is disabled for this card; it won’t automatically switch profiles.

    \&#42; Name: bluez_card.14_06_A7_04_73_78
    → This is a Bluetooth audio device, identified by its MAC address.

    \&#42; bluez5.profile = 'off'
    → In PipeWire (especially with WirePlumber), this value can be outdated or not reflect the actual active state, since profiles can be switched dynamically and not always update the stored property.

    \&#42; Active Profile: a2dp-sink
    → This indicates that the A2DP (Advanced Audio Distribution Profile) is currently active, allowing high-quality audio streaming. It also supports HSP/HFP (headset mode) and multiple SBC-based A2DP variations. This structure helps PipeWire choose or switch profiles depending on use case (for example, music vs. calls)

    NOTE: If there is no Bluetooth audio card (for example, bluez_card) present and no Bluetooth-related active profile (such as a2dp-sink or headset-head-unit), this indicates a problem in the audio system, whether PulseAudio or PipeWire.

    \&#42;Recommendation\&#42;

    \&#42; Test on a clean and latest Fedora system, preferably without having installed multiple conflicting Bluetooth/audio tools.
    \&#42; Make sure the Bluetooth audio device is in proper pairing mode—usually indicated by rapid blinking—by following the manufacturer's instructions.
    \&#42; Avoid tweaking or reinstalling PipeWire/WirePlumber based on general forum advice, unless logs show actual service failure.

    == Pipewire Debugging options

    Debugging usually starts after the bug has been identified, and works best when users are very familiar with the circumstances surrounding the bug.

    PipeWire has its own debugging options. Please see the upstream documentation link:https://gitlab.freedesktop.org/pipewire/pipewire/-/wikis/Troubleshooting\&#35;pipewire-debugging-options[PipeWire debugging].

    == Need More Help?

    If the above steps don't resolve your issue, visit the Fedora community:

    \&#42; https://discussion.fedoraproject.org/ – Ask Fedora

    Contributions and feedback help improve Fedora documentation for everyone.




    \&#42; FAQ
    = Fedora and Red Hat Enterprise Linux
    yohaan vakil;  hankuoffroad ;  mikerkelly87

    // Optional  free form useful additional information as comment


    What is the difference between Fedora and Red Hat Enterprise Linux?

    == Relationship between Fedora and RHEL

    Red Hat Enterprise Linux (RHEL) and Fedora both are open source operating systems. They are related projects, with Fedora being 'upstream' of Red Hat Enterprise Linux. Whereas Fedora is a community-supported project suitable for different kinds of users, Red Hat Enterprise Linux is enterprise business-oriented software supported via commercial subscription options.

    === Red Hat Enterprise Linux

    Red Hat Enterprise Linux is an enterprise Linux operating system. It is oriented toward enterprise and commercial users, is certified for many hardware and cloud platforms, and is supported by Red Hat via various subscription options. Compared to Fedora, Red Hat Enterprise Linux emphasizes stability and enterprise-readiness over the latest technologies or rapid releases. More information about Red Hat offerings can be found at https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux[Red Hat's web site].

    Individual software developers can access a free-of-charge subscription as part of the https://developers.redhat.com/about[Red Hat Developer Program]. Developers can use Red Hat Enterprise Linux on up to 16 physical or virtual systems for development, quality assurance, demos, or small production uses. See the Frequently Asked Questions for the https://developers.redhat.com/articles/faqs-no-cost-red-hat-enterprise-linux[No-cost Red Hat Enterprise Linux Individual Developer Subscription].

    === Fedora

    Fedora is developed by the Fedora Project and sponsored by Red Hat. It follows its own release schedule, with a new version approximately every six months. Fedora provides a modern Linux operating system utilizing many of the latest technologies. It is free for all users and supported via the Fedora community.

    To create Red Hat Enterprise Linux, some version of Fedora is forked and enters an extensive development, testing and certification process to become a new version of Red Hat Enterprise Linux.

    == History of Red Hat Enterprise Linux and Fedora

    Red Hat first offered an enterprise Linux support subscription for Red Hat Linux 6.1. It was not a separate product, but the subscription offering was branded as Red Hat 6.2E. Subsequently, Red Hat started creating a separate product with commercial service level agreements and longer lifecycle based on Red Hat Linux, and later on Fedora.

    .Red Hat Enterprise Linux and Fedora Lineage
    [options='header']
    |===
    |Release |Codename |Release Date |Based on
    |Red Hat Linux 6.2E |Zoot |2000-03-27 |Red Hat Linux 6.2

    |Red Hat Enterprise Linux 2.1 |Pensacola (AS)/ Panama (ES) |2002-03-26
    (AS) |Red Hat Linux 7.2

    |Red Hat Enterprise Linux 3 |Taroon |2003-10-22 |Red Hat Linux 9

    |Red Hat Enterprise Linux 4 |Nahant |2005-02-15 |Fedora Core 3

    |Red Hat Enterprise Linux 5 |Tikanga |2007-03-14 |Fedora Core 6

    |Red Hat Enterprise Linux 6 |Santiago |2010-11-10 |Mix of Fedora 12
    Fedora 13 and several modifications

    |Red Hat Enterprise Linux 7 |Maipo |2014-06-10 |Primarily Fedora 19 with
    several changes from 20 and later

    |Red Hat Enterprise Linux 8|Ootpa |2019-05-07 |Originally Fedora 28, later CentOS Stream 8, which was also based on Fedora 28

    |Red Hat Enterprise Linux 9|Plow |2022-05-17 |CentOS Stream 9, itself based on Fedora 34

    |Red Hat Enterprise Linux 10|Coughlan |2025-05-20 |CentOS Stream 10, itself based on Fedora 40
    |===

    == Difference between Red Hat Enterprise Linux and Fedora

    .Difference between Red Hat Enterprise Linux and Fedora
    [cols='1,3,3',options='header']
    |===
    |
    |Red Hat Enterprise Linux
    |Fedora

    |support
    |Red Hat Enterprise Linux is a commercially supported product by Red Hat and provides service level agreements that is important for enterprise customers. This support involves product assistance as well as prioritization of bug fixes, feature requests, certified hardware and software.
    |Fedora is supported by a wide community of developers and users but it is not commercially supported by Red Hat. Red Hat does http://fedoraproject.org/sponsors[sponsor] the Fedora Project.

    |releases
    |A new version of Red Hat Enterprise Linux comes out every few years and is supported for up to 10 years.
    |New Fedora releases are available about every six months and every release gets updates for about 13 months.

    |available software
    |Software in Red Hat Enterprise Linux is a subset of that available in Fedora. These are the packages enterprise customers need and are supported by Red Hat.
    |Fedora offers a wide range of software, with many thousands of packages available in the repository.

    |update policy
    |Red Hat Enterprise Linux updates are more conservative and generally focus on security and bug fixes.
    |Fedora's Updates Policy is more liberal compared to Red Hat Enterprise Linux.
    |===
