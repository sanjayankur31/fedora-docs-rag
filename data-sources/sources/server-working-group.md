&#42; Goals = Product Requirements Document

:::: note
::: title
:::

Updated document as finalized at the &#42;IRC Working Group Meeting&#42;
on [June 23,
2021](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2021-06-23-16.59.html)
and approved by &#42;FESCo vote&#42; as of [July 9,
2021](https://pagure.io/Fedora-Council/tickets/issue/375). Update was
finalized at the &#42;IRC Working Group Meeting&#42; on [April 20,
2022](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2022-04-20-17.00.html).
Fesco approvement pending.
::::

This document provides an overview of what Fedora Server Edition is, the
goals and objectives, and what it is designed for. It is written from a
user's point of view to allow people to understand what the Server
Edition should do, what it is useful for, and what to expect from it in
the future.

# Fedora Server Vision {#_fedora_server_vision}

Fedora Server is a real-world incarnation of the [Fedora Project's
vision](https://docs.fedoraproject.org/en-US/project/) for
organizations, individual users, and developers to develop, deploy, and
maintain applications and services -- freely, autonomously, and under
their own control.

# Fedora Server Mission {#_fedora_server_mission}

&#42;As a user, you gain the opportunity to use the server of the future
right now.&#42;

Fedora Server provides a stable, flexible, and universally-adaptable
base for the everyday provisioning of services and applications by
organizations and individuals, based on the latest technology and is
available quickly after the upstream releases.

&#42;As a developer or system integrator, you gain an eye on the server
of the future.&#42;

Fedora Server is also a platform for developers and system integrators,
which provides an implementation of the latest server technology for
exploring and evaluating.

# Market Opportunity {#_market_opportunity}

The server operating system market is mature and yet, constantly
evolving. The technologies that are in the midst of changing computing,
such as e.g. cloud or containers, depend, at the end of the day, on
servers running on bare metal and capable of handling the requirements
of those technologies'.

Fedora Server, being a leading-edge Linux distribution, is the ideal
place for developers, system administrators and DevOps specialists to
keep up-to-date with these low-level technologies. Fedora Server
provides the opportunity to explore these features and provide a stable
place to deploy applications, both new and legacy.

Fedora Server provides a stable foundation, with balanced resource
utilization, yet delivering the latest technologies giving
administrators every day exposure to the latest tooling as soon as it is
usable.

# Why use Fedora Server? {#_why_use_fedora_server}

Fedora Server has so many genuine advantages that it is hard to list
them all. The nine most important ones are:

&#42; The twice-yearly, release cycle allows for the inclusion of the
latest versions of system and application software almost immediately.
Users and system administrators are empowered to swiftly respond to new
market options and changing or expanding customer requirements. &#42; A
sophisticated release and quality assurance process enables a high level
of reliability and stability, despite the fast release cycle. This
achieves an excellent balance between 'bleeding edge' and maturity for
use in mainstream deployments. &#42; Fedora Server includes
enterprise-grade security, resulting in carefully pre-configured
releases, offering uncompromising security without extensive
configuration work by system administrators. &#42; A great variety of
available software, all included in that release process, opens up a
wide range of possibilities for flexibility in building a server
according to the specific needs and wishes of a customer or end-user.
&#42; The latest, stable, modern system administration tools (e.g.
cockpit) noticeably reduces the burden of system administration. &#42;
Strict alignment with other Fedora editions as well as the twice-yearly
releases are associated with less disruptive upgrades -- several small
updates are easier to manage than a few big ones. &#42; The upgrade
process itself is very simple and straightforward, without requiring
re-installation. Skipping one release is also viable, in case new
capabilities are not immediately needed. All in all, Fedora is decidedly
system administrator friendly. &#42; Fedora Server ensures utmost
freedom from restrictions imposed by commercial interests or corporate
feature management and excellent backwards hardware compatibility. &#42;
Developers find an excellent development environment for the next
generation server as well as application software with the latest
software versions available.

# Server Edition Objectives {#_server_edition_objectives}

Fedora Server Edition offers a highly flexible and adoptable
multi-purpose server platform, usable at every scale.

&#42; A platform for important infrastructure tasks and basic services
(DNS, DHCP, FreeIPA, and others) &#42; A platform for various important,
dedicated server applications (file/storage server, database server,
user-developed web applications, etc.) &#42; A platform for deploying
Infrastructure-as-a-Service systems for best deployment of Fedora Cloud
images. &#42; A platform for deploying containerized applications
supporting multiple container technologies, among which the system
administrator can choose according to custom requirements. &#42; A
platform for virtual machines, as host as well as guest system,
supporting different technologies, among which the system administrator
can choose according to custom requirements. &#42; Infrastructure to
allow efficiently managing many servers as a single unit. The product
only commits to producing basic tools, but the infrastructure will allow
more advanced tools to be created. &#42; An operating platform capable
to run any combination of forementioned services all according to very
different needs of users rsp system administrators (multipurpose
feature).

Fedora Server can be used as a standalone server that runs an
application or service as well as a member of a cluster in a data
center. As a result of strict adherence to open standards, it natively
cooperates with different server technologies and implementations.

## Additional Overall Objectives {#_additional_overall_objectives}

Aside from the adoption and development of the Fedora Server platform,
we have additional goals that are fundamental in any case:

&#42; Security-minded: secure by design - extending into TPM support,
disk encryption enablement &#42; Community-driven: Intense feedback
about product direction and potential improvements. This is separate
from "bug reports" in that we hope to engage the audience and receive
detailed feedback about use cases, desired features, developing trends
in cloud management, etc. We encourage more patches and contributions
that will help improve the Server Edition, and Fedora in general.

# Primary Use Cases, User Profiles, and most important Features {#_primary_use_cases_user_profiles_and_most_important_features}

## Use Cases {#_use_cases}

The Fedora Server will need to address the following use-cases:

&#42; On premise server for small and medium-sized enterprises hosting
mail service, calendar, and branch specific (probably containerized)
software -- either single node deployment or multi-node deployment with
automatic failover &#42; Dedicated SOHO server, 'bare metal' rented from
a remote provider and under its own full control, offering various
services. Public access through VMs for security reasons. &#42; Single
node or multi-node deployment in an enterprise data center providing
up-to-date software versions according to domain specific requirements
in a stable and secure OS, capable to provide different runtime
environments -- native, VM, different container systems -- driven by
domain specific demands. &#42; Personal home server, located 'on
premise' in own flat / house and used as NAS, backup device, and for
applications such as mail repository, contact database, calendar, ebook
library, media server, etc. &#42; Development box, providing developers
with the latest software version and excellent developing tools

## User Profiles {#_user_profiles}

We will use a set of personas to describe our target users and their
respective needs. We list the typical personas by brief title and a
short list of key characteristics.

### System Administrator \'Macgyver\' {#_system_administrator_macgyver}

&#42; Administrator with limited hardware and personnel resources to
work with &#42; Requires simple automation to cope with repetitive tasks
&#42; Needs to be able to do "a lot with a little"

### DevOps Engineer/Administrator {#_devops_engineeradministrator}

&#42; Focus is on time-to-deploy and time-to-recover as opposed to
uptime &#42; Value is achieved by delivering the latest capabilities
fastest &#42; Needs to be able to deliver quickly to PaaS, SaaS and
bare-metal servers

### Application Developer {#_application_developer}

&#42; Needs a platform with API and ABI stability guarantees &#42; Focus
will be on minimizing risk when making changes &#42; Needs latest
technology in virtualization and containerization &#42; Likes a platform
similar to the workstation

### Decision Maker {#_decision_maker}

&#42; Makes purchasing decisions and directs technology choices &#42;
Interacts with upstream FOSS communities to identify potential value

### The Home Admin {#_the_home_admin}

&#42; I need a somewhat stable machine, with a graphical interface
(Cockpit) and just want to start a couple of containers and/or virtual
machines to have nextcloud running on it. &#42; I need some gitea here,
some gitlab there, some jenkins, some photoprism, minecraft, etc. Can I
build a NAS easily? &#42; I am ok with updates and reboots over night,
but it should work. It would be awesome to have mDNS and a Web UI.

### The Hyperscaler {#_the_hyperscaler}

&#42; I treat my servers as "cattle, not pets". Overall uptime is more
important than individual server uptime &#42; I want to have a reliable
platform for virtualization, core services and container. It should be
out of my way, so I can focus on scaling, monitoring, implementation
&#42; I want to automate server installation, and configurations for
hostname, timeserver, hardening, etc. In addition I want to deploy
typical services like mariadb, httpd, nginx, redis, nodejs, java, etc.
in a reproducible way. To see what the machines are doing, I need a well
documented way to manage, monitor and backup them. &#42; My Security
Team also wants me to disable unneeded services, disable legacy
protocols, enable hardening on several levels.

### The Remixer / \'Let's build upon it\' {#_the_remixer_lets_build_upon_it}

&#42; I love how Fedora works and I want to create something upon it.
&#42; I need a very well documented build process and maybe tools to
produce new install images &#42; Removing the branding should be
possible with some compiler flags or variables, so I don't need to mess
with the code itself. &#42; I have a raspberry/intel nuc/etc. and
playing a bit with new stuff.

## Most Important Features {#_most_important_features}

&#42; The user can easily deploy and configure any supported Fedora
Server application as well as rapidly re-deploy services in accordance
with their DevOps practices. (Examples range from BIND DNS, DHCP,
Database server, iSCSI target, File/Storage server, up to OpenStack
Hypervisor Node, and the like) &#42; The user can query, monitor,
configure and manage a Fedora Server and the resources consumed by
services remotely using stable and consistent public interfaces. &#42;
The user can deploy and configure Fedora Server to provide domain
infrastructure with FreeIPA and Samba Active Directory solutions. Fedora
Server can become Domain Controller in a newly established domain or
join existing domain as a Domain Controller or a Domain Member. &#42;
Users can create, manipulate and terminate large numbers of virtual
machines and containers using a stable and consistent interface. &#42;
The user is enabled to install and manage Fedora Server in a headless
mode, either directly on the command line or supported by Cockpit, a
lightweight Web GUI.

# Logistical Concerns {#_logistical_concerns}

## Delivery Mechanisms {#_delivery_mechanisms}

Fedora Server Edition generates installation resources for different
scenarios

&#42; an offline install ISO image for a full local installation &#42; a
net install ISO image for booting into an online installation &#42; a
virtual disk image to be imported into a Fedora Server Edition KVM
virtual environment &#42; a disk image for installation on supported
aarch64 single board computers (SBC)

Supported installation methods are:

&#42; Manual install without a supporting infrastructure (e.g. the very
first Linux server). &#42; Automated ("mass") install within a larger
Linux infrastructure (e.g. PXE is an option, may have LDAP/IPA).

Existing servers should be upgradable to new releases with minimal
involvement by the admin.

Users will be able to obtain these images from the Fedora Project
website and mirror networks.

## Documentation {#_documentation}

Fedora Server Edition documentation will be made available in a
dedicated section of the Fedora documentation project. For selected
topics, we strive for integration into the generic Fedora documentation.

# About this Document {#_about_this_document}

This document resulted from a broad discussion of the Fedora Server
Edition working group. Contributors include:

&#42; Alexander Bokovoy &#42; Peter Boy (editor) &#42; Davide Cavalca
&#42; Kevin Fenzi &#42; Stephen Gallagher &#42; John Himpel &#42; David
Kaufmann &#42; Jan Kuparinen &#42; Eduard Lucena &#42; Michel Salim
&#42; Stephen Smoogen &#42; Langdon White &#42; Adam Williamson

# Fedora Server Technical Specification {#_fedora_server_technical_specification}

:::::: note
::: title
:::

:::: formalpara
::: title
&#42;This is an approved document&#42;
:::

