- Goals = Product Requirements Document

:::: note
::: title
:::

Updated document as finalized at the **IRC Working Group Meeting** on
[June 23,
2021](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2021-06-23-16.59.html)
and approved by **FESCo vote** as of [July 9,
2021](https://pagure.io/Fedora-Council/tickets/issue/375). Update was
finalized at the **IRC Working Group Meeting** on [April 20,
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

**As a user, you gain the opportunity to use the server of the future
right now.**

Fedora Server provides a stable, flexible, and universally-adaptable
base for the everyday provisioning of services and applications by
organizations and individuals, based on the latest technology and is
available quickly after the upstream releases.

**As a developer or system integrator, you gain an eye on the server of
the future.**

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

- The twice-yearly, release cycle allows for the inclusion of the latest
  versions of system and application software almost immediately. Users
  and system administrators are empowered to swiftly respond to new
  market options and changing or expanding customer requirements.

- A sophisticated release and quality assurance process enables a high
  level of reliability and stability, despite the fast release cycle.
  This achieves an excellent balance between 'bleeding edge' and
  maturity for use in mainstream deployments.

- Fedora Server includes enterprise-grade security, resulting in
  carefully pre-configured releases, offering uncompromising security
  without extensive configuration work by system administrators.

- A great variety of available software, all included in that release
  process, opens up a wide range of possibilities for flexibility in
  building a server according to the specific needs and wishes of a
  customer or end-user.

- The latest, stable, modern system administration tools (e.g. cockpit)
  noticeably reduces the burden of system administration.

- Strict alignment with other Fedora editions as well as the
  twice-yearly releases are associated with less disruptive upgrades --
  several small updates are easier to manage than a few big ones.

- The upgrade process itself is very simple and straightforward, without
  requiring re-installation. Skipping one release is also viable, in
  case new capabilities are not immediately needed. All in all, Fedora
  is decidedly system administrator friendly.

- Fedora Server ensures utmost freedom from restrictions imposed by
  commercial interests or corporate feature management and excellent
  backwards hardware compatibility.

- Developers find an excellent development environment for the next
  generation server as well as application software with the latest
  software versions available.

# Server Edition Objectives {#_server_edition_objectives}

Fedora Server Edition offers a highly flexible and adoptable
multi-purpose server platform, usable at every scale.

- A platform for important infrastructure tasks and basic services (DNS,
  DHCP, FreeIPA, and others)

- A platform for various important, dedicated server applications
  (file/storage server, database server, user-developed web
  applications, etc.)

- A platform for deploying Infrastructure-as-a-Service systems for best
  deployment of Fedora Cloud images.

- A platform for deploying containerized applications supporting
  multiple container technologies, among which the system administrator
  can choose according to custom requirements.

- A platform for virtual machines, as host as well as guest system,
  supporting different technologies, among which the system
  administrator can choose according to custom requirements.

- Infrastructure to allow efficiently managing many servers as a single
  unit. The product only commits to producing basic tools, but the
  infrastructure will allow more advanced tools to be created.

- An operating platform capable to run any combination of forementioned
  services all according to very different needs of users rsp system
  administrators (multipurpose feature).

Fedora Server can be used as a standalone server that runs an
application or service as well as a member of a cluster in a data
center. As a result of strict adherence to open standards, it natively
cooperates with different server technologies and implementations.

## Additional Overall Objectives {#_additional_overall_objectives}

Aside from the adoption and development of the Fedora Server platform,
we have additional goals that are fundamental in any case:

- Security-minded: secure by design - extending into TPM support, disk
  encryption enablement

- Community-driven: Intense feedback about product direction and
  potential improvements. This is separate from "bug reports" in that we
  hope to engage the audience and receive detailed feedback about use
  cases, desired features, developing trends in cloud management, etc.
  We encourage more patches and contributions that will help improve the
  Server Edition, and Fedora in general.

# Primary Use Cases, User Profiles, and most important Features {#_primary_use_cases_user_profiles_and_most_important_features}

## Use Cases {#_use_cases}

The Fedora Server will need to address the following use-cases:

- On premise server for small and medium-sized enterprises hosting mail
  service, calendar, and branch specific (probably containerized)
  software -- either single node deployment or multi-node deployment
  with automatic failover

- Dedicated SOHO server, 'bare metal' rented from a remote provider and
  under its own full control, offering various services. Public access
  through VMs for security reasons.

- Single node or multi-node deployment in an enterprise data center
  providing up-to-date software versions according to domain specific
  requirements in a stable and secure OS, capable to provide different
  runtime environments -- native, VM, different container systems --
  driven by domain specific demands.

- Personal home server, located 'on premise' in own flat / house and
  used as NAS, backup device, and for applications such as mail
  repository, contact database, calendar, ebook library, media server,
  etc.

- Development box, providing developers with the latest software version
  and excellent developing tools

## User Profiles {#_user_profiles}

We will use a set of personas to describe our target users and their
respective needs. We list the typical personas by brief title and a
short list of key characteristics.

### System Administrator \"Macgyver\" {#_system_administrator_macgyver}

- Administrator with limited hardware and personnel resources to work
  with

- Requires simple automation to cope with repetitive tasks

- Needs to be able to do "a lot with a little"

### DevOps Engineer/Administrator {#_devops_engineeradministrator}

- Focus is on time-to-deploy and time-to-recover as opposed to uptime

- Value is achieved by delivering the latest capabilities fastest

- Needs to be able to deliver quickly to PaaS, SaaS and bare-metal
  servers

### Application Developer {#_application_developer}

- Needs a platform with API and ABI stability guarantees

- Focus will be on minimizing risk when making changes

- Needs latest technology in virtualization and containerization

- Likes a platform similar to the workstation

### Decision Maker {#_decision_maker}

- Makes purchasing decisions and directs technology choices

- Interacts with upstream FOSS communities to identify potential value

### The Home Admin {#_the_home_admin}

- I need a somewhat stable machine, with a graphical interface (Cockpit)
  and just want to start a couple of containers and/or virtual machines
  to have nextcloud running on it.

- I need some gitea here, some gitlab there, some jenkins, some
  photoprism, minecraft, etc. Can I build a NAS easily?

- I am ok with updates and reboots over night, but it should work. It
  would be awesome to have mDNS and a Web UI.

### The Hyperscaler {#_the_hyperscaler}

- I treat my servers as "cattle, not pets". Overall uptime is more
  important than individual server uptime

- I want to have a reliable platform for virtualization, core services
  and container. It should be out of my way, so I can focus on scaling,
  monitoring, implementation

- I want to automate server installation, and configurations for
  hostname, timeserver, hardening, etc. In addition I want to deploy
  typical services like mariadb, httpd, nginx, redis, nodejs, java, etc.
  in a reproducible way. To see what the machines are doing, I need a
  well documented way to manage, monitor and backup them.

- My Security Team also wants me to disable unneeded services, disable
  legacy protocols, enable hardening on several levels.

### The Remixer / \"Let's build upon it\" {#_the_remixer_lets_build_upon_it}

- I love how Fedora works and I want to create something upon it.

- I need a very well documented build process and maybe tools to produce
  new install images

- Removing the branding should be possible with some compiler flags or
  variables, so I don't need to mess with the code itself.

- I have a raspberry/intel nuc/etc. and playing a bit with new stuff.

## Most Important Features {#_most_important_features}

- The user can easily deploy and configure any supported Fedora Server
  application as well as rapidly re-deploy services in accordance with
  their DevOps practices. (Examples range from BIND DNS, DHCP, Database
  server, iSCSI target, File/Storage server, up to OpenStack Hypervisor
  Node, and the like)

- The user can query, monitor, configure and manage a Fedora Server and
  the resources consumed by services remotely using stable and
  consistent public interfaces.

- The user can deploy and configure Fedora Server to provide domain
  infrastructure with FreeIPA and Samba Active Directory solutions.
  Fedora Server can become Domain Controller in a newly established
  domain or join existing domain as a Domain Controller or a Domain
  Member.

- Users can create, manipulate and terminate large numbers of virtual
  machines and containers using a stable and consistent interface.

- The user is enabled to install and manage Fedora Server in a headless
  mode, either directly on the command line or supported by Cockpit, a
  lightweight Web GUI.

# Logistical Concerns {#_logistical_concerns}

## Delivery Mechanisms {#_delivery_mechanisms}

Fedora Server Edition generates installation resources for different
scenarios

- an offline install ISO image for a full local installation

- a net install ISO image for booting into an online installation

- a virtual disk image to be imported into a Fedora Server Edition KVM
  virtual environment

- a disk image for installation on supported aarch64 single board
  computers (SBC)

Supported installation methods are:

- Manual install without a supporting infrastructure (e.g. the very
  first Linux server).

- Automated ("mass") install within a larger Linux infrastructure (e.g.
  PXE is an option, may have LDAP/IPA).

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

- Alexander Bokovoy

- Peter Boy (editor)

- Davide Cavalca

- Kevin Fenzi

- Stephen Gallagher

- John Himpel

- David Kaufmann

- Jan Kuparinen

- Eduard Lucena

- Michel Salim

- Stephen Smoogen

- Langdon White

- Adam Williamson

# Fedora Server Technical Specification {#_fedora_server_technical_specification}

:::::: note
::: title
:::

:::: formalpara
::: title
**This is an approved document**
:::

Updated version as finalized at the **Server Working Group IRC Meeting**
on [August 17,
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

- **Core Features**

  describes the basic features and properities. They constitute the base
  system, which is installed by the (graphical) installer by default.

- **System Administration**

  describes properties and capabilities of the default administration
  interface

- **Advanced Features**

  describes additional features that are not part of the default
  (graphical) installation but require subsequent administrative action

- **Server Roles**

  describe various services which Fedora Server can validly and
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

- A **network installation media** providing a minimal package set
  allowing to boot the system, connect to Internet and contact the
  Fedora media server to download packages to be installed.

- A **local installation media** providing the default package set as
  well as any featured services that are meaningfully installed without
  a network connection.

  - It can additionally point at network resources to make available an
    ever larger package set.

  - Nevertheless, this media should be friendly to regions with limited
    Internet connection stability and performance. Thus, it is a
    trade-off between completeness and practical download size..

- A **virtual machine disk image** for simplified installation of Fedora
  Server Edition in a KVM virtual environment. The image reproduces the
  Server Edition completely and without restrictions, as far as features
  are usable in a virtual environment.

- A raw **aarch64 disk image** for installation on a Singe Board
  Computer (SBC).

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

- creates the necessary standard partitions to boot the server
  (BiosBoot, EFI, /boot)

- creates a Volume Group with one Logical Volume of a reasonable minimal
  size to accomodate the root file system and system files using *XFS*

- leaves the remaining space untouched for customization by the system
  administrator for user data, services or other uses. The installer
  must also support the following common options

  - enlarge the one logical volume to accomodate custom data as well
    without any separation (*not recommended*)

  - create one or more logical volumes to accomodate custom data

  - or even create an additional Volume Group dedicated to custom data

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

- localed: localectl

- timedated: timedatectl

- hostnamed: hostnamectl

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

- A mechanism to install the packages necessary to deploy the service.

- A mechanism to deploy a service whose packages are already installed
  on the system by providing the necessary information and procedures to
  provision it.

- A mechanism to install optional components of a service after
  deployment.

- A configuration interface to modify high-level configuration options.

- A helper tool (preferrable based on LVM snapshot) to perform a backup
  or alternativ a list of files on the filesystem that should be
  included in a backup set.

Depending on practical experience, Server Roles may additionally need a
query interface providing metadata information about the service (not
all services must implement all parts of this):

- A list of system services provided by the Supported Server Service, as
  well as data about whether those services are currently running (or
  enabled, in the case of socket-activated services)

- A list of the ports that the role operates on, as well as data about
  whether those ports are currently firewalled.

- A mechanism to open and close ports that the server service operates
  on for some or all interfaces.

- If the Server Service is designed to operate on the network, it should
  automatically open those ports (see Firewall) during deployment.

- An interface to set processor affinity, memory limits, etc. where
  sensible.

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

- Stephen Gallagher (sgallagh)

- Peter Boy (pboy)

- Jason Beard (cooltshirtguy)

- John Himpel (jwhimpel)

- Chris Murphy (cmurf)

- Emmanuel Seyman (eseyman)

- Adam Williamson (adamw)

- Members and Governance = Members Stephen Daley, Peter Boy

- [Jason
  Beard](https://fedoraproject.org/w/index.php?title=User:Cooltshirtguy)
  (***cooltshirtguy***)

- [Alexander Bokovoy](https://fedoraproject.org/wiki/User:Abbra)
  (***abbra***)

- [Peter Boy](https://fedoraproject.org/wiki/User:Pboy) (***pboy***)

- [François Cami](https://fedoraproject.org/wiki/User:Fcami)
  (***fcami***)

- [Davide Cavalca](https://fedoraproject.org/wiki/User:Dcavalca)
  (***dcavalca***)

- [Stephen
  Daley](https://fedoraproject.org/w/index.php?title=User:Mowest)
  (***mowest***)

- [Kevin Fenzi](https://fedoraproject.org/wiki/User:Nirik) (***nirik***)

- [Stephen Gallagher](https://fedoraproject.org/wiki/User:Sgallagh)
  (***sgallagh***)

- [John
  Himpel](https://fedoraproject.org/w/index.php?title=User:Jwhimpel)
  (***jwhimpel***)

- [Neal Gompa](https://fedoraproject.org/wiki/User:Ngompa)
  (***ngompa***)

- [David Kaufmann](https://fedoraproject.org/wiki/User:Astra)
  (***astra***)

- [Jan Kuparinen](https://fedoraproject.org/wiki/User:Copperi)
  (***copperi***)

- [Eduard Lucena](https://fedoraproject.org/wiki/User:X3mboy)
  (***x3mboy***)

- [Michel Alexandre Salim](https://fedoraproject.org/wiki/User:Salimma)
  (***salimma***)

- [Emmanuel Seyman](https://fedoraproject.org/wiki/User:Eseyman)
  (***eseyman***)

- [Adam Williamson](https://fedoraproject.org/wiki/User:Adamw)
  (***adamw***)

- [Langdon White](https://fedoraproject.org/wiki/User:Langdon)
  (***langdon***)

## Meetings {#_meetings}

- The Server working group meets twice-monthly every 1st and 3rd
  Wednesday at 17:00 UTC in #fedora-meeting on irc.libera.chat.

- ical: <https://calendar.fedoraproject.org/server/> (prefer this
  source; the wiki sometimes gets out of date, but we keep that meeting
  correct to reserve the meeting channel).

## Server Working Group Resources {#_server_working_group_resources}

- Mailing list: <server@lists.fedoraproject.org>

- IRC: #fedora-server on irc.libera.chat

- Blog: <http://fedoramagazine.org/>

- Tickets: pagure.io/fedora-server = Federa Server WG Governance Charter
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
Many of our decisions can be made through \"lazy consensus.\" Under this
model, an intended action is announced on the mailing list, discussed,
and if there is no controversy or dissenting views with a few days,
simply done.

For bigger issues, they must be discussed and voted on in a public IRC
meeting. Public IRC meetings are generally held most weeks on Tuesdays
at 4:00pm Eastern US time in
[#fedora-meeting](https://web.libera.chat/?channels=#fedora-meeting) on
Libera. For an IRC meeting to be held, at least three Working Group
members must be present. Votes are accepted by all participants in the
meeting (not just those of Working Group members), so the community is
highly encouraged to join. In the case where an interested party can not
make it to a meeting, they can pre-vote via the mailing list. =
Communicating and Meeting Peter Boy, Stephen Daley :page-authors:
{author}

:::: note
::: title
:::

**Work in Progress** Status: Migrating from WIKI
::::

The Fedora Server Edition Working Group uses various resources

- Mailing list: <server@lists.fedoraproject.org>

- IRC: #fedora-server on irc.libera.chat

- Blog: <http://fedoramagazine.org/>

- Tickets: <https://pagure.io/fedora-server>

## Meetings {#_meetings_2}

- The Server working group meets twice-monthly **every 1st and 3rd
  Wednesday at 17:00 UTC** in #fedora-meeting on irc.libera.chat.
  Please, check your local time using e.g.
  `date -d '2021-11-17 17:00UTC'`

- Each meeting is announced in the Fedora Project Calendar:
  <https://calendar.fedoraproject.org/server/>

- The agenda is announced on the server mailing list
  <server@lists.fedoraproject.org> and available from the ticket system
  at <https://pagure.io/fedora-server/report/Meeting>

- If there is no agenda, the meeting will be cancelled and the
  organisator /chair will send out a cancellation notice to the mailing
  list.

- During meetings, silence indicates consent. If people disagree, then
  that will bring it to a vote.

- In the case where a voting member can not make a meeting where a vote
  is scheduled to happen, they can either pre-vote via the mailing list
  or abstain-by-default.

- After meetings, meeting minutes will be sent to the [server mailing
  list](https://lists.fedoraproject.org/mailman/listinfo/server).

# Meeting Minutes 2026 {#_meeting_minutes_2026}

Stephen Daley; Peter Boy :page-authors: {author}, {author_2}
:page-aliases: wg-minutes-current.adoc

Wednesday, January 28, 2026

:   Because of lacking out quorum we had a open discussion about various
    topics

    - ***Essentials at a glance***

      (This summary is AI generated and edited)

      - **Flock Conference Submission**

        - We discussed submitting a proposal for the upcoming Flock
          conference, suggesting a Birds of a Feather (BoF) session, a
          talk, or both.

        - BoF sessions at Flock are planned for \"Day 0\" and will not
          be officially recorded or streamed, which is acceptable to the
          group.

      - **Working Plan Progress**

        - Progress on creating topics for the working plan in the
          repository has been slow due to time constraints.

        - pboy is evaluating the \"backup / rescue\" topic and notes it
          seems to be a long-term project.

      - **Next Release Testing**

        - Testing for the next release (Fedora 44) is urgent as the
          branch date is the following week (2026-02-03).

        - The KVM and aarch64 Server images are flawed, specifically
          with the wrong file type on the root partition.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2026-01-28/fedora-server.2026-01-28-18.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2026-01-28/fedora-server.2026-01-28-18.00.log.html)

    - ***Actions summary***

      1.  pboy & eseyman: Brainstorm a Flock submission while at FOSDEM.

      2.  pboy: Create the homeserver topic in the repository.

      3.  eseyman: Create the entry for the netboot / install topic in
          the repository.

      4.  korora: Add to the netboot / install topic once it is created.

      5.  korora: Test the flawed KVM virtual machine image for the
          upcoming release.

<!-- -->

Wednesday, January 21, 2026

:   - ***Essentials at a glance***

      - **Announcements**

        Several members, including pboy and eseyman, will will be
        attending FOSDEM. A Fedora/Fedora Docs meeting is planned for
        the Friday evening of the event.

      - **Our program and working plan for the upcomming year**

        We decided on four main projects for the upcoming year:

        - Home server spin

        - Backup documentation/tooling

        - Net-boot (PXE) documentation and Ansible support

        - Ansible/NFS projects

      - **Contribution to Flock 2026**

        A possible relevant topic is the home server spin-off. But we
        need one or two professional usage topics, too.Details to be
        discussed further.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2026-01-21/fedora-server.2026-01-21-18.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2026-01-21/fedora-server.2026-01-21-18.00.log.html)

    - ***Actions summary***

      1.  pboy will create a project entry on Forge for each project
          planned for the coming year

<!-- -->

Wednesday, January 07, 2026

:   - ***Essentials at a glance***

      - **Status migration to forge.fedoraproject.org**

        All work has been completed. Ticket 173 closed.

      - **Restructuring the Server User Documentation**

        The stg branch has been removed from the public Server
        Documentation. The repository no longer contains any relevant
        text.

        *AGREED*: The stg branch can now finally be removed.

      - **Our program and working plan for the upcomming year**

        We finally agreed to create a home server/home lab spin-off.
        Other new projects include pxe boot support and backup/rescue
        system. Details are still being discussed.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2026-01-07/fedora-server.2026-01-07-18.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2026-01-07/fedora-server.2026-01-07-18.00.log.html)
      = Meeting Minutes 2025 Stephen Daley; Peter Boy :page-authors:
      {author}, {author_2}

<!-- -->

Wednesday, December 17, 2025

:   - ***Essentials at a glance***

      - **Restructuring the Server User Documentation**

        *AGREED*: We will finally remove the stg branch from our Docs
        repo.

      - **Pending reviews of our documentation**

        *AGREED*: The PostgreSQL update has been positively reviewed and
        can be released.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-12-17/fedora-server.2025-12-17-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-12-17/fedora-server.2025-12-17-18.00.log.html)

<!-- -->

Wednesday, December 10, 2025

:   - ***Essentials at a glance***

      - **Status migration to forge.fedoraproject.org**

        We had some discussion about organising all tickets in on ticket
        repo instead spreading them over the various repos.

        *AGREED*: We keep all tickets (and projects), even very specific
        detailed tickets for areas of the other repo, together in one
        repo.

      - **Restructuring the Server User Documentation**

        Now that we have an easily accessible, albeit still somewhat
        rough preview in the new forge, we no longer want to stick with
        the cumbersome stg branch.

        *AGREED*: We drop stg branch in favour of the AsciiDoc preview
        in forge.

        pboy will adjust our contributors guides and remove the stg
        branch from the repo as soon as all outstandig discussions are
        closed.,

      - **Our program and working plan for the upcomming year**

        We've put together a preliminary list.

        <https://forge.fedoraproject.org/server/tickets/issues/178>

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-12-10/fedora-server.2025-12-10-18.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-12-10/fedora-server.2025-12-10-18.00.log.html)

<!-- -->

Wednesday, November 26, 2025

:   - ***Essentials at a glance***

      - **Status migration to forge.fedoraproject.org**

        *AGREED*: We move the old wiki to the wiki inside
        forge.fedoraproject.org

      - **Walk through longterm open issues and PRs**

        *AGREED*: We close issue #55 about default editor as resolved.
        It is part of post-installation tasks.

    - HTML Minutes: [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-11-26/fedora-server.2025-11-26-18.00.html)

    - HTML Log: [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-11-26/fedora-server.2025-11-26-18.00.log.html)

    - ***Actions summary***

      1.  DONE: pboy will merge the NFS Doc adduser fix.

      2.  DONE: Ticket 134: We include the ideas to our wiki idea
          collections for documentation and close the ticket.

      3.  DONE: Ticket 112: We close Ticket 112 (LLMNR) as fixed by
          documentation.

      4.  DONE: Aggraxis will dig into the LLMNR (ticket #114) and make
          a proposal.

<!-- -->

Wednesday, November 19, 2025

:   - ***Essentials at a glance***

      - **Server Docs: How to proceed with NFS doc**

        *ACTION*: pboy will merge the NFS Doc adduser fix.

      - **Server Docs Contribution work with new Fedora forge**

        *AGREED*: The overview page \"User Documentation Maintenance\"
        has been accepted.

      - **Walk through longterm open issues and PRs**

        *AGREED*: Ticket 134: We include the ideas to our wiki idea
        collections for documentation and close the ticket.

        *AGREED*: Ticket 132: pboy will write a comment to catch the
        SELinux error. If there is no reaction, we'll close the ticket.

        *AGREED*: Ticket 112: We close Ticket 112 (LLMNR) as fixed by
        documentation.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-11-19/fedora-server.2025-11-19-18.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-11-19/fedora-server.2025-11-19-18.00.log.html)

    - ***Actions summary***

      1.  pboy will merge the NFS Doc adduser fix.

<!-- -->

Wednesday, November 12, 2025

:   - ***Essentials at a glance***

      - **Server Docs Contribution work with new Fedora forge**

        The Main change is the addition of a \"Get Cheat Sheet for
        writers\" to answer questions which came up by several writer
        members. Aggraxis will add a chapter about obtaining an access
        token, that is not entirely straightforward.

      - **Walk through longterm open issues and PRs**

        Issue 112: LLMNR/nDNS issue, we agree to handle this as part of
        the post-installation tasks. Aggraxis will add a section to the
        current version.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-11-12/fedora-server.2025-11-12-18.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-11-12/fedora-server.2025-11-12-18.00.log.html)

<!-- -->

Wednesday, November 05, 2025

:   - ***Essentials at a glance***

      - **Server Docs: How to proceed with NFS doc**

        *AGREED*: pboy will merge Jocelyn's modification into stg, at
        the same time checking if it really works as expected in Forgejo

        *ACTION*: pboy will update the Server how-to-contribute guide.

        *ACTION*: jwhimpel will write a workflow proposal for our
        Ansible development task.

      - **Possible Update issue with PostgeSQL**

        *ACTION*: nirik will tag common bugs with the postgres issue.

        *ACTION*: pboy will check release notes, server docs and
        QuickDocs about the postgres issue.

      - **Walk through longterm open issues and PRs**

        *ACTION*: Aggraxis will dig into the LLMNR (ticket #114) and
        make a proposal.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-11-05/fedora-server.2025-11-05-18.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-11-05/fedora-server.2025-11-05-18.00.log.html)

    - ***Actions summary***

      1.  pboy will update the Server how-to-contribute guide.

      2.  jwhimpel will write a workflow proposal for our Ansible
          development task.

      3.  nirik will tag common bugs with the postgres issue.

      4.  pboy will check release notes, server docs and QuickDocs about
          the postgres issue.

      5.  Aggraxis will dig into the LLMNR (ticket #114) and make a
          proposal.

<!-- -->

Wednesday, October 29, 2025

:   - ***Essentials at a glance***

      - **F43 release testing (resume)**

        Overall, testing went well. Testing the SBC bugs took too much
        time. Too little attention was paid to the potential problems
        caused by individual changes.

        *AGREED*: pboy will write a summary to the list and we should
        see where the discussion takes us

      - **Server Docs: How to proceed with NFS doc**

        *ACTION*: Jocelyn will take a look at the current documentation
        and make a proposal how to proceed.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-10-29/fedora-server.2025-10-29-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-10-29/fedora-server.2025-10-29-17.00.log.html)

    - ***Actions summary***

      1.  Jocelyn will take a look at the current NFS documentation and
          make a proposal how to proceed.

<!-- -->

Wednesday, October 22, 2025

:   - ***Essentials at a glance***

      - **F43 release testing**

        Fortunately, the long standing [SBC
        bug](https://bugzilla.redhat.com/show_bug.cgi?id=2396309) is
        resolved. And arm-image-installer works fine, again. So there is
        no need to drop the ARM SBCs from our download page.

      - **Step 1 adjusting our SBC documentation**

        *AGREED*: WG modifies the SBC docs as proposed in the ticket
        ([#168](https://forge.fedoraproject.org/server/tickets/issues/168))

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-10-22/fedora-server.2025-10-22-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-10-22/fedora-server.2025-10-22-17.00.log.html)

    - ***Actions summary***

      1.  pboy will modify Server docs about SBC as agreed upon.

      2.  Emmanuel Seyman will fix the open PR on forge.

<!-- -->

Wednesday, October 15, 2025

:   - ***Essentials at a glance***

      - **Follow-up actions & announcements**

        *AGREED*: We switch to winter time in sync with US, again. And
        we modify the UTC time to keep local time unchanged.

      - **Improve the structure of our user documentation**

        *AGREED*: Server documentation will be modified according to
        proposal <https://hackmd.io/@pboy/BJnkUjA3el>

      - **Walk through longterm open issues and PRs**

        *AGREED*: Each WG member selects an open issue on Forge and
        either makes a suggestion on what to do or deals with the issue
        themselves until next week meeting.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-10-15/fedora-server.2025-10-15-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-10-15/fedora-server.2025-10-15-17.00.log.html)

    - ***Actions summary***

      1.  Each WG member selects an open issue on Forge and either makes
          a suggestion on what to do or deals with the issue themselves
          until next week meeting.

<!-- -->

Wednesday, October 01, 2025

:   - ***Essentials at a glance***

      - **Setting up our new Forgejo repository space**

        We have a provisional repo structure according to our previous
        discussions and ticket 173.

        *AGREED*: We start with a repo structure as proposed in ticket
        173

        *AGREED*: We keep the naming as is today, for now.

        *AGREED*: For the time being we use one issue list for
        everything. We will examine whether it proves effective.

        *AGREED*: We keep the tickets repo as is

        *AGREED*: We adjust the docs repos to the Antorra required
        structure.

        *AGREED*: We restructure the Ansible repo later

        *AGREED*: We switch as soon as we can switch the docs pages to
        forge and freeze the docs pages on pagure in the meantime

        *ACTION*: pboy will restucture the Docs repos as aggreed

        *ACTION*: jwhimpel will make a proposal for the Ansible repo
        structure.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-10-01/fedora-server.2025-10-01-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-10-01/fedora-server.2025-10-01-17.00.log.html)

    - ***Actions summary***

      1.  pboy will restucture the Docs repos

      2.  jwhimpel will make a proposal for the Ansible repo structure.

<!-- -->

Wednesday, September 24, 2025

:   - ***Essentials at a glance***

      - **Follow-up actions & announcements**

        Since today we have a new forge:

        <https://forge.fedoraproject.org/server>

      - **Future long-term status of the SBC distribution image**

        *AGREED*: If the current installation problems are not fixed by
        the release date, no SBC version of the Server should be
        released at all.

        *AGREED*: WG proposes the Server SBC installation medium as
        release blocking. Details to be coordinated with other editions.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-09-24/fedora-server.2025-09-24-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-09-24/fedora-server.2025-09-24-17.00.log.html)

<!-- -->

Wednesday, September 17, 2025

:   - ***Essentials at a glance***

      - **Follow-up actions & announcements**

        Pboy made contact with Ryan Lerch about new forgejo Fedora
        forge. We'll get a stg account fist to be able to explore our
        options.

      - **F43 release testing**

        Paul repoerted, the remote interactive installation via ks file
        and OEMDRV USB drive is back. So again, you don't need to edit
        the kernel command line (clumpsy with a non_US keyboard layout)
        nor any termnal connected.

        A severe issue is the SBC. It still doesn't work at all.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-09-17/fedora-server.2025-09-17-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-09-17/fedora-server.2025-09-17-17.00.log.html)

<!-- -->

Wednesday, September 10, 2025

:   - ***Essentials at a glance***

      - **Follow-up actions & announcements**

        Eseyman got a reply from the Tomcat group regarding the SELinux
        issue with ajp proxy. Blocking localhost access is intentional.
        The policy is no default network access. And localhost is seen
        as network access. We will pick up this later.

      - **Revision of Server SBC documentation**

        We want to clearly distinct between the Server Edition core use
        case and special uses such as ARM SBCs. In particular, a
        Raspberry Pi 4, the current focus in Fedora, is unsuitable for
        Server. We will reorganize the documentation to clearly separate
        the SBC articles from the main topics.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-09-10/fedora-server.2025-09-10-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-09-10/fedora-server.2025-09-10-17.00.log.html)

<!-- -->

Wednesday, September 03, 2025

:   - ***Essentials at a glance***

      - **Server Web service guide**

        *AGREED*: we create a PR for httpd to include the config files
        as of stg article 2025-09-03

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-09-03/fedora-server.2025-09-03-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-09-03/fedora-server.2025-09-03-17.00.log.html)

<!-- -->

Wednesday, August 27, 2025

:   - ***Essentials at a glance***

      - **Follow-up actions & announcements**

        The change regarding bios boot systems as discussed at last
        meeting is now active.

        [Proposal: Limit release-blocking status of BIOS systems to just
        certain
        scenarios](https://discussion.fedoraproject.org/t/proposal-limit-release-blocking-status-of-bios-systems-to-just-certain-scenarios/160757)

      - **httpd vhost issues**

        There is a new issue with the ajp proxy protocol. The default
        configuratin is blocked by SELinux.

        We want to put forward our Webservice configuration. pboy will
        update the guide in stg to the latest development.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-08-27/fedora-server.2025-08-27-17.02.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-08-27/fedora-server.2025-08-27-17.02.log.html)

<!-- -->

Wednesday, August 20, 2025

:   - ***Essentials at a glance***

      - **Follow-up actions & announcements**

        Folllowing a discussion about the status and differentiation of
        editions

        *AGREED*: We agree to keep server as a package based system for
        the foreseeable future and don't intend to start an alternative
        planning any time soon.

      - **Server Documentation issues**

        *AGREED*: We publish the extended SW Raid doku now as is (adding
        F42 in meta data). Further refinement probably after F43
        release.

        As discussed with QA, this provides them with a concrete test
        path and decision criterion for the SW RAID item in the biosboot
        release blocker criterion.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-08-20/fedora-server.2025-08-20-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-08-20/fedora-server.2025-08-20-17.00.log.html)

<!-- -->

Wednesday, August 13, 2025

:   - ***Essentials at a glance***

      - **F43 release testing**

        The main installation media seem to be OK so far. With SBCs an
        issue with arm-image-installer on LVM are back again.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-08-13/fedora-server.2025-08-13-17.03.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-08-13/fedora-server.2025-08-13-17.03.log.html)

<!-- -->

Wednesday, August 06, 2025

:

- [Meeting
  summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-08-06/fedora-server.2025-08-06-17.00.html)

- [Full
  log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-08-06/fedora-server.2025-08-06-17.00.log.html)

Wednesday, July 30, 2025

:   - ***Essentials at a glance***

      - **Recent changes of release testing criteria**

        After a longer discussion:

        - Optical installation media *AGREED*: Server WG agrees to
          change proposal regarding optical media as the proposal
          suggests

        - BIOS Boot *AGREED*: Server WG agrees with the proposal on the
          condition that a simple Software Raid installation in
          accordance with Server documentation is added with blocking
          status.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-07-30/fedora-server.2025-07-30-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-07-30/fedora-server.2025-07-30-17.00.log.html)

<!-- -->

Wednesday July 09, 2025

:   - ***Essentials at a glance***

      - **Server requirements for the upcoming updated version of
        Anaconda**

        After an intensive discussion:

        - *AGREED*: We want to remove \"Software Selection\" from the
          installation summary.

        - *AGREED*: We want to keep the source selection option for net
          install, but drop it for DVD install it is is not to much work
          to implement.

        - *AGREED*: We want to drop the option menu together with the
          software selection item.

        - *AGREED*: We want to keep the time/timezone item and
          preselected timezone UTC if it can not determined from the
          runtime environment. Can be overwritten during install.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-07-09/fedora-server.2025-07-09-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-07-09/fedora-server.2025-07-09-17.00.log.html)

<!-- -->

Wednesday, June 18, 2025

:   - ***Essentials at a glance***

      - **Announcements**

        According to our voting we have 2 new members:

        - Jocelyn
          ([korora](https://accounts.fedoraproject.org/user/korora/))
          ([voting](https://pagure.io/fedora-server/issue/161))

        - Paul
          ([aggraxis](https://accounts.fedoraproject.org/user/aggraxis/))
          ([voting](https://pagure.io/fedora-server/issue/162))

      - **Ansible assisted installation and configuration of NFS
        service**

        After a longer discussion about various ways to support NFS file
        sharing:

        *AGREED*: In about 14 days, Emmanuel and John will come up with
        a plan about implementation details.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-06-18/fedora-server.2025-06-18-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-06-18/fedora-server.2025-06-18-17.00.log.html)

<!-- -->

Wednesday, June 11, 2025

:   - ***Essentials at a glance***

      - **Server requirements for the upcoming updated version of
        Anaconda**

        *ACTION*: Jocelyn will write a summery of the discussion with
        the status as of next Wednesday, so that we have something to
        base our decision on.

- [Meeting
  summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-06-11/fedora-server.2025-06-11-17.00.html)

- [Full
  log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-06-11/fedora-server.2025-06-11-17.00.log.html)

- ***Actions summary***

  1.  Jocelyn will write a summery of the discussion with the status as
      of next Wednesday, so that we have something to base our decision
      on.

Wednesday, May 28, 2025

:   - ***Essentials at a glance***

      - **Ansible assisted installation and configuration of NFS
        service**

        Eseyman completed an RPM of most interesting Ansible roles,
        specifically the NFS role (currently on COPR). Now we have to
        test the RPM and combine with jwhimpels work.

        *AGREED*: we will use the next two weeks to test the available
        tools and decide how we can best achieve our goal of supporting
        services. And we will consider how we can optimize the
        distribution.

      - **Open Floor**

        We will make our FAS Server Group (server-wg) official,
        containing the authoritative list of WG members. The current
        WIKI list will then be removed..

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-05-28/fedora-server.2025-05-28-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-05-28/fedora-server.2025-05-28-17.00.log.html)

<!-- -->

Wednesday, May 07, 2025

:   AGREED: we skip next meeting (May 14)

    - ***Essentials at a glance***

      - **Ansible assisted installation and configuration of NFS
        service**

        AGREED: We postpone the NFS Ansible project until eseyman has a
        robertdebock rpm ready and eseyman and jwhimpel have a proposal
        how to (re)use it for our purposes.

      - **Server user poll**

        Eseyman reported, he was pleasantly surprised. Lots of people
        seem satisfied with what we ship. The main call for improvement
        is documentation, use cases, best pratices, ...​

        Eseyman and pboy will prepare a finer analyses of the data.

      - **Follow-up of the F42 server development and test cycle**

        AGREED: We try to create a Server Edition test day (or better
        test week)

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-05-07/fedora-server.2025-05-07-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-05-07/fedora-server.2025-05-07-17.00.log.html)

<!-- -->

Wednesday, April 23, 2025

:   - ***Essentials at a glance***

      - **Ansible assisted installation and configuration of NFS
        service**

        ACTION: jwhimpel will create a Beta RPM that will establish the
        \"base\" filesystem and related documentation for our ansible
        setup (on admin's workstation)

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-04-23/fedora-server.2025-04-23-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-04-23/fedora-server.2025-04-23-17.00.log.html)

<!-- -->

Wednesday, April 16, 2025

:   - ***Essentials at a glance***

      - **Follow-up of the F42 server development and test cycle**

        The final release actually no longer contains the possibility of
        a remote interactive installation initialized without terminal
        by kickstart file. This is the result of a system-wide switch
        from VNC to RDP initiated by the Workstation WG. The
        discontinuation is a side effect of the changes in Anaconda and
        was unannounced. We did not expect this omission and
        unfortunately discovered it too late.

        AGREED: We will create a list of minimal manual tests and try to
        establish a test week for F43.

        A particularly intensive checking require all changes that are
        in any way related to the Workstation WG.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-04-16/fedora-server.2025-04-16-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-04-16/fedora-server.2025-04-16-17.00.log.html)

<!-- -->

Wednesday, April 09, 2025

:   Open discussion about the Ansible assisted installation and
    configuration of NFS service project.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-04-09/fedora-server.2025-04-09-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-04-09/fedora-server.2025-04-09-17.00.log.html)

<!-- -->

Wednesday, April 02, 2025

:   - ***Essentials at a glance***

      - **Bug: Fedora 42: Server boot aarch64 image exceeds maximum
        size**

        There is a pending PR.

        ACTION: Paul Maconi (Aggraxis) will take care or the PR
        regarding the size change for aarch64 architecture.

      - **Status /progress Beta Testing**

        Testing so far revealed some minor issues. Really bad, the
        remote interactive installation doesn't work anymore with the
        kickstart file.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-04-02/fedora-server.2025-04-02-15.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-04-02/fedora-server.2025-04-02-15.00.log.html)

<!-- -->

Wednesday, March 26, 2025

:   - ***Essentials at a glance***

      - **Bug: Fedora 42: Server boot aarch64 image exceeds maximum
        size**

        The reasons are obviously specific to the characteristics of
        aarch64 architecture. The x86\_&4 version is not affected.

        AGREED: If the ongoing attempts to reduce the size are not
        successful, Server WG is in favor of an increase to 1.2 GB as an
        exception for now.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-03-26/fedora-server.2025-03-26-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-03-26/fedora-server.2025-03-26-17.00.log.html)

<!-- -->

Wednesday, March 19, 2025

:   - ***Essentials at a glance***

      - **Organisation of Beta Testing**

        Pboy will perform the hardware relataed testing, eseyman takes
        care of SBCs and jwhimpel of VM installation. We will track the
        results in an issue.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-03-19/fedora-server.2025-03-19-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-03-19/fedora-server.2025-03-19-17.00.log.html)

<!-- -->

Wednesday, March 12, 2025

:   - ***Essentials at a glance***

      - **Announcements**

        During US daylight saving time, we adjust the beginning of our
        meeting to 17:00 UTC, so that local daily routines remain
        unchanged.

      - **Scheduled Server podcast for March 11**

        The podcast scheduled for yesterday was delayed, due to staff
        shortage. Mowest will try to join the new meeting together with
        pboy.

      - **Cockpit self-signed certificates change**

        AGREED: Server WG emphasizes that we need access without
        official certificates for private networks

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-03-12/fedora-server.2025-03-12-18.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-03-12/fedora-server.2025-03-12-18.00.log.html)

<!-- -->

Wednesday, March 05, 2025

:   - ***Essentials at a glance***

      - **F43 Change proposal: Disabling support of building OpenSSL
        engines**

        Eseyman will track this.

      - **Open Floor**

        A review of the current state of the \'countme\' statistics is
        to become a regularly recurring agenda item, approximately
        monthly or quarterly.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-03-05/fedora-server.2025-03-05-18.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-03-05/fedora-server.2025-03-05-18.00.log.html)

<!-- -->

Wednesday, February 19, 2025

:   - ***Essentials at a glance***

      - **Server user poll**

        AGREED: We will let the survey closed as decided before.

      - **Ansible assisted installation and configuration of NFS
        service**

        AGREED: Server WG will limit NFS support to NFS 4

      - **Ansible assisted installation and configuration of WEB
        service**

        AGREED: We create a supported web service following the current
        description of a basic setup in the server docs. This is also
        the basis for developing an Ansible playbook.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-02-19/fedora-server.2025-02-19-18.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-02-19/fedora-server.2025-02-19-18.00.log.html)

<!-- -->

Wednesday, February 12, 2025

:   - ***Essentials at a glance***

      - **Server user poll**

        We have a \"brainstorming collection document\" at
        <https://hackmd.io/@pboy/SJzz7VcFJl>. We agreed that everybody
        will enter their idea about data analysis and questions we try
        to answer by data analysis.

        Once the survey is complete, pboy will export the data in a
        secure form and make it available to interested WG members.

      - **Fedora Server Edition - homelab spin-off**

        AGREED Server WG decides to start work on a honelab / homeserver
        spin-off.

      - **FLOCK 2025**

        AGREED Eseyman, Mowest and Pboy will finalize suitable
        contributions to Flock 2025 on the basis of the current
        collection of ideas and submit the application(s).

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-02-12/fedora-server.2025-02-12-18.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-02-12/fedora-server.2025-02-12-18.00.log.html)

    - ***Recent actions status change***

      1.  eseyman DONE will post on redit forum, Fedora general user on
          Discussion, Fedora Devel on Discussion and the corresponding
          mailing lists about the next 2 weeks to participate

      2.  pboy ONGOING will ping Abbra and the freeIPA / localKDC people
          to advice and help us to integrate the right thing into Fedora
          Server.

<!-- -->

Wednesday, February 05, 2025

:   - ***Essentials at a glance***

      - **Server user poll**

        We currently have 4077 participants, of whom 548 have fully
        answered the survey. The others have left out several questions.
        We will continue to promote the poll. The currently scheduled
        end date is February 18.

        ACTION Emmanuel Seyman will post on redit forum, Fedora general
        user on Discussion, Fedora Devel on Discussion and the
        corresponding mailing lists about the next 2 weeks to
        participate

        AGREED mowest takes over the conduct and organization of the
        data analysis. Support from Gwmngilfen, Emmanuel, pboy and
        anyone who is interested

      - **FOSDEM 2025 & FLOCK 2025**

        At *Fosdem* there was a discussion with abbra about freeIPA and
        localKDC (local Key Distribution Center) that is planned for
        F43. It may help us to resolve the UID issue with NFS.

        ACTION pboy will ping Abbra and the freeIPA / localKDC people to
        advice and help us to integrate the right thing into Fedora
        Server.

        Regarding *Flock* we discussed several ideas for contribution.
        We will continue the discussion on the mailing list.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-02-05/fedora-server.2025-02-05-18.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-02-05/fedora-server.2025-02-05-18.00.log.html)

    - ***Actions summary***

      1.  eseyman will post on redit forum, Fedora general user on
          Discussion, Fedora Devel on Discussion and the corresponding
          mailing lists about the next 2 weeks to participate

      2.  pboy will ping Abbra and the freeIPA / localKDC people to
          advice and help us to integrate the right thing into Fedora
          Server.

<!-- -->

Wednesday, January 15, 2025

:   - ***Essentials at a glance***

      - **Ansible assisted installation and configuration of NFS
        service**

        Nothing new so far. But we have a new issue to deal with,
        managing firewall portmapper port (111).

      - **Ansible assisted installation and configuration of WEB
        service**

        Nothing new so far.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-01-15/fedora-server.2025-01-15-18.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-01-15/fedora-server.2025-01-15-18.00.log.html)

<!-- -->

Wednesday, January 8, 2025

:   - ***Essentials at a glance***

      - **Follow-up actions & announcements**

        Just for information see *Current Actions summary* below.

        Fosdem runs from February 1-2. Fedora will be represented by a
        booth, eseyman and pboy will be there.

      - **Server user poll**

        The poll is open and running. We don't have any data on an
        interim result yet.

      - **Revisiting Fedora Server quality criteria and procedures**

        Because of the current issues with NFS which may take some tie
        to get resolved we open another path with [web
        services](https://docs.stg.fedoraproject.org/en-US/fedora-server/services/httpd-basic-setup/).

      - **Work program and goals**

        We postpone this until we have evidence of our server poll.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-01-08/fedora-server.2025-01-08-18.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2025-01-08/fedora-server.2025-01-08-18.00.log.html)

    - ***Current Actions summary***

      1.  ON HOLD pboy will file an issue with releng regarding
          installation media

      2.  ONGOING pboy will close bug #2247872
          (<https://bugzilla.redhat.com/show_bug.cgi?id=2247872>)

      3.  ONGOING pboy will write a draft issue for the goal \"file
          server\" as a base for further finetuning and detailed
          specification

      4.  ONGOING jwhimnpel will develop a Ansible playbook for NFS
          service

      5.  PENDING eseyman review John's playbooks

      6.  DONE Mowest will write a 1st draft of an article about our
          poll.

# Meeting Minutes 2024 {#_meeting_minutes_2024}

Stephen Daley; Peter Boy :page-authors: {author}, {author_2}

Wednesday, December 18, 2024

:   - ***Essentials at a glance***

      - **Ansible assisted installation and configuration of NFS
        service**

        Still discussion how to organize the classic UID/GID issue with
        NFS clients.

        AGREED Regarding NFS we will start with LDAP ansible playbook
        and in parallel establish documentation for the manual way in
        smaller networks.

      - **Server user poll**

        Decided to publish the [Fedora Magazine
        Article](https://fedoramagazine.org/fedora-server-user-survey-your-cattle-or-your-pets/)
        as drafted by Mowest on Dec 20 or Dec 23 and to start the poll
        immediately.

        ACTION DONE: Mowest will write a 1st draft of an article about
        our poll.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-12-18/fedora-server.2024-12-18-18.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-12-18/fedora-server.2024-12-18-18.00.log.html)

    - ***Current Actions summary***

      1.  ON HOLD pboy will file an issue with releng regarding
          installation media

      2.  ONGOING pboy will close bug #2247872
          (<https://bugzilla.redhat.com/show_bug.cgi?id=2247872>)

      3.  ONGOING pboy will write a draft issue for the goal \"file
          server\" as a base for further finetuning and detailed
          specification

      4.  ONGOING jwhimnpel will develop a Ansible playbook for NFS
          service

      5.  PENDING eseyman review John's playbooks

      6.  DONE Mowest will write a 1st draft of an article about our
          poll.

<!-- -->

Wednesday, December 11, 2024

:   - ***Essentials at a glance***

      - **Cockpit boot message**

        We already discussed this topic on [mailing
        list](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-12-11/fedora-server.2024-12-11-18.00.log.html).
        There is a [request to remove the Cockpit
        information](https://bugzilla.redhat.com/show_bug.cgi?id=1635200)
        at every ssh login.

        AGREED: Regarding bug 1635200, WG agrees to keep the current
        Cockpit informational message.

      - **Ansible assisted installation and configuration of NFS
        service**

        It appears that f41's move from dnf to dnf5 has caused my
        ansible modules some heartburn. The issues require further
        research.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-12-11/fedora-server.2024-12-11-18.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-12-11/fedora-server.2024-12-11-18.00.log.html)

<!-- -->

Wednesday, December 4, 2024

:   **Attention**: We agreed to cancel our regular meetings scheduled
    for *Dec 25* and *Jan 1*, but keeping *Dec 18* and *Jan 08*.

    - ***Essentials at a glance***

      - **Server user poll**

        AGREED: The current version in Fedora LimeSurvey instance is the
        final one.

        We discussed and agreed on various steps to spread the word
        about the survey in the Fedora community.

      - **Work program and goals**

        We agree that it is time to produce something really new for
        Fedora Server. Some rough ideas:

        - Creating a *Fedora Home Server* spin for Raspberry Pi / SBCs

        - Installing Fedora Server on Windows WSL or macOS UTM

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-12-04/fedora-server.2024-12-04-18.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-12-04/fedora-server.2024-12-04-18.00.log.html)

    - ***Actions summary***

      1.  ACTION: pboy will compile statistical data on the use of the
          Fedora server for one of the next meetings.

      2.  ACTION: eseyman will post on the Fedora group on Facebook
          about Fedora Server survey.

<!-- -->

Wednesday, November 27, 2024

:   - ***Essentials at a glance***

      - **Server Poll**

        AGREED: The Fedora Server poll should start Dec. 10 24 and run
        until Feb 18 25

        The survey will be available at
        <https://fedoraproject.limequery.com/fedora-server-f41> when it
        has been transferred into the Fedora space.

      - **Ansible assisted installation and configuration of NFS
        service**

        \@jwhimpel plans to update the current repo. Then we can start
        testing and reviewing. He will announce the update on the
        mailing list.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-11-27/fedora-server.2024-11-27-18.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-11-27/fedora-server.2024-11-27-18.00.log.html)

    - ***Actions summary***

      1.  \@jflory7 due:2024-12-04 Import mowest's LimeSurvey survey
          into the Fedora LimeSurvey instance and set it to public

      2.  mowest and pboy will write in FedMag article in time with the
          poll planning

      3.  eseyman will post on the mailing list inviting people to fill
          out the survey when the poll is online

<!-- -->

Wednesday, November 20, 2024

:   - ***Essentials at a glance***

      - **Future release testing procedures**

        **AGREED** pboy writes the draft of a document that describes
        our test strategy.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-11-20/fedora-server.2024-11-20-18.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-11-20/fedora-server.2024-11-20-18.00.log.html)

<!-- -->

Wednesday, November 13, 2024

:   - ***Essentials at a glance***

      - **KVM image migration to KIWI**

        AGREED: The KVM image will be migrated to KIWI now, the
        adjustment of the naming will de dealt with later together with
        the isos.

      - **PostgreSQL -- is our automatic testing sufficient?**

        No decision yet.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-11-13/fedora-server.2024-11-13-18.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-11-13/fedora-server.2024-11-13-18.00.log.html)

    - ***Actions summary***

      1.  ON HOLD pboy will file an issue with releng regarding
          installation media

      2.  ONGOING pboy will close bug #2247872
          (<https://bugzilla.redhat.com/show_bug.cgi?id=2247872>)

      3.  ONGOING pboy will write a draft issue for the goal \"file
          server\" as a base for further finetuning and detailed
          specification

      4.  ONGOING jwhimnpel will develop a Ansible playbook for NFS
          service

      5.  PENDING eseyman review John's playbooks

      6.  DONE eseyman will monitor the change list for possible issues
          which may affect Server

      7.  DONE mowest will reach out to AdamW and discuss how we can use
          the result tables.

      8.  DONE pboy will create a tracking issue and copy the table of F
          40 as a starting point.

      9.  DONE Mowest will create a Lime survey version of the discussed
          draft and reach out to Justin to put the project forward.

      10. PENDING Mowest will write a 1st draft of an article about our
          poll.

<!-- -->

Wednesday, November 06, 2024

:   - ***Essentials at a glance***

      - **New Anaconda installer for Server**

        In F42, only workstation will benefit from the new Anaconda WEB
        UI. Before Server can use it, a lot of missing functionality
        remains to get developed. Workstation will switch to RDP instead
        of VNC. For remote interactive installation, on the kernel line
        the parameter inst.vnc is replaced by inst.rdp.

      - **Current status and further advancement of server docs**

        Thanks to Paul Maconi we have our first entry in the \"Fedora
        Server in a virtualized runtime environment\" project about
        [installing on
        Proxmox](https://docs.fedoraproject.org/en-US/fedora-server/virtualization/vm-install-diskimg-proxmox/).
        Emmanuel will review.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-11-06/fedora-server.2024-11-06-18.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-11-06/fedora-server.2024-11-06-18.00.log.html)

<!-- -->

Wednesday, October 30, 2024

:   - ***Essentials at a glance***

      - **Follow-up actions & announcements**

        ACTION: Mowest will write a 1st draft of an article about our
        poll.

      - **Ansible assisted installation and configuration of NFS
        service**

        NFS 4 is working now, NFS server is running, as well as NFS
        client. Both need some tweaking.

        AGREED Regarding Ansible / NFS we will study and test what we
        have and continue on meeting in 2 weeks.

      - **Looking back at testing release 41**

        AGREED: We discuss this during the next 2-3 weeks on mailing
        list and try to determine a final plan. One issue to take into
        account is the lack of test equipment.

      - **Current membership status and clean up process**

        Our official current list is here: +!link
        <https://fedoraproject.org/wiki/Server>

        We have 7 members that never showed even up for the last 2
        years. Qur usual procedure is to contact them and ask, what they
        are planning. And perhaps agree to retreat. And then we should
        take an initiative to get 1-2 new members. Maybe as part of our
        upcoming poll.

        AGREED: pboy will start to contact dormant members.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-10-30/fedora-server.2024-10-30-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-10-30/fedora-server.2024-10-30-17.00.log.html)

    - ***Actions summary***

      1.  Mowest will write a 1st draft of an article about our poll.

