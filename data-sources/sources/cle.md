This document explains how the CLE team works.

We break down work requests that the team responds to into two
categories, which we believe benefits both the CLE team and the
communities we serve as they allow the team to operate efficiently and
allow us to plan our work.

- Initiatives handled by dedicated project teams

  - Initiatives are projects that require multiple team members to
    complete over multiple weeks/months, in depth scoping and timelines

  - The process for submitting a new initiative is described in the [New
    Initiative workflow](initiatives.xml) document.

- Work requests handled by the Infra & Releng Team

  - This team responds to \'lights on work\' and requests that come in
    on an ad hoc & regular basis such as:

    - BAU infra/releng requests

    - Bug fixes

Some general best practices when working with us are: \* Do not ping a
single person

\+ By doing this you reduce the number of people having access to your
request drastically, meaning, if that person is busy with something
else, your request may take much longer to be processed.

- If it is not in a ticket, it did not happen

  We need to have everything in tickets. This helps us share knowledge
  within the team, efficiently track our workload, and identify
  recurring issues which may be indicative of an underlying problem we
  need to fix in a more systemic manner.

  Even if you have discussed something on IRC, or in a corridor with
  someone in the team, you want to log the discussion and its outcome in
  a ticket so we can get back to it later when we need to investigate
  why this change was made.

- When you cannot open a ticket

  There are a few cases where it is acceptable to send an email or to
  reach directly to people, for example if you cannot access or
  authenticate to the ticket tracking system :)

  In this case, you do not want to send your email or ping a single
  person (cf the first point above).

  - In Fedora, you can use the email `admin` @ fedoraproject.org

  - In CentOS, you can contact the sysadmins on the `#centos-devel`
    channel on `irc.libera.chat`

Both projects have their own, additional, processes for their day to day
work, which you can find in:

- [Day to day for Fedora](day_to_day_fedora.xml)

- [Day to day for CentOS](day_to_day_centos.xml) = Working with
  Community Linux Engineering in Fedora