Updated version as finalized at the &#42;Server Working Group IRC
Meeting&#42; on [August 17,
2022](https://meetbot.fedoraproject.org/fedora-meeting/2022-08-17/fedora-server.2022-08-17-17.00.html)
::::
::::::

> This document aims to describe the technical characteristics and
> properties of the Fedora Server Edition in detail. This includes
> provided services, installed software, and the like. It also defines
> characteristics and features that are not yet or not fully implemented
> in the current Fedora Server Edition release.

## Preamble {#_preamble}

Fedora Server provides a stable, flexible, and universally-adaptable
base for the everyday provisioning of services and applications by
organizations and individuals, based on the latest technology and
available quickly after the upstream releases. It aims to empower users
to deploy the services they need, whether using proven mature techniques
or current technical developments, under their own control and adapted
to their own needs. For this purpose, it provides a broad spectrum of
available techniques from which users can choose completely
independently and without predetermined valuations.

## Overview {#_overview}

The specification defines implementation details, implementation
variants, and especially extensions. They constitute a detailing and
technical elaboration of the goals and principles as stated in the
[Fedora Server Product Requirements
Document](https://docs.fedoraproject.org/en-US/server-working-group/docs/product-requirements-document/).

Specifically, it covers the following topics

&#42; &#42;Core Features&#42;

\+ describes the basic features and properities. They constitute the
base system, which is installed by the (graphical) installer by default.
&#42; &#42;System Administration&#42;

\+ describes properties and capabilities of the default administration
interface &#42; &#42;Advanced Features&#42;

\+ describes additional features that are not part of the default
(graphical) installation but require subsequent administrative action
&#42; &#42;Server Roles&#42;

\+ describe various services which Fedora Server can validly and
concurrently offer to users. Additionally, these are specifically
supported by Ansible provided administratve assistance.

The features and properties specified here are the basis for the
specification of Fedora Server release criteria and release blockers.

## 1. Core Features {#_1_core_features}

This section describes the basic properties and features of the platform
and their intended use.

### 1.1 Supported Architectures and Install Media {#_1_1_supported_architectures_and_install_media}

Fedora Server will definitely run on and provide install media for
x86_64 and aarch64 servers. The project may provide install media for
additional architectures. But these are not part of standard quality
management and may be available ephemerally.

&#42; A &#42;network installation media&#42; providing a minimal package
set allowing to boot the system, connect to Internet and contact the
Fedora media server to download packages to be installed. &#42; A
&#42;local installation media&#42; providing the default package set as
well as any featured services that are meaningfully installed without a
network connection. &#42;&#42; It can additionally point at network
resources to make available an ever larger package set. &#42;&#42;
Nevertheless, this media should be friendly to regions with limited
Internet connection stability and performance. Thus, it is a trade-off
between completeness and practical download size.. &#42; A &#42;virtual
machine disk image&#42; for simplified installation of Fedora Server
Edition in a KVM virtual environment. The image reproduces the Server
Edition completely and without restrictions, as far as features are
usable in a virtual environment. &#42; A raw &#42;aarch64 disk
image&#42; for installation on a Singe Board Computer (SBC).

### 1.2 File System and Storage Organization {#_1_2_file_system_and_storage_organization}

Fedora Server gives the highest priority to maximum reliability and
security of data with a maximum of possible performance.

To achieve this goal, Fedora Server encourages strict *separation of
system and user data* and encourages to further isolate user data, e.g.
by services. Any system maintenance must be possible with the least risk
of endangering or compromising user data (e.g. by temporarly unmounting)
and an error somewhere on the local disk storage should remain as
isolated as possible and without system-wide impact.

Thus, Fedora Server Edition's *default installation*

&#42; creates the necessary standard partitions to boot the server
(BiosBoot, EFI, /boot) &#42; creates a Volume Group with one Logical
Volume of a reasonable minimal size to accomodate the root file system
and system files using *XFS* &#42; leaves the remaining space untouched
for customization by the system administrator for user data, services or
other uses. The installer must also support the following common options
&#42;&#42; enlarge the one logical volume to accomodate custom data as
well without any separation (*not recommended*) &#42;&#42; create one or
more logical volumes to accomodate custom data &#42;&#42; or even create
an additional Volume Group dedicated to custom data

The installer also provides a custom partitioning interface to
accommodate use cases beyond the scope of default partitioning.

Additionally, the installer shall provide an option to enable disk
encryption.

### 1.3 Basic service and daemon management {#_1_3_basic_service_and_daemon_management}

Systemd provides ways to control and monitor the activity and status of
system services, resources they require, and the like. All system
services must provide systemd units to be included in the Fedora Server
standard installation.

### 1.4 SELinux {#_1_4_selinux}

SELinux will be enabled in enforcing mode, using the targeted policy. It
must fully protect any installable system component and functional
application.

Fedora Server Edition must include a user-friendly mechanism for
identifying SELinux denials and find workarounds. Currently, Cockpit's
SELinux module provides this functionality.

Additionally, any Server Role we provide MUST also provide options to
appropriately modify the system's SELinux configuration (adjusting
booleans, for example).

### 1.5 Networking {#_1_5_networking}

By default, NetworkManager controls and manages all network devices and
connections. Any modifications or adjustments to the network
configuration must use the NetworkManager configuration tools or the
public NetworkManager D-BUS API.

Installation or First Boot must create a permanent configuration file
for each physical network device found, or at least a stub configuratin
file. Primarily, DHCP is to be used and enabled if available. Both must
allow the system administrator to customize the default configuration
without restriction.

### 1.6 Firewall {#_1_6_firewall}

The default method in Fedora Server is *firewalld*. It is part of the
basic initial installation and not deselectable.

The default initial configuration must provide the highest security
possible with the ability of remote administration. But it may not
interfere with the normal operation of programs installed by default.

Therefore, on a pristine default system, the only open incoming ports
are SSH and Cockpit.

Configuration of ssh allows root access only with key-based login, if at
all.

Additionally, any Server Role we provide MUST also provide options to
appropriately display and modify firewalld's configuration options.

### 1.7 Account handling {#_1_7_account_handling}

SSSD will provide the backing storage for identity management. The
Fedora Server is expected to nearly always be configured for
'centrally-managed' user information; it must be possible to configure
it to rely on a directory service for this information. Fedora Server
will provide and support the realmd project for joining FreeIPA and
Active Directory domains automatically. Interacting with other identity
sources will remain a manual configuration effort.

### 1.8 Logging {#_1_8_logging}

Fedora Server uses systemd-journald and rsyslog for system logging. It's
recommended all applications submit logs to systemd-journald.

It stores log files locally by default and also supports sending full
log data to an external server to the maximum extent possible. It uses
rsyslog for forwarding data to a central server.

### 1.9 Miscellaneous System Information {#_1_9_miscellaneous_system_information}

System locale, timezone, hostname, etc. will be managed through the
services provided by systemd for this purpose, specifically

&#42; localed: localectl &#42; timedated: timedatectl &#42; hostnamed:
hostnamectl

### 1.10 System Installer {#_1_10_system_installer}

The desired installation experience for the Fedora Server product is to
limit the pre-installation user interaction to the minimum. The storage
configuration UI does provide a single sensible default and an
alternative, fully customizable configuration UI.

Package selection will be supplementary.

Fedora Server expects to be the sole citizen on the system. Support for
coexisting with other operating systems is not a goal.

Fedora Server supports kickstart as implemented by pyKickstart and
Anaconda as the unattended installation mechanism.

## 2. System Administration {#_2_system_administration}

### 2.1 Appearance {#_2_1_appearance}

The primary system management tool is CLI using bash on a system
console. Locally, the default Fedora Server boots to a text terminal
login screen. It expects the system administrator to type the required
commands or using bash scripts or to use Ansible roles and plays.

The local login prompt must also display any appropriate information
needed to establish remote administration of the system, in particular,
Cockpit's access URL (see next paragraph).

For remote installation, ssh and sftp are installed and activated by
default. Additionally, Cockpit is installed and activated by default and
provides a Web based graphical Interface to assist remote system
administration.

The Fedora Server does *not provide a local graphical environment*. If
the administrator elects to install a desktop, they should choose and
install a display manager themselves.

### 2.2 Input Methods {#_2_2_input_methods}

The input method support for the Fedora Server console access is the
LOCALE support in the command shell.

### 2.3 Accessibility {#_2_3_accessibility}

Accessibility support on the Fedora Server will be limited to devices
supporting the vision-impaired on the console.

### 2.4 Software updates {#_2_4_software_updates}

Software updates on the Fedora Server must be possible to perform either
locally using command-line tools (dnf), remote using *ssh* or *Cockpit*,
or centrally by common management systems (e.g. *Satellite*, *Ansible*).

### 2.5 Problem reporting {#_2_5_problem_reporting}

Problems and error conditions (e.g. kernel oopses, Selinux AVCs,
application crashes, OOM, disk errors) should all be reported in the
systemd journal. Support for sending this information to a central place
(like abrt does for crashes today) is mandatory.

## 3. Advanced Features {#_3_advanced_features}

### 3.1 Virtualization {#_3_1_virtualization}

#### 3.1.1 KVM / Libvirt {#_3_1_1_kvm_libvirt}

libvirt-daemon will be used to manage virtualization capabilities.

#### 3.1.2 XEN based Virtualization {#_3_1_2_xen_based_virtualization}

XEN based Virtualisation is available in Fedora and installable with
Fedora Server. While it may work, Xen virtualization is not officially
supported on Fedora Server.

### 3.2 Containerization {#_3_2_containerization}

Fedora Server Editions does support various different container
technologies.

#### 3.2.1 Podman Application Container {#_3_2_1_podman_application_container}

Podman must be installable and usable right out of the box.

#### 3.2.2 Systemd-nspawn System- and Application Container {#_3_2_2_systemd_nspawn_system_and_application_container}

A systemd-nspawn container must be installable and usable right out of
the box.

#### 3.2.3 Libvirt LXC System Container {#_3_2_3_libvirt_lxc_system_container}

A Libvirt LXC container must be installable and usable right out of the
box.

## 4. Server Roles {#_4_server_roles}

Server Roles are a high level set of software services with additional
administrative support to smoothness integrate into Fedora Server
Edition and validated to operate concurrently and conflict-free in
Fedora Server. An example is Mail Service, that includes various system
services as postfix, dovecot and alike.

Server Roles are supposed to get developed in the Fedora 37 -- 40 time
frame.

### 4.1 Server Roles Requirements {#_4_1_server_roles_requirements}

Supported Server Services are supposed facilitate the following
functions

&#42; A mechanism to install the packages necessary to deploy the
service. &#42; A mechanism to deploy a service whose packages are
already installed on the system by providing the necessary information
and procedures to provision it. &#42; A mechanism to install optional
components of a service after deployment. &#42; A configuration
interface to modify high-level configuration options. &#42; A helper
tool (preferrable based on LVM snapshot) to perform a backup or
alternativ a list of files on the filesystem that should be included in
a backup set.

Depending on practical experience, Server Roles may additionally need a
query interface providing metadata information about the service (not
all services must implement all parts of this):

&#42; A list of system services provided by the Supported Server
Service, as well as data about whether those services are currently
running (or enabled, in the case of socket-activated services) &#42; A
list of the ports that the role operates on, as well as data about
whether those ports are currently firewalled. &#42; A mechanism to open
and close ports that the server service operates on for some or all
interfaces. &#42; If the Server Service is designed to operate on the
network, it should automatically open those ports (see Firewall) during
deployment. &#42; An interface to set processor affinity, memory limits,
etc. where sensible.

### 4.2 Server Role Administration {#_4_2_server_role_administration}

Ansible is the projected administration tool.

### 4.3 Projected Server Roles {#_4_3_projected_server_roles}

#### 4.3.1 Domain Controller {#_4_3_1_domain_controller}

The Fedora Server Domain Controller Service will be provided by the
FreeIPA project. This Server Service is a blocker for the release of
Fedora Server.

#### 4.3.2 Database Management System (DBMS) {#_4_3_2_database_management_system_dbms}

The Fedora Server Database Management Systemn is provided by the
PostgreSQL project. This Server Service is a blocker for the release of
Fedora Server.

#### 4.3.3 Local Network File Server service {#_4_3_3_local_network_file_server_service}

The Fedora Server Fileservice will be provided by the Samba project.

#### 4.3.4 WEB Server service {#_4_3_4_web_server_service}

The Fedora Server Web Server will be provided by the Apache project.

#### 4.3.5 Web Application Server service {#_4_3_5_web_application_server_service}

The Fedora Server Web Application Server service will be provided by the
Wildfly project.

#### 4.3.6 Mail Service {#_4_3_6_mail_service}

The Fedora Server Mail Service will be provided by the Postfix project
and supporting projects like Dovecot, Spamassassin, Dkim, etc.

## 5. Appendix {#_5_appendix}

### 5.1 Core Package list {#_5_1_core_package_list}

This list includes all packages the core media are shipping with the
current release. It is the *mandatory minimal list of packages* that
needs to be installed on a system at all times for it to qualify as a
*Fedora Server* install. This package lists the priority focus for QA
and bug fixing. To produce the list, issue the following command:

*TBD*

### 5.2 Authors {#_5_2_authors}

Contributors to this document include:

&#42; Stephen Gallagher (sgallagh) &#42; Peter Boy (pboy) &#42; Jason
Beard (cooltshirtguy) &#42; John Himpel (jwhimpel) &#42; Chris Murphy
(cmurf) &#42; Emmanuel Seyman (eseyman) &#42; Adam Williamson (adamw)

&#42; Members and Governance = Members Stephen Daley, Peter Boy

&#42; [Jason
Beard](https://fedoraproject.org/w/index.php?title=User:Cooltshirtguy)
(&#42;&#42;*cooltshirtguy*&#42;&#42;) &#42; [Alexander
Bokovoy](https://fedoraproject.org/wiki/User:Abbra)
(&#42;&#42;*abbra*&#42;&#42;) &#42; [Peter
Boy](https://fedoraproject.org/wiki/User:Pboy)
(&#42;&#42;*pboy*&#42;&#42;) &#42; [François
Cami](https://fedoraproject.org/wiki/User:Fcami)
(&#42;&#42;*fcami*&#42;&#42;) &#42; [Davide
Cavalca](https://fedoraproject.org/wiki/User:Dcavalca)
(&#42;&#42;*dcavalca*&#42;&#42;) &#42; [Stephen
Daley](https://fedoraproject.org/w/index.php?title=User:Mowest)
(&#42;&#42;*mowest*&#42;&#42;) &#42; [Kevin
Fenzi](https://fedoraproject.org/wiki/User:Nirik)
(&#42;&#42;*nirik*&#42;&#42;) &#42; [Stephen
Gallagher](https://fedoraproject.org/wiki/User:Sgallagh)
(&#42;&#42;*sgallagh*&#42;&#42;) &#42; [John
Himpel](https://fedoraproject.org/w/index.php?title=User:Jwhimpel)
(&#42;&#42;*jwhimpel*&#42;&#42;) &#42; [Neal
Gompa](https://fedoraproject.org/wiki/User:Ngompa)
(&#42;&#42;*ngompa*&#42;&#42;) &#42; [David
Kaufmann](https://fedoraproject.org/wiki/User:Astra)
(&#42;&#42;*astra*&#42;&#42;) &#42; [Jan
Kuparinen](https://fedoraproject.org/wiki/User:Copperi)
(&#42;&#42;*copperi*&#42;&#42;) &#42; [Eduard
Lucena](https://fedoraproject.org/wiki/User:X3mboy)
(&#42;&#42;*x3mboy*&#42;&#42;) &#42; [Michel Alexandre
Salim](https://fedoraproject.org/wiki/User:Salimma)
(&#42;&#42;*salimma*&#42;&#42;) &#42; [Emmanuel
Seyman](https://fedoraproject.org/wiki/User:Eseyman)
(&#42;&#42;*eseyman*&#42;&#42;) &#42; [Adam
Williamson](https://fedoraproject.org/wiki/User:Adamw)
(&#42;&#42;*adamw*&#42;&#42;) &#42; [Langdon
White](https://fedoraproject.org/wiki/User:Langdon)
(&#42;&#42;*langdon*&#42;&#42;)

## Meetings {#_meetings}

&#42; The Server working group meets twice-monthly every 1st and 3rd
Wednesday at 17:00 UTC in &#35;fedora-meeting on irc.libera.chat. &#42;
ical: <https://calendar.fedoraproject.org/server/> (prefer this source;
the wiki sometimes gets out of date, but we keep that meeting correct to
reserve the meeting channel).

## Server Working Group Resources {#_server_working_group_resources}

&#42; Mailing list: <server@lists.fedoraproject.org> &#42; IRC:
&#35;fedora-server on irc.libera.chat &#42; Blog:
<http://fedoramagazine.org/> &#42; Tickets: pagure.io/fedora-server

# Federa Server WG Governance Charter {#_federa_server_wg_governance_charter}

Stephen Daley; Peter Boy :page-authors: {author}, {author_2}

> It was originally approved by the Server Working Group on November 5,
> 2013, and by FESCo on November 6, 2013, The latest version was
> approved September 12, 2017.

This document describes the governing structure for the Fedora Server
WG.

## Membership {#_membership}

The Fedora Server Working Group has a variable number of members. This
group is primarily an organizational team; they exist solely to
establish quorum during voting meetings.

Any WG member may voluntarily exit their chair at any time. New members
may be added to the Working Group by being nominated by an existing
member, then getting a +1 vote and zero -1 votes from three existing
members within a two-week period. After that window is up, the person is
added to the group.

The current composition of the Server Working Group can usually be found
at the Server landing page.

## Making Decisions {#_making_decisions}

Because Fedora is a global project, members of the working group may be
distributed across multiple timezones. It may be possible to have
real-time IRC meetings or Google+ hangouts, but in general we will
conduct business on the mailing list or announce either IRC meetings or
Google+ hangout events in advance should they take place.

The Server Working Group strives to work on consensus and only vote on
things where it's clear people aren't going to be convinced to agree.
Many of our decisions can be made through \'lazy consensus.\' Under this
model, an intended action is announced on the mailing list, discussed,
and if there is no controversy or dissenting views with a few days,
simply done.

For bigger issues, they must be discussed and voted on in a public IRC
meeting. Public IRC meetings are generally held most weeks on Tuesdays
at 4:00pm Eastern US time in
[&#35;fedora-meeting](https://web.libera.chat/?channels=&#35;fedora-meeting)
on Libera. For an IRC meeting to be held, at least three Working Group
members must be present. Votes are accepted by all participants in the
meeting (not just those of Working Group members), so the community is
highly encouraged to join. In the case where an interested party can not
make it to a meeting, they can pre-vote via the mailing list.

# Communicating and Meeting {#_communicating_and_meeting}

Peter Boy, Stephen Daley :page-authors: {author}

:::: note
::: title
:::

&#42;&#42;Work in Progress&#42;&#42; Status: Migrating from WIKI
::::

The Fedora Server Edition Working Group uses various resources

&#42; Mailing list: <server@lists.fedoraproject.org> &#42; IRC:
&#35;fedora-server on irc.libera.chat &#42; Blog:
<http://fedoramagazine.org/> &#42; Tickets:
<https://pagure.io/fedora-server>

## Meetings {#_meetings_2}

&#42; The Server working group meets twice-monthly &#42;every 1st and
3rd Wednesday at 17:00 UTC&#42; in &#35;fedora-meeting on
irc.libera.chat. Please, check your local time using e.g. &#96;date -d
\'2021-11-17 17:00UTC\'&#96; &#42; Each meeting is announced in the
Fedora Project Calendar: <https://calendar.fedoraproject.org/server/>
&#42; The agenda is announced on the server mailing list
<server@lists.fedoraproject.org> and available from the ticket system at
<https://pagure.io/fedora-server/report/Meeting> &#42; If there is no
agenda, the meeting will be cancelled and the organisator /chair will
send out a cancellation notice to the mailing list. &#42; During
meetings, silence indicates consent. If people disagree, then that will
bring it to a vote. &#42; In the case where a voting member can not make
a meeting where a vote is scheduled to happen, they can either pre-vote
via the mailing list or abstain-by-default. &#42; After meetings,
meeting minutes will be sent to the [server mailing
list](https://lists.fedoraproject.org/mailman/listinfo/server).

# Meeting Minutes 2026 {#_meeting_minutes_2026}

Stephen Daley; Peter Boy :page-authors: {author}, {author_2}
:page-aliases: wg-minutes-current.adoc

Wednesday, January 28, 2026

:   Because of lacking out quorum we had a open discussion about various
    topics

&#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

\+ (This summary is AI generated and edited)

&#42;&#42; &#42;Flock Conference Submission&#42;

&#42;&#42;&#42; We discussed submitting a proposal for the upcoming
Flock conference, suggesting a Birds of a Feather (BoF) session, a talk,
or both. &#42;&#42;&#42; BoF sessions at Flock are planned for \'Day 0\'
and will not be officially recorded or streamed, which is acceptable to
the group.

&#42;&#42; &#42;Working Plan Progress&#42;

&#42;&#42;&#42; Progress on creating topics for the working plan in the
repository has been slow due to time constraints. &#42;&#42;&#42; pboy
is evaluating the \'backup / rescue\' topic and notes it seems to be a
long-term project.

&#42;&#42; &#42;Next Release Testing&#42;

&#42;&#42;&#42; Testing for the next release (Fedora 44) is urgent as
the branch date is the following week (2026-02-03). &#42;&#42;&#42; The
KVM and aarch64 Server images are flawed, specifically with the wrong
file type on the root partition.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2026-01-28/fedora-server.2026-01-28-18.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2026-01-28/fedora-server.2026-01-28-18.00.log.html)

&#42; *&#42;&#42;Actions summary&#42;&#42;* . pboy &amp; eseyman:
Brainstorm a Flock submission while at FOSDEM. . pboy: Create the
homeserver topic in the repository. . eseyman: Create the entry for the
netboot / install topic in the repository. . korora: Add to the netboot
/ install topic once it is created. . korora: Test the flawed KVM
virtual machine image for the upcoming release.

Wednesday, January 21, 2026

:   

&#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Announcements&#42;

\+ Several members, including pboy and eseyman, will will be attending
FOSDEM. A Fedora/Fedora Docs meeting is planned for the Friday evening
of the event.

&#42;&#42; &#42;Our program and working plan for the upcomming year&#42;

\+ We decided on four main projects for the upcoming year:

&#42;&#42;&#42; Home server spin &#42;&#42;&#42; Backup
documentation/tooling &#42;&#42;&#42; Net-boot (PXE) documentation and
Ansible support &#42;&#42;&#42; Ansible/NFS projects

&#42;&#42; &#42;Contribution to Flock 2026&#42;

\+ A possible relevant topic is the home server spin-off. But we need
one or two professional usage topics, too.Details to be discussed
further.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2026-01-21/fedora-server.2026-01-21-18.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2026-01-21/fedora-server.2026-01-21-18.00.log.html)

&#42; *&#42;&#42;Actions summary&#42;&#42;* . pboy will create a project
entry on Forge for each project planned for the coming year

Wednesday, January 07, 2026

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Status migration to forge.fedoraproject.org&#42;

\+ All work has been completed. Ticket 173 closed.

&#42;&#42; &#42;Restructuring the Server User Documentation&#42;

\+ The stg branch has been removed from the public Server Documentation.
The repository no longer contains any relevant text.

\+ *AGREED*: The stg branch can now finally be removed.

&#42;&#42; &#42;Our program and working plan for the upcomming year&#42;

\+ We finally agreed to create a home server/home lab spin-off. Other
new projects include pxe boot support and backup/rescue system. Details
are still being discussed.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2026-01-07/fedora-server.2026-01-07-18.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2026-01-07/fedora-server.2026-01-07-18.00.log.html)

# Meeting Minutes 2025 {#_meeting_minutes_2025}

Stephen Daley; Peter Boy :page-authors: {author}, {author_2}

Wednesday, December 17, 2025

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Restructuring the Server User Documentation&#42;

\+ *AGREED*: We will finally remove the stg branch from our Docs repo.

&#42;&#42; &#42;Pending reviews of our documentation&#42;

\+ *AGREED*: The PostgreSQL update has been positively reviewed and can
be released.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-12-17/fedora-server.2025-12-17-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-12-17/fedora-server.2025-12-17-18.00.log.html)

Wednesday, December 10, 2025

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Status migration to forge.fedoraproject.org&#42;

\+ We had some discussion about organising all tickets in on ticket repo
instead spreading them over the various repos.

\+ *AGREED*: We keep all tickets (and projects), even very specific
detailed tickets for areas of the other repo, together in one repo.

&#42;&#42; &#42;Restructuring the Server User Documentation&#42;

\+ Now that we have an easily accessible, albeit still somewhat rough
preview in the new forge, we no longer want to stick with the cumbersome
stg branch.

\+ *AGREED*: We drop stg branch in favour of the AsciiDoc preview in
forge.

\+ pboy will adjust our contributors guides and remove the stg branch
from the repo as soon as all outstandig discussions are closed.,

&#42;&#42; &#42;Our program and working plan for the upcomming year&#42;

\+ We've put together a preliminary list.

\+ <https://forge.fedoraproject.org/server/tickets/issues/178>

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-12-10/fedora-server.2025-12-10-18.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-12-10/fedora-server.2025-12-10-18.00.log.html)

Wednesday, November 26, 2025

:   

&#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Status migration to forge.fedoraproject.org&#42;

\+ *AGREED*: We move the old wiki to the wiki inside
forge.fedoraproject.org

&#42;&#42; &#42;Walk through longterm open issues and PRs&#42;

\+ *AGREED*: We close issue &#35;55 about default editor as resolved. It
is part of post-installation tasks.

&#42; HTML Minutes: [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-11-26/fedora-server.2025-11-26-18.00.html)
&#42; HTML Log: [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-11-26/fedora-server.2025-11-26-18.00.log.html)
&#42; *&#42;&#42;Actions summary&#42;&#42;* . DONE: pboy will merge the
NFS Doc adduser fix. . DONE: Ticket 134: We include the ideas to our
wiki idea collections for documentation and close the ticket. . DONE:
Ticket 112: We close Ticket 112 (LLMNR) as fixed by documentation. .
DONE: Aggraxis will dig into the LLMNR (ticket &#35;114) and make a
proposal.

Wednesday, November 19, 2025

:   

&#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Server Docs: How to proceed with NFS doc&#42;

\+ *ACTION*: pboy will merge the NFS Doc adduser fix.

&#42;&#42; &#42;Server Docs Contribution work with new Fedora forge&#42;

\+ *AGREED*: The overview page \'User Documentation Maintenance\' has
been accepted.

&#42;&#42; &#42;Walk through longterm open issues and PRs&#42;

\+ *AGREED*: Ticket 134: We include the ideas to our wiki idea
collections for documentation and close the ticket.

\+ *AGREED*: Ticket 132: pboy will write a comment to catch the SELinux
error. If there is no reaction, we'll close the ticket.

\+ *AGREED*: Ticket 112: We close Ticket 112 (LLMNR) as fixed by
documentation.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-11-19/fedora-server.2025-11-19-18.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-11-19/fedora-server.2025-11-19-18.00.log.html)
&#42; *&#42;&#42;Actions summary&#42;&#42;* . pboy will merge the NFS
Doc adduser fix.

Wednesday, November 12, 2025

:   

&#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Server Docs Contribution work with new Fedora forge&#42;

\+ The Main change is the addition of a \'Get Cheat Sheet for writers\'
to answer questions which came up by several writer members. Aggraxis
will add a chapter about obtaining an access token, that is not entirely
straightforward.

&#42;&#42; &#42;Walk through longterm open issues and PRs&#42;

\+ Issue 112: LLMNR/nDNS issue, we agree to handle this as part of the
post-installation tasks. Aggraxis will add a section to the current
version.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-11-12/fedora-server.2025-11-12-18.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-11-12/fedora-server.2025-11-12-18.00.log.html)

Wednesday, November 05, 2025

:   

&#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Server Docs: How to proceed with NFS doc&#42;

\+ *AGREED*: pboy will merge Jocelyn's modification into stg, at the
same time checking if it really works as expected in Forgejo

\+ *ACTION*: pboy will update the Server how-to-contribute guide.

\+ *ACTION*: jwhimpel will write a workflow proposal for our Ansible
development task.

&#42;&#42; &#42;Possible Update issue with PostgeSQL&#42;

\+ *ACTION*: nirik will tag common bugs with the postgres issue.

\+ *ACTION*: pboy will check release notes, server docs and QuickDocs
about the postgres issue.

&#42;&#42; &#42;Walk through longterm open issues and PRs&#42;

\+ *ACTION*: Aggraxis will dig into the LLMNR (ticket &#35;114) and make
a proposal.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-11-05/fedora-server.2025-11-05-18.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-11-05/fedora-server.2025-11-05-18.00.log.html)

&#42; *&#42;&#42;Actions summary&#42;&#42;* . pboy will update the
Server how-to-contribute guide. . jwhimpel will write a workflow
proposal for our Ansible development task. . nirik will tag common bugs
with the postgres issue. . pboy will check release notes, server docs
and QuickDocs about the postgres issue. . Aggraxis will dig into the
LLMNR (ticket &#35;114) and make a proposal.

Wednesday, October 29, 2025

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;F43 release testing (resume)&#42;

\+ Overall, testing went well. Testing the SBC bugs took too much time.
Too little attention was paid to the potential problems caused by
individual changes.

\+ *AGREED*: pboy will write a summary to the list and we should see
where the discussion takes us

&#42;&#42; &#42;Server Docs: How to proceed with NFS doc&#42;

\+ *ACTION*: Jocelyn will take a look at the current documentation and
make a proposal how to proceed.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-10-29/fedora-server.2025-10-29-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-10-29/fedora-server.2025-10-29-17.00.log.html)

&#42; *&#42;&#42;Actions summary&#42;&#42;* . Jocelyn will take a look
at the current NFS documentation and make a proposal how to proceed.

Wednesday, October 22, 2025

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;F43 release testing&#42;

\+ Fortunately, the long standing [SBC
bug](https://bugzilla.redhat.com/show_bug.cgi?id=2396309) is resolved.
And arm-image-installer works fine, again. So there is no need to drop
the ARM SBCs from our download page.

&#42;&#42; &#42;Step 1 adjusting our SBC documentation&#42;

\+ *AGREED*: WG modifies the SBC docs as proposed in the ticket
([&#35;168](https://forge.fedoraproject.org/server/tickets/issues/168))

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-10-22/fedora-server.2025-10-22-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-10-22/fedora-server.2025-10-22-17.00.log.html)

&#42; *&#42;&#42;Actions summary&#42;&#42;* . pboy will modify Server
docs about SBC as agreed upon. . Emmanuel Seyman will fix the open PR on
forge.

Wednesday, October 15, 2025

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Follow-up actions &amp; announcements&#42;

\+ *AGREED*: We switch to winter time in sync with US, again. And we
modify the UTC time to keep local time unchanged.

&#42;&#42; &#42;Improve the structure of our user documentation&#42;

\+ *AGREED*: Server documentation will be modified according to proposal
<https://hackmd.io/@pboy/BJnkUjA3el>

&#42;&#42; &#42;Walk through longterm open issues and PRs&#42;

\+ *AGREED*: Each WG member selects an open issue on Forge and either
makes a suggestion on what to do or deals with the issue themselves
until next week meeting.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-10-15/fedora-server.2025-10-15-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-10-15/fedora-server.2025-10-15-17.00.log.html)

&#42; *&#42;&#42;Actions summary&#42;&#42;* . Each WG member selects an
open issue on Forge and either makes a suggestion on what to do or deals
with the issue themselves until next week meeting.

Wednesday, October 01, 2025

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Setting up our new Forgejo repository space&#42;

\+ We have a provisional repo structure according to our previous
discussions and ticket 173.

\+ *AGREED*: We start with a repo structure as proposed in ticket 173

\+ *AGREED*: We keep the naming as is today, for now.

\+ *AGREED*: For the time being we use one issue list for everything. We
will examine whether it proves effective.

\+ *AGREED*: We keep the tickets repo as is

\+ *AGREED*: We adjust the docs repos to the Antorra required structure.

\+ *AGREED*: We restructure the Ansible repo later

\+ *AGREED*: We switch as soon as we can switch the docs pages to forge
and freeze the docs pages on pagure in the meantime

\+ *ACTION*: pboy will restucture the Docs repos as aggreed

\+ *ACTION*: jwhimpel will make a proposal for the Ansible repo
structure.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-10-01/fedora-server.2025-10-01-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-10-01/fedora-server.2025-10-01-17.00.log.html)

&#42; *&#42;&#42;Actions summary&#42;&#42;* . pboy will restucture the
Docs repos . jwhimpel will make a proposal for the Ansible repo
structure.

Wednesday, September 24, 2025

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Follow-up actions &amp; announcements&#42;

\+ Since today we have a new forge:

\+ <https://forge.fedoraproject.org/server>

&#42;&#42; &#42;Future long-term status of the SBC distribution
image&#42;

\+ *AGREED*: If the current installation problems are not fixed by the
release date, no SBC version of the Server should be released at all.

\+ *AGREED*: WG proposes the Server SBC installation medium as release
blocking. Details to be coordinated with other editions.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-09-24/fedora-server.2025-09-24-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-09-24/fedora-server.2025-09-24-17.00.log.html)

Wednesday, September 17, 2025

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Follow-up actions &amp; announcements&#42;

\+ Pboy made contact with Ryan Lerch about new forgejo Fedora forge.
We'll get a stg account fist to be able to explore our options.

&#42;&#42; &#42;F43 release testing&#42;

\+ Paul repoerted, the remote interactive installation via ks file and
OEMDRV USB drive is back. So again, you don't need to edit the kernel
command line (clumpsy with a non_US keyboard layout) nor any termnal
connected.

\+ A severe issue is the SBC. It still doesn't work at all.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-09-17/fedora-server.2025-09-17-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-09-17/fedora-server.2025-09-17-17.00.log.html)

Wednesday, September 10, 2025

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Follow-up actions &amp; announcements&#42;

\+ Eseyman got a reply from the Tomcat group regarding the SELinux issue
with ajp proxy. Blocking localhost access is intentional. The policy is
no default network access. And localhost is seen as network access. We
will pick up this later.

&#42;&#42; &#42;Revision of Server SBC documentation&#42;

\+ We want to clearly distinct between the Server Edition core use case
and special uses such as ARM SBCs. In particular, a Raspberry Pi 4, the
current focus in Fedora, is unsuitable for Server. We will reorganize
the documentation to clearly separate the SBC articles from the main
topics.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-09-10/fedora-server.2025-09-10-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-09-10/fedora-server.2025-09-10-17.00.log.html)

Wednesday, September 03, 2025

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Server Web service guide&#42;

\+ *AGREED*: we create a PR for httpd to include the config files as of
stg article 2025-09-03

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-09-03/fedora-server.2025-09-03-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-09-03/fedora-server.2025-09-03-17.00.log.html)

Wednesday, August 27, 2025

:   

&#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Follow-up actions &amp; announcements&#42;

\+ The change regarding bios boot systems as discussed at last meeting
is now active.

\+ [Proposal: Limit release-blocking status of BIOS systems to just
certain
scenarios](https://discussion.fedoraproject.org/t/proposal-limit-release-blocking-status-of-bios-systems-to-just-certain-scenarios/160757)

&#42;&#42; &#42;httpd vhost issues&#42;

\+ There is a new issue with the ajp proxy protocol. The default
configuratin is blocked by SELinux.

\+ We want to put forward our Webservice configuration. pboy will update
the guide in stg to the latest development.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-08-27/fedora-server.2025-08-27-17.02.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-08-27/fedora-server.2025-08-27-17.02.log.html)

Wednesday, August 20, 2025

:   

&#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Follow-up actions &amp; announcements&#42;

\+ Folllowing a discussion about the status and differentiation of
editions

\+ *AGREED*: We agree to keep server as a package based system for the
foreseeable future and don't intend to start an alternative planning any
time soon.

&#42;&#42; &#42;Server Documentation issues&#42;

\+ *AGREED*: We publish the extended SW Raid doku now as is (adding F42
in meta data). Further refinement probably after F43 release.

\+ As discussed with QA, this provides them with a concrete test path
and decision criterion for the SW RAID item in the biosboot release
blocker criterion.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-08-20/fedora-server.2025-08-20-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-08-20/fedora-server.2025-08-20-17.00.log.html)

Wednesday, August 13, 2025

:   

&#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;F43 release testing&#42;

\+ The main installation media seem to be OK so far. With SBCs an issue
with arm-image-installer on LVM are back again.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-08-13/fedora-server.2025-08-13-17.03.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-08-13/fedora-server.2025-08-13-17.03.log.html)

Wednesday, August 06, 2025

:   

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-08-06/fedora-server.2025-08-06-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-08-06/fedora-server.2025-08-06-17.00.log.html)

Wednesday, July 30, 2025

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Recent changes of release testing criteria&#42;

\+ After a longer discussion:

&#42;&#42;&#42; Optical installation media *AGREED*: Server WG agrees to
change proposal regarding optical media as the proposal suggests
&#42;&#42;&#42; BIOS Boot *AGREED*: Server WG agrees with the proposal
on the condition that a simple Software Raid installation in accordance
with Server documentation is added with blocking status.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-07-30/fedora-server.2025-07-30-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-07-30/fedora-server.2025-07-30-17.00.log.html)

Wednesday July 09, 2025

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Server requirements for the upcoming updated version of
Anaconda&#42;

\+ After an intensive discussion:

&#42;&#42;&#42; *AGREED*: We want to remove \'Software Selection\' from
the installation summary. &#42;&#42;&#42; *AGREED*: We want to keep the
source selection option for net install, but drop it for DVD install it
is is not to much work to implement. &#42;&#42;&#42; *AGREED*: We want
to drop the option menu together with the software selection item.
&#42;&#42;&#42; *AGREED*: We want to keep the time/timezone item and
preselected timezone UTC if it can not determined from the runtime
environment. Can be overwritten during install.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-07-09/fedora-server.2025-07-09-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-07-09/fedora-server.2025-07-09-17.00.log.html)

Wednesday, June 18, 2025

:   

&#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Announcements&#42;

\+ According to our voting we have 2 new members:

&#42;&#42;&#42; Jocelyn
([korora](https://accounts.fedoraproject.org/user/korora/))
([voting](https://pagure.io/fedora-server/issue/161)) &#42;&#42;&#42;
Paul ([aggraxis](https://accounts.fedoraproject.org/user/aggraxis/))
([voting](https://pagure.io/fedora-server/issue/162))

&#42;&#42; &#42;Ansible assisted installation and configuration of NFS
service&#42;

\+ After a longer discussion about various ways to support NFS file
sharing:

\+ *AGREED*: In about 14 days, Emmanuel and John will come up with a
plan about implementation details.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-06-18/fedora-server.2025-06-18-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-06-18/fedora-server.2025-06-18-17.00.log.html)

Wednesday, June 11, 2025

:   

&#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Server requirements for the upcoming updated version of
Anaconda&#42;

\+ *ACTION*: Jocelyn will write a summery of the discussion with the
status as of next Wednesday, so that we have something to base our
decision on.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-06-11/fedora-server.2025-06-11-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-06-11/fedora-server.2025-06-11-17.00.log.html)
&#42; *&#42;&#42;Actions summary&#42;&#42;* . Jocelyn will write a
summery of the discussion with the status as of next Wednesday, so that
we have something to base our decision on.

Wednesday, May 28, 2025

:   

&#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Ansible assisted installation and configuration of NFS
service&#42;

\+ Eseyman completed an RPM of most interesting Ansible roles,
specifically the NFS role (currently on COPR). Now we have to test the
RPM and combine with jwhimpels work.

\+ *AGREED*: we will use the next two weeks to test the available tools
and decide how we can best achieve our goal of supporting services. And
we will consider how we can optimize the distribution.

&#42;&#42; &#42;Open Floor&#42;

\+ We will make our FAS Server Group (server-wg) official, containing
the authoritative list of WG members. The current WIKI list will then be
removed..

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-05-28/fedora-server.2025-05-28-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-05-28/fedora-server.2025-05-28-17.00.log.html)

Wednesday, May 07, 2025

:   AGREED: we skip next meeting (May 14)

&#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Ansible assisted installation and configuration of NFS
service&#42;

\+ AGREED: We postpone the NFS Ansible project until eseyman has a
robertdebock rpm ready and eseyman and jwhimpel have a proposal how to
(re)use it for our purposes.

&#42;&#42; &#42;Server user poll&#42;

\+ Eseyman reported, he was pleasantly surprised. Lots of people seem
satisfied with what we ship. The main call for improvement is
documentation, use cases, best pratices, &#8230;

\+ Eseyman and pboy will prepare a finer analyses of the data.

&#42;&#42; &#42;Follow-up of the F42 server development and test
cycle&#42;

\+ AGREED: We try to create a Server Edition test day (or better test
week)

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-05-07/fedora-server.2025-05-07-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-05-07/fedora-server.2025-05-07-17.00.log.html)

Wednesday, April 23, 2025

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Ansible assisted installation and configuration of NFS
service&#42;

\+ ACTION: jwhimpel will create a Beta RPM that will establish the
\'base\' filesystem and related documentation for our ansible setup (on
admin's workstation)

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-04-23/fedora-server.2025-04-23-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-04-23/fedora-server.2025-04-23-17.00.log.html)

Wednesday, April 16, 2025

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Follow-up of the F42 server development and test
cycle&#42;

\+ The final release actually no longer contains the possibility of a
remote interactive installation initialized without terminal by
kickstart file. This is the result of a system-wide switch from VNC to
RDP initiated by the Workstation WG. The discontinuation is a side
effect of the changes in Anaconda and was unannounced. We did not expect
this omission and unfortunately discovered it too late.

\+ AGREED: We will create a list of minimal manual tests and try to
establish a test week for F43.

\+ A particularly intensive checking require all changes that are in any
way related to the Workstation WG.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-04-16/fedora-server.2025-04-16-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-04-16/fedora-server.2025-04-16-17.00.log.html)

Wednesday, April 09, 2025

:   Open discussion about the Ansible assisted installation and
    configuration of NFS service project.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-04-09/fedora-server.2025-04-09-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-04-09/fedora-server.2025-04-09-17.00.log.html)

Wednesday, April 02, 2025

:   

&#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Bug: Fedora 42: Server boot aarch64 image exceeds
maximum size&#42;

\+ There is a pending PR.

\+ ACTION: Paul Maconi (Aggraxis) will take care or the PR regarding the
size change for aarch64 architecture.

&#42;&#42; &#42;Status /progress Beta Testing&#42;

\+ Testing so far revealed some minor issues. Really bad, the remote
interactive installation doesn't work anymore with the kickstart file.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-04-02/fedora-server.2025-04-02-15.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-04-02/fedora-server.2025-04-02-15.00.log.html)

Wednesday, March 26, 2025

:   

&#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Bug: Fedora 42: Server boot aarch64 image exceeds
maximum size&#42;

\+ The reasons are obviously specific to the characteristics of aarch64
architecture. The x86\_&amp;4 version is not affected.

\+ AGREED: If the ongoing attempts to reduce the size are not
successful, Server WG is in favor of an increase to 1.2 GB as an
exception for now.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-03-26/fedora-server.2025-03-26-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-03-26/fedora-server.2025-03-26-17.00.log.html)

Wednesday, March 19, 2025

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Organisation of Beta Testing&#42;

\+ Pboy will perform the hardware relataed testing, eseyman takes care
of SBCs and jwhimpel of VM installation. We will track the results in an
issue.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-03-19/fedora-server.2025-03-19-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-03-19/fedora-server.2025-03-19-17.00.log.html)

Wednesday, March 12, 2025

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Announcements&#42;

\+ During US daylight saving time, we adjust the beginning of our
meeting to 17:00 UTC, so that local daily routines remain unchanged.

&#42;&#42; &#42;Scheduled Server podcast for March 11&#42;

\+ The podcast scheduled for yesterday was delayed, due to staff
shortage. Mowest will try to join the new meeting together with pboy.

&#42;&#42; &#42;Cockpit self-signed certificates change&#42;

\+ AGREED: Server WG emphasizes that we need access without official
certificates for private networks

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-03-12/fedora-server.2025-03-12-18.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-03-12/fedora-server.2025-03-12-18.00.log.html)

Wednesday, March 05, 2025

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;F43 Change proposal: Disabling support of building
OpenSSL engines&#42;

\+ Eseyman will track this.

&#42;&#42; &#42;Open Floor&#42;

\+ A review of the current state of the \'countme\' statistics is to
become a regularly recurring agenda item, approximately monthly or
quarterly.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-03-05/fedora-server.2025-03-05-18.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-03-05/fedora-server.2025-03-05-18.00.log.html)

Wednesday, February 19, 2025

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Server user poll&#42;

\+ AGREED: We will let the survey closed as decided before.

&#42;&#42; &#42;Ansible assisted installation and configuration of NFS
service&#42;

\+ AGREED: Server WG will limit NFS support to NFS 4

&#42;&#42; &#42;Ansible assisted installation and configuration of WEB
service&#42;

\+ AGREED: We create a supported web service following the current
description of a basic setup in the server docs. This is also the basis
for developing an Ansible playbook.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-02-19/fedora-server.2025-02-19-18.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-02-19/fedora-server.2025-02-19-18.00.log.html)

Wednesday, February 12, 2025

:   

&#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Server user poll&#42;

\+ We have a \'brainstorming collection document\' at
<https://hackmd.io/@pboy/SJzz7VcFJl>. We agreed that everybody will
enter their idea about data analysis and questions we try to answer by
data analysis.

\+ Once the survey is complete, pboy will export the data in a secure
form and make it available to interested WG members.

&#42;&#42; &#42;Fedora Server Edition - homelab spin-off&#42;

\+ AGREED Server WG decides to start work on a honelab / homeserver
spin-off.

&#42;&#42; &#42;FLOCK 2025&#42;

\+ AGREED Eseyman, Mowest and Pboy will finalize suitable contributions
to Flock 2025 on the basis of the current collection of ideas and submit
the application(s).

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-02-12/fedora-server.2025-02-12-18.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-02-12/fedora-server.2025-02-12-18.00.log.html)