<!-- -->

Wednesday, October 23, 2024

:   - ***Essentials at a glance***

      - **Testing Release 41**

        After a short reading break postponed to next meeting.

      - **Server user poll**

        Justin joined us and made an appointment with Mowest to take
        things further. So we'll be able to start soon.

        AGREED: We finally use the version as now online, i.e. without
        an \"other\" option for \"How are you using Fedora Server?\"

      - **New Business: Generation of the Server KVM image**

        LINK: <https://pagure.io/fedora-server/issue/146>

        With release 42 we will switch to KIWI. ImageFactory is no
        longer support nor available at all. Current efforts:

        LINK
        <https://koji.fedoraproject.org/koji/taskinfo?taskID=125070598>

        AGREED:Server WG agrees to switch to KIWI (4:0:0)

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-10-23/fedora-server.2024-10-23-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-10-23/fedora-server.2024-10-23-17.00.log.html)

    - ***Actions summary***

      1.  DONE: pboy will write an updated summary about our release 4
          testing and we continue on mailing list and next meeting.

      2.  DONE: pboy will write a summary of the current state of our
          poll on the mailing list and we continue on mailing list and
          next meeting.

<!-- -->

Wednesday, October 16, 2024

:   - ***Essentials at a glance***

      - **Testing Release 41**

        We agree that manual testing of our installation media and
        procedures is necessary, and some of this is already included in
        the test plans. Furthermore, it would be desirable to tailor the
        test announcement for servers more closely to server issues.

        ACTION: pboy will write an updated summary about our release 4
        testing and we continue on mailing list and next meeting

      - **Server user poll**

        Mowest has requested access to the Fedora Limesurvey instance
        through Gitlab. Furthermore, he created a draft of our survey in
        a free account of Limesurvey
        (<https://mowest.limesurvey.net/778249?lang=en>).

        ACTION: pboy will write a summary of the current state of our
        poll on the mailing list and we continue on mailing list and
        next meeting.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-10-16/fedora-server.2024-10-16-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-10-16/fedora-server.2024-10-16-17.00.log.html)

    - ***Actions summary***

      1.  pboy will write an updated summary about our release 4 testing
          and we continue on mailing list and next meeting.

      2.  pboy will write a summary of the current state of our poll on
          the mailing list and we continue on mailing list and next
          meeting.