CLE members work in Fedora as community members, just like everyone
else. We're part of
[Infrastructure](https://docs.fedoraproject.org/en-US/infra/),
[Design](https://docs.fedoraproject.org/en-US/design/), [Release
Engineering](https://docs.fedoraproject.org/en-US/infra/release_guide/),
[Documentation](https://docs.fedoraproject.org/en-US/fedora-docs/),
[Quality](https://docs.fedoraproject.org/en-US/qa-docs/), the
[Council](https://docs.fedoraproject.org/en-US/council/), and more!
:experimental: = Working with Community Linux Engineering in CentOS

This document explains how to efficiently work with the CLE team. Your
close attention to this document will help both you and us do the work
you are asking us to do.

# Our Workflow {#_our_workflow}

1.  Is your issue/problem related to security of an application or
    service we run?

    - send an email to `security` \@centos.org

2.  Is your issue CentOS CI Infra or CentOS Infra related?

    - Follow next step

3.  File a ticket in
    [https://pagure.io/centos-infra/issues](https://pagure.io/centos-infra/issues/)
    with as much information as you think will be needed to handle your
    issue. This initial ticket will be made in the *Needs review* state.
    Make sure to note if there is a deadline or if this issue blocks
    you.

    - Your ticket will be reviewed within 48 hours at most; usually
      sooner.

    - There is no need to ping team members or notify us about the newly
      filed ticket.

    - Select correct issue template for [Project migration to new
      OpenShift
      Cluster](https://pagure.io/centos-infra/new_issue?template=ci-migration)
      or [new project on-boarding to CentOS
      CI](https://pagure.io/centos-infra/new_issue?template=ci-onboarding)

4.  Is your issue/problem urgent? (credentials exposed, CI Infra down,
    Duffy Pool exhausted etc) or is your issue/problem such that you
    cannot file a ticket (authentication, no account, ticketing system
    down)

    - On IRC (irc.libera.chat) join the `#centos-devel` and state the
      issue there.

    - If no answer, follow the next step

5.  Your ticket will be triaged by a team member and moved to a new
    state:

    - If it's moved to *Waiting on asignee* it's waiting for a team
      member to start working on it.

    - If it's moved to *Waiting on reporter* it means that you need to
      answer questions posed in the ticket before it can be worked on.

    - If the ticket is otherwise closed, it will be with a explanation
      from a team member.

6.  If you have an update to your issue/task or want to know when it
    might be worked on:

    - comment in the ticket adding that information or asking for time
      frame.

7.  When someone is available, your ticket will be assigned to someone
    to work on.

    - Watch for progress reports/ticket being marked done.

8.  If the work is not fully completed as required, please re-open the
    ticket and indicate this.

    - Go back to the previous step for additional work.

# General Ticket Considerations {#_general_ticket_considerations}

Please provide as much information as you can in your ticket to avoid
back and forth for information.

Make sure your ticket:

- Explains the problem or issue you are having, with URLs where possible
  to the services or applications involved.

- Tells us how important or urgent this is to you.

- Includes any error messages or output you see.

It is your responsibility as ticket reporter to follow your ticket,
provide information that is asked for, and keep us aware of any urgency
you may have. Do not simply file and forget your ticket.

Your ticket may take a while to process, depending on the current
workload of the team has and how important we think it is. If your
ticket is blocking you, make sure you note that in the ticket, but keep
in mind that we may already be working on tickets that are blocking more
people.

# IRC {#_irc}

IRC is a great way to communicate, but please do not ping team members
directly. Instead, update your ticket with any new information you have
and when the team member(s) working on that issue have
time/availability, they may contact you on IRC for more interactive
debugging/testing.

# Direct emails {#_direct_emails}

E-mail is also a great communication method, but if you mail work items
or information to one person directly, they cannot easily hand off the
issue, you must wait for them to have time to address the issue (when
others could perhaps have already solved it, etc). So, please avoid
direct emails and instead update tickets with any information you want
to add. :experimental: :toc: = New Initiative Workflow

This document documents a proposed workflow to get new initiatives onto
the CLE backlog.

# The Process {#_the_process}

The process to submit a new initiative to the CLE team to be potentially
worked on is outlined below:

- Propose a new initiative by opening a ticket at
  <https://pagure.io/cpe/initiatives-proposal/new_issue> - the proposal
  should give the "what" and "why" of the work requestedd.

- The product owner will review your ticket, comment and potentially
  schedule some time with the requestor(s) to go over the proposal to
  refine the details. We are looking to establish why this initiative is
  important to do,what benefits it will bring to the community, the
  technical details as the requestor sees them and their estimated 'need
  by' date.

- Once we have established these requirements, the product owner reviews
  the request with the technical leads of the team to scope the effort
  the initiative will require from the team to complete. These details
  include skill sets needed, hardware, storage, automation, dependant
  services that could be impacted by changes made & how long they think
  this would take to complete.

- This information is then reshared with the requestor to verify and
  sign off on and then reviewed by the CLE review team to be accepted or
  rejected to our backlog.

- If rejected, the requestor is notified by the product owner.

- If accepted, the proposal is added to our backlog queue and will be
  refined until it is sufficiently scoped to be included in the list of
  initiatives to be proposed at the quarterly planning.

- Projects that are moved from the backlog queue to the consideration
  queue and are not chosen for that quarter may still be progressed in
  the next quarter(s), or depending on project sizes and timelines, may
  be picked up by the team on free cycles if they choose to work on
  this.

- The team leads, team management team and all the stakeholders review
  all the proposals for the quarterly planning session during which they
  prioritize a number of initiatives for the coming quarter.

- The management team forms the different project teams who will be
  working on the different initiatives during the quarter.

- As the quarter progresses, the product owner will reach out to the
  requestor(s) to sync with them on the progress of the initiatives.

<figure id="img-initiative-flow">
<img src="CLE_new_initiatives_flow.png" alt="The initiative flow" />
<figcaption>Initiatives flow</figcaption>
</figure>

## Proposing a New Initiative {#_proposing_a_new_initiative}

To propose a new initiative, open a new ticket at
<https://pagure.io/cpe/initiatives-proposal/new_issue> and fill in the
template provided.

That template is basically the *what* and *why* of your request and some
other information such as:

- *What* do you want the team to work on?

- *Why* do you think it is worth doing?

- Potential dependencies for this initiative (dependencies on people,
  skillset, other work/initiatives, etc...​).

- Potential deadlines that could impact the initiative.

- Your definition of success

  - The minimum required for this initiative to be considered a success
    and the nice-to-have or really-nice-to-have you would like to
    see/have.

- Area and community concerned/impacted

## First Decision Point: Is This Initiative for the CLE Team? {#_first_decision_point_is_this_initiative_for_the_cle_team}

Based on the information provided in the ticket, the CLE team will
consider whether the initiative is in scope of the [Mission
Statement](index.xml), and if there is a clear benefit for the
communities the CLE team is involved in. If your initiative does not fit
in the scope of our mission statement, it does not mean your challenge
is not worth pursuing - but that the CLE team has limited resources and
needs to be careful on how they are spent. There may be occasions where
an initiative outside of our scope is accepted. Should this happen, it
will be at our team and management's discretion.

The CLE team meets regularly to go over the proposed initiatives. At
this point, it will be decided if your initiative is accepted, or not,
and if necessary, appoint someone to work with you on refining this
proposal.

# Final Notes {#_final_notes}

This new workflow is a change from how the CLE team has worked until
now. The core idea is to maximize the output of the team to the
community. We are not able to accept everything and anything, and we
want to make sure that what we do accept is properly limited in scope
and time. Hopefully this will allow us to work on more initiatives and
bring more beneficial changes to our communities. :experimental: :toc: =
Time Tables

This document aims at recording the different deadlines that the CLE
team tries to aim for its planning.

:::: note
::: title
:::

Please be aware that all initiatives briefed in will be reviewed by our
review team which includes: CLE members (manager, project owner,
technical leads and agile practitioner), Fedora Representative, CentOS
Representative, who will make a decision to accept this work, or decline
due to unavailability of time/people, etc. All accepted initiatives will
be added to our
[backlog](https://tree.taiga.io/project/amoloney1-cpe-team-projects/kanban?epic=null)
::::

# Current {#_current}

- 2020

  - Q4: October to December

    - Q4 deadline for proposal submission: September 9th

    - Q4 planning session: September 18th

    - Q4 starting date: October 5th

- 2021

  - Q1: January to March

    - Q1 deadline for proposal submission: November 27th

    - Q1 planning session: December 10th - To be confirmed

    - Q1 starting date: January 4th 2021

  - Q2: April to June

    - Q2 deadline for proposal submission: March 12th

    - Q2 planning session: March 25th

    - Q2 starting date: April 5th

  - Q3: July to September

    - Q3 deadline for proposal submission: June 10th

    - Q3 planning session: June 24th

    - Q3 starting date: July 5th

  - Q4: October to December

    - Q4 deadline for proposal submission: September 9th

    - Q4 planning session: September 23rd

    - Q4 starting date: October 4th

:::: important
::: title
:::

The closer to the proposal submission deadline we get the less time
proposals will have to be properly scoped which may result in the
proposal not being considered or picked for the next quarter. The more
time a proposal has, the more time it gives us to understand and scope
it.
::::

# Past {#_past}

- 2020

  - Q1: January to March

  - Q2: April to June

    - Q2 deadline for proposal submission: March 9th

    - Q2 planning session: March 18th

  - Q3: July to September

    - Q3 deadline for proposal submission: June 9th

    - Q3 planning session: June 18th

    - Q3 starting date: July 5th :experimental: = Glossary

This document explains some of the terminology used by the team.

# Pain vs Gain {#_pain_vs_gain}

When evaluating tickets during the stand ups, the team evaluates the
pain vs gain of the task asked. These estimates can then be used to
prioritize work ( low pain, high gain would be the first one considered
and high pain, low gain the last).

Here is an idea of what each level corresponds to:

Low trouble

:   easyfix that we know how to do, is documented and doesn't take more
    than a day.

Medium trouble

:   something that is (or sounds) doable, requires a little
    investigation work but should not take too long (done in a week
    max).

High trouble

:   something that we have never done before and will require more
    investigation work and impact analysis before we can get started on
    it or something we know but will take more than a week to do
    properly.

:::: note
::: title
:::

Trouble labels are being converted to story points in [CLE JIRA
project](https://issues.redhat.com/projects/CPE/issues). Story points
are representing the complexity of the issue and being used for deciding
the capacity of the team. The labels are being converted to story points
based on following table:

+-----------------+-----------------+-----------------+-----------------+
|                 | Low trouble     | Medium trouble  | High trouble    |
+-----------------+-----------------+-----------------+-----------------+
| Story points    | 1               | 5               | 10              |
+-----------------+-----------------+-----------------+-----------------+
::::

Low gain

:   we have done without fine until now, it impacts very few people and
    has a work around available.

Medium gain

:   there is a work around available but it impacts quite a number of
    people.

High gain

:   is a supported use-case, impacts a lot of people, there is no work
    around available.

# Dev vs Ops {#_dev_vs_ops}

When evaluating tickets during the stand ups, the team also evalutes if
the ticket requires a developper to be involved or not. The result of
this evaluation is captured by the `dev` or `ops` tags that are set to
the ticket. They also allow to add the ticket to the respective boards
which the team uses to coordinate work.

dev

:   requires development work (a script/ansible to be written) or
    non-straight forward debugging work.

ops

:   it related to configuring an app or running an existing script to
    change a behaviour or requires a little debugging to figure what is
    going on before it can be assessed as requiring a code fix or a
    config fix.

# Priorities {#_priorities}

We are actually mis-using the priority field to reflect the status of
the ticket.

Needs Review

:   This is the default status set on the ticket when it is opened.
    These tickets are meant to be reviewed during the stand up.

🔥 URGENT 🔥

:   World is on fire, if we have set the ticket to that status, you can
    assume we're working on it and you can subscribe to the ticket to
    get updates, please do not ping us so we can focus on it.

Next Meeting

:   This marks tickets that needs to be discussed within the team during
    our weekly team meeting on irc.libera.chat.

Waiting on Assignee

:   This marks tickets that have been triaged and are either waiting on
    someone to pick them up or waiting on the assignee to work/finish
    them.

Waiting on Reporter

:   This marks tickets in which a question was asked to the reporter
    whose answer is needed to progress the ticket.

Waiting on External

:   This marks tickets that are blocked waiting on something or someone
    outside of the team.

# Application categories {#_application_categories}

The Fedora Infrastructure runs a fairly larged number of applications.
CLE runs most of them and maintain (as in maintain the code base,
writing code and patches) quite a few of them. However, not all
applications will get the same level of attention from CLE. So they have
been categorized into two maintenance status and two maintenance level.

Each appliction can then be categorized using these, for example:

- bodhi is: CLE run and maintain - Critical path

- koji is: CLE run and don't maintain (type a) - Critical path

- waiverdb is: CLE run and don't maintain (type b) - Critical path

- simple-koji-ci is: CLE run and don't maintain (type b) - Not critical
  path

## Maintenance status {#_maintenance_status}

CLE run and maintain

:   these are the applications that we run and for which the team is
    responsible for the code base. We lead the project upstream and run
    it in the infrastructure. If something break, we will look at it and
    if that requires patching we will do it.

CLE run and don't maintain

:   these are applications that are running in the infrastructure but
    for which we do not write the code base. There are two types of
    applications in this sections:

    - a\) applications that for which we look after the deployment

    - b\) applications for which other people look after the deployment,
      in which case our work can be described as providing \"power and
      pings\", in other words, providing power and network. If something
      goes wrong, we will try to restart the service and if the service
      doesn't recove, we will contact the maintainers of the
      application.

## Maintenance level {#_maintenance_level}

Critical path

:   these are applications that are needed to build or ship one of our
    deliverables to our users.

Not critical path

:   these are applications that while important for the community will
    not impact the production or delivery of the project's artifacts.
    :experimental: :toc: = Service Level Expectations

The CLE team does not have any formal agreement or contract regarding
the availability of its different services. However, we do try our best
to keep services running, and as a result, you can have some
expectations as to what we will do to this extent.

# Primary Business Hours {#_primary_business_hours}

Fedora Infrastructure's primary business hours are aligned with the work
schedule of Red Hat Inc. Normal hours should be seen as during Monday
through Friday 1400 UTC to 2300 UTC with US national holidays and a 2
week end of year closure affecting staffing and response times.

Services outside of primary business hours are done on call and depend
on the availability of staff.

# Roles and Responsibilities {#_roles_and_responsibilities}

## Fedora Infrastructure to Community {#_fedora_infrastructure_to_community}

- To have staff present and available in appropriate IRC channels to
  answer questions during primary hours.

- To have particular staff on-call during off hours so that community
  members can contact for Critical and Important services.

- Interact with community members with respect and courtesy.

- Work with community members to get accurate and thorough documentation
  of incidents, problems, or feature requests.

- Resolve reported problems as soon as acknowledged if possible.

- Clearly communicate estimated resolution times.

- Move items which can not be resolved within a reasonable time to
  future feature requests or close out.

## Community Members to Fedora Infrastructure {#_community_members_to_fedora_infrastructure}

- Provide full and detailed reports of the problem or requested service.

- Provide clear and complete contact information and times when
  available.

- Interact with CLE members with respect and courtesy.

- Leave alternative contacts who can also be available in case of
  vacation or other emergencies.

- When contacted by Fedora IT, respond back within 5 business days.

## Fedora Infrastructure to Fedora Infrastructure {#_fedora_infrastructure_to_fedora_infrastructure}

- Have a clear schedule of reachable hours.

- Set and take regular vacation time to be rested.

- Rotate through days on-call in IRC and tickets.

- If adding a new service, be available outside of normal business hours
  to help debug problems.

- Follow procedures and checklists when adding or updating services.

- Help with regular audits of the documentation

# Definition of Service Priorities {#_definition_of_service_priorities}

The general design of service priorities is that of concentric circles,
where items rely on services in their own circle or a circle below them.

1.  **Critical** services are ones which Fedora Infrastructure will work
    on 24x7 with a 52 week coverage if an unplanned outage occurs.
    Services will be configured to be highly available with an estimated
    planned/unplanned uptime of 95%. Response time should be within 1
    hour.

2.  **Important** services are ones which Fedora Infrastructure will
    work to be available 24x7 with a 50 week coverage. Response times
    during primary hours should be 1 hour, and outside of it should be 4
    hours.

3.  **Normal** services are ones which Fedora Infrastructure will work
    to be available during primary work hours. Problems outside of these
    hours will be looked at as people are available. The services may be
    available outside of these but are of a lower priority than
    important services.

4.  **Low priority** services are ones which are not critical or
    important for the primary function of Fedora Infrastructure. They
    will be worked on and looked at during primary business hours.
    Response times should be within 1 business day.

5.  **Third Party** services are ones which Fedora Infrastructure has
    outsourced tools and services to. Uptimes, service hours, and
    coverage are dictated by the third party. Depending on the type of
    problem, Fedora Infrastructure will act as an intermediary, or in
    the case of tools like retrace and COPR, direct the user to talk
    with the service owners.

6.  **Deprecated** services are ones which Fedora Infrastructure are no
    longer putting resources into. This may be because the project has
    completed its mission, the upstream software is dead, or the
    original reasons for the product are available. Problems with these
    services will be looked at during primary business hours. Responses
    may be mostly \"Will Not Fix\".

# Limitations on Support {#_limitations_on_support}

- Some services that are associated with Fedora are provided by third
  parties. Changes and outages which affect them are outside the control
  of Fedora Infrastructure.

- Fedora Infrastructure will prioritize issues and requests that affect
  multiple people or teams over a smaller group or individual.

- Fedora Infrastructure has limited budget and hours. Requests and
  features will be prioritized to fit within those.

- Fedora Infrastructure is bound by the laws and regulations of the
  United States of America. This means that certain requests, changes
  and problems are outside the ability of members to deal with.

# Glossary {#_glossary}

- **Planned outage**: A planned outage is one that is announced
  sufficiently ahead of time to allow most users to plan around it.

- **Unplanned outage**: An outage that occurs suddenly without proper
  allowance for users to plan around it.

- **Scheduled outage**: An outage which has been scheduled to occur, but
  may not have been announced with enough time for users to plan around
  it.

- **High Availability**: Systems are available during specified
  operating hours with any unplanned outages \'masked\' by other tools.

- **Continuous Operations**: Systems are available 24 hours a day, 7
  days a week, with no scheduled outages. Unplanned outages are possible
  during this time.

- **Continuous Availability**: Systems or applications are available
  24x7 with no planned or unplanned outages. This is a combination of
  high availability and continuous operations.

- **Level of availability**:

+-----------------------------------+-----------------------------------+
| Percentage                        | Max outage time per day           |
+===================================+===================================+
| 90%                               | 144.0 minutes                     |
+-----------------------------------+-----------------------------------+
| 95%                               | 72.0 minutes                      |
+-----------------------------------+-----------------------------------+
| 99%                               | 14.4 minutes                      |
+-----------------------------------+-----------------------------------+
| 99.9%                             | 1.4 minutes                       |
+-----------------------------------+-----------------------------------+

- **Committed Hours of Availability**: Hours that an organization will
  have staff available to help deal with issues with systems, services,
  and applications. Also known as \"Regular Business Hours\"

- **Outage Hours**: Total number of hours of outage considered normal
  for calculating achieved availability.

- **Response Time**: The time between the users notification of the
  problem and when the help desk will begin to work on that problem.

- **Resolution Update**: The frequency of updates to tickets

# Estimated Time of Resolution: {#_estimated_time_of_resolution}

By priority Levels:

- **Emergency**: Problems which are site wide, and affect the core
  functions of the project.

- **Urgent**: Problems which affect multiple functions and groups in the
  project.

- **Normal**: Problems which affect a single user from performing needed
  duties.

- **Low**: A request for service, instruction, information that has no
  immediate impact on services. :experimental: :toc: = Services SLE

Here is the list of our services per SLE level. For memory these levels
are presented in our [SLE Documentation](sle.xml).

:::: warning
::: title
:::

This document is still a **work in progress**. The services listed there
are at their appropriate level for Fedora but not all of them are under
the responsabilities of the CLE team which is currently not represented
here.
::::

# Critical {#_critical}

- DNS

- Bastion ssh

- Authentication/authorization (FAS)
  <https://admin.fedoraproject.org/accounts/>

- Authentication/authorization (Ipsilon) <https://id.fedoraproject.org>

- Configuration Management (ansible)

- Source control (git)

- Backups

- DHCP/PXE

- IPA

# Important {#_important}

- Koji <https://koji.fedoraproject.org>

- Bodhi <https://bodhi.fedoraproject.org>

- Downloads <https://dl.fedoraproject.org/>

- Fedora Souce code <https://src.fedoraproject.org/>

- MirrorManager <https://admin.fedoraproject.org/mirrormanager>

- Nagios <https://nagios.fedoraproject.org>

- HAProxy <https://admin.fedoraproject.org/haproxy/proxy01>

- Postgres databases

- Mysql databases

- Product Definition Center <https://pdc.fedoraproject.org/>

- Greenwave

- Fedmsg

- DataGrepper <https://apps.fedoraproject.org/datagrepper/>

- Email gateway bastion.fedoraproject.org

- Autosign

- Composer

- Buildhosts

- Docker registry

- Memcached

- Logging

- Basset

- PDC

- resultsdb

- certgetter

- mbs

- odcs

# Normal {#_normal}

- Pagure <https://pagure.io>

- CI <https://ci.centos.org>

- The Mailing Lists <https://lists.fedoraproject.org>

- Wiki <https://fedoraproject.org/wiki/Fedora_Project_Wiki>

- Documentation

- Notifications <https://apps.fedoraproject.org/notifications>

- Kerneltest <https://apps.fedoraproject.org/kerneltest>

- Fedora InfraCloud <https://fedorainfracloud.org>

- FMN

- FAF

- Beaker

- Freshmaker

- Data Analysis

# Low {#_low}

- Ambassadors
  <https://fedoraproject.org/membership-map/ambassadors.html>

- Asknot <http://whatcanidoforfedora.org/>

- Badges <https://badges.fedoraproject.org/>

- Blocker Bugs <https://qa.fedoraproject.org/blockerbugs/>

- Easyfix <https://fedoraproject.org/easyfix/>

- Elections <https://apps.fedoraproject.org/#Elections>

- FedoCal <https://apps.fedoraproject.org/#FedoCal>

- Fedora Magazine <https://fedoramagazine.org/>

- Fedora People <https://fedorapeople.org/>

- GeoIP <https://geoip.fedoraproject.org/>

- github2fedmsg <https://apps.fedoraproject.org/github2fedmsg>

- Mdapi <https://apps.fedoraproject.org/mdapi/>

- Meetbot <https://apps.fedoraproject.org/#Meetbot>

- Nuancier <https://apps.fedoraproject.org/#Nuancier>

- Paste <https://paste.fedoraproject.org>

- Release Monitoring (anitya) <https://release-monitoring.org/>

- Review Status <https://fedoraproject.org/PackageReviewStatus/>

- The Planet <https://fedoraplanet.org/>

- Unbound

- Autocloud

- Bugyou

- Gobby

- Keys

- Koschei

- Loopabull

- Hotness

- OpenShift

- statscache

- Packages <https://admin.fedoraproject.org/pkgdb/packages/>

- bugzilla2fedmsg

- fed-image

- zanata2fedmsg

- secondary

- freemedia

- pager_server

- bz_review

- websites

# Websites {#_websites}

- fedora-web

- fedora-budget

- fedora-docs

- developer

- whatcanidoforfedora

- membership-map

- zanata

- review-stats

- fedora_owner_change

# Third Party {#_third_party}

Outside of Fedora Infrastructure to fix.

- Network connectivity to PHX2/RDU2

- FreeNode IRC <https://freenode.net>

- Libera Chat IRC <https://libera.chat/>

- Ask Fedora <https://ask.fedoraproject.org/>

- COPR <https://copr.fedorainfracloud.org/>

- Retrace <https://retrace.fedoraproject.org>

- Bugzilla <https://bugzilla.redhat.com/>

- Status <https://status.fedoraproject.org>

- Taskotron <https://taskotron.fedoraproject.org/>

- Openqa

- Taiga <https://teams.fedoraproject.org/>

# Deprecated {#_deprecated}

- Torrents <https://torrent.fedoraproject.org>

- Darkserver <https://darkserver.fedoraproject.org/>

- PkgDB <https://admin.fedoraproject.org/pkgdb/>

- Jenkins <https://jenkins.fedorainfracloud.org/>

- summershum

- Tagger <https://apps.fedoraproject.org/tagger/>

- Taiga <https://taiga.fedorainfracloud.org/> :experimental:

# Processes {#_processes}

This section will contain all processes defined in CLE Team.
:experimental:

# Process for unmaintained apps {#_process_for_unmaintained_apps}

This document describes the process of handling apps CLE team doesn't
maintain anymore. The reason why CLE is not maintaining some apps is
simple. We want to focus on the problems that are directly related to
our [Mission Statement](index.xml) and don't maintain large amount of
applications that are not related to it. Because of this we want to
shrink the amount of applications we own, but don't have capacity to
maintain.

## Step by step process {#_step_by_step_process}

1.  **Make it visible that the application is looking for maintainer**

    Add following to the top of README for the application:

    *This application is currently looking for new maintainer.*

    Sent e-mail that the application is looking for maintainer to
    <infrastructure@fedoraproject.org> and <devel@fedoraproject.org>:

    *Hi everyone,*

    *these applications are currently looking for a new maintainer:*

    *\* \<application 1\>*

    *\* \<application 2\>*

    *If you are interested in taking any of these applications* *feel
    free to reach us on #cpe-redhat on <https://libera.chat>.*

    *The application will be orphaned and removed from* *production
    environment if there is no maintainer for 6 months.*

    *Regards,*

    *CLE Team*

2.  **Stop the service on staging**

    Stop the application in staging first (if there is staging
    instance). See if this will broke any other service. If the broken
    service is CLE owned application remove any ties to the application
    that is unmaintained (this will probably be a mini-initiative).

    If the broken application is not CLE owned, let the maintainers of
    the affected application known about this and warn them that the
    unmaintained app will be removed in 6 months if there is no new
    maintainer.

3.  **Wait for 6 months for response**

    If there is a new maintainer found during this period. Hand over the
    application to new maintainer together with all knowledge we have
    about the application. Remove the application from the process.

    Resend the e-mail from the first step each month.

4.  **Stop the service on production**

    Stop the application on production. At this time all the ties to any
    other CLE owned application should be removed.

5.  **Announce the application was orphaned**

    Sent e-mail that the application is no longer available to
    <infrastructure@fedoraproject.org> and <devel@fedoraproject.org>:

    *Hi everyone,*

    *these applications were removed from production environment* *and
    are no longer accessible because they were without* *maintainer for
    more than 6 months:*

    *\* \<application 1\>*

    *\* \<application 2\>*

    *If you are interested in taking any of these applications* *feel
    free to reach us on #cpe-redhat on <https://libera.chat>.*

    *Regards,*

    *CLE Team*

    If new maintainer is found after this announcement. Hand over the
    application to new maintainer together with all knowledge we have
    about the application.
