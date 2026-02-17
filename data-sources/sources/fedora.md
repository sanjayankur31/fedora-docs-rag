Release Notes for Fedora Linux rawhide

> This document provides the release notes for Fedora Linux rawhide. It
> describes major changes offered as compared to Fedora Linux 39.

:::: tip
::: title
:::

Have something that should be included in the release notes? Notice
something wrong? File an issue in the [Release Notes
repository](https://gitlab.com/fedora/docs/fedora-linux-documentation/release-notes/-/issues).
::::

:::: note
::: title
:::

Use the sidebar on the left to navigate the Release Notes as well as
other documentation for Fedora rawhide.
::::

![Fedora Logo](title_logo.svg)

Copyright 2024 Fedora Project Contributors.

The text of and illustrations in this document are licensed by Red Hat
under a Creative Commons Attribution-ShareAlike 3.0 Unported license
(\'CC-BY-SA\'). An explanation of CC-BY-SA is available at
<https://creativecommons.org/licenses/by-sa/3.0/>. The original authors
of this document, and Red Hat, designate the Fedora Project as the
\'Attribution Party\' for purposes of CC-BY-SA. In accordance with
CC-BY-SA, if you distribute this document or an adaptation of it, you
must provide the URL for the original version.

Red Hat, as the licensor of this document, waives the right to enforce,
and agrees not to assert, Section 4d of CC-BY-SA to the fullest extent
permitted by applicable law.

Red Hat, Red Hat Enterprise Linux, the Shadowman logo, JBoss,
MetaMatrix, Fedora, the Infinity Logo, and RHCE are trademarks of Red
Hat, Inc., registered in the United States and other countries.

For guidelines on the permitted uses of the Fedora trademarks, refer to
<https://fedoraproject.org/wiki/Legal:Trademark_guidelines>.

&#42;Linux&#42; ® is the registered trademark of Linus Torvalds in the
United States and other countries.

&#42;Java&#42; ® is a registered trademark of Oracle and/or its
affiliates.

&#42;XFS&#42; ® is a trademark of Silicon Graphics International Corp.
or its subsidiaries in the United States and/or other countries.

&#42;MySQL&#42; ® is a registered trademark of MySQL AB in the United
States, the European Union and other countries.

All other trademarks are the property of their respective owners.

# Welcome to Fedora {#sect-welcome_to_fedora}

The Fedora Project is a partnership of free software community members
from around the globe. The Fedora Project builds open source software
communities and produces a Linux distribution called Fedora.

The Fedora Project's mission is to lead the advancement of free and open
source software and content as a collaborative community. The three
elements of this mission are clear:

&#42; The Fedora Project always strives to lead, not follow.

&#42; The Fedora Project consistently seeks to create, improve, and
spread free/libre code and content.

&#42; The Fedora Project succeeds through shared action on the part of
many people throughout our community.

To find out more general information about Fedora, refer to the
following pages, on the Fedora Project Wiki:

&#42; [Fedora Overview](https://fedoraproject.org/wiki/Overview)

&#42; [Fedora FAQ](https://fedoraproject.org/wiki/FAQ)

&#42; [Help and Discussions](https://fedoraproject.org/wiki/Communicate)

&#42; [Participate in the Fedora
Project](https://fedoraproject.org/wiki/Join)

## Need Help? {#sect-need-help}

There are a number of places you can get assistance should you run into
problems.

If you run into a problem and would like some assistance, go to
<https://ask.fedoraproject.org>. Many answers are already there, but if
you don't find yours, you can simply post a new question. This has the
advantage that anyone else with the same problem can find the answer,
too.

You may also find assistance on the &#96;&#35;fedora&#96; channel on the
IRC network &#96;irc.libera.chat&#96;. Keep in mind that the channel is
populated by volunteers wanting to help, but folks knowledgeable about a
specific topic might not always be available.

## Want to Contribute? {#sect-providing-help}

You can help the Fedora Project community continue to improve Fedora if
you file bug reports and enhancement requests. Refer to [Bugs And
Feature Requests](https://fedoraproject.org/wiki/BugsAndFeatureRequests)
on the Fedora Wiki for more information about bug and feature reporting.
Thank you for your participation.

# Hardware Overview {#sect-hardware-overview}

Fedora rawhide provides software to suit a wide variety of applications.
The storage, memory and processing requirements vary depending on usage.
For example, a high traffic database server requires much more memory
and storage than a business desktop, which in turn has higher
requirements than a single-purpose virtual machine.

## Minimum System Configuration {#hardware_overview-specs}

The figures below are a recommended minimum for the default
installation. Your requirements may differ, and most applications will
benefit from more than the minimum resources.

&#42; 2GHz dual core processor or faster

&#42; 2GB System Memory

&#42; 15GB unallocated drive space

Users of system equipped with the minimum memory of 2GB may want to
consider Fedora Spins with less resource intense Desktop Environments

:::: note
::: title
Low memory installations
:::

Fedora rawhide can be installed and used on systems with limited
resources for some applications. Text, VNC, or kickstart installations
are advised over graphical installation for systems with very low
memory. Larger package sets require more memory during installation, so
users with less than 768MB of system memory may have better results
performing a minimal install and adding to it afterward.

For best results on systems with less than 1GB of memory, use the DVD
installation image.
::::

## Recommended System Configuration {#_recommended_system_configuration}

The figures below are recommended for the default x86_64 Workstation
installation featuring the Gnome desktop . Your requirements may differ,
depending on Desktop Environment and use case.

&#42; 2GHz quad core processor

&#42; 4GB System Memory

&#42; 20GB unallocated drive space

:::: note
::: title
Low memory installations
:::

Fedora rawhide can be installed and used on systems with limited
resources for some applications. Text, VNC, or kickstart installations
are advised over graphical installation for systems with very low
memory. Larger package sets require more memory during installation, so
users with less than 768MB of system memory may have better results
preforming a minimal install and adding to it afterward.

For best results on systems with less than 1GB of memory, use the DVD
installation image.
::::

## Display resolution {#hardware_overview-resolution}

Graphical installation of Fedora requires a minimum screen resolution of
&#42;&#42;1024x768&#42;&#42;. Owners of devices with lower resolution,
such as some netbooks, should use text or VNC installation.

Once installed, Fedora will support these lower resolution devices. The
minimum resolution requirement applies only to graphical installation.

## Graphics Hardware {#hardware_overview-graphics}

### Minimum Hardware for Accelerated Desktops {#hardware_overview-graphics-legacy_gpus}

Fedora rawhide supports most display adapters. Modern, feature-rich
desktop environments like &#42;GNOME&#42; and &#42;KDE Plasma
Workspaces&#42; use video devices to provide 3D-accelerated desktops.
Older graphics hardware may &#42;not support&#42; acceleration:

&#42; Intel prior to GMA9xx

&#42; NVIDIA prior to NV30 (GeForce FX5xxx series)

&#42; Radeon prior to R300 (Radeon 9500)

### CPU Accelerated Graphics {#hardware_overview-graphics-cpu_acceleration}

Systems with older or no graphics acceleration devices can have
accelerated desktop environments using &#42;LLVMpipe&#42; technology,
which uses the CPU to render graphics. &#42;LLVMpipe&#42; requires a
processor with &#96;SSE2&#96; extensions. The extensions supported by
your processor are listed in the &#96;flags:&#96; section of
&#96;/proc/cpuinfo&#96;

### Choosing a Desktop Environment for your hardware {#hardware_overview-graphics-desktops}

Fedora rawhide's default desktop environment, &#42;GNOME&#42;, functions
best with hardware acceleration. Alternative desktops are recommended
for users with older graphics hardware or those seeing insufficient
performance with &#42;LLVMpipe&#42;.

Desktop environments can be added to an existing installation and
selected at login. To list the available desktops, use the
\[command\]&#96;dnf environment list&#96; command:

    \&#35; dnf environment list

Install the desired environment using its ID as listed in the above
command's output:

    \&#35; dnf install @cinnamon-desktop-environment

For more information, see the &#96;dnf5-environment&#96; man page.

# Feedback {#sect-Release_Notes-Feedback}

Thank you for taking the time to provide your comments, suggestions, and
bug reports to the Fedora community; this helps improve the state of
Fedora, Linux, and free software worldwide.

## Providing Feedback on Fedora Software {#_providing_feedback_on_fedora_software}

To provide feedback on Fedora software or other system elements, please
refer to [Bugs And Feature
Requests](https://docs.fedoraproject.org/en-US/quick-docs/bugzilla-file-a-bug/).
A list of commonly reported bugs and known issues for this release is
available from [Common
Bugs](https://discussion.fedoraproject.org/tags/c/ask/common-issues/82/all/f40)
on the forums.

## Providing Feedback on Release Notes {#_providing_feedback_on_release_notes}

If you feel these release notes could be improved in any way, you can
provide your feedback directly to the beat writers. There are several
ways to provide feedback, in order of preference:

&#42; Open an issue at
<https://gitlab.com/fedora/docs/fedora-linux-documentation/release-notes/-/issues> -
&#42;This link is ONLY for feedback on the release notes
themselves.&#42; Refer to the admonition above for details.

&#42; E-mail the Release-Note mailing list at
<relnotes@fedoraproject.org>.

# Changes in Fedora rawhide For System Administrators {#_changes_in_fedora_rawhide_for_system_administrators}

# Changes in Fedora rawhide For Desktop Users {#_changes_in_fedora_rawhide_for_desktop_users}

# Changes in Fedora rawhide For Developers {#_changes_in_fedora_rawhide_for_developers}

&#42;&#42; [Common
Bugs](https://discussion.fedoraproject.org/tags/c/ask/common-issues/82/all/f40)