<!-- -->

Wednesday, October 02, 2024

:   - ***Essentials at a glance***

      - **Testing Release 41**

        We still have to test installation on SBCs. Eseyman will take
        this on.

      - **Server user poll**

        Mowest had no success yet in pushing the poll through the other
        Fedora instances. We can't make any progress in the current
        state without that.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-10-02/fedora-server.2024-10-02-17.01.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-10-02/fedora-server.2024-10-02-17.01.log.html)

<!-- -->

Wednesday, September 25, 2024

:   - ***Essentials at a glance***

      - **Server user poll**

        We decided to use the current version with all inserted
        modifications and with the shorter of the formulated
        alternatives on [hackmd.io](https://hackmd.io/@pboy/ByguCouphC).

        Mowest will create a Lime survey version of the discussed draft
        and reach out to Justin to put the project forward.

      - **Testing Release 41**

        We agreed to continue the discussion on the mailing list due to
        running out of time here. **See** [**pboy: Improving our release
        testing efforts. An attempt to summarize our
        discussion**](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/ODISTPROLKECRXX73LA5VUVZJFIFEHRR/)

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-09-25/fedora-server.2024-09-25-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-09-25/fedora-server.2024-09-25-17.00.log.html)

    - ***Actions summary***

      1.  **ONGOING**: eseyman will monitor the change list for possible
          issues which may affect Serve

      2.  **New**: Mowest will create a Lime survey version of the
          discussed draft and reach out to Justin to put the project
          forward.

<!-- -->

Wednesday, September 18, 2024

:   - ***Essentials at a glance***

      - **Testing Release 41**

        The discussion focused on optimizing our approach to release
        testing. There was agreement on the one hand that the test
        program should be integrated into the distribution QA, and on
        the other hand that tests of individual functionalities should
        be automated. Irrespective of this, there is a need for manual
        testing, particularly of the (hardware) installation media.

        Action: pboy will create a summary on the mailing list, which
        will be the basis for further discussion.

      - **Server user poll**

        We finally agreed on 4 goals:

        - Who is the audience for Fedora Server

        - Where is Fedora Server primarily used: Hardware or VM

        - What are the main use cases for Fedora Server

        - Where are future efforts of the Fedora Server WG best applied

          A final version is to be decided at the next meeting.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-09-18/fedora-server.2024-09-18-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-09-18/fedora-server.2024-09-18-17.00.log.html)

    - ***Actions summary***

      1.  **ACTION**: **ONGOING** eseyman will monitor the change list
          for possible issues which may affect Server

      2.  **ACTION**: **DONE** mowest will reach out to AdamW and
          discuss how we can use the result tables.

<!-- -->

Wednesday, September 04, 2024

:   - ***Essentials at a glance***

      - **Ansible assisted installation and configuration of NFS
        service**

        Jwhimpel has finished a first version of the Ansible code
        including a short documentation. We will discuss this in detail
        at the next meeting when all members have been able to test it.

      - **Testing Release 41**

        Ticket #144 is available for the test. Based on a discussion
        with adamw, pboy will create a draft test description in the
        Fedora Server Wiki area. The aim is to automate as much as
        possible.

        Eseyman has created a list of potentially problematic changes,
        see addendum to the invitation. The list will also be added to
        the ticket. We will discuss it at the next meeting.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-09-04/fedora-server.2024-09-04-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-09-04/fedora-server.2024-09-04-17.00.log.html)

    - ***Actions summary***

      1.  **ACTION**: **ONGOING** eseyman will monitor the change list
          for possible issues which may affect Server

      2.  **ACTION**: **DONE** pboy will create a tracking issue and
          copy the table of F 40 as a starting point.

      3.  **ACTION**: **ONGOING** mowest will reach out to AdamW and
          discuss how we can use the result tables.

<!-- -->

Wednesday, August 28, 2024

:   - ***Essentials at a glance***

      - **Ansible assisted installation and configuration of NFS
        service**

        The server roles are basically working. Jwhimpel will add some
        documentation how to use (and test) it. There are some topics we
        will have to decide after everyone could use it, e.g. type of
        mounts. On the client side, we tend to only support and handle
        Fedora.

      - **Testing Release 41**

        We decided to use the same procedure as last time (F40) for now.

        **ACTION**: eseyman will monitor the change list for possible
        issues which may affect Server

        **ACTION**: pboy will create a tracking issue and copy the table
        of F 40 as a starting point.

        We want to systematize the process and make greater use of the
        Fedora options, e.g. the results tables that are created for
        each build.

        **ACTION**: mowest will reach out to AdamW and discuss how we
        can use the result tables.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-08-28/fedora-server.2024-08-28-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-08-28/fedora-server.2024-08-28-17.00.log.html)

    - ***Actions summary***

      1.  **ACTION**: **DONE** pboy will create 2 empty docs for
          installation & configuration to the repo, then everyone can
          add relevant topics to it and migrate the current integrated
          doc.

      2.  **ACTION**: **DONE** pboy will add all WG core members as
          committers to our pagure repo.

      3.  **ACTION**: eseyman will monitor the change list for possible
          issues which may affect Server

      4.  **ACTION**: pboy will create a tracking issue and copy the
          table of F 40 as a starting point.

      5.  **ACTION**: mowest will reach out to AdamW and discuss how we
          can use the result tables.

<!-- -->

Wednesday, August 21, 2024