&#42; *&#42;&#42;Recent actions status change&#42;&#42;* . eseyman DONE
will post on redit forum, Fedora general user on Discussion, Fedora
Devel on Discussion and the corresponding mailing lists about the next 2
weeks to participate . pboy ONGOING will ping Abbra and the freeIPA /
localKDC people to advice and help us to integrate the right thing into
Fedora Server.

Wednesday, February 05, 2025

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Server user poll&#42;

\+ We currently have 4077 participants, of whom 548 have fully answered
the survey. The others have left out several questions. We will continue
to promote the poll. The currently scheduled end date is February 18.

\+ ACTION Emmanuel Seyman will post on redit forum, Fedora general user
on Discussion, Fedora Devel on Discussion and the corresponding mailing
lists about the next 2 weeks to participate

\+ AGREED mowest takes over the conduct and organization of the data
analysis. Support from Gwmngilfen, Emmanuel, pboy and anyone who is
interested

&#42;&#42; &#42;FOSDEM 2025 &amp; FLOCK 2025&#42;

\+ At *Fosdem* there was a discussion with abbra about freeIPA and
localKDC (local Key Distribution Center) that is planned for F43. It may
help us to resolve the UID issue with NFS.

\+ ACTION pboy will ping Abbra and the freeIPA / localKDC people to
advice and help us to integrate the right thing into Fedora Server.

\+ Regarding *Flock* we discussed several ideas for contribution. We
will continue the discussion on the mailing list.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-02-05/fedora-server.2025-02-05-18.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-02-05/fedora-server.2025-02-05-18.00.log.html)

&#42; *&#42;&#42;Actions summary&#42;&#42;* . eseyman will post on redit
forum, Fedora general user on Discussion, Fedora Devel on Discussion and
the corresponding mailing lists about the next 2 weeks to participate .
pboy will ping Abbra and the freeIPA / localKDC people to advice and
help us to integrate the right thing into Fedora Server.

Wednesday, January 15, 2025

:   

&#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Ansible assisted installation and configuration of NFS
service&#42;

\+ Nothing new so far. But we have a new issue to deal with, managing
firewall portmapper port (111).

&#42;&#42; &#42;Ansible assisted installation and configuration of WEB
service&#42;

\+ Nothing new so far.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-01-15/fedora-server.2025-01-15-18.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-01-15/fedora-server.2025-01-15-18.00.log.html)

Wednesday, January 8, 2025

:   

&#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Follow-up actions &amp; announcements&#42;

\+ Just for information see *Current Actions summary* below.

\+ Fosdem runs from February 1-2. Fedora will be represented by a booth,
eseyman and pboy will be there.

&#42;&#42; &#42;Server user poll&#42;

\+ The poll is open and running. We don't have any data on an interim
result yet.

&#42;&#42; &#42;Revisiting Fedora Server quality criteria and
procedures&#42;

\+ Because of the current issues with NFS which may take some tie to get
resolved we open another path with [web
services](https://docs.stg.fedoraproject.org/en-US/fedora-server/services/httpd-basic-setup/).

&#42;&#42; &#42;Work program and goals&#42;

\+ We postpone this until we have evidence of our server poll. &#42;
[Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-01-08/fedora-server.2025-01-08-18.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-01-08/fedora-server.2025-01-08-18.00.log.html)

&#42; *&#42;&#42;Current Actions summary&#42;&#42;* . ON HOLD pboy will
file an issue with releng regarding installation media . ONGOING pboy
will close bug &#35;2247872
(<https://bugzilla.redhat.com/show_bug.cgi?id=2247872>) . ONGOING pboy
will write a draft issue for the goal \'file server\' as a base for
further finetuning and detailed specification . ONGOING jwhimnpel will
develop a Ansible playbook for NFS service . PENDING eseyman review
John's playbooks . DONE Mowest will write a 1st draft of an article
about our poll.

# Meeting Minutes 2024 {#_meeting_minutes_2024}

Stephen Daley; Peter Boy :page-authors: {author}, {author_2}

Wednesday, December 18, 2024

:   

&#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Ansible assisted installation and configuration of NFS
service&#42;

\+ Still discussion how to organize the classic UID/GID issue with NFS
clients.

\+ AGREED Regarding NFS we will start with LDAP ansible playbook and in
parallel establish documentation for the manual way in smaller networks.

&#42;&#42; &#42;Server user poll&#42;

\+ Decided to publish the [Fedora Magazine
Article](https://fedoramagazine.org/fedora-server-user-survey-your-cattle-or-your-pets/)
as drafted by Mowest on Dec 20 or Dec 23 and to start the poll
immediately.

\+ ACTION DONE: Mowest will write a 1st draft of an article about our
poll.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-12-18/fedora-server.2024-12-18-18.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-12-18/fedora-server.2024-12-18-18.00.log.html)
&#42; *&#42;&#42;Current Actions summary&#42;&#42;* . ON HOLD pboy will
file an issue with releng regarding installation media . ONGOING pboy
will close bug &#35;2247872
(<https://bugzilla.redhat.com/show_bug.cgi?id=2247872>) . ONGOING pboy
will write a draft issue for the goal \'file server\' as a base for
further finetuning and detailed specification . ONGOING jwhimnpel will
develop a Ansible playbook for NFS service . PENDING eseyman review
John's playbooks . DONE Mowest will write a 1st draft of an article
about our poll.

Wednesday, December 11, 2024

:   

&#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Cockpit boot message&#42;

\+ We already discussed this topic on [mailing
list](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-12-11/fedora-server.2024-12-11-18.00.log.html).
There is a [request to remove the Cockpit
information](https://bugzilla.redhat.com/show_bug.cgi?id=1635200) at
every ssh login.

\+ AGREED: Regarding bug 1635200, WG agrees to keep the current Cockpit
informational message.

&#42;&#42; &#42;Ansible assisted installation and configuration of NFS
service&#42;

\+ It appears that f41's move from dnf to dnf5 has caused my ansible
modules some heartburn. The issues require further research.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-12-11/fedora-server.2024-12-11-18.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-12-11/fedora-server.2024-12-11-18.00.log.html)

Wednesday, December 4, 2024

:   &#42;&#42;Attention&#42;&#42;: We agreed to cancel our regular
    meetings scheduled for *Dec 25* and *Jan 1*, but keeping *Dec 18*
    and *Jan 08*.

&#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Server user poll&#42;

\+ AGREED: The current version in Fedora LimeSurvey instance is the
final one.

\+ We discussed and agreed on various steps to spread the word about the
survey in the Fedora community.

&#42;&#42; &#42;Work program and goals&#42;

\+ We agree that it is time to produce something really new for Fedora
Server. Some rough ideas:

&#42;&#42;&#42; Creating a *Fedora Home Server* spin for Raspberry Pi /
SBCs &#42;&#42;&#42; Installing Fedora Server on Windows WSL or macOS
UTM

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-12-04/fedora-server.2024-12-04-18.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-12-04/fedora-server.2024-12-04-18.00.log.html)
&#42; *&#42;&#42;Actions summary&#42;&#42;* . ACTION: pboy will compile
statistical data on the use of the Fedora server for one of the next
meetings. . ACTION: eseyman will post on the Fedora group on Facebook
about Fedora Server survey.

Wednesday, November 27, 2024

:   

&#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Server Poll&#42;

\+ AGREED: The Fedora Server poll should start Dec. 10 24 and run until
Feb 18 25

\+ The survey will be available at
<https://fedoraproject.limequery.com/fedora-server-f41> when it has been
transferred into the Fedora space.

&#42;&#42; &#42;Ansible assisted installation and configuration of NFS
service&#42;

\+ \@jwhimpel plans to update the current repo. Then we can start
testing and reviewing. He will announce the update on the mailing list.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-11-27/fedora-server.2024-11-27-18.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-11-27/fedora-server.2024-11-27-18.00.log.html)
&#42; *&#42;&#42;Actions summary&#42;&#42;* . \@jflory7 due:2024-12-04
Import mowest's LimeSurvey survey into the Fedora LimeSurvey instance
and set it to public . mowest and pboy will write in FedMag article in
time with the poll planning . eseyman will post on the mailing list
inviting people to fill out the survey when the poll is online

Wednesday, November 20, 2024

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Future release testing procedures&#42;

\+ &#42;AGREED&#42; pboy writes the draft of a document that describes
our test strategy.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-11-20/fedora-server.2024-11-20-18.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-11-20/fedora-server.2024-11-20-18.00.log.html)

Wednesday, November 13, 2024

:   

&#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;KVM image migration to KIWI&#42;

\+ AGREED: The KVM image will be migrated to KIWI now, the adjustment of
the naming will de dealt with later together with the isos.

&#42;&#42; &#42;PostgreSQL -- is our automatic testing sufficient?&#42;

\+ No decision yet.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-11-13/fedora-server.2024-11-13-18.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-11-13/fedora-server.2024-11-13-18.00.log.html)
&#42; *&#42;&#42;Actions summary&#42;&#42;* . ON HOLD pboy will file an
issue with releng regarding installation media . ONGOING pboy will close
bug &#35;2247872 (<https://bugzilla.redhat.com/show_bug.cgi?id=2247872>)
. ONGOING pboy will write a draft issue for the goal \'file server\' as
a base for further finetuning and detailed specification . ONGOING
jwhimnpel will develop a Ansible playbook for NFS service . PENDING
eseyman review John's playbooks . DONE eseyman will monitor the change
list for possible issues which may affect Server . DONE mowest will
reach out to AdamW and discuss how we can use the result tables. . DONE
pboy will create a tracking issue and copy the table of F 40 as a
starting point. . DONE Mowest will create a Lime survey version of the
discussed draft and reach out to Justin to put the project forward. .
PENDING Mowest will write a 1st draft of an article about our poll.

Wednesday, November 06, 2024

:   

&#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;New Anaconda installer for Server&#42;

\+ In F42, only workstation will benefit from the new Anaconda WEB UI.
Before Server can use it, a lot of missing functionality remains to get
developed. Workstation will switch to RDP instead of VNC. For remote
interactive installation, on the kernel line the parameter inst.vnc is
replaced by inst.rdp.

&#42;&#42; &#42;Current status and further advancement of server
docs&#42;

\+ Thanks to Paul Maconi we have our first entry in the \'Fedora Server
in a virtualized runtime environment\' project about [installing on
Proxmox](https://docs.fedoraproject.org/en-US/fedora-server/virtualization/vm-install-diskimg-proxmox/).
Emmanuel will review.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-11-06/fedora-server.2024-11-06-18.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-11-06/fedora-server.2024-11-06-18.00.log.html)

Wednesday, October 30, 2024

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Follow-up actions &amp; announcements&#42;

\+ ACTION: Mowest will write a 1st draft of an article about our poll.

&#42;&#42; &#42;Ansible assisted installation and configuration of NFS
service&#42;

\+ NFS 4 is working now, NFS server is running, as well as NFS client.
Both need some tweaking.

\+ AGREED Regarding Ansible / NFS we will study and test what we have
and continue on meeting in 2 weeks.

&#42;&#42; &#42;Looking back at testing release 41&#42;

\+ AGREED: We discuss this during the next 2-3 weeks on mailing list and
try to determine a final plan. One issue to take into account is the
lack of test equipment.

&#42;&#42; &#42;Current membership status and clean up process&#42;

\+ Our official current list is here: +!link
<https://fedoraproject.org/wiki/Server>

\+ We have 7 members that never showed even up for the last 2 years. Qur
usual procedure is to contact them and ask, what they are planning. And
perhaps agree to retreat. And then we should take an initiative to get
1-2 new members. Maybe as part of our upcoming poll.

\+ AGREED: pboy will start to contact dormant members.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-10-30/fedora-server.2024-10-30-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-10-30/fedora-server.2024-10-30-17.00.log.html)

&#42; *&#42;&#42;Actions summary&#42;&#42;* . Mowest will write a 1st
draft of an article about our poll.

Wednesday, October 23, 2024

:   

&#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Testing Release 41&#42;

\+ After a short reading break postponed to next meeting.

&#42;&#42; &#42;Server user poll&#42;

\+ Justin joined us and made an appointment with Mowest to take things
further. So we'll be able to start soon.

\+ AGREED: We finally use the version as now online, i.e. without an
\'other\' option for \'How are you using Fedora Server?\'

&#42;&#42; &#42;New Business: Generation of the Server KVM image&#42;

\+ LINK: <https://pagure.io/fedora-server/issue/146>

\+ With release 42 we will switch to KIWI. ImageFactory is no longer
support nor available at all. Current efforts:

\+ LINK <https://koji.fedoraproject.org/koji/taskinfo?taskID=125070598>

\+ AGREED:Server WG agrees to switch to KIWI (4:0:0)

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-10-23/fedora-server.2024-10-23-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-10-23/fedora-server.2024-10-23-17.00.log.html)

&#42; *&#42;&#42;Actions summary&#42;&#42;* . DONE: pboy will write an
updated summary about our release 4 testing and we continue on mailing
list and next meeting. . DONE: pboy will write a summary of the current
state of our poll on the mailing list and we continue on mailing list
and next meeting.

Wednesday, October 16, 2024

:   

&#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Testing Release 41&#42;

\+ We agree that manual testing of our installation media and procedures
is necessary, and some of this is already included in the test plans.
Furthermore, it would be desirable to tailor the test announcement for
servers more closely to server issues.

\+ ACTION: pboy will write an updated summary about our release 4
testing and we continue on mailing list and next meeting

&#42;&#42; &#42;Server user poll&#42;

\+ Mowest has requested access to the Fedora Limesurvey instance through
Gitlab. Furthermore, he created a draft of our survey in a free account
of Limesurvey (<https://mowest.limesurvey.net/778249?lang=en>).

\+ ACTION: pboy will write a summary of the current state of our poll on
the mailing list and we continue on mailing list and next meeting.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-10-16/fedora-server.2024-10-16-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-10-16/fedora-server.2024-10-16-17.00.log.html)
&#42; *&#42;&#42;Actions summary&#42;&#42;* . pboy will write an updated
summary about our release 4 testing and we continue on mailing list and
next meeting. . pboy will write a summary of the current state of our
poll on the mailing list and we continue on mailing list and next
meeting.

Wednesday, October 02, 2024

:   

&#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Testing Release 41&#42;

\+ We still have to test installation on SBCs. Eseyman will take this
on.

&#42;&#42; &#42;Server user poll&#42;

\+ Mowest had no success yet in pushing the poll through the other
Fedora instances. We can't make any progress in the current state
without that.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-10-02/fedora-server.2024-10-02-17.01.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-10-02/fedora-server.2024-10-02-17.01.log.html)

Wednesday, September 25, 2024

:   

&#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Server user poll&#42;

\+ We decided to use the current version with all inserted modifications
and with the shorter of the formulated alternatives on
[hackmd.io](https://hackmd.io/@pboy/ByguCouphC).

\+ Mowest will create a Lime survey version of the discussed draft and
reach out to Justin to put the project forward.

&#42;&#42; &#42;Testing Release 41&#42;

\+ We agreed to continue the discussion on the mailing list due to
running out of time here. &#42;See&#42; [&#42;pboy: Improving our
release testing efforts. An attempt to summarize our
discussion&#42;](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/ODISTPROLKECRXX73LA5VUVZJFIFEHRR/)

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-09-25/fedora-server.2024-09-25-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-09-25/fedora-server.2024-09-25-17.00.log.html)

&#42; *&#42;&#42;Actions summary&#42;&#42;* . &#42;ONGOING&#42;: eseyman
will monitor the change list for possible issues which may affect Serve
. &#42;New&#42;: Mowest will create a Lime survey version of the
discussed draft and reach out to Justin to put the project forward.

Wednesday, September 18, 2024

:   

&#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Testing Release 41&#42;

\+ The discussion focused on optimizing our approach to release testing.
There was agreement on the one hand that the test program should be
integrated into the distribution QA, and on the other hand that tests of
individual functionalities should be automated. Irrespective of this,
there is a need for manual testing, particularly of the (hardware)
installation media.

\+ Action: pboy will create a summary on the mailing list, which will be
the basis for further discussion.

&#42;&#42; &#42;Server user poll&#42;

\+ We finally agreed on 4 goals:

\+ - Who is the audience for Fedora Server - Where is Fedora Server
primarily used: Hardware or VM - What are the main use cases for Fedora
Server - Where are future efforts of the Fedora Server WG best applied

\+ A final version is to be decided at the next meeting.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-09-18/fedora-server.2024-09-18-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-09-18/fedora-server.2024-09-18-17.00.log.html)
&#42; *&#42;&#42;Actions summary&#42;&#42;* . &#42;ACTION&#42;:
&#42;ONGOING&#42; eseyman will monitor the change list for possible
issues which may affect Server . &#42;ACTION&#42;: &#42;DONE&#42; mowest
will reach out to AdamW and discuss how we can use the result tables.

Wednesday, September 04, 2024

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Ansible assisted installation and configuration of NFS
service&#42;

\+ Jwhimpel has finished a first version of the Ansible code including a
short documentation. We will discuss this in detail at the next meeting
when all members have been able to test it.

&#42;&#42; &#42;Testing Release 41&#42;

\+ Ticket &#35;144 is available for the test. Based on a discussion with
adamw, pboy will create a draft test description in the Fedora Server
Wiki area. The aim is to automate as much as possible.

\+ Eseyman has created a list of potentially problematic changes, see
addendum to the invitation. The list will also be added to the ticket.
We will discuss it at the next meeting.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-09-04/fedora-server.2024-09-04-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-09-04/fedora-server.2024-09-04-17.00.log.html)

&#42; *&#42;&#42;Actions summary&#42;&#42;* . &#42;ACTION&#42;:
&#42;ONGOING&#42; eseyman will monitor the change list for possible
issues which may affect Server . &#42;ACTION&#42;: &#42;DONE&#42; pboy
will create a tracking issue and copy the table of F 40 as a starting
point. . &#42;ACTION&#42;: &#42;ONGOING&#42; mowest will reach out to
AdamW and discuss how we can use the result tables.

Wednesday, August 28, 2024

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Ansible assisted installation and configuration of NFS
service&#42;

\+ The server roles are basically working. Jwhimpel will add some
documentation how to use (and test) it. There are some topics we will
have to decide after everyone could use it, e.g. type of mounts. On the
client side, we tend to only support and handle Fedora.

&#42;&#42; &#42;Testing Release 41&#42;

\+ We decided to use the same procedure as last time (F40) for now.

\+ &#42;ACTION&#42;: eseyman will monitor the change list for possible
issues which may affect Server

\+ &#42;ACTION&#42;: pboy will create a tracking issue and copy the
table of F 40 as a starting point.

\+ We want to systematize the process and make greater use of the Fedora
options, e.g. the results tables that are created for each build.