:   - ***Essentials at a glance***

      - **Follow-up, findings and conclusions from Flock 2024**

        Eseyman gave an [overview of his impressions and
        experiences](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/ZFEQZHECF4DNJA3VH4UIGGITRLFCXKFH/).

        One wish that was expressed was to use Fedora as a router,
        similar to OpenWRT. It was agreed that this is not possible
        within the framework of Fedora Server, as the requirements for
        system and data security are too different.

        One positive feedback was that Fedora was the slowest moving as
        well as the most backward compatible, and nevertheless with
        always up-to-date versions of the server software bits, of the
        Fedora project. A most welcome characteristic of our goals for
        Fedora Server Edition.

      - **Optimizing NFS service documentation**

        jwhimpel will start to add topics the the empty doc templates
        when he completed the first version of the Ansible code.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-08-21/fedora-server.2024-08-21-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-08-21/fedora-server.2024-08-21-17.00.log.html)

    - ***Actions summary***

      1.  **DONE** eseyman will post Flock recap to the list.

      2.  **DONE** jednorozec will implement the patch to bug #2247872

<!-- -->

Wednesday, August 14, 2024

:   - ***Essentials at a glance***

      - **Follow-up, findings and conclusions from Flock 2024**

        We considered a number of different topics that were discussed.
        By and large, our current course in the further development of
        Fedora Server Edition has proven itself. The most important
        change will be the implementation of Ansible for our special
        supported services (previous server roles).

        Everyone agrees that getting to know each other and discussing
        goals and next steps in person was a hugely positive experience
        and a tremendous motivational boost.Nothing else can replace
        that. Flock was very, very worthwhile and all the effort was
        very rewarding. Flock next year is already a positive
        expectation.

        **ACTION**: eseyman will post his Flock recap to the list.

      - **Ansible assisted installation and configuration of NFS
        service**

        We decided to do the development in stg branch and add the
        directory structure there, too.

        **AGREED**: Regarding distribution we prefer the rpm path of
        action.

        **ACTION**: eseyman review John's playbooks

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-08-14/fedora-server.2024-08-14-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-08-14/fedora-server.2024-08-14-17.00.log.html)

    - ***Actions summary***

      1.  **ONGOING** pboy will write a draft issue for the goal \"file
          server\" as a base for further finetuning and detailed
          specification

      2.  **PENDING** pboy will create a hackmd draft for a collection
          of questions about Fedora Server in a virtualized environment

      3.  **PENDING** mowest will come up with a plan and steps to
          conduct the survey on discussion -- waiting for a draft of
          collection of questions

      4.  **NEW** jednorozec will implement the patch to bug #2247872

<!-- -->

Wednesday, July 31, 2024

:   - ***Essentials at a glance***

      - **Ansible assisted installation and configuration of NFS
        service**

        We discussed again about the specific goal we want to achive
        with the Ansible Playbook.

        **AGREED** Server WG agrees to the goal as defined in comment
        <https://pagure.io/fedora-server/issue/138#comment-920322> to
        issue 138

      - **Optimizing NFS service documentation**

        We want to split the current NFS draft in 2 parts: Installation
        and Configuration.

        **ACTION** ***DONE***: pboy will create 2 empty docs for
        installation & configuration to the repo

        **AGREED** to postpone this until we have a working version of
        the Ansible playbook.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-07-31/fedora-server.2024-07-31-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-07-31/fedora-server.2024-07-31-17.00.log.html)

    - ***Actions summary***

      1.  **DONE** pboy will add all WG core members as committers to
          our pagure repo.

      2.  **DONE** pboy will create 2 empty docs for installation &
          configuration to the repo

      3.  **CANCELED** pboy will close bug #2247872
          (<https://bugzilla.redhat.com/show_bug.cgi?id=2247872>) --
          There is still an ongoing discussion about improving Server
          first boot process.

      4.  **ONGOING** pboy will write a draft issue for the goal \"file
          server\" as a base for further finetuning and detailed
          specification

<!-- -->

Wednesday, July 24, 2024

:   - ***Essentials at a glance***

      - **Renaming distribution media for Fedora Server**

        **AGREED**: We defer the renaming until RelEng has decided about
        the future Fedora tool set AND has updated the documentation.

        **ACTION**: ***canceled*** pboy will file an issue with releng
        regarding installation media

      - **Ansible assisted installation and configuration of NFS
        service**

        Eseyman has packed the the robertdebock roles in an rpm :
        <https://eseyman.fedorapeople.org/ansible-robertdebock-roles/>.
        It's an alternative to the current Fedora standard package.
        Jwhimple has 4 roles ready, but can't upload due to permission
        issues and incomplete Server repo configuration.

        **ACTION**: pboy will add all WG core members as committers to
        our pagure repo.

      - **Optimizing NFS service documentation**

        We want to split the current NFS draft in 2 parts: Installation
        and (Basic) Configuration. Jwhimpel will start do add at löeast
        bullet point to outline the intended information. To support
        this, pboy will add correspoding empty files. We agreed to
        document the process using Ansible and by using manually CLI.
        Whether and how we take Cockpit into account is still to be
        decided.

        **ACTION**: pboy will create 2 empty docs for installation &
        configuration to the repo, then everyone can add relevant topics
        to it and migrate the current integrated doc.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-07-24/fedora-server.2024-07-24-16.10.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-07-24/fedora-server.2024-07-24-16.10.log.html)

    - ***Actions summary***

      1.  **ACTION**: ***new*** pboy will add all WG core members as
          committers to our pagure repo.

      2.  **ACTION**: ***new*** pboy will create 2 empty docs for
          installation & configuration to the repo, then everyone can
          add relevant topics to it and migrate the current integrated
          doc.

      3.  **ACTION**: ***canceled*** pboy will file an issue with releng
          regarding installation media

<!-- -->

Wednesday, July 17, 2024

:   - ***Essentials at a glance***

      - **Ansible assisted installation and configuration of NFS
        service**

        Discussed the specific goal of this work. Agreed to focus on a
        playbook for commen/default use case and provide hooks to extend
        to further local use cases.

      - **Fedora Server in a virtualized runtime environment**

        We agreed to start with a poll and ask users how they use Fedora
        Server Edition and what they are missing in the first place.
        Mowest and pboy will work on it.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-07-17/fedora-server.2024-07-17-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/fedora-meeting/2023-11-15/fedora-server.2023-11-15-18.00.log.html)

    - ***Actions summary***

      1.  ACTION: pboy will create a hackmd draft for a collection of
          questions about Fedora Server in a virtualized environment

      2.  ACTION: mowest will come up with a plan and steps to conduct
          the survey on discussion

<!-- -->

Wednesday, July 10, 2024

:   - ***Essentials at a glance***

      We had an open discussion about ongoing activities.

      - Humaton started to check out Kiwi to create Server iso
        distributables. There is a SuSE add-on to achieve that.

      - Humaton will care about ticket #114, which is an undecided long
        standing issue regarding LLMR.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-07-10/fedora-server.2024-07-10-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-07-10/fedora-server.2024-07-10-17.00.log.html)

<!-- -->

Wednesday, July 03, 2024

:   - ***Essentials at a glance***

      - **Change to a weekly meeting schedule**

        **AGREED**: Server WG switches to a *weekly meeting*

      - **Ansible assisted installation and configuration of NFS
        service**

        jwhimnpel will provide 2 Ansible roles in about 2 weeks for
        further discussion and testing.

        eseyman and mowest will work on improving the current docs
        draft.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-07-03/fedora-server.2024-07-03-17.01.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-07-03/fedora-server.2024-07-03-17.01.log.html)

    - ***Actions summary***

      1.  pboy will file an issue with releng regarding installation
          media - pending

      2.  pboy will close bug #2247872 - pending because of ongoing work

      3.  pboy will write a draft issue for the goal \"file server\" as
          a base for further finetuning and detailed specification -
          ongoing

      4.  jwhimpel will provide 2 Ansible roles for NFS service

      5.  eseyman and mowest will start reviewing the currnt NFS doc
          draft

<!-- -->

Wednesday, June 26, 2024

:   - ***Essentials at a glance***

      We had an open discussion about our various ongoing works.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-06-26/fedora-server.2024-06-26-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-06-26/fedora-server.2024-06-26-17.00.log.html)

<!-- -->

Wednesday, June 19, 2024

:   - ***Essentials at a glance***

      - **Ansible assisted installation and configuration of NFS
        service**

        We discussed the results of a short poll about the documentation
        part and how to improve the current article. Amoung others we
        want to split into installation and configuration and in each
        part describe the manual procedure and the Ansible usage.

        We will add a new subdirectory to our repo for Ansible scripts.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-06-19/fedora-server.2024-06-19-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-06-19/fedora-server.2024-06-19-17.00.log.html)

    - ***Actions summary***

      1.  **Action**: pboy will create an additional directory
          fedora-ansible in fedora-server repo

<!-- -->

Wednesday, June 12, 2024

:   - ***Essentials at a glance***

      - **Elevating Fedora Server VM distribution image**

        Jason will start to elevate Fedora Server VM distribution image
        to a release requirement as the other Server installation images

      - **Fixing the \"Everything\" installation medium problem**

        **AGREED**: Server WG agrees that the Fedora Server option has
        to be removed from the Everything Install medium in the long
        term.

        W'll pick this up again as soon as we have free resources.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-06-12/fedora-server.2024-06-12-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-06-12/fedora-server.2024-06-12-17.00.log.html)

<!-- -->

Wednesday, June 05, 2024

:   - ***Essentials at a glance***

      - **Fedora Server goal(s) and \"story\" for F41 / F42**

        **AGREED**: WG's goal is to provide a spin \"local or public
        file server (NFS, Samba, Ansible support)

        **AGREED**: WG's goal is to improve the use of Fedora Server in
        a VPS infrastructure and to promote it as a standard offering.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-06-05/fedora-server.2024-06-05-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-06-05/fedora-server.2024-06-05-17.00.log.html)

    - ***Actions summary***

      1.  **Action**: pboy will write a draft issue for the goal \"file
          server\" as a base for further finetuning and detailed
          specification.

<!-- -->

Wednesday, May 01, 2024

:   - ***Essentials at a glance***

      - **Revisiting Server installation media naming convention**

        **AGREED**: Server WG decides to rename the installation media:
        DVD → offline , netboot → online, KVM → virt, and rawsbc for ARM
        raw image.

        **AGREED**: Server WG decides on a consistent naming convention
        according to the scheme:
        \"Fedora-Server-\<rel\>-\<method\>-\<arch\>-\<version\>.\<filetype\>\"

      - **Elevating Fedora Server VM distribution image**

        jwhimpel will check the details of the procedure and report back
        next meeting.

      - **Open Floor**

        We will start to discuss and develop NFS service supported by
        documentation and by Ansible.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-05-01/fedora-server.2024-05-01-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-05-01/fedora-server.2024-05-01-17.00.log.html)

    - ***Actions summary***

      1.  **Action**: pboy will file an issue with releng.

<!-- -->

Wednesday, Apr 17, 2024

:   - ***Essentials at a glance***

      - **LVM2 configuration & ARM SBC installation**

        The issue is resolved, but but - as Vojtech Trefny, one of ghe
        maintgainers, put it - \"unfortunately not thanks to the changes
        that I made\".

        **AGREED**: Server WG considers the case closed.

      - **Testing F40**

        **AGREED**: Server WG considers F40 ready for publication and
        closes this topic.

      - **Our \"story\" for F40**

        **AGREED**: Regarding our \"story\" for F40 we stick sich ARM
        SBC.

      - **Our \"Fedora Server goal(s) and \"story\" for F41 / F42**

        See: [issue #134](https://pagure.io/fedora-server/issue/134)

        We narrowed the options down to \"Fedora Server VM as VPS\",
        \"Server Edition as identity server \", and \"Server Edition as
        local or public file server \".

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-04-17/fedora-server.2024-04-17-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-04-17/fedora-server.2024-04-17-17.00.log.html)

    - ***Actions summary***

      1.  **Action**: pboy will close [bug
          #2247872](https://bugzilla.redhat.com/show_bug.cgi?id=2247872)

<!-- -->

Wednesday, Apr 03, 2024

:   - ***Essentials at a glance***

      - **Review installation media**

        The discussion revealed obvious inconsistencies between the ways
        of creating our various installation media that have evolved
        over time. All of this is difficult to deal with in a matrix
        discussion. Therefore:

        **AGREED**: An additional meeting out of turn on Wednesday,
        April 10, 17:00 UTC in the Matrix Sever room exclusively to
        discuss the Review Installation Media topic.

        **ACTION**: pboy will prepare the room and provide a test
        opportunity.

      - **Testing F40**

        No additional issues found yet, but not all planned tests have
        been carried out yet.

        It is unclear how and where the test results should be merged on
        the server test page. Pboy will contact Adam about this.

      - **Revisiting Server installation media naming convention**

        The online/offline proposal is welcomed, but the overall
        solution should be presented more clearly.

        A decision will be aimed for by mid-May at the latest so that
        there is sufficient time for implementation.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-04-03/fedora-server.2024-04-03-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-04-03/fedora-server.2024-04-03-17.00.log.html)

<!-- -->

Wednesday, Mar 20, 2024

:   - ***Essentials at a glance***

      - **Follow-up actions & announcements**

        - We will first discuss a possible change to the time of our
          meetings on the mailing list and decide at the next meeting.

      - **LVM2 configuration**

        !link <https://bugzilla.redhat.com/show_bug.cgi?id=2247872>

        The /etc/lvm/devices directory in
        Fedora-Server-KVM-40_Beta-1.9.x86_64.qcow2 is empty now. So far
        no check whether First Boot generates a suitable entry.

        **INFO update**: Beta 1.10 contains a devices file in both
        server images (KVM and aarch64 SBC). So the issue is not
        resolved yet.

        Action: cooltshirtguy will monitor and check the aarch64 SBC
        image, specifically Raspberry Pi.

      - **F40 release tests**

        We have selected items to be tested and allocated work. Details
        at

        !link <https://pagure.io/fedora-server/issue/125/>

      - **Open Floor**

        **!info**: Unfortunately, no movement on the Apache / httpd
        configuration layout yet

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-03-20/fedora-server.2024-03-20-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-03-20/fedora-server.2024-03-20-17.00.log.html)

<!-- -->

Wednesday, Mar 06, 2024

:   - ***Essentials at a glance***

      - **Follow-up actions & announcements**

        We are discussing how to equalize the times of the meetings of
        the Server WG and the Epel Team to enable everyone to
        participate in both. To be continued on the mailing list.

      - **Review installation media**

        An initial analysis has revealed a number of warning messages
        about comps files not being found. Details in:

        Link:
        <https://pagure.io/pungi-fedora/blob/main/f/variants-fedora.xml#_46>

        Link: <https://pagure.io/fedora-server/issue/130>

        *Agreed*: Sever WG will check the current compose groups in
        issues on fedora-server repo.

      - **LVM2 configuration & ARM SBC installation**

        The arm-image-installer script is fixed.

        The LVM configuration issue is still open.

        Link: <https://bugzilla.redhat.com/show_bug.cgi?id=2247872#c19>

        This issue is not accepted as release blocker. So it can happen
        that we release a kind of crap image for the 2nd time in a row.

        But LVM group seems to be working hard on it.

      - **F40 Change Set items requiring our attention**

        Eseyman generated a list of items requiring our attention

        Link:
        <https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/message/CNH57V7LT4GMQN676XFDJWQ6U46BGDMK/>

        *Agreed*: Server WG will continue to discuss this topic on
        mailing list

      - **Open Floor**

        Nothing to discuss today.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-03-06/fedora-server.2024-03-06-18.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-03-06/fedora-server.2024-03-06-18.00.log.html)

<!-- -->

Wednesday, Feb 21, 2024

:   Our first meeting on Matrix.

    - ***Essentials at a glance***

      - **Review installation media**

        We are trying here for more then 2 years for now without a lot
        or results. At Fosdem I met Tomáš, who is very experienced in
        release engineering (to put it a bit understated) and who has
        offered to help us with this. This is a great opportunity for
        Fedora Server Edition.

        After an initial discussion about necessary and desired changes,
        we agreed that Tomáš would further analyze the current
        configuration files and compile them in a blog or on the server
        list.

      - **Revisiting Server installation media naming convention**

        The various server installation media are (still) named very
        differently. But it is now too late for a change to Release 40.

        *Agreed*: We further discuss naming convention on mailing list
        and aim to make a final decision in 4 weeks latest. And then it
        is up to releng to find a workable timeframe. There is no
        urgency.

      - **LVM2 default configuration change**

        The issue is currently not resolved.

        A proper resolution will involve an anaconda fix as well as a
        fix in arm-image-installer. We will continue to work on it.

        Link: <https://bugzilla.redhat.com/show_bug.cgi?id=2258764>

      - **Open Floor**

        Cloud Sig will stop to maintain ImageFactory. For F41 we have to
        select another tool for building the non-iso images. Probable
        choices are Lorax, KIWI, or OSBuild, depending on what is
        supported in pungi and what artifacts are supported by the
        different tools.

        Neil would support a move to Kiwi if we decide to do so. We want
        to make a final decision once releng has decided on available
        and supported options.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-02-21/fedora-server.2024-02-21-18.03.html)

    - [Full
      log](https://meetbot.fedoraproject.org/meeting_matrix_fedoraproject-org/2024-02-21/fedora-server.2024-02-21-18.03.log.html)

<!-- -->

Wednesday, Feb 07, 2024

:   Continuing the Jan 31 meeting

    - ***Essentials at a glance***

      - **LVM2 default configuration change**

        We finally got information about the reasons for the changes in
        LVM default configuration and proper ways to resolve the ARM SBC
        installation issue.

        In short we should retain the current default LVM configuration
        which includes a system.devices file and adjust the
        arm-image-installer script und our documentation.

      - **Test planning for F40**

        We have set up a [list of manually \"smoke
        tests\"](https://hackmd.io/NtO4O9vRT3a71UMZMkceoA?both). We now
        need working group members or other interested parties to take
        over some of the tests and enter their FAS names in the
        corresponding column.

      - **Open Floor**

        We will switch our meetings from IRC to Matrix starting February
        21, provided we can make the necessary organizational
        arrangements in time.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/fedora-meeting/2024-02-07/fedora-server.2024-02-07-18.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/fedora-meeting/2024-02-07/fedora-server.2024-02-07-18.00.log.html)

    - ***Actions summary***

      1.  eseyman will check the change proposal set for items we should
          aware of and care about.

<!-- -->

Wednesday, Jan 31, 2024

:   - ***Essentials at a glance***

      - **LVM2 default configuration change**

        Currently the default LVM configuration results in vgscan and
        vgchange not inspecting new devices that are not listed in
        /etc/lvm/devices/system.devices. A follow-up to this is also the
        error when creating aarch64 SBC filesystem images.

        There was neither a change proposal nor a release notes entry
        for the configuration change, nor any announcement. Accordingly,
        it is also not known why the change was made.

        **ACTION**: eseyman will try to contact the maintainers and get
        information why the change was made.

      - **Test planning for F40**

        We will continue discussion next meeting

      - **A \"story\" for each release**

        We will continue discussion next meeting

    - [Meeting
      summary](https://meetbot.fedoraproject.org/fedora-meeting/2024-01-31/fedora-server.2024-01-31-18.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/fedora-meeting/2024-01-31/fedora-server.2024-01-31-18.00.log.html)

    - ***Actions summary***

      New business

      1.  pboy will create a thread on mailing list to discuss the
          option for LVM fix.

      2.  jwhimpel will try to contact <linux-lvm@lists.linux.dev>

      3.  pboy will create a draft wiki page to help to organise and
          coordinate our release testing efforts.

<!-- -->

Wednesday, Jan 17, 2024

:   - ***Essentials at a glance***

      - **LVM configuration issues**

        Currently the default LVM configuration results in vgscan and
        vgchange not inspecting new devices that are not listed in
        /etc/lvm/devices/system.devices. A follow-up to this is also the
        error when creating aarch64 SBC filesystem images.

        There was neither a change proposal nor a release notes entry
        for the configuration change, nor any announcement. Accordingly,
        it is also not known why the change was made.

        **ACTION**: eseyman will try to contact the maintainers and get
        information why the change was made.

      - **Test planning for F40**

        We will continue discussion next meeting

    - [Meeting
      summary](https://meetbot.fedoraproject.org/fedora-meeting/2024-01-17/fedora-server.2024-01-17-18.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/fedora-meeting/2024-01-17/fedora-server.2024-01-17-18.00.log.html)

    - ***Actions summary***

      1.  pboy will write a info about changing the timeout value and
          nirik will review -- still work in progress

      2.  mowest will take care of discussed modifications of the Server
          download page. - still work in progress

      3.  eseyman will try to contact the maintainers and get
          information why the change was made. = Meeting Minutes 2023
          Stephen Daley; Peter Boy

<!-- -->

Wednesday, Dec 06, 2023

:   - ***Essentials at a glance***

      - **Next meeting on January 19, 2024!**

      - **Fedora Server release and quality criteria**

        We want to further discuss this on mailing list and in the
        ticket.

      - **Work program and goals for F40**

        Various ideas discussed, further discussion on the mailing list
        and in the ticket .

      - **Test planning for F40**

        Extensive discussion without a conclusive result yet. Discussion
        to be continued at the next meeting.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/fedora-meeting/2023-11-15/fedora-server.2023-11-15-18.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/fedora-meeting/2023-11-15/fedora-server.2023-11-15-18.00.log.html)

    - ***Actions summary***

      1.  *ACTION*: Mowest will take care ot disussed modifications of
          the Server download page.

<!-- -->

Wednesday, Nov 15, 2023

:   - ***Essentials at a glance***

      - **Fedora release 39 - State of Server media and Download Web
        page**

        The Situation regarding aarch64 on SBC is a bit better then 2
        weeks ago, but still but still not satisfactory. A SBC is now
        installable if you don't use an installation host with actrive
        LVM drives, but use e.g. Fedora Workstation. In this respect, it
        would be disproportionate to continue to regard this as a
        release blocker. The problem must now be solved for Release 40.

        It's really unfortunate, that we discovered the bug so late in
        the Beta process. We need to review our testing procedures. We
        have relied too much on the automated tests.

        For the next release we should improve the download page. We
        need to find a better name as the outdated term \"DVD\" and
        should clearly distinguish the SBC variant from the other
        installations, it is best to introduce a separate section.

        ACTION: Mowest will take care ot disussed modifications of the
        Server download page.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/fedora-meeting/2023-11-15/fedora-server.2023-11-15-18.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/fedora-meeting/2023-11-15/fedora-server.2023-11-15-18.00.log.html)

    - ***Actions summary***

      1.  *ACTION*: Mowest will take care ot disussed modifications of
          the Server download page.

<!-- -->

Wednesday, Nov 01, 2023

:   - ***Essentials at a glance***

      - **Fedora release 39 rc current state and how to continue**

        The x86_64 versions work great. There is still a severe bug with
        installing the aarch64 SBC version on Fedora Server.

        *AGREED*: If the LVM issue can not be resolved for f39 release,
        Server WG would like to opt out providing a f39 installation
        medium for aarch SBC, continue to distribute f38 and encourage
        to update using dnf.

      - **Package fail2ban orphaned**

        In the meantime the orphaned package was picked by a new
        maintainer.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/fedora-meeting/2023-11-01/fedora-server.2023-10-11-01.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/fedora-meeting/2023-11-01/fedora-server.2023-11-01-17.00.log.html)

    - ***Actions summary***

      none