\+ &#42;ACTION&#42;: mowest will reach out to AdamW and discuss how we
can use the result tables.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-08-28/fedora-server.2024-08-28-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-08-28/fedora-server.2024-08-28-17.00.log.html)
&#42; *&#42;&#42;Actions summary&#42;&#42;* . &#42;ACTION&#42;:
&#42;DONE&#42; pboy will create 2 empty docs for installation &amp;
configuration to the repo, then everyone can add relevant topics to it
and migrate the current integrated doc. . &#42;ACTION&#42;:
&#42;DONE&#42; pboy will add all WG core members as committers to our
pagure repo. . &#42;ACTION&#42;: eseyman will monitor the change list
for possible issues which may affect Server . &#42;ACTION&#42;: pboy
will create a tracking issue and copy the table of F 40 as a starting
point. . &#42;ACTION&#42;: mowest will reach out to AdamW and discuss
how we can use the result tables.

Wednesday, August 21, 2024

:   

&#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Follow-up, findings and conclusions from Flock 2024&#42;

\+ Eseyman gave an [overview of his impressions and
experiences](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/ZFEQZHECF4DNJA3VH4UIGGITRLFCXKFH/).

\+ One wish that was expressed was to use Fedora as a router, similar to
OpenWRT. It was agreed that this is not possible within the framework of
Fedora Server, as the requirements for system and data security are too
different.

\+ One positive feedback was that Fedora was the slowest moving as well
as the most backward compatible, and nevertheless with always up-to-date
versions of the server software bits, of the Fedora project. A most
welcome characteristic of our goals for Fedora Server Edition.

&#42;&#42; &#42;Optimizing NFS service documentation&#42;

\+ jwhimpel will start to add topics the the empty doc templates when he
completed the first version of the Ansible code.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-08-21/fedora-server.2024-08-21-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-08-21/fedora-server.2024-08-21-17.00.log.html)

&#42; *&#42;&#42;Actions summary&#42;&#42;* . &#42;DONE&#42; eseyman
will post Flock recap to the list. . &#42;DONE&#42; jednorozec will
implement the patch to bug &#35;2247872

Wednesday, August 14, 2024

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Follow-up, findings and conclusions from Flock 2024&#42;

\+ We considered a number of different topics that were discussed. By
and large, our current course in the further development of Fedora
Server Edition has proven itself. The most important change will be the
implementation of Ansible for our special supported services (previous
server roles).

\+ Everyone agrees that getting to know each other and discussing goals
and next steps in person was a hugely positive experience and a
tremendous motivational boost.Nothing else can replace that. Flock was
very, very worthwhile and all the effort was very rewarding. Flock next
year is already a positive expectation.

\+ &#42;ACTION&#42;: eseyman will post his Flock recap to the list.

&#42;&#42; &#42;Ansible assisted installation and configuration of NFS
service&#42;

\+ We decided to do the development in stg branch and add the directory
structure there, too.

\+ &#42;AGREED&#42;: Regarding distribution we prefer the rpm path of
action.

\+ &#42;ACTION&#42;: eseyman review John's playbooks

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-08-14/fedora-server.2024-08-14-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-08-14/fedora-server.2024-08-14-17.00.log.html)

&#42; *&#42;&#42;Actions summary&#42;&#42;* . &#42;ONGOING&#42; pboy
will write a draft issue for the goal \'file server\' as a base for
further finetuning and detailed specification . &#42;PENDING&#42; pboy
will create a hackmd draft for a collection of questions about Fedora
Server in a virtualized environment . &#42;PENDING&#42; mowest will come
up with a plan and steps to conduct the survey on discussion -- waiting
for a draft of collection of questions . &#42;NEW&#42; jednorozec will
implement the patch to bug &#35;2247872

Wednesday, July 31, 2024

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Ansible assisted installation and configuration of NFS
service&#42;

\+ We discussed again about the specific goal we want to achive with the
Ansible Playbook.

\+ &#42;AGREED&#42; Server WG agrees to the goal as defined in comment
<https://pagure.io/fedora-server/issue/138&#35;comment-920322> to issue
138

&#42;&#42; &#42;Optimizing NFS service documentation&#42;

\+ We want to split the current NFS draft in 2 parts: Installation and
Configuration.

\+ &#42;ACTION&#42; *&#42;&#42;DONE&#42;&#42;*: pboy will create 2 empty
docs for installation &amp; configuration to the repo

\+ &#42;AGREED&#42; to postpone this until we have a working version of
the Ansible playbook.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-07-31/fedora-server.2024-07-31-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-07-31/fedora-server.2024-07-31-17.00.log.html)

&#42; *&#42;&#42;Actions summary&#42;&#42;* . &#42;DONE&#42; pboy will
add all WG core members as committers to our pagure repo. .
&#42;DONE&#42; pboy will create 2 empty docs for installation &amp;
configuration to the repo . &#42;CANCELED&#42; pboy will close bug
&#35;2247872 (<https://bugzilla.redhat.com/show_bug.cgi?id=2247872>) --
There is still an ongoing discussion about improving Server first boot
process. . &#42;ONGOING&#42; pboy will write a draft issue for the goal
\'file server\' as a base for further finetuning and detailed
specification

Wednesday, July 24, 2024

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Renaming distribution media for Fedora Server&#42;

\+ &#42;AGREED&#42;: We defer the renaming until RelEng has decided
about the future Fedora tool set AND has updated the documentation.

\+ &#42;ACTION&#42;: *&#42;&#42;canceled&#42;&#42;* pboy will file an
issue with releng regarding installation media

&#42;&#42; &#42;Ansible assisted installation and configuration of NFS
service&#42;

\+ Eseyman has packed the the robertdebock roles in an rpm :
<https://eseyman.fedorapeople.org/ansible-robertdebock-roles/>. It's an
alternative to the current Fedora standard package. Jwhimple has 4 roles
ready, but can't upload due to permission issues and incomplete Server
repo configuration.

\+ &#42;ACTION&#42;: pboy will add all WG core members as committers to
our pagure repo.

&#42;&#42; &#42;Optimizing NFS service documentation&#42;

\+ We want to split the current NFS draft in 2 parts: Installation and
(Basic) Configuration. Jwhimpel will start do add at löeast bullet point
to outline the intended information. To support this, pboy will add
correspoding empty files. We agreed to document the process using
Ansible and by using manually CLI. Whether and how we take Cockpit into
account is still to be decided.

\+ &#42;ACTION&#42;: pboy will create 2 empty docs for installation
&amp; configuration to the repo, then everyone can add relevant topics
to it and migrate the current integrated doc.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-07-24/fedora-server.2024-07-24-16.10.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-07-24/fedora-server.2024-07-24-16.10.log.html)

&#42; *&#42;&#42;Actions summary&#42;&#42;* . &#42;ACTION&#42;:
*&#42;&#42;new&#42;&#42;* pboy will add all WG core members as
committers to our pagure repo. . &#42;ACTION&#42;:
*&#42;&#42;new&#42;&#42;* pboy will create 2 empty docs for installation
&amp; configuration to the repo, then everyone can add relevant topics
to it and migrate the current integrated doc. . &#42;ACTION&#42;:
*&#42;&#42;canceled&#42;&#42;* pboy will file an issue with releng
regarding installation media

Wednesday, July 17, 2024

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Ansible assisted installation and configuration of NFS
service&#42;

\+ Discussed the specific goal of this work. Agreed to focus on a
playbook for commen/default use case and provide hooks to extend to
further local use cases.

&#42;&#42; &#42;Fedora Server in a virtualized runtime environment&#42;

\+ We agreed to start with a poll and ask users how they use Fedora
Server Edition and what they are missing in the first place. Mowest and
pboy will work on it.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-07-17/fedora-server.2024-07-17-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/fedora-meeting/2023-11-15/fedora-server.2023-11-15-18.00.log.html)
&#42; *&#42;&#42;Actions summary&#42;&#42;* . ACTION: pboy will create a
hackmd draft for a collection of questions about Fedora Server in a
virtualized environment . ACTION: mowest will come up with a plan and
steps to conduct the survey on discussion

Wednesday, July 10, 2024

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

    We had an open discussion about ongoing activities.

&#42;&#42; Humaton started to check out Kiwi to create Server iso
distributables. There is a SuSE add-on to achieve that. &#42;&#42;
Humaton will care about ticket &#35;114, which is an undecided long
standing issue regarding LLMR.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-07-10/fedora-server.2024-07-10-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-07-10/fedora-server.2024-07-10-17.00.log.html)

Wednesday, July 03, 2024

:   

&#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Change to a weekly meeting schedule&#42;

\+ &#42;AGREED&#42;: Server WG switches to a *weekly meeting*

&#42;&#42; &#42;Ansible assisted installation and configuration of NFS
service&#42;

\+ jwhimnpel will provide 2 Ansible roles in about 2 weeks for further
discussion and testing.

\+ eseyman and mowest will work on improving the current docs draft.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-07-03/fedora-server.2024-07-03-17.01.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-07-03/fedora-server.2024-07-03-17.01.log.html)
&#42; *&#42;&#42;Actions summary&#42;&#42;* . pboy will file an issue
with releng regarding installation media - pending . pboy will close bug
&#35;2247872 - pending because of ongoing work . pboy will write a draft
issue for the goal \'file server\' as a base for further finetuning and
detailed specification - ongoing . jwhimpel will provide 2 Ansible roles
for NFS service . eseyman and mowest will start reviewing the currnt NFS
doc draft

Wednesday, June 26, 2024

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

    We had an open discussion about our various ongoing works.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-06-26/fedora-server.2024-06-26-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-06-26/fedora-server.2024-06-26-17.00.log.html)

Wednesday, June 19, 2024

:   

&#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Ansible assisted installation and configuration of NFS
service&#42;

\+ We discussed the results of a short poll about the documentation part
and how to improve the current article. Amoung others we want to split
into installation and configuration and in each part describe the manual
procedure and the Ansible usage.

\+ We will add a new subdirectory to our repo for Ansible scripts.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-06-19/fedora-server.2024-06-19-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-06-19/fedora-server.2024-06-19-17.00.log.html)
&#42; *&#42;&#42;Actions summary&#42;&#42;* . &#42;Action&#42;: pboy
will create an additional directory fedora-ansible in fedora-server repo

Wednesday, June 12, 2024

:   

&#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Elevating Fedora Server VM distribution image&#42;

\+ Jason will start to elevate Fedora Server VM distribution image to a
release requirement as the other Server installation images

&#42;&#42; &#42;Fixing the \'Everything\' installation medium
problem&#42;

\+ &#42;AGREED&#42;: Server WG agrees that the Fedora Server option has
to be removed from the Everything Install medium in the long term.

\+ W'll pick this up again as soon as we have free resources.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-06-12/fedora-server.2024-06-12-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-06-12/fedora-server.2024-06-12-17.00.log.html)

Wednesday, June 05, 2024

:   

&#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Fedora Server goal(s) and \'story\' for F41 / F42&#42;

\+ &#42;AGREED&#42;: WG's goal is to provide a spin \'local or public
file server (NFS, Samba, Ansible support)

\+ &#42;AGREED&#42;: WG's goal is to improve the use of Fedora Server in
a VPS infrastructure and to promote it as a standard offering.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-06-05/fedora-server.2024-06-05-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-06-05/fedora-server.2024-06-05-17.00.log.html)

&#42; *&#42;&#42;Actions summary&#42;&#42;* . &#42;Action&#42;: pboy
will write a draft issue for the goal \'file server\' as a base for
further finetuning and detailed specification.

Wednesday, May 01, 2024

:   

&#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Revisiting Server installation media naming
convention&#42;

\+ &#42;AGREED&#42;: Server WG decides to rename the installation media:
DVD -&gt; offline , netboot -&gt; online, KVM -&gt; virt, and rawsbc for
ARM raw image.

\+ &#42;AGREED&#42;: Server WG decides on a consistent naming convention
according to the scheme:
\'Fedora-Server-&lt;rel&gt;-&lt;method&gt;-&lt;arch&gt;-&lt;version&gt;.&lt;filetype&gt;\'

&#42;&#42; &#42;Elevating Fedora Server VM distribution image&#42;

\+ jwhimpel will check the details of the procedure and report back next
meeting.

&#42;&#42; &#42;Open Floor&#42;

\+ We will start to discuss and develop NFS service supported by
documentation and by Ansible.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-05-01/fedora-server.2024-05-01-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-05-01/fedora-server.2024-05-01-17.00.log.html)
&#42; *&#42;&#42;Actions summary&#42;&#42;* . &#42;Action&#42;: pboy
will file an issue with releng.

Wednesday, Apr 17, 2024

:   

&#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;LVM2 configuration &amp; ARM SBC installation&#42;

\+ The issue is resolved, but but - as Vojtech Trefny, one of ghe
maintgainers, put it - \'unfortunately not thanks to the changes that I
made\'.

\+ &#42;AGREED&#42;: Server WG considers the case closed.

&#42;&#42; &#42;Testing F40&#42;

\+ &#42;AGREED&#42;: Server WG considers F40 ready for publication and
closes this topic.

&#42;&#42; &#42;Our \'story\' for F40&#42;

\+ &#42;AGREED&#42;: Regarding our \'story\' for F40 we stick sich ARM
SBC.

&#42;&#42; &#42;Our \'Fedora Server goal(s) and \'story\' for F41 /
F42&#42;

\+ See: [issue &#35;134](https://pagure.io/fedora-server/issue/134)

\+ We narrowed the options down to \'Fedora Server VM as VPS\', \'Server
Edition as identity server \', and \'Server Edition as local or public
file server \'.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-04-17/fedora-server.2024-04-17-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-04-17/fedora-server.2024-04-17-17.00.log.html)

&#42; *&#42;&#42;Actions summary&#42;&#42;* . &#42;Action&#42;: pboy
will close [bug
&#35;2247872](https://bugzilla.redhat.com/show_bug.cgi?id=2247872)

Wednesday, Apr 03, 2024

:   

&#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Review installation media&#42;

\+ The discussion revealed obvious inconsistencies between the ways of
creating our various installation media that have evolved over time. All
of this is difficult to deal with in a matrix discussion. Therefore:

\+ &#42;AGREED&#42;: An additional meeting out of turn on Wednesday,
April 10, 17:00 UTC in the Matrix Sever room exclusively to discuss the
Review Installation Media topic.

\+ &#42;ACTION&#42;: pboy will prepare the room and provide a test
opportunity.

&#42;&#42; &#42;Testing F40&#42;

\+ No additional issues found yet, but not all planned tests have been
carried out yet.

\+ It is unclear how and where the test results should be merged on the
server test page. Pboy will contact Adam about this.

&#42;&#42; &#42;Revisiting Server installation media naming
convention&#42;

\+ The online/offline proposal is welcomed, but the overall solution
should be presented more clearly.

\+ A decision will be aimed for by mid-May at the latest so that there
is sufficient time for implementation.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-04-03/fedora-server.2024-04-03-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-04-03/fedora-server.2024-04-03-17.00.log.html)

Wednesday, Mar 20, 2024

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Follow-up actions &amp; announcements&#42;

\+ &#42;&#42;&#42; We will first discuss a possible change to the time
of our meetings on the mailing list and decide at the next meeting.

&#42;&#42; &#42;LVM2 configuration&#42;

\+ !link <https://bugzilla.redhat.com/show_bug.cgi?id=2247872>

\+ The /etc/lvm/devices directory in
Fedora-Server-KVM-40_Beta-1.9.x86_64.qcow2 is empty now. So far no check
whether First Boot generates a suitable entry.

\+ &#42;INFO update&#42;: Beta 1.10 contains a devices file in both
server images (KVM and aarch64 SBC). So the issue is not resolved yet.

\+ Action: cooltshirtguy will monitor and check the aarch64 SBC image,
specifically Raspberry Pi.

&#42;&#42; &#42;F40 release tests&#42;

\+ We have selected items to be tested and allocated work. Details at

\+ !link <https://pagure.io/fedora-server/issue/125/>

&#42;&#42; &#42;Open Floor&#42;

\+ &#42;!info&#42;: Unfortunately, no movement on the Apache / httpd
configuration layout yet

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-03-20/fedora-server.2024-03-20-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-03-20/fedora-server.2024-03-20-17.00.log.html)

Wednesday, Mar 06, 2024

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Follow-up actions &amp; announcements&#42;

\+ We are discussing how to equalize the times of the meetings of the
Server WG and the Epel Team to enable everyone to participate in both.
To be continued on the mailing list.

&#42;&#42; &#42;Review installation media&#42;

\+ An initial analysis has revealed a number of warning messages about
comps files not being found. Details in:

\+ Link:
<https://pagure.io/pungi-fedora/blob/main/f/variants-fedora.xml&#35;_46>

\+ Link: <https://pagure.io/fedora-server/issue/130>

\+ *Agreed*: Sever WG will check the current compose groups in issues on
fedora-server repo.

&#42;&#42; &#42;LVM2 configuration &amp; ARM SBC installation&#42;

\+ The arm-image-installer script is fixed.

\+ The LVM configuration issue is still open.

\+ Link: <https://bugzilla.redhat.com/show_bug.cgi?id=2247872&#35;c19>

\+ This issue is not accepted as release blocker. So it can happen that
we release a kind of crap image for the 2nd time in a row.

\+ But LVM group seems to be working hard on it.

&#42;&#42; &#42;F40 Change Set items requiring our attention&#42;

\+ Eseyman generated a list of items requiring our attention

\+ Link:
<https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/message/CNH57V7LT4GMQN676XFDJWQ6U46BGDMK/>

\+ *Agreed*: Server WG will continue to discuss this topic on mailing
list

&#42;&#42; &#42;Open Floor&#42;

\+ Nothing to discuss today.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-03-06/fedora-server.2024-03-06-18.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-03-06/fedora-server.2024-03-06-18.00.log.html)

Wednesday, Feb 21, 2024

:   Our first meeting on Matrix.

&#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Review installation media&#42;

\+ We are trying here for more then 2 years for now without a lot or
results. At Fosdem I met Tomáš, who is very experienced in release
engineering (to put it a bit understated) and who has offered to help us
with this. This is a great opportunity for Fedora Server Edition.

\+ After an initial discussion about necessary and desired changes, we
agreed that Tomáš would further analyze the current configuration files
and compile them in a blog or on the server list.

&#42;&#42; &#42;Revisiting Server installation media naming
convention&#42;

\+ The various server installation media are (still) named very
differently. But it is now too late for a change to Release 40.

\+ *Agreed*: We further discuss naming convention on mailing list and
aim to make a final decision in 4 weeks latest. And then it is up to
releng to find a workable timeframe. There is no urgency.

&#42;&#42; &#42;LVM2 default configuration change&#42;

\+ The issue is currently not resolved.

\+ A proper resolution will involve an anaconda fix as well as a fix in
arm-image-installer. We will continue to work on it.

\+ Link: <https://bugzilla.redhat.com/show_bug.cgi?id=2258764>

&#42;&#42; &#42;Open Floor&#42;

\+ Cloud Sig will stop to maintain ImageFactory. For F41 we have to
select another tool for building the non-iso images. Probable choices
are Lorax, KIWI, or OSBuild, depending on what is supported in pungi and
what artifacts are supported by the different tools.

\+ Neil would support a move to Kiwi if we decide to do so. We want to
make a final decision once releng has decided on available and supported
options.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-02-21/fedora-server.2024-02-21-18.03.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-02-21/fedora-server.2024-02-21-18.03.log.html)

Wednesday, Feb 07, 2024

:   Continuing the Jan 31 meeting

&#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;LVM2 default configuration change&#42;

\+ We finally got information about the reasons for the changes in LVM
default configuration and proper ways to resolve the ARM SBC
installation issue.

\+ In short we should retain the current default LVM configuration which
includes a system.devices file and adjust the arm-image-installer script
und our documentation.

&#42;&#42; &#42;Test planning for F40&#42;

\+ We have set up a [list of manually \'smoke
tests\'](https://hackmd.io/NtO4O9vRT3a71UMZMkceoA?both). We now need
working group members or other interested parties to take over some of
the tests and enter their FAS names in the corresponding column.

&#42;&#42; &#42;Open Floor&#42;

\+ We will switch our meetings from IRC to Matrix starting February 21,
provided we can make the necessary organizational arrangements in time.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/fedora-meeting/2024-02-07/fedora-server.2024-02-07-18.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/fedora-meeting/2024-02-07/fedora-server.2024-02-07-18.00.log.html)

&#42; *&#42;&#42;Actions summary&#42;&#42;* . eseyman will check the
change proposal set for items we should aware of and care about.

Wednesday, Jan 31, 2024

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;LVM2 default configuration change&#42;

\+ Currently the default LVM configuration results in vgscan and
vgchange not inspecting new devices that are not listed in
/etc/lvm/devices/system.devices. A follow-up to this is also the error
when creating aarch64 SBC filesystem images.

\+ There was neither a change proposal nor a release notes entry for the
configuration change, nor any announcement. Accordingly, it is also not
known why the change was made.

\+ &#42;ACTION&#42;: eseyman will try to contact the maintainers and get
information why the change was made.

&#42;&#42; &#42;Test planning for F40&#42;

\+ We will continue discussion next meeting

&#42;&#42; &#42;A \'story\' for each release&#42;

\+ We will continue discussion next meeting

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/fedora-meeting/2024-01-31/fedora-server.2024-01-31-18.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/fedora-meeting/2024-01-31/fedora-server.2024-01-31-18.00.log.html)

&#42; *&#42;&#42;Actions summary&#42;&#42;*

\+ New business

1.  pboy will create a thread on mailing list to discuss the option for
    LVM fix.

2.  jwhimpel will try to contact <linux-lvm@lists.linux.dev>

3.  pboy will create a draft wiki page to help to organise and
    coordinate our release testing efforts.

Wednesday, Jan 17, 2024

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;LVM configuration issues&#42;

\+ Currently the default LVM configuration results in vgscan and
vgchange not inspecting new devices that are not listed in
/etc/lvm/devices/system.devices. A follow-up to this is also the error
when creating aarch64 SBC filesystem images.

\+ There was neither a change proposal nor a release notes entry for the
configuration change, nor any announcement. Accordingly, it is also not
known why the change was made.

\+ &#42;ACTION&#42;: eseyman will try to contact the maintainers and get
information why the change was made.

&#42;&#42; &#42;Test planning for F40&#42;

\+ We will continue discussion next meeting

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/fedora-meeting/2024-01-17/fedora-server.2024-01-17-18.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/fedora-meeting/2024-01-17/fedora-server.2024-01-17-18.00.log.html)

&#42; *&#42;&#42;Actions summary&#42;&#42;* . pboy will write a info
about changing the timeout value and nirik will review -- still work in
progress . mowest will take care of discussed modifications of the
Server download page. - still work in progress . eseyman will try to
contact the maintainers and get information why the change was made.

# Meeting Minutes 2023 {#_meeting_minutes_2023}

Stephen Daley; Peter Boy

Wednesday, Dec 06, 2023

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Next meeting on January 19, 2024!&#42;

&#42;&#42; &#42;Fedora Server release and quality criteria&#42;

\+ We want to further discuss this on mailing list and in the ticket.
&#42;&#42; &#42;Work program and goals for F40&#42;

\+ Various ideas discussed, further discussion on the mailing list and
in the ticket . &#42;&#42; &#42;Test planning for F40&#42;

\+ Extensive discussion without a conclusive result yet. Discussion to
be continued at the next meeting.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/fedora-meeting/2023-11-15/fedora-server.2023-11-15-18.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/fedora-meeting/2023-11-15/fedora-server.2023-11-15-18.00.log.html)

&#42; *&#42;&#42;Actions summary&#42;&#42;* . *ACTION*: Mowest will take
care ot disussed modifications of the Server download page.

Wednesday, Nov 15, 2023

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Fedora release 39 - State of Server media and Download
Web page&#42;

\+ The Situation regarding aarch64 on SBC is a bit better then 2 weeks
ago, but still but still not satisfactory. A SBC is now installable if
you don't use an installation host with actrive LVM drives, but use e.g.
Fedora Workstation. In this respect, it would be disproportionate to
continue to regard this as a release blocker. The problem must now be
solved for Release 40.

\+ It's really unfortunate, that we discovered the bug so late in the
Beta process. We need to review our testing procedures. We have relied
too much on the automated tests.

\+ For the next release we should improve the download page. We need to
find a better name as the outdated term \'DVD\' and should clearly
distinguish the SBC variant from the other installations, it is best to
introduce a separate section.

\+ ACTION: Mowest will take care ot disussed modifications of the Server
download page.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/fedora-meeting/2023-11-15/fedora-server.2023-11-15-18.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/fedora-meeting/2023-11-15/fedora-server.2023-11-15-18.00.log.html)

&#42; *&#42;&#42;Actions summary&#42;&#42;* . *ACTION*: Mowest will take
care ot disussed modifications of the Server download page.

Wednesday, Nov 01, 2023

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Fedora release 39 rc current state and how to
continue&#42;

\+ The x86_64 versions work great. There is still a severe bug with
installing the aarch64 SBC version on Fedora Server.

\+ *AGREED*: If the LVM issue can not be resolved for f39 release,
Server WG would like to opt out providing a f39 installation medium for
aarch SBC, continue to distribute f38 and encourage to update using dnf.

&#42;&#42; &#42;Package fail2ban orphaned&#42;

\+ In the meantime the orphaned package was picked by a new maintainer.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/fedora-meeting/2023-11-01/fedora-server.2023-10-11-01.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/fedora-meeting/2023-11-01/fedora-server.2023-11-01-17.00.log.html)

&#42; *&#42;&#42;Actions summary&#42;&#42;*

\+ none

Wednesday, Oct 18, 2023

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Maximum size of aarch64 Server network install
image&#42;

\+ *AGREED*: Enlarge aarch64 net install media to 1 GB. Letting
everything else as is.

&#42;&#42; &#42;Fedora release 39 beta first experience and how to
continue&#42;

\+ Mowest has tested the x86_64 installation image and pb the VM image.
No issues found.

\+ There is still an issue with the aarch64 on SBC version. pboy will
check.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/fedora-meeting/2023-10-18/fedora-server.2023-10-18-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/fedora-meeting/2023-10-18/fedora-server.2023-10-18-17.00.log.html)

&#42; *&#42;&#42;Actions summary&#42;&#42;*

\+ none

Wednesday, Sep 20, 2023

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Follow up actions&#42; . Ongoing: pboy will write a info
about how to configure the timeout value and nirik will review. git+
Nothing to announce today.

&#42;&#42; &#42;F40 Change proposal dropping sshd.socket file&#42;

\+ ACTION: jwhimpel will keep an eye on behalf of Server WG on the
\'Change proposal dropping sshd.socket file\' discussion.

&#42;&#42; &#42;Fedora release 39 beta first experience and how to
continue&#42;

\+ ACTION: jdubby will deploy some of the wildfly quickstarts via
localhost and report at our next meeting.

&#42;&#42; &#42;F39/40 Work Project: Fedora Server in a virtualized
runtime environment &#42;

\+ ACTION: mowest and pboy will prepare a community action about Fedora
Server in a virtualized runtime environment

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/fedora-meeting/2023-09-20/fedora-server.2023-09-20-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/fedora-meeting/2023-09-20/fedora-server.2023-09-20-17.00.log.html)

&#42; *&#42;&#42;Actions summary&#42;&#42;* . *ACTION*: Ongoing pboy
will write a info about how to configure the timeout value and nirik
will review . *ACTION*: jwhimpel will keep an eye on behalf of Server WG
on the \'Change proposal dropping sshd.socket file\' discussion. .
*ACTION*: mowest and pboy will prepare a community action about Fedora
Server in a virtualized runtime environment

Wednesday, Sep 06, 2023

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Follow up actions&#42; . Ongoing: pboy will write a info
about how to configure the timeout value and nirik will review. git+
Nothing to announce today.

&#42;&#42; &#42;F39 Work Project: Fedora Server on (ARM) SBC&#42;

\+ ACTION: pboy will complete the intro text about Fedora Server and ARM
SBC

&#42;&#42; &#42;Work Project: Using Ansible to install and configure
Wildfly&#42;

\+ ACTION: jdubby will deploy some of the wildfly quickstarts via
localhost and report at our next meeting.

&#42;&#42; &#42;Fedora release 39 test planning&#42;

\+ ACTION: pboy will open a mailing list thread about F39 change set to
review changes and come up with a list of those that affect server
edition

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/fedora-meeting/2023-09-06/fedora-server.2023-09-06-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/fedora-meeting/2023-09-06/fedora-server.2023-09-06-17.00.log.html)

&#42; *&#42;&#42;Actions summary&#42;&#42;* . *ACTION*: Ongoing pboy
will write a info about how to configure the timeout value and nirik
will review . *ACTION*: pboy will complete the intro text about Fedora
Server and ARM SBC . *ACTION*: jdubby will deploy some of the wildfly
quickstarts via localhost and report at our next meeting. . *ACTION*:
pboy will open a mailing list thread about F39 change set to review
changes and come up with a list of those that affect server edition

Wednesday, Aug 16, 2023

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Follow up actions&#42; . Ongoing: pboy will write a info
about how to configure the timeout value and nirik will review. git+
Nothing to announce today.

&#42;&#42; &#42;F39 Work Project: Fedora Server on (ARM) SBC (&#42;

\+ pboy will write a first draft of the first part of the text about
Server on SBC (Purpose and summary of the literature). Further
discussion on mailing list,

&#42;&#42; &#42;Work Project: Using Ansible to install and configure
Wildfly&#42;

\+ The certificate issue got resolved. Next step is installation and
configuration of the proxy (nginx). Detailed discussion on mailing list.

&#42;&#42; &#42;Fedora release 39 test planning&#42;

\+ After the first impression, there is no potentially critical change
that requires our special attention and testing.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/fedora-meeting/2023-08-16/fedora-server.2023-08-16-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/fedora-meeting/2023-08-16/fedora-server.2023-08-16-17.00.log.html)

&#42; *&#42;&#42;Actions summary&#42;&#42;* . *ACTION*: Ongoing pboy
will write a info about how to configure the timeout value and nirik
will review

Wednesday, Jul 19, 2023

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Follow up actions&#42; . Ongoing: pboy will write a info
about how to configure the timeout value and nirik will review. . Done:
eseyman will review the NFS documentation &#42;&#42;
&#42;Announcement&#42;

\+ Nothing to announce today.

&#42;&#42; &#42;Fedora 39 change Proposal: Enable Firmware Update
Notification&#42;

\+ In a short discussion we had voted 7:0:0 in favour of the change. To
add an email notification is currently useless, because we don't install
any email capability by default.

&#42;&#42; &#42;LLMNR should be disabled in resolved in f39&#42;

\+ Nirik and pboy are to formulate a solution on behalf of the WG.

&#42;&#42; &#42;Work Project: Using Ansible to install and configure
Wildfly&#42;

\+ We made various decisions

&#42;&#42;&#42; We'll use nginx as proxy solution, because it is able to
handle the proxy protocol. &#42;&#42;&#42; pboy asks Java SIG about best
practise for a installation location. &#42;&#42;&#42; We will create a
separate log. Volume for /opt/wildfly according the Fedora Server
Edition storage concept

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/fedora-meeting/2023-07-19/fedora-server.2023-07-19-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/fedora-meeting/2023-07-19/fedora-server.2023-07-19-17.00.log.html)

Wednesday, Jul 05, 2023

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Follow up actions&#42; . Ongoing: pboy will write a info
about how to configure the timeout value and nirik will review. .
Ongoing: eseyman will review the NFS documentation - still WIP
&#42;&#42; &#42;Announcement&#42;

\+ AS it looks at the moment the committee has accepted and is planning
with a presentation: Fedora Server Edition -- Quo Vadis? Unfortunately a
workshop about Server in virtual environment, that I proposed, too,
didn't make it.

&#42;&#42; &#42;Could we drop Active Directory requirements from Fedora
release criteria?&#42;

\+ &#42;Agreed&#42; WG agrees about to use automated testing using Samba
AD as the server end (instead of a native Windows server) and to keep
the status of release criteria.

\+ Full compatibility with Windows Server remains the goal regardless of
the testing procedure. And an *inability to connect to a real Microsoft
AD server remains a release blocking criterion*, since that is (and
remains) the most prominent domain controller in the world.

&#42;&#42; &#42;F39 Work Project: Fedora Server on (ARM) SBC&#42;

\+ We'll complete the current device documentation draft with the
devices nominated until now.

\+ &#42;&#42; &#42;Open Floor&#42;

\+ We want to replace the \'DVD\' in the naming of the installation
media by \'STD\'.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/fedora-meeting/2023-07-05/fedora-server.2023-07-05-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/fedora-meeting/2023-07-05/fedora-server.2023-07-05-17.00.log.html)
&#42; *&#42;&#42;Actions summary&#42;&#42;* . *ACTION*: Ongoing pboy
will write a info about how to configure the timeout value and nirik
will review

Wednesday, Jun 21, 2023

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Follow up actions&#42; . Ongoing: pboy will write a info
about how to configure the timeout value and nirik will review. .
Ongoing: eseyman will review the NFS documentation - still WIP
&#42;&#42; &#42;Announcement&#42;

\+ pboy has submitted a talk and a workshop idea to Flock

&#42;&#42; &#42;F39 Work Project: Fedora Server on (ARM) SBC&#42;

\+ W'll compose a devices list.

\+ ACTION eseyman to post his ARM SBC list to the list by next week.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/fedora-meeting/2023-06-21/fedora-server.2023-06-21-17.02.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/fedora-meeting/2023-06-21/fedora-server.2023-06-21-17.02.log.html)
&#42; *&#42;&#42;Actions summary&#42;&#42;* . *ACTION*: Ongoing pboy
will write a info about how to configure the timeout value and nirik
will review

Wednesday, Jun 07, 2023

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Follow up actions&#42; . Ongoing: pboy will write a info
about how to configure the timeout value and nirik will review.
&#42;&#42; &#42;Announcement&#42;

\+ This year's Flock will be in-person Aug. 2-4 in Cork, Ireland. We'll
discuss our contribution on mailing list and next meeting.

&#42;&#42; &#42;F39 Work Project: Fedora Server on (ARM) SBC&#42;

\+ *AGREED*: The WG agrees on part 1 of the plan in issue 108 and will
create a reference list.

\+ W'll start a list of desirable or available devices in a comment to
on tracking issue &#35;108.

\+ W'll consider the Phoronix list of tests for comparison.

&#42;&#42; &#42;Using Ansible to install and configure Wildfly&#42;

\+ We postpone working on it until July, when jwhimpel has time again.
&#42;&#42; &#42;F39/40 Work Project: Fedora Server in a virtualized
runtime environment&#42;

\+ *AGREED*: WG will perform the community survey as proposed in
&#35;110 .

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/fedora-meeting/2023-06-07/fedora-server.2023-06-07-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/fedora-meeting/2023-06-07/fedora-server.2023-06-07-17.00.log.html)
&#42; *&#42;&#42;Actions summary&#42;&#42;* . *ACTION*: Ongoing pboy
will write a info about how to configure the timeout value and nirik
will review

Wednesday, May 03, 2023

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Follow up actions&#42; . Ongoing: pboy will write a info
about how to configure the timeout value and nirik will review.

&#42;&#42; &#42;Fedora Server goal(s) for F39&#42;

\+ *AGREED*: WG will pursue \'Fedora Server Edition on SBC\' as first
priority for F39, and \'Fedora Server Edition in virtualized
environments\' as 2nd priority.

&#42;&#42; &#42;\'Each Edition has a story for each release\'&#42;

\+ *AGREED*: WG will pursue \'Fedora Server Edition on SBC\' as the
\'story\' for F39 with first priority, \'Fedora Server Edition in
Virtuialized environments\' with 2nd priority.

\+ *ACTION*: pboy will post a first draft regarding \'Fedora Server
Edition on SBCs\' on hackmd.io for further discussion.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/fedora-meeting/2023-05-03/fedora-server.2023-05-03-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/fedora-meeting/2023-05-03/fedora-server.2023-05-03-17.00.log.html)
&#42; *&#42;&#42;Actions summary&#42;&#42;* . *ACTION*: Ongoing pboy
will write a info about how to configure the timeout value and nirik
will review . *ACTION*: pboy will post a first draft regarding \'Fedora
Server Edition on SBCs\' on hackmd.io for further discussion.

Wednesday, April 19, 2023

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Follow up actions&#42; . Ongoing: pboy will write a info
about how to configure the timeout value and nirik will review.

&#42;&#42; &#42;\'Each Edition has a story for each release\'&#42;

\+ On [mailing
list](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/VILYMWVJ7GVHOSLP3C3YC42S3G7JACM4/)
we have a first info and a draft collection of ideas. The challenge is
not so much the \'story\' part, but the \'every release\' part.

\+ *ACTION*: eseyman will try and think up something for next meeting

&#42;&#42; &#42;Fedora Server goal(s) for F39&#42;

\+ *AGREED*: We evaluate 2 options for F39: ServerVM support for various
hosting services and Usage of SBC as a Server device

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/fedora-meeting/2023-04-19/fedora-server.2023-04-19-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/fedora-meeting/2023-04-19/fedora-server.2023-04-19-17.00.log.html)
&#42; *&#42;&#42;Actions summary&#42;&#42;* . *ACTION*: Ongoing pboy
will write a info about how to configure the timeout value and nirik
will review . *ACTION*: eseyman will try and think up something for next
meeting

Wednesday, April 05, 2023

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Follow up actions&#42; . Ongoing: pboy will write a info
about how to configure the timeout value and nirik will review.

&#42;&#42; &#42;F38 Beta testing&#42;

\+ We are fine with F38 and should not experience any surprises.

&#42;&#42; &#42;Shorter Shutdown Timer&#42;

\+ *Nirik* created a PR as decided. It is pushed to stable and will be
included in the installation media.

&#42;&#42; &#42;Fedora Website revamp -- Fedora Server Edition
pages&#42;

\+ AGREED: Server WG would like to get a \'Documentation\' button/link
between Download and Community in the hero graphic

\+ AGREED: Server WG is content with the feature list and descriptions.

&#42;&#42; &#42;Using Ansible to install and configure Wildfly&#42;

\+ We will start thinking about how we're going to get these ansible
roles/playbooks into our users\' hands.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/fedora-meeting/2023-04-05/fedora-server.2023-04-05-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/fedora-meeting/2023-04-05/fedora-server.2023-04-05-17.00.log.html)
&#42; *&#42;&#42;Actions summary&#42;&#42;* . Ongoing: pboy will write a
info about how to configure the timeout value and nirik will review

Wednesday, March 15, 2023

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Follow up actions&#42; . No open actions

&#42;&#42; &#42;Shorter Shutdown Timer&#42;

\+ AGREED: to take the same route as CoreOS and keep the old default
value. (+3, 0, -2 )

\+ ACTION: pboy will write a info about how to configure the timeout
value and nirik will review

&#42;&#42; &#42;Fedora Website revamp -- Fedora Server Edition
pages&#42;

\+ We are still missing a documentation button and link. The feature
list needs some improvement.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/fedora-meeting/2023-03-15/fedora-server.2023-03-15-18.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/fedora-meeting/2023-03-15/fedora-server.2023-03-15-18.00.log.html)
&#42; *&#42;&#42;Actions summary&#42;&#42;* . pboy will write a info
about how to configure the timeout value and nirik will review

Wednesday, March 01, 2023

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Follow up actions&#42; . Ongoing: nirik to look up the
services in our technical specification and check for time out value .
Ongoing: pboy to create a ticket to collect our central messages for the
new web site.

&#42;&#42; &#42;Shorter Shutdown Timer&#42;

\+ We are still evaluating the possible impact and current configuration
of the core services.

\+ We want to add to our documentation how to make changes to the
.service file if someone has an issue.

\+ &#42;action&#42; pboy will create a summary of our discussion about
service specific timeouts.

\+ &#42;action&#42; pboy will open a mailing list discussion about
interdependencies between services and the consequences.

&#42;&#42; &#42;Using Ansible to install and configure Wildfly&#42;

\+ We have still 2 unresolved issues:

\+ &#8230;. a. TLS between apache and Wildfly web app b. Ansiblify
Wildfly &#8230;.

\+ &#42;action&#42; jdubby will update his Ansible/Wildfly repo

\+ &#42;action&#42; eseyman will look at the updated repo

\+ &#42;action&#42; pboy will provide a public server where we can work
in a cooperative work on all the details

&#42;&#42; &#42;Fedora Website revamp -- Fedora Server Edition
pages&#42;

\+ We are generally very content with the current state of the
[completed
draft](https://fedora.gitlab.io/websites-apps/fedora-websites/fedora-websites-3.0/server/).
Mowest informed that the design group considers it \'near final\'.
Anyway we can request changes after the F38 rollout.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/fedora-meeting/2023-02-15/fedora-server.2023-02-15-18.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/fedora-meeting/2023-02-15/fedora-server.2023-02-15-18.00.log.html)
&#42; *&#42;&#42;Actions summary&#42;&#42;* . pboy to create a ticket to
collect our central messages for the new web site . nirik to look up the
services in our technical specification and check for time out value .
pboy pboy will create a summary of our discussion about service specific
timeouts. . pboy will open a mailing list discussion about
interdependencies between services and the consequences. . jdubby will
update his Ansible/Wildfly repo . eseyman will look at the updated repo
. pboy will provide a public server where we can work in a cooperative
work on all the details

Wednesday, February 15, 2023

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Follow up actions&#42; . nirik to look up the services
in our technical specification and check for time out value . pboy to
create a ticket to collect our central messages for the new web site.

&#42;&#42; &#42;Fedora Website revamp -- Fedora Server Edition
pages&#42;

\+ Mowest informs about the availability of a [first complete
draft](https://fedora.gitlab.io/websites-apps/fedora-websites/fedora-websites-3.0/server/),
although still with some placeholders. The discussion about [further
development](https://gitlab.com/fedora/design/team/wwwfpo-2022/-/issues/23&#35;note_1276926623)
is still ongoing. The current topic is the design of the header. We
agree that it should express as well as possible the universality and
wide scope of Fedora Server Edition (from SBC to SME to Data Center).

\+ Next step is the finetuning of the mission statements.

&#42;&#42; &#42;Shorter Shutdown Timer&#42;

\+ We are still evaluating the possible impact and current configuration
of the core services.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/fedora-meeting/2023-02-15/fedora-server.2023-02-15-18.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/fedora-meeting/2023-02-15/fedora-server.2023-02-15-18.00.log.html)
&#42; *&#42;&#42;Actions summary&#42;&#42;* . pboy to create a ticket to
collect our central messages for the new web site . nirik to look up the
services in our technical specification and check for time out value .
pboy to create a list of our core services in the issue for further
discussion

Wednesday, February 01, 2023

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Fedora Website revamp -- Fedora Server Edition
pages&#42;

\+ Mowest made contact with the revamp team. We are now in the flow to
work on it. See the [current
mockup](https://fedora.gitlab.io/websites-apps/fedora-websites/fedora-websites-3.0/server/)!
The texts are a first draft. The graphical assets are mostly
placeholders.

\+ You can also follow the [ongoing conversation about the current
status of the website
design](https://gitlab.com/fedora/design/team/wwwfpo-2022/-/issues/23).
To give feedback, please use our [pagure issue
&#35;66](https://pagure.io/fedora-server/issue/66)!

\+ Next actions:

a.  Review text right now and give suggestions for changes.

b.  Mowest will inform us Emma (the designer) has some of the graphic
    assets ready for review.

c.  Suggestions or ideas for graphic assets that could be used next to
    each of our \'feature points\' as suggestions to the graphics team.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/fedora-meeting/2023-02-01/fedora-server.2023-02-01-18.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/fedora-meeting/2023-02-01/fedora-server.2023-02-01-18.00.log.html)

Wednesday, January 18, 2023

:   &#42; *&#42;&#42;Essentials at a glance&#42;&#42;*

&#42;&#42; &#42;Shorter Shutdown Timer&#42;

\+ We will first review the Core Services of our current [\'*Technical
Specification*\'](docs/server-technical-specification.xml) to see what
configuration is implemented for a shutdown. Furthermore, we will
consider conducting a test tag on this point, although implementation is
likely to be difficult. Depending on the findings, we will decide on the
further handling of the magnitude of the default timeout.

\+ We found contradictions resp. ambiguities about the exact
configuration of the current timeout configuration in Server. Nirik will
clarify this.

\+ *Actions*

1.  nirik will look up the services in our technical specification and
    check for time out value

&#42;&#42; &#42;Fedora Server web site revamp&#42;

\+ Mowest made contact with the revamp team and introduced himself as
Server contact. We are now in the flow to work on it.

\+ The next step is to collect content for our pages. Mowest asks to
contribute key ideas, messages, mission statements for the content of
the page. We prefer professional, meaningful texts, not rather
content-less marketing phrases, which can be found partly on some newly
designed pages.

\+ *Actions*

1.  pboy to create a ticket to collect our central messages for the new
    web site.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/fedora-meeting/2023-01-18/fedora-server.2023-01-18-18.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/fedora-meeting/2023-01-18/fedora-server.2023-01-18-18.00.log.html)
&#42; *&#42;&#42;Actions summary&#42;&#42;*

1.  nirik will look up the services in our technical specification and
    check for time out value

2.  pboy to create a ticket to collect our central messages for the new
    web site.

&#42;&#42;Keep in mind&#42;&#42;: We had moved the time of our meeting
in UTC so that the same local time of day is maintained after the DST
changeover, that means currently 18:00 UTC.

# Meeting Minutes {#_meeting_minutes}

Stephen Daley, Peter Boy :page-authors: {author}

Wednesday,December 21, 2022

:   &#42; *Summary info*

    1.  &#42;Follow up actions&#42;

        *INFO*: No outstanding action item.

    2.  &#42;Using Ansible to install and configure Wildfly&#42;

        *ACTION*: jwhimpel will continue to work on Ansible roles .

    3.  &#42;Server WG work program for upcoming year&#42;

        Continued discussion.

        *ACTION*: eseyman take a look at the work program over the
        holidays

        *ACTION*: jwhimpel will continue to work on Ansible roles

        *ACTION*: eseyman wants to focus on Identity Management for the
        first half of 2023

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/fedora-meeting/2022-12-21/fedora-server.2022-12-21-18.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/fedora-meeting/2022-12-21/fedora-server.2022-12-21-18.00.log.html)

&#42;&#42;Note&#42;&#42;: We moved the time of our meeting to UTC so,
that the same local time of day is maintained after the DST changeover,
that means 18:00 UTC.

Wednesday,December 07, 2022

:   &#42; *Summary info*

    1.  &#42;Follow up actions&#42;

        *INFO*: No outstanding action items

    2.  &#42;Server critical path definition proposal&#42;

        We will review the current version and likely add items as soon
        as we have made progress in reviewing and updating our release
        and quality criteria - now that the technical specifications
        have been updated.

    3.  &#42;Server WG work program for upcoming year&#42;

        Possible focus areas as currently discussed (should be continued
        on the mailing list):

        &#42;&#42; Keeping documentation up to date. &#42;&#42; Using
        Ansible to install and configure Wildfly &#42;&#42; Fedora
        Website Revamp - Fedora Server part &#42;&#42; Review
        installation media

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/fedora-meeting/2022-12-07/fedora-server.2022-12-07-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/fedora-meeting/2022-12-07/fedora-server.2022-12-07-17.00.log.html)

&#42;&#42;Note&#42;&#42;: We are moving the time of our meeting to UTC
so that the same local time of day is maintained after the DST
changeover, that means 18:00 UTC.

Wednesday,October 19, 2022

:   &#42; *Summary info*

    1.  &#42;Follow up actions&#42;

        *INFO*: \@eseyman and \@pboy will keep trying hard to replicate
        and check the Wildfly certificate issue.

    2.  &#42;Release 37 Beta testing&#42;

        *info*: Installation issue with GPT and software RAID are
        resolved.

        *info*: Old systemd-nspawn related bugs are basically resolved
        (bugzilla 1900888, 1900869), but not yet completely

        *info*: The new ServerVM works fine.

        *agreed*: Server Edition rc 1.2 is ready for release.

    3.  &#42;Documentation update Release 37&#42;

        *info*: The most important installation articles are reviewed
        and updated.

        *agreed*: For next release we determine the 5 articles mostly in
        need of an review and work on them on a documentation day in
        &#35;fedora-server.

    4.  &#42;Server critical path definition proposal&#42;

        We will continue the mailing list discussion.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/fedora-meeting/2022-10-19/fedora-server.2022-10-19-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/fedora-meeting/2022-10-19/fedora-server.2022-10-19-17.00.log.html)

Wednesday,October 05, 2022

:   &#42; *Summary info*

    1.  &#42;Follow up actions&#42;

        *INFO*: All our open actions are about the next topics.

    2.  &#42;Release 37 Beta testing&#42;

        *action*: cmurf will test the new ServerVM F37

        SWraid installation on biosBoot GPT has been fixed, needs final
        testing.

    3.  &#42;Documentation update Release 37&#42;

        \@mowest reviewed 2 docs (local install and post installation).
        They are now significantly improved. Reveals the relevance of
        the review process.

    4.  &#42;Using Ansible to install and configure Wildfly&#42;

        There is still an issue with the certificate. eseyman and pboy
        will additionally test it.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/fedora-meeting/2022-10-05/fedora-server.2022-10-05-17.01.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/fedora-meeting/2022-10-05/fedora-server.2022-10-05-17.01.log.html)

Wednesday,September 21, 2022

:   &#42; *Summary info*

    1.  &#42;Follow up actions&#42;

        *INFO*: No outstanding action items

    2.  &#42;Release 37 Beta testing&#42;

        We have assigned various test tasks among us. For details see
        &#35;actions in the minutes below.

    3.  &#42;Documentation update Release 37&#42;

        \@mowest will begin reviewing docs, especially those not
        associated in the release 37 test items.

    4.  &#42;Release criteria, test procedures and systematization of
        tests&#42;

        We agreed to strive for systematization using the test weeks
        tools. Details should first be discussed on the mailing list.