<!-- -->

Wednesday, Oct 18, 2023

:   - ***Essentials at a glance***

      - **Maximum size of aarch64 Server network install image**

        *AGREED*: Enlarge aarch64 net install media to 1 GB. Letting
        everything else as is.

      - **Fedora release 39 beta first experience and how to continue**

        Mowest has tested the x86_64 installation image and pb the VM
        image. No issues found.

        There is still an issue with the aarch64 on SBC version. pboy
        will check.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/fedora-meeting/2023-10-18/fedora-server.2023-10-18-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/fedora-meeting/2023-10-18/fedora-server.2023-10-18-17.00.log.html)

    - ***Actions summary***

      none

<!-- -->

Wednesday, Sep 20, 2023

:   - ***Essentials at a glance***

      - **Follow up actions**

        1.  Ongoing: pboy will write a info about how to configure the
            timeout value and nirik will review. git+ Nothing to
            announce today.

      - **F40 Change proposal dropping sshd.socket file**

        ACTION: jwhimpel will keep an eye on behalf of Server WG on the
        \"Change proposal dropping sshd.socket file\" discussion.

      - **Fedora release 39 beta first experience and how to continue**

        ACTION: jdubby will deploy some of the wildfly quickstarts via
        localhost and report at our next meeting.

      - \*F39/40 Work Project: Fedora Server in a virtualized runtime
        environment \*

        ACTION: mowest and pboy will prepare a community action about
        Fedora Server in a virtualized runtime environment

    - [Meeting
      summary](https://meetbot.fedoraproject.org/fedora-meeting/2023-09-20/fedora-server.2023-09-20-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/fedora-meeting/2023-09-20/fedora-server.2023-09-20-17.00.log.html)

    - ***Actions summary***

      1.  *ACTION*: Ongoing pboy will write a info about how to
          configure the timeout value and nirik will review

      2.  *ACTION*: jwhimpel will keep an eye on behalf of Server WG on
          the \"Change proposal dropping sshd.socket file\" discussion.

      3.  *ACTION*: mowest and pboy will prepare a community action
          about Fedora Server in a virtualized runtime environment

<!-- -->

Wednesday, Sep 06, 2023

:   - ***Essentials at a glance***

      - **Follow up actions**

        1.  Ongoing: pboy will write a info about how to configure the
            timeout value and nirik will review. git+ Nothing to
            announce today.

      - **F39 Work Project: Fedora Server on (ARM) SBC**

        ACTION: pboy will complete the intro text about Fedora Server
        and ARM SBC

      - **Work Project: Using Ansible to install and configure Wildfly**

        ACTION: jdubby will deploy some of the wildfly quickstarts via
        localhost and report at our next meeting.

      - **Fedora release 39 test planning**

        ACTION: pboy will open a mailing list thread about F39 change
        set to review changes and come up with a list of those that
        affect server edition

    - [Meeting
      summary](https://meetbot.fedoraproject.org/fedora-meeting/2023-09-06/fedora-server.2023-09-06-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/fedora-meeting/2023-09-06/fedora-server.2023-09-06-17.00.log.html)

    - ***Actions summary***

      1.  *ACTION*: Ongoing pboy will write a info about how to
          configure the timeout value and nirik will review

      2.  *ACTION*: pboy will complete the intro text about Fedora
          Server and ARM SBC

      3.  *ACTION*: jdubby will deploy some of the wildfly quickstarts
          via localhost and report at our next meeting.

      4.  *ACTION*: pboy will open a mailing list thread about F39
          change set to review changes and come up with a list of those
          that affect server edition

<!-- -->

Wednesday, Aug 16, 2023

:   - ***Essentials at a glance***

      - **Follow up actions**

        1.  Ongoing: pboy will write a info about how to configure the
            timeout value and nirik will review. git+ Nothing to
            announce today.

      - **F39 Work Project: Fedora Server on (ARM) SBC (**

        pboy will write a first draft of the first part of the text
        about Server on SBC (Purpose and summary of the literature).
        Further discussion on mailing list,

      - **Work Project: Using Ansible to install and configure Wildfly**

        The certificate issue got resolved. Next step is installation
        and configuration of the proxy (nginx). Detailed discussion on
        mailing list.

      - **Fedora release 39 test planning**

        After the first impression, there is no potentially critical
        change that requires our special attention and testing.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/fedora-meeting/2023-08-16/fedora-server.2023-08-16-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/fedora-meeting/2023-08-16/fedora-server.2023-08-16-17.00.log.html)

    - ***Actions summary***

      1.  *ACTION*: Ongoing pboy will write a info about how to
          configure the timeout value and nirik will review

<!-- -->

Wednesday, Jul 19, 2023

:   - ***Essentials at a glance***

      - **Follow up actions**

        1.  Ongoing: pboy will write a info about how to configure the
            timeout value and nirik will review.

        2.  Done: eseyman will review the NFS documentation

      - **Announcement**

        Nothing to announce today.

      - **Fedora 39 change Proposal: Enable Firmware Update
        Notification**

        In a short discussion we had voted 7:0:0 in favour of the
        change. To add an email notification is currently useless,
        because we don't install any email capability by default.

      - **LLMNR should be disabled in resolved in f39**

        Nirik and pboy are to formulate a solution on behalf of the WG.

      - **Work Project: Using Ansible to install and configure Wildfly**

        We made various decisions

        - We'll use nginx as proxy solution, because it is able to
          handle the proxy protocol.

        - pboy asks Java SIG about best practise for a installation
          location.

        - We will create a separate log. Volume for /opt/wildfly
          according the Fedora Server Edition storage concept

    - [Meeting
      summary](https://meetbot.fedoraproject.org/fedora-meeting/2023-07-19/fedora-server.2023-07-19-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/fedora-meeting/2023-07-19/fedora-server.2023-07-19-17.00.log.html)

<!-- -->

Wednesday, Jul 05, 2023

:   - ***Essentials at a glance***

      - **Follow up actions**

        1.  Ongoing: pboy will write a info about how to configure the
            timeout value and nirik will review.

        2.  Ongoing: eseyman will review the NFS documentation - still
            WIP

      - **Announcement**

        AS it looks at the moment the committee has accepted and is
        planning with a presentation: Fedora Server Edition -- Quo
        Vadis? Unfortunately a workshop about Server in virtual
        environment, that I proposed, too, didn't make it.

      - **Could we drop Active Directory requirements from Fedora
        release criteria?**

        **Agreed** WG agrees about to use automated testing using Samba
        AD as the server end (instead of a native Windows server) and to
        keep the status of release criteria.

        Full compatibility with Windows Server remains the goal
        regardless of the testing procedure. And an *inability to
        connect to a real Microsoft AD server remains a release blocking
        criterion*, since that is (and remains) the most prominent
        domain controller in the world.

      - **F39 Work Project: Fedora Server on (ARM) SBC**

        We'll complete the current device documentation draft with the
        devices nominated until now.

      - **Open Floor**

        We want to replace the \"DVD\" in the naming of the installation
        media by \"STD\".

    - [Meeting
      summary](https://meetbot.fedoraproject.org/fedora-meeting/2023-07-05/fedora-server.2023-07-05-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/fedora-meeting/2023-07-05/fedora-server.2023-07-05-17.00.log.html)

    - ***Actions summary***

      1.  *ACTION*: Ongoing pboy will write a info about how to
          configure the timeout value and nirik will review

<!-- -->

Wednesday, Jun 21, 2023

:   - ***Essentials at a glance***

      - **Follow up actions**

        1.  Ongoing: pboy will write a info about how to configure the
            timeout value and nirik will review.

        2.  Ongoing: eseyman will review the NFS documentation - still
            WIP

      - **Announcement**

        pboy has submitted a talk and a workshop idea to Flock

      - **F39 Work Project: Fedora Server on (ARM) SBC**

        W'll compose a devices list.

        ACTION eseyman to post his ARM SBC list to the list by next
        week.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/fedora-meeting/2023-06-21/fedora-server.2023-06-21-17.02.html)

    - [Full
      log](https://meetbot.fedoraproject.org/fedora-meeting/2023-06-21/fedora-server.2023-06-21-17.02.log.html)

    - ***Actions summary***

      1.  *ACTION*: Ongoing pboy will write a info about how to
          configure the timeout value and nirik will review

<!-- -->

Wednesday, Jun 07, 2023

:   - ***Essentials at a glance***

      - **Follow up actions**

        1.  Ongoing: pboy will write a info about how to configure the
            timeout value and nirik will review.

      - **Announcement**

        This year's Flock will be in-person Aug. 2-4 in Cork, Ireland.
        We'll discuss our contribution on mailing list and next meeting.

      - **F39 Work Project: Fedora Server on (ARM) SBC**

        *AGREED*: The WG agrees on part 1 of the plan in issue 108 and
        will create a reference list.

        W'll start a list of desirable or available devices in a comment
        to on tracking issue #108.

        W'll consider the Phoronix list of tests for comparison.

      - **Using Ansible to install and configure Wildfly**

        We postpone working on it until July, when jwhimpel has time
        again.

      - **F39/40 Work Project: Fedora Server in a virtualized runtime
        environment**

        *AGREED*: WG will perform the community survey as proposed in
        #110 .

    - [Meeting
      summary](https://meetbot.fedoraproject.org/fedora-meeting/2023-06-07/fedora-server.2023-06-07-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/fedora-meeting/2023-06-07/fedora-server.2023-06-07-17.00.log.html)

    - ***Actions summary***

      1.  *ACTION*: Ongoing pboy will write a info about how to
          configure the timeout value and nirik will review

<!-- -->

Wednesday, May 03, 2023

:   - ***Essentials at a glance***

      - **Follow up actions**

        1.  Ongoing: pboy will write a info about how to configure the
            timeout value and nirik will review.

      - **Fedora Server goal(s) for F39**

        *AGREED*: WG will pursue \'Fedora Server Edition on SBC\' as
        first priority for F39, and \'Fedora Server Edition in
        virtualized environments\' as 2nd priority.

      - **\"Each Edition has a story for each release\"**

        *AGREED*: WG will pursue \'Fedora Server Edition on SBC\' as the
        \'story\' for F39 with first priority, \'Fedora Server Edition
        in Virtuialized environments\' with 2nd priority.

        *ACTION*: pboy will post a first draft regarding \'Fedora Server
        Edition on SBCs\' on hackmd.io for further discussion.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/fedora-meeting/2023-05-03/fedora-server.2023-05-03-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/fedora-meeting/2023-05-03/fedora-server.2023-05-03-17.00.log.html)

    - ***Actions summary***

      1.  *ACTION*: Ongoing pboy will write a info about how to
          configure the timeout value and nirik will review

      2.  *ACTION*: pboy will post a first draft regarding \'Fedora
          Server Edition on SBCs\' on hackmd.io for further discussion.

<!-- -->

Wednesday, April 19, 2023

:   - ***Essentials at a glance***

      - **Follow up actions**

        1.  Ongoing: pboy will write a info about how to configure the
            timeout value and nirik will review.

      - **\"Each Edition has a story for each release\"**

        On [mailing
        list](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/VILYMWVJ7GVHOSLP3C3YC42S3G7JACM4/)
        we have a first info and a draft collection of ideas. The
        challenge is not so much the \"story\" part, but the \"every
        release\" part.

        *ACTION*: eseyman will try and think up something for next
        meeting

      - **Fedora Server goal(s) for F39**

        *AGREED*: We evaluate 2 options for F39: ServerVM support for
        various hosting services and Usage of SBC as a Server device

    - [Meeting
      summary](https://meetbot.fedoraproject.org/fedora-meeting/2023-04-19/fedora-server.2023-04-19-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/fedora-meeting/2023-04-19/fedora-server.2023-04-19-17.00.log.html)

    - ***Actions summary***

      1.  *ACTION*: Ongoing pboy will write a info about how to
          configure the timeout value and nirik will review

      2.  *ACTION*: eseyman will try and think up something for next
          meeting

<!-- -->

Wednesday, April 05, 2023

:   - ***Essentials at a glance***

      - **Follow up actions**

        1.  Ongoing: pboy will write a info about how to configure the
            timeout value and nirik will review.

      - **F38 Beta testing**

        We are fine with F38 and should not experience any surprises.

      - **Shorter Shutdown Timer**

        *Nirik* created a PR as decided. It is pushed to stable and will
        be included in the installation media.

      - **Fedora Website revamp -- Fedora Server Edition pages**

        AGREED: Server WG would like to get a \"Documentation\"
        button/link between Download and Community in the hero graphic

        AGREED: Server WG is content with the feature list and
        descriptions.

      - **Using Ansible to install and configure Wildfly**

        We will start thinking about how we're going to get these
        ansible roles/playbooks into our users\' hands.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/fedora-meeting/2023-04-05/fedora-server.2023-04-05-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/fedora-meeting/2023-04-05/fedora-server.2023-04-05-17.00.log.html)

    - ***Actions summary***

      1.  Ongoing: pboy will write a info about how to configure the
          timeout value and nirik will review

<!-- -->

Wednesday, March 15, 2023

:   - ***Essentials at a glance***

      - **Follow up actions**

        1.  No open actions

      - **Shorter Shutdown Timer**

        AGREED: to take the same route as CoreOS and keep the old
        default value. (+3, 0, -2 )

        ACTION: pboy will write a info about how to configure the
        timeout value and nirik will review

      - **Fedora Website revamp -- Fedora Server Edition pages**

        We are still missing a documentation button and link. The
        feature list needs some improvement.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/fedora-meeting/2023-03-15/fedora-server.2023-03-15-18.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/fedora-meeting/2023-03-15/fedora-server.2023-03-15-18.00.log.html)

    - ***Actions summary***

      1.  pboy will write a info about how to configure the timeout
          value and nirik will review

<!-- -->

Wednesday, March 01, 2023

:   - ***Essentials at a glance***

      - **Follow up actions**

        1.  Ongoing: nirik to look up the services in our technical
            specification and check for time out value

        2.  Ongoing: pboy to create a ticket to collect our central
            messages for the new web site.

      - **Shorter Shutdown Timer**

        We are still evaluating the possible impact and current
        configuration of the core services.

        We want to add to our documentation how to make changes to the
        .service file if someone has an issue.

        **action** pboy will create a summary of our discussion about
        service specific timeouts.

        **action** pboy will open a mailing list discussion about
        interdependencies between services and the consequences.

      - **Using Ansible to install and configure Wildfly**

        We have still 2 unresolved issues:

            a. TLS between apache and Wildfly web app
            b. Ansiblify Wildfly

        **action** jdubby will update his Ansible/Wildfly repo

        **action** eseyman will look at the updated repo

        **action** pboy will provide a public server where we can work
        in a cooperative work on all the details

      - **Fedora Website revamp -- Fedora Server Edition pages**

        We are generally very content with the current state of the
        [completed
        draft](https://fedora.gitlab.io/websites-apps/fedora-websites/fedora-websites-3.0/server/).
        Mowest informed that the design group considers it \"near
        final\". Anyway we can request changes after the F38 rollout.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/fedora-meeting/2023-02-15/fedora-server.2023-02-15-18.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/fedora-meeting/2023-02-15/fedora-server.2023-02-15-18.00.log.html)

    - ***Actions summary***

      1.  pboy to create a ticket to collect our central messages for
          the new web site

      2.  nirik to look up the services in our technical specification
          and check for time out value

      3.  pboy pboy will create a summary of our discussion about
          service specific timeouts.

      4.  pboy will open a mailing list discussion about
          interdependencies between services and the consequences.

      5.  jdubby will update his Ansible/Wildfly repo

      6.  eseyman will look at the updated repo

      7.  pboy will provide a public server where we can work in a
          cooperative work on all the details

<!-- -->

Wednesday, February 15, 2023

:   - ***Essentials at a glance***

      - **Follow up actions**

        1.  nirik to look up the services in our technical specification
            and check for time out value

        2.  pboy to create a ticket to collect our central messages for
            the new web site.

      - **Fedora Website revamp -- Fedora Server Edition pages**

        Mowest informs about the availability of a [first complete
        draft](https://fedora.gitlab.io/websites-apps/fedora-websites/fedora-websites-3.0/server/),
        although still with some placeholders. The discussion about
        [further
        development](https://gitlab.com/fedora/design/team/wwwfpo-2022/-/issues/23#note_1276926623)
        is still ongoing. The current topic is the design of the header.
        We agree that it should express as well as possible the
        universality and wide scope of Fedora Server Edition (from SBC
        to SME to Data Center).

        Next step is the finetuning of the mission statements.

      - **Shorter Shutdown Timer**

        We are still evaluating the possible impact and current
        configuration of the core services.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/fedora-meeting/2023-02-15/fedora-server.2023-02-15-18.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/fedora-meeting/2023-02-15/fedora-server.2023-02-15-18.00.log.html)

    - ***Actions summary***

      1.  pboy to create a ticket to collect our central messages for
          the new web site

      2.  nirik to look up the services in our technical specification
          and check for time out value

      3.  pboy to create a list of our core services in the issue for
          further discussion

<!-- -->

Wednesday, February 01, 2023

:   - ***Essentials at a glance***

      - **Fedora Website revamp -- Fedora Server Edition pages**

        Mowest made contact with the revamp team. We are now in the flow
        to work on it. See the [current
        mockup](https://fedora.gitlab.io/websites-apps/fedora-websites/fedora-websites-3.0/server/)!
        The texts are a first draft. The graphical assets are mostly
        placeholders.

        You can also follow the [ongoing conversation about the current
        status of the website
        design](https://gitlab.com/fedora/design/team/wwwfpo-2022/-/issues/23).
        To give feedback, please use our [pagure issue
        #66](https://pagure.io/fedora-server/issue/66)!

        Next actions:

        a.  Review text right now and give suggestions for changes.

        b.  Mowest will inform us Emma (the designer) has some of the
            graphic assets ready for review.

        c.  Suggestions or ideas for graphic assets that could be used
            next to each of our \"feature points\" as suggestions to the
            graphics team.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/fedora-meeting/2023-02-01/fedora-server.2023-02-01-18.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/fedora-meeting/2023-02-01/fedora-server.2023-02-01-18.00.log.html)

<!-- -->

Wednesday, January 18, 2023

:   - ***Essentials at a glance***

      - **Shorter Shutdown Timer**

        We will first review the Core Services of our current
        [\"*Technical
        Specification*\"](docs/server-technical-specification.xml) to
        see what configuration is implemented for a shutdown.
        Furthermore, we will consider conducting a test tag on this
        point, although implementation is likely to be difficult.
        Depending on the findings, we will decide on the further
        handling of the magnitude of the default timeout.

        We found contradictions resp. ambiguities about the exact
        configuration of the current timeout configuration in Server.
        Nirik will clarify this.

        *Actions*

        1.  nirik will look up the services in our technical
            specification and check for time out value

      - **Fedora Server web site revamp**

        Mowest made contact with the revamp team and introduced himself
        as Server contact. We are now in the flow to work on it.

        The next step is to collect content for our pages. Mowest asks
        to contribute key ideas, messages, mission statements for the
        content of the page. We prefer professional, meaningful texts,
        not rather content-less marketing phrases, which can be found
        partly on some newly designed pages.

        *Actions*

        1.  pboy to create a ticket to collect our central messages for
            the new web site.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/fedora-meeting/2023-01-18/fedora-server.2023-01-18-18.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/fedora-meeting/2023-01-18/fedora-server.2023-01-18-18.00.log.html)

    - ***Actions summary***

      1.  nirik will look up the services in our technical specification
          and check for time out value

      2.  pboy to create a ticket to collect our central messages for
          the new web site.

**Keep in mind**: We had moved the time of our meeting in UTC so that
the same local time of day is maintained after the DST changeover, that
means currently 18:00 UTC.

# Meeting Minutes {#_meeting_minutes}

Stephen Daley, Peter Boy :page-authors: {author}

Wednesday,December 21, 2022

:   - *Summary info*

      1.  **Follow up actions**

          *INFO*: No outstanding action item.

      2.  **Using Ansible to install and configure Wildfly**

          *ACTION*: jwhimpel will continue to work on Ansible roles .

      3.  **Server WG work program for upcoming year**

          Continued discussion.

          *ACTION*: eseyman take a look at the work program over the
          holidays

          *ACTION*: jwhimpel will continue to work on Ansible roles

          *ACTION*: eseyman wants to focus on Identity Management for
          the first half of 2023

    - [Meeting
      summary](https://meetbot.fedoraproject.org/fedora-meeting/2022-12-21/fedora-server.2022-12-21-18.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/fedora-meeting/2022-12-21/fedora-server.2022-12-21-18.00.log.html)

**Note**: We moved the time of our meeting to UTC so, that the same
local time of day is maintained after the DST changeover, that means
18:00 UTC.

Wednesday,December 07, 2022

:   - *Summary info*

      1.  **Follow up actions**

          *INFO*: No outstanding action items

      2.  **Server critical path definition proposal**

          We will review the current version and likely add items as
          soon as we have made progress in reviewing and updating our
          release and quality criteria - now that the technical
          specifications have been updated.

      3.  **Server WG work program for upcoming year**

          Possible focus areas as currently discussed (should be
          continued on the mailing list):

          - Keeping documentation up to date.

          - Using Ansible to install and configure Wildfly

          - Fedora Website Revamp - Fedora Server part

          - Review installation media

    - [Meeting
      summary](https://meetbot.fedoraproject.org/fedora-meeting/2022-12-07/fedora-server.2022-12-07-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/fedora-meeting/2022-12-07/fedora-server.2022-12-07-17.00.log.html)

**Note**: We are moving the time of our meeting to UTC so that the same
local time of day is maintained after the DST changeover, that means
18:00 UTC.

Wednesday,October 19, 2022

:   - *Summary info*

      1.  **Follow up actions**

          *INFO*: \@eseyman and \@pboy will keep trying hard to
          replicate and check the Wildfly certificate issue.

      2.  **Release 37 Beta testing**

          *info*: Installation issue with GPT and software RAID are
          resolved.

          *info*: Old systemd-nspawn related bugs are basically resolved
          (bugzilla 1900888, 1900869), but not yet completely

          *info*: The new ServerVM works fine.

          *agreed*: Server Edition rc 1.2 is ready for release.

      3.  **Documentation update Release 37**

          *info*: The most important installation articles are reviewed
          and updated.

          *agreed*: For next release we determine the 5 articles mostly
          in need of an review and work on them on a documentation day
          in #fedora-server.

      4.  **Server critical path definition proposal**

          We will continue the mailing list discussion.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/fedora-meeting/2022-10-19/fedora-server.2022-10-19-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/fedora-meeting/2022-10-19/fedora-server.2022-10-19-17.00.log.html)

<!-- -->

Wednesday,October 05, 2022

:   - *Summary info*

      1.  **Follow up actions**

          *INFO*: All our open actions are about the next topics.

      2.  **Release 37 Beta testing**

          *action*: cmurf will test the new ServerVM F37

          SWraid installation on biosBoot GPT has been fixed, needs
          final testing.

      3.  **Documentation update Release 37**

          \@mowest reviewed 2 docs (local install and post
          installation). They are now significantly improved. Reveals
          the relevance of the review process.

      4.  **Using Ansible to install and configure Wildfly**

          There is still an issue with the certificate. eseyman and pboy
          will additionally test it.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/fedora-meeting/2022-10-05/fedora-server.2022-10-05-17.01.html)

    - [Full
      log](https://meetbot.fedoraproject.org/fedora-meeting/2022-10-05/fedora-server.2022-10-05-17.01.log.html)

<!-- -->

Wednesday,September 21, 2022

:   - *Summary info*

      1.  **Follow up actions**

          *INFO*: No outstanding action items

      2.  **Release 37 Beta testing**

          We have assigned various test tasks among us. For details see
          #actions in the minutes below.

      3.  **Documentation update Release 37**

          \@mowest will begin reviewing docs, especially those not
          associated in the release 37 test items.

      4.  **Release criteria, test procedures and systematization of
          tests**

          We agreed to strive for systematization using the test weeks
          tools. Details should first be discussed on the mailing list.

    - [Meeting
      summary](https://meetbot.fedoraproject.org/fedora-meeting/2022-09-21/fedora-server.2022-09-21-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/fedora-meeting/2022-09-21/fedora-server.2022-09-21-17.00.log.html)

<!-- -->

Wednesday,September 07, 2022

:   - *Summary info*

      1.  **Follow up actions**

          *INFO*: No outstanding action items

      2.  **Release 37 Beta testing**

          It is verified the [software raid
          bug](https://bugzilla.redhat.com/show_bug.cgi?id=2088113) is a
          release blocker. Not solved yet, but it is being worked on.

      3.  **Server VM status and the way forward**

          Thanks to *nirik* we have a Server VM x86_64 and s390 image in
          F37 and in Rawhide. It was a kind of last minute rescue after
          a rather [bumpy
          ride](https://pagure.io/fedora-kickstarts/pull-request/905).
          And thanks to *sgallagh* for support in the not so easy way to
          get the kick-start file done at all.

          The kick-start failed on ppc64le and aarch64, unfortunately.
          The cause is likely to be different partitioning requirements,
          but the PR for a customized kick-start file was [hanging
          again](https://pagure.io/fedora-kickstarts/pull-request/915).

          We will need to review the current experience for its impact
          on our plan to update the server distribution media. Under the
          current circumstances, implementation seems quite unrealistic
          or at least extremely costly and time-consuming.

    - [Detailed
      agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/P2NNNFYFKIWCKZOPJ3FGHCEIMSDFI3QO/)

    - [Meeting
      summary](https://meetbot.fedoraproject.org/fedora-meeting/2022-09-07/fedora-server.2022-09-07-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/fedora-meeting/2022-09-07/fedora-server.2022-09-07-17.00.log.html)

<!-- -->

Wednesday, August 17, 2022

:   - *Summary info*

      1.  **Follow up actions**

          *INFO*: No outstanding action items

      2.  **Final decision about an updated Fedora Server Technical
          Specification**

          It was consensus, that the document is not immutable and thus
          change be changed later if ideas for improvements surface
          later. Therefore, a decision now and start with the next
          tasks.

          *AGREED*: WG agrees about the techn.spec. in the current
          version, with alt. 1 for section 1.2 and editorial adaptations
          as discussed today.

      3.  **Using Ansible to install and configure Wildfly**

          This is a key component of our \"Supported by Ansible"-project
          (Server Roles), which has taken a back seat to everyday issues
          for far too long.

          jwhimpel has developed a playbook where currently there is
          still a problem with Letsencrypt certificates to be fixed.

          *ACTION*: jwhimpel will provide access to the playbook on
          GitHub so we can re-play the installation and test it.

    - [Detailed
      agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/2UM3SYJ5BPMUSZJMBTNND5UZCGBSNS3E/)

    - [Meeting
      summary](https://meetbot.fedoraproject.org/fedora-meeting/2022-08-17/fedora-server.2022-08-17-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/fedora-meeting/2022-08-17/fedora-server.2022-08-17-17.00.log.html)

<!-- -->

Wednesday, July 20, 2022

:   - *Summary info*

      1.  **Follow up actions**

          *INFO*: No outstanding action items

      2.  **Review current Fedora Server Technical Specification**

          We agreed about all suggestions in comments with the exception
          of the final wording of section 1.2 (File System and Storage
          Organization). We will open a discussion about the wording of
          section 1.2 on mailing list.

          *ACTION*: pboy will create a next version of the techn. spec.
          containing our agreements today.

    - [Detailed
      agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/2DK7BTZZUOASGMU35TJUSYWDZILV7DRV/)

    - [Meeting
      summary](https://meetbot.fedoraproject.org/fedora-meeting/2022-07-20/fedora-server.2022-07-20-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/fedora-meeting/2022-07-20/fedora-server.2022-07-20-17.00.log.html)

<!-- -->

Wednesday, July 06, 2022

:   - *Summary info*

      1.  **Follow up actions**

          *DONE*: Change proposal to add Server VM is accepted

          *INFO*: Tracking bug
          <https://bugzilla.redhat.com/show_bug.cgi?id=2100621>

          *INFO*: Change Proposal regarding the default hostname
          configuration is accepted by FESCo

          *DONE*: pboy to add test of uefi sw raid
          (<https://pagure.io/fedora-server/issue/89>)

      2.  **Software Raid on UEFI systems**

          *AGREED*: We use the Anaconda solution with raid, for the time
          beeing. Further evaluation on mailing list and next meeting.

      3.  **Review current Fedora Server Technical Specification**

          Discussion to continue next meting

      4.  **Open Floor**

    - [Detailed
      agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/W5ACQXVPR3KOHISJC47LNB53KPJU7ISM/)

    - [Meeting
      summary](https://meetbot.fedoraproject.org/fedora-meeting/2022-07-06/fedora-server.2022-07-06-17.01.html)

    - [Full
      log](https://meetbot.fedoraproject.org/fedora-meeting/2022-07-06/fedora-server.2022-07-06-17.01.log.html)

<!-- -->

Wednesday, June 15, 2022

:   - *Summary info*

      1.  **Follow up actions**

          *ONGOING*: Change proposal to add Server VM is still
          processing ( [discussion
          thread](https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/M2YQMVVUCFCV4MMOQ32UMSM5WBBVE2H7/)
          )

          *INFO*: There is now a Change Proposal regarding the default
          hostname configuration ( [discussion
          thread](https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/Y2TT6VZPGTD5UVGPA6PLNYW2BU4JOC77/)
          )

          *AGREED*: Server WG is content with the default hostname
          change proposal

      2.  **Further processing of GPT as default partitioning switch**

          *ACTION*: pboy to add test of uefi sw raid with LVM RAID
          (instead of standard raid)

          *ACTION*: pboy files a bug about sw raid in uefi mode

          Discussion of unversal boot configuration postponed until
          current problems are solved.

      3.  **Test planning for Fedora 37**

          *AGREED*: Server WG will strive for a test week for F38 and
          follow up releases

          First step is a final review of the updated Technical
          Specification next meeting, followed by an update of our
          release and test criteria.

      4.  **How to proceed with Cockpit File Sharing module NFS part**

          link: <https://pagure.io/fedora-server/issue/86>

          Due to the elapsed time further discussion postponed.

      5.  **Open Floor**

    - [Detailed
      agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/THLAKBXD6YEVGH2NDN4ZOCS3K7TYX3V4/)

    - [Meeting
      summary](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2022-06-15-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2022-06-15-17.00.log.html)

<!-- -->

Wednesday, June 01, 2022

:   - *Summary info*

      1.  **Follow up actions**

          *DONE*: Post on devel list thread F37 proposed change to GPT
          as default partitioning schema about the regression regarding
          software raid installations.
          <https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/DIU6IKPCPD2BXDUFDZUZ2G2ZQNT5JW57/>

          *DONE*: Created an issue containing 2 test cases for biosboot
          GPT software raid installations
          <https://pagure.io/fedora-server/issue/87>

          *DONE*: created a stub of NFS server installation and Cockpit
          for administration

          *ONGOING*: Created Change proposal to add Server VM is still
          processing

          *ONGOING*: Discussion about changes around the default
          hostname configuration

          *ONGOING*: Review of the dnsmasq documentation by eseyman

      2.  **Change proposal about GPT as default partitioning for bios
          boot**

          *LINK*:
          <https://fedoraproject.org/wiki/Changes/GPTforBIOSbyDefault>

          Discussion:
          <https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/VSM473WRHKIIIJYZZCVXAO7XFS4ACHPH/>

          FESCo has accepted the Change Proposal without discussion. We
          now have the problem of preserving our users from harm
          unfortunately done intentionally or, at best, negligently by
          some of our own members who are owners of the Change Proposal.
          Unfortunately, the perpetrators do now not care how harm can
          be averted from our users with Release 37 and do not even
          bother to attend the meeting on this topic to find a suitable
          resolution if the issue.

          Stephen Gallagher started a process to qualify the Anaconda
          software raid bug as a blocker to the GPT Change Proposal. If
          accepted by QA as a blocker, it will have to be fixed (or the
          Change reverted) in order to ship Fedora. This would be a
          perfect and constructive solution.

          *Agreed*: Server WG agrees with sgallagh's suggestion to block
          the GPT change until the Anaconda issue is resolved and
          considers it as most essential.

      3.  **Planning for Fedora 37: Additional changes to discuss?
          (continued)**

          For part of the discussion we have a new tracking issue:
          [#88](https://pagure.io/fedora-server/issue/88) , It
          summarizes all the individual measures that we have discussed
          for improvement and entail an adjustment of the installation
          media.

          Agreed: Issue #88 is postponed to F38

          There are various new bug reports regarding the size of
          installation media, very similar to those on F36. We'll ask
          Adam about it, He resolved those issues for F36.

      4.  **How to proceed with Cockpit File Sharing module NFS part**

          link: <https://pagure.io/fedora-server/issue/86>

          Due to the elapsed time further preparatory discussion via
          e-mail.

      5.  **Open Floor**

    - [Detailed
      agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/RFUVXGX4XFUJQFAN4QC3JNIYKPTL66GS/)

    - [Meeting
      summary](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2022-06-01-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2022-06-01-17.00.log.html)

<!-- -->

Wednesday, May 18, 2022

:   - *Summary info*

      1.  **Follow up actions**

          *INFO*: We voted successfully for 4 new members:
          cooltshirtguy, dcavalca, eseyman, mowest, a very warm welcome.
          Our list of members is already updated.

          *ONGOING*: Created Change proposal to add Server VM is still
          processing in preparation phase

          *ONGOING*: Discussion about changes around the default
          hostname configuration

      2.  **Change proposal about GPT as default partitioning for bios
          boot** *LINK*:
          <https://fedoraproject.org/wiki/Changes/GPTforBIOSbyDefault>

          Discussion:
          <https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/Q2ZBWG3YESG4POYAAZVUKSWMZHG3R7KW/>
          TBD

          *Agreed*: Server WG insists that before switching to GPT as
          default for BIOS boot, it is tested, that Anaconda supports a
          software raid setup smoothly.

      3.  **Planning for Fedora 37: Additional changes to discuss?
          (continued)**

          There is an RFE
          (<https://bugzilla.redhat.com/show_bug.cgi?id=2054625>)
          pending to include some additional packages to the full
          installation DVD, which led to a discussion which packages to
          add and whether we accept a further increase of the downloads.

          Agreed: We combine all installation content related issues and
          actions into one new ticket.

          Action: pboy to create a new ticket about installation media
          content review

      4.  **How to proceed with Cockpit File Sharing module**

          link: <https://pagure.io/fedora-server/issue/86>

          Discussion:
          <https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/T75AU7FLZMDUBMXOD3AXSC4VCYIJ6ZMA/>

          Agreed: We will divide the topic in several steps and start
          with nfs.

          We'll start with completing our documentation with installing
          and maintening a nfs server. Pboy will provide a ToC proposal.

      5.  **Open Floor**

          Eseyman will start to review the dnsmasq documentation article
          with the goal to extend it about setup of an PXE server.
          Mowest is about to document his setup of a WOL configuration.

    - [Detailed
      agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/R3VWDITZ6A23ZJXWJTUFUWJLGGV6K5W2/)

    - [Meeting
      summary](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2022-05-18-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2022-05-18-17.00.log.html)

<!-- -->

Wednesday, May 04, 2022

:   - *Summary info*

      1.  **Follow up actions**

          *ONGOING*: Created Change proposal to add Server VM

          *DONE*: Supplement to our Product requirements Document (PRD)

          *DONE and ONGOING*: Voting about new members (open until
          Thursday,05 05:00 UTC).

          *DONE*: Withdrawal of nb and mhoungbo from member list

      2.  **Evaluation of our test efforts for F36**

          We agreed, we did better than with F35 and want to further
          improve with F37. Will open a follow-up discussion on mailing
          list.

      3.  **Planning for Fedora 37: Additional changes to discuss?**

          There is an RFE
          (<https://bugzilla.redhat.com/show_bug.cgi?id=2054625>)
          pending to include some additional packages to the full
          installation DVD, which led to a discussion which packages to
          add and whether we accept a further increase of the downloads.

          *Agreed*: Continue discussion on mailing list.

      4.  Open Floor

          x3mboy raised the question of migrating our repository to
          gitlab.

          *Agreed*: discuss on mailing list

    - [Detailed
      agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/RQIB4PW64KVMD376224UWLHWICTBL3TW/)

    - [Meeting
      summary](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2022-05-04-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2022-05-04-17.00.log.html)

<!-- -->

Wednesday, April 20, 2022

:   - *Summary info*

      1.  **Follow up actions**

          *DONE*: withdrew Ben Williams from the list of approved
          members as he had wanted. Many thanks for his contributions.

          *DONE*: Opened a discussion about Cockpit and the file-sharing
          update follow ups on mailing list.

          *DONE*: Opened a discussion thread about a specification for a
          Server Edition VM on mailing list.

      2.  **Planning for Fedora 37: Introducing a Server VM KVM virtual
          disk image**

          <https://pagure.io/fedora-server/issue/79>

          *Agreed*: WG decides to add a Fedora Server Edition VM image
          and to make a corresponding Change proposal.

          *Action*: pboy creates a change proposal to add a Fedora
          Server Edition VM image

          *Agreed*: WG decides to amend the PRD as proposed in ticket 83

          *Action*: pboy edits the PRD to amend as in issue #83 and
          initializes the required processing

      3.  **Evaluating Fedora Server Working Group**

          <https://pagure.io/fedora-server/issue/67>

          *Agreed*: WG agrees to open a voting on the admision of
          cooltshirtguy, dcavalca, eseyman and mowest in one go.

          *Action*: pboy start a voting the admision of cooltshirtguy,
          dcavalca, eseyman and mowest in one go.

          *Agreed*: WG agrees to withdraw nb and mhoungbo for the time
          being (#67). Many thanks to both of them for their willingness
          to work on the Server WG.

          *Action*: Withdrawal of nb and mhoungbo from member list.

      4.  **Discussion of a potential change to Fedora surrounding the
          default hostname**

          *Agreed*: salimma and Eighth_Doctor work with Dusty and
          probably others to explore the possibilities to get the old
          behaviour (pre f33) back.

      5.  **Current discussion about withdrawal of BIOS boot for new
          installations in F37**

          There was a longer discussion about the subject. And the
          largely unanimous position was that we still need bios boot
          for a longer time for various reasons. Everything must be done
          to find a technical solution that makes this possible under
          the condition of available resources.

          *Agreed*: Davide Cavalca and Michel Alexandre Salim volunteer
          to work further on the subject.

    - [Detailed
      agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/XZBPD436FYFTKU5L6QVUEN2WBCORICQF/)

    - [Meeting
      summary](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2022-04-20-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2022-04-20-17.00.log.html)

Wednesday, April 06, 2022

:   - *Summary info*

      1.  **Follow up actions**

          *Info*: Had an IRC chat with Ben Williams (jbwillia). He is
          busy with other projects and we agreed he will withdraw from
          server WG. So I will remove him from our list. (see
          [#67](https://pagure.io/fedora-server/issue/67)).

          *Action*: Will withdraw Ben Williams from the list of approved
          members for the time being.

          *DONE*: Withdrew Subhendu Ghosh from the list of approved
          members for the time being. \* *DONE*: pb and sgallagh
          resolved the installation issue with virtualization.

      2.  **Fedora 36 tests**

          *Info*: \<cooltshirtguy\> takes over testing AD from
          \<sgallagh\> for the F36 test cycle

          *Info*: \<eseyman\> still testing OpenLDAP

          *Info*: \<pboy\> No issues found with libcirt / postgreSQL /
          java / Tomcat

          *Agreed*: WG will join the Upgrade test day Thursday,
          April 14. Member will test on their own \"real world\"
          configurations

      3.  **Cockpit file-sharing update Change Proposal follow up**

          *Agreed*: We close issue
          [#73](https://pagure.io/fedora-server/issue/73) as completed
          and done.

          *Info*: \<sgallagh\> has it on his (long) backlog to add the
          Cockpit Application stuff to the file-sharing

          *Agreed*: We open a discussion thread about file-sharing
          update followup actions on mailing list

      4.  **Planning Fedora 37**

          *Info*: There is a hot discussion about withdrawel of bios
          boot for F37.

          We will dedicate a own topic about that next meeting

          Regarding our own plannings:

          - [#53](https://pagure.io/fedora-server/issue/53)
            (\"Facilitated and improved support for Fedora Server
            Edition VMs\", pboy)

            There is a
            [comment](https://pagure.io/fedora-server/issue/79#comment-790978)
            with some specification to add a Fedora Server Edition disk
            image to our deliverables as part of out Fedora 37 work.

            *Agreed*: Open a discussion thread about
            <https://pagure.io/fedora-server/issue/79#comment-790978>
            and decide next meeting

    - [Detailed
      agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/565ZBHTE3TCNLTJYGMQEY7Q4CWQ2KOZ6/)

    - [Meeting
      summary](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2022-04-06-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2022-04-06-17.00.log.html)

Wednesday, March 16, 2022

:   - *Summary info*

      1.  **Follow up actions**

          *Info*: Startet to contact members who had not been with us
          for longer than a half year und didn't contribute anything
          (see [#67](https://pagure.io/fedora-server/issue/67)).

          *Info*: Tried to contact Subhendu Ghosh (sghosh). There is no
          FAS account and no mail address available.

          *Agreed*: We withdraw Subhendu Ghosh from the list of approved
          members for the time being.

      2.  **Fedora 36 tests**

          *Action*: sgallagh and pboy work on #80

          *Action*: \<jwhimpel\> The migration to the \"next
          generation\" of ansible seems to be working fine.

      3.  **Planning Fedora 37**

          *Result*: Special interests exist so far in

          - [#53](https://pagure.io/fedora-server/issue/53)
            (\"Facilitated and improved support for Fedora Server
            Edition VMs\", pboy)

          - [#54](https://pagure.io/fedora-server/issue/54) (\"Include
            automatic notification of updates (dnf-automatic) in Fedora
            Server\", cooltshirtguy)

    - [Detailed
      agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/2MXO25NSLOVKH7O3OU2JB4QRZWPB44AN/)

    - [Meeting
      summary](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2022-03-16-17.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2022-03-16-17.00.log.html)

Wednesday, March 02, 2022

:   Standing meeting about

    - Check F36 changes and known issues - final pass

      *Result*: Composed final list of F36 changes to specifically take
      care of

    - Specifying F36 manual test requirements - final pass

      *Result*: Final composition of a list of task & manual tests to be
      applied to F36 Beta

    - Review current Fedora Server Technical Specification -- second
      pass

      *Result*: First draft proposal adopted as is, continue with
      completion of TBDs

      Details

      - [Meeting
        summary](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2022-03-02-17.08.html)

      - [Detailed
        agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/SVZCL47QI3DINKADPN3OGESW72DAIQRK/)

      - [Full
        log](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2022-03-02-17.08.log.html)

Wednesday, February 16, 2022

:   Standing meeting about

    - Cockpit file-sharing update Change Proposal

    - Specifying F36 manual test requirements

      Details

      - [Meeting
        summary](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2022-02-16-17.00.html)

      - [Detailed
        agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/SVZCL47QI3DINKADPN3OGESW72DAIQRK/)

      - [Full
        log](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2022-02-16-17.00.log.html)

Wednesday, February 02, 2022

:   Standing meeting about

    - Current status of Fedora Server User Docs Update

    - Using Ansible to install and configure Wildfly

    - Review current Fedora Server Technical Specification

      Details

      - [Meeting
        summary](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2022-02-02-17.01.html)

      - [Detailed
        agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/QSGS6B22VQBHZGPL6HJPYXMW7O5O7LWC/)

      - [Full
        log](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2022-02-02-17.01.log.html)

Wednesday, January 19, 2022

:   Standing meeting about

    - Current status of Fedora Server User Docs Update

    - Current changeset F36, possible specific impacts on Server

    - Review current Fedora Server Technical Specification

      Details

      - [Meeting
        summary](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2022-01-19-17.01.html)

      - [Detailed
        agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/W3CVVA2JQFYFX7FI6EJ7YBTOLBZJHVSZ/)

      - [Full
        log](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2022-01-19-17.01.log.html)

# Meeting Minutes from 2020-2021 {#_meeting_minutes_from_2020_2021}

Stephen Daley, Peter Boy :page-authors: {author}

Wednesday, December 15, 2021

:   Standing meeting about

    - Migrating WG Wiki Pages to docs.fedoraproject.org

      Details

      - [Meeting
        summary](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2021-12-01-17.00.html)

      - [Detailed
        agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/KWEP6EL4VEDZK3GO5LAEVXQOUL4DBYUD/)

      - [Full
        log](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2021-12-01-17.00.log.html)

Wednesday, December 1, 2021

:   Standing meeting about

    - Migrating WG Wiki Pages to docs.fedoraproject.org

    - Review current Fedora Server Technical Specification

    - Facilitated and improved support for Fedora Server Edition VMs

      Details

      - [Meeting
        summary](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2021-12-01-17.00.html)

      - [Detailed
        agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/KWEP6EL4VEDZK3GO5LAEVXQOUL4DBYUD/)

      - [Full
        log](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2021-12-01-17.00.log.html)

Wednesday, November 17, 2021

:   Standing meeting about

    - Moving Wiki Pages to docs.fedoraproject.org

    - Preparing Fedora Release 36

    - Facilitated deployment of key services by combining rpm and
      Ansible

      Details

      - [Meeting
        summary](https://meetbot.fedoraproject.org/fedora-meeting/2021-11-17/fedora-server.2021-11-17-17.00.html)

      - [Detailed
        agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/B36Q2AACPSRNS4DF4MQ7BQHCG5LTF7T5/)

      - [Full
        log](https://meetbot.fedoraproject.org/fedora-meeting/2021-11-17/fedora-server.2021-11-17-17.00.log.html)

Wednesday, September 15, 2021

:   Standing meeting about

    - Follow up actions

    - Fedora 35: Max size arm-32 exceeded, install media blocked

    - Facilitated deployment of key services by combining rpm and
      Ansible

      Details

      - [Meeting
        summary](https://meetbot.fedoraproject.org/fedora-meeting/2021-09-15/fedora-server.2021-09-15-17.00.html)

      - [Detailed
        agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/A5FMNBDH5R4ADXGZYVNV7TOGIBDP3FDJ/)

      - [Full
        log](https://meetbot.fedoraproject.org/fedora-meeting/2021-09-15/fedora-server.2021-09-15-17.00.log.html)

Wednesday, September 1, 2021

:   Standing meeting about

    - Follow up actions

    - Fedora 35: Max size arm-32 exceeded, install media blocked

    - Facilitated deployment of key services by combining rpm and
      Ansible

      Details

      - [Meeting
        summary](https://meetbot.fedoraproject.org/fedora-meeting/2021/fedora-meeting.2021-09-01-17.00.html)

      - [Detailed
        agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/6JS7MSAECHVZZZWJU2J5AEISMQBDXLJZ/)

      - [Full
        log](https://meetbot.fedoraproject.org/fedora-meeting/2021/fedora-meeting.2021-09-01-17.00.log.html)

Wednesday, August 18, 2021

:   Standing meeting about

    - Follow up actions

    - Facilitated deployment of key services by combining rpm and
      Ansible

    - Work planning update

      Details

      - [Meeting
        summary](https://meetbot.fedoraproject.org/fedora-meeting/2021-08-18/fedora-server.2021-08-18-17.00.html)

      - [Detailed
        agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/WVRMJ3PVBRR44WLQEK5BNYJ2GU7UYT7R/)

      - [Full
        log](https://meetbot.fedoraproject.org/fedora-meeting/2021-08-18/fedora-server.2021-08-18-17.00.log.html)

Wednesday, August 4, 2021

:   Standing meeting about

    - Follow up actions

    - Facilitated deployment of key services by combining rpm and
      Ansible

      Details

      - [Meeting
        summary](https://meetbot.fedoraproject.org/fedora-meeting/2021-08-04/fedora-server.2021-08-04-17.00.html)

      - [Detailed
        agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/PWJNVPZYMAAQZWJZQKB5TDWE5KYY7ID4/)

      - [Full
        log](https://meetbot.fedoraproject.org/fedora-meeting/2021-08-04/fedora-server.2021-08-04-17.00.log.html)

Wednesday, July 21, 2021

:   Standing meeting about

    - Open ticket 32 about composition of installation media

    - Work on Fedora 35

      Details

      - [Meeting
        summary](https://meetbot.fedoraproject.org/fedora-meeting/2021-07-21/fedora-server.2021-07-21-17.00.html)

      - [Full
        log](https://meetbot.fedoraproject.org/fedora-meeting/2021-07-21/fedora-server.2021-07-21-17.00.log.html)

Wednesday, July 07, 2021

:   Meeting about Ongoing Work Projects

    - Status of ongoing activities (some housekeeping)

    - Fedora Server Documentation

      Details

      - [Meeting
        summary](https://meetbot.fedoraproject.org/fedora-meeting/2021-07-07/fedora-server.2021-07-07-17.00.html)

      - [Full
        log](https://meetbot.fedoraproject.org/fedora-meeting/2021-07-07/fedora-server.2021-07-07-17.00.log.html)

Wednesday, June 23, 2021

:   Meeting about Ongoing Work Projects

    - Fedora Server Product Requirement Document (PRD)

    - Fedora Server Documentation

    - Fedora Website - revamp

      Details

      - [Meeting
        summary](https://meetbot.fedoraproject.org/fedora-meeting/2021-06-23/fedora-server.2021-06-23-16.59.html)

      - [Detailed
        agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/TPYYUQJ6WFU5QSMOLD7Z36NDZAIDBGE6/)

      - [Full
        log](https://meetbot.fedoraproject.org/fedora-meeting/2021-06-23/fedora-server.2021-06-23-16.59.log.html)

Wednesday, June 9, 2021

:   Meeting about Ongoing Work Projects

    - Fedora Server Release 35

    - Deploying services via RPM and Ansible

    - Fedora Server documentation review

      Details

      - [Meeting
        summary](https://meetbot.fedoraproject.org/fedora-meeting/2021-06-09/fedora-server.2021-06-09-17.00.html)

      - [Detailed
        agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/ZE3F2U6J5PRB6RISC67DIWTAE2TFQU35/)

      - [Full
        log](https://meetbot.fedoraproject.org/fedora-meeting/2021-06-09/fedora-server.2021-06-09-17.00.log.html)

Wednesday, June 2, 2021

:   Meeting about Ongoing Work Projects

    - Explore opportunities for cooperation with Cloud WG

    - Deploying services via RPM and Ansible

    - Fedora Server documentation review

      Details

      - [Meeting
        summary](https://meetbot.fedoraproject.org/fedora-meeting/2021-06-02/fedora-server.2021-06-02-17.00.html)

      - [Detailed
        agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/message/WF54CWXOL6HLNJDXL5FUZTWPH46CIC63/)

      - [Full
        log](https://meetbot.fedoraproject.org/fedora-meeting/2021-06-02/fedora-server.2021-06-02-17.00.log.html)

Wednesday, May 26, 2021

:   Meeting about Future Fedora Server Releases

    - Deploying services via RPM and Ansible

      Details

      - [Meeting
        summary](https://meetbot.fedoraproject.org/fedora-meeting/2021-05-26/fedora-server.2021-05-26-17.13.html)

      - [Detailed
        agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/message/LO45JYWU7WJLQ7U3XHSLPQJBT6RNLX4G/)

      - [Full
        log](https://meetbot.fedoraproject.org/fedora-meeting/2021-05-26/fedora-server.2021-05-26-17.13.log.html)

Wednesday, May 19, 2021

:   Meeting about Future Fedora Server Releases

    - Issue release composition

    - Planning for next Fedora release(s)

      Details

      - [Meeting
        summary](https://meetbot.fedoraproject.org/fedora-meeting/2021-05-19/fedora-server.2021-05-19-17.00.html)

      - [Detailed
        agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/IX6ZBBURUUIQNV72LKCUUWZPB4Q4JPA2/)

      - [Full
        log](https://meetbot.fedoraproject.org/fedora-meeting/2021-05-19/fedora-server.2021-05-19-17.00.log.html)

Wednesday, May 12, 2021

:   Meeting about Fedora Server PRD and future Fedora Server Releases

    - PRD - various reviewer questions to discuss

    - Planning for next Fedora release(s)

      Details

      - [Meeting
        summary](https://meetbot.fedoraproject.org/fedora-server/2021-05-12/fedora-server.2021-05-12-17.00.html)

      - [Detailed
        agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/KF2CTZMLFQAJTQIGDQIYQEAVAIYNAHYB/)

      - [Full
        log](https://meetbot.fedoraproject.org/fedora-server/2021-05-12/fedora-server.2021-05-12-17.00.log.html)

Wednesday, May 05, 2021

:   Meeting about Fedora Server Releases

    - Planning for next Fedora release(s)

    - Fedora release criteria and process

      Details

      - [Meeting
        summary](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2021-05-05-17.00.html)

      - [Detailed
        agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/EAUPYMONTWRFIZSR4HPPI2TE5FZXGWDT/)

      - [Full
        log](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2021-05-05-17.00.log.html)

Wednesday, April 28, 2021

:   Meeting about Status PRD Update and Fedora Server Release

    - Status Server PRD (Info)

    - Fedora release criteria and process

    - New Issue: Release composition

      Details

      - [Meeting
        summary](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2021-04-28-17.00.html)

      - [Detailed
        agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/32IQLMZDPUS7JCF2FFRVJO5IAYYQLEL4/)

      - [Full
        log](https://meetbot.fedoraproject.org/fedora-meeting/2021-04-28/fedora-server.2021-04-28-17.00.log.html)

Wednesday, April 21, 2021

:   Meeting about PRD Update and Fedora Server Release

    - PRD Update second pass

    - Fedora release criteria and process

    - Planing for next Fedora release

      Details

      - [Meeting
        summary](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2021-04-21-17.00.html)

      - [Detailed
        agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/OXWV357OY4ZCC4EFNPU3H4HZRRQIHVZS/)

      - [Full
        log](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2021-04-21-17.00.log.html)

Wednesday, April 14, 2021

:   Meeting about Mainly Continuation of the last meeting's agenda

    - PRD update discussion

    - Status F34 release

    - Status new documentation

      Details

      - [Meeting
        summary](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2021-04-14-17.00.html)

      - [Detailed
        agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/J7YI5OSM67O5RKMASL3BWUFMK43OBVCU/)

      - [Full
        log](https://meetbot.fedoraproject.org/fedora-meeting/2021-04-14/fedora-server.2021-04-14-17.00.log.html)

Wednesday, April 07, 2021

:   Meeting about continuation of the last meeting's agenda

    - PRD Update Proposal

    - Collaboration with Cloud WG

      Details

      - [Meeting
        summary](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2021-04-07-17.01.html)

      - [Detailed
        agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/LRI6LNKJZYXTS4SUUOZ7NMSIHUWRKM77/)

      - [Full
        log](https://meetbot.fedoraproject.org/fedora-meeting/2021-04-07/fedora-server.2021-04-07-17.01.log.html)

Wednesday, March 31, 2021

:   Meeting about continuation of the last meeting's agenda

    - PRD Update Proposal

    - New Documentation

      Details

      - [Meeting
        summary](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2021-03-31-17.00.html)

      - [Detailed
        agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/JMZY2TI3W6QMKDPNSZ2SRQN5QDW46A4A/)

      - [Full
        log](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2021-03-31-17.00.log.html)

Wednesday, March 24, 2021

:   Meeting about continuation of the last meeting's agenda

    - Documentation Update

    - PRD Update Proposal

      Details

      - [Meeting
        summary](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2021-03-24-17.00.html)

      - [Full
        log](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2021-03-24-17.00.log.html)

Wednesday, March 17, 2021

:   Meeting about continuation of the last meeting's agenda

    - Work needed for Fedora 34

    - PRD Update Proposal

      Details

      - [Meeting
        summary](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2021-03-17-18.00.html)

      - [Detailed
        agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/G7OMZFSWAYTYV2OP7ZEK3K4WGWAEKWV3/)

      - [Full
        log](https://meetbot.fedoraproject.org/teams/fedora-server/fedora-server.2021-03-17-18.00.log.html)

Wednesday, March 3, 2021

:   Meeting about

    - Status Reboot Server Working Group

    - Introduce Dusty Mabe from Cloud Group

      Details

      - [Meeting
        summary](https://meetbot.fedoraproject.org/fedora-meeting/2021-03-03/fedora-server.2021-03-03-18.04.html)

      - [Detailed
        agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/HKMAODK32EQC3MDGLAAVA4LSXAIN2WCM/)

      - [Full
        log](https://meetbot.fedoraproject.org/fedora-meeting/2021-03-03/fedora-server.2021-03-03-18.04.log.html)

Wednesday, February 17, 2021

:   Meeting about

    - Status Reboot Server Working Group

    - Work program for the coming year

    - PRD Update (first round of discussion)

      Details

      - [Meeting
        summary](https://meetbot.fedoraproject.org/fedora-meeting/2021-02-17/fedora-server.2021-02-17-17.58.html)

      - [Detailed
        agenda](https://lists.fedoraproject.org/archives/list/server@lists.fedoraproject.org/thread/RQWDTIBDAUUK63HYIHLBHGJEMROSELOE/)

      - [Full
        log](https://meetbot.fedoraproject.org/fedora-meeting/2021-02-17/fedora-server.2021-02-17-17.58.log.html)

Wednesday, February 3, 2021

:   Meeting about

    - Housekeeping

    - Wiki Update

      Details

      - [Meeting
        summary](https://meetbot.fedoraproject.org/fedora-meeting/2021-02-03/fedora-server.2021-02-03-18.15.html)

      - [Full
        log](https://meetbot.fedoraproject.org/fedora-meeting/2021-02-03/fedora-server.2021-02-03-18.15.log.html)

Wednesday, January 20, 2021

:   Meeting about

    - Status PRD Update

    - Improving Fedora Server documentation and visibility

    - systemd-oomd

      Details

      - [Meeting
        summary](https://meetbot.fedoraproject.org/fedora-meeting/2021-01-20/fedora_server.2021-01-20-17.02.html)

      - [Full
        log](https://meetbot.fedoraproject.org/fedora-meeting/2021-01-20/fedora-server.2021-01-20-17.02.log.html)

Wednesday, December 16, 2020

:   Fedora Server Reboot Meeting

    - Introduction, Quick Hello, the Agenda

    - Basic Framework for What's Needed

    - Round of Introductions (Who you are, what you're interested in)

    - Existing Fedora Server WG

    - Volunteers to actually be on the Working Group

    - Volunteers for practical action: reviewing and updating the PRD

      Details

      - [Meeting
        summary](https://meetbot.fedoraproject.org/teams/serversig/serversig.2020-12-16-18.00.html)

      - [Full
        log](https://meetbot.fedoraproject.org/teams/serversig/serversig.2020-12-16-18.00.log.html)

# Meeting Minutes from 2013 {#_meeting_minutes_from_2013}

Stephen Daley, Peter Boy

Thursday, December 19, 2013

:   - ***Agenda***

      - **PRD: Use Cases**

    - [Meeting
      minutes](https://lists.fedoraproject.org/pipermail/server/2013-December/000657.html)

    - [Full
      log](https://meetbot.fedoraproject.org/fedora-meeting-1/2013-12-19/fedora-meeting-1.2013-12-19-14.59.log.html)

<!-- -->

Tuesday, December 17, 2013

:   - ***Agenda***

      - **Final Assessment of Personas**

      - **PRD: Delivery Plan**

      - **PRD: Delivery Plan - Delivery Media**

      - **Delivery Plan: Release Cadence**

    - [Meeting
      minutes](http://meetbot.fedoraproject.org/fedora-meeting-1/2013-12-17/fedora-meeting-1.2013-12-17-16.00.html)

    - [Full
      log](https://meetbot.fedoraproject.org/fedora-meeting-1/2013-12-17/fedora-meeting-1.2013-12-17-16.00.log.html)

<!-- -->

Tuesday, December 10, 2013

:   - ***Agenda***

      - **Backup and Monitoring**

      - **what goes in the PRD**

      - **Personas**

    - [Meeting
      minutes](http://meetbot.fedoraproject.org/fedora-meeting-1/2013-12-10/fedora-meeting-1.2013-12-10-15.59.html)

    - [Full
      log](https://meetbot.fedoraproject.org/fedora-meeting-1/2013-12-10/fedora-meeting-1.2013-12-10-15.59.log.html)

<!-- -->

Tuesday, December 3, 2013

:   - ***Agenda***

      - **Adam Williamson Confirmation**

      - **Discuss Role Implementation**

    - [Mailing list
      thread](https://lists.fedoraproject.org/pipermail/server/2013-December/000631.html)

    - [Meeting
      minutes](http://meetbot.fedoraproject.org/fedora-meeting-1/2013-12-03/fedora-meeting-1.2013-12-03-15.59.html)

<!-- -->

Tuesday, November 26, 2013

:   - ***Agenda***

      - **Select a new member of the Working Group**

      - **Personas**

    - [Mailing list
      thread](https://lists.fedoraproject.org/pipermail/server/2013-November/000614.html)

    - [Meeting
      minutes](https://meetbot.fedoraproject.org/fedora-meeting-1/2013-11-26/fedora-meeting-1.2013-11-26-16.00.html)

<!-- -->

Tuesday, November 19, 2013

:   - ***Agenda***

      - **Goals for Server Role Installation**

      - **Personas**

      - **Server Lifecycle Proposal**

      - **Updates and Testing Proposal**

      - **Server Role List Proposal**

      - **Installation Roles vs. Post-installation Role Assignment**

    - [Mailing list
      thread](https://lists.fedoraproject.org/pipermail/server/2013-November/000535.html)

    - [Full
      log](https://meetbot.fedoraproject.org/fedora-meeting-1/2013-11-19/fedora-meeting-1.2013-11-19-16.00.log.html)

<!-- -->

Tuesday, November 12, 2013

:   - ***Agenda***

      - **Can a single server have multiple roles?**

      - **Installation of base + roles**

    - [Mailing list
      thread](https://lists.fedoraproject.org/pipermail/server/2013-November/000514.html)

    - [Full
      log](https://meetbot.fedoraproject.org/fedora-meeting-1/2013-11-12/fedora-meeting-1.2013-11-12-16.02.log.html)

<!-- -->

Tuesday, November 5, 2013

:   - ***Agenda***

      - **Finalizing the Governance Charter: Membership (Group
        representation and terms)**

      - **Is Fedora Server One Product?**

    - [Blog
      summary](https://blog.linuxgrrl.com/2013/11/05/fedora-server-working-group-nov-5-meeting-2/)

    - [Mailing list
      thread](https://lists.fedoraproject.org/pipermail/server/2013-November/000425.html)

    - [Full
      log](https://meetbot.fedoraproject.org/fedora-meeting-1/2013-11-05/fedora-meeting-1.2013-11-05-16.02.log.html)

<!-- -->

Wednesday, October 30, 2013

:   - ***Agenda***

      - **Meeting frequency and times**

      - **Ticket Tracker/Wiki**

      - **Governance Charter**

      - **Open Floor**

    - [Blog
      summary](https://blog.linuxgrrl.com/2013/10/30/fedora-server-working-group-initial-meeting-minutes/)

    - [Mailing list
      thread](https://lists.fedoraproject.org/pipermail/server/2013-October/000313.html)

    - [Full
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

- focuses on the specific features and procedures of the Fedora Server
  Edition

- also includes brief explanations and rationales that convey the
  meaning and underlying concepts

- contains copy-and-paste capable instructions that allow even less
  experienced administrators to operate safely and reliably

- refers to the upstream documentation for general information, where
  available

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

When reading a document, you see a \"bug\" button on the rightmost side
below the blue top bar. Click it and you are forwarded to create an
issue. Members of the Working Group are notified and will take care of
it. However, you must have a Fedora account, so you can log in.

### Write in the Fedora Server Matrix room {#_write_in_the_fedora_server_matrix_room}

Open your Web Browser and visit the [Fedora Server Matrix
room](https://matrix.to/#/#server:fedoraproject.org). You can either use
the Web Interface or switch to the Element App. This is an asynchronous
communication channel. It may take some time for someone to respond.

### Edit a page via a Web Editor {#_edit_a_page_via_a_web_editor}

Besides the aforementioned \"bug\" button there is a button that
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

1.  Install the `git-credential-libsecret` package. It will help git
    store your credentials in GNOME Keyring, KWallet, etc.

    ``` bash
    sudo dnf install git-credential-libsecret
    ```

2.  Add the following information to your `~/.gitconfig` file.

    ``` bash
    [credential]
    helper = libsecret
    ```

3.  Generate an Access Token.

    a.  Click on your profile picture in the upper-right corner of
        Forgejo.

    b.  Click on `Settings` in the menu underneath your profile photo.

    c.  Click on `Applications` in the menu on the left side of the
        screen.

    d.  Give the token a name, set it to All (public, private, and
        limited), and then select your permissions. ...​You will at
        **LEAST** need `repository read and write` access.

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
It's best to use a form like \"current version\" - \"proposed version\".
Suggestions will then be included in the text, or perhaps there will be
follow-up questions.

## Quality assurance {#_quality_assurance}

Prior to publication, each article should be reviewed. Such articles are
available in our [staging
area](https://docs.stg.fedoraproject.org/en-US/fedora-server/) and
marked as \"awaiting review\" or similar.

Reviewer should:

- check for technical and content accuracy. Contact the author in case
  of questions.

- check spelling and syntax

- refine the wording and phrases, especially in the case of non-English
  speaking authors

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

- Include of author(s), date of creation, last update, and the Fedora
  version used to test the examples.

- Start with a short summary of the subject matter, objective and
  desired outcome. (one paragraph of 2-3 sentences)

- Divide longer sequences into sections with subheadings and short
  explanations.

- Provide each step with a brief explanation/justification, if possible,
  a general instruction structure and a concrete example.

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
modules/ROOT → pages → installation → interactive-local.adoc. The file
name does resemble the article title in a abbreviated form.

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

The Fedora Server Edition working group and Pagure follow the \"Pull
Request Workflow\". According to this, no one is supposed to change a
published page immediately, but the workflow creates a copy of the page
under your name (the \"fork\") and when you are done, the community is
informed about your proposal (the pull request, or PR for short). The
community can discuss the proposal and after agreement the administrator
can \"pull in\" the proposal. The process is also known as \"merge
request\" (MR).

The pagure Web Editor takes care of all the details \"behind the
scenes\". You don't need to worry about it. Just proceed to edit the
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

It has 2 permanent versions: The \"main\" for the published content and
\"stg\" for planning, development, and discussion. Temporarily,
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

- filesharing-nfs-administration.adoc

- filesharing-nfs-installation.adoc

- filesharing-samba-administration.adoc

- filesharing-samba-installation.adoc

The titles should follow this pattern as far as possible and avoid
redundant parts such as \"How to install ...​\"

- File sharing with NFS - Installation

- File sharing with NFS - Administration

- File sharing using Samba - Installation

- File sharing using Samba - Administration

All file names are in lower case.

## Preparations {#_preparations}

1.  **Create a local subdirectory** where the files of the documentation
    should be stored, and make it your default. We use
    fedora-server-docs in your home directory throughout this guide

    \[...\]\$ mkdir \~/fedora-server-docs \[...\]\$ cd
    \~/fedora-server-docs

2.  Still in your default working directory, **clone fedora-server**
    repository

    \[...\]\$ git clone <https://git@pagure.io/fedora-server.git> -o
    upstream

    Git will copy the complete server repo including all branches,
    specifically \"main\" and \"stg\" mentioned above, into a local repo
    on your local workstation (into *.git/* located in your default
    directory).

    Git does \"tag\" the cloned repo as remote repo \"**upstream**\".

    At the same time it checks out the default branch \"\'\'main\'\'\"
    into your \'\'working directory\'\' (i.e. \~/fedora-server-docs in
    the above example). Therefore, when the operation terminates, you
    will find in your current default directory, which is now your
    \'\'working directory\'\', some files, e.g. README.md,
    docsbuilder.sh and preview.sh and a directory docs. The latter
    contains the content.

    If you leave off \"./\" at the end, git creates another directory in
    your default directory with the name of the repository, i.e.
    fedora-server. And this directory is then the \"*working
    directory*\" to the repository. This can be useful if you want to
    keep track of different fedora docs projects in one directory.

3.  In your browser go to <https://pagure.io/fedora-server/>, log in and
    **create a Fork**. Once you have done it, the button will read *View
    fork*. Switch to your fork and click on Clone and you will see 2
    addresses you can use to clone (copy) the content to your local
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
    versions of the server repository by \"pulling\" the content from
    \"upstream\" and upload your modifications and additions by
    \"pushing\" it to origin, i.e. to your fork. You will than create a
    \"pull request\", i.e. pick up your modifications and additions from
    your fork and integrate it into the generic repository (\"origin\").
    This enables co-writers to review our work and comment on it.

5.  In your working directory build the local version and start the
    preview tool.

    \[...\]\$ ./docsbuilder.sh

6.  Back in your browser enter the **local preview address**\':
    *localhost:8080*

    - You should see a local preview of the current Server documentation

## Working on content {#_working_on_content}

1.  Check if you are on the branch you intend to work on

    \[...\]\$ git branch main \* stg

2.  If not, switch to the branch you want to use.

    \[...\]\$ git checkout \[stg\|main\]

    Git will adjust and modify the content of your working directory
    accordingly!

3.  Before your begin to work update your working directory

    \[...\]\$ git commit -m \"\<YOUR COMMIT MESSAGE\>\"

4.  Modify content

5.  Update preview and check:

    \[...\]\$ ./docsbuilder.sh

    Preview in your browser using the address *\'localhost:8080*

6.  Repeat step 4 & 5 as required.

## Save Your Work {#_save_your_work}

Commit your work locally and then push it into your fork \"*origin*\".

1.  Check status

    \[...\]\$ git status

2.  Add files to commit stage as appropriate

    \[...\]\$ git add \<FILENAME\>

3.  Commit locally

    \[...\]\$ git commit -m \"\<YOUR COMMIT MESSAGE\>\"

4.  Transfer your fork of fedora server to the repository

    \[...\]\$ git push origin \[main\|stg\]

5.  In your browser open <https://pagure.io/fedora-server>, login,
    switch to your fork and create a pull request. = A Git cheat sheet
    For Server Documentation Authors Peter Boy (pboy)

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

1.  **Create a local subdirectory** where the files of the documentation
    should be stored, and make it to your default. We use
    *fedora-server-docs* in your home throughout this guide

        […]$ mkdir ~/fedora-server-docs
        […]$ cd    ~/fedora-server-docs

2.  **Clone the Server documentation sources** into your default working
    directory

        […]$ git clone https://forge.fedoraproject.org/server/user-documentation.git ./
        Cloning into '.'...
        remote: Enumerating objects: 2500, done.
        remote: Counting objects: 100% (510/510), done.
        remote: Compressing objects: 100% (325/325), done.
        remote: Total 2500 (delta 391), reused 171 (delta 171), pack-reused 1990 (from 1)
        Receiving objects: 100% (2500/2500), 19.03 MiB | 2.46 MiB/s, done.
        Resolving deltas: 100% (1357/1357), done.

    The \"./\" causes the repository to be created in the current
    directory. So your future working directory is
    \"\~/fedora-server-docs\" If omitted, Git creates a subdirectory in
    the current directory with the name of the repository and copies it
    there. The working directory would then be
    \"\~/fedora-server-docs/user-documentation\". This would be useful,
    if you also want to clone our wg-documentation.

3.  **Check the result**

        […]$ git status
        On branch main
        Your branch is up to date with 'origin/main'.

        nothing to commit, working tree clean

    Git does \"tag\" or name the cloned repo as clone of the remote repo
    \"**origin**\". It is the default for any action you perform with
    the cxentral remote repository. You can check further details.

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

2.  In the upper right corner you see a button \"**Fork**\". It opens a
    form to set the properties of your fork. Accept the default values
    unchanged, with the exception of the optional Description field.
    Select the button \"Fork Repository\" to create the fork.

3.  The fork becomes the active window. Right around the center, you see
    a blue button \"**HTTPS**\" besides the address of your forck and a
    button to copy the URL.

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

1.  **List the branches** in the remote central repository

        […]$ git branch -a
        * main
        remotes/origin/HEAD -> origin/main
        remotes/origin/main
        remotes/origin/nfs-upd
        remotes/origin/nfs_typo
        remotes/origin/stg

    The command lists your local branches and the branches on the remote
    central repository.

2.  **Create a corresponding local branch** of the branch you want to
    work with, eg. nfs-upd in the above example

        […]$ git checkout nfs-upd
        branch 'nfs-upd' set up to track 'origin/nfs-upd'.
        Switched to a new branch 'nfs-upd'

3.  **Check the result**

        […]$ git branch
        main
        * nfs-upd

        […]$ git status
        On branch nfs-upd
        Your branch is up to date with 'origin/nfs-upd'.

        nothing to commit, working tree clean

    You may also get some more information about your locally available
    branches:

        […]$ git branch -v
        main    1fa76ff modules/ROOT/pages/index.adoc aktualisiert
        * nfs-upd db0c02c fixed some typos in nfs filesharing docs and brought versions in line for FC43

### Create a new branch locally {#_create_a_new_branch_locally}

1.  Ensure, that the source, usually main, is your currently active
    branch

        […]$ git status
        * main
        stg
        {sometext}-upd

2.  Otherwise switch to main.

        […]$ git switch main

3.  Update your local workspace

        […]$ git pull [origin]

    The parameter is optional. The cloned repository's main branch is
    usually the default.

4.  Create a new branch und switch to it at the same time

        […]$ git checkout -b <NEW_BRANCH_NAME>

    Alternatively you can also use

        […]$ git switch -c <NEW_BRANCH_NAME>

### Delete a Branch no longer needed completely locally and remotely {#_delete_a_branch_no_longer_needed_completely_locally_and_remotely}

1.  Delete the remote branch

        […]$ git push -d <REMOTE_NAME> <BRANCH_NAME>

2.  Delete the local branch

        […]$ git branch -D <BRANCH_NAME>

## Working on content {#_working_on_content_2}

1.  Check if you are on the branch you intend to work on

        […]$ git branch
        * main
        stg
        {sometext}-upd

2.  If not, switch to the branch you want to use.

        […]$ git checkout [main|{sometext}-upd]

    Git will adjust and modify the content of your working directory
    accordingly!

3.  Before your begin to work update your working directory

        […]$ git

4.  Modify content

5.  Update preview and check:

        […]$ ./docsbuilder.sh

    Preview in your browser using the address *\'localhost:8080*

6.  Repeat step 4 & 5 as required.

## Save Your Work {#_save_your_work_2}

### Commit your work locally {#_commit_your_work_locally}

While working on content all modifications happen in the volotile
working directory. Every change takes effect immediately; everything is
in flux. To permanently save a status, the working area is saved in the
local git repository (in the \".git\" subdirectory). In Git, this is
known as a *commit.*

1.  Check status

    \[...\]\$ git status

2.  Add files to commit stage as appropriate

    \[...\]\$ git add \<FILENAME\>

3.  Commit locally

    \[...\]\$ git commit -m \"\<YOUR COMMIT MESSAGE\>\"

### Forgot a file in the last commit {#_forgot_a_file_in_the_last_commit}

Add a file to the last commit without modifying the commit log message

1.  Add the file (or several files) to the staging area

        […]$ […]$ git add <FILENAME>

2.  Add it to the last commit

        […]$ git commit  --amend  --no-edit

You can also add a files and replace the commit log message

1.  Add the file (or several files) to the staging area

        […]$ git add <FILENAME>

2.  Add it to the last commit

        […]$ git commit --amend -m "an updated commit message"

### Save your work in the central remote repository {#_save_your_work_in_the_central_remote_repository}

### Transfer your work into the central remote repository {#_transfer_your_work_into_the_central_remote_repository}

Only members of Server WG can do this.

    […]$ git push origin [main|]

### Save your work in your fork {#_save_your_work_in_your_fork}

    […]$ git push {YOUR_FORK_NAME} [main|{sometext}-upd]

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

        […]$ git merge --no-commit --no-ff <YourBranch>

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

**Not recommended**

Sometimes you may need an article located in onother branch in youre
current work branch. An easy way is just to copy it. But be aware, this
way you don't get related files, e.g. images, in one go! You have to
check for file dependencies and copy one by one.

First check, if you are in the intended branch and then copy the file
from another branch

    […]$ git status
    […]$ git checkout <other-branch-name> <file-or-dir>

as an example

    […]$ git status
    On branch main
    Your branch is up to date with 'origin/main'.

    […]$ git checkout gui-upd modules/ROOT/pages/usecase-gui-addon.adoc

### „Cherry-pick" a commit from another branch into your current branch {#_cherry_pick_a_commit_from_another_branch_into_your_current_branch}

**The recommended alternative to copy**

\'Cherry-picking\' picks up a commit that was made in another branch and
applies that very same commit to your current branch. As with the copy
command about it copies files from one branch into another, but not just
one file, but all files that were processed in this commit. With regard
to documents, the text file of the document and all associated files
such as images, etc. will be transferred in one go.

1.  Check if you are on the branch you intend to work on

        […]$ git branch
        * main
        stg
        {sometext}-upd
        {othertext}-new

2.  If not, switch to the branch you want to use.

        […]$ git switch {sometext}-upd

3.  Skip through the log and finde the commit you want to cherry-pick

        […]$ git log
        commit bdb3a418f523167b422099b742bcf6d61068770f (HEAD -> main, origin/main, origin/HEAD)
        Author: Peter Boy <pb@boy-digital.de>
        Date:   Sat Nov 8 10:43:12 2025 +0100

        Amended sections.

        commit afe5fecff99300edb77b841eacd021bf6186edd4
        Author: Peter Boy <pb@boy-digital.de>
        Date:   Fri Nov 7 13:09:24 2025 +0100

        Initial commit of a Git Cheat Sheet for authors.

        commit 29668a512ad66595a550aec08a1171e42f219d11
        Author: Peter Boy <pb@boy-digital.de>
        Date:   Thu Nov 6 15:40:09 2025 +0100

        Updated minutes 2025-11-05 meeting.

        commit ac3d25fd1f6f7be2d05fe3d8d22d570ec77a5b35
        Author: Peter Boy <pb@boy-digital.de>
        Date:   Mon Nov 3 10:27:02 2025 +0100

        Updated minutes

    Copy the commit hash to the clipboard

4.  Cherry-pick the commit

        […]$ git cherry-pick [-x]  <commit-hash>

    If you want to cherry-pick the minutes of the 2025-11-05 meeting of
    the above example, it would be

        […]$ git cherry-pick -x  29668a512ad66595a550aec08a1171e42f219d11

    The abbreviated hash (the first 7 digits instead of 40), that you
    see in the overview in the web interface of the remote repository,
    too, is also sufficient. You may specify multiple commit hashes to
    cherry-pick multiple commits in one go.

    The parameter \"-x\" is optional. It enables you to provide a
    standard commit message, so it might easier in the future to see,
    what you did and why.

### „Cherry-pick" a commit from a forked repo into your current branch {#_cherry_pick_a_commit_from_a_forked_repo_into_your_current_branch}

1.  Find the URL of the other fork or repo. In the Fedora forge Web
    interface click on the number right of the \"Fork\" button. You get
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

- [\"Product Requirements Document\" (initial version
  2014)](archive/product-requirements-document-2014.xml)

- [\"Product Requirements Document\" (renwed version
  2021)](archive/product-requirements-document-2021.xml)

- [\"Fedora Server Technical Specification\" (initial version
  2014)](archive/server-technical-specification-2014.xml)

## Server related documents {#_server_related_documents}

## Research {#_research}

## Proposals {#_proposals}

## Working group work plannings {#_working_group_work_plannings}

- WG work project [Buildup of a renewed documentation on Fedora Server
  specific topics](archive/initial-docs-plan.xml) planning