&#42; [Meeting
summary](https://meetbot.fedoraproject.org/fedora-meeting/2022-09-21/fedora-server.2022-09-21-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/fedora-meeting/2022-09-21/fedora-server.2022-09-21-17.00.log.html)

Wednesday,September 07, 2022

:   &#42; *Summary info*

    1.  &#42;Follow up actions&#42;

        *INFO*: No outstanding action items

    2.  &#42;Release 37 Beta testing&#42;

        It is verified the [software raid
        bug](https://bugzilla.redhat.com/show_bug.cgi?id=2088113) is a
        release blocker. Not solved yet, but it is being worked on.

    3.  &#42;Server VM status and the way forward&#42;

        Thanks to *nirik* we have a Server VM x86_64 and s390 image in
        F37 and in Rawhide. It was a kind of last minute rescue after a
        rather [bumpy
        ride](https://pagure.io/fedora-kickstarts/pull-request/905). And
        thanks to *sgallagh* for support in the not so easy way to get
        the kick-start file done at all.

        The kick-start failed on ppc64le and aarch64, unfortunately. The
        cause is likely to be different partitioning requirements, but
        the PR for a customized kick-start file was [hanging
        again](https://pagure.io/fedora-kickstarts/pull-request/915).

        We will need to review the current experience for its impact on
        our plan to update the server distribution media. Under the
        current circumstances, implementation seems quite unrealistic or
        at least extremely costly and time-consuming.

&#42; [Detailed
agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/P2NNNFYFKIWCKZOPJ3FGHCEIMSDFI3QO/)
&#42; [Meeting
summary](https://meetbot.fedoraproject.org/fedora-meeting/2022-09-07/fedora-server.2022-09-07-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/fedora-meeting/2022-09-07/fedora-server.2022-09-07-17.00.log.html)

Wednesday, August 17, 2022

:   &#42; *Summary info*

    1.  &#42;Follow up actions&#42;

        *INFO*: No outstanding action items

    2.  &#42;Final decision about an updated Fedora Server Technical
        Specification&#42;

        It was consensus, that the document is not immutable and thus
        change be changed later if ideas for improvements surface later.
        Therefore, a decision now and start with the next tasks.

        *AGREED*: WG agrees about the techn.spec. in the current
        version, with alt. 1 for section 1.2 and editorial adaptations
        as discussed today.

    3.  &#42;Using Ansible to install and configure Wildfly&#42;

        This is a key component of our \'Supported by Ansible"-project
        (Server Roles), which has taken a back seat to everyday issues
        for far too long.

        jwhimpel has developed a playbook where currently there is still
        a problem with Letsencrypt certificates to be fixed.

        *ACTION*: jwhimpel will provide access to the playbook on GitHub
        so we can re-play the installation and test it.

&#42; [Detailed
agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/2UM3SYJ5BPMUSZJMBTNND5UZCGBSNS3E/)
&#42; [Meeting
summary](https://meetbot.fedoraproject.org/fedora-meeting/2022-08-17/fedora-server.2022-08-17-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/fedora-meeting/2022-08-17/fedora-server.2022-08-17-17.00.log.html)

Wednesday, July 20, 2022

:   &#42; *Summary info*

    1.  &#42;Follow up actions&#42;

        *INFO*: No outstanding action items

    2.  &#42;Review current Fedora Server Technical Specification&#42;

        We agreed about all suggestions in comments with the exception
        of the final wording of section 1.2 (File System and Storage
        Organization). We will open a discussion about the wording of
        section 1.2 on mailing list.

        *ACTION*: pboy will create a next version of the techn. spec.
        containing our agreements today.

&#42; [Detailed
agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/2DK7BTZZUOASGMU35TJUSYWDZILV7DRV/)
&#42; [Meeting
summary](https://meetbot.fedoraproject.org/fedora-meeting/2022-07-20/fedora-server.2022-07-20-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/fedora-meeting/2022-07-20/fedora-server.2022-07-20-17.00.log.html)

Wednesday, July 06, 2022

:   &#42; *Summary info*

    1.  &#42;Follow up actions&#42;

        *DONE*: Change proposal to add Server VM is accepted

        *INFO*: Tracking bug
        <https://bugzilla.redhat.com/show_bug.cgi?id=2100621>

        *INFO*: Change Proposal regarding the default hostname
        configuration is accepted by FESCo

        *DONE*: pboy to add test of uefi sw raid
        (<https://pagure.io/fedora-server/issue/89>)

    2.  &#42;Software Raid on UEFI systems&#42;

        *AGREED*: We use the Anaconda solution with raid, for the time
        beeing. Further evaluation on mailing list and next meeting.

    3.  &#42;Review current Fedora Server Technical Specification&#42;

        Discussion to continue next meting

    4.  &#42;Open Floor&#42;

&#42; [Detailed
agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/W5ACQXVPR3KOHISJC47LNB53KPJU7ISM/)
&#42; [Meeting
summary](https://meetbot.fedoraproject.org/fedora-meeting/2022-07-06/fedora-server.2022-07-06-17.01.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/fedora-meeting/2022-07-06/fedora-server.2022-07-06-17.01.log.html)

Wednesday, June 15, 2022

:   &#42; *Summary info*

    1.  &#42;Follow up actions&#42;

        *ONGOING*: Change proposal to add Server VM is still processing
        ( [discussion
        thread](https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/M2YQMVVUCFCV4MMOQ32UMSM5WBBVE2H7/)
        )

        *INFO*: There is now a Change Proposal regarding the default
        hostname configuration ( [discussion
        thread](https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/Y2TT6VZPGTD5UVGPA6PLNYW2BU4JOC77/)
        )

        *AGREED*: Server WG is content with the default hostname change
        proposal

    2.  &#42;Further processing of GPT as default partitioning
        switch&#42;

        *ACTION*: pboy to add test of uefi sw raid with LVM RAID
        (instead of standard raid)

        *ACTION*: pboy files a bug about sw raid in uefi mode

        Discussion of unversal boot configuration postponed until
        current problems are solved.

    3.  &#42;Test planning for Fedora 37&#42;

        *AGREED*: Server WG will strive for a test week for F38 and
        follow up releases

        First step is a final review of the updated Technical
        Specification next meeting, followed by an update of our release
        and test criteria.

    4.  &#42;How to proceed with Cockpit File Sharing module NFS
        part&#42;

        link: <https://pagure.io/fedora-server/issue/86>

        Due to the elapsed time further discussion postponed.

    5.  &#42;Open Floor&#42;

&#42; [Detailed
agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/THLAKBXD6YEVGH2NDN4ZOCS3K7TYX3V4/)
&#42; [Meeting
summary](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2022-06-15-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2022-06-15-17.00.log.html)

Wednesday, June 01, 2022

:   &#42; *Summary info*

    1.  &#42;Follow up actions&#42;

        *DONE*: Post on devel list thread F37 proposed change to GPT as
        default partitioning schema about the regression regarding
        software raid installations.
        <https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/DIU6IKPCPD2BXDUFDZUZ2G2ZQNT5JW57/>

        *DONE*: Created an issue containing 2 test cases for biosboot
        GPT software raid installations
        <https://pagure.io/fedora-server/issue/87>

        *DONE*: created a stub of NFS server installation and Cockpit
        for administration

        *ONGOING*: Created Change proposal to add Server VM is still
        processing

        *ONGOING*: Discussion about changes around the default hostname
        configuration

        *ONGOING*: Review of the dnsmasq documentation by eseyman

    2.  &#42;Change proposal about GPT as default partitioning for bios
        boot&#42;

        *LINK*:
        <https://fedoraproject.org/wiki/Changes/GPTforBIOSbyDefault>

        Discussion:
        <https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/VSM473WRHKIIIJYZZCVXAO7XFS4ACHPH/>

        FESCo has accepted the Change Proposal without discussion. We
        now have the problem of preserving our users from harm
        unfortunately done intentionally or, at best, negligently by
        some of our own members who are owners of the Change Proposal.
        Unfortunately, the perpetrators do now not care how harm can be
        averted from our users with Release 37 and do not even bother to
        attend the meeting on this topic to find a suitable resolution
        if the issue.

        Stephen Gallagher started a process to qualify the Anaconda
        software raid bug as a blocker to the GPT Change Proposal. If
        accepted by QA as a blocker, it will have to be fixed (or the
        Change reverted) in order to ship Fedora. This would be a
        perfect and constructive solution.

        *Agreed*: Server WG agrees with sgallagh's suggestion to block
        the GPT change until the Anaconda issue is resolved and
        considers it as most essential.

    3.  &#42;Planning for Fedora 37: Additional changes to discuss?
        (continued)&#42;

        For part of the discussion we have a new tracking issue:
        [&#35;88](https://pagure.io/fedora-server/issue/88) , It
        summarizes all the individual measures that we have discussed
        for improvement and entail an adjustment of the installation
        media.

        Agreed: Issue &#35;88 is postponed to F38

        There are various new bug reports regarding the size of
        installation media, very similar to those on F36. We'll ask Adam
        about it, He resolved those issues for F36.

    4.  &#42;How to proceed with Cockpit File Sharing module NFS
        part&#42;

        link: <https://pagure.io/fedora-server/issue/86>

        Due to the elapsed time further preparatory discussion via
        e-mail.

    5.  &#42;Open Floor&#42;

&#42; [Detailed
agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/RFUVXGX4XFUJQFAN4QC3JNIYKPTL66GS/)
&#42; [Meeting
summary](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2022-06-01-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2022-06-01-17.00.log.html)

Wednesday, May 18, 2022

:   &#42; *Summary info*

    1.  &#42;Follow up actions&#42;

        *INFO*: We voted successfully for 4 new members: cooltshirtguy,
        dcavalca, eseyman, mowest, a very warm welcome. Our list of
        members is already updated.

        *ONGOING*: Created Change proposal to add Server VM is still
        processing in preparation phase

        *ONGOING*: Discussion about changes around the default hostname
        configuration

    2.  &#42;Change proposal about GPT as default partitioning for bios
        boot&#42; *LINK*:
        <https://fedoraproject.org/wiki/Changes/GPTforBIOSbyDefault>

        Discussion:
        <https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/Q2ZBWG3YESG4POYAAZVUKSWMZHG3R7KW/>
        TBD

        *Agreed*: Server WG insists that before switching to GPT as
        default for BIOS boot, it is tested, that Anaconda supports a
        software raid setup smoothly.

    3.  &#42;Planning for Fedora 37: Additional changes to discuss?
        (continued)&#42;

        There is an RFE
        (<https://bugzilla.redhat.com/show_bug.cgi?id=2054625>) pending
        to include some additional packages to the full installation
        DVD, which led to a discussion which packages to add and whether
        we accept a further increase of the downloads.

        Agreed: We combine all installation content related issues and
        actions into one new ticket.

        Action: pboy to create a new ticket about installation media
        content review

    4.  &#42;How to proceed with Cockpit File Sharing module&#42;

        link: <https://pagure.io/fedora-server/issue/86>

        Discussion:
        <https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/T75AU7FLZMDUBMXOD3AXSC4VCYIJ6ZMA/>

        Agreed: We will divide the topic in several steps and start with
        nfs.

        We'll start with completing our documentation with installing
        and maintening a nfs server. Pboy will provide a ToC proposal.

    5.  &#42;Open Floor&#42;

        Eseyman will start to review the dnsmasq documentation article
        with the goal to extend it about setup of an PXE server. Mowest
        is about to document his setup of a WOL configuration.

&#42; [Detailed
agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/R3VWDITZ6A23ZJXWJTUFUWJLGGV6K5W2/)
&#42; [Meeting
summary](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2022-05-18-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2022-05-18-17.00.log.html)

Wednesday, May 04, 2022

:   &#42; *Summary info*

    1.  &#42;Follow up actions&#42;

        *ONGOING*: Created Change proposal to add Server VM

        *DONE*: Supplement to our Product requirements Document (PRD)

        *DONE and ONGOING*: Voting about new members (open until
        Thursday,05 05:00 UTC).

        *DONE*: Withdrawal of nb and mhoungbo from member list

    2.  &#42;Evaluation of our test efforts for F36&#42;

        We agreed, we did better than with F35 and want to further
        improve with F37. Will open a follow-up discussion on mailing
        list.

    3.  &#42;Planning for Fedora 37: Additional changes to discuss?&#42;

        There is an RFE
        (<https://bugzilla.redhat.com/show_bug.cgi?id=2054625>) pending
        to include some additional packages to the full installation
        DVD, which led to a discussion which packages to add and whether
        we accept a further increase of the downloads.

        *Agreed*: Continue discussion on mailing list.

    4.  Open Floor

        x3mboy raised the question of migrating our repository to
        gitlab.

        *Agreed*: discuss on mailing list

&#42; [Detailed
agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/RQIB4PW64KVMD376224UWLHWICTBL3TW/)
&#42; [Meeting
summary](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2022-05-04-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2022-05-04-17.00.log.html)

Wednesday, April 20, 2022

:   &#42; *Summary info*

    1.  &#42;Follow up actions&#42;

        *DONE*: withdrew Ben Williams from the list of approved members
        as he had wanted. Many thanks for his contributions.

        *DONE*: Opened a discussion about Cockpit and the file-sharing
        update follow ups on mailing list.

        *DONE*: Opened a discussion thread about a specification for a
        Server Edition VM on mailing list.

    2.  &#42;Planning for Fedora 37: Introducing a Server VM KVM virtual
        disk image&#42;

        <https://pagure.io/fedora-server/issue/79>

        *Agreed*: WG decides to add a Fedora Server Edition VM image and
        to make a corresponding Change proposal.

        *Action*: pboy creates a change proposal to add a Fedora Server
        Edition VM image

        *Agreed*: WG decides to amend the PRD as proposed in ticket 83

        *Action*: pboy edits the PRD to amend as in issue &#35;83 and
        initializes the required processing

    3.  &#42;Evaluating Fedora Server Working Group&#42;

        <https://pagure.io/fedora-server/issue/67>

        *Agreed*: WG agrees to open a voting on the admision of
        cooltshirtguy, dcavalca, eseyman and mowest in one go.

        *Action*: pboy start a voting the admision of cooltshirtguy,
        dcavalca, eseyman and mowest in one go.

        *Agreed*: WG agrees to withdraw nb and mhoungbo for the time
        being (&#35;67). Many thanks to both of them for their
        willingness to work on the Server WG.

        *Action*: Withdrawal of nb and mhoungbo from member list.

    4.  &#42;Discussion of a potential change to Fedora surrounding the
        default hostname&#42;

        *Agreed*: salimma and Eighth_Doctor work with Dusty and probably
        others to explore the possibilities to get the old behaviour
        (pre f33) back.

    5.  &#42;Current discussion about withdrawal of BIOS boot for new
        installations in F37&#42;

        There was a longer discussion about the subject. And the largely
        unanimous position was that we still need bios boot for a longer
        time for various reasons. Everything must be done to find a
        technical solution that makes this possible under the condition
        of available resources.

        *Agreed*: Davide Cavalca and Michel Alexandre Salim volunteer to
        work further on the subject.

&#42; [Detailed
agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/XZBPD436FYFTKU5L6QVUEN2WBCORICQF/)
&#42; [Meeting
summary](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2022-04-20-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2022-04-20-17.00.log.html)

Wednesday, April 06, 2022

:   &#42; *Summary info*

    1.  &#42;Follow up actions&#42;

        *Info*: Had an IRC chat with Ben Williams (jbwillia). He is busy
        with other projects and we agreed he will withdraw from server
        WG. So I will remove him from our list. (see
        [&#35;67](https://pagure.io/fedora-server/issue/67)).

        *Action*: Will withdraw Ben Williams from the list of approved
        members for the time being.

        *DONE*: Withdrew Subhendu Ghosh from the list of approved
        members for the time being. &#42; *DONE*: pb and sgallagh
        resolved the installation issue with virtualization.

    2.  &#42;Fedora 36 tests&#42;

        *Info*: &lt;cooltshirtguy&gt; takes over testing AD from
        &lt;sgallagh&gt; for the F36 test cycle

        *Info*: &lt;eseyman&gt; still testing OpenLDAP

        *Info*: &lt;pboy&gt; No issues found with libcirt / postgreSQL /
        java / Tomcat

        *Agreed*: WG will join the Upgrade test day Thursday, April 14.
        Member will test on their own \'real world\' configurations

    3.  &#42;Cockpit file-sharing update Change Proposal follow up&#42;

        *Agreed*: We close issue
        [&#35;73](https://pagure.io/fedora-server/issue/73) as completed
        and done.

        *Info*: &lt;sgallagh&gt; has it on his (long) backlog to add the
        Cockpit Application stuff to the file-sharing

        *Agreed*: We open a discussion thread about file-sharing update
        followup actions on mailing list

    4.  &#42;Planning Fedora 37&#42;

        *Info*: There is a hot discussion about withdrawel of bios boot
        for F37.

        We will dedicate a own topic about that next meeting

        Regarding our own plannings:

        &#42;&#42; [&#35;53](https://pagure.io/fedora-server/issue/53)
        (\'Facilitated and improved support for Fedora Server Edition
        VMs\', pboy)

        There is a
        [comment](https://pagure.io/fedora-server/issue/79&#35;comment-790978)
        with some specification to add a Fedora Server Edition disk
        image to our deliverables as part of out Fedora 37 work.

        *Agreed*: Open a discussion thread about
        <https://pagure.io/fedora-server/issue/79&#35;comment-790978>
        and decide next meeting

&#42; [Detailed
agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/565ZBHTE3TCNLTJYGMQEY7Q4CWQ2KOZ6/)
&#42; [Meeting
summary](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2022-04-06-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2022-04-06-17.00.log.html)

Wednesday, March 16, 2022

:   &#42; *Summary info*

    1.  &#42;Follow up actions&#42;

        *Info*: Startet to contact members who had not been with us for
        longer than a half year und didn't contribute anything (see
        [&#35;67](https://pagure.io/fedora-server/issue/67)).

        *Info*: Tried to contact Subhendu Ghosh (sghosh). There is no
        FAS account and no mail address available.

        *Agreed*: We withdraw Subhendu Ghosh from the list of approved
        members for the time being.

    2.  &#42;Fedora 36 tests&#42;

        *Action*: sgallagh and pboy work on &#35;80

        *Action*: &lt;jwhimpel&gt; The migration to the \'next
        generation\' of ansible seems to be working fine.

    3.  &#42;Planning Fedora 37&#42;

        *Result*: Special interests exist so far in

        &#42;&#42; [&#35;53](https://pagure.io/fedora-server/issue/53)
        (\'Facilitated and improved support for Fedora Server Edition
        VMs\', pboy)

        &#42;&#42; [&#35;54](https://pagure.io/fedora-server/issue/54)
        (\'Include automatic notification of updates (dnf-automatic) in
        Fedora Server\', cooltshirtguy)

&#42; [Detailed
agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/2MXO25NSLOVKH7O3OU2JB4QRZWPB44AN/)
&#42; [Meeting
summary](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2022-03-16-17.00.html)
&#42; [Full
log](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2022-03-16-17.00.log.html)

Wednesday, March 02, 2022

:   Standing meeting about &#42; Check F36 changes and known issues -
    final pass

    *Result*: Composed final list of F36 changes to specifically take
    care of &#42; Specifying F36 manual test requirements - final pass

    *Result*: Final composition of a list of task &amp; manual tests to
    be applied to F36 Beta &#42; Review current Fedora Server Technical
    Specification -- second pass

    *Result*: First draft proposal adopted as is, continue with
    completion of TBDs

    Details

    &#42;&#42; [Meeting
    summary](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2022-03-02-17.08.html)
    &#42;&#42; [Detailed
    agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/SVZCL47QI3DINKADPN3OGESW72DAIQRK/)
    &#42;&#42; [Full
    log](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2022-03-02-17.08.log.html)

Wednesday, February 16, 2022

:   Standing meeting about &#42; Cockpit file-sharing update Change
    Proposal &#42; Specifying F36 manual test requirements

    Details

    &#42;&#42; [Meeting
    summary](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2022-02-16-17.00.html)
    &#42;&#42; [Detailed
    agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/SVZCL47QI3DINKADPN3OGESW72DAIQRK/)
    &#42;&#42; [Full
    log](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2022-02-16-17.00.log.html)

Wednesday, February 02, 2022

:   Standing meeting about &#42; Current status of Fedora Server User
    Docs Update &#42; Using Ansible to install and configure Wildfly
    &#42; Review current Fedora Server Technical Specification

    Details

    &#42;&#42; [Meeting
    summary](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2022-02-02-17.01.html)
    &#42;&#42; [Detailed
    agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/QSGS6B22VQBHZGPL6HJPYXMW7O5O7LWC/)
    &#42;&#42; [Full
    log](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2022-02-02-17.01.log.html)

Wednesday, January 19, 2022

:   Standing meeting about &#42; Current status of Fedora Server User
    Docs Update &#42; Current changeset F36, possible specific impacts
    on Server &#42; Review current Fedora Server Technical Specification

    Details

    &#42;&#42; [Meeting
    summary](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2022-01-19-17.01.html)
    &#42;&#42; [Detailed
    agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/W3CVVA2JQFYFX7FI6EJ7YBTOLBZJHVSZ/)
    &#42;&#42; [Full
    log](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2022-01-19-17.01.log.html)

# Meeting Minutes from 2020-2021 {#_meeting_minutes_from_2020_2021}

Stephen Daley, Peter Boy :page-authors: {author}

Wednesday, December 15, 2021

:   Standing meeting about &#42; Migrating WG Wiki Pages to
    docs.fedoraproject.org

    Details

    &#42;&#42; [Meeting
    summary](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2021-12-01-17.00.html)
    &#42;&#42; [Detailed
    agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/KWEP6EL4VEDZK3GO5LAEVXQOUL4DBYUD/)
    &#42;&#42; [Full
    log](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2021-12-01-17.00.log.html)

Wednesday, December 1, 2021

:   Standing meeting about &#42; Migrating WG Wiki Pages to
    docs.fedoraproject.org &#42; Review current Fedora Server Technical
    Specification &#42; Facilitated and improved support for Fedora
    Server Edition VMs

    Details

    &#42;&#42; [Meeting
    summary](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2021-12-01-17.00.html)
    &#42;&#42; [Detailed
    agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/KWEP6EL4VEDZK3GO5LAEVXQOUL4DBYUD/)
    &#42;&#42; [Full
    log](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2021-12-01-17.00.log.html)

Wednesday, November 17, 2021

:   Standing meeting about &#42; Moving Wiki Pages to
    docs.fedoraproject.org &#42; Preparing Fedora Release 36 &#42;
    Facilitated deployment of key services by combining rpm and Ansible

    Details

    &#42;&#42; [Meeting
    summary](https://meetbot.fedoraproject.org/fedora-meeting/2021-11-17/fedora-server.2021-11-17-17.00.html)
    &#42;&#42; [Detailed
    agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/B36Q2AACPSRNS4DF4MQ7BQHCG5LTF7T5/)
    &#42;&#42; [Full
    log](https://meetbot.fedoraproject.org/fedora-meeting/2021-11-17/fedora-server.2021-11-17-17.00.log.html)

Wednesday, September 15, 2021

:   Standing meeting about &#42; Follow up actions &#42; Fedora 35: Max
    size arm-32 exceeded, install media blocked &#42; Facilitated
    deployment of key services by combining rpm and Ansible

    Details

    &#42;&#42; [Meeting
    summary](https://meetbot.fedoraproject.org/fedora-meeting/2021-09-15/fedora-server.2021-09-15-17.00.html)
    &#42;&#42; [Detailed
    agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/A5FMNBDH5R4ADXGZYVNV7TOGIBDP3FDJ/)
    &#42;&#42; [Full
    log](https://meetbot.fedoraproject.org/fedora-meeting/2021-09-15/fedora-server.2021-09-15-17.00.log.html)

Wednesday, September 1, 2021

:   Standing meeting about &#42; Follow up actions &#42; Fedora 35: Max
    size arm-32 exceeded, install media blocked &#42; Facilitated
    deployment of key services by combining rpm and Ansible

    Details

    &#42;&#42; [Meeting
    summary](https://meetbot.fedoraproject.org/fedora-meeting/2021/fedora-meeting.2021-09-01-17.00.html)
    &#42;&#42; [Detailed
    agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/6JS7MSAECHVZZZWJU2J5AEISMQBDXLJZ/)
    &#42;&#42; [Full
    log](https://meetbot.fedoraproject.org/fedora-meeting/2021/fedora-meeting.2021-09-01-17.00.log.html)

Wednesday, August 18, 2021

:   Standing meeting about &#42; Follow up actions &#42; Facilitated
    deployment of key services by combining rpm and Ansible &#42; Work
    planning update

    Details

    &#42;&#42; [Meeting
    summary](https://meetbot.fedoraproject.org/fedora-meeting/2021-08-18/fedora-server.2021-08-18-17.00.html)
    &#42;&#42; [Detailed
    agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/WVRMJ3PVBRR44WLQEK5BNYJ2GU7UYT7R/)
    &#42;&#42; [Full
    log](https://meetbot.fedoraproject.org/fedora-meeting/2021-08-18/fedora-server.2021-08-18-17.00.log.html)

Wednesday, August 4, 2021

:   Standing meeting about &#42; Follow up actions &#42; Facilitated
    deployment of key services by combining rpm and Ansible

    Details

    &#42;&#42; [Meeting
    summary](https://meetbot.fedoraproject.org/fedora-meeting/2021-08-04/fedora-server.2021-08-04-17.00.html)
    &#42;&#42; [Detailed
    agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/PWJNVPZYMAAQZWJZQKB5TDWE5KYY7ID4/)
    &#42;&#42; [Full
    log](https://meetbot.fedoraproject.org/fedora-meeting/2021-08-04/fedora-server.2021-08-04-17.00.log.html)

Wednesday, July 21, 2021

:   Standing meeting about &#42; Open ticket 32 about composition of
    installation media &#42; Work on Fedora 35

    Details

    &#42;&#42; [Meeting
    summary](https://meetbot.fedoraproject.org/fedora-meeting/2021-07-21/fedora-server.2021-07-21-17.00.html)
    &#42;&#42; [Full
    log](https://meetbot.fedoraproject.org/fedora-meeting/2021-07-21/fedora-server.2021-07-21-17.00.log.html)

Wednesday, July 07, 2021

:   Meeting about Ongoing Work Projects &#42; Status of ongoing
    activities (some housekeeping) &#42; Fedora Server Documentation

    Details

    &#42;&#42; [Meeting
    summary](https://meetbot.fedoraproject.org/fedora-meeting/2021-07-07/fedora-server.2021-07-07-17.00.html)
    &#42;&#42; [Full
    log](https://meetbot.fedoraproject.org/fedora-meeting/2021-07-07/fedora-server.2021-07-07-17.00.log.html)

Wednesday, June 23, 2021

:   Meeting about Ongoing Work Projects &#42; Fedora Server Product
    Requirement Document (PRD) &#42; Fedora Server Documentation &#42;
    Fedora Website - revamp

    Details

    &#42;&#42; [Meeting
    summary](https://meetbot.fedoraproject.org/fedora-meeting/2021-06-23/fedora-server.2021-06-23-16.59.html)
    &#42;&#42; [Detailed
    agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/TPYYUQJ6WFU5QSMOLD7Z36NDZAIDBGE6/)
    &#42;&#42; [Full
    log](https://meetbot.fedoraproject.org/fedora-meeting/2021-06-23/fedora-server.2021-06-23-16.59.log.html)

Wednesday, June 9, 2021

:   Meeting about Ongoing Work Projects &#42; Fedora Server Release 35
    &#42; Deploying services via RPM and Ansible &#42; Fedora Server
    documentation review

    Details

    &#42;&#42; [Meeting
    summary](https://meetbot.fedoraproject.org/fedora-meeting/2021-06-09/fedora-server.2021-06-09-17.00.html)
    &#42;&#42; [Detailed
    agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/ZE3F2U6J5PRB6RISC67DIWTAE2TFQU35/)
    &#42;&#42; [Full
    log](https://meetbot.fedoraproject.org/fedora-meeting/2021-06-09/fedora-server.2021-06-09-17.00.log.html)

Wednesday, June 2, 2021

:   Meeting about Ongoing Work Projects &#42; Explore opportunities for
    cooperation with Cloud WG &#42; Deploying services via RPM and
    Ansible &#42; Fedora Server documentation review

    Details

    &#42;&#42; [Meeting
    summary](https://meetbot.fedoraproject.org/fedora-meeting/2021-06-02/fedora-server.2021-06-02-17.00.html)
    &#42;&#42; [Detailed
    agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/message/WF54CWXOL6HLNJDXL5FUZTWPH46CIC63/)
    &#42;&#42; [Full
    log](https://meetbot.fedoraproject.org/fedora-meeting/2021-06-02/fedora-server.2021-06-02-17.00.log.html)

Wednesday, May 26, 2021

:   Meeting about Future Fedora Server Releases &#42; Deploying services
    via RPM and Ansible

    Details

    &#42;&#42; [Meeting
    summary](https://meetbot.fedoraproject.org/fedora-meeting/2021-05-26/fedora-server.2021-05-26-17.13.html)
    &#42;&#42; [Detailed
    agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/message/LO45JYWU7WJLQ7U3XHSLPQJBT6RNLX4G/)
    &#42;&#42; [Full
    log](https://meetbot.fedoraproject.org/fedora-meeting/2021-05-26/fedora-server.2021-05-26-17.13.log.html)

Wednesday, May 19, 2021

:   Meeting about Future Fedora Server Releases &#42; Issue release
    composition &#42; Planning for next Fedora release(s)

    Details

    &#42;&#42; [Meeting
    summary](https://meetbot.fedoraproject.org/fedora-meeting/2021-05-19/fedora-server.2021-05-19-17.00.html)
    &#42;&#42; [Detailed
    agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/IX6ZBBURUUIQNV72LKCUUWZPB4Q4JPA2/)
    &#42;&#42; [Full
    log](https://meetbot.fedoraproject.org/fedora-meeting/2021-05-19/fedora-server.2021-05-19-17.00.log.html)

Wednesday, May 12, 2021

:   Meeting about Fedora Server PRD and future Fedora Server Releases
    &#42; PRD - various reviewer questions to discuss &#42; Planning for
    next Fedora release(s)

    Details

    &#42;&#42; [Meeting
    summary](https://meetbot.fedoraproject.org/fedora-server/2021-05-12/fedora-server.2021-05-12-17.00.html)
    &#42;&#42; [Detailed
    agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/KF2CTZMLFQAJTQIGDQIYQEAVAIYNAHYB/)
    &#42;&#42; [Full
    log](https://meetbot.fedoraproject.org/fedora-server/2021-05-12/fedora-server.2021-05-12-17.00.log.html)

Wednesday, May 05, 2021

:   Meeting about Fedora Server Releases &#42; Planning for next Fedora
    release(s) &#42; Fedora release criteria and process

    Details

    &#42;&#42; [Meeting
    summary](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2021-05-05-17.00.html)
    &#42;&#42; [Detailed
    agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/EAUPYMONTWRFIZSR4HPPI2TE5FZXGWDT/)
    &#42;&#42; [Full
    log](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2021-05-05-17.00.log.html)

Wednesday, April 28, 2021

:   Meeting about Status PRD Update and Fedora Server Release &#42;
    Status Server PRD (Info) &#42; Fedora release criteria and process
    &#42; New Issue: Release composition

    Details

    &#42;&#42; [Meeting
    summary](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2021-04-28-17.00.html)
    &#42;&#42; [Detailed
    agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/32IQLMZDPUS7JCF2FFRVJO5IAYYQLEL4/)
    &#42;&#42; [Full
    log](https://meetbot.fedoraproject.org/fedora-meeting/2021-04-28/fedora-server.2021-04-28-17.00.log.html)

Wednesday, April 21, 2021

:   Meeting about PRD Update and Fedora Server Release &#42; PRD Update
    second pass &#42; Fedora release criteria and process &#42; Planing
    for next Fedora release

    Details

    &#42;&#42; [Meeting
    summary](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2021-04-21-17.00.html)
    &#42;&#42; [Detailed
    agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/OXWV357OY4ZCC4EFNPU3H4HZRRQIHVZS/)
    &#42;&#42; [Full
    log](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2021-04-21-17.00.log.html)

Wednesday, April 14, 2021

:   Meeting about Mainly Continuation of the last meeting's agenda &#42;
    PRD update discussion &#42; Status F34 release &#42; Status new
    documentation

    Details

    &#42;&#42; [Meeting
    summary](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2021-04-14-17.00.html)
    &#42;&#42; [Detailed
    agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/J7YI5OSM67O5RKMASL3BWUFMK43OBVCU/)
    &#42;&#42; [Full
    log](https://meetbot.fedoraproject.org/fedora-meeting/2021-04-14/fedora-server.2021-04-14-17.00.log.html)

Wednesday, April 07, 2021

:   Meeting about continuation of the last meeting's agenda &#42; PRD
    Update Proposal &#42; Collaboration with Cloud WG

    Details

    &#42;&#42; [Meeting
    summary](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2021-04-07-17.01.html)
    &#42;&#42; [Detailed
    agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/LRI6LNKJZYXTS4SUUOZ7NMSIHUWRKM77/)
    &#42;&#42; [Full
    log](https://meetbot.fedoraproject.org/fedora-meeting/2021-04-07/fedora-server.2021-04-07-17.01.log.html)

Wednesday, March 31, 2021

:   Meeting about continuation of the last meeting's agenda &#42; PRD
    Update Proposal &#42; New Documentation

    Details

    &#42;&#42; [Meeting
    summary](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2021-03-31-17.00.html)
    &#42;&#42; [Detailed
    agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/JMZY2TI3W6QMKDPNSZ2SRQN5QDW46A4A/)
    &#42;&#42; [Full
    log](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2021-03-31-17.00.log.html)

Wednesday, March 24, 2021

:   Meeting about continuation of the last meeting's agenda &#42;
    Documentation Update &#42; PRD Update Proposal

    Details

    &#42;&#42; [Meeting
    summary](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2021-03-24-17.00.html)
    &#42;&#42; [Full
    log](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2021-03-24-17.00.log.html)

Wednesday, March 17, 2021

:   Meeting about continuation of the last meeting's agenda &#42; Work
    needed for Fedora 34 &#42; PRD Update Proposal

    Details

    &#42;&#42; [Meeting
    summary](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2021-03-17-18.00.html)
    &#42;&#42; [Detailed
    agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/G7OMZFSWAYTYV2OP7ZEK3K4WGWAEKWV3/)
    &#42;&#42; [Full
    log](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2021-03-17-18.00.log.html)

Wednesday, March 3, 2021

:   Meeting about &#42; Status Reboot Server Working Group &#42;
    Introduce Dusty Mabe from Cloud Group

    Details

    &#42;&#42; [Meeting
    summary](https://meetbot.fedoraproject.org/fedora-meeting/2021-03-03/fedora-server.2021-03-03-18.04.html)
    &#42;&#42; [Detailed
    agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/HKMAODK32EQC3MDGLAAVA4LSXAIN2WCM/)
    &#42;&#42; [Full
    log](https://meetbot.fedoraproject.org/fedora-meeting/2021-03-03/fedora-server.2021-03-03-18.04.log.html)

Wednesday, February 17, 2021

:   Meeting about &#42; Status Reboot Server Working Group &#42; Work
    program for the coming year &#42; PRD Update (first round of
    discussion)

    Details

    &#42;&#42; [Meeting
    summary](https://meetbot.fedoraproject.org/fedora-meeting/2021-02-17/fedora-server.2021-02-17-17.58.html)
    &#42;&#42; [Detailed
    agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/RQWDTIBDAUUK63HYIHLBHGJEMROSELOE/)
    &#42;&#42; [Full
    log](https://meetbot.fedoraproject.org/fedora-meeting/2021-02-17/fedora-server.2021-02-17-17.58.log.html)

Wednesday, February 3, 2021

:   Meeting about &#42; Housekeeping &#42; Wiki Update

    Details

    &#42;&#42; [Meeting
    summary](https://meetbot.fedoraproject.org/fedora-meeting/2021-02-03/fedora-server.2021-02-03-18.15.html)
    &#42;&#42; [Full
    log](https://meetbot.fedoraproject.org/fedora-meeting/2021-02-03/fedora-server.2021-02-03-18.15.log.html)

Wednesday, January 20, 2021

:   Meeting about &#42; Status PRD Update &#42; Improving Fedora Server
    documentation and visibility &#42; systemd-oomd

    Details

    &#42;&#42; [Meeting
    summary](https://meetbot.fedoraproject.org/fedora-meeting/2021-01-20/fedora_server.2021-01-20-17.02.html)
    &#42;&#42; [Full
    log](https://meetbot.fedoraproject.org/fedora-meeting/2021-01-20/fedora-server.2021-01-20-17.02.log.html)

Wednesday, December 16, 2020

:   Fedora Server Reboot Meeting &#42; Introduction, Quick Hello, the
    Agenda &#42; Basic Framework for What's Needed &#42; Round of
    Introductions (Who you are, what you're interested in) &#42;
    Existing Fedora Server WG &#42; Volunteers to actually be on the
    Working Group &#42; Volunteers for practical action: reviewing and
    updating the PRD

    Details

    &#42;&#42; [Meeting
    summary](https://meetbot.fedoraproject.org/teams/serversig/serversig.2020-12-16-18.00.html)
    &#42;&#42; [Full
    log](https://meetbot.fedoraproject.org/teams/serversig/serversig.2020-12-16-18.00.log.html)

# Meeting Minutes from 2013 {#_meeting_minutes_from_2013}

Stephen Daley, Peter Boy

Thursday, December 19, 2013

:   &#42; *&#42;&#42;Agenda&#42;&#42;* &#42;&#42; &#42;PRD: Use
    Cases&#42; &#42; [Meeting
    minutes](https://lists.fedoraproject.org/pipermail/server/2013-December/000657.html)
    &#42; [Full
    log](https://meetbot.fedoraproject.org/fedora-meeting-1/2013-12-19/fedora-meeting-1.2013-12-19-14.59.log.html)

<!-- -->

Tuesday, December 17, 2013

:   &#42; *&#42;&#42;Agenda&#42;&#42;* &#42;&#42; &#42;Final Assessment
    of Personas&#42; &#42;&#42; &#42;PRD: Delivery Plan&#42; &#42;&#42;
    &#42;PRD: Delivery Plan - Delivery Media&#42; &#42;&#42;
    &#42;Delivery Plan: Release Cadence&#42; &#42; [Meeting
    minutes](http://meetbot.fedoraproject.org/fedora-meeting-1/2013-12-17/fedora-meeting-1.2013-12-17-16.00.html)
    &#42; [Full
    log](https://meetbot.fedoraproject.org/fedora-meeting-1/2013-12-17/fedora-meeting-1.2013-12-17-16.00.log.html)

<!-- -->

Tuesday, December 10, 2013

:   &#42; *&#42;&#42;Agenda&#42;&#42;* &#42;&#42; &#42;Backup and
    Monitoring&#42; &#42;&#42; &#42;what goes in the PRD&#42; &#42;&#42;
    &#42;Personas&#42; &#42; [Meeting
    minutes](http://meetbot.fedoraproject.org/fedora-meeting-1/2013-12-10/fedora-meeting-1.2013-12-10-15.59.html)
    &#42; [Full
    log](https://meetbot.fedoraproject.org/fedora-meeting-1/2013-12-10/fedora-meeting-1.2013-12-10-15.59.log.html)

<!-- -->

Tuesday, December 3, 2013

:   &#42; *&#42;&#42;Agenda&#42;&#42;* &#42;&#42; &#42;Adam Williamson
    Confirmation&#42; &#42;&#42; &#42;Discuss Role Implementation&#42;
    &#42; [Mailing list
    thread](https://lists.fedoraproject.org/pipermail/server/2013-December/000631.html)
    &#42; [Meeting
    minutes](http://meetbot.fedoraproject.org/fedora-meeting-1/2013-12-03/fedora-meeting-1.2013-12-03-15.59.html)

<!-- -->

Tuesday, November 26, 2013

:   &#42; *&#42;&#42;Agenda&#42;&#42;* &#42;&#42; &#42;Select a new
    member of the Working Group&#42; &#42;&#42; &#42;Personas&#42; &#42;
    [Mailing list
    thread](https://lists.fedoraproject.org/pipermail/server/2013-November/000614.html)
    &#42; [Meeting
    minutes](https://meetbot.fedoraproject.org/fedora-meeting-1/2013-11-26/fedora-meeting-1.2013-11-26-16.00.html)

<!-- -->

Tuesday, November 19, 2013

:   &#42; *&#42;&#42;Agenda&#42;&#42;* &#42;&#42; &#42;Goals for Server
    Role Installation&#42; &#42;&#42; &#42;Personas&#42; &#42;&#42;
    &#42;Server Lifecycle Proposal&#42; &#42;&#42; &#42;Updates and
    Testing Proposal&#42; &#42;&#42; &#42;Server Role List Proposal&#42;
    &#42;&#42; &#42;Installation Roles vs. Post-installation Role
    Assignment&#42; &#42; [Mailing list
    thread](https://lists.fedoraproject.org/pipermail/server/2013-November/000535.html)
    &#42; [Full
    log](https://meetbot.fedoraproject.org/fedora-meeting-1/2013-11-19/fedora-meeting-1.2013-11-19-16.00.log.html)

<!-- -->

Tuesday, November 12, 2013

:   &#42; *&#42;&#42;Agenda&#42;&#42;* &#42;&#42; &#42;Can a single
    server have multiple roles?&#42; &#42;&#42; &#42;Installation of
    base + roles&#42; &#42; [Mailing list
    thread](https://lists.fedoraproject.org/pipermail/server/2013-November/000514.html)
    &#42; [Full
    log](https://meetbot.fedoraproject.org/fedora-meeting-1/2013-11-12/fedora-meeting-1.2013-11-12-16.02.log.html)

<!-- -->

Tuesday, November 5, 2013

:   &#42; *&#42;&#42;Agenda&#42;&#42;* &#42;&#42; &#42;Finalizing the
    Governance Charter: Membership (Group representation and terms)&#42;
    &#42;&#42; &#42;Is Fedora Server One Product?&#42; &#42; [Blog
    summary](https://blog.linuxgrrl.com/2013/11/05/fedora-server-working-group-nov-5-meeting-2/)
    &#42; [Mailing list
    thread](https://lists.fedoraproject.org/pipermail/server/2013-November/000425.html)
    &#42; [Full
    log](https://meetbot.fedoraproject.org/fedora-meeting-1/2013-11-05/fedora-meeting-1.2013-11-05-16.02.log.html)

<!-- -->

Wednesday, October 30, 2013

:   &#42; *&#42;&#42;Agenda&#42;&#42;* &#42;&#42; &#42;Meeting frequency
    and times&#42; &#42;&#42; &#42;Ticket Tracker/Wiki&#42; &#42;&#42;
    &#42;Governance Charter&#42; &#42;&#42; &#42;Open Floor&#42; &#42;
    [Blog
    summary](https://blog.linuxgrrl.com/2013/10/30/fedora-server-working-group-initial-meeting-minutes/)
    &#42; [Mailing list
    thread](https://lists.fedoraproject.org/pipermail/server/2013-October/000313.html)
    &#42; [Full
    log](http://meetbot.fedoraproject.org/fedora-meeting-1/2013-10-30/fedoraserverwg.2013-10-30-17.00.log.html)

# User Documentation Maintenance {#_user_documentation_maintenance}

The Fedora Server Edition working group; Peter Boy (pboy); Stephen Daley
(mowest) :page-authors: {author}, {author_2}, {author_3}

> Part of the Server Edition Working Group's tasks is to create and
> maintain user documentation. This is intended to enable or facilitate
> users to use the services offered in accordance with our technical
> specifications safely and correctly. Here we describe the basic
> structure of this work and thereby enable all users to contribute to
> the documentation.

## Goals {#_goals}

We want to and maintain a Fedora Server Edition user documentation and
keep it up to date on an ongoing basis that

&#42; focuses on the specific features and procedures of the Fedora
Server Edition &#42; also includes brief explanations and rationales
that convey the meaning and underlying concepts &#42; contains
copy-and-paste capable instructions that allow even less experienced
administrators to operate safely and reliably &#42; refers to the
upstream documentation for general information, where available

## Organization {#_organization}

Fedora uses Antorra CMS to create its documentation website. To enable
authors to contribute to web pages even without solid knowledge of web
design, Antorra uses simpler texts written in AsciiDoc, which are
automatically converted into complex HTML pages. These texts are stored
in Git repositories.

The AsciiDoc source texts for the Fedora Server user documentation are
located at <https://forge.fedoraproject.org/server/user-documentation>.

The public user documentation is available at
<https://docs.fedoraproject.org/en-US/fedora-server/>

## Contributions {#_contributions}

Authors as well as users should be able to contribute to Fedora Server
documentation with as little effort as possible and without technical
hurdles. We provide several ways to contribute.

1.  The most common way for casual contributions is to *open a ticket*
    and describe the issue, and maybe to make a proposal.

2.  Contact the Working Group in our Matrix room.

3.  Edit the page in question using a *Web-based page editor*.

4.  Set up and work in a *local authoring environment* on your desktop.

5.  You may send us an email, e.g. while reading a document on our Web
    pages.

### Open a ticket (problem report) {#_open_a_ticket_problem_report}

When reading a document, you see a \'bug\' button on the rightmost side
below the blue top bar. Click it and you are forwarded to create an
issue. Members of the Working Group are notified and will take care of
it. However, you must have a Fedora account, so you can log in.

### Write in the Fedora Server Matrix room {#_write_in_the_fedora_server_matrix_room}

Open your Web Browser and visit the [Fedora Server Matrix
room](https://matrix.to/&#35;/&#35;server:fedoraproject.org). You can
either use the Web Interface or switch to the Element App. This is an
asynchronous communication channel. It may take some time for someone to
respond.

### Edit a page via a Web Editor {#_edit_a_page_via_a_web_editor}

Besides the aforementioned \'bug\' button there is a button that
stylizes pen and note. It leads to a web-based editor that can be used
to make changes to this very page. These are not applied directly, but
members of the documentation team are notified for a review. For
detailed information see chapter [Working with the Web based page
editor](usr-docs-maintenance/webui-page-editor.xml)

### Working in a local authoring environment {#_working_in_a_local_authoring_environment}

For longer-term engagement, it makes sense to set up a complete
authoring environment. It requires some preparations, but it provides
the most powerful set of tools. The article [Local
Authoring](usr-docs-maintenance/local-authoring.xml) has some tips to
get you started.

### Authenticating with Forgejo {#_authenticating_with_forgejo}

Git actions happen via HTTPS on forge.fedoraproject.org. Here is a quick
way to get set up. Note: These instructions assume you already have git
up and running, but you need to configure it to play nice with Forgejo.

1.  Install the &#96;git-credential-libsecret&#96; package. It will help
    git store your credentials in GNOME Keyring, KWallet, etc.

    ``` _bash
    sudo dnf install git-credential-libsecret
    ```

2.  Add the following information to your &#96;\~/.gitconfig&#96; file.

    ``` _bash
    [credential]
    helper = libsecret
    ```

3.  Generate an Access Token.

    a.  Click on your profile picture in the upper-right corner of
        Forgejo.

    b.  Click on &#96;Settings&#96; in the menu underneath your profile
        photo.

    c.  Click on &#96;Applications&#96; in the menu on the left side of
        the screen.

    d.  Give the token a name, set it to All (public, private, and
        limited), and then select your permissions. &#8230;You will at
        &#42;LEAST&#42; need &#96;repository read and write&#96; access.

    e.  Click Generate token. You will get a warning. Copy this token
        because it will not be shown again.

4.  Push or Pull to Authenticate

    a.  When you git push or pull you should be asked to authenticate.

    b.  In KDE Plasma using KWallet, the first dialog is your username
        (eg. CoolFedoraDude), but it will look like a password secret
        box with no characters echoed. The second box that comes up will
        be where you paste the access token as your password.

    c.  The steps for GNOME Keyring should be similar.

Git should now use your local secret store to retreive your access token
as needed. No more prompts every time you want to push a commit!

### Sending an email {#_sending_an_email}

If you can't use any of the above options because you don't have a FAS
account, you can just write your suggestions or feedback in an email to
the Fedora Server list, <server@lists.fedoraproject.org>, or post a
message on our [discussion
board](https://discussion.fedoraproject.org/tags/c/project/7/server-wg).
You have to register, but it is less effort than creating a FAS account.
It's best to use a form like \'current version\' - \'proposed version\'.
Suggestions will then be included in the text, or perhaps there will be
follow-up questions.

## Quality assurance {#_quality_assurance}

Prior to publication, each article should be reviewed. Such articles are
available in our [staging
area](https://docs.stg.fedoraproject.org/en-US/fedora-server/) and
marked as \'awaiting review\' or similar.

Reviewer should:

&#42; check for technical and content accuracy. Contact the author in
case of questions. &#42; check spelling and syntax &#42; refine the
wording and phrases, especially in the case of non-English speaking
authors

The [staging
area](https://docs.stg.fedoraproject.org/en-US/fedora-server/) also
contains articles at an early stage of development, allowing for early
subject matter exchange and idea collection.

Furthermore, the published pages are mirrored, giving a complete
impression of the later documentation.

## Guidelines {#_guidelines}

The article [What is good documentation for software
projects?](https://opensource.com/article/20/4/documentation?utm_campaign=intrel)
provides a good summary of what we want to achieve with documentation,
although it is not entirely new.

Some pointers for articles:

&#42; Include of author(s), date of creation, last update, and the
Fedora version used to test the examples. &#42; Start with a short
summary of the subject matter, objective and desired outcome. (one
paragraph of 2-3 sentences) &#42; Divide longer sequences into sections
with subheadings and short explanations. &#42; Provide each step with a
brief explanation/justification, if possible, a general instruction
structure and a concrete example.

# Working with the Web based Page Editor {#_working_with_the_web_based_page_editor}

The Fedora Server Edition working group; Peter Boy (pboy); Stephen Daley
(mowest) :page-authors: {author}, {author_2}, {author_3}

> Fedora forge, where Fedora documentation is stored, offers the option
> of editing files directly in a web-based editor in the forge. This
> editor currently only offers basic editing functions. For example, it
> does not provide a preview feature. It is therefore particularly
> suitable for making small changes, such as correcting typos or
> individual sentences, quickly and easily.

:::: important
::: title
:::

This article is outdated and needs updating.
::::

Members of the Fedora Server Working Group make changes directly in the
main version that is published. Therefore, there is no opportunity to
discuss and agree on it beforehand. For major changes, it is advisable
to insert a note that the text is waiting for a final review.

However, changes are not immediately visible to the public, but only
after the pages are updated hourly.

Non-members automatically save the changes in a fork and create a
notification to integrate them (merge request).

## How to access an article for editing {#_how_to_access_an_article_for_editing}

### The easy way {#_the_easy_way}

As an example, you may want to modify the local interactive installation
guide. Open that page in your browser.

<figure>
<img src="docs-maintenance/webui-editor-0010.png"
alt="webui editor 0010" />
<figcaption>Use the editor button</figcaption>
</figure>

At the top you see an editor button. It opens the web page editor with
that article already loaded.

<figure>
<img src="docs-maintenance/webui-editor-0020.png"
alt="webui editor 0020" />
<figcaption>The Web editor opened</figcaption>
</figure>

### The direct way {#_the_direct_way}

Open the server user documentation on Fedora Forge in your browser.

<figure>
<img src="docs-maintenance/webui-editor-0030.png"
alt="webui editor 0030" />
<figcaption>Fedora forge Server user docs repository</figcaption>
</figure>

Follow the directory tree until you find the local installation guide at
modules/ROOT -&gt; pages -&gt; installation -&gt;
interactive-local.adoc. The file name does resemble the article title in
a abbreviated form.

<figure>
<img src="docs-maintenance/webui-editor-0040.png"
alt="webui editor 0040" />
<figcaption>Fedora forge Server user docs repository</figcaption>
</figure>

A click on the file name opens the web editor the same way as with the
easy way.

<figure>
<img src="docs-maintenance/webui-editor-0020.png"
alt="webui editor 0020" />
<figcaption>The file opend by the Web editor</figcaption>
</figure>

## How to modify an article by editing {#_how_to_modify_an_article_by_editing}

The first thing you have to do is to log in with your Fedora account.
Use the button in the top right corner. Afterwards you get some more
options in the menu bar.

<figure>
<img src="docs-maintenance/webui-editor-0050.png"
alt="webui editor 0050" />
<figcaption>The file opend by the Web editor</figcaption>
</figure>

Among other things, there is an editor button there that opens the
editor.

<figure>
<img src="docs-maintenance/webui-editor-0060.png"
alt="webui editor 0060" />
<figcaption>The file opend by the Web editor</figcaption>
</figure>

The Fedora Server Edition working group and Pagure follow the \'Pull
Request Workflow\'. According to this, no one is supposed to change a
published page immediately, but the workflow creates a copy of the page
under your name (the \'fork\') and when you are done, the community is
informed about your proposal (the pull request, or PR for short). The
community can discuss the proposal and after agreement the administrator
can \'pull in\' the proposal. The process is also known as \'merge
request\' (MR).

The pagure Web Editor takes care of all the details \'behind the
scenes\'. You don't need to worry about it. Just proceed to edit the
page.

More details to follow soon.

# Setting up a local authoring environment {#_setting_up_a_local_authoring_environment}

The Fedora Server Edition working group; Peter Boy (pboy); Stephen Daley
(mowest) :page-authors: {author}, {author_2}, {author_3}

> This method involves creating a copy of the documentation source on
> the local workstation. Linux and macOS are directly supported. This
> also includes a script for generating an exact local preview. The
> editing itself can be done with any editor.

:::: important
::: title
:::

This article is outdated and needs updating.
::::

## How it works {#_how_it_works}

As already described in the
[introduction](usr-docs-maintenance/index.xml), the documentation is
written in AsciiDoc and converted into HTML pages by the CMS. The
[Fedora Server user documentation git
repository](https://forge.fedoraproject.org/server/user-documentation)
contains the documentation source text.

It includes the content as well as various scripts to build and preview
the site locally. The directory structure is predefined by the docs
Content Management System (Antora) and must not be changed.

It has 2 permanent versions: The \'main\' for the published content and
\'stg\' for planning, development, and discussion. Temporarily,
additional branches may also be present.

Members of the Fedora Server Working Group have the privilege of making
changes directly in the original, central repository.

Everyone else can also copy the repository, but must save changes in
their own sub-section and then generate a "pull request." This prompts
members of the working group to review the proposed changes and pull
them into the central repository.

In the case of major changes, members of the working group should also
first submit their proposals in a separate sub-section.

## Writing tools {#_writing_tools}

You can use any ASCII editor to work on the documentation files.

A particularly useful OSS Asciidoc editor is
[AsciidocFX](https://asciidocfx.com). It is a Java program, very easy to
install, and provides both an integrated directory access, a toolbar
with the most common AsciiDoc formatting similar to a Word editor and an
integrated instant preview.

## Creating a new documentation article {#_creating_a_new_documentation_article}

An [annotated template](attachment$srv-template.xml) is available to
make things easier. Download it and save it in the appropriate directory
with a new name.

If possible, the files should be named in such a way that related files
appear together in the directory listing. The most important, most
differentiating parts should be at the front. For example

&#42; filesharing-nfs-administration.adoc &#42;
filesharing-nfs-installation.adoc &#42;
filesharing-samba-administration.adoc &#42;
filesharing-samba-installation.adoc

The titles should follow this pattern as far as possible and avoid
redundant parts such as \'How to install &#8230;\'

&#42; File sharing with NFS - Installation &#42; File sharing with NFS -
Administration &#42; File sharing using Samba - Installation &#42; File
sharing using Samba - Administration

All file names are in lower case.

## Preparations {#_preparations}

1.  &#42;Create a local subdirectory&#42; where the files of the
    documentation should be stored, and make it your default. We use
    fedora-server-docs in your home directory throughout this guide

    \[...\]\$ mkdir \~/fedora-server-docs \[...\]\$ cd
    \~/fedora-server-docs

2.  Still in your default working directory, &#42;clone
    fedora-server&#42; repository

    \[...\]\$ git clone <https://git@pagure.io/fedora-server.git> -o
    upstream

    Git will copy the complete server repo including all branches,
    specifically \'main\' and \'stg\' mentioned above, into a local repo
    on your local workstation (into *.git/* located in your default
    directory).

    Git does \'tag\' the cloned repo as remote repo
    \'&#42;upstream&#42;\'.

    At the same time it checks out the default branch \'\'\'main\'\'\'
    into your \'\'working directory\'\' (i.e. \~/fedora-server-docs in
    the above example). Therefore, when the operation terminates, you
    will find in your current default directory, which is now your
    \'\'working directory\'\', some files, e.g. README.md,
    docsbuilder.sh and preview.sh and a directory docs. The latter
    contains the content.

    If you leave off \'./\' at the end, git creates another directory in
    your default directory with the name of the repository, i.e.
    fedora-server. And this directory is then the \'*working
    directory*\' to the repository. This can be useful if you want to
    keep track of different fedora docs projects in one directory.

3.  In your browser go to <https://pagure.io/fedora-server/>, log in and
    &#42;create a Fork&#42;. Once you have done it, the button will read
    *View fork*. Switch to your fork and click on Clone and you will see
    2 addresses you can use to clone (copy) the content to your local
    default directory

    ssh://git@pagure.io/forks/\[MY_FAS\]/fedora-server.git
    [MY_FAS](https://git@pagure.io/forks/)/fedora-server.git

    Still in your default working directory, add the forked Repo to your
    remote repos.

    \[...\]\$ git remote add origin
    ssh://git@pagure.io/forks/\[MY_FAS\]/fedora-server.git

    You can use https as well. For users with a FAS account ssh is
    usually the better choice.

4.  You have now 2 remote repos defined. Check:

    \[...\]\$ git remote -v origin
    ssh://git@pagure.io/forks/\[MY_FAS\]/fedora-server.git (fetch)
    origin ssh://git@pagure.io/forks/\[MY_FAS\]/fedora-server.git (push)
    upstream <https://git@pagure.io/fedora-server.git> (fetch) upstream
    <https://git@pagure.io/fedora-server.git> (push)

    In your workflow you will update your local version to the latest
    versions of the server repository by \'pulling\' the content from
    \'upstream\' and upload your modifications and additions by
    \'pushing\' it to origin, i.e. to your fork. You will than create a
    \'pull request\', i.e. pick up your modifications and additions from
    your fork and integrate it into the generic repository (\'origin\').
    This enables co-writers to review our work and comment on it.

5.  In your working directory build the local version and start the
    preview tool.

    \[...\]\$ ./docsbuilder.sh

6.  Back in your browser enter the &#42;local preview address&#42;\':
    *localhost:8080*

    &#42; You should see a local preview of the current Server
    documentation

## Working on content {#_working_on_content}

1.  Check if you are on the branch you intend to work on

    \[...\]\$ git branch main &#42; stg

2.  If not, switch to the branch you want to use.

    \[...\]\$*git_checkout*\[stg\|main\]

    Git will adjust and modify the content of your working directory
    accordingly!

3.  Before your begin to work update your working directory

    \[...\]\$ git commit -m \'&lt;YOUR COMMIT MESSAGE&gt;\'

4.  Modify content

5.  Update preview and check:

    \[...\]\$ ./docsbuilder.sh

    Preview in your browser using the address *\'localhost:8080*

6.  Repeat step 4 &amp; 5 as required.

## Save Your Work {#_save_your_work}

Commit your work locally and then push it into your fork \'*origin*\'.

1.  Check status

    \[...\]\$ git status

2.  Add files to commit stage as appropriate

    \[...\]\$ git add &lt;FILENAME&gt;

3.  Commit locally

    \[...\]\$ git commit -m \'&lt;YOUR COMMIT MESSAGE&gt;\'

4.  Transfer your fork of fedora server to the repository

    \[...\]\$*git_push_origin*\[main\|stg\]

5.  In your browser open <https://pagure.io/fedora-server>, login,
    switch to your fork and create a pull request.

# A Git cheat sheet For Server Documentation Authors {#_a_git_cheat_sheet_for_server_documentation_authors}

Peter Boy (pboy)

> The sources for the Fedora Server documentation are stored and managed
> in a Git repository. This is not commonly practiced by authors and
> therefore its usage is unknown or not well known and not routine.
> Authors only need a fraction of Git's functionality to manage
> documents. Here we compile the most common work steps and describe
> their Git counterparts.

:::: warning
::: title
:::

This is work in progress
::::

## Prepare your local workspace {#_prepare_your_local_workspace}

Usually, you mirror the central *remote* Server documentation sources on
your *local* workstation and work on the various documents locally. When
done, you copy them back to the central *remote* storage.

In Git terminology this is a *clone* of the repository.

1.  &#42;Create a local subdirectory&#42; where the files of the
    documentation should be stored, and make it to your default. We use
    *fedora-server-docs* in your home throughout this guide

        […]$ mkdir ~/fedora-server-docs
        […]$ cd    ~/fedora-server-docs

2.  &#42;Clone the Server documentation sources&#42; into your default
    working directory

        […]$ git clone https://forge.fedoraproject.org/server/user-documentation.git ./
        Cloning into '.'\&#8230;
        remote: Enumerating objects: 2500, done.
        remote: Counting objects: 100% (510/510), done.
        remote: Compressing objects: 100% (325/325), done.
        remote: Total 2500 (delta 391), reused 171 (delta 171), pack-reused 1990 (from 1)
        Receiving objects: 100% (2500/2500), 19.03 MiB | 2.46 MiB/s, done.
        Resolving deltas: 100% (1357/1357), done.

    The \'./\' causes the repository to be created in the current
    directory. So your future working directory is
    \'\~/fedora-server-docs\' If omitted, Git creates a subdirectory in
    the current directory with the name of the repository and copies it
    there. The working directory would then be
    \'\~/fedora-server-docs/user-documentation\'. This would be useful,
    if you also want to clone our wg-documentation.

3.  &#42;Check the result&#42;

        […]$ git status
        On branch main
        Your branch is up to date with 'origin/main'.

        nothing to commit, working tree clean

    Git does \'tag\' or name the cloned repo as clone of the remote repo
    \'&#42;origin&#42;\'. It is the default for any action you perform
    with the cxentral remote repository. You can check further details.

        […]$ git  remote -v
        origin  https://forge.fedoraproject.org/server/user-documentation.git (fetch)
        origin  https://forge.fedoraproject.org/server/user-documentation.git (push)

    With *fetch*, you apply all changes in the central repository to
    your local workspace. Do this regularly to stay up to date.

    With *push*, you incorporate your changes into the central remote
    repository. Only members of the Server WG can do that.

## Prepare your remote storage space {#_prepare_your_remote_storage_space}

Upon completion of your work, you will want to copy the content back to
the central remote repository. Due to QA processes, only members of the
Server WG can write directly to the central remote repository. Everyone
else must create their own area in which to store their changes.

In Git terminology this is a *fork* of the repository.

1.  Open the [Server User
    Documentation](https://forge.fedoraproject.org/server/user-documentation)
    repository in your browser and log in with your FAS account.

2.  In the upper right corner you see a button
    \'&#42;&#42;Fork&#42;&#42;\'. It opens a form to set the properties
    of your fork. Accept the default values unchanged, with the
    exception of the optional Description field. Select the button
    \'Fork Repository\' to create the fork.

3.  The fork becomes the active window. Right around the center, you see
    a blue button \'&#42;&#42;HTTPS&#42;&#42;\' besides the address of
    your forck and a button to copy the URL.

4.  Add your fork to your remote repositories.

    Choose a descriptive name. Some recommend the name "upstream."
    That's actually a bit misleading. "Upstream" usually refers to the
    project where the ultimate development of the project takes place.
    In the case of server documentation, that would be the central
    remote repository, not a fork, of which there are many. Maybe you
    should choose your username or simply "myfork."

        […]$ git remote add {NAME} {URL}

    As an example, if would use

        […]$ git remote add myfork https://forge.fedoraproject.org/pboy/user-documentation

## Isolate work on new or updated items in a separate area {#_isolate_work_on_new_or_updated_items_in_a_separate_area}

Working on a new article or on an update of an existing one, it is
advantageous to work in a temporary space, copied mostly from the main
branch, independently from modifications on other documents in the repo
and without disturbing the main repo. It is especially useful, if you
work on it for a longer period of time. All changes you make here will
be merged back into the source, usually main, after completion.

In Git terminology this is a *branch* inside the repository.

### Check the central Server documentation repository for branches {#_check_the_central_server_documentation_repository_for_branches}

When you clone the central repository as described above, Git installs
just the main branch on your workspace. You have to check the central
repositry for branches you are interested in and install them manually.

It is not a good idea to simply replicate all branches locally. Some
branches may be outdated and no longer used. To avoid disorganization,
consciously select only the branches that are relevant to your current
work.

1.  &#42;List the branches&#42; in the remote central repository

        […]$ git branch -a
        \&#42; main
        remotes/origin/HEAD -\&gt; origin/main
        remotes/origin/main
        remotes/origin/nfs-upd
        remotes/origin/nfs_typo
        remotes/origin/stg

    The command lists your local branches and the branches on the remote
    central repository.

2.  &#42;Create a corresponding local branch&#42; of the branch you want
    to work with, eg. nfs-upd in the above example

        […]$ git checkout nfs-upd
        branch 'nfs-upd' set up to track 'origin/nfs-upd'.
        Switched to a new branch 'nfs-upd'

3.  &#42;Check the result&#42;

        […]$ git branch
        main
        \&#42; nfs-upd

        […]$ git status
        On branch nfs-upd
        Your branch is up to date with 'origin/nfs-upd'.

        nothing to commit, working tree clean

    You may also get some more information about your locally available
    branches:

        […]$ git branch -v
        main    1fa76ff modules/ROOT/pages/index.adoc aktualisiert
        \&#42; nfs-upd db0c02c fixed some typos in nfs filesharing docs and brought versions in line for FC43

### Create a new branch locally {#_create_a_new_branch_locally}

1.  Ensure, that the source, usually main, is your currently active
    branch

        […]$ git status
        \&#42; main
        stg
        {sometext}-upd

2.  Otherwise switch to main.

        […]$ git switch main

3.  Update your local workspace

        […]$_git_pull_[origin]

    The parameter is optional. The cloned repository's main branch is
    usually the default.

4.  Create a new branch und switch to it at the same time

        […]$ git checkout -b \&lt;NEW_BRANCH_NAME\&gt;

    Alternatively you can also use

        […]$ git switch -c \&lt;NEW_BRANCH_NAME\&gt;

### Delete a Branch no longer needed completely locally and remotely {#_delete_a_branch_no_longer_needed_completely_locally_and_remotely}

1.  Delete the remote branch

        […]$ git push -d \&lt;REMOTE_NAME\&gt; \&lt;BRANCH_NAME\&gt;

2.  Delete the local branch

        […]$ git branch -D \&lt;BRANCH_NAME\&gt;

## Working on content {#_working_on_content_2}

1.  Check if you are on the branch you intend to work on

        […]$ git branch
        \&#42; main
        stg
        {sometext}-upd

2.  If not, switch to the branch you want to use.

        […]$_git_checkout_[main|{sometext}-upd]

    Git will adjust and modify the content of your working directory
    accordingly!

3.  Before your begin to work update your working directory

        […]$ git

4.  Modify content

5.  Update preview and check:

        […]$ ./docsbuilder.sh

    Preview in your browser using the address *\'localhost:8080*

6.  Repeat step 4 &amp; 5 as required.

## Save Your Work {#_save_your_work_2}

### Commit your work locally {#_commit_your_work_locally}

While working on content all modifications happen in the volotile
working directory. Every change takes effect immediately; everything is
in flux. To permanently save a status, the working area is saved in the
local git repository (in the \'.git\' subdirectory). In Git, this is
known as a *commit.*

1.  Check status

    \[...\]\$ git status

2.  Add files to commit stage as appropriate

    \[...\]\$ git add &lt;FILENAME&gt;

3.  Commit locally

    \[...\]\$ git commit -m \'&lt;YOUR COMMIT MESSAGE&gt;\'

### Forgot a file in the last commit {#_forgot_a_file_in_the_last_commit}

Add a file to the last commit without modifying the commit log message

1.  Add the file (or several files) to the staging area

        […]$ […]$ git add \&lt;FILENAME\&gt;

2.  Add it to the last commit

        […]$ git commit  --amend  --no-edit

You can also add a files and replace the commit log message

1.  Add the file (or several files) to the staging area

        […]$ git add \&lt;FILENAME\&gt;

2.  Add it to the last commit

        […]$ git commit --amend -m 'an updated commit message'

### Save your work in the central remote repository {#_save_your_work_in_the_central_remote_repository}

### Transfer your work into the central remote repository {#_transfer_your_work_into_the_central_remote_repository}

Only members of Server WG can do this.

    […]$_git_push_origin_[main|]

### Save your work in your fork {#_save_your_work_in_your_fork}

    […]$_git_push_{YOUR_FORK_NAME}_[main|{sometext}-upd]

## Invite to discuss your work {#_invite_to_discuss_your_work}

### Create a Pull Request {#_create_a_pull_request}

TBD

### Modify a Pull Request {#_modify_a_pull_request}

TBD

## Finally publish your work {#_finally_publish_your_work}

### Merge a branch into main {#_merge_a_branch_into_main}

1.  If you are in your branch, commit all changes as described above.

2.  Switch to main and update your main version

        […]$ git checkout main
        […]$ git pull main

3.  Check whether a merge is possible without any problems.

        git merge --no-commit --no-ff {YOUR_BRANCH_NAME}

4.  If there arise no conflicts, merge your branch. Otherwise resolve
    them as described below.

        […]$ git merge {YOUR_BRANCH_NAME}

5.  Save your merged main to the central remote repository

        […]$ git push

### Merge a branch into stg {#_merge_a_branch_into_stg}

1.  If you are in your branch, commit all changes as described above.

2.  Switch to stg and update your stg version

        […]$ git checkout stg
        […]$ git pull stg

3.  Check whether a merge is possible without any problems.

        git merge --no-commit --no-ff {YOUR_BRANCH_NAME}

4.  If there arise no conflicts, merge your branch. Otherwise resolve
    them as described below.

        […]$ git merge {YOUR_BRANCH_NAME}

5.  Save your merged stg to the central remote repository

        […]$ git push

### Resolve a merge conflict {#_resolve_a_merge_conflict}

#### Merging into stg {#_merging_into_stg}

1.  Check whether a merge is possible without any problems.

        […]$ git merge --no-commit --no-ff \&lt;YourBranch\&gt;

A typical issue here is, you get the files you worked on merged without
any issue. But files you didn't work on can not automatically merged due
to differences between main (the base of your branch) and stg.

Best strategie in this case is just to keep all those files you didn't
modify and merge just those which automatically can get merged. For the
above example you get

    […]$ git merge  -s ort -X ours  pgsql-upd
    Auto-merging modules/ROOT/pages/index.adoc
    Auto-merging modules/ROOT/pages/installation/postinstallation-tasks.adoc
    Auto-merging modules/ROOT/pages/services/filesharing-nfs-installation.adoc
    Merge made by the 'ort' strategy.
    modules/ROOT/nav.adoc                                               |   1 +
    modules/ROOT/pages/services/fedsysadmins-cheatsheet-postgresql.adoc |  59 +++++++++++++++++++++++++++++++++++
    modules/ROOT/pages/services/postgresql-setup.adoc                   | 179 +++++++++++++++++++++++++++++++++++++++++++++++++++++++--------------------------------------------------
    3 files changed, 157 insertions(+), 90 deletions(-)
    create mode 100644 modules/ROOT/pages/services/fedsysadmins-cheatsheet-postgresql.adoc

#### Merging into main {#_merging_into_main}

TBD

## Miscellaneous {#_miscellaneous}

### Copy an article from one branch into another {#_copy_an_article_from_one_branch_into_another}

&#42;Not recommended&#42;

Sometimes you may need an article located in onother branch in youre
current work branch. An easy way is just to copy it. But be aware, this
way you don't get related files, e.g. images, in one go! You have to
check for file dependencies and copy one by one.

First check, if you are in the intended branch and then copy the file
from another branch

    […]$ git status
    […]$ git checkout \&lt;other-branch-name\&gt; \&lt;file-or-dir\&gt;

as an example

    […]$ git status
    On branch main
    Your branch is up to date with 'origin/main'.

    […]$ git checkout gui-upd modules/ROOT/pages/usecase-gui-addon.adoc

### „Cherry-pick" a commit from another branch into your current branch {#_cherry_pick_a_commit_from_another_branch_into_your_current_branch}

&#42;The recommended alternative to copy&#42;

\'Cherry-picking\' picks up a commit that was made in another branch and
applies that very same commit to your current branch. As with the copy
command about it copies files from one branch into another, but not just
one file, but all files that were processed in this commit. With regard
to documents, the text file of the document and all associated files
such as images, etc. will be transferred in one go.

1.  Check if you are on the branch you intend to work on

        […]$ git branch
        \&#42; main
        stg
        {sometext}-upd
        {othertext}-new

2.  If not, switch to the branch you want to use.

        […]$ git switch {sometext}-upd

3.  Skip through the log and finde the commit you want to cherry-pick

        […]$ git log
        commit bdb3a418f523167b422099b742bcf6d61068770f (HEAD -\&gt; main, origin/main, origin/HEAD)
        Author: Peter Boy \&lt;pb@boy-digital.de\&gt;
        Date:   Sat Nov 8 10:43:12 2025 +0100

        Amended sections.

        commit afe5fecff99300edb77b841eacd021bf6186edd4
        Author: Peter Boy \&lt;pb@boy-digital.de\&gt;
        Date:   Fri Nov 7 13:09:24 2025 +0100

        Initial commit of a Git Cheat Sheet for authors.

        commit 29668a512ad66595a550aec08a1171e42f219d11
        Author: Peter Boy \&lt;pb@boy-digital.de\&gt;
        Date:   Thu Nov 6 15:40:09 2025 +0100

        Updated minutes 2025-11-05 meeting.

        commit ac3d25fd1f6f7be2d05fe3d8d22d570ec77a5b35
        Author: Peter Boy \&lt;pb@boy-digital.de\&gt;
        Date:   Mon Nov 3 10:27:02 2025 +0100

        Updated minutes

    Copy the commit hash to the clipboard

4.  Cherry-pick the commit

        […]$ git cherry-pick [-x]  \&lt;commit-hash\&gt;

    If you want to cherry-pick the minutes of the 2025-11-05 meeting of
    the above example, it would be

        […]$ git cherry-pick -x  29668a512ad66595a550aec08a1171e42f219d11

    The abbreviated hash (the first 7 digits instead of 40), that you
    see in the overview in the web interface of the remote repository,
    too, is also sufficient. You may specify multiple commit hashes to
    cherry-pick multiple commits in one go.

    The parameter \'-x\' is optional. It enables you to provide a
    standard commit message, so it might easier in the future to see,
    what you did and why.

### „Cherry-pick" a commit from a forked repo into your current branch {#_cherry_pick_a_commit_from_a_forked_repo_into_your_current_branch}

1.  Find the URL of the other fork or repo. In the Fedora forge Web
    interface click on the number right of the \'Fork\' button. You get
    a list of the currently existing forks. Select the one you want to
    cherry-pick and copy the URL into the clipboard.

2.  Add the other repo to your remote repos. Choose a descriptive name,
    eg the username.

        […]$ git remote add {USERNAME} {URL}

    As an example, if you want to add my fork

        […]$ git remote add pboys https://forge.fedoraproject.org/pboy/user-documentation

3.  Fetch the branches

        […]$ git fetch  {USERNAME}

4.  As above get the log of the other branch, find the commit you want
    to cherry-pick and copy the commit hash into the clipboard

        […]$ git log  {USERNAME}/{BRANCH}

5.  Cherry-pick the commit

        […]$ git cherry-pick {COMMIT_HASH}

### Compare the same file in different branches {#_compare_the_same_file_in_different_branches}

TBD

# Archive {#_archive}

The Fedora Server Edition Working Group :page-authors: {author}

For reference and documentation of the Server Edition evolution process,
we continue to provide older versions of various documents for review.

## Archived approved documents {#_archived_approved_documents}

&#42; [\'Product Requirements Document\' (initial version
2014)](archive/product-requirements-document-2014.xml) &#42; [\'Product
Requirements Document\' (renwed version
2021)](archive/product-requirements-document-2021.xml) &#42; [\'Fedora
Server Technical Specification\' (initial version
2014)](archive/server-technical-specification-2014.xml)

## Server related documents {#_server_related_documents}

## Research {#_research}

## Proposals {#_proposals}

## Working group work plannings {#_working_group_work_plannings}

&#42; WG work project [Buildup of a renewed documentation on Fedora
Server specific topics](archive/initial-docs-plan.xml) planning
